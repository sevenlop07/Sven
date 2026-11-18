#!/usr/bin/env python3
"""
blender_roblox_kit.py — Reusable Procedural Roblox Cast, Face-Swap, Lip-Sync & LookDev Kit for Blender 5.3.
Eliminates dependence on external .obj character rigs when building 3D Roblox shorts in Headless Blender 5.3.
Includes temp_render_to() to work around Windows OpenImageIO write blocks on protected directories.
"""
import json
import math
import os
import shutil
import tempfile
import bpy
import bmesh
from mathutils import Vector, Euler, Matrix

STUD = 0.28
TEX_W, TEX_H = 585.0, 559.0
CORE_SKILL_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CORE_ASSETS_DIR = os.path.join(CORE_SKILL_DIR, "assets")
CORE_ANIMS_DIR = os.path.join(CORE_ASSETS_DIR, "anims")
CORE_CLOTHES_DIR = os.path.join(CORE_ASSETS_DIR, "clothes")
CORE_FACES_CARTOON_DIR = os.path.join(CORE_ASSETS_DIR, "faces_cartoon")
CORE_FACES_RUBBERHOSE_DIR = os.path.join(CORE_ASSETS_DIR, "faces_rubberhose")
CORE_FACES_UGC_DIR = CORE_FACES_CARTOON_DIR
CORE_FACES_HD_DIR = CORE_FACES_RUBBERHOSE_DIR
CORE_PROPS_DIR = os.path.join(CORE_ASSETS_DIR, "props")
CORE_SETS_DIR = os.path.join(CORE_ASSETS_DIR, "sets")
CORE_ANIMALS_DIR = os.path.join(CORE_ASSETS_DIR, "animals")
CORE_NATURE_DIR = os.path.join(CORE_ASSETS_DIR, "nature")
CORE_HAIRS_DIR = os.path.join(CORE_ASSETS_DIR, "hairs")


def get_core_asset(*parts) -> str:
    """Resolve a path inside roblox-director/assets/ (independent of output/)."""
    return os.path.join(CORE_ASSETS_DIR, *parts)


def load_core_glb(name_or_path: str, col=None, location_m=(0.0, 0.0, 0.0), yaw_deg: float = 0.0, scale: float = 1.0):
    """Import a ground-aligned Roblox Creator Store .glb prop/set/animal/nature/hair from Core assets/."""
    target = name_or_path
    if not os.path.exists(target):
        for folder in (CORE_PROPS_DIR, CORE_SETS_DIR, CORE_ANIMALS_DIR, CORE_NATURE_DIR, CORE_HAIRS_DIR, CORE_ASSETS_DIR):
            for cand in (name_or_path, f"{name_or_path}.glb"):
                p = os.path.join(folder, cand)
                if os.path.exists(p):
                    target = p
                    break
            if os.path.exists(target):
                break
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=target)
    imported = [o for o in bpy.data.objects if o not in before]
    roots = [o for o in imported if o.parent is None]
    if len(roots) == 1:
        obj = roots[0]
    elif len(roots) > 1:
        root_name = os.path.splitext(os.path.basename(target))[0]
        obj = bpy.data.objects.new(root_name, None)
        bpy.context.scene.collection.objects.link(obj)
        for r in roots:
            r.parent = obj
        imported.append(obj)
    else:
        meshes = [o for o in imported if o.type == "MESH"]
        obj = meshes[0] if meshes else imported[0]
    if col is not None:
        for o in imported:
            for c in list(o.users_collection):
                c.objects.unlink(o)
            col.objects.link(o)
    obj.location = Vector(location_m)
    obj.rotation_euler = Euler((0.0, 0.0, math.radians(yaw_deg)))
    if scale != 1.0:
        obj.scale = (scale, scale, scale)
    return obj


def attach_core_hair(char_info: dict, hair_name_or_glb: str, hair_hex: str = None):
    """Attach a pre-extracted Roblox Studio hair .glb from Core assets/hairs/ cleanly onto an R15 Head bone."""
    target = hair_name_or_glb
    if not os.path.exists(target):
        for cand in (hair_name_or_glb, f"{hair_name_or_glb}.glb"):
            p = os.path.join(CORE_HAIRS_DIR, cand)
            if os.path.exists(p):
                target = p
                break
    arm = char_info["armature"]
    col = char_info["collection"]
    m = char_info["metrics"]
    hs = m["hs"]
    hx, hy, hz = m["head_center"]

    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=target)
    imp = [o for o in bpy.data.objects if o not in before and o.type == "MESH"]
    obj = imp[0]
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)

    obj.parent = arm
    obj.matrix_parent_inverse = Matrix.Identity(4)
    obj.scale = (hs, hs, hs)
    obj.location = Vector((hx, hy, hz)) * STUD
    obj.rotation_euler = Euler((0.0, 0.0, 0.0))
    if hair_hex:
        mat = make_stylized_hair_mat(f"{arm.name}_StudioHair", hex_to_linear_rgba(hair_hex), roughness=0.46)
        obj.data.materials.clear()
        obj.data.materials.append(mat)
    vg = obj.vertex_groups.get("Head") or obj.vertex_groups.new(name="Head")
    vg.add(list(range(len(obj.data.vertices))), 1.0, "REPLACE")
    mod = obj.modifiers.new("Armature", "ARMATURE")
    mod.object = arm
    return obj

TORSO_UV = {
    "front": (231, 74, 128, 128), "back": (427, 74, 128, 128),
    "right": (165, 74, 64, 128),  "left": (361, 74, 64, 128),
    "top":   (231, 8, 128, 64),   "bottom": (231, 204, 128, 64),
}
RLIMB_UV = {
    "left":  (19, 355, 64, 128),  "back": (85, 355, 64, 128),
    "right": (151, 355, 64, 128), "front": (217, 355, 64, 128),
    "top":   (217, 289, 64, 64),  "bottom": (217, 485, 64, 64),
}
LLIMB_UV = {
    "front": (308, 355, 64, 128), "left": (374, 355, 64, 128),
    "back":  (440, 355, 64, 128), "right": (506, 355, 64, 128),
    "top":   (308, 289, 64, 64),  "bottom": (308, 485, 64, 64),
}


def hex_to_linear_rgba(hex_str: str):
    """Convert #RRGGBB sRGB hex to Blender linear RGBA."""
    h = hex_str.lstrip("#")
    vals = [int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in vals]
    return (lin[0], lin[1], lin[2], 1.0)


def px_to_uv(x, y, w, h, pad=1.5):
    return (x + pad) / TEX_W, 1.0 - (y + h - pad) / TEX_H, (x + w - pad) / TEX_W, 1.0 - (y + pad) / TEX_H


def get_stage_dir(slug: str = "default") -> str:
    """Return a %TEMP% staging directory safe from Windows OpenImageIO write blocks."""
    d = os.path.join(tempfile.gettempdir(), f"sven_blender_{slug}")
    os.makedirs(d, exist_ok=True)
    return d


def temp_render_to(final_path: str):
    """Render via %TEMP% and attempt copy to final_path; falls back cleanly to %TEMP% if blocked."""
    tmp_dir = os.path.join(tempfile.gettempdir(), "sven_blender_stage")
    os.makedirs(tmp_dir, exist_ok=True)
    tmp_file = os.path.join(tmp_dir, os.path.basename(final_path))
    bpy.context.scene.render.filepath = tmp_file
    bpy.ops.render.render(write_still=True)
    try:
        os.makedirs(os.path.dirname(os.path.abspath(final_path)), exist_ok=True)
        shutil.copy2(tmp_file, final_path)
        return final_path
    except OSError:
        return tmp_file


def temp_save_blend(final_blend_path: str):
    tmp_dir = os.path.join(tempfile.gettempdir(), "sven_blender_stage")
    os.makedirs(tmp_dir, exist_ok=True)
    tmp_file = os.path.join(tmp_dir, os.path.basename(final_blend_path))
    bpy.ops.wm.save_as_mainfile(filepath=tmp_file)
    try:
        os.makedirs(os.path.dirname(os.path.abspath(final_blend_path)), exist_ok=True)
        shutil.copy2(tmp_file, final_blend_path)
        return final_blend_path
    except OSError:
        return tmp_file


def make_solid_mat(name, linear_rgba, roughness=0.45):
    mat = bpy.data.materials.new(name=name)
    bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = linear_rgba
    bsdf.inputs["Roughness"].default_value = roughness
    return mat


def make_skin_cloth_mat(name, skin_rgba, cloth_img_path):
    mat = bpy.data.materials.new(name=name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 0.52
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.inputs[6].default_value = skin_rgba
    tex = nt.nodes.new("ShaderNodeTexImage")
    img = bpy.data.images.load(cloth_img_path, check_existing=True)
    img.colorspace_settings.name = "sRGB"
    tex.image = img
    tex.extension = "CLIP"
    nt.links.new(tex.outputs["Alpha"], mix.inputs[0])
    nt.links.new(tex.outputs["Color"], mix.inputs[7])
    nt.links.new(mix.outputs[2], bsdf.inputs["Base Color"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_head_face_mat(name, skin_rgba, face_png_path):
    mat = bpy.data.materials.new(name=name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 0.42
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.inputs[6].default_value = skin_rgba
    tex = nt.nodes.new("ShaderNodeTexImage")
    img = bpy.data.images.load(face_png_path, check_existing=True)
    img.colorspace_settings.name = "sRGB"
    tex.image = img
    tex.extension = "CLIP"
    nt.links.new(tex.outputs["Alpha"], mix.inputs[0])
    nt.links.new(tex.outputs["Color"], mix.inputs[7])
    nt.links.new(mix.outputs[2], bsdf.inputs["Base Color"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat, tex


def make_stylized_hair_mat(name, base_rgba, roughness=0.58):
    """Stylized Roblox UGC hair shader with root-to-tip shading & directional strand grooves."""
    mat = bpy.data.materials.new(name=name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = roughness
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = 0.28

    tc = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(tc.outputs["UV"], sep.inputs["Vector"])

    # Anisotropic strand grain stretched heavily along ribbon V (length) vs U (width)
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Scale"].default_value = (26.0, 2.5, 8.0)
    nt.links.new(tc.outputs["UV"], mp.inputs["Vector"])
    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 3.2
    noise.inputs["Detail"].default_value = 4.0
    nt.links.new(mp.outputs["Vector"], noise.inputs["Vector"])

    # Root-to-tip & mid-band highlight variation
    dark_col = (base_rgba[0] * 0.56, base_rgba[1] * 0.56, base_rgba[2] * 0.58, 1.0)
    hi_col = (min(1.0, base_rgba[0] * 1.24 + 0.03), min(1.0, base_rgba[1] * 1.22 + 0.03), min(1.0, base_rgba[2] * 1.20 + 0.03), 1.0)

    mix_s = nt.nodes.new("ShaderNodeMix")
    mix_s.data_type = "RGBA"
    mix_s.inputs[6].default_value = dark_col
    mix_s.inputs[7].default_value = hi_col
    nt.links.new(noise.outputs["Fac"], mix_s.inputs[0])

    mix_base = nt.nodes.new("ShaderNodeMix")
    mix_base.data_type = "RGBA"
    mix_base.inputs[0].default_value = 0.42
    mix_base.inputs[6].default_value = base_rgba
    nt.links.new(mix_s.outputs[2], mix_base.inputs[7])

    # Subtle bump along strand grooves so lights catch individual lock ridges
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.14
    bump.inputs["Distance"].default_value = 0.008
    nt.links.new(noise.outputs["Fac"], bump.inputs["Height"])

    nt.links.new(mix_base.outputs[2], bsdf.inputs["Base Color"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def _face_dir(normal: Vector) -> str:
    ax, ay, az = abs(normal.x), abs(normal.y), abs(normal.z)
    if ay >= ax and ay >= az:
        return "front" if normal.y < 0 else "back"
    if ax >= ay and ax >= az:
        return "left" if normal.x > 0 else "right"
    return "top" if normal.z > 0 else "bottom"


def _create_uv_box(name, size_studs, center_studs, uv_table, mat, collection, v_range=(0.0, 1.0), bevel_m=0.011):
    sx, sy, sz = [s * STUD for s in size_studs]
    cx, cy, cz = [c * STUD for c in center_studs]
    vb, vt = v_range
    mesh = bpy.data.meshes.new(name + "_Mesh")
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x *= sx; v.co.y *= sy; v.co.z *= sz
    uv_layer = bm.loops.layers.uv.new("UVMap")
    for f in bm.faces:
        side = _face_dir(f.normal)
        u0, v0, u1, v1 = px_to_uv(*uv_table[side])
        for loop in f.loops:
            co = loop.vert.co
            if side == "front":   u_t, v_t = (co.x / sx) + 0.5, vb + ((co.z / sz) + 0.5) * (vt - vb)
            elif side == "back":  u_t, v_t = (-co.x / sx) + 0.5, vb + ((co.z / sz) + 0.5) * (vt - vb)
            elif side == "left":  u_t, v_t = (co.y / sy) + 0.5, vb + ((co.z / sz) + 0.5) * (vt - vb)
            elif side == "right": u_t, v_t = (-co.y / sy) + 0.5, vb + ((co.z / sz) + 0.5) * (vt - vb)
            elif side == "top":   u_t, v_t = (co.x / sx) + 0.5, (co.y / sy) + 0.5
            else:                 u_t, v_t = (co.x / sx) + 0.5, (-co.y / sy) + 0.5
            loop[uv_layer].uv = (u0 + u_t * (u1 - u0), v0 + v_t * (v1 - v0))
    bm.to_mesh(mesh); bm.free()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = (cx, cy, cz)
    obj.data.materials.append(mat)
    collection.objects.link(obj)
    bev = obj.modifiers.new("Bevel", "BEVEL")
    bev.width = bevel_m; bev.segments = 2; bev.limit_method = "NONE"
    for p in obj.data.polygons: p.use_smooth = True
    return obj


def _create_roblox_head(name, center_studs, scale_h, mat_head, collection):
    cx, cy, cz = [c * STUD for c in center_studs]
    r = 0.60 * scale_h * STUD
    half_h = 0.58 * scale_h * STUD
    fillet = r * 0.36
    profile = [(0.0, -half_h)]
    for i in range(1, 7):
        ang = -math.pi * 0.5 + (math.pi * 0.5) * (i / 6)
        profile.append(((r - fillet) + fillet * math.cos(ang), -(half_h - fillet) + fillet * math.sin(ang)))
    for k in range(1, 5):
        profile.append((r, -(half_h - fillet) + 2.0 * (half_h - fillet) * (k / 5.0)))
    for i in range(0, 6):
        ang = (math.pi * 0.5) * (i / 6)
        profile.append(((r - fillet) + fillet * math.cos(ang), (half_h - fillet) + fillet * math.sin(ang)))
    profile.append((0.0, half_h))

    n_seg = 40
    mesh = bpy.data.meshes.new(name + "_Mesh")
    bm = bmesh.new()
    uv_layer = bm.loops.layers.uv.new("UVMap")
    bot_pole = bm.verts.new((0.0, 0.0, profile[0][1]))
    rings = [[bm.verts.new((rr * math.cos(2 * math.pi * s / n_seg), rr * math.sin(2 * math.pi * s / n_seg), zz))
              for s in range(n_seg)] for rr, zz in profile[1:-1]]
    top_pole = bm.verts.new((0.0, 0.0, profile[-1][1]))
    for s in range(n_seg):
        sn = (s + 1) % n_seg
        bm.faces.new((bot_pole, rings[0][sn], rings[0][s]))
        bm.faces.new((rings[-1][s], rings[-1][sn], top_pole))
    for ri in range(len(rings) - 1):
        for s in range(n_seg):
            sn = (s + 1) % n_seg
            bm.faces.new((rings[ri][s], rings[ri][sn], rings[ri + 1][sn], rings[ri + 1][s]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    arc_half = math.radians(35.0)
    face_h = 0.74 * scale_h * STUD
    for f in bm.faces:
        f.smooth = True
        is_front = f.normal.y < -0.25
        for loop in f.loops:
            co = loop.vert.co
            if not is_front:
                loop[uv_layer].uv = (-1.0, -1.0)
            else:
                ang = math.atan2(co.x, max(1e-5, -co.y))
                loop[uv_layer].uv = (0.5 + ang / (2.0 * arc_half), 0.5 + (co.z + 0.04 * STUD) / face_h)
    bm.to_mesh(mesh); bm.free()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = (cx, cy, cz)
    obj.data.materials.append(mat_head)
    collection.objects.link(obj)
    return obj


def _catmull_eval(pts, widths, thicks, num_steps=14):
    n = len(pts)
    if n < 2:
        return [Vector(pts[0])], [(widths[0], thicks[0])]
    vpts = [Vector(p) for p in pts]
    ext_p = [vpts[0] + (vpts[0] - vpts[1])] + vpts + [vpts[-1] + (vpts[-1] - vpts[-2])]
    vals = list(zip(widths, thicks))
    ext_v = [vals[0]] + vals + [vals[-1]]
    out_p, out_v = [], []
    segs = n - 1
    for s in range(num_steps):
        u_glob = (s / float(num_steps - 1)) * segs
        seg = min(segs - 1, int(u_glob))
        t = u_glob - seg
        t2, t3 = t * t, t * t * t
        p0, p1, p2, p3 = ext_p[seg], ext_p[seg + 1], ext_p[seg + 2], ext_p[seg + 3]
        p = 0.5 * (
            (2.0 * p1)
            + (-p0 + p2) * t
            + (2.0 * p0 - 5.0 * p1 + 4.0 * p2 - p3) * t2
            + (-p0 + 3.0 * p1 - 3.0 * p2 + p3) * t3
        )
        v1, v2 = ext_v[seg + 1], ext_v[seg + 2]
        w = v1[0] + (v2[0] - v1[0]) * t
        th = v1[1] + (v2[1] - v1[1]) * t
        out_p.append(p)
        out_v.append((max(0.0, w), max(0.0, th)))
    return out_p, out_v


def _add_hair_ribbon(
    name,
    points_studs,
    widths_studs,
    thicks_studs,
    mat_hair,
    collection,
    head_center_studs=(0.0, 0.0, 0.0),
    arch=0.35,
    roll_deg=0.0,
    steps=14,
):
    """Build a sculpted faceted-ridge anime/UGC hair lock mesh with sharp pointed tip & clean UVs."""
    hc = Vector(head_center_studs) * STUD
    pts_m = [Vector(p) * STUD for p in points_studs]
    w_m = [w * STUD for w in widths_studs]
    th_m = [t * STUD for t in thicks_studs]
    samples, szs = _catmull_eval(pts_m, w_m, th_m, num_steps=steps)

    mesh = bpy.data.meshes.new(name + "_M")
    bm = bmesh.new()
    uv_layer = bm.loops.layers.uv.new("UVMap")
    rings = []
    roll_rad = math.radians(roll_deg)

    for i in range(len(samples) - 1):
        p = samples[i]
        w_cur, th_cur = szs[i]
        t_v = i / float(len(samples) - 1)
        # Taper cleanly in final 25% of blade toward sharp point
        if t_v > 0.72:
            k_tip = max(0.18, 1.0 - ((t_v - 0.72) / 0.28) * 0.72)
            w_cur *= k_tip
            th_cur *= k_tip
        if i == 0:
            tan = (samples[1] - samples[0])
        else:
            tan = (samples[i + 1] - samples[i - 1])
        if tan.length < 1e-6:
            tan = Vector((0.0, 0.0, -1.0))
        tan.normalize()

        rad_v = p - hc
        n_out = rad_v - tan * rad_v.dot(tan)
        if n_out.length < 1e-5:
            up_fb = Vector((0.0, -1.0, 0.0)) if abs(tan.z) > 0.8 else Vector((0.0, 0.0, 1.0))
            n_out = tan.cross(up_fb)
        n_out.normalize()
        binorm = tan.cross(n_out).normalized()
        if abs(roll_rad) > 1e-4:
            c_r, s_r = math.cos(roll_rad), math.sin(roll_rad)
            n_out, binorm = (n_out * c_r + binorm * s_r).normalized(), (binorm * c_r - n_out * s_r).normalized()

        pts_sec = [
            p - w_cur * binorm - 0.10 * th_cur * n_out,
            p - 0.46 * w_cur * binorm + 0.56 * th_cur * n_out,
            p + (1.0 + arch) * th_cur * n_out,
            p + 0.46 * w_cur * binorm + 0.56 * th_cur * n_out,
            p + w_cur * binorm - 0.10 * th_cur * n_out,
            p - 0.58 * th_cur * n_out,
        ]
        rings.append(([bm.verts.new(pv) for pv in pts_sec], t_v))

    tan0 = (samples[1] - samples[0]).normalized() if len(samples) > 1 else Vector((0, 0, -1))
    root_v = bm.verts.new(samples[0] - tan0 * (0.025 * STUD))
    tip_v = bm.verts.new(samples[-1])

    u_coords = [0.0, 0.25, 0.5, 0.75, 1.0, 0.5]
    r0, v0 = rings[0]
    for k in range(6):
        kn = (k + 1) % 6
        f = bm.faces.new((root_v, r0[kn], r0[k]))
        for lp, u_c, vv in zip(f.loops, (0.5, u_coords[kn], u_coords[k]), (0.0, v0, v0)):
            lp[uv_layer].uv = (u_c, vv)
    for ri in range(len(rings) - 1):
        ra, va = rings[ri]
        rb, vb = rings[ri + 1]
        for k in range(6):
            kn = (k + 1) % 6
            f = bm.faces.new((ra[k], ra[kn], rb[kn], rb[k]))
            for lp, (u_c, vv) in zip(f.loops, [(u_coords[k], va), (u_coords[kn], va), (u_coords[kn], vb), (u_coords[k], vb)]):
                lp[uv_layer].uv = (u_c, vv)
    rlast, vlast = rings[-1]
    for k in range(6):
        kn = (k + 1) % 6
        f = bm.faces.new((rlast[k], rlast[kn], tip_v))
        for lp, (u_c, vv) in zip(f.loops, [(u_coords[k], vlast), (u_coords[kn], vlast), (0.5, 1.0)]):
            lp[uv_layer].uv = (u_c, vv)

    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    for f in bm.faces:
        f.smooth = True
    bm.to_mesh(mesh)
    bm.free()

    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat_hair)
    es = obj.modifiers.new("EdgeSplit", "EDGE_SPLIT")
    es.split_angle = math.radians(56)
    collection.objects.link(obj)
    return obj


def _add_hair_strand(name, points, radii, mat_hair, collection):
    """Compatibility wrapper rendering crisp sculpted hair ribbon instead of round pipe."""
    widths = [max(0.02, r * 1.15) for r in radii]
    thicks = [max(0.015, r * 0.55) for r in radii]
    return _add_hair_ribbon(name, points, widths, thicks, mat_hair, collection)


def _add_curl_puff(name, center_m, rad_m, squash_xyz, mat_hair, collection, segs=14, rings=10):
    mesh = bpy.data.meshes.new(name + "_M")
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segs, v_segments=rings, radius=rad_m)
    uv_layer = bm.loops.layers.uv.new("UVMap")
    for v in bm.verts:
        # Subtle lumpy organic curl facet modulation
        wob = 1.0 + 0.08 * math.sin(v.co.x * 32.0 + v.co.z * 28.0) * math.cos(v.co.y * 30.0)
        v.co.x *= squash_xyz[0] * wob
        v.co.y *= squash_xyz[1] * wob
        v.co.z *= squash_xyz[2] * wob
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    for f in bm.faces:
        f.smooth = True
        for lp in f.loops:
            lp[uv_layer].uv = (0.5 + lp.vert.co.x * 2.0, 0.5 + lp.vert.co.z * 2.0)
    bm.to_mesh(mesh); bm.free()
    o = bpy.data.objects.new(name, mesh)
    o.location = center_m
    o.data.materials.append(mat_hair)
    collection.objects.link(o)
    return o


def _build_skull_liner(prefix, head_center, hs, mat_hair, collection, shell_off=0.052, z_front=0.24, z_back=-0.34):
    """Exact conformal skull/hair cap hugging _create_roblox_head profile with uniform offset (zero skin poke-through)."""
    cx, cy, cz = [c * STUD for c in head_center]
    r0 = 0.60 * hs * STUD
    hh0 = 0.58 * hs * STUD
    fil0 = 0.36 * r0
    r_c = r0 - fil0
    z_c = hh0 - fil0
    off = shell_off * hs * STUD
    r_shell = r0 + off
    fil_shell = fil0 + off
    top_z = hh0 + off

    n_seg = 40
    n_lat = 18
    mesh = bpy.data.meshes.new(prefix + "_HairCap_Mesh")
    bm = bmesh.new()
    uv_layer = bm.loops.layers.uv.new("UVMap")

    rings = []
    # Inner tuck ring at hairline so bottom edge is watertight and cleanly recessed into head
    in_ring = []
    for s in range(n_seg):
        ang = 2.0 * math.pi * s / n_seg
        front_t = (-math.sin(ang) + 1.0) * 0.5
        zc_ang = (z_back + (z_front - z_back) * (front_t ** 1.35)) * hs * STUD
        r_in = 0.56 * hs * STUD if zc_ang <= z_c else max(0.1 * hs * STUD, r_c + math.sqrt(max(0.0, fil0 ** 2 - min(fil0, zc_ang - z_c) ** 2)) - 0.02 * STUD)
        in_ring.append(bm.verts.new((r_in * math.cos(ang), r_in * math.sin(ang), zc_ang)))

    # Distribute latitude rings denser near the rounded upper fillet so top chords never dip into head skin
    for li in range(n_lat):
        tf = (li / float(n_lat)) ** 0.85
        row = []
        for s in range(n_seg):
            ang = 2.0 * math.pi * s / n_seg
            front_t = (-math.sin(ang) + 1.0) * 0.5
            zc_ang = (z_back + (z_front - z_back) * (front_t ** 1.35)) * hs * STUD
            zz = zc_ang + tf * (top_z - zc_ang)
            if zz <= z_c:
                rr = r_shell
            else:
                dz = min(fil_shell, zz - z_c)
                rr = r_c + math.sqrt(max(0.0, fil_shell * fil_shell - dz * dz))
            row.append(bm.verts.new((rr * math.cos(ang), rr * math.sin(ang), zz)))
        rings.append(row)
    top_pole = bm.verts.new((0.0, 0.0, top_z))

    for s in range(n_seg):
        sn = (s + 1) % n_seg
        bm.faces.new((in_ring[s], in_ring[sn], rings[0][sn], rings[0][s]))
        bm.faces.new((rings[-1][s], rings[-1][sn], top_pole))
    for ri in range(len(rings) - 1):
        for s in range(n_seg):
            sn = (s + 1) % n_seg
            bm.faces.new((rings[ri][s], rings[ri][sn], rings[ri + 1][sn], rings[ri + 1][s]))

    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    for f in bm.faces:
        f.smooth = True
        for lp in f.loops:
            lp[uv_layer].uv = (0.5 + lp.vert.co.x * 1.6, 0.5 + lp.vert.co.z * 1.6)
    bm.to_mesh(mesh); bm.free()
    cap = bpy.data.objects.new(prefix + "_HairCap", mesh)
    cap.location = (cx, cy, cz)
    cap.data.materials.append(mat_hair)
    collection.objects.link(cap)
    return cap


def _build_curved_visor(prefix, head_center, hs, mat_cap, collection):
    cx, cy, cz = head_center
    bm = bmesh.new()
    nx, ny = 14, 6
    verts_top, verts_bot = [], []
    half_w = 0.62 * hs * STUD
    depth = 0.52 * hs * STUD
    thick = 0.048 * hs * STUD
    for iy in range(ny + 1):
        ty = iy / float(ny)
        row_t, row_b = [], []
        y_loc = -ty * depth
        w_row = half_w * (1.0 - 0.24 * (ty ** 2))
        for ix in range(nx + 1):
            tx = (ix / float(nx)) * 2.0 - 1.0
            x_loc = tx * w_row
            arch_z = -0.11 * hs * STUD * (tx * tx) - 0.08 * hs * STUD * ty - 0.04 * hs * STUD * (ty * ty)
            row_t.append(bm.verts.new((x_loc, y_loc, arch_z + thick * 0.5)))
            row_b.append(bm.verts.new((x_loc, y_loc, arch_z - thick * 0.5)))
        verts_top.append(row_t)
        verts_bot.append(row_b)
    for iy in range(ny):
        for ix in range(nx):
            bm.faces.new((verts_top[iy][ix], verts_top[iy][ix + 1], verts_top[iy + 1][ix + 1], verts_top[iy + 1][ix]))
            bm.faces.new((verts_bot[iy][ix], verts_bot[iy + 1][ix], verts_bot[iy + 1][ix + 1], verts_bot[iy][ix + 1]))
    for ix in range(nx):
        bm.faces.new((verts_top[0][ix], verts_bot[0][ix], verts_bot[0][ix + 1], verts_top[0][ix + 1]))
        bm.faces.new((verts_top[ny][ix], verts_top[ny][ix + 1], verts_bot[ny][ix + 1], verts_bot[ny][ix]))
    for iy in range(ny):
        bm.faces.new((verts_top[iy][0], verts_top[iy + 1][0], verts_bot[iy + 1][0], verts_bot[iy][0]))
        bm.faces.new((verts_top[iy][nx], verts_bot[iy][nx], verts_bot[iy + 1][nx], verts_top[iy + 1][nx]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    for f in bm.faces:
        f.smooth = True
    mesh = bpy.data.meshes.new(prefix + "_Visor_M")
    bm.to_mesh(mesh); bm.free()
    visor = bpy.data.objects.new(prefix + "_CapVisor", mesh)
    visor.location = (cx * STUD, (cy - 0.54 * hs) * STUD, (cz + 0.30 * hs) * STUD)
    visor.data.materials.append(mat_cap)
    es = visor.modifiers.new("EdgeSplit", "EDGE_SPLIT")
    es.split_angle = math.radians(48)
    collection.objects.link(visor)
    return visor


BODY_PROFILES = {
    "default":      {"tw": 2.00, "td": 1.00, "th": 2.00, "lw": 1.00, "lh": 2.00, "ah": 2.00, "hs": 1.25},
    "boy_athletic": {"tw": 2.02, "td": 1.00, "th": 2.02, "lw": 1.00, "lh": 2.04, "ah": 2.02, "hs": 1.25},
    "stocky_boss":  {"tw": 2.48, "td": 1.32, "th": 2.05, "lw": 1.12, "lh": 1.86, "ah": 2.00, "hs": 1.30},
    "girl_slim":    {"tw": 1.72, "td": 0.86, "th": 1.94, "lw": 0.82, "lh": 2.06, "ah": 1.94, "hs": 1.22},
    "tall_lanky":   {"tw": 1.82, "td": 0.90, "th": 2.18, "lw": 0.86, "lh": 2.38, "ah": 2.24, "hs": 1.22},
    "kid_chubby":   {"tw": 1.80, "td": 1.02, "th": 1.54, "lw": 0.88, "lh": 1.52, "ah": 1.54, "hs": 1.24},
}


def _build_hair(prefix, head_center, scale_h, mat_hair, collection, hair_style="spiky", cap_accent_hex="#D93829"):
    """Build 1 of 10 stylized 3D Roblox UGC hairstyles with faceted ribbon locks framing outside the 35-deg face arc."""
    if hair_style == "bald":
        return []
    cx, cy, cz = head_center
    hs = scale_h
    parts = []

    def P(ox, oy, oz):
        return (cx + ox * hs, cy + oy * hs, cz + oz * hs)

    def W(vals):
        return [v * hs for v in vals]

    def R(sname, pts, widths, thicks, arch=0.38, roll=0.0, steps=14):
        parts.append(
            _add_hair_ribbon(
                f"{prefix}_Hair_{sname}", pts, W(widths), W(thicks), mat_hair, collection,
                head_center_studs=head_center, arch=arch, roll_deg=roll, steps=steps,
            )
        )

    if hair_style in ("spiky", "spiky_teen"):
        parts.append(_build_skull_liner(prefix, head_center, hs, mat_hair, collection, shell_off=0.020, z_front=0.22, z_back=-0.34))
        # Rich anime bangs sweeping naturally down to upper brow + tall dynamic crown spikes
        R("BangC",  [P(-0.04, -0.30, 0.52), P(0.02, -0.57, 0.34), P(0.14, -0.62, 0.16)], [0.22, 0.19, 0.02], [0.09, 0.08, 0.015], roll=-10)
        R("BangL1", [P(0.14, -0.26, 0.52), P(0.32, -0.53, 0.34), P(0.44, -0.58, 0.14)], [0.22, 0.18, 0.02], [0.09, 0.075, 0.015], roll=-18)
        R("BangL2", [P(0.30, -0.14, 0.50), P(0.52, -0.40, 0.28), P(0.62, -0.44, 0.04)], [0.18, 0.16, 0.02], [0.08, 0.065, 0.015], roll=-22)
        R("BangR1", [P(-0.18, -0.26, 0.52), P(-0.36, -0.53, 0.34), P(-0.48, -0.58, 0.14)], [0.22, 0.18, 0.02], [0.09, 0.075, 0.015], roll=18)
        R("BangR2", [P(-0.32, -0.14, 0.50), P(-0.54, -0.40, 0.28), P(-0.64, -0.44, 0.04)], [0.18, 0.16, 0.02], [0.08, 0.065, 0.015], roll=22)
        # Crown dynamic upward spikes
        R("SpkTop1", [P(-0.06, 0.06, 0.54), P(-0.22, -0.22, 0.84), P(-0.40, -0.52, 0.94)], [0.26, 0.20, 0.02], [0.11, 0.085, 0.015], arch=0.55)
        R("SpkTop2", [P(0.14, 0.10, 0.54), P(0.28, -0.14, 0.82), P(0.46, -0.38, 0.90)], [0.24, 0.18, 0.02], [0.10, 0.08, 0.015], arch=0.55)
        R("SpkTopC", [P(0.02, -0.06, 0.56), P(0.06, -0.36, 0.80), P(0.18, -0.60, 0.76)], [0.22, 0.17, 0.02], [0.10, 0.075, 0.015], arch=0.52)
        R("SpkBack1", [P(0.0, 0.28, 0.48), P(0.0, 0.64, 0.64), P(0.0, 0.90, 0.50)], [0.30, 0.24, 0.02], [0.12, 0.09, 0.015], arch=0.50)
        R("SpkBackL", [P(0.32, 0.28, 0.42), P(0.62, 0.54, 0.48), P(0.82, 0.64, 0.28)], [0.22, 0.18, 0.02], [0.09, 0.075, 0.015])
        R("SpkBackR", [P(-0.32, 0.28, 0.42), P(-0.62, 0.54, 0.48), P(-0.82, 0.64, 0.28)], [0.22, 0.18, 0.02], [0.09, 0.075, 0.015])
        R("SideL", [P(0.54, 0.02, 0.32), P(0.61, -0.14, 0.04), P(0.58, -0.24, -0.24)], [0.16, 0.13, 0.02], [0.07, 0.06, 0.01])
        R("SideR", [P(-0.54, 0.02, 0.32), P(-0.61, -0.14, 0.04), P(-0.58, -0.24, -0.24)], [0.16, 0.13, 0.02], [0.07, 0.06, 0.01])
        R("NapeC", [P(0.0, 0.46, 0.22), P(0.0, 0.64, -0.10), P(0.0, 0.58, -0.44)], [0.34, 0.26, 0.03], [0.12, 0.09, 0.015])

    elif hair_style == "slick_part":
        # Sharp executive/Sigma quiff: snug hairline skull cap + seamless swept pompadour + tight sideburns!
        parts.append(_build_skull_liner(prefix, head_center, hs, mat_hair, collection, shell_off=0.018, z_front=0.24, z_back=-0.30))
        R("QuiffMain", [P(-0.22, -0.48, 0.26), P(-0.04, -0.58, 0.64), P(0.24, -0.16, 0.74), P(0.30, 0.40, 0.50)], [0.32, 0.38, 0.32, 0.12], [0.13, 0.17, 0.14, 0.04], arch=0.52, roll=-8)
        R("QuiffCrest", [P(-0.04, -0.50, 0.26), P(0.22, -0.48, 0.58), P(0.44, -0.02, 0.58), P(0.42, 0.44, 0.34)], [0.22, 0.26, 0.24, 0.08], [0.10, 0.12, 0.10, 0.03], arch=0.48, roll=-14)
        R("QuiffSide", [P(-0.32, -0.44, 0.26), P(-0.46, -0.14, 0.54), P(-0.44, 0.28, 0.44), P(-0.28, 0.54, 0.22)], [0.20, 0.22, 0.18, 0.06], [0.09, 0.10, 0.08, 0.03], roll=14)
        R("SideburnL", [P(0.55, -0.18, 0.24), P(0.56, -0.22, 0.02), P(0.55, -0.20, -0.18)], [0.08, 0.07, 0.02], [0.03, 0.025, 0.01])
        R("SideburnR", [P(-0.55, -0.18, 0.24), P(-0.56, -0.22, 0.02), P(-0.55, -0.20, -0.18)], [0.08, 0.07, 0.02], [0.03, 0.025, 0.01])
        R("NapeTaper", [P(0.0, 0.44, 0.30), P(0.0, 0.60, 0.02), P(0.0, 0.56, -0.32)], [0.36, 0.28, 0.10], [0.08, 0.065, 0.02])

    elif hair_style == "messy_curtain":
        # Trendy K-pop / Roblox fluffy wolf-cut: rich layered comma bangs hugging forehead cleanly!
        parts.append(_build_skull_liner(prefix, head_center, hs, mat_hair, collection, shell_off=0.020, z_front=0.22, z_back=-0.36))
        R("CommaL1", [P(0.02, -0.36, 0.52), P(0.24, -0.58, 0.34), P(0.36, -0.56, 0.12)], [0.22, 0.19, 0.02], [0.09, 0.08, 0.015], roll=-14)
        R("CommaR1", [P(-0.02, -0.36, 0.52), P(-0.24, -0.58, 0.34), P(-0.36, -0.56, 0.12)], [0.22, 0.19, 0.02], [0.09, 0.08, 0.015], roll=14)
        R("CommaL2", [P(0.14, -0.28, 0.54), P(0.42, -0.50, 0.30), P(0.52, -0.48, 0.02), P(0.44, -0.44, -0.14)], [0.22, 0.20, 0.14, 0.02], [0.09, 0.08, 0.05, 0.01], roll=-18)
        R("CommaR2", [P(-0.14, -0.28, 0.54), P(-0.42, -0.50, 0.30), P(-0.52, -0.48, 0.02), P(-0.44, -0.44, -0.14)], [0.22, 0.20, 0.14, 0.02], [0.09, 0.08, 0.05, 0.01], roll=18)
        R("WispL3",  [P(0.28, -0.10, 0.54), P(0.56, -0.34, 0.26), P(0.62, -0.26, -0.10), P(0.56, -0.22, -0.32)], [0.18, 0.18, 0.12, 0.02], [0.08, 0.07, 0.05, 0.01], roll=-20)
        R("WispR3",  [P(-0.28, -0.10, 0.54), P(-0.56, -0.34, 0.26), P(-0.62, -0.26, -0.10), P(-0.56, -0.22, -0.32)], [0.18, 0.18, 0.12, 0.02], [0.08, 0.07, 0.05, 0.01], roll=20)
        R("FluffTopL", [P(0.08, -0.12, 0.54), P(0.34, 0.12, 0.70), P(0.52, 0.42, 0.44)], [0.28, 0.26, 0.06], [0.11, 0.10, 0.03], arch=0.50)
        R("FluffTopR", [P(-0.08, -0.12, 0.54), P(-0.34, 0.12, 0.70), P(-0.52, 0.42, 0.44)], [0.28, 0.26, 0.06], [0.11, 0.10, 0.03], arch=0.50)
        R("CrownSpk",  [P(0.0, 0.08, 0.54), P(-0.06, 0.26, 0.74), P(0.04, 0.58, 0.50)], [0.26, 0.22, 0.04], [0.10, 0.09, 0.02], arch=0.52)
        R("WolfNapeC", [P(0.0, 0.40, 0.34), P(0.0, 0.66, -0.04), P(0.0, 0.74, -0.44)], [0.36, 0.30, 0.06], [0.12, 0.10, 0.025])
        R("WolfNapeL", [P(0.36, 0.34, 0.28), P(0.62, 0.44, -0.10), P(0.72, 0.40, -0.42)], [0.20, 0.18, 0.03], [0.08, 0.07, 0.015])
        R("WolfNapeR", [P(-0.36, 0.34, 0.28), P(-0.62, 0.44, -0.10), P(-0.72, 0.40, -0.42)], [0.20, 0.18, 0.03], [0.08, 0.07, 0.015])

    elif hair_style == "bob_chin":
        parts.append(_build_skull_liner(prefix, head_center, hs, mat_hair, collection, shell_off=0.020, z_front=0.22, z_back=-0.38))
        R("SweepBang", [P(-0.32, -0.36, 0.50), P(0.04, -0.58, 0.36), P(0.44, -0.50, 0.20)], [0.22, 0.19, 0.03], [0.085, 0.075, 0.015], roll=-12)
        R("SideBangL", [P(0.16, -0.32, 0.52), P(0.50, -0.46, 0.30), P(0.58, -0.34, -0.08)], [0.20, 0.17, 0.03], [0.08, 0.065, 0.015], roll=-15)
        for sgn, sn in ((1, "L"), (-1, "R")):
            R(f"BobCheek{sn}", [P(sgn * 0.28, -0.10, 0.50), P(sgn * 0.60, -0.20, 0.12), P(sgn * 0.58, -0.24, -0.36), P(sgn * 0.44, -0.20, -0.50)], [0.25, 0.26, 0.20, 0.04], [0.10, 0.10, 0.08, 0.02])
            R(f"BobBack{sn}",  [P(sgn * 0.34, 0.24, 0.48), P(sgn * 0.60, 0.46, 0.06), P(sgn * 0.48, 0.52, -0.42)], [0.26, 0.26, 0.08], [0.10, 0.10, 0.03])
        R("BobBackC", [P(0.0, 0.34, 0.50), P(0.0, 0.66, 0.08), P(0.0, 0.60, -0.46)], [0.38, 0.36, 0.14], [0.12, 0.11, 0.04])

    elif hair_style == "long_ponytail":
        parts.append(_build_skull_liner(prefix, head_center, hs, mat_hair, collection, shell_off=0.020, z_front=0.22, z_back=-0.34))
        R("TopCrownL", [P(0.02, -0.32, 0.50), P(0.26, 0.0, 0.61), P(0.14, 0.50, 0.36)], [0.28, 0.30, 0.16], [0.10, 0.11, 0.06], arch=0.45)
        R("TopCrownR", [P(-0.02, -0.32, 0.50), P(-0.26, 0.0, 0.61), P(-0.14, 0.50, 0.36)], [0.28, 0.30, 0.16], [0.10, 0.11, 0.06], arch=0.45)
        R("BangC", [P(-0.06, -0.38, 0.50), P(0.02, -0.58, 0.34), P(0.14, -0.58, 0.20)], [0.22, 0.18, 0.02], [0.08, 0.065, 0.01], roll=-8)
        R("BangL", [P(0.06, -0.34, 0.50), P(0.34, -0.54, 0.34), P(0.52, -0.44, 0.16)], [0.22, 0.18, 0.02], [0.08, 0.065, 0.01], roll=-14)
        R("BangR", [P(-0.08, -0.34, 0.50), P(-0.36, -0.54, 0.34), P(-0.52, -0.44, 0.16)], [0.22, 0.18, 0.02], [0.08, 0.065, 0.01], roll=14)
        R("TendrilL", [P(0.48, -0.30, 0.26), P(0.56, -0.38, -0.10), P(0.50, -0.32, -0.50)], [0.11, 0.09, 0.015], [0.05, 0.04, 0.01])
        R("TendrilR", [P(-0.48, -0.30, 0.26), P(-0.56, -0.38, -0.10), P(-0.50, -0.32, -0.50)], [0.11, 0.09, 0.015], [0.05, 0.04, 0.01])
        parts.append(_add_curl_puff(f"{prefix}_PonyTie", (cx * STUD, (cy + 0.58 * hs) * STUD, (cz + 0.30 * hs) * STUD), 0.18 * hs * STUD, (1.1, 0.9, 1.1), mat_hair, collection, segs=12, rings=8))
        R("PonyCore", [P(0.0, 0.58, 0.30), P(0.0, 1.02, 0.12), P(0.0, 1.08, -0.68), P(0.0, 0.90, -1.48)], [0.24, 0.30, 0.22, 0.03], [0.12, 0.14, 0.10, 0.02], arch=0.45, steps=18)
        R("PonyWingL", [P(0.04, 0.60, 0.28), P(0.28, 0.98, 0.04), P(0.34, 1.00, -0.64), P(0.22, 0.86, -1.26)], [0.16, 0.20, 0.14, 0.02], [0.08, 0.09, 0.06, 0.015], steps=16)
        R("PonyWingR", [P(-0.04, 0.60, 0.28), P(-0.28, 0.98, 0.04), P(-0.34, 1.00, -0.64), P(-0.22, 0.86, -1.26)], [0.16, 0.20, 0.14, 0.02], [0.08, 0.09, 0.06, 0.015], steps=16)

    elif hair_style == "curly_fro":
        # Lush Gen-Z broccoli curly crown + fluffy forehead fringe curls + tight skull base
        parts.append(_build_skull_liner(prefix, head_center, hs, mat_hair, collection, shell_off=0.020, z_front=0.30, z_back=-0.28))
        curl_spec = [
            (0.0, -0.02, 0.60, 0.34, (1.20, 1.15, 0.92)),
            (-0.30, -0.14, 0.56, 0.28, (1.12, 1.05, 0.95)), (0.30, -0.14, 0.56, 0.28, (1.12, 1.05, 0.95)),
            (-0.48, 0.16, 0.44, 0.27, (1.05, 1.08, 0.95)), (0.48, 0.16, 0.44, 0.27, (1.05, 1.08, 0.95)),
            (-0.24, 0.34, 0.48, 0.29, (1.08, 1.12, 0.92)), (0.24, 0.34, 0.48, 0.29, (1.08, 1.12, 0.92)),
            (0.0, 0.48, 0.36, 0.30, (1.20, 0.98, 0.95)),
            (-0.50, 0.38, 0.22, 0.24, (1.0, 1.05, 1.0)),  (0.50, 0.38, 0.22, 0.24, (1.0, 1.05, 1.0)),
            (0.0, 0.58, 0.12, 0.26, (1.25, 0.90, 1.0)),
            # Front lush overlapping curly fringe bobbing cleanly down onto upper forehead (z=0.32..0.38)!
            (-0.42, -0.44, 0.36, 0.22, (1.05, 1.02, 0.96)), (-0.16, -0.52, 0.38, 0.24, (1.08, 1.02, 0.95)),
            (0.16, -0.52, 0.39, 0.23, (1.08, 1.02, 0.95)),  (0.42, -0.44, 0.36, 0.22, (1.05, 1.02, 0.96)),
            (-0.56, -0.22, 0.32, 0.21, (1.0, 1.08, 1.0)),   (0.56, -0.22, 0.32, 0.21, (1.0, 1.08, 1.0)),
        ]
        for idx, (ox, oy, oz, rad, sq) in enumerate(curl_spec):
            parts.append(_add_curl_puff(f"{prefix}_HairCurl_{idx}", (P(ox, oy, oz)[0] * STUD, P(ox, oy, oz)[1] * STUD, P(ox, oy, oz)[2] * STUD), rad * hs * STUD, sq, mat_hair, collection))

    elif hair_style == "cap_hair":
        mat_cap = make_solid_mat(prefix + "_CapMat", hex_to_linear_rgba(cap_accent_hex), 0.58)
        parts.append(_build_skull_liner(prefix + "_Cap", head_center, hs, mat_cap, collection, shell_off=0.062, z_front=0.28, z_back=-0.16))
        parts.append(_add_curl_puff(f"{prefix}_CapBtn", (cx * STUD, (cy + 0.02 * hs) * STUD, (cz + 0.67 * hs) * STUD), 0.08 * hs * STUD, (1.1, 1.1, 0.50), mat_cap, collection, segs=12, rings=6))
        parts.append(_build_curved_visor(prefix, head_center, hs, mat_cap, collection))
        # Tufts tucked strictly BELOW visor & temple rim so zero hair pokes through visor top!
        R("CapTuftL", [P(0.40, -0.28, 0.24), P(0.62, -0.40, 0.14), P(0.66, -0.36, -0.06)], [0.14, 0.12, 0.02], [0.055, 0.045, 0.01], roll=-18)
        R("CapTuftR", [P(-0.40, -0.28, 0.24), P(-0.62, -0.40, 0.14), P(-0.66, -0.36, -0.06)], [0.14, 0.12, 0.02], [0.055, 0.045, 0.01], roll=18)
        R("CapBack",  [P(0.0, 0.48, 0.04), P(0.0, 0.66, -0.16), P(0.0, 0.60, -0.40)], [0.34, 0.26, 0.05], [0.09, 0.07, 0.02])

    elif hair_style == "twin_buns":
        parts.append(_build_skull_liner(prefix, head_center, hs, mat_hair, collection, shell_off=0.020, z_front=0.22, z_back=-0.34))
        for sgn, sn in ((1, "L"), (-1, "R")):
            bpos = P(sgn * 0.50, 0.08, 0.58)
            parts.append(_add_curl_puff(f"{prefix}_Bun_{sn}", (bpos[0] * STUD, bpos[1] * STUD, bpos[2] * STUD), 0.25 * hs * STUD, (0.95, 1.02, 1.05), mat_hair, collection, segs=16, rings=10))
            R(f"BunBang{sn}", [P(sgn * 0.02, -0.34, 0.50), P(sgn * 0.32, -0.54, 0.34), P(sgn * 0.52, -0.44, 0.14)], [0.19, 0.16, 0.02], [0.075, 0.065, 0.01])
            R(f"BunLock{sn}", [P(sgn * 0.48, -0.30, 0.26), P(sgn * 0.56, -0.38, -0.08), P(sgn * 0.50, -0.30, -0.48)], [0.11, 0.09, 0.015], [0.05, 0.04, 0.01])

    elif hair_style == "mohawk_fade":
        for idx, (oy, oz, tilt_y, h_top, w_b) in enumerate([
            (-0.46, 0.48, -0.70, 0.88, 0.20),
            (-0.22, 0.56, -0.40, 1.06, 0.24),
            (0.04,  0.58, -0.10, 1.08, 0.24),
            (0.28,  0.52,  0.22, 0.98, 0.22),
            (0.48,  0.34,  0.56, 0.74, 0.19),
            (0.56,  0.08,  0.76, 0.36, 0.17),
        ]):
            R(f"Hawk_{idx}", [P(0.0, oy, oz), P(0.0, oy + (tilt_y - oy) * 0.55, (oz + h_top) * 0.55), P(0.0, tilt_y, h_top)], [w_b, w_b * 0.80, 0.02], [0.10, 0.08, 0.015], arch=0.58, steps=12)

    return parts


def build_roblox_character(
    name: str,
    shirt_path: str,
    pants_path: str,
    face_png: str,
    skin_hex: str = "#F2C296",
    hair_hex: str = "#2B1B14",
    location_m=(0.0, 0.0, 0.0),
    yaw_deg: float = 0.0,
    scale_h: float = None,
    rig_type: str = "R15",
    hair_style: str = "spiky",
    body_profile: str = "default",
    accessories: list = None,
    cap_accent_hex: str = "#D93829",
):
    """
    Build a unique, articulated R15 (or R6) Roblox character with customizable body_profile,
    8 hair styles, 35-deg UGC Anime face projection, and optional 3D accessories.
    """
    prof = dict(BODY_PROFILES.get(body_profile, BODY_PROFILES["default"]))
    if scale_h is not None:
        prof["hs"] = scale_h
    tw, td, th = prof["tw"], prof["td"], prof["th"]
    lw, lh, ah, hs = prof["lw"], prof["lh"], prof["ah"], prof["hs"]

    col = bpy.data.collections.new(f"Char_{name}")
    bpy.context.scene.collection.children.link(col)

    skin_rgba = hex_to_linear_rgba(skin_hex)
    hair_rgba = hex_to_linear_rgba(hair_hex)
    mat_shirt = make_skin_cloth_mat(f"{name}_Shirt", skin_rgba, shirt_path)
    mat_pants = make_skin_cloth_mat(f"{name}_Pants", skin_rgba, pants_path)
    mat_head, face_tex_node = make_head_face_mat(f"{name}_Head", skin_rgba, face_png)
    mat_hair = make_stylized_hair_mat(f"{name}_Hair", hair_rgba, roughness=0.56)

    hip_z = lh
    neck_z = lh + th
    arm_x = 0.5 * tw + 0.5 * lw + 0.02
    leg_x = 0.255 * tw
    head_center = (0.0, 0.0, neck_z + 0.52 * hs)
    hair_parts = _build_hair(name, head_center, hs, mat_hair, col, hair_style=hair_style, cap_accent_hex=cap_accent_hex)

    if rig_type.upper() == "R15":
        lt_h = 0.325 * th; ut_h = 0.675 * th
        ua_h = 0.525 * ah; la_h = 0.475 * ah
        ul_h = 0.50 * lh; ll_h = 0.50 * lh
        parts_map = [
            (_create_uv_box(f"{name}_LowerTorso", (tw, td, lt_h), (0.0, 0.0, hip_z + 0.5 * lt_h), TORSO_UV, mat_shirt, col, v_range=(0.0, 0.325)), "LowerTorso"),
            (_create_uv_box(f"{name}_UpperTorso", (tw, td, ut_h), (0.0, 0.0, hip_z + lt_h + 0.5 * ut_h), TORSO_UV, mat_shirt, col, v_range=(0.325, 1.0)), "UpperTorso"),
            (_create_uv_box(f"{name}_UpperArmR", (lw, lw, ua_h), (-arm_x, 0.0, neck_z - 0.5 * ua_h), RLIMB_UV, mat_shirt, col, v_range=(0.475, 1.0)), "RightUpperArm"),
            (_create_uv_box(f"{name}_LowerArmR", (lw, lw, la_h), (-arm_x, 0.0, neck_z - ua_h - 0.5 * la_h), RLIMB_UV, mat_shirt, col, v_range=(0.0, 0.475)), "RightLowerArm"),
            (_create_uv_box(f"{name}_UpperArmL", (lw, lw, ua_h), (arm_x, 0.0, neck_z - 0.5 * ua_h), LLIMB_UV, mat_shirt, col, v_range=(0.475, 1.0)), "LeftUpperArm"),
            (_create_uv_box(f"{name}_LowerArmL", (lw, lw, la_h), (arm_x, 0.0, neck_z - ua_h - 0.5 * la_h), LLIMB_UV, mat_shirt, col, v_range=(0.0, 0.475)), "LeftLowerArm"),
            (_create_uv_box(f"{name}_UpperLegR", (lw, lw, ul_h), (-leg_x, 0.0, ll_h + 0.5 * ul_h), RLIMB_UV, mat_pants, col, v_range=(0.5, 1.0)), "RightUpperLeg"),
            (_create_uv_box(f"{name}_LowerLegR", (lw, lw, ll_h), (-leg_x, 0.0, 0.5 * ll_h), RLIMB_UV, mat_pants, col, v_range=(0.0, 0.5)), "RightLowerLeg"),
            (_create_uv_box(f"{name}_UpperLegL", (lw, lw, ul_h), (leg_x, 0.0, ll_h + 0.5 * ul_h), LLIMB_UV, mat_pants, col, v_range=(0.5, 1.0)), "LeftUpperLeg"),
            (_create_uv_box(f"{name}_LowerLegL", (lw, lw, ll_h), (leg_x, 0.0, 0.5 * ll_h), LLIMB_UV, mat_pants, col, v_range=(0.0, 0.5)), "LeftLowerLeg"),
            (_create_roblox_head(f"{name}_Head", head_center, hs, mat_head, col), "Head"),
        ] + [(hp, "Head") for hp in hair_parts]
    else:
        parts_map = [
            (_create_uv_box(f"{name}_Torso", (tw, td, th), (0, 0, hip_z + 0.5 * th), TORSO_UV, mat_shirt, col), "Torso"),
            (_create_uv_box(f"{name}_ArmR", (lw, lw, ah), (-arm_x, 0, neck_z - 0.5 * ah), RLIMB_UV, mat_shirt, col), "Arm.R"),
            (_create_uv_box(f"{name}_ArmL", (lw, lw, ah), (arm_x, 0, neck_z - 0.5 * ah), LLIMB_UV, mat_shirt, col), "Arm.L"),
            (_create_uv_box(f"{name}_LegR", (lw, lw, lh), (-leg_x, 0, 0.5 * lh), RLIMB_UV, mat_pants, col), "Leg.R"),
            (_create_uv_box(f"{name}_LegL", (lw, lw, lh), (leg_x, 0, 0.5 * lh), LLIMB_UV, mat_pants, col), "Leg.L"),
            (_create_roblox_head(f"{name}_Head", head_center, hs, mat_head, col), "Head"),
        ] + [(hp, "Head") for hp in hair_parts]

    arm_data = bpy.data.armatures.new(f"RIG_{name}_Data")
    arm_obj = bpy.data.objects.new(f"RIG_{name}", arm_data)
    col.objects.link(arm_obj)
    bpy.context.view_layer.objects.active = arm_obj
    with bpy.context.temp_override(object=arm_obj, active_object=arm_obj):
        bpy.ops.object.mode_set(mode="EDIT")
        eb = arm_data.edit_bones
        def ab(bn, h, t, p=None, c=False):
            b = eb.new(bn); b.head = Vector(h) * STUD; b.tail = Vector(t) * STUD
            if p: b.parent = p; b.use_connect = c
            return b
        br = ab("Root", (0, 0, 0), (0, 0, 1))
        if rig_type.upper() == "R15":
            split_z = hip_z + 0.325 * th
            sh_z = neck_z - 0.16 * ah; el_z = neck_z - 0.525 * ah; hd_z = neck_z - ah; kn_z = 0.5 * lh
            lt = ab("LowerTorso", (0, 0, hip_z), (0, 0, split_z), br)
            ut = ab("UpperTorso", (0, 0, split_z), (0, 0, neck_z), lt, True)
            ab("Head", (0, 0, neck_z), (0, 0, neck_z + hs), ut, True)
            lua = ab("LeftUpperArm", (arm_x, 0, sh_z), (arm_x, 0, el_z), ut)
            ab("LeftLowerArm", (arm_x, 0, el_z), (arm_x, 0, hd_z), lua, True)
            rua = ab("RightUpperArm", (-arm_x, 0, sh_z), (-arm_x, 0, el_z), ut)
            ab("RightLowerArm", (-arm_x, 0, el_z), (-arm_x, 0, hd_z), rua, True)
            lul = ab("LeftUpperLeg", (leg_x, 0, hip_z), (leg_x, 0, kn_z), lt)
            ab("LeftLowerLeg", (leg_x, 0, kn_z), (leg_x, 0, 0.0), lul, True)
            rul = ab("RightUpperLeg", (-leg_x, 0, hip_z), (-leg_x, 0, kn_z), lt)
            ab("RightLowerLeg", (-leg_x, 0, kn_z), (-leg_x, 0, 0.0), rul, True)
        else:
            sh_z = neck_z - 0.175 * ah
            bt = ab("Torso", (0, 0, hip_z), (0, 0, neck_z), br)
            ab("Head", (0, 0, neck_z), (0, 0, neck_z + hs), bt, True)
            ab("Arm.L", (arm_x, 0, sh_z), (arm_x, 0, neck_z - ah), bt)
            ab("Arm.R", (-arm_x, 0, sh_z), (-arm_x, 0, neck_z - ah), bt)
            ab("Leg.L", (leg_x, 0, hip_z), (leg_x, 0, 0), bt)
            ab("Leg.R", (-leg_x, 0, hip_z), (-leg_x, 0, 0), bt)
        bpy.ops.object.mode_set(mode="OBJECT")

    for obj, bname in parts_map:
        wm = obj.matrix_world.copy()
        obj.parent = arm_obj
        obj.matrix_parent_inverse = arm_obj.matrix_world.inverted()
        obj.matrix_world = wm
        vg = obj.vertex_groups.get(bname) or obj.vertex_groups.new(name=bname)
        vg.add(list(range(len(obj.data.vertices))), 1.0, "REPLACE")
        mod = obj.modifiers.new("Armature", "ARMATURE")
        mod.object = arm_obj

    arm_obj.location = Vector(location_m)
    arm_obj.rotation_euler = Euler((0.0, 0.0, math.radians(yaw_deg)))
    info = {
        "armature": arm_obj, "face_tex_node": face_tex_node, "collection": col, "rig_type": rig_type.upper(),
        "hair_hex": hair_hex, "hair_mat": mat_hair,
        "metrics": {
            "tw": tw, "td": td, "th": th, "lh": lh, "hs": hs, "neck_z": neck_z,
            "head_center": head_center, "eye_z": (neck_z + 0.56 * hs) * STUD,
            "head_top_z": (neck_z + 1.15 * hs) * STUD, "shoulder_w": (tw + 2.0 * lw) * STUD,
            "stride_m": 0.58 * (lh / 2.0),
        },
    }
    for acc in (accessories or []):
        if isinstance(acc, str):
            add_accessory(info, acc)
        elif isinstance(acc, dict):
            add_accessory(info, **acc)
    return info


def add_accessory(char_info: dict, acc_type: str, color_hex: str = None, accent_hex: str = "#E53935"):
    """Attach stylized 3D silhouette accessories & sculpted facial hair weighted cleanly to Head or UpperTorso."""
    arm = char_info["armature"]; col = char_info["collection"]; m = char_info["metrics"]
    cx, cy, cz = m["head_center"]; hs = m["hs"]; neck_z = m["neck_z"]; td = m["td"]
    head_bone = "Head"
    torso_bone = "UpperTorso" if char_info.get("rig_type") == "R15" else "Torso"
    c_hex = color_hex if color_hex is not None else "#1E2430"
    mat_c = make_solid_mat(f"{arm.name}_{acc_type}_Mat", hex_to_linear_rgba(c_hex), 0.38)
    mat_a = make_solid_mat(f"{arm.name}_{acc_type}_Acc", hex_to_linear_rgba(accent_hex), 0.35)
    if acc_type in ("mustache", "goatee", "full_beard", "stubble_scruff"):
        if color_hex is not None:
            mat_fh = make_stylized_hair_mat(f"{arm.name}_{acc_type}_Hair", hex_to_linear_rgba(color_hex), 0.62)
        else:
            mat_fh = char_info.get("hair_mat") or make_stylized_hair_mat(f"{arm.name}_{acc_type}_Hair", hex_to_linear_rgba(char_info.get("hair_hex", "#2B1B14")), 0.62)
    else:
        mat_fh = mat_c
    created = []

    def _box(n, loc_s, sz_s, mt, rot_d=(0, 0, 0), bone=head_bone):
        o = _create_uv_box(f"{arm.name}_{n}", sz_s, loc_s, {"front": (0,0,10,10), "back": (0,0,10,10), "left": (0,0,10,10), "right": (0,0,10,10), "top": (0,0,10,10), "bottom": (0,0,10,10)}, mt, col, bevel_m=0.004)
        o.rotation_euler = Euler([math.radians(a) for a in rot_d])
        created.append((o, bone))
        return o

    def _fhp(ox, oy, oz):
        return (cx + ox * hs, cy + oy * hs, cz + oz * hs)

    def _fh_rib(sname, pts, ws, ths, arch=0.45, roll=0.0, steps=12):
        o = _add_hair_ribbon(
            f"{arm.name}_{sname}", pts, [v * hs for v in ws], [v * hs for v in ths],
            mat_fh, col, head_center_studs=m["head_center"], arch=arch, roll_deg=roll, steps=steps,
        )
        created.append((o, head_bone))
        return o

    def _add_mustache_wings(z_off=-0.095, curl_up=0.022, thick=0.026):
        for sgn, sn in ((1, "L"), (-1, "R")):
            _fh_rib(
                f"Stache_{sn}",
                [
                    _fhp(sgn * 0.008, -0.618, z_off + 0.006),
                    _fhp(sgn * 0.115, -0.608, z_off - 0.012),
                    _fhp(sgn * 0.215, -0.574, z_off - 0.004),
                    _fhp(sgn * 0.275, -0.538, z_off + curl_up),
                ],
                [0.036, 0.044, 0.028, 0.006],
                [thick, thick * 1.1, thick * 0.75, 0.006],
                arch=0.50,
            )

    if acc_type == "glasses_round":
        fy = cy - 0.612 * hs; fz = cz + 0.055 * hs
        rad_g = 0.155 * hs * STUD
        mat_lens = make_solid_mat(f"{arm.name}_Lens", (0.75, 0.90, 1.0, 1.0), 0.08)
        bsdf_l = next(n for n in mat_lens.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
        bsdf_l.inputs["Alpha"].default_value = 0.16
        mat_lens.blend_method = "BLEND" if hasattr(mat_lens, "blend_method") else "HASHED"
        for sgn, sn in ((-1, "L"), (1, "R")):
            ox = sgn * 0.235 * hs * STUD
            bpy.ops.mesh.primitive_torus_add(
                major_segments=24, minor_segments=8, major_radius=rad_g, minor_radius=0.018 * hs * STUD,
                location=(ox, fy * STUD, fz * STUD), rotation=(math.radians(90), 0, 0),
            )
            ring = bpy.context.active_object; ring.name = f"{arm.name}_GlassRing_{sn}"
            ring.data.materials.append(mat_c)
            for p in ring.data.polygons: p.use_smooth = True
            for c in list(ring.users_collection): c.objects.unlink(ring)
            col.objects.link(ring); created.append((ring, head_bone))
            bpy.ops.mesh.primitive_cylinder_add(
                vertices=24, radius=rad_g * 0.92, depth=0.01 * STUD,
                location=(ox, (fy + 0.01) * STUD, fz * STUD), rotation=(math.radians(90), 0, 0),
            )
            lens = bpy.context.active_object; lens.name = f"{arm.name}_GlassLens_{sn}"
            lens.data.materials.append(mat_lens)
            for c in list(lens.users_collection): c.objects.unlink(lens)
            col.objects.link(lens); created.append((lens, head_bone))
            _box(f"Temple_{sn}", (sgn * 0.44 * hs, fy + 0.35 * hs, fz), (0.03, 0.70 * hs, 0.04), mat_c)
        _box("Bridge", (0.0, fy, fz + 0.02 * hs), (0.14 * hs, 0.03, 0.035), mat_c)
    elif acc_type == "glasses_square":
        fy = cy - 0.605 * hs; fz = cz + 0.055 * hs
        w_f = 0.34 * hs; h_f = 0.21 * hs; t_r = 0.040 * hs
        mat_lens = make_solid_mat(f"{arm.name}_Lens", (0.75, 0.90, 1.0, 1.0), 0.08)
        bsdf_l = next(n for n in mat_lens.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
        bsdf_l.inputs["Alpha"].default_value = 0.16
        mat_lens.blend_method = "BLEND" if hasattr(mat_lens, "blend_method") else "HASHED"
        for sgn, sn in ((-1, "L"), (1, "R")):
            ox = sgn * 0.24 * hs
            _box(f"RimT_{sn}", (ox, fy, fz + h_f * 0.45), (w_f, 0.045, t_r), mat_c)
            _box(f"RimB_{sn}", (ox, fy, fz - h_f * 0.45), (w_f, 0.045, t_r), mat_c)
            _box(f"RimO_{sn}", (ox + sgn * w_f * 0.45, fy, fz), (t_r, 0.045, h_f), mat_c)
            _box(f"RimI_{sn}", (ox - sgn * w_f * 0.45, fy, fz), (t_r, 0.045, h_f), mat_c)
            _box(f"Lens_{sn}", (ox, fy + 0.01, fz), (w_f * 0.85, 0.015, h_f * 0.85), mat_lens)
            _box(f"Temple_{sn}", (sgn * 0.44 * hs, fy + 0.35 * hs, fz), (0.035, 0.70 * hs, 0.045), mat_c)
        _box("Bridge", (0.0, fy, fz + 0.03), (0.16 * hs, 0.035, 0.040), mat_c)
    elif acc_type == "mustache":
        _add_mustache_wings(z_off=-0.092, curl_up=0.025, thick=0.028)
    elif acc_type == "goatee":
        _add_mustache_wings(z_off=-0.092, curl_up=-0.015, thick=0.024)
        _fh_rib("SoulPatch", [_fhp(0.0, -0.602, -0.30), _fhp(0.0, -0.608, -0.44), _fhp(0.0, -0.52, -0.62)], [0.055, 0.075, 0.015], [0.022, 0.030, 0.010], arch=0.45)
        for sgn, sn in ((1, "L"), (-1, "R")):
            _fh_rib(f"GoateeJaw_{sn}", [_fhp(sgn * 0.16, -0.585, -0.32), _fhp(sgn * 0.12, -0.585, -0.48), _fhp(sgn * 0.02, -0.525, -0.62)], [0.045, 0.055, 0.015], [0.020, 0.026, 0.010])
    elif acc_type == "full_beard":
        _add_mustache_wings(z_off=-0.092, curl_up=-0.018, thick=0.028)
        _fh_rib("BeardChin", [_fhp(0.0, -0.605, -0.32), _fhp(0.0, -0.635, -0.50), _fhp(0.0, -0.54, -0.72)], [0.16, 0.18, 0.03], [0.055, 0.075, 0.02], arch=0.48)
        for sgn, sn in ((1, "L"), (-1, "R")):
            _fh_rib(
                f"BeardJaw_{sn}",
                [
                    _fhp(sgn * 0.56, -0.22, 0.12),
                    _fhp(sgn * 0.57, -0.36, -0.18),
                    _fhp(sgn * 0.40, -0.52, -0.44),
                    _fhp(sgn * 0.10, -0.60, -0.66),
                ],
                [0.08, 0.13, 0.15, 0.04],
                [0.03, 0.05, 0.06, 0.02],
                arch=0.45,
            )
            _fh_rib(f"BeardCheek_{sn}", [_fhp(sgn * 0.44, -0.46, -0.18), _fhp(sgn * 0.28, -0.56, -0.38), _fhp(sgn * 0.08, -0.60, -0.62)], [0.08, 0.10, 0.03], [0.03, 0.045, 0.015])
    elif acc_type == "stubble_scruff":
        _fh_rib("SoulTuft", [_fhp(0.0, -0.600, -0.30), _fhp(0.0, -0.604, -0.40), _fhp(0.0, -0.565, -0.50)], [0.045, 0.055, 0.012], [0.016, 0.020, 0.008])
        for sgn, sn in ((1, "L"), (-1, "R")):
            _fh_rib(f"ScruffSide_{sn}", [_fhp(sgn * 0.57, -0.22, 0.14), _fhp(sgn * 0.58, -0.32, -0.14), _fhp(sgn * 0.44, -0.46, -0.38)], [0.05, 0.055, 0.015], [0.016, 0.018, 0.008])
    elif acc_type == "top_hat":
        _box("HatBrim", (0, 0, neck_z + 1.05 * hs), (1.72 * hs, 1.72 * hs, 0.10), mat_c)
        _box("HatBand", (0, 0, neck_z + 1.18 * hs), (1.16 * hs, 1.16 * hs, 0.16), mat_a)
        _box("HatCrown", (0, 0, neck_z + 1.56 * hs), (1.10 * hs, 1.10 * hs, 0.72 * hs), mat_c)
    elif acc_type == "chef_hat":
        _box("ChefBand", (0, 0, neck_z + 1.10 * hs), (1.28 * hs, 1.28 * hs, 0.26), mat_c)
        _box("ChefPuff", (0, 0.04, neck_z + 1.54 * hs), (1.46 * hs, 1.46 * hs, 0.68 * hs), mat_c)
    elif acc_type == "backpack":
        by = 0.5 * td + 0.34
        _box("PackMain", (0, by, neck_z - 0.92), (1.45, 0.62, 1.48), mat_c, bone=torso_bone)
        _box("PackPocket", (0, by + 0.24, neck_z - 1.22), (1.10, 0.28, 0.72), mat_a, bone=torso_bone)
    elif acc_type == "bowtie":
        fy = -0.5 * td - 0.06; fz = neck_z - 0.14
        _box("BowL", (-0.22, fy, fz), (0.28, 0.08, 0.18), mat_a, (0, 10, 0), bone=torso_bone)
        _box("BowR", (0.22, fy, fz), (0.28, 0.08, 0.18), mat_a, (0, -10, 0), bone=torso_bone)
        _box("BowC", (0.0, fy - 0.02, fz), (0.14, 0.10, 0.14), mat_c, bone=torso_bone)

    bpy.context.view_layer.update()
    for ob, bn in created:
        ob.matrix_world = arm.matrix_world @ ob.matrix_world
        wm = ob.matrix_world.copy()
        ob.parent = arm; ob.matrix_parent_inverse = arm.matrix_world.inverted(); ob.matrix_world = wm
        vg = ob.vertex_groups.new(name=bn); vg.add(list(range(len(ob.data.vertices))), 1.0, "REPLACE")
        mod = ob.modifiers.new("Armature", "ARMATURE"); mod.object = arm
    return [o for o, _ in created]


def add_scarf_3d(char_info: dict, color_hex: str = "#D93829", stripe_hex: str = "#8C1D18"):
    """Attach a stylized 3D neck scarf (collar torus + two hanging ends) weighted to UpperTorso/Torso."""
    arm_obj = char_info["armature"]
    col = char_info["collection"]
    bone_name = "UpperTorso" if char_info.get("rig_type") == "R15" else "Torso"

    mat_main = make_solid_mat(f"{arm_obj.name}_ScarfMain", hex_to_linear_rgba(color_hex), roughness=0.68)
    mat_stripe = make_solid_mat(f"{arm_obj.name}_ScarfStripe", hex_to_linear_rgba(stripe_hex), roughness=0.68)

    # Neck collar ring at Z = 3.98 studs (bmesh direct scale so matrix_world is clean 1,1,1)
    cm = bpy.data.meshes.new(f"{arm_obj.name}_ScarfCollar_M")
    bm = bmesh.new()
    bmesh.ops.create_circle(bm, cap_ends=False, radius=0.64 * STUD, segments=28)
    bpy.ops.mesh.primitive_torus_add(
        major_radius=0.60 * STUD, minor_radius=0.11 * STUD,
        major_segments=28, minor_segments=12,
        location=(0.0, 0.0, 3.96 * STUD)
    )
    bm.free(); bpy.data.meshes.remove(cm)
    collar = bpy.context.active_object
    collar.name = f"{arm_obj.name}_ScarfCollar"
    collar.scale = (1.12, 0.92, 0.85)
    collar.data.materials.append(mat_main)
    for p in collar.data.polygons: p.use_smooth = True

    # Two hanging front scarf tails built cleanly with bmesh (exact stud sizes, no unapplied scale)
    tails = []
    for idx, (tx, ty, tz, sx, sy, sz, rot_y) in enumerate([
        (-0.24, -0.56, 3.30, 0.30, 0.08, 1.25, -5),
        (0.24, -0.58, 3.16, 0.30, 0.08, 1.50, 4),
    ]):
        tm = bpy.data.meshes.new(f"{arm_obj.name}_ScarfTail_{idx}_M")
        tbm = bmesh.new()
        bmesh.ops.create_cube(tbm, size=1.0)
        for v in tbm.verts:
            v.co.x *= sx * STUD
            v.co.y *= sy * STUD
            v.co.z *= sz * STUD
        tbm.to_mesh(tm); tbm.free()
        t_obj = bpy.data.objects.new(f"{arm_obj.name}_ScarfTail_{idx}", tm)
        t_obj.location = (tx * STUD, ty * STUD, tz * STUD)
        t_obj.rotation_euler = Euler((math.radians(-4), math.radians(rot_y), 0))
        t_obj.data.materials.append(mat_main if idx == 0 else mat_stripe)
        bev = t_obj.modifiers.new("Bevel", "BEVEL")
        bev.width = 0.006; bev.segments = 2
        for p in t_obj.data.polygons: p.use_smooth = True
        tails.append(t_obj)

    bpy.context.view_layer.update()
    for ob in [collar] + tails:
        for c in list(ob.users_collection): c.objects.unlink(ob)
        col.objects.link(ob)
        bpy.context.view_layer.update()
        ob.matrix_world = arm_obj.matrix_world @ ob.matrix_world
        wm = ob.matrix_world.copy()
        ob.parent = arm_obj
        ob.matrix_parent_inverse = arm_obj.matrix_world.inverted()
        ob.matrix_world = wm
        vg = ob.vertex_groups.new(name=bone_name)
        vg.add(list(range(len(ob.data.vertices))), 1.0, "REPLACE")
        mod = ob.modifiers.new("Armature", "ARMATURE")
        mod.object = arm_obj
    return [collar] + tails


def set_character_face(char_info: dict, face_png_path: str):
    img = bpy.data.images.load(face_png_path, check_existing=True)
    img.colorspace_settings.name = "sRGB"
    char_info["face_tex_node"].image = img


def load_face_pack(faces_dir: str) -> dict:
    """Preload all PNG faces in faces_dir as sRGB Blender Image datablocks keyed by stem."""
    pack = {}
    if not os.path.isdir(faces_dir):
        return pack
    for fname in sorted(os.listdir(faces_dir)):
        if fname.lower().endswith(".png"):
            stem = os.path.splitext(fname)[0]
            img = bpy.data.images.load(os.path.join(faces_dir, fname), check_existing=True)
            img.colorspace_settings.name = "sRGB"
            pack[stem] = img
    return pack


def ensure_character_face_pack(
    out_dir: str,
    archetype: str = "boy_youth",
    iris_dark: str = "#20569E",
    iris_lite: str = "#52AEF5",
    brow_hex: str = "#18141C",
    lip_hex: str = None,
    mark: str = "none",
    face_style: str = None,
) -> str:
    """
    Generate/return a 20-face Expressive Cartoon or 1930s Rubberhose pack via make_faces_expressive.
    Default replaces legacy anime faces: dramatic/youth -> 'cartoon', comedic/meme/sigma/boomer -> 'rubberhose'.
    """
    if face_style is None:
        face_style = "rubberhose" if archetype in ("meme_sigma", "derp_goofy", "chill_smug", "slapstick_toon", "grumpy_boomer") else "cartoon"
    if not os.path.exists(os.path.join(out_dir, "silly_tongue.png")):
        import make_faces_expressive as mfe
        mfe.generate_pack(out_dir, style=face_style)
    return out_dir


def build_lipsync_schedule(
    words_json_path: str,
    total_frames: int,
    fps: int = 30,
    base_expr: str = "happy",
    emotion_overrides: list = None,
    blink_interval_frames: int = 105,
) -> list:
    """
    Build a 1-indexed frame list of expression keys syncing 3 mouth shapes
    (smile_closed / talk_mid / talk_open) to words.json syllable weight & punctuation,
    plus periodic blinks and emotion overrides.
    emotion_overrides: optional list of (start_frame, end_frame, expr_name, lip_sync_bool).
    """
    word_map = {}
    if words_json_path and os.path.exists(words_json_path):
        data = json.load(open(words_json_path, encoding="utf-8"))
        words = data.get("words") or [w for s in data.get("segments", []) for w in s.get("words", [])]
        for w in words:
            tok = str(w.get("word", "")).strip()
            clean = "".join(ch for ch in tok if ch.isalnum())
            fs = max(1, int(round(float(w["start"]) * fps)))
            fe = min(total_frames, int(round(float(w["end"]) * fps)))
            emph = 2 if (tok.endswith(("!", "?")) or len(clean) >= 6) else (1 if len(clean) >= 3 else 0)
            for fr in range(fs, fe + 1):
                rel = (fr - fs) / float(max(1, fe - fs))
                word_map[fr] = (emph, rel)

    overrides = emotion_overrides or []
    sched = [base_expr] * (total_frames + 1)
    for fr in range(1, total_frames + 1):
        expr, allow_lip = base_expr, True
        for s_f, e_f, ov_name, ov_lip in overrides:
            if s_f <= fr <= e_f:
                expr, allow_lip = ov_name, ov_lip
                break
        if allow_lip and fr in word_map:
            emph, rel = word_map[fr]
            if emph == 2:
                # Stressed / exclamatory word: strong open core (0.20..0.72), mid edges
                expr = "talk_open" if (0.18 <= rel <= 0.72) else ("talk_mid" if rel < 0.90 else "smile_closed")
            elif emph == 1:
                # Normal word: crisp mid -> open -> mid -> close envelope
                expr = "talk_open" if (0.28 <= rel <= 0.62) else ("talk_mid" if rel < 0.86 else "smile_closed")
            else:
                # Short particle/conjunction
                expr = "talk_mid" if rel <= 0.72 else "smile_closed"
        elif blink_interval_frames > 0 and (fr % blink_interval_frames) in (0, 1, 2):
            if expr in ("neutral", "happy", "smile_closed"):
                expr = "blink"
        sched[fr] = expr
    return sched


def make_wet_pbr_ground(name="WetGround_PBR", dark_hex="#1E120A", light_hex="#4A2F1B", scale=3.2, bump_strength=0.32):
    """Create procedural glossy wet PBR ground shader with puddle roughness variation & bump."""
    mat = bpy.data.materials.new(name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    tc = nt.nodes.new("ShaderNodeTexCoord")
    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = scale
    noise.inputs["Detail"].default_value = 8.0
    noise.inputs["Roughness"].default_value = 0.62
    col_ramp = nt.nodes.new("ShaderNodeValToRGB")
    col_ramp.color_ramp.elements[0].position = 0.25
    col_ramp.color_ramp.elements[0].color = hex_to_linear_rgba(dark_hex)
    col_ramp.color_ramp.elements[1].position = 0.78
    col_ramp.color_ramp.elements[1].color = hex_to_linear_rgba(light_hex)
    r_ramp = nt.nodes.new("ShaderNodeValToRGB")
    r_ramp.color_ramp.elements[0].position = 0.35
    r_ramp.color_ramp.elements[0].color = (0.04, 0.04, 0.04, 1.0)
    r_ramp.color_ramp.elements[1].position = 0.75
    r_ramp.color_ramp.elements[1].color = (0.36, 0.36, 0.36, 1.0)
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = bump_strength
    bump.inputs["Distance"].default_value = 0.04
    nt.links.new(tc.outputs["Object"], noise.inputs["Vector"])
    nt.links.new(noise.outputs["Fac"], col_ramp.inputs["Fac"])
    nt.links.new(noise.outputs["Fac"], r_ramp.inputs["Fac"])
    nt.links.new(noise.outputs["Fac"], bump.inputs["Height"])
    nt.links.new(col_ramp.outputs["Color"], bsdf.inputs["Base Color"])
    nt.links.new(r_ramp.outputs["Color"], bsdf.inputs["Roughness"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


# ==============================================================================
# SNAPPY TIMING, BONE PROP TRACKING, PARABOLIC PHYSICS & COLLISION AUDIT
# ==============================================================================

def key_r15_pose(arm_obj, frame: int, loc=None, yaw_deg: float = None, interpolation: str = None, **bones):
    """Keyframe R15 root location/yaw and local XYZ Euler bone rotations cleanly."""
    if loc is not None:
        arm_obj.location = Vector(loc)
        arm_obj.keyframe_insert(data_path="location", frame=frame)
    if yaw_deg is not None:
        arm_obj.rotation_euler = Euler((0.0, 0.0, math.radians(yaw_deg)))
        arm_obj.keyframe_insert(data_path="rotation_euler", frame=frame)
    pb = arm_obj.pose.bones
    for bname, degs in bones.items():
        if bname in pb:
            b = pb[bname]
            b.rotation_mode = "XYZ"
            b.rotation_euler = Euler([math.radians(a) for a in degs])
            b.keyframe_insert(data_path="rotation_euler", frame=frame)
    if interpolation and arm_obj.animation_data and arm_obj.animation_data.action:
        for layer in arm_obj.animation_data.action.layers:
            for strip in layer.strips:
                for cb in strip.channelbags:
                    for fc in cb.fcurves:
                        for kp in fc.keyframe_points:
                            if int(round(kp.co.x)) == frame:
                                kp.interpolation = interpolation


def snap_r15_pose(arm_obj, fs: int, snap_frames: int = 8, overshoot: float = 0.06,
                  loc=None, yaw_deg: float = None, stagger: bool = True,
                  anticipate: bool = False, antic_ratio: float = 0.14, **target_bones):
    """
    Smooth human-weighted pose transition with optional anticipation wind-up + ease-out overshoot.
    Staggers Spine/Legs -> Arms (+2f) -> Head (+3f) for organic human weight.
    """
    d = max(5, snap_frames)
    torso_keys = {k: v for k, v in target_bones.items() if "Torso" in k or "Leg" in k}
    arm_keys = {k: v for k, v in target_bones.items() if "Arm" in k}
    head_keys = {k: v for k, v in target_bones.items() if k == "Head"}

    if anticipate and d >= 7 and fs >= 3:
        antic_bones = {}
        pb = arm_obj.pose.bones
        for bn, degs in target_bones.items():
            if bn in pb:
                cur_deg = tuple(math.degrees(a) for a in pb[bn].rotation_euler)
                antic_bones[bn] = tuple(cur_deg[k] - (degs[k] - cur_deg[k]) * antic_ratio for k in range(3))
        if antic_bones:
            key_r15_pose(arm_obj, fs, **antic_bones)
            fs_eff = fs + 3
            d_eff = max(4, d - 3)
        else:
            fs_eff, d_eff = fs, d
    else:
        fs_eff, d_eff = fs, d

    if not stagger:
        key_r15_pose(arm_obj, fs_eff + d_eff, loc=loc, yaw_deg=yaw_deg, **target_bones)
        return

    # Root & Spine/Legs lead naturally
    key_r15_pose(arm_obj, fs_eff + d_eff, loc=loc, yaw_deg=yaw_deg, **torso_keys)
    # Arms follow 2 frames later with controlled overshoot settle
    if arm_keys:
        if overshoot > 0.01 and d_eff <= 10:
            over_arms = {bn: tuple(a * (1.0 + overshoot) for a in degs) for bn, degs in arm_keys.items()}
            key_r15_pose(arm_obj, fs_eff + max(3, int(round(d_eff * 0.72))) + 1, **over_arms)
        key_r15_pose(arm_obj, fs_eff + d_eff + 2, **arm_keys)
    # Head & gaze settle 3 frames after torso for lifelike overlap
    if head_keys:
        key_r15_pose(arm_obj, fs_eff + d_eff + 3, **head_keys)


def act_r15_sequence(arm_obj, beats: list, breathe: bool = True, breathe_cycle: int = 72, anticipate_fast: bool = True):
    """
    Choreograph natural human acting from asymmetric story beats:
    beats = [(frame, dur, loc, yaw_deg, bones_dict), ...]
    Enforces planted feet (zero Z jitter), staggered Spine->Arm->Head motion,
    automatic wind-up anticipation on dynamic beats, and calm chest breathing.
    """
    for idx, entry in enumerate(beats):
        fr, dur, loc, yaw_deg, bones = entry
        use_antic = anticipate_fast and idx > 0 and dur <= 10
        snap_r15_pose(arm_obj, fr, snap_frames=dur, overshoot=0.06 if dur <= 10 else 0.0,
                      loc=loc, yaw_deg=yaw_deg, stagger=True, anticipate=use_antic, **(bones or {}))
    if breathe and len(beats) >= 2:
        fs_all = beats[0][0]
        fe_all = beats[-1][0] + beats[-1][1] + 6
        span = fe_all - fs_all
        if span >= 40:
            base_ut = beats[0][4].get("UpperTorso", (0, 0, 0)) if beats[0][4] else (0, 0, 0)
            half_c = max(18, breathe_cycle // 2)
            fr = fs_all + half_c
            k = 0
            while fr < fe_all - 10:
                delta = -1.6 if (k % 2 == 0) else 1.2
                if all(abs(fr - b[0]) > 10 and abs(fr - (b[0] + b[1])) > 8 for b in beats):
                    key_r15_pose(arm_obj, fr, UpperTorso=(base_ut[0] + delta, base_ut[1], base_ut[2]))
                fr += half_c
                k += 1


def speak_emphasis_r15(
    char_info: dict,
    words_json_path: str,
    fs: int,
    fe: int,
    fps: int = 30,
    base_pose_name: str = "neutral_relaxed",
    loc=None,
    yaw_deg: float = None,
    energy: float = 1.0,
):
    """
    Drive realistic conversational torso/hand/head acting directly from stressed words
    in words.json inside [fs..fe] (zero static robot freezing during long dialogue!).
    """
    arm_obj = char_info["armature"]
    base = dict(POSE_LIB.get(base_pose_name, POSE_LIB["neutral_relaxed"]))
    accent_frames = []
    if words_json_path and os.path.exists(words_json_path):
        data = json.load(open(words_json_path, encoding="utf-8"))
        words = data.get("words") or []
        t0, t1 = (fs - 1) / float(fps), fe / float(fps)
        in_win = [w for w in words if float(w["end"]) >= t0 and float(w["start"]) <= t1]
        last_fr = fs - 22
        for w in in_win:
            tok = str(w.get("word", "")).strip()
            clean = "".join(ch for ch in tok if ch.isalnum())
            w_fr = max(fs, min(fe - 8, int(round(float(w["start"]) * fps)) + 1))
            is_punct = tok.endswith(("!", "?", ","))
            if (is_punct or len(clean) >= 5) and (w_fr - last_fr) >= 20:
                accent_frames.append((w_fr, is_punct))
                last_fr = w_fr
    if not accent_frames and (fe - fs) >= 26:
        accent_frames = [(fs + 4, False)]

    beats = [(fs, 6, loc, yaw_deg, base)]
    uh = base.get("Head", (0, 0, 0))
    ut = base.get("UpperTorso", (0, 0, 0))
    ra = base.get("RightUpperArm", (-18, 0, -6))
    rl = base.get("RightLowerArm", (-28, 0, 0))
    la = base.get("LeftUpperArm", (-14, 0, 6))
    ll = base.get("LeftLowerArm", (-24, 0, 0))
    patterns = [
        ((5 * energy, 2, 6), (4 * energy, 0, 4), (-32 * energy, 0, -14), (-34, 0, 0), (-12, 0, 8), (-18, 0, 0)),
        ((-3 * energy, -3, -7), (-2, 1, -4), (-14, 0, -8), (-22, 0, 0), (-36 * energy, 0, 14), (-36, 0, 0)),
        ((4 * energy, 4, 2), (5 * energy, 0, 0), (-26 * energy, 0, -20), (-28, 0, 0), (-24 * energy, 0, 18), (-26, 0, 0)),
    ]
    for k, (w_fr, heavy) in enumerate(accent_frames):
        dh, dt, dra, drl, dla, dll = patterns[k % len(patterns)]
        sc = 1.25 if heavy else 1.0
        pose = dict(base)
        pose["Head"] = (uh[0] + dh[0] * sc, uh[1] + dh[1], uh[2] + dh[2])
        pose["UpperTorso"] = (ut[0] + dt[0] * sc, ut[1] + dt[1], ut[2] + dt[2])
        pose["RightUpperArm"] = (ra[0] + dra[0] * sc, ra[1] + dra[1], ra[2] + dra[2])
        pose["RightLowerArm"] = (rl[0] + drl[0], rl[1], rl[2])
        pose["LeftUpperArm"] = (la[0] + dla[0] * sc, la[1] + dla[1], la[2] + dla[2])
        pose["LeftLowerArm"] = (ll[0] + dll[0], ll[1], ll[2])
        beats.append((w_fr, 8, loc, yaw_deg, pose))
    act_r15_sequence(arm_obj, beats, breathe=True, anticipate_fast=False)


def anim_walk_r15_natural(arm_obj, fs: int, fe: int, ps, pe, yaw: float,
                          stride_frames: int = None, amp_leg: float = 34.0, amp_arm: float = 28.0,
                          bob: float = 0.024, fixed_bones: dict = None, stride_m: float = 0.62):
    """
    Natural R15 human gait with ease-in start, distance-calibrated stride_m,
    4-beat knee-bend passing clearance, and clean planted landing settle (zero frozen mid-air feet).
    """
    span = max(1, fe - fs)
    dist_xy = math.hypot(pe[0] - ps[0], pe[1] - ps[1])
    if stride_frames is None:
        cycles = max(1.0, round(dist_xy / max(0.25, stride_m)))
    else:
        cycles = max(1.0, round(span / float(max(8, stride_frames))))
    steps = max(8, int(round(cycles * 8)))
    fixed = dict(fixed_bones or {})
    for i in range(steps + 1):
        t = i / float(steps)
        fr = int(round(fs + t * span))
        # Smooth acceleration & braking velocity curve (75% linear + 25% cosine ease)
        t_pos = 0.75 * t + 0.25 * (0.5 - 0.5 * math.cos(math.pi * t))
        # Smooth ramp up/down at step 0 and final planted landing
        env = min(1.0, t / 0.14) * min(1.0, (1.0 - t) / 0.14) if 0.0 < t < 1.0 else 0.0
        ph = t * cycles * 2.0 * math.pi
        sw = math.sin(ph) * env
        cw = math.cos(ph) * env
        x = ps[0] + (pe[0] - ps[0]) * t_pos
        y = ps[1] + (pe[1] - ps[1]) * t_pos
        z = ps[2] + max(0.0, 1.0 - abs(math.cos(ph))) * bob * env
        pose = {
            "LowerTorso": (3 * env, sw * 2.5, sw * 5.0),
            "UpperTorso": (6 * env, -sw * 2.2, -sw * 6.5),
            "Head": (-4 * env, 0, sw * 2.5),
            "LeftUpperLeg": (sw * amp_leg, 0, 1.5 * env),
            "LeftLowerLeg": (max(0.0, (-sw * 34.0 + (8.0 if cw < 0 else 0.0)) * env), 0, 0),
            "RightUpperLeg": (-sw * amp_leg, 0, -1.5 * env),
            "RightLowerLeg": (max(0.0, (sw * 34.0 + (8.0 if cw > 0 else 0.0)) * env), 0, 0),
            "LeftUpperArm": (-sw * amp_arm - 4.0 * env, 0, 6),
            "LeftLowerArm": (-16.0 - max(0.0, sw * 18.0), 0, 0),
            "RightUpperArm": (sw * amp_arm - 4.0 * env, 0, -6),
            "RightLowerArm": (-16.0 - max(0.0, -sw * 18.0), 0, 0),
        }
        pose.update(fixed)
        key_r15_pose(arm_obj, fr, loc=(x, y, z), yaw_deg=yaw, **pose)


def anim_walk_r15_snappy(arm_obj, fs: int, fe: int, ps, pe, yaw: float,
                         stride_frames: int = 16, amp_leg: float = 36.0, amp_arm: float = 30.0, bob: float = 0.028, fixed_bones: dict = None):
    """Alias to anim_walk_r15_natural with natural grounded biomechanics."""
    anim_walk_r15_natural(arm_obj, fs, fe, ps, pe, yaw, stride_frames=stride_frames,
                          amp_leg=amp_leg, amp_arm=amp_arm, bob=bob, fixed_bones=fixed_bones)


def gesture_beats_r15(arm_obj, fs: int, fe: int, style: str = "talk", tempo: int = 28,
                      loc=None, yaw_deg: float = None, base_bones: dict = None):
    """
    Smooth, non-repetitive human conversational phrasing (NEVER rapid odd/even robot vibration!).
    Plants feet firmly at loc (zero Z bounce) and smoothly shifts torso, arms, and head every ~1.0s.
    """
    base = dict(base_bones or {})
    span = max(1, fe - fs)
    step = max(24, tempo * 2 if tempo < 18 else tempo)
    n_pts = max(1, span // step)
    uh = base.get("Head", (0, 0, 0))
    ut = base.get("UpperTorso", (0, 0, 0))
    ra = base.get("RightUpperArm", (-50, 0, -10))
    la = base.get("LeftUpperArm", (-24, 0, 10))
    beats = []
    # Distinct organic variations instead of A/B metronome shake
    patterns = [
        ((3, 2, 4), (-2, 1, 3), (-10, 0, -2), (-6, 0, 2)),
        ((-2, -3, -5), (1, -1, -2), (6, 0, 2), (-14, 0, 4)),
        ((0, 4, 2), (2, 0, 0), (-6, 0, -4), (4, 0, 0)),
    ]
    for k in range(n_pts + 1):
        fr = min(fe - 6, fs + k * step)
        if fr < fs:
            fr = fs
        dh, dt, dra, dla = patterns[k % len(patterns)]
        pose = dict(base)
        pose["Head"] = (uh[0] + dh[0], uh[1] + dh[1], uh[2] + dh[2])
        pose["UpperTorso"] = (ut[0] + dt[0], ut[1] + dt[1], ut[2] + dt[2])
        pose["RightUpperArm"] = (ra[0] + dra[0], ra[1] + dra[1], ra[2] + dra[2])
        pose["LeftUpperArm"] = (la[0] + dla[0], la[1] + dla[1], la[2] + dla[2])
        beats.append((fr, 11, loc, yaw_deg, pose))
    act_r15_sequence(arm_obj, beats, breathe=False)


def bake_prop_follow(prop_obj, arm_obj, bone_name: str, fs: int, fe: int,
                     local_offset=(0.0, 0.24, -0.05), local_rot_deg=(0.0, 0.0, 0.0),
                     step: int = 1, follow_rot: str = "bone"):
    """
    Physically weld/track a prop to a character's animated R15 bone across [fs..fe].
    follow_rot='bone' inherits full 3D wrist orientation; follow_rot='root' tracks the
    animated hand world position while keeping readable covers upright relative to character yaw.
    """
    scene = bpy.context.scene
    loc_m = Matrix.Translation(Vector(local_offset))
    rot_e = Euler([math.radians(a) for a in local_rot_deg], "XYZ")
    off_m = loc_m @ rot_e.to_matrix().to_4x4()
    for fr in range(fs, fe + 1, max(1, step)):
        scene.frame_set(fr)
        pb = arm_obj.pose.bones.get(bone_name)
        if pb is None:
            continue
        mw = arm_obj.matrix_world @ pb.matrix @ off_m
        prop_obj.location = mw.to_translation()
        if follow_rot == "root":
            r_root = arm_obj.rotation_euler.to_matrix().to_4x4() @ rot_e.to_matrix().to_4x4()
            prop_obj.rotation_euler = r_root.to_euler("XYZ")
        else:
            prop_obj.rotation_euler = mw.to_euler("XYZ")
        prop_obj.keyframe_insert(data_path="location", frame=fr)
        prop_obj.keyframe_insert(data_path="rotation_euler", frame=fr)


def animate_toss_physics(obj, fs: int, fe: int, start_loc, end_loc, arc_height: float = 0.65,
                         start_rot_deg=(0, 0, 0), end_rot_deg=(0, 0, 0)):
    """Animate a realistic parabolic gravity throw arc across [fs..fe]."""
    p0 = Vector(start_loc)
    p1 = Vector(end_loc)
    r0 = Vector(start_rot_deg)
    r1 = Vector(end_rot_deg)
    span = max(1, fe - fs)
    for fr in range(fs, fe + 1):
        t = (fr - fs) / float(span)
        pos = p0.lerp(p1, t)
        pos.z += 4.0 * arc_height * t * (1.0 - t)
        rot = r0.lerp(r1, t)
        obj.location = pos
        obj.rotation_euler = Euler([math.radians(a) for a in rot])
        obj.keyframe_insert(data_path="location", frame=fr)
        obj.keyframe_insert(data_path="rotation_euler", frame=fr)


def animate_drop_physics(obj, fs: int, fe: int, start_loc, start_rot_deg=(0, 0, 0),
                         floor_z: float = 0.08, gravity: float = 20.0, restitution: float = 0.44,
                         lateral_vel=(0.0, 0.0), spin_vel_deg=(240.0, 180.0, 90.0),
                         rest_rot_deg=(90.0, 0.0, 35.0), fps: int = 30) -> dict:
    """
    Simulate real gravity fall + multi-bounce impact + spin damping + flat floor settle across [fs..fe].
    Returns {"impact_frame": first_hit_frame, "end_loc": tuple} so reactions/SFX sync frame-accurately.
    """
    dt = 1.0 / float(fps)
    pos = Vector(start_loc)
    vel = Vector((lateral_vel[0], lateral_vel[1], 0.0))
    rot = Vector(start_rot_deg)
    spin = Vector(spin_vel_deg)
    first_hit = None
    bounces = 0
    settled = False
    for fr in range(fs, fe + 1):
        obj.location = pos
        obj.rotation_euler = Euler([math.radians(a) for a in rot])
        obj.keyframe_insert(data_path="location", frame=fr)
        obj.keyframe_insert(data_path="rotation_euler", frame=fr)
        if settled:
            continue
        vel.z -= gravity * dt
        pos += vel * dt
        rot += spin * dt
        if pos.z <= floor_z:
            pos.z = floor_z
            if first_hit is None:
                first_hit = fr
            bounces += 1
            if abs(vel.z) * restitution < 0.75 or bounces >= 3:
                vel = Vector((0.0, 0.0, 0.0))
                spin = Vector((0.0, 0.0, 0.0))
                rot = Vector(rest_rot_deg)
                settled = True
            else:
                vel.z = abs(vel.z) * restitution
                vel.x *= 0.55
                vel.y *= 0.55
                spin *= 0.35
    return {"impact_frame": first_hit or fs, "end_loc": tuple(pos)}


def _world_aabb(obj, depsgraph):
    ev = obj.evaluated_get(depsgraph)
    if ev.type != "MESH" or not ev.data or len(ev.bound_box) < 8:
        return None
    pts = [ev.matrix_world @ Vector(c) for c in ev.bound_box]
    xs = [p.x for p in pts]; ys = [p.y for p in pts]; zs = [p.z for p in pts]
    return (min(xs), max(xs), min(ys), max(ys), min(zs), max(zs))


def _aabb_overlap_depth(a, b, margin=0.0):
    ax0, ax1, ay0, ay1, az0, az1 = a
    bx0, bx1, by0, by1, bz0, bz1 = b
    ox = min(ax1 - margin, bx1 - margin) - max(ax0 + margin, bx0 + margin)
    oy = min(ay1 - margin, by1 - margin) - max(ay0 + margin, by0 + margin)
    oz = min(az1 - margin, bz1 - margin) - max(az0 + margin, bz0 + margin)
    if ox > 0 and oy > 0 and oz > 0:
        return min(ox, oy, oz)
    return 0.0


def audit_scene_collisions(char_infos: list, obstacles: list = None, frames: list = None,
                           min_char_sep: float = 0.76, margin: float = 0.035) -> list:
    """
    Evaluate deformed Blender mesh AABBs across sample frames to catch character-vs-character
    or character-vs-obstacle interpenetration BEFORE full rendering!
    Returns a list of collision dicts (empty list = 100% clean).
    """
    scene = bpy.context.scene
    frames = frames or [scene.frame_start]
    obstacles = obstacles or []
    violations = []
    torso_suffixes = ("_LowerTorso", "_UpperTorso", "_Torso", "_Head")

    for fr in frames:
        scene.frame_set(fr)
        dg = bpy.context.evaluated_depsgraph_get()
        # 1. Character vs Character root torso/head clearance & AABB overlap
        char_boxes = []
        for ci in char_infos:
            arm = ci["armature"]
            if arm.location.z < -0.5:
                continue  # intentionally hidden offstage
            boxes = []
            for child in arm.children:
                if child.type == "MESH" and any(child.name.endswith(s) for s in torso_suffixes):
                    bb = _world_aabb(child, dg)
                    if bb:
                        boxes.append((child.name, bb))
            char_boxes.append((arm.name, arm.location.copy(), boxes))

        for i in range(len(char_boxes)):
            n_a, loc_a, b_a = char_boxes[i]
            for j in range(i + 1, len(char_boxes)):
                n_b, loc_b, b_b = char_boxes[j]
                if (loc_a - loc_b).length > 3.0:
                    continue
                d_xy = math.hypot(loc_a.x - loc_b.x, loc_a.y - loc_b.y)
                d_z = abs(loc_a.z - loc_b.z)
                if d_xy < min_char_sep and d_z < 1.1:
                    for ma, ba in b_a:
                        for mb, bb in b_b:
                            ov = _aabb_overlap_depth(ba, bb, margin=margin)
                            if ov > 0.015:
                                violations.append({"frame": fr, "type": "CHAR_CHAR", "a": ma, "b": mb, "depth_m": round(ov, 3)})

        # 2. Character torso/legs vs Static Obstacles (fences, signs, props, LEGO bricks)
        obs_boxes = []
        for ob in obstacles:
            bb = _world_aabb(ob, dg)
            if bb and bb[5] > -0.3:
                obs_boxes.append((ob.name, bb))
        ignore_tags = ("Hair", "Bulb", "Hat", "Chef", "Rim", "Temple", "Bridge", "Mustache", "Pack", "Bow", "Cap", "Scarf")
        for n_a, loc_a, _ in char_boxes:
            arm = bpy.data.objects.get(n_a)
            for child in arm.children:
                if child.type == "MESH" and not any(t in child.name for t in ignore_tags):
                    ba = _world_aabb(child, dg)
                    if not ba:
                        continue
                    for oname, bb in obs_boxes:
                        ov = _aabb_overlap_depth(ba, bb, margin=margin)
                        if ov > 0.03:
                            violations.append({"frame": fr, "type": "CHAR_OBSTACLE", "a": child.name, "b": oname, "depth_m": round(ov, 3)})
    return violations


# ==============================================================================
# NATURAL POSE LIBRARY, CORE TARGET-FIRST CAMERA ENGINE & PLAYBLAST MOTION QA
# ==============================================================================

POSE_LIB = {
    "neutral_relaxed": {
        "LowerTorso": (0, 0, 0), "UpperTorso": (2, 0, 0), "Head": (-2, 0, 0),
        "RightUpperArm": (-8, 0, -6), "RightLowerArm": (-18, 0, 0),
        "LeftUpperArm": (-6, 0, 6), "LeftLowerArm": (-16, 0, 0),
        "LeftUpperLeg": (0, 0, 0), "LeftLowerLeg": (0, 0, 0), "RightUpperLeg": (0, 0, 0), "RightLowerLeg": (0, 0, 0),
    },
    "hands_on_hips": {
        "LowerTorso": (0, 0, 0), "UpperTorso": (-5, 0, 0), "Head": (-3, 0, 0),
        "RightUpperArm": (-16, 0, -28), "RightLowerArm": (-68, -20, 0),
        "LeftUpperArm": (-16, 0, 28), "LeftLowerArm": (-68, 20, 0),
        "LeftUpperLeg": (0, 0, 0), "LeftLowerLeg": (0, 0, 0), "RightUpperLeg": (0, 0, 0), "RightLowerLeg": (0, 0, 0),
    },
    "cross_arms": {
        "LowerTorso": (0, 0, 0), "UpperTorso": (-4, 0, 0), "Head": (-2, 0, 4),
        "RightUpperArm": (-38, 0, 16), "RightLowerArm": (-82, 32, 0),
        "LeftUpperArm": (-42, 0, -16), "LeftLowerArm": (-78, -32, 0),
    },
    "point_casual": {
        "UpperTorso": (6, 0, -6), "Head": (-2, 0, 6),
        "RightUpperArm": (-78, 0, -12), "RightLowerArm": (-16, 0, 0),
        "LeftUpperArm": (-12, 0, 8), "LeftLowerArm": (-24, 0, 0),
    },
    "scratch_head": {
        "UpperTorso": (4, 0, 5), "Head": (6, 0, -8),
        "RightUpperArm": (-135, 0, 12), "RightLowerArm": (-95, 0, 0),
        "LeftUpperArm": (-10, 0, 8), "LeftLowerArm": (-22, 0, 0),
    },
    "chin_think": {
        "UpperTorso": (3, 0, -4), "Head": (8, 0, 6),
        "RightUpperArm": (-56, 0, 18), "RightLowerArm": (-92, 0, 0),
        "LeftUpperArm": (-16, 0, -12), "LeftLowerArm": (-64, 0, 0),
    },
    "lean_inspect": {
        "LowerTorso": (12, 0, 0), "UpperTorso": (16, 0, 0), "Head": (12, 0, 0),
        "RightUpperArm": (-48, 0, -10), "RightLowerArm": (-34, 0, 0),
        "LeftUpperArm": (-40, 0, 10), "LeftLowerArm": (-36, 0, 0),
    },
    "recoil_shock": {
        "LowerTorso": (-6, 0, 0), "UpperTorso": (-12, 0, 0), "Head": (-18, 0, 0),
        "RightUpperArm": (-105, 0, -24), "RightLowerArm": (-58, 0, 0),
        "LeftUpperArm": (-105, 0, 24), "LeftLowerArm": (-58, 0, 0),
    },
    "shrug_open": {
        "UpperTorso": (-4, 0, 0), "Head": (-4, 0, 8),
        "RightUpperArm": (-46, 0, -28), "RightLowerArm": (-52, 0, 0),
        "LeftUpperArm": (-46, 0, 28), "LeftLowerArm": (-52, 0, 0),
    },
}


def apply_pose_lib(char_info: dict, frame: int, pose_name: str, dur: int = 10, loc=None, yaw_deg: float = None, **overrides):
    """Transition smoothly using a curated POSE_LIB entry with staggered Torso->Arm->Head overlap."""
    pose = dict(POSE_LIB.get(pose_name, POSE_LIB["neutral_relaxed"]))
    pose.update(overrides)
    snap_r15_pose(char_info["armature"], frame, snap_frames=dur, loc=loc, yaw_deg=yaw_deg, stagger=True, **pose)


SHOT_PRESETS = {
    "EWS":    {"lens": 24.0, "dist": 6.5, "dof_f": 8.0},
    "WS":     {"lens": 26.0, "dist": 4.2, "dof_f": 5.6},
    "MS":     {"lens": 36.0, "dist": 2.4, "dof_f": 4.5},
    "OTS":    {"lens": 40.0, "dist": 1.85, "dof_f": 3.5},
    "MCU":    {"lens": 48.0, "dist": 1.45, "dof_f": 3.2},
    "CU":     {"lens": 58.0, "dist": 0.98, "dof_f": 2.8},
    "INSERT": {"lens": 52.0, "dist": 0.85, "dof_f": 2.8},
}


def _cam_aim(cam, fr: int, pos: Vector, tgt: Vector, lens: float, roll_deg: float, focus_dist: float, fstop: float):
    cam.location = pos
    e = (tgt - pos).to_track_quat("-Z", "Y").to_euler()
    e.rotate_axis("Z", math.radians(roll_deg))
    cam.rotation_euler = e
    cam.data.lens = lens
    cam.data.dof.use_dof = True
    cam.data.dof.focus_distance = focus_dist
    cam.data.dof.aperture_fstop = fstop
    cam.keyframe_insert(data_path="location", frame=fr)
    cam.keyframe_insert(data_path="rotation_euler", frame=fr)
    cam.data.keyframe_insert(data_path="lens", frame=fr)
    cam.data.dof.keyframe_insert(data_path="focus_distance", frame=fr)


def place_shot_camera(
    cam,
    fs: int,
    fe: int,
    target,
    scale: str = "MCU",
    angle: str = "eye",
    over=None,
    axis_side: int = 1,
    yaw_offset_deg: float = 18.0,
    move: str = "push_in",
    move_amt: float = 0.08,
    caption_safe: bool = True,
    shot_log: list = None,
):
    """
    Core Target-First Camera Rig enforcing Sven Core Cinema Rules:
    - Places OTS/Reverse-OTS strictly on one side of the 180-deg axis (`axis_side`=+1/-1).
    - Calibrates lens per Shot Scale (`58mm CU`, `48mm MCU`, `26mm WS`) to prevent blocky head distortion.
    - Applies Caption-Safe framing so faces sit cleanly above y=55% in 9:16.
    - Supports real 3D camera moves (`static`, `push_in`, `pull_out`, `truck`, `dolly_zoom`).
    - Sets CONSTANT interpolation on cut end frame `fe`.
    """
    spec = SHOT_PRESETS.get(scale.upper(), SHOT_PRESETS["MCU"])
    lens1 = spec["lens"]
    dist = spec["dist"]
    fstop = spec["dof_f"]

    # Resolve target 3D point & eye height
    if isinstance(target, dict) and "armature" in target:
        arm = target["armature"]
        bpy.context.scene.frame_set(fs)
        t_loc = arm.matrix_world.translation.copy()
        eye_z = t_loc.z + target["metrics"]["eye_z"]
        fwd_local = arm.rotation_euler.to_matrix() @ Vector((0.0, -1.0, 0.0))
    else:
        t_loc = Vector(target)
        eye_z = t_loc.z
        fwd_local = Vector((0.0, -1.0, 0.0))

    # Compute camera approach vector
    if scale.upper() == "OTS" and over is not None and isinstance(over, dict):
        o_loc = over["armature"].matrix_world.translation.copy()
        line_vec = (t_loc - o_loc)
        line_vec.z = 0.0
        if line_vec.length < 1e-3:
            line_vec = Vector((1.0, 0.0, 0.0))
        line_dir = line_vec.normalized()
        # Keep camera strictly on one half-plane of the 180-deg line across A->B and B->A!
        perp = Vector((line_dir.y, -line_dir.x, 0.0))
        if perp.y > 0.0:
            perp = -perp
        perp *= axis_side
        o_eye_z = o_loc.z + over["metrics"]["eye_z"]
        cam_base = Vector((o_loc.x, o_loc.y, o_eye_z - 0.04)) - line_dir * 0.92 + perp * 0.68
        focus_d = (Vector((t_loc.x, t_loc.y, eye_z)) - cam_base).length
    else:
        ang_rad = math.radians(yaw_offset_deg * axis_side)
        c_dir = Vector((fwd_local.x * math.cos(ang_rad) - fwd_local.y * math.sin(ang_rad),
                        fwd_local.x * math.sin(ang_rad) + fwd_local.y * math.cos(ang_rad), 0.0)).normalized()
        cam_base = Vector((t_loc.x, t_loc.y, eye_z)) + c_dir * dist
        focus_d = dist

    # 4-Axis vertical angle & dutch roll
    pitch_z = 0.0; roll = 0.0
    if angle == "low":
        pitch_z = -0.36 * min(1.8, dist * 0.45)
    elif angle == "high":
        pitch_z = +0.62 * min(2.2, dist * 0.48)
    elif angle == "dutch":
        roll = 4.5 * axis_side

    res_x = max(1, bpy.context.scene.render.resolution_x)
    res_y = max(1, bpy.context.scene.render.resolution_y)
    vfov_tan = (18.0 / lens1) * (res_y / float(res_x))
    cap_off_z = -0.10 * focus_d * vfov_tan if (caption_safe and res_y > res_x and scale.upper() in ("MCU", "CU", "OTS", "MS")) else 0.0

    pos1 = Vector((cam_base.x, cam_base.y, eye_z + pitch_z))
    tgt1 = Vector((t_loc.x, t_loc.y, eye_z + cap_off_z))
    fwd_cam = (tgt1 - pos1).normalized()
    right_cam = fwd_cam.cross(Vector((0.0, 0.0, 1.0))).normalized()

    pos2 = pos1.copy(); tgt2 = tgt1.copy(); lens2 = lens1; focus2 = focus_d
    handled_arc = False
    if move == "push_in":
        pos2 = pos1 + fwd_cam * (focus_d * move_amt)
        focus2 = max(0.3, (tgt2 - pos2).length)
    elif move == "pull_out":
        pos2 = pos1 - fwd_cam * (focus_d * move_amt)
        focus2 = (tgt2 - pos2).length
    elif move == "truck":
        shift = right_cam * (focus_d * move_amt * 1.4 * axis_side)
        pos2 = pos1 + shift
        tgt2 = tgt1 + shift * 0.65
        focus2 = (tgt2 - pos2).length
    elif move == "crane_up":
        pos2 = pos1 + Vector((0.0, 0.0, max(0.28, focus_d * move_amt * 1.6)))
        focus2 = (tgt2 - pos2).length
    elif move == "crane_down":
        pos2 = pos1 - Vector((0.0, 0.0, max(0.22, focus_d * move_amt * 1.3)))
        focus2 = (tgt2 - pos2).length
    elif move == "orbit_arc":
        handled_arc = True
        arc_deg = 22.0 * max(0.4, move_amt * 10.0) * axis_side
        off0 = pos1 - tgt1
        steps_arc = max(4, min(10, (fe - fs) // 10))
        for si in range(steps_arc + 1):
            tk = si / float(steps_arc)
            fk = int(round(fs + tk * (fe - fs)))
            ang = math.radians(arc_deg * (0.5 - 0.5 * math.cos(math.pi * tk)))
            ca, sa = math.cos(ang), math.sin(ang)
            o_rot = Vector((off0.x * ca - off0.y * sa, off0.x * sa + off0.y * ca, off0.z))
            pk = tgt1 + o_rot
            _cam_aim(cam, fk, pk, tgt1, lens1, roll, o_rot.length, fstop)
    elif move == "dolly_zoom":
        scale_f = 1.48
        pos2 = tgt1 - (tgt1 - pos1) * scale_f
        lens2 = lens1 * scale_f
        focus2 = (tgt2 - pos2).length

    if not handled_arc:
        _cam_aim(cam, fs, pos1, tgt1, lens1, roll, focus_d, fstop)
        _cam_aim(cam, fe, pos2, tgt2, lens2, roll, focus2, fstop)

    for ad in (cam.animation_data, cam.data.animation_data):
        if ad and ad.action:
            for layer in ad.action.layers:
                for strip in layer.strips:
                    for cb in strip.channelbags:
                        for fc in cb.fcurves:
                            for kp in fc.keyframe_points:
                                kfr = int(round(kp.co.x))
                                if kfr == fe:
                                    kp.interpolation = "CONSTANT"
                                elif kfr == fs and move in ("push_in", "pull_out", "dolly_zoom"):
                                    kp.handle_left_type = "FREE"
                                    kp.handle_right_type = "AUTO_CLAMPED"

    if shot_log is not None:
        shot_log.append({
            "fs": fs, "fe": fe, "dur": round((fe - fs + 1) / 30.0, 2),
            "scale": scale.upper(), "angle": angle, "move": move, "lens": lens1,
        })
    return pos1, tgt1


def add_camera_shake(cam, impact_frame: int, amp_m: float = 0.042, amp_deg: float = 1.5, dur_frames: int = 12):
    """Add decaying damped physical impact trauma shake on a camera without breaking cut boundaries."""
    sc = bpy.context.scene
    for k in range(dur_frames + 1):
        fr = impact_frame + k
        if fr < sc.frame_start or fr > sc.frame_end:
            continue
        sc.frame_set(fr)
        t = k / float(max(1, dur_frames))
        decay = (1.0 - t) ** 1.8
        loc = cam.location.copy()
        rot = cam.rotation_euler.copy()
        if k < dur_frames:
            sx = math.sin(k * 2.45) * amp_m * decay
            sz = math.cos(k * 3.10) * amp_m * 0.85 * decay
            sr = math.radians(math.sin(k * 2.8) * amp_deg * decay)
            cam.location = Vector((loc.x + sx, loc.y, loc.z + sz))
            cam.rotation_euler = Euler((rot.x + sr * 0.4, rot.y + sr, rot.z))
        cam.keyframe_insert("location", frame=fr)
        cam.keyframe_insert("rotation_euler", frame=fr)


def audit_camera_plan(shot_log: list) -> dict:
    """Audit camera sequence against Sven Core look.md thresholds."""
    n = max(1, len(shot_log))
    close_n = sum(1 for s in shot_log if s["scale"] in ("CU", "MCU", "INSERT"))
    ms_n = sum(1 for s in shot_log if s["scale"] in ("MS", "OTS"))
    non_eye_n = sum(1 for s in shot_log if s["angle"] != "eye")
    move_n = sum(1 for s in shot_log if s["move"] != "static")
    same_adj = sum(1 for i in range(1, len(shot_log)) if shot_log[i]["scale"] == shot_log[i - 1]["scale"] and shot_log[i]["angle"] == shot_log[i - 1]["angle"])
    return {
        "shots": len(shot_log),
        "close_pct": round(100.0 * close_n / n, 1),
        "ms_pct": round(100.0 * ms_n / n, 1),
        "non_eye_pct": round(100.0 * non_eye_n / n, 1),
        "move_pct": round(100.0 * move_n / n, 1),
        "adjacent_repeat_warnings": same_adj,
    }


def render_playblast_qa(stage_dir: str, fps_step: int = 3, res_scale: float = 0.5, samples: int = 4) -> str:
    """
    Fast low-sample motion playblast (~10 fps @ half resolution) so agents and users
    can verify motion speed, foot-lock, and zero jitter before full 30fps GPU rendering.
    """
    sc = bpy.context.scene
    old_rx, old_ry, old_pct = sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage
    old_samp = sc.eevee.taa_render_samples if hasattr(sc, "eevee") and hasattr(sc.eevee, "taa_render_samples") else None
    sc.render.resolution_percentage = int(round(res_scale * 100))
    if old_samp is not None:
        sc.eevee.taa_render_samples = samples
    pb_dir = os.path.join(stage_dir, "playblast_frames")
    shutil.rmtree(pb_dir, ignore_errors=True)
    os.makedirs(pb_dir, exist_ok=True)
    idx = 1
    for fr in range(sc.frame_start, sc.frame_end + 1, max(1, fps_step)):
        sc.frame_set(fr)
        sc.render.filepath = os.path.join(pb_dir, f"{idx:04d}.png")
        bpy.ops.render.render(write_still=True)
        idx += 1
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = old_rx, old_ry, old_pct
    if old_samp is not None:
        sc.eevee.taa_render_samples = old_samp
    return pb_dir



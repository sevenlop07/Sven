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
CORE_CLOTHES_DIR = os.path.join(CORE_ASSETS_DIR, "clothes")
CORE_FACES_CINEMA_DIR = os.path.join(CORE_ASSETS_DIR, "faces_cinema_expressive")
CORE_FACES_STORYBOOK_DIR = os.path.join(CORE_ASSETS_DIR, "faces_storybook_toon")
CORE_FACES_UGC_DIR = CORE_FACES_CINEMA_DIR  # default alias -> cinema_expressive for CGI Cinema
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


def pack_all_textures():
    """Pack all external image textures into the current .blend so it is 100% portable across Windows/Linux/Cloud."""
    for img in bpy.data.images:
        if img.filepath and not img.packed_file:
            try:
                if os.path.exists(bpy.path.abspath(img.filepath)) or os.path.exists(img.filepath):
                    img.pack()
            except Exception:
                pass


def iter_action_fcurves(action):
    """Yield all F-Curves from a Blender 5.3 Slotted Action (or legacy Action) without version conflicts."""
    if not action:
        return
    if hasattr(action, "layers") and action.layers:
        for layer in action.layers:
            for strip in getattr(layer, "strips", []):
                for cb in getattr(strip, "channelbags", []):
                    for fc in getattr(cb, "fcurves", []):
                        yield fc
    for fc in getattr(action, "fcurves", []):
        yield fc


def temp_save_blend(final_blend_path: str):
    pack_all_textures()
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
    mat.diffuse_color = linear_rgba
    return mat


CLOTH_FABRIC_PROFILES = {
    "default": {"rough": 0.54, "sheen": 0.12, "sheen_r": 0.55, "coat": 0.00, "coat_r": 0.25, "bump": 0.09, "bump_d": 0.008},
    "puffer":  {"rough": 0.30, "sheen": 0.00, "sheen_r": 0.50, "coat": 0.45, "coat_r": 0.22, "bump": 0.16, "bump_d": 0.012},
    "wool":    {"rough": 0.88, "sheen": 0.78, "sheen_r": 0.45, "coat": 0.00, "coat_r": 0.30, "bump": 0.22, "bump_d": 0.010},
    "coat":    {"rough": 0.72, "sheen": 0.28, "sheen_r": 0.55, "coat": 0.00, "coat_r": 0.30, "bump": 0.14, "bump_d": 0.010},
    "denim":   {"rough": 0.80, "sheen": 0.22, "sheen_r": 0.60, "coat": 0.00, "coat_r": 0.30, "bump": 0.16, "bump_d": 0.009},
}


def make_wool_mat(name, linear_rgba, roughness=0.88, sheen=0.80):
    """Soft fuzzy wool/fleece material with Blender 5.3 Sheen edge-glow and subtle weave bump."""
    mat = bpy.data.materials.new(name=name)
    mat.diffuse_color = linear_rgba
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = linear_rgba
    bsdf.inputs["Roughness"].default_value = roughness
    if "Sheen Weight" in bsdf.inputs:
        bsdf.inputs["Sheen Weight"].default_value = sheen
    if "Sheen Roughness" in bsdf.inputs:
        bsdf.inputs["Sheen Roughness"].default_value = 0.46
    tc = nt.nodes.new("ShaderNodeTexCoord")
    ns = nt.nodes.new("ShaderNodeTexNoise")
    ns.inputs["Scale"].default_value = 38.0
    ns.inputs["Detail"].default_value = 6.0
    nt.links.new(tc.outputs["Object"], ns.inputs["Vector"])
    bp = nt.nodes.new("ShaderNodeBump")
    bp.inputs["Strength"].default_value = 0.16
    bp.inputs["Distance"].default_value = 0.006
    nt.links.new(ns.outputs["Fac"], bp.inputs["Height"])
    nt.links.new(bp.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_skin_cloth_mat(name, skin_rgba, cloth_img_path, fabric: str = "default", ao_strength: float = 0.18):
    """
    Micro-PBR Roblox skin + classic clothing shader:
    - Separates bare skin (satin vinyl + subtle SSS) from cloth via PNG Alpha mask
    - Applies fabric-specific Roughness, Sheen (wool/coat), Coat (puffer/raincoat), and micro-Bump
    - Multiplies subtle cavity Ambient Occlusion into Base Color to ground collars, underarms & accessories.
    """
    prof = CLOTH_FABRIC_PROFILES.get(fabric, CLOTH_FABRIC_PROFILES["default"])
    mat = bpy.data.materials.new(name=name)
    mat.diffuse_color = skin_rgba
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    if "Sheen Roughness" in bsdf.inputs:
        bsdf.inputs["Sheen Roughness"].default_value = prof["sheen_r"]
    if "Coat Roughness" in bsdf.inputs:
        bsdf.inputs["Coat Roughness"].default_value = prof["coat_r"]

    tex = nt.nodes.new("ShaderNodeTexImage")
    img = bpy.data.images.load(cloth_img_path, check_existing=True)
    img.colorspace_settings.name = "sRGB"
    if not img.packed_file:
        try:
            img.pack()
        except Exception:
            pass
    tex.image = img
    tex.extension = "CLIP"

    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.inputs[6].default_value = skin_rgba
    nt.links.new(tex.outputs["Alpha"], mix.inputs[0])
    nt.links.new(tex.outputs["Color"], mix.inputs[7])

    # Subtle cavity AO darkening around neck, underarms & accessory seams
    if ao_strength > 0.001:
        ao = nt.nodes.new("ShaderNodeAmbientOcclusion")
        ao.samples = 8
        ao.inputs["Distance"].default_value = 0.10
        nt.links.new(mix.outputs[2], ao.inputs["Color"])
        mix_ao = nt.nodes.new("ShaderNodeMix")
        mix_ao.data_type = "RGBA"
        mix_ao.blend_type = "MULTIPLY"
        mix_ao.inputs[0].default_value = ao_strength
        nt.links.new(mix.outputs[2], mix_ao.inputs[6])
        nt.links.new(ao.outputs["AO"], mix_ao.inputs[7])
        nt.links.new(mix_ao.outputs[2], bsdf.inputs["Base Color"])
    else:
        nt.links.new(mix.outputs[2], bsdf.inputs["Base Color"])

    # Alpha-driven Roughness: bare skin (0.40) vs fabric profile roughness
    mr = nt.nodes.new("ShaderNodeMix")
    mr.data_type = "FLOAT"
    mr.inputs[2].default_value = 0.40
    mr.inputs[3].default_value = prof["rough"]
    nt.links.new(tex.outputs["Alpha"], mr.inputs[0])
    nt.links.new(mr.outputs[0], bsdf.inputs["Roughness"])

    # Alpha-driven Sheen & Coat (only on cloth, never on bare skin)
    if "Sheen Weight" in bsdf.inputs and prof["sheen"] > 0.001:
        ms = nt.nodes.new("ShaderNodeMix")
        ms.data_type = "FLOAT"
        ms.inputs[2].default_value = 0.0
        ms.inputs[3].default_value = prof["sheen"]
        nt.links.new(tex.outputs["Alpha"], ms.inputs[0])
        nt.links.new(ms.outputs[0], bsdf.inputs["Sheen Weight"])
    if "Coat Weight" in bsdf.inputs and prof["coat"] > 0.001:
        mc = nt.nodes.new("ShaderNodeMix")
        mc.data_type = "FLOAT"
        mc.inputs[2].default_value = 0.06
        mc.inputs[3].default_value = prof["coat"]
        nt.links.new(tex.outputs["Alpha"], mc.inputs[0])
        nt.links.new(mc.outputs[0], bsdf.inputs["Coat Weight"])
    if "Subsurface Weight" in bsdf.inputs:
        m_sss = nt.nodes.new("ShaderNodeMix")
        m_sss.data_type = "FLOAT"
        m_sss.inputs[2].default_value = 0.08
        m_sss.inputs[3].default_value = 0.0
        nt.links.new(tex.outputs["Alpha"], m_sss.inputs[0])
        nt.links.new(m_sss.outputs[0], bsdf.inputs["Subsurface Weight"])

    # Micro-Bump from cloth texture luminance (masked by Alpha so bare skin stays smooth)
    if prof["bump"] > 0.001:
        bw = nt.nodes.new("ShaderNodeRGBToBW")
        nt.links.new(tex.outputs["Color"], bw.inputs["Color"])
        mul_b = nt.nodes.new("ShaderNodeMath")
        mul_b.operation = "MULTIPLY"
        nt.links.new(bw.outputs["Val"], mul_b.inputs[0])
        nt.links.new(tex.outputs["Alpha"], mul_b.inputs[1])
        bp = nt.nodes.new("ShaderNodeBump")
        bp.inputs["Strength"].default_value = prof["bump"]
        bp.inputs["Distance"].default_value = prof["bump_d"]
        nt.links.new(mul_b.outputs["Value"], bp.inputs["Height"])
        nt.links.new(bp.outputs["Normal"], bsdf.inputs["Normal"])

    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_head_face_mat(name, skin_rgba, face_png_path, skin_sss: float = 0.10, face_roughness: float = 0.74, ao_strength: float = 0.15):
    """
    Stylized Vinyl/Art-Toy Roblox head shader with Anti-Glare 2D Face Decal protection:
    - Bare skin gets warm satin finish + subtle Subsurface Scattering + cavity AO under hair/chin
    - Drawn face area (Alpha=1) locks high Roughness & low Specular so bright Key/Sun lights NEVER glare over cartoon eyes.
    """
    mat = bpy.data.materials.new(name=name)
    mat.diffuse_color = skin_rgba
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")

    tex = nt.nodes.new("ShaderNodeTexImage")
    img = bpy.data.images.load(face_png_path, check_existing=True)
    img.colorspace_settings.name = "sRGB"
    if not img.packed_file:
        try:
            img.pack()
        except Exception:
            pass
    tex.image = img
    tex.extension = "CLIP"

    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.inputs[6].default_value = skin_rgba
    nt.links.new(tex.outputs["Alpha"], mix.inputs[0])
    nt.links.new(tex.outputs["Color"], mix.inputs[7])

    if ao_strength > 0.001:
        ao = nt.nodes.new("ShaderNodeAmbientOcclusion")
        ao.samples = 8
        ao.inputs["Distance"].default_value = 0.08
        mix_ao = nt.nodes.new("ShaderNodeMix")
        mix_ao.data_type = "RGBA"
        mix_ao.blend_type = "MULTIPLY"
        mix_ao.inputs[0].default_value = ao_strength
        nt.links.new(mix.outputs[2], mix_ao.inputs[6])
        nt.links.new(ao.outputs["AO"], mix_ao.inputs[7])
        nt.links.new(mix_ao.outputs[2], bsdf.inputs["Base Color"])
    else:
        nt.links.new(mix.outputs[2], bsdf.inputs["Base Color"])

    # Anti-Glare Roughness & Specular mask driven by face PNG Alpha
    mr = nt.nodes.new("ShaderNodeMix")
    mr.data_type = "FLOAT"
    mr.inputs[2].default_value = 0.40
    mr.inputs[3].default_value = face_roughness
    nt.links.new(tex.outputs["Alpha"], mr.inputs[0])
    nt.links.new(mr.outputs[0], bsdf.inputs["Roughness"])

    if "Specular IOR Level" in bsdf.inputs:
        msp = nt.nodes.new("ShaderNodeMix")
        msp.data_type = "FLOAT"
        msp.inputs[2].default_value = 0.46
        msp.inputs[3].default_value = 0.14
        nt.links.new(tex.outputs["Alpha"], msp.inputs[0])
        nt.links.new(msp.outputs[0], bsdf.inputs["Specular IOR Level"])

    if "Subsurface Weight" in bsdf.inputs and skin_sss > 0.001:
        m_sss = nt.nodes.new("ShaderNodeMix")
        m_sss.data_type = "FLOAT"
        m_sss.inputs[2].default_value = skin_sss
        m_sss.inputs[3].default_value = 0.0
        nt.links.new(tex.outputs["Alpha"], m_sss.inputs[0])
        nt.links.new(m_sss.outputs[0], bsdf.inputs["Subsurface Weight"])

    if "Coat Weight" in bsdf.inputs:
        mc = nt.nodes.new("ShaderNodeMix")
        mc.data_type = "FLOAT"
        mc.inputs[2].default_value = 0.08
        mc.inputs[3].default_value = 0.0
        nt.links.new(tex.outputs["Alpha"], mc.inputs[0])
        nt.links.new(mc.outputs[0], bsdf.inputs["Coat Weight"])
        if "Coat Roughness" in bsdf.inputs:
            bsdf.inputs["Coat Roughness"].default_value = 0.32

    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat, tex


def make_stylized_hair_mat(name, base_rgba, roughness=0.58):
    """Stylized Roblox UGC hair shader with root-to-tip shading & directional strand grooves."""
    mat = bpy.data.materials.new(name=name)
    mat.diffuse_color = base_rgba
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


def _create_segmented_limb_box(name, size_studs, center_studs, uv_table, mat, collection, bevel_m=0.014):
    """
    Create a single connected R15 limb (Arm or Leg) with an indented horizontal elbow/knee crease groove at z=0.
    Eliminates ugly stair-step box separation when elbows/knees bend 90 deg while keeping the crisp R15 seam line.
    Returns (obj, weights_spec) where weights_spec maps vertex z to (upper_weight, lower_weight).
    """
    sx, sy, sz = [s * STUD for s in size_studs]
    cx, cy, cz = [c * STUD for c in center_studs]
    mesh = bpy.data.meshes.new(name + "_Mesh")
    bm = bmesh.new()

    # 5 Z-levels: bottom, below-crease, indented crease center, above-crease, top
    z_levels = [
        (-0.500 * sz, 1.000),
        (-0.024 * sz, 1.000),
        (0.000 * sz,  0.945),
        (+0.024 * sz, 1.000),
        (+0.500 * sz, 1.000),
    ]
    rings = []
    for zv, sc_xy in z_levels:
        hx = 0.5 * sx * sc_xy
        hy = 0.5 * sy * sc_xy
        rings.append([
            bm.verts.new((-hx, -hy, zv)),
            bm.verts.new((+hx, -hy, zv)),
            bm.verts.new((+hx, +hy, zv)),
            bm.verts.new((-hx, +hy, zv)),
        ])

    # Bottom cap (-Z) and Top cap (+Z)
    bm.faces.new((rings[0][0], rings[0][3], rings[0][2], rings[0][1]))
    bm.faces.new((rings[-1][0], rings[-1][1], rings[-1][2], rings[-1][3]))
    # Side quads across the 4 vertical segments
    for r_i in range(len(rings) - 1):
        ra, rb = rings[r_i], rings[r_i + 1]
        for k in range(4):
            kn = (k + 1) % 4
            bm.faces.new((ra[k], ra[kn], rb[kn], rb[k]))

    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    uv_layer = bm.loops.layers.uv.new("UVMap")
    for f in bm.faces:
        side = _face_dir(f.normal)
        u0, v0, u1, v1 = px_to_uv(*uv_table[side])
        for loop in f.loops:
            co = loop.vert.co
            # Normalize x/y by local ring half-width so UVs don't pinch at the indented crease
            sc_cur = 0.945 if abs(co.z) < 0.005 * sz else 1.0
            nx = co.x / (sx * sc_cur)
            ny = co.y / (sy * sc_cur)
            nz = (co.z / sz) + 0.5
            if side == "front":   u_t, v_t = nx + 0.5, nz
            elif side == "back":  u_t, v_t = -nx + 0.5, nz
            elif side == "left":  u_t, v_t = ny + 0.5, nz
            elif side == "right": u_t, v_t = -ny + 0.5, nz
            elif side == "top":   u_t, v_t = nx + 0.5, ny + 0.5
            else:                 u_t, v_t = nx + 0.5, -ny + 0.5
            loop[uv_layer].uv = (u0 + u_t * (u1 - u0), v0 + v_t * (v1 - v0))

    bm.to_mesh(mesh); bm.free()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = (cx, cy, cz)
    obj.data.materials.append(mat)
    collection.objects.link(obj)
    bev = obj.modifiers.new("Bevel", "BEVEL")
    bev.width = bevel_m; bev.segments = 2; bev.limit_method = "ANGLE"; bev.angle_limit = math.radians(62.0)
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
    "elder_man":    {"tw": 2.14, "td": 1.12, "th": 1.94, "lw": 0.98, "lh": 1.90, "ah": 1.92, "hs": 1.26},
    "elder_woman":  {"tw": 1.78, "td": 0.92, "th": 1.82, "lw": 0.84, "lh": 1.84, "ah": 1.84, "hs": 1.22},
}


def build_roblox_character(
    name: str,
    shirt_path: str,
    pants_path: str,
    face_png: str,
    skin_hex: str = "#F2C296",
    hair_hex: str = None,
    location_m=(0.0, 0.0, 0.0),
    yaw_deg: float = 0.0,
    scale_h: float = None,
    rig_type: str = "R15",
    hair_style: str = "boy",
    body_profile: str = "default",
    accessories: list = None,
    shirt_fabric: str = "default",
    pants_fabric: str = "default",
):
    """
    Build the locked-standard Roblox character (ROBLOX_DIRECTOR.md §4.0): articulated R15 rig, archetype
    body_profile, micro-PBR fabric presets ('default','puffer','wool','coat','denim'), anti-glare 2D face decal,
    sculpted stylized hair (`hair_style` = "boy" | "boy_part" | "boy_fluffy" | "girl" | "girl_bob" | "girl_ponytail" | "old_man" | "old_woman" | "bald", built by
    blender_hair_locks.py; `hair_hex` None = the style's default colour) and optional 3D accessories.
    """
    if rig_type.upper() != "R15":
        raise ValueError("only R15 is supported (ROBLOX_DIRECTOR.md §4.0)")
    import blender_hair_locks as _hair
    if hair_style != "bald" and hair_style not in _hair.STYLES:
        raise ValueError(f"hair_style must be 'bald' or one of {_hair.STYLES}")
    if hair_hex is None:
        hair_hex = _hair.DEFAULT_HEX.get(hair_style, "#2B1B14")
    prof = dict(BODY_PROFILES.get(body_profile, BODY_PROFILES["default"]))
    if scale_h is not None:
        prof["hs"] = scale_h
    tw, td, th = prof["tw"], prof["td"], prof["th"]
    lw, lh, ah, hs = prof["lw"], prof["lh"], prof["ah"], prof["hs"]

    col = bpy.data.collections.new(f"Char_{name}")
    bpy.context.scene.collection.children.link(col)

    skin_rgba = hex_to_linear_rgba(skin_hex)
    hair_rgba = hex_to_linear_rgba(hair_hex)
    mat_shirt = make_skin_cloth_mat(f"{name}_Shirt", skin_rgba, shirt_path, fabric=shirt_fabric)
    mat_pants = make_skin_cloth_mat(f"{name}_Pants", skin_rgba, pants_path, fabric=pants_fabric)
    mat_head, face_tex_node = make_head_face_mat(f"{name}_Head", skin_rgba, face_png)
    mat_hair = make_stylized_hair_mat(f"{name}_Hair", hair_rgba, roughness=0.56)

    hip_z = lh
    neck_z = lh + th
    arm_x = 0.5 * tw + 0.5 * lw + 0.02
    leg_x = 0.255 * tw
    head_center = (0.0, 0.0, neck_z + 0.52 * hs)

    parts_map = [   # R15 only
            (_create_uv_box(f"{name}_UpperTorso", (tw, td, th), (0.0, 0.0, hip_z + 0.5 * th), TORSO_UV, mat_shirt, col, v_range=(0.0, 1.0), bevel_m=0.015), "UpperTorso"),
            (_create_segmented_limb_box(f"{name}_ArmR", (lw, lw, ah), (-arm_x, 0.0, neck_z - 0.5 * ah), RLIMB_UV, mat_shirt, col, bevel_m=0.014), ("RightUpperArm", "RightLowerArm")),
            (_create_segmented_limb_box(f"{name}_ArmL", (lw, lw, ah), (arm_x, 0.0, neck_z - 0.5 * ah), LLIMB_UV, mat_shirt, col, bevel_m=0.014), ("LeftUpperArm", "LeftLowerArm")),
            (_create_segmented_limb_box(f"{name}_LegR", (lw, lw, lh), (-leg_x, 0.0, 0.5 * lh), RLIMB_UV, mat_pants, col, bevel_m=0.014), ("RightUpperLeg", "RightLowerLeg")),
            (_create_segmented_limb_box(f"{name}_LegL", (lw, lw, lh), (leg_x, 0.0, 0.5 * lh), LLIMB_UV, mat_pants, col, bevel_m=0.014), ("LeftUpperLeg", "LeftLowerLeg")),
            (_create_roblox_head(f"{name}_Head", head_center, hs, mat_head, col), "Head"),
        ]

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
        split_z = hip_z + 0.325 * th
        sh_z = neck_z - 0.16 * ah; el_z = neck_z - 0.50 * ah; hd_z = neck_z - ah; kn_z = 0.50 * lh
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
        bpy.ops.object.mode_set(mode="OBJECT")

    for obj, bspec in parts_map:
        wm = obj.matrix_world.copy()
        obj.parent = arm_obj
        obj.matrix_parent_inverse = arm_obj.matrix_world.inverted()
        obj.matrix_world = wm
        if isinstance(bspec, tuple):
            ub_name, lb_name = bspec
            vg_u = obj.vertex_groups.get(ub_name) or obj.vertex_groups.new(name=ub_name)
            vg_l = obj.vertex_groups.get(lb_name) or obj.vertex_groups.new(name=lb_name)
            for idx, v in enumerate(obj.data.vertices):
                if v.co.z > 0.015 * STUD:
                    vg_u.add([idx], 1.0, "REPLACE")
                elif v.co.z < -0.015 * STUD:
                    vg_l.add([idx], 1.0, "REPLACE")
                else:
                    vg_u.add([idx], 0.5, "REPLACE")
                    vg_l.add([idx], 0.5, "REPLACE")
        else:
            vg = obj.vertex_groups.get(bspec) or obj.vertex_groups.new(name=bspec)
            vg.add(list(range(len(obj.data.vertices))), 1.0, "REPLACE")
        mod = obj.modifiers.new("Armature", "ARMATURE")
        mod.object = arm_obj
        if hasattr(mod, "use_deform_preserve_volume"):
            mod.use_deform_preserve_volume = True

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
    if hair_style != "bald":
        info["hair_obj"] = _hair.build_lock_hair(info, style=hair_style, hair_hex=hair_hex)
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
    elif acc_type == "earmuffs":
        # Plush 3D winter earmuffs with wool Sheen material + clean uniform arched headband tube (zero tapered tail!)
        muff_hex = color_hex if color_hex is not None else "#EDF2F8"
        band_hex = accent_hex if accent_hex != "#E53935" else "#D5DEE8"
        mat_muff = make_wool_mat(f"{arm.name}_EarmuffPlush", hex_to_linear_rgba(muff_hex), roughness=0.90, sheen=0.88)
        mat_band = make_solid_mat(f"{arm.name}_EarmuffBand", hex_to_linear_rgba(band_hex), roughness=0.42)
        for sgn, sn in ((-1, "R"), (1, "L")):
            m_pos = ((cx + sgn * 0.68 * hs) * STUD, (cy - 0.02 * hs) * STUD, (cz - 0.02 * hs) * STUD)
            muff = _add_curl_puff(f"{arm.name}_EarMuff_{sn}", m_pos, 0.30 * hs * STUD, (0.72, 1.02, 1.12), mat_muff, col, segs=18, rings=12)
            created.append((muff, head_bone))
        # Uniform-thickness curved headband arch over top of hair crown (-80 deg .. +80 deg)
        bm_b = bmesh.new()
        n_arc, n_ring = 22, 10
        r_x = 0.72 * hs * STUD
        r_z = 0.71 * hs * STUD
        tube_w = 0.065 * hs * STUD
        tube_t = 0.028 * hs * STUD
        rings_b = []
        for i in range(n_arc + 1):
            ang = math.radians(-80.0 + 160.0 * (i / float(n_arc)))
            px = cx * STUD + r_x * math.sin(ang)
            py = (cy - 0.02 * hs) * STUD
            pz = cz * STUD + r_z * math.cos(ang)
            nx = math.sin(ang)
            nz = math.cos(ang)
            row = []
            for j in range(n_ring):
                th = 2.0 * math.pi * j / n_ring
                off_n = tube_t * math.cos(th)
                off_y = tube_w * math.sin(th)
                row.append(bm_b.verts.new((px + nx * off_n, py + off_y, pz + nz * off_n)))
            rings_b.append(row)
        for i in range(n_arc):
            for j in range(n_ring):
                jn = (j + 1) % n_ring
                bm_b.faces.new((rings_b[i][j], rings_b[i][jn], rings_b[i + 1][jn], rings_b[i + 1][j]))
        bm_b.faces.new(list(reversed(rings_b[0])))
        bm_b.faces.new(rings_b[-1])
        bmesh.ops.recalc_face_normals(bm_b, faces=bm_b.faces)
        for f in bm_b.faces:
            f.smooth = True
        m_band = bpy.data.meshes.new(f"{arm.name}_EarmuffBand_M")
        bm_b.to_mesh(m_band); bm_b.free()
        band = bpy.data.objects.new(f"{arm.name}_EarmuffBand", m_band)
        band.data.materials.append(mat_band)
        col.objects.link(band)
        created.append((band, head_bone))

    bpy.context.view_layer.update()
    for ob, bn in created:
        ob.matrix_world = arm.matrix_world @ ob.matrix_world
        wm = ob.matrix_world.copy()
        ob.parent = arm; ob.matrix_parent_inverse = arm.matrix_world.inverted(); ob.matrix_world = wm
        vg = ob.vertex_groups.new(name=bn); vg.add(list(range(len(ob.data.vertices))), 1.0, "REPLACE")
        mod = ob.modifiers.new("Armature", "ARMATURE"); mod.object = arm
    return [o for o, _ in created]


def add_scarf_3d(char_info: dict, color_hex: str = "#D93829", stripe_hex: str = "#8C1D18"):
    """Attach a stylized 3D wool-sheen neck scarf (collar torus + zero-clipping hanging ends) weighted to UpperTorso/Torso."""
    arm_obj = char_info["armature"]
    col = char_info["collection"]
    m = char_info["metrics"]
    neck_z = m["neck_z"]
    td = m["td"]
    bone_name = "UpperTorso" if char_info.get("rig_type") == "R15" else "Torso"

    mat_main = make_wool_mat(f"{arm_obj.name}_ScarfMain", hex_to_linear_rgba(color_hex), roughness=0.88, sheen=0.82)
    mat_stripe = make_wool_mat(f"{arm_obj.name}_ScarfStripe", hex_to_linear_rgba(stripe_hex), roughness=0.88, sheen=0.82)

    # Neck collar ring hugging neck_z with clean clearance over shoulders
    bpy.ops.mesh.primitive_torus_add(
        major_radius=0.62 * STUD, minor_radius=0.13 * STUD,
        major_segments=28, minor_segments=14,
        location=(0.0, 0.0, (neck_z - 0.02) * STUD)
    )
    collar = bpy.context.active_object
    collar.name = f"{arm_obj.name}_ScarfCollar"
    collar.scale = (1.14, 0.96, 0.90)
    collar.data.materials.append(mat_main)
    for p in collar.data.polygons: p.use_smooth = True

    # Two hanging front scarf tails offset cleanly in front of torso (-0.5*td - 0.10) to eliminate sitting/bending clipping
    front_y = -0.5 * td - 0.11
    tails = []
    for idx, (tx, ty, tz, sx, sy, sz, rot_y) in enumerate([
        (-0.24, front_y, neck_z - 0.66, 0.30, 0.09, 1.18, -5),
        ( 0.24, front_y - 0.025, neck_z - 0.78, 0.30, 0.09, 1.38, 4),
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
        t_obj.rotation_euler = Euler((math.radians(-7), math.radians(rot_y), 0))
        t_obj.data.materials.append(mat_main if idx == 0 else mat_stripe)
        bev = t_obj.modifiers.new("Bevel", "BEVEL")
        bev.width = 0.008; bev.segments = 2
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
    face_style: str = "cinema_expressive",
    age: str = None,
) -> str:
    """
    Generate/return a 20-face Roblox pack via make_faces_expressive.py:
      - 'cinema_expressive' (default for GibbsonTV / Semi-Real Roblox CGI Cinema)
      - 'storybook_toon' (optional for kids/Shorts reels)
    """
    style = face_style or "cinema_expressive"
    if style not in ("cinema_expressive", "storybook_toon"):
        raise ValueError("supported face_style: 'cinema_expressive' (default Cinema CGI) or 'storybook_toon' (Shorts)")
    if age is None:
        age = archetype if archetype in ("elder_man", "elder_woman") else "youth"
    shipped = CORE_FACES_CINEMA_DIR if style == "cinema_expressive" else CORE_FACES_STORYBOOK_DIR
    if not os.path.exists(os.path.join(out_dir, "neutral.png")):
        try:
            import make_faces_expressive as mfe
            mfe.generate_pack(out_dir, style=style, age=age)
        except ImportError:  # Blender's Python has no PIL: fall back to the shipped pack
            if os.path.isdir(shipped):
                return shipped
    return out_dir


def _make_outerwear_pbr_mat(name: str, color_hex: str, roughness: float = 0.62, sheen: float = 0.45, wetness: float = 0.0):
    """Semi-real Cycles PBR garment shader: micro-weave bump + AO crevice + optional rain wetness clearcoat."""
    mat = bpy.data.materials.new(name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    base = hex_to_linear_rgba(color_hex)

    # Subtle fabric/leather micro-grain + Cycles AO darkening
    tc = nt.nodes.new("ShaderNodeTexCoord")
    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 95.0
    noise.inputs["Detail"].default_value = 8.0
    noise.inputs["Roughness"].default_value = 0.65
    nt.links.new(tc.outputs["Object"], noise.inputs["Vector"])

    ao = nt.nodes.new("ShaderNodeAmbientOcclusion")
    ao.samples = 8
    ao.inputs["Distance"].default_value = 0.14
    ao.inputs["Color"].default_value = base

    mix_ao = nt.nodes.new("ShaderNodeMix")
    mix_ao.data_type = "RGBA"
    mix_ao.blend_type = "MULTIPLY"
    mix_ao.inputs["Factor"].default_value = 0.35
    rgba_in = [s for s in mix_ao.inputs if s.type == "RGBA"]
    rgba_in[0].default_value = base
    nt.links.new(ao.outputs["AO"], rgba_in[1])
    nt.links.new(next(s for s in mix_ao.outputs if s.type == "RGBA"), bsdf.inputs["Base Color"])

    # Roughness modulated by rain wetness
    eff_rough = max(0.14, roughness * (1.0 - 0.58 * wetness))
    r_map = nt.nodes.new("ShaderNodeMapRange")
    r_map.inputs["From Min"].default_value = 0.25
    r_map.inputs["From Max"].default_value = 0.75
    r_map.inputs["To Min"].default_value = max(0.08, eff_rough - 0.12)
    r_map.inputs["To Max"].default_value = min(0.95, eff_rough + 0.10)
    nt.links.new(noise.outputs["Fac"], r_map.inputs["Value"])
    nt.links.new(r_map.outputs["Result"], bsdf.inputs["Roughness"])

    if "Sheen Weight" in bsdf.inputs:
        bsdf.inputs["Sheen Weight"].default_value = sheen * (1.0 - 0.4 * wetness)
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = min(0.85, 0.08 + 0.72 * wetness)
        bsdf.inputs["Coat Roughness"].default_value = max(0.06, 0.24 - 0.16 * wetness)

    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.14
    bump.inputs["Distance"].default_value = 0.004
    nt.links.new(noise.outputs["Fac"], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def _bind_wearable_parts(char_info: dict, items: list):
    """Parent and armature-weight a list of (obj, bone_name) wearables cleanly to the R15 rig."""
    arm = char_info["armature"]
    col = char_info["collection"]
    bpy.context.view_layer.update()
    out = []
    for ob, bn in items:
        for c in list(ob.users_collection):
            c.objects.unlink(ob)
        col.objects.link(ob)
        bpy.context.view_layer.update()
        ob.matrix_world = arm.matrix_world @ ob.matrix_world
        wm = ob.matrix_world.copy()
        ob.parent = arm
        ob.matrix_parent_inverse = arm.matrix_world.inverted()
        ob.matrix_world = wm
        vg = ob.vertex_groups.get(bn) or ob.vertex_groups.new(name=bn)
        vg.add(list(range(len(ob.data.vertices))), 1.0, "REPLACE")
        mod = ob.modifiers.new("Armature", "ARMATURE")
        mod.object = arm
        out.append(ob)
    return out


def add_jacket_3d(
    char_info: dict,
    style: str = "open_jacket",
    color_hex: str = "#1C232E",
    lining_hex: str = "#2C3542",
    hardware_hex: str = "#B0A899",
    wetness: float = 0.0,
):
    """
    Attach real 3D layered Semi-Real CGI outerwear to an R15 character (GibbsonTV standard):
      - 'open_jacket': thick beveled open front panels, sculpted angled lapels, upturned collar, metallic zip strips
      - 'trench': extended noir trench coat with upturned dramatic collar + lower coattail panels on LowerTorso
      - 'hoodie': layered zip/pullover jacket + sculpted 3D draped hood behind neck + front drawstrings
    """
    arm = char_info["armature"]
    m = char_info["metrics"]
    tw, td, th, lh, neck_z = m["tw"], m["td"], m["th"], m["lh"], m["neck_z"]
    hip_z = lh
    mid_z = hip_z + 0.50 * th
    ub = "UpperTorso" if char_info.get("rig_type") == "R15" else "Torso"
    lb = "LowerTorso" if char_info.get("rig_type") == "R15" else "Torso"

    mat_out = _make_outerwear_pbr_mat(f"{arm.name}_JktOut", color_hex, roughness=0.58, sheen=0.42, wetness=wetness)
    mat_lin = _make_outerwear_pbr_mat(f"{arm.name}_JktLin", lining_hex, roughness=0.72, sheen=0.55, wetness=wetness * 0.4)
    mat_hw = make_solid_mat(f"{arm.name}_JktHW", hex_to_linear_rgba(hardware_hex), roughness=0.26)
    bsdf_hw = next((n for n in mat_hw.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if bsdf_hw and "Metallic" in bsdf_hw.inputs:
        bsdf_hw.inputs["Metallic"].default_value = 0.85

    created = []

    def _slab(name, loc_s, sz_s, mat, rot_d=(0.0, 0.0, 0.0), bone=ub, bevel=0.008):
        bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=1.0)
        for v in bm.verts:
            v.co.x *= sz_s[0] * STUD
            v.co.y *= sz_s[1] * STUD
            v.co.z *= sz_s[2] * STUD
        me = bpy.data.meshes.new(f"{arm.name}_{name}_M")
        bm.to_mesh(me)
        bm.free()
        ob = bpy.data.objects.new(f"{arm.name}_{name}", me)
        ob.location = (loc_s[0] * STUD, loc_s[1] * STUD, loc_s[2] * STUD)
        ob.rotation_euler = Euler([math.radians(a) for a in rot_d])
        ob.data.materials.append(mat)
        bev = ob.modifiers.new("Bevel", "BEVEL")
        bev.width = bevel
        bev.segments = 2
        for p in ob.data.polygons:
            p.use_smooth = True
        created.append((ob, bone))
        return ob

    # Back panel & side wrap panels (slight outward clearance over torso, zero clipping with arms)
    j_h = th * 1.04
    _slab("JktBack", (0.0, td * 0.50 + 0.055, mid_z), (tw + 0.14, 0.10, j_h), mat_out)
    for sx, tag in ((-1.0, "R"), (1.0, "L")):
        _slab(f"JktSide_{tag}", (sx * (tw * 0.50 + 0.045), 0.02, mid_z), (0.09, td + 0.10, j_h), mat_out)
        # Front open jacket panel (leaves a real 3D vertical gap showing the inner shirt!)
        front_w = tw * 0.36
        front_x = sx * (tw * 0.50 - front_w * 0.44 + 0.03)
        _slab(f"JktFront_{tag}", (front_x, -td * 0.50 - 0.055, mid_z), (front_w, 0.095, j_h), mat_out)
        # Sculpted angled lapel fold catching rim & chiaroscuro key light
        lap_x = sx * (tw * 0.21)
        _slab(f"JktLapel_{tag}", (lap_x, -td * 0.50 - 0.088, neck_z - 0.42), (0.24, 0.065, 0.72), mat_lin, rot_d=(-6.0, sx * 14.0, sx * -16.0), bevel=0.006)
        # Metallic zipper track along inner front edge
        zip_x = sx * (tw * 0.145)
        _slab(f"JktZip_{tag}", (zip_x, -td * 0.50 - 0.095, mid_z - 0.06), (0.032, 0.024, j_h * 0.86), mat_hw, bevel=0.002)
        # Sculpted shoulder epaulette/cap seam
        _slab(f"JktShoulder_{tag}", (sx * (tw * 0.35), 0.0, neck_z + 0.03), (tw * 0.36, td + 0.14, 0.08), mat_out, bevel=0.007)

    # Dramatic upturned collar wrapping neck back & sides
    col_h = 0.34 if style == "trench" else 0.26
    _slab("JktCollarBack", (0.0, td * 0.38 + 0.04, neck_z + col_h * 0.42), (tw * 0.74, 0.11, col_h), mat_out, rot_d=(12.0, 0.0, 0.0), bevel=0.007)
    for sx, tag in ((-1.0, "R"), (1.0, "L")):
        _slab(f"JktCollarSide_{tag}", (sx * (tw * 0.36), 0.04, neck_z + col_h * 0.38), (0.10, td * 0.74, col_h * 0.92), mat_out, rot_d=(0.0, sx * -12.0, 0.0), bevel=0.007)

    # Full 3D Long Jacket Sleeves wrapping upper & lower arm bones (leaves wrists/hands exposed!)
    if char_info.get("rig_type") == "R15":
        lw_s = max(0.75, (m["shoulder_w"] / STUD - tw) * 0.5)
        arm_x = 0.5 * tw + 0.5 * lw_s + 0.04
        ah_s = th * 1.00
        for sx, side_name in ((1.0, "Left"), (-1.0, "Right")):
            _slab(f"JktSleeveUp_{side_name}", (sx * arm_x, 0.0, neck_z - 0.26 * ah_s), (lw_s + 0.10, td + 0.10, 0.50 * ah_s), mat_out, bone=f"{side_name}UpperArm", bevel=0.010)
            _slab(f"JktSleeveLo_{side_name}", (sx * arm_x, 0.0, neck_z - 0.68 * ah_s), (lw_s + 0.08, td + 0.08, 0.36 * ah_s), mat_out, bone=f"{side_name}LowerArm", bevel=0.009)
            _slab(f"JktCuff_{side_name}", (sx * arm_x, 0.0, neck_z - 0.85 * ah_s), (lw_s + 0.11, td + 0.11, 0.09), mat_lin, bone=f"{side_name}LowerArm", bevel=0.005)

    # Trench coat lower coattails (weighted to LowerTorso so walking legs stay readable)
    if style == "trench":
        tail_h = lh * 0.52
        tail_z = hip_z - tail_h * 0.44
        _slab("TrenchBack", (0.0, td * 0.50 + 0.075, tail_z), (tw + 0.22, 0.10, tail_h), mat_out, rot_d=(6.0, 0.0, 0.0), bone=lb)
        for sx, tag in ((-1.0, "R"), (1.0, "L")):
            _slab(f"TrenchFlap_{tag}", (sx * (tw * 0.36), -td * 0.50 - 0.075, tail_z), (tw * 0.38, 0.09, tail_h * 0.95), mat_out, rot_d=(-5.0, 0.0, 0.0), bone=lb)
            _slab(f"TrenchSide_{tag}", (sx * (tw * 0.50 + 0.065), 0.02, tail_z), (0.09, td + 0.14, tail_h * 0.96), mat_out, rot_d=(0.0, sx * -5.0, 0.0), bone=lb)

    # Draped 3D hoodie hood behind neck + drawstrings
    if style == "hoodie":
        bpy.ops.mesh.primitive_torus_add(
            major_radius=0.56 * STUD, minor_radius=0.17 * STUD,
            major_segments=24, minor_segments=12,
            location=(0.0, 0.22 * STUD, (neck_z + 0.06) * STUD),
            rotation=(math.radians(24.0), 0.0, 0.0),
        )
        hood = bpy.context.active_object
        hood.name = f"{arm.name}_HoodDrape"
        hood.scale = (1.18, 1.05, 0.85)
        bpy.ops.object.transform_apply(scale=True)
        hood.data.materials.append(mat_out)
        for p in hood.data.polygons:
            p.use_smooth = True
        created.append((hood, ub))
        for sx, tag in ((-1.0, "R"), (1.0, "L")):
            _slab(f"HoodString_{tag}", (sx * 0.17, -td * 0.50 - 0.105, neck_z - 0.36), (0.032, 0.028, 0.58), mat_hw, rot_d=(-4.0, sx * 4.0, 0.0), bevel=0.002)

    return _bind_wearable_parts(char_info, created)


def add_belt_3d(char_info: dict, leather_hex: str = "#1A130E", buckle_hex: str = "#A89F8D", pouch: bool = True):
    """Attach a 3D weathered leather belt + metallic buckle + optional side utility pouch to LowerTorso."""
    arm = char_info["armature"]
    m = char_info["metrics"]
    tw, td, lh = m["tw"], m["td"], m["lh"]
    lb = "LowerTorso" if char_info.get("rig_type") == "R15" else "Torso"
    mat_l = _make_outerwear_pbr_mat(f"{arm.name}_BeltLeather", leather_hex, roughness=0.44, sheen=0.12)
    mat_b = make_solid_mat(f"{arm.name}_BeltBuckle", hex_to_linear_rgba(buckle_hex), roughness=0.22)
    bsdf_b = next((n for n in mat_b.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if bsdf_b and "Metallic" in bsdf_b.inputs:
        bsdf_b.inputs["Metallic"].default_value = 0.90

    created = []
    def _part(name, loc_s, sz_s, mat, bevel=0.005):
        bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=1.0)
        for v in bm.verts:
            v.co.x *= sz_s[0] * STUD
            v.co.y *= sz_s[1] * STUD
            v.co.z *= sz_s[2] * STUD
        me = bpy.data.meshes.new(f"{arm.name}_{name}_M")
        bm.to_mesh(me); bm.free()
        ob = bpy.data.objects.new(f"{arm.name}_{name}", me)
        ob.location = (loc_s[0] * STUD, loc_s[1] * STUD, loc_s[2] * STUD)
        ob.data.materials.append(mat)
        bev = ob.modifiers.new("Bevel", "BEVEL"); bev.width = bevel; bev.segments = 2
        for p in ob.data.polygons: p.use_smooth = True
        created.append((ob, lb))
        return ob

    bz = lh + 0.08
    _part("BeltBand", (0.0, 0.0, bz), (tw + 0.16, td + 0.16, 0.22), mat_l)
    _part("BeltBuckle", (0.0, -td * 0.50 - 0.10, bz), (0.34, 0.07, 0.26), mat_b, bevel=0.003)
    if pouch:
        _part("BeltPouch", (tw * 0.50 + 0.13, -0.06, bz - 0.06), (0.18, 0.34, 0.36), mat_l)
    return _bind_wearable_parts(char_info, created)


def add_backpack_3d(char_info: dict, color_hex: str = "#2A3038", strap_hex: str = "#16181D", accent_hex: str = "#5C4735", wetness: float = 0.0):
    """Attach a 3D contoured weathered canvas/nylon backpack + dual shoulder straps to UpperTorso."""
    arm = char_info["armature"]
    m = char_info["metrics"]
    tw, td, th, lh, neck_z = m["tw"], m["td"], m["th"], m["lh"], m["neck_z"]
    ub = "UpperTorso" if char_info.get("rig_type") == "R15" else "Torso"
    mat_p = _make_outerwear_pbr_mat(f"{arm.name}_PackMain", color_hex, roughness=0.68, sheen=0.40, wetness=wetness)
    mat_s = _make_outerwear_pbr_mat(f"{arm.name}_PackStrap", strap_hex, roughness=0.60, sheen=0.25, wetness=wetness)
    mat_a = _make_outerwear_pbr_mat(f"{arm.name}_PackAcc", accent_hex, roughness=0.52, sheen=0.20, wetness=wetness)

    created = []
    def _part(name, loc_s, sz_s, mat, bevel=0.014):
        bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=1.0)
        for v in bm.verts:
            v.co.x *= sz_s[0] * STUD
            v.co.y *= sz_s[1] * STUD
            v.co.z *= sz_s[2] * STUD
        me = bpy.data.meshes.new(f"{arm.name}_{name}_M")
        bm.to_mesh(me); bm.free()
        ob = bpy.data.objects.new(f"{arm.name}_{name}", me)
        ob.location = (loc_s[0] * STUD, loc_s[1] * STUD, loc_s[2] * STUD)
        ob.data.materials.append(mat)
        bev = ob.modifiers.new("Bevel", "BEVEL"); bev.width = bevel; bev.segments = 3
        for p in ob.data.polygons: p.use_smooth = True
        created.append((ob, ub))
        return ob

    pz = lh + th * 0.52
    py = td * 0.50 + 0.44
    _part("PackBody", (0.0, py, pz), (tw * 0.78, 0.66, th * 0.84), mat_p, bevel=0.022)
    _part("PackPocket", (0.0, py + 0.34, pz - 0.22), (tw * 0.62, 0.22, th * 0.42), mat_a, bevel=0.014)
    _part("PackTopFlap", (0.0, py + 0.04, pz + th * 0.36), (tw * 0.76, 0.70, 0.18), mat_a, bevel=0.012)
    for sx, tag in ((-1.0, "R"), (1.0, "L")):
        _part(f"PackStrapFront_{tag}", (sx * (tw * 0.34), -td * 0.50 - 0.105, pz), (0.16, 0.06, th * 0.94), mat_s, bevel=0.004)
        _part(f"PackStrapTop_{tag}", (sx * (tw * 0.34), 0.04, neck_z + 0.06), (0.16, td + 0.26, 0.06), mat_s, bevel=0.004)
    return _bind_wearable_parts(char_info, created)


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

def _char_offset_to_bone_local(arm_obj, bone_name: str, delta_char_m: Vector) -> Vector:
    b = arm_obj.data.bones.get(bone_name)
    if b is None:
        return delta_char_m
    return b.matrix_local.to_3x3().inverted() @ delta_char_m


def key_r15_pose(arm_obj, frame: int, loc=None, yaw_deg: float = None, interpolation: str = "BEZIER",
                 hip_offset=None, **bones):
    """
    Keyframe R15 root location/yaw, optional LowerTorso center-of-mass hip_offset (Squash & Stretch / Weight Shift),
    and local XYZ Euler bone rotations cleanly with AUTO_CLAMPED Bezier Slow-In / Slow-Out handles.
    """
    if loc is not None:
        arm_obj.location = Vector(loc)
        arm_obj.keyframe_insert(data_path="location", frame=frame)
    if yaw_deg is not None:
        arm_obj.rotation_euler = Euler((0.0, 0.0, math.radians(yaw_deg)))
        arm_obj.keyframe_insert(data_path="rotation_euler", frame=frame)
    pb = arm_obj.pose.bones
    if hip_offset is not None and "LowerTorso" in pb:
        lt = pb["LowerTorso"]
        lt.location = _char_offset_to_bone_local(arm_obj, "LowerTorso", Vector(hip_offset))
        lt.keyframe_insert(data_path="location", frame=frame)
    for bname, degs in bones.items():
        if bname.startswith("_"):
            continue
        if bname in pb and isinstance(degs, (tuple, list)) and len(degs) == 3:
            b = pb[bname]
            b.rotation_mode = "XYZ"
            b.rotation_euler = Euler([math.radians(a) for a in degs])
            b.keyframe_insert(data_path="rotation_euler", frame=frame)
    if arm_obj.animation_data and arm_obj.animation_data.action:
        for fc in iter_action_fcurves(arm_obj.animation_data.action):
            for kp in fc.keyframe_points:
                if int(round(kp.co.x)) == frame:
                    if interpolation == "VECTOR":
                        kp.interpolation = "BEZIER"
                        kp.handle_left_type = "VECTOR"
                        kp.handle_right_type = "VECTOR"
                    elif interpolation:
                        kp.interpolation = interpolation
                        if kp.interpolation == "BEZIER":
                            kp.handle_left_type = "AUTO_CLAMPED"
                            kp.handle_right_type = "AUTO_CLAMPED"
            fc.update()


def snap_r15_pose(arm_obj, fs: int, snap_frames: int = 9, overshoot: float = 0.07,
                  loc=None, yaw_deg: float = None, stagger: bool = True,
                  anticipate: bool = True, antic_ratio: float = 0.16,
                  arc_breakdown: bool = True, hip_offset=None, hold_frames: int = 0, **target_bones):
    """
    12-Principles Disney-Grade Pose Transition Engine:
    1. Squash & Stretch (`hip_offset` center-of-mass dip during transition & impact compression).
    2. Anticipation (`3f` reverse wind-up before dynamic movement).
    5. Follow Through & Overlapping Action (Staggered chain: LowerTorso/Legs -> UpperTorso (+1f) -> Arms (+2f with Overshoot) -> Head (+3f)).
    6. Slow In & Slow Out (`BEZIER` with `AUTO_CLAMPED` F-curve handles).
    7. Arcs (Automatic midpoint breakdown keyframe curving head pitch and opening arm elbows away from torso).
    9. Timing & Moving Hold (Optional `hold_frames` micro-breathing hold so characters never freeze into dead statues).
    """
    d = max(5, snap_frames)
    pose_hip = hip_offset if hip_offset is not None else target_bones.get("_hip_offset", (0.0, 0.0, 0.0))
    clean_bones = {k: v for k, v in target_bones.items() if not k.startswith("_") and isinstance(v, (tuple, list)) and len(v) == 3}

    lower_keys = {k: v for k, v in clean_bones.items() if k == "LowerTorso" or "Leg" in k}
    upper_keys = {k: v for k, v in clean_bones.items() if k == "UpperTorso"}
    arm_keys = {k: v for k, v in clean_bones.items() if "Arm" in k}
    head_keys = {k: v for k, v in clean_bones.items() if k == "Head"}

    pb = arm_obj.pose.bones
    bpy.context.scene.frame_set(fs)
    start_rots = {
        bn: tuple(math.degrees(a) for a in pb[bn].rotation_euler)
        for bn in clean_bones if bn in pb
    }

    # Principle 2: Anticipation (3-frame counter-windup + slight crouch dip)
    if anticipate and d >= 7 and fs >= 2:
        antic_bones = {}
        max_delta = 0.0
        for bn, degs in clean_bones.items():
            if bn in start_rots:
                cur_deg = start_rots[bn]
                delta = max(abs(degs[k] - cur_deg[k]) for k in range(3))
                max_delta = max(max_delta, delta)
                antic_bones[bn] = tuple(cur_deg[k] - (degs[k] - cur_deg[k]) * antic_ratio for k in range(3))
        if antic_bones and max_delta > 12.0:
            antic_hip = (pose_hip[0] * 0.3, pose_hip[1] * 0.3, min(pose_hip[2], -0.022))
            key_r15_pose(arm_obj, fs + 2, hip_offset=antic_hip, **antic_bones)
            fs_eff = fs + 2
            d_eff = max(4, d - 2)
        else:
            fs_eff, d_eff = fs, d
    else:
        fs_eff, d_eff = fs, d

    # Principle 7: Arcs (Midpoint breakdown keyframe curving limbs & dipping head turn)
    if arc_breakdown and d_eff >= 6:
        f_mid = fs_eff + max(2, d_eff // 2)
        arc_bones = {}
        for bn, tgt_deg in clean_bones.items():
            cur_deg = start_rots.get(bn, tgt_deg)
            mid = [0.5 * (cur_deg[k] + tgt_deg[k]) for k in range(3)]
            delta = max(abs(tgt_deg[k] - cur_deg[k]) for k in range(3))
            if bn == "Head" and delta > 10.0:
                # Natural downward chin arc (+4.5 deg pitch) during head turns
                mid[0] += 4.5
                arc_bones[bn] = tuple(mid)
            elif bn in ("RightUpperArm", "LeftUpperArm") and delta > 22.0:
                # Open elbow outward away from ribs to preserve silhouette & follow a circular arc
                sgn = -1.0 if bn == "RightUpperArm" else 1.0
                mid[2] += sgn * 11.0
                arc_bones[bn] = tuple(mid)
        mid_hip = (pose_hip[0] * 0.6, pose_hip[1] * 0.6, pose_hip[2] - 0.018)
        if arc_bones:
            key_r15_pose(arm_obj, f_mid, hip_offset=mid_hip, **arc_bones)

    if not stagger:
        key_r15_pose(arm_obj, fs_eff + d_eff, loc=loc, yaw_deg=yaw_deg, hip_offset=pose_hip, **clean_bones)
        return

    # Principle 5: Follow Through & Overlapping Action (Hips/Legs -> Chest (+1f) -> Arms (+2f w/ Overshoot) -> Head (+3f))
    f_arrive = fs_eff + d_eff
    key_r15_pose(arm_obj, f_arrive, loc=loc, yaw_deg=yaw_deg, hip_offset=pose_hip, **lower_keys)
    if upper_keys:
        key_r15_pose(arm_obj, f_arrive + 1, **upper_keys)
    if arm_keys:
        if overshoot > 0.01 and d_eff <= 14:
            over_arms = {}
            for bn, degs in arm_keys.items():
                cur_d = start_rots.get(bn, (0.0, 0.0, 0.0))
                over_arms[bn] = tuple(degs[k] + (degs[k] - cur_d[k]) * overshoot for k in range(3))
            key_r15_pose(arm_obj, f_arrive, **over_arms)
        key_r15_pose(arm_obj, f_arrive + 2, **arm_keys)
    if head_keys:
        key_r15_pose(arm_obj, f_arrive + 3, **head_keys)

    # Principle 9: Moving Hold (Keep character alive with micro-breathing during post-pose hold)
    if hold_frames >= 12:
        f_hold_mid = f_arrive + 3 + (hold_frames // 2)
        f_hold_end = f_arrive + 3 + hold_frames
        ut_base = clean_bones.get("UpperTorso", (2.0, 0.0, 0.0))
        hd_base = clean_bones.get("Head", (-2.0, 0.0, 0.0))
        hold_mid_bones = {
            "UpperTorso": (ut_base[0] - 1.6, ut_base[1], ut_base[2] + 0.6),
            "Head": (hd_base[0] + 1.0, hd_base[1], hd_base[2] - 0.5),
        }
        key_r15_pose(arm_obj, f_hold_mid, **hold_mid_bones)
        key_r15_pose(arm_obj, f_hold_end, hip_offset=pose_hip, **clean_bones)


def act_r15_sequence(arm_obj, beats: list, breathe: bool = True, breathe_cycle: int = 72, anticipate_fast: bool = True):
    """
    Choreograph natural human acting from asymmetric story beats:
    beats = [(frame, dur, loc, yaw_deg, bones_dict), ...]
    Enforces planted feet (zero Z jitter), staggered Spine->Chest->Arm->Head motion,
    automatic wind-up anticipation, midpoint arcs, and calm chest breathing.
    """
    for idx, entry in enumerate(beats):
        fr, dur, loc, yaw_deg, bones = entry
        use_antic = anticipate_fast and idx > 0 and dur <= 12
        next_fr = beats[idx + 1][0] if idx + 1 < len(beats) else (fr + dur + 20)
        hold_f = max(0, next_fr - (fr + dur + 4)) if breathe else 0
        snap_r15_pose(arm_obj, fr, snap_frames=dur, overshoot=0.07 if dur <= 12 else 0.03,
                      loc=loc, yaw_deg=yaw_deg, stagger=True, anticipate=use_antic,
                      arc_breakdown=True, hold_frames=min(28, hold_f), **(bones or {}))
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


def _world_bvh(obj, depsgraph, inset_m: float = 0.0):
    """Build a world-space BVHTree from an evaluated mesh (optionally shrunk slightly toward center for joint tolerance)."""
    from mathutils.bvhtree import BVHTree
    ev = obj.evaluated_get(depsgraph)
    if ev.type != "MESH" or not ev.data:
        return None
    me = ev.to_mesh()
    if not me or len(me.polygons) == 0:
        ev.to_mesh_clear()
        return None
    mw = ev.matrix_world
    verts = [mw @ v.co for v in me.vertices]
    if inset_m > 1e-5 and verts:
        ctr = sum(verts, Vector((0.0, 0.0, 0.0))) / float(len(verts))
        shrunk = []
        for p in verts:
            dv = p - ctr
            L = dv.length
            shrunk.append(ctr + dv * max(0.0, (L - inset_m) / L) if L > 1e-5 else p)
        verts = shrunk
    polys = [tuple(p.vertices) for p in me.polygons]
    ev.to_mesh_clear()
    return BVHTree.FromPolygons(verts, polys)


def _collect_mesh_objects(objs):
    """Expand any Empty/Armature/parent hierarchy into visible MESH objects."""
    seen, out = set(), []
    for ob in (objs or []):
        if ob is None:
            continue
        cands = [ob] + list(ob.children_recursive)
        for c in cands:
            if c.type == "MESH" and c.name not in seen and not c.hide_render:
                seen.add(c.name)
                out.append(c)
    return out


def _is_volume_only(o):
    """True for haze/smoke boxes: every material drives only the Volume output (no Surface) — not an obstacle."""
    mats = [m for m in o.data.materials if m] if o.type == "MESH" else []
    if not mats:
        return False
    for m in mats:
        out = next((n for n in m.node_tree.nodes if n.type == "OUTPUT_MATERIAL"), None) if m.node_tree else None
        if out is None or out.inputs["Surface"].is_linked or not out.inputs["Volume"].is_linked:
            return False
    return True


def _auto_collect_env_meshes(char_infos: list, ground_names: tuple, ignore_names: tuple):
    """Recursively collect every visible scene MESH outside character collections & ground planes."""
    char_obj_names = set()
    for ci in (char_infos or []):
        col = ci.get("collection")
        if col:
            for o in col.all_objects:
                char_obj_names.add(o.name)
        arm = ci.get("armature")
        if arm:
            char_obj_names.add(arm.name)
            for c in arm.children_recursive:
                char_obj_names.add(c.name)

    hidden_cols = {"_PH_Templates", "HeroLights", "_LL_HeroCast"}
    g_low = tuple(g.lower() for g in (ground_names or ()))
    ig_low = tuple(g.lower() for g in (ignore_names or ()))
    out = []
    for o in bpy.context.scene.objects:
        if o.type != "MESH" or o.hide_render or o.name in char_obj_names or _is_volume_only(o):
            continue
        if any(c.name in hidden_cols or c.hide_render for c in o.users_collection):
            continue
        n_low = o.name.lower()
        if any(tok in n_low for tok in g_low) or any(tok in n_low for tok in ig_low):
            continue
        out.append(o)
    return out


def _render_collision_debug(frame: int, focus_pt: Vector, out_dir: str, tag: str):
    """Render a quick top-angled diagnostic frame zoomed onto a detected collision."""
    os.makedirs(out_dir, exist_ok=True)
    sc = bpy.context.scene
    prev_cam, prev_rx, prev_ry = sc.camera, sc.render.resolution_x, sc.render.resolution_y
    prev_fp = sc.render.filepath
    cd = bpy.data.cameras.new("_ClipDebugCam")
    co = bpy.data.objects.new("_ClipDebugCam", cd)
    sc.collection.objects.link(co)
    co.location = focus_pt + Vector((1.6, -2.2, 1.8))
    co.rotation_euler = (focus_pt - co.location).to_track_quat("-Z", "Y").to_euler()
    cd.lens = 38.0
    sc.camera = co
    sc.render.resolution_x, sc.render.resolution_y = 640, 640
    sc.frame_set(frame)
    path = os.path.join(out_dir, f"clip_debug_f{frame:04d}_{tag}.png")
    sc.render.filepath = path
    try:
        bpy.ops.render.render(write_still=True)
    finally:
        sc.camera = prev_cam
        sc.render.resolution_x, sc.render.resolution_y = prev_rx, prev_ry
        sc.render.filepath = prev_fp
        bpy.data.objects.remove(co, do_unlink=True)
        bpy.data.cameras.remove(cd, do_unlink=True)
    return path


def audit_scene_collisions(
    char_infos: list,
    obstacles: list = None,
    frames: list = None,
    min_char_sep: float = 0.76,
    margin: float = 0.035,
    auto_collect_env: bool = True,
    ground_names: tuple = ("ground", "terrain", "floor", "road", "sidewalk", "lawn", "snow", "ice", "pond", "mud", "asphalt"),
    ignore_names: tuple = (),
    frame_step: int = 5,
    use_bvh: bool = True,
    check_ground_sink: bool = True,
    ground_z: float = 0.0,
    max_sink_m: float = 0.065,
    check_self_clip: bool = True,
    strict: bool = False,
    debug_dir: str = None,
) -> list:
    """
    Law R-COLLIDE 5-Layer Zero-Clipping Audit across the full animation timeline:
    1. Auto-collects ALL environment meshes (expanding GLB/Empty hierarchies) unless disabled.
    2. Samples the entire animation timeline (every `frame_step` frames) when `frames=None`.
    3. Uses AABB broadphase + exact world-space `BVHTree.overlap` triangle intersection (zero hollow-porch false positives).
    4. Detects CHAR_OBSTACLE, CHAR_CHAR, GROUND_SINK (buried feet), and SELF_CLIP (arm/prop stabbing torso).
    5. Optionally renders debug frames (`debug_dir`) and blocks bad builds (`strict=True` raises RuntimeError).
    Returns a list of collision dicts (empty list = 100% clean).
    """
    scene = bpy.context.scene
    if frames is None:
        fs, fe = scene.frame_start, scene.frame_end
        if fe <= fs:
            frames = [fs]
        else:
            frames = list(range(fs, fe + 1, max(1, int(frame_step))))
            if frames[-1] != fe:
                frames.append(fe)

    obs_meshes = _collect_mesh_objects(obstacles)
    if auto_collect_env:
        seen = {o.name for o in obs_meshes}
        for o in _auto_collect_env_meshes(char_infos, ground_names, ignore_names):
            if o.name not in seen:
                obs_meshes.append(o)
                seen.add(o.name)

    violations = []
    # Hair & delicate face/glasses parts are excluded from broad obstacle/self checks; Scarf, Earmuffs, Body, Limbs ARE checked!
    skip_part_tags = ("Hair", "Bulb", "Rim", "Temple", "Bridge", "Mustache", "Stache", "Beard", "Scruff", "Lens")
    debug_rendered = False

    # Pre-cache static obstacle AABBs/BVHs once at first frame if they are not animated
    scene.frame_set(frames[0])
    dg0 = bpy.context.evaluated_depsgraph_get()
    static_obs = {}
    for ob in obs_meshes:
        is_anim = bool(ob.animation_data and ob.animation_data.action) or bool(ob.parent and ob.parent.animation_data)
        if not is_anim:
            bb = _world_aabb(ob, dg0)
            if bb and bb[5] > -0.3:
                static_obs[ob.name] = (ob, bb, _world_bvh(ob, dg0) if use_bvh else None)

    for fr in frames:
        scene.frame_set(fr)
        dg = bpy.context.evaluated_depsgraph_get()

        # Gather dynamic obstacles (animated props/doors) + pre-cached static obstacles
        obs_frame = list(static_obs.values())
        for ob in obs_meshes:
            if ob.name in static_obs:
                continue
            bb = _world_aabb(ob, dg)
            if bb and bb[5] > -0.3:
                obs_frame.append((ob, bb, _world_bvh(ob, dg) if use_bvh else None))

        # Gather active character part AABBs & lazy BVHs
        char_records = []
        for ci in char_infos:
            arm = ci["armature"]
            if arm.location.z < -0.5:
                continue
            parts = []
            for child in _collect_mesh_objects(list(arm.children) + list(ci.get("collection").objects if ci.get("collection") else [])):
                if any(t in child.name for t in skip_part_tags):
                    continue
                bb = _world_aabb(child, dg)
                if bb:
                    parts.append({"obj": child, "name": child.name, "bb": bb, "bvh": None})
            char_records.append({"arm": arm, "name": arm.name, "loc": arm.location.copy(), "parts": parts})

        def _get_bvh(part_dict, inset=0.0):
            if inset == 0.0:
                if part_dict["bvh"] is None:
                    part_dict["bvh"] = _world_bvh(part_dict["obj"], dg, inset_m=0.0)
                return part_dict["bvh"]
            return _world_bvh(part_dict["obj"], dg, inset_m=inset)

        # 1. Character vs Character (body, head, arms & legs — exact BVHTree confirmation)
        for i in range(len(char_records)):
            ca = char_records[i]
            for j in range(i + 1, len(char_records)):
                cb = char_records[j]
                if (ca["loc"] - cb["loc"]).length > 3.2:
                    continue
                for pa in ca["parts"]:
                    for pb in cb["parts"]:
                        ov = _aabb_overlap_depth(pa["bb"], pb["bb"], margin=0.008)
                        if ov <= 0.012:
                            continue
                        if use_bvh:
                            ba, bb = _get_bvh(pa), _get_bvh(pb)
                            hits = ba.overlap(bb) if (ba and bb) else []
                            if len(hits) < 2:
                                continue
                            violations.append({"frame": fr, "type": "CHAR_CHAR", "a": pa["name"], "b": pb["name"], "depth_m": round(ov, 3), "tris": len(hits)})
                        else:
                            violations.append({"frame": fr, "type": "CHAR_CHAR", "a": pa["name"], "b": pb["name"], "depth_m": round(ov, 3)})

        # 2. Character vs Environment Obstacles (exact BVHTree confirmation)
        for ca in char_records:
            for pa in ca["parts"]:
                for ob, ob_bb, ob_bvh in obs_frame:
                    ov = _aabb_overlap_depth(pa["bb"], ob_bb, margin=0.006)
                    if ov <= 0.015:
                        continue
                    if use_bvh:
                        ba = _get_bvh(pa, inset=0.008)
                        hits = ba.overlap(ob_bvh) if (ba and ob_bvh) else []
                        if len(hits) < 2:
                            continue
                        violations.append({"frame": fr, "type": "CHAR_OBSTACLE", "a": pa["name"], "b": ob.name, "depth_m": round(ov, 3), "tris": len(hits)})
                    else:
                        if ov > margin:
                            violations.append({"frame": fr, "type": "CHAR_OBSTACLE", "a": pa["name"], "b": ob.name, "depth_m": round(ov, 3)})

        # 3. Ground-Sink Check (feet/legs sinking below ground_z)
        if check_ground_sink:
            for ca in char_records:
                for pa in ca["parts"]:
                    if "Leg" in pa["name"] or "Shoe" in pa["name"]:
                        z_min = pa["bb"][4]
                        sink = ground_z - z_min
                        if sink > max_sink_m:
                            violations.append({"frame": fr, "type": "GROUND_SINK", "a": pa["name"], "b": f"ground_z={ground_z:.2f}", "depth_m": round(sink, 3)})

        # 4. Self-Clip Check (arms stabbing into own torso; uses 2.2cm inset so shoulder contact never false-triggers)
        if check_self_clip and use_bvh:
            for ca in char_records:
                torsos = [p for p in ca["parts"] if p["name"].endswith(("_UpperTorso", "_Torso"))]
                arms = [p for p in ca["parts"] if "_Arm" in p["name"]]
                for tr in torsos:
                    bt = _get_bvh(tr, inset=0.022)
                    if not bt:
                        continue
                    for ar in arms:
                        if _aabb_overlap_depth(tr["bb"], ar["bb"], margin=0.018) <= 0.01:
                            continue
                        ba = _get_bvh(ar, inset=0.022)
                        hits = bt.overlap(ba) if ba else []
                        if len(hits) >= 4:
                            violations.append({"frame": fr, "type": "SELF_CLIP", "a": ar["name"], "b": tr["name"], "tris": len(hits)})

        if debug_dir and violations and not debug_rendered:
            v0 = violations[0]
            focus = char_records[0]["loc"] + Vector((0, 0, 0.9)) if char_records else Vector((0, 0, 1.0))
            for ca in char_records:
                for pa in ca["parts"]:
                    if pa["name"] == v0["a"]:
                        b = pa["bb"]
                        focus = Vector((0.5 * (b[0] + b[1]), 0.5 * (b[2] + b[3]), 0.5 * (b[4] + b[5])))
            _render_collision_debug(fr, focus, debug_dir, v0["type"])
            debug_rendered = True

    if strict and violations:
        sample = "; ".join(f"f{v['frame']}:{v['type']}({v['a']} vs {v['b']})" for v in violations[:5])
        raise RuntimeError(f"[Law R-COLLIDE] {len(violations)} collision(s) detected — render blocked! First hits: {sample}")
    return violations


# ==============================================================================
# NATURAL POSE LIBRARY, CORE TARGET-FIRST CAMERA ENGINE & PLAYBLAST MOTION QA
# ==============================================================================

POSE_LIB = {
    # --------------------------------------------------------------------------
    # GROUP A: CONVERSATIONAL & CHARACTER APPEAL (Contrapposto, Zero Twinning)
    # --------------------------------------------------------------------------
    "neutral_relaxed": {
        "_hip_offset": (0.025, 0.0, -0.015),
        "LowerTorso": (2, 3, 4), "UpperTorso": (2, -2, -5), "Head": (-2, 1, 3),
        "RightUpperArm": (-9, 0, -8), "RightLowerArm": (-20, 0, 0),
        "LeftUpperArm": (-5, 0, 7), "LeftLowerArm": (-14, 0, 0),
        "LeftUpperLeg": (0, 0, 0), "LeftLowerLeg": (0, 0, 0), "RightUpperLeg": (0, 0, 0), "RightLowerLeg": (0, 0, 0),
    },
    "confident_stand": {
        "_hip_offset": (-0.03, 0.015, -0.012),
        "LowerTorso": (-2, -3, -5), "UpperTorso": (-6, 3, 6), "Head": (-4, -2, -4),
        "RightUpperArm": (-14, 0, -14), "RightLowerArm": (-26, 0, 0),
        "LeftUpperArm": (-8, 0, 11), "LeftLowerArm": (-18, 0, 0),
        "LeftUpperLeg": (0, 0, 0), "LeftLowerLeg": (0, 0, 0), "RightUpperLeg": (0, 0, 0), "RightLowerLeg": (0, 0, 0),
    },
    "hands_on_hips": {
        "_hip_offset": (0.035, 0.01, -0.018),
        "LowerTorso": (-2, 4, 5), "UpperTorso": (-6, -3, -6), "Head": (-3, 2, 4),
        "RightUpperArm": (-18, 0, -32), "RightLowerArm": (-72, -22, 0),
        "LeftUpperArm": (-14, 0, 26), "LeftLowerArm": (-64, 18, 0),
        "LeftUpperLeg": (0, 0, 0), "LeftLowerLeg": (0, 0, 0), "RightUpperLeg": (0, 0, 0), "RightLowerLeg": (0, 0, 0),
    },
    "cross_arms": {
        "_hip_offset": (-0.03, 0.0, -0.015),
        "LowerTorso": (-1, -3, -4), "UpperTorso": (-5, 2, 5), "Head": (-2, -2, 5),
        "RightUpperArm": (-38, 0, 16), "RightLowerArm": (-84, 34, 0),
        "LeftUpperArm": (-44, 0, -18), "LeftLowerArm": (-78, -32, 0),
    },
    "listening_tilt": {
        "_hip_offset": (0.03, 0.0, -0.016),
        "LowerTorso": (2, 3, 4), "UpperTorso": (4, -2, -5), "Head": (3, 7, 8),
        "RightUpperArm": (-12, 0, -9), "RightLowerArm": (-28, 0, 0),
        "LeftUpperArm": (-6, 0, 7), "LeftLowerArm": (-16, 0, 0),
    },
    "shrug_open": {
        "_hip_offset": (0.02, -0.01, -0.022),
        "LowerTorso": (-2, 2, 3), "UpperTorso": (-5, -2, -4), "Head": (-4, 5, 9),
        "RightUpperArm": (-52, 0, -32), "RightLowerArm": (-58, -12, 0),
        "LeftUpperArm": (-42, 0, 25), "LeftLowerArm": (-48, 10, 0),
    },
    "chin_think": {
        "_hip_offset": (-0.025, 0.0, -0.018),
        "LowerTorso": (2, -3, -4), "UpperTorso": (5, 2, 5), "Head": (9, -3, 7),
        "RightUpperArm": (-58, 0, 18), "RightLowerArm": (-95, 0, 0),
        "LeftUpperArm": (-22, 0, -14), "LeftLowerArm": (-68, -18, 0),
    },
    "scratch_head": {
        "_hip_offset": (0.025, 0.0, -0.02),
        "LowerTorso": (2, 2, 4), "UpperTorso": (5, -3, 6), "Head": (7, -4, -9),
        "RightUpperArm": (-138, 0, 14), "RightLowerArm": (-96, 0, 0),
        "LeftUpperArm": (-12, 0, 10), "LeftLowerArm": (-24, 0, 0),
    },

    # --------------------------------------------------------------------------
    # GROUP B: DRAMATIC CONFLICT & EMOTIONAL EXAGGERATION
    # --------------------------------------------------------------------------
    "point_casual": {
        "_hip_offset": (0.02, 0.02, -0.018),
        "LowerTorso": (3, 2, 4), "UpperTorso": (7, -2, -8), "Head": (-3, 2, 7),
        "RightUpperArm": (-82, 0, -14), "RightLowerArm": (-18, 0, 0),
        "LeftUpperArm": (-14, 0, 11), "LeftLowerArm": (-26, 0, 0),
    },
    "accuse_point": {
        "_hip_offset": (0.03, 0.06, -0.045),
        "LowerTorso": (8, 3, 6), "UpperTorso": (14, -3, -12), "Head": (-6, 3, 10),
        "RightUpperArm": (-96, 0, -10), "RightLowerArm": (-8, 0, 0),
        "LeftUpperArm": (18, 0, 18), "LeftLowerArm": (-34, 0, 0),
    },
    "recoil_shock": {
        "_hip_offset": (-0.03, -0.08, -0.075),
        "LowerTorso": (-8, -4, -6), "UpperTorso": (-15, 4, 9), "Head": (-20, -5, -8),
        "RightUpperArm": (-114, 0, -28), "RightLowerArm": (-64, 0, 0),
        "LeftUpperArm": (-96, 0, 22), "LeftLowerArm": (-52, 0, 0),
    },
    "defensive_step_back": {
        "_hip_offset": (-0.04, -0.06, -0.055),
        "LowerTorso": (-5, -5, -10), "UpperTorso": (-10, 4, 14), "Head": (-8, -4, -12),
        "RightUpperArm": (-76, 0, 14), "RightLowerArm": (-68, 0, 0),
        "LeftUpperArm": (-88, 0, 24), "LeftLowerArm": (-54, 0, 0),
    },
    "facepalm_regret": {
        "_hip_offset": (0.015, -0.02, -0.04),
        "LowerTorso": (6, 2, 3), "UpperTorso": (14, -2, -4), "Head": (18, 4, 5),
        "RightUpperArm": (-118, 0, 20), "RightLowerArm": (-102, 0, 0),
        "LeftUpperArm": (-16, 0, 10), "LeftLowerArm": (-32, 0, 0),
    },
    "laugh_belly": {
        "_hip_offset": (0.02, -0.03, -0.035),
        "LowerTorso": (-6, 3, 4), "UpperTorso": (-14, -3, -5), "Head": (-18, 4, 6),
        "RightUpperArm": (-36, 0, 14), "RightLowerArm": (-78, 22, 0),
        "LeftUpperArm": (-44, 0, -16), "LeftLowerArm": (-74, -20, 0),
    },
    "cheer_victory": {
        "_hip_offset": (0.02, 0.02, 0.025),
        "LowerTorso": (-4, 3, 5), "UpperTorso": (-12, -3, -7), "Head": (-16, 2, 6),
        "RightUpperArm": (-156, 0, -22), "RightLowerArm": (-28, 0, 0),
        "LeftUpperArm": (-142, 0, 18), "LeftLowerArm": (-36, 0, 0),
    },
    "bow_respect": {
        "_hip_offset": (0.0, -0.04, -0.05),
        "LowerTorso": (18, 0, 0), "UpperTorso": (26, 0, 0), "Head": (14, 0, 0),
        "RightUpperArm": (-28, 0, 16), "RightLowerArm": (-76, 24, 0),
        "LeftUpperArm": (-30, 0, -16), "LeftLowerArm": (-74, -24, 0),
    },

    # --------------------------------------------------------------------------
    # GROUP C: ENVIRONMENT & ARCHITECTURAL INTERACTION (Bell Tower / Monuments)
    # --------------------------------------------------------------------------
    "look_up_awe": {
        "_hip_offset": (-0.02, -0.02, -0.02),
        "LowerTorso": (-5, -2, -4), "UpperTorso": (-14, 2, 6), "Head": (-28, -3, -5),
        "RightUpperArm": (-24, 0, -22), "RightLowerArm": (-32, 0, 0),
        "LeftUpperArm": (-18, 0, 16), "LeftLowerArm": (-24, 0, 0),
    },
    "lean_balustrade": {
        "_hip_offset": (0.02, 0.08, -0.045),
        "LowerTorso": (14, 2, 3), "UpperTorso": (18, -2, -4), "Head": (-8, 3, 6),
        "RightUpperArm": (-64, 0, -14), "RightLowerArm": (-56, -12, 0),
        "LeftUpperArm": (-58, 0, 12), "LeftLowerArm": (-62, 10, 0),
    },
    "lean_inspect": {
        "_hip_offset": (0.02, 0.07, -0.06),
        "LowerTorso": (14, 3, 5), "UpperTorso": (18, -2, -6), "Head": (14, 2, 6),
        "RightUpperArm": (-52, 0, -14), "RightLowerArm": (-38, 0, 0),
        "LeftUpperArm": (-36, 0, 12), "LeftLowerArm": (-42, 0, 0),
    },
    "reach_offer": {
        "_hip_offset": (0.025, 0.04, -0.025),
        "LowerTorso": (4, 2, 5), "UpperTorso": (8, -2, -8), "Head": (-2, 2, 6),
        "RightUpperArm": (-68, 0, -8), "RightLowerArm": (-24, 0, 0),
        "LeftUpperArm": (-14, 0, 10), "LeftLowerArm": (-28, 0, 0),
    },

    # --------------------------------------------------------------------------
    # GROUP D: KINETIC ACTION & MARTIAL / COMBAT
    # --------------------------------------------------------------------------
    "combat_guard": {
        "_hip_offset": (-0.04, -0.02, -0.095),
        "LowerTorso": (6, -5, -14), "UpperTorso": (10, 4, 22), "Head": (-6, -4, -18),
        "RightUpperArm": (-68, 0, -18), "RightLowerArm": (-88, 0, 0),
        "LeftUpperArm": (-82, 0, 16), "LeftLowerArm": (-72, 0, 0),
    },
    "draw_weapon": {
        "_hip_offset": (-0.03, -0.03, -0.065),
        "LowerTorso": (4, -4, 12), "UpperTorso": (8, 4, -22), "Head": (-4, -3, 16),
        "RightUpperArm": (-42, 0, 26), "RightLowerArm": (-94, 28, 0),
        "LeftUpperArm": (-32, 0, 18), "LeftLowerArm": (-46, 0, 0),
    },
    "strike_slash": {
        "_hip_offset": (0.04, 0.09, -0.085),
        "LowerTorso": (12, 4, -10), "UpperTorso": (18, -4, 24), "Head": (-8, 3, -14),
        "RightUpperArm": (-108, 0, -24), "RightLowerArm": (-14, 0, 0),
        "LeftUpperArm": (24, 0, 22), "LeftLowerArm": (-42, 0, 0),
    },
    "sprint_start": {
        "_hip_offset": (0.0, 0.08, -0.09),
        "LowerTorso": (16, 0, -6), "UpperTorso": (22, 0, 10), "Head": (-12, 0, -4),
        "RightUpperArm": (-76, 0, -12), "RightLowerArm": (-64, 0, 0),
        "LeftUpperArm": (42, 0, 12), "LeftLowerArm": (-52, 0, 0),
    },
}


def apply_pose_lib(char_info: dict, frame: int, pose_name: str, dur: int = 10,
                   loc=None, yaw_deg: float = None, anticipate: bool = True,
                   arc_breakdown: bool = True, overshoot: float = 0.07,
                   hold_frames: int = 18, lock_feet_ik: bool = True, **overrides):
    """
    Transition smoothly to a curated POSE_LIB entry enforcing all 12 Principles of Animation:
    - Contrapposto asymmetry & zero twinning
    - Foot IK ground lock (`0.000m` foot sliding during hip compression/sway)
    - 3-frame reverse anticipation + midpoint circular breakdown arc
    - Staggered Hips -> Chest (+1f) -> Arms (+2f w/ Overshoot) -> Head (+3f) overlap
    - Moving Hold micro-breathing settle across `hold_frames`.
    """
    arm = char_info["armature"]
    # (lock_feet_ik used the removed mocap/IK hybrid rig; kept as a no-op argument for call compatibility.
    #  Use RobloxAnimator for acting — it keeps feet planted by construction.)
    pose = dict(POSE_LIB.get(pose_name, POSE_LIB["neutral_relaxed"]))
    pose.update(overrides)
    snap_r15_pose(
        arm, frame, snap_frames=dur, overshoot=overshoot,
        loc=loc, yaw_deg=yaw_deg, stagger=True,
        anticipate=anticipate, arc_breakdown=arc_breakdown,
        hold_frames=hold_frames, **pose
    )


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
    old_cyc_samp = sc.cycles.samples if hasattr(sc, "cycles") and hasattr(sc.cycles, "samples") else None
    sc.render.resolution_percentage = int(round(res_scale * 100))
    if old_samp is not None:
        sc.eevee.taa_render_samples = samples
    if old_cyc_samp is not None:
        sc.cycles.samples = max(2, samples)
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
    if old_cyc_samp is not None:
        sc.cycles.samples = old_cyc_samp
    return pb_dir


# ==============================================================================
# IMPACT PHYSICS, HIT-STOP & PROCEDURAL VFX ENGINE (BLENDER 5.3)
# ==============================================================================

def _get_vfx_collection(col=None):
    if col is not None:
        return col
    c = bpy.data.collections.get("VFX_Impacts")
    if not c:
        c = bpy.data.collections.new("VFX_Impacts")
        bpy.context.scene.collection.children.link(c)
    return c


def make_emissive_vfx_mat(name: str, color_hex: str = "#FFB830", strength: float = 40.0, roughness: float = 0.25):
    """Create a glowing emissive VFX material compatible with Cycles, EEVEE, and Workbench."""
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name=name)
    rgba = hex_to_linear_rgba(color_hex)
    mat.diffuse_color = rgba
    nt = mat.node_tree
    bsdf = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if bsdf:
        bsdf.inputs["Base Color"].default_value = rgba
        bsdf.inputs["Roughness"].default_value = roughness
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = rgba
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = strength
    return mat


def enable_compositor_bloom(threshold: float = 2.8, strength: float = 0.22):
    """Configure Blender 5.0-5.3 Compositor Glare (Fog Glow / Bloom) so emissive VFX glow organically."""
    scene = bpy.context.scene
    scene.use_nodes = True
    try:
        ng = bpy.data.node_groups.get("Sven_VFX_Comp") or bpy.data.node_groups.new("Sven_VFX_Comp", "CompositorNodeTree")
        scene.compositing_node_group = ng
        ng.nodes.clear()
        if not any(item.in_out == "OUTPUT" for item in ng.interface.items_tree):
            ng.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
        rl = ng.nodes.new("CompositorNodeRLayers")
        glare = ng.nodes.new("CompositorNodeGlare")
        out = ng.nodes.new("NodeGroupOutput")
        if hasattr(glare, "glare_type"):
            glare.glare_type = "FOG_GLOW"
        for sock_name, val in (("Type", "Fog Glow"), ("Threshold", threshold), ("Strength", strength), ("Size", 7)):
            if sock_name in glare.inputs:
                try:
                    glare.inputs[sock_name].default_value = val
                except Exception:
                    pass
        ng.links.new(rl.outputs["Image"], glare.inputs["Image"])
        ng.links.new(glare.outputs["Image"], out.inputs[0])
        return True
    except Exception:
        return False


def _set_fcurve_interp(obj, frame: int, interp: str = "LINEAR"):
    if not obj.animation_data or not obj.animation_data.action:
        return
    for fc in iter_action_fcurves(obj.animation_data.action):
        for kp in fc.keyframe_points:
            if int(round(kp.co.x)) == frame:
                if interp == "VECTOR":
                    kp.interpolation = "BEZIER"
                    kp.handle_left_type = "VECTOR"
                    kp.handle_right_type = "VECTOR"
                else:
                    kp.interpolation = interp
        fc.update()


def spawn_impact_light_flash(
    impact_frame: int,
    impact_loc,
    color_hex: str = "#FFA830",
    peak_watts: float = 160.0,
    dur_frames: int = 6,
    col=None,
):
    """
    Interactive Point Light Flash at impact_loc:
    0W at impact_frame-1 -> peak_watts at impact_frame (LINEAR snap) -> 0W at impact_frame+dur_frames.
    """
    vfx_col = _get_vfx_collection(col)
    rgba = hex_to_linear_rgba(color_hex)
    ldata = bpy.data.lights.new(f"VFX_Flash_{impact_frame}", type="POINT")
    ldata.color = (rgba[0], rgba[1], rgba[2])
    ldata.shadow_soft_size = 0.28
    lob = bpy.data.objects.new(f"VFX_Flash_{impact_frame}", ldata)
    lob.location = Vector(impact_loc)
    vfx_col.objects.link(lob)

    f_pre = max(1, impact_frame - 1)
    f_end = impact_frame + max(2, dur_frames)
    for fr, val in ((1, 0.0), (f_pre, 0.0), (impact_frame, float(peak_watts)), (impact_frame + 1, float(peak_watts * 0.65)), (f_end, 0.0)):
        ldata.energy = val
        ldata.keyframe_insert(data_path="energy", frame=fr)
    if ldata.animation_data and ldata.animation_data.action:
        for fc in iter_action_fcurves(ldata.animation_data.action):
            for kp in fc.keyframe_points:
                kp.interpolation = "LINEAR"
            fc.update()
    return lob


def spawn_impact_sparks(
    impact_frame: int,
    impact_loc,
    normal=(0.0, -1.0, 0.75),
    count: int = 18,
    speed_m: float = 4.6,
    dur_frames: int = 11,
    color_hex: str = "#FFC038",
    emission_strength: float = 48.0,
    gravity_m: float = 13.5,
    col=None,
) -> list:
    """
    Spawn 3D velocity-aligned emissive spark streaks bursting outward from impact_loc at impact_frame.
    Each streak stays at scale (0,0,0) prior to impact_frame, launches at full velocity on impact_frame,
    curves downward under gravity, and burns out to scale (0,0,0) at impact_frame + dur_frames.
    """
    vfx_col = _get_vfx_collection(col)
    mat = make_emissive_vfx_mat(f"M_VFX_Spark_{color_hex.lstrip('#')}", color_hex=color_hex, strength=emission_strength)
    p0 = Vector(impact_loc)
    n_dir = Vector(normal).normalized() if Vector(normal).length > 1e-4 else Vector((0, 0, 1))
    up = Vector((0, 0, 1)) if abs(n_dir.z) < 0.95 else Vector((1, 0, 0))
    t1 = n_dir.cross(up).normalized()
    t2 = n_dir.cross(t1).normalized()

    # Shared low-poly 3-sided streak mesh oriented along local +Z
    me = bpy.data.meshes.get("VFX_SparkStreak_Mesh")
    if not me:
        bm = bmesh.new()
        add__cone = bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=True, segments=4, radius1=0.022, radius2=0.004, depth=0.28)
        me = bpy.data.meshes.new("VFX_SparkStreak_Mesh")
        bm.to_mesh(me)
        bm.free()
        me.materials.append(mat)

    sparks = []
    f_pre = max(1, impact_frame - 1)
    fps = float(bpy.context.scene.render.fps or 30.0)
    for i in range(count):
        # Deterministic pseudo-random cone directions (Fibonacci hemisphere around n_dir)
        phi = i * 2.3999632
        spread = 0.25 + 0.68 * ((i % 7) / 6.0)
        v_dir = (n_dir * 0.85 + (t1 * math.cos(phi) + t2 * math.sin(phi)) * spread).normalized()
        v_mag = speed_m * (0.65 + 0.65 * (((i * 17) % 11) / 10.0))
        vel0 = v_dir * v_mag

        ob = bpy.data.objects.new(f"VFX_Spark_{impact_frame}_{i:02d}", me)
        vfx_col.objects.link(ob)

        # Hide before impact
        ob.location = p0
        ob.scale = (0.0, 0.0, 0.0)
        ob.keyframe_insert("location", frame=1)
        ob.keyframe_insert("scale", frame=1)
        ob.keyframe_insert("location", frame=f_pre)
        ob.keyframe_insert("scale", frame=f_pre)
        _set_fcurve_interp(ob, f_pre, "CONSTANT")

        life_f = max(4, int(round(dur_frames * (0.72 + 0.35 * ((i % 5) / 4.0)))))
        for k in range(life_f + 1):
            fr = impact_frame + k
            dt = k / fps
            u = k / float(life_f)
            pos = p0 + vel0 * dt + Vector((0.0, 0.0, -0.5 * gravity_m * dt * dt))
            inst_vel = vel0 + Vector((0.0, 0.0, -gravity_m * dt))
            ob.location = pos
            if inst_vel.length > 1e-4:
                ob.rotation_euler = inst_vel.normalized().to_track_quat("Z", "Y").to_euler()
                ob.keyframe_insert("rotation_euler", frame=fr)
            sc_xy = max(0.0, 1.0 - pow(u, 1.6))
            sc_z = max(0.0, (1.15 - u) * (inst_vel.length / max(1.0, speed_m)))
            if k == life_f:
                sc_xy, sc_z = 0.0, 0.0
            ob.scale = (sc_xy, sc_xy, sc_z)
            ob.keyframe_insert("location", frame=fr)
            ob.keyframe_insert("scale", frame=fr)
            _set_fcurve_interp(ob, fr, "LINEAR")

        sparks.append(ob)
    return sparks


def spawn_dust_shockwave(
    impact_frame: int,
    impact_loc,
    max_radius_m: float = 1.45,
    dur_frames: int = 12,
    puff_count: int = 10,
    ring_color_hex: str = "#FFE4B5",
    dust_color_hex: str = "#D8CFC4",
    emission_strength: float = 10.0,
    col=None,
) -> list:
    """
    Spawn a fast-expanding ground/air shockwave ring + perimeter billowy dust cloud puffs at impact_frame.
    Follows Disney/anime fast-out cubic expansion R(u) = R_max * (1 - (1 - u)^3) with clean scale dissolve.
    """
    vfx_col = _get_vfx_collection(col)
    mat_ring = make_emissive_vfx_mat(f"M_VFX_ShockRing_{ring_color_hex.lstrip('#')}", color_hex=ring_color_hex, strength=emission_strength)
    mat_dust = make_solid_mat(f"M_VFX_Dust_{dust_color_hex.lstrip('#')}", hex_to_linear_rgba(dust_color_hex), roughness=0.88)

    p0 = Vector(impact_loc)
    f_pre = max(1, impact_frame - 1)
    created = []

    # 1. Expanding Shockwave Torus Ring
    bm_r = bmesh.new()
    segs, minor_segs = 28, 8
    R0, r0 = 1.0, 0.055
    rings = []
    for i in range(segs):
        a = 2.0 * math.pi * i / segs
        ca, sa = math.cos(a), math.sin(a)
        c_pt = Vector((ca * R0, sa * R0, 0.0))
        rad_dir = Vector((ca, sa, 0.0))
        ring = []
        for j in range(minor_segs):
            b = 2.0 * math.pi * j / minor_segs
            pt = c_pt + rad_dir * (math.cos(b) * r0) + Vector((0.0, 0.0, math.sin(b) * r0 * 0.55))
            ring.append(bm_r.verts.new(pt))
        rings.append(ring)
    for i in range(segs):
        ni = (i + 1) % segs
        for j in range(minor_segs):
            nj = (j + 1) % minor_segs
            bm_r.faces.new((rings[i][j], rings[ni][j], rings[ni][nj], rings[i][nj]))
    me_r = bpy.data.meshes.new(f"VFX_ShockRing_{impact_frame}_M")
    bm_r.to_mesh(me_r); bm_r.free()
    for poly in me_r.polygons:
        poly.use_smooth = True
    me_r.materials.append(mat_ring)
    ring_ob = bpy.data.objects.new(f"VFX_ShockRing_{impact_frame}", me_r)
    ring_ob.location = p0 + Vector((0.0, 0.0, 0.04))
    vfx_col.objects.link(ring_ob)
    created.append(ring_ob)

    ring_ob.scale = (0.0, 0.0, 0.0)
    ring_ob.keyframe_insert("scale", frame=1)
    ring_ob.keyframe_insert("scale", frame=f_pre)
    _set_fcurve_interp(ring_ob, f_pre, "CONSTANT")

    for k in range(dur_frames + 1):
        fr = impact_frame + k
        u = k / float(max(1, dur_frames))
        # Fast-out cubic expansion
        rad_s = max_radius_m * (0.12 + 0.88 * (1.0 - pow(1.0 - u, 3.0)))
        thick_s = max(0.0, 1.0 - pow(u, 1.4))
        if k == dur_frames:
            rad_s, thick_s = 0.0, 0.0
        ring_ob.scale = (rad_s, rad_s, thick_s)
        ring_ob.keyframe_insert("scale", frame=fr)
        _set_fcurve_interp(ring_ob, fr, "LINEAR")

    # 2. Perimeter Dust Cloud Puffs
    me_p = bpy.data.meshes.get("VFX_DustPuff_Mesh")
    if not me_p:
        bm_p = bmesh.new()
        bmesh.ops.create_icosphere(bm_p, subdivisions=2, radius=0.22)
        me_p = bpy.data.meshes.new("VFX_DustPuff_Mesh")
        bm_p.to_mesh(me_p); bm_p.free()
        for poly in me_p.polygons:
            poly.use_smooth = True
        me_p.materials.append(mat_dust)

    for i in range(puff_count):
        ang = (2.0 * math.pi * i / max(1, puff_count)) + (i % 3) * 0.14
        dir_xy = Vector((math.cos(ang), math.sin(ang), 0.0))
        p_ob = bpy.data.objects.new(f"VFX_DustPuff_{impact_frame}_{i:02d}", me_p)
        vfx_col.objects.link(p_ob)
        created.append(p_ob)

        p_ob.location = p0
        p_ob.scale = (0.0, 0.0, 0.0)
        p_ob.keyframe_insert("location", frame=1)
        p_ob.keyframe_insert("scale", frame=1)
        p_ob.keyframe_insert("location", frame=f_pre)
        p_ob.keyframe_insert("scale", frame=f_pre)
        _set_fcurve_interp(p_ob, f_pre, "CONSTANT")

        p_life = dur_frames + (i % 3) * 2
        for k in range(p_life + 1):
            fr = impact_frame + k
            u = k / float(max(1, p_life))
            ease_out = 1.0 - pow(1.0 - u, 2.6)
            dist = max_radius_m * (0.20 + 0.78 * ease_out)
            lift = 0.08 + 0.26 * ease_out
            p_ob.location = p0 + dir_xy * dist + Vector((0.0, 0.0, lift))
            # Puff swells quickly to peak at u=0.3, then shrinks away cleanly
            sc = math.sin(math.pi * pow(u, 0.65)) * (1.15 if i % 2 == 0 else 0.88)
            if k == p_life:
                sc = 0.0
            p_ob.scale = (sc * 1.15, sc * 1.15, sc * 0.82)
            p_ob.keyframe_insert("location", frame=fr)
            p_ob.keyframe_insert("scale", frame=fr)
            _set_fcurve_interp(p_ob, fr, "LINEAR")

    return created


def spawn_energy_slash_arc(
    impact_frame: int,
    center_loc,
    yaw_deg: float = 0.0,
    tilt_deg: float = 22.0,
    radius_m: float = 0.92,
    dur_frames: int = 7,
    color_hex: str = "#38D8FF",
    emission_strength: float = 55.0,
    col=None,
):
    """
    Spawn a glowing crescent 3D energy blade/strike wave at impact_frame - 1 that sweeps forward
    through impact_frame and dissipates cleanly by impact_frame + dur_frames.
    """
    vfx_col = _get_vfx_collection(col)
    mat = make_emissive_vfx_mat(f"M_VFX_Slash_{color_hex.lstrip('#')}", color_hex=color_hex, strength=emission_strength)

    bm = bmesh.new()
    arc_segs = 20
    arc_span = math.radians(135.0)
    top_v, bot_v, edge_v, back_v = [], [], [], []
    for i in range(arc_segs + 1):
        u = -0.5 + (i / float(arc_segs))
        ang = u * arc_span
        taper = math.cos(u * math.pi)
        r_out = radius_m * (1.0 + 0.08 * taper)
        r_in = radius_m - (0.04 + 0.24 * taper)
        thick = 0.015 + 0.045 * taper
        ca, sa = math.cos(ang), math.sin(ang)
        edge_v.append(bm.verts.new((sa * r_out, -ca * r_out, 0.0)))
        back_v.append(bm.verts.new((sa * r_in, -ca * r_in, 0.0)))
        rm = 0.5 * (r_out + r_in)
        top_v.append(bm.verts.new((sa * rm, -ca * rm, thick)))
        bot_v.append(bm.verts.new((sa * rm, -ca * rm, -thick)))

    for i in range(arc_segs):
        bm.faces.new((edge_v[i], edge_v[i + 1], top_v[i + 1], top_v[i]))
        bm.faces.new((top_v[i], top_v[i + 1], back_v[i + 1], back_v[i]))
        bm.faces.new((back_v[i], back_v[i + 1], bot_v[i + 1], bot_v[i]))
        bm.faces.new((bot_v[i], bot_v[i + 1], edge_v[i + 1], edge_v[i]))
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0005)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)

    me = bpy.data.meshes.new(f"VFX_SlashArc_{impact_frame}_M")
    bm.to_mesh(me); bm.free()
    for poly in me.polygons:
        poly.use_smooth = True
    me.materials.append(mat)

    ob = bpy.data.objects.new(f"VFX_SlashArc_{impact_frame}", me)
    vfx_col.objects.link(ob)

    p0 = Vector(center_loc)
    f_start = max(1, impact_frame - 1)
    f_pre = max(1, f_start - 1)
    rot_e = Euler((math.radians(tilt_deg), math.radians(18.0), math.radians(yaw_deg)), "XYZ")
    fwd = Euler((0.0, 0.0, math.radians(yaw_deg))).to_matrix() @ Vector((0.0, -1.0, 0.0))

    ob.location = p0
    ob.rotation_euler = rot_e
    ob.scale = (0.0, 0.0, 0.0)
    ob.keyframe_insert("location", frame=1)
    ob.keyframe_insert("scale", frame=1)
    ob.keyframe_insert("location", frame=f_pre)
    ob.keyframe_insert("scale", frame=f_pre)
    _set_fcurve_interp(ob, f_pre, "CONSTANT")

    for k in range(dur_frames + 1):
        fr = f_start + k
        u = k / float(max(1, dur_frames))
        ob.location = p0 + fwd * (0.55 * (1.0 - pow(1.0 - u, 2.2)))
        ob.rotation_euler = Euler((rot_e.x, rot_e.y, rot_e.z + math.radians(28.0 * u)), "XYZ")
        sc_xy = 0.65 + 0.55 * (1.0 - pow(1.0 - u, 2.0))
        sc_z = max(0.0, 1.0 - pow(u, 1.3))
        if k == dur_frames:
            sc_xy, sc_z = 0.0, 0.0
        ob.scale = (sc_xy, sc_xy, sc_z)
        ob.keyframe_insert("location", frame=fr)
        ob.keyframe_insert("rotation_euler", frame=fr)
        ob.keyframe_insert("scale", frame=fr)
        _set_fcurve_interp(ob, fr, "LINEAR")

    return ob


def trigger_physical_impact(
    impact_frame: int,
    impact_loc,
    attacker: dict = None,
    victim: dict = None,
    camera=None,
    vfx_preset: str = "heavy_hit",
    hit_stop_frames: int = 2,
    knockback_m: float = 0.42,
    spark_color_hex: str = "#FFB830",
    slash_color_hex: str = "#38D8FF",
    col=None,
) -> dict:
    """
    The All-in-One Impact Synchronization Triad Orchestrator:
    1. Attacker: Wind-up anticipation -> VECTOR strike arrival at impact_frame -> Hit-Stop freeze (hit_stop_frames).
    2. Victim: Holds pre-hit stance until impact_frame, compresses during Hit-Stop, then launches into
       asymmetric Staggered Recoil + physical knockback slide starting at impact_frame + hit_stop_frames.
    3. VFX Burst: Spawns synchronized Impact Sparks, Ground/Air Dust Shockwave, optional Energy Slash Arc,
       and an interactive 4200W Point Light Flash at impact_loc.
    4. Camera & Compositor: Triggers damped trauma shake on `camera` at impact_frame and enables Compositor Bloom.
    """
    p_hit = Vector(impact_loc)
    hs_f = max(1, int(hit_stop_frames))
    vfx_objs = []

    # 1. Attacker Strike & Hit-Stop Freeze
    if attacker and "armature" in attacker:
        arm_a = attacker["armature"]
        bpy.context.scene.frame_set(max(1, impact_frame - 6))
        loc_a = arm_a.location.copy()
        yaw_a = math.degrees(arm_a.rotation_euler.z)
        # Anticipation coil at impact_frame - 5
        if impact_frame >= 6:
            apply_pose_lib(attacker, impact_frame - 6, "draw_weapon", dur=3, loc=loc_a, yaw_deg=yaw_a,
                           anticipate=False, arc_breakdown=False, overshoot=0.0, hold_frames=0)
        # Snap strike arrival at impact_frame with VECTOR handle
        strike_pose = dict(POSE_LIB["strike_slash"])
        key_r15_pose(arm_a, impact_frame, loc=loc_a, yaw_deg=yaw_a, interpolation="VECTOR",
                     hip_offset=strike_pose.get("_hip_offset"), **strike_pose)
        # Hit-Stop Freeze across [impact_frame .. impact_frame + hs_f]
        key_r15_pose(arm_a, impact_frame + hs_f, loc=loc_a, yaw_deg=yaw_a, interpolation="BEZIER",
                     hip_offset=strike_pose.get("_hip_offset"), **strike_pose)
        # Follow-through recovery settle
        apply_pose_lib(attacker, impact_frame + hs_f + 2, "combat_guard", dur=10, loc=loc_a, yaw_deg=yaw_a,
                       anticipate=False, arc_breakdown=True, overshoot=0.05, hold_frames=14)

    # 2. Victim Hit-Stop Compression -> Staggered Recoil & Knockback Slide
    if victim and "armature" in victim:
        arm_v = victim["armature"]
        bpy.context.scene.frame_set(max(1, impact_frame - 1))
        loc_v0 = arm_v.location.copy()
        yaw_v = math.degrees(arm_v.rotation_euler.z)
        # Direction away from impact_loc (or backward along victim's facing)
        push_dir = Vector((loc_v0.x - p_hit.x, loc_v0.y - p_hit.y, 0.0))
        if push_dir.length < 1e-3:
            push_dir = Euler((0.0, 0.0, math.radians(yaw_v))).to_matrix() @ Vector((0.0, 1.0, 0.0))
        push_dir.normalize()
        loc_v_end = loc_v0 + push_dir * knockback_m

        # Hold pre-impact position right up to impact_frame
        arm_v.location = loc_v0
        arm_v.keyframe_insert("location", frame=max(1, impact_frame - 1))
        # At impact_frame .. impact_frame + hs_f: Initial impact compression (head & chest take the blow first)
        hit_compress = {
            "LowerTorso": (-3, -2, -4), "UpperTorso": (-18, 5, 10), "Head": (-24, -6, -10),
            "RightUpperArm": (-45, 0, -18), "RightLowerArm": (-40, 0, 0),
            "LeftUpperArm": (-38, 0, 16), "LeftLowerArm": (-36, 0, 0),
        }
        key_r15_pose(arm_v, impact_frame, loc=loc_v0, yaw_deg=yaw_v, interpolation="VECTOR",
                     hip_offset=(-0.02, -0.04, -0.085), **hit_compress)
        key_r15_pose(arm_v, impact_frame + hs_f, loc=loc_v0 + push_dir * (knockback_m * 0.12), yaw_deg=yaw_v,
                     interpolation="VECTOR", hip_offset=(-0.02, -0.05, -0.095), **hit_compress)
        # Release from Hit-Stop into full Recoil Shock + Knockback slide (Unlock foot IK during slide if sliding > 0.15m)
        recoil_pose = dict(POSE_LIB["recoil_shock"])
        snap_r15_pose(
            arm_v, impact_frame + hs_f, snap_frames=9, overshoot=0.10,
            loc=loc_v_end, yaw_deg=yaw_v, stagger=True, anticipate=False,
            arc_breakdown=True, hold_frames=16, **recoil_pose
        )

    # 3. Synchronized VFX Burst + Interactive Point Light Flash
    vfx_col = _get_vfx_collection(col)
    flash_color = slash_color_hex if vfx_preset in ("energy_slash", "sword_slash") else spark_color_hex
    vfx_objs.append(spawn_impact_light_flash(impact_frame, p_hit, color_hex=flash_color, peak_watts=160.0, dur_frames=6, col=vfx_col))

    if vfx_preset in ("heavy_hit", "spark_clash", "energy_slash", "sword_slash", "explosion"):
        vfx_objs.extend(spawn_impact_sparks(
            impact_frame, p_hit, count=20 if vfx_preset != "spark_clash" else 28,
            speed_m=4.8, dur_frames=11, color_hex=spark_color_hex, col=vfx_col
        ))
    if vfx_preset in ("heavy_hit", "ground_slam", "explosion"):
        ground_pt = Vector((p_hit.x, p_hit.y, max(0.03, p_hit.z - 0.65))) if vfx_preset in ("heavy_hit", "explosion") else p_hit
        vfx_objs.extend(spawn_dust_shockwave(
            impact_frame, ground_pt, max_radius_m=1.45 if vfx_preset == "heavy_hit" else 2.2,
            dur_frames=12, puff_count=10, ring_color_hex=spark_color_hex, col=vfx_col
        ))
    if vfx_preset in ("energy_slash", "sword_slash", "heavy_hit", "explosion"):
        yaw_s = math.degrees(attacker["armature"].rotation_euler.z) if (attacker and "armature" in attacker) else 0.0
        vfx_objs.append(spawn_energy_slash_arc(
            impact_frame, p_hit, yaw_deg=yaw_s, radius_m=0.92, dur_frames=7, color_hex=slash_color_hex, col=vfx_col
        ))

    # 4. Camera Trauma Shake & Blender 5.3 Compositor Bloom
    if camera is not None:
        add_camera_shake(camera, impact_frame, amp_m=0.055, amp_deg=1.8, dur_frames=11)
    enable_compositor_bloom(threshold=2.8, strength=0.22)

    return {
        "impact_frame": impact_frame,
        "hit_stop_end": impact_frame + hs_f,
        "impact_loc": tuple(p_hit),
        "vfx_count": len(vfx_objs),
        "preset": vfx_preset,
    }


def eval_ballistic_bounce(pos0: Vector, vel0: Vector, ang_vel: Vector, dt: float, half_z: float, gravity: float = 18.0):
    """
    Universal 3D projectile trajectory solver with ground plane collision (z = half_z),
    2 energy-damping restitution bounces (e1=0.40, e2=0.22), and friction skid decay.
    """
    if dt <= 0.0:
        return pos0.copy(), Euler((0.0, 0.0, 0.0), "XYZ")
    dz = max(0.0, pos0.z - half_z)
    disc = vel0.z * vel0.z + 2.0 * gravity * dz
    t_hit1 = (vel0.z + math.sqrt(max(0.0, disc))) / gravity
    vz_impact1 = math.sqrt(max(0.0, disc))
    vz1 = vz_impact1 * 0.40
    t_b1 = 2.0 * vz1 / gravity
    vz2 = vz1 * 0.45
    t_b2 = 2.0 * vz2 / gravity

    if dt <= t_hit1:
        x = pos0.x + vel0.x * dt
        y = pos0.y + vel0.y * dt
        z = pos0.z + vel0.z * dt - 0.5 * gravity * dt * dt
        rt = dt
    elif dt <= t_hit1 + t_b1:
        u = dt - t_hit1
        x = pos0.x + vel0.x * t_hit1 + vel0.x * 0.60 * u
        y = pos0.y + vel0.y * t_hit1 + vel0.y * 0.60 * u
        z = half_z + vz1 * u - 0.5 * gravity * u * u
        rt = t_hit1 + u * 0.60
    elif dt <= t_hit1 + t_b1 + t_b2:
        u = dt - (t_hit1 + t_b1)
        x = pos0.x + vel0.x * (t_hit1 + 0.60 * t_b1) + vel0.x * 0.30 * u
        y = pos0.y + vel0.y * (t_hit1 + 0.60 * t_b1) + vel0.y * 0.30 * u
        z = half_z + vz2 * u - 0.5 * gravity * u * u
        rt = t_hit1 + 0.60 * t_b1 + u * 0.32
    else:
        u = min(0.45, dt - (t_hit1 + t_b1 + t_b2))
        skid = u * (1.0 - u / 0.9)
        x = pos0.x + vel0.x * (t_hit1 + 0.60 * t_b1 + 0.30 * t_b2 + 0.16 * skid)
        y = pos0.y + vel0.y * (t_hit1 + 0.60 * t_b1 + 0.30 * t_b2 + 0.16 * skid)
        z = half_z
        rt = t_hit1 + 0.60 * t_b1 + 0.32 * t_b2 + 0.15 * skid

    return Vector((x, y, max(half_z, z))), Euler((ang_vel.x * rt, ang_vel.y * rt, ang_vel.z * rt), "XYZ")


def add_shoes_3d(char_info: dict, shoe_hex: str = "#BC5E9A", sole_hex: str = "#3A1D32"):
    """Attach sculpted 3D rounded slippers/shoes onto LeftLowerLeg and RightLowerLeg (protruding toe cap + sole)."""
    arm = char_info["armature"]
    col = char_info["collection"]
    m = char_info["metrics"]
    tw = m["tw"]
    lw = m.get("lw", 1.0)
    leg_x = 0.255 * tw
    mat_shoe = make_solid_mat(f"{arm.name}_Shoe3D", hex_to_linear_rgba(shoe_hex), roughness=0.42)
    mat_sole = make_solid_mat(f"{arm.name}_Sole3D", hex_to_linear_rgba(sole_hex), roughness=0.65)
    created = []
    for sgn, bname in ((-1.0, "RightLowerLeg"), (1.0, "LeftLowerLeg")):
        ox = sgn * leg_x * STUD
        # Rounded slipper upper protruding slightly forward (-Y)
        bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=1.0)
        for v in bm.verts:
            v.co.x *= 1.06 * lw * STUD
            v.co.y *= 1.22 * lw * STUD
            v.co.z *= 0.32 * STUD
        me = bpy.data.meshes.new(f"{arm.name}_{bname}_Shoe_M")
        bm.to_mesh(me); bm.free()
        ob = bpy.data.objects.new(f"{arm.name}_{bname}_Shoe", me)
        ob.location = (ox, -0.10 * lw * STUD, 0.16 * STUD)
        ob.data.materials.append(mat_shoe)
        bev = ob.modifiers.new("Bevel", "BEVEL")
        bev.width = 0.018; bev.segments = 3
        for p in ob.data.polygons:
            p.use_smooth = True
        col.objects.link(ob)
        created.append((ob, bname))
        # Thin dark sole
        bm_s = bmesh.new()
        bmesh.ops.create_cube(bm_s, size=1.0)
        for v in bm_s.verts:
            v.co.x *= 1.08 * lw * STUD
            v.co.y *= 1.24 * lw * STUD
            v.co.z *= 0.07 * STUD
        me_s = bpy.data.meshes.new(f"{arm.name}_{bname}_Sole_M")
        bm_s.to_mesh(me_s); bm_s.free()
        ob_s = bpy.data.objects.new(f"{arm.name}_{bname}_Sole", me_s)
        ob_s.location = (ox, -0.10 * lw * STUD, 0.035 * STUD)
        ob_s.data.materials.append(mat_sole)
        col.objects.link(ob_s)
        created.append((ob_s, bname))

    bpy.context.view_layer.update()
    for ob, bn in created:
        ob.matrix_world = arm.matrix_world @ ob.matrix_world
        wm = ob.matrix_world.copy()
        ob.parent = arm
        ob.matrix_parent_inverse = arm.matrix_world.inverted()
        ob.matrix_world = wm
        vg = ob.vertex_groups.new(name=bn)
        vg.add(list(range(len(ob.data.vertices))), 1.0, "REPLACE")
        mod = ob.modifiers.new("Armature", "ARMATURE")
        mod.object = arm
    return [o for o, _ in created]


def add_jacket_collar_3d(char_info: dict, collar_hex: str = "#265CB0"):
    """Attach 3D raised jacket collar triangles framing the neck/scarf on UpperTorso (matching té5666.mp4)."""
    arm = char_info["armature"]
    col = char_info["collection"]
    m = char_info["metrics"]
    neck_z = m["neck_z"]
    mat_c = make_solid_mat(f"{arm.name}_Collar3D", hex_to_linear_rgba(collar_hex), roughness=0.48)
    created = []
    for sgn, tag in ((-1.0, "R"), (1.0, "L")):
        bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=1.0)
        for v in bm.verts:
            v.co.x *= 0.14 * STUD
            v.co.y *= 0.56 * STUD
            v.co.z *= 0.36 * STUD
            if v.co.z > 0:
                v.co.y -= 0.12 * STUD
        me = bpy.data.meshes.new(f"{arm.name}_Collar_{tag}_M")
        bm.to_mesh(me); bm.free()
        ob = bpy.data.objects.new(f"{arm.name}_Collar_{tag}", me)
        ob.location = (sgn * 0.68 * STUD, -0.06 * STUD, (neck_z + 0.10) * STUD)
        ob.rotation_euler = Euler((math.radians(-10), math.radians(sgn * 18), 0))
        ob.data.materials.append(mat_c)
        bev = ob.modifiers.new("Bevel", "BEVEL")
        bev.width = 0.006; bev.segments = 2
        for p in ob.data.polygons:
            p.use_smooth = True
        col.objects.link(ob)
        created.append(ob)

    bpy.context.view_layer.update()
    for ob in created:
        ob.matrix_world = arm.matrix_world @ ob.matrix_world
        wm = ob.matrix_world.copy()
        ob.parent = arm
        ob.matrix_parent_inverse = arm.matrix_world.inverted()
        ob.matrix_world = wm
        vg = ob.vertex_groups.new(name="UpperTorso")
        vg.add(list(range(len(ob.data.vertices))), 1.0, "REPLACE")
        mod = ob.modifiers.new("Armature", "ARMATURE")
        mod.object = arm
    return created


def spawn_3d_liquid_splat(
    impact_frame: int,
    impact_loc,
    dark_hex: str = "#25160B",
    mid_hex: str = "#4A2F18",
    scale_mult: float = 1.0,
    dur_frames: int = 18,
    col=None,
) -> list:
    """
    Spawn a 3D Glossy Liquid/Mud Splash Crown (8 curved petals) + 14 Ballistic Droplets + Expanding Surface Ripple Ring.
    """
    vfx_col = _get_vfx_collection(col)
    mat_liq = make_wet_pbr_ground(f"M_VFX_Liquid_{dark_hex.lstrip('#')}", dark_hex=dark_hex, light_hex=mid_hex, scale=4.5, bump_strength=0.35)
    mat_foam = make_solid_mat(f"M_VFX_Ripple_{mid_hex.lstrip('#')}", hex_to_linear_rgba("#8C7A68"), roughness=0.25)
    p0 = Vector(impact_loc)
    f_pre = max(1, impact_frame - 1)
    fps = float(bpy.context.scene.render.fps or 30.0)
    created = []

    for i in range(8):
        ang = 2.0 * math.pi * i / 8.0 + (i % 2) * 0.15
        dir_xy = Vector((math.cos(ang), math.sin(ang), 0.0))
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=0.11 * scale_mult, location=p0)
        pet = bpy.context.active_object
        pet.name = f"VFX_SplatPetal_{impact_frame}_{i}"
        for v in pet.data.vertices:
            v.co.z *= 1.85
            v.co.x *= 0.65
        for p in pet.data.polygons:
            p.use_smooth = True
        pet.data.materials.append(mat_liq)
        for c in list(pet.users_collection):
            c.objects.unlink(pet)
        vfx_col.objects.link(pet)
        created.append(pet)

        pet.scale = (0.0, 0.0, 0.0)
        pet.keyframe_insert("scale", frame=1)
        pet.keyframe_insert("scale", frame=f_pre)
        _set_fcurve_interp(pet, f_pre, "CONSTANT")

        for k in range(dur_frames + 1):
            fr = impact_frame + k
            u = k / float(max(1, dur_frames))
            rad = (0.12 + 0.34 * (1.0 - (1.0 - u) ** 2.4)) * scale_mult
            hz = 0.26 * scale_mult * math.sin(math.pi * (u ** 0.72))
            pet.location = p0 + dir_xy * rad + Vector((0.0, 0.0, hz))
            pet.rotation_euler = Euler((math.sin(ang) * (0.4 + 0.7 * u), -math.cos(ang) * (0.4 + 0.7 * u), ang), "XYZ")
            sc = math.sin(math.pi * (u ** 0.65)) * (1.15 if i % 2 == 0 else 0.90)
            if k == dur_frames:
                sc = 0.0
            pet.scale = (sc, sc, sc)
            pet.keyframe_insert("location", frame=fr)
            pet.keyframe_insert("rotation_euler", frame=fr)
            pet.keyframe_insert("scale", frame=fr)

    for i in range(14):
        ang = i * 2.39996
        spd_xy = (0.6 + 1.1 * ((i % 5) / 4.0)) * scale_mult
        vz = (2.2 + 1.8 * ((i % 4) / 3.0)) * scale_mult
        vel = Vector((math.cos(ang) * spd_xy, math.sin(ang) * spd_xy, vz))
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=0.055 * scale_mult, location=p0)
        dr = bpy.context.active_object
        dr.name = f"VFX_SplatDrop_{impact_frame}_{i}"
        for p in dr.data.polygons:
            p.use_smooth = True
        dr.data.materials.append(mat_liq)
        for c in list(dr.users_collection):
            c.objects.unlink(dr)
        vfx_col.objects.link(dr)
        created.append(dr)

        dr.scale = (0.0, 0.0, 0.0)
        dr.keyframe_insert("scale", frame=1)
        dr.keyframe_insert("scale", frame=f_pre)
        _set_fcurve_interp(dr, f_pre, "CONSTANT")

        life = dur_frames + 4
        for k in range(life + 1):
            fr = impact_frame + k
            dt = k / fps
            u = k / float(life)
            pos = p0 + vel * dt + Vector((0.0, 0.0, -0.5 * 16.0 * dt * dt))
            pos.z = max(0.01, pos.z)
            dr.location = pos
            sc = 1.0 - (u ** 2.2) if k < life else 0.0
            dr.scale = (sc, sc, sc)
            dr.keyframe_insert("location", frame=fr)
            dr.keyframe_insert("scale", frame=fr)

    bpy.ops.mesh.primitive_torus_add(
        major_segments=32, minor_segments=8, major_radius=0.35 * scale_mult, minor_radius=0.022 * scale_mult,
        location=p0 + Vector((0.0, 0.0, 0.012))
    )
    rip = bpy.context.active_object
    rip.name = f"VFX_SplatRipple_{impact_frame}"
    for p in rip.data.polygons:
        p.use_smooth = True
    rip.data.materials.append(mat_foam)
    for c in list(rip.users_collection):
        c.objects.unlink(rip)
    vfx_col.objects.link(rip)
    created.append(rip)

    rip.scale = (0.0, 0.0, 0.0)
    rip.keyframe_insert("scale", frame=1)
    rip.keyframe_insert("scale", frame=f_pre)
    _set_fcurve_interp(rip, f_pre, "CONSTANT")
    for k in range(dur_frames + 4):
        fr = impact_frame + k
        u = k / float(dur_frames + 3)
        rs = 0.35 + 1.45 * (1.0 - (1.0 - u) ** 2.5)
        zs = max(0.0, 1.0 - u ** 1.4)
        if k == dur_frames + 3:
            rs, zs = 0.0, 0.0
        rip.scale = (rs, rs, zs)
        rip.keyframe_insert("scale", frame=fr)

    return created


# ---------------------------------------------------------------------------
# Sven Core Auto-Director Extensions (Blockout, 20-Preset Camera Path,
# Multi-Angle Stdlib Contact Sheet QA, & 5-Family Humanoid Retargeting)
# ---------------------------------------------------------------------------
try:
    from blender_auto_director import (
        PRESETS as CAMERA_PATH_PRESETS,
        blockout_llm_prompt,
        build_blockout_scene,
        build_camera_path,
        capture_views_sheet,
        clear_blockout_scene,
        encode_blockout_rows,
        fit_distance,
        frame_camera,
        parse_blockout_plan,
        plan_from_text,
    )
except ImportError:
    pass




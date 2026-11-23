#!/usr/bin/env python3
"""
roblox_json_to_glb.py — Convert models extracted from Roblox Studio (studio_kit/harvest_extract.lua: Parts, MeshParts,
SpecialMesh FileMeshes via EditableMesh, texture colours baked to vertex colours) into clean, ground-aligned .glb files
for Blender 5.3. Host-side driver: tools/harvest_assets.py (search → insert → sanitize → extract → convert → catalog).

Blender CLI (run through blender -b --factory-startup -P roblox_json_to_glb.py -- …):
  convert <model.json> <out.glb> [--preview <png>]     one model → .glb (+ 3/4-view preview render)
  preview <model.glb> <out.png>                       3/4-view preview of an existing .glb
  measure <out.json> <a.glb> [<b.glb> …]              write {path: {dims_m, tris, materials}} for the catalog
"""
import json
import math
import os
import sys
import bpy
import bmesh
from mathutils import Matrix, Vector, Euler

STUD = 0.28
# Rigid +90deg X rotation: (x, y, z)_roblox -> (x, -z, y)_blender (det = +1, keeps winding clean)
Q_R2B = Matrix.Rotation(math.radians(90.0), 4, "X")


def _srgb_to_lin(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _make_roblox_material(name: str, col_rgb, mat_name: str, tr: float = 0.0, ref: float = 0.0, use_vc: bool = False):
    r, g, b = [c / 255.0 for c in col_rgb]
    lr, lg, lb = _srgb_to_lin(r), _srgb_to_lin(g), _srgb_to_lin(b)
    key = f"RBX_{mat_name}_{col_rgb[0]}_{col_rgb[1]}_{col_rgb[2]}_{int(tr*100)}{'_vc' if use_vc else ''}"
    if key in bpy.data.materials:
        return bpy.data.materials[key]

    mat = bpy.data.materials.new(key)
    mat.use_nodes = True
    nt = mat.node_tree
    bsdf = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = (lr, lg, lb, 1.0)
    if use_vc:  # texture colours baked per vertex (glTF COLOR_0 multiplies the base colour)
        vc = nt.nodes.new("ShaderNodeVertexColor")
        vc.layer_name = "Col"
        nt.links.new(vc.outputs["Color"], bsdf.inputs["Base Color"])

    mn = mat_name.lower()
    if "neon" in mn:
        bsdf.inputs["Roughness"].default_value = 0.2
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (lr, lg, lb, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 3.5
    elif "metal" in mn or "diamondplate" in mn:
        bsdf.inputs["Metallic"].default_value = 0.88
        bsdf.inputs["Roughness"].default_value = 0.26
    elif "glass" in mn or tr >= 0.15:
        bsdf.inputs["Roughness"].default_value = 0.06
        if "Transmission Weight" in bsdf.inputs:
            bsdf.inputs["Transmission Weight"].default_value = 0.65 if tr > 0.1 else 0.0
        bsdf.inputs["Alpha"].default_value = max(0.28, 1.0 - tr)
        mat.blend_method = "BLEND" if hasattr(mat, "blend_method") else "HASHED"
    elif "fabric" in mn:
        bsdf.inputs["Roughness"].default_value = 0.88
        if "Sheen Weight" in bsdf.inputs:
            bsdf.inputs["Sheen Weight"].default_value = 0.45
    elif "wood" in mn:
        bsdf.inputs["Roughness"].default_value = 0.58
    elif "smoothplastic" in mn:
        bsdf.inputs["Metallic"].default_value = max(0.0, min(0.75, ref * 0.9))
        bsdf.inputs["Roughness"].default_value = max(0.10, 0.28 - ref * 0.18)
    else:
        bsdf.inputs["Roughness"].default_value = 0.46
    return mat


def _cf_to_mat4(cf_arr) -> Matrix:
    x, y, z, r00, r01, r02, r10, r11, r12, r20, r21, r22 = cf_arr
    return Matrix((
        (r00, r01, r02, x),
        (r10, r11, r12, y),
        (r20, r21, r22, z),
        (0.0, 0.0, 0.0, 1.0),
    ))


def build_from_json(json_path: str, col):
    data = json.load(open(json_path, encoding="utf-8"))
    model_name = data["name"]
    meshes_dict = data.get("meshes") or {}
    parts = data["parts"]

    any_vc = any((m or {}).get("c") for m in meshes_dict.values())
    created_objs = []
    for idx, p in enumerate(parts):
        bm = bmesh.new()
        sz = p["sz"]
        mid = p.get("mid")
        mdata = meshes_dict.get(mid) if mid else None

        if mdata and mdata.get("v") and mdata.get("f"):
            verts_flat = mdata["v"]
            faces_flat = mdata["f"]
            ext = mdata["ext"]
            if p.get("ms"):  # SpecialMesh FileMesh: rendered size = mesh units × Scale (independent of part size)
                sx, sy, sz_s = p["ms"]
            else:            # MeshPart: mesh bounds are stretched to the part Size
                sx = sz[0] / ext[0] if isinstance(ext[0], (int, float)) and abs(ext[0]) > 1e-5 else 1.0
                sy = sz[1] / ext[1] if isinstance(ext[1], (int, float)) and abs(ext[1]) > 1e-5 else 1.0
                sz_s = sz[2] / ext[2] if isinstance(ext[2], (int, float)) and abs(ext[2]) > 1e-5 else 1.0
            vcols = mdata.get("c")
            vc_layer = bm.verts.layers.float_color.new("Col") if vcols else None
            bm_verts = []
            for i in range(0, len(verts_flat), 3):
                vx, vy, vz = verts_flat[i], verts_flat[i + 1], verts_flat[i + 2]
                if isinstance(vx, (int, float)) and isinstance(vy, (int, float)) and isinstance(vz, (int, float)):
                    bv = bm.verts.new((vx * sx, vy * sy, vz * sz_s))
                    if vc_layer is not None:
                        c = vcols[i // 3] if i // 3 < len(vcols) else 0xFFFFFF
                        bv[vc_layer] = (_srgb_to_lin(((c >> 16) & 255) / 255.0), _srgb_to_lin(((c >> 8) & 255) / 255.0),
                                        _srgb_to_lin((c & 255) / 255.0), 1.0)
                    bm_verts.append(bv)
                else:
                    bm_verts.append(None)
            bm.verts.ensure_lookup_table()
            for i in range(0, len(faces_flat), 3):
                v0, v1, v2 = bm_verts[faces_flat[i]], bm_verts[faces_flat[i + 1]], bm_verts[faces_flat[i + 2]]
                if v0 is not None and v1 is not None and v2 is not None:
                    try:
                        bm.faces.new((v0, v1, v2))
                    except ValueError:
                        pass
            bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_faces], context="VERTS")
            bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        else:
            shape = p.get("shape", "Block")
            sm_type = p.get("smType")
            sm_scale = p.get("smScale")
            eff_sz = list(sz)
            if sm_scale:
                eff_sz = [sz[0] * sm_scale[0], sz[1] * sm_scale[1], sz[2] * sm_scale[2]]

            if shape == "Cylinder" or sm_type == "Cylinder":
                # Roblox Cylinder axis is local X! Length=eff_sz[0], Diameter=min(eff_sz[1], eff_sz[2])
                rad = 0.5 * min(eff_sz[1], eff_sz[2])
                bmesh.ops.create_cone(
                    bm, cap_ends=True, cap_tris=False, segments=20,
                    radius1=rad, radius2=rad, depth=eff_sz[0],
                    matrix=Matrix.Rotation(math.radians(90.0), 4, "Y"),
                )
            elif shape == "Ball" or sm_type == "Sphere":
                bmesh.ops.create_uvsphere(bm, u_segments=16, v_segments=12, radius=0.5)
                bmesh.ops.scale(bm, vec=Vector(eff_sz), verts=bm.verts)
            elif shape == "Wedge" or sm_type == "Wedge":
                hx, hy, hz = eff_sz[0] * 0.5, eff_sz[1] * 0.5, eff_sz[2] * 0.5
                # Roblox WedgePart: sloped from (+Y, +Z) down to (-Y, -Z)
                v0 = bm.verts.new((-hx, -hy, -hz))
                v1 = bm.verts.new((hx, -hy, -hz))
                v2 = bm.verts.new((hx, -hy, hz))
                v3 = bm.verts.new((-hx, -hy, hz))
                v4 = bm.verts.new((-hx, hy, hz))
                v5 = bm.verts.new((hx, hy, hz))
                bm.faces.new((v0, v3, v2, v1))  # Bottom (-Y)
                bm.faces.new((v3, v4, v5, v2))  # Back (+Z)
                bm.faces.new((v0, v1, v5, v4))  # Slope
                bm.faces.new((v0, v4, v3))      # Left (-X)
                bm.faces.new((v1, v2, v5))      # Right (+X)
                bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
            else:
                bmesh.ops.create_cube(bm, size=1.0)
                bmesh.ops.scale(bm, vec=Vector(eff_sz), verts=bm.verts)
                if min(eff_sz) > 0.08:
                    bmesh.ops.bevel(bm, geom=list(bm.edges), offset=min(eff_sz) * 0.035, segments=1, affect="EDGES")

        # Transform vertices from Part local Roblox space -> Model local Blender meters (Z-up)
        cf_m = _cf_to_mat4(p["cf"])
        xform = Matrix.Scale(STUD, 4) @ Q_R2B @ cf_m
        bmesh.ops.transform(bm, matrix=xform, verts=bm.verts)

        mesh_d = bpy.data.meshes.new(f"{model_name}_{idx}")
        bm.to_mesh(mesh_d)
        bm.free()

        for poly in mesh_d.polygons:
            poly.use_smooth = True

        has_vc = "Col" in mesh_d.color_attributes
        if any_vc and not has_vc:  # every joined part needs the layer, else the join fills it with black
            attr = mesh_d.color_attributes.new("Col", "FLOAT_COLOR", "POINT")
            for d in attr.data:
                d.color = (1.0, 1.0, 1.0, 1.0)
        obj = bpy.data.objects.new(f"{model_name}_{idx}_{p['n'][:18]}", mesh_d)
        mat = _make_roblox_material(p["n"], p["col"], p["mat"], p.get("tr", 0.0), p.get("ref", 0.0), use_vc=has_vc)
        obj.data.materials.append(mat)
        col.objects.link(obj)
        created_objs.append(obj)

    # Join into 1 clean multi-material mesh with origin grounded at bottom-center (0, 0, 0)
    if not created_objs:
        return None
    bpy.ops.object.select_all(action="DESELECT")
    for o in created_objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = created_objs[0]
    bpy.ops.object.join()
    merged = bpy.context.view_layer.objects.active
    merged.name = model_name

    # Re-center XY and set Z bottom = 0.0
    xs = [v.co.x for v in merged.data.vertices]
    ys = [v.co.y for v in merged.data.vertices]
    zs = [v.co.z for v in merged.data.vertices]
    cx, cy, min_z = 0.5 * (min(xs) + max(xs)), 0.5 * (min(ys) + max(ys)), min(zs)
    for v in merged.data.vertices:
        v.co.x -= cx
        v.co.y -= cy
        v.co.z -= min_z
    merged.data.update()
    return merged


def export_glb(obj, out_glb: str):
    os.makedirs(os.path.dirname(os.path.abspath(out_glb)), exist_ok=True)
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.export_scene.gltf(filepath=out_glb, use_selection=True, export_format="GLB")
    return os.path.getsize(out_glb)


def render_preview(obj, out_png: str, size: int = 512):
    """3/4 view on a neutral floor, fitted to the model bounds (for the catalog contact sheet)."""
    sc = bpy.context.scene
    engines = {e.identifier for e in sc.render.bl_rna.properties["engine"].enum_items}
    sc.render.engine = "BLENDER_EEVEE" if "BLENDER_EEVEE" in engines else "BLENDER_EEVEE_NEXT"
    sc.render.resolution_x = sc.render.resolution_y = size
    world = bpy.data.worlds.new("PrevWorld")
    world.use_nodes = True
    bg = world.node_tree.nodes.get("Background")
    bg.inputs["Color"].default_value = (0.62, 0.68, 0.76, 1.0)
    bg.inputs["Strength"].default_value = 0.9
    sc.world = world
    dims = obj.dimensions
    r = max(dims.x, dims.y, dims.z, 0.1)
    bpy.ops.mesh.primitive_plane_add(size=r * 8, location=(0, 0, 0))
    floor = bpy.context.active_object
    fm = bpy.data.materials.new("PrevFloor")
    fm.use_nodes = True
    next(n for n in fm.node_tree.nodes if n.type == "BSDF_PRINCIPLED").inputs["Base Color"].default_value = (0.32, 0.33, 0.35, 1)
    floor.data.materials.append(fm)
    sun_d = bpy.data.lights.new("PrevSun", "SUN")
    sun_d.energy = 3.2
    sun = bpy.data.objects.new("PrevSun", sun_d)
    sun.rotation_euler = Euler((math.radians(50), 0, math.radians(35)))
    sc.collection.objects.link(sun)
    cam_d = bpy.data.cameras.new("PrevCam")
    cam_d.lens = 50
    cam = bpy.data.objects.new("PrevCam", cam_d)
    sc.collection.objects.link(cam)
    sc.camera = cam
    ctr = Vector((0, 0, dims.z * 0.5))
    d = Vector((math.cos(math.radians(-55)), math.sin(math.radians(-55)), 0.55)).normalized()
    cam.location = ctr + d * r * 2.3
    cam.rotation_euler = (ctr - cam.location).to_track_quat("-Z", "Y").to_euler()
    os.makedirs(os.path.dirname(os.path.abspath(out_png)), exist_ok=True)
    sc.render.filepath = out_png
    bpy.ops.render.render(write_still=True)


def _mesh_stats(objs):
    tris = sum(sum(len(p.vertices) - 2 for p in o.data.polygons) for o in objs if o.type == "MESH")
    mats = {m.name for o in objs if o.type == "MESH" for m in o.data.materials if m}
    xs, ys, zs = [], [], []
    for o in objs:
        if o.type != "MESH":
            continue
        for c in o.bound_box:
            w = o.matrix_world @ Vector(c)
            xs.append(w.x); ys.append(w.y); zs.append(w.z)
    dims = [round(max(a) - min(a), 3) for a in (xs, ys, zs)] if xs else [0, 0, 0]
    return {"dims_m": dims, "tris": tris, "materials": len(mats)}


def cli(argv):
    if not argv:
        print(__doc__)
        return 2
    cmd = argv[0]
    if cmd == "convert":
        src, out_glb = argv[1], argv[2]
        preview = argv[argv.index("--preview") + 1] if "--preview" in argv else None
        bpy.ops.wm.read_factory_settings(use_empty=True)
        obj = build_from_json(src, bpy.context.scene.collection)
        if obj is None:
            print("@@JSON@@" + json.dumps({"ok": False, "error": "no visible parts"}))
            return 1
        nbytes = export_glb(obj, out_glb)
        info = dict(_mesh_stats([obj]), ok=True, glb=out_glb, bytes=nbytes)
        if preview:
            render_preview(obj, preview)
            info["preview"] = preview
        print("@@JSON@@" + json.dumps(info))
        return 0
    if cmd == "preview":  # existing .glb → preview png (catalog --previews)
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=argv[1])
        meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
        if not meshes:
            print("@@JSON@@" + json.dumps({"ok": False, "error": "no meshes"}))
            return 1
        bpy.ops.object.select_all(action="DESELECT")
        for o in meshes:
            o.select_set(True)
        bpy.context.view_layer.objects.active = meshes[0]
        bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
        if len(meshes) > 1:
            bpy.ops.object.join()
        obj = bpy.context.view_layer.objects.active
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        render_preview(obj, argv[2])
        print("@@JSON@@" + json.dumps({"ok": True, "preview": argv[2]}))
        return 0
    if cmd == "measure":
        out_json, res = argv[1], {}
        for g in argv[2:]:
            bpy.ops.wm.read_factory_settings(use_empty=True)
            try:
                bpy.ops.import_scene.gltf(filepath=g)
                res[g] = _mesh_stats(list(bpy.context.scene.objects))
            except Exception as e:  # keep measuring the rest
                res[g] = {"error": str(e)[:200]}
        json.dump(res, open(out_json, "w", encoding="utf-8"), indent=1)
        print("@@JSON@@" + json.dumps({"ok": True, "measured": len(res)}))
        return 0
    print(f"unknown command {cmd}")
    return 2


if __name__ == "__main__":
    _argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    sys.exit(cli(_argv))



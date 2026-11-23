#!/usr/bin/env python3
"""
roblox_json_to_glb.py — Convert extracted Roblox Studio JSON models (Parts, MeshParts, EditableMesh)
into clean, ground-aligned, PBR-shaded .glb files stored in roblox-director/assets/ for Blender 5.3.
"""
import json
import math
import os
import shutil
import sys
import bpy
import bmesh
from mathutils import Matrix, Vector, Euler

KIT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, KIT_DIR)
import blender_roblox_kit as kit  # noqa: E402
import blender_env_lighting as env_kit  # noqa: E402
import blender_roblox_anim as rba  # noqa: E402

STUD = 0.28
# Rigid +90deg X rotation: (x, y, z)_roblox -> (x, -z, y)_blender (det = +1, keeps winding clean)
Q_R2B = Matrix.Rotation(math.radians(90.0), 4, "X")


def _srgb_to_lin(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _make_roblox_material(name: str, col_rgb, mat_name: str, tr: float = 0.0, ref: float = 0.0):
    r, g, b = [c / 255.0 for c in col_rgb]
    lr, lg, lb = _srgb_to_lin(r), _srgb_to_lin(g), _srgb_to_lin(b)
    key = f"RBX_{mat_name}_{col_rgb[0]}_{col_rgb[1]}_{col_rgb[2]}_{int(tr*100)}"
    if key in bpy.data.materials:
        return bpy.data.materials[key]

    mat = bpy.data.materials.new(key)
    mat.use_nodes = True
    nt = mat.node_tree
    bsdf = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = (lr, lg, lb, 1.0)

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
            sx = sz[0] / ext[0] if isinstance(ext[0], (int, float)) and abs(ext[0]) > 1e-5 else 1.0
            sy = sz[1] / ext[1] if isinstance(ext[1], (int, float)) and abs(ext[1]) > 1e-5 else 1.0
            sz_s = sz[2] / ext[2] if isinstance(ext[2], (int, float)) and abs(ext[2]) > 1e-5 else 1.0
            bm_verts = []
            for i in range(0, len(verts_flat), 3):
                vx, vy, vz = verts_flat[i], verts_flat[i + 1], verts_flat[i + 2]
                if isinstance(vx, (int, float)) and isinstance(vy, (int, float)) and isinstance(vz, (int, float)):
                    bm_verts.append(bm.verts.new((vx * sx, vy * sy, vz * sz_s)))
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

        obj = bpy.data.objects.new(f"{model_name}_{idx}_{p['n'][:18]}", mesh_d)
        mat = _make_roblox_material(p["n"], p["col"], p["mat"], p.get("tr", 0.0), p.get("ref", 0.0))
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


def main():
    scratch = r"C:\Users\adminb\.gemini\antigravity\brain\aa681843-8fde-4f4e-a614-7b90ca406cf5\scratch"
    stage_dir = kit.get_stage_dir("roblox_core_showcase")
    stage_glb = os.path.join(stage_dir, "core_glb")
    os.makedirs(stage_glb, exist_ok=True)
    targets = [
        ("Prop_SchoolDeskChair", "props", os.path.join(kit.CORE_ASSETS_DIR, "props", "Prop_SchoolDeskChair.glb")),
        ("Prop_Car_RobloxResources", "props", os.path.join(kit.CORE_ASSETS_DIR, "props", "Prop_Car_RobloxResources.glb")),
        ("Set_LivingRoom", "sets", os.path.join(kit.CORE_ASSETS_DIR, "sets", "Set_LivingRoom.glb")),
    ]
    exported = []
    staged_glbs = {}
    for name, cat, out_glb in targets:
        bpy.ops.wm.read_factory_settings(use_empty=True)
        col = bpy.context.scene.collection
        obj = build_from_json(os.path.join(scratch, f"{name}.json"), col)
        tmp_glb = os.path.join(stage_glb, f"{name}.glb")
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.export_scene.gltf(filepath=tmp_glb, use_selection=True, export_format="GLB")
        staged_glbs[name] = tmp_glb
        dims = tuple(round(v, 3) for v in obj.dimensions)
        exported.append({"name": name, "cat": cat, "tmp_glb": tmp_glb, "core_glb": out_glb, "bytes": os.path.getsize(tmp_glb), "dims_m": dims})

    # Also render a quick Blender 5.3 RTX showcase with R15 cast standing next to the imported Roblox .glb assets!
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col_env = bpy.data.collections.new("Environment")
    bpy.context.scene.collection.children.link(col_env)
    sc = bpy.context.scene
    sc.render.resolution_x = 1280
    sc.render.resolution_y = 720
    sc.render.resolution_percentage = 100
    sc.render.fps = 30
    if hasattr(sc, "eevee") and hasattr(sc.eevee, "taa_render_samples"):
        sc.eevee.taa_render_samples = 12

    env_kit.apply_cinematic_mood(col_env, mood="golden_day", sun_azimuth_deg=135.0)
    env_kit.build_suburban_street_set(col_env, mood="golden_day", make_wet_road_fn=kit.make_wet_pbr_ground)

    # Import Car onto asphalt street, Desk + LivingRoom on sidewalk/yard
    bpy.ops.import_scene.gltf(filepath=staged_glbs["Prop_Car_RobloxResources"])
    car_obj = bpy.context.selected_objects[0]
    car_obj.location = (-1.1, -1.65, 0.0)
    car_obj.rotation_euler = Euler((0.0, 0.0, math.radians(-85.0)))

    bpy.ops.import_scene.gltf(filepath=staged_glbs["Prop_SchoolDeskChair"])
    desk_obj = bpy.context.selected_objects[0]
    desk_obj.location = (2.35, 1.05, 0.08)
    desk_obj.rotation_euler = Euler((0.0, 0.0, math.radians(15.0)))

    sigma = kit.build_roblox_character(
        "Sigma", os.path.join(kit.CORE_CLOTHES_DIR, "shirt_mayor.png"), os.path.join(kit.CORE_CLOTHES_DIR, "pants_mayor.png"),
        os.path.join(kit.CORE_FACES_STORYBOOK_DIR, "smirk.png"),
        skin_hex="#ECC094", hair_hex="#1E2028",
        location_m=(-0.15, 0.65, 0.08), yaw_deg=18,
        body_profile="boy_athletic", hair_style="slick_part", accessories=["stubble_scruff"],
    )
    pony = kit.build_roblox_character(
        "Pony", os.path.join(kit.CORE_CLOTHES_DIR, "shirt_c1.png"), os.path.join(kit.CORE_CLOTHES_DIR, "pants_p1.png"),
        os.path.join(kit.CORE_FACES_STORYBOOK_DIR, "happy.png"),
        skin_hex="#F4C7A1", hair_hex="#8B3A2B",
        location_m=(1.05, 0.70, 0.08), yaw_deg=-15,
        body_profile="girl_slim", hair_style="long_ponytail",
        accessories=[{"acc_type": "glasses_round", "color_hex": "#22252A"}],
    )
    rba.RobloxAnimator(sigma, fps=30).add("wave", 0.0, 2.0).bake(frame_start=1, frame_end=30)
    rba.RobloxAnimator(pony, fps=30).add("clap", 0.0, 2.0).bake(frame_start=1, frame_end=30)

    cam_d = bpy.data.cameras.new("MainCam")
    cam_d.lens = 34.0
    cam = bpy.data.objects.new("MainCam", cam_d)
    col_env.objects.link(cam)
    sc.camera = cam
    cam.location = (0.65, -5.6, 1.55)
    cam.rotation_euler = Euler((math.radians(82), 0.0, math.radians(4)))

    sc.frame_set(9)
    stage_dir = kit.get_stage_dir("roblox_core_showcase")
    out_png = os.path.join(stage_dir, "mixamo_test", "roblox_creator_store_auto.png")
    os.makedirs(os.path.dirname(out_png), exist_ok=True)
    sc.render.filepath = out_png
    bpy.ops.render.render(write_still=True)

    print("@@JSON@@" + json.dumps({"ok": True, "exported": exported, "preview": out_png}))


if __name__ == "__main__":
    main()

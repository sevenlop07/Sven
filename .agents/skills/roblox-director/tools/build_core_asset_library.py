#!/usr/bin/env python3
"""
build_core_asset_library.py — Batch Converts Roblox Creator Store JSONs + Pre-Baked Stylized-PBR
Hybrid Cinema Models into Permanent .glb Files inside .agents/skills/roblox-director/assets/
"""
import glob
import json
import math
import os
import random
import shutil
import sys
import tempfile

import bpy
import bmesh
from mathutils import Vector, Euler

HERE = os.path.dirname(os.path.abspath(__file__))
KIT_DIR = os.path.normpath(os.path.join(HERE, "..", "studio_kit"))
ASSETS_DIR = os.path.normpath(os.path.join(HERE, "..", "assets"))
if KIT_DIR not in sys.path:
    sys.path.insert(0, KIT_DIR)

import roblox_json_to_glb as r2g
import blender_env_lighting as env


def _set_bsdf(bsdf, name, val):
    sock = bsdf.inputs.get(name)
    if sock is not None:
        sock.default_value = val


def make_mat(name, color, roughness=0.45, metallic=0.0, coat=0.0, coat_rough=0.05,
             emission=None, emission_strength=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    rgba = (color[0], color[1], color[2], 1.0) if len(color) == 3 else color
    _set_bsdf(bsdf, "Base Color", rgba)
    _set_bsdf(bsdf, "Roughness", roughness)
    _set_bsdf(bsdf, "Metallic", metallic)
    _set_bsdf(bsdf, "Coat Weight", coat)
    _set_bsdf(bsdf, "Coat Roughness", coat_rough)
    if emission and emission_strength > 0:
        _set_bsdf(bsdf, "Emission Color", (emission[0], emission[1], emission[2], 1.0))
        _set_bsdf(bsdf, "Emission Strength", emission_strength)
    return m


def _export_active_collection_to_glb(stage_dir: str, rel_dest: str) -> tuple:
    tmp_glb = os.path.join(stage_dir, "glbs", rel_dest)
    os.makedirs(os.path.dirname(tmp_glb), exist_ok=True)
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.export_scene.gltf(filepath=tmp_glb, use_selection=True, export_format="GLB")
    return tmp_glb, os.path.getsize(tmp_glb)


def bake_stylized_hybrid_assets(stage_dir: str) -> list:
    """Bakes 8 high-detail Stylized-PBR Hybrid Roblox Cinema .glb models (zero runtime Subsurf overhead)."""
    baked = []

    # 1. Nature_StylizedPine_Hybrid.glb (Chunky 4-tier soft-beveled pine tree like té5666.mp4)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col = bpy.context.scene.collection
    mat_bark = make_mat("HybridBark", (0.14, 0.085, 0.05), roughness=0.78)
    mat_p1 = make_mat("HybridPineDark", (0.045, 0.125, 0.055), roughness=0.46, coat=0.28)
    mat_p2 = make_mat("HybridPineMid", (0.065, 0.165, 0.070), roughness=0.42, coat=0.28)

    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.24, depth=2.2, location=(0, 0, 1.1))
    tr = bpy.context.active_object
    tr.data.materials.append(mat_bark)
    for tier in range(4):
        tz = 1.85 + tier * 1.15
        trad = 1.70 - tier * 0.32
        th = 1.90 - tier * 0.22
        bpy.ops.mesh.primitive_cone_add(vertices=24, radius1=trad, radius2=0.10, depth=th, location=(0, 0, tz))
        cn = bpy.context.active_object
        bv = cn.modifiers.new("Bevel", "BEVEL")
        bv.width = 0.06
        bv.segments = 2
        bpy.context.view_layer.objects.active = cn
        bpy.ops.object.modifier_apply(modifier=bv.name)
        for p in cn.data.polygons:
            p.use_smooth = True
        cn.data.materials.append(mat_p1 if tier % 2 == 0 else mat_p2)
    dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join("nature", "Nature_StylizedPine_Hybrid.glb"))
    baked.append(("Nature_StylizedPine_Hybrid.glb", sz))

    # 2. Nature_StylizedBoulder_Moss.glb (Pre-subdivided craggy mossy river boulder)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col = bpy.context.scene.collection
    mat_moss = make_mat("HybridMossRock", (0.075, 0.145, 0.058), roughness=0.38, coat=0.35)
    rng = random.Random(77)
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=4, radius=1.0)
    for v in bm.verts:
        nx, ny, nz = v.co.x, v.co.y, v.co.z
        crag = 1.0 + 0.20 * math.sin(nx * 3.5 + 1.1) * math.cos(ny * 3.2 + 0.7) + 0.12 * math.cos(nz * 4.2)
        v.co.x *= 1.15 * crag
        v.co.y *= 0.88 * crag
        v.co.z = (nz * 0.58 * crag * (0.55 if nz < -0.15 else 1.0)) + 0.32
    me = bpy.data.meshes.new("BoulderMoss")
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = bpy.data.objects.new("BoulderMoss", me)
    col.objects.link(ob)
    ob.data.materials.append(mat_moss)
    dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join("nature", "Nature_StylizedBoulder_Moss.glb"))
    baked.append(("Nature_StylizedBoulder_Moss.glb", sz))

    # 3. Set_AlpineChalet_Hybrid.glb (Detailed Alpine Wooden Chalet House with Gable Roof & Red Shutters)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col = bpy.context.scene.collection
    m_wall = make_mat("ChaletWoodWall", (0.42, 0.25, 0.13), roughness=0.62)
    m_roof = make_mat("ChaletRoofSlate", (0.16, 0.17, 0.20), roughness=0.52, coat=0.25)
    m_trim = make_mat("ChaletWhiteTrim", (0.90, 0.89, 0.86), roughness=0.45)
    m_shut = make_mat("ChaletRedShutter", (0.58, 0.14, 0.11), roughness=0.48)
    m_glass = make_mat("ChaletDarkGlass", (0.03, 0.05, 0.07), roughness=0.04, metallic=0.15, coat=0.92)
    env._add_box("Chalet_Body", (0, 0, 1.65), (4.8, 3.8, 3.3), m_wall, col, bevel_m=0.02)
    env._add_gable_roof("Chalet_Roof", (0, 0, 3.30), 5.4, 4.4, 1.85, m_roof, col)
    for wx in (-1.2, 1.2):
        fy = -1.91
        env._add_box(f"WinFrm_{wx}", (wx, fy, 1.55), (0.98, 0.08, 1.12), m_trim, col, bevel_m=0.008)
        env._add_box(f"WinGls_{wx}", (wx, fy - 0.04, 1.55), (0.84, 0.03, 0.96), m_glass, col, bevel_m=0.0)
        for sgn in (-1, 1):
            env._add_box(f"Shut_{wx}_{sgn}", (wx + sgn * 0.65, fy - 0.02, 1.55), (0.28, 0.06, 1.05), m_shut, col, bevel_m=0.006)
    dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join("sets", "Set_AlpineChalet_Hybrid.glb"))
    baked.append(("Set_AlpineChalet_Hybrid.glb", sz))

    # 4. Prop_MudCastle_Hybrid.glb (Glossy wet 3-tower mud castle from té5666.mp4)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col = bpy.context.scene.collection
    m_mud = make_mat("WetMudCastle", (0.11, 0.072, 0.045), roughness=0.06, coat=0.88, coat_rough=0.02)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, radius=0.45, location=(0, 0, 0.14))
    base = bpy.context.active_object
    base.scale = (1.3, 0.9, 0.45)
    base.data.materials.append(m_mud)
    for tx, tz, tr_r in [(-0.28, 0.34, 0.14), (0.0, 0.46, 0.17), (0.28, 0.32, 0.13)]:
        bpy.ops.mesh.primitive_cone_add(vertices=20, radius1=tr_r, radius2=tr_r * 0.35, depth=tz * 1.4, location=(tx, 0, tz * 0.7))
        tw = bpy.context.active_object
        for p in tw.data.polygons:
            p.use_smooth = True
        tw.data.materials.append(m_mud)
    dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join("props", "Prop_MudCastle_Hybrid.glb"))
    baked.append(("Prop_MudCastle_Hybrid.glb", sz))

    # 5. Prop_CampfireRing_Hybrid.glb (10 river stones + 4 firewood logs + glowing flame cones)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col = bpy.context.scene.collection
    m_stone = make_mat("HybridFireStone", (0.14, 0.15, 0.17), roughness=0.28, coat=0.55)
    m_log = make_mat("HybridFireLog", (0.15, 0.09, 0.05), roughness=0.78)
    m_flame1 = make_mat("HybridFlameCore", (1.0, 0.85, 0.35), roughness=0.1, emission=(1.0, 0.78, 0.22), emission_strength=12.0)
    m_flame2 = make_mat("HybridFlameOuter", (1.0, 0.38, 0.06), roughness=0.2, emission=(1.0, 0.32, 0.04), emission_strength=8.5)
    for i in range(10):
        ang = (i / 10.0) * math.pi * 2.0
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=0.15, location=(math.cos(ang) * 0.50, math.sin(ang) * 0.50, 0.08))
        st = bpy.context.active_object
        st.scale = (1.2, 0.95, 0.65)
        st.rotation_euler = (0, 0, ang)
        for p in st.data.polygons:
            p.use_smooth = True
        st.data.materials.append(m_stone)
    for i in range(4):
        ang = (i / 4.0) * math.pi + 0.3
        bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=0.075, depth=0.82, location=(0, 0, 0.16), rotation=(1.15, 0, ang))
        lg = bpy.context.active_object
        lg.data.materials.append(m_log)
    for idx, (ox, oy, rad, h, is_c) in enumerate([(0, 0, 0.18, 0.55, True), (0.1, 0.08, 0.14, 0.45, False), (-0.1, -0.07, 0.14, 0.44, False)]):
        bpy.ops.mesh.primitive_cone_add(vertices=14, radius1=rad, radius2=0.01, depth=h, location=(ox, oy, 0.26 + h * 0.35))
        fl = bpy.context.active_object
        for p in fl.data.polygons:
            p.use_smooth = True
        fl.data.materials.append(m_flame1 if is_c else m_flame2)
    dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join("props", "Prop_CampfireRing_Hybrid.glb"))
    baked.append(("Prop_CampfireRing_Hybrid.glb", sz))

    # 6. Prop_WoodenFence_Hybrid.glb (Weathered rustic village wooden picket fence section)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col = bpy.context.scene.collection
    m_fwood = make_mat("HybridFenceWood", (0.28, 0.22, 0.16), roughness=0.68)
    for i in range(-4, 5):
        x = i * 0.42
        h_v = 0.92 + 0.06 * math.sin(i * 2.1)
        env._add_box(f"Post_{i}", (x, 0.0, h_v * 0.5), (0.13, 0.055, h_v), m_fwood, col, bevel_m=0.006)
    env._add_box("Rail_Top", (0.0, -0.03, 0.72), (3.6, 0.055, 0.07), m_fwood, col, bevel_m=0.005)
    env._add_box("Rail_Bot", (0.0, -0.03, 0.32), (3.6, 0.055, 0.07), m_fwood, col, bevel_m=0.005)
    dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join("props", "Prop_WoodenFence_Hybrid.glb"))
    baked.append(("Prop_WoodenFence_Hybrid.glb", sz))

    # 7. Set_AlpineChalet_Teal.glb (Stucco & Stone Alpine Cottage with Terracotta Roof & Teal Shutters)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col = bpy.context.scene.collection
    m_stucco = make_mat("ChaletStuccoWall", (0.78, 0.74, 0.67), roughness=0.65)
    m_terra = make_mat("ChaletTerraRoof", (0.58, 0.20, 0.12), roughness=0.52, coat=0.22)
    m_trim2 = make_mat("ChaletDarkTrim", (0.20, 0.14, 0.10), roughness=0.55)
    m_shut_t = make_mat("ChaletTealShutter", (0.14, 0.42, 0.39), roughness=0.48)
    m_glass2 = make_mat("ChaletDarkGlass2", (0.03, 0.05, 0.07), roughness=0.04, metallic=0.15, coat=0.92)
    env._add_box("Cottage_Body", (0, 0, 1.70), (5.0, 4.0, 3.4), m_stucco, col, bevel_m=0.02)
    env._add_gable_roof("Cottage_Roof", (0, 0, 3.40), 5.6, 4.6, 1.90, m_terra, col)
    env._add_box("Cottage_Chimney", (1.6, 0.6, 4.4), (0.65, 0.65, 1.5), m_trim2, col, bevel_m=0.01)
    env._add_box("Cottage_Door", (0.0, -2.01, 1.05), (0.95, 0.08, 2.05), m_trim2, col, bevel_m=0.01)
    for wx in (-1.45, 1.45):
        fy = -2.01
        env._add_box(f"WinFrmT_{wx}", (wx, fy, 1.65), (0.96, 0.08, 1.12), m_trim2, col, bevel_m=0.008)
        env._add_box(f"WinGlsT_{wx}", (wx, fy - 0.04, 1.65), (0.82, 0.03, 0.96), m_glass2, col, bevel_m=0.0)
        for sgn in (-1, 1):
            env._add_box(f"ShutT_{wx}_{sgn}", (wx + sgn * 0.64, fy - 0.02, 1.65), (0.28, 0.06, 1.05), m_shut_t, col, bevel_m=0.006)
    dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join("sets", "Set_AlpineChalet_Teal.glb"))
    baked.append(("Set_AlpineChalet_Teal.glb", sz))

    # 8. Prop_WoodenArchBridge_Hybrid.glb (Arched Wooden River Footbridge with Railings)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col = bpy.context.scene.collection
    m_bwood = make_mat("BridgeWoodPlank", (0.34, 0.21, 0.11), roughness=0.60, coat=0.25)
    m_bpost = make_mat("BridgeDarkBeam", (0.20, 0.12, 0.06), roughness=0.65)
    for i in range(-10, 11):
        u = i / 10.0
        px = u * 3.8
        pz = 0.55 * (1.0 - u * u) + 0.15
        pitch = math.degrees(math.atan2(-1.1 * u, 3.8))
        env._add_box(f"Plank_{i}", (px, 0.0, pz), (0.34, 2.2, 0.08), m_bwood, col, bevel_m=0.008, rot_deg=(0, pitch, 0))
    for i in range(-4, 5):
        u = i / 4.0
        px = u * 3.6
        pz = 0.55 * (1.0 - u * u) + 0.15
        for sy in (-1.02, 1.02):
            env._add_box(f"BPost_{i}_{sy}", (px, sy, pz + 0.45), (0.12, 0.12, 1.05), m_bpost, col, bevel_m=0.008)
    for sy in (-1.02, 1.02):
        env._add_box(f"BRail_{sy}", (0.0, sy, 1.05), (7.5, 0.08, 0.09), m_bpost, col, bevel_m=0.006)
    dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join("props", "Prop_WoodenArchBridge_Hybrid.glb"))
    baked.append(("Prop_WoodenArchBridge_Hybrid.glb", sz))

    # 9. Set_CampingTent_Hybrid.glb (Stylized A-Frame Canvas Camping Tent + Wooden Poles)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col = bpy.context.scene.collection
    m_canvas = make_mat("TentCanvasOlive", (0.72, 0.44, 0.14), roughness=0.72)
    m_pole = make_mat("TentWoodPole", (0.24, 0.15, 0.08), roughness=0.62)
    env._add_gable_roof("Tent_Body", (0, 0, 0.05), 2.4, 2.8, 1.65, m_canvas, col)
    env._add_box("Tent_PoleF", (0, -1.42, 0.88), (0.09, 0.09, 1.76), m_pole, col, bevel_m=0.005)
    env._add_box("Tent_PoleB", (0, 1.42, 0.88), (0.09, 0.09, 1.76), m_pole, col, bevel_m=0.005)
    dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join("sets", "Set_CampingTent_Hybrid.glb"))
    baked.append(("Set_CampingTent_Hybrid.glb", sz))

    # 10. Prop_ParkBenchLamp_Hybrid.glb (Wooden Park Bench + Wrought-Iron Warm Lantern Post)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    col = bpy.context.scene.collection
    m_iron = make_mat("LampIronBlack", (0.07, 0.08, 0.09), roughness=0.32, metallic=0.85)
    m_slat = make_mat("BenchWoodSlat", (0.45, 0.26, 0.12), roughness=0.55)
    m_bulb = make_mat("LanternWarmGlow", (1.0, 0.85, 0.55), roughness=0.1, emission=(1.0, 0.80, 0.45), emission_strength=10.0)
    # Bench
    env._add_box("Bench_Seat", (0.0, 0.0, 0.45), (1.8, 0.52, 0.07), m_slat, col, bevel_m=0.008)
    env._add_box("Bench_Back", (0.0, 0.24, 0.82), (1.8, 0.07, 0.52), m_slat, col, bevel_m=0.008, rot_deg=(-10, 0, 0))
    for lx in (-0.75, 0.75):
        env._add_box(f"Bench_Leg_{lx}", (lx, 0.0, 0.22), (0.08, 0.50, 0.45), m_iron, col, bevel_m=0.006)
    # Street Lamp beside bench
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.06, depth=3.2, location=(1.35, 0.15, 1.6))
    lp = bpy.context.active_object
    lp.data.materials.append(m_iron)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=0.22, location=(1.35, 0.15, 3.32))
    lb = bpy.context.active_object
    lb.data.materials.append(m_bulb)
    dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join("props", "Prop_ParkBenchLamp_Hybrid.glb"))
    baked.append(("Prop_ParkBenchLamp_Hybrid.glb", sz))

    return baked


def main():
    stage_dir = os.path.join(tempfile.gettempdir(), "sven_asset_harvest")
    os.makedirs(stage_dir, exist_ok=True)

    # Creator Store JSONs come from tools/harvest_assets.py (default folder output/_asset_harvest/json; pass another
    # folder after "--"). The category follows the name prefix (Prop_/Set_/Nature_/Pet_/Hair_).
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    json_dir = argv[0] if argv else os.path.join(HERE, "..", "..", "..", "..", "output", "_asset_harvest", "json")
    prefix_cat = {"Prop": "props", "Set": "sets", "Nature": "nature", "Pet": "animals", "Hair": "hairs"}

    converted = []
    for jf in sorted(glob.glob(os.path.join(json_dir, "*.json"))):
        mname = os.path.splitext(os.path.basename(jf))[0]
        bpy.ops.wm.read_factory_settings(use_empty=True)
        obj = r2g.build_from_json(jf, bpy.context.scene.collection)
        if obj is not None:
            cat = prefix_cat.get(mname.split("_")[0], "props")
            dest, sz = _export_active_collection_to_glb(stage_dir, os.path.join(cat, f"{mname}.glb"))
            dims = tuple(round(v, 2) for v in obj.dimensions)
            converted.append((f"{cat}/{mname}.glb", sz, dims))
            print(f"[CreatorStore -> GLB] {cat}/{mname}.glb ({sz / 1024:.1f} KB, dims={dims}m)", flush=True)

    baked = bake_stylized_hybrid_assets(stage_dir)
    for bname, bsz in baked:
        print(f"[StylizedHybrid -> GLB] {bname} ({bsz / 1024:.1f} KB)", flush=True)

    print(f"=== Completed Asset Library Expansion: {len(converted)} Creator Store GLBs + {len(baked)} Stylized Hybrid GLBs ===", flush=True)


def render_hybrid_showcase(stage_dir: str):
    """Renders a 4-panel Stylized-PBR Hybrid Roblox Cinema Showcase using the new GLB Asset Library."""
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    col = bpy.data.collections.new("HybridShowcase")
    sc.collection.children.link(col)

    env.apply_cinematic_mood(col, mood="real_outdoor", exposure=-0.22)
    env.apply_polyhaven_hdri("kloofendal_48d_partly_cloudy_puresky", strength=0.38, rot_z_deg=25.0)
    sc.render.engine = "BLENDER_EEVEE"
    sc.render.resolution_x = 1280
    sc.render.resolution_y = 720
    sc.render.use_persistent_data = True
    if hasattr(sc, "eevee"):
        sc.eevee.taa_render_samples = 16
        for attr in ("use_raytracing", "use_gtao", "use_shadows"):
            if hasattr(sc.eevee, attr):
                setattr(sc.eevee, attr, True)

    # Stylized-PBR Hybrid Terrain (Lush moss-and-mud color ramp + wet puddle mirror plane)
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=80, y_segments=80, size=50.0)
    for v in bm.verts:
        x, y = v.co.x, v.co.y
        d_puddle = math.hypot(x * 0.8, y + 1.5)
        dip = -0.25 * math.exp(-(d_puddle ** 2) / 18.0)
        d_river = abs(x - 18.0)
        river_dip = -0.35 * math.exp(-(d_river ** 2) / 6.0)
        undul = 0.08 * math.sin(x * 0.4) * math.cos(y * 0.4)
        v.co.z = dip + river_dip + undul
    me_t = bpy.data.meshes.new("HybridTerrain")
    bm.to_mesh(me_t)
    bm.free()
    for p in me_t.polygons:
        p.use_smooth = True
    terr = bpy.data.objects.new("HybridTerrain", me_t)
    col.objects.link(terr)
    terr.data.materials.append(env.make_wet_mud_puddle_mat("HybridMudGrass", "#3B281A", "#1A110B"))

    bpy.ops.mesh.primitive_plane_add(size=80.0, location=(0, 0, -0.04))
    wtr = bpy.context.active_object
    for c in list(wtr.users_collection):
        c.objects.unlink(wtr)
    col.objects.link(wtr)
    m_wtr = make_mat("HybridMirrorWater", (0.03, 0.07, 0.065), roughness=0.02, metallic=0.08, coat=0.90, coat_rough=0.015)
    wtr.data.materials.append(m_wtr)

    # Zone 1 (Center x=0): Twin Alpine Chalets (Wood/Red & Stucco/Teal), Stylized Pines, Moss Boulders, Mud Castle & Fence
    env.spawn_core_glb_asset(col, "sets/Set_AlpineChalet_Hybrid.glb", (-3.4, 6.2, 0.02), (0, 0, 8), 1.0)
    env.spawn_core_glb_asset(col, "sets/Set_AlpineChalet_Teal.glb", (3.6, 6.5, 0.02), (0, 0, -10), 1.0)
    env.spawn_core_glb_asset(col, "props/Prop_WoodenFence_Hybrid.glb", (-3.6, 3.2, 0.02), (0, 0, 0), 1.0)
    env.spawn_core_glb_asset(col, "props/Prop_WoodenFence_Hybrid.glb", (3.6, 3.2, 0.02), (0, 0, 0), 1.0)
    env.spawn_core_glb_asset(col, "props/Prop_MudCastle_Hybrid.glb", (-0.6, -0.8, -0.02), (0, 0, 20), 1.2)
    for idx, (px, py, psc) in enumerate([(-8.2, 5.5, 1.15), (-6.8, 10.5, 1.35), (0.0, 11.2, 1.45), (8.2, 5.8, 1.25), (7.2, 10.8, 1.40)]):
        env.spawn_core_glb_asset(col, "nature/Nature_StylizedPine_Hybrid.glb", (px, py, 0.0), (0, 0, idx * 45), psc)
    for idx, (bx, by, bsc) in enumerate([(-2.8, -0.4, 0.85), (2.9, -0.2, 0.95), (-2.2, 2.2, 0.75)]):
        env.spawn_core_glb_asset(col, "nature/Nature_StylizedBoulder_Moss.glb", (bx, by, -0.04), (0, 0, idx * 70), bsc)

    # Zone 2 (East x=+18): Arched Wooden River Bridge, Canvas Camping Tent, Campfire Ring, Picnic Table & Treasure Chest
    env.spawn_core_glb_asset(col, "props/Prop_WoodenArchBridge_Hybrid.glb", (17.5, 2.8, -0.04), (0, 0, 10), 0.75)
    env.spawn_core_glb_asset(col, "sets/Set_CampingTent_Hybrid.glb", (22.5, 5.2, 0.04), (0, 0, -28), 1.0)
    env.spawn_core_glb_asset(col, "props/Prop_CampfireRing_Hybrid.glb", (20.8, 1.8, 0.02), (0, 0, 0), 1.15)
    env.spawn_core_glb_asset(col, "props/Prop_PicnicTable_CS.glb", (14.2, 5.5, 0.04), (0, 0, 25), 0.95)
    env.spawn_core_glb_asset(col, "props/Prop_TreasureChest_CS.glb", (19.6, 1.4, 0.03), (0, 0, -35), 1.1)
    env.spawn_core_glb_asset(col, "nature/Nature_QuentyPine_CS.glb", (24.8, 8.8, 0.0), (0, 0, 15), 0.75)
    env.spawn_core_glb_asset(col, "nature/Nature_StylizedPine_Hybrid.glb", (13.2, 8.8, 0.0), (0, 0, 60), 1.3)

    # Zone 3 (West x=-18): Town Street, Pickup Truck, Red Sedan, Park Bench & Lantern, Chalet & Shiba Pet
    env.spawn_core_glb_asset(col, "sets/Set_AlpineChalet_Teal.glb", (-18.2, 7.5, 0.04), (0, 0, 4), 1.0)
    env.spawn_core_glb_asset(col, "props/Prop_PickupTruck_CS.glb", (-15.2, 1.8, 0.04), (0, 0, 55), 0.62)
    env.spawn_core_glb_asset(col, "props/Prop_Car_RobloxResources.glb", (-20.8, 2.2, 0.04), (0, 0, -65), 0.82)
    env.spawn_core_glb_asset(col, "props/Prop_ParkBenchLamp_Hybrid.glb", (-18.2, 4.0, 0.04), (0, 0, 0), 1.0)
    env.spawn_core_glb_asset(col, "animals/Pet_Dog_Shiba.glb", (-17.4, 1.4, 0.04), (0, 0, -20), 1.0)
    env.spawn_core_glb_asset(col, "nature/Nature_StylizedPine_Hybrid.glb", (-23.8, 8.2, 0.0), (0, 0, 30), 1.3)

    cam_d = bpy.data.cameras.new("ShowCam")
    cam_d.lens = 35.0
    cam = bpy.data.objects.new("ShowCam", cam_d)
    col.objects.link(cam)
    sc.camera = cam

    views = [
        ("panel_01_alpine_village", Vector((-0.5, -5.8, 1.45)), Vector((-0.2, 5.5, 1.65)), 34.0),
        ("panel_02_river_camp_bridge", Vector((17.5, -3.5, 1.85)), Vector((19.5, 4.5, 1.15)), 32.0),
        ("panel_03_town_vehicles", Vector((-18.2, -3.8, 1.75)), Vector((-18.2, 4.5, 1.25)), 32.0),
        ("panel_04_campfire_closeup", Vector((19.5, -0.8, 1.05)), Vector((21.5, 3.2, 0.65)), 40.0),
    ]
    prev_dir = os.path.join(stage_dir, "showcase")
    os.makedirs(prev_dir, exist_ok=True)
    for idx, (vname, cpos, lkat, flens) in enumerate(views, 1):
        cam.location = cpos
        cam.rotation_euler = (lkat - cpos).normalized().to_track_quat("-Z", "Y").to_euler()
        cam_d.lens = flens
        sc.frame_set(idx)
        sc.render.filepath = os.path.join(prev_dir, f"{vname}.png")
        bpy.ops.render.render(write_still=True)
        print(f"[Showcase] Rendered {vname}.png", flush=True)


if __name__ == "__main__":
    if "--showcase-only" in sys.argv:
        sdir = os.path.join(tempfile.gettempdir(), "sven_blender_asset_harvest")
        os.makedirs(sdir, exist_ok=True)
        render_hybrid_showcase(sdir)
    else:
        main()


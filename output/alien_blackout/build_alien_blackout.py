#!/usr/bin/env python3
"""
build_alien_blackout.py — Stage R4 Polished 6-Pillar 3D Scene Builder for `alien_blackout`
Format: 9:16 (1080x1920 final / 540x960 preview), 30 fps, 1586 frames (52.85s)
Look: Blender 5.3 Cycles GPU (`real_outdoor` 8PM wet night PBR + night clouds + mountain horizon) & Face Cartoon.
"""
import argparse
import json
import math
import os
import sys

import bpy
from mathutils import Euler, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
STUDIO_KIT = os.path.join(REPO_ROOT, ".agents", "skills", "roblox-director", "studio_kit")
if STUDIO_KIT not in sys.path:
    sys.path.insert(0, STUDIO_KIT)

import blender_roblox_kit as kit
import blender_env_lighting as env

ASSETS_DIR = os.path.join(REPO_ROOT, ".agents", "skills", "roblox-director", "assets")
CLOTHES_DIR = os.path.join(ASSETS_DIR, "clothes")
CARTOON_DIR = os.path.join(ASSETS_DIR, "faces_cartoon")
PLAN_PATH = os.path.join(HERE, "director_plan.json")
WORDS_PATH = os.path.join(HERE, "words.json")


def clear_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def key_val(obj_or_data, attr: str, frame: int, val, constant: bool = True):
    setattr(obj_or_data, attr, val)
    obj_or_data.keyframe_insert(data_path=attr, frame=frame)
    if constant and obj_or_data.animation_data and obj_or_data.animation_data.action:
        act = obj_or_data.animation_data.action
        for fc in kit.iter_action_fcurves(act):
            if fc.data_path == attr:
                for kp in fc.keyframe_points:
                    if int(round(kp.co.x)) == frame:
                        kp.interpolation = "CONSTANT"


def key_emissive_strength(mat, frame: int, strength: float, constant: bool = True):
    nt = mat.node_tree
    bsdf = next((n for n in nt.nodes if n.type in ("BSDF_PRINCIPLED", "EMISSION")), None)
    if not bsdf:
        return
    sock = bsdf.inputs.get("Emission Strength") or bsdf.inputs.get("Strength")
    if not sock:
        return
    sock.default_value = strength
    sock.keyframe_insert(data_path="default_value", frame=frame)
    if constant and nt.animation_data and nt.animation_data.action:
        for fc in kit.iter_action_fcurves(nt.animation_data.action):
            for kp in fc.keyframe_points:
                if int(round(kp.co.x)) == frame:
                    kp.interpolation = "CONSTANT"


def key_emissive_color(mat, frame: int, rgba, constant: bool = True):
    nt = mat.node_tree
    bsdf = next((n for n in nt.nodes if n.type in ("BSDF_PRINCIPLED", "EMISSION")), None)
    if not bsdf:
        return
    sock = bsdf.inputs.get("Emission Color") or bsdf.inputs.get("Color")
    if not sock:
        return
    sock.default_value = rgba
    sock.keyframe_insert(data_path="default_value", frame=frame)


def make_anim_emissive_mat(name: str, hex_col: str, strength: float = 3.0):
    mat = bpy.data.materials.new(name=name)
    nt = mat.node_tree
    bsdf = nt.nodes.get("Principled BSDF")
    rgba = env._hex_rgba(hex_col)
    bsdf.inputs["Base Color"].default_value = (rgba[0] * 0.18, rgba[1] * 0.18, rgba[2] * 0.18, 1.0)
    bsdf.inputs["Roughness"].default_value = 0.18
    if "Emission Color" in bsdf.inputs:
        bsdf.inputs["Emission Color"].default_value = rgba
        bsdf.inputs["Emission Strength"].default_value = strength
    return mat


def create_banh_mi(name: str, loc, col, mat_bread):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=18, ring_count=12, radius=1.0, location=loc)
    bm = bpy.context.active_object
    bm.name = name
    bm.scale = (0.16, 0.068, 0.056)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bm.data.materials.append(mat_bread)
    for p in bm.data.polygons:
        p.use_smooth = True
    for c in list(bm.users_collection):
        c.objects.unlink(bm)
    col.objects.link(bm)
    return bm


def create_phone_prop(name: str, col):
    mat_body = env.make_solid_mat("PhoneBody", "#181A20", roughness=0.25, metallic=0.6)
    mat_scr = make_anim_emissive_mat("PhoneChatScreen", "#38C8FF", strength=0.0)
    nt = mat_scr.node_tree
    tc = nt.nodes.new("ShaderNodeTexCoord")
    wv = nt.nodes.new("ShaderNodeTexWave")
    wv.wave_type = "BANDS"
    wv.bands_direction = "Z"
    wv.inputs["Scale"].default_value = 3.8
    nt.links.new(tc.outputs["Generated"], wv.inputs["Vector"])
    cr = nt.nodes.new("ShaderNodeValToRGB")
    cr.color_ramp.elements[0].position = 0.42
    cr.color_ramp.elements[0].color = (0.05, 0.22, 0.55, 1.0)
    cr.color_ramp.elements[1].position = 0.65
    cr.color_ramp.elements[1].color = (0.35, 0.98, 0.52, 1.0)
    nt.links.new(wv.outputs["Fac"], cr.inputs["Fac"])
    bsdf = nt.nodes.get("Principled BSDF")
    nt.links.new(cr.outputs["Color"], bsdf.inputs["Emission Color"])

    body = env._add_box(name, (0, 0, 0), (0.12, 0.016, 0.22), mat_body, col, bevel_m=0.004)
    scr = env._add_box(name + "_Screen", (0, -0.009, 0), (0.104, 0.005, 0.195), mat_scr, col, bevel_m=0.001)
    scr.parent = body
    # Add local cool-blue phone light that illuminates Minh's face when phone screen turns ON
    ld_ph = bpy.data.lights.new(name + "_Glow", type="POINT")
    ld_ph.energy = 0.0
    ld_ph.color = (0.35, 0.78, 1.0)
    ld_ph.shadow_soft_size = 0.15
    lo_ph = bpy.data.objects.new(name + "_Glow", ld_ph)
    lo_ph.parent = body
    lo_ph.location = (0.0, -0.22, 0.08)
    col.objects.link(lo_ph)
    return body, mat_scr, lo_ph


def build_alley_world(col_env, col_props):
    obstacles = []
    # Night real_outdoor wet ground across LOC_02 alley
    m_wet = env.make_wet_mud_puddle_mat("AlleyWetAsphalt", "#252830", "#0D0F14")
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=96, y_subdivisions=64, size=1.0, location=(0.0, 4.0, 0.0))
    gnd = bpy.context.active_object
    gnd.name = "Alley_Wet_Ground"
    gnd.scale = (72.0, 56.0, 1.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    for v in gnd.data.vertices:
        d = math.hypot(v.co.x, v.co.y)
        w = 0.025 * math.sin(v.co.x * 1.3) * math.cos(v.co.y * 1.2)
        if -1.8 <= v.co.y <= 8.2 and -30.0 <= v.co.x <= 15.0:
            v.co.z = 0.0
        else:
            v.co.z = w * min(1.0, 0.4 + 0.08 * d)
    gnd.data.update()
    for p in gnd.data.polygons:
        p.use_smooth = True
    gnd.data.materials.append(m_wet)
    env._link(gnd, col_env)

    # Sidewalks & dark wet curb
    m_sidewalk = env.make_paving_mat("AlleySidewalk", "#464B54", "#2B2E36")
    env._add_box("Sidewalk_North", (1.0, 2.55, 0.02), (28.0, 1.6, 0.04), m_sidewalk, col_env, bevel_m=0.008)
    env._add_box("Sidewalk_South", (1.0, -3.6, 0.02), (28.0, 1.8, 0.04), m_sidewalk, col_env, bevel_m=0.008)

    env.build_mountain_horizon(col_env, peak_y=36.0)
    m_wood = env.make_weathered_wood_mat("AlleyFenceWood", "#4A4139", "#211D19")
    for x in [i * 0.45 for i in range(-26, 28) if not (7.2 <= i * 0.45 <= 9.8)]:
        env._add_box(f"SouthFence_{x:.2f}", (x, -2.95, 0.44), (0.12, 0.05, 0.88), m_wood, col_env, bevel_m=0.005)
    env._add_box("SouthFenceRail", (0.0, -2.95, 0.62), (25.0, 0.05, 0.06), m_wood, col_env, bevel_m=0.004)

    m_stucco1 = env.make_weathered_stone_mat("House01Stucco", "#ABA395", "#5C564C", scale=2.0)
    m_stone2 = env.make_weathered_stone_mat("House02Stone", "#46423D", "#1E1C1A", scale=2.6)
    m_stucco3 = env.make_weathered_stone_mat("House03Stucco", "#948473", "#493F35", scale=2.2)
    m_stone4 = env.make_weathered_stone_mat("Room04Stone", "#3A3E45", "#171A1E", scale=2.6)
    m_roof_r = env.make_cladding_mat("AlleyRoofRed", "#96331E", "#4A180D", row_freq=10.5, brick_offset=0.5)
    m_roof_t = env.make_cladding_mat("AlleyRoofTeal", "#275450", "#122B29", row_freq=10.5, brick_offset=0.5)
    m_trim = env.make_weathered_wood_mat("HouseTrim", "#2B2018", "#140E0A")
    m_win_warm = make_anim_emissive_mat("NeighborhoodWarmWin", "#FFD278", strength=4.2)
    # Saturated green emission capped <= 3.2 so AgX renders glowing emerald instead of clipping pure white!
    m_win_alien = make_anim_emissive_mat("Room04AlienWin", "#1CE84A", strength=0.2)

    def build_closed_house(cname, cx, wall_m, roof_m):
        cy = 5.0
        body = env._add_box(f"{cname}_Body", (cx, cy, 1.65), (4.4, 3.6, 3.3), wall_m, col_env, bevel_m=0.02)
        env._add_gable_roof(f"{cname}_Roof", (cx, cy, 3.30), 4.9, 4.1, 1.65, roof_m, col_env)
        for wx in (cx - 1.1, cx + 1.1):
            fy = cy - 1.81
            env._add_box(f"{cname}_WFrm_{wx:.1f}", (wx, fy, 1.55), (0.95, 0.08, 1.05), m_trim, col_env)
            env._add_box(f"{cname}_WGls_{wx:.1f}", (wx, fy - 0.03, 1.55), (0.82, 0.04, 0.90), m_win_warm, col_env)
            env._add_box(f"{cname}_WMulV_{wx:.1f}", (wx, fy - 0.055, 1.55), (0.045, 0.025, 0.90), m_trim, col_env)
            env._add_box(f"{cname}_WMulH_{wx:.1f}", (wx, fy - 0.055, 1.55), (0.82, 0.025, 0.045), m_trim, col_env)
        obstacles.append(body)

    build_closed_house("House01_Minh", -7.4, m_stucco1, m_roof_r)
    build_closed_house("House02_CoHoa", -2.2, m_stone2, m_roof_t)
    build_closed_house("House03_ChuTu", 3.0, m_stucco3, m_roof_r)

    # Room 04 (LOC_03) at x = 6.4..10.8, y = 3.22..7.80
    r_cx, r_cy = 8.6, 5.5
    m_floor04 = env.make_weathered_wood_mat("Room04Floor", "#3E342B", "#1E1813")
    env._add_box("Room04_Floor", (r_cx, r_cy, 0.02), (4.4, 4.6, 0.04), m_floor04, col_env)
    obstacles.append(env._add_box("Room04_BackWall", (r_cx, 7.75, 1.65), (4.5, 0.18, 3.3), m_stone4, col_env))
    obstacles.append(env._add_box("Room04_LeftWall", (6.45, r_cy, 1.65), (0.18, 4.6, 3.3), m_stone4, col_env))
    obstacles.append(env._add_box("Room04_RightWall", (10.75, r_cy, 1.65), (0.18, 4.6, 3.3), m_stone4, col_env))
    obstacles.append(env._add_box("Room04_FrontL", (7.18, 3.22, 1.65), (1.54, 0.18, 3.3), m_stone4, col_env))
    obstacles.append(env._add_box("Room04_FrontR", (10.02, 3.22, 1.65), (1.54, 0.18, 3.3), m_stone4, col_env))
    env._add_box("Room04_FrontHeader", (8.60, 3.22, 2.75), (1.34, 0.18, 1.1), m_stone4, col_env)

    # Alien Frosted Window on FrontL wall with dark cross mullions + silhouette bar
    env._add_box("Room04_AlienWinFrm", (7.25, 3.12, 1.55), (0.98, 0.08, 1.12), m_trim, col_env)
    env._add_box("Room04_AlienWinGls", (7.25, 3.08, 1.55), (0.86, 0.04, 0.96), m_win_alien, col_env)
    env._add_box("Room04_AlienMulV", (7.25, 3.04, 1.55), (0.055, 0.03, 0.96), m_trim, col_env)
    env._add_box("Room04_AlienMulH", (7.25, 3.04, 1.55), (0.86, 0.03, 0.055), m_trim, col_env)
    env._add_box("Room04_Ceiling", (r_cx, r_cy, 3.30), (4.5, 4.7, 0.12), m_stone4, col_env)
    env._add_gable_roof("Room04_Roof", (r_cx, r_cy, 3.36), 5.0, 5.1, 1.6, m_roof_t, col_env)

    # Hinged Door PROP_05 swinging cleanly inward-left (-108°) so doorway opens unobstructed!
    door_pivot = bpy.data.objects.new("Room04_DoorPivot", None)
    door_pivot.location = (7.95, 3.22, 0.02)
    col_props.objects.link(door_pivot)
    door_glb = kit.load_core_glb("Prop_InteriorDoor.glb", col=col_props, location_m=(7.95, 3.22, 0.02), scale=1.0)
    door_glb.parent = door_pivot
    door_glb.location = (0.64, 0.0, 1.05)

    # Room 04 Interior Dining Table + Chair + White Plate + 2 Golden Banh Mi (east side x=10.05, y=5.95)
    table = env._add_box("Room04_Table", (10.05, 5.95, 0.39), (1.05, 0.80, 0.78), m_wood, col_props, bevel_m=0.015)
    obstacles.append(table)
    kit.load_core_glb("Prop_DiningChair.glb", col=col_props, location_m=(10.05, 5.25, 0.02), yaw_deg=180.0, scale=0.95)
    m_plate = env.make_solid_mat("CeramicPlate", "#F0EFEA", roughness=0.22)
    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=0.28, depth=0.024, location=(10.02, 5.95, 0.79))
    plate = bpy.context.active_object
    plate.name = "BanhMi_Plate"
    plate.data.materials.append(m_plate)
    env._link(plate, col_props)
    m_bread = env.make_solid_mat("BanhMi_Golden", "#DF8E35", roughness=0.58)
    bm1 = create_banh_mi("BanhMi_01", (9.90, 5.90, 0.84), col_props, m_bread)
    bm2 = create_banh_mi("BanhMi_02", (10.12, 6.02, 0.84), col_props, m_bread)

    # PROP_06 Exposed Glowing Cosmic Battery Cage + Braided Ceiling Cable at (8.75, 5.05)
    m_core_metal = env.make_solid_mat("BatteryMetal", "#252E36", roughness=0.25, metallic=0.88)
    m_core_glow = make_anim_emissive_mat("BatteryNeonCore", "#1EFF52", strength=10.5)
    # Glowing exposed plasma tube as main visible cylinder
    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=0.20, depth=0.38, location=(8.75, 5.05, 0.27))
    bat_core = bpy.context.active_object
    bat_core.name = "CosmicBattery_Glow"
    bat_core.data.materials.append(m_core_glow)
    env._link(bat_core, col_props)
    # Metal bottom cap, top cap + 4 thin vertical ribs around the glowing plasma tube
    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=0.23, depth=0.07, location=(8.75, 5.05, 0.055))
    bat_bot = bpy.context.active_object
    bat_bot.name = "CosmicBattery_BotCap"
    bat_bot.data.materials.append(m_core_metal)
    env._link(bat_bot, col_props)
    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=0.23, depth=0.07, location=(8.75, 5.05, 0.48))
    bat_top = bpy.context.active_object
    bat_top.name = "CosmicBattery_TopCap"
    bat_top.data.materials.append(m_core_metal)
    bat_top.parent = bat_core
    bat_top.location = (0, 0, 0.21)
    bat_bot.parent = bat_core
    bat_bot.location = (0, 0, -0.215)
    for k in range(4):
        ang = math.radians(k * 90.0 + 45.0)
        rx, ry = 0.21 * math.cos(ang), 0.21 * math.sin(ang)
        bpy.ops.mesh.primitive_cylinder_add(vertices=10, radius=0.018, depth=0.42, location=(8.75 + rx, 5.05 + ry, 0.27))
        rib = bpy.context.active_object
        rib.name = f"CosmicBattery_Rib_{k}"
        rib.data.materials.append(m_core_metal)
        env._link(rib, col_props)
        rib.parent = bat_core
        rib.location = (rx, ry, 0.0)

    m_cable = env.make_solid_mat("CeilingCableMat", "#14161A", roughness=0.45)
    bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=0.022, depth=2.76, location=(8.75, 5.05, 1.88))
    cable = bpy.context.active_object
    cable.name = "Ceiling_PowerCable"
    cable.data.materials.append(m_cable)
    env._link(cable, col_props)

    # Parked Car & clean side trees (no off-origin foreground bush clutter near car!)
    car = kit.load_core_glb("Prop_Car_RobloxResources.glb", col=col_props, location_m=(2.2, 1.35, 0.02), yaw_deg=90.0, scale=0.88)
    obstacles.append(car)
    kit.load_core_glb("Nature_OakPinePack_CS.glb", col=col_env, location_m=(-10.8, 5.4, 0.0), scale=1.15)
    kit.load_core_glb("Nature_ClassicTree_CS.glb", col=col_env, location_m=(12.2, 5.6, 0.0), scale=1.2)

    # 3 Streetlamps with keyable emissive bulbs so lamp glass turns genuinely OFF at blackout!
    lamp_lights = []
    lamp_bulb_mat = make_anim_emissive_mat("AlleyLampBulb_Anim", "#FFE099", strength=10.0)
    for idx, lx in enumerate((-5.2, 0.5, 5.9)):
        env.build_streetlamp(f"AlleyLamp_{idx+1}", loc=(lx, 2.25, 0.04), col=col_env, lamp_energy=0.0, face_road=-1.0)
        bulb = bpy.data.objects.get(f"AlleyLamp_{idx+1}_Bulb")
        if bulb:
            bulb.data.materials.clear()
            bulb.data.materials.append(lamp_bulb_mat)
        ld = bpy.data.lights.new(f"AlleyLight_{idx+1}", type="POINT")
        ld.energy = 135.0
        ld.color = (1.0, 0.82, 0.50)
        ld.shadow_soft_size = 0.35
        lo = bpy.data.objects.new(f"AlleyLight_{idx+1}", ld)
        lo.location = (lx, 1.75, 2.85)
        col_env.objects.link(lo)
        lamp_lights.append(lo)

    # Room 04 Lights
    ld_alien = bpy.data.lights.new("AlienCoreLight", type="POINT")
    ld_alien.energy = 210.0
    ld_alien.color = (0.14, 1.0, 0.32)
    ld_alien.shadow_soft_size = 0.25
    lo_alien = bpy.data.objects.new("AlienCoreLight", ld_alien)
    lo_alien.location = (8.75, 4.95, 1.25)
    col_env.objects.link(lo_alien)

    ld_r04_moon = bpy.data.lights.new("Room04MoonBounce", type="AREA")
    ld_r04_moon.energy = 42.0
    ld_r04_moon.size = 1.6
    ld_r04_moon.color = (0.45, 0.68, 1.0)
    lo_r04_moon = bpy.data.objects.new("Room04MoonBounce", ld_r04_moon)
    lo_r04_moon.location = (8.4, 3.6, 2.3)
    lo_r04_moon.rotation_euler = (Vector((8.8, 5.2, 0.5)) - lo_r04_moon.location).to_track_quat("-Z", "Y").to_euler()
    col_env.objects.link(lo_r04_moon)

    ld_r04_warm = bpy.data.lights.new("Room04WarmLight", type="POINT")
    ld_r04_warm.energy = 0.0
    ld_r04_warm.color = (1.0, 0.88, 0.64)
    ld_r04_warm.shadow_soft_size = 0.35
    lo_r04_warm = bpy.data.objects.new("Room04WarmLight", ld_r04_warm)
    lo_r04_warm.location = (9.1, 5.2, 2.75)
    col_env.objects.link(lo_r04_warm)

    ld_spill = bpy.data.lights.new("AlienWindowSpill", type="SPOT")
    ld_spill.energy = 260.0
    ld_spill.color = (0.16, 1.0, 0.32)
    ld_spill.spot_size = math.radians(82.0)
    ld_spill.spot_blend = 0.48
    lo_spill = bpy.data.objects.new("AlienWindowSpill", ld_spill)
    lo_spill.location = (7.25, 2.95, 1.55)
    lo_spill.rotation_euler = Euler((math.radians(72.0), 0.0, math.radians(180.0)), "XYZ")
    col_env.objects.link(lo_spill)

    # Extra Porch/Sky escape wash lighting Zor-7 at Beat 21 when neighborhood power is back ON!
    ld_porch = bpy.data.lights.new("Room04PorchWash", type="AREA")
    ld_porch.energy = 0.0
    ld_porch.size = 2.4
    ld_porch.color = (1.0, 0.88, 0.68)
    lo_porch = bpy.data.objects.new("Room04PorchWash", ld_porch)
    lo_porch.location = (8.2, -0.4, 2.6)
    lo_porch.rotation_euler = (Vector((8.6, 1.6, 2.0)) - lo_porch.location).to_track_quat("-Z", "Y").to_euler()
    col_env.objects.link(lo_porch)

    # LOC_01 Minh Interior Room (spacious 6m x 6m at x=-24.0 so camera stays 100% unobstructed inside!)
    mx = -24.0
    m_wall_in = env.make_weathered_stone_mat("MinhRoomWall", "#B8B0A4", "#70685E", scale=1.5)
    env._add_box("Minh_Floor", (mx, 0.0, 0.01), (6.0, 6.2, 0.02), m_floor04, col_env)
    env._add_box("Minh_WallBack", (mx, 2.95, 1.65), (6.0, 0.16, 3.3), m_wall_in, col_env)
    env._add_box("Minh_WallLeft", (mx - 2.9, 0.0, 1.65), (0.16, 6.0, 3.3), m_wall_in, col_env)
    env._add_box("Minh_WallRight", (mx + 2.9, 0.0, 1.65), (0.16, 6.0, 3.3), m_wall_in, col_env)
    m_minh_win = make_anim_emissive_mat("MinhExteriorGreenWin", "#1EE84B", strength=2.6)
    env._add_box("Minh_WindowFrm", (mx + 2.80, 0.55, 1.45), (0.08, 1.25, 1.25), m_trim, col_env)
    env._add_box("Minh_WindowGls", (mx + 2.78, 0.55, 1.45), (0.04, 1.12, 1.12), m_minh_win, col_env)

    # Clean Minh wooden desk (y=1.02..1.70, z=0..0.76) + custom animatable Laptop + BankersLamp (zero collision & never blocks Minh's face!)
    minh_desk = env._add_box("Minh_Desk", (mx, 1.36, 0.38), (1.50, 0.68, 0.76), m_wood, col_props, bevel_m=0.012)
    obstacles.append(minh_desk)
    m_lap_body = env.make_solid_mat("LaptopBody", "#232832", roughness=0.30, metallic=0.7)
    m_lap_scr = make_anim_emissive_mat("LaptopScreenMat", "#45B5FF", strength=4.5)
    env._add_box("Minh_LaptopBase", (mx, 1.25, 0.775), (0.38, 0.26, 0.02), m_lap_body, col_props, bevel_m=0.003)
    env._add_box("Minh_LaptopLid",  (mx, 1.38, 0.90),  (0.38, 0.018, 0.25), m_lap_body, col_props, bevel_m=0.003, rot_deg=(-16, 0, 0))
    env._add_box("Minh_LaptopDisp", (mx, 1.368, 0.90), (0.34, 0.008, 0.21), m_lap_scr, col_props, bevel_m=0.001, rot_deg=(-16, 0, 0))
    kit.load_core_glb("Prop_BankersLamp.glb", col=col_props, location_m=(mx - 0.56, 1.38, 0.76), yaw_deg=25.0, scale=0.80)
    kit.load_core_glb("Nature_PottedMonstera.glb", col=col_env, location_m=(mx + 1.85, 2.05, 0.02), scale=0.9)

    ld_desk = bpy.data.lights.new("MinhDeskLamp", type="POINT")
    ld_desk.energy = 85.0
    ld_desk.color = (1.0, 0.84, 0.52)
    lo_desk = bpy.data.objects.new("MinhDeskLamp", ld_desk)
    lo_desk.location = (mx - 0.45, 1.15, 1.38)
    col_env.objects.link(lo_desk)

    ld_laptop = bpy.data.lights.new("MinhLaptopGlow", type="POINT")
    ld_laptop.energy = 16.0
    ld_laptop.color = (0.42, 0.78, 1.0)
    lo_laptop = bpy.data.objects.new("MinhLaptopGlow", ld_laptop)
    lo_laptop.location = (mx + 0.10, 0.92, 1.15)
    col_env.objects.link(lo_laptop)

    # Soft cool moonlight aiming straight at Minh's face both at desk & standing, plus alley night sky wash!
    ld_minh_moon = bpy.data.lights.new("MinhMoonFill", type="AREA")
    ld_minh_moon.energy = 48.0
    ld_minh_moon.size = 2.4
    ld_minh_moon.color = (0.50, 0.72, 1.0)
    lo_minh_moon = bpy.data.objects.new("MinhMoonFill", ld_minh_moon)
    lo_minh_moon.location = (mx - 0.4, 2.15, 2.05)
    lo_minh_moon.rotation_euler = (Vector((mx, 0.58, 1.25)) - lo_minh_moon.location).to_track_quat("-Z", "Y").to_euler()
    col_env.objects.link(lo_minh_moon)

    ld_alley_moon = bpy.data.lights.new("AlleyNightMoonWash", type="AREA")
    ld_alley_moon.energy = 65.0
    ld_alley_moon.size = 6.5
    ld_alley_moon.color = (0.45, 0.66, 1.0)
    lo_alley_moon = bpy.data.objects.new("AlleyNightMoonWash", ld_alley_moon)
    lo_alley_moon.location = (-0.5, -2.5, 4.2)
    lo_alley_moon.rotation_euler = (Vector((0.2, 0.0, 1.0)) - lo_alley_moon.location).to_track_quat("-Z", "Y").to_euler()
    col_env.objects.link(lo_alley_moon)

    ld_porch_moon = bpy.data.lights.new("PorchNightRim", type="AREA")
    ld_porch_moon.energy = 45.0
    ld_porch_moon.size = 2.0
    ld_porch_moon.color = (0.50, 0.72, 1.0)
    lo_porch_moon = bpy.data.objects.new("PorchNightRim", ld_porch_moon)
    lo_porch_moon.location = (9.6, 0.6, 2.3)
    lo_porch_moon.rotation_euler = (Vector((8.65, 2.15, 1.25)) - lo_porch_moon.location).to_track_quat("-Z", "Y").to_euler()
    col_env.objects.link(lo_porch_moon)

    ld_minh_green = bpy.data.lights.new("MinhWinGreenRim", type="AREA")
    ld_minh_green.energy = 36.0
    ld_minh_green.size = 1.4
    ld_minh_green.color = (0.16, 1.0, 0.34)
    lo_minh_green = bpy.data.objects.new("MinhWinGreenRim", ld_minh_green)
    lo_minh_green.location = (mx + 2.45, 0.25, 1.45)
    lo_minh_green.rotation_euler = (Vector((mx, -0.45, 1.32)) - lo_minh_green.location).to_track_quat("-Z", "Y").to_euler()
    col_env.objects.link(lo_minh_green)

    return {
        "obstacles": obstacles,
        "lamp_lights": lamp_lights,
        "lamp_bulb_mat": lamp_bulb_mat,
        "m_win_warm": m_win_warm,
        "m_win_alien": m_win_alien,
        "m_core_glow": m_core_glow,
        "lo_alien": lo_alien,
        "lo_r04_moon": lo_r04_moon,
        "lo_r04_warm": lo_r04_warm,
        "lo_spill": lo_spill,
        "lo_porch": lo_porch,
        "lo_desk": lo_desk,
        "lo_laptop": lo_laptop,
        "m_lap_scr": m_lap_scr,
        "lo_minh_green": lo_minh_green,
        "door_pivot": door_pivot,
        "bat_core": bat_core,
        "cable": cable,
        "bm1": bm1,
        "bm2": bm2,
    }


def setup_world_lighting_timeline(env_refs):
    # Genuine 8PM deep twilight/night PBR sky with subtle dark storm clouds
    sc = bpy.context.scene
    w = sc.world
    nt = w.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputWorld")
    bg = nt.nodes.new("ShaderNodeBackground")
    bg.inputs["Strength"].default_value = 0.28

    tc = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(tc.outputs["Generated"], sep.inputs["Vector"])
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.0
    ramp.color_ramp.elements[0].color = env._hex_rgba("#162340")
    ramp.color_ramp.elements[1].position = 0.52
    ramp.color_ramp.elements[1].color = env._hex_rgba("#040812")
    nt.links.new(sep.outputs["Z"], ramp.inputs["Fac"])

    cn = nt.nodes.new("ShaderNodeTexNoise")
    cn.inputs["Scale"].default_value = 3.8
    cn.inputs["Detail"].default_value = 8.0
    cn.inputs["Roughness"].default_value = 0.6
    nt.links.new(tc.outputs["Generated"], cn.inputs["Vector"])
    cramp = nt.nodes.new("ShaderNodeValToRGB")
    cramp.color_ramp.elements[0].position = 0.52
    cramp.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
    cramp.color_ramp.elements[1].position = 0.78
    cramp.color_ramp.elements[1].color = (0.35, 0.42, 0.58, 1.0)
    nt.links.new(cn.outputs["Fac"], cramp.inputs["Fac"])

    mix_c = nt.nodes.new("ShaderNodeMix")
    mix_c.data_type = "RGBA"
    mix_c.inputs[7].default_value = env._hex_rgba("#243352")
    nt.links.new(cramp.outputs["Color"], mix_c.inputs[0])
    nt.links.new(ramp.outputs["Color"], mix_c.inputs[6])
    nt.links.new(mix_c.outputs[2], bg.inputs["Color"])
    nt.links.new(bg.outputs["Background"], out.inputs["Surface"])

    ksun = bpy.data.objects.get("KeySun")
    if ksun:
        ksun.data.energy = 0.14
        ksun.data.temperature = 7200.0
    sfill = bpy.data.objects.get("SkyFill")
    if sfill:
        sfill.data.energy = 1.6
        sfill.data.color = (0.38, 0.56, 0.92)
    hrim = bpy.data.objects.get("HeroRim")
    if hrim:
        hrim.data.energy = 6.5
        hrim.data.color = (0.50, 0.75, 1.0)
    sc.view_settings.exposure = 0.10

    # Blackout & Power-Restore Lighting Timeline
    for lo in env_refs["lamp_lights"]:
        key_val(lo.data, "energy", 1, 145.0)
        key_val(lo.data, "energy", 66, 145.0)
        key_val(lo.data, "energy", 67, 0.0)       # 2.23s Blackout!
        key_val(lo.data, "energy", 1226, 0.0)
        key_val(lo.data, "energy", 1227, 175.0)   # 40.90s Power Restored!
    key_emissive_strength(env_refs["m_win_warm"], 1, 4.5)
    key_emissive_strength(env_refs["m_win_warm"], 66, 4.5)
    key_emissive_strength(env_refs["m_win_warm"], 67, 0.0)
    key_emissive_strength(env_refs["m_win_warm"], 1226, 0.0)
    key_emissive_strength(env_refs["m_win_warm"], 1227, 6.2)

    key_emissive_strength(env_refs["lamp_bulb_mat"], 1, 12.0)
    key_emissive_strength(env_refs["lamp_bulb_mat"], 66, 12.0)
    key_emissive_strength(env_refs["lamp_bulb_mat"], 67, 0.0)
    key_emissive_strength(env_refs["lamp_bulb_mat"], 1226, 0.0)
    key_emissive_strength(env_refs["lamp_bulb_mat"], 1227, 14.0)

    key_emissive_strength(env_refs["m_win_alien"], 1, 0.15)
    key_emissive_strength(env_refs["m_win_alien"], 67, 2.8)
    key_emissive_strength(env_refs["m_win_alien"], 1157, 2.8)
    key_emissive_strength(env_refs["m_win_alien"], 1158, 0.0)
    key_emissive_strength(env_refs["m_win_alien"], 1227, 4.2)
    key_emissive_color(env_refs["m_win_alien"], 1, (0.10, 0.96, 0.28, 1.0))
    key_emissive_color(env_refs["m_win_alien"], 1227, (1.0, 0.84, 0.52, 1.0))

    key_val(env_refs["lo_spill"].data, "energy", 1, 0.0)
    key_val(env_refs["lo_spill"].data, "energy", 67, 320.0)
    key_val(env_refs["lo_spill"].data, "energy", 1157, 320.0)
    key_val(env_refs["lo_spill"].data, "energy", 1158, 0.0)

    key_emissive_strength(env_refs["m_core_glow"], 1, 10.5)
    key_emissive_strength(env_refs["m_core_glow"], 1157, 10.5)
    key_emissive_strength(env_refs["m_core_glow"], 1158, 0.0)
    key_val(env_refs["lo_alien"].data, "energy", 1, 210.0)
    key_val(env_refs["lo_alien"].data, "energy", 1157, 210.0)
    key_val(env_refs["lo_alien"].data, "energy", 1158, 0.0)

    key_val(env_refs["lo_r04_warm"].data, "energy", 1, 0.0)
    key_val(env_refs["lo_r04_warm"].data, "energy", 1226, 0.0)
    key_val(env_refs["lo_r04_warm"].data, "energy", 1227, 230.0)

    key_val(env_refs["lo_porch"].data, "energy", 1, 0.0)
    key_val(env_refs["lo_porch"].data, "energy", 1226, 0.0)
    key_val(env_refs["lo_porch"].data, "energy", 1227, 95.0)

    # LOC_01 Minh desk blackout at fr 267 (8.90s)
    key_val(env_refs["lo_desk"].data, "energy", 1, 85.0)
    key_val(env_refs["lo_desk"].data, "energy", 266, 85.0)
    key_val(env_refs["lo_desk"].data, "energy", 267, 0.0)
    key_val(env_refs["lo_laptop"].data, "energy", 1, 16.0)
    key_val(env_refs["lo_laptop"].data, "energy", 266, 16.0)
    key_val(env_refs["lo_laptop"].data, "energy", 267, 0.0)
    key_emissive_strength(env_refs["m_lap_scr"], 1, 4.5)
    key_emissive_strength(env_refs["m_lap_scr"], 266, 4.5)
    key_emissive_strength(env_refs["m_lap_scr"], 267, 0.0)
    key_val(env_refs["lo_minh_green"].data, "energy", 1, 6.0)
    key_val(env_refs["lo_minh_green"].data, "energy", 267, 36.0)


def aim_cam(cam, fs: int, fe: int, pos1, tgt1, lens: float, roll_deg: float = 0.0, fstop: float = 4.0, pos2=None, tgt2=None, shot_log=None, scale_tag="MCU", angle_tag="eye"):
    p1 = Vector(pos1)
    t1 = Vector(tgt1)
    fd1 = max(0.3, (t1 - p1).length)
    kit._cam_aim(cam, fs, p1, t1, lens, roll_deg, fd1, fstop)
    p2 = Vector(pos2) if pos2 is not None else p1
    t2 = Vector(tgt2) if tgt2 is not None else t1
    fd2 = max(0.3, (t2 - p2).length)
    kit._cam_aim(cam, fe, p2, t2, lens, roll_deg, fd2, fstop)
    for fc in getattr(cam.animation_data.action, "fcurves", []):
        for kp in fc.keyframe_points:
            if int(round(kp.co.x)) == fe:
                kp.interpolation = "CONSTANT"
    if shot_log is not None:
        mv_tag = "push_in" if (pos2 is not None or tgt2 is not None) else "static"
        shot_log.append({"fs": fs, "fe": fe, "scale": scale_tag, "angle": angle_tag, "move": mv_tag})


def build_cast_and_acting(env_refs, col_props, total_frames: int):
    minh = kit.build_roblox_character(
        "Minh",
        os.path.join(CLOTHES_DIR, "shirt_me.png"),
        os.path.join(CLOTHES_DIR, "pants_me.png"),
        os.path.join(CARTOON_DIR, "neutral.png"),
        skin_hex="#F2C296", hair_hex="#231915",
        location_m=(-24.0, 0.58, 0.0), yaw_deg=180.0,
        rig_type="R15", hair_style="bald", body_profile="boy_athletic",
    )
    kit.attach_core_hair(minh, "Hair_ClassicSpiky_CS.glb", "#231915")

    cohoa = kit.build_roblox_character(
        "CoHoa",
        os.path.join(CLOTHES_DIR, "shirt_mom.png"),
        os.path.join(CLOTHES_DIR, "pants_mom.png"),
        os.path.join(CARTOON_DIR, "scared.png"),
        skin_hex="#F5C9A6", hair_hex="#2B1B18",
        location_m=(-2.0, 0.5, 0.0), yaw_deg=0.0,
        rig_type="R15", hair_style="long_ponytail", body_profile="girl_slim",
    )

    chutu = kit.build_roblox_character(
        "ChuTu",
        os.path.join(CLOTHES_DIR, "shirt_dad.png"),
        os.path.join(CLOTHES_DIR, "pants_dad.png"),
        os.path.join(CARTOON_DIR, "steam_angry.png"),
        skin_hex="#E5B084", hair_hex="#342E2C",
        location_m=(3.0, 0.5, 0.0), yaw_deg=-90.0,
        rig_type="R15", hair_style="slick_part", body_profile="stocky_boss",
        accessories=["mustache"],
    )

    zor7 = kit.build_roblox_character(
        "Zor7",
        os.path.join(CLOTHES_DIR, "shirt_c7.png"),
        os.path.join(CLOTHES_DIR, "pants_dad.png"),
        os.path.join(CARTOON_DIR, "smirk.png"),
        skin_hex="#86DDA8", hair_hex="#1D222B",
        location_m=(8.95, 5.85, 0.02), yaw_deg=0.0,
        rig_type="R15", hair_style="bald", body_profile="tall_lanky",
    )
    kit.attach_core_hair(zor7, "Hair_CrazyDev_CS.glb", "#1D222B")

    miu_obj = kit.load_core_glb("Pet_Cat_Tuxedo.glb", col=col_props, location_m=(-2.0, 0.1, -3.0), scale=0.58)
    phone_obj, phone_scr_mat, lo_ph = create_phone_prop("Minh_Smartphone", col_props)
    phone_obj.location = (-24.0, 0.5, -4.0)

    def animate_root_track(arm_obj, keys: list):
        """Exact world loc/yaw timeline decoupled from staggered bone acting (zero Bezier drift across scene cuts)."""
        for fr, loc, yaw_deg, const in keys:
            arm_obj.location = loc
            arm_obj.rotation_euler = Euler((0.0, 0.0, math.radians(yaw_deg)), "XYZ")
            arm_obj.keyframe_insert(data_path="location", frame=fr)
            arm_obj.keyframe_insert(data_path="rotation_euler", frame=fr)
            if const and arm_obj.animation_data and arm_obj.animation_data.action:
                for fc in getattr(arm_obj.animation_data.action, "fcurves", []):
                    if fc.data_path in ("location", "rotation_euler"):
                        for kp in fc.keyframe_points:
                            if int(round(kp.co.x)) == fr:
                                kp.interpolation = "CONSTANT"

    # Minh Acting (bones staggered cleanly; root track isolated with CONSTANT on scene cuts!)
    m_arm = minh["armature"]
    minh_beats = [
        (1,   10, None, None, {"UpperTorso": (8, 0, 0), "RightUpperArm": (-42, 0, 12), "RightLowerArm": (-52, 0, 0), "LeftUpperArm": (-42, 0, -12), "LeftLowerArm": (-52, 0, 0)}),
        (265, 10, None, None, {"UpperTorso": (10, 0, 0), "RightUpperArm": (-48, 0, 10), "RightLowerArm": (-55, 0, 0), "LeftUpperArm": (-48, 0, -10), "LeftLowerArm": (-55, 0, 0)}),
        (275,  8, None, None, {"UpperTorso": (-14, 0, 0), "Head": (-10, 0, 0), "RightUpperArm": (-72, 0, 26), "RightLowerArm": (-35, 0, 0), "LeftUpperArm": (-72, 0, -26), "LeftLowerArm": (-35, 0, 0)}),
        (332, 10, None, None, {"UpperTorso": (6, 0, 0), "RightUpperArm": (-55, 0, 18), "RightLowerArm": (-75, 0, 0), "LeftUpperArm": (-15, 0, -10)}),
        (345,  8, None, None, {"UpperTorso": (-4, 0, 0), "Head": (12, 0, 0), "RightUpperArm": (-72, 0, -10), "RightLowerArm": (-48, 0, 0), "LeftUpperArm": (10, 0, -12)}),
        (472,  8, None, None, {"UpperTorso": (-4, 0, 0), "Head": (12, 0, 0), "RightUpperArm": (-72, 0, -10), "RightLowerArm": (-48, 0, 0), "LeftUpperArm": (-24, 0, -14)}),
        (486,  8, None, None, {"UpperTorso": (0, 0, 10), "Head": (0, 0, 18), "RightUpperArm": (-15, 0, 10), "RightLowerArm": (-20, 0, 0), "LeftUpperArm": (8, 0, -10)}),
        (544,  6, None, None, {"UpperTorso": (0, 0, 0), "Head": (0, 0, 0), "RightUpperArm": (-18, 0, 8), "LeftUpperArm": (-18, 0, -8)}),
        (680,  8, None, None, {"UpperTorso": (8, 0, 0), "RightUpperArm": (-20, 0, 8), "LeftUpperArm": (16, 0, -8)}),
        (736, 12, None, None, {"UpperTorso": (10, 0, 0), "RightUpperArm": (16, 0, 8), "LeftUpperArm": (-20, 0, -8)}),
        (745,  8, None, None, {"UpperTorso": (6, 0, 0), "RightUpperArm": (-20, 0, 10), "LeftUpperArm": (-20, 0, -10)}),
        (805, 10, None, None, {"UpperTorso": (-10, 0, 0), "Head": (-8, 0, 0), "RightUpperArm": (-58, 0, 22), "RightLowerArm": (-48, 0, 0), "LeftUpperArm": (-58, 0, -22), "LeftLowerArm": (-48, 0, 0)}),
        (1285, 8, None, None, {"UpperTorso": (4, 0, 0), "RightUpperArm": (-45, 0, 16), "RightLowerArm": (-55, 0, 0), "LeftUpperArm": (-45, 0, -16), "LeftLowerArm": (-55, 0, 0)}),
        (1505,10, None, None, {"UpperTorso": (-18, 0, 0), "Head": (-30, 0, 0), "RightUpperArm": (-95, 0, 18), "LeftUpperArm": (-35, 0, -15)}),
        (1586, 8, None, None, {"UpperTorso": (-20, 0, 0), "Head": (-34, 0, 0), "RightUpperArm": (-95, 0, 18), "LeftUpperArm": (-35, 0, -15)}),
    ]
    kit.act_r15_sequence(m_arm, minh_beats, breathe=True)
    animate_root_track(m_arm, [
        (1,    (-24.0, 0.58, 0.0), 180.0, False),
        (265,  (-24.0, 0.58, 0.0), 180.0, False),
        (276,  (-24.0, 0.42, 0.0), 180.0, True),
        (336,  (-24.0, 0.42, 0.0), 180.0, True),
        (344,  (-24.0,-0.45, 0.0),   8.0, True),
        (476,  (-24.0,-0.45, 0.0),   8.0, False),
        (488,  (-24.0,-0.45, 0.0),  68.0, True),
        (543,  (-24.0,-0.45, 0.0),  68.0, True),
        (544,  (-1.55,-0.35, 0.0),  90.0, True),
        (677,  (-1.55,-0.35, 0.0),  90.0, True),
        (678,  ( 3.10,-0.75, 0.0),  72.0, False),
        (736,  ( 5.70, 0.35, 0.0),  65.0, True),
        (744,  ( 5.70, 0.35, 0.0),  65.0, True),
        (745,  ( 7.45, 1.55, 0.0), 155.0, True),
        (1586, ( 7.45, 1.55, 0.0), 155.0, True),
    ])

    # Smartphone held squarely in front of Minh's right hand facing -Y camera across fr 340..475!
    for fr_hide in (1, 338, 477):
        phone_obj.location = (-24.0, 0.5, -4.0)
        phone_obj.rotation_euler = Euler((0, 0, 0), "XYZ")
        phone_obj.keyframe_insert("location", frame=fr_hide)
        phone_obj.keyframe_insert("rotation_euler", frame=fr_hide)
    for fr_show in (340, 475):
        phone_obj.location = (-23.82, -0.82, 1.16)
        phone_obj.rotation_euler = Euler((math.radians(-14.0), 0.0, math.radians(8.0)), "XYZ")
        phone_obj.keyframe_insert("location", frame=fr_show)
        phone_obj.keyframe_insert("rotation_euler", frame=fr_show)
    if phone_obj.animation_data and phone_obj.animation_data.action:
        for fc in getattr(phone_obj.animation_data.action, "fcurves", []):
            for kp in fc.keyframe_points:
                kp.interpolation = "CONSTANT"
    key_emissive_strength(phone_scr_mat, 1, 0.0)
    key_emissive_strength(phone_scr_mat, 338, 0.0)
    key_emissive_strength(phone_scr_mat, 340, 6.5)
    key_emissive_strength(phone_scr_mat, 476, 0.0)
    key_val(lo_ph.data, "energy", 1, 0.0)
    key_val(lo_ph.data, "energy", 338, 0.0)
    key_val(lo_ph.data, "energy", 340, 26.0)
    key_val(lo_ph.data, "energy", 476, 0.0)

    # Co Hoa + Miu Tuxedo Cat (faces -X toward Minh at yaw=-90°!)
    h_arm = cohoa["armature"]
    cohoa_beats = [
        (1,   10, None, None, {"RightUpperArm": (-45, 0, 12), "LeftUpperArm": (-45, 0, -12)}),
        (544,  8, None, None, {"UpperTorso": (12, 0, 0), "RightUpperArm": (-52, 0, 12), "RightLowerArm": (-58, 0, 0), "LeftUpperArm": (-52, 0, -12), "LeftLowerArm": (-58, 0, 0)}),
        (585, 10, None, None, {"UpperTorso": (-4, 0, 0), "RightUpperArm": (-50, 0, 14), "RightLowerArm": (-62, 0, 0), "LeftUpperArm": (-50, 0, -14), "LeftLowerArm": (-62, 0, 0)}),
        (615,  8, None, None, {"UpperTorso": (0, 0, 10), "Head": (0, 0, -16), "RightUpperArm": (-52, 0, 12), "RightLowerArm": (-60, 0, 0), "LeftUpperArm": (-82, 0, -64), "LeftLowerArm": (-12, 0, 0)}),
        (680,  8, None, None, {"UpperTorso": (10, 0, 0), "RightUpperArm": (-48, 0, 10), "LeftUpperArm": (-48, 0, -10)}),
        (736, 12, None, None, {"UpperTorso": (12, 0, 0), "RightUpperArm": (-48, 0, 10), "LeftUpperArm": (-48, 0, -10)}),
        (745,  8, None, None, {"UpperTorso": (4, 0, 0), "RightUpperArm": (-48, 0, 10), "RightLowerArm": (-55, 0, 0), "LeftUpperArm": (-48, 0, -10), "LeftLowerArm": (-55, 0, 0)}),
        (805, 10, None, None, {"UpperTorso": (-10, 0, 0), "Head": (-10, 0, 0), "RightUpperArm": (-55, 0, 18), "LeftUpperArm": (-55, 0, -18)}),
        (1290, 8, None, None, {"UpperTorso": (2, 0, 0), "RightUpperArm": (-45, 0, 15), "RightLowerArm": (-55, 0, 0), "LeftUpperArm": (-45, 0, -15), "LeftLowerArm": (-55, 0, 0)}),
        (1505,10, None, None, {"UpperTorso": (-18, 0, 0), "Head": (-32, 0, 0), "RightUpperArm": (-50, 0, 14), "LeftUpperArm": (-50, 0, -14)}),
        (1586, 8, None, None, {"UpperTorso": (-20, 0, 0), "Head": (-35, 0, 0), "RightUpperArm": (-50, 0, 14), "LeftUpperArm": (-50, 0, -14)}),
    ]
    kit.act_r15_sequence(h_arm, cohoa_beats, breathe=True)
    animate_root_track(h_arm, [
        (1,    (-2.20, 5.50, -3.0), -90.0, True),
        (543,  (-2.20, 5.50, -3.0), -90.0, True),
        (544,  ( 1.05, 0.25,  0.0), -72.0, False),
        (582,  ( 0.35,-0.35,  0.0), -90.0, True),
        (608,  ( 0.35,-0.35,  0.0), -90.0, False),
        (622,  ( 0.35,-0.35,  0.0), -35.0, True),
        (677,  ( 0.35,-0.35,  0.0), -35.0, True),
        (678,  ( 4.25,-0.10,  0.0),  65.0, False),
        (736,  ( 6.85, 0.85,  0.0),  65.0, True),
        (744,  ( 6.85, 0.85,  0.0),  65.0, True),
        (745,  ( 8.55, 1.35,  0.0), 180.0, True),
        (1586, ( 8.55, 1.35,  0.0), 180.0, True),
    ])

    # Lock Miu Tuxedo Cat cleanly at forearm/chest height (z=0.72m, below CoHoa's chin!)
    miu_obj.location = (-2.2, 5.5, -3.0); miu_obj.keyframe_insert("location", frame=1)
    miu_obj.location = (-2.2, 5.5, -3.0); miu_obj.keyframe_insert("location", frame=543)
    if miu_obj.animation_data and miu_obj.animation_data.action:
        for fc in getattr(miu_obj.animation_data.action, "fcurves", []):
            for kp in fc.keyframe_points:
                if int(round(kp.co.x)) in (1, 543):
                    kp.interpolation = "CONSTANT"
    for fr_m in range(544, 1587, 2):
        bpy.context.scene.frame_set(fr_m)
        mw = h_arm.matrix_world
        miu_obj.location = mw @ Vector((0.0, -0.34, 0.72))
        miu_obj.rotation_euler = Euler((0.0, 0.0, h_arm.rotation_euler.z + math.radians(90.0)), "XYZ")
        miu_obj.keyframe_insert("location", frame=fr_m)
        miu_obj.keyframe_insert("rotation_euler", frame=fr_m)

    # Chu Tu
    c_arm = chutu["armature"]
    chutu_beats = [
        (1,   10, None, None, {}),
        (678,  8, None, None, {"UpperTorso": (14, 0, 0), "RightUpperArm": (-35, 0, 12), "LeftUpperArm": (15, 0, -10)}),
        (736, 12, None, None, {"UpperTorso": (12, 0, 0), "RightUpperArm": (15, 0, 12), "LeftUpperArm": (-35, 0, -10)}),
        (745,  8, None, None, {"UpperTorso": (10, 0, 0), "RightUpperArm": (-82, 0, 10), "RightLowerArm": (-35, 0, 0), "LeftUpperArm": (-12, 0, -12)}),
        (788,  8, None, None, {"UpperTorso": (12, 0, 0), "RightUpperArm": (-76, 0, 12), "RightLowerArm": (-28, 0, 0), "LeftUpperArm": (-22, 0, -12)}),
        (805, 10, None, None, {"UpperTorso": (-12, 0, 0), "Head": (-10, 0, 0), "RightUpperArm": (-62, 0, 26), "RightLowerArm": (-45, 0, 0), "LeftUpperArm": (-62, 0, -26), "LeftLowerArm": (-45, 0, 0)}),
        (1290, 8, None, None, {"UpperTorso": (4, 0, 0), "RightUpperArm": (-52, 0, 22), "RightLowerArm": (-65, 0, 0), "LeftUpperArm": (-52, 0, -22), "LeftLowerArm": (-65, 0, 0)}),
        (1505,10, None, None, {"UpperTorso": (-18, 0, 0), "Head": (-32, 0, 0), "RightUpperArm": (-90, 0, 22), "LeftUpperArm": (-30, 0, -15)}),
        (1586, 8, None, None, {"UpperTorso": (-20, 0, 0), "Head": (-34, 0, 0), "RightUpperArm": (-90, 0, 22), "LeftUpperArm": (-30, 0, -15)}),
    ]
    kit.act_r15_sequence(c_arm, chutu_beats, breathe=True)
    animate_root_track(c_arm, [
        (1,    (3.00, 5.50, -3.0),  75.0, True),
        (677,  (3.00, 5.50, -3.0),  75.0, True),
        (678,  (5.55, 0.25,  0.0),  72.0, False),
        (736,  (8.15, 1.35,  0.0), 108.0, True),
        (744,  (8.15, 1.35,  0.0), 108.0, True),
        (745,  (8.75, 2.25,  0.0),-145.0, True),
        (804,  (8.75, 2.25,  0.0),-145.0, False),
        (812,  (9.55, 1.85,  0.0),-162.0, True),
        (1586, (9.55, 1.85,  0.0),-162.0, True),
    ])

    # Zor-7 standing clearly beside/behind Cosmic Battery (8.95, 5.85)
    z_arm = zor7["armature"]
    zor7_beats = [
        (1,   10, None, None, {"UpperTorso": (14, 0, 0), "Head": (12, 0, 0), "RightUpperArm": (-72, 0, 12), "RightLowerArm": (-32, 0, 0), "LeftUpperArm": (-72, 0, -12), "LeftLowerArm": (-32, 0, 0)}),
        (1088,10, None, None, {"UpperTorso": (16, 0, 0), "Head": (14, 0, 0), "RightUpperArm": (-75, 0, 10), "RightLowerArm": (-36, 0, 0), "LeftUpperArm": (-75, 0, -10), "LeftLowerArm": (-36, 0, 0)}),
        (1098, 6, None, None, {"UpperTorso": (-12, 0, 0), "Head": (-8, 0, 0), "RightUpperArm": (-88, 0, 34), "LeftUpperArm": (-88, 0, -34)}),
        (1118, 8, None, None, {"UpperTorso": (4, 0, 0), "Head": (6, 0, 8), "RightUpperArm": (-60, 0, 16), "RightLowerArm": (-40, 0, 0), "LeftUpperArm": (-20, 0, -14)}),
        (1165, 8, None, None, {"UpperTorso": (-12, 0, 0), "RightUpperArm": (-110, 0, 10), "RightLowerArm": (-28, 0, 0), "LeftUpperArm": (-45, 0, -18)}),
        (1225, 8, None, None, {"UpperTorso": (2, 0, 0), "RightUpperArm": (-32, 0, 14), "LeftUpperArm": (-32, 0, -14)}),
        (1360, 8, None, None, {"UpperTorso": (22, 0, 0), "RightUpperArm": (-82, 0, 12), "RightLowerArm": (-24, 0, 0), "LeftUpperArm": (-82, 0, -12), "LeftLowerArm": (-24, 0, 0)}),
        (1445, 8, None, None, {"UpperTorso": (10, 0, 0), "RightUpperArm": (-56, 0, 14), "RightLowerArm": (-72, 0, 0), "LeftUpperArm": (-56, 0, -14), "LeftLowerArm": (-72, 0, 0)}),
        (1508, 6, None, None, {"UpperTorso": (-10, 0, 0), "Head": (12, 0, 0), "RightUpperArm": (-138, 0, 22), "LeftUpperArm": (-138, 0, -22), "RightUpperLeg": (-22, 0, 0), "LeftUpperLeg": (18, 0, 0)}),
        (1545,18, None, None, {"UpperTorso": (-14, 0, 0), "Head": (18, 0, 0), "RightUpperArm": (-155, 0, 20), "LeftUpperArm": (-155, 0, -20), "RightUpperLeg": (-18, 0, 0), "LeftUpperLeg": (12, 0, 0)}),
        (1586,20, None, None, {"UpperTorso": (-16, 0, 0), "Head": (20, 0, 0), "RightUpperArm": (-160, 0, 20), "LeftUpperArm": (-160, 0, -20)}),
    ]
    kit.act_r15_sequence(z_arm, zor7_beats, breathe=True)
    animate_root_track(z_arm, [
        (1,    (8.95, 5.85, 0.02),  12.0, True),
        (1088, (8.95, 5.85, 0.02),  12.0, False),
        (1098, (8.95, 5.85, 0.18),  16.0, False),
        (1118, (8.95, 5.85, 0.02),  12.0, True),
        (1348, (8.95, 5.85, 0.02),  12.0, False),
        (1365, (9.02, 5.95, 0.02), -90.0, True),
        (1499, (9.02, 5.95, 0.02), -90.0, True),
        (1500, (8.60, 2.35, 0.45),  22.0, False),
        (1545, (8.60, 1.35, 2.85),  24.0, False),
        (1586, (8.60, 0.20, 6.20),  28.0, True),
    ])

    # Door swings INWARD LEFT (+105°) into Room 04 wall — ZERO porch or doorway obstruction!
    dp = env_refs["door_pivot"]
    dp.rotation_euler = Euler((0, 0, 0), "XYZ"); dp.keyframe_insert("rotation_euler", frame=1)
    dp.rotation_euler = Euler((0, 0, 0), "XYZ"); dp.keyframe_insert("rotation_euler", frame=794)
    dp.rotation_euler = Euler((0, 0, math.radians(+105.0)), "XYZ"); dp.keyframe_insert("rotation_euler", frame=840)

    # Cable Yank
    cb = env_refs["cable"]
    cb.location = (8.75, 5.05, 1.88); cb.keyframe_insert("location", frame=1)
    cb.location = (8.75, 5.05, 1.88); cb.keyframe_insert("location", frame=1156)
    cb.location = (8.75, 5.05, 2.75); cb.keyframe_insert("location", frame=1175)

    bm1, bm2, bat = env_refs["bm1"], env_refs["bm2"], env_refs["bat_core"]
    for fr_init in (1, 1468):
        bm1.location = (9.90, 5.90, 0.84); bm1.keyframe_insert("location", frame=fr_init)
        bm2.location = (10.12, 6.02, 0.84); bm2.keyframe_insert("location", frame=fr_init)
    kit.bake_prop_follow(bm1, z_arm, "RightLowerArm", 1470, total_frames, local_offset=(0.0, -0.04, -0.22), step=2)
    kit.bake_prop_follow(bm2, z_arm, "LeftLowerArm",  1470, total_frames, local_offset=(0.0, -0.04, -0.22), step=2)

    bat.location = (8.75, 5.05, 0.27); bat.keyframe_insert("location", frame=1)
    bat.location = (8.75, 5.05, 0.27); bat.keyframe_insert("location", frame=1498)
    kit.bake_prop_follow(bat, z_arm, "LowerTorso", 1500, total_frames, local_offset=(0.0, -0.34, 0.05), step=2, follow_rot="root")

    # Setup Dynamic Cartoon Expressions
    face_pack = kit.load_face_pack(CARTOON_DIR)
    minh_sched = kit.build_lipsync_schedule(WORDS_PATH, total_frames, fps=30, base_expr="neutral", emotion_overrides=[
        (232, 266, "neutral", False),
        (267, 336, "angry", False),
        (337, 475, "shocked", False),
        (476, 677, "shocked", False),
        (678, 797, "angry", False),
        (798, 1226, "shocked", False),
        (1227, 1348, "happy", False),
        (1349, 1586, "pop_eyes", False),
    ])
    cohoa_sched = ["scared"] * (total_frames + 1)
    for fr in range(605, 678): cohoa_sched[fr] = "shocked"
    for fr in range(798, 1227): cohoa_sched[fr] = "shocked"
    for fr in range(1227, 1349): cohoa_sched[fr] = "happy"
    for fr in range(1349, total_frames + 1): cohoa_sched[fr] = "pop_eyes"

    chutu_sched = ["steam_angry"] * (total_frames + 1)
    for fr in range(798, 1227): chutu_sched[fr] = "shocked"
    for fr in range(1227, 1349): chutu_sched[fr] = "happy"
    for fr in range(1349, total_frames + 1): chutu_sched[fr] = "pop_eyes"

    zor7_sched = ["smirk"] * (total_frames + 1)
    for fr in range(1089, 1126): zor7_sched[fr] = "shocked"
    for fr in range(1500, total_frames + 1): zor7_sched[fr] = "silly_tongue"

    char_face_map = [
        (minh["face_tex_node"], minh_sched),
        (cohoa["face_tex_node"], cohoa_sched),
        (chutu["face_tex_node"], chutu_sched),
        (zor7["face_tex_node"], zor7_sched),
    ]

    def _face_updater(scene, depsgraph=None):
        fr = max(1, min(total_frames, scene.frame_current))
        for tex_node, sched in char_face_map:
            key = sched[fr]
            img = face_pack.get(key) or face_pack.get("neutral")
            if img and tex_node.image != img:
                tex_node.image = img

    bpy.app.handlers.frame_change_pre.clear()
    bpy.app.handlers.frame_change_pre.append(_face_updater)
    _face_updater(bpy.context.scene)

    return {"Minh": minh, "CoHoa": cohoa, "ChuTu": chutu, "Zor7": zor7, "Miu": miu_obj, "Phone": phone_obj}


def build_21_beat_cameras(plan, cast, env_refs):
    cam_d = bpy.data.cameras.new("MasterCam")
    cam = bpy.data.objects.new("MasterCam", cam_d)
    bpy.context.scene.collection.children[0].objects.link(cam)
    bpy.context.scene.camera = cam

    shot_log = []
    for b in plan["beats"]:
        bi = b["beat_index"]
        fs, fe = b["fs"], b["fe"]

        if bi == 1:
            aim_cam(cam, fs, fe, (-4.2, -1.2, 1.55), (3.8, 2.4, 1.35), lens=26.0, pos2=(-3.4, -0.8, 1.50), shot_log=shot_log, scale_tag="WS", angle_tag="eye")
        elif bi == 2:
            # Dark alley framing glowing green Room 04 window down the wet street
            aim_cam(cam, fs, fe, (3.6, -0.6, 1.15), (7.45, 3.10, 1.40), lens=44.0, shot_log=shot_log, scale_tag="MCU", angle_tag="low")
        elif bi == 3:
            # CU framing frosted green mullioned window at Room 04
            aim_cam(cam, fs, fe, (5.8, 1.25, 1.85), (7.25, 3.08, 1.52), lens=54.0, pos2=(6.0, 1.45, 1.80), shot_log=shot_log, scale_tag="CU", angle_tag="high")
        elif bi == 4:
            # LOC_01 Minh's desk shot from front-right framing Minh's angry face cleanly above dark laptop & desk!
            aim_cam(cam, fs, fe, (-23.10, 1.68, 1.48), (-24.0, 0.50, 1.24), lens=32.0, pos2=(-23.22, 1.70, 1.46), shot_log=shot_log, scale_tag="MCU", angle_tag="low")
        elif bi == 5:
            # LOC_01 Minh standing clear at y=-0.45 holding bright glowing smartphone facing camera
            aim_cam(cam, fs, fe, (-24.15, -2.15, 1.18), (-24.0, -0.45, 1.18), lens=36.0, pos2=(-24.25, -2.35, 1.20), shot_log=shot_log, scale_tag="MS", angle_tag="low")
        elif bi == 6:
            # INSERT directly framing Minh's bright cyan-green smartphone chat screen!
            aim_cam(cam, fs, fe, (-23.82, -1.32, 1.20), (-23.82, -0.82, 1.16), lens=44.0, roll_deg=5.0, pos2=(-23.82, -1.24, 1.19), shot_log=shot_log, scale_tag="INSERT", angle_tag="dutch")
        elif bi == 7:
            # CU Minh standing clear at y=-0.45 turning right toward emerald green window!
            aim_cam(cam, fs, fe, (-22.65, -0.95, 1.32), (-24.0, -0.45, 1.32), lens=44.0, roll_deg=-4.5, shot_log=shot_log, scale_tag="CU", angle_tag="dutch")
        elif bi == 8:
            # OTS past Minh's shoulder cleanly targeting Co Hoa's terrified face + Miu!
            aim_cam(cam, fs, fe, (-2.30, -0.95, 1.28), (0.35, -0.35, 1.24), lens=38.0, shot_log=shot_log, scale_tag="OTS", angle_tag="low")
        elif bi == 9:
            # CU Co Hoa scared/shocked face pointing down alley while holding Miu
            aim_cam(cam, fs, fe, (-0.55, -1.45, 1.48), (0.35, -0.35, 1.24), lens=44.0, pos2=(-0.40, -1.30, 1.44), shot_log=shot_log, scale_tag="CU", angle_tag="high")
        elif bi == 10:
            # Creep walk down alley targeting Chu Tu's determined profile + Minh & CoHoa behind!
            aim_cam(cam, fs, fe, (8.6, -2.05, 1.85), (6.5, 0.45, 1.15), lens=38.0, pos2=(9.1, -1.90, 1.80), shot_log=shot_log, scale_tag="MCU", angle_tag="high")
        elif bi == 11:
            # CU Chu Tu angry mustachioed face + raised knocking fist right in front of closed Room 04 door!
            aim_cam(cam, fs, fe, (9.65, 2.82, 1.32), (8.75, 2.25, 1.24), lens=36.0, pos2=(9.55, 2.75, 1.32), shot_log=shot_log, scale_tag="CU", angle_tag="low")
        elif bi == 12:
            # MS reverse angle INSIDE open Room 04 doorway framing ALL 3 shocked faces + Miu!
            aim_cam(cam, fs, fe, (8.60, 4.10, 1.34), (8.45, 1.50, 1.18), lens=24.0, roll_deg=4.5, pos2=(8.60, 4.25, 1.32), shot_log=shot_log, scale_tag="MS", angle_tag="dutch")
        elif bi == 13:
            # MS inside Room 04 framing Zor-7 (x=8.95) clear of cable (x=8.75) holding wire!
            aim_cam(cam, fs, fe, (9.45, 3.35, 1.32), (8.88, 5.65, 1.18), lens=34.0, pos2=(9.35, 3.65, 1.30), shot_log=shot_log, scale_tag="MS", angle_tag="eye")
        elif bi == 14:
            # CU 45° framing glowing emerald Cosmic Battery Cage on Room 04 floor!
            aim_cam(cam, fs, fe, (8.05, 3.95, 0.88), (8.75, 5.05, 0.28), lens=54.0, pos2=(8.18, 4.10, 0.82), shot_log=shot_log, scale_tag="CU", angle_tag="low")
        elif bi == 15:
            # MCU Zor-7 startled shocked -> smirk facing doorway
            aim_cam(cam, fs, fe, (9.15, 4.35, 1.32), (8.95, 5.85, 1.34), lens=48.0, pos2=(9.10, 4.50, 1.32), shot_log=shot_log, scale_tag="MCU", angle_tag="eye")
        elif bi == 16:
            # CU hand yanking cable free of dark battery (cool moon doorway bounce keeps action crisp!)
            aim_cam(cam, fs, fe, (8.10, 4.10, 0.92), (8.82, 5.20, 0.85), lens=48.0, shot_log=shot_log, scale_tag="CU", angle_tag="low")
        elif bi == 17:
            # WS alley all streetlights + cottage windows brightly back ON!
            aim_cam(cam, fs, fe, (-3.6, -1.0, 1.35), (4.0, 2.4, 1.35), lens=26.0, pos2=(-4.3, -1.2, 1.40), shot_log=shot_log, scale_tag="WS", angle_tag="low")
        elif bi == 18:
            # MCU from inside Room 04 doorway framing Minh, CoHoa, ChuTu smiling happy together!
            aim_cam(cam, fs, fe, (8.60, 3.95, 1.32), (8.45, 1.50, 1.20), lens=26.0, pos2=(8.60, 4.05, 1.30), shot_log=shot_log, scale_tag="MCU", angle_tag="low")
        elif bi == 19:
            # MS inside warm Room 04 tracking Zor-7 lunging toward dining table
            aim_cam(cam, fs, fe, (7.85, 4.15, 1.35), (9.35, 5.95, 1.20), lens=36.0, pos2=(8.05, 4.35, 1.32), shot_log=shot_log, scale_tag="MS", angle_tag="eye")
        elif bi == 20:
            # CU overhead-diagonal onto tabletop clearly framing the 2 golden Banh Mi + Zor-7's green hands grabbing!
            aim_cam(cam, fs, fe, (8.55, 4.45, 1.52), (9.55, 5.95, 0.92), lens=30.0, pos2=(8.70, 4.60, 1.46), shot_log=shot_log, scale_tag="CU", angle_tag="high")
        elif bi == 21:
            # WS exterior porch sky escape tracking Zor-7 blasting skyward clutching Banh Mi & Battery!
            aim_cam(cam, fs, fe, (6.5, -1.35, 1.15), (8.6, 1.5, 2.25), lens=26.0, pos2=(6.1, -1.85, 1.20), tgt2=(8.6, 1.2, 3.10), shot_log=shot_log, scale_tag="WS", angle_tag="low")

    return cam, shot_log


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["preview", "final"], default="preview")
    ap.add_argument("--beats", default="", help="Optional comma-separated beat indices to render in preview mode")
    ap.add_argument("--samples", type=int, default=16, help="Cycles samples per frame")
    ap.add_argument("--max-frames", type=int, default=0, help="Limit frame count for benchmarking")
    args = ap.parse_args(argv)

    clear_scene()
    plan = json.load(open(PLAN_PATH, encoding="utf-8"))
    total_frames = int(round(plan["runtime"] * plan["fps"]))
    sc = bpy.context.scene
    sc.render.fps = plan["fps"]
    sc.frame_start = 1
    sc.frame_end = total_frames

    col_env = bpy.data.collections.new("Env_Alley")
    sc.collection.children.link(col_env)
    col_props = bpy.data.collections.new("Props")
    sc.collection.children.link(col_props)

    env.apply_cinematic_mood(col_env, mood="real_outdoor", clouds=True, use_cycles=True, cycles_samples=args.samples)
    sc.cycles.max_bounces = 4
    sc.cycles.diffuse_bounces = 2
    sc.cycles.glossy_bounces = 2
    sc.cycles.adaptive_threshold = 0.03
    sc.render.use_persistent_data = True
    env_refs = build_alley_world(col_env, col_props)
    setup_world_lighting_timeline(env_refs)
    cast = build_cast_and_acting(env_refs, col_props, total_frames)
    cam, shot_log = build_21_beat_cameras(plan, cast, env_refs)

    cam_audit = kit.audit_camera_plan(shot_log)
    sample_frames = sorted(set([10, 68, 130, 268, 400, 560, 630, 710, 845, 960, 1105, 1165, 1260, 1380, 1460, 1525]))
    col_audit = kit.audit_scene_collisions(
        [cast["Minh"], cast["CoHoa"], cast["ChuTu"], cast["Zor7"]],
        obstacles=env_refs["obstacles"],
        frames=sample_frames,
    )
    print(f"[AUDIT_CAMERA] {json.dumps(cam_audit)}")
    print(f"[AUDIT_COLLISIONS] violations={len(col_audit)} details={json.dumps(col_audit[:10])}")

    stage_dir = kit.get_stage_dir("alien_blackout")
    os.makedirs(stage_dir, exist_ok=True)
    with open(os.path.join(stage_dir, "audit_report.json"), "w", encoding="utf-8") as af:
        json.dump({"camera_audit": cam_audit, "collision_violations": len(col_audit), "collision_details": col_audit[:20]}, af, indent=2)
    kit.pack_all_textures()
    blend_path = os.path.join(stage_dir, "scene_built.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)
    print(f"[SAVED_BLEND] {blend_path}")

    if args.mode == "preview":
        only_beats = {int(x.strip()) for x in args.beats.split(",") if x.strip()} if args.beats else None
        prev_dir = os.path.join(stage_dir, "preview")
        os.makedirs(prev_dir, exist_ok=True)
        sc.render.resolution_x = 540
        sc.render.resolution_y = 960
        sc.render.image_settings.file_format = "PNG"
        for b in plan["beats"]:
            bi = b["beat_index"]
            if only_beats and bi not in only_beats:
                continue
            mid = (b["fs"] + b["fe"]) // 2
            if bi == 1: mid = 82
            elif bi == 4: mid = 295
            elif bi == 12: mid = 865
            elif bi == 15: mid = 1108
            elif bi == 16: mid = 1172
            elif bi == 20: mid = 1445
            elif bi == 21: mid = 1532
            sc.frame_set(mid)
            sc.render.filepath = os.path.join(prev_dir, f"beat_{bi:02d}_f{mid:04d}.png")
            bpy.ops.render.render(write_still=True)
        print(f"[PREVIEW_DONE] rendered -> {prev_dir}")
    else:
        import time
        srt_shots = json.load(open(os.path.join(HERE, "srt_shots.json"), encoding="utf-8"))["shots"]
        shots_dir = os.path.join(stage_dir, "shots")
        os.makedirs(shots_dir, exist_ok=True)
        sc.render.resolution_x = 1080
        sc.render.resolution_y = 1920
        sc.render.image_settings.file_format = "PNG"

        # Map each frame 1..total_frames into compile_video.py shot folders s01..s13 seamlessly!
        def _shot_folder_for_frame(fr_idx: int) -> str:
            t_sec = (fr_idx - 1) / float(plan["fps"])
            for s in srt_shots:
                if float(s["window_start"]) - 1e-4 <= t_sec < float(s["window_end"]) - 1e-4:
                    return f"s{int(s['index']):02d}"
            return f"s{int(srt_shots[-1]['index']):02d}"

        end_fr = args.max_frames if args.max_frames > 0 else total_frames
        t0 = time.time()
        rendered = 0
        for fr in range(1, end_fr + 1):
            sf = _shot_folder_for_frame(fr)
            s_dir = os.path.join(shots_dir, sf)
            os.makedirs(s_dir, exist_ok=True)
            out_fp = os.path.join(s_dir, f"frame_{fr:05d}.png")
            if os.path.exists(out_fp) and os.path.getsize(out_fp) > 1000:
                continue
            t_fr = time.time()
            sc.frame_set(fr)
            sc.render.filepath = out_fp
            bpy.ops.render.render(write_still=True)
            rendered += 1
            dt_fr = time.time() - t_fr
            avg_fr = (time.time() - t0) / max(1, rendered)
            print(f"[FRAME {fr:04d}/{end_fr:04d}] ({sf}) rendered in {dt_fr:.2f}s (avg {avg_fr:.2f}s/f)", flush=True)
        dt = time.time() - t0
        print(f"[FINAL_RENDER_DONE] rendered={rendered} frames in {dt:.1f}s ({dt/max(1,rendered):.2f}s/frame) -> {shots_dir}")


if __name__ == "__main__":
    main()

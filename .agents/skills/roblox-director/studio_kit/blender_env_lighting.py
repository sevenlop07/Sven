#!/usr/bin/env python3
"""
blender_env_lighting.py — Studio-Grade Procedural Sets & 6-Point Cinematic Lighting for @RobloxDirector.
Replaces flat untextured cubes and washed-out floodlights with:
- Physical MULTIPLE_SCATTERING sky / night city-glow + directional warm/cool 3-point + Hero Rim rig
- Blender 5.3 Compositor Aerial Mist haze + subtle FOG_GLOW bloom on practical windows & streetlamps
- Procedural textured paving slabs, beveled curbstones, wet asphalt + dashed lane markings
- Detailed pitched-roof clapboard houses (porches, chimneys, shuttered glowing windows, flower boxes)
- Real picket fences, cast-iron streetlamps, layered foliage trees, mailboxes & hydrants on all 3 planes
"""
import math
import bpy
import bmesh
from mathutils import Euler, Vector


def _hex_rgba(hex_str: str, alpha: float = 1.0):
    h = hex_str.lstrip("#")
    r, g, b = [int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4)]
    def lin(c): return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return (lin(r), lin(g), lin(b), alpha)


def _link(obj, col):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)
    return obj


def _set_socket(node, name, value):
    if name in node.inputs:
        node.inputs[name].default_value = value


def make_solid_mat(name: str, hex_col: str, roughness: float = 0.55, metallic: float = 0.0):
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = _hex_rgba(hex_col)
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    return mat


def make_emissive_mat(name: str, hex_col: str = "#FFE09E", strength: float = 3.0):
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    col = _hex_rgba(hex_col)
    bsdf.inputs["Base Color"].default_value = col
    bsdf.inputs["Roughness"].default_value = 0.15
    if "Emission Color" in bsdf.inputs:
        bsdf.inputs["Emission Color"].default_value = col
        bsdf.inputs["Emission Strength"].default_value = strength
    return mat


def make_cladding_mat(name: str, base_hex: str, dark_hex: str, row_freq: float = 7.5, brick_offset: float = 0.0, mortar: float = 0.03, roughness: float = 0.68):
    """Procedural horizontal clapboard siding or staggered brick masonry with real plank/grout bump."""
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = roughness

    tc = nt.nodes.new("ShaderNodeTexCoord")
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Scale"].default_value = (1.0, 1.0, 1.0)
    nt.links.new(tc.outputs["Object"], mp.inputs["Vector"])

    # Combine XY so horizontal siding wraps cleanly on both X-facing and Y-facing walls!
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(mp.outputs["Vector"], sep.inputs["Vector"])
    add_xy = nt.nodes.new("ShaderNodeMath")
    add_xy.operation = "ADD"
    nt.links.new(sep.outputs["X"], add_xy.inputs[0])
    nt.links.new(sep.outputs["Y"], add_xy.inputs[1])
    comb = nt.nodes.new("ShaderNodeCombineXYZ")
    nt.links.new(add_xy.outputs["Value"], comb.inputs["X"])
    nt.links.new(sep.outputs["Z"], comb.inputs["Y"])

    brick = nt.nodes.new("ShaderNodeTexBrick")
    brick.offset = brick_offset
    brick.inputs["Scale"].default_value = row_freq
    brick.inputs["Mortar Size"].default_value = mortar
    brick.inputs["Mortar Smooth"].default_value = 0.35
    brick.inputs["Bias"].default_value = 0.0
    brick.inputs["Brick Width"].default_value = 3.8 if brick_offset == 0.0 else 0.72
    brick.inputs["Row Height"].default_value = 0.25 if brick_offset == 0.0 else 0.32
    brick.inputs["Color1"].default_value = _hex_rgba(base_hex)
    brick.inputs["Color2"].default_value = _hex_rgba(dark_hex)
    brick.inputs["Mortar"].default_value = _hex_rgba(dark_hex)
    nt.links.new(comb.outputs["Vector"], brick.inputs["Vector"])

    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.28
    bump.inputs["Distance"].default_value = 0.025
    nt.links.new(brick.outputs["Fac"], bump.inputs["Height"])

    nt.links.new(brick.outputs["Color"], bsdf.inputs["Base Color"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_paving_mat(name: str = "SidewalkSlabs", light_hex: str = "#CBD1DA", dark_hex: str = "#AAB2BE"):
    """Procedural concrete sidewalk slabs with expansion joints and subtle weathered grit."""
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")

    tc = nt.nodes.new("ShaderNodeTexCoord")
    brick = nt.nodes.new("ShaderNodeTexBrick")
    brick.offset = 0.0
    brick.inputs["Scale"].default_value = 1.15
    brick.inputs["Mortar Size"].default_value = 0.018
    brick.inputs["Mortar Smooth"].default_value = 0.25
    brick.inputs["Brick Width"].default_value = 1.25
    brick.inputs["Row Height"].default_value = 1.25
    brick.inputs["Color1"].default_value = _hex_rgba(light_hex)
    brick.inputs["Color2"].default_value = _hex_rgba(dark_hex)
    brick.inputs["Mortar"].default_value = _hex_rgba("#6E7582")
    nt.links.new(tc.outputs["Object"], brick.inputs["Vector"])

    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 4.5
    noise.inputs["Detail"].default_value = 6.0
    nt.links.new(tc.outputs["Object"], noise.inputs["Vector"])

    mix_col = nt.nodes.new("ShaderNodeMix")
    mix_col.data_type = "RGBA"
    mix_col.inputs[0].default_value = 0.14
    nt.links.new(brick.outputs["Color"], mix_col.inputs[6])
    nt.links.new(noise.outputs["Fac"], mix_col.inputs[7])

    mix_r = nt.nodes.new("ShaderNodeMapRange")
    mix_r.inputs["From Min"].default_value = 0.3
    mix_r.inputs["From Max"].default_value = 0.7
    mix_r.inputs["To Min"].default_value = 0.58
    mix_r.inputs["To Max"].default_value = 0.85
    nt.links.new(noise.outputs["Fac"], mix_r.inputs["Value"])

    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.22
    bump.inputs["Distance"].default_value = 0.015
    nt.links.new(brick.outputs["Fac"], bump.inputs["Height"])

    nt.links.new(mix_col.outputs[2], bsdf.inputs["Base Color"])
    nt.links.new(mix_r.outputs["Result"], bsdf.inputs["Roughness"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_foliage_mat(name: str, col1_hex: str = "#3E7E44", col2_hex: str = "#5CA34C"):
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 0.72
    if "Subsurface Weight" in bsdf.inputs:
        bsdf.inputs["Subsurface Weight"].default_value = 0.18
    tc = nt.nodes.new("ShaderNodeTexCoord")
    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 6.5
    noise.inputs["Detail"].default_value = 5.0
    nt.links.new(tc.outputs["Object"], noise.inputs["Vector"])
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.30
    ramp.color_ramp.elements[0].color = _hex_rgba(col1_hex)
    ramp.color_ramp.elements[1].position = 0.72
    ramp.color_ramp.elements[1].color = _hex_rgba(col2_hex)
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.30
    bump.inputs["Distance"].default_value = 0.03
    nt.links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
    nt.links.new(noise.outputs["Fac"], bump.inputs["Height"])
    nt.links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_weathered_stone_mat(name: str, base_hex: str = "#8C867E", dark_hex: str = "#2F2C2A", scale: float = 3.2):
    """Gritty weathered masonry/stucco with multi-scale bump, Voronoi cracks & Ambient Occlusion crevice dirt."""
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")

    tc = nt.nodes.new("ShaderNodeTexCoord")
    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = scale
    noise.inputs["Detail"].default_value = 9.0
    noise.inputs["Roughness"].default_value = 0.65
    nt.links.new(tc.outputs["Object"], noise.inputs["Vector"])

    vor = nt.nodes.new("ShaderNodeTexVoronoi")
    vor.feature = "DISTANCE_TO_EDGE"
    vor.inputs["Scale"].default_value = scale * 2.2
    nt.links.new(tc.outputs["Object"], vor.inputs["Vector"])

    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.28
    ramp.color_ramp.elements[0].color = _hex_rgba(dark_hex)
    ramp.color_ramp.elements[1].position = 0.72
    ramp.color_ramp.elements[1].color = _hex_rgba(base_hex)
    nt.links.new(noise.outputs["Fac"], ramp.inputs["Fac"])

    ao = nt.nodes.new("ShaderNodeAmbientOcclusion")
    ao.inputs["Distance"].default_value = 0.45
    mix_ao = nt.nodes.new("ShaderNodeMix")
    mix_ao.data_type = "RGBA"
    mix_ao.blend_type = "MULTIPLY"
    mix_ao.inputs[0].default_value = 0.65
    nt.links.new(ramp.outputs["Color"], mix_ao.inputs[6])
    nt.links.new(ao.outputs["Color"], mix_ao.inputs[7])

    map_r = nt.nodes.new("ShaderNodeMapRange")
    map_r.inputs["To Min"].default_value = 0.62
    map_r.inputs["To Max"].default_value = 0.94
    nt.links.new(noise.outputs["Fac"], map_r.inputs["Value"])

    mul_b = nt.nodes.new("ShaderNodeMath")
    mul_b.operation = "MULTIPLY_ADD"
    mul_b.inputs[1].default_value = 0.65
    nt.links.new(noise.outputs["Fac"], mul_b.inputs[0])
    nt.links.new(vor.outputs["Distance"], mul_b.inputs[2])

    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.55
    bump.inputs["Distance"].default_value = 0.04
    nt.links.new(mul_b.outputs["Value"], bump.inputs["Height"])

    nt.links.new(mix_ao.outputs[2], bsdf.inputs["Base Color"])
    nt.links.new(map_r.outputs["Result"], bsdf.inputs["Roughness"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_weathered_wood_mat(name: str = "WeatheredFenceWood", base_hex: str = "#5B534C", dark_hex: str = "#2A2623"):
    """Weathered vertical wood grain with plank bump and dark AO crevices."""
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 0.82

    tc = nt.nodes.new("ShaderNodeTexCoord")
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Scale"].default_value = (14.0, 14.0, 1.8)
    nt.links.new(tc.outputs["Object"], mp.inputs["Vector"])

    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 3.5
    noise.inputs["Detail"].default_value = 8.0
    nt.links.new(mp.outputs["Vector"], noise.inputs["Vector"])

    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.30
    ramp.color_ramp.elements[0].color = _hex_rgba(dark_hex)
    ramp.color_ramp.elements[1].position = 0.74
    ramp.color_ramp.elements[1].color = _hex_rgba(base_hex)
    nt.links.new(noise.outputs["Fac"], ramp.inputs["Fac"])

    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.42
    bump.inputs["Distance"].default_value = 0.025
    nt.links.new(noise.outputs["Fac"], bump.inputs["Height"])

    nt.links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_wet_mud_puddle_mat(name: str = "WetMudPuddles", mud_hex: str = "#382619", wet_hex: str = "#1A110B"):
    """Realistic wet earth/mud ground splitting mirror puddles (roughness 0.05) and matte mud ridges."""
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")

    tc = nt.nodes.new("ShaderNodeTexCoord")
    noise_macro = nt.nodes.new("ShaderNodeTexNoise")
    noise_macro.inputs["Scale"].default_value = 1.6
    noise_macro.inputs["Detail"].default_value = 6.0
    nt.links.new(tc.outputs["Object"], noise_macro.inputs["Vector"])

    noise_micro = nt.nodes.new("ShaderNodeTexNoise")
    noise_micro.inputs["Scale"].default_value = 12.0
    noise_micro.inputs["Detail"].default_value = 8.0
    nt.links.new(tc.outputs["Object"], noise_micro.inputs["Vector"])

    col_ramp = nt.nodes.new("ShaderNodeValToRGB")
    col_ramp.color_ramp.elements[0].position = 0.38
    col_ramp.color_ramp.elements[0].color = _hex_rgba(wet_hex)
    col_ramp.color_ramp.elements[1].position = 0.66
    col_ramp.color_ramp.elements[1].color = _hex_rgba(mud_hex)
    nt.links.new(noise_macro.outputs["Fac"], col_ramp.inputs["Fac"])

    rough_ramp = nt.nodes.new("ShaderNodeValToRGB")
    rough_ramp.color_ramp.elements[0].position = 0.44
    rough_ramp.color_ramp.elements[0].color = (0.05, 0.05, 0.05, 1.0)
    rough_ramp.color_ramp.elements[1].position = 0.56
    rough_ramp.color_ramp.elements[1].color = (0.72, 0.72, 0.72, 1.0)
    nt.links.new(noise_macro.outputs["Fac"], rough_ramp.inputs["Fac"])

    # Flat mirror normals on wet puddles, bumpy micro-grit on raised mud
    mul_bump = nt.nodes.new("ShaderNodeMath")
    mul_bump.operation = "MULTIPLY"
    nt.links.new(noise_micro.outputs["Fac"], mul_bump.inputs[0])
    nt.links.new(rough_ramp.outputs["Color"], mul_bump.inputs[1])

    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.48
    bump.inputs["Distance"].default_value = 0.03
    nt.links.new(mul_bump.outputs["Value"], bump.inputs["Height"])

    nt.links.new(col_ramp.outputs["Color"], bsdf.inputs["Base Color"])
    nt.links.new(rough_ramp.outputs["Color"], bsdf.inputs["Roughness"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_dark_window_glass_mat(name: str = "DarkReflectiveGlass"):
    """Daytime exterior window glass: dark interior backing + sharp sky reflection (no fake daytime neon)."""
    return make_solid_mat(name, "#0C1016", roughness=0.05, metallic=0.12)


def _add_box(name, loc, size, mat, col, bevel_m=0.012, rot_deg=(0, 0, 0)):
    mesh = bpy.data.meshes.new(name + "_M")
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x *= size[0]
        v.co.y *= size[1]
        v.co.z *= size[2]
    bm.to_mesh(mesh)
    bm.free()
    o = bpy.data.objects.new(name, mesh)
    o.location = loc
    o.rotation_euler = Euler([math.radians(a) for a in rot_deg])
    o.data.materials.append(mat)
    if bevel_m > 0.001:
        bv = o.modifiers.new("Bevel", "BEVEL")
        bv.width = bevel_m
        bv.segments = 2
    for p in o.data.polygons:
        p.use_smooth = True
    col.objects.link(o)
    return o


def _add_gable_roof(name, loc, width, depth, ridge_h, mat, col):
    """True pitched triangular gable roof mesh with overhanging eaves."""
    hw, hd = width * 0.5, depth * 0.5
    mesh = bpy.data.meshes.new(name + "_M")
    bm = bmesh.new()
    v_fl = bm.verts.new((-hw, -hd, 0.0))
    v_fr = bm.verts.new((hw, -hd, 0.0))
    v_br = bm.verts.new((hw, hd, 0.0))
    v_bl = bm.verts.new((-hw, hd, 0.0))
    v_rf = bm.verts.new((0.0, -hd, ridge_h))
    v_rb = bm.verts.new((0.0, hd, ridge_h))
    bm.faces.new((v_fl, v_fr, v_rf))
    bm.faces.new((v_br, v_bl, v_rb))
    bm.faces.new((v_fl, v_rf, v_rb, v_bl))
    bm.faces.new((v_fr, v_br, v_rb, v_rf))
    bm.faces.new((v_fl, v_bl, v_br, v_fr))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(mesh)
    bm.free()
    o = bpy.data.objects.new(name, mesh)
    o.location = loc
    o.data.materials.append(mat)
    es = o.modifiers.new("EdgeSplit", "EDGE_SPLIT")
    es.split_angle = math.radians(35)
    col.objects.link(o)
    return o


def build_hero_house(
    name: str,
    loc=(0.0, 5.8, 0.0),
    width: float = 4.8,
    depth: float = 3.8,
    wall_h: float = 3.3,
    wall_hex: str = "#E27864",
    wall_dark_hex: str = "#B85545",
    roof_hex: str = "#4C302B",
    trim_hex: str = "#F4F1E8",
    shutter_hex: str = "#2F4858",
    col=None,
    window_glow: float = 2.4,
    with_porch: bool = True,
):
    """Build a detailed multi-part suburban house with clapboard walls, gable roof, porch, chimney & glowing windows."""
    if col is None:
        col = bpy.context.scene.collection
    cx, cy, cz = loc
    root = bpy.data.objects.new(name + "_Root", None)
    root.location = (cx, cy, cz)
    col.objects.link(root)

    m_found = make_paving_mat(f"{name}_Found", "#8E95A0", "#737A86")
    m_wall = make_cladding_mat(f"{name}_Wall", wall_hex, wall_dark_hex, row_freq=6.5, brick_offset=0.0, mortar=0.025, roughness=0.68)
    m_roof = make_cladding_mat(f"{name}_Roof", roof_hex, "#2A1A18", row_freq=9.0, brick_offset=0.5, mortar=0.035, roughness=0.72)
    m_trim = make_solid_mat(f"{name}_Trim", trim_hex, 0.48)
    m_shut = make_solid_mat(f"{name}_Shutter", shutter_hex, 0.55)
    m_door = make_solid_mat(f"{name}_Door", "#5B3222", 0.45)
    m_brass = make_solid_mat(f"{name}_Brass", "#E2B246", 0.25, metallic=0.85)
    m_win = make_emissive_mat(f"{name}_WinGlow", "#FFDFA0", strength=window_glow)
    m_chim = make_cladding_mat(f"{name}_Brick", "#9D4438", "#6E2E26", row_freq=10.0, brick_offset=0.5, mortar=0.04, roughness=0.78)

    parts = []
    def attach(ob):
        ob.parent = root
        parts.append(ob)
        return ob

    # Foundation plinth + textured main box + corner pilasters
    attach(_add_box(f"{name}_Base", (0, 0, 0.18), (width + 0.14, depth + 0.14, 0.36), m_found, col))
    body = attach(_add_box(f"{name}_Body", (0, 0, 0.36 + wall_h * 0.5), (width, depth, wall_h), m_wall, col, bevel_m=0.008))
    for sx in (-1, 1):
        for sy in (-1, 1):
            attach(_add_box(f"{name}_Corner_{sx}_{sy}", (sx * (width * 0.5 - 0.05), sy * (depth * 0.5 - 0.05), 0.36 + wall_h * 0.5), (0.14, 0.14, wall_h + 0.02), m_trim, col))

    # Gable roof + eave fascia + brick chimney
    roof_z = 0.36 + wall_h
    attach(_add_box(f"{name}_Fascia", (0, 0, roof_z - 0.04), (width + 0.44, depth + 0.44, 0.14), m_trim, col))
    attach(_add_gable_roof(f"{name}_Gable", (0, 0, roof_z + 0.03), width + 0.52, depth + 0.52, 1.45, m_roof, col))
    attach(_add_box(f"{name}_Chimney", (width * 0.28, 0.25, roof_z + 1.05), (0.48, 0.48, 1.25), m_chim, col))
    attach(_add_box(f"{name}_ChimCap", (width * 0.28, 0.25, roof_z + 1.70), (0.58, 0.58, 0.10), m_found, col))

    # Framed Glowing Windows with Shutters & Flower Sills (front y = -depth/2)
    fy = -depth * 0.5
    def add_window(wtag, wx, wz, ww=0.86, wh=0.98):
        attach(_add_box(f"{name}_{wtag}_Frm", (wx, fy - 0.02, wz), (ww + 0.14, 0.08, wh + 0.14), m_trim, col))
        attach(_add_box(f"{name}_{wtag}_Gls", (wx, fy - 0.055, wz), (ww, 0.03, wh), m_win, col, bevel_m=0.0))
        attach(_add_box(f"{name}_{wtag}_MulV", (wx, fy - 0.072, wz), (0.045, 0.03, wh), m_trim, col, bevel_m=0.0))
        attach(_add_box(f"{name}_{wtag}_MulH", (wx, fy - 0.072, wz), (ww, 0.03, 0.045), m_trim, col, bevel_m=0.0))
        attach(_add_box(f"{name}_{wtag}_Sill", (wx, fy - 0.08, wz - wh * 0.5 - 0.06), (ww + 0.24, 0.16, 0.08), m_trim, col))
        for sgn in (-1, 1):
            attach(_add_box(f"{name}_{wtag}_Sht{sgn}", (wx + sgn * (ww * 0.5 + 0.20), fy - 0.03, wz), (0.24, 0.05, wh + 0.04), m_shut, col))

    if with_porch:
        # Door on left/center + porch overhang + columns + practical glowing porch lantern
        dx = -width * 0.20
        attach(_add_box(f"{name}_PorchDeck", (dx, fy - 0.52, 0.18), (1.85, 1.05, 0.36), m_found, col))
        attach(_add_box(f"{name}_PorchStep", (dx, fy - 1.15, 0.09), (1.45, 0.34, 0.18), m_found, col))
        attach(_add_box(f"{name}_DoorFrm", (dx, fy - 0.02, 1.44), (1.06, 0.10, 2.02), m_trim, col))
        attach(_add_box(f"{name}_Door", (dx, fy - 0.05, 1.42), (0.90, 0.06, 1.92), m_door, col))
        attach(_add_box(f"{name}_Knob", (dx + 0.32, fy - 0.10, 1.32), (0.08, 0.08, 0.08), m_brass, col))
        attach(_add_box(f"{name}_PorchRoof", (dx, fy - 0.56, 2.66), (2.05, 1.18, 0.16), m_roof, col))
        for px in (dx - 0.85, dx + 0.85):
            attach(_add_box(f"{name}_PorchCol_{px:.1f}", (px, fy - 0.96, 1.48), (0.14, 0.14, 2.28), m_trim, col))
        attach(_add_box(f"{name}_Lantern", (dx + 0.64, fy - 0.12, 2.02), (0.14, 0.14, 0.22), m_win, col))
        pl = bpy.data.lights.new(f"{name}_PorchLight", type="POINT")
        pl.energy = 14.0
        pl.use_temperature = True
        pl.temperature = 2700.0
        pl.shadow_soft_size = 0.25
        plo = bpy.data.objects.new(f"{name}_PorchLight", pl)
        plo.location = (dx, fy - 0.35, 2.05)
        col.objects.link(plo)
        attach(plo)
        add_window("WinG1", width * 0.24, 1.56)
    else:
        add_window("WinG1", -width * 0.24, 1.56)
        add_window("WinG2", width * 0.24, 1.56)

    # Upper windows (clean second-story row)
    if wall_h >= 3.0:
        add_window("WinU1", -width * 0.24, 2.75, ww=0.78, wh=0.80)
        add_window("WinU2", width * 0.24, 2.75, ww=0.78, wh=0.80)

    return body


def build_picket_fence(name: str, start_x: float, end_x: float, y: float, z: float = 0.08, col=None, fence_hex: str = "#F4F2EA"):
    """Real multi-picket fence with capped posts & stringer rails."""
    if col is None:
        col = bpy.context.scene.collection
    m_f = make_solid_mat(f"{name}_Mat", fence_hex, 0.52)
    length = abs(end_x - start_x)
    mid_x = 0.5 * (start_x + end_x)
    # 2 horizontal rails
    _add_box(f"{name}_RailTop", (mid_x, y, z + 0.56), (length, 0.05, 0.06), m_f, col, bevel_m=0.005)
    _add_box(f"{name}_RailBot", (mid_x, y, z + 0.20), (length, 0.05, 0.06), m_f, col, bevel_m=0.005)
    # Individual pickets every 0.22m & posts every 2.2m
    n_pk = max(2, int(round(length / 0.22)))
    for i in range(n_pk + 1):
        px = start_x + (end_x - start_x) * (i / float(n_pk))
        is_post = (i % 10 == 0 or i == n_pk)
        if is_post:
            _add_box(f"{name}_Post_{i}", (px, y, z + 0.42), (0.12, 0.12, 0.84), m_f, col, bevel_m=0.008)
            _add_box(f"{name}_PostCap_{i}", (px, y, z + 0.86), (0.16, 0.16, 0.05), m_f, col, bevel_m=0.006)
        else:
            _add_box(f"{name}_Pkt_{i}", (px, y - 0.03, z + 0.36), (0.09, 0.035, 0.72), m_f, col, bevel_m=0.005)
    # Invisible collision box representative for fast audit (keeps gaps between pickets open!)
    col_ref = _add_box(f"{name}_ColRef", (mid_x, y, z + 0.36), (length, 0.12, 0.72), m_f, col, bevel_m=0.0)
    col_ref.hide_render = True
    return col_ref


def build_streetlamp(name: str, loc=(0.0, 0.15, 0.08), col=None, lamp_energy: float = 35.0, face_road: float = -1.0):
    """Stylized cast-iron streetlamp with curved neck & warm glowing practical lantern."""
    if col is None:
        col = bpy.context.scene.collection
    x, y, z = loc
    m_iron = make_solid_mat("LampIron", "#202630", 0.38, metallic=0.72)
    m_bulb = make_emissive_mat("LampBulbGlow", "#FFD990", strength=4.8)
    base = _add_box(f"{name}_Base", (x, y, z + 0.25), (0.28, 0.28, 0.50), m_iron, col, bevel_m=0.015)
    _add_box(f"{name}_Pole", (x, y, z + 1.85), (0.11, 0.11, 2.85), m_iron, col, bevel_m=0.015)
    _add_box(f"{name}_Arm", (x, y + face_road * 0.26, z + 3.24), (0.09, 0.56, 0.09), m_iron, col, bevel_m=0.01)
    _add_box(f"{name}_Cap", (x, y + face_road * 0.48, z + 3.16), (0.34, 0.34, 0.08), m_iron, col, bevel_m=0.01)
    _add_box(f"{name}_Bulb", (x, y + face_road * 0.48, z + 2.98), (0.22, 0.22, 0.28), m_bulb, col, bevel_m=0.01)
    sp = bpy.data.lights.new(f"{name}_Spot", type="SPOT")
    sp.energy = lamp_energy
    sp.spot_size = math.radians(105)
    sp.spot_blend = 0.65
    sp.use_temperature = True
    sp.temperature = 2700.0
    sp.shadow_soft_size = 0.22
    spo = bpy.data.objects.new(f"{name}_Spot", sp)
    spo.location = (x, y + face_road * 0.48, z + 2.86)
    spo.rotation_euler = Euler((math.radians(-12 * face_road), 0, 0))
    col.objects.link(spo)
    return base


def build_stylized_tree(name: str, loc=(0.0, 4.0, 0.08), scale: float = 1.0, col=None, leaf_hex: str = "#3B7E43", leaf_hi: str = "#5CA64D"):
    """Layered multi-cluster stylized tree casting rich shadows."""
    if col is None:
        col = bpy.context.scene.collection
    x, y, z = loc
    m_bark = make_solid_mat("TreeBark_Stylized", "#5A3B28", 0.85)
    m_leaf = make_foliage_mat(f"{name}_Leaves", leaf_hex, leaf_hi)
    trunk = _add_box(f"{name}_Trunk", (x, y, z + 0.95 * scale), (0.32 * scale, 0.32 * scale, 1.90 * scale), m_bark, col, bevel_m=0.04)
    puffs = [
        (0.0, 0.0, 2.35, 1.05),
        (-0.58, 0.15, 2.05, 0.78),
        (0.58, -0.10, 2.08, 0.80),
        (0.10, 0.45, 2.18, 0.82),
        (-0.10, -0.45, 2.15, 0.76),
        (0.0, 0.0, 2.92, 0.72),
    ]
    for idx, (ox, oy, oz, r) in enumerate(puffs):
        bpy.ops.mesh.primitive_ico_sphere_add(
            subdivisions=2, radius=r * scale,
            location=(x + ox * scale, y + oy * scale, z + oz * scale),
        )
        lf = bpy.context.active_object
        lf.name = f"{name}_Crown_{idx}"
        lf.data.materials.append(m_leaf)
        for p in lf.data.polygons:
            p.use_smooth = True
        _link(lf, col)
    return trunk


def apply_cinematic_mood(
    col_env,
    mood: str = "golden_day",
    sun_azimuth_deg: float = 132.0,
    exposure: float = 0.0,
    add_bloom: bool = True,
    add_mist: bool = True,
    clouds: bool = False,
    use_cycles: bool = False,
    cycles_samples: int = 36,
):
    """
    Configure Blender 5.3 World Sky, 3-Point Directional Sun+Bounce+HeroRim Rig,
    and 5.3 Compositor Aerial Mist + FOG_GLOW Bloom.
    moods: 'golden_day', 'normal_day', 'sunset_twist', 'scary_night', 'sad_overcast', 'real_outdoor'.
    use_cycles=True activates RTX GPU Cycles + OPTIX/OpenImageDenoise for deep natural GI & puddle reflections.
    """
    sc = bpy.context.scene
    if use_cycles:
        sc.render.engine = "CYCLES"
        try:
            prefs = bpy.context.preferences.addons["cycles"].preferences
            prefs.compute_device_type = "OPTIX"
            prefs.get_devices()
            for dev in prefs.devices:
                dev.use = True
            sc.cycles.device = "GPU"
        except Exception:
            try:
                prefs = bpy.context.preferences.addons["cycles"].preferences
                prefs.compute_device_type = "CUDA"
                prefs.get_devices()
                for dev in prefs.devices:
                    dev.use = True
                sc.cycles.device = "GPU"
            except Exception:
                sc.cycles.device = "CPU"
        sc.cycles.samples = cycles_samples
        sc.cycles.use_adaptive_sampling = True
        sc.cycles.use_denoising = True
    else:
        sc.render.engine = "BLENDER_EEVEE"
        if hasattr(sc, "eevee") and hasattr(sc.eevee, "use_raytracing"):
            sc.eevee.use_raytracing = True

    sc.view_settings.view_transform = "AgX"
    try:
        sc.view_settings.look = "AgX - Medium High Contrast" if mood != "sad_overcast" else "AgX - Base Contrast"
    except Exception:
        pass

    MOOD_CFG = {
        "golden_day":   {"elev": 22.0, "sun_e": 2.6, "sun_k": 4300.0, "fill_e": 11.0, "fill_col": (0.62, 0.80, 1.0), "rim_e": 34.0, "rim_col": (1.0, 0.78, 0.48), "sky_str": 0.14, "exp": -0.20, "mist_col": (0.85, 0.82, 0.76, 1.0), "mist_mix": 0.18},
        "normal_day":   {"elev": 36.0, "sun_e": 2.8, "sun_k": 5500.0, "fill_e": 13.0, "fill_col": (0.72, 0.86, 1.0), "rim_e": 28.0, "rim_col": (1.0, 0.92, 0.78), "sky_str": 0.16, "exp": -0.20, "mist_col": (0.76, 0.86, 0.96, 1.0), "mist_mix": 0.15},
        "real_outdoor": {"elev": 30.0, "sun_e": 3.4, "sun_k": 5400.0, "fill_e": 3.2,  "fill_col": (0.62, 0.78, 1.0), "rim_e": 18.0, "rim_col": (0.98, 0.92, 0.82), "sky_str": 0.22, "exp": -0.35, "mist_col": (0.74, 0.82, 0.90, 1.0), "mist_mix": 0.14},
        "sunset_twist": {"elev": 9.0,  "sun_e": 2.4, "sun_k": 3200.0, "fill_e": 9.0,  "fill_col": (0.48, 0.62, 0.95), "rim_e": 48.0, "rim_col": (1.0, 0.56, 0.26), "sky_str": 0.13, "exp": -0.05, "mist_col": (0.94, 0.68, 0.54, 1.0), "mist_mix": 0.24},
        "scary_night":  {"elev": 32.0, "sun_e": 0.7, "sun_k": 7800.0, "fill_e": 6.0,  "fill_col": (0.28, 0.42, 0.76), "rim_e": 36.0, "rim_col": (0.48, 0.74, 1.0), "sky_str": 0.24, "exp": -0.35, "mist_col": (0.06, 0.10, 0.20, 1.0), "mist_mix": 0.30},
        "sad_overcast": {"elev": 44.0, "sun_e": 1.1, "sun_k": 6800.0, "fill_e": 16.0, "fill_col": (0.74, 0.82, 0.94), "rim_e": 20.0, "rim_col": (0.78, 0.88, 1.0), "sky_str": 0.14, "exp": -0.25, "mist_col": (0.64, 0.70, 0.78, 1.0), "mist_mix": 0.22},
    }
    cfg = MOOD_CFG.get(mood, MOOD_CFG["golden_day"])
    sc.view_settings.exposure = cfg["exp"] + exposure

    # World sky setup
    w = bpy.data.worlds.new(f"World_{mood}")
    sc.world = w
    nt = w.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputWorld")
    bg = nt.nodes.new("ShaderNodeBackground")
    bg.inputs["Strength"].default_value = cfg["sky_str"]

    if mood == "scary_night":
        tc = nt.nodes.new("ShaderNodeTexCoord")
        sep = nt.nodes.new("ShaderNodeSeparateXYZ")
        nt.links.new(tc.outputs["Generated"], sep.inputs["Vector"])
        ramp = nt.nodes.new("ShaderNodeValToRGB")
        ramp.color_ramp.elements[0].position = 0.0
        ramp.color_ramp.elements[0].color = _hex_rgba("#1C2742")
        ramp.color_ramp.elements[1].position = 0.45
        ramp.color_ramp.elements[1].color = _hex_rgba("#040814")
        nt.links.new(sep.outputs["Z"], ramp.inputs["Fac"])
        nt.links.new(ramp.outputs["Color"], bg.inputs["Color"])
    else:
        sky = nt.nodes.new("ShaderNodeTexSky")
        sky.sky_type = "MULTIPLE_SCATTERING" if hasattr(sky, "sky_type") else "PREETHAM"
        if hasattr(sky, "sun_disc"):
            sky.sun_disc = False
        if hasattr(sky, "sun_elevation"):
            sky.sun_elevation = math.radians(cfg["elev"])
        if hasattr(sky, "sun_rotation"):
            sky.sun_rotation = math.radians(sun_azimuth_deg)
        if hasattr(sky, "air_density"):
            sky.air_density = 1.25 if mood == "golden_day" else 1.0
        if hasattr(sky, "dust_density"):
            sky.dust_density = 1.6 if mood in ("golden_day", "sunset_twist") else 1.0
        if clouds or mood == "real_outdoor":
            tc = nt.nodes.new("ShaderNodeTexCoord")
            mp = nt.nodes.new("ShaderNodeMapping")
            mp.inputs["Scale"].default_value = (1.6, 1.6, 4.5)
            nt.links.new(tc.outputs["Generated"], mp.inputs["Vector"])
            cn = nt.nodes.new("ShaderNodeTexNoise")
            cn.inputs["Scale"].default_value = 3.4
            cn.inputs["Detail"].default_value = 9.0
            cn.inputs["Roughness"].default_value = 0.62
            nt.links.new(mp.outputs["Vector"], cn.inputs["Vector"])
            cramp = nt.nodes.new("ShaderNodeValToRGB")
            cramp.color_ramp.elements[0].position = 0.50
            cramp.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
            cramp.color_ramp.elements[1].position = 0.74
            cramp.color_ramp.elements[1].color = (0.85, 0.85, 0.85, 1.0)
            nt.links.new(cn.outputs["Fac"], cramp.inputs["Fac"])
            mix_c = nt.nodes.new("ShaderNodeMix")
            mix_c.data_type = "RGBA"
            mix_c.inputs[7].default_value = (4.2, 4.3, 4.5, 1.0)
            nt.links.new(cramp.outputs["Color"], mix_c.inputs[0])
            nt.links.new(sky.outputs["Color"], mix_c.inputs[6])
            nt.links.new(mix_c.outputs[2], bg.inputs["Color"])
        else:
            nt.links.new(sky.outputs["Color"], bg.inputs["Color"])
    nt.links.new(bg.outputs["Background"], out.inputs["Surface"])

    # Sun Key Light (positioned at side/back azimuth so characters & buildings have rich shadow modeling)
    az_rad = math.radians(sun_azimuth_deg)
    el_rad = math.radians(cfg["elev"])
    sun_d = bpy.data.lights.new("KeySun", type="SUN")
    sun_d.energy = cfg["sun_e"]
    sun_d.use_temperature = True
    sun_d.temperature = cfg["sun_k"]
    sun_d.angle = math.radians(3.5 if mood != "sad_overcast" else 16.0)
    sun_o = bpy.data.objects.new("KeySun", sun_d)
    # Point from sky sun dir toward origin
    sun_dir = Vector((math.sin(az_rad) * math.cos(el_rad), math.cos(az_rad) * math.cos(el_rad), math.sin(el_rad)))
    sun_o.rotation_euler = (-sun_dir).to_track_quat("-Z", "Y").to_euler()
    col_env.objects.link(sun_o)

    # Cool Opposite Sky Bounce Fill (moderate, directional — keeps contrast alive!)
    fill_d = bpy.data.lights.new("SkyFill", type="AREA")
    fill_d.energy = cfg["fill_e"]
    fill_d.size = 7.5
    fill_d.color = cfg["fill_col"]
    fill_o = bpy.data.objects.new("SkyFill", fill_d)
    fill_o.location = (-3.5, -5.5, 3.6)
    fill_o.rotation_euler = (Vector((0.0, 1.0, 1.0)) - fill_o.location).to_track_quat("-Z", "Y").to_euler()
    col_env.objects.link(fill_o)

    # Hero Warm Rim Backlight separating character hair & shoulders from mid/back buildings
    rim_d = bpy.data.lights.new("HeroRim", type="AREA")
    rim_d.energy = cfg["rim_e"]
    rim_d.size = 4.5
    rim_d.color = cfg["rim_col"]
    rim_o = bpy.data.objects.new("HeroRim", rim_d)
    rim_o.location = (2.8, 3.8, 3.4)
    rim_o.rotation_euler = (Vector((0.0, 0.8, 1.1)) - rim_o.location).to_track_quat("-Z", "Y").to_euler()
    col_env.objects.link(rim_o)

    # Blender 5.3 Compositor: Aerial Mist Depth Haze + Subtle FOG_GLOW Bloom
    if add_bloom or add_mist:
        if add_mist:
            sc.view_layers[0].use_pass_mist = True
            w.mist_settings.start = 10.0
            w.mist_settings.depth = 38.0
            w.mist_settings.falloff = "QUADRATIC"
        ng = bpy.data.node_groups.new("SvenComp", "CompositorNodeTree")
        sc.compositing_node_group = ng
        ng.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
        rl = ng.nodes.new("CompositorNodeRLayers")
        out_c = ng.nodes.new("NodeGroupOutput")
        cur_out = rl.outputs["Image"]

        if add_mist and "Mist" in rl.outputs:
            m_mul = ng.nodes.new("ShaderNodeMath")
            m_mul.operation = "MULTIPLY"
            m_mul.inputs[1].default_value = cfg["mist_mix"]
            ng.links.new(rl.outputs["Mist"], m_mul.inputs[0])
            mix_m = ng.nodes.new("ShaderNodeMix")
            mix_m.data_type = "RGBA"
            mix_m.inputs[7].default_value = cfg["mist_col"]
            ng.links.new(m_mul.outputs["Value"], mix_m.inputs[0])
            ng.links.new(cur_out, mix_m.inputs[6])
            cur_out = mix_m.outputs[2]

        if add_bloom:
            gl = ng.nodes.new("CompositorNodeGlare")
            _set_socket(gl, "Type", "Fog Glow")
            _set_socket(gl, "Quality", "High")
            _set_socket(gl, "Threshold", 1.15)
            _set_socket(gl, "Strength", 0.22)
            _set_socket(gl, "Size", 0.60)
            ng.links.new(cur_out, gl.inputs["Image"])
            cur_out = gl.outputs["Image"]

        ng.links.new(cur_out, out_c.inputs[0])


def build_suburban_street_set(col_env, mood: str = "golden_day", make_wet_road_fn=None):
    """
    Build a complete 3-Depth-Plane Roblox neighborhood corridor (Foreground, Midground Hero Stage,
    and Opposite/Flanking Background Skyline) so EVERY camera angle (WS, OTS, CU) sees tactile architectural depth.
    Returns list of solid collision obstacle objects for audit_scene_collisions.
    """
    obstacles = []
    is_night = (mood == "scary_night")
    w_glow = 4.2 if is_night else (2.4 if mood in ("golden_day", "sunset_twist") else 1.2)

    # 1. Ground Terrain: Wet PBR Asphalt Road + Lane Stripes + Concrete Slab Sidewalks + Beveled Curbs + Lawn Yards
    if make_wet_road_fn is not None:
        m_road = make_wet_road_fn("SuburbRoad_PBR", "#171C24", "#2E3644", scale=4.5, bump_strength=0.18)
    else:
        m_road = make_paving_mat("SuburbRoad_Fallback", "#262D38", "#181D25")
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=36, y_subdivisions=14, size=1.0, location=(0, -2.5, 0.015))
    road = bpy.context.active_object
    road.name = "Road_Asphalt"
    road.scale = (96.0, 5.4, 1.0)
    road.data.materials.append(m_road)
    _link(road, col_env)

    # Crisp painted dashed yellow road centerlines
    m_stripe = make_solid_mat("RoadYellow", "#E6B232", 0.45)
    for sx in range(-36, 38, 3):
        _add_box(f"RoadStripe_{sx}", (sx, -2.5, 0.02), (1.35, 0.14, 0.01), m_stripe, col_env, bevel_m=0.0)

    m_slab = make_paving_mat("SidewalkSlabs", "#B8C0CB", "#99A2B0")
    m_curb = make_paving_mat("GraniteCurb", "#969EAD", "#7F8796")
    m_grass = make_foliage_mat("SuburbGrass", "#3A743B", "#529647")

    # Hero Sidewalk (y = -0.3 .. +2.4) + Raised Curbstone + Lawn behind fence
    _add_box("Sidewalk_Hero", (0, 1.05, 0.04), (96, 2.75, 0.08), m_slab, col_env, bevel_m=0.008)
    _add_box("Curb_Hero", (0, -0.35, 0.055), (96, 0.20, 0.11), m_curb, col_env, bevel_m=0.014)
    _add_box("Lawn_Hero", (0, 9.0, 0.03), (96, 14.0, 0.06), m_grass, col_env, bevel_m=0.0)

    # Opposite Sidewalk + Lawn (y = -5.2 .. -14.0) — fills pull-outs & reverse angles cleanly!
    _add_box("Sidewalk_Opp", (0, -6.4, 0.04), (96, 2.6, 0.08), m_slab, col_env, bevel_m=0.008)
    _add_box("Curb_Opp", (0, -5.15, 0.055), (96, 0.20, 0.11), m_curb, col_env, bevel_m=0.014)
    _add_box("Lawn_Opp", (0, -12.0, 0.03), (96, 10.0, 0.06), m_grass, col_env, bevel_m=0.0)
    # Rolling distant backdrop trees & cul-de-sac bend (avoid flat box walls blocking road ends!)
    _add_box("HorizonRidge_N", (0, 28.0, 1.4), (110, 10.0, 3.6), m_grass, col_env, bevel_m=1.2)
    build_stylized_tree("Tree_EndR1", (24.0, 0.2, 0.06), 1.65, col_env, "#2F6638", "#488946")
    build_stylized_tree("Tree_EndR2", (26.5, -3.5, 0.06), 1.50, col_env, "#336B3B", "#4F9149")
    build_stylized_tree("Tree_EndL1", (-24.0, 0.2, 0.06), 1.65, col_env, "#2F6638", "#488946")
    build_stylized_tree("Tree_EndL2", (-26.5, -3.5, 0.06), 1.50, col_env, "#336B3B", "#4F9149")

    # 2. White Picket Fence separating sidewalk & front yards (y = 2.50)
    obstacles.append(build_picket_fence("Fence_Left", -14.0, -1.2, 2.52, 0.08, col_env))
    obstacles.append(build_picket_fence("Fence_Right", 1.2, 14.0, 2.52, 0.08, col_env))

    # 3. Hero Houses (Midground Action Stage) + Flanking Neighboring Houses (stops empty void on OTS cuts!)
    obstacles.append(build_hero_house("House_Coral", (-4.2, 5.8, 0.06), 4.9, 3.9, 3.4, "#DE7561", "#AF4F40", "#4D2C28", "#F4F1E8", "#2E4756", col_env, w_glow, with_porch=True))
    obstacles.append(build_hero_house("House_Amber", (3.2, 5.8, 0.06), 4.9, 3.9, 3.4, "#E9B954", "#C29232", "#3A4960", "#F4F1E8", "#6B3028", col_env, w_glow, with_porch=True))
    obstacles.append(build_hero_house("House_SageFlankR", (10.6, 5.6, 0.06), 4.8, 3.8, 3.2, "#7BA086", "#587C64", "#363A45", "#F4F1E8", "#3B4252", col_env, w_glow, with_porch=False))
    obstacles.append(build_hero_house("House_SkyFlankL", (-11.6, 5.6, 0.06), 4.8, 3.8, 3.2, "#6E8EAD", "#4D6C8A", "#383B48", "#F4F1E8", "#2B3240", col_env, w_glow, with_porch=False))

    # 4. Streetlamps, Trees, Shrubs & Props (Midground + Distant Skyline + Foreground framing!)
    lamp_e = 65.0 if is_night else 24.0
    obstacles.append(build_streetlamp("Lamp_Left", (-3.2, -0.05, 0.08), col_env, lamp_energy=lamp_e, face_road=-1.0))
    obstacles.append(build_streetlamp("Lamp_Right", (4.8, -0.05, 0.08), col_env, lamp_energy=lamp_e, face_road=-1.0))

    m_red = make_solid_mat("HydrantRed", "#D4382C", 0.35)
    m_mail = make_solid_mat("MailBlue", "#2E5B9A", 0.42)
    m_wood = make_solid_mat("PostWood", "#6A4832", 0.72)
    # Detailed Hydrant (body, top dome, silver nozzles) & Mailbox
    m_silv = make_solid_mat("HydrantSilver", "#C8CFD8", 0.25, metallic=0.85)
    obstacles.append(_add_box("FireHydrant", (-1.55, 0.02, 0.34), (0.24, 0.24, 0.50), m_red, col_env, bevel_m=0.03))
    _add_box("HydrantCap", (-1.55, 0.02, 0.61), (0.28, 0.28, 0.08), m_red, col_env, bevel_m=0.02)
    _add_box("HydrantDome", (-1.55, 0.02, 0.67), (0.14, 0.14, 0.06), m_silv, col_env, bevel_m=0.02)
    _add_box("HydrantNoz", (-1.55, 0.02, 0.44), (0.34, 0.10, 0.10), m_silv, col_env, bevel_m=0.01)
    obstacles.append(_add_box("MailboxPost", (1.65, 2.25, 0.48), (0.12, 0.12, 0.80), m_wood, col_env, bevel_m=0.01))
    _add_box("MailboxBox", (1.65, 2.22, 0.94), (0.24, 0.40, 0.24), m_mail, col_env, bevel_m=0.02)

    # Midground & Flanking Trees (seen behind characters in OTS shots!)
    tree_specs = [
        ("Tree_MidC",  (-0.5, 4.6, 0.06), 1.05, "#3C7D42", "#5AA44E"),
        ("Tree_Right", (6.8, 3.8, 0.06), 1.15, "#34723D", "#539B4B"),
        ("Tree_Left",  (-7.6, 3.9, 0.06), 1.10, "#417E3C", "#65AA4E"),
        ("Tree_Far1",  (9.2, 8.8, 0.06), 1.45, "#2F6638", "#488946"),
        ("Tree_Far2",  (-9.4, 8.8, 0.06), 1.40, "#336B3B", "#4F9149"),
        ("Tree_DownR", (14.8, 2.6, 0.06), 1.30, "#35733C", "#549E4D"),
        ("Tree_DownL", (-14.8, 2.6, 0.06), 1.30, "#35733C", "#549E4D"),
        ("Tree_Opp1",  (-5.5, -8.5, 0.06), 1.20, "#38723F", "#569A4C"),
        ("Tree_Opp2",  (5.5, -8.5, 0.06), 1.20, "#38723F", "#569A4C"),
    ]
    for tn, tloc, tsc, lc1, lc2 in tree_specs:
        obstacles.append(build_stylized_tree(tn, tloc, tsc, col_env, lc1, lc2))

    # Stylized low garden hedges hugging picket fences cleanly
    m_hedge = make_foliage_mat("HedgeMat", "#2E6934", "#468C44")
    for hx, hw in [(-5.8, 2.2), (-2.2, 1.5), (2.4, 1.8), (6.0, 2.4)]:
        _add_box(f"Hedge_{hx:.1f}", (hx, 2.95, 0.34), (hw, 0.65, 0.56), m_hedge, col_env, bevel_m=0.08)

    return obstacles


def build_mountain_horizon(col_env, peak_y: float = 38.0):
    """Add displaced real-world rocky/snow mountain ridges on the distant horizon."""
    m_mtn = make_weathered_stone_mat("MountainRock", "#666C68", "#2B302E", scale=0.45)
    m_snow = make_weathered_stone_mat("MountainSnow", "#E8EEF2", "#9AA6B2", scale=1.2)
    specs = [
        ("Mtn_Center", (0.0, peak_y + 12.0, -0.2), 42.0, 22.0, 14.5),
        ("Mtn_Left", (-26.0, peak_y + 6.0, -0.2), 34.0, 20.0, 11.0),
        ("Mtn_Right", (28.0, peak_y + 8.0, -0.2), 36.0, 22.0, 12.5),
    ]
    for name, loc, w, d, h in specs:
        mesh = bpy.data.meshes.new(name + "_M")
        bm = bmesh.new()
        bmesh.ops.create_icosphere(bm, subdivisions=4, radius=0.5)
        for v in bm.verts:
            # Flatten base, sharpen ridge crest with pseudo-noise
            n = 0.82 + 0.24 * math.sin(v.co.x * 9.0 + v.co.y * 7.0) * math.cos(v.co.z * 8.0)
            v.co.x *= w * n
            v.co.y *= d * n
            v.co.z = max(0.0, (v.co.z + 0.15) * h * 1.45 * n)
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        bm.to_mesh(mesh)
        bm.free()
        o = bpy.data.objects.new(name, mesh)
        o.location = loc
        o.data.materials.append(m_mtn)
        for p in o.data.polygons:
            p.use_smooth = True
        _link(o, col_env)
        # Snow cap peak
        cap = bpy.data.objects.new(name + "_Cap", mesh.copy())
        cap.location = (loc[0], loc[1], loc[2] + h * 0.62)
        cap.scale = (0.34, 0.34, 0.40)
        cap.data.materials.clear()
        cap.data.materials.append(m_snow)
        _link(cap, col_env)


def build_real_world_village_set(col_env, ground_mode: str = "mud_puddles"):
    """
    Gritty Real-World Cinematic PBR Set (inspired by Cycles/Blender PBR outdoors):
    Displaced wet mud puddles or gritty wet asphalt, weathered stone & stucco houses with dark reflective
    daytime windows, weathered grey wood picket fences, rocky distant mountain backdrop & lush realistic foliage.
    """
    obstacles = []
    if ground_mode == "mud_puddles":
        m_ground = make_wet_mud_puddle_mat("RealMudGround", "#3D2B1D", "#1A120C")
    else:
        m_ground = make_wet_mud_puddle_mat("RealWetEarth", "#2B2C2E", "#131518")

    bpy.ops.mesh.primitive_grid_add(x_subdivisions=96, y_subdivisions=72, size=1.0, location=(0.0, 2.0, 0.0))
    gnd = bpy.context.active_object
    gnd.name = "Real_Terrain_Ground"
    gnd.scale = (64.0, 56.0, 1.0)
    # Subtle micro-relief displacement in world Z so puddles form real shallow reflections
    bpy.context.view_layer.objects.active = gnd
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    for v in gnd.data.vertices:
        dist_center = math.hypot(v.co.x, v.co.y)
        wave = 0.045 * math.sin(v.co.x * 1.45) * math.cos(v.co.y * 1.35) + 0.025 * math.sin(v.co.x * 3.7 - v.co.y * 2.9)
        # Keep hero foreground feet zone near z = 0.00..0.04
        v.co.z = wave * min(1.0, 0.45 + 0.1 * dist_center)
    gnd.data.update()
    for p in gnd.data.polygons:
        p.use_smooth = True
    gnd.data.materials.append(m_ground)
    _link(gnd, col_env)

    # Weathered dark wood fence line (real wood grain, spaced unevenly like rustic village)
    m_wood = make_weathered_wood_mat("RealFenceWood", "#4E463E", "#24201C")
    for x in [i * 0.42 for i in range(-18, 19) if abs(i * 0.42) > 0.7]:
        h_var = 0.92 + 0.10 * math.sin(x * 3.7)
        tilt = 2.0 * math.sin(x * 5.1)
        _add_box(f"RFence_{x:.2f}", (x, 2.35, h_var * 0.5), (0.14, 0.06, h_var), m_wood, col_env, bevel_m=0.006, rot_deg=(0, tilt, 0))
    _add_box("RFence_RailTop", (-4.2, 2.31, 0.72), (7.0, 0.06, 0.07), m_wood, col_env, bevel_m=0.005)
    _add_box("RFence_RailTopR", (4.2, 2.31, 0.72), (7.0, 0.06, 0.07), m_wood, col_env, bevel_m=0.005)

    # Weathered stone & stucco village cottages with dark reflective daytime glass (no artificial daytime glow!)
    m_stone = make_weathered_stone_mat("VillageStone", "#3B3734", "#181615", scale=2.8)
    m_stucco = make_weathered_stone_mat("VillageStucco", "#CFCAC0", "#7D776D", scale=1.8)
    m_tile_r = make_cladding_mat("TileRoofRed", "#A83B24", "#5C1E12", row_freq=11.0, brick_offset=0.5, mortar=0.04, roughness=0.62)
    m_tile_t = make_cladding_mat("TileRoofTeal", "#2C5E58", "#16332F", row_freq=11.0, brick_offset=0.5, mortar=0.04, roughness=0.62)
    m_glass = make_dark_window_glass_mat("VillageDarkGlass")
    m_shut_r = make_weathered_wood_mat("ShutterRed", "#9E2E20", "#4A150E")
    m_shut_t = make_weathered_wood_mat("ShutterTeal", "#246B65", "#113633")
    m_trim = make_weathered_wood_mat("DarkBeamWood", "#3A2C22", "#1B140F")

    def build_cottage(cname, cx, cy, wall_m, roof_m, shut_m):
        c_body = _add_box(f"{cname}_Body", (cx, cy, 1.65), (4.6, 3.8, 3.3), wall_m, col_env, bevel_m=0.02)
        _add_gable_roof(f"{cname}_Roof", (cx, cy, 3.30), 5.2, 4.3, 1.85, roof_m, col_env)
        for wx in (cx - 1.15, cx + 1.15):
            fy = cy - 1.91
            _add_box(f"{cname}_WinFrm_{wx:.1f}", (wx, fy, 1.55), (0.98, 0.08, 1.12), m_trim, col_env, bevel_m=0.008)
            _add_box(f"{cname}_WinGls_{wx:.1f}", (wx, fy - 0.042, 1.55), (0.84, 0.03, 0.96), m_glass, col_env, bevel_m=0.0)
            _add_box(f"{cname}_MulV_{wx:.1f}", (wx, fy - 0.056, 1.55), (0.045, 0.025, 0.96), m_trim, col_env, bevel_m=0.0)
            _add_box(f"{cname}_MulH_{wx:.1f}", (wx, fy - 0.056, 1.55), (0.84, 0.025, 0.045), m_trim, col_env, bevel_m=0.0)
            for sgn in (-1, 1):
                _add_box(f"{cname}_Shut_{wx:.1f}_{sgn}", (wx + sgn * 0.65, fy - 0.02, 1.55), (0.28, 0.06, 1.05), shut_m, col_env, bevel_m=0.006)
        obstacles.append(c_body)

    build_cottage("Cottage_Stone", -3.8, 5.2, m_stone, m_tile_t, m_shut_r)
    build_cottage("Cottage_Stucco", 2.4, 5.2, m_stucco, m_tile_r, m_shut_t)

    # Distant mountain ridge backdrop + horizon treeline
    build_mountain_horizon(col_env, peak_y=36.0)
    for tx, ty, sc_t in [(-8.5, 9.5, 1.3), (8.2, 10.5, 1.4), (-14.0, 18.0, 1.8), (15.0, 20.0, 1.9)]:
        obstacles.append(build_stylized_tree(f"VTree_{tx:.0f}", (tx, ty, 0.0), sc_t, col_env, "#2B562E", "#41773C"))

    return obstacles

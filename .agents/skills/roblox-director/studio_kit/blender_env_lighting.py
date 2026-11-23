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


def make_wet_mud_puddle_mat(name: str = "WetMudPuddles", mud_hex: str = "#3E2816", wet_hex: str = "#1A1008"):
    """
    Studio-grade wet earth/mud ground shader:
    - Blends sunken Z-height basins + macro noise into mirror-reflective water puddles (Roughness 0.025, Coat 0.78)
    - Raised mud ridges receive chunky wet-clay specular coat + multi-scale normal bump.
    """
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = 0.78
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.75
        bsdf.inputs["Coat Roughness"].default_value = 0.03

    tc = nt.nodes.new("ShaderNodeTexCoord")
    noise_macro = nt.nodes.new("ShaderNodeTexNoise")
    noise_macro.inputs["Scale"].default_value = 1.6
    noise_macro.inputs["Detail"].default_value = 6.0
    nt.links.new(tc.outputs["Object"], noise_macro.inputs["Vector"])

    noise_micro = nt.nodes.new("ShaderNodeTexNoise")
    noise_micro.inputs["Scale"].default_value = 12.0
    noise_micro.inputs["Detail"].default_value = 9.0
    nt.links.new(tc.outputs["Object"], noise_micro.inputs["Vector"])

    col_ramp = nt.nodes.new("ShaderNodeValToRGB")
    col_ramp.color_ramp.elements[0].position = 0.36
    col_ramp.color_ramp.elements[0].color = _hex_rgba(wet_hex)
    col_ramp.color_ramp.elements[1].position = 0.68
    col_ramp.color_ramp.elements[1].color = _hex_rgba(mud_hex)
    nt.links.new(noise_macro.outputs["Fac"], col_ramp.inputs["Fac"])

    rough_ramp = nt.nodes.new("ShaderNodeValToRGB")
    rough_ramp.color_ramp.elements[0].position = 0.42
    rough_ramp.color_ramp.elements[0].color = (0.025, 0.025, 0.025, 1.0)
    rough_ramp.color_ramp.elements[1].position = 0.58
    rough_ramp.color_ramp.elements[1].color = (0.32, 0.32, 0.32, 1.0)
    nt.links.new(noise_macro.outputs["Fac"], rough_ramp.inputs["Fac"])

    # Flat mirror normals on wet puddles, bumpy micro-grit on raised mud ridges
    mul_bump = nt.nodes.new("ShaderNodeMath")
    mul_bump.operation = "MULTIPLY"
    nt.links.new(noise_micro.outputs["Fac"], mul_bump.inputs[0])
    nt.links.new(rough_ramp.outputs["Color"], mul_bump.inputs[1])

    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.48
    bump.inputs["Distance"].default_value = 0.032
    nt.links.new(mul_bump.outputs["Value"], bump.inputs["Height"])

    nt.links.new(col_ramp.outputs["Color"], bsdf.inputs["Base Color"])
    nt.links.new(rough_ramp.outputs["Color"], bsdf.inputs["Roughness"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_snow_ice_ground_mat(
    name: str = "SnowIceGround",
    snow_hex: str = "#DCE7F5",
    ice_hex: str = "#5D8BB8",
    ice_threshold: float = 0.42,
):
    """Backward-compatible alias delegating to Law R-WORLD `make_photoreal_snow_ice_mat` (PolyHaven snow_02 PBR + raytraced ice)."""
    return make_photoreal_snow_ice_mat(name=name)


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
        active_backend = "CPU"
        try:
            prefs = bpy.context.preferences.addons["cycles"].preferences
            for backend in ("OPTIX", "CUDA"):
                try:
                    prefs.compute_device_type = backend
                    prefs.get_devices()
                    gpu_devs = [d for d in prefs.devices if d.type != "CPU"]
                    if gpu_devs:
                        for dev in prefs.devices:
                            dev.use = (dev.type != "CPU")
                        active_backend = backend
                        break
                except Exception:
                    continue
            sc.cycles.device = "GPU" if active_backend != "CPU" else "CPU"
        except Exception:
            sc.cycles.device = "CPU"
        sc.cycles.samples = cycles_samples
        sc.cycles.use_adaptive_sampling = True
        sc.cycles.adaptive_threshold = 0.04
        sc.render.use_persistent_data = True
        sc.cycles.use_denoising = True
        try:
            has_nvoptix = (os.name == "nt") or os.path.exists("/usr/share/nvidia/nvoptix.bin")
            if active_backend == "OPTIX" and has_nvoptix:
                sc.cycles.denoiser = "OPTIX"
            else:
                sc.cycles.denoiser = "OPENIMAGEDENOISE"
                if hasattr(sc.cycles, "denoising_prefilter"):
                    sc.cycles.denoising_prefilter = "FAST"
                if hasattr(sc.cycles, "denoising_use_gpu"):
                    sc.cycles.denoising_use_gpu = (active_backend != "CPU" and has_nvoptix)
        except Exception:
            pass
    else:
        sc.render.engine = "BLENDER_EEVEE"
        sc.render.use_persistent_data = True
        if hasattr(sc, "eevee"):
            if hasattr(sc.eevee, "use_raytracing"):
                sc.eevee.use_raytracing = True
            if hasattr(sc.eevee, "use_gtao"):
                sc.eevee.use_gtao = True
            if hasattr(sc.eevee, "gtao_distance"):
                sc.eevee.gtao_distance = 0.55
            if hasattr(sc.eevee, "use_shadows"):
                sc.eevee.use_shadows = True

    sc.view_settings.view_transform = "AgX"
    try:
        sc.view_settings.look = "AgX - Medium High Contrast" if mood != "sad_overcast" else "AgX - Base Contrast"
    except Exception:
        pass

    MOOD_CFG = {
        "golden_day":   {"elev": 22.0, "sun_e": 2.6, "sun_k": 4300.0, "fill_e": 11.0, "fill_col": (0.62, 0.80, 1.0), "rim_e": 34.0, "rim_col": (1.0, 0.78, 0.48), "sky_str": 0.14, "exp": -0.20, "mist_col": (0.85, 0.82, 0.76, 1.0), "mist_mix": 0.18},
        "normal_day":   {"elev": 36.0, "sun_e": 2.8, "sun_k": 5500.0, "fill_e": 13.0, "fill_col": (0.72, 0.86, 1.0), "rim_e": 28.0, "rim_col": (1.0, 0.92, 0.78), "sky_str": 0.16, "exp": -0.20, "mist_col": (0.76, 0.86, 0.96, 1.0), "mist_mix": 0.15},
        "winter_snow":  {"elev": 24.0, "sun_e": 2.1, "sun_k": 6400.0, "fill_e": 9.0,  "fill_col": (0.64, 0.80, 1.0), "rim_e": 30.0, "rim_col": (0.76, 0.90, 1.0), "sky_str": 0.14, "exp": -0.28, "mist_col": (0.68, 0.80, 0.94, 1.0), "mist_mix": 0.24},
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


def setup_hero_light_linking(
    cast_collections: list,
    target_loc=(0.0, 0.0, 1.15),
    key_side: float = 1.0,
    key_energy: float = 34.0,
    rim_energy: float = 68.0,
    key_color=(1.0, 0.96, 0.90),
    rim_color=(0.74, 0.90, 1.0),
    practical_loc=None,
    practical_color=(1.0, 0.64, 0.24),
    practical_energy: float = 55.0,
    col_lights=None,
):
    """
    Blender 5.3 Light-Linked Character Hero Rig:
    - Hero_Key_LL (40 deg off camera axis, +30 deg elevation): carves smooth 3D shadow modeling on blocky faces & bevels
      WITHOUT blowing out bright snow or background walls.
    - Hero_Rim_LL (142 deg contrasting-temp backlight): paints a crisp rim halo separating shoulders, puffer & hair from dark cabins/snow.
    - Optional real Warm Practical PointLight (e.g. village lantern) casting warm orange bounce onto earmuffs & jacket.
    """
    sc = bpy.context.scene
    if col_lights is None:
        col_lights = bpy.data.collections.get("HeroLights") or bpy.data.collections.new("HeroLights")
        if col_lights.name not in sc.collection.children:
            sc.collection.children.link(col_lights)

    # Create a dedicated Light-Linking Receiver collection containing all cast collections (not linked to scene tree)
    ll_col = bpy.data.collections.get("_LL_HeroCast") or bpy.data.collections.new("_LL_HeroCast")
    for c in list(ll_col.children):
        ll_col.children.unlink(c)
    for o in list(ll_col.objects):
        ll_col.objects.unlink(o)
    for item in (cast_collections or []):
        if isinstance(item, bpy.types.Collection):
            if item.name not in ll_col.children:
                ll_col.children.link(item)
        elif isinstance(item, bpy.types.Object):
            if item.name not in ll_col.objects:
                ll_col.objects.link(item)

    tgt = Vector(target_loc)
    created = {}

    def _make_ll_area(name, loc, energy, color, size_x, size_y, spread_deg=85.0):
        ld = bpy.data.lights.new(name, type="AREA")
        ld.shape = "RECTANGLE"
        ld.size = size_x
        ld.size_y = size_y
        ld.energy = energy
        ld.color = color
        if hasattr(ld, "spread"):
            ld.spread = math.radians(spread_deg)
        lo = bpy.data.objects.new(name, ld)
        lo.location = Vector(loc)
        lo.rotation_euler = (tgt - lo.location).to_track_quat("-Z", "Y").to_euler()
        col_lights.objects.link(lo)
        if hasattr(lo, "light_linking") and (len(ll_col.children) > 0 or len(ll_col.objects) > 0):
            lo.light_linking.receiver_collection = ll_col
        return lo

    # Key at ~40 deg azimuth from front (-Y), elevated +30 deg
    key_pos = tgt + Vector((key_side * 1.95, -2.35, 1.45))
    created["key"] = _make_ll_area("Hero_Key_LL", key_pos, key_energy, key_color, 1.8, 1.6, spread_deg=78.0)

    # Rim on opposite rear flank (~142 deg) for crisp shoulder/hair separation
    rim_pos = tgt + Vector((-key_side * 1.65, 2.05, 1.35))
    created["rim"] = _make_ll_area("Hero_Rim_LL", rim_pos, rim_energy, rim_color, 1.4, 1.2, spread_deg=65.0)

    # Optional real practical light (lantern/window bounce — illuminates BOTH character & nearby props naturally)
    if practical_loc is not None:
        pd = bpy.data.lights.new("Practical_WarmBounce", type="POINT")
        pd.energy = practical_energy
        pd.color = practical_color
        pd.shadow_soft_size = 0.22
        po = bpy.data.objects.new("Practical_WarmBounce", pd)
        po.location = Vector(practical_loc)
        col_lights.objects.link(po)
        created["practical"] = po

    return created


def build_snowy_pine_tree(name: str, loc=(0.0, 6.0, 0.0), scale: float = 1.0, col=None):
    """Backward-compatible alias delegating to Law R-WORLD `build_organic_snow_pine` (5-tier jagged snow-laden boughs)."""
    return build_organic_snow_pine(col or bpy.context.scene.collection, name=name, loc=loc, scale=scale)


def build_hanging_lantern(col, post_loc=(-1.35, 1.15, 0.0), glow_hex="#FFB84D", glow_strength: float = 11.0):
    """Build a timber lantern post with emissive warm glass and return its exact practical PointLight coordinates."""
    px, py, pz = post_loc
    m_wood = make_weathered_wood_mat("LanternPostWood", "#4B3526", "#221710")
    m_iron = make_solid_mat("LanternIron", "#1F232A", roughness=0.40, metallic=0.80)
    m_glow = make_emissive_mat("LanternWarmGlass", glow_hex, strength=glow_strength)

    _add_box("LanternPost", (px, py, pz + 1.35), (0.14, 0.14, 2.70), m_wood, col, bevel_m=0.01)
    _add_box("LanternArm", (px + 0.36, py - 0.10, pz + 2.48), (0.86, 0.11, 0.11), m_wood, col, bevel_m=0.01)
    _add_box("LanternBrace", (px + 0.18, py - 0.06, pz + 2.26), (0.42, 0.08, 0.08), m_wood, col, bevel_m=0.008, rot_deg=(0, -45, 0))
    lx, ly, lz = px + 0.68, py - 0.18, pz + 2.08
    _add_box("LanternChain", (lx, ly, lz + 0.24), (0.03, 0.03, 0.32), m_iron, col, bevel_m=0.004)
    _add_box("LanternCap", (lx, ly, lz + 0.13), (0.26, 0.26, 0.06), m_iron, col, bevel_m=0.01)
    _add_box("LanternGlass", (lx, ly, lz), (0.19, 0.19, 0.22), m_glow, col, bevel_m=0.01)
    _add_box("LanternBase", (lx, ly, lz - 0.13), (0.24, 0.24, 0.05), m_iron, col, bevel_m=0.01)
    return Vector((lx, ly - 0.08, lz - 0.05))


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
    sub = gnd.modifiers.new("Subsurf", "SUBSURF")
    sub.levels = 1
    sub.render_levels = 2
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


# ==============================================================================
# POLYHAVEN CC0 1K INSTANCED ASSET, PBR TEXTURE & HDRI ENGINE
# ==============================================================================
import os
_PH_CACHE = {}


def get_polyhaven_dir() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(here, "..", "assets", "polyhaven"))


def _optimize_ph_material_for_eevee(mat):
    """Configures PolyHaven glTF materials for fast EEVEE Next rendering (DITHERED alpha, no overdraw)."""
    if not mat:
        return
    if hasattr(mat, "surface_render_method"):
        # DITHERED (Hashed) avoids expensive per-pixel alpha sorting lag on leaves/ferns/grass
        if getattr(mat, "surface_render_method", "") == "BLENDED":
            mat.surface_render_method = "DITHERED"
    if hasattr(mat, "blend_method"):
        if getattr(mat, "blend_method", "") == "BLEND":
            mat.blend_method = "HASHED"


def load_polyhaven_template(asset_id: str) -> list:
    """
    Imports a PolyHaven 1K glTF model ONCE into a hidden '_PH_Templates' collection
    and returns its list of mesh objects for zero-overhead VRAM instancing.
    """
    if asset_id in _PH_CACHE:
        valid = [o for o in _PH_CACHE[asset_id] if o and o.name in bpy.data.objects]
        if valid:
            return valid

    ph_dir = get_polyhaven_dir()
    gltf_path = os.path.join(ph_dir, "models", asset_id, f"{asset_id}_1k.gltf")
    if not os.path.exists(gltf_path):
        raise FileNotFoundError(f"PolyHaven glTF not found: {gltf_path}. Run tools/fetch_polyhaven_assets.py first.")

    sc = bpy.context.scene
    tpl_col = bpy.data.collections.get("_PH_Templates")
    if tpl_col is None:
        tpl_col = bpy.data.collections.new("_PH_Templates")
        sc.collection.children.link(tpl_col)
        tpl_col.hide_render = True
        tpl_col.hide_viewport = True

    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=gltf_path)
    imported = [o for o in bpy.data.objects if o not in before]

    mesh_objs = []
    for o in imported:
        if o.type == "MESH" and len(o.data.vertices) > 0:
            # Bake world matrix rotation/scale into a single unique template mesh data block
            # and shift vertices so local origin (0, 0, 0) is at bottom-center (cx, cy, z_min).
            o.data = o.data.copy()
            mat_w = o.matrix_world.copy()
            # Keep only rotation & scale from glTF node transform, then recenter bounding box
            rot_scale = mat_w.to_3x3().to_4x4()
            o.data.transform(rot_scale)
            xs = [v.co.x for v in o.data.vertices]
            ys = [v.co.y for v in o.data.vertices]
            zs = [v.co.z for v in o.data.vertices]
            cx = 0.5 * (min(xs) + max(xs))
            cy = 0.5 * (min(ys) + max(ys))
            zmin = min(zs)
            for v in o.data.vertices:
                v.co.x -= cx
                v.co.y -= cy
                v.co.z -= zmin
            o.data.update()
            o.parent = None
            o.location = (0.0, 0.0, 0.0)
            o.rotation_euler = (0.0, 0.0, 0.0)
            o.scale = (1.0, 1.0, 1.0)
            for slot in o.material_slots:
                _optimize_ph_material_for_eevee(slot.material)
            mesh_objs.append(o)
        for c in list(o.users_collection):
            c.objects.unlink(o)
        tpl_col.objects.link(o)

    mesh_objs.sort(key=lambda x: x.name)
    _PH_CACHE[asset_id] = mesh_objs
    return mesh_objs


def spawn_polyhaven_model(
    col_env,
    asset_id: str,
    location=(0.0, 0.0, 0.0),
    rotation_deg=(0.0, 0.0, 0.0),
    scale=1.0,
    child_index=None,
    name_prefix=None,
):
    """
    Spawns a lightweight linked-mesh instance (sharing ob.data on GPU VRAM) of a PolyHaven 1K model.
    If the model contains multiple distinct meshes (e.g. rock_moss_set_01), child_index selects one
    piece and centers it at `location`; otherwise all pieces are parented under a root Empty.
    """
    templates = load_polyhaven_template(asset_id)
    if not templates:
        return None

    sc_vec = (scale, scale, scale) if isinstance(scale, (int, float)) else tuple(scale)
    rot_rad = tuple(math.radians(a) for a in rotation_deg)
    prefix = name_prefix or f"PH_{asset_id}"

    if child_index is not None or len(templates) == 1:
        src = templates[child_index % len(templates)] if child_index is not None else templates[0]
        inst = bpy.data.objects.new(prefix, src.data)
        inst.location = location
        inst.rotation_euler = rot_rad
        inst.scale = sc_vec
        col_env.objects.link(inst)
        return inst

    root = bpy.data.objects.new(prefix, None)
    root.location = location
    root.rotation_euler = rot_rad
    root.scale = sc_vec
    col_env.objects.link(root)

    for idx, src in enumerate(templates):
        inst = bpy.data.objects.new(f"{prefix}_{idx}", src.data)
        inst.location = src.location.copy()
        inst.rotation_euler = src.rotation_euler.copy()
        inst.scale = src.scale.copy()
        inst.parent = root
        col_env.objects.link(inst)
    return root


def make_polyhaven_pbr_mat(
    name: str,
    tex_id: str,
    uv_scale=(12.0, 12.0),
    coat_weight: float = 0.0,
    coat_rough: float = 0.05,
    normal_strength: float = 1.0,
    use_object_coords: bool = True,
):
    """Builds a Blender 5.3 Principled BSDF material wired to PolyHaven 1K Diffuse, Roughness & Normal GL maps."""
    ph_dir = get_polyhaven_dir()
    tdir = os.path.join(ph_dir, "textures", tex_id)

    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()

    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])

    for sname, sval in (("Coat Weight", coat_weight), ("Coat Roughness", coat_rough)):
        sock = bsdf.inputs.get(sname)
        if sock is not None:
            sock.default_value = sval

    tc = nt.nodes.new("ShaderNodeTexCoord")
    mp = nt.nodes.new("ShaderNodeMapping")
    if use_object_coords:
        # Object coordinates are in meters, so scale = 1 / tile_meters (e.g. 0.45 repeats every ~2.2m)
        sx = uv_scale[0] if uv_scale[0] < 3.0 else (uv_scale[0] / 48.0)
        sy = uv_scale[1] if uv_scale[1] < 3.0 else (uv_scale[1] / 48.0)
        mp.inputs["Scale"].default_value = (sx, sy, sx)
        nt.links.new(tc.outputs["Object"], mp.inputs["Vector"])
    else:
        mp.inputs["Scale"].default_value = (uv_scale[0], uv_scale[1], 1.0)
        nt.links.new(tc.outputs["UV"], mp.inputs["Vector"])

    def _find_tex(kind):
        for ext in ("jpg", "png"):
            p = os.path.join(tdir, f"{tex_id}_{kind}_1k.{ext}")
            if os.path.exists(p):
                return p
        return None

    diff_p = _find_tex("diff")
    if diff_p:
        tex_d = nt.nodes.new("ShaderNodeTexImage")
        tex_d.image = bpy.data.images.load(diff_p, check_existing=True)
        nt.links.new(mp.outputs["Vector"], tex_d.inputs["Vector"])
        nt.links.new(tex_d.outputs["Color"], bsdf.inputs["Base Color"])

    rough_p = _find_tex("rough")
    if rough_p:
        tex_r = nt.nodes.new("ShaderNodeTexImage")
        tex_r.image = bpy.data.images.load(rough_p, check_existing=True)
        tex_r.image.colorspace_settings.name = "Non-Color"
        nt.links.new(mp.outputs["Vector"], tex_r.inputs["Vector"])
        nt.links.new(tex_r.outputs["Color"], bsdf.inputs["Roughness"])

    nor_p = _find_tex("nor_gl")
    if nor_p:
        tex_n = nt.nodes.new("ShaderNodeTexImage")
        tex_n.image = bpy.data.images.load(nor_p, check_existing=True)
        tex_n.image.colorspace_settings.name = "Non-Color"
        nt.links.new(mp.outputs["Vector"], tex_n.inputs["Vector"])
        n_map = nt.nodes.new("ShaderNodeNormalMap")
        n_map.inputs["Strength"].default_value = normal_strength
        nt.links.new(tex_n.outputs["Color"], n_map.inputs["Color"])
        nt.links.new(n_map.outputs["Normal"], bsdf.inputs["Normal"])

    return m


def apply_polyhaven_hdri(
    hdri_id: str = "kloofendal_48d_partly_cloudy_puresky",
    strength: float = 0.65,
    rot_z_deg: float = 0.0,
):
    """Wires a cached PolyHaven 2K HDRI pure-sky environment map into the active Blender World."""
    ph_dir = get_polyhaven_dir()
    hdr_path = os.path.join(ph_dir, "hdris", f"{hdri_id}_2k.hdr")
    if not os.path.exists(hdr_path):
        return False

    sc = bpy.context.scene
    if sc.world is None:
        sc.world = bpy.data.worlds.new("PolyHavenWorld")
    w = sc.world
    w.use_nodes = True
    nt = w.node_tree
    nt.nodes.clear()

    out = nt.nodes.new("ShaderNodeOutputWorld")
    bg = nt.nodes.new("ShaderNodeBackground")
    bg.inputs["Strength"].default_value = strength
    nt.links.new(bg.outputs["Background"], out.inputs["Surface"])

    env_tex = nt.nodes.new("ShaderNodeTexEnvironment")
    env_tex.image = bpy.data.images.load(hdr_path, check_existing=True)
    nt.links.new(env_tex.outputs["Color"], bg.inputs["Color"])

    tc = nt.nodes.new("ShaderNodeTexCoord")
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Rotation"].default_value = (0.0, 0.0, math.radians(rot_z_deg))
    nt.links.new(tc.outputs["Generated"], mp.inputs["Vector"])
    nt.links.new(mp.outputs["Vector"], env_tex.inputs["Vector"])
    return True


_CORE_GLB_CACHE = {}


def load_core_glb_template(rel_path: str) -> list:
    """
    Imports a .glb file from .agents/skills/roblox-director/assets/<rel_path> ONCE into
    '_PH_Templates' with bottom-centered geometry (z_min=0) for zero-overhead VRAM instancing.
    """
    key = rel_path.replace("\\", "/")
    if key in _CORE_GLB_CACHE:
        valid = [o for o in _CORE_GLB_CACHE[key] if o and o.name in bpy.data.objects]
        if valid:
            return valid

    here = os.path.dirname(os.path.abspath(__file__))
    glb_path = os.path.normpath(os.path.join(here, "..", "assets", rel_path))
    if not os.path.exists(glb_path):
        raise FileNotFoundError(f"Core GLB asset not found: {glb_path}")

    sc = bpy.context.scene
    tpl_col = bpy.data.collections.get("_PH_Templates")
    if tpl_col is None:
        tpl_col = bpy.data.collections.new("_PH_Templates")
        sc.collection.children.link(tpl_col)
        tpl_col.hide_render = True
        tpl_col.hide_viewport = True

    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=glb_path)
    imported = [o for o in bpy.data.objects if o not in before]

    mesh_objs = [o for o in imported if o.type == "MESH" and len(o.data.vertices) > 0]
    for o in imported:
        for c in list(o.users_collection):
            c.objects.unlink(o)
        tpl_col.objects.link(o)

    if mesh_objs:
        # Compute combined world bounding box across all mesh parts of the GLB
        all_w = []
        for o in mesh_objs:
            mw = o.matrix_world.copy()
            o.data = o.data.copy()
            o.data.transform(mw)
            o.parent = None
            o.location = (0.0, 0.0, 0.0)
            o.rotation_euler = (0.0, 0.0, 0.0)
            o.scale = (1.0, 1.0, 1.0)
            for v in o.data.vertices:
                all_w.append(v.co.copy())
        cx = 0.5 * (min(v.x for v in all_w) + max(v.x for v in all_w))
        cy = 0.5 * (min(v.y for v in all_w) + max(v.y for v in all_w))
        zmin = min(v.z for v in all_w)
        for o in mesh_objs:
            for v in o.data.vertices:
                v.co.x -= cx
                v.co.y -= cy
                v.co.z -= zmin
            o.data.update()
            for slot in o.material_slots:
                _optimize_ph_material_for_eevee(slot.material)

    _CORE_GLB_CACHE[key] = mesh_objs
    return mesh_objs


def spawn_core_glb_asset(
    col_env,
    rel_path: str,
    location=(0.0, 0.0, 0.0),
    rotation_deg=(0.0, 0.0, 0.0),
    scale=1.0,
    name_prefix=None,
    target_height_m: float = None,
):
    """
    Spawns a lightweight VRAM-instanced copy of any .glb asset in assets/<rel_path>.
    Law R-COLLIDE Layer 1: Pass `target_height_m` (meters) to auto-normalize stud-scale or
    unpredictably sized GLB assets so houses/trees/props never invade the character acting stage!
    """
    templates = load_core_glb_template(rel_path)
    if not templates:
        return None
    if target_height_m is not None and target_height_m > 0.01:
        z_max = max(v.co.z for o in templates for v in o.data.vertices)
        if z_max > 1e-4:
            norm_s = float(target_height_m) / float(z_max)
            scale = norm_s if isinstance(scale, (int, float)) else tuple(s * norm_s for s in scale)
    sc_vec = (scale, scale, scale) if isinstance(scale, (int, float)) else tuple(scale)
    rot_rad = tuple(math.radians(a) for a in rotation_deg)
    stem = os.path.splitext(os.path.basename(rel_path))[0]
    prefix = name_prefix or f"Asset_{stem}"

    if len(templates) == 1:
        inst = bpy.data.objects.new(prefix, templates[0].data)
        inst.location = location
        inst.rotation_euler = rot_rad
        inst.scale = sc_vec
        col_env.objects.link(inst)
        return inst

    root = bpy.data.objects.new(prefix, None)
    root.location = location
    root.rotation_euler = rot_rad
    root.scale = sc_vec
    col_env.objects.link(root)
    for idx, src in enumerate(templates):
        inst = bpy.data.objects.new(f"{prefix}_{idx}", src.data)
        inst.parent = root
        col_env.objects.link(inst)
    return root


def compute_stage_footprints(col_env=None, ground_names=("ground", "terrain", "floor", "road", "sidewalk", "lawn", "snow", "ice", "pond", "mud", "asphalt")) -> list:
    """Return 2D/3D world bounding footprints for every static environment mesh to plan zero-clipping staging."""
    dg = bpy.context.evaluated_depsgraph_get()
    g_low = tuple(g.lower() for g in ground_names)
    objs = list(col_env.all_objects) if col_env else list(bpy.context.scene.objects)
    out = []
    for o in objs:
        if o.type != "MESH" or o.hide_render:
            continue
        if any(tok in o.name.lower() for tok in g_low):
            continue
        ev = o.evaluated_get(dg)
        if not ev.data or len(ev.bound_box) < 8:
            continue
        pts = [ev.matrix_world @ Vector(c) for c in ev.bound_box]
        xs, ys, zs = [p.x for p in pts], [p.y for p in pts], [p.z for p in pts]
        out.append({"name": o.name, "x0": round(min(xs), 3), "x1": round(max(xs), 3), "y0": round(min(ys), 3), "y1": round(max(ys), 3), "z0": round(min(zs), 3), "z1": round(max(zs), 3)})
    return out


# ==============================================================================
# LAW R-WORLD — 5-VECTOR AI-CORE ENVIRONMENT ARCHITECTURE FOR BLENDER 5.3
# Translates the Sven AI Video Core [context]: 5-Vector Blueprint + 6-Point
# Physical Lighting Contract + 2x2 Location Grid directly into Blender 3D Sets.
# ==============================================================================

def make_photoreal_snow_ice_mat(
    name: str = "PhotorealSnowIce",
    ice_center=(2.15, -1.10),
    ice_radius: float = 1.55,
    snow_tile: float = 0.35,
):
    """
    Vector 1 & 2 Ground Shader:
    Blends real PolyHaven 1K photoscanned `snow_02` PBR (Diffuse + Roughness + Normal)
    seamlessly into an organically perturbed raytraced frozen ice pond (Roughness 0.028, Coat 0.92)
    so there is ZERO hard disc edge and 100% natural micro-sparkle + mirror reflections.
    """
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = 0.65
    if "Coat Roughness" in bsdf.inputs:
        bsdf.inputs["Coat Roughness"].default_value = 0.028
    if "Sheen Roughness" in bsdf.inputs:
        bsdf.inputs["Sheen Roughness"].default_value = 0.42
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])

    tc = nt.nodes.new("ShaderNodeTexCoord")
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Scale"].default_value = (snow_tile, snow_tile, snow_tile)
    nt.links.new(tc.outputs["Object"], mp.inputs["Vector"])

    # Load cached PolyHaven snow_02 1K maps if present
    ph_dir = os.path.join(get_polyhaven_dir(), "textures", "snow_02")
    def _ph_img(kind, non_color=False):
        for ext in ("jpg", "png"):
            p = os.path.join(ph_dir, f"snow_02_{kind}_1k.{ext}")
            if os.path.exists(p):
                t = nt.nodes.new("ShaderNodeTexImage")
                t.image = bpy.data.images.load(p, check_existing=True)
                if non_color:
                    t.image.colorspace_settings.name = "Non-Color"
                nt.links.new(mp.outputs["Vector"], t.inputs["Vector"])
                return t
        return None

    tex_d = _ph_img("diff", False)
    tex_r = _ph_img("rough", True)
    tex_n = _ph_img("nor_gl", True)

    # Organic distance mask from ice_center + macro noise perturbation (0 = mirror ice, 1 = crisp snow)
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(tc.outputs["Object"], sep.inputs["Vector"])
    dx = nt.nodes.new("ShaderNodeMath"); dx.operation = "SUBTRACT"; dx.inputs[1].default_value = ice_center[0]
    dy = nt.nodes.new("ShaderNodeMath"); dy.operation = "SUBTRACT"; dy.inputs[1].default_value = ice_center[1]
    nt.links.new(sep.outputs["X"], dx.inputs[0]); nt.links.new(sep.outputs["Y"], dy.inputs[0])
    dx2 = nt.nodes.new("ShaderNodeMath"); dx2.operation = "MULTIPLY"; nt.links.new(dx.outputs["Value"], dx2.inputs[0]); nt.links.new(dx.outputs["Value"], dx2.inputs[1])
    dy2 = nt.nodes.new("ShaderNodeMath"); dy2.operation = "MULTIPLY"; nt.links.new(dy.outputs["Value"], dy2.inputs[0]); nt.links.new(dy.outputs["Value"], dy2.inputs[1])
    sum2 = nt.nodes.new("ShaderNodeMath"); sum2.operation = "ADD"; nt.links.new(dx2.outputs["Value"], sum2.inputs[0]); nt.links.new(dy2.outputs["Value"], sum2.inputs[1])
    dist = nt.nodes.new("ShaderNodeMath"); dist.operation = "SQRT"; nt.links.new(sum2.outputs["Value"], dist.inputs[0])

    n_edge = nt.nodes.new("ShaderNodeTexNoise")
    n_edge.inputs["Scale"].default_value = 1.35
    n_edge.inputs["Detail"].default_value = 6.0
    nt.links.new(tc.outputs["Object"], n_edge.inputs["Vector"])
    n_pert = nt.nodes.new("ShaderNodeMath"); n_pert.operation = "MULTIPLY"; n_pert.inputs[1].default_value = 0.62
    nt.links.new(n_edge.outputs["Fac"], n_pert.inputs[0])
    d_pert = nt.nodes.new("ShaderNodeMath"); d_pert.operation = "ADD"
    nt.links.new(dist.outputs["Value"], d_pert.inputs[0]); nt.links.new(n_pert.outputs["Value"], d_pert.inputs[1])

    mask = nt.nodes.new("ShaderNodeMapRange")
    mask.clamp = True
    mask.inputs["From Min"].default_value = ice_radius - 0.14
    mask.inputs["From Max"].default_value = ice_radius + 0.24
    mask.inputs["To Min"].default_value = 0.0
    mask.inputs["To Max"].default_value = 1.0
    nt.links.new(d_pert.outputs["Value"], mask.inputs["Value"])

    # Color: cool translucent alpine ice vs crisp photoscanned snow_02 (tinted gently cool-blue)
    col_snow = nt.nodes.new("ShaderNodeMix")
    col_snow.data_type = "RGBA"
    col_snow.blend_type = "MULTIPLY"
    col_snow.inputs[0].default_value = 0.35
    col_snow.inputs[7].default_value = _hex_rgba("#CFE0F5")
    if tex_d:
        nt.links.new(tex_d.outputs["Color"], col_snow.inputs[6])
    else:
        col_snow.inputs[6].default_value = _hex_rgba("#E4ECF7")

    col_final = nt.nodes.new("ShaderNodeMix")
    col_final.data_type = "RGBA"
    col_final.inputs[6].default_value = _hex_rgba("#386590")
    nt.links.new(mask.outputs["Result"], col_final.inputs[0])
    nt.links.new(col_snow.outputs[2], col_final.inputs[7])
    nt.links.new(col_final.outputs[2], bsdf.inputs["Base Color"])

    # Roughness: mirror ice (0.028) vs photoscanned snow roughness
    r_final = nt.nodes.new("ShaderNodeMix")
    r_final.data_type = "FLOAT"
    r_final.inputs[2].default_value = 0.028
    if tex_r:
        nt.links.new(tex_r.outputs["Color"], r_final.inputs[3])
    else:
        r_final.inputs[3].default_value = 0.72
    nt.links.new(mask.outputs["Result"], r_final.inputs[0])
    nt.links.new(r_final.outputs[0], bsdf.inputs["Roughness"])

    if "Coat Weight" in bsdf.inputs:
        c_mix = nt.nodes.new("ShaderNodeMix"); c_mix.data_type = "FLOAT"
        c_mix.inputs[2].default_value = 0.92; c_mix.inputs[3].default_value = 0.10
        nt.links.new(mask.outputs["Result"], c_mix.inputs[0])
        nt.links.new(c_mix.outputs[0], bsdf.inputs["Coat Weight"])

    if "Sheen Weight" in bsdf.inputs:
        s_mix = nt.nodes.new("ShaderNodeMix"); s_mix.data_type = "FLOAT"
        s_mix.inputs[2].default_value = 0.0; s_mix.inputs[3].default_value = 0.38
        nt.links.new(mask.outputs["Result"], s_mix.inputs[0])
        nt.links.new(s_mix.outputs[0], bsdf.inputs["Sheen Weight"])

    if tex_n:
        n_map = nt.nodes.new("ShaderNodeNormalMap")
        nt.links.new(tex_n.outputs["Color"], n_map.inputs["Color"])
        # Smooth mirror normals on ice, crisp photoscanned normal relief on snow
        nt.links.new(mask.outputs["Result"], n_map.inputs["Strength"])
        nt.links.new(n_map.outputs["Normal"], bsdf.inputs["Normal"])

    return mat


def build_organic_snow_pine(col, name: str, loc=(0.0, 6.0, 0.0), scale: float = 1.0, seed: int = 1):
    """
    Vector 2 Background Foliage: 5-tier organically perturbed snow-laden alpine pine tree
    with PolyHaven `bark_brown_02` trunk + jagged snow-draped evergreen boughs (zero smooth cones).
    """
    x, y, z = loc
    m_trunk = make_polyhaven_pbr_mat("PineBarkPH", "bark_brown_02", uv_scale=(1.4, 1.4), normal_strength=0.8) if os.path.isdir(os.path.join(get_polyhaven_dir(), "textures", "bark_brown_02")) else make_weathered_wood_mat("PineTrunkWood", "#4A3222", "#26180F")
    m_pine = make_foliage_mat("AlpinePineDark", "#1D3F32", "#2F5C48")
    m_snow = make_polyhaven_pbr_mat("PineSnowPH", "snow_02", uv_scale=(0.9, 0.9), normal_strength=0.5) if os.path.isdir(os.path.join(get_polyhaven_dir(), "textures", "snow_02")) else make_solid_mat("PineSnowCap", "#DDE9F7", roughness=0.76)

    bpy.ops.mesh.primitive_cylinder_add(vertices=10, radius=0.14 * scale, depth=1.25 * scale, location=(x, y, z + 0.62 * scale))
    tr = bpy.context.active_object
    tr.name = f"{name}_Trunk"
    tr.data.materials.append(m_trunk)
    _link(tr, col)

    tiers = [
        (1.38, 1.28, 1.25),
        (2.08, 1.06, 1.18),
        (2.74, 0.84, 1.10),
        (3.32, 0.60, 0.98),
        (3.84, 0.36, 0.80),
    ]
    for idx, (tz, rad, h) in enumerate(tiers):
        # Build irregular radial bough mesh via bmesh instead of smooth cone
        for is_snow in (False, True):
            r_use = rad * (0.88 if is_snow else 1.0) * scale
            h_use = h * (0.58 if is_snow else 1.0) * scale
            z_use = z + (tz + (h * 0.22 if is_snow else 0.0)) * scale
            mesh = bpy.data.meshes.new(f"{name}_{'Snow' if is_snow else 'Bough'}_{idx}_M")
            bm = bmesh.new()
            bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=18, radius1=r_use, radius2=0.04 * scale, depth=h_use)
            for v in bm.verts:
                ang = math.atan2(v.co.y, v.co.x)
                r_xy = math.hypot(v.co.x, v.co.y)
                if r_xy > 0.05 * scale:
                    # 7 jagged organic pine bough lobes drooping slightly at tips
                    lobe = 1.0 + 0.22 * math.sin(ang * 7.0 + seed * 1.9 + idx * 1.3) + 0.09 * math.cos(ang * 13.0 - idx)
                    v.co.x *= lobe
                    v.co.y *= lobe
                    if v.co.z < 0.0:
                        v.co.z -= 0.14 * scale * max(0.0, lobe - 0.95)
            bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
            bm.to_mesh(mesh); bm.free()
            o = bpy.data.objects.new(f"{name}_{'Snow' if is_snow else 'Bough'}_{idx}", mesh)
            o.location = (x, y, z_use)
            o.data.materials.append(m_snow if is_snow else m_pine)
            for p in o.data.polygons: p.use_smooth = True
            _link(o, col)
    return tr


def build_cinematic_alpine_cabin(
    col,
    name: str,
    loc=(0.5, 6.0, 0.0),
    w: float = 4.4,
    d: float = 3.4,
    h: float = 2.9,
    wall_style: str = "chalet",
    warm_win: bool = True,
    add_smoke: bool = True,
):
    """
    Vector 2 & 3 Detailed Architecture (Zero Sterile Box!):
    Stone masonry plinth (PolyHaven rock_face_03), timber-framed plank walls, recessed glowing
    muntin windows with shutters & real warm amber outdoor light spill, thick snow-blanketed
    overhanging gable roof, brick chimney with 3D curling smoke, porch deck & stacked firewood.
    """
    cx, cy, cz = loc
    m_stone = make_polyhaven_pbr_mat("CabinStonePH", "rock_face_03", uv_scale=(0.8, 0.8), normal_strength=0.9) if os.path.isdir(os.path.join(get_polyhaven_dir(), "textures", "rock_face_03")) else make_weathered_stone_mat("CabinStone", "#5A5D62", "#282A2E")
    m_snow_roof = make_polyhaven_pbr_mat("RoofSnowPH", "snow_02", uv_scale=(0.55, 0.55), normal_strength=0.65) if os.path.isdir(os.path.join(get_polyhaven_dir(), "textures", "snow_02")) else make_solid_mat("SnowRoof", "#DDE8F6", roughness=0.72)
    m_trim = make_weathered_wood_mat("CabinTimberTrim", "#2B1E17", "#140D0A")
    m_bark = make_polyhaven_pbr_mat("FirewoodBarkPH", "bark_brown_02", uv_scale=(2.0, 2.0), normal_strength=0.8) if os.path.isdir(os.path.join(get_polyhaven_dir(), "textures", "bark_brown_02")) else m_trim

    if wall_style == "log":
        m_wall = make_cladding_mat(f"{name}_LogWall", "#573724", "#2B190F", row_freq=5.2, brick_offset=0.0, mortar=0.045, roughness=0.80)
        m_shut = make_weathered_wood_mat(f"{name}_Shut", "#3A2218", "#1A0F0A")
    else:
        m_wall = make_cladding_mat(f"{name}_ChaletWall", "#949C6E", "#646B47", row_freq=6.4, brick_offset=0.0, mortar=0.035, roughness=0.74)
        m_shut = make_weathered_wood_mat(f"{name}_Shut", "#3A4E58", "#1C282E")

    m_win = make_emissive_mat(f"{name}_WinGlow", "#FFC978", strength=4.2) if warm_win else make_dark_window_glass_mat(f"{name}_WinDark")

    # 1. Stone foundation plinth + main timber body
    plinth_h = 0.42
    _add_box(f"{name}_StonePlinth", (cx, cy, cz + plinth_h * 0.5), (w + 0.14, d + 0.14, plinth_h), m_stone, col, bevel_m=0.025)
    body = _add_box(f"{name}_Body", (cx, cy, cz + plinth_h + (h - plinth_h) * 0.5), (w, d, h - plinth_h), m_wall, col, bevel_m=0.02)

    # 2. Heavy overhanging timber roof + sculpted thick white snow-blanket overhang!
    _add_gable_roof(f"{name}_TimberRoof", (cx, cy, cz + h - 0.04), w + 0.86, d + 0.86, 1.55, m_trim, col)
    _add_gable_roof(f"{name}_SnowBlanket", (cx, cy, cz + h + 0.14), w + 0.94, d + 0.94, 1.58, m_snow_roof, col)

    # 3. Corner posts, fascia beams & front porch deck with snow-dusted railing
    fy = cy - d * 0.5 - 0.04
    for bx in (cx - w * 0.48, cx, cx + w * 0.48):
        _add_box(f"{name}_Post_{bx:.1f}", (bx, fy, cz + h * 0.5), (0.16, 0.14, h), m_trim, col, bevel_m=0.01)
    _add_box(f"{name}_BeamTop", (cx, fy, cz + h - 0.08), (w + 0.20, 0.16, 0.16), m_trim, col, bevel_m=0.01)
    _add_box(f"{name}_PorchDeck", (cx, fy - 0.38, cz + 0.18), (w + 0.10, 0.82, 0.34), m_trim, col, bevel_m=0.015)

    # 4. Recessed multi-pane glowing windows with sills, shutters & REAL warm outdoor light spill!
    for wx in (cx - w * 0.25, cx + w * 0.25):
        wz = cz + h * 0.56
        _add_box(f"{name}_WinFrame_{wx:.1f}", (wx, fy - 0.02, wz), (0.94, 0.08, 1.04), m_trim, col, bevel_m=0.01)
        _add_box(f"{name}_WinSill_{wx:.1f}", (wx, fy - 0.11, wz - 0.52), (1.06, 0.20, 0.08), m_trim, col, bevel_m=0.01)
        _add_box(f"{name}_WinSnow_{wx:.1f}", (wx, fy - 0.12, wz - 0.46), (0.98, 0.15, 0.06), m_snow_roof, col, bevel_m=0.015)
        _add_box(f"{name}_WinGlass_{wx:.1f}", (wx, fy - 0.075, wz), (0.78, 0.04, 0.88), m_win, col, bevel_m=0.0)
        _add_box(f"{name}_MulV_{wx:.1f}", (wx, fy - 0.105, wz), (0.045, 0.03, 0.88), m_trim, col, bevel_m=0.0)
        _add_box(f"{name}_MulH_{wx:.1f}", (wx, fy - 0.105, wz), (0.78, 0.03, 0.045), m_trim, col, bevel_m=0.0)
        for sgn in (-1, 1):
            _add_box(f"{name}_Shut_{wx:.1f}_{sgn}", (wx + sgn * 0.62, fy - 0.04, wz), (0.28, 0.06, 0.96), m_shut, col, bevel_m=0.008)
        if warm_win:
            ld = bpy.data.lights.new(f"{name}_WinSpill_{wx:.1f}", type="AREA")
            ld.size = 0.75; ld.energy = 28.0; ld.color = (1.0, 0.72, 0.34)
            lo = bpy.data.objects.new(f"{name}_WinSpill_{wx:.1f}", ld)
            lo.location = (wx, fy - 0.22, wz - 0.05)
            lo.rotation_euler = Euler((math.radians(72), 0.0, 0.0))
            col.objects.link(lo)

    # 5. Stacked firewood logs beside porch + Stone chimney with curling 3D smoke puffs!
    for r_i in range(2):
        for c_i in range(4 - r_i):
            lx = cx - w * 0.32 + (c_i + 0.5 * r_i) * 0.15
            lz = cz + 0.42 + r_i * 0.12
            bpy.ops.mesh.primitive_cylinder_add(vertices=8, radius=0.065, depth=0.46, location=(lx, fy - 0.26, lz), rotation=(math.radians(90), 0, math.radians(6 * (c_i - 1))))
            lg = bpy.context.active_object; lg.name = f"{name}_Log_{r_i}_{c_i}"
            lg.data.materials.append(m_bark); _link(lg, col)

    chim_x, chim_y = cx + w * 0.28, cy + 0.15
    _add_box(f"{name}_Chimney", (chim_x, chim_y, cz + h + 1.15), (0.62, 0.62, 1.55), m_stone, col, bevel_m=0.02)
    _add_box(f"{name}_ChimCap", (chim_x, chim_y, cz + h + 1.96), (0.76, 0.76, 0.12), m_snow_roof, col, bevel_m=0.02)

    if add_smoke:
        m_smk = bpy.data.materials.new(f"{name}_SmokeMat")
        bs = next(n for n in m_smk.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
        bs.inputs["Base Color"].default_value = _hex_rgba("#DCE4EE")
        bs.inputs["Roughness"].default_value = 0.95
        bs.inputs["Alpha"].default_value = 0.24
        if hasattr(m_smk, "surface_render_method"):
            m_smk.surface_render_method = "DITHERED"
        for k in range(5):
            r_p = 0.22 + k * 0.14
            bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=r_p, location=(chim_x + k * 0.22, chim_y + k * 0.14, cz + h + 2.25 + k * 0.52))
            sm = bpy.context.active_object; sm.name = f"{name}_Smoke_{k}"
            sm.data.materials.append(m_smk)
            for p in sm.data.polygons: p.use_smooth = True
            _link(sm, col)
    return body


def build_atmospheric_particles(
    col,
    kind: str = "snow",
    bounds=(-5.5, 5.5, -4.5, 8.5, 0.35, 4.4),
    count: int = 190,
    seed: int = 7,
):
    """
    Vector 4 Atmospheric Scattering Medium:
    Spawns lightweight 3D airborne snowflakes or dust motes across FG/MG/BG planes so shallow DOF
    turns near particles into cinematic bokeh and practical lanterns illuminate floating atmosphere.
    """
    import random
    rng = random.Random(seed)
    m_p = bpy.data.materials.new(f"Atmos_{kind}")
    bs = next(n for n in m_p.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    if kind == "snow":
        bs.inputs["Base Color"].default_value = (0.94, 0.97, 1.0, 1.0)
        bs.inputs["Roughness"].default_value = 0.35
        if "Emission Color" in bs.inputs:
            bs.inputs["Emission Color"].default_value = (0.82, 0.90, 1.0, 1.0)
            bs.inputs["Emission Strength"].default_value = 0.55
    else:
        bs.inputs["Base Color"].default_value = (1.0, 0.92, 0.72, 1.0)
        if "Emission Color" in bs.inputs:
            bs.inputs["Emission Color"].default_value = (1.0, 0.88, 0.62, 1.0)
            bs.inputs["Emission Strength"].default_value = 0.85

    x0, x1, y0, y1, z0, z1 = bounds
    bm = bmesh.new()
    for _ in range(count):
        px = rng.uniform(x0, x1)
        py = rng.uniform(y0, y1)
        pz = rng.uniform(z0, z1)
        rad = rng.uniform(0.008, 0.022) if kind == "snow" else rng.uniform(0.005, 0.012)
        res = bmesh.ops.create_icosphere(bm, subdivisions=1, radius=rad)
        for v in res["verts"]:
            v.co += Vector((px, py, pz))
    mesh = bpy.data.meshes.new(f"AtmosParticles_{kind}_M")
    bm.to_mesh(mesh); bm.free()
    obj = bpy.data.objects.new(f"AtmosParticles_{kind}", mesh)
    obj.data.materials.append(m_p)
    obj.visible_shadow = False if hasattr(obj, "visible_shadow") else None
    _link(obj, col)
    return obj


def build_5vector_winter_village(col_env, sun_azimuth_deg: float = 128.0, add_snow_particles: bool = True):
    """
    Master 5-Vector AI-Core Environment Builder (Winter Alpine Village):
    - Vector 1: PolyHaven 2K PureSky HDRI + low-angle winter sun + photoreal PolyHaven `snow_02` PBR ground
    - Vector 2: 3-plane set dressing (FG PolyHaven boulders/stumps/fence strictly outside acting corridor,
                MG 2 detailed snow-blanketed alpine cabins with warm window spill + porch bench + hanging lantern +
                organic raytraced ice pond, BG organic snow pines + PolyHaven `mountainside` alpine cliffs)
    - Vector 3: 6-Point Lighting Contract (low directional cross-sun + real glowing window/lantern pools)
    - Vector 4: 3D suspended snowfall + chimney smoke + quadratic cold Aerial Mist + AgX Fog Glow
    - Vector 5: Guaranteed clear actor safe corridor (x: -3.2..+3.2, y: -2.2..+2.0) for Law R-COLLIDE!
    Returns dict with `lantern_pos`, `bench_loc`, `ice_center`.
    """
    # Vector 1 & 3: Moody crisp winter sky + low directional cross-sun + HDRI ambient reflection
    apply_cinematic_mood(col_env, mood="winter_snow", sun_azimuth_deg=sun_azimuth_deg, exposure=0.06, add_bloom=True, add_mist=True)
    # Lower sun elevation to 16 deg for rich golden-cool diagonal snow shadows!
    sun_o = bpy.data.objects.get("KeySun")
    if sun_o and sun_o.data:
        sun_o.data.energy = 2.6
        sun_o.data.temperature = 5800.0
        az_r, el_r = math.radians(sun_azimuth_deg), math.radians(16.0)
        sd = Vector((math.sin(az_r) * math.cos(el_r), math.cos(az_r) * math.cos(el_r), math.sin(el_r)))
        sun_o.rotation_euler = (-sd).to_track_quat("-Z", "Y").to_euler()
    # Layer cached PolyHaven 2K PureSky HDRI for crisp natural sky reflections in ice & puffer jackets!
    apply_polyhaven_hdri("kloofendal_48d_partly_cloudy_puresky", strength=0.32, rot_z_deg=sun_azimuth_deg)

    # Vector 2 Ground: Subsurf-displaced snowdrifts + organic raytraced ice pond using PolyHaven `snow_02` PBR!
    # Origin locked at (0, 0, 0) so Object coords == World coords for exact ice_center placement!
    ice_center = (2.15, -1.05)
    m_ground = make_photoreal_snow_ice_mat("WinterSnowIce_PH", ice_center=ice_center, ice_radius=1.55)
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=110, y_subdivisions=96, size=1.0, location=(0.0, 0.0, 0.0))
    gnd = bpy.context.active_object
    gnd.name = "Winter_Terrain_Ground"
    gnd.scale = (72.0, 72.0, 1.0)
    bpy.context.view_layer.objects.active = gnd
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    for v in gnd.data.vertices:
        d_pond = math.hypot(v.co.x - ice_center[0], v.co.y - ice_center[1])
        # Keep flat mirror surface inside frozen ice pond & flat safe walking corridor near characters
        if d_pond < 1.75:
            v.co.z = 0.0
        elif -3.2 <= v.co.x <= 3.2 and -2.2 <= v.co.y <= 1.8:
            v.co.z = 0.015 * math.sin(v.co.x * 1.1) * math.cos(v.co.y * 1.1)
        else:
            # Soft rolling snowdrifts outside the acting corridor
            drift = 0.16 * math.sin(v.co.x * 0.42 + 0.5) * math.cos(v.co.y * 0.38) + 0.07 * math.sin(v.co.x * 1.3 - v.co.y * 1.1)
            dist_c = math.hypot(v.co.x * 0.4, (v.co.y - 0.5) * 0.5)
            v.co.z = max(-0.02, drift * min(1.0, max(0.0, (dist_c - 1.2) * 0.55)))
    gnd.data.update()
    for p in gnd.data.polygons: p.use_smooth = True
    gnd.data.materials.append(m_ground)
    sub = gnd.modifiers.new("Subsurf", "SUBSURF")
    sub.levels = 1; sub.render_levels = 2
    _link(gnd, col_env)

    # Midground Architecture (clearly behind y = 5.4 so acting corridor stays 100% collision-free!)
    build_cinematic_alpine_cabin(col_env, "Chalet_Hero", (0.45, 6.4, 0.0), w=4.4, d=3.4, h=2.9, wall_style="chalet", warm_win=True, add_smoke=True)
    build_cinematic_alpine_cabin(col_env, "Cabin_Grandma", (4.55, 5.8, 0.0), w=4.2, d=3.2, h=2.8, wall_style="log", warm_win=True, add_smoke=True)

    # Midground Storytelling Landmarks: Porch Bench + Hanging Warm Village Lantern + Rustic Timber Fence
    m_bench = make_weathered_wood_mat("PorchBenchWood", "#6B4E38", "#322217")
    _add_box("GrandpaBenchSeat", (-2.40, 0.35, 0.36), (1.45, 0.56, 0.08), m_bench, col_env, bevel_m=0.012)
    _add_box("GrandpaBenchLegL", (-2.96, 0.35, 0.17), (0.10, 0.46, 0.34), m_bench, col_env, bevel_m=0.008)
    _add_box("GrandpaBenchLegR", (-1.84, 0.35, 0.17), (0.10, 0.46, 0.34), m_bench, col_env, bevel_m=0.008)
    _add_box("GrandpaBenchBack", (-2.40, 0.62, 0.72), (1.45, 0.07, 0.42), m_bench, col_env, bevel_m=0.012, rot_deg=(-8, 0, 0))

    # Rustic weathered fence behind Grandpa & beside cabins (y = 3.1..3.5 — safely clear of cast!)
    for fx in (-5.4, -4.4, -3.4, -2.4, 5.8, 6.8):
        _add_box(f"SnowFencePost_{fx:.1f}", (fx, 3.25, 0.48), (0.11, 0.11, 0.96), m_bench, col_env, bevel_m=0.01, rot_deg=(0, 3 * math.sin(fx), 0))
    _add_box("SnowFenceRailL1", (-3.9, 3.22, 0.68), (3.2, 0.06, 0.08), m_bench, col_env, bevel_m=0.006)
    _add_box("SnowFenceRailL2", (-3.9, 3.22, 0.36), (3.2, 0.06, 0.08), m_bench, col_env, bevel_m=0.006)

    lantern_pos = build_hanging_lantern(col_env, post_loc=(-1.35, 1.35, 0.0), glow_hex="#FFB347", glow_strength=13.0)

    # Foreground & Mid-Flank Photoscanned PolyHaven 3D Scatter (strictly OUTSIDE acting safe zone!)
    ph_scatter = [
        ("boulder_01",   (-4.4, -1.6, -0.05), (0, 0, 24),  0.85, "FG_BoulderL"),
        ("rock_07",      ( 4.6, -1.9, -0.04), (0, 0, 118), 0.72, "FG_RockR"),
        ("tree_stump_01",(-4.1,  1.8, -0.02), (0, 0, 45),  0.90, "MG_StumpL"),
        ("stone_01",     ( 3.9, -0.3, -0.03), (0, 0, 72),  0.65, "MG_StoneR"),
        ("dry_branches_medium_01", (-3.7, -2.1, 0.02), (0, 0, 35), 0.95, "FG_BranchesL"),
    ]
    for aid, ploc, prot, psc, pnm in ph_scatter:
        if os.path.isdir(os.path.join(get_polyhaven_dir(), "models", aid)):
            spawn_polyhaven_model(col_env, aid, location=ploc, rotation_deg=prot, scale=psc, name_prefix=pnm)

    # Background Organic Snow-Laden Pine Forest (exact real-world meters!)
    pine_coords = [
        (-5.0, 4.4, 1.05, 1), (-3.5, 5.0, 1.20, 2), (-2.1, 5.8, 1.14, 3),
        (-6.2, 7.0, 1.35, 4), (-4.2, 8.2, 1.42, 5), (-2.3, 9.4, 1.46, 6),
        (-1.2, 10.2, 1.50, 7), (2.4, 10.4, 1.45, 8), (6.9, 5.4, 1.22, 9),
        (8.2, 8.8, 1.46, 10), (-8.0, 9.6, 1.52, 11),
        # Far alpine skyline treeline
        (-6.4, 14.8, 1.82, 12), (-1.8, 15.8, 1.92, 13), (3.2, 15.2, 1.86, 14), (7.6, 14.4, 1.78, 15),
        # 180-deg Reverse-Angle Backdrop Trees (y = -11..-15 so Reverse OTS / 2x2 Panel 2 NEVER faces an empty void!)
        (-5.5, -11.5, 1.35, 16), (-1.8, -12.8, 1.48, 17), (2.2, -12.2, 1.40, 18), (6.0, -11.2, 1.32, 19),
    ]
    for idx, (px, py, psc, sd) in enumerate(pine_coords):
        build_organic_snow_pine(col_env, f"OrgSnowPine_{idx}", (px, py, 0.0), scale=psc, seed=sd)

    # Photoscanned PolyHaven Mountainside Cliffs + Snowy Alpine Horizon Peaks!
    if os.path.isdir(os.path.join(get_polyhaven_dir(), "models", "mountainside")):
        spawn_polyhaven_model(col_env, "mountainside", location=(-12.0, 24.0, -0.5), rotation_deg=(0, 0, 12), scale=3.2, name_prefix="BG_MountainL")
        spawn_polyhaven_model(col_env, "mountainside", location=(14.0, 26.0, -0.5), rotation_deg=(0, 0, -28), scale=3.6, name_prefix="BG_MountainR")
    build_mountain_horizon(col_env, peak_y=32.0)

    # Vector 4: 3D Suspended Falling Snow Particles catching lantern & sun bokeh!
    if add_snow_particles:
        build_atmospheric_particles(col_env, kind="snow", bounds=(-5.5, 5.5, -4.5, 8.5, 0.35, 4.4), count=210, seed=7)

    return {"lantern_pos": lantern_pos, "bench_loc": (-2.40, 0.35, 0.0), "ice_center": ice_center}


def render_location_2x2_grid(out_path: str, focus_loc=(0.0, 0.5, 1.1), cast_collections: list = None):
    """
    Vector 5 Spatial Topology Audit (Mirrors Sven Core setting.html §4B 16:9 2x2 Location Reference Sheet):
    Temporarily hides characters (if passed) and renders 4 synchronized panels into a single 16:9 PNG
    using Blender's built-in numpy + bpy.data.images (zero external Pillow dependency):
    Top-Left: Wide Establishing | Top-Right: 180-deg Reverse | Bottom-Left: Bird's-Eye Layout | Bottom-Right: Landmark Detail.
    """
    import numpy as np
    sc = bpy.context.scene
    prev_cam = sc.camera
    prev_rx, prev_ry = sc.render.resolution_x, sc.render.resolution_y
    prev_fp = sc.render.filepath

    hidden = []
    for col in (cast_collections or []):
        if not col.hide_render:
            col.hide_render = True
            hidden.append(col)

    cd = bpy.data.cameras.new("_LocGridCam")
    co = bpy.data.objects.new("_LocGridCam", cd)
    sc.collection.objects.link(co)
    sc.camera = co
    pw, ph = 640, 360
    sc.render.resolution_x, sc.render.resolution_y = pw, ph

    fx, fy, fz = focus_loc
    views = [
        ("tl", (fx - 0.3, fy - 6.8, fz + 0.8), (fx, fy + 1.5, fz), 30.0),             # Wide Establishing
        ("tr", (fx + 1.2, fy + 3.6, fz + 0.7), (fx - 0.8, fy - 2.5, fz - 0.1), 32.0),  # 180 Reverse
        ("bl", (fx, fy - 2.5, 11.5), (fx, fy + 1.5, 0.0), 28.0),                       # Bird's-Eye Spatial Layout
        ("br", (fx - 0.2, fy - 3.4, fz + 0.4), (fx - 0.7, fy + 1.6, fz + 0.5), 42.0),  # Landmark Detail
    ]
    tmp_dir = os.path.dirname(os.path.abspath(out_path))
    os.makedirs(tmp_dir, exist_ok=True)
    panels = []
    try:
        for tag, cloc, ctgt, lens in views:
            co.location = Vector(cloc)
            co.rotation_euler = (Vector(ctgt) - co.location).to_track_quat("-Z", "Y").to_euler()
            cd.lens = lens
            cd.dof.use_dof = False
            p = os.path.join(tmp_dir, f"_locgrid_{tag}.png")
            sc.render.filepath = p
            bpy.ops.render.render(write_still=True)
            im = bpy.data.images.load(p, check_existing=False)
            arr = np.array(im.pixels[:], dtype=np.float32).reshape((ph, pw, 4))
            panels.append(arr)
            bpy.data.images.remove(im)

        # Blender image pixels are bottom-to-top: rows [ph:2*ph] = TOP row, [0:ph] = BOTTOM row
        grid = np.zeros((ph * 2, pw * 2, 4), dtype=np.float32)
        grid[ph:ph * 2, 0:pw, :] = panels[0]       # Top-Left (Wide)
        grid[ph:ph * 2, pw:pw * 2, :] = panels[1]  # Top-Right (180 Reverse)
        grid[0:ph, 0:pw, :] = panels[2]            # Bottom-Left (Bird's-Eye)
        grid[0:ph, pw:pw * 2, :] = panels[3]       # Bottom-Right (Landmark Detail)
        out_img = bpy.data.images.new("_LocGrid2x2", width=pw * 2, height=ph * 2, alpha=False)
        out_img.pixels.foreach_set(grid.ravel())
        out_img.filepath_raw = out_path
        out_img.file_format = "PNG"
        out_img.save()
        bpy.data.images.remove(out_img)
    finally:
        for col in hidden:
            col.hide_render = False
        sc.camera = prev_cam
        sc.render.resolution_x, sc.render.resolution_y = prev_rx, prev_ry
        sc.render.filepath = prev_fp
        bpy.data.objects.remove(co, do_unlink=True)
        bpy.data.cameras.remove(cd, do_unlink=True)
    return out_path




#!/usr/bin/env python3
"""
blender_animals_nature.py — Stylized Roblox Core Animals (Dog, Cat, Bunny, Duck, Bird)
and Everyday Nature (Sakura Tree, Flower Bush, Potted Monstera + Creator Store Oak/Pine) for Blender 5.3.
Provides both live animatable rigs (head/tail/legs/wings parented cleanly) and .glb export into Core assets/.
"""
import math
import os
import bpy
import bmesh
from mathutils import Euler, Matrix, Vector


def _srgb(hex_str: str):
    h = hex_str.lstrip("#")
    vals = [int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4)]
    return tuple(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in vals) + (1.0,)


def _mat(name: str, hex_str: str, rough: float = 0.45, metal: float = 0.0):
    key = f"AN_{name}_{hex_str}_{int(rough*100)}"
    if key in bpy.data.materials:
        return bpy.data.materials[key]
    m = bpy.data.materials.new(key)
    m.use_nodes = True
    bsdf = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = _srgb(hex_str)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metal
    return m


def _box_part(name: str, size, loc, col, mat, rot_deg=(0, 0, 0), bevel_frac=0.14, parent=None):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    if bevel_frac > 0:
        bmesh.ops.bevel(bm, geom=list(bm.edges), offset=min(size) * bevel_frac, segments=2, affect="EDGES")
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    for p in mesh.polygons:
        p.use_smooth = True
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    if parent:
        obj.parent = parent
    obj.location = Vector(loc)
    obj.rotation_euler = Euler([math.radians(a) for a in rot_deg])
    return obj


def _sphere_part(name: str, size, loc, col, mat, rot_deg=(0, 0, 0), parent=None):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=16, v_segments=12, radius=0.5)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    for p in mesh.polygons:
        p.use_smooth = True
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    if parent:
        obj.parent = parent
    obj.location = Vector(loc)
    obj.rotation_euler = Euler([math.radians(a) for a in rot_deg])
    return obj


def _cone_part(name: str, r1: float, r2: float, depth: float, loc, col, mat, rot_deg=(0, 0, 0), segs=12, parent=None):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=segs, radius1=r1, radius2=r2, depth=depth)
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    for p in mesh.polygons:
        p.use_smooth = True
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    if parent:
        obj.parent = parent
    obj.location = Vector(loc)
    obj.rotation_euler = Euler([math.radians(a) for a in rot_deg])
    return obj


def _add_eyes_and_nose(head, eye_y, eye_z, eye_sep, col, eye_hex="#181820", nose_hex="#22181C", eye_sz=0.055):
    m_eye = _mat("Eye", eye_hex, rough=0.08)
    m_hl = _mat("EyeHL", "#FFFFFF", rough=0.05)
    m_nose = _mat("Nose", nose_hex, rough=0.25)
    for sx in (-1, 1):
        _sphere_part(f"{head.name}_Eye_{sx}", (eye_sz, eye_sz * 0.65, eye_sz * 1.15), (sx * eye_sep, eye_y, eye_z), col, m_eye, parent=head)
        _sphere_part(f"{head.name}_HL_{sx}", (eye_sz * 0.36, eye_sz * 0.36, eye_sz * 0.36), (sx * eye_sep + sx * eye_sz * 0.14, eye_y - eye_sz * 0.24, eye_z + eye_sz * 0.22), col, m_hl, parent=head)
    _sphere_part(f"{head.name}_Nose", (eye_sz * 1.15, eye_sz * 0.85, eye_sz * 0.85), (0.0, eye_y - eye_sz * 0.65, eye_z - eye_sz * 1.1), col, m_nose, parent=head)


def build_pet_dog(name: str, col, location=(0, 0, 0), yaw_deg=0.0, coat_hex="#E5A254", belly_hex="#F7E5C8", collar_hex="#D93838"):
    """Cute Roblox-stylized Shiba/Golden dog facing -Y with animatable head & tail pivots."""
    root = bpy.data.objects.new(name, None)
    root.empty_display_size = 0.25
    col.objects.link(root)
    root.location = Vector(location)
    root.rotation_euler = Euler((0, 0, math.radians(yaw_deg)))

    m_coat = _mat("DogCoat", coat_hex, 0.55)
    m_belly = _mat("DogBelly", belly_hex, 0.58)
    m_col = _mat("Collar", collar_hex, 0.35)
    m_gold = _mat("Brass", "#F2C144", 0.22, metal=0.9)

    _box_part(f"{name}_Body", (0.28, 0.54, 0.25), (0.0, 0.02, 0.28), col, m_coat, bevel_frac=0.18, parent=root)
    _box_part(f"{name}_Chest", (0.23, 0.14, 0.22), (0.0, -0.22, 0.28), col, m_belly, bevel_frac=0.18, parent=root)
    _box_part(f"{name}_Collar", (0.26, 0.10, 0.24), (0.0, -0.21, 0.33), col, m_col, rot_deg=(18, 0, 0), bevel_frac=0.12, parent=root)
    _sphere_part(f"{name}_Tag", (0.06, 0.04, 0.06), (0.0, -0.27, 0.24), col, m_gold, parent=root)

    for sx in (-1, 1):
        for sy, lbl in ((-0.17, "F"), (0.20, "B")):
            _box_part(f"{name}_Leg_{lbl}{sx}", (0.09, 0.09, 0.22), (sx * 0.10, sy, 0.11), col, m_coat, bevel_frac=0.22, parent=root)
            _box_part(f"{name}_Paw_{lbl}{sx}", (0.095, 0.11, 0.045), (sx * 0.10, sy - 0.01, 0.022), col, m_belly, bevel_frac=0.2, parent=root)

    head_piv = bpy.data.objects.new(f"{name}_HeadPivot", None)
    col.objects.link(head_piv)
    head_piv.parent = root
    head_piv.location = (0.0, -0.24, 0.42)
    _box_part(f"{name}_Head", (0.31, 0.30, 0.28), (0.0, -0.05, 0.08), col, m_coat, bevel_frac=0.18, parent=head_piv)
    _box_part(f"{name}_Muzzle", (0.16, 0.15, 0.11), (0.0, -0.21, 0.02), col, m_belly, bevel_frac=0.2, parent=head_piv)
    for sx in (-1, 1):
        _cone_part(f"{name}_Ear_{sx}", 0.065, 0.012, 0.13, (sx * 0.11, -0.02, 0.26), col, m_coat, rot_deg=(8, -sx * 18, 0), segs=6, parent=head_piv)
    _add_eyes_and_nose(head_piv, -0.20, 0.11, 0.082, col, eye_sz=0.046)

    tail_piv = bpy.data.objects.new(f"{name}_TailPivot", None)
    col.objects.link(tail_piv)
    tail_piv.parent = root
    tail_piv.location = (0.0, 0.28, 0.36)
    _box_part(f"{name}_Tail", (0.075, 0.22, 0.075), (0.0, 0.09, 0.09), col, m_coat, rot_deg=(-48, 0, 0), bevel_frac=0.22, parent=tail_piv)
    return {"root": root, "head": head_piv, "tail": tail_piv}


def build_pet_cat(name: str, col, location=(0, 0, 0), yaw_deg=0.0, coat_hex="#EE8838", belly_hex="#FFF2DE", eye_hex="#33A854", collar_hex="#4682E0"):
    """Cute Roblox-stylized Cat (Tabby / Tuxedo) facing -Y with pointed pink ears, whiskers & curved tail."""
    root = bpy.data.objects.new(name, None)
    root.empty_display_size = 0.22
    col.objects.link(root)
    root.location = Vector(location)
    root.rotation_euler = Euler((0, 0, math.radians(yaw_deg)))

    m_coat = _mat("CatCoat", coat_hex, 0.50)
    m_belly = _mat("CatBelly", belly_hex, 0.55)
    m_pink = _mat("PinkEar", "#F7A6B6", 0.5)
    m_col = _mat("CatCollar", collar_hex, 0.32)

    _box_part(f"{name}_Body", (0.22, 0.44, 0.20), (0.0, 0.02, 0.23), col, m_coat, bevel_frac=0.2, parent=root)
    _box_part(f"{name}_Chest", (0.17, 0.10, 0.17), (0.0, -0.17, 0.23), col, m_belly, bevel_frac=0.2, parent=root)
    _box_part(f"{name}_Collar", (0.21, 0.08, 0.19), (0.0, -0.16, 0.28), col, m_col, rot_deg=(15, 0, 0), bevel_frac=0.14, parent=root)

    for sx in (-1, 1):
        for sy, lbl in ((-0.13, "F"), (0.17, "B")):
            _box_part(f"{name}_Leg_{lbl}{sx}", (0.07, 0.07, 0.17), (sx * 0.075, sy, 0.085), col, m_coat, bevel_frac=0.24, parent=root)
            _box_part(f"{name}_Paw_{lbl}{sx}", (0.075, 0.085, 0.035), (sx * 0.075, sy - 0.01, 0.018), col, m_belly, bevel_frac=0.2, parent=root)

    head_piv = bpy.data.objects.new(f"{name}_HeadPivot", None)
    col.objects.link(head_piv)
    head_piv.parent = root
    head_piv.location = (0.0, -0.18, 0.36)
    _box_part(f"{name}_Head", (0.28, 0.26, 0.24), (0.0, -0.04, 0.07), col, m_coat, bevel_frac=0.2, parent=head_piv)
    _box_part(f"{name}_Cheeks", (0.18, 0.08, 0.09), (0.0, -0.16, 0.02), col, m_belly, bevel_frac=0.22, parent=head_piv)
    for sx in (-1, 1):
        _cone_part(f"{name}_Ear_{sx}", 0.06, 0.008, 0.12, (sx * 0.095, -0.02, 0.22), col, m_coat, rot_deg=(5, -sx * 14, 0), segs=4, parent=head_piv)
        _cone_part(f"{name}_EarIn_{sx}", 0.036, 0.005, 0.08, (sx * 0.095, -0.035, 0.215), col, m_pink, rot_deg=(5, -sx * 14, 0), segs=4, parent=head_piv)
    _add_eyes_and_nose(head_piv, -0.17, 0.09, 0.074, col, eye_hex=eye_hex, nose_hex="#EE7A8C", eye_sz=0.045)

    tail_piv = bpy.data.objects.new(f"{name}_TailPivot", None)
    col.objects.link(tail_piv)
    tail_piv.parent = root
    tail_piv.location = (0.0, 0.23, 0.29)
    _box_part(f"{name}_Tail1", (0.055, 0.18, 0.055), (0.0, 0.08, 0.09), col, m_coat, rot_deg=(-52, 0, 0), bevel_frac=0.25, parent=tail_piv)
    _box_part(f"{name}_Tail2", (0.05, 0.14, 0.05), (0.0, 0.15, 0.21), col, m_coat, rot_deg=(-18, 0, 0), bevel_frac=0.25, parent=tail_piv)
    return {"root": root, "head": head_piv, "tail": tail_piv}


def build_pet_bunny(name: str, col, location=(0, 0, 0), yaw_deg=0.0, fur_hex="#FAF7F2"):
    """Cute Roblox-stylized White Bunny with tall pink inner ears & cotton tail."""
    root = bpy.data.objects.new(name, None)
    col.objects.link(root)
    root.location = Vector(location)
    root.rotation_euler = Euler((0, 0, math.radians(yaw_deg)))
    m_fur = _mat("BunnyFur", fur_hex, 0.62)
    m_pink = _mat("BunnyPink", "#F9A8BC", 0.5)

    _box_part(f"{name}_Body", (0.22, 0.30, 0.22), (0.0, 0.02, 0.14), col, m_fur, bevel_frac=0.24, parent=root)
    _box_part(f"{name}_Head", (0.23, 0.22, 0.21), (0.0, -0.10, 0.31), col, m_fur, bevel_frac=0.24, parent=root)
    for sx in (-1, 1):
        _box_part(f"{name}_Foot_{sx}", (0.075, 0.16, 0.05), (sx * 0.085, -0.04, 0.025), col, m_fur, bevel_frac=0.22, parent=root)
        _box_part(f"{name}_Ear_{sx}", (0.055, 0.035, 0.22), (sx * 0.065, -0.07, 0.49), col, m_fur, rot_deg=(-10, -sx * 8, 0), bevel_frac=0.22, parent=root)
        _box_part(f"{name}_EarIn_{sx}", (0.032, 0.02, 0.16), (sx * 0.065, -0.085, 0.49), col, m_pink, rot_deg=(-10, -sx * 8, 0), bevel_frac=0.2, parent=root)
    _sphere_part(f"{name}_CottonTail", (0.10, 0.10, 0.10), (0.0, 0.19, 0.12), col, m_fur, parent=root)
    _add_eyes_and_nose(root, -0.21, 0.33, 0.062, col, nose_hex="#F48AA4", eye_sz=0.038)
    return {"root": root}


def build_pet_duck(name: str, col, location=(0, 0, 0), yaw_deg=0.0, body_hex="#F9D949"):
    """Cute Roblox Park Duck / Duckling with bright orange beak, wings & webbed feet."""
    root = bpy.data.objects.new(name, None)
    col.objects.link(root)
    root.location = Vector(location)
    root.rotation_euler = Euler((0, 0, math.radians(yaw_deg)))
    m_body = _mat("DuckYellow", body_hex, 0.45)
    m_beak = _mat("DuckOrange", "#F27924", 0.35)
    m_eye = _mat("DuckEye", "#181820", 0.08)
    m_hl = _mat("DuckHL", "#FFFFFF", 0.05)

    _box_part(f"{name}_Body", (0.22, 0.32, 0.19), (0.0, 0.02, 0.16), col, m_body, bevel_frac=0.22, parent=root)
    _box_part(f"{name}_Head", (0.19, 0.19, 0.18), (0.0, -0.10, 0.32), col, m_body, bevel_frac=0.22, parent=root)
    _box_part(f"{name}_Beak", (0.12, 0.11, 0.045), (0.0, -0.23, 0.29), col, m_beak, bevel_frac=0.22, parent=root)
    for sx in (-1, 1):
        _box_part(f"{name}_Wing_{sx}", (0.045, 0.22, 0.12), (sx * 0.12, 0.03, 0.17), col, m_body, bevel_frac=0.2, parent=root)
        _box_part(f"{name}_Leg_{sx}", (0.035, 0.035, 0.07), (sx * 0.06, 0.0, 0.045), col, m_beak, bevel_frac=0.15, parent=root)
        _box_part(f"{name}_Foot_{sx}", (0.08, 0.11, 0.02), (sx * 0.06, -0.025, 0.01), col, m_beak, bevel_frac=0.2, parent=root)
        _sphere_part(f"{name}_Eye_{sx}", (0.038, 0.03, 0.042), (sx * 0.065, -0.195, 0.34), col, m_eye, parent=root)
        _sphere_part(f"{name}_HL_{sx}", (0.014, 0.014, 0.014), (sx * 0.072, -0.205, 0.35), col, m_hl, parent=root)
    _box_part(f"{name}_Tail", (0.10, 0.12, 0.06), (0.0, 0.20, 0.23), col, m_body, rot_deg=(-35, 0, 0), bevel_frac=0.2, parent=root)
    return {"root": root}


def build_pet_bird(name: str, col, location=(0, 0, 0), yaw_deg=0.0, body_hex="#4A90D9", belly_hex="#F2EFE9"):
    """Cute Roblox Songbird with fanned tail & tucked wings."""
    root = bpy.data.objects.new(name, None)
    col.objects.link(root)
    root.location = Vector(location)
    root.rotation_euler = Euler((0, 0, math.radians(yaw_deg)))
    m_body = _mat("BirdBlue", body_hex, 0.44)
    m_belly = _mat("BirdBelly", belly_hex, 0.5)
    m_beak = _mat("BirdBeak", "#F2A922", 0.32)
    m_eye = _mat("BirdEye", "#15151B", 0.08)

    _box_part(f"{name}_Body", (0.14, 0.22, 0.13), (0.0, 0.0, 0.13), col, m_body, rot_deg=(12, 0, 0), bevel_frac=0.24, parent=root)
    _box_part(f"{name}_Belly", (0.11, 0.14, 0.09), (0.0, -0.04, 0.10), col, m_belly, bevel_frac=0.24, parent=root)
    _box_part(f"{name}_Head", (0.13, 0.13, 0.12), (0.0, -0.08, 0.22), col, m_body, bevel_frac=0.25, parent=root)
    _cone_part(f"{name}_Beak", 0.032, 0.004, 0.065, (0.0, -0.17, 0.21), col, m_beak, rot_deg=(90, 0, 0), segs=4, parent=root)
    for sx in (-1, 1):
        _box_part(f"{name}_Wing_{sx}", (0.03, 0.17, 0.09), (sx * 0.075, 0.02, 0.13), col, m_body, rot_deg=(-8, 0, 0), bevel_frac=0.22, parent=root)
        _box_part(f"{name}_Leg_{sx}", (0.018, 0.018, 0.07), (sx * 0.035, 0.0, 0.035), col, m_beak, bevel_frac=0.1, parent=root)
        _sphere_part(f"{name}_Eye_{sx}", (0.026, 0.022, 0.028), (sx * 0.048, -0.14, 0.235), col, m_eye, parent=root)
    _box_part(f"{name}_Tail", (0.08, 0.15, 0.025), (0.0, 0.16, 0.14), col, m_body, rot_deg=(-22, 0, 0), bevel_frac=0.2, parent=root)
    return {"root": root}


def build_nature_sakura_tree(name: str, col, location=(0, 0, 0)):
    """Stylized Roblox Sakura blossom tree with sculpted trunk & pink blossom clusters."""
    root = bpy.data.objects.new(name, None)
    col.objects.link(root)
    root.location = Vector(location)
    m_bark = _mat("SakuraBark", "#5E3F33", 0.82)
    m_blos1 = _mat("SakuraPink1", "#F7A6C4", 0.65)
    m_blos2 = _mat("SakuraPink2", "#FAC8DA", 0.68)

    _cone_part(f"{name}_Trunk", 0.34, 0.22, 2.2, (0.0, 0.0, 1.1), col, m_bark, segs=8, parent=root)
    _cone_part(f"{name}_BranchL", 0.16, 0.10, 1.3, (-0.42, 0.1, 2.35), col, m_bark, rot_deg=(12, -32, 0), segs=7, parent=root)
    _cone_part(f"{name}_BranchR", 0.16, 0.10, 1.4, (0.45, -0.1, 2.40), col, m_bark, rot_deg=(-10, 34, 0), segs=7, parent=root)
    clusters = [
        ((0.0, 0.0, 3.25), (2.2, 2.1, 1.35), m_blos1),
        ((-0.95, 0.25, 2.75), (1.45, 1.40, 1.05), m_blos2),
        ((1.00, -0.20, 2.85), (1.50, 1.45, 1.10), m_blos1),
        ((0.10, 0.90, 2.95), (1.35, 1.35, 1.00), m_blos2),
        ((-0.15, -0.85, 3.00), (1.40, 1.35, 1.05), m_blos1),
    ]
    for i, (pos, sz, mat) in enumerate(clusters):
        _sphere_part(f"{name}_Blossom_{i}", sz, pos, col, mat, parent=root)
    return {"root": root}


def build_nature_bush_flowers(name: str, col, location=(0, 0, 0)):
    """Lush garden bush with colorful daisies/tulips."""
    root = bpy.data.objects.new(name, None)
    col.objects.link(root)
    root.location = Vector(location)
    m_leaf1 = _mat("BushLeaf1", "#3D8E42", 0.72)
    m_leaf2 = _mat("BushLeaf2", "#52A84C", 0.70)
    m_center = _mat("FlwCtr", "#FFD23F", 0.4)
    flw_mats = [_mat("FlwPink", "#F46E94", 0.45), _mat("FlwWhite", "#FAF8F2", 0.45), _mat("FlwBlue", "#6AB3F7", 0.45)]

    clumps = [((0.0, 0.0, 0.34), (0.88, 0.80, 0.68), m_leaf1), ((-0.36, 0.12, 0.26), (0.58, 0.56, 0.50), m_leaf2), ((0.38, -0.08, 0.28), (0.60, 0.55, 0.52), m_leaf2)]
    for i, (p, s, m) in enumerate(clumps):
        _sphere_part(f"{name}_Leaf_{i}", s, p, col, m, parent=root)
    blooms = [(-0.22, -0.32, 0.42), (0.16, -0.35, 0.48), (-0.42, -0.10, 0.34), (0.36, -0.22, 0.38), (0.02, -0.18, 0.62)]
    for i, (bx, by, bz) in enumerate(blooms):
        _sphere_part(f"{name}_Flw_{i}", (0.11, 0.11, 0.05), (bx, by, bz), col, flw_mats[i % 3], parent=root)
        _sphere_part(f"{name}_Ctr_{i}", (0.045, 0.045, 0.045), (bx, by, bz + 0.02), col, m_center, parent=root)
    return {"root": root}


def build_nature_potted_monstera(name: str, col, location=(0, 0, 0)):
    """Indoor potted plant (terracotta pot + soil + broad stylized leaves)."""
    root = bpy.data.objects.new(name, None)
    col.objects.link(root)
    root.location = Vector(location)
    m_pot = _mat("Terracotta", "#C46842", 0.65)
    m_soil = _mat("Soil", "#3B2B22", 0.90)
    m_leaf = _mat("MonsteraLeaf", "#2F7D3E", 0.42)

    _cone_part(f"{name}_Pot", 0.16, 0.22, 0.36, (0.0, 0.0, 0.18), col, m_pot, segs=16, parent=root)
    _cone_part(f"{name}_Rim", 0.235, 0.235, 0.06, (0.0, 0.0, 0.34), col, m_pot, segs=16, parent=root)
    _cone_part(f"{name}_Soil", 0.19, 0.19, 0.04, (0.0, 0.0, 0.33), col, m_soil, segs=12, parent=root)
    for i in range(6):
        ang = i * 60.0
        rad = math.radians(ang)
        dx, dy = 0.14 * math.cos(rad), 0.14 * math.sin(rad)
        _box_part(f"{name}_Stem_{i}", (0.022, 0.022, 0.34), (dx * 0.45, dy * 0.45, 0.48), col, m_leaf, rot_deg=(-22 * math.sin(rad), 22 * math.cos(rad), ang), bevel_frac=0.1, parent=root)
        _box_part(f"{name}_Leaf_{i}", (0.24, 0.18, 0.02), (dx * 1.4, dy * 1.4, 0.64 + (i % 2) * 0.08), col, m_leaf, rot_deg=(0, -25, ang), bevel_frac=0.35, parent=root)
    return {"root": root}


def animate_pet_idle_wag(pet_info: dict, fs: int, fe: int, wag_hz: float = 2.5, head_bob: bool = True):
    """Add friendly 30fps tail wag & subtle head curiosity tilt onto a live dog/cat pet rig."""
    tail = pet_info.get("tail")
    head = pet_info.get("head")
    step = 4
    for f in range(fs, fe + 1, step):
        t = (f - fs) / 30.0
        if tail:
            tail.rotation_euler = Euler((0.0, 0.0, math.radians(22.0 * math.sin(2.0 * math.pi * wag_hz * t))))
            tail.keyframe_insert("rotation_euler", frame=f)
        if head and head_bob:
            head.rotation_euler = Euler((math.radians(4.0 * math.sin(t * 2.0)), math.radians(7.0 * math.sin(t * 1.4)), 0.0))
            head.keyframe_insert("rotation_euler", frame=f)

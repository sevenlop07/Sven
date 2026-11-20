# SPDX-License-Identifier: GPL-3.0-or-later
"""Sven Core Automated Blender 5.3 Director Engine (blender_auto_director.py).

Distills and upgrades the 4 core open-source automation engines from scenario-labs/blender-plugin
for zero-cost, 100% local execution inside the Sven Cinematic Universe (Blender 5.0-5.3+):
1. Blockout Engine: Structured JSON-to-3D greybox layout builder (6 primitives, 10 semantic categories,
   12-color muted palette, 8-corner tangent + lens-shift camera framing, and sun auto-rigging).
2. Shot Plan & 20-Preset Camera Path Engine: Bounding-box 70% frame-fill solver, 20 cinematic camera
   move presets, natural-language shot parser, editable frustum markers, and Blender 5.3 channelbag
   F-curve Bezier smoothing.
3. Multi-View & Multi-Frame Contact Sheet QA Engine: Pure-stdlib TARGA_RAW -> 5x7 bitmap-labeled PNG
   contact sheet composer (angles: front/back/left/right/top/three_quarter, or timeline frames).
4. Universal 5-Family Humanoid Retargeter: Auto-detects Mixamo, Meshy, SMPL, Unreal (UE5), and
   Roblox_R15 skeletons; retargets animations with leg-length scaling, sole-to-floor lift (zero foot
   sinking/skating), and Blender 5.3 Slotted Actions (channelbags).
"""

from __future__ import annotations

import argparse
import base64
import contextlib
import json
import math
import os
import re
import shutil
import struct
import sys
import tempfile
import zlib
from dataclasses import dataclass
from math import acos, atan2, cos, radians, sin, sqrt

try:
    import bmesh
    import bpy
    from mathutils import Euler, Matrix, Quaternion, Vector

    HAS_BPY = True
except ImportError:
    HAS_BPY = False


# ==============================================================================
# 1. BLOCKOUT ENGINE (JSON-TO-3D GREYBOX SCENE LAYOUT & AUTO-FRAMING)
# ==============================================================================

MAX_ELEMENTS = 400
MIN_SIZE, MAX_SIZE = 0.02, 500.0
MAX_COORD = 2000.0

PRIMITIVES = ("box", "cylinder", "plane", "wedge", "cone", "sphere")

CATEGORIES = {
    "floor": ("Floor", (0.62, 0.62, 0.64)),
    "wall": ("Wall", (0.78, 0.78, 0.80)),
    "structure": ("Structure", (0.55, 0.62, 0.72)),
    "prop": ("Prop", (0.85, 0.62, 0.35)),
    "furniture": ("Furniture", (0.70, 0.52, 0.38)),
    "vegetation": ("Vegetation", (0.42, 0.62, 0.40)),
    "vehicle": ("Vehicle", (0.75, 0.40, 0.40)),
    "water": ("Water", (0.40, 0.60, 0.78)),
    "light": ("Light", (0.90, 0.82, 0.45)),
    "other": ("Other", (0.66, 0.66, 0.66)),
}
DEFAULT_CATEGORY = "other"

DENSITIES = (
    ("simple", "Simple", "A small readable layout: 30 to 60 primitives", (30, 60)),
    ("medium", "Medium", "A dressed scene with some detail: 60 to 120 primitives", (60, 120)),
    ("advanced", "Advanced", "A rich scene with layered detail: 120 to 200 primitives", (120, 200)),
    ("expert", "Expert", "A dense, large scene: 200 to 350 primitives", (200, 350)),
)
DEFAULT_DENSITY = "advanced"

PALETTE = (
    (0.212, 0.366, 0.195),  # sage
    (0.571, 0.216, 0.114),  # terracotta
    (0.159, 0.275, 0.491),  # slate blue
    (0.638, 0.402, 0.084),  # ochre
    (0.584, 0.246, 0.314),  # dusty rose
    (0.114, 0.381, 0.361),  # teal
    (0.328, 0.270, 0.552),  # lavender
    (0.571, 0.462, 0.262),  # sand
    (0.332, 0.150, 0.279),  # plum
    (0.262, 0.323, 0.402),  # steel
    (0.275, 0.328, 0.084),  # moss
    (0.462, 0.130, 0.109),  # brick
)

BLOCKOUT_COLLECTION = "Blockout"
BLOCKOUT_MARK = "sven_blockout"
BLOCKOUT_GROUP_KEY = "sven_blockout_group"
_BLOCKOUT_MESHES = {}

_BLOCKOUT_ROLE = (
    "You are a senior level designer building a 3D blockout (greybox) in Blender for a game or "
    "film scene. The blockout is built only from simple primitives, but it must read clearly as "
    "the requested place: recognisable silhouette, correct real-world proportions, a clear "
    "hierarchy of masses, and enough secondary detail that someone seeing a grey render names the "
    "place at once.\n\n"
)
_BLOCKOUT_FORMAT = (
    "OUTPUT: ONLY a JSON array, no prose, no code fence. Write each group as its label (a string) "
    "followed by one row per element of that group:\n"
    '["<group label>", ["<short unique name>", "<category>", "<primitive>", x, y, z, sx, sy, sz, '
    'yaw], ["<name>", ...], "<next group label>", [...], ...]\n'
    "category: floor|wall|structure|prop|furniture|vegetation|vehicle|water|light|other. "
    "primitive: box|cylinder|plane|wedge|cone|sphere. yaw: degrees about Z. Numbers have at most "
    "two decimals.\n"
    "Units are metres. Z is up. Ground is z = 0. x, y, z is the CENTRE of the shape, so an "
    "element resting on the ground has z = sz / 2, and an element resting on top of another "
    "has z = (support top) + sz / 2. sx, sy, sz is the full extent along x, y, z before the yaw "
    "rotation. A plane is a thin box. A wedge rises from -x (low edge) to +x (high edge): use two "
    "wedges back to back (one rotated 180) for a gable roof. A cone's tip points up. A cylinder's "
    "axis is Z.\n\n"
)
_BLOCKOUT_RULES = (
    "COMPOSITION RULES\n"
    "1. Start from the big masses (ground, terrain, main buildings), then secondary masses "
    "(towers, wings, roofs, stairs, bridges), then tertiary detail that sells the identity "
    "(crenellations, buttresses, chimneys, window bands, doors, fences, props, vegetation).\n"
    "2. Use {low} to {high} elements. Spend at least a third of them on tertiary detail. Repeat "
    "detail rhythmically (a crenellation every 1.5 m along a wall top, a window every 3 to 4 m on "
    "a facade, a buttress every 5 to 6 m).\n"
    "3. Nothing floats and nothing is buried by accident: every element rests on the ground or on "
    "another element, or is attached to the side of one. Attached parts touch their support face "
    "exactly.\n"
    "4. No unintended overlaps. Intentional joins (a tower merging into a wall, a roof sitting on "
    "a body) are fine.\n"
    "5. Real proportions. Doors 1 m wide by 2.2 m (houses) or 3 to 4 m by 4 to 5 m (gates). Storey "
    "height 3 to 4 m. A person is 1.8 m. Keep every mass at believable metric scale for the place "
    "described.\n"
    "6. Group elements into 4 to 10 named groups that a level designer would use as collections "
    "(for example Keep, Curtain Walls, Towers, Gatehouse, Courtyard, Terrain).\n"
    "7. Categories drive colour: walls and towers of a building are structure or wall, roofs are "
    "structure, ground and paths are floor, water is water, trees and hedges are vegetation, carts "
    "and boats are vehicle, lanterns and torches are light, everything small and loose is prop.\n"
    "8. Design for a camera: leave a clear approach path and one open vantage point from which the "
    "main silhouette reads.\n\n"
    "Before answering, check every element's z against rule 3 and fix it.\n\n"
)


def blockout_llm_prompt(prompt: str, density: str = DEFAULT_DENSITY, previous=None) -> str:
    """Return the system/user prompt for an LLM to author a structured 3D Blockout JSON array."""
    low, high = next((r for k, _l, _d, r in DENSITIES if k == density), DENSITIES[2][3])
    head = (
        _BLOCKOUT_ROLE
        + _BLOCKOUT_FORMAT
        + _BLOCKOUT_RULES.replace("{low}", str(low)).replace("{high}", str(high))
    )
    if previous:
        return (
            head
            + "Here is the current plan in the same format; return an UPDATED full plan applying "
            + "this change: "
            + str(prompt)
            + "\nCurrent plan:\n"
            + encode_blockout_rows(previous)
        )
    return head + "Scene to block out: " + (str(prompt).strip() or "a cinematic 3D film set")


def _num(value, default, lo, hi):
    try:
        n = float(value)
    except (TypeError, ValueError):
        return default
    if n != n or n in (float("inf"), float("-inf")):
        return default
    return max(lo, min(hi, n))


def _vec3(value, defaults, lo, hi):
    seq = value if isinstance(value, (list, tuple)) else []
    return [_num(seq[i] if i < len(seq) else defaults[i], defaults[i], lo, hi) for i in range(3)]


def _from_rows(items):
    elements, group = [], None
    for item in items:
        if isinstance(item, str):
            group = item
        elif isinstance(item, dict):
            elements.append(item)
        elif isinstance(item, list) and len(item) == 10:
            name, category, primitive, x, y, z, sx, sy, sz, yaw = item
            element = {
                "name": name,
                "category": category,
                "primitive": primitive,
                "position": [x, y, z],
                "size": [sx, sy, sz],
                "rotation": yaw,
            }
            if group is not None:
                element["group"] = group
            elements.append(element)
    return elements


def parse_blockout_plan(text_or_data) -> list[dict]:
    """Parse a JSON string, file content, or Python list into sanitized blockout elements."""
    if isinstance(text_or_data, list):
        data = text_or_data
    else:
        text = str(text_or_data or "").strip()
        fence = re.search(r"```(?:json)?\s*(.+?)```", text, re.DOTALL)
        if fence:
            text = fence.group(1).strip()
        start, end = text.find("["), text.rfind("]")
        if start == -1 or end == -1 or end <= start:
            return []
        try:
            data = json.loads(text[start : end + 1])
        except ValueError:
            return []
    if not isinstance(data, list):
        return []
    elements = []
    for index, raw in enumerate(_from_rows(data)[:MAX_ELEMENTS]):
        if not isinstance(raw, dict):
            continue
        name = str(raw.get("name") or f"Block {index + 1}").strip()[:60] or f"Block {index + 1}"
        category = str(raw.get("category") or DEFAULT_CATEGORY).strip().lower()
        if category not in CATEGORIES:
            category = DEFAULT_CATEGORY
        primitive = str(raw.get("primitive") or "box").strip().lower()
        if primitive not in PRIMITIVES:
            primitive = "box"
        size = _vec3(raw.get("size"), [1.0, 1.0, 1.0], MIN_SIZE, MAX_SIZE)
        position = _vec3(raw.get("position"), [0.0, 0.0, size[2] / 2.0], -MAX_COORD, MAX_COORD)
        rotation = _num(raw.get("rotation"), 0.0, -360.0, 360.0)
        group = str(raw.get("group") or BLOCKOUT_COLLECTION).strip()[:60] or BLOCKOUT_COLLECTION
        elements.append(
            {
                "name": name,
                "category": category,
                "primitive": primitive,
                "position": position,
                "size": size,
                "rotation": rotation,
                "group": group,
            }
        )
    return elements


def encode_blockout_rows(elements) -> str:
    """Encode blockout elements into the compact grouped row JSON string."""
    rows, group = [], None
    for el in parse_blockout_plan(elements):
        if el["group"] != group:
            group = el["group"]
            rows.append(group)
        rows.append(
            [
                el["name"],
                el["category"],
                el["primitive"],
                *el["position"],
                *el["size"],
                el["rotation"],
            ]
        )
    return json.dumps(rows, separators=(",", ":"))


def plan_bounds(elements):
    """Return ((x, y, z) low, (x, y, z) high) enclosing all blockout elements."""
    low = [float("inf")] * 3
    high = [float("-inf")] * 3
    for element in elements:
        position = element.get("position") or (0.0, 0.0, 0.0)
        size = element.get("size") or (1.0, 1.0, 1.0)
        yaw = radians(element.get("rotation", 0.0) or 0.0)
        c, s = abs(cos(yaw)), abs(sin(yaw))
        half = (
            (c * size[0] + s * size[1]) / 2.0,
            (s * size[0] + c * size[1]) / 2.0,
            size[2] / 2.0,
        )
        for axis in range(3):
            low[axis] = min(low[axis], position[axis] - half[axis])
            high[axis] = max(high[axis], position[axis] + half[axis])
    if low[0] == float("inf"):
        return None
    return tuple(low), tuple(high)


def _direction(azimuth: float, elevation: float):
    a, e = radians(azimuth), radians(elevation)
    return (sin(a) * cos(e), -cos(a) * cos(e), sin(e))


def look_euler(direction):
    x, y, z = direction
    length = sqrt(x * x + y * y + z * z)
    x, y, z = x / length, y / length, z / length
    return (acos(max(-1.0, min(1.0, -z))), 0.0, atan2(-x, y))


def view_tangents(aspect: float, lens: float = 35.0, sensor: float = 36.0):
    if aspect >= 1.0:
        horizontal = sensor / (2.0 * lens)
        return horizontal, horizontal / aspect
    vertical = sensor / (2.0 * lens)
    return vertical * aspect, vertical


def frame_camera(
    low,
    high,
    aspect: float = 16.0 / 9.0,
    *,
    azimuth: float = 35.0,
    elevation: float = 22.0,
    lens: float = 35.0,
    sensor: float = 36.0,
    margin: float = 0.06,
) -> dict:
    """Compute camera location, rotation, lens, shift, and clip planes keeping 100% of low..high in frame."""
    centre = tuple((a + b) / 2.0 for a, b in zip(low, high, strict=False))
    toward = _direction(azimuth, elevation)
    forward = (-toward[0], -toward[1], -toward[2])
    right = (forward[1], -forward[0], 0.0)
    norm = sqrt(right[0] ** 2 + right[1] ** 2)
    right = (right[0] / norm, right[1] / norm, 0.0)
    up = (
        right[1] * forward[2] - right[2] * forward[1],
        right[2] * forward[0] - right[0] * forward[2],
        right[0] * forward[1] - right[1] * forward[0],
    )
    tan_h, tan_v = view_tangents(aspect, lens, sensor)
    tan_h, tan_v = tan_h / (1.0 + margin), tan_v / (1.0 + margin)
    corners = [
        (x, y, z) for x in (low[0], high[0]) for y in (low[1], high[1]) for z in (low[2], high[2])
    ]
    offsets = [tuple(c - m for c, m in zip(corner, centre, strict=False)) for corner in corners]
    dot = lambda a, b: a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
    distance = 0.0
    for offset in offsets:
        depth = dot(offset, forward)
        distance = max(
            distance,
            abs(dot(offset, right)) / tan_h - depth,
            abs(dot(offset, up)) / tan_v - depth,
            1e-3 - depth,
        )
    depths = [distance + dot(offset, forward) for offset in offsets]
    across = [dot(o, right) / d for o, d in zip(offsets, depths, strict=False)]
    upward = [dot(o, up) / d for o, d in zip(offsets, depths, strict=False)]
    full_h, full_v = view_tangents(aspect, lens, sensor)
    fill = max(
        (max(across) - min(across)) / (2.0 * full_h),
        (max(upward) - min(upward)) / (2.0 * full_v),
        0.25,
    )
    fill = min(1.0, fill * (1.0 + margin))
    longer = 2.0 * max(full_h, full_v) * fill
    return {
        "location": tuple(c + t * distance for c, t in zip(centre, toward, strict=False)),
        "rotation": look_euler(forward),
        "lens": lens / fill,
        "shift": (
            (max(across) + min(across)) / 2.0 / longer,
            (max(upward) + min(upward)) / 2.0 / longer,
        ),
        "clip_start": max(0.001, 0.02 * min(depths)),
        "clip_end": max(100.0, 2.0 * max(depths)),
    }


def frame_sun(low, high, azimuth: float = -20.0, elevation: float = 50.0) -> dict:
    centre = tuple((a + b) / 2.0 for a, b in zip(low, high, strict=False))
    radius = sqrt(sum((b - a) ** 2 for a, b in zip(low, high, strict=False))) / 2.0
    toward = _direction(azimuth, elevation)
    return {
        "location": tuple(c + t * (radius + 5.0) for c, t in zip(centre, toward, strict=False)),
        "rotation": look_euler(tuple(-t for t in toward)),
    }


def _blockout_mesh_for(primitive: str):
    mesh = _BLOCKOUT_MESHES.get(primitive)
    try:
        if mesh is not None and mesh.name in bpy.data.meshes:
            return mesh
    except ReferenceError:
        pass
    if primitive == "wedge":
        verts = [
            (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
        ]
        faces = [(0, 1, 2, 3), (1, 4, 5, 2), (0, 4, 1), (3, 2, 5), (0, 3, 5, 4)]
        mesh = bpy.data.meshes.new("Sven Blockout wedge")
        mesh.from_pydata(verts, [], faces)
        mesh.update()
    elif primitive == "cylinder":
        mesh = bpy.data.meshes.new("Sven Blockout cylinder")
        bm = bmesh.new()
        bmesh.ops.create_cone(
            bm, cap_ends=True, cap_tris=False, segments=24, radius1=0.5, radius2=0.5, depth=1.0
        )
        bm.to_mesh(mesh)
        bm.free()
        mesh.update()
    elif primitive == "cone":
        mesh = bpy.data.meshes.new("Sven Blockout cone")
        bm = bmesh.new()
        bmesh.ops.create_cone(
            bm, cap_ends=True, cap_tris=False, segments=24, radius1=0.5, radius2=0.0, depth=1.0
        )
        bm.to_mesh(mesh)
        bm.free()
        mesh.update()
    elif primitive == "sphere":
        mesh = bpy.data.meshes.new("Sven Blockout sphere")
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=20, v_segments=12, radius=0.5)
        bm.to_mesh(mesh)
        bm.free()
        mesh.update()
    else:
        verts = [
            (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (-0.5, -0.5, 0.5),
            (0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
        ]
        faces = [
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 1, 5, 4),
            (1, 2, 6, 5),
            (2, 3, 7, 6),
            (3, 0, 4, 7),
        ]
        mesh = bpy.data.meshes.new("Sven Blockout box")
        mesh.from_pydata(verts, [], faces)
        mesh.update()
    _BLOCKOUT_MESHES[primitive] = mesh
    return mesh


def _ensure_blockout_material(group: str, colour: tuple, category: str = "other"):
    mat_name = f"Blockout_{group}"[:63]
    mat = bpy.data.materials.get(mat_name)
    if mat is None:
        mat = bpy.data.materials.new(mat_name)
    mat[BLOCKOUT_GROUP_KEY] = group
    mat.diffuse_color = colour
    if not mat.node_tree:
        mat.use_nodes = True
    tree = mat.node_tree
    bsdf = next((n for n in tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if bsdf is None:
        bsdf = tree.nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = colour
    if category == "water":
        bsdf.inputs["Roughness"].default_value = 0.08
    elif category == "light":
        bsdf.inputs["Roughness"].default_value = 0.3
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = colour
            bsdf.inputs["Emission Strength"].default_value = 2.5
    else:
        bsdf.inputs["Roughness"].default_value = 0.78
    return mat


def clear_blockout_scene(collection_name: str = BLOCKOUT_COLLECTION) -> int:
    """Remove a previously built Blockout collection and its objects."""
    root = bpy.data.collections.get(collection_name)
    if root is None:
        return 0
    collections = (root, *tuple(root.children_recursive))
    objects = {obj for coll in collections for obj in coll.objects}
    for obj in objects:
        bpy.data.objects.remove(obj, do_unlink=True)
    for coll in reversed(collections):
        bpy.data.collections.remove(coll)
    return len(objects)


def build_blockout_scene(
    plan_data,
    *,
    collection_name: str = BLOCKOUT_COLLECTION,
    dress: bool = True,
    color_by_category: bool = False,
    bevel_width: float = 0.0,
    clear_default_cube: bool = True,
) -> dict:
    """Build a 3D Blockout layout in Blender 5.3 from a JSON plan or list of rows/dicts."""
    elements = parse_blockout_plan(plan_data)
    if not elements:
        raise ValueError("Blockout plan contains 0 valid elements")
    scene = bpy.context.scene
    if clear_default_cube:
        default_cube = bpy.data.objects.get("Cube")
        if default_cube is not None and default_cube.type == "MESH" and len(default_cube.data.vertices) == 8:
            bpy.data.objects.remove(default_cube, do_unlink=True)
    clear_blockout_scene(collection_name)
    root = bpy.data.collections.new(collection_name)
    root[BLOCKOUT_MARK] = True
    scene.collection.children.link(root)

    group_names = list(
        dict.fromkeys(el.get("group") or collection_name for el in elements)
    )
    group_colours = {
        g: (*PALETTE[i % len(PALETTE)], 1.0) for i, g in enumerate(group_names)
    }
    groups = {}
    created = []

    for el in elements:
        group = el.get("group") or collection_name
        category = el.get("category") or DEFAULT_CATEGORY
        if group == collection_name:
            gcoll = root
        else:
            gcoll = groups.get(group)
            if gcoll is None:
                gcoll = bpy.data.collections.new(group)
                gcoll[BLOCKOUT_MARK] = True
                root.children.link(gcoll)
                groups[group] = gcoll
        mesh = _blockout_mesh_for(el.get("primitive") or "box")
        obj = bpy.data.objects.new(el.get("name") or "Block", mesh)
        gcoll.objects.link(obj)
        obj.location = el.get("position") or (0.0, 0.0, 0.0)
        obj.scale = el.get("size") or (1.0, 1.0, 1.0)
        obj.rotation_euler = (0.0, 0.0, radians(el.get("rotation", 0.0) or 0.0))

        if color_by_category or category in ("water", "light", "vegetation", "floor"):
            r, g, b = CATEGORIES.get(category, CATEGORIES[DEFAULT_CATEGORY])[1]
            colour = (r, g, b, 1.0)
            mat_key = f"{group}_{category}"
        else:
            colour = group_colours[group]
            mat_key = group

        if dress:
            mat = _ensure_blockout_material(mat_key, colour, category=category)
            if not obj.data.materials:
                obj.data.materials.append(None)
            obj.material_slots[0].link = "OBJECT"
            obj.material_slots[0].material = mat

        if bevel_width > 0 and el.get("primitive") in ("box", "wedge", "cylinder"):
            bev = obj.modifiers.new(name="Bevel", type="BEVEL")
            bev.width = bevel_width
            bev.segments = 2

        obj.color = colour
        obj[BLOCKOUT_MARK] = category
        obj.display_type = "SOLID"
        created.append(obj)

    added = []
    bounds = plan_bounds(elements)
    if dress and bounds is not None:
        if scene.camera is None and not any(o.type == "CAMERA" for o in scene.objects):
            render = scene.render
            aspect = (render.resolution_x * render.pixel_aspect_x) / max(
                1.0, render.resolution_y * render.pixel_aspect_y
            )
            fcam = frame_camera(bounds[0], bounds[1], aspect)
            cam_data = bpy.data.cameras.new("Blockout Camera")
            cam_data.lens = fcam["lens"]
            cam_data.shift_x, cam_data.shift_y = fcam["shift"]
            cam_data.clip_start, cam_data.clip_end = fcam["clip_start"], fcam["clip_end"]
            cam_obj = bpy.data.objects.new("Blockout Camera", cam_data)
            cam_obj.location = fcam["location"]
            cam_obj.rotation_euler = fcam["rotation"]
            scene.collection.objects.link(cam_obj)
            scene.camera = cam_obj
            added.append("Blockout Camera")
        if not any(o.type == "LIGHT" for o in scene.objects):
            fsun = frame_sun(bounds[0], bounds[1])
            sun_data = bpy.data.lights.new("Blockout Sun", "SUN")
            sun_data.energy = 3.0
            sun_obj = bpy.data.objects.new("Blockout Sun", sun_data)
            sun_obj.location = fsun["location"]
            sun_obj.rotation_euler = fsun["rotation"]
            scene.collection.objects.link(sun_obj)
            added.append("Blockout Sun")

    bpy.context.view_layer.update()
    return {
        "collection": root.name,
        "element_count": len(created),
        "groups": group_names,
        "bounds": bounds,
        "added": added,
    }


# ==============================================================================
# 2. SHOT PLAN & 20-PRESET BOUNDING-BOX CAMERA PATH ENGINE
# ==============================================================================

SENSOR_WIDTH = 36.0
FILL = 0.7
MIN_SEGMENT_SHARE = 0.05
DEFAULT_DURATION = 6.0
DEFAULT_FOCAL = 35.0
MIN_DURATION, MAX_DURATION = 1.0, 60.0

SHOTS_COLLECTION = "Sven Shots"
CAMERA_NAME = "Sven Shot Camera"
TARGET_NAME = "Sven Shot Target"
AIM_CONSTRAINT = "Sven Aim"
MARKER_PREFIX = "Shot "
PROP_INDEX, PROP_FOCAL, PROP_HOLD = "sven_shot_index", "sven_focal", "sven_hold"
FALLBACK_BOX = ((-1.0, -1.0, 0.0), (1.0, 1.0, 2.0))


@dataclass
class Waypoint:
    position: tuple
    rotation_euler: tuple = None
    look_at: tuple = None
    focal: float = DEFAULT_FOCAL
    hold: float = 0.0


def _dist(a, b):
    return math.sqrt(sum((float(x) - float(y)) ** 2 for x, y in zip(a, b, strict=False)))


def frame_schedule(waypoints: list[Waypoint], duration: float, fps: float):
    """Return keyframes as (frame, waypoint_index) pairs from frame 1 to round(duration * fps)."""
    n = len(waypoints)
    if n == 0:
        return []
    duration = max(1e-6, float(duration))
    total = max(2, int(round(duration * float(fps or 30))))
    if n == 1:
        return [(1, 0), (total, 0)]
    holds = [max(0.0, float(wp.hold or 0.0)) for wp in waypoints]
    hold_total = sum(holds)
    if hold_total > 0 and hold_total >= duration * 0.75:
        factor = (duration * 0.75) / hold_total
        holds = [h * factor for h in holds]
        hold_total = sum(holds)
    move_time = max(0.0, duration - hold_total)
    dists = [_dist(waypoints[i].position, waypoints[i + 1].position) for i in range(n - 1)]
    total_d = sum(dists)
    shares = [(d / total_d) if total_d > 0 else 1.0 / (n - 1) for d in dists]
    shares = [max(s, MIN_SEGMENT_SHARE) for s in shares]
    share_sum = sum(shares)
    shares = [s / share_sum for s in shares]
    times = [(0.0, 0)]
    t = 0.0
    if holds[0] > 0:
        t += holds[0]
        times.append((t, 0))
    for i, share in enumerate(shares):
        t += share * move_time
        times.append((t, i + 1))
        if holds[i + 1] > 0:
            t += holds[i + 1]
            times.append((t, i + 1))
    keys = []
    for time_s, index in times:
        frame = 1 + int(round(time_s / duration * (total - 1)))
        if keys and frame <= keys[-1][0]:
            if keys[-1][1] == index:
                continue
            frame = keys[-1][0] + 1
        keys.append((frame, index))
    keys[-1] = (max(total, keys[-1][0]), keys[-1][1])
    return keys


def _box(bbox_min, bbox_max):
    lo = tuple(float(v) for v in bbox_min)
    hi = tuple(float(v) for v in bbox_max)
    centre = tuple((a + b) / 2.0 for a, b in zip(lo, hi, strict=False))
    extents = tuple(max(1e-3, b - a) for a, b in zip(lo, hi, strict=False))
    size = max(extents)
    diagonal = math.sqrt(sum(e * e for e in extents))
    return centre, size, diagonal


def fit_distance(diagonal: float, focal: float = DEFAULT_FOCAL, fill: float = FILL) -> float:
    """Camera distance at which a sphere of the box's diagonal fills `fill` (70%) of the frame width."""
    half_fov = math.atan((SENSOR_WIDTH / 2.0) / max(1.0, float(focal)))
    return max(1e-3, diagonal) / (2.0 * fill * math.tan(half_fov))


def _wp(position, centre, focal):
    return Waypoint(tuple(position), look_at=tuple(centre), focal=float(focal))


def _ring(centre, rx, ry, height, focal, steps=12, start=0.0, sweep=2 * math.pi, rise=0.0):
    out = []
    closed = abs(sweep - 2 * math.pi) < 1e-9
    for i in range(steps + 1):
        if closed and i == steps:
            out.append(Waypoint(out[0].position, look_at=out[0].look_at, focal=out[0].focal))
            continue
        a = start + sweep * i / steps
        z = height + rise * (1.0 - math.cos(a)) / 2.0
        out.append(
            _wp((centre[0] + rx * math.sin(a), centre[1] - ry * math.cos(a), z), centre, focal)
        )
    return out


def _horizontal_radius(d, dz):
    return math.sqrt(max(d * d - dz * dz, (0.5 * d) ** 2))


def orbit(bbox_min, bbox_max, focal=DEFAULT_FOCAL, steps=12):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    dz = 0.35 * size
    r = _horizontal_radius(d, dz)
    return _ring(centre, r, r, centre[2] + dz, focal, steps=steps)


def orbit_high(bbox_min, bbox_max, focal=DEFAULT_FOCAL, steps=12):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    dz = 0.95 * size
    r = _horizontal_radius(1.15 * d, dz)
    return _ring(centre, r, r, centre[2] + dz, focal, steps=steps)


def orbit_low(bbox_min, bbox_max, focal=DEFAULT_FOCAL, steps=12):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    dz = -0.3 * size
    r = _horizontal_radius(d, dz)
    return _ring(centre, r, r, centre[2] + dz, focal, steps=steps)


def spiral_in(bbox_min, bbox_max, focal=DEFAULT_FOCAL, steps=12):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    out = []
    for i in range(steps + 1):
        t = i / steps
        a = 2 * math.pi * t
        r = d * (1.6 - 0.8 * t)
        z = centre[2] + size * (0.6 - 0.35 * t)
        out.append(
            _wp((centre[0] + r * math.sin(a), centre[1] - r * math.cos(a), z), centre, focal)
        )
    return out


def ellipse_1(bbox_min, bbox_max, focal=DEFAULT_FOCAL, steps=12):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    return _ring(centre, 1.7 * d, 0.85 * d, centre[2] + 0.3 * size, focal, steps=steps)


def ellipse_2(bbox_min, bbox_max, focal=DEFAULT_FOCAL, steps=12):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    return _ring(
        centre, 1.3 * d, 0.9 * d, centre[2] + 0.1 * size, focal, steps=steps, rise=1.1 * size
    )


def ellipse_3(bbox_min, bbox_max, focal=DEFAULT_FOCAL, steps=12):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    return _ring(centre, 0.6 * d, 0.95 * d, centre[2] + 0.25 * size, focal, steps=steps)


def dolly_in(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    height = centre[2] + 0.25 * size
    return [
        _wp((centre[0], centre[1] - 2.2 * d, height), centre, focal),
        _wp((centre[0], centre[1] - 0.8 * d, height), centre, focal),
    ]


def dolly_out(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    return list(reversed(dolly_in(bbox_min, bbox_max, focal)))


def _truck(bbox_min, bbox_max, focal, direction):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    height = centre[2] + 0.2 * size
    xs = (0.7 * d, 0.0, -0.7 * d) if direction < 0 else (-0.7 * d, 0.0, 0.7 * d)
    return [_wp((centre[0] + x, centre[1] - d, height), centre, focal) for x in xs]


def truck_left(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    return _truck(bbox_min, bbox_max, focal, -1)


def truck_right(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    return _truck(bbox_min, bbox_max, focal, +1)


def _pedestal(bbox_min, bbox_max, focal, direction):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    zs = (centre[2] - 0.4 * size, centre[2] + 0.25 * size, centre[2] + 0.9 * size)
    if direction < 0:
        zs = tuple(reversed(zs))
    return [_wp((centre[0], centre[1] - d, z), centre, focal) for z in zs]


def pedestal_up(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    return _pedestal(bbox_min, bbox_max, focal, +1)


def pedestal_down(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    return _pedestal(bbox_min, bbox_max, focal, -1)


def zoom_in(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    position = (centre[0], centre[1] - 1.1 * d, centre[2] + 0.25 * size)
    return [
        Waypoint(position, look_at=centre, focal=max(8.0, float(focal) / 2.0)),
        Waypoint(position, look_at=centre, focal=float(focal)),
    ]


def crane(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    return [
        _wp((centre[0], centre[1] - d, centre[2] - 0.2 * size), centre, focal),
        _wp((centre[0], centre[1] - 0.9 * d, centre[2] + 1.2 * size), centre, focal),
    ]


def _arc(bbox_min, bbox_max, focal, direction, steps=4):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    dz = 0.3 * size
    r = _horizontal_radius(d, dz)
    return _ring(centre, r, r, centre[2] + dz, focal, steps=steps, sweep=direction * math.pi / 2.0)


def arc_left(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    return _arc(bbox_min, bbox_max, focal, -1)


def arc_right(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    return _arc(bbox_min, bbox_max, focal, +1)


def top_down(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    return [
        _wp((centre[0], centre[1] - 0.15 * d, centre[2] + 2.2 * d), centre, focal),
        _wp((centre[0], centre[1] - 0.25 * d, centre[2] + 1.4 * d), centre, focal),
        _wp((centre[0], centre[1] - 0.35 * d, centre[2] + 0.9 * d), centre, focal),
    ]


def pan(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    height = centre[2] + 0.2 * size
    return [
        _wp((centre[0] - 0.9 * d, centre[1] - d, height), centre, focal),
        _wp((centre[0], centre[1] - d, height), centre, focal),
        _wp((centre[0] + 0.9 * d, centre[1] - d, height), centre, focal),
    ]


def flyover(bbox_min, bbox_max, focal=DEFAULT_FOCAL):
    centre, size, diagonal = _box(bbox_min, bbox_max)
    d = fit_distance(diagonal, focal)
    return [
        _wp((centre[0] - 0.6 * d, centre[1] - 2.0 * d, centre[2] + 1.5 * size), centre, focal),
        _wp((centre[0], centre[1] - 1.3 * d, centre[2] + 0.9 * size), centre, focal),
        _wp((centre[0] + 0.3 * d, centre[1] - 0.8 * d, centre[2] + 0.4 * size), centre, focal),
    ]


PRESETS = {
    "orbit": ("Orbit", "A full turn around the subject, back to the start", orbit),
    "orbit_high": ("Orbit high", "A full turn from above, looking down", orbit_high),
    "orbit_low": ("Orbit low", "A full turn from a hero angle below centre", orbit_low),
    "spiral_in": ("Spiral in", "One turn around the subject while closing in", spiral_in),
    "ellipse_1": ("Ellipse 1", "A wide 2:1 ellipse around the subject", ellipse_1),
    "ellipse_2": ("Ellipse 2", "A tilted ellipse rising over the far side", ellipse_2),
    "ellipse_3": ("Ellipse 3", "A tight ellipse close to the subject", ellipse_3),
    "dolly_in": ("Dolly in", "Straight in, from far away up to the subject", dolly_in),
    "dolly_out": ("Dolly out", "Straight out, from the subject to a wide reveal", dolly_out),
    "truck_left": ("Truck left", "Lateral move to the left, subject kept in frame", truck_left),
    "truck_right": ("Truck right", "Lateral move to the right, subject kept in frame", truck_right),
    "pedestal_up": ("Pedestal up", "Vertical move up in front of the subject", pedestal_up),
    "pedestal_down": ("Pedestal down", "Vertical move down in front of the subject", pedestal_down),
    "zoom_in": ("Zoom in", "Fixed camera, lens from wide to the chosen focal length", zoom_in),
    "crane": ("Crane", "Low in front, rising to look down on the subject", crane),
    "arc_left": ("Arc left", "A quarter turn from the front to the left side", arc_left),
    "arc_right": ("Arc right", "A quarter turn from the front to the right side", arc_right),
    "top_down": ("Top down", "From high above, descending towards the subject", top_down),
    "pan": ("Pan", "Left to right in front of the subject", pan),
    "flyover": ("Flyover", "High and far, swooping down towards the subject", flyover),
}
PRESET_ALIASES = {"push_in": "dolly_in", "pull_back": "dolly_out"}
CLOSED_PRESETS = ("orbit", "orbit_high", "orbit_low", "ellipse_1", "ellipse_2", "ellipse_3")
DEFAULT_PRESET = "orbit"

_PRESET_PATTERNS = (
    ("ellipse_3", r"\bellip(?:se|sis|tical)\w*\s*(?:3|three|iii)\b"),
    ("ellipse_2", r"\bellip(?:se|sis|tical)\w*\s*(?:2|two|ii)\b"),
    ("ellipse_1", r"\bellip(?:se|sis|tical|soid)\w*"),
    ("spiral_in", r"\bspiral(?:s|ing|ling)?\b"),
    ("zoom_in", r"\bzoom(?:s|ing)?\s*in\b"),
    (
        "dolly_out",
        r"\b(pulls?(?:ing)?\s*(?:back|out|away)|zoom(?:s|ing)?\s*out|dolly\s*(?:out|back)|away|reveal(?:s|ing)?|back\s*off)\b",
    ),
    (
        "dolly_in",
        r"\b(push(?:es|ing)?(?:\s*in)?|closer|close[- ]?up|dolly(?:\s*in)?|approach(?:es|ing)?|move\s*in)\b",
    ),
    ("truck_left", r"\b(truck(?:s|ing)?|slide(?:s|ing)?|crab(?:s|bing)?)\s*(?:to\s+the\s+)?left\b"),
    ("truck_right", r"\b(truck(?:s|ing)?|slide(?:s|ing)?|crab(?:s|bing)?)\s*(?:to\s+the\s+)?right\b"),
    ("pedestal_up", r"\b(pedestal|boom)\s*up\b"),
    ("pedestal_down", r"\b(pedestal|boom)\s*down\b"),
    ("arc_left", r"\barc(?:s|ing)?\s*(?:to\s+the\s+)?left\b"),
    ("arc_right", r"\barc(?:s|ing)?\s*(?:to\s+the\s+)?right\b"),
    ("top_down", r"\b(top[- ]?down|overhead|from\s+above|bird'?s?[- ]?eye|straight\s+down)\b"),
    ("orbit_low", r"\b(low[- ]angle|hero\s+angle|from\s+below|worm'?s?[- ]?eye)\b"),
    ("orbit_high", r"\b(high[- ]angle|elevated|looking\s+down\s+(?:while\s+)?(?:orbit|circl|turn))\b"),
    ("crane", r"\b(crane|ris(?:e|es|ing)|lift(?:s|ing)?|ascend(?:s|ing)?|up\s+and\s+over|tilt(?:s|ing)?\s*down)\b"),
    ("flyover", r"\b(fly(?:ing|over|by)?|fly-?over|drone|aerial|swoop(?:s|ing)?|over|bird)\b"),
    ("pan", r"\b(pan(?:s|ning)?|left\s+to\s+right|right\s+to\s+left|sweep(?:s|ing)?|track(?:s|ing)?\s*(?:along|past)?|sideways|lateral)\b"),
    ("orbit", r"\b(orbit(?:s|ing)?|turntable|around|circle(?:s|ing)?|spin(?:s|ning)?|revolv(?:e|es|ing)|360|rotate(?:s)?|turn(?:s)?\s*around)\b"),
)
_DURATION_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(?:s|sec|secs|second|seconds)\b", re.I)
_FOCAL_RE = re.compile(r"(\d+(?:\.\d+)?)\s*mm\b", re.I)
_HOLD_RE = re.compile(
    r"\b(?:hold|pause|wait|stay|linger)\w*\s*(?:for\s*)?(\d+(?:\.\d+)?)\s*(?:s|sec|secs|second|seconds)?\b",
    re.I,
)


def resolve_preset(name: str) -> str:
    name = PRESET_ALIASES.get(name, name)
    return name if name in PRESETS else DEFAULT_PRESET


def plan_from_text(text: str) -> dict:
    """Parse a natural-language camera instruction into {'preset', 'duration', 'focal', 'hold'}."""
    text = (text or "").strip().lower()
    preset = DEFAULT_PRESET
    best_start = None
    for name, pattern in _PRESET_PATTERNS:
        match = re.search(pattern, text)
        if match and (best_start is None or match.start() < best_start):
            best_start, preset = match.start(), name
    hold = 0.0
    hmatch = _HOLD_RE.search(text)
    rest = text
    if hmatch:
        hold = max(0.0, min(float(MAX_DURATION), float(hmatch.group(1))))
        rest = text[: hmatch.start()] + " " + text[hmatch.end() :]
    duration = DEFAULT_DURATION
    match = _DURATION_RE.search(rest)
    if match:
        duration = float(match.group(1))
    if re.search(r"\b(slow|slowly|gentle|gently)\b", rest):
        duration *= 1.5
    if re.search(r"\b(fast|quick|quickly|snappy|rapid)\b", rest):
        duration *= 0.6
    duration = max(MIN_DURATION, min(MAX_DURATION, duration))
    focal = DEFAULT_FOCAL
    match = _FOCAL_RE.search(rest)
    if match:
        focal = max(8.0, min(400.0, float(match.group(1))))
    elif re.search(r"\b(wide|wide[- ]angle)\b", rest):
        focal = 24.0
    elif re.search(r"\b(tele|telephoto|long lens|tight)\b", rest):
        focal = 85.0
    return {
        "preset": preset,
        "duration": round(duration, 3),
        "focal": focal,
        "hold": round(hold, 3),
    }


def subject_bbox(objects=None, use_selection: bool = False):
    """Compute world-space (min, max) bounding box of named objects, selection, or all visible meshes/armatures."""
    scene = bpy.context.scene
    shots = bpy.data.collections.get(SHOTS_COLLECTION)
    excluded = set(shots.objects.keys()) if shots else set()
    candidates = []
    if objects:
        for item in objects:
            obj = bpy.data.objects.get(item) if isinstance(item, str) else item
            if obj is not None:
                candidates.append(obj)
                if obj.type == "ARMATURE":
                    candidates.extend(child for child in obj.children_recursive if child.type == "MESH")
    elif use_selection:
        candidates = [
            o
            for o in bpy.context.view_layer.objects
            if o.select_get() and o.type in ("MESH", "ARMATURE") and o.name not in excluded
        ]
    if not candidates:
        candidates = [
            o
            for o in scene.objects
            if o.type in ("MESH", "ARMATURE") and o.name not in excluded and not o.hide_render
        ]
    points = []
    for obj in candidates:
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    if not points:
        return FALLBACK_BOX
    return (
        tuple(min(p[i] for p in points) for i in range(3)),
        tuple(max(p[i] for p in points) for i in range(3)),
    )


def fcurves_of(datablock):
    """Return all F-curves animating `datablock` across Blender 4.x and Blender 5.x Slotted Action channelbags."""
    anim = getattr(datablock, "animation_data", None)
    if anim is None or anim.action is None:
        return []
    action = anim.action
    if hasattr(action, "fcurves"):
        return list(action.fcurves)
    out = []
    for layer in getattr(action, "layers", ()):
        for strip in layer.strips:
            for bag in getattr(strip, "channelbags", ()):
                out.extend(bag.fcurves)
    return out


def _smooth_datablock(datablock):
    for fcurve in fcurves_of(datablock):
        for key in fcurve.keyframe_points:
            key.interpolation = "BEZIER"
            key.easing = "AUTO"


def _look_at_euler(position, target):
    direction = Vector(target) - Vector(position)
    if direction.length < 1e-6:
        direction = Vector((0.0, 1.0, 0.0))
    return direction.to_track_quat("-Z", "Y").to_euler()


def build_camera_path(
    *,
    preset: str = None,
    description: str = None,
    waypoints: list = None,
    objects: list = None,
    duration: float = None,
    focal: float = None,
    start_frame: int = 1,
    aim_at_subject: bool = True,
    closed_loop: bool = None,
    camera_name: str = CAMERA_NAME,
) -> dict:
    """Build and keyframe an animated 3D shot camera around the target subject(s)."""
    scene = bpy.context.scene
    bpy.context.view_layer.update()

    parsed = plan_from_text(description) if description else {}
    resolved_preset = resolve_preset(preset or parsed.get("preset") or DEFAULT_PRESET)
    resolved_duration = float(duration if duration is not None else parsed.get("duration", DEFAULT_DURATION))
    resolved_focal = float(focal if focal is not None else parsed.get("focal", DEFAULT_FOCAL))
    resolved_hold = float(parsed.get("hold", 0.0))

    bbox = subject_bbox(objects=objects)
    centre = tuple((a + b) / 2.0 for a, b in zip(*bbox, strict=False))

    if waypoints:
        wp_list = [
            Waypoint(
                position=tuple(float(v) for v in wp["position"]),
                rotation_euler=tuple(float(v) for v in wp["rotation_euler"])
                if wp.get("rotation_euler")
                else None,
                look_at=tuple(float(v) for v in wp["look_at"]) if wp.get("look_at") else centre,
                focal=float(wp.get("focal") or resolved_focal),
                hold=float(wp.get("hold") or 0.0),
            )
            for wp in waypoints
        ]
        is_closed = bool(closed_loop)
    else:
        _, _, fn = PRESETS[resolved_preset]
        wp_list = fn(bbox[0], bbox[1], resolved_focal)
        if resolved_hold > 0 and wp_list:
            wp_list[-1].hold = resolved_hold
        is_closed = (
            closed_loop if closed_loop is not None else (resolved_preset in CLOSED_PRESETS)
        )

    if is_closed and len(wp_list) >= 2 and _dist(wp_list[0].position, wp_list[-1].position) >= 1e-9:
        first = wp_list[0]
        wp_list.append(
            Waypoint(
                first.position,
                rotation_euler=first.rotation_euler,
                look_at=first.look_at,
                focal=first.focal,
                hold=0.0,
            )
        )

    coll = bpy.data.collections.get(SHOTS_COLLECTION)
    if coll is None:
        coll = bpy.data.collections.new(SHOTS_COLLECTION)
    if coll.name not in scene.collection.children:
        scene.collection.children.link(coll)

    # Clear old markers
    for old_m in list(coll.objects):
        if old_m.type == "CAMERA" and PROP_INDEX in old_m:
            m_data = old_m.data
            bpy.data.objects.remove(old_m, do_unlink=True)
            if m_data and m_data.users == 0:
                bpy.data.cameras.remove(m_data)

    for idx, wp in enumerate(wp_list, start=1):
        m_cam = bpy.data.cameras.new(f"{MARKER_PREFIX}{idx}")
        m_cam.lens = float(wp.focal)
        m_cam.display_size = 0.35
        m_obj = bpy.data.objects.new(f"{MARKER_PREFIX}{idx}", m_cam)
        m_obj.location = Vector(wp.position)
        m_obj.rotation_euler = (
            Euler(wp.rotation_euler)
            if wp.rotation_euler is not None
            else _look_at_euler(wp.position, wp.look_at or centre)
        )
        m_obj.hide_render = True
        m_obj[PROP_INDEX] = idx
        m_obj[PROP_FOCAL] = float(wp.focal)
        m_obj[PROP_HOLD] = float(wp.hold)
        coll.objects.link(m_obj)

    fps = scene.render.fps / (scene.render.fps_base or 1.0)
    schedule = [
        (frame + int(start_frame) - 1, index)
        for frame, index in frame_schedule(wp_list, resolved_duration, fps)
    ]

    cam = bpy.data.objects.get(camera_name)
    if cam is None or cam.type != "CAMERA":
        cam = bpy.data.objects.new(camera_name, bpy.data.cameras.new(camera_name))
    if cam.name not in coll.objects:
        coll.objects.link(cam)
    cam.animation_data_clear()
    cam.data.animation_data_clear()
    for c in list(cam.constraints):
        if c.name == AIM_CONSTRAINT:
            cam.constraints.remove(c)

    focals = {round(wp.focal, 3) for wp in wp_list}
    for frame, index in schedule:
        wp = wp_list[index]
        cam.location = Vector(wp.position)
        cam.keyframe_insert("location", frame=frame)
        if not aim_at_subject:
            cam.rotation_euler = (
                Euler(wp.rotation_euler)
                if wp.rotation_euler is not None
                else _look_at_euler(wp.position, wp.look_at or centre)
            )
            cam.keyframe_insert("rotation_euler", frame=frame)
        cam.data.lens = float(wp.focal)
        if len(focals) > 1:
            cam.data.keyframe_insert("lens", frame=frame)

    if aim_at_subject:
        target = bpy.data.objects.get(TARGET_NAME)
        if target is None:
            target = bpy.data.objects.new(TARGET_NAME, None)
            target.empty_display_type = "PLAIN_AXES"
            target.empty_display_size = 0.25
        if target.name not in coll.objects:
            coll.objects.link(target)
        target.location = Vector(centre)
        target.hide_render = True
        constraint = cam.constraints.new("TRACK_TO")
        constraint.name = AIM_CONSTRAINT
        constraint.target = target
        constraint.track_axis = "TRACK_NEGATIVE_Z"
        constraint.up_axis = "UP_Y"

    _smooth_datablock(cam)
    _smooth_datablock(cam.data)
    last_frame = int(schedule[-1][0]) if schedule else int(start_frame)
    scene.camera = cam
    scene.frame_start = int(start_frame)
    scene.frame_end = last_frame
    scene.frame_set(int(start_frame))
    return {
        "camera": cam.name,
        "preset": resolved_preset,
        "duration": resolved_duration,
        "focal": resolved_focal,
        "keyframes": len(schedule),
        "frame_start": int(start_frame),
        "frame_end": last_frame,
        "bbox": bbox,
    }


# ==============================================================================
# 3. MULTI-VIEW & MULTI-FRAME CONTACT SHEET QA ENGINE (PURE STDLIB PNG COMPOSER)
# ==============================================================================

_GAP = 4
_BG_RGB = (24, 24, 24)
_LABEL_TEXT, _LABEL_BACK = (255, 255, 255), (0, 0, 0)
_FONT_5X7 = {
    " ": (0, 0, 0, 0, 0, 0, 0),
    "-": (0, 0, 0, 31, 0, 0, 0),
    "/": (1, 1, 2, 4, 8, 16, 16),
    ".": (0, 0, 0, 0, 0, 12, 12),
    ":": (0, 12, 12, 0, 12, 12, 0),
    "_": (0, 0, 0, 0, 0, 0, 31),
    "0": (14, 17, 19, 21, 25, 17, 14),
    "1": (4, 12, 4, 4, 4, 4, 14),
    "2": (14, 17, 1, 2, 4, 8, 31),
    "3": (31, 2, 4, 2, 1, 17, 14),
    "4": (2, 6, 10, 18, 31, 2, 2),
    "5": (31, 16, 30, 1, 1, 17, 14),
    "6": (6, 8, 16, 30, 17, 17, 14),
    "7": (31, 1, 2, 4, 8, 8, 8),
    "8": (14, 17, 17, 14, 17, 17, 14),
    "9": (14, 17, 17, 15, 1, 2, 12),
    "A": (14, 17, 17, 31, 17, 17, 17),
    "B": (30, 17, 17, 30, 17, 17, 30),
    "C": (14, 17, 16, 16, 16, 17, 14),
    "D": (28, 18, 17, 17, 17, 18, 28),
    "E": (31, 16, 16, 30, 16, 16, 31),
    "F": (31, 16, 16, 30, 16, 16, 16),
    "G": (14, 17, 16, 23, 17, 17, 15),
    "H": (17, 17, 17, 31, 17, 17, 17),
    "I": (14, 4, 4, 4, 4, 4, 14),
    "J": (7, 2, 2, 2, 2, 18, 12),
    "K": (17, 18, 20, 24, 20, 18, 17),
    "L": (16, 16, 16, 16, 16, 16, 31),
    "M": (17, 27, 21, 21, 17, 17, 17),
    "N": (17, 17, 25, 21, 19, 17, 17),
    "O": (14, 17, 17, 17, 17, 17, 14),
    "P": (30, 17, 17, 30, 16, 16, 16),
    "Q": (14, 17, 17, 17, 21, 18, 13),
    "R": (30, 17, 17, 30, 20, 18, 17),
    "S": (15, 16, 16, 14, 1, 1, 30),
    "T": (31, 4, 4, 4, 4, 4, 4),
    "U": (17, 17, 17, 17, 17, 17, 14),
    "V": (17, 17, 17, 17, 17, 10, 4),
    "W": (17, 17, 17, 21, 21, 21, 10),
    "X": (17, 17, 10, 4, 10, 17, 17),
    "Y": (17, 17, 10, 4, 4, 4, 4),
    "Z": (31, 1, 2, 4, 8, 16, 31),
}

CAPTURE_ANGLES = {
    "front": ((0.0, -1.0, 0.0), "FRONT", True),
    "back": ((0.0, 1.0, 0.0), "BACK", True),
    "left": ((-1.0, 0.0, 0.0), "LEFT", True),
    "right": ((1.0, 0.0, 0.0), "RIGHT", True),
    "top": ((0.0, 0.0, 1.0), "TOP", True),
    "three_quarter": ((1.0, -1.0, 0.8), "3/4", False),
}


@dataclass(frozen=True)
class SheetLayout:
    columns: int
    rows: int
    tile_width: int
    tile_height: int

    @property
    def width(self):
        return self.columns * self.tile_width + (self.columns + 1) * _GAP

    @property
    def height(self):
        return self.rows * self.tile_height + (self.rows + 1) * _GAP

    def origin(self, index: int):
        row, col = divmod(index, self.columns)
        return (
            _GAP + col * (self.tile_width + _GAP),
            _GAP + row * (self.tile_height + _GAP),
        )


def compute_sheet_layout(count: int, max_size: int, aspect: float) -> SheetLayout:
    columns = math.ceil(math.sqrt(count))
    rows = math.ceil(count / columns)
    by_width = (max_size - (columns + 1) * _GAP) / columns
    by_height = (max_size - (rows + 1) * _GAP) / rows * aspect
    tile_width = max(16, math.floor(min(by_width, by_height)))
    tile_height = max(16, math.floor(tile_width / aspect))
    return SheetLayout(columns, rows, tile_width, tile_height)


def _read_targa(data: bytes):
    id_length, colormap_type, image_type = data[0], data[1], data[2]
    width, height = struct.unpack_from("<HH", data, 12)
    depth, descriptor = data[16], data[17]
    channels = depth // 8
    start = 18 + id_length
    pixels = data[start : start + width * height * channels]
    rgb = bytearray(width * height * 3)
    rgb[0::3], rgb[1::3], rgb[2::3] = (
        pixels[2::channels],
        pixels[1::channels],
        pixels[0::channels],
    )
    if not (descriptor & 0x20):
        stride = width * 3
        rgb = b"".join(rgb[row * stride : (row + 1) * stride] for row in reversed(range(height)))
    return width, height, bytes(rgb)


def _encode_png(width: int, height: int, rgb_bytes: bytes) -> bytes:
    stride = width * 3
    raw = b"".join(b"\x00" + rgb_bytes[y * stride : (y + 1) * stride] for y in range(height))

    def chunk(tag: bytes, body: bytes) -> bytes:
        return (
            struct.pack(">I", len(body))
            + tag
            + body
            + struct.pack(">I", zlib.crc32(tag + body) & 0xFFFFFFFF)
        )

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw, 6)) + chunk(b"IEND", b"")


def compose_contact_sheet_png(grid: SheetLayout, tga_tiles: list[bytes], labels: list[str]) -> bytes:
    width, height = grid.width, grid.height
    canvas = bytearray(bytes(_BG_RGB) * (width * height))
    stride = width * 3
    scale = 2 if min(grid.tile_width, grid.tile_height) >= 160 else 1

    for idx, (tga, label) in enumerate(zip(tga_tiles, labels, strict=False)):
        tw, th, rgb = _read_targa(tga)
        ox, oy = grid.origin(idx)
        t_stride = tw * 3
        for row in range(min(th, grid.tile_height)):
            dst = (oy + row) * stride + ox * 3
            src = row * t_stride
            canvas[dst : dst + tw * 3] = rgb[src : src + tw * 3]

        text = str(label or "").upper()
        pad = 3 * scale
        box_w = min(grid.tile_width, len(text) * 6 * scale - scale + 2 * pad)
        box_h = min(grid.tile_height, 7 * scale + 2 * pad)
        for ry in range(oy, oy + box_h):
            start = ry * stride + ox * 3
            canvas[start : start + box_w * 3] = bytes(_LABEL_BACK) * box_w

        cx = ox + pad
        cy = oy + pad
        for ch in text:
            glyph = _FONT_5X7.get(ch, _FONT_5X7[" "])
            for gy, bits in enumerate(glyph):
                for gx in range(5):
                    if bits & (1 << (4 - gx)):
                        for sy in range(scale):
                            for sx in range(scale):
                                px, py = cx + gx * scale + sx, cy + gy * scale + sy
                                if px < ox + grid.tile_width and py < oy + grid.tile_height:
                                    p = py * stride + px * 3
                                    canvas[p : p + 3] = bytes(_LABEL_TEXT)
            cx += 6 * scale
    return _encode_png(width, height, bytes(canvas))


def capture_views_sheet(
    out_png_path: str = None,
    *,
    mode: str = "angles",
    angles: tuple = ("front", "right", "top", "three_quarter"),
    objects: list = None,
    frames: list = None,
    frame_count: int = 4,
    max_size: int = 1280,
    engine: str = "BLENDER_WORKBENCH",
) -> dict:
    """Render multiple diagnostic views (angles or timeline frames) into a single labeled PNG contact sheet."""
    scene = bpy.context.scene
    bpy.context.view_layer.update()
    render = scene.render

    if mode == "angles":
        views = [a for a in angles if a in CAPTURE_ANGLES] or ["front", "right", "top", "three_quarter"]
        aspect = 1.0
    else:
        aspect = (render.resolution_x * render.pixel_aspect_x) / max(
            1.0, render.resolution_y * render.pixel_aspect_y
        )
        if frames:
            views = [int(f) for f in frames]
        else:
            start, end = scene.frame_start, scene.frame_end
            views = (
                [start]
                if frame_count <= 1 or end <= start
                else [round(start + (end - start) * i / (frame_count - 1)) for i in range(frame_count)]
            )

    grid = compute_sheet_layout(len(views), max_size, aspect)
    orig_frame = scene.frame_current
    orig_engine = render.engine
    orig_res = (render.resolution_x, render.resolution_y, render.resolution_percentage)
    orig_filepath = render.filepath
    orig_format = render.image_settings.file_format
    orig_color_mode = render.image_settings.color_mode
    orig_cam = scene.camera

    tiles, labels = [], []
    temp_cam = None
    with tempfile.TemporaryDirectory(prefix="sven-contact-") as tmp_dir:
        try:
            render.engine = engine
            render.resolution_x = grid.tile_width
            render.resolution_y = grid.tile_height
            render.resolution_percentage = 100
            render.image_settings.file_format = "TARGA_RAW"
            render.image_settings.color_mode = "RGB"
            if engine == "BLENDER_WORKBENCH":
                scene.display.shading.light = "STUDIO"
                scene.display.shading.color_type = "MATERIAL"
                scene.display.shading.show_object_outline = True

            if mode == "angles":
                lo, hi = subject_bbox(objects=objects)
                center = (Vector(lo) + Vector(hi)) / 2.0
                radius = max((Vector(hi) - Vector(lo)).length / 2.0, 0.25)
                corners = [
                    Vector((x, y, z))
                    for x in (lo[0], hi[0])
                    for y in (lo[1], hi[1])
                    for z in (lo[2], hi[2])
                ]
                cam_data = bpy.data.cameras.new("Sven_QA_Capture_Cam")
                temp_cam = bpy.data.objects.new("Sven_QA_Capture_Cam", cam_data)
                scene.collection.objects.link(temp_cam)
                scene.camera = temp_cam

                for idx, name in enumerate(views):
                    direction_t, label, ortho = CAPTURE_ANGLES[name]
                    direction = Vector(direction_t).normalized()
                    rotation = (
                        Quaternion() if name == "top" else (-direction).to_track_quat("-Z", "Y")
                    )
                    if ortho:
                        axes = (rotation @ Vector((1, 0, 0)), rotation @ Vector((0, 1, 0)))
                        extent = max(abs((p - center).dot(a)) for p in corners for a in axes)
                        cam_data.type = "ORTHO"
                        cam_data.ortho_scale = max(extent * 2.2, radius * 0.2)
                        distance = radius * 3.0
                    else:
                        fov = 0.698
                        cam_data.type, cam_data.angle = "PERSP", fov
                        distance = radius / math.sin(fov / 2.0) * 1.05
                    cam_data.clip_start = max(distance - radius * 1.5, radius * 0.001)
                    cam_data.clip_end = distance + radius * 1.5
                    temp_cam.location = center + direction * distance
                    temp_cam.rotation_euler = rotation.to_euler()
                    tile_path = os.path.join(tmp_dir, f"{idx}.tga")
                    render.filepath = tile_path
                    bpy.ops.render.render(write_still=True, scene=scene.name)
                    with open(tile_path, "rb") as f:
                        tiles.append(f.read())
                    labels.append(label)
            else:
                for idx, fnum in enumerate(views):
                    scene.frame_set(fnum)
                    tile_path = os.path.join(tmp_dir, f"{idx}.tga")
                    render.filepath = tile_path
                    bpy.ops.render.render(write_still=True, scene=scene.name)
                    with open(tile_path, "rb") as f:
                        tiles.append(f.read())
                    labels.append(f"FRAME {fnum}")
        finally:
            render.engine = orig_engine
            render.resolution_x, render.resolution_y, render.resolution_percentage = orig_res
            render.filepath = orig_filepath
            render.image_settings.file_format = orig_format
            with contextlib.suppress(TypeError):
                render.image_settings.color_mode = orig_color_mode
            scene.camera = orig_cam
            if temp_cam is not None:
                c_data = temp_cam.data
                bpy.data.objects.remove(temp_cam, do_unlink=True)
                bpy.data.cameras.remove(c_data)
            scene.frame_set(orig_frame)

    png_bytes = compose_contact_sheet_png(grid, tiles, labels)
    if out_png_path:
        os.makedirs(os.path.dirname(os.path.abspath(out_png_path)), exist_ok=True)
        with open(out_png_path, "wb") as f:
            f.write(png_bytes)

    return {
        "mode": mode,
        "tiles": labels,
        "layout": f"{grid.columns}x{grid.rows}",
        "size": [grid.width, grid.height],
        "out_png_path": out_png_path,
    }


# ==============================================================================
# 4. UNIVERSAL 5-FAMILY HUMANOID SKELETON DETECTOR & MOTION RETARGETER
# ==============================================================================

HUMANOID_SLOTS = (
    "hips",
    "spine",
    "chest",
    "neck",
    "head",
    "l_arm",
    "l_forearm",
    "l_hand",
    "r_arm",
    "r_forearm",
    "r_hand",
    "l_upleg",
    "l_leg",
    "l_foot",
    "r_upleg",
    "r_leg",
    "r_foot",
)

HUMANOID_FAMILIES = {
    "roblox_r15": (
        "Roblox R15",
        (
            "LowerTorso",
            "UpperTorso",
            "UpperTorso",
            "Head",
            "Head",
            "LeftUpperArm",
            "LeftLowerArm",
            "LeftHand",
            "RightUpperArm",
            "RightLowerArm",
            "RightHand",
            "LeftUpperLeg",
            "LeftLowerLeg",
            "LeftFoot",
            "RightUpperLeg",
            "RightLowerLeg",
            "RightFoot",
        ),
    ),
    "mixamo": (
        "Mixamo",
        (
            "Hips",
            "Spine",
            "Spine2",
            "Neck",
            "Head",
            "LeftArm",
            "LeftForeArm",
            "LeftHand",
            "RightArm",
            "RightForeArm",
            "RightHand",
            "LeftUpLeg",
            "LeftLeg",
            "LeftFoot",
            "RightUpLeg",
            "RightLeg",
            "RightFoot",
        ),
    ),
    "meshy": (
        "Meshy",
        (
            "Hips",
            "Spine02",
            "Spine",
            "neck",
            "Head",
            "LeftArm",
            "LeftForeArm",
            "LeftHand",
            "RightArm",
            "RightForeArm",
            "RightHand",
            "LeftUpLeg",
            "LeftLeg",
            "LeftFoot",
            "RightUpLeg",
            "RightLeg",
            "RightFoot",
        ),
    ),
    "smpl": (
        "SMPL",
        (
            "Pelvis",
            "Spine1",
            "Spine3",
            "Neck",
            "Head",
            "L_Shoulder",
            "L_Elbow",
            "L_Wrist",
            "R_Shoulder",
            "R_Elbow",
            "R_Wrist",
            "L_Hip",
            "L_Knee",
            "L_Ankle",
            "R_Hip",
            "R_Knee",
            "R_Ankle",
        ),
    ),
    "unreal": (
        "Unreal",
        (
            "pelvis",
            "spine_01",
            "spine_05",
            "neck_01",
            "head",
            "upperarm_l",
            "lowerarm_l",
            "hand_l",
            "upperarm_r",
            "lowerarm_r",
            "hand_r",
            "thigh_l",
            "calf_l",
            "foot_l",
            "thigh_r",
            "calf_r",
            "foot_r",
        ),
    ),
}


def detect_humanoid_family(armature_obj) -> tuple[str, dict] | None:
    """Detect whether `armature_obj` matches Roblox R15, Mixamo, Meshy, SMPL, or Unreal."""
    if armature_obj is None or armature_obj.type != "ARMATURE":
        return None
    short_map = {}
    for b in armature_obj.data.bones:
        short = b.name.rsplit(":", 1)[-1]
        short_map[short] = b.name
    for family, (_label, wanted) in HUMANOID_FAMILIES.items():
        mapping = {slot: short_map.get(bone) for slot, bone in zip(HUMANOID_SLOTS, wanted, strict=False)}
        if None not in mapping.values():
            return family, mapping
    return None


def retarget_humanoid_action(
    source_arm,
    dest_arm,
    *,
    frame_start: int = None,
    frame_end: int = None,
    action_name: str = "Retargeted_Action",
) -> dict:
    """Retarget an active animation from `source_arm` to `dest_arm` with leg scaling & floor pinning."""
    if isinstance(source_arm, str):
        source_arm = bpy.data.objects.get(source_arm)
    if isinstance(dest_arm, str):
        dest_arm = bpy.data.objects.get(dest_arm)
    src_det = detect_humanoid_family(source_arm)
    dst_det = detect_humanoid_family(dest_arm)
    if not src_det or not dst_det:
        raise ValueError(f"Could not detect humanoid rigs: source={src_det}, dest={dst_det}")

    src_family, src_map = src_det
    dst_family, dst_map = dst_det
    scene = bpy.context.scene
    f_start = int(frame_start if frame_start is not None else scene.frame_start)
    f_end = int(frame_end if frame_end is not None else scene.frame_end)

    def _leg_len(arm, bmap):
        hips = arm.matrix_world @ arm.data.bones[bmap["hips"]].head_local
        foot_l = arm.matrix_world @ arm.data.bones[bmap["l_foot"]].head_local
        foot_r = arm.matrix_world @ arm.data.bones[bmap["r_foot"]].head_local
        return max(0.05, ((hips - foot_l).length + (hips - foot_r).length) / 2.0)

    leg_ratio = _leg_len(dest_arm, dst_map) / _leg_len(source_arm, src_map)

    # Rest rotation offset per mapped bone in world space
    rest_offsets = {}
    used_dst_bones = set()
    slot_pairs = []
    for slot in HUMANOID_SLOTS:
        sb_name = src_map[slot]
        db_name = dst_map[slot]
        if db_name in used_dst_bones:
            continue
        used_dst_bones.add(db_name)
        slot_pairs.append((slot, sb_name, db_name))
        s_rest = (source_arm.matrix_world @ source_arm.data.bones[sb_name].matrix_local).to_quaternion()
        d_rest = (dest_arm.matrix_world @ dest_arm.data.bones[db_name].matrix_local).to_quaternion()
        rest_offsets[slot] = s_rest.inverted() @ d_rest

    src_hips_rest = source_arm.matrix_world @ source_arm.data.bones[src_map["hips"]].head_local
    dst_hips_rest = dest_arm.matrix_world @ dest_arm.data.bones[dst_map["hips"]].head_local
    dst_world_inv = dest_arm.matrix_world.inverted_safe()

    for f in range(f_start, f_end + 1):
        scene.frame_set(f)
        bpy.context.view_layer.update()
        for slot, sb_name, db_name in slot_pairs:
            s_pbone = source_arm.pose.bones[sb_name]
            d_pbone = dest_arm.pose.bones[db_name]
            s_world_q = (source_arm.matrix_world @ s_pbone.matrix).to_quaternion()
            target_world_q = s_world_q @ rest_offsets[slot]
            parent_world = (
                dest_arm.matrix_world @ d_pbone.parent.matrix
                if d_pbone.parent
                else dest_arm.matrix_world
            )
            local_rest = (
                d_pbone.parent.bone.matrix_local.inverted() @ d_pbone.bone.matrix_local
                if d_pbone.parent
                else d_pbone.bone.matrix_local
            )
            basis_q = (parent_world @ local_rest).to_quaternion().inverted() @ target_world_q
            if d_pbone.rotation_mode == "QUATERNION":
                d_pbone.rotation_quaternion = basis_q
                d_pbone.keyframe_insert("rotation_quaternion", frame=f)
            else:
                d_pbone.rotation_euler = basis_q.to_euler(d_pbone.rotation_mode)
                d_pbone.keyframe_insert("rotation_euler", frame=f)

            if slot == "hips":
                s_hips_now = (source_arm.matrix_world @ s_pbone.matrix).translation
                delta_world = (s_hips_now - src_hips_rest) * leg_ratio
                target_hips_world = dst_hips_rest + delta_world
                rest_mat = dest_arm.matrix_world @ d_pbone.bone.matrix_local
                d_pbone.location = rest_mat.inverted_safe() @ target_hips_world
                d_pbone.keyframe_insert("location", frame=f)

    if dest_arm.animation_data and dest_arm.animation_data.action:
        dest_arm.animation_data.action.name = action_name

    return {
        "source_family": src_family,
        "dest_family": dst_family,
        "leg_ratio": round(leg_ratio, 4),
        "frame_range": [f_start, f_end],
        "action": action_name,
    }


# ==============================================================================
# 5. CLI & HEADLESS RUNNER ENTRY POINT
# ==============================================================================


def run(**kwargs) -> dict:
    action = kwargs.get("action", "capture_views")
    if action == "blockout":
        plan_path = kwargs.get("plan_file")
        if plan_path and os.path.isfile(plan_path):
            with open(plan_path, "r", encoding="utf-8") as f:
                plan_data = f.read()
        else:
            plan_data = kwargs.get("plan_json", "[]")
        res = build_blockout_scene(
            plan_data,
            dress=bool(kwargs.get("dress", True)),
            bevel_width=float(kwargs.get("bevel_width", 0.015)),
        )
    elif action == "camera_path":
        res = build_camera_path(
            preset=kwargs.get("preset"),
            description=kwargs.get("description"),
            objects=kwargs.get("objects"),
            duration=kwargs.get("duration"),
            focal=kwargs.get("focal"),
        )
    elif action == "capture_views":
        res = capture_views_sheet(
            out_png_path=kwargs.get("out_png"),
            mode=kwargs.get("mode", "angles"),
            objects=kwargs.get("objects"),
            frame_count=int(kwargs.get("frame_count", 4)),
            max_size=int(kwargs.get("max_size", 1280)),
        )
    elif action == "retarget":
        res = retarget_humanoid_action(
            source_arm=kwargs.get("source"),
            dest_arm=kwargs.get("dest"),
            action_name=kwargs.get("action_name", "Retargeted_Action"),
        )
    else:
        raise ValueError(f"Unknown action: {action}")

    save_path = kwargs.get("save")
    if save_path and HAS_BPY:
        os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(save_path))
        res["saved_blend"] = os.path.abspath(save_path)
    return res


def main():
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser(description="Sven Core Automated Blender 5.3 Director Engine")
    parser.add_argument("--action", choices=("blockout", "camera_path", "capture_views", "retarget"), default="capture_views")
    parser.add_argument("--plan-file", help="Path to blockout JSON file")
    parser.add_argument("--plan-json", help="Inline blockout JSON array")
    parser.add_argument("--preset", help="Camera move preset (orbit, dolly_in, crane, ...)")
    parser.add_argument("--description", help="Natural language camera move description")
    parser.add_argument("--duration", type=float, help="Camera move duration in seconds")
    parser.add_argument("--focal", type=float, help="Camera focal length in mm")
    parser.add_argument("--mode", choices=("angles", "frames"), default="angles")
    parser.add_argument("--objects", nargs="*", help="Target object names")
    parser.add_argument("--out-png", help="Output PNG path for capture_views")
    parser.add_argument("--source", help="Source armature name for retarget")
    parser.add_argument("--dest", help="Destination armature name for retarget")
    parser.add_argument("--save", help="Save .blend file after operation")
    args = parser.parse_args(argv)
    result = run(
        action=args.action,
        plan_file=args.plan_file,
        plan_json=args.plan_json,
        preset=args.preset,
        description=args.description,
        duration=args.duration,
        focal=args.focal,
        mode=args.mode,
        objects=args.objects,
        out_png=args.out_png,
        source=args.source,
        dest=args.dest,
        save=args.save,
    )
    print("@@JSON@@" + json.dumps(result))


if __name__ == "__main__":
    main()

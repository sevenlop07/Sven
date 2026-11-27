"""Compact token-efficient scene inspection (headless & live parity with mcp-for-blender get_scene_info).

Returns one header summary plus one concise line per object with requested fields:
  placement: location, size, ground (on_ground / floating +Xm / sunk -Xm), rotation, scale, parent
  contents:  children, hidden, details (faces/bones/light power), materials, modifiers, animation
  health:    topology (quads/tris/ngons/non_manifold/boundary/loose), weights (unweighted/max_inf)

Usage:
  blender -b file.blend -P scene_inspect.py -- [--query chair] [--root Hero]
      [--fields location size ground materials] [--limit 40] [--ground-z 0.0]
  Python / Live MCP:
      import scene_inspect; print(scene_inspect.run(fields=["location", "size", "ground"])["summary"])
"""
import math
import os
import sys

import bmesh
import bpy
from mathutils import Vector

sys.path.insert(0, os.path.dirname(__file__))
import _bpyx as bx  # noqa: E402

DEFAULT_FIELDS = ("location", "size", "ground", "children", "hidden")
ALL_FIELDS = (
    "location", "size", "ground", "rotation", "scale", "parent",
    "children", "hidden", "details", "materials", "modifiers", "animation",
    "topology", "weights",
)


def _world_aabb(ob):
    if ob.bound_box and ob.type in ("MESH", "CURVE", "FONT", "SURFACE", "CURVES", "VOLUME", "ARMATURE"):
        pts = [ob.matrix_world @ Vector(c) for c in ob.bound_box]
        lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
        hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
        return lo, hi
    p = ob.matrix_world.translation.copy()
    return p, p


def _ground_status(lo_z, ground_z=0.0, tol=0.01):
    delta = lo_z - ground_z
    if abs(delta) <= tol:
        return "on_ground", round(delta, 4)
    if delta > 0:
        return f"floating(+{delta:.3f}m)", round(delta, 4)
    return f"sunk({delta:.3f}m)", round(delta, 4)


def _topology_stats(ob):
    if ob.type != "MESH" or ob.data is None:
        return None
    bm = bmesh.new()
    try:
        bm.from_mesh(ob.data)
        quads = sum(1 for f in bm.faces if len(f.verts) == 4)
        tris = sum(1 for f in bm.faces if len(f.verts) == 3)
        ngons = sum(1 for f in bm.faces if len(f.verts) > 4)
        non_manifold = sum(1 for e in bm.edges if not e.is_manifold and not e.is_boundary)
        boundary = sum(1 for e in bm.edges if e.is_boundary)
        loose = sum(1 for v in bm.verts if not v.link_edges)
        return {
            "verts": len(bm.verts),
            "faces": len(bm.faces),
            "quads": quads,
            "tris": tris,
            "ngons": ngons,
            "non_manifold": non_manifold,
            "boundary": boundary,
            "loose": loose,
        }
    finally:
        bm.free()


def _weight_stats(ob):
    if ob.type != "MESH" or ob.data is None:
        return None
    arm = ob.parent if (ob.parent and ob.parent.type == "ARMATURE") else None
    if not arm:
        for m in ob.modifiers:
            if m.type == "ARMATURE" and m.object:
                arm = m.object
                break
    if not arm and not ob.vertex_groups:
        return None
    deform_names = {b.name for b in arm.data.bones if b.use_deform} if arm else set()
    deform_indices = {
        vg.index for vg in ob.vertex_groups
        if (not deform_names or vg.name in deform_names)
    }
    unweighted = 0
    over4 = 0
    max_inf = 0
    for v in ob.data.vertices:
        infs = [g for g in v.groups if g.weight > 1e-4 and (not deform_indices or g.group in deform_indices)]
        c = len(infs)
        if c == 0:
            unweighted += 1
        if c > 4:
            over4 += 1
        if c > max_inf:
            max_inf = c
    return {
        "armature": arm.name if arm else None,
        "vgroups": len(ob.vertex_groups),
        "unweighted": unweighted,
        "over4": over4,
        "max_inf": max_inf,
    }


def _collect_targets(sc, query=None, root=None):
    if root:
        if root not in bpy.data.objects:
            raise KeyError(f"root object not found: {root}")
        r_ob = bpy.data.objects[root]
        out = []

        def walk(o, depth):
            out.append((o, depth))
            for ch in sorted(o.children, key=lambda c: c.name):
                walk(ch, depth + 1)

        walk(r_ob, 0)
        return out

    objs = sorted(sc.objects, key=lambda o: o.name)
    if query:
        q = query.lower()
        return [(o, 0) for o in objs if q in o.name.lower()]
    # Top-level objects by default for compact hierarchy overview
    return [(o, 0) for o in objs if o.parent is None]


def run(query=None, root=None, fields=None, limit=40, ground_z=0.0, ground_tol=0.01, **_):
    sc = bpy.context.scene
    bpy.context.view_layer.update()
    fset = tuple(fields) if fields else DEFAULT_FIELDS
    bad = [f for f in fset if f not in ALL_FIELDS]
    if bad:
        raise ValueError(f"unknown fields: {bad}; valid: {list(ALL_FIELDS)}")

    counts = {}
    for o in sc.objects:
        counts[o.type] = counts.get(o.type, 0) + 1

    active = bpy.context.view_layer.objects.active
    mode = active.mode if active else "OBJECT"
    header = (
        f"Blender {bpy.app.version_string} | engine={sc.render.engine} | "
        f"frame={sc.frame_current} ({sc.frame_start}-{sc.frame_end}@{sc.render.fps}fps) | "
        f"total={len(sc.objects)} {counts} | active={active.name if active else None} ({mode})"
    )

    targets = _collect_targets(sc, query=query, root=root)
    truncated = len(targets) > limit
    targets = targets[:limit]

    items = []
    lines = [header]

    for ob, depth in targets:
        lo, hi = _world_aabb(ob)
        size = hi - lo
        loc = ob.matrix_world.translation
        entry = {"name": ob.name, "type": ob.type, "depth": depth}
        parts = [f"{'  ' * depth}{ob.name} [{ob.type}]"]

        if "location" in fset:
            entry["location"] = bx.r(loc, 3)
            parts.append(f"loc=({loc.x:.2f},{loc.y:.2f},{loc.z:.2f})")
        if "size" in fset:
            entry["size"] = bx.r(size, 3)
            parts.append(f"size=({size.x:.2f},{size.y:.2f},{size.z:.2f})")
        if "ground" in fset:
            g_label, g_delta = _ground_status(lo.z, ground_z=ground_z, tol=ground_tol)
            entry["ground"] = g_label
            entry["ground_delta_m"] = g_delta
            parts.append(f"ground={g_label}")
        if "rotation" in fset:
            deg = [round(math.degrees(a), 1) for a in ob.matrix_world.to_euler()]
            entry["rotation_deg"] = deg
            parts.append(f"rot={tuple(deg)}")
        if "scale" in fset:
            sc_v = bx.r(ob.scale, 3)
            entry["scale"] = sc_v
            parts.append(f"scale={tuple(sc_v)}")
        if "parent" in fset and ob.parent:
            entry["parent"] = ob.parent.name
            parts.append(f"parent={ob.parent.name}")
        if "children" in fset and ob.children:
            entry["children"] = len(ob.children)
            parts.append(f"children={len(ob.children)}")
        if "hidden" in fset and (ob.hide_viewport or ob.hide_render):
            entry["hidden"] = {"viewport": ob.hide_viewport, "render": ob.hide_render}
            parts.append(f"hidden(vp={int(ob.hide_viewport)},ren={int(ob.hide_render)})")
        if "details" in fset:
            if ob.type == "MESH" and ob.data:
                det = f"faces={len(ob.data.polygons)},verts={len(ob.data.vertices)}"
            elif ob.type == "ARMATURE" and ob.data:
                det = f"bones={len(ob.data.bones)}"
            elif ob.type == "LIGHT" and ob.data:
                det = f"light={ob.data.type},energy={ob.data.energy:.1f}"
            elif ob.type == "CAMERA" and ob.data:
                det = f"lens={ob.data.lens:.1f}mm"
            else:
                det = ob.type.lower()
            entry["details"] = det
            parts.append(det)
        if "materials" in fset and hasattr(ob, "material_slots") and ob.material_slots:
            mats = [s.material.name if s.material else "<empty>" for s in ob.material_slots]
            entry["materials"] = mats
            parts.append(f"mats={mats}")
        if "modifiers" in fset and ob.modifiers:
            mods = [f"{m.name}:{m.type}" for m in ob.modifiers]
            entry["modifiers"] = mods
            parts.append(f"mods={mods}")
        if "animation" in fset and ob.animation_data and ob.animation_data.action:
            act = ob.animation_data.action
            entry["animation"] = act.name
            parts.append(f"action={act.name}")
        if "topology" in fset:
            topo = _topology_stats(ob)
            if topo:
                entry["topology"] = topo
                parts.append(
                    f"topo(q={topo['quads']},t={topo['tris']},ng={topo['ngons']},"
                    f"nm={topo['non_manifold']},bd={topo['boundary']},ls={topo['loose']})"
                )
        if "weights" in fset:
            ws = _weight_stats(ob)
            if ws:
                entry["weights"] = ws
                parts.append(
                    f"weights(arm={ws['armature']},unw={ws['unweighted']},>4={ws['over4']},max={ws['max_inf']})"
                )

        items.append(entry)
        lines.append(" | ".join(parts))

    if truncated:
        lines.append(f"... truncated to limit={limit} (pass --limit or --query to narrow)")

    return {
        "ok": True,
        "header": header,
        "count": len(items),
        "truncated": truncated,
        "items": items,
        "summary": "\n".join(lines),
    }


if __name__ == "__main__":
    p = bx.parser(__doc__)
    p.add_argument("--query", default=None, help="filter objects whose name contains text")
    p.add_argument("--root", default=None, help="inspect hierarchy under this object")
    p.add_argument("--fields", nargs="*", default=None, choices=list(ALL_FIELDS))
    p.add_argument("--limit", type=int, default=40)
    p.add_argument("--ground-z", type=float, default=0.0)
    p.add_argument("--ground-tol", type=float, default=0.01)
    bx.cli(run, p)

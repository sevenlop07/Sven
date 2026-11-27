"""Render a multi-angle or multi-frame review contact sheet (headless-safe) for visual QA.

Modes:
  - solid: Workbench studio lighting + cavity (default silhouette & form check)
  - random: Workbench random color per object/part (spots detached parts)
  - wire: Workbench black wireframe overlay over solid (topology check)
  - material: Workbench material/texture preview colors
  - xray: Translucent Workbench mesh + headless bone-proxy overlay for linked armatures
  - rendered: Fast denoised render with the scene's active engine, lights & world (EEVEE/Cycles)

Multi-frame animation strip:
  Pass --frames 1 15 30 45 (or --frame-count 6 to sample scene.frame_start..frame_end)
  to render a single-angle or active-camera animation strip tiled into one contact sheet.

Usage:
  blender -b f.blend -P review_shots.py -- [--objects A B] [--out //review.png]
      [--views front right back left top three_quarter camera]
      [--mode solid|random|wire|material|xray|rendered] [--res 512]
      [--frames 1 15 30 | --frame-count 6] [--samples 16]
  Live MCP: prefer `look` (mcp-for-blender); this script gives headless parity.
Returns {"ok": True, "sheet": path, "views": [paths], "layout": "CxR", "order": [...]}
"""
import math
import os
import sys
import tempfile

import bmesh
import bpy
import numpy as np
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(__file__))
import _bpyx as bx  # noqa: E402

DIRS = {
    "front": (0, -1, 0.15),
    "back": (0, 1, 0.15),
    "right": (1, 0, 0.15),
    "left": (-1, 0, 0.15),
    "top": (0, -0.001, 1),
    "bottom": (0, 0.001, -1),
    "three_quarter": (1, -1, 0.6),
}


def _bounds(obs):
    bpy.context.view_layer.update()  # bound_box is stale on freshly built objects
    pts = []
    for o in obs:
        if o.bound_box:
            pts.extend(o.matrix_world @ Vector(c) for c in o.bound_box)
        else:
            pts.append(o.matrix_world.translation.copy())
    if not pts:
        return Vector((0, 0, 0)), 1.0
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return (lo + hi) / 2, max((hi - lo).length / 2, 1e-3)


def _find_related_armatures(obs):
    arms = set()
    for o in obs:
        if o.type == "ARMATURE":
            arms.add(o)
        if o.parent and o.parent.type == "ARMATURE":
            arms.add(o.parent)
        for m in o.modifiers:
            if m.type == "ARMATURE" and m.object and m.object.type == "ARMATURE":
                arms.add(m.object)
    return sorted(arms, key=lambda a: a.name)


def _build_bone_proxy(arm, radius_hint=0.015):
    """Build a temporary octahedral mesh matching the armature's current pose bones.

    Headless `bpy.ops.render.render()` does not rasterize Armature bone overlays,
    so a thin high-contrast proxy mesh lets `mode="xray"` inspect rigs in `-b` mode.
    """
    bm = bmesh.new()
    mw = arm.matrix_world
    for pb in arm.pose.bones:
        h = mw @ pb.head
        t = mw @ pb.tail
        vec = t - h
        length = vec.length
        if length < 1e-4:
            continue
        r = max(min(length * 0.12, radius_hint * 1.5), radius_hint * 0.45)
        z_axis = vec.normalized()
        up = Vector((0, 0, 1)) if abs(z_axis.z) < 0.95 else Vector((1, 0, 0))
        x_axis = z_axis.cross(up).normalized() * r
        y_axis = z_axis.cross(x_axis).normalized() * r
        mid = h + vec * 0.2

        vh = bm.verts.new(h)
        vt = bm.verts.new(t)
        v0 = bm.verts.new(mid + x_axis)
        v1 = bm.verts.new(mid + y_axis)
        v2 = bm.verts.new(mid - x_axis)
        v3 = bm.verts.new(mid - y_axis)
        ring = (v0, v1, v2, v3)
        for i in range(4):
            a, b = ring[i], ring[(i + 1) % 4]
            try:
                bm.faces.new((vh, b, a))
                bm.faces.new((vt, a, b))
            except ValueError:
                pass

    me = bpy.data.meshes.new(f"QA_BoneProxy_{arm.name}")
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(me.name, me)
    ob.color = (0.08, 0.85, 0.95, 1.0)
    return ob


def _resolve_frames(sc, frames=None, frame_count=0):
    if frames:
        return [int(f) for f in frames]
    if frame_count and frame_count > 0:
        f0, f1 = int(sc.frame_start), int(sc.frame_end)
        if frame_count == 1 or f1 <= f0:
            return [f0]
        return [int(round(f0 + (f1 - f0) * i / (frame_count - 1))) for i in range(frame_count)]
    return None


def _configure_view_cam(cam, cam_data, obs, view_key):
    center, radius = _bounds(obs)
    fov = 2 * math.atan(cam_data.sensor_width / (2 * cam_data.lens))
    dist = radius / math.sin(fov / 2) * 1.05
    cam_data.clip_end = max(dist * 4, 100.0)
    cam_data.clip_start = max(dist / 1000.0, 0.005)
    d = Vector(DIRS[view_key] if isinstance(view_key, str) else view_key).normalized()
    cam.location = center + d * dist
    cam.rotation_euler = (-d).to_track_quat("-Z", "Y").to_euler()


def run(objects=None, out="", views=None, mode="solid", res=512,
        frames=None, frame_count=0, samples=16, **_):
    bx.object_mode()
    obs = bx.objects(objects, types=("MESH", "CURVE", "FONT", "SURFACE", "CURVES", "VOLUME"))
    if not obs:
        raise ValueError("nothing to render")

    sc = bpy.context.scene
    frame_list = _resolve_frames(sc, frames=frames, frame_count=frame_count)
    if frame_list:
        views = views[:1] if views else ["three_quarter"]
    else:
        views = views or ["front", "right", "top", "three_quarter"]

    out = bpy.path.abspath(out) if out else os.path.join(
        os.path.dirname(bpy.data.filepath) or tempfile.gettempdir(), "review_sheet.png"
    )
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)

    r, sh = sc.render, sc.display.shading
    orig_frame = sc.frame_current
    saved = dict(
        engine=r.engine,
        rx=r.resolution_x,
        ry=r.resolution_y,
        pct=r.resolution_percentage,
        fp=r.filepath,
        cam=sc.camera,
        light=sh.light,
        color=sh.color_type,
        cavity=sh.show_cavity,
        outline=sh.show_object_outline,
        xray=sh.show_xray,
        xray_alpha=sh.xray_alpha,
        transp=r.film_transparent,
        eevee_samples=getattr(sc.eevee, "taa_render_samples", None),
        cycles_samples=getattr(sc.cycles, "samples", None),
        cycles_denoise=getattr(sc.cycles, "use_denoising", None),
    )
    hidden = {o: o.hide_render for o in sc.objects}
    saved_colors = {o: tuple(o.color) for o in obs}
    temp = []
    temp_meshes = []
    temp_cams = []

    try:
        armatures = _find_related_armatures(obs) if mode == "xray" else []

        if mode == "rendered":
            # Keep scene lights, world, and active engine; just cap samples for fast preview
            if r.engine == "BLENDER_WORKBENCH":
                r.engine = "BLENDER_EEVEE"
            if r.engine == "BLENDER_EEVEE" and hasattr(sc.eevee, "taa_render_samples"):
                sc.eevee.taa_render_samples = max(4, int(samples))
            elif r.engine == "CYCLES":
                sc.cycles.samples = max(4, int(samples))
                if hasattr(sc.cycles, "use_denoising"):
                    sc.cycles.use_denoising = True
            for o in sc.objects:
                if o.type in ("LIGHT", "LIGHT_PROBE", "CAMERA"):
                    continue
                if objects:
                    o.hide_render = o not in obs
        else:
            for o in sc.objects:
                o.hide_render = o not in obs
            r.engine = "BLENDER_WORKBENCH"
            sh.light = "STUDIO"
            sh.show_cavity = mode in ("solid", "wire")
            sh.show_object_outline = True
            sh.show_xray = (mode == "xray")
            if mode == "xray":
                sh.xray_alpha = 0.35
                sh.color_type = "OBJECT"
                for o in obs:
                    o.color = (0.72, 0.76, 0.82, 0.45)
            else:
                sh.color_type = {
                    "random": "RANDOM",
                    "material": "MATERIAL",
                    "wire": "OBJECT",
                }.get(mode, "SINGLE")

            if mode == "wire":
                wire_t = _bounds(obs)[1] * 0.006
                for o in obs:
                    if o.type != "MESH":
                        continue
                    w = o.copy()
                    w.data = o.data
                    w.modifiers.new("QA_Wire", "WIREFRAME").thickness = wire_t
                    w.color = (0, 0, 0, 1)
                    sc.collection.objects.link(w)
                    temp.append(w)
                    o.color = (0.8, 0.8, 0.8, 1)

        r.resolution_x = r.resolution_y = int(res)
        r.resolution_percentage = 100
        r.film_transparent = False
        r.image_settings.media_type = "IMAGE"
        r.image_settings.file_format = "PNG"

        cam_data = bpy.data.cameras.new("QA_Cam")
        cam_data.lens = 50
        cam = bpy.data.objects.new("QA_Cam", cam_data)
        sc.collection.objects.link(cam)
        temp.append(cam)
        temp_cams.append(cam_data)

        paths = []
        order = []

        def _spawn_bone_proxies():
            proxies = []
            if mode != "xray" or not armatures:
                return proxies
            radius_hint = max(_bounds(obs)[1] * 0.015, 0.008)
            for arm in armatures:
                px = _build_bone_proxy(arm, radius_hint=radius_hint)
                sc.collection.objects.link(px)
                proxies.append(px)
            return proxies

        def _clear_bone_proxies(proxies):
            for px in proxies:
                me = px.data
                bpy.data.objects.remove(px, do_unlink=True)
                if me and me.users == 0:
                    bpy.data.meshes.remove(me)

        def _render_one(tag, view_key):
            if view_key == "camera":
                if saved["cam"] is None:
                    raise ValueError("view='camera' requested but scene has no active camera")
                sc.camera = saved["cam"]
            else:
                sc.camera = cam
                _configure_view_cam(cam, cam_data, obs, view_key)
            p = os.path.splitext(out)[0] + f"_{tag}.png"
            r.filepath = p
            bpy.ops.render.render(write_still=True)
            paths.append(p)
            order.append(tag)

        if frame_list:
            v = views[0]
            for f in frame_list:
                sc.frame_set(f)
                bpy.context.view_layer.update()
                proxies = _spawn_bone_proxies()
                try:
                    _render_one(f"f{f:04d}", v)
                finally:
                    _clear_bone_proxies(proxies)
        else:
            proxies = _spawn_bone_proxies()
            try:
                for v in views:
                    _render_one(str(v), v)
            finally:
                _clear_bone_proxies(proxies)

        # Tile into a contact sheet (pure bpy + numpy, zero external deps)
        imgs = []
        for p in paths:
            im = bpy.data.images.load(p, check_existing=False)
            a = np.empty(res * res * 4, dtype=np.float32)
            im.pixels.foreach_get(a)
            imgs.append(a.reshape(res, res, 4))
            bpy.data.images.remove(im)
        n = len(imgs)
        cols = n if n <= 3 else 2 if n == 4 else 3
        rows = math.ceil(n / cols)
        sheet = np.empty((rows * res, cols * res, 4), dtype=np.float32)
        sheet[:] = imgs[0][0, 0]
        for i, a in enumerate(imgs):
            rr, cc = rows - 1 - i // cols, i % cols  # pixel rows are bottom-up
            sheet[rr * res:(rr + 1) * res, cc * res:(cc + 1) * res] = a
        im = bpy.data.images.new("QA_Sheet", cols * res, rows * res, alpha=True)
        im.pixels.foreach_set(sheet.ravel())
        im.filepath_raw = out
        im.file_format = "PNG"
        im.save()
        bpy.data.images.remove(im)
    finally:
        sc.frame_set(orig_frame)
        for o in temp:
            bpy.data.objects.remove(o, do_unlink=True)
        for me in temp_meshes:
            if me.users == 0:
                bpy.data.meshes.remove(me)
        for cd in temp_cams:
            if cd.users == 0:
                bpy.data.cameras.remove(cd)
        for o, h in hidden.items():
            o.hide_render = h
        for o, col in saved_colors.items():
            o.color = col
        r.engine, r.resolution_x, r.resolution_y = saved["engine"], saved["rx"], saved["ry"]
        r.resolution_percentage, r.filepath, sc.camera = saved["pct"], saved["fp"], saved["cam"]
        r.film_transparent = saved["transp"]
        sh.light, sh.color_type, sh.show_cavity = saved["light"], saved["color"], saved["cavity"]
        sh.show_object_outline = saved["outline"]
        sh.show_xray, sh.xray_alpha = saved["xray"], saved["xray_alpha"]
        if saved["eevee_samples"] is not None and hasattr(sc.eevee, "taa_render_samples"):
            sc.eevee.taa_render_samples = saved["eevee_samples"]
        if saved["cycles_samples"] is not None and hasattr(sc.cycles, "samples"):
            sc.cycles.samples = saved["cycles_samples"]
        if saved["cycles_denoise"] is not None and hasattr(sc.cycles, "use_denoising"):
            sc.cycles.use_denoising = saved["cycles_denoise"]

    return {
        "ok": True,
        "mode": mode,
        "sheet": out,
        "views": paths,
        "layout": f"{cols}x{rows}",
        "order": order,
    }


if __name__ == "__main__":
    p = bx.add_common(bx.parser(__doc__), save=False)
    p.add_argument("--out", default="")
    p.add_argument("--views", nargs="*", default=None, choices=list(DIRS) + ["camera"])
    p.add_argument(
        "--mode",
        default="solid",
        choices=["solid", "random", "wire", "material", "xray", "rendered"],
    )
    p.add_argument("--res", type=int, default=512)
    p.add_argument("--frames", nargs="*", type=int, default=None,
                   help="explicit frame list for an animation contact strip")
    p.add_argument("--frame-count", type=int, default=0,
                   help="evenly sample N frames from scene.frame_start..frame_end")
    p.add_argument("--samples", type=int, default=16,
                   help="sample cap for --mode rendered (default: 16)")
    bx.cli(run, p)

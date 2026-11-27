#!/usr/bin/env python3
"""
blender_hair_locks.py — Sculpted Stylized Roblox Hair Engine (Law R-LOOK, code-built, zero licence risk).

Art-direction principles (Pixar / Top-Tier Roblox UGC):
  1. Unified Sculpted Main Volume: the crown, sides, and nape are sculpted as ONE cohesive volumetric hair mass
     with asymmetric silhouette shaping, parting valley, soft directional wave flutes, and clean hairline curves
     (zero forehead cap band, zero hollow gaps, zero detached sausage tubes).
  2. Sleek Stylized Ribbon Locks: bangs, side sweeps, and accent tips use a wide, flatter beveled-crescent cross-section
     whose roots embed smoothly inside the main volume, tapering to clean curved stylized points.
  3. Continuous Watertight Drapes for long hair and bobs with sculpted vertical wave undulations (no spaghetti tubes).
  4. Rich Cycles stylized hair shader: root-to-tip warmth gradient + soft AO crevice depth + silky sheen + combed bump.
"""
import math
import random

import bmesh
import bpy
from mathutils import Vector

STUD = 0.28
STYLES = (
    "boy",
    "boy_part",
    "boy_fluffy",
    "girl",
    "girl_bob",
    "girl_ponytail",
    "old_man",
    "old_woman",
)
DEFAULT_HEX = {
    "boy": "#3A2316",
    "boy_part": "#221A17",
    "boy_fluffy": "#4B2F1D",
    "girl": "#4E2A1B",
    "girl_bob": "#271B18",
    "girl_ponytail": "#5B3421",
    "old_man": "#C8C6C1",
    "old_woman": "#D6D4CF",
}


def _lin(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4)]
    return tuple(x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c) + (1.0,)


def make_lock_hair_mat(name, hair_hex, is_tie=False):
    """Stylized Pixar/Roblox UGC hair shader: root-to-tip gradient + soft AO + silky sheen + combed strand bump."""
    base = _lin(hair_hex)
    mat = bpy.data.materials.new(name)
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")

    if is_tie:
        bsdf.inputs["Base Color"].default_value = base
        bsdf.inputs["Roughness"].default_value = 0.50
        if "Sheen Weight" in bsdf.inputs:
            bsdf.inputs["Sheen Weight"].default_value = 0.45
        nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
        return mat

    bsdf.inputs["Roughness"].default_value = 0.40
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = 0.40
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.14
        bsdf.inputs["Coat Roughness"].default_value = 0.34
    if "Sheen Weight" in bsdf.inputs:
        bsdf.inputs["Sheen Weight"].default_value = 0.25
        bsdf.inputs["Sheen Roughness"].default_value = 0.45

    uv = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(uv.outputs["UV"], sep.inputs["Vector"])

    ramp = nt.nodes.new("ShaderNodeValToRGB")
    e = ramp.color_ramp.elements
    e[0].position, e[0].color = 0.0, tuple(c * 0.58 for c in base[:3]) + (1.0,)
    e[1].position, e[1].color = 1.0, tuple(min(1.0, c * 1.24 + 0.010) for c in base[:3]) + (1.0,)
    mid = ramp.color_ramp.elements.new(0.45)
    mid.color = tuple(min(1.0, c * 1.00) for c in base[:3]) + (1.0,)
    nt.links.new(sep.outputs["Y"], ramp.inputs["Fac"])

    mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Scale"].default_value = (22.0, 1.3, 1.0)
    nt.links.new(uv.outputs["UV"], mp.inputs["Vector"])

    wave = nt.nodes.new("ShaderNodeTexWave")
    wave.wave_type = "BANDS"
    wave.bands_direction = "X"
    wave.inputs["Scale"].default_value = 3.2
    wave.inputs["Distortion"].default_value = 1.4
    wave.inputs["Detail"].default_value = 2.5
    nt.links.new(mp.outputs["Vector"], wave.inputs["Vector"])

    str_mix = nt.nodes.new("ShaderNodeMix")
    str_mix.data_type = "RGBA"
    str_mix.blend_type = "MULTIPLY"
    str_mix.inputs["Factor"].default_value = 0.14
    rgba_s = [s for s in str_mix.inputs if s.type == "RGBA"]
    nt.links.new(ramp.outputs["Color"], rgba_s[0])
    nt.links.new(wave.outputs["Color"], rgba_s[1])
    col_out = next(s for s in str_mix.outputs if s.type == "RGBA")

    ao = nt.nodes.new("ShaderNodeAmbientOcclusion")
    ao.samples = 8
    ao.inputs["Distance"].default_value = 0.06
    nt.links.new(col_out, ao.inputs["Color"])

    ao_mix = nt.nodes.new("ShaderNodeMix")
    ao_mix.data_type = "RGBA"
    ao_mix.blend_type = "MULTIPLY"
    ao_mix.inputs["Factor"].default_value = 0.30
    rgba_a = [s for s in ao_mix.inputs if s.type == "RGBA"]
    nt.links.new(col_out, rgba_a[0])
    nt.links.new(ao.outputs["AO"], rgba_a[1])
    nt.links.new(next(s for s in ao_mix.outputs if s.type == "RGBA"), bsdf.inputs["Base Color"])

    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.10
    bump.inputs["Distance"].default_value = 0.004
    nt.links.new(wave.outputs["Fac"], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])

    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


class _ExactHead:
    """Exact rounded-cylinder head matching `_create_roblox_head` in blender_roblox_kit.py."""

    def __init__(self, char_info):
        m = char_info["metrics"]
        self.hs = m["hs"]
        self.c = Vector(m["head_center"]) * STUD
        self.r = 0.60 * self.hs * STUD
        self.hh = 0.58 * self.hs * STUD
        self.fil = 0.36 * self.r
        self.r_c = self.r - self.fil
        self.z_c = self.hh - self.fil
        self.brow_z = self.c.z + 0.30 * self.hh

    def radius_at_z(self, dz, pad=0.0):
        r_s = self.r + pad
        fil_s = self.fil + pad
        top_z = self.hh + pad
        if abs(dz) >= top_z:
            return 0.0
        if abs(dz) <= self.z_c:
            return r_s
        z_rem = abs(dz) - self.z_c
        return self.r_c + math.sqrt(max(0.0, fil_s * fil_s - z_rem * z_rem))

    def surface_theta_z(self, theta, dz_frac, pad=0.0):
        dz = dz_frac * (self.hh + pad)
        rad = self.radius_at_z(dz, pad=pad)
        return Vector((rad * math.sin(theta), -rad * math.cos(theta), dz)) + self.c

    def normal(self, p):
        d = p - self.c
        rad = math.hypot(d.x, d.y)
        if d.z > self.z_c and rad < self.r_c:
            return Vector((0.0, 0.0, 1.0))
        if abs(d.z) <= self.z_c and rad > 1e-6:
            return Vector((d.x / rad, d.y / rad, 0.0))
        if rad > 1e-6:
            cx = (d.x / rad) * self.r_c
            cy = (d.y / rad) * self.r_c
            cz = self.z_c if d.z >= 0 else -self.z_c
            n = Vector((d.x - cx, d.y - cy, d.z - cz))
            if n.length > 1e-6:
                return n.normalized()
        return Vector((0.0, 0.0, 1.0 if d.z >= 0 else -1.0))

    def push_out(self, p, pad=0.008):
        d = p - self.c
        rad = math.hypot(d.x, d.y)
        r_s = self.r + pad
        hh_s = self.hh + pad
        fil_s = self.fil + pad
        if abs(d.z) <= self.z_c:
            if rad < r_s and rad > 1e-6:
                s = r_s / rad
                return Vector((self.c.x + d.x * s, self.c.y + d.y * s, p.z))
            return p
        sgn = 1.0 if d.z >= 0 else -1.0
        if rad <= self.r_c:
            if abs(d.z) < hh_s:
                return Vector((p.x, p.y, self.c.z + sgn * hh_s))
            return p
        dr = rad - self.r_c
        dz = abs(d.z) - self.z_c
        dist = math.hypot(dr, dz)
        if dist < fil_s and dist > 1e-6:
            sc = fil_s / dist
            new_r = self.r_c + dr * sc
            new_z = self.z_c + dz * sc
            ux, uy = d.x / rad, d.y / rad
            return Vector((self.c.x + ux * new_r, self.c.y + uy * new_r, self.c.z + sgn * new_z))
        return p


def _catmull_rom(ctrl, steps=16):
    n = len(ctrl)
    if n < 2:
        return list(ctrl)
    pts = [ctrl[0] + (ctrl[0] - ctrl[1])] + list(ctrl) + [ctrl[-1] + (ctrl[-1] - ctrl[-2])]
    out = []
    segs = n - 1
    for i in range(steps + 1):
        u = (i / steps) * segs
        seg = min(int(u), segs - 1)
        t = u - seg
        p0, p1, p2, p3 = pts[seg], pts[seg + 1], pts[seg + 2], pts[seg + 3]
        t2, t3 = t * t, t * t * t
        out.append(0.5 * (
            (2.0 * p1)
            + (-p0 + p2) * t
            + (2.0 * p0 - 5.0 * p1 + 4.0 * p2 - p3) * t2
            + (-p0 + 3.0 * p1 - 3.0 * p2 + p3) * t3
        ))
    return out


# Sleek stylized hair-ribbon cross-section: wide, softly arched beveled roof (NOT a round sausage tube!)
_RIBBON_PROFILE = (
    (1.00, -0.05),
    (0.84, 0.35),
    (0.46, 0.78),
    (0.00, 1.00),
    (-0.46, 0.78),
    (-0.84, 0.35),
    (-1.00, -0.05),
    (-0.48, -0.18),
    (0.00, -0.22),
    (0.48, -0.18),
)


def _ribbon_lock(bm, uv_layer, head, ctrl_pts, w_max, h_max, steps=14,
                 w_root=0.82, w_peak_t=0.28, tip_pow=1.25, twist_deg=0.0,
                 push_pad=0.005, mat_idx=0):
    """Build one sleek, wide stylized hair ribbon lock that blends smoothly from the main hair mass."""
    pts = _catmull_rom(ctrl_pts, steps=steps)
    if push_pad is not None:
        pts = [head.push_out(p, pad=push_pad) if idx > 0 else p for idx, p in enumerate(pts)]

    n_prof = len(_RIBBON_PROFILE)
    rings = []
    prev_side = None
    for i, p in enumerate(pts):
        t = i / steps
        if i == 0:
            tan = (pts[1] - pts[0]).normalized()
        elif i == steps:
            tan = (pts[-1] - pts[-2]).normalized()
        else:
            tan = (pts[i + 1] - pts[i - 1]).normalized()

        out_dir = head.normal(p)
        out_ortho = out_dir - tan * out_dir.dot(tan)
        if out_ortho.length < 1e-4:
            ref = Vector((0.0, 1.0, 0.0)) if abs(tan.y) < 0.85 else Vector((1.0, 0.0, 0.0))
            out_ortho = ref - tan * ref.dot(tan)
        out_ortho.normalize()
        side = tan.cross(out_ortho).normalized()
        if prev_side is not None and side.dot(prev_side) < 0:
            side = -side
            out_ortho = -out_ortho
        prev_side = side

        tw = math.radians(twist_deg) * t
        if abs(tw) > 1e-4:
            cs, sn = math.cos(tw), math.sin(tw)
            sd = side * cs + out_ortho * sn
            od = out_ortho * cs - side * sn
        else:
            sd, od = side, out_ortho

        if t < w_peak_t:
            u = t / max(w_peak_t, 1e-4)
            env = w_root + (1.0 - w_root) * (math.sin(u * math.pi * 0.5) ** 0.8)
        else:
            u = (t - w_peak_t) / max(1.0 - w_peak_t, 1e-4)
            env = max(0.0, 1.0 - (u ** tip_pow))

        if i == steps:
            rings.append([bm.verts.new(p)])
        else:
            hw = 0.5 * w_max * env
            hh = h_max * env
            rings.append([bm.verts.new(p + sd * (px * hw) + od * (py * hh)) for px, py in _RIBBON_PROFILE])

    for i in range(steps - 1):
        v0, v1 = i / steps, (i + 1) / steps
        r0, r1 = rings[i], rings[i + 1]
        for k in range(n_prof):
            k2 = (k + 1) % n_prof
            f = bm.faces.new((r0[k], r0[k2], r1[k2], r1[k]))
            f.smooth = True
            f.material_index = mat_idx
            u0, u1 = k / n_prof, (k + 1) / n_prof
            for lp, uv in zip(f.loops, ((u0, v0), (u1, v0), (u1, v1), (u0, v1))):
                lp[uv_layer].uv = uv

    r_last = rings[steps - 1]
    v_tip = rings[steps][0]
    v_prev = (steps - 1) / steps
    for k in range(n_prof):
        k2 = (k + 1) % n_prof
        f = bm.faces.new((r_last[k], r_last[k2], v_tip))
        f.smooth = True
        f.material_index = mat_idx
        u0, u1 = k / n_prof, (k + 1) / n_prof
        for lp, uv in zip(f.loops, ((u0, v_prev), (u1, v_prev), (0.5 * (u0 + u1), 1.0))):
            lp[uv_layer].uv = uv

    f_root = bm.faces.new(list(reversed(rings[0])))
    f_root.smooth = True
    f_root.material_index = mat_idx
    for lp in f_root.loops:
        lp[uv_layer].uv = (0.5, 0.0)


def _sculpt_mass(bm, uv_layer, head, pad_base=0.020, z_front=0.56, z_back=-0.62,
                 part_deg=None, part_depth=0.011, crown_lift=0.022,
                 sculpt_fn=None, z_low_fn=None, n_t=64, n_p=24,
                 top_cutoff=None, skip_front_deg=0.0, mat_idx=0):
    """Unified high-resolution sculpted hair mass wrapping `_ExactHead` with custom silhouette shaping."""
    top_max = top_cutoff if top_cutoff is not None else 1.0
    part_rad = math.radians(part_deg) if part_deg is not None else None

    def _low_z(th):
        if z_low_fn is not None:
            return z_low_fn(th)
        back_w = 0.5 - 0.5 * math.cos(th)
        ang_abs = abs(math.degrees(math.atan2(math.sin(th), math.cos(th))))
        # Natural sideburn / temple dip around ~75°
        temple = math.exp(-((ang_abs - 76.0) / 22.0) ** 2)
        return z_front + (z_back - z_front) * (back_w ** 1.15) - 0.22 * temple

    in_ring = []
    for i in range(n_t):
        th = 2.0 * math.pi * i / n_t
        dz = _low_z(th) * head.hh
        rad_in = max(0.01, head.radius_at_z(dz, pad=-0.008))
        in_ring.append(bm.verts.new(Vector((rad_in * math.sin(th), -rad_in * math.cos(th), dz)) + head.c))

    rings = []
    for j in range(n_p):
        tf = (j / float(n_p)) ** 0.88
        row = []
        for i in range(n_t):
            th = 2.0 * math.pi * i / n_t
            z_low = _low_z(th)
            zf = z_low + tf * (top_max - z_low)

            pad = pad_base + crown_lift * (tf ** 1.35)
            # Soft taper into hairline at bottom edge for natural organic transition
            if j == 0:
                pad *= 0.65
            elif j == 1:
                pad *= 0.88

            if part_rad is not None:
                d_th = math.atan2(math.sin(th - part_rad), math.cos(th - part_rad))
                if tf > 0.12 and abs(d_th) < 0.55:
                    pad -= part_depth * math.exp(-((d_th / 0.13) ** 2)) * math.sin(min(1.0, tf) * math.pi * 0.92)

            extra_vec = Vector((0.0, 0.0, 0.0))
            if sculpt_fn is not None:
                dp, dv = sculpt_fn(th, tf, zf)
                pad += dp
                extra_vec = dv

            p = head.surface_theta_z(th, zf, pad=max(0.006, pad)) + extra_vec
            row.append(bm.verts.new(p))
        rings.append(row)

    closed = top_cutoff is None
    top_pole = None
    if closed:
        extra_top = sculpt_fn(0.0, 1.0, 1.0) if sculpt_fn is not None else (0.0, Vector((0, 0, 0)))
        top_p = head.c + Vector((0.0, 0.0, head.hh + pad_base + crown_lift + extra_top[0] - (part_depth * 0.35 if part_rad else 0.0))) + extra_top[1]
        top_pole = bm.verts.new(top_p)

    # Optional top inner tuck for bald-crown elder hair (so open top edge is smooth & watertight!)
    top_in_ring = None
    if not closed:
        top_in_ring = []
        for i in range(n_t):
            th = 2.0 * math.pi * i / n_t
            dz = top_max * head.hh
            rad_in = max(0.01, head.radius_at_z(dz, pad=-0.006))
            top_in_ring.append(bm.verts.new(Vector((rad_in * math.sin(th), -rad_in * math.cos(th), dz)) + head.c))

    def _keep(i):
        if not skip_front_deg:
            return True
        deg = (360.0 * (i + 0.5) / n_t) % 360.0
        return not (deg < skip_front_deg or deg > 360.0 - skip_front_deg)

    for i in range(n_t):
        if not _keep(i):
            continue
        i2 = (i + 1) % n_t
        f0 = bm.faces.new((in_ring[i], in_ring[i2], rings[0][i2], rings[0][i]))
        f0.smooth = True
        f0.material_index = mat_idx
        for lp in f0.loops:
            lp[uv_layer].uv = (i / n_t * 5.0, 0.08)

        for j in range(n_p - 1):
            f = bm.faces.new((rings[j][i], rings[j][i2], rings[j + 1][i2], rings[j + 1][i]))
            f.smooth = True
            f.material_index = mat_idx
            u0, u1 = (i / n_t) * 6.0, ((i + 1) / n_t) * 6.0
            v0, v1 = 0.12 + 0.65 * (j / n_p), 0.12 + 0.65 * ((j + 1) / n_p)
            for lp, uv in zip(f.loops, ((u0, v0), (u1, v0), (u1, v1), (u0, v1))):
                lp[uv_layer].uv = uv

        if closed:
            ft = bm.faces.new((rings[-1][i], rings[-1][i2], top_pole))
            ft.smooth = True
            ft.material_index = mat_idx
            for lp in ft.loops:
                lp[uv_layer].uv = ((i / n_t) * 6.0, 0.25)
        else:
            ftop = bm.faces.new((rings[-1][i], rings[-1][i2], top_in_ring[i2], top_in_ring[i]))
            ftop.smooth = True
            ftop.material_index = mat_idx
            for lp in ftop.loops:
                lp[uv_layer].uv = ((i / n_t) * 5.0, 0.72)

    # Close front side edges cleanly when skip_front_deg > 0 (old_man horseshoe ends)
    if skip_front_deg > 0:
        for i in range(n_t):
            i2 = (i + 1) % n_t
            k_cur, k_nxt = _keep(i), _keep(i2)
            if k_cur != k_nxt:
                edge_i = i2 if k_cur else i2
                for j in range(n_p - 1):
                    # Stitch vertical cap from outer ring back to inner head wall
                    dz0 = (rings[j][edge_i].co.z - head.c.z)
                    dz1 = (rings[j + 1][edge_i].co.z - head.c.z)
                    th = 2.0 * math.pi * edge_i / n_t
                    vi0 = bm.verts.new(Vector((head.radius_at_z(dz0, -0.005) * math.sin(th), -head.radius_at_z(dz0, -0.005) * math.cos(th), dz0)) + head.c)
                    vi1 = bm.verts.new(Vector((head.radius_at_z(dz1, -0.005) * math.sin(th), -head.radius_at_z(dz1, -0.005) * math.cos(th), dz1)) + head.c)
                    verts = (rings[j][edge_i], vi0, vi1, rings[j + 1][edge_i]) if k_cur else (vi0, rings[j][edge_i], rings[j + 1][edge_i], vi1)
                    fe = bm.faces.new(verts)
                    fe.smooth = True
                    fe.material_index = mat_idx
                    for lp in fe.loops:
                        lp[uv_layer].uv = (0.5, 0.5)


def _sculpt_drape(bm, uv_layer, head, th_min_deg, th_max_deg, length_hh,
                  flare_out=0.045, curl_in=0.0, pad_top=0.024, thick=0.026,
                  wave_amp=0.010, wave_n=7, n_u=44, n_v=18, mat_idx=0):
    """Continuous double-sided volumetric hair drape with soft sculpted wave undulations (zero gaps, zero spaghetti)."""
    outer, inner = [], []
    for iv in range(n_v + 1):
        v = iv / n_v
        row_o, row_i = [], []
        for iu in range(n_u + 1):
            u = iu / n_u
            th = math.radians(th_min_deg + (th_max_deg - th_min_deg) * u)
            z_start = head.hh * 0.68
            edge_lift = 0.14 * ((2.0 * u - 1.0) ** 2)
            # Soft layered rounded hem (smooth organic scallop)
            hem_wave = 0.032 * math.sin(u * math.pi * wave_n)
            drop = (length_hh * (1.0 - edge_lift + hem_wave)) * head.hh
            z = z_start - v * drop

            base_r = head.radius_at_z(max(-head.hh * 0.65, min(head.hh * 0.85, z)), pad=pad_top)
            if z < -head.hh * 0.35:
                base_r = head.r + pad_top
            # Smooth zero-ridge blend at the top edge (v -> 0) into the crown shell
            top_blend = min(1.0, v / 0.24) ** 1.4
            swell = flare_out * math.sin(v * math.pi * 0.85) * top_blend
            c_in = -curl_in * (v ** 2.4)
            # Soft wide S-curve vertical flutes along the drape (looks like sculpted stylized hair waves!)
            flute = wave_amp * math.sin(u * math.pi * wave_n * 2.0 + 0.55 * math.sin(v * math.pi)) * math.sin(v * math.pi * 0.92) * top_blend
            r_out = base_r + swell + c_in + flute - (0.008 * (1.0 - top_blend))
            loc_th = thick * (1.0 - 0.68 * (v ** 1.7)) * (0.55 + 0.45 * math.sin(u * math.pi))
            r_in = max(head.r * 0.72, r_out - loc_th)

            sx, sy = math.sin(th), -math.cos(th)
            po = Vector((r_out * sx, r_out * sy, z)) + head.c
            pi = Vector((r_in * sx, r_in * sy, z + 0.003 * v)) + head.c
            if v < 0.75:
                po = head.push_out(po, pad=0.012)
            row_o.append(bm.verts.new(po))
            row_i.append(bm.verts.new(pi))
        outer.append(row_o)
        inner.append(row_i)

    for iv in range(n_v):
        v0, v1 = 0.15 + 0.85 * (iv / n_v), 0.15 + 0.85 * ((iv + 1) / n_v)
        for iu in range(n_u):
            u0, u1 = (iu / n_u) * 5.0, ((iu + 1) / n_u) * 5.0
            fo = bm.faces.new((outer[iv][iu], outer[iv][iu + 1], outer[iv + 1][iu + 1], outer[iv + 1][iu]))
            fi = bm.faces.new((inner[iv][iu + 1], inner[iv][iu], inner[iv + 1][iu], inner[iv + 1][iu + 1]))
            for f, uvs in ((fo, ((u0, v0), (u1, v0), (u1, v1), (u0, v1))),
                           (fi, ((u1, v0), (u0, v0), (u0, v1), (u1, v1)))):
                f.smooth = True
                f.material_index = mat_idx
                for lp, uv in zip(f.loops, uvs):
                    lp[uv_layer].uv = uv

    for iu in range(n_u):
        fb = bm.faces.new((outer[n_v][iu], outer[n_v][iu + 1], inner[n_v][iu + 1], inner[n_v][iu]))
        fb.smooth = True
        fb.material_index = mat_idx
        for lp in fb.loops:
            lp[uv_layer].uv = (iu / n_u * 5.0, 0.98)
    for iv in range(n_v):
        fl = bm.faces.new((inner[iv][0], outer[iv][0], outer[iv + 1][0], inner[iv + 1][0]))
        fr = bm.faces.new((outer[iv][n_u], inner[iv][n_u], inner[iv + 1][n_u], outer[iv + 1][n_u]))
        for f in (fl, fr):
            f.smooth = True
            f.material_index = mat_idx
            for lp in f.loops:
                lp[uv_layer].uv = (0.5, 0.5)


def _sculpt_torus_ring(bm, uv_layer, center, axis_dir, major_r, minor_r, n_maj=28, n_min=12, mat_idx=1):
    az = axis_dir.normalized()
    ref = Vector((1, 0, 0)) if abs(az.x) < 0.8 else Vector((0, 0, 1))
    ax = az.cross(ref).normalized()
    ay = az.cross(ax).normalized()
    rings = []
    for i in range(n_maj):
        th = 2.0 * math.pi * i / n_maj
        rad_dir = ax * math.cos(th) + ay * math.sin(th)
        c_pt = center + rad_dir * major_r
        rings.append([bm.verts.new(c_pt + (rad_dir * math.cos(2.0 * math.pi * j / n_min) + az * math.sin(2.0 * math.pi * j / n_min)) * minor_r) for j in range(n_min)])
    for i in range(n_maj):
        i2 = (i + 1) % n_maj
        for j in range(n_min):
            j2 = (j + 1) % n_min
            f = bm.faces.new((rings[i][j], rings[i2][j], rings[i2][j2], rings[i][j2]))
            f.smooth = True
            f.material_index = mat_idx
            for lp in f.loops:
                lp[uv_layer].uv = (i / n_maj, j / n_min)


def _sculpt_bun_dome(bm, uv_layer, center, axis_dir, r_xy, r_z, n_u=36, n_v=16, twist_turns=1.6, mat_idx=0):
    """Smooth sculpted spiral-fluted hair bun dome (clean rounded grandma silhouette with subtle twist ridges)."""
    az = axis_dir.normalized()
    ref = Vector((1, 0, 0)) if abs(az.x) < 0.8 else Vector((0, 0, 1))
    ax = az.cross(ref).normalized()
    ay = az.cross(ax).normalized()

    rings = []
    for iv in range(1, n_v):
        ph = -math.pi * 0.42 + (math.pi * 0.90) * (iv / n_v)
        c_ph, s_ph = math.cos(ph), math.sin(ph)
        row = []
        for iu in range(n_u):
            th = 2.0 * math.pi * iu / n_u
            # Gentle helical spiral flutes around the bun (reads as twisted hair without spiky gaps!)
            flute = 1.0 + 0.065 * math.sin(5.0 * th + twist_turns * 2.0 * math.pi * (iv / n_v)) * (c_ph ** 0.7)
            rr = r_xy * c_ph * flute
            zz = r_z * s_ph
            p = center + (ax * math.cos(th) + ay * math.sin(th)) * rr + az * zz
            row.append(bm.verts.new(p))
        rings.append(row)
    bot_p = bm.verts.new(center - az * (r_z * 0.92))
    top_p = bm.verts.new(center + az * (r_z * 1.02))

    for iu in range(n_u):
        iu2 = (iu + 1) % n_u
        fb = bm.faces.new((bot_p, rings[0][iu2], rings[0][iu]))
        ft = bm.faces.new((rings[-1][iu], rings[-1][iu2], top_p))
        for f in (fb, ft):
            f.smooth = True
            f.material_index = mat_idx
            for lp in f.loops:
                lp[uv_layer].uv = (iu / n_u * 4.0, 0.5)
        for iv in range(len(rings) - 1):
            f = bm.faces.new((rings[iv][iu], rings[iv][iu2], rings[iv + 1][iu2], rings[iv + 1][iu]))
            f.smooth = True
            f.material_index = mat_idx
            u0, u1 = (iu / n_u) * 5.0, ((iu + 1) / n_u) * 5.0
            v0, v1 = 0.25 + 0.65 * (iv / len(rings)), 0.25 + 0.65 * ((iv + 1) / len(rings))
            for lp, uv in zip(f.loops, ((u0, v0), (u1, v0), (u1, v1), (u0, v1))):
                lp[uv_layer].uv = uv


def _p(head, th_deg, dz_frac, pad):
    return head.surface_theta_z(math.radians(th_deg), dz_frac, pad=pad)


# ==============================================================================
# 8 REFINED STUDIO-QUALITY HAIRSTYLES (PASS 2)
# ==============================================================================

def _style_boy(bm, uv, head, rnd):
    """Signature Swept Stylized Boy Hair — cohesive sculpted UGC volume, sleek layered bangs, clean tapered back."""
    # Asymmetric sculpted crown mass: slightly taller & fuller sweeping toward character's left (+X) & front (-Y)
    def _boy_sculpt(th, tf, zf):
        # Soft directional hair flutes across the sculpted mass
        flute = 0.005 * math.sin(10.0 * th + 1.2 * tf) * math.sin(tf * math.pi)
        # Crown lift slightly skewed left-front like classic UGC anime boy hair
        asym = 0.014 * math.sin(th + 0.5) * (tf ** 1.3)
        back_full = 0.012 * (0.5 - 0.5 * math.cos(th)) * math.sin(tf * math.pi)
        return (flute + asym + back_full, Vector((0.008 * (tf ** 1.6), -0.006 * (tf ** 1.5), 0.008 * (tf ** 1.8))))

    # Raise z_front to 0.58 so the bangs completely cover the hairline (zero dark band!)
    _sculpt_mass(bm, uv, head, pad_base=0.022, z_front=0.58, z_back=-0.62,
                 part_deg=26, part_depth=0.008, crown_lift=0.032, sculpt_fn=_boy_sculpt)

    # 1. Clean bold sweeping UGC bangs (flowing harmoniously to one side, zero tiny curly hooks!)
    bangs = [
        # (th0, z0, th1, z1, th2, z2, th3, z3, w, h, tw)
        (24, 0.92, -6, 0.74, -34, 0.46, -54, 0.24, 0.125, 0.020, -4),
        (16, 0.88, -8, 0.64, -22, 0.36, -28, 0.24, 0.105, 0.018, -3),
        (28, 0.90, 14, 0.68, 6, 0.38, -2, 0.25, 0.108, 0.018, 2),
        (30, 0.88, 46, 0.68, 56, 0.40, 52, 0.22, 0.102, 0.018, 6),
        (36, 0.86, 58, 0.66, 72, 0.38, 72, 0.12, 0.092, 0.017, 8),
    ]
    for a0, z0, a1, z1, a2, z2, a3, z3, w, h, tw in bangs:
        pts = [_p(head, a0, z0, 0.010), _p(head, a1, z1, 0.036), _p(head, a2, z2, 0.030), _p(head, a3, z3, 0.018)]
        _ribbon_lock(bm, uv, head, pts, w, h, steps=15, w_root=0.90, twist_deg=tw, push_pad=0.007)

    # 2. Stylish UGC spiky-soft crown crest tufts breaking the silhouette dynamically
    tufts = [
        (160, 0.88, 95, 1.02, 32, 0.98, -18, 0.76, 0.112, 0.022),
        (205, 0.88, 140, 1.00, 88, 0.94, 48, 0.68, 0.106, 0.021),
        (-125, 0.86, -82, 0.98, -52, 0.84, -46, 0.56, 0.098, 0.019),
    ]
    for a0, z0, a1, z1, a2, z2, a3, z3, w, h in tufts:
        pts = [
            _p(head, a0, z0, 0.012),
            _p(head, a1, z1, 0.044) + Vector((0, 0, 0.022)),
            _p(head, a2, z2, 0.048) + Vector((0, 0, 0.014)),
            _p(head, a3, z3, 0.028),
        ]
        _ribbon_lock(bm, uv, head, pts, w, h, steps=14, w_root=0.86, push_pad=0.008)

    # 3. Clean sleek sideburns (back silhouette stays smooth & cohesive from the sculpted mass!)
    for sx in (-1, 1):
        pts_sb = [_p(head, sx * 72, 0.52, 0.012), _p(head, sx * 70, 0.10, 0.026), _p(head, sx * 64, -0.32, 0.015)]
        _ribbon_lock(bm, uv, head, pts_sb, 0.068, 0.015, steps=12, w_root=0.85, push_pad=0.006)


def _style_boy_part(bm, uv, head, rnd):
    """Clean Korean 7/3 Comma Side-Part — smooth sculpted mass, plush C-comma bangs, sleek tapered back."""
    def _part_sculpt(th, tf, zf):
        # Slightly fuller left side from the +28° part, sleek close right side, clean smooth back
        vol_l = 0.012 * max(0.0, math.cos(th + 0.6)) * math.sin(tf * math.pi)
        flute = 0.003 * math.sin(14.0 * th) * math.sin(tf * math.pi)
        return (vol_l + flute, Vector((0, 0, 0)))

    _sculpt_mass(bm, uv, head, pad_base=0.020, z_front=0.58, z_back=-0.64,
                 part_deg=28, part_depth=0.013, crown_lift=0.024, sculpt_fn=_part_sculpt)

    # Big sleek comma sweep from +28° part curving gracefully across the forehead toward -X
    comma_main = [
        (28, 0.88, 2, 0.72, -26, 0.44, -46, 0.24, 0.118, 0.020),
        (24, 0.84, 6, 0.62, -10, 0.34, -22, 0.26, 0.092, 0.017),
        (26, 0.90, -18, 0.76, -54, 0.46, -68, 0.12, 0.105, 0.019),
    ]
    for a0, z0, a1, z1, a2, z2, a3, z3, w, h in comma_main:
        pts = [_p(head, a0, z0, 0.010), _p(head, a1, z1, 0.036), _p(head, a2, z2, 0.030), _p(head, a3, z3, 0.018)]
        _ribbon_lock(bm, uv, head, pts, w, h, steps=15, w_root=0.88, push_pad=0.006)

    # Shorter right comma swoop from +28° curving cleanly to right temple
    comma_side = [
        (30, 0.88, 50, 0.68, 62, 0.40, 56, 0.22, 0.095, 0.018),
        (34, 0.88, 62, 0.70, 76, 0.42, 76, 0.06, 0.092, 0.017),
    ]
    for a0, z0, a1, z1, a2, z2, a3, z3, w, h in comma_side:
        pts = [_p(head, a0, z0, 0.010), _p(head, a1, z1, 0.034), _p(head, a2, z2, 0.026), _p(head, a3, z3, 0.016)]
        _ribbon_lock(bm, uv, head, pts, w, h, steps=14, w_root=0.88, push_pad=0.006)


def _style_boy_fluffy(bm, uv, head, rnd):
    """Soft Wavy Fluffy Mop — sculpted cloud-like wavy dome + gentle scalloped wavy bangs (zero worm coils!)."""
    def _fluffy_sculpt(th, tf, zf):
        # Soft multi-lobe organic cloud undulations sculpted directly into a thick plush dome
        env_t = math.sin(min(1.0, tf) * math.pi * 0.95)
        w1 = 0.013 * math.sin(7.0 * th + 2.2 * tf) * env_t
        w2 = 0.008 * math.cos(11.0 * th - 3.0 * tf) * env_t
        crown_puff = 0.018 * (tf ** 0.9)
        return (w1 + w2 + crown_puff, Vector((0.0, 0.0, 0.010 * tf)))

    def _fluffy_low(th):
        back_w = 0.5 - 0.5 * math.cos(th)
        # Soft wavy scalloped hairline around forehead & nape
        scallop = 0.06 * math.sin(9.0 * th)
        return 0.42 + (-0.64 - 0.42) * (back_w ** 1.1) + scallop

    _sculpt_mass(bm, uv, head, pad_base=0.034, z_front=0.44, z_back=-0.64,
                 crown_lift=0.034, sculpt_fn=_fluffy_sculpt, z_low_fn=_fluffy_low, n_t=72, n_p=28)

    # Soft wavy overlapping bangs draping gently above brows (wide & plush, hugging the cloud dome)
    for i in range(6):
        th = -56.0 + 112.0 * (i / 5.0)
        sw = 10.0 if i % 2 == 0 else -10.0
        pts = [
            _p(head, th, 0.78, 0.020),
            _p(head, th + sw * 0.6, 0.56, 0.048),
            _p(head, th - sw * 0.2, 0.36, 0.044),
            _p(head, th + sw * 0.3, 0.24, 0.026),
        ]
        _ribbon_lock(bm, uv, head, pts, 0.095, 0.022, steps=14, w_root=0.90, tip_pow=1.5, push_pad=0.010)


def _style_girl(bm, uv, head, rnd):
    """Long Layered Silky Girl Hair — smooth sculpted crown & continuous wavy long drape + airy curtain bangs."""
    hh = head.hh
    def _girl_sculpt(th, tf, zf):
        return (0.003 * math.sin(14.0 * th) * math.sin(tf * math.pi), Vector((0, 0, 0)))

    # Raise z_front to 0.58 so bangs hide hairline completely!
    _sculpt_mass(bm, uv, head, pad_base=0.021, z_front=0.58, z_back=-0.82,
                 part_deg=20, part_depth=0.011, crown_lift=0.020, sculpt_fn=_girl_sculpt)

    # Continuous gap-free sculpted long hair drape with gentle vertical wave undulations (ZERO spaghetti tubes!)
    _sculpt_drape(bm, uv, head, th_min_deg=74, th_max_deg=286, length_hh=2.35,
                  flare_out=0.044, curl_in=0.0, pad_top=0.024, thick=0.028,
                  wave_amp=0.011, wave_n=6, n_u=48, n_v=18)

    # Graceful sleek cheek-framing long sidelocks (1 per side, hugging cheeks smoothly)
    for sx in (-1, 1):
        pts = [
            _p(head, sx * 64, 0.78, 0.014),
            _p(head, sx * 64, 0.16, 0.030),
            _p(head, sx * 62, -0.52, 0.032),
            Vector((head.r * 1.14 * math.sin(math.radians(sx * 58)), -head.r * 1.14 * math.cos(math.radians(sx * 58)), head.c.z - hh * 1.55)),
        ]
        _ribbon_lock(bm, uv, head, pts, 0.082, 0.018, steps=16, w_root=0.86, push_pad=0.008)

    # Airy arched curtain bangs parting cleanly at +20° (sleek, hugging forehead smoothly above brows)
    curtain = [
        (20, 0.88, -2, 0.70, -28, 0.44, -56, 0.22, 0.112, 0.019),
        (18, 0.82, 2, 0.60, -14, 0.34, -30, 0.26, 0.084, 0.016),
        (20, 0.88, 40, 0.70, 58, 0.44, 68, 0.18, 0.108, 0.019),
        (22, 0.82, 34, 0.60, 48, 0.34, 58, 0.26, 0.082, 0.016),
    ]
    for a0, z0, a1, z1, a2, z2, a3, z3, w, h in curtain:
        pts = [_p(head, a0, z0, 0.010), _p(head, a1, z1, 0.032), _p(head, a2, z2, 0.028), _p(head, a3, z3, 0.018)]
        _ribbon_lock(bm, uv, head, pts, w, h, steps=15, w_root=0.88, push_pad=0.007)


def _style_girl_bob(bm, uv, head, rnd):
    """Chic Rounded C-Curl Bob — adorable smooth volumetric bob hugging the cheeks & jaw + airy bangs."""
    _sculpt_mass(bm, uv, head, pad_base=0.022, z_front=0.58, z_back=-0.72,
                 part_deg=18, part_depth=0.010, crown_lift=0.022)

    # Unified plush C-curl bob drape (slightly wider front coverage so zero seam at cheeks!)
    _sculpt_drape(bm, uv, head, th_min_deg=58, th_max_deg=302, length_hh=1.54,
                  flare_out=0.044, curl_in=0.040, pad_top=0.024, thick=0.028,
                  wave_amp=0.006, wave_n=6, n_u=48, n_v=18)

    # Airy side-swept bangs seamlessly bridging the front hairline
    bangs = [
        (18, 0.88, -6, 0.70, -32, 0.44, -56, 0.24, 0.114, 0.019),
        (16, 0.82, 0, 0.58, -14, 0.34, -26, 0.26, 0.088, 0.016),
        (20, 0.88, 40, 0.70, 56, 0.44, 62, 0.22, 0.106, 0.018),
    ]
    for a0, z0, a1, z1, a2, z2, a3, z3, w, h in bangs:
        pts = [_p(head, a0, z0, 0.010), _p(head, a1, z1, 0.032), _p(head, a2, z2, 0.028), _p(head, a3, z3, 0.018)]
        _ribbon_lock(bm, uv, head, pts, w, h, steps=14, w_root=0.88, push_pad=0.007)


def _style_girl_ponytail(bm, uv, head, rnd):
    """High Dynamic Ponytail — sleek combed crown + soft flat-hugging bangs & wisps + scrunchie + lush tail."""
    r, hh = head.r, head.hh
    def _pony_sculpt(th, tf, zf):
        return (0.004 * math.sin(18.0 * th) * math.sin(tf * math.pi), Vector((0, 0, 0)))

    _sculpt_mass(bm, uv, head, pad_base=0.020, z_front=0.58, z_back=-0.64,
                 part_deg=16, part_depth=0.008, crown_lift=0.020, sculpt_fn=_pony_sculpt)

    # Sleek, flat-hugging arched bangs (zero raised brow puffs, zero dark cap band!)
    bangs = [
        (16, 0.88, -6, 0.70, -30, 0.44, -56, 0.24, 0.108, 0.018),
        (14, 0.82, -2, 0.58, -14, 0.36, -24, 0.28, 0.082, 0.015),
        (18, 0.88, 38, 0.70, 54, 0.44, 62, 0.22, 0.104, 0.018),
    ]
    for a0, z0, a1, z1, a2, z2, a3, z3, w, h in bangs:
        pts = [_p(head, a0, z0, 0.010), _p(head, a1, z1, 0.028), _p(head, a2, z2, 0.025), _p(head, a3, z3, 0.016)]
        _ribbon_lock(bm, uv, head, pts, w, h, steps=14, w_root=0.88, push_pad=0.006)

    # Delicate face-framing cheek wisps
    for sx in (-1, 1):
        pts_w = [
            _p(head, sx * 64, 0.62, 0.012),
            _p(head, sx * 60, 0.08, 0.024),
            _p(head, sx * 56, -0.50, 0.020),
            _p(head, sx * 50, -0.88, 0.014),
        ]
        _ribbon_lock(bm, uv, head, pts_w, 0.048, 0.013, steps=14, w_root=0.80, push_pad=0.006)

    # Hair scrunchie at high back crown
    tie_c = head.c + Vector((0.0, r * 1.05, hh * 0.66))
    tie_ax = Vector((0.0, 0.84, 0.54)).normalized()
    _sculpt_torus_ring(bm, uv, tie_c, tie_ax, major_r=r * 0.24, minor_r=r * 0.09, mat_idx=1)

    # Lush multi-layer cascading ponytail
    tail_specs = [
        (0.00, 0.14, 0.09, 0.38, 0.118, 0.044),
        (-0.044, 0.11, 0.06, 0.34, 0.094, 0.034),
        (0.044, 0.11, 0.06, 0.34, 0.094, 0.034),
        (-0.024, 0.08, 0.02, 0.30, 0.082, 0.030),
        (0.024, 0.08, 0.02, 0.30, 0.082, 0.030),
        (0.00, 0.16, 0.12, 0.28, 0.084, 0.028),
    ]
    for xs, ya, zl, ld, w, h in tail_specs:
        p0 = tie_c + Vector((xs * 0.25, -0.01, 0.0))
        p1 = tie_c + Vector((xs * 0.85, ya * 0.65, zl))
        p2 = tie_c + Vector((xs * 1.22, ya * 1.12, -ld * 0.38))
        p3 = tie_c + Vector((xs * 0.88, ya * 0.94, -ld * 0.85))
        p4 = tie_c + Vector((xs * 0.55, ya * 1.16, -ld))
        _ribbon_lock(bm, uv, head, [p0, p1, p2, p3, p4], w, h, steps=16, w_root=0.44, w_peak_t=0.38, push_pad=None)


def _style_old_man(bm, uv, head, rnd):
    """Distinguished Silver Elder — smooth combed silver horseshoe band hugging temples & fuller sculpted nape."""
    def _elder_sculpt(th, tf, zf):
        ang_abs = abs(math.degrees(math.atan2(math.sin(th), math.cos(th))))
        # Soft bushy puff above the ears (~92°) + fuller rounded back nape
        ear_puff = 0.022 * math.exp(-((ang_abs - 94.0) / 34.0) ** 2) * math.sin(tf * math.pi)
        back_vol = 0.014 * math.exp(-((ang_abs - 180.0) / 56.0) ** 2) * math.sin(tf * math.pi)
        # Subtle vertical/diagonal combed hair flutes (NEVER horizontal sweatband rings!)
        combed = 0.003 * math.sin(22.0 * th + 0.6 * tf) * math.sin(tf * math.pi)
        return (ear_puff + back_vol + combed, Vector((0, 0, 0)))

    def _elder_low(th):
        ang_abs = abs(math.degrees(math.atan2(math.sin(th), math.cos(th))))
        if ang_abs < 95.0:
            return -0.26 - 0.16 * math.exp(-((ang_abs - 72.0) / 18.0) ** 2)
        return -0.32 - 0.36 * ((ang_abs - 95.0) / 85.0) ** 1.05

    _sculpt_mass(bm, uv, head, pad_base=0.018, z_front=-0.24, z_back=-0.68,
                 crown_lift=0.003, sculpt_fn=_elder_sculpt, z_low_fn=_elder_low,
                 n_t=64, n_p=18, top_cutoff=0.28, skip_front_deg=56.0)


def _style_old_woman(bm, uv, head, rnd):
    """Warm Elegant Grandma — sleek parted combed-back silver hair + prominent sculpted coiled high bun."""
    r, hh = head.r, head.hh
    def _grandma_sculpt(th, tf, zf):
        ang_abs = abs(math.degrees(math.atan2(math.sin(th), math.cos(th))))
        # Subtle soft temple fullness without looking puffy like a chef hat
        temple_wave = 0.009 * math.exp(-((ang_abs - 72.0) / 34.0) ** 2) * math.sin(tf * math.pi)
        combed = 0.0035 * math.sin(18.0 * th) * math.sin(tf * math.pi)
        return (temple_wave + combed, Vector((0.0, 0.004 * tf, 0.0)))

    def _grandma_low(th):
        ang_abs = abs(math.degrees(math.atan2(math.sin(th), math.cos(th))))
        front_arch = 0.42 - 0.16 * math.sin(min(math.pi, math.radians(ang_abs * 1.4)))
        back_t = (ang_abs / 180.0) ** 1.25
        return front_arch * (1.0 - back_t) + (-0.64) * back_t

    _sculpt_mass(bm, uv, head, pad_base=0.018, z_front=0.42, z_back=-0.64,
                 part_deg=0, part_depth=0.011, crown_lift=0.014,
                 sculpt_fn=_grandma_sculpt, z_low_fn=_grandma_low, n_t=64, n_p=24)

    # Soft sleek parted curtain wave framing the upper forehead gently (hugging the crown!)
    for sx in (-1, 1):
        pts = [
            _p(head, sx * 4, 0.78, 0.012),
            _p(head, sx * 36, 0.60, 0.024),
            _p(head, sx * 74, 0.44, 0.022),
            _p(head, sx * 120, 0.50, 0.018),
        ]
        _ribbon_lock(bm, uv, head, pts, 0.084, 0.012, steps=14, w_root=0.90, push_pad=0.006)

    # Prominent iconic grandma bun sitting cleanly at upper back crown (visible in Front 3/4, Side & Back!)
    bun_c = head.c + Vector((0.0, r * 0.88, hh * 0.98))
    bun_ax = Vector((0.0, 0.58, 0.81)).normalized()
    _sculpt_torus_ring(bm, uv, bun_c - bun_ax * 0.045, bun_ax, major_r=r * 0.38, minor_r=r * 0.068, mat_idx=1)
    _sculpt_bun_dome(bm, uv, bun_c, bun_ax, r_xy=r * 0.54, r_z=r * 0.45, mat_idx=0)


_BUILDERS = {
    "boy": _style_boy,
    "boy_part": _style_boy_part,
    "boy_fluffy": _style_boy_fluffy,
    "girl": _style_girl,
    "girl_bob": _style_girl_bob,
    "girl_ponytail": _style_girl_ponytail,
    "old_man": _style_old_man,
    "old_woman": _style_old_woman,
}

_TIE_HEX = {
    "girl_ponytail": "#D94A4A",
    "old_woman": "#7A5D7A",
}


def build_lock_hair(char_info, style="boy", hair_hex=None, seed=1, tie_hex=None):
    if style not in _BUILDERS:
        raise ValueError(f"unknown hair style {style}; choose from {STYLES}")
    head = _ExactHead(char_info)
    rnd = random.Random(seed)
    bm = bmesh.new()
    uv = bm.loops.layers.uv.new("UVMap")
    _BUILDERS[style](bm, uv, head, rnd)

    arm, col = char_info["armature"], char_info["collection"]
    me = bpy.data.meshes.new(f"{arm.name}_SculptHair_M")
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me)
    bm.free()

    obj = bpy.data.objects.new(f"{arm.name}_SculptHair", me)
    col.objects.link(obj)
    obj.data.materials.append(make_lock_hair_mat(f"{arm.name}_SculptHairMat", hair_hex or DEFAULT_HEX[style]))
    if style in _TIE_HEX or tie_hex:
        obj.data.materials.append(make_lock_hair_mat(f"{arm.name}_HairTieMat", tie_hex or _TIE_HEX.get(style, "#C84B4B"), is_tie=True))
    obj.visible_shadow = False
    obj.parent = arm
    obj.matrix_parent_inverse.identity()
    vg = obj.vertex_groups.new(name="Head")
    vg.add(list(range(len(me.vertices))), 1.0, "REPLACE")
    obj.modifiers.new("Armature", "ARMATURE").object = arm
    return obj

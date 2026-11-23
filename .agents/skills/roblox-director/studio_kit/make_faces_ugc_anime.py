#!/usr/bin/env python3
"""
RETIRED (Law R-LOOK): kept for reference only. Use make_faces_expressive.py (storybook_toon / cartoon / rubberhose);
the quality-gate hook flags any new script that imports this file (ROBLOX_DIRECTOR.md section 4.1 rule 8).

make_faces_ugc_anime.py — 4x Supersampled (4096->1024) Multi-Archetype Roblox UGC Anime Face Generator.
Supports 6 distinct facial architectures (boy_youth, cool_rival, girl_heroine, femme_sharp, boss_elder, alien_cute)
+ optional facial marks (freckles, cheek_scar, under_eye_mole, bandaid) so every cast member looks truly unique!

Generates 12 expressive faces (neutral, happy, smile_closed, talk_mid, talk_open, blink,
laugh, angry, shocked, sad, smirk, scared) + a 4x3 atlas_preview.jpg.
"""
import argparse
import os
from PIL import Image, ImageDraw

S4 = 4096
INK = (24, 20, 28, 255)
WHITE = (255, 255, 255, 255)
SHADOW = (214, 224, 242, 255)
MOUTH_BG = (116, 22, 34, 255)
TONGUE = (238, 116, 132, 255)
BLUSH_PINK = (255, 130, 145, 135)
BLUSH_CORAL = (255, 142, 132, 145)
TEAR = (165, 224, 255, 235)

FACE_ARCHETYPES = {
    "boy_youth": {
        "rx": 545, "ry": 585, "pupil": 1.00, "lid_base": 0.0,
        "brow_w": 82, "brow_y": 0, "lash_wing": False, "cat_eye": False,
        "blush": True, "blush_col": BLUSH_PINK, "nose": "dot",
        "lip_col": None, "age_lines": False, "star_shine": False,
    },
    "cool_rival": {
        "rx": 565, "ry": 445, "pupil": 0.86, "lid_base": 0.22,
        "brow_w": 96, "brow_y": 140, "lash_wing": False, "cat_eye": True,
        "blush": False, "blush_col": None, "nose": "bridge",
        "lip_col": None, "age_lines": False, "star_shine": False,
    },
    "girl_heroine": {
        "rx": 540, "ry": 635, "pupil": 1.04, "lid_base": 0.0,
        "brow_w": 58, "brow_y": -30, "lash_wing": True, "cat_eye": False,
        "blush": True, "blush_col": BLUSH_CORAL, "nose": "tiny",
        "lip_col": "#D85A6F", "age_lines": False, "star_shine": True,
    },
    "femme_sharp": {
        "rx": 575, "ry": 470, "pupil": 0.85, "lid_base": 0.16,
        "brow_w": 54, "brow_y": 60, "lash_wing": True, "cat_eye": True,
        "blush": False, "blush_col": None, "nose": "bridge",
        "lip_col": "#9B1B30", "age_lines": False, "star_shine": False,
    },
    "boss_elder": {
        "rx": 485, "ry": 410, "pupil": 0.78, "lid_base": 0.20,
        "brow_w": 124, "brow_y": 180, "lash_wing": False, "cat_eye": False,
        "blush": False, "blush_col": None, "nose": "bridge",
        "lip_col": None, "age_lines": True, "star_shine": False,
    },
    "alien_cute": {
        "rx": 625, "ry": 690, "pupil": 1.12, "lid_base": 0.0,
        "brow_w": 42, "brow_y": -110, "lash_wing": False, "cat_eye": False,
        "blush": True, "blush_col": (120, 235, 190, 130), "nose": "none",
        "lip_col": None, "age_lines": False, "star_shine": True, "comedy": None,
    },
    # === COMEDY / MEME / SLAPSTICK ROBLOX STYLES ===
    "meme_sigma": {
        "rx": 465, "ry": 315, "pupil": 0.80, "lid_base": 0.28,
        "brow_w": 115, "brow_y": 140, "lash_wing": False, "cat_eye": True,
        "blush": False, "blush_col": None, "nose": "sigma",
        "lip_col": None, "age_lines": False, "star_shine": False, "comedy": "sigma",
    },
    "derp_goofy": {
        "rx": 575, "ry": 610, "pupil": 0.62, "lid_base": 0.0,
        "brow_w": 76, "brow_y": -20, "lash_wing": False, "cat_eye": False,
        "blush": True, "blush_col": BLUSH_PINK, "nose": "dot",
        "lip_col": None, "age_lines": False, "star_shine": False, "comedy": "derp",
    },
    "chill_smug": {
        "rx": 500, "ry": 395, "pupil": 0.58, "lid_base": 0.44,
        "brow_w": 72, "brow_y": 200, "lash_wing": False, "cat_eye": False,
        "blush": False, "blush_col": None, "nose": "tiny",
        "lip_col": None, "age_lines": False, "star_shine": False, "comedy": "chill",
    },
    "slapstick_toon": {
        "rx": 620, "ry": 655, "pupil": 0.48, "lid_base": 0.0,
        "brow_w": 92, "brow_y": -60, "lash_wing": False, "cat_eye": False,
        "blush": True, "blush_col": BLUSH_CORAL, "nose": "dot",
        "lip_col": None, "age_lines": False, "star_shine": False, "comedy": "slapstick",
    },
    "grumpy_boomer": {
        "rx": 490, "ry": 385, "pupil": 0.74, "lid_base": 0.30,
        "brow_w": 135, "brow_y": 180, "lash_wing": False, "cat_eye": False,
        "blush": False, "blush_col": None, "nose": "bridge",
        "lip_col": None, "age_lines": True, "star_shine": False, "comedy": "grumpy",
    },
}


def hex_rgba(h: str, a=255):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (a,)


def bezier_pts(p0, p1, p2, steps=48):
    return [
        ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0],
         (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1])
        for t in (i / steps for i in range(steps + 1))
    ]


def draw_tapered(draw, p0, p1, p2, w0, w1, w2, col, steps=56):
    pts = bezier_pts(p0, p1, p2, steps)
    for i, (x, y) in enumerate(pts):
        t = i / (len(pts) - 1)
        w = (w0 + (w1 - w0) * (t * 2)) if t < 0.5 else (w1 + (w2 - w1) * ((t - 0.5) * 2))
        r = max(2, w * 0.5)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=col)


def draw_anime_eye(
    d, cx, cy, iris_dark, iris_lite,
    rx=545, ry=585, look=(0, 0), pupil_scale=1.0, lid_top=0.0, lid_tilt=0.0,
    watery=False, is_left=True, lash_wing=False, cat_eye=False, star_shine=False
):
    m = Image.new("L", (S4, S4), 0)
    md = ImageDraw.Draw(m)
    md.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=255)
    if lid_top > 0.01:
        cut_y = cy - ry + 2 * ry * lid_top
        md.polygon([
            (cx - rx - 40, cy - ry - 40),
            (cx + rx + 40, cy - ry - 40),
            (cx + rx + 40, cut_y - lid_tilt),
            (cx - rx - 40, cut_y + lid_tilt),
        ], fill=0)

    layer = Image.new("RGBA", (S4, S4), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=WHITE)
    ld.chord([cx - rx + 20, cy - ry + 20, cx + rx - 20, cy + ry - 120], 190, 350, fill=SHADOW)

    ix = cx + look[0] * rx * 0.35
    iy = cy + int(ry * 0.06) + look[1] * ry * 0.30 + (ry * lid_top * 0.32)
    irx, iry = int(rx * 0.58 * pupil_scale), int(min(rx * 0.62, ry * 0.62) * pupil_scale)
    ld.ellipse([ix - irx, iy - iry, ix + irx, iy + iry], fill=iris_dark)
    ld.ellipse([ix - int(irx * 0.78), iy - int(iry * 0.65),
                ix + int(irx * 0.78), iy + int(iry * 0.78)], fill=iris_lite)
    pr = int(min(irx, iry) * 0.46)
    ld.ellipse([ix - pr, iy - pr - 8, ix + pr, iy + pr + 8], fill=INK)

    # Dual / triple anime catchlights
    g1 = max(24, int(irx * 0.25))
    g2 = max(14, int(irx * 0.14))
    ld.ellipse([ix - int(irx * 0.62), iy - int(iry * 0.66),
                ix - int(irx * 0.62) + g1 * 2, iy - int(iry * 0.66) + g1 * 2], fill=WHITE)
    ld.ellipse([ix + int(irx * 0.24), iy + int(iry * 0.28),
                ix + int(irx * 0.24) + g2 * 2, iy + int(iry * 0.28) + g2 * 2], fill=WHITE)
    if star_shine:
        g3 = max(12, int(irx * 0.11))
        ld.ellipse([ix + int(irx * 0.35), iy - int(iry * 0.52),
                    ix + int(irx * 0.35) + g3 * 2, iy - int(iry * 0.52) + g3 * 2], fill=WHITE)
    if watery:
        ld.chord([cx - rx + 40, cy + ry - 240, cx + rx - 40, cy + ry - 10], 0, 180, fill=TEAR)

    comp = Image.new("RGBA", (S4, S4), (0, 0, 0, 0))
    comp.paste(layer, (0, 0), m)
    d._image.alpha_composite(comp)

    out_im = Image.new("RGBA", (S4, S4), (0, 0, 0, 0))
    od = ImageDraw.Draw(out_im)
    od.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], outline=INK, width=48 if not cat_eye else 40)
    comp2 = Image.new("RGBA", (S4, S4), (0, 0, 0, 0))
    comp2.paste(out_im, (0, 0), m)
    d._image.alpha_composite(comp2)

    sgn = -1 if is_left else 1
    if lid_top <= 0.01:
        wing_up = -190 if cat_eye else -140
        draw_tapered(d, (cx - rx - 55, cy - 140), (cx, cy - ry - 110), (cx + rx + 55, cy - 140), 34, 108, 34, INK)
        if lash_wing:
            # Winged outer eyelashes for heroine / sharp femme styles
            ox = cx + sgn * (rx + 25)
            draw_tapered(d, (ox - sgn * 80, cy - 165), (ox + sgn * 70, cy + wing_up - 60), (ox + sgn * 165, cy + wing_up - 120), 68, 42, 8, INK)
            draw_tapered(d, (ox - sgn * 40, cy - 60), (ox + sgn * 50, cy - 120), (ox + sgn * 120, cy - 170), 42, 26, 6, INK)
    else:
        cut_y = cy - ry + 2 * ry * lid_top
        draw_tapered(d, (cx - rx - 45, cut_y + lid_tilt), (cx, cut_y - 36), (cx + rx + 45, cut_y - lid_tilt), 38, 96, 38, INK)
        if lash_wing:
            ox = cx + sgn * (rx + 20)
            oy = cut_y + (lid_tilt if is_left else -lid_tilt)
            draw_tapered(d, (ox - sgn * 60, oy), (ox + sgn * 70, oy - 75), (ox + sgn * 155, oy - 135), 62, 38, 8, INK)


def draw_features(d, spec: dict, blush_override=None, mark="none"):
    show_blush = spec["blush"] if blush_override is None else blush_override
    if show_blush and spec["blush_col"]:
        bc = spec["blush_col"]
        d.ellipse([360, 2460, 1080, 2780], fill=bc)
        d.ellipse([3016, 2460, 3736, 2780], fill=bc)
    nose = spec["nose"]
    if nose == "dot":
        d.ellipse([1990, 2420, 2106, 2490], fill=(178, 128, 116, 175))
    elif nose == "tiny":
        d.ellipse([2015, 2425, 2081, 2475], fill=(184, 132, 122, 155))
    elif nose == "bridge":
        draw_tapered(d, (2048, 2020), (2068, 2240), (2015, 2430), 16, 28, 18, (150, 102, 92, 185))
    elif nose == "sigma":
        # Angular Roblox Man Face nose & cleft chin!
        draw_tapered(d, (2035, 1780), (2085, 2190), (1995, 2395), 18, 34, 24, (130, 88, 76, 220))
        draw_tapered(d, (1920, 2380), (2048, 2465), (2176, 2380), 18, 32, 18, (130, 88, 76, 200))
        draw_tapered(d, (1960, 3510), (2048, 3465), (2136, 3510), 20, 42, 20, (130, 88, 76, 185))
    if spec["age_lines"]:
        # Crow's feet & subtle mature creases
        draw_tapered(d, (460, 1920), (580, 1890), (650, 1880), 8, 20, 12, (130, 88, 76, 175))
        draw_tapered(d, (470, 2020), (590, 1970), (660, 1950), 8, 18, 10, (130, 88, 76, 155))
        draw_tapered(d, (3636, 1920), (3516, 1890), (3446, 1880), 8, 20, 12, (130, 88, 76, 175))
        draw_tapered(d, (3626, 2020), (3506, 1970), (3436, 1950), 8, 18, 10, (130, 88, 76, 155))
        draw_tapered(d, (1440, 2600), (1380, 2840), (1410, 3080), 10, 22, 10, (140, 96, 84, 145))
        draw_tapered(d, (2656, 2600), (2716, 2840), (2686, 3080), 10, 22, 10, (140, 96, 84, 145))

    # Optional unique face mark
    if mark == "freckles":
        for fx, fy in [(620, 2500), (770, 2460), (920, 2520), (700, 2600), (860, 2610),
                       (3176, 2520), (3326, 2460), (3476, 2500), (3236, 2610), (3396, 2600)]:
            d.ellipse([fx - 26, fy - 22, fx + 26, fy + 22], fill=(158, 92, 68, 195))
    elif mark == "under_eye_mole":
        d.ellipse([3210, 2440, 3290, 2520], fill=INK)
    elif mark == "cheek_scar":
        draw_tapered(d, (540, 2420), (780, 2620), (980, 2760), 18, 34, 14, (175, 76, 78, 220))
        d.line([(650, 2460), (590, 2560)], fill=(175, 76, 78, 200), width=18)
        d.line([(810, 2580), (740, 2680)], fill=(175, 76, 78, 200), width=18)
    elif mark == "bandaid":
        d.rounded_rectangle([3000, 2490, 3660, 2710], radius=48, fill=(242, 224, 198, 255), outline=(180, 148, 118, 255), width=22)
        d.rectangle([3210, 2515, 3450, 2685], fill=(228, 204, 174, 255))


def draw_sweat(d, x=3540, y=980):
    d.polygon([(x, y), (x - 165, y + 460), (x + 165, y + 460)], fill=TEAR)
    d.ellipse([x - 168, y + 310, x + 168, y + 630], fill=TEAR, outline=(42, 92, 165, 255), width=34)


def draw_spiral_eye(d, cx, cy, radius=380):
    import math
    pts = []
    for i in range(int(6.2 * math.pi / 0.12)):
        t = i * 0.12
        rr = radius * (t / (6.2 * math.pi))
        pts.append((cx + rr * math.cos(t), cy + rr * math.sin(t)))
    d.line(pts, fill=INK, width=54, joint="curve")


def draw_anger_vein(d, cx=3460, cy=880):
    import math
    red = (228, 54, 62, 255)
    for a in (45, 135, 225, 315):
        r = math.radians(a)
        p0 = (cx + 75 * math.cos(r), cy + 75 * math.sin(r))
        p1 = (cx + 185 * math.cos(r + 0.45), cy + 185 * math.sin(r + 0.45))
        p2 = (cx + 265 * math.cos(r), cy + 265 * math.sin(r))
        draw_tapered(d, p0, p1, p2, 34, 42, 24, red, steps=24)


def generate_pack(
    out_dir: str,
    iris_dark_hex: str = "#20569E",
    iris_lite_hex: str = "#52AEF5",
    archetype: str = "boy_youth",
    brow_hex: str = "#18141C",
    lip_hex: str = None,
    mark: str = "none",
):
    spec = dict(FACE_ARCHETYPES.get(archetype, FACE_ARCHETYPES["boy_youth"]))
    os.makedirs(out_dir, exist_ok=True)
    idark = hex_rgba(iris_dark_hex)
    ilite = hex_rgba(iris_lite_hex)
    brow_col = hex_rgba(brow_hex)
    lip_tint = hex_rgba(lip_hex) if lip_hex else (hex_rgba(spec["lip_col"]) if spec["lip_col"] else None)

    rx, ry = spec["rx"], spec["ry"]
    p_sc = spec["pupil"]
    lid_b = spec["lid_base"]
    bw = spec["brow_w"]
    by = spec["brow_y"]
    lw = spec["lash_wing"]
    ce = spec["cat_eye"]
    ss = spec["star_shine"]
    com = spec.get("comedy")
    L, R = (1160, 1860), (2936, 1860)

    def make(name, fn):
        im = Image.new("RGBA", (S4, S4), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        fn(d)
        small = im.resize((1024, 1024), Image.Resampling.LANCZOS)
        small.save(os.path.join(out_dir, f"{name}.png"))
        return small

    def brow_pair(d, dy_l=0, dy_r=0, tilt_in=0, arch_up=0):
        if com == "sigma":
            # Iconic Man Face / Rock eyebrow raise (left low & intense, right cocked high)
            dy_l += 50; dy_r -= 140; tilt_in += 60
        elif com == "derp":
            # Crooked goofy eyebrows
            dy_l -= 110; dy_r += 120
        elif com == "grumpy":
            tilt_in += 210; dy_l += 80; dy_r += 80
            draw_tapered(d, (1940, 1180), (1960, 1340), (1950, 1480), 16, 26, 14, INK)
            draw_tapered(d, (2140, 1180), (2120, 1340), (2130, 1480), 16, 26, 14, INK)
        mid_w = bw
        end_w = max(22, int(bw * 0.42))
        d_in = tilt_in
        d_arch = arch_up
        draw_tapered(d, (560, 1040 + by + dy_l - d_in), (1160, 820 + by + dy_l - d_arch), (1740, 1000 + by + dy_l + d_in), end_w, mid_w, end_w, brow_col)
        draw_tapered(d, (2356, 1000 + by + dy_r + d_in), (2936, 820 + by + dy_r - d_arch), (3536, 1040 + by + dy_r - d_in), end_w, mid_w, end_w, brow_col)

    def eye_pair(d, look_l=(0.06, 0), look_r=(-0.06, 0), p_mult=1.0, lid_add=0.0, tilt=0, watery=False, rx_off=0, ry_off=0):
        if com == "derp":
            # Hilarious cross-eyed / walleyed derp asymmetry!
            draw_anime_eye(d, *L, idark, ilite, rx=rx + 35 + rx_off, ry=ry + 40 + ry_off, look=(-0.68, -0.18), pupil_scale=p_sc * p_mult, lid_top=max(0.0, lid_b + lid_add), is_left=True)
            draw_anime_eye(d, *R, idark, ilite, rx=rx - 65 + rx_off, ry=ry - 95 + ry_off, look=(0.68, 0.28), pupil_scale=p_sc * p_mult * 0.85, lid_top=max(0.0, lid_b + lid_add), is_left=False)
            return
        if com == "grumpy":
            look_l = (-0.32, 0.05); look_r = (-0.32, 0.05)
        draw_anime_eye(d, *L, idark, ilite, rx=rx + rx_off, ry=ry + ry_off, look=look_l, pupil_scale=p_sc * p_mult, lid_top=max(0.0, lid_b + lid_add), lid_tilt=-tilt, watery=watery, is_left=True, lash_wing=lw, cat_eye=ce, star_shine=ss)
        draw_anime_eye(d, *R, idark, ilite, rx=rx + rx_off, ry=ry + ry_off, look=look_r, pupil_scale=p_sc * p_mult, lid_top=max(0.0, lid_b + lid_add), lid_tilt=tilt, watery=watery, is_left=False, lash_wing=lw, cat_eye=ce, star_shine=ss)

    def m_happy_grin(d, h_bot=3420):
        if com == "derp":
            # Goofy lop-sided grin with 1 big buck tooth & tongue flopped out!
            d.pieslice([1340, 2460, 2756, h_bot], 0, 180, fill=MOUTH_BG, outline=INK, width=54)
            d.rectangle([1880, 2940, 2140, 3160], fill=WHITE, outline=INK, width=36)
            d.ellipse([2120, 3080, 2660, 3560], fill=TONGUE, outline=INK, width=44)
            d.line([(1340, 2940), (2756, 2940)], fill=INK, width=54)
            return
        d.pieslice([1340, 2460, 2756, h_bot], 0, 180, fill=MOUTH_BG, outline=INK, width=52)
        d.chord([1460, 2860, 2636, 3140], 0, 180, fill=WHITE)
        d.chord([1640, 3120, 2456, h_bot], 0, 180, fill=TONGUE)
        d.line([(1340, 2940), (2756, 2940)], fill=INK, width=52)

    def m_oval(d, rx_m=420, ry_m=320, cy_m=2960):
        d.ellipse([2048 - rx_m, cy_m - ry_m, 2048 + rx_m, cy_m + ry_m], fill=MOUTH_BG, outline=INK, width=52)
        d.chord([2048 - rx_m + 90, cy_m + 40, 2048 + rx_m - 90, cy_m + ry_m], 0, 180, fill=TONGUE)

    def m_closed_smile(d, curve=180):
        if com == "sigma":
            # Cocky crooked Man-Face smirk!
            draw_tapered(d, (1500, 2960), (2180, 3060), (2740, 2680), 34, 68, 30, INK)
            draw_tapered(d, (2620, 2600), (2740, 2680), (2760, 2800), 18, 28, 18, INK)
            return
        if com == "chill":
            # Iconic wide relaxed Chill Face smile
            draw_tapered(d, (1240, 2820), (2048, 3260), (2856, 2820), 34, 64, 34, INK)
            return
        if com == "derp":
            # Silly smile with cute pink tongue sticking out the side!
            draw_tapered(d, (1500, 2900), (2048, 3140), (2596, 2900), 34, 64, 34, INK)
            d.ellipse([2120, 2980, 2520, 3360], fill=TONGUE, outline=INK, width=42)
            draw_tapered(d, (2320, 3020), (2320, 3150), (2320, 3240), 14, 18, 12, INK)
            return
        if com == "grumpy":
            draw_tapered(d, (1520, 3120), (2048, 2820), (2576, 3120), 34, 62, 34, INK)
            return
        if lip_tint:
            d.polygon([(1560, 2920), (1860, 2840), (2048, 2890), (2236, 2840), (2536, 2920),
                       (2280, 3040 + curve // 2), (2048, 3080 + curve // 2), (1816, 3040 + curve // 2)], fill=lip_tint)
        draw_tapered(d, (1520, 2880), (2048, 2900 + curve), (2576, 2880), 28, 56, 28, INK)

    def f_neutral(d):
        draw_features(d, spec, mark=mark)
        eye_pair(d)
        brow_pair(d)
        m_closed_smile(d, curve=120)

    def f_happy(d):
        draw_features(d, spec, mark=mark)
        eye_pair(d, lid_add=-0.08)
        brow_pair(d, arch_up=70)
        m_happy_grin(d)

    def f_smile_closed(d):
        draw_features(d, spec, mark=mark)
        eye_pair(d)
        brow_pair(d, arch_up=40)
        m_closed_smile(d, curve=220)

    def f_talk_mid(d):
        draw_features(d, spec, mark=mark)
        eye_pair(d)
        brow_pair(d, arch_up=60)
        m_oval(d, rx_m=440, ry_m=225, cy_m=2960)

    def f_talk_open(d):
        draw_features(d, spec, mark=mark)
        eye_pair(d, lid_add=-0.06)
        brow_pair(d, arch_up=100)
        m_oval(d, rx_m=500, ry_m=360, cy_m=3010)
        if com in ("derp", "slapstick"):
            d.rectangle([1820, 2660, 2030, 2840], fill=WHITE, outline=INK, width=28)
            d.rectangle([2060, 2660, 2270, 2840], fill=WHITE, outline=INK, width=28)

    def f_blink(d):
        draw_features(d, spec, mark=mark)
        draw_tapered(d, (640, 1860), (1160, 2040), (1680, 1860), 34, 86, 34, INK)
        draw_tapered(d, (2416, 1860), (2936, 2040), (3456, 1860), 34, 86, 34, INK)
        brow_pair(d, dy_l=80, dy_r=80)
        m_closed_smile(d, curve=160)

    def f_laugh(d):
        draw_features(d, spec, mark=mark)
        draw_tapered(d, (660, 1540), (1680, 1860), (660, 2160), 40, 94, 40, INK)
        draw_tapered(d, (3436, 1540), (2416, 1860), (3436, 2160), 40, 94, 40, INK)
        brow_pair(d, arch_up=60)
        m_happy_grin(d, h_bot=3520)

    def f_angry(d):
        draw_features(d, spec, blush_override=False, mark=mark)
        eye_pair(d, p_mult=0.80, lid_add=0.14, tilt=140)
        brow_pair(d, tilt_in=260, dy_l=140, dy_r=140)
        d.chord([1400, 2660, 2696, 3480], 180, 360, fill=MOUTH_BG, outline=INK, width=52)
        d.chord([1540, 2900, 2556, 3220], 180, 360, fill=TONGUE)
        if com in ("slapstick", "grumpy", "derp"):
            draw_anger_vein(d, 3550, 720)

    def f_shocked(d):
        draw_features(d, spec, blush_override=False, mark=mark)
        if com == "slapstick":
            draw_spiral_eye(d, *L, radius=400)
            draw_spiral_eye(d, *R, radius=400)
            brow_pair(d, dy_l=-160, dy_r=-160, arch_up=200)
            m_oval(d, rx_m=380, ry_m=460, cy_m=3040)
            return
        if com == "chill":
            # Funny twist: Chill guy stays half-lidded and calm even when shocked!
            eye_pair(d, p_mult=0.65)
            brow_pair(d, dy_l=-60, dy_r=-60)
            m_oval(d, rx_m=240, ry_m=240, cy_m=2980)
            draw_sweat(d, 3540, 980)
            return
        eye_pair(d, p_mult=0.45, lid_add=-0.45, rx_off=35, ry_off=70)
        brow_pair(d, dy_l=-160, dy_r=-160, arch_up=220)
        m_oval(d, rx_m=330, ry_m=400, cy_m=3040)
        draw_sweat(d, 3540, 980)

    def f_sad(d):
        draw_features(d, spec, mark=mark)
        if com == "slapstick":
            # Waterfall cartoon crying streams!
            d.rectangle([920, 2020, 1400, 4096], fill=TEAR)
            d.rectangle([2696, 2020, 3176, 4096], fill=TEAR)
        eye_pair(d, look_l=(0, 0.2), look_r=(0, 0.2), lid_add=0.22, tilt=-130, watery=True)
        brow_pair(d, tilt_in=-180, dy_l=120, dy_r=120)
        draw_tapered(d, (1620, 3120), (2048, 2800), (2476, 3120), 32, 60, 32, INK)

    def f_smirk(d):
        draw_features(d, spec, blush_override=False, mark=mark)
        eye_pair(d, look_l=(0.20, 0), look_r=(0.20, 0), p_mult=0.90, lid_add=0.08, tilt=40)
        draw_tapered(d, (560, 1020 + by), (1160, 740 + by), (1740, 1000 + by), 34, bw, 30, brow_col)
        draw_tapered(d, (2356, 1140 + by), (2936, 1080 + by), (3536, 1040 + by), 34, bw, 30, brow_col)
        if com == "sigma":
            draw_tapered(d, (1500, 2960), (2180, 3060), (2740, 2680), 36, 70, 30, INK)
            return
        if lip_tint:
            d.polygon([(1640, 2940), (2180, 2960), (2620, 2760), (2220, 3100)], fill=lip_tint)
        draw_tapered(d, (1620, 2940), (2180, 3100), (2640, 2740), 32, 62, 28, INK)

    def f_scared(d):
        draw_features(d, spec, blush_override=False, mark=mark)
        eye_pair(d, p_mult=0.38, lid_add=-0.45, watery=True)
        brow_pair(d, tilt_in=-160)
        pts = [(1520, 3020), (1700, 2880), (1880, 3060), (2048, 2880), (2216, 3060), (2396, 2880), (2576, 3020)]
        for i in range(len(pts) - 1):
            d.line([pts[i], pts[i + 1]], fill=INK, width=52, joint="curve")
        draw_sweat(d, 3540, 980)

    names_fns = [
        ("neutral", f_neutral), ("happy", f_happy), ("smile_closed", f_smile_closed),
        ("talk_mid", f_talk_mid), ("talk_open", f_talk_open), ("blink", f_blink),
        ("laugh", f_laugh), ("angry", f_angry), ("shocked", f_shocked),
        ("sad", f_sad), ("smirk", f_smirk), ("scared", f_scared),
    ]
    thumbs = [(n, make(n, fn)) for n, fn in names_fns]

    tile = 320
    atlas = Image.new("RGB", (4 * tile, 3 * tile), (242, 200, 164))
    ad = ImageDraw.Draw(atlas)
    for idx, (n, im) in enumerate(thumbs):
        r, c = divmod(idx, 4)
        x0, y0 = c * tile, r * tile
        sm = im.resize((tile, tile), Image.Resampling.LANCZOS)
        atlas.paste(sm, (x0, y0), sm)
        ad.rectangle([x0 + 6, y0 + 6, x0 + 18 + len(n) * 9, y0 + 28], fill=(20, 22, 28))
        ad.text((x0 + 12, y0 + 10), n, fill=(254, 221, 48))
    atlas.save(os.path.join(out_dir, "atlas_preview.jpg"), quality=92)
    print(f"Generated {len(names_fns)} UGC Anime faces [{archetype}, mark={mark}] -> {out_dir}")


if __name__ == "__main__":
    default_out = os.path.join(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")), "assets", "faces_ugc_anime")
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=default_out)
    ap.add_argument("--iris-dark", default="#20569E")
    ap.add_argument("--iris-lite", default="#52AEF5")
    ap.add_argument("--archetype", choices=list(FACE_ARCHETYPES.keys()), default="boy_youth")
    ap.add_argument("--brow-hex", default="#18141C")
    ap.add_argument("--lip-hex", default=None)
    ap.add_argument("--mark", choices=["none", "freckles", "under_eye_mole", "cheek_scar", "bandaid"], default="none")
    args = ap.parse_args()
    generate_pack(args.out_dir, args.iris_dark, args.iris_lite, args.archetype, args.brow_hex, args.lip_hex, args.mark)

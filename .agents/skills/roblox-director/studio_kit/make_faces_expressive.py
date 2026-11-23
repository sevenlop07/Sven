#!/usr/bin/env python3
"""
make_faces_expressive.py — 4K->1024 Supersampled Expressive Cartoon & 1930s Rubberhose Roblox Face Pack.
Replaces legacy stiff faces with tapered calligraphic ink lines, curved eyelids, dimple creases,
pie-cut / starry / heart / popping eyes, full comedic & dramatic reactions, and lip-sync mouth shapes.
"""
import argparse
import math
import os
from PIL import Image, ImageDraw

S = 4
N = 1024 * S

INK_CARTOON = (36, 20, 14, 255)
INK_RETRO = (18, 16, 20, 255)
WHITE = (255, 255, 255, 255)
SCLERA_SHADE = (232, 224, 214, 255)
MOUTH_DARK = (74, 18, 26, 255)
TONGUE_RED = (234, 96, 86, 255)
TONGUE_HI = (248, 138, 124, 255)
TEAR_BLUE = (112, 206, 252, 235)
TEAR_EDGE = (42, 118, 182, 255)
LID_TAN = (224, 168, 122, 240)
BLUSH_PINK = (242, 110, 102, 150)
HEART_RED = (228, 66, 48, 255)

EL, ER, EY = 512 - 122, 512 + 122, 438
MY = 684


def P(x, y):
    return (x * S, y * S)


def _new():
    return Image.new("RGBA", (N, N), (0, 0, 0, 0))


def bez2(p0, p1, p2, n=48):
    return [
        (
            (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0],
            (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1],
        )
        for t in (i / n for i in range(n + 1))
    ]


def bez3(p0, p1, p2, p3, n=56):
    return [
        (
            (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0],
            (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1],
        )
        for t in (i / n for i in range(n + 1))
    ]


def taper_stroke(d, pts, w_max, col, min_frac=0.18):
    """Draw a smooth variable-width calligraphic ink stroke tapering toward both ends."""
    n = len(pts) - 1
    if n < 1:
        return
    for i in range(n + 1):
        t = i / max(1, n)
        profile = min_frac + (1.0 - min_frac) * math.sin(math.pi * t)
        r = 0.5 * w_max * profile * S
        x, y = P(*pts[i])
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)
    for i in range(n):
        t = (i + 0.5) / max(1, n)
        profile = min_frac + (1.0 - min_frac) * math.sin(math.pi * t)
        w = max(2, int(w_max * profile * S))
        d.line([P(*pts[i]), P(*pts[i + 1])], fill=col, width=w, joint="curve")


def draw_brow(d, cx, cy, span=120, arch=28, tilt_deg=0, w=22, col=INK_CARTOON):
    a = math.radians(tilt_deg)
    hx, hy = 0.5 * span * math.cos(a), 0.5 * span * math.sin(a)
    nx, ny = math.sin(a), -math.cos(a)
    p0 = (cx - hx, cy - hy)
    p2 = (cx + hx, cy + hy)
    p1 = (cx + nx * arch * 1.4, cy + ny * arch * 1.4)
    taper_stroke(d, bez2(p0, p1, p2), w, col, min_frac=0.22)


def draw_eye(
    d,
    cx,
    cy,
    rx=94,
    ry=122,
    look=(0.0, 0.0),
    pupil_scale=0.44,
    style="cartoon",
    lid_top=0.0,
    lid_bot=0.0,
    lid_tilt=0.0,
    lid_fill=None,
    pupil_col=None,
    glint="dot",
    ink=INK_CARTOON,
    outline_w=12,
):
    pcol = pupil_col or ink
    # Clipped eye interior
    mask = Image.new("L", (N, N), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([P(cx - rx, cy - ry), P(cx + rx, cy + ry)], fill=255)

    layer = _new()
    ld = ImageDraw.Draw(layer)
    ld.ellipse([P(cx - rx, cy - ry), P(cx + rx, cy + ry)], fill=WHITE)
    # Subtle warm upper sclera crescent depth
    ld.ellipse([P(cx - rx * 1.05, cy - ry * 1.15), P(cx + rx * 1.05, cy - ry * 0.45)], fill=SCLERA_SHADE)

    px = cx + look[0] * (rx * 0.46)
    py = cy + look[1] * (ry * 0.42)
    prx = rx * pupil_scale
    pry = ry * pupil_scale * (1.15 if style == "rubberhose" else 1.08)

    if glint == "pie":
        # Classic 1930s Pac-Man wedge pie-cut pupil!
        ld.pieslice([P(px - prx, py - pry), P(px + prx, py + pry)], start=318, end=272, fill=pcol)
    elif glint == "star":
        ld.ellipse([P(px - prx * 1.15, py - pry * 1.15), P(px + prx * 1.15, py + pry * 1.15)], fill=pcol)
        spts = []
        sr = prx * 0.72
        for k in range(8):
            ang = k * math.pi / 4.0
            rr = sr if k % 2 == 0 else sr * 0.30
            spts.append(P(px + rr * math.cos(ang), py + rr * math.sin(ang)))
        ld.polygon(spts, fill=WHITE)
    elif glint == "solid":
        # Viral Storybook-Toon high-contrast solid vertical oval pupil (0.2s mobile thumbnail readability)
        ld.ellipse([P(px - prx * 0.88, py - pry * 1.04), P(px + prx * 0.88, py + pry * 1.04)], fill=pcol)
    else:
        ld.ellipse([P(px - prx, py - pry), P(px + prx, py + pry)], fill=pcol)
        if glint == "dot":
            ld.ellipse([P(px - prx * 0.56, py - pry * 0.58), P(px - prx * 0.08, py - pry * 0.12)], fill=WHITE)
            ld.ellipse([P(px + prx * 0.16, py + pry * 0.18), P(px + prx * 0.40, py + pry * 0.42)], fill=WHITE)

    # Eyelid overlays inside sclera mask
    if lid_top > 0.01:
        yt = cy - ry + 2 * ry * lid_top
        lfill = lid_fill or (WHITE if style == "cartoon" else LID_TAN)
        poly_pts = [P(cx - rx - 10, cy - ry - 10), P(cx + rx + 10, cy - ry - 10), P(cx + rx + 10, yt - lid_tilt), P(cx - rx - 10, yt + lid_tilt)]
        ld.polygon(poly_pts, fill=lfill)
        ld.line([P(cx - rx - 6, yt + lid_tilt), P(cx + rx + 6, yt - lid_tilt)], fill=ink, width=int(outline_w * 0.9 * S))

    if lid_bot > 0.01:
        yb = cy + ry - 2 * ry * lid_bot
        bfill = lid_fill or (WHITE if style == "cartoon" else LID_TAN)
        poly_b = [P(cx - rx - 10, yb - lid_tilt * 0.5), P(cx + rx + 10, yb + lid_tilt * 0.5), P(cx + rx + 10, cy + ry + 10), P(cx - rx - 10, cy + ry + 10)]
        ld.polygon(poly_b, fill=bfill)
        ld.line([P(cx - rx - 6, yb - lid_tilt * 0.5), P(cx + rx + 6, yb + lid_tilt * 0.5)], fill=ink, width=int(outline_w * 0.85 * S))

    clipped = _new()
    clipped.paste(layer, (0, 0), mask)
    d._image.alpha_composite(clipped)
    d.ellipse([P(cx - rx, cy - ry), P(cx + rx, cy + ry)], outline=ink, width=int(outline_w * S))


def draw_closed_eye(d, cx, cy, w=120, arch=-34, col=INK_CARTOON, lw=15):
    taper_stroke(d, bez2((cx - w * 0.5, cy), (cx, cy + arch * 1.4), (cx + w * 0.5, cy)), lw, col, 0.22)


def draw_retro_nose(d, cx=512, cy=562, col=INK_RETRO):
    taper_stroke(d, bez2((cx - 18, cy - 10), (cx - 42, cy + 14), (cx + 12, cy + 28)), 10, col, 0.25)


def draw_mouth_open(d, cx, cy, w, h, teeth=True, tongue=True, shape="smile_d", ink=INK_CARTOON):
    if shape == "smile_d":
        top_pts = bez2((cx - w * 0.5, cy - h * 0.25), (cx, cy - h * 0.05), (cx + w * 0.5, cy - h * 0.25), 32)
        bot_pts = bez2((cx + w * 0.5, cy - h * 0.25), (cx, cy + h * 1.15), (cx - w * 0.5, cy - h * 0.25), 40)
        pts = top_pts + bot_pts[1:]
    elif shape == "grit":
        top_pts = bez2((cx - w * 0.5, cy - h * 0.15), (cx, cy - h * 0.45), (cx + w * 0.5, cy - h * 0.15), 28)
        bot_pts = bez2((cx + w * 0.5, cy + h * 0.15), (cx, cy + h * 0.45), (cx - w * 0.5, cy + h * 0.15), 28)
        pts = top_pts + bot_pts
    else:  # oval / shocked
        pts = [(cx + 0.5 * w * math.cos(t), cy + 0.5 * h * math.sin(t)) for t in (i * 2 * math.pi / 48 for i in range(48))]

    mask = Image.new("L", (N, N), 0)
    ImageDraw.Draw(mask).polygon([P(*p) for p in pts], fill=255)
    layer = _new()
    ld = ImageDraw.Draw(layer)
    ld.polygon([P(*p) for p in pts], fill=WHITE if shape == "grit" else MOUTH_DARK)

    ys = [p[1] for p in pts]
    top_y, bot_y = min(ys), max(ys)
    if shape == "grit":
        ld.line([P(cx - w, cy), P(cx + w, cy)], fill=ink, width=int(9 * S))
        for vx in range(int(cx - w * 0.36), int(cx + w * 0.40), int(max(36, w * 0.18))):
            ld.line([P(vx, top_y), P(vx, bot_y)], fill=ink, width=int(7 * S))
    else:
        if teeth:
            ld.rectangle([P(cx - w, top_y - 10), P(cx + w, top_y + (bot_y - top_y) * 0.28)], fill=WHITE)
            ld.line([P(cx - w, top_y + (bot_y - top_y) * 0.28), P(cx + w, top_y + (bot_y - top_y) * 0.28)], fill=ink, width=int(6 * S))
        if tongue:
            ld.ellipse([P(cx - w * 0.32, bot_y - (bot_y - top_y) * 0.44), P(cx + w * 0.32, bot_y + (bot_y - top_y) * 0.28)], fill=TONGUE_RED)

    clipped = _new()
    clipped.paste(layer, (0, 0), mask)
    d._image.alpha_composite(clipped)
    taper_stroke(d, pts + [pts[0]], 12, ink, 0.8)


def draw_cheek_dimples(d, cx, cy, spread, col=INK_CARTOON):
    for sgn in (-1, 1):
        px = cx + sgn * spread
        taper_stroke(d, bez2((px - sgn * 18, cy - 22), (px + sgn * 22, cy), (px - sgn * 14, cy + 22)), 9, col, 0.2)


def draw_heart(d, cx, cy, sz=72, col=HEART_RED, ink=INK_CARTOON):
    pts = []
    for i in range(60):
        t = 2 * math.pi * i / 60.0
        x = 16 * math.sin(t) ** 3
        y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        pts.append((cx + x * (sz / 18.0), cy + y * (sz / 18.0)))
    d.polygon([P(*p) for p in pts], fill=col)
    taper_stroke(d, pts + [pts[0]], 10, ink, 0.85)


def _draw_age_overlay(d, age: str, ink):
    """Add crisp mobile-readable age & cheek-blush details without cluttering eyes or lip-sync."""
    if age == "elder_man":
        wrink = (96, 54, 24, 235)
        for ry0, ry1, span, lw in ((170, 238, 195, 9), (206, 265, 160, 8), (240, 290, 120, 7)):
            d.arc([P(512 - span, ry0), P(512 + span, ry1)], 200, 340, fill=wrink, width=int(lw * S))
        # Soft white horseshoe mustache framing mouth + subtle cheek mole
        d.arc([P(392, MY - 74), P(632, MY + 74)], 195, 345, fill=(248, 250, 255, 240), width=int(15 * S))
        d.ellipse([P(256, MY + 18), P(280, MY + 42)], fill=(82, 48, 26, 220))
    elif age == "elder_woman":
        for sx in (EL - 115, ER + 115):
            d.ellipse([P(sx - 12, MY - 32), P(sx + 12, MY - 8)], fill=ink)


def render_face(name: str, style: str = "storybook_toon", age: str = "youth") -> Image.Image:
    im = _new()
    d = ImageDraw.Draw(im)
    d._image = im

    ink = INK_RETRO if style in ("rubberhose", "storybook_toon") else INK_CARTOON
    glint = "solid" if style == "storybook_toon" else ("pie" if style == "rubberhose" else "dot")
    es = 1.04 if style == "storybook_toon" else (0.94 if style == "rubberhose" else 1.0)

    if style == "storybook_toon":
        # Subtle warm/cold cheek blush anchors the character in cinema lighting
        b_col = (232, 114, 108, 72) if age != "elder_man" else (222, 132, 92, 58)
        for sx in (EL - 98, ER + 98):
            d.ellipse([P(sx - 56, EY + 116), P(sx + 56, EY + 158)], fill=b_col)
        _draw_age_overlay(d, age, ink)

    def nose():
        if style == "rubberhose":
            draw_retro_nose(d, 512, 558, ink)

    if name == "neutral":
        draw_eye(d, EL, EY, 88 * es, 114 * es, look=(0, 0.05), style=style, glint=glint, ink=ink)
        draw_eye(d, ER, EY, 88 * es, 114 * es, look=(0, 0.05), style=style, glint=glint, ink=ink)
        draw_brow(d, EL - 8, EY - 148, 128, 22, -6, 20, ink)
        draw_brow(d, ER + 8, EY - 148, 128, 22, 6, 20, ink)
        nose()
        taper_stroke(d, bez2((446, MY + 8), (512, MY + 22), (578, MY + 8)), 13, ink, 0.25)

    elif name in ("smile_closed", "happy"):
        draw_eye(d, EL, EY, 94 * es, 124 * es, look=(0.05, 0.08), style=style, glint="star" if (style == "rubberhose" and name == "happy") else glint, ink=ink)
        draw_eye(d, ER, EY, 94 * es, 124 * es, look=(-0.05, 0.08), style=style, glint="star" if (style == "rubberhose" and name == "happy") else glint, ink=ink)
        draw_brow(d, EL - 10, EY - 156, 132, 32, -10, 22, ink)
        draw_brow(d, ER + 10, EY - 156, 132, 32, 10, 22, ink)
        nose()
        if name == "smile_closed":
            taper_stroke(d, bez2((352, MY - 28), (512, MY + 88), (672, MY - 28)), 15, ink, 0.25)
            draw_cheek_dimples(d, 512, MY - 28, 174, ink)
            taper_stroke(d, bez2((462, MY + 74), (512, MY + 92), (562, MY + 74)), 8, ink, 0.2)
        else:
            draw_mouth_open(d, 512, MY + 8, 286, 148, teeth=True, tongue=True, shape="smile_d", ink=ink)
            draw_cheek_dimples(d, 512, MY - 34, 168, ink)

    elif name == "talk_mid":
        draw_eye(d, EL, EY, 90 * es, 118 * es, look=(0, 0), style=style, glint=glint, ink=ink)
        draw_eye(d, ER, EY, 90 * es, 118 * es, look=(0, 0), style=style, glint=glint, ink=ink)
        draw_brow(d, EL - 8, EY - 150, 126, 28, -8, 20, ink)
        draw_brow(d, ER + 8, EY - 150, 126, 28, 8, 20, ink)
        nose()
        draw_mouth_open(d, 512, MY + 18, 175, 92, teeth=True, tongue=True, shape="smile_d", ink=ink)

    elif name == "talk_open":
        draw_eye(d, EL, EY, 94 * es, 124 * es, look=(0, -0.05), style=style, glint=glint, ink=ink)
        draw_eye(d, ER, EY, 94 * es, 124 * es, look=(0, -0.05), style=style, glint=glint, ink=ink)
        draw_brow(d, EL - 8, EY - 160, 130, 34, -10, 20, ink)
        draw_brow(d, ER + 8, EY - 160, 130, 34, 10, 20, ink)
        nose()
        draw_mouth_open(d, 512, MY + 22, 165, 132, teeth=False, tongue=True, shape="oval", ink=ink)

    elif name == "laugh":
        draw_closed_eye(d, EL, EY + 14, 132, arch=-44, col=ink, lw=18)
        draw_closed_eye(d, ER, EY + 14, 132, arch=-44, col=ink, lw=18)
        draw_brow(d, EL - 10, EY - 134, 132, 34, -12, 22, ink)
        draw_brow(d, ER + 10, EY - 134, 132, 34, 12, 22, ink)
        nose()
        draw_mouth_open(d, 512, MY - 6, 336, 178, teeth=True, tongue=True, shape="smile_d", ink=ink)
        draw_cheek_dimples(d, 512, MY - 48, 188, ink)
        for sx in (EL - 110, ER + 110):
            d.ellipse([P(sx - 44, EY + 92), P(sx + 44, EY + 132)], fill=BLUSH_PINK)

    elif name == "wink":
        draw_eye(d, EL, EY, 94 * es, 122 * es, look=(0.08, 0.04), style=style, glint=glint, ink=ink)
        draw_closed_eye(d, ER, EY + 8, 128, arch=-38, col=ink, lw=16)
        draw_brow(d, EL - 12, EY - 158, 132, 34, -10, 22, ink)
        draw_brow(d, ER + 14, EY - 116, 124, 20, 16, 20, ink)
        nose()
        taper_stroke(d, bez2((356, MY - 14), (506, MY + 92), (682, MY - 36)), 15, ink, 0.25)
        draw_cheek_dimples(d, 512, MY - 24, 174, ink)

    elif name == "smirk":
        draw_eye(d, EL, EY + 6, 92 * es, 118 * es, look=(0.25, 0.05), lid_top=0.38, lid_tilt=-14, lid_fill=LID_TAN if style == "rubberhose" else WHITE, style=style, glint=glint, ink=ink)
        draw_eye(d, ER, EY + 6, 92 * es, 118 * es, look=(0.25, 0.05), lid_top=0.32, lid_tilt=10, lid_fill=LID_TAN if style == "rubberhose" else WHITE, style=style, glint=glint, ink=ink)
        draw_brow(d, EL - 8, EY - 126, 126, 14, 14, 24, ink)
        draw_brow(d, ER + 10, EY - 158, 128, 36, -12, 22, ink)
        nose()
        taper_stroke(d, bez2((412, MY + 14), (534, MY + 44), (666, MY - 24)), 14, ink, 0.24)
        taper_stroke(d, bez2((646, MY - 42), (674, MY - 24), (656, MY - 4)), 9, ink, 0.2)

    elif name in ("angry", "steam_angry"):
        draw_eye(d, EL, EY + 10, 92 * es, 112 * es, look=(0.18, 0.05), lid_top=0.28, lid_tilt=-34, style=style, glint=glint, ink=ink)
        draw_eye(d, ER, EY + 10, 92 * es, 112 * es, look=(-0.18, 0.05), lid_top=0.28, lid_tilt=34, style=style, glint=glint, ink=ink)
        draw_brow(d, EL + 16, EY - 102, 152, 16, 26, 28, ink)
        draw_brow(d, ER - 16, EY - 102, 152, 16, -26, 28, ink)
        nose()
        if name == "angry":
            draw_mouth_open(d, 512, MY + 18, 310, 110, shape="grit", ink=ink)
            draw_cheek_dimples(d, 512, MY + 18, 178, ink)
        else:
            taper_stroke(d, bez2((388, MY + 44), (512, MY - 14), (636, MY + 44)), 16, ink, 0.3)
            # Bold comic anger steam puffs shooting from cheeks
            for sgn in (-1, 1):
                px, py = 512 + sgn * 185, MY - 30
                d.ellipse([P(px - 52, py - 34), P(px + 52, py + 34)], fill=(255, 255, 255, 240), outline=ink, width=int(8 * S))
                d.ellipse([P(px + sgn * 68 - 34, py + 14 - 24), P(px + sgn * 68 + 34, py + 14 + 24)], fill=(255, 255, 255, 240), outline=ink, width=int(7 * S))
                taper_stroke(d, bez2((px - sgn * 48, py - 6), (px - sgn * 12, py - 14), (px + sgn * 10, py - 4)), 6, ink, 0.3)

    elif name == "shocked":
        draw_eye(d, EL - 8, EY - 12, 106, 138, look=(0, 0), pupil_scale=0.26, style=style, glint=glint, ink=ink)
        draw_eye(d, ER + 8, EY - 12, 106, 138, look=(0, 0), pupil_scale=0.26, style=style, glint=glint, ink=ink)
        draw_brow(d, EL - 12, EY - 190, 132, 38, -14, 22, ink)
        draw_brow(d, ER + 12, EY - 190, 132, 38, 14, 22, ink)
        nose()
        draw_mouth_open(d, 512, MY + 36, 152, 184, teeth=True, tongue=True, shape="oval", ink=ink)

    elif name == "pop_eyes":
        # Classic comic/rubberhose bugging-out cylinder/bulge eyes + screaming jaw!
        for cx_p, sgn in ((EL - 34, -1), (ER + 34, 1)):
            d.rounded_rectangle([P(cx_p - 122, EY - 82), P(cx_p + 122, EY + 82)], radius=78 * S, fill=WHITE, outline=ink, width=int(12 * S))
            draw_eye(d, cx_p + sgn * 30, EY, 72, 76, look=(sgn * 0.25, 0), pupil_scale=0.34, style=style, glint="star" if style == "rubberhose" else "dot", ink=ink, outline_w=10)
        draw_brow(d, EL - 30, EY - 152, 136, 38, -16, 22, ink)
        draw_brow(d, ER + 30, EY - 152, 136, 38, 16, 22, ink)
        draw_mouth_open(d, 512, MY + 44, 260, 180, teeth=True, tongue=True, shape="smile_d", ink=ink)

    elif name in ("sad", "cry"):
        draw_eye(d, EL, EY + 14, 88 * es, 112 * es, look=(0, 0.25), lid_top=0.34 if name == "sad" else 0.16, lid_tilt=28, style=style, glint=glint, ink=ink)
        draw_eye(d, ER, EY + 14, 88 * es, 112 * es, look=(0, 0.25), lid_top=0.34 if name == "sad" else 0.16, lid_tilt=-28, style=style, glint=glint, ink=ink)
        draw_brow(d, EL - 12, EY - 124, 132, 22, -24, 22, ink)
        draw_brow(d, ER + 12, EY - 124, 132, 22, 24, 22, ink)
        nose()
        if name == "sad":
            taper_stroke(d, bez2((414, MY + 44), (512, MY - 26), (610, MY + 44)), 14, ink, 0.25)
        else:
            for cx_t, sgn in ((EL - 28, -1), (ER + 28, 1)):
                pts_t = bez2((cx_t, EY + 74), (cx_t + sgn * 84, EY + 116), (cx_t + sgn * 124, EY + 196)) + bez2((cx_t + sgn * 124, EY + 196), (cx_t + sgn * 44, EY + 144), (cx_t - sgn * 14, EY + 96))
                d.polygon([P(*p) for p in pts_t], fill=TEAR_BLUE, outline=TEAR_EDGE, width=int(6 * S))
            draw_mouth_open(d, 512, MY + 26, 210, 96, teeth=True, tongue=False, shape="oval", ink=ink)

    elif name == "scared":
        draw_eye(d, EL, EY, 96 * es, 126 * es, look=(0.24, 0.08), pupil_scale=0.28, style=style, glint=glint, ink=ink)
        draw_eye(d, ER, EY, 96 * es, 126 * es, look=(0.24, 0.08), pupil_scale=0.28, style=style, glint=glint, ink=ink)
        draw_brow(d, EL - 12, EY - 156, 134, 14, -22, 22, ink)
        draw_brow(d, ER + 12, EY - 156, 134, 14, 22, 22, ink)
        nose()
        wavy = [(376 + i * 272 / 6.0, MY + (22 if i % 2 == 0 else -18)) for i in range(7)]
        taper_stroke(d, wavy, 13, ink, 0.35)

    elif name == "silly_tongue":
        draw_eye(d, EL, EY, 94 * es, 124 * es, look=(0.15, -0.35), style=style, glint=glint, ink=ink)
        draw_eye(d, ER, EY, 94 * es, 124 * es, look=(-0.15, -0.35), style=style, glint=glint, ink=ink)
        draw_brow(d, EL - 10, EY - 166, 126, 36, -12, 22, ink)
        draw_brow(d, ER + 10, EY - 146, 126, 26, 8, 22, ink)
        nose()
        taper_stroke(d, bez2((358, MY - 14), (512, MY + 72), (666, MY - 14)), 14, ink, 0.25)
        draw_cheek_dimples(d, 512, MY - 16, 168, ink)
        t_pts = bez2((476, MY + 28), (470, MY + 168), (558, MY + 152)) + bez2((558, MY + 152), (596, MY + 114), (562, MY + 24))
        d.polygon([P(*p) for p in t_pts], fill=TONGUE_RED)
        taper_stroke(d, t_pts + [t_pts[0]], 11, ink, 0.85)
        taper_stroke(d, bez2((522, MY + 36), (528, MY + 92), (522, MY + 122)), 7, ink, 0.2)

    elif name == "heart_eyes":
        draw_brow(d, EL - 12, EY - 142, 126, 32, -10, 22, ink)
        draw_brow(d, ER + 12, EY - 142, 126, 32, 10, 22, ink)
        draw_heart(d, EL, EY + 8, sz=88, ink=ink)
        draw_heart(d, ER, EY + 8, sz=88, ink=ink)
        nose()
        taper_stroke(d, bez2((412, MY - 12), (512, MY + 66), (612, MY - 12)), 14, ink, 0.25)
        for sx in (EL - 102, ER + 102):
            d.ellipse([P(sx - 40, EY + 104), P(sx + 40, EY + 140)], fill=BLUSH_PINK)

    elif name == "exhausted":
        draw_eye(d, EL, EY + 8, 90 * es, 114 * es, look=(0, 0.12), lid_top=0.48, lid_fill=LID_TAN, style=style, glint=glint, ink=ink)
        draw_eye(d, ER, EY + 8, 90 * es, 114 * es, look=(0, 0.12), lid_top=0.48, lid_fill=LID_TAN, style=style, glint=glint, ink=ink)
        draw_brow(d, EL - 8, EY - 114, 126, 10, -10, 18, ink)
        draw_brow(d, ER + 8, EY - 114, 126, 10, 10, 18, ink)
        nose()
        taper_stroke(d, bez2((436, MY + 22), (512, MY + 2), (588, MY + 22)), 12, ink, 0.25)

    elif name == "dizzy":
        for cx_d in (EL, ER):
            pts_sp = []
            for i in range(120):
                t = i * 6.0 * math.pi / 120.0
                rr = 82.0 * (i / 120.0)
                pts_sp.append((cx_d + rr * math.cos(t), EY + rr * math.sin(t)))
            taper_stroke(d, pts_sp, 14, ink, 0.65)
        draw_brow(d, EL - 8, EY - 134, 124, 24, -14, 20, ink)
        draw_brow(d, ER + 8, EY - 134, 124, 24, 14, 20, ink)
        nose()
        wavy = [(390 + i * 244 / 5.0, MY + (18 if i % 2 == 0 else -18)) for i in range(6)]
        taper_stroke(d, wavy, 12, ink, 0.35)

    elif name == "blink":
        draw_closed_eye(d, EL, EY + 14, 124, arch=24, col=ink, lw=15)
        draw_closed_eye(d, ER, EY + 14, 124, arch=24, col=ink, lw=15)
        draw_brow(d, EL - 8, EY - 138, 124, 22, -6, 18, ink)
        draw_brow(d, ER + 8, EY - 138, 124, 22, 6, 18, ink)
        nose()
        taper_stroke(d, bez2((446, MY + 8), (512, MY + 22), (578, MY + 8)), 13, ink, 0.25)

    # Frame boldly (k=1.42 around facial center) so eyes & mouth read big and crisp on 35deg Roblox head UV
    k = 1.42
    cx_f, cy_f = 512 * S, 542 * S
    big = im.resize((int(N * k), int(N * k)), Image.Resampling.LANCZOS)
    ox, oy = int(cx_f * k - 512 * S), int(cy_f * k - 512 * S)
    im = big.crop((ox, oy, ox + N, oy + N))
    return im.resize((1024, 1024), Image.Resampling.LANCZOS)


ALL_EXPRESSIONS = [
    "neutral", "happy", "smile_closed", "talk_mid", "talk_open",
    "laugh", "wink", "smirk", "angry", "steam_angry",
    "shocked", "pop_eyes", "sad", "cry", "scared",
    "silly_tongue", "heart_eyes", "exhausted", "dizzy", "blink",
]


def generate_pack(out_dir: str, style: str = "storybook_toon", age: str = "youth"):
    os.makedirs(out_dir, exist_ok=True)
    thumbs = []
    for name in ALL_EXPRESSIONS:
        im = render_face(name, style=style, age=age)
        im.save(os.path.join(out_dir, f"{name}.png"))
        thumbs.append((name, im))

    # Render clean preview atlas on warm Roblox skin backdrop
    tile = 280
    cols, rows = 5, 4
    atlas = Image.new("RGB", (cols * tile, rows * tile), (242, 200, 164))
    ad = ImageDraw.Draw(atlas)
    for idx, (n, im) in enumerate(thumbs):
        r, c = divmod(idx, cols)
        x0, y0 = c * tile, r * tile
        sm = im.resize((tile, tile), Image.Resampling.LANCZOS)
        atlas.paste(sm, (x0, y0), sm)
        ad.rectangle([x0 + 6, y0 + 6, x0 + 18 + len(n) * 7, y0 + 24], fill=(22, 18, 22))
        ad.text((x0 + 10, y0 + 9), n, fill=(254, 224, 60))
    atlas.save(os.path.join(out_dir, "atlas_preview.jpg"), quality=92)
    print(f"Generated {len(thumbs)} expressive faces [style={style}, age={age}] -> {out_dir}")


if __name__ == "__main__":
    base = os.path.join(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")), "assets")
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", choices=["storybook_toon", "cartoon", "rubberhose", "all"], default="all")
    ap.add_argument("--age", choices=["youth", "elder_man", "elder_woman"], default="youth")
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()
    if args.style == "all":
        generate_pack(os.path.join(base, "faces_storybook_toon"), "storybook_toon", args.age)
        generate_pack(os.path.join(base, "faces_cartoon"), "cartoon", args.age)
        generate_pack(os.path.join(base, "faces_rubberhose"), "rubberhose", args.age)
    else:
        out = args.out_dir or os.path.join(base, f"faces_{args.style}")
        generate_pack(out, args.style, args.age)

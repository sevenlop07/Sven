#!/usr/bin/env python3
"""
checks.py — Cross-platform (Windows & macOS) Preview Contact Sheet Generator for @RobloxDirector.
Replaces legacy Mac-only checks.sh. Builds a cleanly labeled grid contact sheet from preview images
so Stage R4 check sheets can be visually inspected in 1 read_file call.

Usage:
  python checks.py <preview_dir> <out_sheet.jpg> [--cols 4] [--aspect 9:16|16:9]
"""
import argparse
import math
import os
from PIL import Image, ImageDraw, ImageFont


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("preview_dir")
    ap.add_argument("out_sheet")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--aspect", choices=["9:16", "16:9"], default="9:16")
    args = ap.parse_args()

    imgs = sorted(
        f for f in os.listdir(args.preview_dir)
        if f.lower().endswith((".png", ".jpg", ".jpeg")) and not f.startswith("chk_sheet")
    )
    if not imgs:
        raise SystemExit(f"No preview images found in {args.preview_dir}")

    tw, th = (480, 270) if args.aspect == "16:9" else (300, 534)
    cols = min(args.cols, len(imgs))
    rows = math.ceil(len(imgs) / cols)
    sheet = Image.new("RGB", (cols * tw, rows * th), (18, 20, 26))
    draw = ImageDraw.Draw(sheet)

    try:
        font = ImageFont.truetype("arialbd.ttf", 20)
    except Exception:
        font = ImageFont.load_default()

    for idx, fname in enumerate(imgs):
        im = Image.open(os.path.join(args.preview_dir, fname)).convert("RGB")
        im.thumbnail((tw, th), Image.Resampling.LANCZOS)
        tile = Image.new("RGB", (tw, th), (18, 20, 26))
        ox = (tw - im.width) // 2
        oy = (th - im.height) // 2
        tile.paste(im, (ox, oy))

        r, c = divmod(idx, cols)
        x0, y0 = c * tw, r * th
        sheet.paste(tile, (x0, y0))

        label = os.path.splitext(fname)[0]
        draw.rectangle([x0 + 6, y0 + 6, x0 + 18 + len(label) * 11, y0 + 34], fill=(0, 0, 0))
        draw.text((x0 + 12, y0 + 10), label, fill=(254, 221, 48), font=font)

    os.makedirs(os.path.dirname(os.path.abspath(args.out_sheet)), exist_ok=True)
    sheet.save(args.out_sheet, quality=92)
    print(f"Saved check sheet ({len(imgs)} shots, {cols}x{rows}) -> {args.out_sheet}")


if __name__ == "__main__":
    main()

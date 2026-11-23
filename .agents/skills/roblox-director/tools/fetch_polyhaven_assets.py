#!/usr/bin/env python3
"""
fetch_polyhaven_assets.py — PolyHaven CC0 1K Asset Downloader & Real-Time GPU Budget Guard
==========================================================================================
Downloads and caches lightweight, high-detail CC0 assets from https://api.polyhaven.com into:
  .agents/skills/roblox-director/assets/polyhaven/
    ├── models/<asset_id>/<asset_id>_1k.gltf (+ .bin + textures/*.jpg)
    ├── textures/<tex_id>/<tex_id>_diff_1k.jpg (+ rough_1k.jpg + nor_gl_1k.jpg)
    └── hdris/<hdri_id>/<hdri_id>_1k.hdr (or 2k.hdr)

Enforces a strict --max-mb (default 25 MB per model) so ultra-heavy 500MB+ VFX hero scans
are never pulled into real-time EEVEE Next scenes.
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
POLYHAVEN_DIR = os.path.normpath(os.path.join(HERE, "..", "assets", "polyhaven"))
UA = "SvenPolyHavenManager/1.0 (https://sven.local; studio@sven.local)"

# Curated lightweight (< 25 MB) high-detail PolyHaven CC0 Nature Pack
NATURE_CORE_MODELS = [
    "rock_moss_set_01",       # 1.85 MB - Photoscanned mossy forest rocks set 1
    "rock_moss_set_02",       # 1.85 MB - Photoscanned mossy forest rocks set 2
    "boulder_01",             # 5.50 MB - Photoscanned creek boulder
    "rock_face_01",           # 2.91 MB - Photoscanned rocky cliff face 1 (waterfalls/canyons)
    "rock_face_02",           # 3.36 MB - Photoscanned rocky cliff face 2
    "mountainside",           # 7.04 MB - Photoscanned 3D mountain peak/ridge
    "rock_07",                # 2.08 MB - Detailed natural rock 07
    "stone_01",               # 3.55 MB - River stone 01
    "dead_tree_trunk",        # 4.57 MB - Fallen mossy forest log
    "tree_stump_01",          # 3.76 MB - Mossy forest tree stump
    "dry_branches_medium_01", # 3.10 MB - Natural dry forest branches / firewood
    "fern_02",                # 1.09 MB - Lush forest fern cluster
    "grass_medium_01",        # 2.92 MB - Alpine meadow grass clump 01
    "grass_medium_02",        # 0.76 MB - Alpine meadow grass clump 02
    "celandine_01",           # 1.45 MB - Yellow wildflower cluster
    "dandelion_01",           # 2.96 MB - White/yellow dandelion wildflowers
    "moss_01",                # 0.88 MB - Lush 3D ground moss patch
    "shrub_02",               # 1.88 MB - Forest bush / shrub 02
    "shrub_03",               # 1.55 MB - Forest bush / shrub 03
    "pine_sapling_small",     # 20.88 MB - Young pine tree with real bark & needle branches
]

NATURE_CORE_TEXTURES = [
    "brown_mud_leaves_01",    # Wet mud & forest leaves PBR terrain
    "forest_ground_04",       # Pine forest floor PBR terrain
    "aerial_grass_rock",      # Alpine grass & rock PBR terrain
    "rock_face_03",           # Wet slate cliff PBR texture
    "bark_brown_02",          # Conifer pine bark PBR texture
    "snow_02",                # Alpine snow PBR texture
]

NATURE_CORE_HDRIS = [
    "kloofendal_48d_partly_cloudy_puresky",  # Crisp daylight pure sky with natural clouds
    "kloppenheim_06_puresky",                # Warm sunset / golden-hour pure sky
]


def _api_get(path: str) -> dict:
    url = f"https://api.polyhaven.com/{path.lstrip('/')}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def _download_file(url: str, dest: str) -> int:
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 256:
        return os.path.getsize(dest)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
        data = r.read()
        f.write(data)
    return len(data)


def fetch_model(asset_id: str, res: str = "1k", max_mb: float = 25.0) -> str:
    model_dir = os.path.join(POLYHAVEN_DIR, "models", asset_id)
    gltf_path = os.path.join(model_dir, f"{asset_id}_{res}.gltf")
    if os.path.exists(gltf_path) and os.path.getsize(gltf_path) > 256:
        print(f"[PolyHaven Model] Cached: {asset_id} -> {gltf_path}")
        return gltf_path

    files = _api_get(f"files/{asset_id}")
    if "gltf" not in files or res not in files["gltf"]:
        raise RuntimeError(f"Model '{asset_id}' does not offer gltf/{res} on PolyHaven.")
    info = files["gltf"][res]["gltf"]
    inc = info.get("include", {})
    total_bytes = info["size"] + sum(v["size"] for v in inc.values())
    total_mb = total_bytes / (1024.0 * 1024.0)
    if total_mb > max_mb:
        raise ValueError(
            f"Model '{asset_id}' is {total_mb:.1f} MB (> --max-mb {max_mb:.1f} MB GPU budget). Skipped."
        )

    _download_file(info["url"], gltf_path)
    for rel_path, meta in inc.items():
        inc_dest = os.path.join(model_dir, rel_path.replace("/", os.sep))
        _download_file(meta["url"], inc_dest)

    print(f"[PolyHaven Model] Downloaded {asset_id} ({total_mb:.2f} MB, {len(inc)+1} files)")
    return gltf_path


def fetch_texture(tex_id: str, res: str = "1k") -> dict:
    tex_dir = os.path.join(POLYHAVEN_DIR, "textures", tex_id)
    os.makedirs(tex_dir, exist_ok=True)
    files = _api_get(f"files/{tex_id}")

    out_paths = {}
    # Fetch Diffuse/Color, Roughness, and OpenGL Normal in JPG format for fast VRAM loading
    map_keys = [
        ("diff", ("Diffuse", "col_1", "col_01", "Color")),
        ("rough", ("Rough",)),
        ("nor_gl", ("nor_gl",)),
    ]
    for short_name, candidates in map_keys:
        for cand in candidates:
            if cand in files and res in files[cand]:
                fmt_map = files[cand][res]
                chosen_fmt = "jpg" if "jpg" in fmt_map else ("png" if "png" in fmt_map else next(iter(fmt_map)))
                info = fmt_map[chosen_fmt]
                dest = os.path.join(tex_dir, f"{tex_id}_{short_name}_{res}.{chosen_fmt}")
                _download_file(info["url"], dest)
                out_paths[short_name] = dest
                break

    print(f"[PolyHaven Texture] Ready: {tex_id} ({list(out_paths.keys())})")
    return out_paths


def fetch_hdri(hdri_id: str, res: str = "2k") -> str:
    hdri_dir = os.path.join(POLYHAVEN_DIR, "hdris")
    os.makedirs(hdri_dir, exist_ok=True)
    dest = os.path.join(hdri_dir, f"{hdri_id}_{res}.hdr")
    if os.path.exists(dest) and os.path.getsize(dest) > 1024:
        print(f"[PolyHaven HDRI] Cached: {hdri_id} -> {dest}")
        return dest

    files = _api_get(f"files/{hdri_id}")
    if "hdri" in files and res in files["hdri"]:
        fmt_map = files["hdri"][res]
        ext = "hdr" if "hdr" in fmt_map else next(iter(fmt_map))
        dest = os.path.join(hdri_dir, f"{hdri_id}_{res}.{ext}")
        sz = _download_file(fmt_map[ext]["url"], dest)
        print(f"[PolyHaven HDRI] Downloaded {hdri_id} ({sz / (1024*1024):.2f} MB)")
        return dest
    raise RuntimeError(f"HDRI '{hdri_id}' not found at resolution {res}")


def inspect_in_blender():
    import subprocess
    sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "blender-core", "scripts")))
    from run_in_blender import find_blender
    exe = find_blender()
    kit_dir = os.path.normpath(os.path.join(HERE, "..", "studio_kit")).replace("\\", "/")
    expr = (
        f"import bpy, sys; sys.path.insert(0, '{kit_dir}'); import blender_env_lighting as env\n"
        f"for aid in {repr(NATURE_CORE_MODELS)}:\n"
        f"    objs = env.load_polyhaven_template(aid)\n"
        f"    dims = [(round(o.dimensions.x,2), round(o.dimensions.y,2), round(o.dimensions.z,2)) for o in objs[:3]]\n"
        f"    polys = sum(len(o.data.polygons) for o in objs)\n"
        f"    print(f'{{aid:24s}} | {{len(objs):2d}} meshes | {{polys:6d}} polys | dims={{dims}}')\n"
    )
    subprocess.run([exe, "-b", "--factory-startup", "--python-expr", expr], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preset", choices=["nature_core"], default="nature_core")
    ap.add_argument("--models", nargs="*", default=[])
    ap.add_argument("--textures", nargs="*", default=[])
    ap.add_argument("--hdris", nargs="*", default=[])
    ap.add_argument("--max-mb", type=float, default=25.0)
    ap.add_argument("--inspect", action="store_true")
    args = ap.parse_args()

    if args.inspect:
        inspect_in_blender()
        return

    models = list(args.models)
    textures = list(args.textures)
    hdris = list(args.hdris)
    if args.preset == "nature_core" and not (models or textures or hdris):
        models = NATURE_CORE_MODELS
        textures = NATURE_CORE_TEXTURES
        hdris = NATURE_CORE_HDRIS

    print(f"=== Syncing PolyHaven CC0 Library -> {POLYHAVEN_DIR} ===")
    for mid in models:
        try:
            fetch_model(mid, res="1k", max_mb=args.max_mb)
        except Exception as e:
            print(f"[WARN] Model {mid}: {e}")

    for tid in textures:
        try:
            fetch_texture(tid, res="1k")
        except Exception as e:
            print(f"[WARN] Texture {tid}: {e}")

    for hid in hdris:
        try:
            fetch_hdri(hid, res="2k")
        except Exception as e:
            print(f"[WARN] HDRI {hid}: {e}")

    print("=== PolyHaven CC0 Sync Complete ===")


if __name__ == "__main__":
    main()

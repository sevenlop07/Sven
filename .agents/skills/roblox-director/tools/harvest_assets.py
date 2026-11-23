#!/usr/bin/env python3
r"""
harvest_assets.py — Reproducible Roblox asset harvester + core asset catalog (runtime-neutral, any agent).

Needs Roblox Studio open (any place, Edit mode) and the bridge running in its own console window:
    node .agents/skills/roblox-director/studio_kit/bridge.mjs
Blender 5.3 is found by blender-core's find_blender() (or BLENDER_EXE).

Commands
  search  "<query>" ["<query>" …] [--max 12]        free Creator Store models → id | title | creator (cached for harvest)
  harvest <Name>:<assetId> [<Name>:<assetId> …]       insert → sanitize → extract (paged) → .glb in assets/<category>/
          [--no-textures] [--keep] [--force]          + preview + catalog entry. Name prefix picks the folder:
          [--max-boxes 0.10]                          (rejects models whose meshes/unions Roblox won't let us read)
                                                      Prop_ props · Set_ sets · Nature_ nature · Pet_ animals · Hair_ hairs
                                                      (end Creator Store names with _CS, e.g. Prop_FoodCart_CS)
  convert <Name> [<Name> …]                           re-run only the Blender step from output/_asset_harvest/json/<Name>.json
  catalog [--previews]                                rescan assets/**.glb → assets/catalog.json (dims, tris, source, licence)
  sheet   [--out <png>]                               contact sheet of every catalog preview (view it before picking)

Files
  output/_asset_harvest/json/<Name>.json        raw extraction (gitignored scratch; re-convertible)
  output/_asset_harvest/search_cache.json       last search results (title/creator for provenance)
  assets/<category>/<Name>.glb                  the asset agents load (kit.load_core_glb / env.spawn_core_glb_asset)
  assets/_previews/<Name>.jpg                   256 px 3/4 view used by the sheet
  assets/catalog.json                           one row per asset: path, category, dims_m, tris, source, licence note

What can be harvested: Roblox only lets EditableMesh read meshes you own or that are open to you, so meshes by other
creators come back "no permission" and would be drawn as boxes (unions too). Part-built (blocky) models convert fully;
mesh-heavy models are rejected by --max-boxes — use them in Studio-captured films instead.

Licence: Creator Store models are licensed for use on Roblox. Rows from the store carry
licence="roblox_creator_store" — fine for Studio-captured films; for Blender renders outside Roblox the user decides
(ROBLOX_DIRECTOR.md §4.5). Procedural (_Hybrid / code-built) and CC0 rows are free to use.
"""
import argparse
import glob
import json
import os
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.normpath(os.path.join(HERE, ".."))
KIT = os.path.join(SKILL, "studio_kit")
ASSETS = os.path.join(SKILL, "assets")
REPO = os.path.normpath(os.path.join(SKILL, "..", "..", ".."))
WORK = os.path.join(REPO, "output", "_asset_harvest")
JSON_DIR = os.path.join(WORK, "json")
PREVIEWS = os.path.join(ASSETS, "_previews")
CATALOG = os.path.join(ASSETS, "catalog.json")
SEARCH_CACHE = os.path.join(WORK, "search_cache.json")
LUA_LIB = os.path.join(KIT, "harvest_extract.lua")
CONVERTER = os.path.join(KIT, "roblox_json_to_glb.py")
PAGE = 60000          # execute_luau output is capped near 100k chars
HARVEST_PARENT = "game.ServerStorage._AssetHarvest"
PREFIX_CAT = {"Prop": "props", "Set": "sets", "Nature": "nature", "Pet": "animals", "Hair": "hairs"}
GLB_CATS = ("props", "sets", "nature", "animals", "hairs", "asmr_nature")
LICENCE_NOTE = {
    "roblox_creator_store": "Roblox Creator Store: licensed for use on Roblox. OK for Studio-captured films; "
                            "Blender renders outside Roblox need the user's licence call (ROBLOX_DIRECTOR.md §4.5).",
    "procedural": "Built by Sven code (studio_kit / tools): free to use.",
    "cc0": "CC0 (e.g. PolyHaven): free to use, credit optional.",
    "unknown": "Origin not recorded: check before commercial use.",
}

sys.path.insert(0, KIT)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.normpath(os.path.join(SKILL, "..", "blender-core", "scripts")))


# ---------------------------------------------------------------- Studio side
def _rb():
    import rb  # studio_kit/rb.py (file-queue client of bridge.mjs)
    return rb


def studio_id():
    rb = _rb()
    r = rb.send({"name": "list_roblox_studios", "arguments": {}}, timeout=30)
    try:
        studios = json.loads(rb.text(r))["studios"]
    except Exception:
        sys.exit(f"[harvest] bridge/Studio not reachable: {rb.text(r)[:300]}\n"
                 "Start Studio + `node studio_kit/bridge.mjs` in its own console window.")
    if not studios:
        sys.exit("[harvest] no Roblox Studio instance is open")
    if len(studios) > 1:
        saved = rb.sid
        pick = next((s for s in studios if s["id"] == saved), None)
        if not pick:
            sys.exit("[harvest] several Studios open; write the right id into studio_kit/studio_id.txt: "
                     + ", ".join(f'{s["name"]}={s["id"]}' for s in studios))
        return pick["id"]
    return studios[0]["id"]


def lua(sid, code, timeout=300):
    rb = _rb()
    r = rb.send({"name": "execute_luau", "arguments": {"code": code, "datamodel_type": "Edit", "studio_id": sid}},
                timeout=timeout)
    return rb.text(r)


def call(sid, tool, args, timeout=170):
    rb = _rb()
    args = dict(args, studio_id=sid)
    return rb.text(rb.send({"name": tool, "arguments": args}, timeout=timeout))


def _lq(s):
    return json.dumps(s)  # a JSON string literal is a valid Luau string literal for our names/paths


def cmd_search(a):
    sid = studio_id()
    cache = json.load(open(SEARCH_CACHE, encoding="utf-8")) if os.path.exists(SEARCH_CACHE) else {}
    for q in a.queries:
        out = call(sid, "search_asset", {"query": q, "assetType": "Model", "scope": "creator_store",
                                         "priceFilter": "free", "maxResults": a.max})
        try:
            res = json.loads(out)["results"]
        except Exception:
            print(f"## {q}: {out[:300]}")
            continue
        print(f"## {q}")
        for r in res:
            aid = str(r["assetId"])
            cache[aid] = {"title": r.get("name", ""), "creator": r.get("creatorName", ""), "query": q}
            desc = (r.get("description") or "").replace("\n", " ")[:90]
            print(f"  {aid:>14} | {r.get('name', '')[:48]:48} | {r.get('creatorName', '')[:20]:20} | {desc}")
    os.makedirs(WORK, exist_ok=True)
    json.dump(cache, open(SEARCH_CACHE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


def extract_one(sid, name, asset_id, textures=True, keep=False):
    folder = HARVEST_PARENT.split(".")[-1]
    path = f"{HARVEST_PARENT}.{name}"
    lua(sid, f"""local ss = game:GetService("ServerStorage")
local f = ss:FindFirstChild({_lq(folder)}) or Instance.new("Folder")
f.Name = {_lq(folder)}; f.Parent = ss
local old = f:FindFirstChild({_lq(name)}); if old then old:Destroy() end
return "ok" """)
    ins = call(sid, "insert_asset", {"assetId": str(asset_id), "assetName": name, "assetType": "Model",
                                     "parentPath": HARVEST_PARENT})
    print(f"[harvest] insert {name} ({asset_id}): {ins[:140].strip()}")
    lib = open(LUA_LIB, encoding="utf-8").read()
    ready = lua(sid, lib)
    if "SvenHarvest ready" not in ready:
        raise RuntimeError(f"Luau lib failed to load: {ready[:400]}")
    summ_txt = lua(sid, f"return _G.SvenHarvest.prepare({_lq(path)}, {{key = {_lq(name)}, "
                        f"textures = {'true' if textures else 'false'}}})", timeout=600)
    try:
        summ = json.loads(summ_txt)
    except ValueError:
        raise RuntimeError(f"extract failed: {summ_txt[:400]}")
    if "error" in summ:
        raise RuntimeError(summ["error"])
    total, chunks, i = summ["bytes"], [], 1
    while i <= total:
        chunks.append(lua(sid, f"return _G.SvenHarvest.page({_lq(name)}, {i}, {PAGE})"))
        i += PAGE
    raw = "".join(chunks)
    lua(sid, f"_G.SvenHarvest.drop({_lq(name)}) return 'ok'")
    if not keep:
        lua(sid, f"""local m = game:GetService("ServerStorage")[{_lq(folder)}]:FindFirstChild({_lq(name)})
if m then m:Destroy() end return "ok" """)
    if len(raw) != total:
        raise RuntimeError(f"paged read mismatch: got {len(raw)} of {total} chars")
    data = json.loads(raw)
    os.makedirs(JSON_DIR, exist_ok=True)
    jp = os.path.join(JSON_DIR, f"{name}.json")
    json.dump(data, open(jp, "w", encoding="utf-8"))
    san = summ.get("sanitized", {})
    print(f"[harvest] {name}: {summ['parts']} parts, {summ['meshes']} meshes "
          f"(mesh fail {summ['meshFail']}, texture fail {summ['texFail']}, unions as boxes {summ.get('unions', 0)}), "
          f"{total / 1024:.0f} KB JSON, "
          f"stripped {san.get('removed', 0)} unsafe objects {san.get('classes') or ''}")
    failed = summ.get("failed") or []
    for f in failed[:5]:
        print(f"    mesh not readable (box fallback): {f}")
    if len(failed) > 5:
        print(f"    … {len(failed) - 5} more")
    return jp, summ


# ---------------------------------------------------------------- Blender side
def blender(*args):
    from run_in_blender import find_blender
    exe = find_blender()
    if not exe:
        sys.exit("[harvest] Blender 5.3 not found; set BLENDER_EXE")
    cmd = [exe, "-b", "--factory-startup", "--python-exit-code", "1", "-P", CONVERTER, "--", *args]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    for line in p.stdout.splitlines():
        if line.startswith("@@JSON@@"):
            return json.loads(line[8:])
    tail = "\n".join((p.stdout + p.stderr).splitlines()[-15:])
    raise RuntimeError(f"Blender step failed (exit {p.returncode}):\n{tail}")


def _jpg_preview(png, name):
    os.makedirs(PREVIEWS, exist_ok=True)
    out = os.path.join(PREVIEWS, f"{name}.jpg")
    try:
        from PIL import Image
        Image.open(png).convert("RGB").resize((256, 256)).save(out, quality=85)
    except ImportError:
        import shutil
        out = os.path.join(PREVIEWS, f"{name}.png")
        shutil.copy(png, out)
    return out


def convert_one(name):
    cat = PREFIX_CAT.get(name.split("_")[0])
    if not cat:
        raise RuntimeError(f"name must start with one of {sorted(PREFIX_CAT)}_ (got {name})")
    jp = os.path.join(JSON_DIR, f"{name}.json")
    stage = os.path.join(tempfile.gettempdir(), "sven_asset_harvest")  # Blender writes to %TEMP% (OIIO-safe)
    os.makedirs(stage, exist_ok=True)
    tmp_glb, tmp_png = os.path.join(stage, f"{name}.glb"), os.path.join(stage, f"{name}.png")
    info = blender("convert", jp, tmp_glb, "--preview", tmp_png)
    dest = os.path.join(ASSETS, cat, f"{name}.glb")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(tmp_glb, "rb") as s, open(dest, "wb") as d:
        d.write(s.read())
    prev = _jpg_preview(tmp_png, name)
    print(f"[harvest] → {os.path.relpath(dest, REPO)}  dims {info['dims_m']} m, {info['tris']} tris, "
          f"{info['bytes'] / 1024:.0f} KB; preview {os.path.relpath(prev, REPO)}")
    return dest, info


# ---------------------------------------------------------------- catalog
def load_catalog():
    if os.path.exists(CATALOG):
        return json.load(open(CATALOG, encoding="utf-8"))
    return {"version": 1, "assets": {}}


def save_catalog(cat):
    cat["licence_notes"] = LICENCE_NOTE
    cat["assets"] = dict(sorted(cat["assets"].items()))
    json.dump(cat, open(CATALOG, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


def _guess_source(name):
    if name.endswith("_CS") or "_CS_" in name or name.endswith("_RobloxResources"):
        return "roblox_creator_store"
    return "procedural" if name.endswith("_Hybrid") else "unknown"


def catalog_upsert(cat, rel, info, source=None, extra=None):
    name = os.path.splitext(os.path.basename(rel))[0]
    row = cat["assets"].get(name, {})
    row.update({"path": rel.replace("\\", "/"), "category": rel.replace("\\", "/").split("/")[0]})
    for k in ("dims_m", "tris", "materials"):
        if k in info:
            row[k] = info[k]
    row.setdefault("source", source or _guess_source(name))
    if source:
        row["source"] = source
    for ext in (".jpg", ".png"):
        if os.path.exists(os.path.join(PREVIEWS, name + ext)):
            row["preview"] = f"_previews/{name}{ext}"
    if extra:
        row.update(extra)
    cat["assets"][name] = row


def cmd_harvest(a):
    sid = studio_id()
    cache = json.load(open(SEARCH_CACHE, encoding="utf-8")) if os.path.exists(SEARCH_CACHE) else {}
    cat = load_catalog()
    ok = 0
    for item in a.items:
        name, _, aid = item.partition(":")
        if not aid.isdigit() or name.split("_")[0] not in PREFIX_CAT:
            print(f"[harvest] skip {item}: use <Prefix>_<Name>:<assetId>, prefix in {sorted(PREFIX_CAT)}")
            continue
        if name in cat["assets"] and not a.force:
            print(f"[harvest] skip {name}: already in catalog (use --force to replace)")
            continue
        try:
            _, summ = extract_one(sid, name, aid, textures=not a.no_textures, keep=a.keep)
            boxes = summ.get("fallback", 0) + summ.get("unions", 0)
            share = boxes / max(1, summ["parts"])
            if share > a.max_boxes:
                print(f"[harvest] REJECT {name}: {boxes}/{summ['parts']} parts would be plain boxes "
                      f"({share:.0%} > --max-boxes {a.max_boxes:.0%}); meshes owned by other creators cannot be read. "
                      "Pick a part-built model (search text: many parts, few meshes) or capture it in Studio.")
                continue
            dest, info = convert_one(name)
        except Exception as e:  # keep going with the rest of the batch
            print(f"[harvest] FAILED {name}: {e}")
            continue
        meta = cache.get(aid, {})
        catalog_upsert(cat, os.path.relpath(dest, ASSETS), info, source="roblox_creator_store", extra={
            "asset_id": int(aid), "title": meta.get("title", ""), "creator": meta.get("creator", ""),
            "extent_studs": summ.get("extentStuds"), "mesh_fail": summ.get("meshFail", 0),
            "texture_fail": summ.get("texFail", 0), "unions_as_boxes": summ.get("unions", 0), "harvested": time.strftime("%Y-%m-%d"),
        })
        save_catalog(cat)
        ok += 1
    print(f"[harvest] done: {ok}/{len(a.items)} assets → {os.path.relpath(CATALOG, REPO)}")


def cmd_convert(a):
    cat = load_catalog()
    for name in a.names:
        dest, info = convert_one(name)
        catalog_upsert(cat, os.path.relpath(dest, ASSETS), info)
    save_catalog(cat)


def cmd_catalog(a):
    glbs = sorted(g for c in GLB_CATS for g in glob.glob(os.path.join(ASSETS, c, "*.glb")))
    out = os.path.join(tempfile.gettempdir(), "sven_asset_measure.json")
    blender("measure", out, *glbs)
    measured = json.load(open(out, encoding="utf-8"))
    cat = load_catalog()
    live = set()
    for g in glbs:
        rel = os.path.relpath(g, ASSETS)
        live.add(os.path.splitext(os.path.basename(g))[0])
        catalog_upsert(cat, rel, measured.get(g, {}))
        if a.previews:
            name = os.path.splitext(os.path.basename(g))[0]
            if not any(os.path.exists(os.path.join(PREVIEWS, name + e)) for e in (".jpg", ".png")):
                stage = os.path.join(tempfile.gettempdir(), "sven_asset_harvest")
                os.makedirs(stage, exist_ok=True)
                png = os.path.join(stage, f"{name}.png")
                blender("preview", g, png)
                _jpg_preview(png, name)
                catalog_upsert(cat, rel, {})
    for gone in set(cat["assets"]) - live:
        del cat["assets"][gone]
    save_catalog(cat)
    srcs = {}
    for r in cat["assets"].values():
        srcs[r["source"]] = srcs.get(r["source"], 0) + 1
    print(f"[catalog] {len(cat['assets'])} assets → {os.path.relpath(CATALOG, REPO)}  by source: {srcs}")


def cmd_sheet(a):
    from PIL import Image, ImageDraw
    cat = load_catalog()
    rows = [(n, r) for n, r in cat["assets"].items() if r.get("preview")]
    if not rows:
        sys.exit("[sheet] no previews yet (run harvest, or catalog --previews)")
    cols, cell, lab = 6, 256, 34
    sheet = Image.new("RGB", (cols * cell, ((len(rows) + cols - 1) // cols) * (cell + lab)), (24, 24, 28))
    d = ImageDraw.Draw(sheet)
    for i, (n, r) in enumerate(rows):
        x, y = (i % cols) * cell, (i // cols) * (cell + lab)
        sheet.paste(Image.open(os.path.join(ASSETS, r["preview"])).convert("RGB").resize((cell, cell)), (x, y))
        dims = " x ".join(f"{v:.1f}" for v in r.get("dims_m", [])) + " m"
        d.text((x + 6, y + cell + 3), n[:38], fill=(235, 235, 235))
        d.text((x + 6, y + cell + 18), f"{dims}  [{r['source'][:12]}]", fill=(160, 170, 185))
    out = a.out or os.path.join(WORK, "catalog_sheet.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    sheet.save(out)
    print(f"[sheet] {len(rows)} assets → {out}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("search"); s.add_argument("queries", nargs="+"); s.add_argument("--max", type=int, default=12)
    h = sp.add_parser("harvest"); h.add_argument("items", nargs="+")
    h.add_argument("--no-textures", action="store_true"); h.add_argument("--keep", action="store_true")
    h.add_argument("--force", action="store_true")
    h.add_argument("--max-boxes", type=float, default=0.10,
                   help="reject when more than this share of parts falls back to boxes (unreadable mesh / union)")
    c = sp.add_parser("convert"); c.add_argument("names", nargs="+")
    k = sp.add_parser("catalog"); k.add_argument("--previews", action="store_true")
    t = sp.add_parser("sheet"); t.add_argument("--out", default="")
    a = ap.parse_args()
    {"search": cmd_search, "harvest": cmd_harvest, "convert": cmd_convert, "catalog": cmd_catalog,
     "sheet": cmd_sheet}[a.cmd](a)


if __name__ == "__main__":
    main()

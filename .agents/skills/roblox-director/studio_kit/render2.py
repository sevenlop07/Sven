#!/usr/bin/env python3
"""Queue tiled shots (2 captures per frame) -> frames2/<id>/; then stitch.py makes frames_hd/<id>/."""
import argparse, json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sid = open(os.path.join(HERE, "studio_id.txt")).read().strip() if os.path.exists(os.path.join(HERE, "studio_id.txt")) else ""

def load_shot_frames(shots_file):
    data = json.load(open(shots_file, encoding="utf-8"))
    out = {}
    if isinstance(data, dict) and "shots" in data:
        for s in data["shots"]:
            k = s.get("shot_id") or f"s{int(s['index']):02d}"
            dur = float(s.get("window_duration") or (float(s["window_end"]) - float(s["window_start"])))
            out[k] = max(8, round(dur * 30))
            out[f"s{int(s['index']):02d}"] = out[k]
    else:
        for sc in data:
            for s in sc["shots"]:
                out[s["id"]] = max(8, round(s["end"] * 30) - round(s["t"] * 30))
    return out

ap = argparse.ArgumentParser()
ap.add_argument("--shots", default="")
ap.add_argument("--out-prefix", default="frames2")
ap.add_argument("args", nargs="*")
pa = ap.parse_args()
shots_path = pa.shots or (os.path.join(HERE, "..", "shots", "shots.json") if os.path.exists(os.path.join(HERE, "..", "shots", "shots.json")) else os.path.join(HERE, "srt_shots.json"))
N = load_shot_frames(shots_path)
TEMPLATE = '''local F = {{F}}
local ok, e = pcall(function() shared.MT.frameTile("%s", F) end)
if F <= 2 then task.wait(0.6) else task.wait(0.03) end
if not ok then error(e) end
return "ok"'''
force = "force" in pa.args
lim = None
for a in pa.args:
    if a.startswith("n="): lim = int(a[2:])
ids = [a for a in pa.args if a in N]
for k, shot in enumerate(ids):
    n = min(N[shot], lim) if lim else N[shot]
    job = {"render": {"tool": "execute_luau", "code_arg": "code", "args": {"datamodel_type": "Edit", "studio_id": sid},
                      "template": TEMPLATE % shot, "frames": [1, 2 * n], "force": force,
                      "capture": {"name": "screen_capture", "arguments": {"capture_id": "ScreenCapture_1", "studio_id": sid}},
                      "out": f"{pa.out_prefix}/{shot}"}}
    name = f"{int(time.time()*1000)+k}_{shot}.json"
    json.dump(job, open(os.path.join(HERE, "queue", name + ".tmp"), "w")); os.rename(os.path.join(HERE, "queue", name + ".tmp"), os.path.join(HERE, "queue", name))
print("queued", len(ids), "shots,", sum(2 * (min(N[a], lim) if lim else N[a]) for a in ids), "captures")

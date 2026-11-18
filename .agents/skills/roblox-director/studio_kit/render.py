#!/usr/bin/env python3
"""Queue animated shots for capture: render.py [--shots path/to/srt_shots.json] [--out-prefix frames] s001 s002 ..."""
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
ap.add_argument("--out-prefix", default="frames")
ap.add_argument("args", nargs="*")
pa = ap.parse_args()
shots_path = pa.shots or (os.path.join(HERE, "..", "shots", "shots.json") if os.path.exists(os.path.join(HERE, "..", "shots", "shots.json")) else os.path.join(HERE, "srt_shots.json"))
N = load_shot_frames(shots_path)
TEMPLATE = '''local f = {{F}}
local ok, e = pcall(function() shared.MT.frame("%s", f) end)
if f == 1 then task.wait(0.6) else task.wait(0.03) end
if not ok then error(e) end
return "ok"'''
force = "force" in pa.args
shot_ids = [a for a in pa.args if a in N]
for k, shot in enumerate(shot_ids):
    job = {"render": {"tool": "execute_luau", "code_arg": "code", "args": {"datamodel_type": "Edit", "studio_id": sid},
                      "template": TEMPLATE % shot, "frames": [1, N[shot]], "force": force,
                      "capture": {"name": "screen_capture", "arguments": {"capture_id": "ScreenCapture_1", "studio_id": sid}},
                      "out": f"{pa.out_prefix}/{shot}"}}
    name = f"{int(time.time()*1000)+k}_{shot}.json"
    json.dump(job, open(os.path.join(HERE, "queue", name + ".tmp"), "w")); os.rename(os.path.join(HERE, "queue", name + ".tmp"), os.path.join(HERE, "queue", name))
print("queued", len(shot_ids), "shots,", sum(N[a] for a in shot_ids), "frames")

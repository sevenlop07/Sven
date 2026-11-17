#!/usr/bin/env python3
"""Queue 4K tiled shots: frames4k_v2/<id>/NNNNN.png = capture k of frame f, index (f-1)*R+k. Then stitch4k.py."""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sid = open(os.path.join(HERE, "studio_id.txt")).read().strip()
T = json.load(open(os.path.join(HERE, "tiles4k.json")))
N = {}
for sc in json.load(open(os.path.join(HERE, "..", "shots", "shots.json"))):
    for s in sc["shots"]:
        N[s["id"]] = max(8, round(s["end"] * 30) - round(s["t"] * 30))
TEMPLATE = '''local F = {{F}}
local ok, e = pcall(function() shared.MT.frameTileN("%s", F) end)
if F <= %d then task.wait(0.6) else task.wait(0.03) end
if not ok then error(e) end
return "ok"'''
force = "force" in sys.argv
lim = next((int(a[2:]) for a in sys.argv if a.startswith("n=")), None)
ids = [a for a in sys.argv[1:] if a in N]
tot = 0
for k, shot in enumerate(ids):
    R = T[shot]["rows"]; n = min(N[shot], lim) if lim else N[shot]; tot += R * n
    job = {"render": {"tool": "execute_luau", "code_arg": "code", "args": {"datamodel_type": "Edit", "studio_id": sid},
                      "template": TEMPLATE % (shot, R), "frames": [1, R * n], "force": force,
                      "capture": {"name": "screen_capture", "arguments": {"capture_id": "ScreenCapture_1", "studio_id": sid}},
                      "out": f"frames4k_v2/{shot}"}}
    name = f"{int(time.time()*1000)+k}_{shot}.json"
    json.dump(job, open(os.path.join(HERE, "queue", name + ".tmp"), "w")); os.rename(os.path.join(HERE, "queue", name + ".tmp"), os.path.join(HERE, "queue", name))
print("queued", len(ids), "shots,", tot, "captures")

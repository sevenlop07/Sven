#!/usr/bin/env python3
"""Queue tiled shots (2 captures per frame) -> frames2/<id>/; then stitch.py makes frames_hd/<id>/."""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sid = open(os.path.join(HERE, "studio_id.txt")).read().strip()
N = {}
for sc in json.load(open(os.path.join(HERE, "..", "shots", "shots.json"))):
    for s in sc["shots"]:
        N[s["id"]] = max(8, round(s["end"] * 30) - round(s["t"] * 30))
TEMPLATE = '''local F = {{F}}
local ok, e = pcall(function() shared.MT.frameTile("%s", F) end)
if F <= 2 then task.wait(0.6) else task.wait(0.03) end
if not ok then error(e) end
return "ok"'''
force = "force" in sys.argv
lim = None
for a in sys.argv:
    if a.startswith("n="): lim = int(a[2:])
ids = [a for a in sys.argv[1:] if a in N]
for k, shot in enumerate(ids):
    n = min(N[shot], lim) if lim else N[shot]
    job = {"render": {"tool": "execute_luau", "code_arg": "code", "args": {"datamodel_type": "Edit", "studio_id": sid},
                      "template": TEMPLATE % shot, "frames": [1, 2 * n], "force": force,
                      "capture": {"name": "screen_capture", "arguments": {"capture_id": "ScreenCapture_1", "studio_id": sid}},
                      "out": f"frames2/{shot}"}}
    name = f"{int(time.time()*1000)+k}_{shot}.json"
    json.dump(job, open(os.path.join(HERE, "queue", name + ".tmp"), "w")); os.rename(os.path.join(HERE, "queue", name + ".tmp"), os.path.join(HERE, "queue", name))
print("queued", len(ids), "shots,", sum(2 * (min(N[a], lim) if lim else N[a]) for a in ids), "captures")

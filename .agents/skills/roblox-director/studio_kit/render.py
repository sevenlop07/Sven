#!/usr/bin/env python3
"""Queue animated shots for capture: render.py s001 s002 ...  (frames go to frames/<id>/00001.jpg ...)"""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sid = open(os.path.join(HERE, "studio_id.txt")).read().strip()
N = {}
i = 0
for sc in json.load(open(os.path.join(HERE, "..", "shots", "shots.json"))):
    for s in sc["shots"]:
        N[s["id"]] = max(8, round(s["end"] * 30) - round(s["t"] * 30))
TEMPLATE = '''local f = {{F}}
local ok, e = pcall(function() shared.MT.frame("%s", f) end)
if f == 1 then task.wait(0.6) else task.wait(0.03) end
if not ok then error(e) end
return "ok"'''
force = "force" in sys.argv
for k, shot in enumerate(a for a in sys.argv[1:] if a in N):
    job = {"render": {"tool": "execute_luau", "code_arg": "code", "args": {"datamodel_type": "Edit", "studio_id": sid},
                      "template": TEMPLATE % shot, "frames": [1, N[shot]], "force": force,
                      "capture": {"name": "screen_capture", "arguments": {"capture_id": "ScreenCapture_1", "studio_id": sid}},
                      "out": f"frames/{shot}"}}
    name = f"{int(time.time()*1000)+k}_{shot}.json"
    json.dump(job, open(os.path.join(HERE, "queue", name + ".tmp"), "w")); os.rename(os.path.join(HERE, "queue", name + ".tmp"), os.path.join(HERE, "queue", name))
print("queued", len([a for a in sys.argv[1:] if a in N]), "shots,", sum(N[a] for a in sys.argv[1:] if a in N), "frames")

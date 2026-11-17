#!/usr/bin/env python3
"""Plan 4K tiles per shot from fov.json and the capture size: writes tiles4k.json and tiles4k.lua (shared.MT_TILES).
Each frame = R captures from the same camera centre, pitched to rows; stitch4k.py joins them into 2160x3840."""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 2160, 3840
CW, CH = 1896, 1040          # capture size (viewport 948x520 pt)
MARGIN = 1.6                 # degrees of overlap each side
plan = {}
for sid, V in json.load(open(os.path.join(HERE, "fov.json"))).items():
    fo = (H / 2) / math.tan(math.radians(V / 2))
    tx = (W / 2) / fo                                  # tan of output half width
    ft = (CW / 2) / (tx * 1.04)                        # tile focal so the width fits
    Ft = 2 * math.degrees(math.atan((CH / 2) / ft))    # tile vertical FOV
    rows = 3
    while Ft / 2 < V / (2 * rows) + MARGIN: rows += 1
    pitches = [V / 2 - (i + 0.5) * V / rows for i in range(rows)]
    plan[sid] = {"V": V, "rows": rows, "Ft": Ft, "p": pitches, "res": ft / fo}
json.dump(plan, open(os.path.join(HERE, "tiles4k.json"), "w"), indent=1)
lua = "shared.MT_TILES = {\n" + "".join(
    f'\t{k} = {{ rows = {v["rows"]}, Ft = {v["Ft"]:.5f}, p = {{ {", ".join(f"{x:.5f}" for x in v["p"])} }} }},\n' for k, v in sorted(plan.items())) + "}\nreturn 'tiles ok'"
open(os.path.join(HERE, "tiles4k.lua"), "w").write(lua)
rs = [v["rows"] for v in plan.values()]; res = [v["res"] for v in plan.values()]
print("rows", min(rs), max(rs), "captures/frame avg", sum(rs) / len(rs), "res vs native 4K", round(min(res), 2), round(max(res), 2))

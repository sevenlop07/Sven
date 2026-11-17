"""Step-wise 4K join (each step < 3 min): list | part K | final"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.normpath(os.path.join(HERE, "..")); VID = os.path.normpath(os.path.join(EP, "..", "..", "..", "videos", "monster-test"))
A = os.path.join(VID, "assets"); PARTS = os.path.join(HERE, "parts4k_v2"); os.makedirs(PARTS, exist_ok=True)
CH = 900
step = sys.argv[1]
if step == "list":
    lst, short = [], []
    for sc in json.load(open(os.path.join(EP, "shots", "shots.json"))):
        for s in sc["shots"]:
            n = max(8, round(s["end"] * 30) - round(s["t"] * 30))
            d = os.path.join(HERE, "frames_4k_v2", s["id"])
            fr = sorted(f for f in os.listdir(d) if f[:5].isdigit() and f.endswith(".jpg"))[:n] if os.path.isdir(d) else []
            if len(fr) < n: short.append(f"{s['id']}:{len(fr)}/{n}")
            for j in range(n): lst.append(os.path.join(d, fr[min(j, len(fr) - 1)]) if fr else lst[-1])
    json.dump(lst, open(os.path.join(HERE, "frames_4k_v2_list.json"), "w"))
    print("frames", len(lst), "parts", (len(lst) + CH - 1) // CH, "short:", short or "none")
elif step == "part":
    k = int(sys.argv[2]); lst = json.load(open(os.path.join(HERE, "frames_4k_v2_list.json")))[k * CH:(k + 1) * CH]
    cat = os.path.join(PARTS, f"p{k:02d}.txt")
    with open(cat, "w") as fh:
        for p in lst: fh.write(f"file '{p}'\nduration {1/30:.6f}\n")
    out = os.path.join(PARTS, f"p{k:02d}.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", cat, "-frames:v", str(len(lst)), "-r", "30", "-c:v", "libx264", "-crf", "16",
                    "-preset", "veryfast", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "5.2", "-g", "30", out], check=True)
    print("part", k, len(lst))
elif step == "final":
    n = len(json.load(open(os.path.join(HERE, "frames_4k_v2_list.json")))); parts = sorted(f for f in os.listdir(PARTS) if f.endswith(".mp4"))
    with open(os.path.join(PARTS, "all.txt"), "w") as fh:
        for p in parts: fh.write(f"file '{os.path.join(PARTS, p)}'\n")
    out4k = os.path.join(A, "roblox_anim_4k_v2.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(PARTS, "all.txt"), "-c", "copy", "-movflags", "+faststart", out4k], check=True)
    print("4k done", n)

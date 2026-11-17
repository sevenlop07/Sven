"""Join the Roblox Studio frames (frames/<id>/NNNNN.png, JPEG data, 1896x1042 landscape) into the 9:16 picture track
videos/monster-test/assets/roblox_anim.mp4, timed to the voice. Missing frames repeat the last good one."""
import json, os, shutil, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.normpath(os.path.join(HERE, ".."))
ROOT = os.path.normpath(os.path.join(EP, "..", "..", ".."))
VID = os.path.join(ROOT, "videos", "monster-test")
ALL = os.path.join(HERE, "frames_all")
shutil.rmtree(ALL, ignore_errors=True); os.makedirs(ALL)
i, short, last = 1, [], None
for sc in json.load(open(os.path.join(EP, "shots", "shots.json"))):
    for s in sc["shots"]:
        n = max(8, round(s["end"] * 30) - round(s["t"] * 30))
        d = os.path.join(HERE, "frames", s["id"])
        fr = sorted(f for f in os.listdir(d) if f[:5].isdigit()) if os.path.isdir(d) else []
        if len(fr) < n: short.append(f"{s['id']}:{len(fr)}/{n}")
        for j in range(n):
            src = os.path.join(d, fr[min(j, len(fr) - 1)]) if fr else last
            dst = os.path.join(ALL, f"{i:05d}.jpg")
            try: os.link(src, dst)
            except OSError: shutil.copy(src, dst)
            last = src; i += 1
print("frames", i - 1, "short shots:", short or "none")
out = os.path.join(VID, "assets", "roblox_anim.mp4")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", "30", "-i", os.path.join(ALL, "%05d.jpg"),
                "-vf", "crop=trunc(ih*9/16/2)*2:ih,scale=1080:1920:flags=lanczos,setsar=1", "-c:v", "libx264", "-crf", "18",
                "-preset", "veryfast", "-pix_fmt", "yuv420p", "-g", "15", "-movflags", "+faststart", out + ".part.mp4"], check=True)
os.replace(out + ".part.mp4", out)
w = json.load(open(os.path.join(VID, "words.json")))
w["videos/monster-test/assets/roblox_anim.mp4"] = w["videos/monster-test/audio/vo.wav"]
json.dump(w, open(os.path.join(VID, "words.json"), "w"), indent=1)
js = open(os.path.join(VID, "video_anim.js")).read().replace("assets/monster_anim.mp4", "assets/roblox_anim.mp4")
js = js.replace("Picture = the Blender animation", "Picture = the Roblox Studio animation")
open(os.path.join(VID, "video_roblox.js"), "w").write(js)
shutil.copy(os.path.join(VID, "video_roblox.js"), os.path.join(VID, "video.js"))
print("DONE", out)

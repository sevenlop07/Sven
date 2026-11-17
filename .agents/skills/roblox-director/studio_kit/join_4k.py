"""Stitch every 4K shot (stitch4k.py), join frames_4k/<id>/ into videos/monster-test/assets/roblox_anim_4k.mp4 (2160x3840, 30 fps)
timed to the voice, plus an HD copy (roblox_anim_hd.mp4) for Studio Preview, a 4K master with voice+music, and a phone preview."""
import json, os, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stitch4k
EP = os.path.normpath(os.path.join(HERE, ".."))
VID = os.path.normpath(os.path.join(EP, "..", "..", "..", "videos", "monster-test"))
lst, short = [], []
for sc in json.load(open(os.path.join(EP, "shots", "shots.json"))):
    for s in sc["shots"]:
        n = max(8, round(s["end"] * 30) - round(s["t"] * 30))
        stitch4k.shot(s["id"])
        d = os.path.join(HERE, "frames_4k", s["id"])
        fr = sorted(f for f in os.listdir(d) if f[:5].isdigit())[:n] if os.path.isdir(d) else []
        if len(fr) < n: short.append(f"{s['id']}:{len(fr)}/{n}")
        for j in range(n):
            lst.append(os.path.join(d, fr[min(j, len(fr) - 1)]) if fr else lst[-1])
print("frames", len(lst), "short shots:", short or "none")
cat = os.path.join(HERE, "frames_4k_list.txt")
with open(cat, "w") as fh:
    for p in lst: fh.write(f"file '{p}'\nduration {1/30:.6f}\n")
A = os.path.join(VID, "assets")
out4k = os.path.join(A, "roblox_anim_4k.mp4"); outhd = os.path.join(A, "roblox_anim_hd.mp4")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", cat, "-frames:v", str(len(lst)), "-r", "30",
                "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "5.2",
                "-g", "30", "-movflags", "+faststart", out4k + ".part.mp4"], check=True)
os.replace(out4k + ".part.mp4", out4k)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", out4k, "-vf", "scale=1080:1920:flags=lanczos", "-c:v", "libx264", "-crf", "17",
                "-preset", "veryfast", "-pix_fmt", "yuv420p", "-g", "15", "-movflags", "+faststart", outhd + ".part.mp4"], check=True)
os.replace(outhd + ".part.mp4", outhd)
w = json.load(open(os.path.join(VID, "words.json")))
for k in ("roblox_anim_4k.mp4", "roblox_anim_hd.mp4"): w["videos/monster-test/assets/" + k] = w["videos/monster-test/audio/vo.wav"]
json.dump(w, open(os.path.join(VID, "words.json"), "w"), indent=1)
js = open(os.path.join(VID, "video_roblox.js")).read().replace("assets/roblox_anim.mp4", "assets/roblox_anim_hd.mp4")
open(os.path.join(VID, "video_roblox_hd.js"), "w").write(js); shutil.copy(os.path.join(VID, "video_roblox_hd.js"), os.path.join(VID, "video.js"))
os.makedirs(os.path.join(VID, "out"), exist_ok=True)
mix = "[2:a]volume=0.22[b];[1:a][b]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[a]"
aud = ["-i", os.path.join(VID, "audio", "vo.wav"), "-stream_loop", "-1", "-i", os.path.join(VID, "audio", "bg.mp3"), "-filter_complex", mix, "-map", "0:v", "-map", "[a]"]
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out4k] + aud + ["-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-shortest", "-movflags", "+faststart",
                os.path.join(VID, "out", "roblox_4k_raw_mix.mp4")], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", outhd] + aud + ["-vf", "scale=720:1280:flags=lanczos", "-c:v", "libx264", "-crf", "22", "-preset", "veryfast",
                "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", os.path.join(VID, "out", "roblox_hd_phone.mp4")], check=True)
print("DONE", out4k, outhd)

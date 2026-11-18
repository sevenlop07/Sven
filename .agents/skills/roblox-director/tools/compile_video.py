#!/usr/bin/env python3
"""
compile_video.py — Generalized Stage R5 Video, Audio Mix (-14 LUFS) & Subtitle Compiler for @RobloxDirector.
Supports both 9:16 (1080x1920 / 2160x3840) and 16:9 (1920x1080 / 3840x2160),
reads srt_shots.json (from audio_to_srt.py) or shots.json, mixes voice + BGM (-14 LUFS),
and burns in .ass or .srt subtitles via FFmpeg.

Usage:
  python compile_video.py --project-dir output/my_film --voice voice.mp3 --shots srt_shots.json --frames-dir frames --out final.mp4 [--aspect 9:16|16:9] [--bgm music.mp3] [--subs caps.ass]
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_BGM = os.path.normpath(os.path.join(HERE, "..", "music", "roblox-story-bg.mp3"))
FFMPEG = r"C:\Users\adminb\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"
if not os.path.exists(FFMPEG):
    FFMPEG = "ffmpeg"


def load_shots(shots_path: str) -> list:
    data = json.load(open(shots_path, encoding="utf-8"))
    if isinstance(data, dict) and "shots" in data:
        out = []
        for s in data["shots"]:
            sid = s.get("shot_id") or s.get("id") or f"s{s['index']:02d}"
            # normalize "Shot 01" -> "s01" as fallback folder name if needed
            short_id = f"s{int(s['index']):02d}" if "index" in s else sid
            dur = float(s.get("window_duration") or (float(s["window_end"]) - float(s["window_start"])))
            out.append({"id": sid, "short_id": short_id, "duration": max(0.25, dur)})
        return out
    if isinstance(data, list):
        out = []
        for sc in data:
            for s in sc.get("shots", []):
                dur = max(0.25, float(s["end"]) - float(s["t"]))
                out.append({"id": s["id"], "short_id": s["id"], "duration": dur})
        return out
    raise ValueError(f"Unsupported shots schema in {shots_path}")


def find_shot_media(frames_dir: str, shot: dict):
    """Locate either a per-shot directory of PNG/JPG frames OR a per-shot .mp4 clip."""
    for cand in (shot["id"], shot["short_id"]):
        mp4 = os.path.join(frames_dir, f"{cand}.mp4")
        if os.path.isfile(mp4):
            return ("mp4", mp4)
        folder = os.path.join(frames_dir, cand)
        if os.path.isdir(folder):
            imgs = sorted(f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg")))
            if imgs:
                return ("frames", [os.path.join(folder, f) for f in imgs])
        for ext in (".png", ".jpg", ".jpeg"):
            still = os.path.join(frames_dir, f"{cand}{ext}")
            if os.path.isfile(still):
                return ("still", still)
    return (None, None)


def build_raw_video(shots: list, frames_dir: str, out_raw: str, w: int, h: int, fps: int = 30):
    tmp_dir = os.path.join(os.path.dirname(os.path.abspath(out_raw)), "_compile_tmp")
    shutil.rmtree(tmp_dir, ignore_errors=True)
    os.makedirs(tmp_dir, exist_ok=True)

    concat_list = os.path.join(tmp_dir, "concat.txt")
    entries = []
    scale_vf = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1"

    for idx, s in enumerate(shots):
        kind, media = find_shot_media(frames_dir, s)
        if not kind:
            raise FileNotFoundError(f"Missing frames/clip for shot '{s['id']}' / '{s['short_id']}' in {frames_dir}")
        seg_mp4 = os.path.join(tmp_dir, f"seg_{idx:03d}.mp4")
        n_frames = max(1, round(s["duration"] * fps))

        if kind == "mp4":
            subprocess.run([
                FFMPEG, "-y", "-v", "error", "-i", media, "-t", f"{s['duration']:.3f}",
                "-vf", scale_vf, "-r", str(fps), "-c:v", "libx264", "-crf", "17",
                "-preset", "veryfast", "-pix_fmt", "yuv420p", seg_mp4
            ], check=True)
        elif kind == "still":
            subprocess.run([
                FFMPEG, "-y", "-v", "error", "-loop", "1", "-i", media,
                "-t", f"{s['duration']:.3f}", "-vf", scale_vf, "-r", str(fps),
                "-c:v", "libx264", "-crf", "17", "-preset", "veryfast", "-pix_fmt", "yuv420p", seg_mp4
            ], check=True)
        else:
            list_txt = os.path.join(tmp_dir, f"frames_{idx:03d}.txt")
            with open(list_txt, "w", encoding="utf-8") as fh:
                for j in range(n_frames):
                    fp = media[min(j, len(media) - 1)].replace("\\", "/")
                    fh.write(f"file '{fp}'\nduration {1.0 / fps:.6f}\n")
            subprocess.run([
                FFMPEG, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", list_txt,
                "-frames:v", str(n_frames), "-vf", scale_vf, "-r", str(fps),
                "-c:v", "libx264", "-crf", "17", "-preset", "veryfast", "-pix_fmt", "yuv420p", seg_mp4
            ], check=True)

        entries.append(f"file '{seg_mp4.replace(chr(92), '/')}'")

    with open(concat_list, "w", encoding="utf-8") as fh:
        fh.write("\n".join(entries) + "\n")

    subprocess.run([
        FFMPEG, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", concat_list,
        "-c:v", "copy", "-movflags", "+faststart", out_raw
    ], check=True)
    shutil.rmtree(tmp_dir, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-dir", required=True)
    ap.add_argument("--voice", required=True, help="Voice .mp3 or .wav path (relative to project-dir or absolute)")
    ap.add_argument("--shots", default="srt_shots.json")
    ap.add_argument("--frames-dir", default="shots")
    ap.add_argument("--bgm", default=DEFAULT_BGM)
    ap.add_argument("--bgm-vol", type=float, default=0.18)
    ap.add_argument("--subs", default="", help="Optional .ass or .srt subtitle file to burn in")
    ap.add_argument("--aspect", choices=["9:16", "16:9"], default="9:16")
    ap.add_argument("--uhd", action="store_true", help="Export 4K (2160x3840 or 3840x2160) instead of 1080p")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--out", default="final_master.mp4")
    args = ap.parse_args()

    pdir = os.path.abspath(args.project_dir)
    res_p = lambda p: p if os.path.isabs(p) else os.path.join(pdir, p)

    shots_path = res_p(args.shots)
    voice_path = res_p(args.voice)
    frames_dir = res_p(args.frames_dir)
    out_mp4 = res_p(args.out)
    raw_mp4 = os.path.join(pdir, "_raw_video.mp4")

    if args.aspect == "16:9":
        w, h = (3840, 2160) if args.uhd else (1920, 1080)
    else:
        w, h = (2160, 3840) if args.uhd else (1080, 1920)

    shots = load_shots(shots_path)
    build_raw_video(shots, frames_dir, raw_mp4, w, h, args.fps)

    # Audio mix (-14 LUFS, <= -1.0 dBTP) + optional subtitle burn-in
    cmd = [FFMPEG, "-y", "-v", "error", "-i", raw_mp4, "-i", voice_path]
    has_bgm = bool(args.bgm and os.path.exists(res_p(args.bgm)))
    if has_bgm:
        cmd += ["-stream_loop", "-1", "-i", res_p(args.bgm)]
        af = f"[2:a]volume={args.bgm_vol}[b];[1:a][b]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.0[a]"
    else:
        af = "[1:a]loudnorm=I=-14:TP=-1.0[a]"
    cmd += ["-filter_complex", af, "-map", "0:v", "-map", "[a]"]

    subs_path = res_p(args.subs) if args.subs else ""
    if subs_path and os.path.exists(subs_path):
        escaped = subs_path.replace("\\", "/").replace(":", "\\:")
        vf = f"ass='{escaped}'" if subs_path.lower().endswith(".ass") else f"subtitles='{escaped}'"
        cmd += ["-vf", vf, "-c:v", "libx264", "-crf", "17", "-preset", "veryfast", "-pix_fmt", "yuv420p"]
    else:
        cmd += ["-c:v", "copy"]

    cmd += ["-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out_mp4]
    subprocess.run(cmd, check=True)
    if os.path.exists(raw_mp4):
        os.remove(raw_mp4)

    print(json.dumps({"ok": True, "out": out_mp4, "resolution": f"{w}x{h}", "fps": args.fps, "shots": len(shots)}, indent=2))


if __name__ == "__main__":
    main()

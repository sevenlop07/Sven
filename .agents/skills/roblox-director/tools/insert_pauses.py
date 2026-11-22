#!/usr/bin/env python3
"""insert_pauses.py - put the script's designed pauses into the narration audio (script.md §6, §11).

TTS ignores pause tags, so Block 2A stays clean text and the 2-3 designed pauses (0.6-1.3 s: one right after the twist
line, one right before the last line) are written as pause rows in the script sheet: `*(pause 1.0 s, hold the shot)*`.
This tool finds where each pause row sits in the recorded voice and inserts that much silence there.

usage:
  python tools/audio_to_srt.py voice.mp3 --script story.txt --out-dir output/<slug>          # 1. word timings
  python tools/insert_pauses.py voice.mp3 output/<slug>/words.json script-sheet.md -o voice_paused.wav
  python tools/audio_to_srt.py voice_paused.wav --script story.txt --out-dir output/<slug>   # 2. re-time (R3)

How it matches: each pause row is anchored to the end of the spoken row just before it. The last 1-3 words of that row
are searched in order in words.json (lower-case, punctuation stripped, digits allowed); the silence starts 0.05 s after
the matched word ends. A pause that cannot be anchored is reported and skipped (fix the row text or add it by hand).
Needs ffmpeg on PATH. Output is 44.1 kHz stereo WAV (lossless for the final mix).
"""
import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sheetlib import load  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

norm = lambda t: re.sub(r"[^\w]", "", t.lower())


def anchors(sheet):
    """[(pause_secs, last_words_of_previous_spoken_row, row_text)] in script order."""
    rows = load(sheet)["rows"]
    out, prev = [], None
    for r in rows:
        if r["kind"] == "line":
            prev = r
        elif r["kind"] == "pause" and prev is not None:
            toks = [norm(x) for x in prev["text"].split() if norm(x)]
            out.append((r["secs"], toks[-3:], prev["text"]))
    return out


def locate(words, tail, start_idx):
    """index of the last word of `tail` found in order from start_idx, trying 3, 2 then 1 trailing words."""
    W = [norm(w["word"]) for w in words]
    for k in (3, 2, 1):
        t = tail[-k:]
        for i in range(start_idx, len(W) - len(t) + 1):
            if W[i:i + len(t)] == t:
                return i + len(t) - 1
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio"); ap.add_argument("words_json"); ap.add_argument("sheet")
    ap.add_argument("-o", "--out", default=None)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    words = json.load(open(a.words_json, encoding="utf-8"))["words"]
    cuts, pos, skipped = [], 0, []
    for secs, tail, text in anchors(a.sheet):
        i = locate(words, tail, pos)
        if i is None:
            skipped.append(text)
            continue
        t = round(float(words[i]["end"]) + 0.05, 3)
        cuts.append((t, secs, text))
        pos = i + 1
    for t, secs, text in cuts:
        print(f"pause {secs:.2f} s at {t:.2f} s  after: '{text[:50]}'")
    for text in skipped:
        print(f"SKIPPED (no match in words.json): '{text[:60]}'")
    if not cuts:
        print("no pauses to insert")
        return 1 if skipped else 0
    if a.dry_run:
        return 0
    out = a.out or os.path.splitext(a.audio)[0] + "_paused.wav"
    fmt = "aresample=44100,aformat=sample_fmts=fltp:channel_layouts=stereo"
    parts, labels, prev = [], [], 0.0
    for k, (t, secs, _) in enumerate(cuts):
        parts.append(f"[0:a]atrim={prev}:{t},asetpts=PTS-STARTPTS,{fmt}[v{k}]")
        parts.append(f"anullsrc=r=44100:cl=stereo,atrim=0:{secs},asetpts=PTS-STARTPTS,{fmt}[s{k}]")
        labels += [f"[v{k}]", f"[s{k}]"]
        prev = t
    parts.append(f"[0:a]atrim={prev},asetpts=PTS-STARTPTS,{fmt}[vend]")
    labels.append("[vend]")
    graph = ";".join(parts) + ";" + "".join(labels) + f"concat=n={len(labels)}:v=0:a=1[out]"
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", a.audio, "-filter_complex", graph,
           "-map", "[out]", "-c:a", "pcm_s16le", out]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stderr[-1500:])
        return res.returncode
    added = sum(s for _, s, _ in cuts)
    print(f"wrote {out}: {len(cuts)} pauses, +{added:.2f} s. Re-run audio_to_srt.py on it so R3 timings include the pauses.")
    return 1 if skipped else 0


if __name__ == "__main__":
    sys.exit(main())

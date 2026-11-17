#!/usr/bin/env python3
"""
audio_to_srt.py — Generalized MP3/WAV-to-SRT & Contiguous Shot Timeline Extractor for @RobloxDirector.
Extracts exact sentence-level .srt blocks, word-level words.json, and contiguous Shot 1..N windows (0.00s -> runtime)
from any user-supplied .mp3/.wav audio file using faster-whisper (+ verbatim word snapping when --script is provided).

Usage:
  python audio_to_srt.py <audio.mp3> [--script story.txt] [--out-dir <folder>] [--model base] [--min-shot-sec 1.5]
Outputs:
  - <out-dir>/<stem>.srt         (Standard SRT subtitle file with exact audio timestamps)
  - <out-dir>/words.json         (Word-level timestamps for lip-sync & captions)
  - <out-dir>/srt_shots.json     (Contiguous Shot 1..N timeline spine covering 0.00s -> runtime_sec)
"""
import argparse, difflib, json, os, re, subprocess, sys

FFMPEG = r"C:\Users\adminb\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"
if not os.path.exists(FFMPEG):
    FFMPEG = "ffmpeg"

def fmt_srt_time(seconds: float) -> str:
    ms = int(round(max(0.0, seconds) * 1000))
    h = ms // 3600000
    ms %= 3600000
    m = ms // 60000
    ms %= 60000
    s = ms // 1000
    ms %= 1000
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def get_audio_duration(audio_path: str) -> float:
    p = subprocess.run([FFMPEG, "-i", audio_path], capture_output=True, text=True, errors="replace")
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", p.stderr)
    if m:
        return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    return 30.0

def syl_count(word: str) -> int:
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 1
    return max(1, len(re.findall(r"[aeiouy]+", w)))

def snap_words_to_script(asr_words: list, script_text: str) -> list:
    """Aligns ASR words to the ground-truth script tokens so homophones (e.g. 'solved' -> 'salt') are fixed while preserving exact ASR timestamps."""
    script_tokens = [t for t in re.split(r"\s+", script_text.strip()) if t]
    if not script_tokens or not asr_words:
        return asr_words
    norm_asr = [re.sub(r"[^\w']", "", w["word"]).lower() for w in asr_words]
    norm_scr = [re.sub(r"[^\w']", "", t).lower() for t in script_tokens]
    sm = difflib.SequenceMatcher(None, norm_asr, norm_scr)
    fixed = [dict(w) for w in asr_words]
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("equal", "replace") and (i2 - i1) == (j2 - j1):
            for k in range(i2 - i1):
                fixed[i1 + k]["word"] = script_tokens[j1 + k]
    return fixed

def build_contiguous_shots(segments: list, runtime: float, min_shot_sec: float = 1.5) -> list:
    """Merges ultra-short fragments (< min_shot_sec) and builds contiguous Shot 1..N windows from 0.00s to runtime."""
    if not segments:
        return []
    merged = []
    for seg in segments:
        if merged and (seg["end"] - seg["start"] < min_shot_sec) and (seg["end"] - merged[-1]["start"] <= 4.2):
            merged[-1]["end"] = seg["end"]
            merged[-1]["text"] = merged[-1]["text"].rstrip() + " " + seg["text"].lstrip()
            merged[-1]["duration"] = round(merged[-1]["end"] - merged[-1]["start"], 3)
        else:
            merged.append(dict(seg))

    shots = []
    for i, seg in enumerate(merged):
        win_start = 0.0 if i == 0 else round(merged[i]["start"], 3)
        win_end = round(runtime, 3) if i == len(merged) - 1 else round(merged[i + 1]["start"], 3)
        pause_after = round(max(0.0, win_end - seg["end"]), 3)
        shots.append({
            "shot_id": f"Shot {i + 1}",
            "index": i + 1,
            "window_start": win_start,
            "window_end": win_end,
            "window_duration": round(win_end - win_start, 3),
            "speech_start": seg["start"],
            "speech_end": seg["end"],
            "pause_after_sec": pause_after,
            "srt_text": seg["text"]
        })
    return shots

def transcribe_faster_whisper(audio_path: str, model_size: str, script_text: str = None):
    from faster_whisper import WhisperModel
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments_gen, info = model.transcribe(audio_path, word_timestamps=True, vad_filter=True)
    segments = []
    words = []
    for idx, seg in enumerate(segments_gen, 1):
        text = seg.text.strip()
        if not text:
            continue
        s_start = round(float(seg.start), 3)
        s_end = round(float(seg.end), 3)
        seg_words = []
        for w in (seg.words or []):
            clean = w.word.strip()
            if clean:
                w_obj = {"word": clean, "start": round(float(w.start), 3), "end": round(float(w.end), 3)}
                words.append(w_obj)
                seg_words.append(w_obj)
        segments.append({
            "index": idx,
            "start": s_start,
            "end": s_end,
            "duration": round(s_end - s_start, 3),
            "text": text,
            "_word_count": len(seg_words)
        })
    if script_text:
        words = snap_words_to_script(words, script_text)
        wi = 0
        for seg in segments:
            wc = seg.pop("_word_count", 0)
            if wc > 0 and wi + wc <= len(words):
                seg["text"] = " ".join(w["word"] for w in words[wi:wi + wc])
                wi += wc
    else:
        for seg in segments:
            seg.pop("_word_count", None)
    return segments, words, round(float(info.duration), 2)

def fallback_align_from_script(audio_path: str, script_text: str):
    dur = get_audio_duration(audio_path)
    lines = [ln.strip() for ln in re.split(r"[\r\n]+|(?<=[.!?])\s+", script_text) if ln.strip()]
    weights = [sum(syl_count(w) for w in ln.split()) + 2 for ln in lines]
    total_w = max(1, sum(weights))
    usable = max(1.0, dur - 0.4)
    t = 0.1
    segments = []
    words = []
    for idx, (ln, w) in enumerate(zip(lines, weights), 1):
        seg_dur = usable * (w / total_w)
        s_start = round(t, 3)
        s_end = round(t + seg_dur - 0.12, 3)
        segments.append({
            "index": idx,
            "start": s_start,
            "end": s_end,
            "duration": round(s_end - s_start, 3),
            "text": ln
        })
        toks = ln.split()
        tws = [syl_count(tok) for tok in toks]
        tw_sum = max(1, sum(tws))
        wt = s_start
        talk_dur = max(0.2, (s_end - s_start))
        for tok, tw in zip(toks, tws):
            wd = talk_dur * (tw / tw_sum)
            words.append({"word": tok.strip("\"“”"), "start": round(wt, 3), "end": round(wt + wd, 3)})
            wt += wd
        t += seg_dur
    return segments, words, round(dur, 2)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio", help="Input .mp3 or .wav file")
    ap.add_argument("--script", help="Optional text file with the ground-truth story script")
    ap.add_argument("--out-dir", help="Output directory (defaults to audio file's directory)")
    ap.add_argument("--model", default="base", help="Faster-Whisper model size (tiny, base, small)")
    ap.add_argument("--min-shot-sec", type=float, default=1.5, help="Minimum shot duration when merging short fragments")
    args = ap.parse_args()

    out_dir = args.out_dir or os.path.dirname(os.path.abspath(args.audio))
    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(args.audio))[0]
    script_text = open(args.script, encoding="utf-8").read() if (args.script and os.path.exists(args.script)) else None

    try:
        segments, words, runtime = transcribe_faster_whisper(args.audio, args.model, script_text)
        method = f"faster-whisper ({args.model})" + (" + script-snap" if script_text else "")
    except Exception as e:
        if script_text:
            segments, words, runtime = fallback_align_from_script(args.audio, script_text)
            method = "script-syllable-alignment"
        else:
            raise RuntimeError(f"Transcription failed and no --script provided: {e}")

    # Write .srt
    srt_path = os.path.join(out_dir, f"{stem}.srt")
    srt_blocks = []
    for seg in segments:
        srt_blocks.append(f"{seg['index']}\n{fmt_srt_time(seg['start'])} --> {fmt_srt_time(seg['end'])}\n{seg['text']}\n")
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_blocks))

    # Write words.json
    words_path = os.path.join(out_dir, "words.json")
    with open(words_path, "w", encoding="utf-8") as f:
        json.dump({"source": method, "runtime": runtime, "words": words}, f, indent=2, ensure_ascii=False)

    # Build contiguous Shot 1..N timeline spine covering 0.00s -> runtime
    contiguous_shots = build_contiguous_shots(segments, runtime, args.min_shot_sec)
    shots_path = os.path.join(out_dir, "srt_shots.json")
    with open(shots_path, "w", encoding="utf-8") as f:
        json.dump({"runtime": runtime, "shot_count": len(contiguous_shots), "shots": contiguous_shots}, f, indent=2, ensure_ascii=False)

    print(json.dumps({
        "ok": True,
        "method": method,
        "runtime_sec": runtime,
        "srt_segments": len(segments),
        "contiguous_shots": len(contiguous_shots),
        "word_count": len(words),
        "srt_file": srt_path,
        "words_json": words_path,
        "srt_shots_json": shots_path
    }, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

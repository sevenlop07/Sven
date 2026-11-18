#!/usr/bin/env python3
"""
srt_to_director_plan.py — Automated SRT + words.json to Sven Core 3D Director Blueprint.
Converts contiguous srt_shots.json + words.json into multi-beat director_plan.json:
- Auto sub-cuts >3.6s SRT blocks at natural clause/pause boundaries in words.json
- Splits each beat into exact Speech Window (lip-sync + word accents) & Pause Window (reaction/physics)
- Assigns Shot Scale, 4-Axis Angle, Camera Move & 180-deg Axis Side with zero adjacent repeats
- Audits thresholds (Close>=25%, MS<=40%, NonEye>=35%, Move>=70%, Repeats=0)
"""
import argparse
import json
import os
import re


def _infer_emotion(text: str, rel_pos: float) -> str:
    low = text.lower()
    if any(k in low for k in ("!", "sốc", "giật", "bay", "hút", "trời", "chết", "cứu", "what", "whoa", "no!")):
        if "?" in text:
            return "shocked"
        return "shocked" if rel_pos < 0.85 else "laugh"
    if "?" in text:
        return "smirk" if "nhất" in low or "gì" in low else "shocked"
    if any(k in low for k in ("cười", "khúc khích", "haha", "vui", "thắng")):
        return "laugh"
    if any(k in low for k in ("giận", "quát", "cấm", "bực", "tức")):
        return "angry"
    if any(k in low for k in ("sợ", "run", "khóc", "buồn")):
        return "scared"
    return "happy" if rel_pos < 0.45 else "smirk"


def _find_split_time(shot: dict, words: list, max_beat_sec: float, min_beat_sec: float = 1.45):
    ws, we = float(shot["window_start"]), float(shot["window_end"])
    dur = we - ws
    if dur <= max_beat_sec:
        return None
    in_w = [w for w in words if float(w["start"]) >= ws + min_beat_sec and float(w["end"]) <= we - min_beat_sec]
    if len(in_w) < 2:
        return round(ws + dur * 0.52, 3)

    target_mid = ws + dur * 0.50
    best_t, best_score = None, -1e9
    for idx, w in enumerate(in_w[:-1]):
        tok = str(w.get("word", "")).strip()
        gap = max(0.0, float(in_w[idx + 1]["start"]) - float(w["end"]))
        t_cut = round(0.5 * (float(w["end"]) + float(in_w[idx + 1]["start"])), 3)
        if (t_cut - ws) < min_beat_sec or (we - t_cut) < min_beat_sec:
            continue
        punct_bonus = 3.0 if tok.endswith((".", "!", "?", ":")) else (2.0 if tok.endswith((",", ";")) else 0.0)
        dist_pen = abs(t_cut - target_mid)
        score = punct_bonus + gap * 4.0 - dist_pen
        if score > best_score:
            best_score = score
            best_t = t_cut
    return best_t


def _extract_accents(words: list, ts: float, te: float, fps: int, fs: int, fe: int) -> list:
    in_w = [w for w in words if float(w["end"]) >= ts and float(w["start"]) <= te]
    accents = []
    last_fr = fs - 20
    for w in in_w:
        tok = str(w.get("word", "")).strip()
        clean = re.sub(r"[^\w]", "", tok)
        w_fr = max(fs, min(fe - 6, int(round(float(w["start"]) * fps)) + 1))
        heavy = tok.endswith(("!", "?", ",", "."))
        if (heavy or len(clean) >= 4) and (w_fr - last_fr) >= 18:
            accents.append({"frame": w_fr, "word": tok, "heavy": heavy})
            last_fr = w_fr
    if not accents and in_w:
        mid_w = in_w[len(in_w) // 2]
        w_fr = max(fs, min(fe - 6, int(round(float(mid_w["start"]) * fps)) + 1))
        accents.append({"frame": w_fr, "word": str(mid_w.get("word", "")).strip(), "heavy": False})
    return accents


def compile_director_plan(srt_shots: dict, words_data: dict, fps: int = 30, max_beat_sec: float = 3.6, aspect: str = "16:9") -> dict:
    runtime = float(srt_shots["runtime"])
    total_frames = int(round(runtime * fps))
    words = (words_data or {}).get("words", [])
    raw_shots = srt_shots.get("shots", [])

    # 1. Sub-cut long SRT blocks on exact word clause gaps
    raw_beats = []
    for sh in raw_shots:
        split_t = _find_split_time(sh, words, max_beat_sec=max_beat_sec)
        ws, we = float(sh["window_start"]), float(sh["window_end"])
        sp_s, sp_e = float(sh["speech_start"]), float(sh["speech_end"])
        txt = sh["srt_text"]
        if split_t is None:
            raw_beats.append({
                "parent_shot": sh["shot_id"], "t_start": ws, "t_end": we,
                "speech_start": sp_s, "speech_end": sp_e, "srt_text": txt, "sub": "full",
            })
        else:
            w_a = [w["word"] for w in words if float(w["start"]) >= ws - 0.05 and float(w["end"]) <= split_t + 0.02]
            w_b = [w["word"] for w in words if float(w["start"]) > split_t - 0.02 and float(w["end"]) <= we + 0.05]
            raw_beats.append({
                "parent_shot": sh["shot_id"], "t_start": ws, "t_end": split_t,
                "speech_start": sp_s, "speech_end": min(sp_e, split_t),
                "srt_text": " ".join(w_a) if w_a else txt, "sub": "part_A",
            })
            raw_beats.append({
                "parent_shot": sh["shot_id"], "t_start": split_t, "t_end": we,
                "speech_start": max(split_t, sp_s), "speech_end": max(split_t, sp_e),
                "srt_text": " ".join(w_b) if w_b else "(Reaction / Pause)", "sub": "part_B",
            })

    # 2. Assign Sven Core Camera Scale, Angle & Move ensuring >45-deg cut contrast & zero repeats
    scale_cycle_story = ["WS", "MCU", "OTS", "CU", "MS", "INSERT", "MCU", "OTS"]
    angle_cycle = ["eye", "low", "eye", "high", "low", "dutch"]
    move_cycle = ["push_in", "static", "push_in", "truck", "pull_out", "orbit_arc"]

    beats_out = []
    prev_scale, prev_angle = None, None
    n_beats = max(1, len(raw_beats))

    for i, b in enumerate(raw_beats):
        fs = 1 if i == 0 else max(beats_out[-1]["fe"] + 1, int(round(b["t_start"] * fps)) + 1)
        fe = total_frames if i == n_beats - 1 else max(fs + 12, int(round(b["t_end"] * fps)))
        sp_fs = max(fs, int(round(b["speech_start"] * fps)) + 1)
        sp_fe = min(fe, int(round(b["speech_end"] * fps)))
        has_pause = (fe - sp_fe) >= 10
        rel = i / float(max(1, n_beats - 1))
        emo = _infer_emotion(b["srt_text"], rel)

        if i == 0:
            sc, ang, mv, mv_amt = "WS", "eye", "push_in", 0.09
        elif 0.72 <= rel <= 0.90 and ("!" in b["srt_text"] or emo == "shocked"):
            sc, ang, mv, mv_amt = "CU", "dutch", "dolly_zoom", 0.10
        elif i == n_beats - 1:
            sc, ang, mv, mv_amt = "WS", "high", "pull_out", 0.10
        elif b["sub"] == "part_B":
            # Punchline / second half of long SRT sentence always tightens in!
            sc = "CU" if prev_scale != "CU" else "MCU"
            ang = "low" if emo in ("smirk", "angry") else ("dutch" if emo == "shocked" else "high")
            mv, mv_amt = ("static" if i % 3 == 0 else "push_in"), 0.08
        else:
            sc = scale_cycle_story[i % len(scale_cycle_story)]
            ang = angle_cycle[i % len(angle_cycle)]
            mv = move_cycle[i % len(move_cycle)]
            mv_amt = 0.08

        # Guarantee zero adjacent identical (scale, angle)
        if sc == prev_scale and ang == prev_angle:
            sc = "CU" if sc != "CU" else "MCU"
            ang = "low" if ang != "low" else "high"
        # Cap MS/OTS <= 40% by preferring MCU/CU when needed
        if i > 2 and sc in ("MS", "OTS"):
            ms_so_far = sum(1 for x in beats_out if x["scale"] in ("MS", "OTS"))
            if (ms_so_far + 1) / float(len(beats_out) + 1) > 0.38:
                sc = "MCU" if prev_scale != "MCU" else "CU"

        prev_scale, prev_angle = sc, ang
        accents = _extract_accents(words, b["t_start"], b["t_end"], fps, fs, fe)
        beats_out.append({
            "beat_index": i + 1,
            "parent_shot": b["parent_shot"],
            "sub": b["sub"],
            "t_start": round(b["t_start"], 3),
            "t_end": round(b["t_end"], 3),
            "dur_sec": round((fe - fs + 1) / float(fps), 2),
            "fs": fs,
            "fe": fe,
            "speech_fs": sp_fs,
            "speech_fe": sp_fe,
            "pause_fs": (sp_fe + 1) if has_pause else None,
            "pause_fe": fe if has_pause else None,
            "scale": sc,
            "angle": ang,
            "move": mv,
            "move_amt": mv_amt,
            "axis_side": 1,
            "emotion": emo,
            "camera_shake_suggested": ("!" in b["srt_text"] and emo in ("shocked", "angry")),
            "accent_frames": accents,
            "srt_text": b["srt_text"],
        })

    nb = max(1, len(beats_out))
    close_n = sum(1 for x in beats_out if x["scale"] in ("CU", "MCU", "INSERT"))
    ms_n = sum(1 for x in beats_out if x["scale"] in ("MS", "OTS"))
    non_eye_n = sum(1 for x in beats_out if x["angle"] != "eye")
    move_n = sum(1 for x in beats_out if x["move"] != "static")
    repeats = sum(1 for k in range(1, nb) if beats_out[k]["scale"] == beats_out[k - 1]["scale"] and beats_out[k]["angle"] == beats_out[k - 1]["angle"])

    return {
        "runtime": runtime,
        "fps": fps,
        "aspect": aspect,
        "beat_count": nb,
        "audit": {
            "close_pct": round(100.0 * close_n / nb, 1),
            "ms_pct": round(100.0 * ms_n / nb, 1),
            "non_eye_pct": round(100.0 * non_eye_n / nb, 1),
            "move_pct": round(100.0 * move_n / nb, 1),
            "adjacent_repeat_warnings": repeats,
        },
        "beats": beats_out,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("srt_shots", help="Path to srt_shots.json")
    ap.add_argument("--words", default="", help="Path to words.json (defaults to sibling words.json)")
    ap.add_argument("--out", default="", help="Output director_plan.json path")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--max-beat-sec", type=float, default=3.6)
    ap.add_argument("--aspect", choices=["16:9", "9:16"], default="16:9")
    args = ap.parse_args()

    srt_shots = json.load(open(args.srt_shots, encoding="utf-8"))
    words_path = args.words or os.path.join(os.path.dirname(os.path.abspath(args.srt_shots)), "words.json")
    words_data = json.load(open(words_path, encoding="utf-8")) if os.path.exists(words_path) else {}
    plan = compile_director_plan(srt_shots, words_data, fps=args.fps, max_beat_sec=args.max_beat_sec, aspect=args.aspect)

    out_path = args.out or os.path.join(os.path.dirname(os.path.abspath(args.srt_shots)), "director_plan.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)
    print(json.dumps({"ok": True, "out": out_path, "beat_count": plan["beat_count"], "audit": plan["audit"]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

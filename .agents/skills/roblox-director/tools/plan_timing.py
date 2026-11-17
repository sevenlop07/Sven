#!/usr/bin/env python3
"""plan_timing.py - a planned words.json + cuts.txt from a script sheet, so shotlist_check / pacing_check / make_caps
run on a plan before any voice exists. Zero tokens. The real take's words.json replaces both (rebuild cuts from it).
usage: python3 plan_timing.py script-sheet.md [--shots shot-list.md] [--tail 1.2] [--wpm 220] [--out .] [--rewrite-times]
  writes  words_planned.json  (token times: each row's time split by the spoken syllables of its words, with a 0.15 s
                               gap after every sentence; designed pauses are real gaps; slow reads stretch their row)
          cuts.txt            only with --shots: the shot list's starts, excluding 0
          cuts_draft.txt      without --shots: a draft cut 1 frame before each row start, plus one at the first comma of
                               10+-word rows, rows over 3.5 s and the hook (never overwrites a real cuts.txt)
                               Draft cuts plan no holds, so pacing_check's ending-pace line means something only with --shots
Order on a plan: (1) --rewrite-times on the sheet, (2) build the shot list from words_planned.json, (3) --shots shotlist.md
for the real cuts.txt, (4) pacing_check.
  prints  the model's `start-end (pct %)` per row and the runtime (paste the line for pacing_check: duration).
  --rewrite-times  writes those times into the sheet's time column in place (keeps a .bak copy).
Planned times are HYPOTHESIS: a real take moves cuts by about +-0.1-0.2 s."""
import argparse, json, os, re, shutil
import sheetlib
from sheetlib import load, spoken, syl, sentences, split_row

ap = argparse.ArgumentParser()
ap.add_argument("sheet"); ap.add_argument("--wpm", type=float, default=220); ap.add_argument("--shots"); ap.add_argument("--tail", type=float, default=1.2)
ap.add_argument("--out", default="."); ap.add_argument("--rewrite-times", action="store_true")
a = ap.parse_args()
sheetlib.WPS = a.wpm / 60
D = load(a.sheet, a.tail); R = D["rows"]; RT = D["runtime"]
GAP, LEAD = 0.15, 1 / 30
words = []
for k, r in enumerate(R):
    if r["kind"] != "line": continue
    sents = [s.split() for s in sentences(r["text"])]
    dur = r["end"] - r["start"]; gap = min(GAP, 0.4 * dur / max(1, len(sents)))
    pre_pause = k + 1 < len(R) and R[k + 1]["kind"] == "pause"     # a pause row IS the whole silence: no extra gap
    talk = dur - gap * (len(sents) - pre_pause)
    wt = [[max(1, sum(syl(w) for w in spoken(tok))) for tok in s] for s in sents]
    unit = talk / max(1, sum(map(sum, wt)))
    t = r["start"]
    for s, ws in zip(sents, wt):
        for tok, w in zip(s, ws):
            clean = tok.strip("\"“”")
            words.append(dict(word=clean, start=round(t, 3), end=round(t + w * unit, 3))); t += w * unit
        t += gap
os.makedirs(a.out, exist_ok=True)
json.dump(dict(source="planned by plan_timing.py (220 wpm model)", runtime=round(RT, 2), words=words),
          open(os.path.join(a.out, "words_planned.json"), "w"), indent=0)

if a.shots:
    cuts = []
    for ln in open(a.shots, encoding="utf-8"):
        c = split_row(ln) if ln.strip().startswith("|") else []
        if len(c) >= 12 and re.match(r"^\d+$", c[0]) and re.search(r"\d", c[1]):
            st0 = float(re.split(r"\s*[-–]\s*", c[1].replace("s", ""))[0])
            if st0 > 0: cuts.append(st0)
    src = a.shots
else:
    cuts, wi = [], 0
    for r in R:
        if r["kind"] != "line": continue
        if r["start"] > 0.2: cuts.append(round(r["start"] - LEAD, 3))
        if r["words"] >= 10 or r["end"] - r["start"] > 3.5 or (r["start"] < 0.2 and r["end"] > 2.5):
            # pacing.md rule 5: 10+ word rows get a 2nd shot at a clause break; the first cut lands by 2.5 s
            mine = [w for w in words if r["start"] - 1e-6 <= w["start"] < r["end"]]
            k = next((i for i, w in enumerate(mine[:-2]) if i >= 2 and w["word"].endswith(",")), len(mine) // 2)
            if r["start"] < 0.2 and mine[k + 1]["start"] > 2.5: k = max(i for i, w in enumerate(mine) if w["start"] <= 2.5) - 1
            cuts.append(round(mine[k + 1]["start"] - LEAD, 3))
    src = "draft (one cut per row start)"
cut_file = os.path.join(a.out, "cuts.txt" if a.shots else "cuts_draft.txt")
open(cut_file, "w").write("\n".join(f"{c:.3f}" for c in sorted(cuts)) + "\n")

fmt = lambda r: (f"{r['start']:.1f}-{r['end']:.1f}" + ("" if r["kind"] == "pause" else f" ({100 * r['start'] / RT:.0f} %)"))
for r in R: print(f"{fmt(r):22s} {r['text'][:60] if r['kind'] == 'line' else '(pause %.1f s)' % r['secs']}")
print(f"\n{len(words)} tokens, speech ends {D['speech_end']:.2f} s, runtime {RT:.2f} s; cuts: {len(cuts)} from {src}")
print(f"next: python3 pacing_check.py {cut_file} {a.out}/words_planned.json {RT:.2f}")
if a.rewrite_times:
    if D["time_col"] is None: raise SystemExit("no time column to rewrite")
    lines = open(a.sheet, encoding="utf-8").read().split("\n"); shutil.copy(a.sheet, a.sheet + ".bak")
    for r in R:
        c = split_row(lines[r["lineno"]]); c[D["time_col"]] = fmt(r); lines[r["lineno"]] = "| " + " | ".join(c) + " |"
    open(a.sheet, "w", encoding="utf-8").write("\n".join(lines))
    print(f"rewrote the time column of {a.sheet} (backup {a.sheet}.bak)")

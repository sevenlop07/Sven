#!/usr/bin/env python3
# shotlist_check.py shotlist.md  -> look targets from the shot-list table (templates/shot-list.md codes). Zero tokens.
# A setup = set + size + angle family (eye/low/high/top/dutch, degrees ignored), whoever is in it: the same framing in
# the same room reads as the same shot (L17, HYPOTHESIS). Move variety: no move type on >40 % of shots, >=3 types (L20,
# HYPOTHESIS). INFO lines are counts to read, not pass/fail.
import re, sys
from collections import Counter
if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"): sys.exit("usage: python3 shotlist_check.py shotlist.md")
rows, short, build, sec = [], [], [], ""
for ln in open(sys.argv[1], encoding="utf-8"):
    if ln.startswith("## "): sec = ln
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    if sec.lower().startswith("## build cost") and ln.startswith("|") and len(c) >= 4 and not set(c[0]) <= set("-: ") and c[0] != "item":
        build.append(c); continue
    if len(c) >= 12 and re.match(r"^\d+$", c[0]) and re.search(r"\d", c[1]):
        rows.append(c)
    elif ln.startswith("|") and re.match(r"^\d+$", c[0]) and re.search(r"\d", c[1] if len(c) > 1 else ""):
        short.append(c[0])
if short: print(f"WARNING: shot rows with fewer than 12 cells were skipped: {short}")
if not rows: sys.exit("no shot rows found")
def times(t):
    a, b = re.split(r"\s*[-–]\s*", t.replace("s", ""))[:2]; return float(a), float(b)
MOODS = ("normalDay", "sad", "sadWarm", "scaryNight", "twistReveal", "twistNight", "dreamMemory", "sad_night", "sadWarm_night")
n = len(rows); T = [times(r[1]) for r in rows]; L = [b - a for a, b in T]
size = [r[3].upper().split()[0] for r in rows]; ang = [r[4].lower().split()[0] if r[4].strip() else "eye" for r in rows]
cam = [r[5].upper().lstrip()[:1] for r in rows]
face = ["(F)" in r[6] for r in rows]; key = [r[2].lstrip().startswith("★") for r in rows]
idle = [r[7].lower().startswith("idle") for r in rows]
rule = ["RULE" in r[10].upper() for r in rows]; change = ["RULE-CHANGE" in r[10].upper() for r in rows]
holds = [l for l in L if l > 3.5]
subj = lambda r: re.sub(r"\(F\).*", "", r[6]).split(":")[0].strip().lower()
setups = Counter((r[8].lower(), size[i], ang[i]) for i, r in enumerate(rows))
def mtype(c):
    m = re.sub(r"^[EZS]\s*", "", c.strip()).lower()
    for k in ("push", "pull", "truck", "track", "crane", "orbit", "pan", "tilt", "dolly", "follow", "static", "rack", "whip", "zoom"):
        if m.startswith(k) or (k == "static" and c.strip().upper().startswith("S")): return k
    return m.split()[0] if m else "?"
moves = Counter(mtype(r[5]) for r in rows)
pct = lambda x: 100 * sum(x) / n
def line(name, val, ok): print(f"{name:44s} {val:>10s}  {ok if isinstance(ok, str) else ('PASS' if ok else 'FAIL')}")
close = pct([s in ("CU", "MCU", "ECU") for s in size]); wide = pct([s in ("WS", "EWS") for s in size]); ins = pct([s == "INS" for s in size])
line("L1 close shots >=25%", f"{close:.0f}%", close >= 25)
line("L2 MS <=40%", f"{pct([s == 'MS' for s in size]):.0f}%", pct([s == 'MS' for s in size]) <= 40)
line("L3 wides (WS+EWS) 15-30%", f"{wide:.0f}%", 15 <= wide <= 30)
line("L4 inserts (INS) 8-12%", f"{ins:.0f}%", 8 <= ins <= 12)
line("L5 readable face >=60%", f"{pct(face):.0f}%", pct(face) >= 60)
kf = [face[i] for i in range(n) if key[i]]
line("L5 key lines with readable face 100%", f"{sum(kf)}/{len(kf)}", all(kf))
line("L6 non-eye angles >=35%", f"{pct([a != 'eye' for a in ang]):.0f}%", pct([a != 'eye' for a in ang]) >= 35)
line("L7 in-engine moves (E) >=70%", f"{pct([c == 'E' for c in cam]):.0f}%", pct([c == 'E' for c in cam]) >= 70)
line("L8 edit-zoom only (Z) <=20%", f"{pct([c == 'Z' for c in cam]):.0f}%", pct([c == 'Z' for c in cam]) <= 20)
line("L8 static (S) <=10%", f"{pct([c == 'S' for c in cam]):.0f}%", pct([c == 'S' for c in cam]) <= 10)
line("L9 shots >3.5 s (holds) <=2, all <=6 s", f"{len(holds)}", len(holds) <= 2 and max(L) <= 6)
line("L10 first cut <=2.5 s", f"{L[0]:.2f}s", L[0] <= 2.5)
line("L11 rule object in shot 1 and >=50%", f"{pct(rule):.0f}%", rule[0] and pct(rule) >= 50)
line("L12 RULE-CHANGE shots (each change shown)", f"{sum(change)}", "INFO")
line("L14 shots with mouth flaps", f"{sum('flap' in r[7].lower() or 'flap' in r[6].lower() for r in rows)}", "INFO")
line("L15 stiff idle <=40%", f"{pct(idle):.0f}%", pct(idle) <= 40)
line("L16 locations 5-8", f"{len(set(r[8].lower() for r in rows))}", 5 <= len(set(r[8].lower() for r in rows)) <= 8)
top = setups.most_common(1)[0]
line("L17 max repeats of one setup <=2", f"{top[1]}", top[1] <= 2)
if top[1] > 2: print(f"    most repeated: {top[0]}")
line("L18 final shot >=3 s", f"{L[-1]:.2f}s", L[-1] >= 3)
mt, mc = moves.most_common(1)[0]
line("L20 move variety: top type <=40 %, >=3 types", f"{mt} {100 * mc / n:.0f}%", 100 * mc / n <= 40 and len(moves) >= 3)
over = []
for c in build:
    nw = re.findall(r"\d+", c[1]); cap = re.findall(r"≤\s*(\d+)", c[3]) or re.findall(r"\d+", c[3])   # the first "≤N" is the cap
    if nw and cap and int(nw[0]) > int(cap[0]) and not (len(c) > 4 and c[4].strip()): over.append(f"{c[0]} {nw[0]}>{cap[0]}")
line("build-cost block: new <= cap (or a reason)", f"{len(build)} rows" if build else "missing", (not over) if build else "INFO: fill it")
if over: print("    over cap with no reason:", over)
bad = sorted({r[9].split()[0].split("@")[0] for r in rows if r[9].strip() and r[9].split()[0].split("@")[0].rstrip(",") not in MOODS})
line("mood column uses preset names (mood@clock)", f"{len(bad)} other", "INFO: variants? " + ", ".join(bad) if bad else True)

#!/usr/bin/env python3
"""script_check.py - the numbers for script.md §9.3 from a script sheet. Zero tokens.
usage: python3 script_check.py script-sheet.md [--target 117] [--tail 1.2] [--last-reveal 52] [--wpm 220]
       [--log ROTATION-LOG.md] [--pretwist pretwist.txt] [--rules ../script.md]
  --log       checks the core rotation fields against the last episodes (templates/rotation-log.md). The plan's own
              row is skipped: --ep E04, or the sheet's "Episode" field, or a last row identical to this plan
  --pretwist  writes the lines before the reveal to a file for the blind guess test (script.md §3.3)
  --target       target runtime in s (default: the first "target" / "runtime" number in the sheet text)
  --last-reveal  last episode's reveal % (rotation log), for the >=10-point shift
Also: the voice tests of script.md §0.1 and the no-copy check of §9.4 (patterns.txt, ref_lines.txt, examples/gold-*.md),
and header fields (a `field | value` table): "Twist mechanism words", "Logic questions", "Guess test", "Staged contrast".
Times come from the sheetlib model (220 wpm, slow reads, pause rows), NOT from the sheet's time column; rows whose
written start is >0.3 s off the model are listed so you can fix the column. Lines marked CHECK need a human look
(fragments, specifics that are objects, tense, "sounds like the user"). Banned phrases are read from script.md §9.1."""
import argparse, os, re, statistics as st
import sheetlib
from sheetlib import load, spoken, syl, sentences

ap = argparse.ArgumentParser()
ap.add_argument("sheet"); ap.add_argument("--wpm", type=float, default=220); ap.add_argument("--target", type=float); ap.add_argument("--tail", type=float, default=1.2)
ap.add_argument("--last-reveal", type=float); ap.add_argument("--log"); ap.add_argument("--pretwist"); ap.add_argument("--ep")
HERE = os.path.dirname(os.path.abspath(__file__))
ap.add_argument("--rules", default=os.path.join(HERE, "..", "script.md"))
a = ap.parse_args()
sheetlib.WPS = a.wpm / 60
D = load(a.sheet, a.tail); R = D["rows"]; RT = D["runtime"]
L = [r for r in R if r["kind"] == "line"]; P = [r for r in R if r["kind"] == "pause"]
TXT = open(a.sheet, encoding="utf-8").read()
HDR = {}
for ln in TXT.split("\n"):
    c = [x.strip() for x in ln.strip().strip("|").split("|")] if ln.startswith("|") else []
    if len(c) == 2 and c[0] and not set(c[0]) <= set("-: "): HDR[c[0].lower().strip("* ")] = c[1]
hdr = lambda key: next((v for k, v in HDR.items() if k.startswith(key)), "")   # field names must START with the key
def load_patterns(path):
    P, sec = {}, None
    for ln in open(path, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln.strip() or ln.startswith("#"): continue
        if ln.startswith("["): sec = ln.strip("[] "); P[sec] = []; continue
        parts = [x.strip() for x in ln.split(" | ")]
        P[sec].append((re.compile(parts[0], re.I), parts[1] if len(parts) > 1 else "", parts[2] if len(parts) > 2 else ""))
    return P
PAT = load_patterns(os.path.join(HERE, "patterns.txt"))
out = []
def row(item, name, val, ok): out.append(f"{'PASS' if ok is True else ('FAIL' if ok is False else ok):9s} {item:4s} {name:48s} {val}")
pct = lambda t: 100 * t / RT

# ---- sentences (spoken words, narration + dialogue) ----
S = []   # (speaker, text, n_spoken, in_quote_dialogue)
for r in L:
    for s in sentences(r["text"]):
        S.append((r["speaker"], s, sum(len(spoken(x)) for x in s.split())))
lens = [n for _, _, n in S]; N = len(S); W = sum(r["words"] for r in L)

# ---- 2 rule line ----
r0 = L[0]; t0 = r0["text"]
row("2", "line 1: 8-15 words, 'In this world/town,'", f"{r0['words']} words", 8 <= r0["words"] <= 15 and bool(re.match(r"in this (world|town),", t0, re.I)))
row("2", "line 1 spoken in 2.0-4.5 s", f"{r0['end'] - r0['start']:.1f} s", 2.0 <= r0["end"] - r0["start"] <= 4.5)

# ---- 3 stake + rule clear ----
stake = next((r["start"] for r in L[1:] if any(re.sub(r"[^\w']", "", x).lower() in ("i", "me", "my", "mine", "i'm", "i'd", "i've")
                                               for x in r["tokens"])), None)
row("3", "stake line (first I/me/my/mine) starts by 6 s", f"{stake:.1f} s" if stake is not None else "none", stake is not None and stake <= 6)
rc = [r for r in L if "rule clear" in r["beat"].lower()]
if rc: row("3", "rule fully clear <=9 % and <=15 s", f"{rc[-1]['end']:.1f} s = {pct(rc[-1]['end']):.1f} %", pct(rc[-1]["end"]) <= 9 and rc[-1]["end"] <= 15)
else: row("3", "rule fully clear <=9 % and <=15 s", "tag the row that completes the rule 'rule clear' in the beat column", "CHECK")

# ---- 5 beats ----
def first(pat, flags=re.I):
    return next((r for r in L if re.search(pat, r["beat"], flags)), None)
B = dict(inciting=first(r"inciting"), misread=first(r"misread"), doubt=first(r"doubt"),
         reveal=first(r"^\W*(reveal|TWIST)", 0) or first(r"\breveal"), twist=first(r"TWIST", 0), turn=first(r"^\W*turn"),
         climax=first(r"climax(?! build)"), payoff=first(r"extra payoff"), last=first(r"LAST LINE", 0) or L[-1])
B["twist"] = B["twist"] or B["reveal"]
def beat(name, r, lo, hi, note=""):
    if not r: row("5", f"{name} {lo}-{hi} %", "no row tagged", "CHECK"); return
    p = pct(r["start"]); row("5", f"{name} {lo}-{hi} %{note}", f"{r['start']:.1f} s = {p:.1f} %", lo <= p <= hi)
beat("misread plant", B["misread"], 10, 36)
if B["misread"] and not re.search(r"\b(said|says|say|called|call|thought|think|believed?|knew|everyone|everybody|kids|grown-ups|people|"
                                    r"sign|poster|news|police|teacher|mom|dad|rumou?r)\b|\"", B["misread"]["text"], re.I):
    row("5", "misread row states the belief, attributed", f"'{B['misread']['text'][:50]}' reads as an observation", "CHECK")
beat("reveal (first truth line)", B["reveal"], 49, 78)
beat("twist line", B["twist"], 49, 78)
beat("climax starts", B["climax"], 69, 96)
beat("extra payoff", B["payoff"], 85, 100)
beat("last line starts", B["last"], 92, 100)
if B["doubt"] and B["reveal"]: row("5", "doubt before the reveal", f"{pct(B['doubt']['start']):.1f} %", B["doubt"]["start"] < B["reveal"]["start"])
if B["turn"] and B["reveal"]: row("5", "turn after the reveal", f"{pct(B['turn']['start']):.1f} %", B["turn"]["start"] > B["reveal"]["start"])
if a.last_reveal is not None and B["twist"]:
    row("5", "reveal shift vs last episode >=10 points", f"{pct(B['twist']['start']) - a.last_reveal:+.1f}", abs(pct(B["twist"]["start"]) - a.last_reveal) >= 10)
if B["inciting"] and B["reveal"]:
    w1 = sum(r["words"] for r in L if r["start"] < B["inciting"]["start"]); w2 = sum(r["words"] for r in L if B["inciting"]["start"] <= r["start"] < B["reveal"]["start"])
    sh = [100 * x / W for x in (w1, w2, W - w1 - w2)]
    row("5", "act word share each <=55 %", " / ".join(f"{x:.0f}" for x in sh), max(sh) <= 55)

# ---- 8 specifics (numbers are objective; named objects are a hand count) ----
NUMW = set("two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen "
           "nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand".split())
nums = [x.strip("\"',.!?") for r in L for x in r["tokens"] if re.search(r"\d", x) or x.strip("\"',.!?").lower() in NUMW]
per100 = len(nums) / RT * 100
row("8", ">=3 concrete specifics per 100 s (numbers only)", f"{len(nums)} = {per100:.1f}/100 s: {', '.join(nums[:14])}", True if per100 >= 3 else "CHECK")

# ---- 9 sentence stats ----
row("9", "sentences: mean 6-8 spoken words", f"{N} sentences, mean {st.mean(lens):.1f}", 6 <= st.mean(lens) <= 8)
p6 = 100 * sum(n <= 6 for n in lens) / N; p3 = 100 * sum(n <= 3 for n in lens) / N
row("9", "sentences <=6 words 45-65 %", f"{p6:.0f} %", 45 <= p6 <= 65)
row("9", "sentences <=3 words 15-25 %", f"{p3:.0f} %", 15 <= p3 <= 25)
row("9", "longest sentence <=20 words", f"{max(lens)}", max(lens) <= 20)
starts = [bool(re.match(r"^[\"“]?(and|but|so|then)\b", s, re.I)) for _, s, _ in S]
run3 = any(all(starts[i:i + 3]) for i in range(len(starts) - 2))
row("9", "And/But/So/Then starts <=20 %, never 3 in a row", f"{100 * sum(starts) / N:.0f} %{' (3 in a row!)' if run3 else ''}", sum(starts) / N <= .20 and not run3)
fw = [re.sub(r"[^\w']", "", s.split()[0]).lower() for _, s, _ in S]
same = [S[i][1] for i in range(len(fw) - 2) if fw[i] == fw[i + 1] == fw[i + 2] and fw[i] not in ("and", "but", "so", "then")]
row("9", "same opening word never 3 in a row", f"{len(same)} runs {same[:2]}", not same)
VERB = re.compile(r"\b(is|are|was|were|be|been|am|has|have|had|do|does|did|can|could|will|would|said|says|got|get|went|go|came|come|"
                  r"made|make|makes|knew|know|saw|see|took|take|told|tell|put|ran|let|felt|left|thought|sat|stuck|threw|broke|"
                  r"wore|held|found|heard|gave|kept|fell|stood|wrote|hid|met|brought|bought|slept|woke|lost|won|"
                  r"wants|needs|likes|knows|goes|comes|looks|gets|says|shows|turns|stops|keeps|tells|feels|"
                  r"\w+'(s|re|m|d|ve|ll)|\w+n't|\w+ed)\b|\b(i|you|he|she|it|we|they|who)\s+\w+", re.I)
frag = [s for _, s, _ in S[1:] if not VERB.search(s)]   # (line 1 is the rule)
row("9", "verbless fragments 12-25 %, each adds a fact", f"{100 * len(frag) / N:.0f} % candidates: {' | '.join(frag[:8])}", "CHECK")

# ---- 0 voice: FK grade + long words ----
sw = [w for r in L for x in r["tokens"] for w in spoken(x)]
sy = [syl(w) for w in sw]
fk = 0.39 * len(sw) / N + 11.8 * sum(sy) / len(sw) - 15.59
row("0", "Flesch-Kincaid grade <=2.5 (heuristic syllables)", f"{fk:.1f}", fk <= 2.5)
long = sorted({w.lower() for w, n in zip(sw, sy) if n >= 3})
row("0", "3+ syllable words <=5 %, concrete nouns only", f"{100 * sum(n >= 3 for n in sy) / len(sw):.1f} %: {', '.join(long[:14])}", True if sum(n >= 3 for n in sy) / len(sw) <= .05 else False)

# ---- 0.1 voice: the user's register (patterns.txt) ----
NS = [x for x in S if x[0] == "NARR"]
narr_secs = sum(r["end"] - r["start"] for r in L if r["speaker"] == "NARR")
mk = [(s, [rx.pattern for rx, _, _ in PAT["casual-markers"] if rx.search(s)]) for _, s, _ in NS]
nmk = sum(len(m) for _, m in mk); need = narr_secs / 15
double = [s for s, m in mk if len(m) > 1]
used = {}
for _, m in mk:
    for x in m: used[x] = used.get(x, 0) + 1
tic = [k for k, v in used.items() if v >= 4]
row("0.1", "casual markers ~1 per 15 s of narration", f"{nmk} for {narr_secs:.0f} s (need {need:.0f}){' 2 in one: ' + str(double[:2]) if double else ''}{' tic: ' + str(tic) if tic else ''}",
    nmk >= need - 0.5 and not double and not tic)
tone = list(dict.fromkeys((s, lab) for _, s, _ in S for rx, lab, _ in PAT["narrator-tone"] if rx.search(s)))
row("0.1", "narrator-tone / written-English patterns: 0", f"{len(tone)} {[f'{l}: {x[:40]}' for x, l in tone[:5]]}", not tone)
unc = [s for _, s, _ in S if any(rx.search(s) for rx, _, _ in PAT["uncontracted"])]
row("0.1", "uncontracted pairs (stressed on purpose?)", f"{len(unc)} {[x[:40] for x in unc[:4]]}", True if not unc else "CHECK")
sim = [s for _, s, _ in S if any(rx.search(s) for rx, _, _ in PAT["similes"])]
row("0.1", "similes <=1 per 30 s", f"{len(sim)} (max {RT / 30:.0f}) {[x[:30] for x in sim[:3]]}", len(sim) <= RT / 30)

# ---- 13 no-copy: shapes + n-gram overlap with the refs and the golds (script.md §9.4) ----
me = os.path.basename(a.sheet).replace(".md", "")
shape = [(s, src, lab) for _, s, _ in S for rx, src, lab in PAT["copy-shapes"] if me not in src and rx.search(s)]
row("13", "no gold/ref line shapes (patterns.txt)", f"{len(shape)} {[f'{lab} <- {x[:30]}' for x, src, lab in shape[:4]]}", not shape)
STOP = set("a an the and but so then i me my you your he him his she her it its we our they them their to of in on at for with "
           "was were is are be been had has have do did not no just that this there what when who all one up out".split())
tok = lambda t: re.findall(r"[a-z0-9']+", t.lower())
def grams(t, n):
    w = tok(t)
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1) if sum(x not in STOP for x in w[i:i + n]) >= n - 2
            and "world" not in w[i:i + n] and "town" not in w[i:i + n][:3]}
src = []
for ln in (open(os.path.join(HERE, "ref_lines.txt"), encoding="utf-8") if os.path.exists(os.path.join(HERE, "ref_lines.txt")) else []):
    if not ln.startswith("#") and ln.count(" | ") >= 2: src.append((ln.split(" | ")[0], ln.split(" | ", 2)[2].strip()))
for g in sorted(os.listdir(os.path.join(HERE, "..", "examples"))):
    gp = os.path.join(HERE, "..", "examples", g)
    if g.endswith(".md") and os.path.abspath(gp) != os.path.abspath(a.sheet):
        src += [(g[:-3], r["text"]) for r in load(gp)["rows"] if r["kind"] == "line"]
over = {4: [], 5: []}
for n in (4, 5):
    G = {}
    for who, t in src:
        for x in grams(t, n): G.setdefault(x, who)
    for _, s, _ in S[1:]:
        hit = [(" ".join(x), G[x]) for x in grams(s, n) if x in G]
        if hit: over[n].append(f"'{hit[0][0]}' ({hit[0][1]})")
row("13", "no 5-word overlap (3+ content words) with refs/golds", f"{len(over[5])} {over[5][:4]}", not over[5])
row("13", "4-word overlaps (common English is fine)", f"{len(over[4])} {over[4][:5]}", True if not over[4] else "CHECK")

# ---- 4 / 7 twist mechanism, ending, logic, guess test (header fields) ----
mech = [x.strip().lower() for x in re.split(r"[,;/]", re.sub(r"\(.*?\)", "", hdr("twist mechanism"))) if x.strip() and x.strip() != "-"]
if mech and B["reveal"]:
    hit = lambda m, t: re.search(r"\b" + re.escape(m) + r"\b", t, re.I)          # whole words only
    early = [r["text"] for r in L if r["start"] < B["reveal"]["start"] and any(hit(m, r["text"]) for m in mech)]
    # a hit that sits only inside a capitalised name ("called her Bad Luck Lulu") is a CHECK, not a FAIL
    cap_name = lambda m, t: re.search(r"\b" + r"\s+".join(re.escape(w.capitalize()) for w in m.split()) + r"\b", t)
    real = [t for t in early if any(hit(m, t) and not cap_name(m, t) for m in mech)]
    row("S4", "no line before the reveal states the mechanism", f"{len(early)} {[t[:40] for t in early[:3]]}", True if not early else (False if real else "CHECK"))
else: row("S4", "no line before the reveal states the mechanism", "add a 'Twist mechanism words' header field", "CHECK")
GEN = ["true", "lie", "lies", "heal", "healed", "close", "closed", "gone", "fixed", "real", "finally", "learned"]
lt = B["last"]["text"].lower()
named = [m for m in GEN + mech if re.search(r"\b" + re.escape(m) + r"\b", lt)]
row("7", "last line names no mechanism / doesn't explain", f"{named} in '{B['last']['text'][:40]}'", not named)
row("S3", "logic questions answered (header 'Logic questions')", (hdr("logic questions")[:60] + "…") if hdr("logic questions") else "missing", True if len(hdr("logic questions")) > 20 else "CHECK")
gt = hdr("guess test").lower()
blind = re.search(r"haiku|fresh|blind|agent|aung|reader", gt)
# a bonus, not a gate (script.md §3.3): not guessed = PASS + bonus, partial = PASS, full match on guess #1 = WARN
if not blind or "unchecked" in gt: res = "UNCHECKED"
elif re.search(r"not guessed|no match|none match", gt): res = True
elif "partial" in gt: res = True
elif re.search(r"guessed", gt) and not re.search(r"#\s*[23]|guess [23]", gt): res = "WARN"
else: res = True
row("S4", "blind guess test (bonus): not / partial / #1 = WARN", hdr("guess test")[:70] or "missing", res)
if a.pretwist and B["reveal"]:
    open(a.pretwist, "w", encoding="utf-8").write("\n".join(r["text"] for r in L if r["start"] < B["reveal"]["start"]) + "\n")
    print(f"wrote {a.pretwist}: {sum(r['start'] < B['reveal']['start'] for r in L)} lines before the reveal, for the blind reader")

# ---- 13b skeleton no-copy (tools/skeletons.txt) ----
SK, SLOTS = [], []
for ln in open(os.path.join(HERE, "skeletons.txt"), encoding="utf-8"):
    if ln.startswith("#") or not ln.strip(): continue
    c = [x.strip() for x in ln.split("|")]
    if c[0] == "name": SLOTS = c[1:]
    else: SK.append((c[0], dict(zip(SLOTS, c[1:]))))
parse_sk = lambda txt: dict((k.strip().lower(), v.strip().lower()) for k, v in (x.split("=", 1) for x in re.split(r"[;,]", txt) if "=" in x))
mine = parse_sk(hdr("skeleton"))
VOC = {}
for ln in open(os.path.join(HERE, "skeletons.txt"), encoding="utf-8"):
    m = re.match(r"#\s*(\w+)\s*:\s*(.+)", ln)
    if m and "|" in m[2] and m[1] != "family": VOC[m[1]] = [x.strip() for x in m[2].split("|")]
same = lambda d: sum(mine.get(k) == str(v).lower() and not mine.get(k, "").startswith("other") for k, v in d.items() if k != "family") \
    + bool(set(re.findall(r"\d+", mine.get("family", ""))) & set(re.findall(r"\d+", str(d.get("family", "")))))
if len(mine) >= 8:
    bad_v = [f"{k}={v}" for k, v in mine.items() if k in VOC and v not in VOC[k] and not v.startswith("other")]
    if bad_v: row("13", "skeleton values from tools/skeletons.txt", f"unknown: {bad_v}", False)
    worst = max(((n, same(d)) for n, d in SK if n != me), key=lambda x: x[1])
    row("13", f"skeleton shares <=4 of {len(SLOTS)} slots with any gold/ref", f"closest {worst[0]}: {worst[1]} same", worst[1] <= 4)
    sig = mine.get("signature", "")
    twins = [n for n, d in SK if n != me and sig not in ("", "none") and d.get("signature") == sig]
    row("13", "signature move is no ref's or gold's", f"signature={sig or 'missing'} {twins}", (not twins) if sig else "CHECK")
else: row("13", "skeleton shares <=4 slots with any gold/ref", "add the 'Skeleton' header field (slot=value; see tools/skeletons.txt)", "CHECK")

# ---- rotation core fields vs the log (templates/rotation-log.md) ----
HINT = {"dad": "parent-child", "mom": "parent-child", "son": "parent-child", "grandpa": "grandparent-partner / grandparent-child",
        "grandma": "grandparent-partner / grandparent-child", "sister": "sibling", "brother": "sibling", "neighbour": "stranger-family",
        "neighbor": "stranger-family", "friend": "friend-narrator", "narrator": "self (only if the twist is about the narrator himself)",
        "love": "romance", "reconnect": "reunion", "estranged": "reunion", "protect": "protection", "shield": "protection",
        "scared": "dread", "free": "freedom", "secret": "exposure / sacrifice-revealed", "died": "loss", "lost": "loss"}
def vocab_ok(field, v):
    if field not in VOC or not v: return True, ""
    if v in VOC[field] or v.startswith("other"): return True, ""
    hint = [h for k, h in HINT.items() if k in v]
    return False, f"'{v}' is not a {field} word: map it to {hint[0] if hint else ' / '.join(VOC[field])}"
fams = lambda t: set(re.findall(r"\b(1[01]|[1-9])\b", t or ""))        # "3 + 10" -> {3, 10}
if a.log:
    rows_, cols = [], None
    for ln in open(a.log, encoding="utf-8"):
        c = [x.strip().lower() for x in ln.strip().strip("|").split("|")] if ln.startswith("|") else []
        if not c or set("".join(c)) <= set("-: "): continue
        if c[0] == "ep": cols = c; continue
        if cols: rows_.append(dict(zip(cols, c)))
    col = lambda r, key: r.get(key, next((v for k, v in r.items() if k.startswith(key)), ""))
    cur = dict(family=fams(mine.get("family", "") or hdr("twist family")[:12]), subject=mine.get("subject", ""),
               outcome=mine.get("outcome", ""), reveal=mine.get("reveal", ""))
    norm_ep = lambda e: re.sub(r"^\D*0*", "", e or "")
    own = norm_ep((a.ep or hdr("episode")).strip().lower())
    def is_own(r):
        return (own and norm_ep(col(r, "ep")) == own) or (r is rows_[-1] and fams(col(r, "family")) == cur["family"]
                and col(r, "subject") == cur["subject"] and col(r, "outcome") == cur["outcome"])
    skipped = [col(r, "ep") for r in rows_ if is_own(r)]
    rows_ = [r for r in rows_ if not is_own(r)]
    if skipped: out.append(f"INFO      rot  skipped the plan's own log row: ep {skipped}")
    for r in rows_:
        for f in ("subject", "outcome"):
            ok, msg = vocab_ok(f, col(r, f))
            if not ok: row("rot", f"log ep {col(r, 'ep')}: controlled {f} word", msg, False)
    for f in ("subject", "outcome", "reveal"):
        ok, msg = vocab_ok(f, cur[f])
        if not ok: row("rot", f"this plan: controlled {f} word", msg, False)
    last5, last3, last = rows_[-5:], rows_[-3:], (rows_[-1] if rows_ else {})
    win = set().union(*[fams(col(r, "family")) for r in last5]) if last5 else set()
    row("rot", "families (primary + secondary) not in the last 5", f"{sorted(cur['family'])} vs {sorted(win)}", bool(cur["family"]) and not (cur["family"] & win))
    row("rot", "subject pair not in the last 3", f"{cur['subject']} vs {[col(r, 'subject') for r in last3]}", bool(cur["subject"]) and cur["subject"] not in [col(r, "subject") for r in last3])
    row("rot", "emotional outcome not in the last 3", f"{cur['outcome']} vs {[col(r, 'outcome') for r in last3]}", bool(cur["outcome"]) and cur["outcome"] not in [col(r, "outcome") for r in last3])
    lrv = col(last, "reveal move") if last else ""
    if cur["reveal"] and lrv: row("rot", "reveal move differs from the last episode", f"{cur['reveal']} vs {lrv}", cur["reveal"] != lrv)
    for r in last5:   # the channel against itself: skeletons logged for earlier episodes
        d = parse_sk(col(r, "skeleton"))
        if len(d) >= 8 and len(mine) >= 8:
            n = same(d); row("rot", f"skeleton vs ep {col(r, 'ep')} <=4 shared", f"{n} same", n <= 4)
    lr = re.search(r"\d+\.?\d*", col(last, "reveal %")) if last else None
    if lr and B["twist"]: row("rot", "reveal % (twist line) >=10 points from the last", f"{pct(B['twist']['start']):.1f} vs {lr[0]}", abs(pct(B["twist"]["start"]) - float(lr[0])) >= 10)
    ev = re.search(r"\b([abc])\b", hdr("music event 1").lower() or "")
    evs = [col(r, "event type")[:1] for r in rows_]
    if ev: row("rot", "event-1 type differs from last; A has 2 episodes between", f"{ev[1].upper()} vs {[e.upper() for e in evs[-2:]]}", ev[1] != (evs[-1] if evs else "") and not (ev[1] == "a" and "a" in evs[-2:]))
    else: row("rot", "event-1 type differs from last", "add the 'Music event 1 type' header field (A / B / C)", "CHECK")

# ---- 10 dialogue ----
dlg_words, cur, run, mx, longest = 0, None, 0, 0, 0
for r in L:
    if r["speaker"] in ("SIGN", "TEXT"): cur, run = None, 0; continue   # read-out rule-object text is not dialogue
    if r["speaker"] != "NARR":
        dlg_words += r["words"]; longest = max(longest, r["words"])
        k = len(sentences(r["text"])); run = run + k if r["speaker"] == cur else k; cur = r["speaker"]; mx = max(mx, run)
    else:
        cur, run = None, 0
        for q in re.findall(r"[\"“]([^\"”]+)[\"”]", r["text"]):
            n = sum(len(spoken(x)) for x in q.split()); dlg_words += n; longest = max(longest, n)
row("10", "dialogue 3-20 % of words (incl. narrated quotes)", f"{100 * dlg_words / W:.1f} %", 3 <= 100 * dlg_words / W <= 20)
row("10", "dialogue line <=10 words; run <=3 sentences", f"longest {longest}, run {mx}", longest <= 10 and mx <= 3)
spk = sorted({r["speaker"] for r in L} - {"NARR", "SIGN", "TEXT"})
row("10", "other speakers 2-4 (voices <=3 besides NARR)", f"{len(spk)}: {', '.join(spk)}", True if 2 <= len(spk) <= 4 else "CHECK")

# ---- 11 banned list (read from script.md §9.1) + structures ----
txt = open(a.rules, encoding="utf-8").read()
sec = txt[txt.find("### 9.1"):txt.find("### 9.2")]
phr = []
for q in re.findall(r"\"([^\"]+)\"", sec):
    q = re.sub(r"\[[^\]]*\]|\.\.\.|…", "", q).strip()
    if " / " in q:
        parts = [x.strip() for x in q.split(" / ")]; pre = parts[0].rsplit(" ", 1)[0]
        phr += [parts[0]] + [f"{pre} {x}" for x in parts[1:]]
    elif q: phr.append(q)
m = re.search(r"abstract long adjectives:(.*)", sec)
if m: phr += [x.strip() for x in m[1].split(",") if x.strip()]
full = " ".join(r["text"] for r in L)
hits = []
for p in phr:
    if p.endswith(","):   # an opener like "See," only counts at a sentence start
        hits += [p for _, s, _ in S if s.lower().startswith(p.lower())]
    elif re.search(r"(?<!\w)" + re.escape(p.rstrip(",.")) + r"(?!\w)", full, re.I): hits.append(p)
hits += [lab for rx, lab, _ in PAT.get("banned-regex", []) if any(rx.search(x) for _, x, _ in S)]
row("11", f"banned phrases (§9.1, {len(phr)} + {len(PAT.get('banned-regex', []))} regex)", f"{len(hits)} hits {hits}", not hits)
stag = [S[i][1] + " " + S[i + 1][1] for i in range(N - 1)
        if (m := re.match(r"^[\"“]?(\w+) (wasn't|isn't|weren't|aren't)\b", S[i][1], re.I)) and re.match(rf"^[\"“]?{m[1]} (was|is|were|are)\b", S[i + 1][1], re.I)]
row("11", "'It wasn't X. It was Y.' max 1", f"{len(stag)} {stag[:2]}", len(stag) <= 1)
if stag:
    planted = hdr("staged contrast")
    row("11", "staged contrast: X planted (header, quote + time)", planted[:60] or "missing", True if re.search(r"\d+\.?\d*\s*s", planted) else False)
qv = [s for sp, s, _ in S if sp == "NARR" and s.endswith("?") and not s.startswith(("\"", "“"))]
row("11", "narrator questions max 1", f"{len(qv)} {qv[:3]}", len(qv) <= 1)
dash = sum(full.count(c) for c in ("—", " – ", ";", "...", "…"))
row("11", "no em dashes / semicolons / ellipses", f"{dash}", dash == 0)
adv = re.findall(r"\b(?:said|says|asked|whispered|shouted|yelled)\s+\w+ly\b|\b\w+ly\s+(?:said|asked|whispered)\b", full, re.I)
row("11", "no adverb + said", f"{adv}", not adv)

# ---- 12 timing + pauses (the one pause rule: script.md §6) ----
speech = sum(r["end"] - r["start"] for r in L)
lo = 160 if RT <= 80 else 200
row("12", f"wpm (speech only, slow reads in) {lo}-240", f"{W / speech * 60:.0f} ({W} words / {speech:.1f} s)", lo <= W / speech * 60 <= 240)
tw = B["twist"] or B["reveal"]
pa = [p for p in P if tw and 0 <= p["start"] - tw["start"] <= 3 + (tw["end"] - tw["start"]) and 0.8 <= p["secs"] <= 1.3]
li = R.index(B["last"]); pb = R[li - 1] if li and R[li - 1]["kind"] == "pause" else None
row("12", "2-3 designed pauses, each 0.6-1.3 s", ", ".join(f"{p['secs']:.1f}" for p in P) or "none", 2 <= len(P) <= 3 and all(.6 <= p["secs"] <= 1.3 for p in P))
row("12", "pause A 0.8-1.3 s right after the twist line", f"{pa[0]['secs']:.1f} s at {pa[0]['start']:.1f}" if pa else "missing", bool(pa))
row("12", "pause B 0.6-1.0 s right before the last line", f"{pb['secs']:.1f} s" if pb else "missing", bool(pb) and .6 <= pb["secs"] <= 1.0)
tgt = a.target
if tgt is None and re.search(r"(\d{2,3}(?:\.\d)?)\s*s", hdr("target runtime")):
    tgt = float(re.search(r"(\d{2,3}(?:\.\d)?)\s*s", hdr("target runtime"))[1])
if tgt is None:
    m = re.search(r"target[^|\n]*?(\d{2,3}(?:\.\d)?)\s*s", open(a.sheet, encoding="utf-8").read(), re.I)
    tgt = float(m[1]) if m else None
row("12", "runtime = target +-5 % (60-180 s)", f"{RT:.1f} s vs target {tgt}" if tgt else f"{RT:.1f} s (no target found: pass --target)",
    (abs(RT - tgt) / tgt <= .05 and 60 <= tgt <= 180) if tgt else "CHECK")

# ---- caption highlights (captions.md §1.1) ----
post = [r for r in L[1:]]
hw = sum(len(re.sub(r"\(manual\)", "", r["hl"]).split()) for r in post if r["hl"].strip() not in ("", "-") and "whole" not in r["hl"].lower())
ntok = sum(len(r["tokens"]) for r in post)
words_hl = [re.sub(r"\(manual\)", "", r["hl"]).strip() for r in post if r["hl"].strip() not in ("", "-") and "whole" not in r["hl"].lower()]
row("cap", "accent words after the hook <=13 %", f"{hw}/{ntok} = {100 * hw / max(ntok, 1):.1f} %" if hw else "no caption column", (100 * hw / ntok <= 13) if hw else "CHECK")
row("cap", "accents only names / rule words / 1-2 peaks", ", ".join(words_hl[:30]), "CHECK")

# ---- drift between the sheet's time column and the model ----
drift = []
for r in L:
    m = re.match(r"\s*(\d+\.?\d*)", r["sheet_time"] or "")
    if m and abs(float(m[1]) - r["start"]) > 0.3: drift.append(f"'{r['text'][:24]}' {m[1]} vs {r['start']:.1f}")
row("time", "sheet time column vs model (<=0.3 s)", f"{len(drift)} rows off {drift[:3]}", True if not drift else "CHECK")

chars = {}
for r in L: chars[r["speaker"]] = chars.get(r["speaker"], 0) + len(r["text"])
print(f"{a.sheet}: {len(L)} lines, {W} spoken words, {len(P)} pauses, speech ends {D['speech_end']:.1f} s, runtime {RT:.1f} s (tail {a.tail})")
print("\n".join(out))
print("ElevenLabs text characters (credit ask = characters x takes): " + ", ".join(f"{k} {v}" for k, v in chars.items()))
print("By hand: rubric #1, twist family vs log #4, clues #6 (2-4, <=2 direct), motif #7, tense, the user's read #12, the CHECK lines.")

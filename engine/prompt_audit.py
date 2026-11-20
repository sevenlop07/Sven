#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prompt_audit.py — audit one Stage 4 scene prompt (Code Block 1, workflow.md §9.3).

    python engine/prompt_audit.py output/<slug>/prompts/ep-NN-scene-KK.md
    python engine/prompt_audit.py --docs          # lint every Code Block 1 example inside the core docs

The file may contain the bare prompt or a Markdown file with the prompt inside the first ```text block.
Checks (numbers from engine/references/0c-canonical-numbers.md):
  structure   block order Style → [context] → [subject] → [prop] → [sound] → Shot 1..N → 3-line footer
  references  every <<<Image N>>> declared once, never inside Shot lines; [context] lock = fixed furniture and lighting
  separation  character-handled items (cup, glass, knife, phone, letter…) never listed in [context] (§2.6)
  shots       header "Shot K (MM:SS-MM:SS) - scale, angle/move targeting Name, speed tag"; contiguous from 00:00;
              ends at 00:10 / 00:15 / 00:30; prose 12–30 words; no → arrows, no meta-instructions
  dialogue    window ≥ 0.4 + words/2.5 + 0.5 s and 3.2–4.5 s per spoken shot (D4); clip word budget; interjections
              on ≤ 1 in 3 lines, never twice in a row (D2); vocal tags without alto/baritone/tenor/soprano (D3)
  ending      Law D5: wordless final shot (Mode 1) or short final line with ~0.8 s closed-lip tail (Mode 2)
  identity    zero clothing / age / hair-colour words in [subject] action text and shots (Gates 3A/3E)
  footer      Master-level line, Strict visual consistency line (hand clause), Do-not line with duplicate props,
              female-hand clause when a woman is on screen, no-text clause
Exit 1 when any ERROR is found.
"""
import glob
import math
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

RATE = 2.5
LEAD, BUFFER, TAIL = 0.4, 0.5, 0.8
SPOKEN_MIN, SPOKEN_MAX = 3.0, 4.5
WORDS_10S, WORDS_15S, WORDS_15S_ACTION = 22, 32, 16
PROSE_MIN, PROSE_MAX = 12, 30
SPEED_TAGS = ["natural real-time speed", "snappy real-time speed", "crisp real-time speed", "explosive real-time speed",
              "blistering whip-fast speed", "ultra-slow-motion suspension"]
ACTION_TAGS = SPEED_TAGS[3:]
INTERJECTIONS = ["huh", "whoa", "hah", "oh", "uh", "ah", "hmm", "wait", "what", "hey", "wow", "ugh", "hửm", "á", "ối",
                 "hơ", "ủa", "hả", "trời", "ơ", "ồ", "ê", "chà", "hừ", "ôi"]
HANDHELD = ["cup", "teacup", "mug", "glass", "glasses", "wine glass", "bottle", "knife", "cleaver", "ladle", "spoon", "fork",
            "chopsticks", "whisk", "mixer", "rolling pin", "spatula", "pan", "phone", "smartphone", "letter", "envelope",
            "contract", "ledger", "receipt", "pen", "keyring", "keys", "key", "wallet", "sword", "dagger", "gun", "pistol",
            "umbrella", "watch", "ring", "photo", "photograph", "folder", "file", "document", "bowl", "plate", "dough"]
CLOTHING = ["jacket", "suit", "dress", "skirt", "coat", "shirt", "blouse", "t-shirt", "hoodie", "jeans",
            "trousers", "sweater", "cardigan", "gown", "necktie", "scarf", "apron", "hat", "heels"]
AGE_RX = re.compile(r"\b\d{1,2}[- ]year[- ]old\b|\byears old\b|\b(young|elderly|teenage|middle-aged)\b", re.I)
HAIR_RX = re.compile(r"\b(blonde?|brunette|redhead|silver-haired|grey-haired|gray-haired|black-haired|silver-bearded)\b", re.I)
META_RX = re.compile(r"speaking immediately|finishes (?:his|her|their) sentence|holds still|from the opening second", re.I)
REGISTER_RX = re.compile(r"\b(alto|baritone|tenor|soprano)\b", re.I)
# Motion Density Law (workflow.md §2.5, 0c §1): primary actions vs. duration
PRIMARY_VERBS = ["sets", "places", "puts", "lays", "lifts", "raises", "lowers", "picks", "grabs", "snatches", "seizes",
                 "takes", "hands", "passes", "gives", "throws", "tosses", "drops", "slams", "stands", "rises", "sits",
                 "kneels", "walks", "steps", "strides", "runs", "sprints", "dashes", "jumps", "leaps", "vaults", "climbs",
                 "turns", "spins", "pivots", "whirls", "reaches", "opens", "closes", "shuts", "unlocks", "pushes", "pulls",
                 "drags", "swings", "slashes", "strikes", "punches", "kicks", "blocks", "parries", "lunges", "dodges",
                 "pours", "cuts", "slices", "chops", "stirs", "flips", "tilts", "taps", "knocks", "hugs", "embraces",
                 "kisses", "slaps", "tears", "rips", "folds", "writes", "signs", "dials", "types", "wipes", "bites",
                 "sips", "drinks", "eats", "crosses", "enters", "exits", "leaves", "approaches", "retreats", "backs",
                 "points", "shoves", "catches", "skids", "brakes", "drifts", "slides", "crouches", "bends"]
MICRO_RX = re.compile(r"\b(breath\w*|breath(?:es|ing)|exhal\w*|inhal\w*|blink\w*|gaze|glanc\w*|eyes?|brows?|jaw|lips?|"
                      r"finger\w*|tremb\w*|trembl\w*|flicker\w*|drift\w*|rain|smoke|steam\w*|mist|wind|sway\w*|ripple\w*|"
                      r"lingering|slowly|a beat|settl\w*|fog\w*|dust|sparks?|embers?|foam\w*|fizz\w*|condensation)\b", re.I)
PRIMARY_RX = re.compile(r"\b(" + "|".join(PRIMARY_VERBS) + r")\b", re.I)
FAST_TAGS = ["snappy real-time speed", "crisp real-time speed", "explosive real-time speed",
             "blistering whip-fast speed"]


def density_limit(dur, hdr):
    """Allowed primary actions for one shot (0c §1 Motion density)."""
    h = hdr.lower()
    if any(t in h for t in FAST_TAGS):
        if dur <= 2.5:
            return 1
        return max(2, math.ceil(dur / 4.0) * 3)      # inertial long take: <= 3 linked moves per ~4s
    return max(1, int((dur + 0.5) // 3.5))         # dialogue / drama: one primary action per 3–4s


SHOT_RX = re.compile(r"^Shot\s+(\d+)\s*\((\d{1,2}):(\d{2}(?:\.\d+)?)\s*-\s*(\d{1,2}):(\d{2}(?:\.\d+)?)\)\s*-\s*(.+)$")
DIALOGUE_RX = re.compile(r'^\s*([A-ZÀ-Ỹ][\wÀ-ỹ\'\- ]{0,40}?)\s*\(([^)]*)\)\s*:\s*["“](.+?)["”]\s*$')
TURN_RX = re.compile(r"^\s*\((\d{1,2}):(\d{2}(?:\.\d+)?)\s*-\s*(\d{1,2}):(\d{2}(?:\.\d+)?)\)")


VN_RX = re.compile(r"[ăâđêôơưàáạảãầấậẩẫằắặẳẵèéẹẻẽềếệểễìíịỉĩòóọỏõồốộổỗờớợởỡùúụủũừứựửữỳýỵỷỹ]", re.I)


def rate_for(lines):
    """~2.5 EN words/s or ~3.0 VN syllables/s (0c §2)."""
    return 3.0 if any(VN_RX.search(l[2]) for l in lines) else RATE


def secs(m, s):
    return int(m) * 60 + float(s)


def extract_prompt(text):
    m = re.search(r"```(?:text)?\n(.*?)```", text, re.S)
    return m.group(1) if m and "Shot 1" in m.group(1) else text


def words(s):
    return len([w for w in re.split(r"\s+", s.strip()) if re.search(r"\w", w)])


def block(lines, start_rx, stop_rx):
    out, on = [], False
    for ln in lines:
        if re.match(start_rx, ln):
            on = True
            out.append(ln)
            continue
        if on and re.match(stop_rx, ln):
            break
        if on:
            out.append(ln)
    return "\n".join(out)


def audit_prompt(p):
    E, W = [], []
    lines = [l.rstrip() for l in p.strip("\n").split("\n")]
    text = "\n".join(lines)

    # ---------- structure ----------
    order = []
    for i, l in enumerate(lines):
        for tag, rx in (("style", r"^Style\s*:"), ("context", r"^\[context\]\s*:"), ("subject", r"^\[subject\]\s*:"),
                        ("prop", r"^\[prop\]\s*:"), ("sound", r"^\[sound\]\s*:"), ("shot", r"^Shot\s+1\b"),
                        ("master", r"^Master-level\b"), ("strict", r"^Strict visual consistency"),
                        ("donot", r"^Do not generate")):
            if re.match(rx, l, re.I) and tag not in [o[0] for o in order]:
                order.append((tag, i))
    tags = [t for t, _ in order]
    for need in ("style", "context", "subject", "sound", "shot", "master", "strict", "donot"):
        if need not in tags and not (need in ("context", "subject") and re.search(r"^\[(storyboard|video reference)\]", text, re.M | re.I)):
            E.append(f"missing block: {need}")
    canon = ["style", "context", "subject", "prop", "sound", "shot", "master", "strict", "donot"]
    seq = [t for t in canon if t in tags]
    if [t for t in tags if t in seq] != seq:
        E.append(f"blocks out of order: {tags} (expected {seq})")
    if re.search(r"^(INT\.|EXT\.)", text, re.M):
        W.append("top slugline found — the Unified Storyboard Format has no slugline")

    ctx = block(lines, r"^\[context\]", r"^\[(subject|prop|sound)\]|^Shot\s+\d")
    subj = block(lines, r"^\[subject\]", r"^\[(prop|sound)\]|^Shot\s+\d")
    prop = block(lines, r"^\[prop\]", r"^\[sound\]|^Shot\s+\d")
    shots_txt = block(lines, r"^Shot\s+1\b", r"^Master-level\b|^Strict visual consistency|^Do not generate")

    # ---------- references ----------
    # a storyboard grid / source video may be referenced panel by panel (STORYBOARD / REF_VIDEO formats)
    hdr = re.search(r"^\[(?:storyboard|video reference)\][^\n]*\n?[^\n]*?<<<Image\s+(\d+)>>>", text, re.M | re.I)
    board = {hdr.group(1)} if hdr else set()
    head_txt = text.split("\nShot 1", 1)[0]          # declarations live in the header blocks; the footer may cite images
    imgs = [n for n in re.findall(r"<<<Image\s+(\d+)>>>", head_txt) if n not in board]
    for n in sorted(set(imgs)):
        if imgs.count(n) > 1:
            E.append(f"<<<Image {n}>>> declared {imgs.count(n)} times — declare once at its header")
    if [n for n in re.findall(r"<<<Image\s+(\d+)>>>", shots_txt) if n not in board]:
        E.append("<<<Image N>>> appears inside Shot lines — refer by Proper Name only")
    if re.search(r"<<<[^>]*\s[^>]*\w[^>]*>>>", text) and re.search(r"<<<(?!Image\s+\d+>>>|Video\s+\d+>>>)", text):
        E.append("descriptive words inside <<<…>>> brackets")
    lock = re.search(r"<<<Image\s+\d+>>>\s*\(fully_preserved\s*-\s*([^)]*)\)", ctx)
    if ctx and not lock:
        E.append("[context] lacks the '(fully_preserved - …)' lock after <<<Image 1>>>")
    elif lock and re.search(r"\bprops?\b", lock.group(1), re.I):
        E.append("[context] lock mentions props — use 'same architectural layout, fixed furniture and lighting throughout'")

    # ---------- separation law ----------
    ctx_body = ctx.lower()
    used = (subj + "\n" + prop + "\n" + shots_txt).lower()
    material = r"(?!\s+(?:coffee|table|tables|door|doors|wall|walls|window|windows|panel|panels|roof|ceiling|partition|counter|shelf|shelves|case|cabinet|top|tabletop|railing|facade|dome|box))"
    dup = sorted({h for h in HANDHELD if re.search(r"\b" + re.escape(h) + r"s?\b" + material, ctx_body)
                  and re.search(r"\b" + re.escape(h) + r"s?\b" + material, used)})
    if dup:
        E.append(f"character-handled item(s) {dup} listed in [context] and used by a character — move them to [subject]/[prop] (duplicate-prop bug, §2.6)")

    # ---------- subject identity ----------
    subj_action = re.sub(r"\(fully_preserved[^)]*\)", "", subj)
    subj_action = "\n".join(l for l in subj_action.split("\n") if not re.search(r"'s skin", l))
    scan = subj_action + "\n" + shots_txt
    clothes = sorted({c for c in CLOTHING if re.search(r"\b" + re.escape(c) + r"\b", scan, re.I)})
    if clothes:
        E.append(f"clothing words {clothes} in [subject]/shots — outfit is locked by the reference image (Gate 3A)")
    if AGE_RX.search(scan):
        E.append("age words in [subject]/shots (Gate 3E)")
    if HAIR_RX.search(scan):
        E.append("hair-colour words in [subject]/shots (Gate 3E)")
    for name in re.findall(r"^([A-ZÀ-Ỹ][\wÀ-ỹ\-]+)\s*<<<Image", subj, re.M):
        if f"the only {name} in frame" not in subj:
            W.append(f"[subject] {name}: missing singularity seal '— the only {name} in frame'")
        if not re.search(re.escape(name) + r"'s skin", subj):
            E.append(f"[subject] {name}: missing the skin/hands sub-lock line")
    female = bool(re.search(r"same female face|skin, hands and makeup", subj))
    male = bool(re.search(r"same male face", subj))

    # ---------- shots ----------
    shots, cur = [], None
    for l in shots_txt.split("\n"):
        m = SHOT_RX.match(l.strip())
        if m:
            cur = {"n": int(m.group(1)), "a": secs(m.group(2), m.group(3)), "b": secs(m.group(4), m.group(5)),
                   "hdr": m.group(6), "prose": [], "lines": [], "turns": 0}
            shots.append(cur)
            continue
        if cur is None or not l.strip():
            continue
        d = DIALOGUE_RX.match(l)
        if d:
            cur["lines"].append((d.group(1).strip(), d.group(2), d.group(3)))
        else:
            if TURN_RX.match(l):
                cur["turns"] += 1
            cur["prose"].append(l.strip())
    if not shots:
        E.append("no 'Shot K (MM:SS-MM:SS) - …' headers parsed")
        return E, W
    t = 0.0
    for k, s in enumerate(shots, 1):
        if s["n"] != k:
            E.append(f"Shot numbering: found Shot {s['n']} at position {k}")
        if abs(s["a"] - t) > 0.05:
            E.append(f"Shot {s['n']} starts at {s['a']:.1f}s, expected {t:.1f}s (timeline must be contiguous from 00:00)")
        t = s["b"]
        hdr = s["hdr"]
        if not re.search(r"targeting|locked on|focus(?:ed)? on|tracking", hdr, re.I):
            E.append(f"Shot {s['n']} header names no target ('targeting [Name]' / 'locked on [product]' — Law 3 Target-First)")
        if not any(tag in hdr.lower() for tag in SPEED_TAGS):
            E.append(f"Shot {s['n']} header lacks a [Shot Speed] tag (0b §4.2)")
        if hdr.count(",") < 2:
            W.append(f"Shot {s['n']} header should have 3 parts: scale, angle/move targeting Name, speed")
        prose = " ".join(s["prose"])
        if "→" in prose or "→" in hdr:
            E.append(f"Shot {s['n']}: '→' arrows are banned in prompts")
        if META_RX.search(prose):
            E.append(f"Shot {s['n']}: meta-instruction in prose")
        # ---- Motion Density Law: action overload / time underload ----
        dur = s["b"] - s["a"]
        acts = PRIMARY_RX.findall(prose)
        limit = density_limit(dur, hdr)
        if s["turns"] == 0 and len(acts) > limit:
            W.append(f"Shot {s['n']}: {len(acts)} primary actions {sorted(set(a.lower() for a in acts))} in {dur:.1f}s "
                     f"(allowed {limit}) — action overload; keep one primary action per beat (Motion Density Law)")
        if s["turns"] == 0 and not s["lines"] and dur >= 4.5 and len(acts) <= 1 and not MICRO_RX.search(prose) \
                and "ultra-slow-motion" not in hdr.lower():
            W.append(f"Shot {s['n']}: {dur:.1f}s wordless shot with {len(acts)} primary action and no micro-motion — "
                     f"time underload; stretch the action (prep ➔ execution ➔ after-beat) and add breath / gaze / environment motion")
        if s["turns"] == 0:
            wc = words(prose)
            cap = PROSE_MAX * max(1.0, (s["b"] - s["a"]) / 4.0)   # long takes carry proportionally more beats
            if wc > cap + 10:
                E.append(f"Shot {s['n']}: {wc} words of prose (> {int(cap)}) — one action, 1–2 sentences per ~4s (Gate 3R)")
            elif wc > cap or wc < PROSE_MIN:
                W.append(f"Shot {s['n']}: {wc} words of prose (target {PROSE_MIN}–{int(cap)})")
    end = shots[-1]["b"]
    if round(end, 1) not in (10.0, 15.0, 30.0):
        E.append(f"clip ends at {end:.1f}s — allowed durations are 10.0 / 15.0 / 30.0 s")

    # ---------- dialogue ----------
    all_lines = [(s, ln) for s in shots for ln in s["lines"]]
    total = sum(words(l[2]) for _, l in all_lines)
    action = any(tag in s["hdr"].lower() for s in shots for tag in ACTION_TAGS)
    cap = WORDS_10S if end <= 10.05 else (WORDS_15S_ACTION if action else WORDS_15S)
    if total > cap:
        E.append(f"{total} spoken words > {cap} budget for this clip (0c §2)")
    for s in shots:
        if not s["lines"] or s["turns"]:
            continue
        w = sum(words(l[2]) for l in s["lines"])
        dur = s["b"] - s["a"]
        need = LEAD + w / rate_for(s["lines"]) + BUFFER
        vn = rate_for(s["lines"]) == 3.0
        mode2_ok = dur >= 3.2 - 1e-6 and w <= (10 if vn else 8)
        if dur + 1e-6 < need:
            msg = f"Shot {s['n']}: {w} spoken {'syllables' if vn else 'words'} need ≥ {need:.1f}s by the D4 formula, shot is {dur:.1f}s"
            if mode2_ok:
                pass  # canonical Mode 2 exception (0c §2): ≤ 8 EN words / ≤ 10 VN syllables in ≥ 3.2s
            else:
                E.append(msg + " (Law D4)")
        if dur < SPOKEN_MIN:
            E.append(f"Shot {s['n']}: spoken shot of {dur:.1f}s < {SPOKEN_MIN}s (Law D4)")
        elif dur > SPOKEN_MAX + 0.05 and len(shots) > 1:
            W.append(f"Shot {s['n']}: spoken shot of {dur:.1f}s > {SPOKEN_MAX}s window")
        if len(s["lines"]) > 1 and len({l[0] for l in s["lines"]}) > 1:
            W.append(f"Shot {s['n']}: two speakers in one cut — one speaker per spoken shot window")
    inter_rx = re.compile(r"^\s*(" + "|".join(sorted(map(re.escape, INTERJECTIONS), key=len, reverse=True)) + r")\b[\s?!.…,]", re.I)
    hits = [inter_rx.match(l[2]) for _, l in all_lines]
    n_hit = sum(1 for h in hits if h)
    if all_lines and n_hit > math.ceil(len(all_lines) / 3):
        E.append(f"{n_hit}/{len(all_lines)} lines open with an interjection — ration ≤ 1 in 3 (Law D2)")
    seq = [h.group(1).lower() for h in hits if h]
    if any(a == b for a, b in zip(seq, seq[1:])):
        E.append("same interjection twice in a row (Law D2)")
    for (_, l), h in zip(all_lines, hits):
        if h and re.search(r"calm|icy|authority|cold", l[1], re.I):
            W.append(f"{l[0]}: interjection on a calm/authority line — drop it (Law D2)")
        if REGISTER_RX.search(l[1]):
            E.append(f"{l[0]}: musical register word in the vocal tag (Law D3)")
        if not re.search(r"expressive (female|male) voice", l[1], re.I):
            W.append(f"{l[0]}: vocal tag should start 'expressive female/male voice, [behaviour] in a [tone]' (Law D3)")

    # ---------- ending (Law D5) ----------
    last = shots[-1]
    if last["lines"] and not last["turns"]:
        w = sum(words(l[2]) for l in last["lines"])
        dur = last["b"] - last["a"]
        vn = rate_for(last["lines"]) == 3.0
        if w > (10 if vn else 8):
            E.append(f"final shot speaks {w} {'syllables' if vn else 'words'} — Mode 2 final line must be 6–8 EN words / ≤ 10 VN syllables (Law D5)")
        elif dur + 1e-6 < LEAD + w / rate_for(last["lines"]) + TAIL:
            if dur >= 3.4 - 1e-6:
                pass  # canonical Mode 2 / CTA-A exception (0c §2): final 6–8 word turn in ≥ 3.4s
            else:
                E.append(f"final shot {dur:.1f}s leaves no ~0.8s closed-lip tail for {w} words (Law D5 Mode 2)")
    elif not last["lines"]:
        dur = last["b"] - last["a"]
        if not (1.8 <= dur <= 3.6) and len(shots) > 1 and not action:
            W.append(f"wordless final shot is {dur:.1f}s — Mode 1 payoff is usually 2.0–3.0s")

    # ---------- footer ----------
    strict = re.search(r"^Strict visual consistency.*$", text, re.M)
    donot = re.search(r"^Do not generate.*$", text, re.M)
    if strict and female and "feminine" not in strict.group(0):
        E.append("Strict visual consistency line lacks the feminine hand clause (female on screen)")
    if strict and male and not female and "makeup" in strict.group(0):
        W.append("Strict visual consistency line mentions makeup with male characters only")
    if donot:
        dn = donot.group(0).lower()
        if "duplicate" not in dn:
            E.append("Do not generate line lacks 'duplicate props or utensils' (§2.6 footer)")
        if female and "rough masculine hands" not in dn:
            E.append("Do not generate line lacks 'rough masculine hands on female characters' (female on screen)")
        if not re.search(r"subtitles|written text", dn):
            E.append("Do not generate line lacks the no-text clause")
    return E, W


def audit_file(path):
    raw = open(path, encoding="utf-8").read()
    return audit_prompt(extract_prompt(raw))


def doc_examples():
    files = [os.path.join(ROOT, f) for f in ("workflow.md", ".agents/DIRECTOR.md", ".agents/STORYBOARD_DIRECTOR.md",
                                              ".agents/COMMERCIAL_DIRECTOR.md", ".agents/skills/combat-director/SKILL.md",
                                              "engine/references/0b-temporal-camera-grammar.md",
                                              "engine/references/4-ai-video-prompt-compiler.md")]
    for f in files:
        if not os.path.exists(f):
            continue
        L = open(f, encoding="utf-8").read().split("\n")
        i = 0
        while i < len(L):
            if L[i].lstrip().startswith("```"):
                j = i + 1
                while j < len(L) and not L[j].lstrip().startswith("```"):
                    j += 1
                body = "\n".join(L[i + 1:j])
                if re.search(r"^Shot 1 \(00:00", body, re.M) and ("[subject]" in body or "[storyboard]" in body) \
                        and "[Proper_Name" not in body and "[Name]" not in body and "[Evocative" not in body:
                    yield os.path.relpath(f, ROOT), i + 1, body
                i = j + 1
            else:
                i += 1


def main():
    if "--docs" in sys.argv:
        bad = 0
        for f, line, body in doc_examples():
            E, W = audit_prompt(body)
            status = "OK " if not E else "ERR"
            bad += bool(E)
            print(f"{status} {f}:{line}  ({len(E)} error(s), {len(W)} warning(s))")
            for e in E:
                print(f"      ERROR {e}")
        return 1 if bad else 0
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path = sys.argv[1]
    E, W = audit_file(path)
    print(f"[prompt_audit] {path}")
    for e in E:
        print(f"  ERROR {e}")
    for w in W:
        print(f"  WARN  {w}")
    print(f"[prompt_audit] {len(E)} error(s), {len(W)} warning(s)")
    return 1 if E else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
screenplay_audit.py — audit a saved Stage 3 episode script (workflow.md §8.3–§8.4).

Stage 3 runs in chat; once Pass B is written the agent saves the full script (Pass A + Pass B, as shown in chat)
to output/<slug>/ep-NN-script.md and runs:

    python engine/screenplay_audit.py output/<slug>/ep-NN-script.md

It replaces, for chat-based Stage 3, the depth audits that episode_audit_suite.py ran on the retired tap-X.html files
(W9 feeling labels / title spoken, W10 prediction ledger & plant order, W11 single-location stagnation) and adds
engagement checks (Retention Map, value shifts, open loops at every cut, rhythm, word budgets, interjection rationing,
repetition against the previous episode, Engagement Scorecard pass mark).

Exit code 1 when any ERROR is found; WARN lines must be fixed or justified with a `BREAK: <rule> — <reason>` line.
Numbers come from engine/references/0c-canonical-numbers.md; project overrides from output/<slug>/project_rules.json
("emotion_label_terms", "title_phrases", "interjections").
"""
import json
import math
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# --- canonical numbers (0c-canonical-numbers.md §2, §5) ---
WORDS_10S = 22
WORDS_15S_DIALOGUE = 32
WORDS_15S_ACTION = 16
SCORE_PASS = 12
SCORE_MAX = 16
MAX_SAME_TYPE_RUN = 2          # never 3 consecutive scenes with the same structure
PATTERN_SHIFT_EVERY = 3        # shift at least every 2–3 scenes

DEFAULT_EMOTION_TERMS = [
    'ghét', 'thương', 'buồn', 'sợ', 'giận', 'tủi thân', 'hạnh phúc', 'cô đơn', 'đau lòng',
    'hối hận', 'tha thứ', 'nhớ thương',
    'love you', 'hate', 'afraid', 'scared', 'angry', 'sad', 'happy', 'lonely', 'grateful', 'forgive', 'i feel',
]
DEFAULT_INTERJECTIONS = [
    'hửm', 'á', 'ối', 'ối trời', 'hơ', 'ủa', 'hả', 'trời', 'ơ', 'ồ', 'ê', 'chà', 'hừ', 'ái chà', 'ôi',
    'huh', 'whoa', 'hah', 'oh', 'uh', 'ah', 'hmm', 'wait', 'what', 'hey', 'wow', 'ugh',
]

SCENE_RX = re.compile(r'^\s*[•\-*]\s*(?:Cảnh|Canh|Scene)\s+(\d+)\s*\[([^\]]*)\]\s*:?\s*(.*)$', re.I)
COLS_RX = re.compile(r'(?:Giá trị|Value)\s*:\s*(?P<val>[^|]*)\|\s*(?:Vòng lặp|Loops?)\s*:\s*(?P<loop>[^|]*)\|\s*'
                     r'(?:Khán giả|Audience)\s*:\s*(?P<aud>[^|]*)\|\s*(?:Cường độ|Intensity)\s*:\s*\[?(?P<int>\d+)', re.I)
LINK_RX = re.compile(r'^\s*↳\s*\[?\s*(NHƯNG|VÌ VẬY|VI VAY|BUT|THEREFORE|VÀ RỒI|VA ROI|AND THEN)\b', re.I)
BLOCK_RX = re.compile(r'^\s*-{2,}\s*(?:CẢNH|CANH|SCENE)\s+(\d+)\s*\(([^)]*)\)', re.I)
DIALOGUE_RX = re.compile(r'([A-ZÀ-Ỹ][\wÀ-ỹ\-]*(?:\s[A-ZÀ-Ỹ][\wÀ-ỹ\-]*)?)\s*(?:\([^)]*\))?\s*:\s*["“]([^"”]+)["”]')
SCORE_RX = re.compile(r'=\s*\[?\s*(\d{1,2})\s*\]?\s*/\s*16')
SUBSCORE_RX = re.compile(r'(\w[\wÀ-ỹ ]*?)\s*\[?\s*([0-2])\s*\]?\s*/\s*2\b')


def norm(t):
    return re.sub(r'\s+', ' ', t.replace(' ', ' ')).strip()


def load_rules(path):
    d = os.path.dirname(os.path.abspath(path))
    p = os.path.join(d, 'project_rules.json')
    if os.path.exists(p):
        try:
            return json.load(open(p, encoding='utf-8'))
        except Exception:
            return {}
    return {}


def section(text, start_pat, end_pats):
    m = re.search(start_pat, text, re.I)
    if not m:
        return ''
    rest = text[m.end():]
    ends = [re.search(e, rest, re.I) for e in end_pats]
    cut = min([e.start() for e in ends if e] or [len(rest)])
    return rest[:cut]


def scene_refs(s):
    return [int(x) for x in re.findall(r'(?:Cảnh|Canh|Scene|\bs)\s*\[?\s*(\d{1,2})', s, re.I)]


def parse(text):
    data = {'scenes': [], 'links': [], 'blocks': {}}
    lines = text.split('\n')
    cur = None
    for ln in lines:
        m = SCENE_RX.match(ln)
        if m:
            fields = [f.strip() for f in m.group(2).split('|')]
            desc = m.group(3).strip()
            cur = {'n': int(m.group(1)), 'fields': fields, 'desc': desc,
                   'dur': 15 if any(re.match(r'15', f) for f in fields) or '15s' in fields[0] else 10,
                   'type': fields[1].lower() if len(fields) > 1 else '',
                   'combat': any('combat' in f.lower() for f in fields),
                   'loc': norm(desc.strip('[] ').split(',')[0]).lower(),
                   'cols': None}
            data['scenes'].append(cur)
            continue
        if cur and cur['cols'] is None:
            c = COLS_RX.search(ln)
            if c:
                cur['cols'] = c.groupdict()
                continue
        lk = LINK_RX.match(ln)
        if lk:
            data['links'].append(lk.group(1).upper())
    # prose blocks (Pass B)
    block, buf = None, []
    for ln in lines:
        b = BLOCK_RX.match(ln)
        if b or re.match(r'^\s*📓|^\s*PHẦN 5|^\s*={5,}', ln):
            if block is not None:
                data['blocks'][block[0]] = (block[1], '\n'.join(buf))
            block, buf = ((int(b.group(1)), b.group(2)) if b else None), []
            continue
        if block is not None:
            buf.append(ln)
    if block is not None:
        data['blocks'][block[0]] = (block[1], '\n'.join(buf))
    return data


def audit(path):
    text = open(path, encoding='utf-8').read()
    rules = load_rules(path)
    errors, warns, notes = [], [], []
    d = parse(text)
    scenes = d['scenes']
    has_break = lambda key: re.search(r'BREAK\s*:[^\n]*' + key, text, re.I) is not None

    # ---------- structure ----------
    for label, pat in [('PHẦN 1', r'PHẦN 1'), ('PHẦN 3A (Retention Map)', r'PHẦN 3A|RETENTION MAP'),
                       ('PHẦN 3B (scene list)', r'PHẦN 3B|DANH SÁCH CẢNH')]:
        if not re.search(pat, text, re.I):
            errors.append(f"Missing section {label} (workflow.md §8.3 Pass A)")
    pass_b = bool(re.search(r'PHẦN 4|VĂN XUÔI', text, re.I)) and bool(d['blocks'])
    if not pass_b:
        notes.append("Pass A only (no PHẦN 4 prose blocks) — prose, budget and dialogue checks skipped")
    if len(scenes) < 4:
        errors.append(f"Only {len(scenes)} scene-list lines parsed — use '• Cảnh 01 [10s | Hook | @Director | ...]: ...'")
    nums = [s['n'] for s in scenes]
    if nums and nums != list(range(nums[0], nums[0] + len(nums))):
        warns.append(f"Scene numbering is not contiguous: {nums}")

    # ---------- retention map ----------
    rmap = section(text, r'PHẦN 3A|RETENTION MAP', [r'PHẦN 3B', r'DANH SÁCH CẢNH'])
    hook_m = re.search(r'Hook 3 gi[âa]y[^\n]*?#\s*(\d{1,2})', rmap or text, re.I)
    if not hook_m:
        errors.append("Retention Map: no 'Hook 3 giây Cảnh 01: #N — ...' line with a hook type #1–#12")
    else:
        hook_line = re.search(r'Hook 3 gi[âa]y[^\n]*', rmap or text, re.I).group(0)
        if not re.search(r'➔|->|→|câu hỏi|question', hook_line, re.I):
            warns.append("Retention Map: hook line does not name the question it opens")
    cliff_m = re.search(r'Cliffhanger cuối tập\s*:\s*C\s*([1-7])', text, re.I)
    if not cliff_m:
        errors.append("Retention Map: no 'Cliffhanger cuối tập: C1–C7' line")
    if not re.search(r'Câu hỏi của tập|Episode question', text, re.I):
        warns.append("Retention Map: no episode yes/no question")

    # ---------- scene columns ----------
    flat, no_cols, intensities = [], [], []
    loop_open_at, loop_paid_at = {}, {}
    for s in scenes:
        c = s['cols']
        if not c:
            no_cols.append(s['n'])
            continue
        val = c['val']
        if not re.search(r'➔|->|→', val) or re.search(r'\[\s*\.\.\.\s*\]|không đổi|no shift', val, re.I):
            flat.append(s['n'])
        intensities.append((s['n'], int(c['int'])))
        for kind, lid in re.findall(r'(mở|open|đẩy|push|trả|pay)\w*\s+L(\d+)', c['loop'], re.I):
            lid = int(lid)
            if kind.lower() in ('mở', 'open'):
                loop_open_at.setdefault(lid, s['n'])
            elif kind.lower() in ('trả', 'pay'):
                loop_paid_at.setdefault(lid, s['n'])
    if no_cols:
        errors.append(f"Scenes without the retention columns (Giá trị | Vòng lặp | Khán giả | Cường độ): {no_cols}")
    if flat:
        (warns if len(flat) <= 2 else errors).append(
            f"Scenes with no value shift (state A ➔ state B): {flat} — no shift = merge or cut (doctrine §1)")
    for lid, pay in loop_paid_at.items():
        op = loop_open_at.get(lid)
        if op is None:
            errors.append(f"Loop L{lid} is paid in scene {pay} but never opened (payoff without plant)")
        elif op >= pay:
            errors.append(f"Loop L{lid} opens in scene {op} but is paid in scene {pay} (plant must come earlier)")
    if scenes and loop_open_at:
        dead_cuts = []
        for s in scenes[:-1]:
            live = [l for l, o in loop_open_at.items() if o <= s['n'] and loop_paid_at.get(l, 10**6) > s['n']]
            if not live:
                dead_cuts.append(f"{s['n']}→{s['n'] + 1}")
        if dead_cuts:
            warns.append(f"Cuts with no open loop (viewer has no reason to stay): {dead_cuts} (0c §5)")
        last = scenes[-1]['n']
        if not [l for l, o in loop_open_at.items() if loop_paid_at.get(l, 10**6) > last]:
            warns.append("Every loop is closed by the last scene — the episode needs an open question into the next one")
    elif scenes:
        errors.append("No loops recorded ('Vòng lặp: mở L1 / đẩy L1 / trả L1')")
    if intensities:
        vals = [v for _, v in intensities]
        if max(vals) < 8:
            warns.append(f"Intensity curve peaks at {max(vals)} — the climax should reach 8–10")
        if min(vals) > 4 and not has_break('lull'):
            warns.append("Intensity curve has no lull (≤ 4) — contrast makes the peak land")
        if intensities[0][1] < 6:
            warns.append(f"Scene {intensities[0][0]} (hook) intensity is {intensities[0][1]} — open hot (≥ 6)")

    # ---------- rhythm ----------
    run, prev = 1, None
    for s in scenes:
        t = re.sub(r'[^a-zà-ỹ/ ]', '', s['type'])
        run = run + 1 if t and t == prev else 1
        if run > MAX_SAME_TYPE_RUN:
            warns.append(f"Scenes up to {s['n']}: {run} consecutive '{s['type']}' scenes (never 3 in a row — 0c §5)")
        prev = t
    if scenes and not any(re.search(r'v\.?o\.?|silent|lặng|câm|kể chuyện', s['type']) for s in scenes) and not has_break('silent'):
        warns.append("No silent / V.O. / storytelling scene in the episode (0c §5: ≥ 1)")

    # ---------- causality links ----------
    bad = [l for l in d['links'] if l in ('VÀ RỒI', 'VA ROI', 'AND THEN')]
    if bad:
        errors.append(f"{len(bad)} scene link(s) use 'Và rồi / And then' — connect with 'Vì vậy' or 'Nhưng' or cut the scene")
    if scenes and len(d['links']) < len(scenes) - 1:
        warns.append(f"Only {len(d['links'])} 'NHƯNG / VÌ VẬY' links for {len(scenes)} scenes (expected {len(scenes) - 1})")

    # ---------- W11 single location ----------
    locs = [s['loc'] for s in scenes if s['loc']]
    if len(locs) >= 6 and len(set(locs)) == 1 and not has_break('location'):
        warns.append(f"W11 All {len(locs)} scenes in one space ('{locs[0]}') — use 2–4 location sequences (0c §4) or add BREAK")

    # ---------- W10 prediction ledger ----------
    pred = re.search(r'PREDICT\s*\|([^\n]*)', text)
    if not pred:
        errors.append("W10 No 'PREDICT |' row (Audience Prediction Ledger, doctrine §9.2)")
    else:
        items = re.split(r'\bP\d+\b', pred.group(1))
        broken = [it for it in items if re.search(r'BẺ|BROKEN', it, re.I)]
        if len(broken) < 2:
            errors.append(f"W10 Only {len(broken)} BROKEN prediction(s); need ≥ 2 per episode")
        for it in broken:
            pay_m = re.search(r'(?:BẺ|BROKEN)\s*(?:ở|at)?\s*(?:Cảnh|Scene|s)?\s*\[?(\d{1,2})', it, re.I)
            plant_part = re.split(r'cài|plant', it, flags=re.I)
            if not pay_m:
                warns.append(f"W10 BROKEN entry without a payoff scene: '{norm(it)[:60]}'")
                continue
            if len(plant_part) < 2:
                errors.append(f"W10 BROKEN at scene {pay_m.group(1)} has no plant ('| cài ở Cảnh AA, BB')")
                continue
            plants = [int(x) for x in re.findall(r'\d{1,2}', plant_part[1])]
            late = [p for p in plants if p >= int(pay_m.group(1))]
            if not plants:
                errors.append(f"W10 BROKEN at scene {pay_m.group(1)} lists no plant scene numbers")
            elif late:
                errors.append(f"W10 BROKEN at scene {pay_m.group(1)} planted at {late} (plants must come earlier)")
    for row in ('KNOW', 'MISREAD', 'TWIST'):
        if not re.search(row + r'\s*\|', text):
            warns.append(f"Episode Spine row '{row} |' missing (doctrine §9.9)")
    twist = re.search(r'TWIST\s*\|[^\n]*?(?:Lớn|Major)\s*:\s*(?:Cảnh|Scene)?\s*\[?(\d{1,2})\]?[^\n]*?TW-?\s*(\d{2})', text, re.I)

    # ---------- repetition vs previous episode ----------
    m_ep = re.search(r'ep-(\d+)-script\.md$', os.path.basename(path), re.I)
    if m_ep and int(m_ep.group(1)) > 1:
        prev_path = os.path.join(os.path.dirname(path), f"ep-{int(m_ep.group(1)) - 1:0{len(m_ep.group(1))}d}-script.md")
        if os.path.exists(prev_path):
            pt = open(prev_path, encoding='utf-8').read()
            ph = re.search(r'Hook 3 gi[âa]y[^\n]*?#\s*(\d{1,2})', pt, re.I)
            pc = re.search(r'Cliffhanger cuối tập\s*:\s*C\s*([1-7])', pt, re.I)
            ptw = re.search(r'TWIST\s*\|[^\n]*?(?:Lớn|Major)\s*:[^\n]*?TW-?\s*(\d{2})', pt, re.I)
            if hook_m and ph and hook_m.group(1) == ph.group(1):
                warns.append(f"Hook type #{hook_m.group(1)} repeats the previous episode (rotate — 0c §5)")
            if cliff_m and pc and cliff_m.group(1) == pc.group(1):
                warns.append(f"Cliffhanger type C{cliff_m.group(1)} repeats the previous episode")
            if twist and ptw and twist.group(2) == ptw.group(1):
                warns.append(f"Major twist TW-{twist.group(2)} repeats the previous episode")
        else:
            notes.append(f"previous episode script not found ({os.path.basename(prev_path)}) — repetition check skipped")

    # ---------- prose / dialogue (Pass B) ----------
    if pass_b:
        title_m = re.search(r'TẬP\s*\[?\d+\]?\s*:\s*([^|\n]+)', text)
        title_words = re.sub(r'[^\w\s]', ' ', (title_m.group(1) if title_m else '').lower()).split()
        title_phrases = {' '.join(title_words[i:i + 3]) for i in range(max(0, len(title_words) - 2))}
        title_phrases |= {str(p).lower() for p in rules.get('title_phrases', [])}
        emo = [str(t).lower() for t in rules.get('emotion_label_terms', DEFAULT_EMOTION_TERMS)]
        emo_rx = re.compile(r'(?<!\w)(' + '|'.join(re.escape(t) for t in sorted(emo, key=len, reverse=True)) + r')(?!\w)', re.I) if emo else None
        inter = [str(t).lower() for t in rules.get('interjections', DEFAULT_INTERJECTIONS)]
        inter_rx = re.compile(r'^\s*(' + '|'.join(re.escape(t) for t in sorted(inter, key=len, reverse=True)) + r')\s*[?!.…,—-]', re.I)
        listed = {s['n']: s for s in scenes}
        missing_blocks = [n for n in listed if n not in d['blocks']]
        if missing_blocks:
            errors.append(f"Pass B: no prose block ('--- CẢNH K (10s ...) ---') for scenes {missing_blocks}")
        for n, (hdr, body) in sorted(d['blocks'].items()):
            if not re.search(r'Thẻ ý đồ|Intent', body, re.I):
                warns.append(f"Scene {n}: no 'Thẻ ý đồ' (Intent Card) line")
            lines = DIALOGUE_RX.findall(body)
            words = sum(len(l.split()) for _, l in lines)
            sc = listed.get(n, {})
            dur = 15 if '15' in hdr else 10
            combat = 'combat' in hdr.lower() or sc.get('combat')
            cap = WORDS_15S_ACTION if (dur == 15 and combat) else (WORDS_15S_DIALOGUE if dur == 15 else WORDS_10S)
            if words > cap:
                errors.append(f"Scene {n}: {words} spoken words > {cap} budget for {dur}s{' action' if combat else ''} (0c §2)")
            starts = [inter_rx.match(l) for _, l in lines]
            hits = [m.group(1).lower() for m in starts if m]
            if lines and len(hits) > math.ceil(len(lines) / 3):
                warns.append(f"Scene {n}: {len(hits)}/{len(lines)} lines open with an interjection (ration ≤ 1 in 3 — Law D2, 0c §2)")
            for a, b in zip(hits, hits[1:]):
                if a == b:
                    warns.append(f"Scene {n}: interjection '{a}' repeated back to back")
                    break
            for spk, l in lines:
                flat_l = ' ' + ' '.join(re.sub(r'[^\w\s]', ' ', l.lower()).split()) + ' '
                th = [p for p in title_phrases if p and f' {p} ' in flat_l]
                if th:
                    warns.append(f"W9 Scene {n} {spk} speaks the title {th} — the title is kept by images (doctrine §8.8)")
                if emo_rx:
                    found = sorted({m.lower() for m in emo_rx.findall(l)})
                    if found:
                        warns.append(f"W9 Scene {n} {spk} labels a feeling {found} — play it through action/memory/request or add BREAK (doctrine §8.9)")
        if not re.search(r'Ai biết gì|Who knows', text, re.I):
            warns.append("PHẦN 5: no 'Ai biết gì' ledger")
        if not re.search(r'Sổ vòng lặp|Loop ledger', text, re.I):
            warns.append("PHẦN 5: no loop ledger")

    # ---------- scorecard ----------
    scores = SCORE_RX.findall(text)
    if not scores:
        errors.append("No Engagement Scorecard total ('= N/16') — workflow.md §8.4")
    else:
        total = int(scores[-1])
        if total < SCORE_PASS:
            errors.append(f"Engagement Scorecard {total}/16 below pass mark {SCORE_PASS}/16 — rewrite the weakest criteria")
        card_lines = [l for l in text.split('\n') if SCORE_RX.search(l) and SUBSCORE_RX.search(l)]
        zeros = [norm(k).lstrip('·').strip() for k, v in SUBSCORE_RX.findall(card_lines[-1]) if v == '0'] if card_lines else []
        if zeros:
            errors.append(f"Engagement Scorecard has criteria at 0: {zeros}")

    return errors, warns, notes, len(scenes)


def main():
    if len(sys.argv) < 2:
        print("usage: python engine/screenplay_audit.py output/<slug>/ep-NN-script.md")
        return 2
    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"file not found: {path}")
        return 2
    errors, warns, notes, n = audit(path)
    print(f"[screenplay_audit] {path} — {n} scenes")
    for e in errors:
        print(f"  ERROR {e}")
    for w in warns:
        print(f"  WARN  {w}")
    for x in notes:
        print(f"  note  {x}")
    print(f"[screenplay_audit] {len(errors)} error(s), {len(warns)} warning(s)")
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())

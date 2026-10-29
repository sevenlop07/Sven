#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sven Cinematic Universe — AI Video Episode Compiler Linter
File: engine/episode_audit_suite.py
Purpose: Strictly validates output/<project>/tap-X.html before delivery.
Enforces all SSOT rules from director/SKILL.md, 4-ai-video-prompt-compiler.md, and Anti-Ghost Prop standards.

Rule classes (see workflow.md §2.10 and engine/references/0-creative-doctrine.md):
- Hard Constraints  -> blocking errors (delivery is blocked).
- Project Rules     -> read from output/<slug>/project_rules.json next to the tap file (Gates 4D/4E/4F);
                       skipped when the file is absent. Never hard-code one film's rules into this engine.
- Monotony Warnings -> non-blocking creative-review prompts (repeated phase splits, repeated reply openers,
                       voice-mode runs, back-to-back lines by one speaker; W9 story depth and W10 plot engine
                       read the Story Spine card). They are printed, not counted as errors.
"""

import html as html_lib
import json
import os
import re
import sys
from collections import Counter

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SCENE_SPLIT_RX = r'(<div[^>]*class="scene-card"[^>]*id="((?:s|sc)-\d{2})".*?)(?=<div[^>]*class="scene-card"|<div class="interactive-dock"|$)'
CARD_QUOTE_RX = r'class="[^"]*dia-(?:en|spoken)-quote[^"]*"[^>]*>(.*?)</span>'
PROMPT_RX = r'<pre[^>]*id="(p-\d{2})"[^>]*>(.*?)</pre>'
# A spoken / V.O. / O.S. line inside Code Block 1: support rich somatic action-speech verbs
SPEECH_VERBS_PATTERN = (
    r'(?:(?:(?:furiously|gently|coldly|harshly|bitterly|softly|breathlessly|icily|sharply|'
    r'desperately|tightly|dryly|fiercely|angrily|wearily|quietly|firmly|urgently|hoarsely|scornfully|proudly)\s+)?'
    r'(?:says|speaks|whispers|snaps|mutters|cries|replies|pleads|retorts|hisses|barks|yells|growls|'
    r'demands|murmurs|gasps|shouts|screams|snarls|taunts|scoffs|coaxes|bellows|groans|'
    r'snapping|whispering|hissing|barking|pleading|muttering|growling|shouting|demanding|murmuring|retorting))'
)
PROMPT_LINE_RX = re.compile(
    r'(?:^|\n|\.\s*|—\s*|\;\s*)([A-Za-z_][\w]*)\s+' + SPEECH_VERBS_PATTERN + r'\s*[:：]\s*[“"]\s*(.+?)\s*[”"]\s*[\(（]\s*(Voice of[^\)）]*)[\)）]',
    re.IGNORECASE,
)
TIME_BRACKET_RX = re.compile(r'\[(0\d:\d{2}(?:\.\d+)?)\s*[–\-]\s*(0\d:\d{2}(?:\.\d+)?)\]')
VO_RX = re.compile(r'\b(voice-over|voiceover|V\.O\.|inner voice|lips remain sealed|lips stay sealed)\b', re.IGNORECASE)
OS_RX = re.compile(r'\b(off-screen|O\.S\.)\b', re.IGNORECASE)
# Dialogue line inside visual prose (stripped before visual-prose checks; only the line itself, never the action prose)
DIALOGUE_STRIP_RX = re.compile(
    r'[A-Za-z_][\w]*\s+' + SPEECH_VERBS_PATTERN + r'\s*[:：]\s*[“"].*?[”"]\s*[\(（].*?[\)）]',
    re.MULTILINE | re.DOTALL | re.IGNORECASE,
)
VI_CHAR_RX = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', re.IGNORECASE)
ALLOWED_DURATIONS = (10.0, 15.0, 30.0)
# Banned dead-air phrasing that leaves characters idle without active micro-actions, causing AI hallucination
DEAD_AIR_RX = re.compile(
    r'\b(the\s+frame\s+holds\s+still|frame\s+holds\s+still|holds?\s+still|stands?\s+rigid\s+through|'
    r'sits?\s+rigid\s+through|weeping\s+in\s+(?:the\s+)?background\s+through|standing\s+still\s+through|'
    r'freeze\s+hold|frozen\s+hold|blinks?\s+(?:quietly|in\s+mild\s+surprise)\s+through)\b',
    re.IGNORECASE,
)
# Banned literal meta-tokens/placeholders in Code Block 1 (must be replaced with real inferred acoustic/visual prose)
LITERAL_PLACEHOLDER_RX = re.compile(
    r'\b(audio tag|cảm xúc khi nói|TRẠNG THÁI|LÀM GÌ|CẢM XÚC RA SAO|Ở ĐÂU)\b',
    re.IGNORECASE,
)
# Timing estimates for warnings (see engine/references/0b-temporal-camera-grammar.md §2–§3).
# Deliberately on the fast side so only clearly over-packed phases are flagged.
RATE_VI_SYL = 4.5
RATE_EN_WORD = 2.5
BREATH_S = 0.3
LIP_START_S = 0.3
LIP_CLEAR_S = 0.8
# W8: camera moves that are lip-sync-unsafe while travelling (0b-temporal-camera-grammar.md §5)
UNSAFE_MOVE_RX = re.compile(
    r'\b(whip[- ]pan\w*|crash zoom|dolly zoom|vertigo|orbit\w*|arc(?:s|ing)?|crane[sd]?|craning|pedestal|pivot\w*|'
    r'(?:rapid|swift|fast|quick|whip)\s+tilt\w*|camera\s+(?:rises|lifts|cranes|tilts|pans|swings|whips))\b',
    re.IGNORECASE)
# Prose stating that the move lands before the line (the timing is written into the prompt)
MOVE_SETTLED_RX = re.compile(
    r'(settl\w*\s+before|lands?\s+before|before\s+\w+\s+speaks|only once|once\s+(?:the\s+)?(?:camera|arc|lift|pivot|move|crane|tilt)\w*\s+(?:settles|lands|stops)|already\s+settled)',
    re.IGNORECASE)
TRACK_RX = re.compile(r'Track\s+(AB|A|B)\s+—')
# W9: words that label a feeling instead of playing it (Creative Doctrine §8.9).
# Override per project with project_rules.json -> "emotion_label_terms"; add "title_phrases" for extra title n-grams.
DEFAULT_EMOTION_TERMS = [
    'ghét', 'thương', 'buồn', 'sợ', 'giận', 'tủi thân', 'hạnh phúc', 'cô đơn', 'đau lòng',
    'hối hận', 'xin lỗi', 'đội ơn', 'biết ơn', 'tha thứ', 'nhớ thương',
    'love you', 'hate', 'afraid', 'scared', 'angry', 'sad', 'happy', 'lonely', 'sorry', 'grateful', 'forgive', 'i feel',
]


def _norm(text):
    """Normalize a quote for verbatim comparison: unescape, strip tags/quotes, collapse whitespace."""
    t = html_lib.unescape(re.sub(r'<[^>]+>', '', text or ''))
    for qchar in ['"', "'", chr(8220), chr(8221), chr(171), chr(187)]:
        t = t.replace(qchar, ' ')
    return ' '.join(t.split())


def _to_seconds(stamp):
    mm, ss = stamp.split(':')
    return int(mm) * 60 + float(ss)


def _load_project_rules(file_path):
    """Load output/<slug>/project_rules.json (same folder as the tap file). Returns {} when absent."""
    rules_path = os.path.join(os.path.dirname(os.path.abspath(file_path)), 'project_rules.json')
    if not os.path.exists(rules_path):
        return {}, None
    try:
        with open(rules_path, 'r', encoding='utf-8-sig') as f:
            return json.load(f), rules_path
    except Exception as exc:  # malformed rules must not silently disable checks
        return {'__error__': str(exc)}, rules_path


def _prompt_lines(p_text):
    """Return [(speaker, line, parenthetical, kind)] where kind is spoken / vo / os."""
    out = []
    for spk, line, paren in PROMPT_LINE_RX.findall(html_lib.unescape(p_text)):
        kind = 'vo' if VO_RX.search(paren) else ('os' if OS_RX.search(paren) else 'spoken')
        out.append((spk.strip(), line.strip(), paren.strip(), kind))
    return out


def _estimate_line_seconds(line):
    """Estimated delivery time of one line: counted words / language rate + breath.
    Contractions stay one word (father's); punctuation-only tokens (—, …) are not words."""
    text = html_lib.unescape(re.sub(r'<[^>]+>', '', line or ''))
    words = [t for t in text.split() if re.search(r'\w', t)]
    rate = RATE_VI_SYL if VI_CHAR_RX.search(line) else RATE_EN_WORD
    return len(words) / rate + BREATH_S


def _phases(p_text):
    """Split a prompt into [(start_s, end_s, phase_text)] using its time brackets."""
    text = html_lib.unescape(p_text)
    marks = list(TIME_BRACKET_RX.finditer(text))
    out = []
    for i, m in enumerate(marks):
        stop = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        chunk = text[m.end():stop]
        cut = re.search(r'Continuous fluid motion', chunk)
        if cut:
            chunk = chunk[:cut.start()]
        out.append((_to_seconds(m.group(1)), _to_seconds(m.group(2)), chunk))
    return out


def _voice_mode(lines):
    """Classify a scene's voice mode from its Code Block 1 lines (Creative Doctrine §4)."""
    if not lines:
        return 'silence'
    kinds = {k for _, _, _, k in lines}
    speakers = {s for s, _, _, _ in lines}
    if 'vo' in kinds and 'spoken' in kinds:
        return 'hybrid spoken+V.O.'
    if kinds == {'vo'}:
        return 'inner V.O.'
    if 'os' in kinds:
        return 'off-screen'
    if len(speakers) == 1:
        return 'solo / monologue'
    if len(speakers) == 2:
        return 'dialogue'
    return 'ensemble'


def audit_episode_html(file_path):
    print("=" * 70)
    print(f"[*] EXECUTING MASTER EPISODE AUDIT SUITE (PILLAR 4): {file_path}")
    print("=" * 70)

    if not os.path.exists(file_path):
        print(f"[X] FATAL ERROR: File not found: {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    errors = []
    warnings = []
    project_rules, rules_path = _load_project_rules(file_path)
    if '__error__' in project_rules:
        errors.append(f"Project Rules Fail: cannot parse {rules_path}: {project_rules['__error__']}")
        project_rules = {}

    # 1. Structural Tag Balance
    div_open = len(re.findall(r"<div[\s>]", html, re.IGNORECASE))
    div_close = len(re.findall(r"</div>", html, re.IGNORECASE))
    if div_open != div_close:
        errors.append(f"Gate 1A Fail: Div tag mismatch (Open={div_open}, Close={div_close}, Diff={div_open-div_close})")
    else:
        print(f"[+] Gate 1A Passed: Div Tag Balance (Total: {div_open})")

    pre_open = len(re.findall(r"<pre[\s>]", html, re.IGNORECASE))
    pre_close = len(re.findall(r"</pre>", html, re.IGNORECASE))
    if pre_open != pre_close:
        errors.append(f"Gate 1B Fail: Pre tag mismatch (Open={pre_open}, Close={pre_close})")
    else:
        print(f"[+] Gate 1B Passed: Pre Tag Balance (Total: {pre_open})")

    # 2. Scene Count & Scene Atom duration (10 s default; 15 / 30 s allowed, see 0b-temporal-camera-grammar.md §9)
    scene_cards = re.findall(r'<div[^>]*class="scene-card"', html)
    scene_count = len(scene_cards)
    is_30s_commercial = any(k in html.lower() for k in ["30.0 giây", "30 giây", "30s", "commercial"]) and scene_count == 3
    min_scenes = 3 if is_30s_commercial else 6
    if scene_count < min_scenes:
        errors.append(f"Gate 2 Fail: Found only {scene_count} scenes (Minimum {min_scenes} required for episode/commercial)")
    else:
        time_tags = re.findall(r'00:\d{2}\s*[–\-]\s*00:\d{2}|01:\d{2}\s*[–\-]\s*01:\d{2}|10\.0s|10 Giây', html)
        if len(time_tags) < scene_count:
            errors.append(f"Gate 2 Fail: Only {len(time_tags)}/{scene_count} scenes explicitly state their clip duration (00:00 – 00:10 / 00:15 / 00:30)")
        else:
            print(f"[+] Gate 2 Passed: Exactly {scene_count} Scenes with stated clip durations (10 s default; 15 / 30 s allowed)")
    # Scene count vs. the project's approved episode length (workflow.md §2.4; non-blocking)
    expected_scenes = project_rules.get('episode_scenes')
    if not is_30s_commercial:
        if expected_scenes and scene_count != int(expected_scenes):
            warnings.append(f"Scene count: {scene_count} scenes, but project_rules.json sets episode_scenes = {expected_scenes} (workflow §2.4)")
        elif not expected_scenes and scene_count not in (6, 9, 12):
            warnings.append(f"Scene count: {scene_count} scenes is not a default episode length (6 / 9 / 12) — record the user-approved count as episode_scenes in project_rules.json (workflow §2.4)")

    # 3. AI Video Execution Prompts & Rigorous Skill Compliance
    prompt_matches = re.findall(PROMPT_RX, html, re.DOTALL | re.IGNORECASE)
    if len(prompt_matches) < scene_count:
        errors.append(f"Gate 3 Fail: Found {len(prompt_matches)} prompt blocks with id='p-XX', expected {scene_count}")
    else:
        age_rx = re.compile(r'\b(\d{1,2}-year-old|aged \d{1,2})\b', re.IGNORECASE)
        pronoun_rx = re.compile(r'\b(he|she|his|her|him|they|their|them|herself|himself|themselves)\b', re.IGNORECASE)
        jargon_rx = re.compile(r'\b(\d{4}K|\d{3,4}\s*Kelvin|24fps|ARRI|Alexa|Panavision|Sony Venice|DaVinci Resolve|Kodak Vision|f/1\.\d|f/2|ISO\s*\d+|\d{2,3}\s?mm)\b', re.IGNORECASE)
        # Brand RED is case-sensitive and needs a model name; the colour word "red" is allowed.
        red_brand_rx = re.compile(r'\bRED\s+(?:V-Raptor|Komodo|Monstro|Helium|camera)\b')
        costume_rx = re.compile(r'\b(pyjamas|pajamas|blouse|trousers|chiffon dress|culotte|skirt)\b', re.IGNORECASE)
        base_minor_terms = [
            'boy', 'boys', 'girl', 'girls', 'kid', 'kids', 'child', 'children',
            'baby', 'babies', 'infant', 'infants', 'toddler', 'toddlers',
            'newborn', 'newborns', 'teen', 'teens', 'teenager', 'teenagers',
            'boyish', 'girlish', 'pediatric'
        ]
        # Retired child aliases (per project). No hard-coded film default (engine stays film-agnostic).
        project_minor_names = project_rules.get('minor_character_names', [])
        banned_minor_all = list(set(base_minor_terms + [str(m).lower() for m in project_minor_names]))
        minor_rx = re.compile(r'\b(' + '|'.join(re.escape(t) for t in sorted(banned_minor_all, key=len, reverse=True)) + r')\b', re.IGNORECASE)

        # Minor Protection Protocol (Pillar 4 §[10d]): approved ho_ten of every under-18 character.
        minor_characters = [str(m).strip() for m in project_rules.get('minor_characters', []) if str(m).strip()]
        minor_char_rx = re.compile(r'\b(' + '|'.join(re.escape(m) for m in minor_characters) + r')\b', re.IGNORECASE) if minor_characters else None
        # Sexual lexicon: banned anywhere in a prompt where a minor is present.
        minor_sexual_rx = re.compile(r'\b(sexy|seductive\w*|sultry|alluring|sensual\w*|erotic\w*|flirt\w*|kiss\w*|caress\w*|naked|nude|nudity|undress\w*|lingerie|topless|making out)\b', re.IGNORECASE)
        # A parent's kiss on the forehead or hair is caring contact (Band I/II) and is allowed.
        caring_kiss_rx = re.compile(r'\bkiss\w*\b[^.;\n]{0,40}\b(forehead|hair|crown of)\b', re.IGNORECASE)
        # Body-focused lexicon: banned in any sentence that names the minor.
        minor_body_rx = re.compile(r'\b(physique|curves|curvy|hourglass|figure-hugging|thighs?|hips|buttocks|bosom|breasts?|cleavage|bare skin|bare shoulders|bare legs|form-fitting|skin-tight|tight-fitting|crop top|cropped top|miniskirt|mini skirt|low-cut|see-through|underwear|bikini|swimsuit|lips parted|pouting)\b', re.IGNORECASE)
        # Violence lexicon: banned anywhere in a prompt where a minor is present.
        # Physical-violence terms only; emotional idioms ("wounded disbelief", "choked sob") are not listed.
        minor_violence_rx = re.compile(r'\b(slap|slaps|slapped|slapping|punch|punches|punched|punching|kick|kicks|kicked|kicking|shove|shoves|shoved|shoving|strangl\w*|knife|knives|blade|blades|gun|guns|weapon\w*|blood|bloody|bloodied|bleeding|bruis\w*|restrain\w*)\b', re.IGNORECASE)
        adult_label_words = r'(adult|grown woman|grown man|young woman|young man|aged (?:1[89]|[2-9]\d))'

        age_violations = []
        freeze_violations = []
        pronoun_violations = []
        jargon_violations = []
        costume_violations = []
        minor_violations = []

        freeze_rx = re.compile(r'\b(freeze\s+frame|freeze\s+hold|frozen\s+frame|zero-velocity)\b', re.IGNORECASE)

        for p_id, p_text in prompt_matches:
            # Check forbidden freeze holds (continuous natural motion, script-driven pacing)
            v_fz = freeze_rx.findall(p_text)
            if v_fz:
                freeze_violations.append(f"{p_id}: {v_fz}")

            # Strip spoken lines (with their acting parentheticals) to inspect visual narrative prose only.
            # Only the dialogue line itself is removed; the surrounding action prose is still checked.
            narrative_prose = DIALOGUE_STRIP_RX.sub('', html_lib.unescape(p_text))
            narrative_prose = re.sub(r'[\(（]\s*Voice of a \d{1,2}-year-old.*?[\)）]', '', narrative_prose, flags=re.DOTALL | re.IGNORECASE)
            narrative_prose = re.sub(r'Strictly zero violence.*?zero harm to minors.*', '', narrative_prose, flags=re.IGNORECASE)
            narrative_prose = re.sub(r'Do not generate.*', '', narrative_prose, flags=re.DOTALL | re.IGNORECASE)

            # Check age
            v_age = age_rx.findall(narrative_prose)
            if v_age: age_violations.append(f"{p_id}: {v_age}")

            # Check pronouns
            v_pro = pronoun_rx.findall(narrative_prose)
            if v_pro: pronoun_violations.append(f"{p_id}: {v_pro}")

            # Check hardware & Kelvin jargon
            v_jar = jargon_rx.findall(narrative_prose) + red_brand_rx.findall(narrative_prose)
            if v_jar: jargon_violations.append(f"{p_id}: {v_jar}")

            # Check costume (fixed: previously evaluated only against the last prompt)
            v_cos = costume_rx.findall(narrative_prose)
            if v_cos: costume_violations.append(f"{p_id}: {v_cos}")

            # Check minor safety (fixed: previously evaluated only against the last prompt)
            v_min = minor_rx.findall(narrative_prose)
            if v_min: minor_violations.append(f"{p_id}: {v_min}")

            # Minor Protection Protocol: only for prompts that name a registered under-18 character
            if minor_char_rx is not None:
                full_prompt = html_lib.unescape(p_text)
                # Negative safety directives may name banned concepts; they are not depictions.
                full_prompt = re.sub(r'Strictly zero violence.*?zero harm to minors[^\n]*', '', full_prompt, flags=re.IGNORECASE)
                full_prompt = re.sub(r'Do not generate.*', '', full_prompt, flags=re.DOTALL | re.IGNORECASE)
                present = sorted(set(m.lower() for m in minor_char_rx.findall(full_prompt)))
                if present:
                    scan_full = caring_kiss_rx.sub('', full_prompt)
                    v_sex = minor_sexual_rx.findall(scan_full)
                    if v_sex: minor_violations.append(f"{p_id}: sexual lexicon with minor {present}: {v_sex}")
                    v_vio = minor_violence_rx.findall(full_prompt)
                    if v_vio: minor_violations.append(f"{p_id}: violence lexicon with minor {present}: {v_vio}")
                    for sentence in re.split(r'[.;\n]', narrative_prose):
                        if minor_char_rx.search(sentence):
                            v_body = minor_body_rx.findall(sentence)
                            if v_body: minor_violations.append(f"{p_id}: body-focused lexicon on minor: {v_body}")
                    label_scan = re.sub(r'\[100%[^\]]*\]', ' ', narrative_prose)
                    for name in present:
                        n = re.escape(name)
                        lab_rx = re.compile(r'\b' + n + r'\b[^.;\n]{0,40}\b' + adult_label_words + r'\b|\b' + adult_label_words + r'\s+' + n + r'\b', re.IGNORECASE)
                        if lab_rx.search(label_scan):
                            minor_violations.append(f"{p_id}: adult label attached to minor '{name}' (never relabel a minor)")

        # Comprehensive Document-Wide Check for Hardware & Kelvin Jargon across ALL <pre> blocks (including 16:9 Model Sheets)
        all_pres = re.findall(r'<pre[^>]*id="([^"]*)"[^>]*>(.*?)</pre>', html, re.DOTALL | re.IGNORECASE)
        for pre_id, pre_text in all_pres:
            v_jar_all = jargon_rx.findall(pre_text) + red_brand_rx.findall(pre_text)
            if v_jar_all and not any(pre_id in item for item in jargon_violations):
                jargon_violations.append(f"{pre_id}: {v_jar_all}")

        if age_violations:
            errors.append(f"Gate 3A Fail: Mode B Zero-Age Law violated in: {age_violations}")
        else:
            print("[+] Gate 3A Passed: Zero Age Violations in Video Prompts (Mode B Compliant)")

        if freeze_violations:
            errors.append(f"Gate 3B Fail: Forbidden Freeze Holds detected: {freeze_violations}")
        else:
            print("[+] Gate 3B Passed: Dynamic Kinetic Rhythm (No Freeze Holds, Script-Driven Pacing)")

        if pronoun_violations:
            errors.append(f"Gate 3C Fail: Forbidden Pronouns detected in prose: {pronoun_violations} (Must use proper names)")
        else:
            print("[+] Gate 3C Passed: ZERO Forbidden Pronouns (§6b & Gate 3 Compliant)")

        if jargon_violations:
            errors.append(f"Gate 3D Fail: Camera Hardware / Kelvin Jargon detected: {jargon_violations} (Must use natural sensory prose)")
        else:
            print("[+] Gate 3D Passed: ZERO Hardware & Kelvin Jargon (Anti-Hardware Law Compliant)")

        if costume_violations:
            errors.append(f"Gate 3E Fail: Mode B Costume Descriptions detected: {costume_violations} (Costume locked by 16:9 Model Sheet)")
        else:
            print("[+] Gate 3E Passed: ZERO Mode B Costume Violations (Model Sheet SSOT Compliant)")

        if minor_violations:
            errors.append(f"Gate 3F Fail: Minor Protection Protocol violated (Pillar 4 §[10d]): {minor_violations}")
        else:
            print(f"[+] Gate 3F Passed: Minor Protection Protocol (generic minor nouns / retired aliases clear; {len(minor_characters)} registered minor character(s) checked)")

        # Gate 3G: Mandatory Master Prompt Prefix
        prefix_rx = re.compile(r'Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design', re.IGNORECASE)
        prefix_missing = [p_id for p_id, p_text in prompt_matches if not prefix_rx.search(p_text)]
        if prefix_missing:
            errors.append(f"Gate 3G Fail: Missing Master Prompt Prefix in: {prefix_missing}")
        else:
            print("[+] Gate 3G Passed: 100% Prompts begin with Master Cinematography & Sound Prefix")

        # Gate 3H: The Total Mathematical Purge Law (Zero Cartesian Math Document-Wide)
        # Strictly bans raw coordinate math in Tier 1 Audit Cards, Video Prompts, and Code Block 2 Handovers
        coord_rx = re.compile(r'(?<!z-)(?<![a-zA-Z0-9_])[XYZ]\s*:\s*[-+]?\d', re.IGNORECASE)
        all_coord_matches = coord_rx.findall(html)
        if all_coord_matches:
            errors.append(f"Gate 3H Fail: Raw Cartesian Coordinates detected document-wide: {all_coord_matches[:10]} (Math coordinates strictly banned; must use Observable Physical Architecture)")
        else:
            print("[+] Gate 3H Passed: ZERO Cartesian Math Coordinates Document-Wide (100% Observable Physical Architecture)")

        # Gate 3I: The Stateless Prompt Law (Zero Cross-Scene Dependencies in Code Block 1)
        cross_scene_rx = re.compile(r'\b(from Scene \d+|in Scene \d+|previous scene|next scene)\b', re.IGNORECASE)
        cross_violations = [p_id for p_id, p_text in prompt_matches if cross_scene_rx.search(p_text)]
        if cross_violations:
            errors.append(f"Gate 3I Fail: Cross-scene dependencies detected in Video Prompts: {cross_violations} (Prompts must be 100% stateless)")
        else:
            print("[+] Gate 3I Passed: ZERO Cross-Scene Dependencies in Video Prompts (100% Stateless)")

        # Gate 3J: The 3-Block Label Standard ([context]:, [subject]:, [Pro] : / [Prop] :)
        context_rx = re.compile(r'^\s*\[context\]\s*:', re.MULTILINE | re.IGNORECASE)
        subject_rx = re.compile(r'^\s*\[subject\]\s*:', re.MULTILINE | re.IGNORECASE)
        prop_label_rx = re.compile(r'^\s*\[Pro(?:p)?\]\s*:', re.MULTILINE | re.IGNORECASE)

        missing_labels = []
        for p_id, p_text in prompt_matches:
            missing = []
            if not context_rx.search(p_text): missing.append("[context]:")
            if not subject_rx.search(p_text): missing.append("[subject]:")
            if not prop_label_rx.search(p_text): missing.append("[Pro] :")
            if missing:
                missing_labels.append(f"{p_id}: missing {missing}")
        if missing_labels:
            errors.append(f"Gate 3J Fail: 3-Block Label Standard violated in: {missing_labels}")
        else:
            print("[+] Gate 3J Passed: 100% Video Prompts enforce the 3-Block Label Standard ([context]:, [subject]:, [Pro] :)")

        # Gate 3K: Multi-Modal Reference Anchor Syntax
        # Characters: [100% Appearance, attire, and facial features Refer to image X]
        # Context & Props: [100% Refer to image ...]
        ref_subject_rx = re.compile(r'\[100%\s*Appearance,\s*attire,\s*and\s*facial\s*features\s*Refer\s*to\s*image\s*[^\]]+\]', re.IGNORECASE)
        ref_general_rx = re.compile(r'\[100%\s*Refer\s*to\s*image\s*[^\]]+\]', re.IGNORECASE)

        ref_syntax_violations = []
        for p_id, p_text in prompt_matches:
            if not ref_subject_rx.search(p_text) or not ref_general_rx.search(p_text):
                ref_syntax_violations.append(p_id)
        if ref_syntax_violations:
            errors.append(f"Gate 3K Fail: Multi-Modal Reference Anchor Syntax missing in: {ref_syntax_violations}")
        else:
            print("[+] Gate 3K Passed: 100% Video Prompts enforce Multi-Modal Reference Anchor Syntax")

        # Gate 3L: Block Spacing Integrity (Empty line separation between blocks)
        spacing_violations = []
        for p_id, p_text in prompt_matches:
            p_lf = p_text.replace("\r\n", "\n")
            # Check for double newline before [subject]: and before [Pro] :
            if "\n\n[subject]:" not in p_lf and "\n\n[subject] :" not in p_lf:
                spacing_violations.append(f"{p_id}: missing blank line before [subject]:")
            elif not any(marker in p_lf for marker in ["\n\n[PROP]:", "\n\n[PROP] :", "\n\n[Prop]:", "\n\n[Prop] :", "\n\n[Pro] :"]):
                spacing_violations.append(f"{p_id}: missing blank line before [Pro] :")
        if spacing_violations:
            errors.append(f"Gate 3L Fail: Missing blank line separation between prompt blocks in: {spacing_violations}")
        else:
            print("[+] Gate 3L Passed: 100% Video Prompts maintain clean blank-line separation between blocks")

        # Gate 3M: Sub-Timeline Phase Division Law (Track A & Track B) + clip duration (10 / 15 / 30 s)
        # Phases must start at 00:00, be contiguous and non-overlapping, and end exactly at an allowed duration.
        timeline_violations = []
        for p_id, p_text in prompt_matches:
            brackets = [(_to_seconds(a), _to_seconds(b)) for a, b in TIME_BRACKET_RX.findall(html_lib.unescape(p_text))]
            if len(brackets) < 2:
                timeline_violations.append(f"{p_id}: found {len(brackets)} time brackets (Single lumped timeline forbidden; must subdivide into at least 2 distinct phases)")
                continue
            problems = []
            if abs(brackets[0][0]) > 0.05:
                problems.append(f"first phase starts at {brackets[0][0]}s, not 00:00")
            for (s1, e1), (s2, e2) in zip(brackets, brackets[1:]):
                if abs(s2 - e1) > 0.05:
                    problems.append(f"{'overlap' if s2 < e1 else 'gap'} between {e1}s and {s2}s")
            for s, e in brackets:
                if e <= s:
                    problems.append(f"empty or reversed phase {s}-{e}s")
            end = brackets[-1][1]
            if not any(abs(end - d) <= 0.05 for d in ALLOWED_DURATIONS):
                problems.append(f"clip ends at {end}s (allowed: 10, 15, 30)")
            if problems:
                timeline_violations.append(f"{p_id}: " + "; ".join(problems))
        if timeline_violations:
            errors.append(f"Gate 3M Fail: Phase timeline violations: {timeline_violations}")
        else:
            print("[+] Gate 3M Passed: Phases contiguous from 00:00 to a 10 / 15 / 30 s clip end (Track A & Track B)")

        # Gate 3N: Standard Diffusion Stability & Negative Directives
        stability_rx = re.compile(r'Continuous fluid motion,\s*realistic physics,.*?\bzero morphing\b', re.IGNORECASE)
        subtitle_rx = re.compile(r'Do not generate subtitles,\s*dialogue text,\s*titles,\s*timestamps,\s*or written text', re.IGNORECASE)
        neg_missing = [p_id for p_id, p_text in prompt_matches if not stability_rx.search(p_text) or not subtitle_rx.search(p_text)]
        if neg_missing:
            errors.append(f"Gate 3N Fail: Missing standard stability/negative directives in: {neg_missing}")
        else:
            print("[+] Gate 3N Passed: 100% Video Prompts enforce Standard Stability & Negative Directives")

        # Gate 3O: The Zero Dead Air & Micro-Action Continuity Law
        # Strictly bans phrases that leave characters idle/static, causing AI video hallucination
        dead_air_violations = []
        for p_id, p_text in prompt_matches:
            v_dead = DEAD_AIR_RX.findall(p_text)
            if v_dead:
                dead_air_violations.append(f"{p_id}: {v_dead}")
        if dead_air_violations:
            errors.append(f"Gate 3O Fail: Dead air phrases detected causing AI hallucination (Zero Dead Air Law violated): {dead_air_violations}")
        else:
            print("[+] Gate 3O Passed: ZERO Dead Air Phrases in Prompts (100% Continuous Micro-Action Progression)")

        # Gate 3P: Zero Literal Placeholder Tokens in Prompts
        placeholder_violations = []
        for p_id, p_text in prompt_matches:
            narrative_prose = DIALOGUE_STRIP_RX.sub('', html_lib.unescape(p_text))
            v_ph = LITERAL_PLACEHOLDER_RX.findall(narrative_prose)
            if v_ph:
                placeholder_violations.append(f"{p_id}: {v_ph}")
        if placeholder_violations:
            errors.append(f"Gate 3P Fail: Literal placeholder/meta tokens detected in prompts (must use inferred acoustic/visual prose): {placeholder_violations}")
        else:
            print("[+] Gate 3P Passed: ZERO Literal Placeholder Tokens in Prompts (100% Inferred Real Acoustics & Prose)")

        # Gate 3Q: The Optical Camera Clause Law (Banning Dangling "Focus on [name]")
        # Optical framing, focal plane, and depth of field must be declared upfront inside the Camera Clause before "—", never as a trailing sentence.
        dangling_focus_rx = re.compile(r'(?:^|[.;—\n])\s*Focus on\s+[A-Za-z_]+', re.IGNORECASE)
        dangling_focus_violations = []
        for p_id, p_text in prompt_matches:
            v_df = dangling_focus_rx.findall(p_text)
            if v_df:
                dangling_focus_violations.append(f"{p_id}: {v_df}")
        if dangling_focus_violations:
            errors.append(f"Gate 3Q Fail: Dangling 'Focus on [name]' detected in prompts: {dangling_focus_violations} (Optical framing, focal plane, and depth of field must be declared inside the Camera Clause before '—', never as a dangling sentence)")
        else:
            print("[+] Gate 3Q Passed: ZERO Dangling 'Focus on [name]' Phrases (100% Optical Camera Clause Compliant)")

    # Per-scene model: card quotes + Code Block 1 lines (used by Gates 4–4F and monotony warnings)
    raw_scenes = re.findall(SCENE_SPLIT_RX, html, re.DOTALL | re.IGNORECASE)
    scenes = []
    for s_html, s_id in raw_scenes:
        card_quotes = [_norm(q) for q in re.findall(CARD_QUOTE_RX, s_html, re.DOTALL | re.IGNORECASE)]
        prompt_m = re.search(PROMPT_RX, s_html, re.DOTALL | re.IGNORECASE)
        p_text = prompt_m.group(2) if prompt_m else ''
        scenes.append({
            'id': s_id,
            'num': int(re.search(r'(?:s|sc)-(\d+)', s_id).group(1)),
            'html': s_html,
            'card_quotes': [q for q in card_quotes if q],
            'prompt': p_text,
            'lines': _prompt_lines(p_text),
        })

    # 4. Dialogue Parity & Lip-Sync Breakdown
    # Scenes without dialogue (silence, pure action) are valid voice modes (Creative Doctrine §4).
    # Parity is enforced only where lines exist, in both directions (card -> prompt and prompt -> card).
    dia_spoken_matches = re.findall(CARD_QUOTE_RX, html, re.DOTALL | re.IGNORECASE)
    dia_spoken = len(dia_spoken_matches)
    dia_vn = len(re.findall(r'class="dia-vn-dub"', html, re.IGNORECASE))
    prompt_line_total = sum(len(s['lines']) for s in scenes)

    if dia_spoken != dia_vn:
        errors.append(f"Gate 4 Fail: Mismatch between spoken dialogue lines ({dia_spoken}) and directing/dub notes ({dia_vn})")
    else:
        unmatched_quotes = []
        orphan_prompt_lines = []
        for sc in scenes:
            norm_p = _norm(sc['prompt'])
            for q in sc['card_quotes']:
                if q not in norm_p:
                    unmatched_quotes.append(f"{sc['id']}: '{q}'")
            card_blob = ' || '.join(sc['card_quotes'])
            for spk, line, _, _ in sc['lines']:
                nl = _norm(line)
                if nl and nl not in card_blob:
                    orphan_prompt_lines.append(f"{sc['id']}: {spk} '{nl}'")
        if unmatched_quotes:
            errors.append(f"Gate 4 Fail: Dialogue - Prompt Verbatim Desynchronization! Lines missing from prompt: {unmatched_quotes}")
        if orphan_prompt_lines:
            errors.append(f"Gate 4 Fail: Prompt lines missing from the dialogue cards: {orphan_prompt_lines}")
        if not unmatched_quotes and not orphan_prompt_lines:
            silent = [sc['id'] for sc in scenes if not sc['card_quotes'] and not sc['lines']]
            note = f"; silent scenes: {silent}" if silent else ""
            print(f"[+] Gate 4 Passed: Dialogue Parity & Verbatim Prompt Synchronization ({dia_spoken} card lines, {prompt_line_total} prompt lines{note})")

    # Gate 4B: Dialogue Word Count Hard Cap (The 10-Second Shot Mental Model)
    # - Single-Speaker Shot: Target 25-30 words (Hard cap <= 32 words)
    # - Two-Shot Exchange: Max <= 15 words per speaker (15-Word Split Law!), Total <= 32 words
    word_cap_violations = []
    for sc in scenes:
        spoken_in_sc = [l for l in sc['lines'] if l[3] == 'spoken']
        if len(spoken_in_sc) <= 1:
            for spk, line, _, _ in sc['lines']:
                n = len(_norm(line).split())
                if n > 32:
                    word_cap_violations.append(f"{sc['id']} prompt {spk} ({n} words > single-speaker cap 32w): '{_norm(line)}'")
            for q in sc['card_quotes']:
                n = len(_norm(q).split())
                if n > 32:
                    word_cap_violations.append(f"{sc['id']} card ({n} words > single-speaker cap 32w): '{_norm(q)}'")
        else:
            tot_words = 0
            for spk, line, _, _ in sc['lines']:
                n = len(_norm(line).split())
                tot_words += n
                if n > 15:
                    word_cap_violations.append(f"{sc['id']} prompt {spk} ({n} words > two-shot cap 15w; must split shot): '{_norm(line)}'")
            for q in sc['card_quotes']:
                n = len(_norm(q).split())
                if n > 15:
                    word_cap_violations.append(f"{sc['id']} card ({n} words > two-shot cap 15w; must split shot): '{_norm(q)}'")
            if tot_words > 32:
                word_cap_violations.append(f"{sc['id']} total shot words ({tot_words} words > 32w cap)")
    if word_cap_violations:
        errors.append(f"Gate 4B Fail: Dialogue lines exceed word cap: {word_cap_violations}")
    else:
        print(f"[+] Gate 4B Passed: 100% Dialogue Lines adhere to word cap (Single-speaker <= 32w, Two-Shot <= 15w/speaker; Total lines: {dia_spoken})")

    # Gate 4C: Line Causality (warning only)
    # Monologue, solo lines, and V.O. are valid voice modes. Address words are NOT required.
    # Warn when one speaker delivers back-to-back spoken lines with no intervening reaction or V.O.
    causality_notes = []
    for sc in scenes:
        seq = sc['lines']
        distinct = {s for s, _, _, _ in seq}
        if len(distinct) < 2:
            continue  # single-speaker scene = deliberate monologue / solo mode
        for a, b in zip(seq, seq[1:]):
            if a[0] == b[0] and a[3] == 'spoken' and b[3] == 'spoken':
                causality_notes.append(f"{sc['id']}: {a[0]} speaks twice in a row inside an exchange")
    if causality_notes:
        warnings.append(f"Gate 4C: back-to-back lines by one speaker (confirm a reaction sits between them): {causality_notes}")
    print("[+] Gate 4C Passed: Line causality is non-blocking; monologue / solo / V.O. scenes accepted")

    # Gate 4D: Kinship Address Ladder (Project Rule — project_rules.json["kinship_ladder"])
    ladder = project_rules.get('kinship_ladder')
    if not ladder:
        print("[~] Gate 4D Skipped: no kinship_ladder in project_rules.json")
    else:
        from_scene = int(ladder.get('from_scene', 1))
        speakers = [s.lower() for s in ladder.get('speakers', [])]
        banned = ladder.get('banned_terms', [])
        banned_rx = re.compile(r'\b(' + '|'.join(re.escape(b) for b in banned) + r')\b', re.IGNORECASE) if banned else None
        pronoun_ladder_violations = []
        for sc in scenes:
            if sc['num'] < from_scene or not banned_rx:
                continue
            dia_items = re.findall(r'<div[^>]*class="dia-item"[^>]*>.*?<span[^>]*class="dia-speaker"[^>]*>(.*?)</span>.*?<span[^>]*class="[^"]*dia-(?:en|spoken)-quote[^"]*"[^>]*>(.*?)</span>', sc['html'], re.DOTALL | re.IGNORECASE)
            for spk_str, quote_str in dia_items:
                spk = spk_str.split('[')[0].strip()
                if any(s in spk.lower() for s in speakers) and banned_rx.search(quote_str):
                    pronoun_ladder_violations.append(f"{sc['id']}: banned address term from {spk} after the declared shift: '{_norm(quote_str)}'")
        if pronoun_ladder_violations:
            errors.append(f"Gate 4D Fail: Kinship Address Ladder (project rule) violated: {pronoun_ladder_violations}")
        else:
            print("[+] Gate 4D Passed: Kinship Address Ladder (project rule) respected")

    # Gate 4E: Domestic Meal & Biological Continuity (Project Rule — project_rules.json["meal_terms"])
    meal_terms = [m.lower() for m in project_rules.get('meal_terms', [])]
    if not meal_terms:
        print("[~] Gate 4E Skipped: no meal_terms in project_rules.json")
    else:
        meal_terms_by_scene = {}
        for sc in scenes:
            low = sc['html'].lower()
            found = sorted({m for m in meal_terms if m in low})
            if found:
                meal_terms_by_scene[sc['num']] = found
        meal_contradictions = []
        for s_num in range(1, len(scenes)):
            if s_num in meal_terms_by_scene and (s_num + 1) in meal_terms_by_scene:
                m1 = set(meal_terms_by_scene[s_num])
                m2 = set(meal_terms_by_scene[s_num + 1])
                if not m1.intersection(m2):
                    meal_contradictions.append(f"Scene {s_num:02d} ({m1}) vs Scene {s_num+1:02d} ({m2})")
        if meal_contradictions:
            errors.append(f"Gate 4E Fail: Domestic meal contradiction across consecutive timeline scenes: {meal_contradictions}")
        else:
            print("[+] Gate 4E Passed: Domestic Meal & Biological Continuity 100% Consistent")

    # Gate 4F: Anti-Bookish Grammar (Project Rule — project_rules.json["bookish_terms"])
    bookish_terms = [b.lower() for b in project_rules.get('bookish_terms', [])]
    if not bookish_terms:
        print("[~] Gate 4F Skipped: no bookish_terms in project_rules.json")
    else:
        bookish_violations = []
        for sc in scenes:
            for q in sc['card_quotes']:
                for bt in bookish_terms:
                    if bt in q.lower():
                        bookish_violations.append(f"{sc['id']}: '{bt}' in '{q}'")
        if bookish_violations:
            errors.append(f"Gate 4F Fail: Bookish written grammar detected in spoken dialogue: {bookish_violations}")
        else:
            print("[+] Gate 4F Passed: ZERO Bookish Written Grammar in Spoken Dialogue (Colloquial Dialect Compliant)")

    # Gate 4G: Speech Action Verb Standard (Mandatory: says, speaks, whispers, snaps, mutters, cries, replies, pleads, retorts)
    # Strictly bans naked "character:" without an action verb
    naked_speaker_rx = re.compile(r'^\s*([A-Za-z_][\w]*)\s*[:：]\s*[“"]', re.MULTILINE)
    naked_violations = []
    for sc in scenes:
        for m in naked_speaker_rx.finditer(html_lib.unescape(sc['prompt'])):
            naked_violations.append(f"{sc['id']}: '{m.group(1)}:' missing speech action verb (must use says, replies, snaps, whispers, pleads, retorts)")
    if naked_violations:
        errors.append(f"Gate 4G Fail: Naked speaker declaration without speech action verb: {naked_violations}")
    else:
        print("[+] Gate 4G Passed: 100% Spoken Dialogue lines declare Speech Action Verbs (says, replies, snaps, whispers, pleads, retorts)")

    # Gate 4H: Cross-Scene Handover Continuity & Kinetic Baton Relay
    # Ensures every scene has Code Block 2 (HANDOVER STATE AT 00:10.0) with Kinetic Momentum Bridge
    handover_violations = []
    for sc in scenes:
        low = sc['html'].lower()
        if "handover state" not in low and "code block 2" not in low:
            handover_violations.append(f"{sc['id']}: missing Code Block 2 Handover State Snapshot")
        elif "kinetic momentum" not in low and "momentum bridge" not in low and "handover" not in low:
            handover_violations.append(f"{sc['id']}: missing Kinetic Momentum Bridge to next scene")
    if handover_violations:
        errors.append(f"Gate 4H Fail: Cross-Scene Handover Continuity violations: {handover_violations}")
    else:
        print("[+] Gate 4H Passed: 100% Scenes maintain Cross-Scene Handover States & Kinetic Momentum Bridges")

    # 5. Interactive Copy Buttons & UI Infrastructure
    copy_btns = len(re.findall(r'class="copy-btn"', html))
    has_copy_all = "copyAllPrompts" in html
    has_toast = 'id="toast"' in html

    if copy_btns < scene_count:
        errors.append(f"Gate 5 Fail: Found only {copy_btns} copy buttons for {scene_count} scenes")
    elif not has_copy_all:
        errors.append("Gate 5 Fail: Missing 'Copy All Prompts' master action button in header")
    elif not has_toast:
        errors.append("Gate 5 Fail: Missing clipboard toast notification element")
    else:
        print(f"[+] Gate 5 Passed: Interactive Productivity System ({copy_btns} Copy Buttons + Copy All + Toast)")

    # W. Monotony Warnings (non-blocking; Creative Doctrine §5)
    if len(scenes) >= 4:
        # W1: identical phase-split pattern in >= 50% of prompts
        patterns = []
        for sc in scenes:
            brackets = TIME_BRACKET_RX.findall(sc['prompt'])
            if len(brackets) >= 2:
                cuts = tuple(round(_to_seconds(end), 1) for _, end in brackets[:-1])
                patterns.append(cuts)
        if patterns:
            top, count = Counter(patterns).most_common(1)[0]
            if count >= max(3, (len(patterns) + 1) // 2):
                warnings.append(f"W1 Phase splits: {count}/{len(patterns)} scenes cut at the same points {list(top)}s — let each scene's beats set its own split")

        # W2: repeated reply openers (first word in >= 4 scenes, or first two words in >= 3 scenes)
        one_word, two_word = Counter(), Counter()
        for sc in scenes:
            replies = [ln for ln in sc['lines'][1:]] if len(sc['lines']) > 1 else []
            seen1, seen2 = set(), set()
            for _, line, _, _ in replies:
                words = re.sub(r'[^\w\s]', ' ', _norm(line).lower()).split()
                if words:
                    seen1.add(words[0])
                if len(words) >= 2:
                    seen2.add(' '.join(words[:2]))
            one_word.update(seen1)
            two_word.update(seen2)
        rep2 = [f"'{k}' x{v}" for k, v in two_word.items() if v >= 3]
        rep1 = [f"'{k}' x{v}" for k, v in one_word.items() if v >= 4]
        if rep2 or rep1:
            warnings.append(f"W2 Reply openers repeat across scenes: {rep2 + rep1} — address words are optional; vary the attack of each reply")

        # W3: same voice mode in >= 3 consecutive scenes; uniform turn counts
        modes = [_voice_mode(sc['lines']) for sc in scenes]
        run_start = 0
        for i in range(1, len(modes) + 1):
            if i == len(modes) or modes[i] != modes[run_start]:
                if i - run_start >= 3:
                    ids = f"{scenes[run_start]['id']}..{scenes[i-1]['id']}"
                    warnings.append(f"W3 Voice mode run: '{modes[run_start]}' for {i - run_start} consecutive scenes ({ids}) — state the reason or vary the mode")
                run_start = i
        turns = [len(sc['lines']) for sc in scenes]
        t_top, t_count = Counter(turns).most_common(1)[0]
        if len(scenes) >= 6 and t_count >= 0.7 * len(scenes):
            warnings.append(f"W3 Turn counts: {t_count}/{len(scenes)} scenes have exactly {t_top} line(s) — vary the rhythm")
        print(f"[i] Voice modes by scene: " + ", ".join(f"{sc['id']}={m}" for sc, m in zip(scenes, modes)))

    # W4–W6. Timing grammar warnings (0b-temporal-camera-grammar.md §3, §7, §8)
    window_notes, share_notes, syntax_notes, move_notes, track_notes = [], [], [], [], []
    for sc in scenes:
        phases = _phases(sc['prompt'])
        if not phases:
            continue
        duration = phases[-1][1]
        total_speech = 0.0
        for start, end, chunk in phases:
            lines = _prompt_lines(chunk)
            if not lines:
                continue
            lip = [_estimate_line_seconds(ln) for _, ln, _, kind in lines if kind != 'vo']
            vo = [_estimate_line_seconds(ln) for _, ln, _, kind in lines if kind == 'vo']
            need = sum(lip) + sum(vo) + ((LIP_START_S + LIP_CLEAR_S) if lip else 0.0)
            total_speech += sum(lip) + sum(vo)
            if need > (end - start) + 0.05:
                window_notes.append(f"{sc['id']} [{start:g}-{end:g}s]: lines need ~{need:.1f}s, phase is {end - start:.1f}s")
        is_single_spk = len([l for l in sc['lines'] if l[3] == 'spoken']) <= 1
        max_share = 0.75 if (is_single_spk and duration <= 12.0) else (0.55 if duration >= 25.0 else 0.60)
        if duration > 0 and total_speech / duration > max_share:
            share_notes.append(f"{sc['id']}: ~{total_speech:.1f}s of speech in {duration:g}s ({100 * total_speech / duration:.0f}%, cap is {int(max_share*100)}%)")
        legacy = re.findall(r'(△|\]\s*(?:TRACK|Shot)\b[^\n]*\|)|\b(?:Phase|Shot)\s+\d\b', html_lib.unescape(sc['prompt']))
        if legacy:
            syntax_notes.append(sc['id'])
        # W8a: spoken line while the camera travels in a lip-sync-unsafe way
        for start, end, chunk in phases:
            spoken = [ln for ln in _prompt_lines(chunk) if ln[3] != 'vo']
            if not spoken:
                continue
            prose = DIALOGUE_STRIP_RX.sub(' ', chunk)
            moves = sorted({m.lower() for m in UNSAFE_MOVE_RX.findall(prose)})
            if moves and not MOVE_SETTLED_RX.search(prose):
                move_notes.append(f"{sc['id']} [{start:g}-{end:g}s] {moves} under {spoken[0][0]}'s line")
        # W8b: track label must match content (0b §8 rules)
        tm = TRACK_RX.search(html_lib.unescape(sc['prompt']))
        cuts = len(re.findall(r'\bCut to\b', sc['prompt']))
        if tm:
            track = tm.group(1)
            if track == 'A' and cuts:
                track_notes.append(f"{sc['id']}: Track A but {cuts} 'Cut to'")
            elif track in ('B', 'AB') and not cuts:
                track_notes.append(f"{sc['id']}: Track {track} but no 'Cut to'")
            elif track == 'AB' and not re.search(r'\bIn the same take\b', sc['prompt']):
                track_notes.append(f"{sc['id']}: Track AB but no phase continues the take ('In the same take')")
    if move_notes:
        warnings.append(f"W8 Camera travelling under a spoken line (arc / orbit / crane / pivot / whip / rapid tilt) — let the move land first and write it ('settles before X speaks'): {move_notes}")
    if track_notes:
        warnings.append(f"W8 Track label does not match the prompt: {track_notes}")
    if window_notes:
        warnings.append(f"W4 Lip-sync window: phases too short for their lines (start ≥ 0.3s, end ≥ 0.8s before the cut): {window_notes}")
    if share_notes:
        warnings.append(f"W5 Speech share above ~60% of the clip: {share_notes}")
    if syntax_notes:
        warnings.append(f"W6 Legacy prompt syntax (△ / pipes / Shot-Phase labels) in: {syntax_notes} — use '[time] scale, angle, move — prose'")

    # W9. Story-level depth (Creative Doctrine §8.8–§8.10): title spoken, feelings labelled, Story Spine missing
    title_m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.S | re.I)
    title_words = re.sub(r'[^\w\s]', ' ', _norm(title_m.group(1)).lower()).split() if title_m else []
    title_phrases = {' '.join(title_words[i:i + 3]) for i in range(len(title_words) - 2)}
    title_phrases |= {str(p).lower() for p in project_rules.get('title_phrases', [])}
    emotion_terms = [str(t).lower() for t in project_rules.get('emotion_label_terms', DEFAULT_EMOTION_TERMS)]
    emo_rx = re.compile(r'(?<!\w)(' + '|'.join(re.escape(t) for t in sorted(emotion_terms, key=len, reverse=True)) + r')(?!\w)',
                        re.IGNORECASE) if emotion_terms else None
    title_notes, emotion_notes = [], []
    for sc in scenes:
        for spk, line, _, _ in sc['lines']:
            flat = ' ' + ' '.join(re.sub(r'[^\w\s]', ' ', _norm(line).lower()).split()) + ' '
            hits = sorted(p for p in title_phrases if p and f' {p} ' in flat)
            if hits:
                title_notes.append(f"{sc['id']} {spk}: {hits}")
            if emo_rx:
                found = sorted({m.lower() for m in emo_rx.findall(_norm(line))})
                if found:
                    emotion_notes.append(f"{sc['id']} {spk}: {found}")
    if title_notes:
        warnings.append(f"W9 Title spoken in dialogue: {title_notes} — the title is a promise kept by images, not by a line (Doctrine §8.8)")
    if emotion_notes:
        warnings.append(f"W9 Lines label a feeling: {emotion_notes} — play it through an action, memory or request, or justify with a BREAK line (Doctrine §8.9)")
    if not re.search(r'id="story-spine"', html):
        warnings.append("W9 No Story Spine Card (id=\"story-spine\") — write the Spine before the scenes (Doctrine §8.10)")

    # W10. Plot engine (Creative Doctrine §9.2, §9.7, §8.7): prediction ledger and plant-before-payoff order
    spine_m = re.search(r'<div[^>]*id="story-spine"[^>]*>', html)
    if spine_m:
        depth, pos = 1, spine_m.end()
        for tag in re.finditer(r'<(/?)div\b[^>]*>', html[pos:], re.I):
            depth += -1 if tag.group(1) else 1
            if depth == 0:
                pos = spine_m.end() + tag.start()
                break
        spine_text = _norm(re.sub(r'<[^>]+>', ' ', html[spine_m.end():pos]))
        rows = dict((m.group(1).upper(), m.group(2)) for m in
                    re.finditer(r'\[([A-ZÉ]+)\]\s*(.*?)(?=\[[A-ZÉ]+\]|$)', spine_text, re.S))
        plot_notes = []
        ledger = rows.get('PREDICT')
        if ledger is None:
            plot_notes.append("no [PREDICT] row (Audience Prediction Ledger)")
        else:
            broken = re.findall(r'BROKEN\s+s(\d{2})([^|]*\|\s*plant\s+((?:s\d{2}[,\s]*)+))?', ledger)
            if len(broken) < 2:
                plot_notes.append(f"only {len(broken)} BROKEN prediction(s); need ≥ 2")
            for pay, has_plant, plants in broken:
                if not has_plant:
                    plot_notes.append(f"BROKEN s{pay} has no '| plant sNN'")
                    continue
                late = [f"s{p}" for p in re.findall(r's(\d{2})', plants) if int(p) >= int(pay)]
                if late:
                    plot_notes.append(f"BROKEN s{pay} planted at {late} (plant must come earlier)")
        for seg in re.split(r'[·;]', rows.get('LOOPS', '')):
            if '→' not in seg:
                continue
            before, after = seg.split('→', 1)
            plants = [int(p) for p in re.findall(r's(\d{2})', before)]
            pays = re.findall(r's(\d{2})', after)
            if plants and pays and max(plants) >= int(pays[0]):
                plot_notes.append(f"loop '{seg.strip()[:40]}…' pays at s{pays[0]} before or at its plant s{max(plants):02d}")
        if plot_notes:
            warnings.append(f"W10 Plot engine: {plot_notes} — plant earlier, break ≥ 2 predictions (Doctrine §9.2, §9.7)")

    # Summary
    print("-" * 70)
    if warnings:
        print("[W] CREATIVE REVIEW WARNINGS (non-blocking — fix, or justify in one line at CP4):")
        for w in warnings:
            print(f"  • {w}")
        print("-" * 70)
    if errors:
        print("[!] EPISODE AUDIT FAILED WITH THE FOLLOWING VIOLATIONS:")
        for err in errors:
            print(f"  • {err}")
        print("[!] DELIVERY IS STRICTLY BLOCKED. AGENT MUST RECTIFY BEFORE NOTIFYING USER.")
        print("-" * 70)
        return False
    else:
        print("[V] ALL MASTER EPISODE GATES PASSED! FILE IS 100% PRODUCTION-READY.")
        print("-" * 70)
        return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python engine/episode_audit_suite.py <path_to_tap_html>')
        sys.exit(1)
    target = sys.argv[1]
    success = audit_episode_html(target)
    sys.exit(0 if success else 1)

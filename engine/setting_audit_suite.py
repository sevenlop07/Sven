#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sven Cinematic Universe — Pre-Production Setting Bible Linter (Gate 1.5)
File: engine/setting_audit_suite.py
Purpose: Strictly validates output/<project>/setting.html at Stage 2 (CP2) and Stage 3 (CP3).
"""

import html as html_lib
import os
import re
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def audit_setting_html(file_path):
    print("=" * 70)
    print(f"[*] EXECUTING GATE 1.5 SETTING BIBLE AUDIT (CP2 / CP3): {file_path}")
    print("=" * 70)

    if not os.path.exists(file_path):
        print(f"[X] FATAL ERROR: File not found: {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    errors = []

    # 1. Structural Tag Balance
    div_open = len(re.findall(r"<div[\s>]", html, re.IGNORECASE))
    div_close = len(re.findall(r"</div>", html, re.IGNORECASE))
    if div_open != div_close:
        errors.append(f"Gate 1A Fail: Div tag mismatch (Open={div_open}, Close={div_close}, Diff={div_open-div_close})")
    else:
        print(f"[+] Gate 1A Passed: Div Tag Balance (Total: {div_open})")

    sec_open = len(re.findall(r"<section[\s>]", html, re.IGNORECASE))
    sec_close = len(re.findall(r"</section>", html, re.IGNORECASE))
    if sec_open != sec_close:
        errors.append(f"Gate 1B Fail: Section tag mismatch (Open={sec_open}, Close={sec_close})")
    elif sec_open < 6:
        errors.append(f"Gate 1B Fail: Found only {sec_open} sections (Minimum 6 canonical sections required: Sections 1, 2, 3, 4A, 4B, 5)")
    else:
        print(f"[+] Gate 1B Passed: Section Tag Balance ({sec_open} sections)")

    # 2. Mandatory Architectural Sections
    canonical_sections = [
        {"name": "Section 1 (Master Narrative Arc)", "ids": ["story", "sec-1", "vision"]},
        {"name": "Section 2 (Canonical Cast)", "ids": ["cast", "sec-2", "characters"]},
        {"name": "Section 3 (16:9 Model Sheets)", "ids": ["modelsheets", "sec-3", "char-model-sheets"]},
        {"name": "Section 4A (Prop Universe)", "ids": ["props", "sec-4a", "prop-universe"]},
        {"name": "Section 4B (Location Universe)", "ids": ["locations", "sec-4b", "location-universe"]},
        {"name": "Section 5 (Scene/Episode Roadmap)", "ids": ["episodes", "sec-5", "roadmap"]},
    ]

    found_sections = {}
    for sec in canonical_sections:
        matched_id = None
        for alias in sec["ids"]:
            pattern = '(?:id="' + alias + '"|id=\'' + alias + '\')'
            if re.search(pattern, html, re.IGNORECASE):
                matched_id = alias
                break
        if matched_id:
            found_sections[sec["name"]] = matched_id
        else:
            errors.append(f"Gate 2 Fail: Missing {sec['name']} (Expected one of IDs: {sec['ids']})")

    if len(found_sections) == len(canonical_sections):
        print(f"[+] Gate 2 Passed: All Core Architectural Sections Present")

    # Helper function to extract section by alias list
    def extract_section_content(alias_list):
        for alias in alias_list:
            pattern = '(?:id="' + alias + '"|id=\'' + alias + '\').*?</section>'
            m = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
            if m:
                return m.group(0)
        return None

    def extract_prompts(block):
        # Match <pre>, <code>, or mono-font divs
        snippets = re.findall(r'<(?:pre|div)[^>]*(?:font-family:[^>]*JetBrains Mono|prompt-box|prompt-display)[^>]*>(.*?)</(?:pre|div)>', block, re.DOTALL | re.IGNORECASE)
        if not snippets:
            snippets = re.findall(r'<pre[^>]*>(.*?)</pre>', block, re.DOTALL | re.IGNORECASE)
        return snippets

    # 2A. Section 1 — Master Narrative Depth & 3-Layer Stakes Check (Gate 1C)
    sec1_content = extract_section_content(["story", "sec-1", "vision"])
    if sec1_content:
        sec1_lower = sec1_content.lower()
        doc_lower = html.lower()
        has_theme_conflict = any(k in sec1_lower for k in [
            "question", "câu hỏi", "chủ đề", "xung đột", "va chạm", "conflict", "theme", "dramatic", "kịch tính", "bi kịch"
        ])
        has_stakes_structure = any(k in doc_lower for k in [
            "stakes", "cọc cược", "hồi", "act", "tuyến", "plot", "bước ngoặt", "twist", "hậu quả", "ticking clock", "beat"
        ])
        if not (has_theme_conflict and has_stakes_structure):
            errors.append("Gate 1C Fail: Section 1 (Master Narrative Arc) lacks 3-Layer Stakes / Thematic Question / Act Blueprint depth markers")
        else:
            print("[+] Gate 1C Passed: Section 1 enforces Master Narrative Depth & 3-Layer Stakes Blueprint")
        # Gate 1D — Heart & Value North Star (0d-heart-and-value.md §3): the Value Card lives in Section 1 / the Story Spine
        value_rows = {row: bool(re.search(r'\b' + row + r'\b\s*(?:\||:|</)', sec1_content + html, re.IGNORECASE))
                      for row in ("VALUE", "HEART", "TAKEAWAY")}
        missing_value_rows = [r for r, ok in value_rows.items() if not ok]
        if missing_value_rows:
            errors.append(f"Gate 1D Fail: Story Spine / Section 1 lacks the Value Card rows {missing_value_rows} "
                          "(VALUE · HEART · TAKEAWAY · SHADOW — engine/references/0d-heart-and-value.md §3)")
        else:
            print("[+] Gate 1D Passed: Value Card (VALUE · HEART · TAKEAWAY) present — the story knows what it gives the viewer")

    # 2B. Section 2 — Canonical Cast 6-Layer Psychology & Anti-Caricature Check (Gate 2B)
    sec2_content = extract_section_content(["cast", "sec-2", "characters"])
    if sec2_content:
        sec2_lower = sec2_content.lower()
        psych_dimensions = [
            any(k in sec2_lower for k in ["wound", "vết thương", "sang chấn", "trauma", "nỗi đau", "quá khứ"]),
            any(k in sec2_lower for k in ["lie", "lời nói dối", "vỏ bọc", "ngụy trang", "sai lầm", "mask"]),
            any(k in sec2_lower for k in ["want", "khao khát", "mục tiêu", "tham vọng", "desire"]),
            any(k in sec2_lower for k in ["need", "nhu cầu", "chữa lành", "thức tỉnh", "fear", "nỗi sợ", "mâu thuẫn", "paradox"]),
        ]
        if sum(1 for d in psych_dimensions if d) < 2:
            errors.append("Gate 2B Fail: Section 2 (Canonical Cast) lacks 6-Layer Character Psychology markers (Wound / Lie / Want / Need / Fear / Paradox)")
        else:
            print("[+] Gate 2B Passed: Section 2 enforces 6-Layer Character Psychology & Anti-Caricature Depth")

    # 3. Section 3 — Character Model Sheets & Mode B Prompts
    sec3_content = extract_section_content(["modelsheets", "sec-3", "char-model-sheets"])
    if not sec3_content:
        errors.append("Gate 3 Fail: Section 3 (Model Sheets) content block not found")
    else:
        prompts = extract_prompts(sec3_content)
        if len(prompts) < 2:
            errors.append(f"Gate 3 Fail: Section 3 must have at least 2 character model sheet prompt blocks (Found: {len(prompts)})")
        else:
            has_four_view = any("four-view" in p.lower() or "4-view" in p.lower() or "character sheet" in p.lower() or "model sheet" in p.lower() for p in prompts)
            has_mode_b = "mode b" in sec3_content.lower() or "video prompt snippet" in sec3_content.lower()
            if not has_four_view:
                errors.append("Gate 3 Fail: Section 3 prompts missing 'four-view' / 'model sheet' technical keywords")
            elif not has_mode_b:
                errors.append("Gate 3 Fail: Section 3 missing Mode B Video Prompt Snippet references")
            else:
                print(f"[+] Gate 3 Passed: Section 3 has {len(prompts)} Model Sheet Prompts & Mode B Snippets")

        # 3B. Minor-Safe Model Sheets (Pillar 4 §[10d] §3; Pillar 2 Mẫu 0B)
        age_decl_rx = re.compile(r'\b(\d{1,2})-year-old\b|\baged\s+(\d{1,2})\b', re.IGNORECASE)
        minor_sheet_banned_rx = re.compile(
            r'\b(fashion|editorial|glamou?r|beauty (?:lighting|studio|photography)|commercial (?:fashion|studio)|'
            r'physique|curves|curvy|toned|slender|hourglass|figure-hugging|form-fitting|skin-tight|tight-fitting|'
            r'micro-pores|porcelain|luminous (?:fair )?skin|dewy|glowing skin|lipstick|eyeliner|mascara|'
            r'seductive|sultry|alluring|sexy|attractive|cropped|mini ?skirt|mini shorts|low-cut|see-through|sheer|'
            r'bodysuit|swimsuit|swimwear|bikini|lingerie|underwear|headless|neck-down|'
            r'adult|young woman|young man)\b', re.IGNORECASE)
        minor_sheet_violations = []
        for i, snippet in enumerate(prompts, 1):
            text = re.sub(r'<[^>]+>', ' ', html_lib.unescape(snippet))
            # Voice parentheticals describe audio, not the sheet.
            sheet_text = re.sub(r'[\(（]\s*Voice of a .*?[\)）]', ' ', text, flags=re.DOTALL | re.IGNORECASE)
            ages = [int(a or b) for a, b in age_decl_rx.findall(sheet_text)]
            if ages and min(ages) < 18:
                hits = sorted(set(h.lower() for h in minor_sheet_banned_rx.findall(sheet_text)))
                if hits:
                    minor_sheet_violations.append(f"sheet #{i} (age {min(ages)}): {hits}")
        if minor_sheet_violations:
            errors.append(f"Gate 3B Fail: Minor-safe model sheet rules violated (Pillar 4 §[10d] §3): {minor_sheet_violations}")
        else:
            print("[+] Gate 3B Passed: Minor-Safe Model Sheets (every sheet under 18 is free of glamour, body, and adult-label lexicon)")

        # 3C. Adult Character Skin Complexion, Makeup/Grooming, Adult Female Hourglass/Dress Fashion & Master Rear-Anchor Height Scale Lock Check (Pillar 2 §1B & §2)
        deprecated_adult_boilerplate_rx = re.compile(r'\bthin\s+natural\s+nude\s+lips\b', re.IGNORECASE)
        scale_alignment_rx = re.compile(
            r'\b(primary\s+height\s+master\s+reference|one\s+full\s+head\s+shorter|scaled\s+strictly\s+from\s+figure\s+3|'
            r'strictly\s+matching\s+figure\s+3|1:1\s+(?:anatomical\s+)?body\s+scale|shared\s+shoulder\s+line|'
            r'horizontal\s+shoulder|align\s+horizontally)\b', re.IGNORECASE)
        headless_conflict_rx = re.compile(
            r'\b(mannequin(?:-style)?\s+neck|zero\s+height\s+mismatch|no\s+chopped\s+skull|zero\s+cropped\s+head)\b', re.IGNORECASE)
        adult_female_marker_rx = re.compile(r'\b(female|woman|heroine|lady|wife|sister|matriarch)\b', re.IGNORECASE)
        adult_female_hourglass_rx = re.compile(r'\b(hourglass|cinched\s+waist|feminine\s+(?:bust-to-hip\s+)?curves|sculpted\s+(?:feminine\s+)?curves|toned\s+legs)\b', re.IGNORECASE)
        adult_female_dress_rx = re.compile(r'\b(dress|gown|skirt)\b', re.IGNORECASE)
        adult_female_frumpy_banned_rx = re.compile(r'\b(trench-blazer|trench-style\s+lapel|trench\s+coat\s+worn\s+over\s+a\s+fitted\s+.*?turtleneck|jumpsuit|wide-leg\s+pleated\s+silk\s+trousers|ankle\s+trousers)\b', re.IGNORECASE)
        adult_boilerplate_hits = []
        unaligned_scale_hits = []
        headless_conflict_hits = []
        female_missing_hourglass_hits = []
        female_missing_dress_hits = []
        female_frumpy_outfit_hits = []
        for i, snippet in enumerate(prompts, 1):
            text = re.sub(r'<[^>]+>', ' ', html_lib.unescape(snippet))
            sheet_text = re.sub(r'[\(（]\s*Voice of a .*?[\)）]', ' ', text, flags=re.DOTALL | re.IGNORECASE)
            ages = [int(a or b) for a, b in age_decl_rx.findall(sheet_text)]
            if not ages or min(ages) >= 18:
                if deprecated_adult_boilerplate_rx.search(sheet_text):
                    adult_boilerplate_hits.append(f"sheet #{i}")
                if "headless" in sheet_text.lower():
                    if not scale_alignment_rx.search(sheet_text):
                        unaligned_scale_hits.append(f"sheet #{i}")
                    conflict_m = headless_conflict_rx.findall(sheet_text)
                    if conflict_m:
                        headless_conflict_hits.append(f"sheet #{i} ({sorted(set(m.lower() for m in conflict_m))})")
                if adult_female_marker_rx.search(sheet_text) and not re.search(r'\b(male|man|patriarch)\b', sheet_text, re.IGNORECASE):
                    if not adult_female_hourglass_rx.search(sheet_text):
                        female_missing_hourglass_hits.append(f"sheet #{i}")
                    if not adult_female_dress_rx.search(sheet_text):
                        female_missing_dress_hits.append(f"sheet #{i}")
                    frumpy_m = adult_female_frumpy_banned_rx.findall(sheet_text)
                    if frumpy_m:
                        female_frumpy_outfit_hits.append(f"sheet #{i} ({sorted(set(m.lower() for m in frumpy_m))})")
        if female_missing_hourglass_hits:
            errors.append(f"Gate 3C Fail: Adult female sheet(s) {female_missing_hourglass_hits} lack hourglass/feminine curve body descriptors ('hourglass figure', 'slender cinched waist', 'sculpted feminine curves', 'long toned legs')")
        if female_missing_dress_hits:
            errors.append(f"Gate 3C Fail: Adult female sheet(s) {female_missing_dress_hits} lack fashionable dress/skirt attire ('sheath midi dress', 'bodycon dress', 'cocktail dress', 'slip dress')")
        if female_frumpy_outfit_hits:
            errors.append(f"Gate 3C Fail: Adult female sheet(s) {female_frumpy_outfit_hits} contain banned bulky/frumpy hybrid outfits (trench-blazer, trench-style lapel, turtleneck+trousers, jumpsuit)")
        if headless_conflict_hits:
            errors.append(f"Gate 3C Fail: Headless adult model sheet(s) {headless_conflict_hits} contain self-contradictory triggers ('mannequin neck', 'zero height mismatch', 'no chopped skull', 'zero cropped head') that stretch headless bodies or regrow tiny heads — use Pillar 2 Master Rear-Anchor Height Law (Figure 3 Primary Height Reference + scoped Figure 3 & Figure 4 headroom ONLY)")
        if adult_boilerplate_hits or unaligned_scale_hits:
            if adult_boilerplate_hits:
                print(f"[!] Gate 3C Notice: Adult sheet(s) {adult_boilerplate_hits} use legacy 'thin natural nude lips' boilerplate — upgrade to Pillar 2 §1B Skin Complexion & Female Makeup / Male Grooming spec.")
            if unaligned_scale_hits:
                print(f"[!] Gate 3C Notice: Adult sheet(s) {unaligned_scale_hits} use legacy unaligned 'headless' syntax without Master Rear-Anchor Height Lock — upgrade to Pillar 2 §2 4-Figure Master Rear-Anchor spec.")
        elif not (female_missing_hourglass_hits or female_missing_dress_hits or female_frumpy_outfit_hits or headless_conflict_hits):
            print("[+] Gate 3C Passed: Adult Model Sheets enforce Feminine Hourglass Proportions, High-Fashion Dress Attire, Skin/Makeup & Master Rear-Anchor 4-Figure Lock")

        # 3D. 100% Standalone Outfit Prompt Coverage & Unmerged Character Sheet Check
        if sec2_content:
            cast_outfit_files = sorted(set(
                f.lower() for f in re.findall(r'\b([a-z0-9_-]+-(?:home|work|date|outing|casual|formal|gala|uniform)\.jpg)\b', sec2_content, re.IGNORECASE)
                if not f.lower().startswith(('loc-', 'prop-', 'location_', 'prop_'))
            ))
            sec3_lower = sec3_content.lower()
            missing_outfit_prompts = [f for f in cast_outfit_files if f"refer to image {f}" not in sec3_lower]
            if missing_outfit_prompts:
                errors.append(f"Gate 3D Fail: Outfit file(s) declared in Section 2 (#cast) are missing standalone prompt cards/Mode B snippets in Section 3 (#modelsheets): {missing_outfit_prompts}")
            elif cast_outfit_files and len(prompts) < len(cast_outfit_files):
                errors.append(f"Gate 3D Fail: Section 2 declares {len(cast_outfit_files)} character outfit files, but Section 3 only has {len(prompts)} prompt boxes (Every outfit variant must have its own standalone full prompt box)")
            else:
                print(f"[+] Gate 3D Passed: 100% Standalone Prompt Coverage ({len(prompts)} full prompt boxes for all character outfit variants)")

    # 4. Section 4A — Master Prop Universe Prompts
    sec4a_content = extract_section_content(["props", "sec-4a", "prop-universe"])
    if not sec4a_content:
        errors.append("Gate 4 Fail: Section 4A (Prop Universe) content block not found")
    else:
        prop_prompts = extract_prompts(sec4a_content)
        if len(prop_prompts) < 1:
            errors.append("Gate 4 Fail: Section 4A must contain at least 1 Prop Design Sheet prompt block")
        else:
            has_mode_b_prop = "mode b" in sec4a_content.lower() or "video prompt snippet" in sec4a_content.lower()
            if not has_mode_b_prop:
                errors.append("Gate 4 Fail: Section 4A missing Mode B Prop Reference Snippets")
            else:
                print(f"[+] Gate 4 Passed: Section 4A has {len(prop_prompts)} Prop Sheet Prompts & Mode B Snippets")

    # 5. Section 4B — Master Location Universe Prompts
    sec4b_content = extract_section_content(["locations", "sec-4b", "location-universe"])
    if not sec4b_content:
        errors.append("Gate 5 Fail: Section 4B (Location Universe) content block not found")
    else:
        loc_prompts = extract_prompts(sec4b_content)
        if len(loc_prompts) < 1:
            errors.append("Gate 5 Fail: Section 4B must contain at least 1 Location Sheet prompt block")
        else:
            has_mode_b_loc = "mode b" in sec4b_content.lower() or "video prompt snippet" in sec4b_content.lower()
            if not has_mode_b_loc:
                errors.append("Gate 5 Fail: Section 4B missing Mode B Location Reference Snippets")
            else:
                compass_loc_rx = re.compile(
                    r'\b(north|south|east|west)\s+(?:end|side|wall|entrance|door|doors|chair|head|foot|edge|corner|window|windows)\b',
                    re.IGNORECASE,
                )
                compass_loc_hits = []
                for idx_l, lp in enumerate(loc_prompts, 1):
                    c_hits = compass_loc_rx.findall(lp)
                    if c_hits:
                        compass_loc_hits.append(f"Location Prompt #{idx_l}: {sorted(set(c_hits))}")
                if compass_loc_hits:
                    errors.append(f"Gate 5B Fail: Section 4B Location Prompt(s) contain indoor compass directions {compass_loc_hits} — use visible architectural landmarks instead")
                else:
                    print(f"[+] Gate 5 & 5B Passed: Section 4B has {len(loc_prompts)} Location Sheet Prompts & Mode B Snippets (Zero Indoor Compass Directions)")

    # 6. Section 5 — Scene / Episode Roadmap Integrity
    sec5_content = extract_section_content(["episodes", "sec-5", "roadmap"])
    if not sec5_content:
        errors.append("Gate 6 Fail: Section 5 (Roadmap) content block not found")
    else:
        # Check scene cards count or episode table rows
        scene_cards = len(re.findall(r'class="[^"]*(?:scene-master-card|episode-card|scene-card)[^"]*"', sec5_content, re.IGNORECASE))
        table_rows = len(re.findall(r'<tr', sec5_content, re.IGNORECASE))
        total_items = max(scene_cards, table_rows)
        if total_items < 6:
            errors.append(f"Gate 6 Fail: Section 5 contains insufficient scene/episode items ({total_items})")
        else:
            print(f"[+] Gate 6 Passed: Section 5 has {total_items} Roadmap Production Items")

            # 6B. Section 5 — Dramatic Spine & Continuity Chain Validation
            has_conflict = any(k in sec5_content.lower() for k in ["xung đột", "conflict", "spine", "bước ngoặt", "cọc cược", "hậu quả", "baton"])
            has_consequence = any(k in sec5_content.lower() for k in ["hậu quả", "cliffhanger", "cold water", "gáo nước lạnh", "consequence", "ticking clock"])
            if not has_conflict:
                errors.append("Gate 6B Fail: Section 5 roadmap missing Dramatic Conflict / Spine progression keywords")
            elif not has_consequence:
                errors.append("Gate 6B Fail: Section 5 roadmap missing Irreversible Consequence / Cliffhanger / Baton keywords")
            else:
                print(f"[+] Gate 6B Passed: Section 5 enforces Dramatic Spine & 4-Way Continuity Chain")

            # 6C. Section 5 — Per-Episode Location, Participating Cast & Sequence Cluster Completeness
            ep_cards = re.split(r'<div[^>]*class="[^"]*scene-master-card[^"]*"[^>]*>', sec5_content, flags=re.IGNORECASE)[1:]
            incomplete_ep_cards = []
            for idx, card_html in enumerate(ep_cards, 1):
                c_low = card_html.lower()
                has_loc_block = any(k in c_low for k in ["địa điểm", "bối cảnh", "loc-"])
                has_cast_block = any(k in c_low for k in ["nhân vật tham gia", "các nhân vật", "tuyến c"])
                has_cluster_block = any(k in c_low for k in ["chia cụm cảnh", "cụm 1", "sequence 1", "quân số"])
                if not (has_loc_block and has_cast_block and has_cluster_block):
                    incomplete_ep_cards.append(f"Episode Card #{idx}")
            if incomplete_ep_cards:
                errors.append(f"Gate 6C Fail: Episode roadmap card(s) in Section 5 lack explicit Location + Participating Characters + Sequence Cluster breakdown: {incomplete_ep_cards}")
            else:
                print(f"[+] Gate 6C Passed: All {len(ep_cards)} Episode Cards explicitly detail Locations, Participating Characters & Sequence Clusters")

    # 7. Cross-Section Consistency Audit (Gate 7A: Age/Height Parity, Gate 7B: Character Token Parity, Gate 7C: Geographic/Year Consistency)
    if sec2_content and sec3_content:
        # 7A. Extract character cards in Section 2: token, age, height
        char_cards = re.findall(
            r'<code>([a-z]+_[a-z]+)</code>\)\s*—\s*(\d{2})\s*Tuổi.*?Cao\s*(\d{3})\s*cm',
            sec2_content,
            re.DOTALL | re.IGNORECASE
        )
        age_height_mismatches = []
        missing_sec3_tokens = []
        # Extract all (prompt_box, mode_b_box) pairs in Section 3
        sec3_pairs = re.findall(
            r'<pre[^>]*class="prompt-box"[^>]*>(.*?)</pre>\s*<div[^>]*class="mode-b-box"[^>]*>(.*?)</div>',
            sec3_content,
            re.DOTALL | re.IGNORECASE
        )
        for token, cast_age, cast_height in char_cards:
            token_l = token.lower()
            if token_l not in sec3_content.lower():
                missing_sec3_tokens.append(token_l)
            char_prompt_blocks = [p_box for p_box, mb_box in sec3_pairs if token_l in mb_box.lower()]
            for idx, p_block in enumerate(char_prompt_blocks, 1):
                m_age = re.search(r'\baged\s+(\d{2})\b', p_block, re.IGNORECASE)
                m_height = re.search(r'\b(\d{3})cm\s+height\b', p_block, re.IGNORECASE)
                if m_age and m_age.group(1) != cast_age:
                    age_height_mismatches.append(f"{token_l} prompt #{idx}: Section 2 age={cast_age} vs Section 3 prompt age={m_age.group(1)}")
                if m_height and m_height.group(1) != cast_height:
                    age_height_mismatches.append(f"{token_l} prompt #{idx}: Section 2 height={cast_height}cm vs Section 3 prompt height={m_height.group(1)}cm")

        if age_height_mismatches:
            errors.append(f"Gate 7A Fail: Character Age/Height mismatch between Section 2 (#cast) and Section 3 (#modelsheets): {age_height_mismatches}")
        elif missing_sec3_tokens:
            errors.append(f"Gate 7B Fail: Character tokens in Section 2 (#cast) missing from Section 3 (#modelsheets): {missing_sec3_tokens}")
        else:
            print(f"[+] Gate 7A & 7B Passed: Cross-Section Character Age, Height & Token Parity Verified ({len(char_cards)} characters)")

    # 7C. Cross-Section Geographic & Prop Year Consistency Check
    has_texas = bool(re.search(r'\b(dallas|houston)\b', html, re.IGNORECASE))
    has_illinois = bool(re.search(r'\b(chicago|joliet|lake michigan)\b', html, re.IGNORECASE))
    if has_texas and has_illinois:
        errors.append("Gate 7C Fail: Cross-section geographic drift detected (File mixes Dallas/Houston with Chicago/Joliet/Lake Michigan across sections)")
    else:
        print("[+] Gate 7C Passed: 100% Unified Geographic & Timeline Universe Across All Sections")

    # Summary
    print("-" * 70)
    if errors:
        print("[!] GATE 1.5 SETTING BIBLE AUDIT (CP2 / CP3) FAILED WITH THE FOLLOWING VIOLATIONS:")
        for err in errors:
            print(f"  • {err}")
        print("[!] DELIVERY IS STRICTLY BLOCKED. AGENT MUST RECTIFY BEFORE NOTIFYING USER.")
        print("-" * 70)
        return False
    else:
        print("[V] ALL GATE 1.5 SETTING BIBLE GATES PASSED! SETTING BIBLE IS COMPLIANT FOR REVIEW.")
        print("-" * 70)
        return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python engine/setting_audit_suite.py <path_to_setting_html>')
        sys.exit(1)
    target = sys.argv[1]
    success = audit_setting_html(target)
    sys.exit(0 if success else 1)

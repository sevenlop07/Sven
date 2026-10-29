#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sven Cinematic Universe — Pre-Production Setting Bible Linter
File: engine/setting_audit_suite.py
Purpose: Strictly validates output/<project>/setting.html before Checkpoint 1.
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
    print(f"[*] EXECUTING PRE-CHECKPOINT 1 SETTING BIBLE AUDIT: {file_path}")
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
    elif sec_open < 8:
        errors.append(f"Gate 1B Fail: Found only {sec_open} sections (Minimum 10 required for full series bible)")
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
                print(f"[+] Gate 5 Passed: Section 4B has {len(loc_prompts)} Location Sheet Prompts & Mode B Snippets")

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

    # Summary
    print("-" * 70)
    if errors:
        print("[!] PRE-CHECKPOINT 1 AUDIT FAILED WITH THE FOLLOWING VIOLATIONS:")
        for err in errors:
            print(f"  • {err}")
        print("[!] DELIVERY IS STRICTLY BLOCKED. AGENT MUST RECTIFY BEFORE NOTIFYING USER.")
        print("-" * 70)
        return False
    else:
        print("[V] ALL PRE-CHECKPOINT 1 GATES PASSED! SETTING BIBLE IS COMPLIANT FOR REVIEW.")
        print("-" * 70)
        return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python engine/setting_audit_suite.py <path_to_setting_html>')
        sys.exit(1)
    target = sys.argv[1]
    success = audit_setting_html(target)
    sys.exit(0 if success else 1)

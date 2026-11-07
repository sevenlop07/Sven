#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sven Cinematic Universe — Master Production Runbook Manager
File: engine/runbook_manager.py
Purpose: Machine-readable preset loader and project initializer for Sven Showrunner.
Usage:
  python engine/runbook_manager.py list
  python engine/runbook_manager.py inspect <preset_slug>
  python engine/runbook_manager.py init <preset_slug> <project_slug> [--aspect-ratio 16:9|9:16|4:3|2.39:1] [--visual-style 3d-semi-real|pixar-3d|theatrical-live-action|...] [--force]
"""

import os
import sys
import json
import argparse

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
RUNBOOKS_FILE = os.path.join(SCRIPT_DIR, "runbooks.json")

def load_runbooks():
    if not os.path.exists(RUNBOOKS_FILE):
        print(f"[!] Fatal: Runbooks catalog not found at {RUNBOOKS_FILE}")
        sys.exit(1)
    with open(RUNBOOKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def list_runbooks():
    data = load_runbooks()
    print("=" * 80)
    print("🎬 SVEN CINEMATIC UNIVERSE — PRODUCTION PRESETS & RUNBOOKS")
    print("   Aspect Ratio Law: 100% User-Governed across all genres.")
    print("=" * 80)
    for r in data.get("runbooks", []):
        models = ", ".join(r.get("target_video_models", []))
        scenes = r.get("default_episode_scenes", 9)
        duration = r.get("default_scene_duration_s", 10.0)
        total_s = r.get("total_runtime_target_s", scenes * duration)
        def_ar = r.get("default_aspect_ratio", "16:9")
        supported_ar = ", ".join(r.get("supported_aspect_ratios", ["16:9", "9:16"]))
        print(f"► [{r['slug']}] {r['title']}")
        print(f"   • Aspect Ratio  : User-Selectable (Default: {def_ar} | Supported: {supported_ar})")
        print(f"   • Mode          : {r.get('prompt_grammar_mode', 'N/A')}")
        print(f"   • Episode Scale : {scenes} scenes x {duration}s = {total_s}s total runtime")
        print(f"   • Max Words/Line: {r.get('screenplay_constraints', {}).get('max_words_per_line', 18)} words")
        print(f"   • Target Models : {models}")
        print(f"   • Genre Module  : {r.get('genre_module', 'N/A')}")
        print("-" * 80)
    styles = data.get("visual_style_presets", {})
    if styles:
        print("🎨 MASTER VISUAL STYLE PRESETS (--visual-style):")
        for s_key, s_val in styles.items():
            print(f"   • [{s_key}] : {s_val.get('name', '')}")
        print("=" * 80)

def inspect_runbook(slug):
    data = load_runbooks()
    found = next((r for r in data.get("runbooks", []) if r["slug"] == slug), None)
    if not found:
        print(f"[!] Error: Runbook '{slug}' not found.")
        print(f"Available slugs: {', '.join(r['slug'] for r in data.get('runbooks', []))}")
        sys.exit(1)
    print("=" * 80)
    print(f"📋 RUNBOOK SPECIFICATION: {found['slug']}")
    print("=" * 80)
    print(json.dumps(found, indent=2, ensure_ascii=False))

def init_project(slug, project_slug, aspect_ratio=None, visual_style=None, dialect=None, force=False):
    data = load_runbooks()
    preset = next((r for r in data.get("runbooks", []) if r["slug"] == slug), None)
    if not preset:
        print(f"[!] Error: Preset '{slug}' does not exist.")
        sys.exit(1)

    style_presets = data.get("visual_style_presets", {})
    chosen_style_slug = visual_style if visual_style else "3d-semi-real"
    chosen_style_obj = style_presets.get(chosen_style_slug, {
        "name": chosen_style_slug,
        "code_block_1_header": "",
        "model_sheet_template": "MẪU 2B (3D Semi-Realistic Animation)"
    })

    target_dir = os.path.join(PROJECT_ROOT, "output", project_slug)
    os.makedirs(target_dir, exist_ok=True)
    rules_file = os.path.join(target_dir, "project_rules.json")

    if os.path.exists(rules_file) and not force:
        print(f"[!] Warning: {rules_file} already exists.")
        print("    Use --force to overwrite with preset defaults.")
        sys.exit(1)

    chosen_ar = aspect_ratio if aspect_ratio else preset.get("default_aspect_ratio", "16:9")

    # Dynamically adapt dialect & address rules by genre preset instead of locking to Southern family drama
    genre_defaults = {
        "family-melodrama-epic": {
            "dialect": "Southern Vietnamese (Giọng Nam Bộ chuẩn: nghen, hén, hổng, chớ bộ, nè, nha)",
            "address": "Standard Family Kinship (Má, Con, Anh, Em)",
            "banned": ["anh yêu", "em yêu"]
        },
        "healing-social-drama": {
            "dialect": "Natural Colloquial Vietnamese (Adaptive: Northern / Southern / Central per setting)",
            "address": "Contextual Social & Family Kinship",
            "banned": []
        },
        "microdrama-vertical": {
            "dialect": "Sharp Modern Urban Vietnamese (Nhịp nhanh, sắc gọn, hiện đại)",
            "address": "Hierarchical Status & Corporate/Relationship Address (Chủ tịch, Tổng giám đốc, Tôi - Cô/Anh)",
            "banned": []
        },
        "sitcom-episodic": {
            "dialect": "Snappy Everyday Colloquial (Tung hứng đời thường, bắt nhịp hài tự nhiên)",
            "address": "Flexible Roommate / Colleague / Family Address",
            "banned": []
        },
        "action-combat-thriller": {
            "dialect": "High-Stakes Tactical & Martial Register (Đanh thép, ngắn gọn, dứt khoát)",
            "address": "Faction / Rival / Martial Hierarchy",
            "banned": []
        },
        "thriller-mystery-crime": {
            "dialect": "Measured Investigative & Psychological Register (Sắc lạnh, kiệm lời, nhiều ẩn ý)",
            "address": "Investigative / Suspect / Professional Address",
            "banned": []
        },
        "fantasy-time-travel-isekai": {
            "dialect": "Era-Adaptive Register (Cổ phong chuẩn mực cho tuyến Cổ đại/Tiên hiệp; Hiện đại sắc bén cho tuyến Đô thị/Xuyên không)",
            "address": "Sect / Dynasty / Hunter Hierarchy (Sư huynh, Điện hạ, Tiểu thư, Tông chủ / Đội trưởng, Thợ săn)",
            "banned": []
        },
        "music-video-narrative": {
            "dialect": "Zero Spoken Dialogue (Lyric Sync / Pure Visual Poetry)",
            "address": "N/A (Visual Only)",
            "banned": []
        }
    }
    g_cfg = genre_defaults.get(slug, {
        "dialect": "Adaptive Natural Register (Matched to Setting & Genre)",
        "address": "Contextual Relationship Address",
        "banned": []
    })
    chosen_dialect = dialect if dialect else g_cfg["dialect"]

    project_rules = {
        "project_slug": project_slug,
        "runbook_preset": slug,
        "title": preset.get("title", ""),
        "aspect_ratio": chosen_ar,
        "_aspect_ratio_note": "Governed by User Choice. The Director and Screenwriter adapt staging dynamically to this framing.",
        "visual_style_slug": chosen_style_slug,
        "visual_style_name": chosen_style_obj.get("name", ""),
        "visual_style_header": chosen_style_obj.get("code_block_1_header", ""),
        "model_sheet_template": chosen_style_obj.get("model_sheet_template", ""),
        "target_video_models": preset.get("target_video_models", []),
        "episode_scenes": preset.get("default_episode_scenes", 9),
        "_episode_scenes_note": f"{preset.get('default_episode_scenes', 9)} scenes x {preset.get('default_scene_duration_s', 10.0)}s (or 15.0s for Seedance Action/Chase peaks).",
        "default_scene_duration_s": preset.get("default_scene_duration_s", 10.0),
        "allowed_scene_durations_s": preset.get("allowed_scene_durations_s", [10.0, 15.0]),
        "stage4_delivery_mode": "interactive-scene-by-scene-copilot",
        "html_deliverable_policy": "ONLY output/<slug>/setting.html (Stage 2 Resource Prep). Zero tap-X.html files. Stage 3 (1 episode at a time) & Stage 4 (1 scene at a time with TH1/TH2/TH3 cross-check) run 100% interactively in chat.",
        "continuity_reference_protocol": "3-Case Reference Law (TH1 Same Time & Location -> Last-Frame Relay | TH2 Different Location/Time -> New Asset Anchor | TH3 Supernatural/Time-Travel -> Split Subject-Context Continuity)",
        "action_chase_model_routing": "Seedance (10.0s / 15.0s) for high-tension action, chase, pursuit, struggle, or combat scenes",
        "max_active_characters_per_10s_clip": preset.get("max_active_characters_per_10s_clip", 3),
        "max_characters_per_episode": preset.get("max_characters_per_episode", 6),
        "dynamic_cast_sizing": "Short Film (1 ep): 3-4 chars | Mini-Series (3-5 eps): 5-6 chars | Full Series (6-10+ eps): 7-9 chars | Mega Series (12-20+ eps): 10-14 chars",
        "subplot_architecture": "Triple-Helix Plot Weave (A-Plot 60% Primary Spine + B-Plot 25% Relationship/Thematic Mirror + C-Plot 15% Hidden Bomb/Satellite)",
        "minor_character_names": [],
        "max_words_per_line": preset.get("screenplay_constraints", {}).get("max_words_per_line", 18),
        "cadence_style": preset.get("screenplay_constraints", {}).get("cadence_style", ""),
        "hook_mandate": preset.get("screenplay_constraints", {}).get("hook_mandate", ""),
        "cliffhanger_mandate": preset.get("screenplay_constraints", {}).get("cliffhanger_mandate", ""),
        "dialect_standard": chosen_dialect,
        "kinship_ladder": {
            "from_scene": 1,
            "speakers": [],
            "banned_terms": g_cfg["banned"]
        },
        "address_standard": g_cfg["address"],
        "meal_terms": [],
        "bookish_terms": [
            "tuy nhiên", "do đó", "bởi vì", "mặt khác", "chúng tôi xin",
            "kính thưa", "tiến độ", "hạng mục", "nghiệm thu", "ngân sách",
            "phê duyệt", "triển khai", "báo cáo", "rất là", "chúng ta hãy"
        ]
    }

    with open(rules_file, "w", encoding="utf-8") as f:
        json.dump(project_rules, f, indent=2, ensure_ascii=False)

    print("=" * 80)
    print(f"[+] SUCCESS: Initialized project '{project_slug}' with Runbook [{slug}]")
    print(f"    Target directory: {target_dir}")
    print(f"    Config written  : {rules_file}")
    print(f"    Aspect Ratio    : {chosen_ar} (User-Governed)")
    print(f"    Visual Style    : [{chosen_style_slug}] {chosen_style_obj.get('name', '')}")
    print(f"    Episode Scenes  : {preset.get('default_episode_scenes')}")
    print(f"    Max Words/Line  : {preset.get('screenplay_constraints', {}).get('max_words_per_line')}")
    print("=" * 80)

def main():
    parser = argparse.ArgumentParser(description="Sven Production Runbook Manager")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    subparsers.add_parser("list", help="List all available production runbooks")

    inspect_p = subparsers.add_parser("inspect", help="Inspect detailed spec of a runbook")
    inspect_p.add_argument("slug", help="Runbook preset slug (e.g. microdrama-vertical)")

    init_p = subparsers.add_parser("init", help="Initialize a project with a runbook preset")
    init_p.add_argument("slug", help="Runbook preset slug")
    init_p.add_argument("project_slug", help="Target project slug (under output/)")
    init_p.add_argument("--aspect-ratio", dest="aspect_ratio", choices=["16:9", "9:16", "4:3", "1:1", "2.39:1"], help="Override aspect ratio according to user preference")
    init_p.add_argument("--visual-style", dest="visual_style", help="Visual style preset slug (default: 3d-semi-real; options: 3d-semi-real, pixar-3d, theatrical-live-action, unreal-game-cg, arcane-painterly, xianxia-3d-donghua)")
    init_p.add_argument("--dialect", dest="dialect", help="Override dialect/language standard for the project")
    init_p.add_argument("--force", action="store_true", help="Force overwrite existing project_rules.json")

    args = parser.parse_args()

    if args.command == "list":
        list_runbooks()
    elif args.command == "inspect":
        inspect_runbook(args.slug)
    elif args.command == "init":
        init_project(args.slug, args.project_slug, aspect_ratio=args.aspect_ratio, visual_style=args.visual_style, dialect=args.dialect, force=args.force)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

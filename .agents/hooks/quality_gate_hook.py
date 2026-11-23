#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sven Cinematic Universe — Quality Gate Hook (runtime-agnostic)
File: .agents/hooks/quality_gate_hook.py

Runs after a file write/edit and audits it:
  * setting.html  -> engine/setting_audit_suite.py
  * tap-N.html    -> engine/episode_audit_suite.py (tap files are banned by the Single-HTML law anyway)
  * ep-NN-script.md (saved Stage 3 script) -> engine/screenplay_audit.py (workflow.md §8.4)
  * ep-NN-scene-KK.md (saved Stage 4 scene prompt) -> engine/prompt_audit.py (workflow.md §9.3)
  * core docs (workflow.md, AGENT(S).md, .agents/*.md, engine/references/0*.md, engine/genres/*.md)
    -> engine/doc_range_check.py (JIT line ranges must stay inside the referenced files)
  * Roblox Law R-ANIM lint (ROBLOX_DIRECTOR.md §4) on Python/Lua files under output/ or the roblox kit:
    mocap retargeting (Mixamo/BVH/FBX/RoMixamo, retarget_mocap_to_r15, retarget_humanoid_action) is banned for Roblox films.

Input formats (stdin JSON):
  * Claude Code:  {"tool_name": "Write", "tool_input": {"file_path": ...}, "cwd": ...}
  * Antigravity:  {"toolCall": {"name": ..., "args": {"Path"|"TargetFile"|...}}}
  * or argv[1] = file path (manual run)

Output contract:
  * Claude Code: problems -> stderr + exit 2 (fed back to the model); clean -> exit 0, no output.
  * Antigravity: always prints {} on stdout (problems are logged to last_audit.log and echoed on stderr).
"""

import json
import os
import re
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_DIR = os.path.dirname(SCRIPT_DIR)
WORKSPACE_ROOT = os.path.dirname(AGENTS_DIR)
LOG_FILE = os.path.join(SCRIPT_DIR, "last_audit.log")

MOCAP_PAT = re.compile(r"retarget_mocap_to_r15\s*\(|retarget_humanoid_action\s*\(|\bMixamo\b|RoMixamo|assets[/\\]anims[/\\]|\.bvh\b", re.I)
LEGACY_FACE_PAT = re.compile(r"\bmake_faces_ugc_anime\b|\bmake_faces_v2\b", re.I)
# files that legitimately mention mocap or retired generators (the deprecated helpers themselves, docs explaining the ban, this hook)
MOCAP_ALLOW = ("blender_r15_hybrid.py", "blender_auto_director.py", "blender_roblox_kit.py", "retarget.py",
               "quality_gate_hook.py", "diag_retarget.py", "probe_clips.py", "make_faces_ugc_anime.py", "make_faces_v2.py")


def log(msg):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass


def read_input():
    """Return (target_file, runtime) where runtime is 'claude', 'antigravity' or 'manual'."""
    if len(sys.argv) > 1:
        return sys.argv[1], "manual"
    if sys.stdin.isatty():
        return None, "manual"
    try:
        raw = sys.stdin.read().strip()
        data = json.loads(raw) if raw else {}
    except Exception as e:
        log(f"[!] Error parsing hook input: {e}")
        return None, "manual"
    if "tool_input" in data or "tool_name" in data:
        ti = data.get("tool_input") or {}
        tr = data.get("tool_response") or {}
        path = ti.get("file_path") or ti.get("notebook_path") or tr.get("filePath")
        if path and not os.path.isabs(path):
            path = os.path.join(data.get("cwd") or WORKSPACE_ROOT, path)
        return path, "claude"
    args = (data.get("toolCall") or {}).get("args") or {}
    path = args.get("Path") or args.get("path") or args.get("TargetFile") or args.get("target_file")
    return path, "antigravity"


def run_audit(script_rel, target, label):
    script = os.path.join(WORKSPACE_ROOT, script_rel)
    if not os.path.exists(script):
        return None
    res = subprocess.run([sys.executable, script, target], capture_output=True, text=True, encoding="utf-8")
    log(f"[{label}] {target}\n{res.stdout}\n{res.stderr}")
    if res.returncode != 0:
        tail = "\n".join((res.stdout + "\n" + res.stderr).strip().splitlines()[-25:])
        return f"{label} FAILED for {target} (exit {res.returncode}):\n{tail}"
    return None


def lint_r_anim(target):
    name = os.path.basename(target)
    norm = target.replace("\\", "/").lower()
    if name in MOCAP_ALLOW or not name.lower().endswith((".py", ".lua")):
        return None
    if "/output/" not in norm and "roblox-director" not in norm:
        return None
    try:
        text = open(target, encoding="utf-8", errors="ignore").read()
    except OSError:
        return None
    hits = []
    face_hits = []
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if s.startswith(("#", "--")):
            continue
        if MOCAP_PAT.search(line):
            hits.append(f"  line {i}: {s[:120]}")
        if LEGACY_FACE_PAT.search(line):
            face_hits.append(f"  line {i}: {s[:120]}")
    msgs = []
    if hits:
        msgs.append("Law R-ANIM violation (ROBLOX_DIRECTOR.md section 4.1): mocap retargeting is banned for Roblox characters. "
                    "Use studio_kit/blender_roblox_anim.py (RobloxAnimator) and gate with render_pose_qa.\n" + "\n".join(hits[:10]))
    if face_hits:
        msgs.append("Law R-LOOK violation (ROBLOX_DIRECTOR.md section 4.1): legacy anime face generators (make_faces_ugc_anime / make_faces_v2) are retired. "
                    "Use studio_kit/make_faces_expressive.py (storybook_toon / cartoon / rubberhose) or kit.ensure_character_face_pack().\n" + "\n".join(face_hits[:10]))
    return "\n\n".join(msgs) if msgs else None


def lint_roblox_docs(target):
    """Roblox doc edits must keep every referenced file/function real (tools/doc_link_check.py)."""
    norm = target.replace("\\", "/").lower()
    if not norm.endswith(".md"):
        return None
    if "roblox-director" not in norm and not norm.endswith("roblox_director.md"):
        return None
    checker = os.path.join(AGENTS_DIR, "skills", "roblox-director", "tools", "doc_link_check.py")
    if not os.path.exists(checker):
        return None
    res = subprocess.run([sys.executable, checker, "--quiet"], capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        return "Roblox doc link check failed (fix or remove these references):\n" + res.stdout.strip()[:2000]
    return None


def lint_doc_ranges(target):
    """Core doc edits must keep every JIT line range valid (engine/doc_range_check.py)."""
    norm = target.replace("\\", "/").lower()
    if not norm.endswith(".md") or "/output/" in norm:
        return None
    core = ("/workflow.md", "/agent.md", "/agents.md", "/.agents/", "/engine/references/0", "/engine/genres/")
    if not any(k in norm for k in core):
        return None
    checker = os.path.join(WORKSPACE_ROOT, "engine", "doc_range_check.py")
    if not os.path.exists(checker):
        return None
    res = subprocess.run([sys.executable, checker, "--fix", "--quiet"], capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        return "Doc line-range check failed (update the StartLine/EndLine maps):\n" + res.stdout.strip()[:2000]
    return None


def main():
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    target, runtime = read_input()
    problems = []
    if target and os.path.exists(target):
        filename = os.path.basename(target).lower()
        if re.search(r"tap-\d+\.html$", filename):
            problems.append(run_audit(os.path.join("engine", "episode_audit_suite.py"), target, "Episode Audit Suite"))
        elif filename == "setting.html":
            problems.append(run_audit(os.path.join("engine", "setting_audit_suite.py"), target, "Setting Audit Suite"))
        elif re.search(r"ep-\d+-script\.md$", filename):
            problems.append(run_audit(os.path.join("engine", "screenplay_audit.py"), target, "Screenplay Audit"))
        elif re.search(r"ep-\d+-scene-\d+\.md$", filename):
            problems.append(run_audit(os.path.join("engine", "prompt_audit.py"), target, "Scene Prompt Audit"))
        problems.append(lint_r_anim(target))
        problems.append(lint_roblox_docs(target))
        problems.append(lint_doc_ranges(target))
    problems = [p for p in problems if p]

    if runtime == "antigravity":
        if problems:
            sys.stderr.write("\n\n".join(problems) + "\n")
        print(json.dumps({}))
        return 0
    if problems:
        sys.stderr.write("[Sven quality gate]\n" + "\n\n".join(problems) + "\n")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

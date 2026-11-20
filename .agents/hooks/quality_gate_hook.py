#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sven Cinematic Universe — Quality Gate Hook (runtime-agnostic)
File: .agents/hooks/quality_gate_hook.py

Runs after a file write/edit and audits it:
  * setting.html  -> engine/setting_audit_suite.py
  * tap-N.html    -> engine/episode_audit_suite.py (tap files are banned by the Single-HTML law anyway)
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
# files that legitimately mention mocap (the deprecated helpers themselves, docs explaining the ban, this hook)
MOCAP_ALLOW = ("blender_r15_hybrid.py", "blender_auto_director.py", "blender_roblox_kit.py", "retarget.py",
               "quality_gate_hook.py", "diag_retarget.py", "probe_clips.py")


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
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if s.startswith(("#", "--")):
            continue
        if MOCAP_PAT.search(line):
            hits.append(f"  line {i}: {s[:120]}")
    if not hits:
        return None
    return ("Law R-ANIM violation (ROBLOX_DIRECTOR.md section 4.1): mocap retargeting is banned for Roblox characters. "
            "Use studio_kit/blender_roblox_anim.py (RobloxAnimator) and gate with render_pose_qa.\n" + "\n".join(hits[:10]))


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
        problems.append(lint_r_anim(target))
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

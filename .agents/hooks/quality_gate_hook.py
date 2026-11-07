#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sven Cinematic Universe — Antigravity Quality Gate Hook
File: .agents/hooks/quality_gate_hook.py
Purpose: Automatically audits episode and setting HTML files upon generation or edit.
"""

import sys
import os
import json
import subprocess
import re

# Determine workspace root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_DIR = os.path.dirname(SCRIPT_DIR)
WORKSPACE_ROOT = os.path.dirname(AGENTS_DIR)

LOG_FILE = os.path.join(SCRIPT_DIR, "last_audit.log")

def log(msg):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass

def main():
    # Read stdin
    target_file = None
    tool_name = None

    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    elif not sys.stdin.isatty():
        try:
            raw_input = sys.stdin.read().strip()
            if raw_input:
                data = json.loads(raw_input)
                tool_call = data.get("toolCall", {})
                tool_name = tool_call.get("name")
                args = tool_call.get("args", {})
                target_file = (
                    args.get("Path")
                    or args.get("path")
                    or args.get("TargetFile")
                    or args.get("target_file")
                )
        except Exception as e:
            log(f"[!] Error parsing hook input: {e}")

    if target_file and os.path.exists(target_file):
        norm_path = os.path.normpath(target_file)
        filename = os.path.basename(norm_path).lower()

        # Check for tap-X.html
        if re.search(r"tap-\d+\.html$", filename):
            audit_script = os.path.join(WORKSPACE_ROOT, "engine", "episode_audit_suite.py")
            if os.path.exists(audit_script):
                log(f"[*] Triggering Episode Audit Suite for: {norm_path}")
                res = subprocess.run([sys.executable, audit_script, norm_path], capture_output=True, text=True, encoding="utf-8")
                log(f"[Episode Audit Output]\n{res.stdout}\n{res.stderr}")

        # Check for setting.html
        elif filename == "setting.html":
            audit_script = os.path.join(WORKSPACE_ROOT, "engine", "setting_audit_suite.py")
            if os.path.exists(audit_script):
                log(f"[*] Triggering Setting Audit Suite for: {norm_path}")
                res = subprocess.run([sys.executable, audit_script, norm_path], capture_output=True, text=True, encoding="utf-8")
                log(f"[Setting Audit Output]\n{res.stdout}\n{res.stderr}")

    # Antigravity PostToolUse contract expects an empty JSON object on stdout
    print(json.dumps({}))

if __name__ == "__main__":
    main()

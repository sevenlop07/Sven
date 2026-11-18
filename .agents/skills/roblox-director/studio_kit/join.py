#!/usr/bin/env python3
"""
join.py — Backward-compatible wrapper forwarding to tools/compile_video.py.
Replaces the legacy monster-test hardcoded script.

Usage:
  python join.py --project-dir output/<slug> --voice voice.mp3 [--shots srt_shots.json] [--frames-dir frames] [--subs caps.ass] [--aspect 9:16|16:9] [--out final.mp4]
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
COMPILE = os.path.normpath(os.path.join(HERE, "..", "tools", "compile_video.py"))
sys.exit(subprocess.call([sys.executable, COMPILE] + sys.argv[1:]))

#!/usr/bin/env python3
r"""
run_roblox_blender.py — Host-side Blender 5.3 Runner + Two-Way Live %TEMP% Sync for @RobloxDirector.
1. Pre-syncs existing rendered frames from output/<slug>/shots into %TEMP%/sven_blender_<slug>/shots so Blender
   automatically skips already-completed frames on resume.
2. Streams live Blender progress output in real time (zero frozen terminal).
3. Background-syncs newly rendered frames from %TEMP%/sven_blender_<slug>/ back to output/<slug>/ every 15s
   and performs a final complete sync on exit so progress is never lost.

Usage:
  python run_roblox_blender.py --slug my_film <script.py> [-- script_args...]
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
BLENDER_CORE_SCRIPTS = os.path.normpath(os.path.join(HERE, "..", "..", "blender-core", "scripts"))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
if BLENDER_CORE_SCRIPTS not in sys.path:
    sys.path.insert(0, BLENDER_CORE_SCRIPTS)

from run_in_blender import find_blender


def _sync_dirs(src: str, dst: str):
    if os.path.isdir(src):
        os.makedirs(dst, exist_ok=True)
        try:
            shutil.copytree(src, dst, dirs_exist_ok=True)
        except Exception:
            pass


def main():
    a = sys.argv[1:]
    rest = []
    if "--" in a:
        i = a.index("--")
        a, rest = a[:i], a[i + 1:]

    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True, help="Project folder name under output/<slug>")
    ap.add_argument("--blend", default="")
    ap.add_argument("script")
    args = ap.parse_args(a)

    exe = find_blender()
    if not exe:
        print("[ERROR] Blender 5.3 not found; set BLENDER_EXE environment variable.", file=sys.stderr)
        sys.exit(2)

    stage_dir = os.path.join(tempfile.gettempdir(), f"sven_blender_{args.slug}")
    out_dir = os.path.join(REPO_ROOT, "output", args.slug)
    os.makedirs(stage_dir, exist_ok=True)
    os.environ["ROBLOX_STAGE_DIR"] = stage_dir

    # 1. Pre-sync existing shots/frames from output/<slug> -> %TEMP%/sven_blender_<slug>
    for sub in ("shots", "frames"):
        if os.path.isdir(os.path.join(out_dir, sub)):
            _sync_dirs(os.path.join(out_dir, sub), os.path.join(stage_dir, sub))

    cmd = [exe, "-b"]
    if args.blend:
        cmd.append(os.path.abspath(args.blend))
    else:
        cmd.append("--factory-startup")
    cmd += ["--python-exit-code", "1", "-P", os.path.abspath(args.script)]
    if rest:
        cmd += ["--"] + rest

    stop_evt = threading.Event()

    def _bg_sync_worker():
        while not stop_evt.wait(15.0):
            _sync_dirs(stage_dir, out_dir)

    sync_thread = threading.Thread(target=_bg_sync_worker, daemon=True)
    sync_thread.start()

    noise_prefixes = ("Blender ", "Read prefs", "Color management", "00:")
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", bufsize=1)
    for line in proc.stdout:
        s = line.rstrip()
        if not s:
            continue
        if s.startswith("Fra:") and "Mem:" in s:
            continue
        if any(s.startswith(p) for p in noise_prefixes) and "ERROR" not in s and "Read blend" not in s:
            continue
        print(s, flush=True)

    ret = proc.wait()
    stop_evt.set()
    sync_thread.join(timeout=2.0)

    if os.path.isdir(stage_dir):
        _sync_dirs(stage_dir, out_dir)
        print(f"[run_roblox_blender] Synced {stage_dir} -> {out_dir}", flush=True)
    sys.exit(ret)


if __name__ == "__main__":
    main()

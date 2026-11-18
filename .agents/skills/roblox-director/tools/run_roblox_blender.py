#!/usr/bin/env python3
"""
run_roblox_blender.py — Host-side Blender 5.3 Runner + Automatic %TEMP% Sync for @RobloxDirector.
Runs any Blender script via blender-core/scripts/run_in_blender.py and automatically copies
staged outputs from %TEMP%/sven_blender_<slug>/ into output/<slug>/ so blender.exe never hits
Windows OpenImageIO directory write restrictions on D:\.

Usage:
  python run_roblox_blender.py --slug my_film <script.py> [-- script_args...]
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
RUN_IN_BLENDER = os.path.normpath(os.path.join(HERE, "..", "..", "blender-core", "scripts", "run_in_blender.py"))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))


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

    cmd = [sys.executable, RUN_IN_BLENDER]
    if args.blend:
        cmd += ["--blend", args.blend]
    cmd.append(os.path.abspath(args.script))
    if rest:
        cmd += ["--"] + rest

    proc = subprocess.run(cmd)
    stage_dir = os.path.join(tempfile.gettempdir(), f"sven_blender_{args.slug}")
    out_dir = os.path.join(REPO_ROOT, "output", args.slug)
    if os.path.isdir(stage_dir):
        os.makedirs(out_dir, exist_ok=True)
        shutil.copytree(stage_dir, out_dir, dirs_exist_ok=True)
        print(f"[run_roblox_blender] Synced {stage_dir} -> {out_dir}")
    sys.exit(proc.returncode)


if __name__ == "__main__":
    main()

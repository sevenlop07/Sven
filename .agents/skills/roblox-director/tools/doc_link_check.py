#!/usr/bin/env python3
"""
doc_link_check.py — verify that the Roblox Director docs only reference things that exist.

Checks every file name (*.py *.lua *.md *.mjs *.json *.glb *.fbx *.ipynb) and every kit/rba/hyb/env/MT function
mentioned in .agents/ROBLOX_DIRECTOR.md, .agents/rules/sven-bootstrap.md, .claude/skills|agents roblox files and
.agents/skills/roblox-director/**/*.md against the repository.

  python .agents/skills/roblox-director/tools/doc_link_check.py            # report, exit 1 if anything is missing
  python .agents/skills/roblox-director/tools/doc_link_check.py --quiet    # only print problems

Run it after editing any Roblox doc (the quality-gate hook runs it automatically on .md edits under roblox-director).
"""
import glob
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
SKILL = os.path.join(ROOT, ".agents", "skills", "roblox-director")

# names produced at run time inside output/<slug>/ (or user-supplied), not files of the repo
RUNTIME_OUTPUTS = {
    "audio.json", "shots.json", "words.json", "words_planned.json", "srt_shots.json", "director_plan.json",
    "cloth_ids.json", "fov.json", "script-beats.json", "audit_report.json", "story.txt", "voice.mp3",
    "scene_built.blend", "qa.md", "notes.md", "shotlist.md", "sheet.md", "rotation.md", "final.mp4",
}
FILE_RE = re.compile(r"(?<![\w.<-])([\w\-]+\.(?:py|lua|md|mjs|json|glb|fbx|ipynb))\b(?!>)")
FN_RE = re.compile(r"\b(kit|rba|hyb|env)\.([A-Za-z_]\w*)\s*\(")
MT_RE = re.compile(r"\bMT\.([A-Za-z_]\w*)")


def docs():
    out = [os.path.join(ROOT, ".agents", "ROBLOX_DIRECTOR.md"), os.path.join(ROOT, ".agents", "rules", "sven-bootstrap.md")]
    out += glob.glob(os.path.join(SKILL, "**", "*.md"), recursive=True)
    out += glob.glob(os.path.join(ROOT, ".claude", "skills", "roblox-director", "*.md"))
    out += glob.glob(os.path.join(ROOT, ".claude", "agents", "roblox-director.md"))
    return [p for p in out if os.path.exists(p)]


def repo_files():
    names = set()
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__")]
        for f in files:
            names.add(f.lower())
    return names


def code_symbols():
    py, lua = "", ""
    for f in glob.glob(os.path.join(SKILL, "studio_kit", "*.py")) + glob.glob(os.path.join(SKILL, "tools", "*.py")):
        py += open(f, encoding="utf-8", errors="ignore").read()
    for f in glob.glob(os.path.join(SKILL, "studio_kit", "*.lua")):
        lua += open(f, encoding="utf-8", errors="ignore").read()
    return py, lua


def main():
    quiet = "--quiet" in sys.argv
    names = repo_files()
    py, lua = code_symbols()
    problems = []
    for d in docs():
        rel = os.path.relpath(d, ROOT)
        text = open(d, encoding="utf-8", errors="ignore").read()
        for i, line in enumerate(text.splitlines(), 1):
            for m in FILE_RE.findall(line):
                low = m.lower()
                if low in names or low in RUNTIME_OUTPUTS or low.startswith(("<", "your")):
                    continue
                problems.append(f"{rel}:{i}: missing file '{m}'")
            for mod, fn in FN_RE.findall(line):
                if not re.search(r"\b(?:def|class) " + re.escape(fn) + r"\b", py) and not re.search(r"\b" + re.escape(fn) + r"\s*=", py):
                    problems.append(f"{rel}:{i}: unknown function {mod}.{fn}()")
            for fn in MT_RE.findall(line):
                if "MT." + fn not in lua:
                    problems.append(f"{rel}:{i}: unknown Luau helper MT.{fn}")
    for p in problems:
        print(p)
    if not quiet:
        print(f"[doc_link_check] {len(docs())} docs scanned, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

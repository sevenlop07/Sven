#!/usr/bin/env python3
"""
doc_range_check.py — keep the JIT line-range maps honest.

The core docs tell agents to read reference files by line range (`StartLine: a, EndLine: b`,
`(L390–720)`, `read_file(Path=..., StartLine=1, EndLine=162)`). When a file grows or shrinks, those ranges
silently point at the wrong section. This script finds every range that is attached to a file name and checks:

  1. the referenced file exists in the repo;
  2. EndLine does not exceed the file's current length;
  3. (anchored ranges) when a range is written as `(L361–425 §5)` or `(StartLine: 361, EndLine: 425 · §5)`,
     the line at StartLine must be a markdown heading that contains the anchor text (`§5`).

  python engine/doc_range_check.py                 # check the core docs, exit 1 on problems
  python engine/doc_range_check.py --quiet         # print problems only
  python engine/doc_range_check.py --map workflow.md   # print the headings of a file with line numbers

Run it after editing workflow.md, AGENT.md, AGENTS.md, .agents/*.md or any reference file.
"""
import glob
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

FILE_RE = re.compile(r"([\w\-./]+\.md)\b")
RANGE_RES = [
    re.compile(r"StartLine\s*[:=]\s*(\d+)\s*,\s*EndLine\s*[:=]\s*(\d+)(?:\s*[·—-]\s*(§[\w.]+))?"),
    re.compile(r"\bL(\d+)\s*[–-]\s*(\d+)(?:\s+(§[\w.]+))?"),
]


def core_docs():
    pats = ["AGENTS.md", "AGENT.md", "CLAUDE.md", "workflow.md", ".agents/*.md", ".agents/rules/*.md",
            ".agents/skills/*/SKILL.md", ".claude/skills/*/SKILL.md", ".claude/agents/*.md",
            "engine/genres/*.md", "engine/references/0*.md"]
    out = []
    for p in pats:
        out += glob.glob(os.path.join(ROOT, p))
    return sorted({p for p in out if "blender-" not in p})


def index_md():
    idx = {}
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__", "output")]
        for f in files:
            if f.endswith(".md"):
                idx.setdefault(f.lower(), []).append(os.path.join(root, f))
    return idx


def resolve(name, idx):
    rel = re.sub(r"^.*?/project/sven/", "", name, flags=re.I).lstrip("/")
    cand = os.path.join(ROOT, rel)
    if os.path.exists(cand):
        return cand
    hits = idx.get(os.path.basename(rel).lower(), [])
    if "/" in rel:  # partial path such as combat-director/SKILL.md
        tail = rel.replace("/", os.sep).lower()
        hits = [h for h in hits if h.lower().endswith(tail)]
    return hits[0] if len(hits) == 1 else None  # ambiguous or unknown -> not checked


_cache = {}


def lines_of(path):
    if path not in _cache:
        _cache[path] = open(path, encoding="utf-8", errors="ignore").read().split("\n")
    return _cache[path]


def check():
    idx = index_md()
    problems = []
    for doc in core_docs():
        rel = os.path.relpath(doc, ROOT)
        for i, line in enumerate(lines_of(doc), 1):
            files = [(m.start(), m.group(1)) for m in FILE_RE.finditer(line)]
            if not files:
                continue
            for rx in RANGE_RES:
                for m in rx.finditer(line):
                    prev = [f for pos, f in files if pos < m.start()]
                    if not prev:
                        continue
                    target = resolve(prev[-1], idx)
                    a, b, anchor = int(m.group(1)), int(m.group(2)), m.group(3)
                    if target is None:
                        continue
                    n = len(lines_of(target))
                    tname = os.path.relpath(target, ROOT)
                    if a > b:
                        problems.append(f"{rel}:{i}: inverted range L{a}-{b} for {tname}")
                    if b > n + 1:
                        problems.append(f"{rel}:{i}: range L{a}-{b} exceeds {tname} ({n} lines)")
                    if anchor:
                        head = lines_of(target)[a - 1] if a - 1 < n else ""
                        if not head.lstrip().startswith("#") or anchor not in head:
                            problems.append(f"{rel}:{i}: anchor {anchor} not found at {tname}:L{a} (found: {head[:70]!r})")
    return problems


def print_map(name):
    target = resolve(name, index_md())
    if not target:
        print(f"unknown file {name}")
        return 1
    L = lines_of(target)
    for i, line in enumerate(L, 1):
        if re.match(r"^#{1,3} ", line):
            print(f"{i:>5}  {line[:110]}")
    print(f"{len(L):>5}  <EOF>")
    return 0


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if "--map" in sys.argv:
        return print_map(sys.argv[sys.argv.index("--map") + 1])
    problems = check()
    for p in problems:
        print(p)
    if "--quiet" not in sys.argv:
        print(f"[doc_range_check] {len(core_docs())} docs scanned, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

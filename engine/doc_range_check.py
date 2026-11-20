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
  python engine/doc_range_check.py --fix               # move anchored ranges to where their heading now is

Run it after editing workflow.md, AGENT.md, AGENTS.md, .agents/*.md or any reference file.
"""
import glob
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

FILE_RE = re.compile(r"([\w\-./]+\.md)\b")
RANGE_RES = [
    re.compile(r"StartLine\s*[:=]\s*(\d+)\s*,\s*EndLine\s*[:=]\s*(\d+)(?:\s*[·—-]\s*(§[\w.]+(?:[–-]§[\w.]+)?))?"),
    re.compile(r"\bL(\d+)\s*[–-]\s*(\d+)(?:\s+(§[\w.]+(?:[–-]§[\w.]+)?))?"),
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


def _anchor_rx(anchor):
    return re.compile(re.escape(anchor) + r"(?![\w.])")


def _find_heading(lines, anchor):
    rx = _anchor_rx(anchor)
    for k, l in enumerate(lines):
        if l.lstrip().startswith("#") and rx.search(l):
            return k + 1
    return None


def _section_end(lines, start):
    """Last line of the section that begins at heading line `start` (1-based): the line before the next heading of the
    same or higher level, minus trailing blank lines and `---` separators."""
    level = len(lines[start - 1]) - len(lines[start - 1].lstrip("#"))
    end = len(lines)
    for k in range(start, len(lines)):
        s = lines[k]
        if s.startswith("#"):
            lv = len(s) - len(s.lstrip("#"))
            if lv <= level:
                end = k
                break
    while end > start and lines[end - 1].strip() in ("", "---"):
        end -= 1
    return end


def check(fix=False):
    idx = index_md()
    problems, fixes = [], {}
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
                    tl = lines_of(target)
                    n = len(tl)
                    tname = os.path.relpath(target, ROOT)
                    if anchor:
                        first, _, last = re.sub(r"[–-]§", "|§", anchor).partition("|")
                        new_a = _find_heading(tl, first)
                        last_a = _find_heading(tl, last) if last else new_a
                        new_b = _section_end(tl, last_a) if (new_a and last_a) else None
                        if new_a is None:
                            problems.append(f"{rel}:{i}: anchor {anchor} has no heading in {tname}")
                        elif (a, b) != (new_a, new_b):
                            if fix:
                                fixes.setdefault((doc, i), []).append((m.start(1), m.end(1), str(new_a)))
                                fixes[(doc, i)].append((m.start(2), m.end(2), str(new_b)))
                                a, b = new_a, new_b
                            else:
                                problems.append(f"{rel}:{i}: anchored range L{a}-{b} {anchor} is now L{new_a}-{new_b} in {tname} — run with --fix")
                    if a > b:
                        problems.append(f"{rel}:{i}: inverted range L{a}-{b} for {tname}")
                    if b > n + 1:
                        problems.append(f"{rel}:{i}: range L{a}-{b} exceeds {tname} ({n} lines)")
    if fix and fixes:
        bydoc = {}
        for (doc, i), spans in fixes.items():
            bydoc.setdefault(doc, {})[i] = spans
        for doc, linemap in bydoc.items():
            L = open(doc, encoding="utf-8").read().split("\n")
            for i, spans in linemap.items():
                ln = L[i - 1]
                for st, en, val in sorted(spans, reverse=True):
                    ln = ln[:st] + val + ln[en:]
                L[i - 1] = ln
            open(doc, "w", encoding="utf-8", newline="").write("\n".join(L))
            _cache.pop(doc, None)
            print(f"[doc_range_check] fixed {len(linemap)} line(s) in {os.path.relpath(doc, ROOT)}")
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
    problems = check(fix="--fix" in sys.argv)
    for p in problems:
        print(p)
    if "--quiet" not in sys.argv:
        print(f"[doc_range_check] {len(core_docs())} docs scanned, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

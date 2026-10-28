"""Re-validate tap-1.html through the root compiler (workflow.md §9.7, revision mode).

Revision patches (scripts/revisions/*.py) edit tap-1.html scene by scene with asserted replacements.
This script then passes the result through engine/prompt_compiler.compile_and_validate_episode(),
which rewrites the file and runs the full episode audit; any failing gate raises and blocks delivery.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENGINE = os.path.abspath(os.path.join(ROOT, "..", "..", "engine"))
sys.path.insert(0, ENGINE)
from prompt_compiler import compile_and_validate_episode  # noqa: E402

TAP = os.path.join(ROOT, "tap-1.html")
# Universal-newline read: the compiler writes in text mode, so CRLF is restored without doubling.
with open(TAP, encoding="utf-8") as f:
    content = f.read()
compile_and_validate_episode(content, TAP)

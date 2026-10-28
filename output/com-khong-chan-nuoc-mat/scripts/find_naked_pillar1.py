import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('engine/references/1-narrative-screenplay-architecture.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

rx = re.compile(r'^\s*([A-Za-z_][\w]*)\s*[:：]\s*[“"]')
for i, l in enumerate(lines):
    if rx.search(l):
        print(f"Line {i+1}: {l.strip()[:100]}")

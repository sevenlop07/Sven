import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    for w in ['be_tin', 'bé tin', 'baby', 'infant', 'newborn']:
        if re.search(r'\b' + w + r'\b', line, re.I):
            print(f"L{idx} [{w}]: {line.strip()[:100]}")
    if re.search(r'\bbé\b', line, re.I):
        print(f"L{idx} [bé]: {line.strip()[:100]}")

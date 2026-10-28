import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

forbidden = ['baby', 'kid', 'infant', 'newborn', 'be_tin']
for idx, line in enumerate(lines, 1):
    for word in forbidden:
        if re.search(r'\b' + word + r'\b', line, re.I):
            print(f"L{idx} [{word}]: {line.strip()[:100]}")
    if re.search(r'\bbé\b', line, re.I):
        print(f"L{idx} [bé]: {line.strip()[:100]}")

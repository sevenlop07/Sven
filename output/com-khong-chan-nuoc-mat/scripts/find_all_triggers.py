import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

triggers = ['bruise', 'bruised', 'bruises', 'bầm', 'dập', 'collapse', 'collapsing', 'faint', 'unconscious', 'clatter', 'clattering', 'crash', 'crashing']
pattern = re.compile(r'\b(' + '|'.join(triggers) + r')\b', re.IGNORECASE)

for i, line in enumerate(lines, 1):
    m = pattern.findall(line)
    if m:
        print(f"Line {i} ({set(m)}): {line.strip()[:100]}")

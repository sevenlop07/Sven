import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

triggers = ['bầm', 'dập', 'té', 'ngất', 'collapse', 'bruised', 'bruise']
pattern = re.compile(r'\b(' + '|'.join(triggers) + r')\b', re.IGNORECASE)

for i, line in enumerate(lines, 1):
    m = pattern.findall(line)
    if m:
        print(f"Line {i} ({set(m)}): {line.strip()[:100]}")

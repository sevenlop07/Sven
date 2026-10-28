import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'.{0,40}(?:be_tin|bé tin|baby|kid|infant|newborn).{0,40}', text, re.I)
print(f"Total matches in setting.html: {len(matches)}")
for m in matches[:15]:
    print(" ", m.strip().replace(chr(10), ' '))

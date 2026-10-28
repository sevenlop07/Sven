import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('engine/references/3-cinematography-3d-staging.md', 'r', encoding='utf-8') as f:
    text = f.read()

print("Occurrences in 3-cinematography-3d-staging.md:")
for m in re.finditer(r'(Track\s+[AB]|single-shot|multi-shot|cú máy đơn|cắt cảnh)', text, re.I):
    idx = m.start()
    print(f"[{m.group(0)}] Line {text[:idx].count(chr(10))+1}: {text[max(0, idx-50):min(len(text), idx+100)].replace(chr(10), ' ')}")

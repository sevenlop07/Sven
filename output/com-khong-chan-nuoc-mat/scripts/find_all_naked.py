import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

ref_dir = 'engine/references'
for fn in sorted(os.listdir(ref_dir)):
    if not fn.endswith('.md'):
        continue
    with open(os.path.join(ref_dir, fn), 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, l in enumerate(lines):
        m = re.search(r'^\s*([a-zA-Z0-9_\-]+)\s*[:：]\s*[“"]', l)
        if m:
            print(f'{fn}:{idx+1}: {l.strip()[:100]}')

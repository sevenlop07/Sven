import re
import os
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"output/com-khong-chan-nuoc-mat/tap-1.html", "r", encoding="utf-8") as f:
    text = f.read()

scenes = re.findall(r'<div class="scene-card" id="(s-\d{2})".*?<strong[^>]*>(.*?)</strong>', text, re.DOTALL)
for s, title in scenes:
    print(f"{s}: {title.strip()}")

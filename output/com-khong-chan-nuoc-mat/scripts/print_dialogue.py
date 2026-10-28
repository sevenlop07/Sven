import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/tap-1.html', encoding='utf-8') as f:
    text = f.read()

scenes = re.findall(r'<div class="scene-card" id="(s-\d+)">(.*?)(?=<div class="scene-card" id="s-\d+"|$)', text, re.S)

for s_id, s_content in scenes:
    print(f"=== {s_id} ===")
    dia_items = re.findall(r'<span class="dia-speaker">(.*?)</span>\s*<span class="dia-spoken-quote">(.*?)</span>', s_content)
    for spk, q in dia_items:
        print(f"  {spk.strip()}: {q.strip()}")

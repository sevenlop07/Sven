import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

scenes = re.findall(r'(<div[^>]*class="scene-card"[^>]*id="((?:s|sc)-\d{2})".*?)(?=<div[^>]*class="scene-card"|<div class="interactive-dock"|$)', html, re.DOTALL)

for s_block, s_id in scenes:
    if s_id in ['s-01', 's-04', 's-05', 's-08', 's-09']:
        print(f"\n==================== FULL {s_id} ====================")
        # print dialogue block
        dia_m = re.search(r'(<div[^>]*class="dialogue-box".*?</div>\s*</div>)', s_block, re.DOTALL)
        if dia_m:
            print("--- DIA BLOCK ---")
            print(dia_m.group(1)[:500])
        # print prompt
        p_m = re.search(r'<pre[^>]*id="p-\d{2}"[^>]*>(.*?)</pre>', s_block, re.DOTALL)
        if p_m:
            print("--- PROMPT ---")
            print(p_m.group(1))

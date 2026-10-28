import sys
import os
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

scenes = re.findall(r'(<div[^>]*class="scene-card"[^>]*id="((?:s|sc)-\d{2})".*?)(?=<div[^>]*class="scene-card"|<div class="interactive-dock"|$)', html, re.DOTALL)
print(f"Total scene cards found: {len(scenes)}")

for s_block, s_id in scenes:
    card_quotes = re.findall(r'class="[^"]*dia-(?:en|spoken)-quote[^"]*"[^>]*>(.*?)</span>', s_block)
    prompt_match = re.search(r'<pre[^>]*id="p-\d{2}"[^>]*>(.*?)</pre>', s_block, re.DOTALL)
    
    prompt_text = prompt_match.group(1).strip() if prompt_match else "NO PROMPT"
    spoken_in_p = re.findall(r'^\s*([A-Za-z_][\w]*)(?:\s+(?:says|speaks|whispers|snaps|mutters|cries|replies|pleads|retorts))?\s*[:：]\s*[“"]\s*(.+?)\s*[”"]\s*[\(（]\s*(Voice of[^\)）]*)[\)）]', prompt_text, re.MULTILINE | re.IGNORECASE)
    
    print(f"\n==================== [{s_id}] ====================")
    print(f"Card quotes count: {len(card_quotes)}")
    for q in card_quotes:
        clean_q = re.sub(r'<[^>]+>', '', q).strip()
        print(f"  CARD: \"{clean_q}\" ({len(clean_q.split())} words)")
    print(f"Prompt spoken lines: {len(spoken_in_p)}")
    for char, line, voice in spoken_in_p:
        print(f"  PROMPT: {char} : \"{line}\" ({len(line.split())} words)")

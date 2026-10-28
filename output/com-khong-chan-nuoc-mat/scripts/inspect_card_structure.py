import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

s1_match = re.search(r'(<div[^>]*class="scene-card"[^>]*id="s-01".*?)(?=<div[^>]*class="scene-card"|<div class="interactive-dock"|$)', html, re.DOTALL)
if s1_match:
    s1_text = s1_match.group(1)
    # print headers and id tags inside s1
    ids = re.findall(r'id="([^"]+)"', s1_text)
    print("IDs in s-01:", ids)
    classes = set(re.findall(r'class="([^"]+)"', s1_text))
    print("Classes in s-01:", sorted(list(classes))[:15])

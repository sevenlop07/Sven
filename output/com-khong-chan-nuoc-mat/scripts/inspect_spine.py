import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

spine_m = re.search(r'(<div[^>]*class="story-spine-card".*?</div>\s*</div>)', html, re.DOTALL)
if spine_m:
    print(spine_m.group(1)[:2500])
else:
    # check for spine or story summary
    m = re.search(r'id="story-spine"(.*?)</div>', html, re.DOTALL)
    if m:
        print(m.group(1)[:2000])
    else:
        print("Story spine card not found by exact class, searching...")
        m2 = re.findall(r'<div class="[^"]*spine[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)
        print(f"Spine matches: {len(m2)}")

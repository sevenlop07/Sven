import re

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

prompts = re.findall(r'<pre[^>]*id="(p-\d{2})"[^>]*>(.*?)</pre>', html, re.DOTALL)
for p_id, p_text in prompts:
    for word in ['baby', 'kid', 'infant', 'newborn', 'be_tin', 'bé tin']:
        m = re.findall(r'\b' + word + r'\b', p_text, re.I)
        if m:
            print(f"[{p_id}] Found forbidden word '{word}': {len(m)} times")
    if re.search(r'\bbé\b', p_text, re.I):
        print(f"[{p_id}] Found 'bé'")

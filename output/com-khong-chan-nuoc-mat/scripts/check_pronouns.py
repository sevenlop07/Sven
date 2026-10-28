import re

pronoun_rx = re.compile(r'\b(he|she|his|her|him|they|their|them|herself|himself|themselves)\b', re.IGNORECASE)

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

prompts = re.findall(r'<pre[^>]*id="(p-\d{2})"[^>]*>(.*?)</pre>', html, re.DOTALL)
for p_id, p_text in prompts:
    # strip dialogue lines
    prose = re.sub(r'^\s*[A-Za-z_][\w]*(?:\s+(?:says|speaks|whispers|snaps|mutters|cries))?\s*[:：]\s*[“"].*?[”"]\s*[\(（].*?[\)）]', '', p_text, flags=re.MULTILINE | re.DOTALL)
    prose = re.sub(r'Do not generate.*', '', prose, flags=re.DOTALL)
    matches = pronoun_rx.findall(prose)
    if matches:
        print(f"{p_id}: {matches}")
        for line in prose.split('\n'):
            m = pronoun_rx.findall(line)
            if m:
                print(f"  Line: {line.strip()}")

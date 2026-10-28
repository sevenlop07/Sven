import re
import os
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"output/com-khong-chan-nuoc-mat/tap-1.html", "r", encoding="utf-8") as f:
    text = f.read()

for s_id in ['s-02', 's-03', 's-05', 's-08', 's-10']:
    p_id = 'p-' + s_id[-2:]
    m_p = re.search(r'id="' + p_id + r'"[^>]*>(.*?)</pre>', text, re.DOTALL)
    if m_p:
        lines = re.findall(r'^\s*([A-Za-z_][\w]*\s+(?:says|speaks|whispers|snaps|mutters|cries|replies|pleads|retorts)\s*[:：]\s*[“"]\s*(.+?)\s*[”"])', m_p.group(1), re.MULTILINE)
        print(f"=== {s_id} ===")
        for full, quote in lines:
            words = [t for t in quote.split() if re.search(r'\w', t)]
            sec = len(words) / 4.5 + 0.3
            print(f"  {full} [{len(words)} words, ~{sec:.2f}s]")

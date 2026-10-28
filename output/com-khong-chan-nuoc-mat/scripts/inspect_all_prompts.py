import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

prompts = re.findall(r'<pre[^>]*id="(p-\d{2})"[^>]*>(.*?)</pre>', html, re.DOTALL)
for p_id, p_text in prompts:
    print(f"=== {p_id} ===")
    subj_m = re.search(r'\[subject\]:(.*?)(?=\n\n\[Pro)', p_text, re.DOTALL | re.IGNORECASE)
    prop_m = re.search(r'\[Pro(?:p)?\]\s*:(.*?)(?=\n\nDiegetic|\nDiegetic)', p_text, re.DOTALL | re.IGNORECASE)
    phases = re.findall(r'(\[\d{2}:\d{2}[–\-]\d{2}:\d{2}\].*?)(?=\[\d{2}:\d{2}[–\-]\d{2}:\d{2}\]|Continuous fluid motion|\Z)', p_text, re.DOTALL)
    print("SUBJ:", subj_m.group(1).strip() if subj_m else "NONE")
    print("PROP:", prop_m.group(1).strip() if prop_m else "NONE")
    print(f"PHASES ({len(phases)}):")
    for ph in phases:
        print("  - " + ph.strip()[:160] + "...")
    print("\n")

import re

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

scenes = re.findall(r'<div[^>]*class="scene-card"[^>]*id="((?:s|sc)-\d{2})".*?<pre[^>]*id="(p-\d{2})"[^>]*>(.*?)</pre>', html, re.DOTALL)
print(f"Total scenes: {len(scenes)}")

for s_id, p_id, p_text in scenes:
    subject_m = re.search(r'\[subject\]:(.*?)(?=\n\n\[)', p_text, re.DOTALL)
    subj = subject_m.group(1).strip() if subject_m else "NONE"
    has_tin_in_subj = "tin" in subj.lower()
    has_tin_in_text = "tin" in p_text.lower()
    print(f"\n[{s_id} | {p_id}]")
    print(f"  Subject: {subj.replace(chr(10), ' ')}")
    print(f"  'tin' in subject: {has_tin_in_subj} | 'tin' in prompt: {has_tin_in_text}")

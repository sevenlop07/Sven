import re

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

prompts = re.findall(r'<pre[^>]*id="(p-\d{2})"[^>]*>(.*?)</pre>', html, re.DOTALL)

for p_id, p_text in prompts:
    if p_id in [f'p-0{i}' for i in range(1, 10)]:
        print(f"\n==================== {p_id} ====================")
        subj_m = re.search(r'\[subject\]:(.*?)(?=\n\n\[PROP\])', p_text, re.DOTALL)
        if subj_m:
            print("[subject]:")
            print(subj_m.group(1).strip())
        # print lines mentioning crib or bed
        crib_lines = [l.strip() for l in p_text.split('\n') if 'crib' in l.lower() or 'noi_go' in l.lower()]
        print("Crib/Noi_go mentions:")
        for cl in crib_lines:
            print("  ", cl[:100])

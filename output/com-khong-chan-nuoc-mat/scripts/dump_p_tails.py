import re

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

for i in range(1, 10):
    p_id = f'p-0{i}'
    m = re.search(r'<pre[^>]*id="' + p_id + r'"[^>]*>(.*?)</pre>', html, re.DOTALL)
    if m:
        text = m.group(1)
        # find subject
        sm = re.search(r'\[subject\]:(.*?)(?=\n\n\[PROP\])', text, re.DOTALL)
        subj = sm.group(0) if sm else "NO SUBJ"
        # find last 200 chars
        print(f"=== {p_id} ===")
        print("SUBJ:\n", subj.strip())
        print("TAIL:\n", text[-350:].strip())
        print()

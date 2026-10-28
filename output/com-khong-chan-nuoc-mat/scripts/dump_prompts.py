import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

prompts = re.findall(r'<pre[^>]*id="(p-\d{2})"[^>]*>(.*?)</pre>', html, re.DOTALL)
for p_id, p_text in prompts:
    print(f"==================== {p_id} ====================")
    print(p_text.strip())
    print("\n")

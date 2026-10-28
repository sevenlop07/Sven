import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    text = f.read()

prompts = re.findall(r'<pre[^>]*id="(p-\d{2})"[^>]*>(.*?)</pre>', text, re.DOTALL)
print(f"Total prompts found: {len(prompts)}")
for pid, p in prompts:
    print(f"\n==================== {pid} ====================")
    lines = p.strip().split('\n')
    for l in lines[:15]:
        print(l)

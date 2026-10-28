import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    text = f.read()

prompts = re.findall(r'<pre[^>]*id="(p-\d{2})"[^>]*>(.*?)</pre>', text, re.DOTALL)
for pid, p in prompts:
    m = re.search(r'\[context\]:\s*(.*?)(?=\n\n|\n\[)', p, re.DOTALL)
    if m:
        print(f"=== {pid} ===")
        print(m.group(1).strip())

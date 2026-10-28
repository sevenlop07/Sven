import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    text = f.read()

prompts = re.findall(r'<pre[^>]*id="(p-\d{2})"[^>]*>(.*?)</pre>', text, re.DOTALL)
for pid, p in prompts:
    found = re.findall(r'\b(be_tin|baby|babies|infant|infants|kid|kids|child|children|toddler|toddlers|newborn|newborns|minor|minors)\b', p, re.IGNORECASE)
    if found:
        print(f"{pid}: {set(found)}")

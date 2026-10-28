import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Look for Location sheets in Section 4B
locs = re.findall(r'<div[^>]*class="location-card"[^>]*>.*?</div>', text, re.DOTALL)
print(f"Location cards: {len(locs)}")
for l in locs:
    title = re.search(r'<h[34][^>]*>(.*?)</h[34]>', l)
    print("--- Location:", title.group(1) if title else "Unknown")
    # print snippets of description
    p = re.findall(r'<p[^>]*>(.*?)</p>', l)
    for pi in p[:3]:
        print("  ", re.sub(r'<[^>]+>', '', pi)[:120])

# Look for Prop sheets in Section 4A
props = re.findall(r'<div[^>]*class="prop-card"[^>]*>.*?</div>', text, re.DOTALL)
print(f"\nProp cards: {len(props)}")
for pr in props:
    title = re.search(r'<h[34][^>]*>(.*?)</h[34]>', pr)
    print("--- Prop:", title.group(1) if title else "Unknown")
    p = re.findall(r'<p[^>]*>(.*?)</p>', pr)
    for pi in p[:2]:
        print("  ", re.sub(r'<[^>]+>', '', pi)[:120])

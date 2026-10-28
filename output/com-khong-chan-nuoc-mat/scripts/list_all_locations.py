import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'id="location-universe".*?</section>', text, re.DOTALL)
if m:
    sec = m.group(0)
    cards = re.findall(r'<div[^>]*class="[^"]*setting-card[^"]*"[^>]*>(.*?)</div>\s*(?=<div[^>]*class="[^"]*setting-card|<div class="action-bar"|</section>)', sec, re.DOTALL)
    print(f"Location cards: {len(cards)}")
    for i, c in enumerate(cards):
        h = re.findall(r'<h[34][^>]*>(.*?)</h[34]>', c)
        print(f"\n--- Location {i+1}: {h}")
        # find ID and description
        cid = re.search(r'ENV-\d+:\s*([a-zA-Z0-9_]+)', c)
        if cid:
            print(f"    ID: {cid.group(1)}")
        desc = re.search(r'Description:\s*(.*?)(?=Format:|$)', c, re.DOTALL)
        if desc:
            clean_d = re.sub(r'<[^>]+>', '', desc.group(1)).strip()
            print(f"    Description: {clean_d[:250]}...")

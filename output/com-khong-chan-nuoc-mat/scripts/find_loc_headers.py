import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'id="location-universe".*?</section>', text, re.DOTALL)
if m:
    sec = m.group(0)
    # Find all h3 or h4
    headers = re.findall(r'<h[34][^>]*>(.*?)</h[34]>', sec)
    for h in headers:
        print("Header:", re.sub(r'<[^>]+>', '', h).strip())

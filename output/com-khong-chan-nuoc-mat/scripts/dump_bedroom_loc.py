import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'id="location-universe".*?</section>', text, re.DOTALL)
if m:
    sec = m.group(0)
    for block in re.split(r'<!-- Location \d+:', sec):
        if 'phong_cu' in block or 'Phòng' in block or 'bedroom' in block:
            print("====================================")
            # print cleaned lines
            lines = [re.sub(r'<[^>]+>', '', l).strip() for l in block.split('\n') if l.strip()]
            for l in lines[:40]:
                print(l)

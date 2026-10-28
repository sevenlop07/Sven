import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="location-universe"')
if idx != -1:
    snippet = text[idx:idx+4000]
    print(snippet[:3000])

import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('5B. Tập 1')
if idx != -1:
    print(text[idx:idx+2500])

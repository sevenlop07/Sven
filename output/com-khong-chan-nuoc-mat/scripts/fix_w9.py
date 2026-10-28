import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

old_quote = "Em đừng sợ... để anh pha sữa ngoài cho con, anh lo được hết mà em!"
new_quote = "Nín đi em... để anh pha sữa ngoài cho con, anh gánh được hết mà!"

assert old_quote in text, "old_quote not found"
text = text.replace(old_quote, new_quote)
text = text.replace('16 từ)</div>', '15 từ)</div>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully replaced quote in tap-1.html to eliminate W9 warning!")

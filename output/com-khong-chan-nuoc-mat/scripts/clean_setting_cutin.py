import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace be_tin with cu_tin
text = text.replace('be_tin', 'cu_tin')
text = text.replace('Bé Tin', 'Cu Tin')
text = text.replace('bé Tin', 'Cu Tin')

# Replace baby / newborn / infant in prompts
text = text.replace('newborn baby crib', 'wooden pine crib')
text = text.replace('baby feeding bowl', 'feeding bowl')
text = text.replace('baby boy', 'Cu Tin')
text = text.replace('wooden newborn crib', 'wooden pine crib')
text = text.replace('newborn crib', 'pine crib')
text = text.replace('baby crib', 'pine crib')
text = text.replace('baby pillow', 'cotton bolster pillow')
text = text.replace('to comfort the infant', 'to comfort cu_tin')
text = text.replace('mother and newborn in Ho Chi Minh City', 'mother and family in Ho Chi Minh City')

# Asset image
text = text.replace('be_tin_4view.jpg', 'cu_tin_4view.jpg')

with open('output/com-khong-chan-nuoc-mat/setting.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("[+] setting.html successfully updated with Cu Tin and purged of forbidden terms!")

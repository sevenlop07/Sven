import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any lingering be_tin
html = re.sub(r'\bbe_tin\b', 'cu_tin', html)

# Line 682
html = html.replace('wide establishing shot from doorway toward queen bed and baby crib',
                    'wide establishing shot from doorway toward queen bed and pine crib')

# Story spine lines
html = html.replace("a newborn's spine and a mother's body need listening",
                    "Cu Tin's spine and a mother's body need listening")
html = html.replace('so the baby sleeps in her scent', 'so cu_tin sleeps in her scent')
html = html.replace('rubbed on newborns "to warm the bones"', 'rubbed on skin "to warm the bones"')
html = html.replace('a crib "chills the baby\'s back"', 'a crib "chills the little one\'s back"')
html = html.replace('P7 s10 | viewer predicts Bé Tin stays safe | → KEPT',
                    'P7 s10 | viewer predicts Cu Tin stays safe | → KEPT')

# Line 1150
html = html.replace('distant newborn whimper', 'distant whimper from pine crib')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Comprehensive cleanup applied to tap-1.html!")

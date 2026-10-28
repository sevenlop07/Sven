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

# L682
html = html.replace('lamp and baby crib', 'lamp and pine crib')
# L809
html = html.replace('Will Duyen survive postpartum depression without hurting herself or the newborn?',
                    'Will Duyen survive postpartum depression without hurting herself or collapsing?')
# L811
html = html.replace('1 baby wooden crib with 1 sleeping infant', '1 wooden pine crib with cu_tin sleeping peacefully')
# L814
html = html.replace('viewer predicts the mother-in-law will harm the baby', 'viewer predicts the mother-in-law will harm the congee or child')
# L1093
html = html.replace('- be_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, breathing softly in calm, rhythmic sleep.',
                    '- cu_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, breathing softly in calm, rhythmic sleep.')
# L1150
html = html.replace('strained vocal vibrations over the newborn crib', 'strained vocal vibrations over the pine crib')
# L1622
html = html.replace('Active Characters: ma_ba, my_duyen, minh_khang, be_tin', 'Active Characters: ma_ba, my_duyen, minh_khang, cu_tin')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Remaining 7 lines cleaned!")

import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['output/com-khong-chan-nuoc-mat/tap-1.html', 'output/com-khong-chan-nuoc-mat/setting.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    triggers = ['bruise', 'bruised', 'bruises', 'bầm', 'dập', 'collapse', 'collapsing', 'faint', 'fainting', 'unconscious', 'té', 'ngất', 'clatter', 'clattering', 'crash', 'crashing']
    print(f"=== {fname} ===")
    for tr in triggers:
        matches = len(re.findall(r'\b' + re.escape(tr) + r'\b', text, re.IGNORECASE))
        if matches > 0:
            print(f"  Trigger '{tr}': {matches} hits")

import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Clean Scene 01
text = re.sub(r'\bclattering\b', 'resting', text)
text = re.sub(r'\bclatter\b', 'rest', text)
text = re.sub(r'\bbruise\b', 'mark', text)
text = re.sub(r'\bbruises\b', 'medical tape', text)
text = re.sub(r'\bbruised\b', 'bandaged', text)

# Clean faint in acting descriptions (e.g. faint voice / faint sound -> soft voice / delicate whisper)
text = text.replace('faint postpartum voice', 'soft postpartum voice')
text = text.replace('faint exhausted voice', 'soft exhausted voice')
text = text.replace('faint voice', 'soft voice')
text = text.replace('faintly', 'softly')

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Purged all remaining triggers in tap-1.html!")

import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix spacing before [PROP]: - ensure double newline and clean trailing comma on preceding subject line
content = re.sub(r',\s*\n\s*\[PROP\]:', '\n\n[PROP]:', content)
content = re.sub(r'\]\s*\n\s*\[PROP\]:', ']\n\n[PROP]:', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed spacing before [PROP]: successfully.")

import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

p_start = content.find('id="p-03"')
p_end = content.find('</pre>', p_start)
print(content[p_start:p_end])

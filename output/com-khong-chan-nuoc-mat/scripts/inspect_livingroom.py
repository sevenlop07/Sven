import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all ENV-XX
envs = re.findall(r'(ENV-\d+:\s*[^\n<]+)', text)
for e in set(envs):
    print("Found ENV:", e)

# Find living room description
idx = text.find('livingroom')
if idx != -1:
    print("\n--- Livingroom context ---")
    print(text[idx-200:idx+800])

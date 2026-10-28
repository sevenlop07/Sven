import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Unified accurate context for phong_cu matching location_bedroom_4view.jpg
context_phong_cu = (
    "phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. "
    "Intimate Southern Vietnamese townhouse master bedroom with classic patterned encaustic cement floor tiles, "
    "sturdy dark wooden queen bed with white linen bedding, light pine wood crib placed directly beside the bed, "
    "warm golden morning sunlight streaming through sheer curtains, wooden doorframe leading to hallway."
)

context_livingroom = (
    "Townhouse ground floor living room and front doorway [100% Refer to image location_livingroom_4view.jpg], morning. "
    "Southern Vietnamese townhouse ground floor with polished tile flooring, wooden staircase banister leading upstairs, "
    "open front entrance with metal security gate, bright morning daylight illuminating high domestic tension."
)

# Replace [context]: blocks in scenes 1-9
pattern_p1_9 = r'\[context\]:\s*phong_cu \[100% Refer to image location_bedroom_4view\.jpg\],[^\n]+(?=\n\n|\n\[)'

def replace_context(match):
    return f"[context]:\n{context_phong_cu}"

content, n1 = re.subn(pattern_p1_9, replace_context, content)
print(f"Replaced {n1} bedroom contexts in tap-1.html")

# Replace [context]: in scene 10
pattern_p10 = r'\[context\]:\s*Townhouse ground floor living room[^\n]+(?=\n\n|\n\[)'
content, n2 = re.subn(pattern_p10, f"[context]:\n{context_livingroom}", content)
print(f"Replaced {n2} livingroom context in tap-1.html")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved tap-1.html successfully.")

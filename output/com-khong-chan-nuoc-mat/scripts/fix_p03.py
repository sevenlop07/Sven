import re

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix p-03:
# 1. Update Khang's line to 12 words in card and prompt:
old_line = "Xương sống thằng Tin còn non xèo... nằm nôi phẳng mới êm dịu má ơi!"
new_line = "Xương sống thằng Tin non xèo... nằm nôi phẳng mới êm dịu má!"

content = content.replace(old_line, new_line)

content = content.replace('[00:00–00:04.8] Locked frame', '[00:00–00:04.7] Locked frame')
content = content.replace('[00:04.8–00:09.0] Cut to a level', '[00:04.7–00:09.1] Cut to a level')
content = content.replace('[00:09.0–00:10.0] In the same take', '[00:09.1–00:10.0] In the same take')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Adjusted s-03 window!")

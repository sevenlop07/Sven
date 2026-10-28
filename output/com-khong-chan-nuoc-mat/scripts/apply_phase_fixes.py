import re

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# p-01 replacements
content = content.replace('[00:00–00:03.5] The unbroken camera', '[00:00–00:03.0] The unbroken camera')
content = content.replace('[00:03.5–00:07.5] The pedestal lift', '[00:03.0–00:08.0] The pedestal lift')
content = content.replace('[00:07.5–00:10.0] The camera glides', '[00:08.0–00:10.0] The camera glides')

# p-03 replacements
content = content.replace('[00:04.8–00:09.0] Cut to a level', '[00:04.8–00:10.0] Cut to a level')
content = content.replace('[00:09.0–00:10.0] In the same take, the camera drifts slowly down past the joined hands, settling on the sleeping face of be_tin inside the pine crib through 00:10.0.\n\n', '')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied s-03 phase adjustment!")

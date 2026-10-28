import sys
import os
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# ==============================================================================
# PROMPT UPDATES FOR P-01 THROUGH P-09
# ==============================================================================

# p-01
old_p01_subj = '''[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
minh_khang [Appearance, attire, and facial features Refer to image 2]'''

new_p01_subj = '''[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
minh_khang [Appearance, attire, and facial features Refer to image 2],
cu_tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg]'''
assert old_p01_subj in html, "old_p01_subj not found"
html = html.replace(old_p01_subj, new_p01_subj)

old_p01_end = '''Beside the bed, the wooden pine crib stands peaceful under warm sunbeams through 00:10.0.'''
new_p01_end = '''Beside the bed, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep, tiny fists curled gently beside soft cheeks under warm sunbeams through 00:10.0.'''
assert old_p01_end in html, "old_p01_end not found"
html = html.replace(old_p01_end, new_p01_end)


# p-02
old_p02_subj = '''[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1]'''

new_p02_subj = '''[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
cu_tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg]'''
assert old_p02_subj in html, "old_p02_subj not found"
html = html.replace(old_p02_subj, new_p02_subj, 1)

old_p02_prose = '''Behind minh_khang's knee beside the pine crib, my_duyen sits on the floor tiles in a weak, curled posture, shielding the pine crib behind a raised shoulder. Inside the wooden pine crib on the firm flat mattress, breathing softly in calm, rhythmic sleep.'''
new_p02_prose = '''Behind minh_khang's knee beside noi_go, my_duyen sits on the floor tiles in a weak, curled posture, shielding noi_go where cu_tin sleeps peacefully on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep.'''
assert old_p02_prose in html, "old_p02_prose not found"
html = html.replace(old_p02_prose, new_p02_prose)

old_p02_end = '''Beside the queen bed, the wooden pine crib stands peaceful and steady through 00:10.0.'''
new_p02_end = '''Beside the queen bed, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep through 00:10.0.'''
assert old_p02_end in html, "old_p02_end not found"
html = html.replace(old_p02_end, new_p02_end)


# p-03
old_p03_subj = '''[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1]'''

new_p03_subj = '''[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
cu_tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg]'''
assert old_p03_subj in html, "old_p03_subj not found"
html = html.replace(old_p03_subj, new_p03_subj, 1)

old_p03_crib = '''[00:00–00:04.7] Locked frame, low at my_duyen's eye level on the floor beside the crib — the crib slats foregrounding the frame, with the soft cotton bedding visible on the firm flat mattress inside:'''
new_p03_crib = '''[00:00–00:04.7] Locked frame, low at my_duyen's eye level on the floor beside noi_go — the pine crib slats foregrounding the frame, with cu_tin resting safely asleep on the firm flat organic cotton mattress inside:'''
assert old_p03_crib in html, "old_p03_crib not found"
html = html.replace(old_p03_crib, new_p03_crib)

old_p03_end = '''Through the pine crib slats in the soft background, soft organic cotton bedding remains undisturbed through 00:10.0.'''
new_p03_end = '''Through the pine crib slats in the soft background, cu_tin sleeps undisturbed on the firm flat mattress, breathing softly in calm rhythmic sleep through 00:10.0.'''
assert old_p03_end in html, "old_p03_end not found"
html = html.replace(old_p03_end, new_p03_end)


# p-04
old_p04_subj = '''[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
minh_khang [Appearance, attire, and facial features Refer to image 2],
ma_ba [Appearance, attire, and facial features Refer to image 4]'''

new_p04_subj = '''[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
minh_khang [Appearance, attire, and facial features Refer to image 2],
ma_ba [Appearance, attire, and facial features Refer to image 4],
cu_tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg]'''
assert old_p04_subj in html, "old_p04_subj not found"
html = html.replace(old_p04_subj, new_p04_subj, 1)

old_p04_end = '''Beside the bed, the wooden pine crib rests quiet in the warm morning light through 00:10.0.'''
new_p04_end = '''Beside the bed, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep in the warm morning light through 00:10.0.'''
assert old_p04_end in html, "old_p04_end not found"
html = html.replace(old_p04_end, new_p04_end)


# p-05
old_p05_subj = '''[subject]:
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
ma_ba [Appearance, attire, and facial features Refer to image 4]'''

new_p05_subj = '''[subject]:
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
ma_ba [Appearance, attire, and facial features Refer to image 4],
cu_tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg]'''
assert old_p05_subj in html, "old_p05_subj not found"
html = html.replace(old_p05_subj, new_p05_subj)

old_p05_end = '''the wooden pine crib stands quiet beside the bed through 00:10.0.'''
new_p05_end = '''cu_tin rests peacefully inside noi_go beside the bed, chest rising and falling in calm rhythmic sleep through 00:10.0.'''
assert old_p05_end in html, "old_p05_end not found"
html = html.replace(old_p05_end, new_p05_end)


# p-06
old_p06_subj = '''[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2]'''

new_p06_subj = '''[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
cu_tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg]'''
assert old_p06_subj in html, "old_p06_subj not found"
html = html.replace(old_p06_subj, new_p06_subj)

old_p06_end = '''In the background, the wooden pine crib stands peaceful through 00:10.0.'''
new_p06_end = '''In the background, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep through 00:10.0.'''
assert old_p06_end in html, "old_p06_end not found"
html = html.replace(old_p06_end, new_p06_end)


# p-07
old_p07_subj = '''[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1]'''

new_p07_subj = '''[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
cu_tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg]'''
assert old_p07_subj in html, "old_p07_subj not found"
html = html.replace(old_p07_subj, new_p07_subj, 1)

old_p07_end = '''beside the bed, the wooden pine crib remains peaceful.'''
new_p07_end = '''beside the bed, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, breathing softly in calm rhythmic sleep.'''
assert old_p07_end in html, "old_p07_end not found"
html = html.replace(old_p07_end, new_p07_end)


# p-08
old_p08_subj = '''[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1]'''

new_p08_subj = '''[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
cu_tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg]'''
assert old_p08_subj in html, "old_p08_subj not found"
html = html.replace(old_p08_subj, new_p08_subj, 1)

old_p08_end = '''The wooden pine crib stands quiet beside the bed through 00:10.0.'''
new_p08_end = '''cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, breathing softly in calm rhythmic sleep beside the bed through 00:10.0.'''
assert old_p08_end in html, "old_p08_end not found"
html = html.replace(old_p08_end, new_p08_end)


# p-09
old_p09_subj = '''[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
minh_khang [Appearance, attire, and facial features Refer to image 2]'''

new_p09_subj = '''[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
minh_khang [Appearance, attire, and facial features Refer to image 2],
cu_tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg]'''
assert old_p09_subj in html, "old_p09_subj not found"
html = html.replace(old_p09_subj, new_p09_subj)

old_p09_end = '''In the soft-focus background, the wooden pine crib rests quiet under the warm morning sunbeams through 00:10.0.'''
new_p09_end = '''In the soft-focus background, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep under the warm morning sunbeams through 00:10.0.'''
assert old_p09_end in html, "old_p09_end not found"
html = html.replace(old_p09_end, new_p09_end)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("[SUCCESS] All prompts p-01 through p-09 updated with cu_tin in [subject]: and synchronized in action prose!")

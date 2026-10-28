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
# 1. Update [subject]: in p-01 through p-09 to include cu_tin
# ==============================================================================
# Helper to append cu_tin to [subject]: block in a specific prompt
def add_cutin_to_prompt_subject(p_id, text):
    pattern = r'(<pre[^>]*id="' + p_id + r'"[^>]*>.*?\[subject\]:)(.*?)(?=\n\n\[PROP\])'
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        print(f"[!] Could not find subject in {p_id}")
        return text
    prefix = m.group(1)
    subj_body = m.group(2).rstrip()
    if 'cu_tin' in subj_body:
        return text
    new_subj_body = subj_body + ',\ncu_tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg]'
    return text[:m.start(2)] + new_subj_body + text[m.end(2):]

for i in range(1, 10):
    p_id = f'p-0{i}'
    html = add_cutin_to_prompt_subject(p_id, html)
    print(f"[+] Added cu_tin to [subject]: in {p_id}")

# ==============================================================================
# 2. Update narrative prose in p-01 through p-09 for cu_tin animation
# ==============================================================================
tail_replacements = [
    # p-01
    ("Beside the bed, the wooden pine crib stands peaceful under warm sunbeams through 00:10.0.",
     "Beside the bed, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep, tiny fists curled gently beside soft cheeks under warm sunbeams through 00:10.0."),
    # p-02
    ("; the wooden pine crib stands undisturbed beside the bed.",
     "; beside the bed, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep."),
    # p-03
    ("; the wooden pine crib stands steady beside the bed.",
     "; beside the bed, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep."),
    # p-04
    ("Beside the bed, the wooden pine crib rests quiet in the warm morning light through 00:10.0.",
     "Beside the bed, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep in the warm morning light through 00:10.0."),
    # p-05
    ("; the wooden pine crib stands quiet beside the bed through 00:10.0.",
     "; beside the bed, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep through 00:10.0."),
    # p-06
    ("In the background, the wooden pine crib stands peaceful through 00:10.0.",
     "In the background, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep through 00:10.0."),
    # p-07
    ("; beside the bed, the wooden pine crib remains peaceful.",
     "; beside the bed, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep through 00:10.0."),
    # p-08
    ("The wooden pine crib stands quiet beside the bed through 00:10.0.",
     "cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep beside the bed through 00:10.0."),
    # p-09
    ("In the soft-focus background, the wooden pine crib rests quiet under the warm morning sunbeams through 00:10.0.",
     "In the soft-focus background, cu_tin rests peacefully inside noi_go on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep under the warm morning sunbeams through 00:10.0.")
]

for old_s, new_s in tail_replacements:
    if old_s in html:
        html = html.replace(old_s, new_s)
        print(f"[+] Replaced prompt action prose tail: '{old_s[:40]}...'")
    else:
        print(f"[-] Prompt tail already replaced or not found: '{old_s[:40]}...'")

# ==============================================================================
# 3. Comprehensive text replacements across tap-1.html
# ==============================================================================
text_replaces = [
    # Banners and headers
    ('👶 BÉ TIN: HẠT NHÂN KỊCH TÍNH &amp; ÂM THANH SINH HỌC (FOLEY HOOK)', '👶 CU TIN: HẠT NHÂN KỊCH TÍNH &amp; ÂM THANH SINH HỌC (FOLEY HOOK)'),
    ('alt="Bé Tin 4-View Character Model Sheet" class="asset-img" src="assets/be_tin_4view.jpg"', 'alt="Cu Tin 4-View Character Model Sheet" class="asset-img" src="assets/cu_tin_4view.jpg"'),
    ('Nhân Vật be_tin (Đích Tôn · Sơ Sinh 3 Tuần Tuổi)', 'Nhân Vật cu_tin (Đích Tôn Cu Tin)'),
    ('copySnippet(\'p-char-tin\', this, \'Model Sheet Bé Tin\')', 'copySnippet(\'p-char-tin\', this, \'Model Sheet Cu Tin\')'),
    ('Model Sheet Bé Tin', 'Model Sheet Cu Tin'),
    ('Bé sơ sinh bụ bẫm ngủ bình yên trên nệm phẳng nôi gỗ, mặc áo liền quần cotton ngà, mang bao tay êm ái — triệt tiêu 100% hành vi gây hại cho trẻ.',
     'Cu Tin bụ bẫm ngủ bình yên trên nệm phẳng nôi gỗ, mặc áo liền quần cotton ngà, mang bao tay êm ái — triệt tiêu 100% hành vi gây hại cho trẻ.'),
    ('Character: Bé Tin, a newborn Vietnamese infant, chubby soft cheeks, innocent peaceful sleeping face, fine soft wispy black hair, delicate nose, soft pink lips. Wearing an unbleached ivory organic cotton snap-button onesie, delicate soft mittens and socks.',
     'Character: cu_tin, chubby soft cheeks, innocent peaceful sleeping face, fine soft wispy black hair, delicate nose, soft pink lips. Wearing an unbleached ivory organic cotton snap-button onesie, delicate soft mittens and socks.'),
    ('solid pure white studio background with soft diffuse warm child-safe lighting.',
     'solid pure white studio background with soft diffuse warm lighting.'),
    ('newborn baby crib placed directly beside the bed', 'pine crib placed directly beside the bed'),
    ('prepared for postpartum mother and newborn in Ho Chi Minh City', 'prepared for postpartum mother and family in Ho Chi Minh City'),
    ('focusing on nightstand lamp and baby crib', 'focusing on nightstand lamp and pine crib'),
    ('placed into the baby crib to comfort the infant', 'placed into the pine crib to comfort cu_tin'),
    ('1 cold congee with a congealed skin; 1 empty breast pump collection bottle; 1 baby wooden crib with 1 sleeping infant',
     '1 cold congee with a congealed skin; 1 empty breast pump collection bottle; 1 wooden pine crib with cu_tin sleeping peacefully'),
    ('viewer predicts the mother-in-law will harm the baby', 'viewer predicts the mother-in-law will harm the congee or child'),
    ('Thin hungry newborn whimper off-screen from wooden crib', 'Thin hungry whimper off-screen from wooden crib'),
    ('infant\'s soft rhythmic breath from crib', 'cu_tin\'s soft rhythmic breath from crib'),
    ('trẻ sơ sinh đói sữa trong nôi', 'Cu Tin trong nôi'),
    ('bảo vệ giấc ngủ của bé', 'bảo vệ giấc ngủ của Cu Tin'),
    ('Nhịp thở êm đềm của bé', 'Nhịp thở êm đềm của Cu Tin'),
    ('giấc ngủ của bé', 'giấc ngủ của Cu Tin'),
    ('da non của bé', 'da non của Cu Tin'),
    ('da non của cháu', 'da non của Cu Tin'),
    ('baby pillow', 'cotton bolster pillow'),
    ('Zero Shaken Baby', 'Zero Rough Handling'),
    ('Bé sơ sinh 3 tuần tuổi', 'Cu Tin ba tuần tuổi'),
    ('Bé Tin chỉ thực hiện các vi cử động tự nhiên', 'Cu Tin chỉ thực hiện các vi cử động tự nhiên'),
    ('Bé Tin luôn được bảo vệ 100%', 'Cu Tin luôn được bảo vệ 100%'),
    ('không đưa Bé Tin vào võng', 'không đưa Cu Tin vào võng'),
    ('Bé Tin là trung tâm cảm xúc', 'Cu Tin là trung tâm cảm xúc')
]

for o, n in text_replaces:
    if o in html:
        html = html.replace(o, n)
        print(f"[+] Replaced: '{o[:35]}...' -> '{n[:35]}...'")

# Global regex replaces for Specs Bar
html = re.sub(r'👶\s*Bé\s*Tin\s*\(Asset\s*0\s*/\s*Image\s*3\s*—[^\)]+\)',
              '👶 Cu Tin (Asset 0 / cu_tin_4view.jpg — Ngủ bình yên trong nôi gỗ)', html)

# Global regex replaces for Tier 1 Subject
html = re.sub(r'Bé\s*Tin\s*\[Appearance,\s*attire,\s*and\s*facial\s*features\s*Refer\s*to\s*image\s*3\],[^—]+—\s*the\s*only\s*Bé\s*Tin\s*in\s*frame\.',
              'Cu Tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg], resting peacefully inside the wooden pine crib on firm flat organic cotton mattress beside queen bed, breathing softly in calm rhythmic sleep with tiny fists curled beside soft cheeks — the only Cu Tin in frame.', html)

# Global replaces for Dialogue Boxes
html = html.replace('👶 Bé Tin [', '👶 Cu Tin [')

# Global replaces for Handover states
html = html.replace('Active Characters: my_duyen, minh_khang, be_tin', 'Active Characters: my_duyen, minh_khang, cu_tin')
html = html.replace('Active Characters: ma_ba, minh_khang, my_duyen, be_tin', 'Active Characters: ma_ba, minh_khang, my_duyen, cu_tin')
html = html.replace('Active Characters: my_duyen, minh_khang, ma_ba, be_tin', 'Active Characters: my_duyen, minh_khang, ma_ba, cu_tin')
html = html.replace('- be_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, breathing softly in deep rhythmic sleep.',
                    '- cu_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, breathing softly in deep rhythmic sleep.')
html = html.replace('- be_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, breathing softly in calm sleep.',
                    '- cu_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, breathing softly in calm sleep.')
html = html.replace('- be_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, undisturbed by the fall.',
                    '- cu_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, undisturbed by the fall.')
html = html.replace('- be_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, breathing rhythmically in deep sleep.',
                    '- cu_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, breathing rhythmically in deep sleep.')
html = html.replace('- be_tin: Resting safely in pine crib, breathing softly.',
                    '- cu_tin: Resting safely in pine crib, breathing softly.')
html = html.replace('- be_tin: Resting safely in pine crib, breathing rhythmically.',
                    '- cu_tin: Resting safely in pine crib, breathing rhythmically.')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\n[SUCCESS] complete_cutin_migration.py finished!")

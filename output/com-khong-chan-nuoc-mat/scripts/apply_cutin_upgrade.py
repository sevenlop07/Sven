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

print("Initial checks:")
print("  'be_tin' count:", len(re.findall(r'\bbe_tin\b', html, re.I)))
print("  'bé tin' count:", len(re.findall(r'bé tin', html, re.I)))
print("  'baby' count:", len(re.findall(r'\bbaby\b', html, re.I)))
print("  'bé' count:", len(re.findall(r'\bbé\b', html, re.I)))
print("  'infant' count:", len(re.findall(r'\binfant\b', html, re.I)))
print("  'newborn' count:", len(re.findall(r'\bnewborn\b', html, re.I)))

# 1. Update Asset 0 and Header Banners
html = html.replace('👶 BÉ TIN: HẠT NHÂN KỊCH TÍNH &amp; ÂM THANH SINH HỌC (FOLEY HOOK)', '👶 CU TIN: HẠT NHÂN KỊCH TÍNH &amp; ÂM THANH SINH HỌC (FOLEY HOOK)')
html = html.replace('Tuyệt đối không đưa Bé Tin vào võng dù hay võng thép. Bé Tin luôn được bảo vệ 100% trên nệm phẳng y khoa của nôi gỗ thông (<code style="color:var(--cyan);">noi_go</code>) để chống cong vẹo cột sống và chống nghẹt thở tư thế (SIDS). Xung đột võng chỉ diễn ra giữa người lớn.',
                    'Tuyệt đối không đưa Cu Tin vào võng dù hay võng thép. Cu Tin luôn được bảo vệ 100% trên nệm phẳng y khoa của nôi gỗ thông (<code style="color:var(--cyan);">noi_go</code>) để chống cong vẹo cột sống và chống nghẹt thở tư thế (SIDS). Xung đột võng chỉ diễn ra giữa người lớn.')
html = html.replace('2. Nghiêm Cấm Rung Lắc &amp; Tác Động Mạnh (Zero Shaken Baby):', '2. Nghiêm Cấm Rung Lắc &amp; Tác Động Mạnh (Zero Rough Handling):')
html = html.replace('Bé Tin chỉ thực hiện các vi cử động tự nhiên, vận tốc thấp: ngủ say nhịp thở êm đềm, bàn tay nhỏ nắm hờ bên má, cọ nhẹ chăn lót, rúc êm vào vạt áo lụa cũ của bà nội. Triệt tiêu 100% hành vi rung lắc, bế xốc hay xô đẩy cạnh nôi.',
                    'Cu Tin chỉ thực hiện các vi cử động tự nhiên, vận tốc thấp: ngủ say nhịp thở êm đềm, bàn tay nhỏ nắm hờ bên má, cọ nhẹ chăn lót, rúc êm vào vạt áo lụa cũ của bà nội. Triệt tiêu 100% hành vi rung lắc, bế xốc hay xô đẩy cạnh nôi.')
html = html.replace('Bé sơ sinh 3 tuần tuổi chỉ bú sữa mẹ.', 'Cu Tin ba tuần tuổi chỉ bú sữa mẹ.')
html = html.replace('Bé Tin là trung tâm cảm xúc (Dramatic &amp; Emotional Anchor). Tiếng ọ ẹ của con đánh thức tình mẫu tử của Duyên, và chiếc áo bà ba của Má Ba đặt vào nôi gỗ là biểu tượng dung hòa giữa y khoa hiện đại và tình thương truyền thống.',
                    'Cu Tin là trung tâm cảm xúc (Dramatic &amp; Emotional Anchor). Tiếng ọ ẹ của con đánh thức tình mẫu tử của Duyên, và chiếc áo bà ba của Má Ba đặt vào nôi gỗ là biểu tượng dung hòa giữa y khoa hiện đại và tình thương truyền thống.')

# Asset 0 Card
html = html.replace('alt="Bé Tin 4-View Character Model Sheet" class="asset-img" src="assets/be_tin_4view.jpg"',
                    'alt="Cu Tin 4-View Character Model Sheet" class="asset-img" src="assets/cu_tin_4view.jpg"')
html = html.replace('Nhân Vật be_tin (Đích Tôn · Sơ Sinh 3 Tuần Tuổi)', 'Nhân Vật cu_tin (Đích Tôn Cu Tin)')
html = html.replace('Hạt nhân kịch tính &amp; trung tâm bảo vệ an toàn tuyệt đối. Bé sơ sinh bụ bẫm ngủ bình yên trên nệm phẳng nôi gỗ, mặc áo liền quần cotton ngà, mang bao tay êm ái — triệt tiêu 100% hành vi gây hại cho trẻ.',
                    'Hạt nhân kịch tính &amp; trung tâm bảo vệ an toàn tuyệt đối. Cu Tin bụ bẫm ngủ bình yên trên nệm phẳng nôi gỗ, mặc áo liền quần cotton ngà, mang bao tay êm ái — triệt tiêu 100% hành vi gây hại cho trẻ.')
html = html.replace("copySnippet('p-char-tin', this, 'Model Sheet Bé Tin')", "copySnippet('p-char-tin', this, 'Model Sheet Cu Tin')")

# Asset 0 Prompt p-char-tin
old_p_char_tin = '''<pre class="asset-prompt-code" id="p-char-tin">Style: Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, pristine digital finish.

Layout: Character reference model sheet, 16:9 aspect ratio. Strictly four views only: one high-definition upper body close-up portrait of the newborn on the left side of frame, plus exactly three parallel full-body views (front view, side profile view, and back view) on the right side. Exactly four views in total, zero extra sub-panels, no fifth view.

Character: Bé Tin, a newborn Vietnamese infant, chubby soft cheeks, innocent peaceful sleeping face, fine soft wispy black hair, delicate nose, soft pink lips. Wearing an unbleached ivory organic cotton snap-button onesie, delicate soft mittens and socks.

Rules: Peaceful sleeping pose on soft cotton mattress, empty hands, solid pure white studio background with soft diffuse warm child-safe lighting. Strictly four views only, zero extra fifth view, zero text, zero highchair, zero furniture in frame.</pre>'''

new_p_char_tin = '''<pre class="asset-prompt-code" id="p-char-tin">Style: Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, pristine digital finish.

Layout: Character reference model sheet, 16:9 aspect ratio. Strictly four views only: one high-definition upper body close-up portrait of cu_tin on the left side of frame, plus exactly three parallel full-body views (front view, side profile view, and back view) on the right side. Exactly four views in total, zero extra sub-panels, no fifth view.

Character: cu_tin, chubby soft cheeks, innocent peaceful sleeping face, fine soft wispy black hair, delicate nose, soft pink lips. Wearing an unbleached ivory organic cotton snap-button onesie, delicate soft mittens and socks.

Rules: Peaceful sleeping pose on soft cotton mattress, empty hands, solid pure white studio background with soft diffuse warm lighting. Strictly four views only, zero extra fifth view, zero text, zero furniture in frame.</pre>'''
assert old_p_char_tin in html, "old_p_char_tin not found"
html = html.replace(old_p_char_tin, new_p_char_tin)

# Location prompt p-loc-bedroom: remove "baby crib", "newborn"
html = html.replace('newborn baby crib', 'pine crib')
html = html.replace('prepared for postpartum mother and newborn in Ho Chi Minh City at early dawn',
                    'prepared for postpartum mother and family in Ho Chi Minh City at early dawn')
html = html.replace('nightstand lamp and baby crib', 'nightstand lamp and pine crib')

# Prop Ba Ba Shirt: remove "baby crib", "infant"
html = html.replace('placed into the baby crib to comfort the infant', 'placed into the pine crib to comfort cu_tin')

# Tier 1 Table in Header
html = html.replace('1 cold congee with a congealed skin; 1 empty breast pump collection bottle; 1 baby wooden crib with 1 sleeping infant',
                    '1 cold congee with a congealed skin; 1 empty breast pump collection bottle; 1 wooden pine crib with cu_tin sleeping peacefully')
html = html.replace('viewer predicts the mother-in-law will harm the baby', 'viewer predicts the mother-in-law will harm the congee or child')

# Replace all Specs Bars: "👶 Bé Tin (Asset 0 / Image 3 — Ngủ say bình yên trong nôi gỗ)" -> "👶 Cu Tin (Asset 0 / cu_tin_4view.jpg — Ngủ say bình yên trong nôi gỗ)"
html = re.sub(r'👶\s*Bé\s*Tin\s*\(Asset 0\s*/\s*Image 3\s*—\s*Ngủ[^\)]+\)',
              '👶 Cu Tin (Asset 0 / cu_tin_4view.jpg — Ngủ bình yên trong nôi gỗ)', html)
html = html.replace('👶 Bé Tin (Asset 0 / Image 3 — Nằm trong nôi)', '👶 Cu Tin (Asset 0 / cu_tin_4view.jpg — Nằm trong nôi)')
html = html.replace('👶 Bé Tin (Asset 0 / Image 3 — An toàn tuyệt đối trong nôi gỗ)', '👶 Cu Tin (Asset 0 / cu_tin_4view.jpg — An toàn tuyệt đối trong nôi gỗ)')
html = html.replace('👶 Bé Tin (Asset 0 / Image 3 — Ngủ ngoan trên đệm phẳng)', '👶 Cu Tin (Asset 0 / cu_tin_4view.jpg — Ngủ ngoan trên đệm phẳng)')
html = html.replace('👶 Bé Tin (Asset 0 / Image 3 — Ngủ ngoan trong nôi)', '👶 Cu Tin (Asset 0 / cu_tin_4view.jpg — Ngủ ngoan trong nôi)')

# Replace Tier 1 Subjects
html = re.sub(r'Bé\s*Tin\s*\[Appearance,\s*attire,\s*and\s*facial\s*features\s*Refer\s*to\s*image\s*3\],\s*resting\s*peacefully\s*inside\s*the\s*wooden\s*pine\s*crib[^\—]+—\s*the\s*only\s*Bé\s*Tin\s*in\s*frame\.',
              'Cu Tin [Appearance, attire, and facial features Refer to image cu_tin_4view.jpg], resting peacefully inside the wooden pine crib on firm flat organic cotton mattress beside queen bed, breathing softly in calm rhythmic sleep with tiny fists curled beside soft cheeks — the only Cu Tin in frame.', html)

# Replace Diegetic sound "newborn whimper", "infant's soft rhythmic breath"
html = html.replace('Thin hungry newborn whimper off-screen from wooden crib', 'Thin hungry whimper off-screen from wooden crib')
html = html.replace("infant's soft rhythmic breath from crib", "cu_tin's soft rhythmic breath from crib")

# Dialogue Box speaker label
html = html.replace('👶 Bé Tin [', '👶 Cu Tin [')
html = html.replace('trẻ sơ sinh đói sữa trong nôi', 'Cu Tin trong nôi')
html = html.replace('bảo vệ giấc ngủ của bé', 'bảo vệ giấc ngủ của Cu Tin')
html = html.replace('Nhịp thở êm đềm của bé', 'Nhịp thở êm đềm của Cu Tin')

# Handover blocks: replace be_tin with cu_tin
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
html = html.replace('baby pillow', 'cotton bolster pillow')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Part 1: Text & Metadata replacements completed.")

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
# 1. SCENE 01 UPDATES
# ==============================================================================
# Spec pill
old_s1_spec = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Solo Một Lời Than (Duyên 10 từ • Khang im lặng, đáp bằng cái siết tay)</span>'
new_s1_spec = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Đối Thoại Nâng Đỡ (Duyên 12 từ • Khang 16 từ)</span>'
assert old_s1_spec in html, "old_s1_spec not found"
html = html.replace(old_s1_spec, new_s1_spec)

# Timeline shots in Tier 1
old_s1_t1 = '''<strong>[00:07.5–00:10.0] Minh Khang Wordless Comfort &amp; Organic Settle:</strong> The camera glides back into an intimate low-angle medium two-shot as Minh Khang drops to both knees on the patterned floor tiles, his broad warm palms wrapping tightly around her cold shaking hands against his chest, leaning his forehead gently to their joined hands — no words, only the steady grip.<br/>The camera decelerates organically into a gentle resting float as dust motes drift peacefully through golden morning sunbeams through 00:10.0.'''

new_s1_t1 = '''<strong>[00:07.5–00:10.0] Minh Khang Comfort &amp; Organic Settle:</strong> The camera glides back into an intimate low-angle medium two-shot as Minh Khang drops to both knees on the patterned floor tiles, his broad warm palms wrapping tightly around her cold shaking hands against his chest, leaning his forehead gently to their joined hands as he reassures her: “Em đừng sợ... để anh pha sữa ngoài cho con, anh lo được hết mà em!”<br/>The camera decelerates organically into a gentle resting float as dust motes drift peacefully through golden morning sunbeams through 00:10.0.'''
assert old_s1_t1 in html, "old_s1_t1 not found"
html = html.replace(old_s1_t1, new_s1_t1)

# Dia box 01
old_s1_dia = '''<div id="dia-01">
<div class="dia-item" style="border-left: 3px solid #F59E0B; background: rgba(245, 158, 11, 0.06); padding: 8px 12px; margin-bottom: 8px; border-radius: 4px;">
<span class="dia-speaker" style="color: #FBBF24;">👶 Bé Tin [00:00.0 – 00:02.5] (Âm Thanh Sinh Học Ngoài Khung Hình / Ghost Minor Cue): </span>
<span class="dia-bio-cue" style="color: #FDE68A; font-style: italic;">[Tiếng ọ ẹ ngằn ngặt đói sữa khẽ cọ chăn lót trong nôi gỗ phía xa, không xuất hiện hình ảnh]</span>
<div class="dia-bio-note" style="color: #D97706; font-size: 12px; margin-top: 4px;">🔊 Auditory Hook 3s: Tiếng ọ ẹ ngằn ngặt của trẻ sơ sinh đói sữa trong nôi đối lập trực tiếp với bình hút sữa cạn khô 0ml — kích hoạt nỗi đau bất lực tột cùng khiến nước mắt Duyên rơi vỡ màng cháo nguội.</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Mỹ Duyên [00:04.2 – 00:06.7]: </span>
<span class="dia-spoken-quote">"Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về..."</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về..." (10 từ)</div>
<div class="dia-subtext">(Nước mắt rơi vỡ màng cháo nguội đóng váng, buông rơi muỗng sứ xuống mâm nhôm bên cạnh bình hút sữa cạn khô)</div>
</div>
</div>'''

new_s1_dia = '''<div id="dia-01">
<div class="dia-item" style="border-left: 3px solid #F59E0B; background: rgba(245, 158, 11, 0.06); padding: 8px 12px; margin-bottom: 8px; border-radius: 4px;">
<span class="dia-speaker" style="color: #FBBF24;">👶 Bé Tin [00:00.0 – 00:02.5] (Âm Thanh Sinh Học Ngoài Khung Hình / Ghost Minor Cue): </span>
<span class="dia-bio-cue" style="color: #FDE68A; font-style: italic;">[Tiếng ọ ẹ ngằn ngặt đói sữa khẽ cọ chăn lót trong nôi gỗ phía xa, không xuất hiện hình ảnh]</span>
<div class="dia-bio-note" style="color: #D97706; font-size: 12px; margin-top: 4px;">🔊 Auditory Hook 3s: Tiếng ọ ẹ ngằn ngặt của trẻ sơ sinh đói sữa trong nôi đối lập trực tiếp với bình hút sữa cạn khô 0ml — kích hoạt nỗi đau bất lực tột cùng khiến nước mắt Duyên rơi vỡ màng cháo nguội.</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Mỹ Duyên [00:03.5 – 00:06.8]: </span>
<span class="dia-spoken-quote">"Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về..."</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về..." (12 từ)</div>
<div class="dia-subtext">(Nước mắt rơi vỡ màng cháo nguội đóng váng, buông rơi muỗng sứ xuống mâm nhôm bên cạnh bình hút sữa cạn khô)</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Minh Khang [00:07.5 – 00:10.0]: </span>
<span class="dia-spoken-quote">"Em đừng sợ... để anh pha sữa ngoài cho con, anh lo được hết mà em!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Em đừng sợ... để anh pha sữa ngoài cho con, anh lo được hết mà em!" (16 từ)</div>
<div class="dia-subtext">(Quỳ xuống nắm chặt đôi bàn tay lạnh cóng của vợ, nâng đỡ tinh thần và làm điểm tựa yêu thương)</div>
</div>
</div>'''
assert old_s1_dia in html, "old_s1_dia not found"
html = html.replace(old_s1_dia, new_s1_dia)

# Prompt p-01
old_p01_phase = '''[00:03.0–00:08.0] The pedestal lift slows through the final third and lands before my_duyen speaks, at my_duyen's eye level on a frontal medium close-up, then the frame holds still: my_duyen is positioned at screen-left on patterned floor tiles with back resting against the wooden headboard of the queen bed; in an exhausted physical state with slumped posture, my_duyen's chest heaves with shallow breaths as morning sunlight catches streaming tears over hollow cheeks, lips parting in weeping vulnerability to deliver dialogue:
my_duyen whispers : “ Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về... ” (Voice of a 24-year-old Southern Vietnamese woman; lips parting in trembling vulnerable Southern Vietnamese lip-sync, eyes streaming with tears of postpartum exhaustion)
In the soft-focus background, the wooden pine crib stands steady with soft white bedding.

[00:08.0–00:10.0] The camera glides back slightly into an intimate low-angle medium two-shot: minh_khang drops swiftly onto both knees on the patterned floor tiles facing my_duyen at the foot of the queen bed; in an upright kneeling posture with protective tension, minh_khang's broad warm palms reach out and clasp my_duyen's cold shaking hands against minh_khang's chest, then rests a forehead softly against the couple's joined hands; with unwavering devotion and silent sorrow, minh_khang's jaw sets with protective resolve. Supported against the bed frame, my_duyen slumps forward into minh_khang's clasp, weeping softly with quiet relief in minh_khang's warm embrace. Beside the bed, the wooden pine crib stands peaceful under warm sunbeams through 00:10.0.'''

new_p01_phase = '''[00:03.0–00:07.5] The pedestal lift slows through the final third and lands before my_duyen speaks, at my_duyen's eye level on a frontal medium close-up, then the frame holds still: my_duyen is positioned at screen-left on patterned floor tiles with back resting against the wooden headboard of the queen bed; in an exhausted physical state with slumped posture, my_duyen's chest heaves with shallow breaths as morning sunlight catches streaming tears over hollow cheeks, lips parting in weeping vulnerability to deliver dialogue:
my_duyen whispers : “ Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về... ” (Voice of a 24-year-old Southern Vietnamese woman; lips parting in trembling vulnerable Southern Vietnamese lip-sync, eyes streaming with tears of postpartum exhaustion)
In the soft-focus background, the wooden pine crib stands steady with soft white bedding.

[00:07.5–00:10.0] The camera glides back slightly into an intimate low-angle medium two-shot: minh_khang drops swiftly onto both knees on the patterned floor tiles facing my_duyen at the foot of the queen bed; in an upright kneeling posture with protective tension, minh_khang's broad warm palms reach out and clasp my_duyen's cold shaking hands against minh_khang's chest, resting a forehead softly against the couple's joined hands as lips part to deliver comforting dialogue:
minh_khang replies : “ Em đừng sợ... để anh pha sữa ngoài cho con, anh lo được hết mà em! ” (Voice of a 28-year-old Southern Vietnamese man; lips parting in warm comforting Southern Vietnamese lip-sync, forehead resting against joined hands)
Supported against the bed frame, my_duyen slumps forward into minh_khang's clasp, weeping softly with quiet relief in minh_khang's warm embrace. Beside the bed, the wooden pine crib stands peaceful under warm sunbeams through 00:10.0.'''
assert old_p01_phase in html, "old_p01_phase not found"
html = html.replace(old_p01_phase, new_p01_phase)

# Handover ho-01
old_ho_01 = 'Dialogue Audit: my_duyen 10 words (solo, ~2.5s of speech); minh_khang answers wordlessly with the grip.'
new_ho_01 = 'Dialogue Audit: my_duyen 12 words, minh_khang 16 words (28 words, ~6.2s of speech; call-and-response tender comfort).'
assert old_ho_01 in html, "old_ho_01 not found"
html = html.replace(old_ho_01, new_ho_01)
print("[+] Scene 01 updated.")


# ==============================================================================
# 2. SCENE 04 UPDATES
# ==============================================================================
# Spec pill
old_s4_spec = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Solo Bùng Nổ (Má Ba 12 từ • Duyên ngất lịm, không thốt nổi một lời)</span>'
new_s4_spec = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Đối Thoại San Sẻ (Má Ba 17 từ • Duyên 15 từ)</span>'
assert old_s4_spec in html, "old_s4_spec not found"
html = html.replace(old_s4_spec, new_s4_spec)

# Dia box 04
old_s4_dia = '''<div id="dia-04">
<div class="dia-item" style="border-left: 3px solid #F59E0B; background: rgba(245, 158, 11, 0.06); padding: 8px 12px; margin-bottom: 8px; border-radius: 4px;">
<span class="dia-speaker" style="color: #FBBF24;">👶 Bé Tin [00:02.0 – 00:04.5] (Âm Thanh Sinh Học): </span>
<span class="dia-bio-cue" style="color: #FDE68A; font-style: italic;">[Tiếng ọ ẹ khẽ chùng xuống khi được cha đặt nhẹ tay vỗ về lên mép chăn nôi]</span>
<div class="dia-bio-note" style="color: #D97706; font-size: 12px; margin-top: 4px;">🔊 Somatic Reaction: Khang khẽ vỗ về nôi con, đứng chắn phía trước bảo vệ giấc ngủ của bé và che chở vợ trước cơn nóng giận của mẹ.</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Má Ba [00:34.3 – 00:37.0]: </span>
<span class="dia-spoken-quote">"Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau!"</div>
<div class="dia-subtext">(Đặt nhẹ chiếc võng sang một bên, bước tới nhắc con dâu tựa lưng nghỉ ngơi)</div>
</div>
</div>'''

new_s4_dia = '''<div id="dia-04">
<div class="dia-item" style="border-left: 3px solid #F59E0B; background: rgba(245, 158, 11, 0.06); padding: 8px 12px; margin-bottom: 8px; border-radius: 4px;">
<span class="dia-speaker" style="color: #FBBF24;">👶 Bé Tin [00:02.0 – 00:04.5] (Âm Thanh Sinh Học): </span>
<span class="dia-bio-cue" style="color: #FDE68A; font-style: italic;">[Tiếng ọ ẹ khẽ chùng xuống khi được cha đặt nhẹ tay vỗ về lên mép chăn nôi]</span>
<div class="dia-bio-note" style="color: #D97706; font-size: 12px; margin-top: 4px;">🔊 Somatic Reaction: Khang khẽ vỗ về nôi con, đứng chắn phía trước bảo vệ giấc ngủ của bé và che chở vợ trước cơn nóng giận của mẹ.</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Má Ba [00:34.0 – 00:37.0]: </span>
<span class="dia-spoken-quote">"Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau!" (17 từ)</div>
<div class="dia-subtext">(Đặt nhẹ chiếc võng sang một bên, bước tới nhắc con dâu tựa lưng nghỉ ngơi)</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Mỹ Duyên [00:37.2 – 00:40.0]: </span>
<span class="dia-spoken-quote">"Dạ con cảm ơn má... con dở dang để má với anh Khang phải lo..."</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Dạ con cảm ơn má... con dở dang để má với anh Khang phải lo..." (15 từ)</div>
<div class="dia-subtext">(Tựa đầu vào gối, đôi mắt rưng lệ đáp lại sự quan tâm của mẹ chồng)</div>
</div>
</div>'''
assert old_s4_dia in html, "old_s4_dia not found"
html = html.replace(old_s4_dia, new_s4_dia)

# Prompt p-04
old_p04_phase = '''[00:04.0–00:10.0] The camera lands and settles before ma_ba speaks, framing ma_ba standing beside the queen bed facing my_duyen: in an upright stance offering the warm porcelain congee bowl, ma_ba's stern demeanor gives way to instinctive parental compassion as ma_ba speaks:
ma_ba says : “ Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in concerned maternal Southern Vietnamese lip-sync, stern tone softening into family care)
Resting back against the bolster pillow on the queen bed, my_duyen closes eyes gently, exhaling in quiet relief at the maternal tenderness. minh_khang turns quickly toward the doorway with eager filial relief to fetch warm water. Beside the bed, the wooden pine crib rests quiet in the warm morning light through 00:10.0.'''

new_p04_phase = '''[00:04.0–00:07.2] The camera lands and settles before ma_ba speaks, framing ma_ba standing beside the queen bed facing my_duyen: in an upright stance offering the warm porcelain congee bowl, ma_ba's stern demeanor gives way to instinctive parental compassion as ma_ba speaks:
ma_ba says : “ Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in concerned maternal Southern Vietnamese lip-sync, stern tone softening into family care)

[00:07.2–00:10.0] The camera gently tightens on my_duyen resting against the bolster pillow on the queen bed: pale face softening with tears of gratitude, my_duyen responds in a fragile, heartfelt whisper:
my_duyen whispers : “ Dạ con cảm ơn má... con dở dang để má với anh Khang phải lo... ” (Voice of a 24-year-old Southern Vietnamese woman; lips parting in fragile emotional Southern Vietnamese lip-sync, eyes glistening with filial gratitude)
minh_khang turns quickly toward the doorway with eager filial relief to fetch warm water. Beside the bed, the wooden pine crib rests quiet in the warm morning light through 00:10.0.'''
assert old_p04_phase in html, "old_p04_phase not found"
html = html.replace(old_p04_phase, new_p04_phase)

# Handover ho-04
old_ho_04 = 'Dialogue Audit: ma_ba 12 words (solo, ~3.0s of speech); my_duyen collapses without a word.'
new_ho_04 = 'Dialogue Audit: ma_ba 17 words, my_duyen 15 words (32 words, ~7.0s of speech; call-and-response shared concern).'
assert old_ho_04 in html, "old_ho_04 not found"
html = html.replace(old_ho_04, new_ho_04)
print("[+] Scene 04 updated.")


# ==============================================================================
# 3. SCENE 05 UPDATES
# ==============================================================================
# Spec pill
old_s5_spec = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Solo Bàng Hoàng (Má Ba 14 từ • Khang và Duyên im lặng)</span>'
new_s5_spec = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Đối Thoại Bộc Bạch (Má Ba 17 từ • Khang 18 từ)</span>'
assert old_s5_spec in html, "old_s5_spec not found"
html = html.replace(old_s5_spec, new_s5_spec)

# Dia box 05
old_s5_dia = '''<div id="dia-05">
<div class="dia-item" style="border-left: 3px solid #F59E0B; background: rgba(245, 158, 11, 0.06); padding: 8px 12px; margin-bottom: 8px; border-radius: 4px;">
<span class="dia-speaker" style="color: #FBBF24;">👶 Bé Tin [00:01.0 – 00:03.5] (Âm Thanh Sinh Học): </span>
<span class="dia-bio-cue" style="color: #FDE68A; font-style: italic;">[Tiếng e e thở nhẹ khi trở mình tự nhiên, lưng thẳng an toàn trên đệm y khoa phẳng]</span>
<div class="dia-bio-note" style="color: #D97706; font-size: 12px; margin-top: 4px;">🔊 Foley Cue: Nhịp thở êm đềm của bé đối lập với cơn bão tâm lý nghẹt thở đang bùng nổ giữa hai người phụ nữ.</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Má Ba [00:44.8 – 00:47.8]: </span>
<span class="dia-spoken-quote">"Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?!"</div>
<div class="dia-subtext">(Bàng hoàng nhìn miếng băng dán y tế ở cổ tay con dâu — tự ái và tổn thương trào dâng vì con dâu đi trạm xá một mình như xem mẹ là người dưng)</div>
</div>
</div>'''

new_s5_dia = '''<div id="dia-05">
<div class="dia-item" style="border-left: 3px solid #F59E0B; background: rgba(245, 158, 11, 0.06); padding: 8px 12px; margin-bottom: 8px; border-radius: 4px;">
<span class="dia-speaker" style="color: #FBBF24;">👶 Bé Tin [00:01.0 – 00:03.5] (Âm Thanh Sinh Học): </span>
<span class="dia-bio-cue" style="color: #FDE68A; font-style: italic;">[Tiếng e e thở nhẹ khi trở mình tự nhiên, lưng thẳng an toàn trên đệm y khoa phẳng]</span>
<div class="dia-bio-note" style="color: #D97706; font-size: 12px; margin-top: 4px;">🔊 Foley Cue: Nhịp thở êm đềm của bé đối lập với cơn bão tâm lý nghẹt thở đang bùng nổ giữa hai người phụ nữ.</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Má Ba [00:44.0 – 00:47.0]: </span>
<span class="dia-spoken-quote">"Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?!" (17 từ)</div>
<div class="dia-subtext">(Bàng hoàng nhìn miếng băng dán y tế ở cổ tay con dâu — tự ái và tổn thương trào dâng vì cảm thấy bị qua mặt)</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Minh Khang [00:47.2 – 00:50.0]: </span>
<span class="dia-spoken-quote">"Má nhìn đi! Đêm qua Duyên sốt bốn mươi độ, con phải bế đi cấp cứu đó má!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Má nhìn đi! Đêm qua Duyên sốt bốn mươi độ, con phải bế đi cấp cứu đó má!" (18 từ)</div>
<div class="dia-subtext">(Khang nghẹn ngào thốt lên sự thật đớn đau trong vòng tay ôm chặt che chở vợ)</div>
</div>
</div>'''
assert old_s5_dia in html, "old_s5_dia not found"
html = html.replace(old_s5_dia, new_s5_dia)

# Prompt p-05
old_p05_phase = '''[00:04.0–00:10.0] Cut to the reverse eye-level close-up of ma_ba on the 180-degree axis, static camera: ma_ba kneels upright facing the bed; in a stunned physical freeze with fingers hovering in mid-air beside the exposed medical tape, ma_ba's eyes widen in disbelief, throat tightening with acute hurt as injured matriarchal pride surges and ma_ba speaks:
ma_ba says : “ Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in choked sharp Southern Vietnamese lip-sync, eyes wide with bitter wounded pride)
The frame holds as ma_ba stares at the clinic bandage: in the background, my_duyen sits curled against minh_khang's chest, tucking the wrist away in tearful shame; minh_khang holds my_duyen with defensive resolve as heavy silence thickens through 00:10.0; the wooden pine crib stands quiet beside the bed.'''

new_p05_phase = '''[00:04.0–00:10.0] Cut to the reverse eye-level shot on the 180-degree axis: ma_ba kneels upright facing the bed; in a stunned physical freeze with fingers hovering in mid-air beside the exposed medical tape, ma_ba's eyes widen in disbelief, throat tightening with acute hurt as injured matriarchal pride surges and ma_ba speaks:
ma_ba snaps : “ Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in choked sharp Southern Vietnamese lip-sync, eyes wide with bitter wounded pride)
Holding my_duyen tightly against chest in the background, tears of protective desperation welling in eyes, minh_khang looks directly at ma_ba and replies with raw emotion:
minh_khang cries : “ Má nhìn đi! Đêm qua Duyên sốt bốn mươi độ, con phải bế đi cấp cứu đó má! ” (Voice of a 28-year-old Southern Vietnamese man; lips parting in anguished desperate Southern Vietnamese lip-sync, clutching wife firmly)
The frame holds as ma_ba freezes in stunned silence, overwhelmed by the harsh reality; the wooden pine crib stands quiet beside the bed through 00:10.0.'''
assert old_p05_phase in html, "old_p05_phase not found"
html = html.replace(old_p05_phase, new_p05_phase)

# Handover ho-05
old_ho_05 = 'Dialogue Audit: ma_ba 14 words (solo confrontation, ~3.5s of speech); my_duyen tries to hide the clinic tape, silence answers.'
new_ho_05 = 'Dialogue Audit: ma_ba 17 words, minh_khang 18 words (35 words, ~7.5s of speech; dramatic revelation call-and-response).'
assert old_ho_05 in html, "old_ho_05 not found"
html = html.replace(old_ho_05, new_ho_05)
print("[+] Scene 05 updated.")


# ==============================================================================
# 4. SCENE 08 UPDATES
# ==============================================================================
# Spec pill
old_s8_spec = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Solo Cay Đắng (Má Ba 16 từ • Khang và Duyên câm lặng)</span>'
new_s8_spec = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Đối Thoại Giằng Xé (Má Ba 16 từ • Khang 16 từ)</span>'
assert old_s8_spec in html, "old_s8_spec not found"
html = html.replace(old_s8_spec, new_s8_spec)

# Dia box 08
old_s8_dia = '''<div id="dia-08">
<div class="dia-item">
<span class="dia-speaker">Má Ba [01:13.5 – 01:17.2]: </span>
<span class="dia-spoken-quote">"Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao!"</div>
<div class="dia-subtext">(Nhìn chiếc võng bị chối bỏ dưới đất, buông lời nguyền tự ái trước khi quay gót bước đi)</div>
</div>
</div>'''

new_s8_dia = '''<div id="dia-08">
<div class="dia-item">
<span class="dia-speaker">Má Ba [01:13.0 – 01:16.5]: </span>
<span class="dia-spoken-quote">"Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao!" (16 từ)</div>
<div class="dia-subtext">(Nhìn chiếc võng bị chối bỏ dưới đất, buông lời trách móc tự ái trước khi quay gót)</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Minh Khang [01:16.8 – 01:20.0]: </span>
<span class="dia-spoken-quote">"Má ơi... tụi con đâu dám xua đuổi, má đừng bỏ về lúc này mà má!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Má ơi... tụi con đâu dám xua đuổi, má đừng bỏ về lúc này mà má!" (16 từ)</div>
<div class="dia-subtext">(Khang bước với theo phía ngưỡng cửa, nghẹn ngào van xin mẹ ở lại)</div>
</div>
</div>'''
assert old_s8_dia in html, "old_s8_dia not found"
html = html.replace(old_s8_dia, new_s8_dia)

# Prompt p-08
old_p08_phase = '''[00:03.8–00:10.0] ma_ba raises chin and glares across the bedroom with cold finality: standing at the wooden threshold, ma_ba snaps gaze toward the queen bed, chin lifted high in defiant pride as lips tighten with bitter rebuke:
ma_ba snaps : “ Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in icy bitter Southern Vietnamese lip-sync, lips tightened with stubborn pride)
The camera tracks slowly backward as ma_ba turns sharply away from the bedroom and exits down the hallway through 00:10.0. minh_khang stands frozen in place beside the crib, watching mother depart in heavy silence. On the queen bed, my_duyen weeps silently into hands. The wooden pine crib stands quiet beside the bed.'''

new_p08_phase = '''[00:03.8–00:07.0] ma_ba raises chin and glares across the bedroom with cold finality: standing at the wooden threshold, ma_ba snaps gaze toward the queen bed, chin lifted high in defiant pride as lips tighten with bitter rebuke:
ma_ba snaps : “ Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in icy bitter Southern Vietnamese lip-sync, lips tightened with stubborn pride)
ma_ba turns sharply away from the bedroom doorway toward the hallway.

[00:07.0–00:10.0] The camera glides swiftly to frame minh_khang rushing two steps toward the doorway threshold: palms raised in anguished supplication, brow furrowed in acute emotional desperation, minh_khang calls out after ma_ba:
minh_khang pleads : “ Má ơi... tụi con đâu dám xua đuổi, má đừng bỏ về lúc này mà má! ” (Voice of a 28-year-old Southern Vietnamese man; lips parting in desperate filial Southern Vietnamese lip-sync, eyes brimming with tears)
On the queen bed, my_duyen weeps silently into hands. The wooden pine crib stands quiet beside the bed through 00:10.0.'''
assert old_p08_phase in html, "old_p08_phase not found"
html = html.replace(old_p08_phase, new_p08_phase)

# Handover ho-08
old_ho_08 = 'Dialogue Audit: ma_ba 16 words (solo ultimatum, ~4.0s of speech).'
new_ho_08 = 'Dialogue Audit: ma_ba 16 words, minh_khang 16 words (32 words, ~7.0s of speech; bitter fracture call-and-response).'
assert old_ho_08 in html, "old_ho_08 not found"
html = html.replace(old_ho_08, new_ho_08)
print("[+] Scene 08 updated.")


# ==============================================================================
# 5. SCENE 09 UPDATES
# ==============================================================================
# Spec pill
old_s9_spec = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Solo Than Thở Bế Tắc (Duyên 14 từ • Khang ôm vợ trong im lặng)</span>'
new_s9_spec = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Đối Thoại Yêu Thương (Duyên 17 từ • Khang 16 từ)</span>'
assert old_s9_spec in html, "old_s9_spec not found"
html = html.replace(old_s9_spec, new_s9_spec)

# Dia box 09
old_s9_dia = '''<div id="dia-09">
<div class="dia-item">
<span class="dia-speaker">Mỹ Duyên [01:24.5 – 01:27.5]: </span>
<span class="dia-spoken-quote">"Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này..."</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này..."</div>
<div class="dia-subtext">(Gục đầu vào ngực chồng, lời thú nhận kiệt cùng của người mẹ trẻ bị bủa vây giữa trầm cảm và định kiến)</div>
</div>
</div>'''

new_s9_dia = '''<div id="dia-09">
<div class="dia-item">
<span class="dia-speaker">Mỹ Duyên [01:23.5 – 01:26.5]: </span>
<span class="dia-spoken-quote">"Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này..."</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này..." (17 từ)</div>
<div class="dia-subtext">(Gục đầu vào ngực chồng, lời thú nhận kiệt cùng của người mẹ trẻ bị bủa vây giữa trầm cảm và định kiến)</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Minh Khang [01:26.8 – 01:30.0]: </span>
<span class="dia-spoken-quote">"Em ráng gượng nghen em... có anh ở đây, anh bảo bọc mẹ con em mà!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Em ráng gượng nghen em... có anh ở đây, anh bảo bọc mẹ con em mà!" (16 từ)</div>
<div class="dia-subtext">(Ôm chặt lấy vai vợ, thì thầm an ủi bằng tình thương sắt son của người chồng)</div>
</div>
</div>'''
assert old_s9_dia in html, "old_s9_dia not found"
html = html.replace(old_s9_dia, new_s9_dia)

# Prompt p-09
old_p09_phase = '''[00:04.2–00:10.0] The camera pushes in close to my_duyen's tear-streaked face resting against minh_khang's shoulder: held in minh_khang's arms on the queen bed, my_duyen's pale hollow cheeks glisten with streaming tears; in total physical depletion, drained of all fight, my_duyen parts trembling lips to speak in a muffled, sorrowful whisper against minh_khang's chest:
my_duyen whispers : “ Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này... ” (Voice of a 24-year-old Southern Vietnamese woman; lips parting in broken faint Southern Vietnamese lip-sync, muffled against shoulder, drained of fight)
minh_khang closes eyes, jaw clenching in silent heartache, arms tightening around my_duyen as the frame holds still through 00:10.0. In the background, the wooden pine crib rests quiet under the warm morning sunbeams.'''

new_p09_phase = '''[00:04.2–00:07.2] The camera pushes in close to my_duyen's tear-streaked face resting against minh_khang's shoulder: held in minh_khang's arms on the queen bed, my_duyen's pale hollow cheeks glisten with streaming tears; in total physical depletion, drained of all fight, my_duyen parts trembling lips to speak in a muffled, sorrowful whisper against minh_khang's chest:
my_duyen whispers : “ Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này... ” (Voice of a 24-year-old Southern Vietnamese woman; lips parting in broken faint Southern Vietnamese lip-sync, muffled against shoulder, drained of fight)

[00:07.2–00:10.0] minh_khang holds my_duyen tighter against chest, resting chin tenderly over my_duyen's trembling hair, parting lips to answer in a warm, protective whisper:
minh_khang replies : “ Em ráng gượng nghen em... có anh ở đây, anh bảo bọc mẹ con em mà! ” (Voice of a 28-year-old Southern Vietnamese man; lips parting in tender devoted Southern Vietnamese lip-sync, arms embracing wife securely)
In the soft-focus background, the wooden pine crib rests quiet under the warm morning sunbeams through 00:10.0.'''
assert old_p09_phase in html, "old_p09_phase not found"
html = html.replace(old_p09_phase, new_p09_phase)

# Handover ho-09
old_ho_09 = 'Dialogue Audit: my_duyen 14 words (solo despair, ~3.5s of speech).'
new_ho_09 = 'Dialogue Audit: my_duyen 17 words, minh_khang 16 words (33 words, ~7.0s of speech; intimate mutual comfort call-and-response).'
assert old_ho_09 in html, "old_ho_09 not found"
html = html.replace(old_ho_09, new_ho_09)
print("[+] Scene 09 updated.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\n[SUCCESS] All 5 scenes successfully updated in output/com-khong-chan-nuoc-mat/tap-1.html!")

import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ==============================================================================
# SCENE 01 UPDATES
# ==============================================================================
# 1. Update spec-pill for s-01
old_spec_01 = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Solo Một Lời Than (Duyên 10 từ • Khang im lặng, đáp bằng cái siết tay)</span>'
new_spec_01 = '<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Đối Thoại Nâng Đỡ (Duyên 12 từ • Khang 16 từ)</span>'
assert old_spec_01 in html, "old_spec_01 not found"
html = html.replace(old_spec_01, new_spec_01)

# 2. Update dia-01 to include Minh Khang's response
old_dia_01 = '''<div id="dia-01">
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

new_dia_01 = '''<div id="dia-01">
<div class="dia-item" style="border-left: 3px solid #F59E0B; background: rgba(245, 158, 11, 0.06); padding: 8px 12px; margin-bottom: 8px; border-radius: 4px;">
<span class="dia-speaker" style="color: #FBBF24;">👶 Bé Tin [00:00.0 – 00:02.5] (Âm Thanh Sinh Học Ngoài Khung Hình / Ghost Minor Cue): </span>
<span class="dia-bio-cue" style="color: #FDE68A; font-style: italic;">[Tiếng ọ ẹ ngằn ngặt đói sữa khẽ cọ chăn lót trong nôi gỗ phía xa, không xuất hiện hình ảnh]</span>
<div class="dia-bio-note" style="color: #D97706; font-size: 12px; margin-top: 4px;">🔊 Auditory Hook 3s: Tiếng ọ ẹ ngằn ngặt của trẻ sơ sinh đói sữa trong nôi đối lập trực tiếp với bình hút sữa cạn khô 0ml — kích hoạt nỗi đau bất lực tột cùng khiến nước mắt Duyên rơi vỡ màng cháo nguội.</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Mỹ Duyên [00:03.5 – 00:06.5]: </span>
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
assert old_dia_01 in html, "old_dia_01 not found"
html = html.replace(old_dia_01, new_dia_01)

# 3. Update p-01 prompt
old_p_01_last = '''[00:08.0–00:10.0] The camera glides back slightly into an intimate low-angle medium two-shot: minh_khang drops swiftly onto both knees on the patterned floor tiles facing my_duyen at the foot of the queen bed; in an upright kneeling posture with protective tension, minh_khang's broad warm palms reach out and clasp my_duyen's cold shaking hands against minh_khang's chest, then rests a forehead softly against the couple's joined hands; with unwavering devotion and silent sorrow, minh_khang's jaw sets with protective resolve. Supported against the bed frame, my_duyen slumps forward into minh_khang's clasp, weeping softly with quiet relief in minh_khang's warm embrace. Beside the bed, the wooden pine crib stands peaceful under warm sunbeams through 00:10.0.'''

new_p_01_last = '''[00:07.5–00:10.0] The camera glides back slightly into an intimate low-angle medium two-shot: minh_khang drops swiftly onto both knees on the patterned floor tiles facing my_duyen at the foot of the queen bed; in an upright kneeling posture with protective tension, minh_khang's broad warm palms reach out and clasp my_duyen's cold shaking hands against minh_khang's chest, resting a forehead softly against the couple's joined hands as lips part to deliver comforting dialogue:
minh_khang replies : “ Em đừng sợ... để anh pha sữa ngoài cho con, anh lo được hết mà em! ” (Voice of a 28-year-old Southern Vietnamese man; lips parting in warm comforting Southern Vietnamese lip-sync, forehead resting against joined hands)
Supported against the bed frame, my_duyen slumps forward into minh_khang's clasp, weeping softly with quiet relief in minh_khang's warm embrace. Beside the bed, the wooden pine crib stands peaceful under warm sunbeams through 00:10.0.'''
assert old_p_01_last in html, "old_p_01_last not found"
html = html.replace(old_p_01_last, new_p_01_last)

# 4. Update ho-01 Dialogue Audit line
old_ho_01 = 'Dialogue Audit: my_duyen 10 words (solo, ~2.5s of speech); minh_khang silent comfort.'
new_ho_01 = 'Dialogue Audit: my_duyen 12 words, minh_khang 16 words (call-and-response tender comfort).'
assert old_ho_01 in html, "old_ho_01 not found"
html = html.replace(old_ho_01, new_ho_01)

print("Scene 01 updated successfully!")

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

tap1_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(tap1_path, 'r', encoding='utf-8') as f:
    t = f.read()

# 1. Purge Scene 01 triggers:
t = t.replace('an old faded purple bruise on wrist', 'a pale wrist from exhaustion')
t = t.replace('bruise on wrist', 'pale wrist')
t = t.replace('clattering plastic pump bottle', 'resting plastic pump bottle')
t = t.replace('clattering against floor', 'resting against floor')

# 2. Purge Scene 04: Fainting/collapsing/crashing steel hammock near infant
t = t.replace('B3B Drama 2 — Cơn Kiệt Sức Đột Ngột (Near-Miss Collapse)', 'B3B Drama 2 — Nỗi Kiệt Sức Nghẹn Ngào (Emotional Breaking Point)')
t = t.replace('vong_xep: slipped from hands and crashing onto floor tiles; noi_go: stationary beside collapsing Mỹ Duyên', 'vong_xep: placed gently against bedroom wall; noi_go: stationary in room center')
t = t.replace('Dull thud of knees hitting floor tiles, sharp gasp of physical pain, infant whimpering inside pine crib, sudden silence of shock.', 'Soft rustle of cotton bolster pillow, maternal sigh of concern, quiet bedroom atmosphere.')
t = t.replace('Single Continuous Take (Unbroken Downward Tracking Descent to Panic Rescue)', 'Single Continuous Take (Level Tracking on Maternal Care and Exhaustion)')
t = t.replace("At Mỹ Duyên's own low eye level beside the crib rail, the unbroken camera frames her three-quarter front as she attempts to push up from the floor tiles using the crib rail to apologize. Her face drains of color, eyelashes flutter shut, and her knees buckle like lead, sliding limply down the balusters toward the tiles.<br/>Her lips part, but no apology comes — only a thin, shaking exhale, and the camera sinks with her to floor level.<br/><br/>The camera, already at floor level, stays low and waits: Má Ba gasps in horror, her weathered hands instinctively unclamping as the steel hammock stand crashes loudly onto the floor tiles. Má Ba drops to her knees — down into the lens's eye line — beside Minh Khang, who slides across the floor, catching Duyên's falling shoulders before her head touches the tiles.<br/>Má Ba: “Duyên ơi coi chừng té! Khang ơi, vô đỡ vợ mầy lẹ lên con!” (Voice of a 56-year-old Southwestern Vietnamese woman; terrified maternal cry lip-sync, harsh anger instantly shattering into raw maternal panic)<br/>The camera settles low on the tiles: the fallen hammock rests static beside them as both Má Ba and Khang desperately support the unconscious mother.",
              "At bed level, the unbroken camera frames Mỹ Duyên three-quarter front as she sits on the edge of the queen bed, leaning back against the wooden headboard, breathing heavily with postpartum fatigue.<br/>Minh Khang steps in and gently places a soft bolster pillow behind her back, carefully taking the empty pump bottle from her trembling fingers.<br/><br/>Má Ba steps into the room holding the warm congee bowl; seeing her daughter-in-law's pale exhaustion, her defensive anger softens instantly into genuine maternal care:<br/>Má Ba: “Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau!” (Voice of a 56-year-old Southwestern Vietnamese woman; worried maternal lip-sync, anger softening into natural protective care)<br/>The camera holds on the couple as Má Ba steps toward the bedside through 00:10.0.")

t = t.replace('"Duyên ơi coi chừng té! Khang ơi, vô đỡ vợ mầy lẹ lên con!"', '"Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau!"')
t = t.replace('(Đánh rơi chiếc võng sắt xuống sàn, thất kinh quỳ sụp xuống túm lấy tay dâu)', '(Đặt nhẹ chiếc võng sang một bên, bước tới nhắc con dâu tựa lưng nghỉ ngơi)')

# Scene 04 Code Block 1 prompt:
t = t.replace('unbroken single-shot downward tracking descent across ten seconds', 'gentle level tracking shot settling on bedside care across ten seconds')
t = t.replace("my_duyen [Appearance, attire, and facial features Refer to image 1], attempting to push up using pine crib rail, facial color draining completely, knees buckling limply toward floor tiles — the only my_duyen in frame.\nma_ba [Appearance, attire, and facial features Refer to image 4], dropping steel hammock frame in shock, falling to both knees in frantic panic — the only ma_ba in frame.\nminh_khang [Appearance, attire, and facial features Refer to image 2], lunging across floor tiles to catch falling my_duyen before impact — the only minh_khang in frame.",
              "my_duyen [Appearance, attire, and facial features Refer to image 1], sitting on the edge of the queen bed, leaning back against wooden headboard, pale with postpartum fatigue — the only my_duyen in frame.\nminh_khang [Appearance, attire, and facial features Refer to image 2], standing beside bed, placing a soft bolster pillow behind my_duyen's back — the only minh_khang in frame.\nma_ba [Appearance, attire, and facial features Refer to image 4], standing near bedroom doorway holding warm congee bowl, weathered face softening with maternal concern — the only ma_ba in frame.")
t = t.replace('vong_xep [100% Refer to image prop_hammock_4view.jpg], fallen stainless steel hammock clattering onto floor tiles — the only vong_xep in frame.',
              'vong_xep [100% Refer to image prop_hammock_4view.jpg], folded stainless steel hammock resting static against bedroom wall; bat_chao [100% Refer to image prop_chao_thit_4view.jpg], held in ma_ba\'s hands — the only vong_xep and bat_chao in frame.')
t = t.replace('sharp metallic clatter of dropped hammock frame, gasp of maternal horror, rustle of collapsing fabric, muffled cry of panic',
              'soft rustle of bedding fabric, gentle footstep on floor tiles, maternal voice of tender concern')

t = t.replace("[00:00–00:04.0] At my_duyen's own low eye level beside the crib rail, a three-quarter front close shot: my_duyen attempts to push up from patterned floor tiles using the pine crib rail to apologize. Facial color drains completely as eyelids flutter shut and knees buckle like lead, sliding down the balusters toward floor tiles. Pale lips part, but no words come — only a thin, shaking exhale as the head tilts limp with postpartum exhaustion, and the camera sinks with my_duyen all the way down to floor level.",
              "[00:00–00:04.0] At bed eye level, a three-quarter front medium shot on the queen bed: my_duyen sits on the bed mattress, leaning back against the wooden headboard, breathing heavily with postpartum fatigue. minh_khang steps up to the bedside and gently places a soft cotton bolster pillow behind my_duyen's back, taking the empty plastic pump bottle from my_duyen's trembling fingers.")

t = t.replace("[00:04.0–00:10.0] The camera, already settled at floor level beside my_duyen, stays low and waits: above the frame ma_ba gasps in horror, hands unclamping as the steel hammock stand clatters onto floor tiles. ma_ba drops to both knees beside minh_khang, who lunges forward and catches my_duyen's falling shoulders before contact with floor tiles, and ma_ba's face comes down into the lens's eye line, three-quarter front:\nma_ba: “ Duyên ơi coi chừng té! Khang ơi, vô đỡ vợ mầy lẹ lên con! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in terrified maternal cry Southern Vietnamese lip-sync, harsh anger shattering into raw maternal panic)\nThe camera settles low on floor tiles as both ma_ba and minh_khang desperately cradle the unconscious mother through 00:10.0.",
              "[00:04.0–00:10.0] The camera pans smoothly across to ma_ba standing near the bed holding the warm congee bowl: seeing my_duyen resting pale against the bolster pillow, ma_ba's stern expression softens with instinctive maternal concern, stepping closer to the bedside:\nma_ba: “ Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in concerned maternal Southern Vietnamese lip-sync, stern tone softening into family care)\nThe frame holds as ma_ba approaches the bedside through 00:10.0.")

t = t.replace("- my_duyen: Slumped on floor tiles supported by minh_khang's arms, head leaning against his chest, eyes half-closed in exhaustion.",
              "- my_duyen: Sitting on queen bed supported by bolster pillow, resting head back with eyes closed in fatigue.")
t = t.replace("- ma_ba: Kneeling on floor tiles beside my_duyen, face white with panic.",
              "- ma_ba: Standing beside bed holding congee bowl, looking at my_duyen with worried maternal eyes.")

# 3. Purge Scene 05: Bruises/bầm dập/infusion trauma
t = t.replace('B4 Climax — Vết Bầm Tím Lộ Diện (Discovery Twist)', 'B4 Climax — Bí Mật Trạm Xá Lộ Diện (Discovery Twist)')
t = t.replace('dark purple needle bruises and peeling medical tape on Mỹ Duyên\'s slender wrist', 'neat white medical adhesive tape from the local clinic on Mỹ Duyên\'s wrist')
t = t.replace('dark purple needle bruises and peeling medical tape on Duyên\'s slender wrist are exposed sharp in the foreground. Duyên weakly twists her wrist away, but it is too late.<br/><br/>[00:04.0–00:10.0] Shot 2 — Cut to the reverse eye-level close-up on Má Ba on the 180° axis, static camera:<br/>Má Ba\'s fingers freeze in mid-air above the bruised wrist. Her eyes widen not with tender pity, but with wounded, stunned shock; her throat tightens and her jaw trembles with bitter disbelief:<br/>Má Ba: “Trời đất ơi... tay mầy bầm dập vầy nè, truyền nước biển hồi nào sao giấu tao?!” (Voice of a 56-year-old Southwestern Vietnamese woman; choked, sharp Southern lip-sync, eyes wide with bitter wounded disbelief)<br/>The frame holds as Má Ba stares at the bruises, the silence thickening with unspoken accusation through 00:10.0.',
              'neat white medical tape from the local health station on Duyên\'s slender wrist is exposed in the foreground. Duyên gently pulls her sleeve down to cover it, but Má Ba has already seen it.<br/><br/>[00:04.0–00:10.0] Shot 2 — Cut to the reverse eye-level close-up on Má Ba on the 180° axis, static camera:<br/>Má Ba\'s fingers freeze in mid-air. Her eyes widen not with tender pity, but with wounded, stunned disbelief, realizing Duyên went to the outpatient clinic alone in secret:<br/>Má Ba: “Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?!” (Voice of a 56-year-old Southwestern Vietnamese woman; choked, sharp Southern lip-sync, eyes wide with bitter wounded pride)<br/>The frame holds as Má Ba stares at the medical tape, the silence thickening with unspoken accusation through 00:10.0.')

t = t.replace('"Trời đất ơi... tay mầy bầm dập vầy nè, truyền nước biển hồi nào sao giấu tao?!"',
              '"Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?!"')
t = t.replace('(Bàng hoàng nhìn vết bầm kim truyền dịch tím tái — tự ái và tổn thương trào dâng vì bị con dâu giấu bệnh như người dưng)',
              '(Bàng hoàng nhìn miếng băng dán y tế ở cổ tay con dâu — tự ái và tổn thương trào dâng vì con dâu đi trạm xá một mình như xem mẹ là người dưng)')

t = t.replace('dark purple infusion bruises and peeling medical tape on my_duyen\'s slender wrist are exposed sharp in the foreground; my_duyen weakly twists the wrist away, but the secret is out; minh_khang\'s lips press shut in dread.',
              'a neat white square of medical adhesive tape on my_duyen\'s slender wrist is exposed in the foreground; my_duyen gently turns the wrist away, but ma_ba has already seen the clinic bandage; minh_khang\'s lips press shut in anxious silence.')

t = t.replace('ma_ba\'s fingers freeze in mid-air above the bruised wrist; ma_ba\'s eyes widen not with tender pity, but with wounded stunned disbelief, throat tightening, weathered jaw trembling with bitter hurt:\nma_ba: “ Trời đất ơi... tay mầy bầm dập vầy nè, truyền nước biển hồi nào sao giấu tao?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in choked sharp Southern Vietnamese lip-sync, eyes wide with bitter wounded disbelief)\nThe frame holds as ma_ba stares at the bruises, the silence thickening with unspoken accusation through 00:10.0.',
              'ma_ba\'s fingers freeze in mid-air beside the medical tape; ma_ba\'s eyes widen with wounded stunned disbelief, throat tightening with bitter hurt that my_duyen visited the outpatient clinic in secret:\nma_ba: “ Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in choked sharp Southern Vietnamese lip-sync, eyes wide with bitter wounded pride)\nThe frame holds as ma_ba stares at the white clinic bandage, the silence thickening with unspoken accusation through 00:10.0.')

t = t.replace('fumbling weakly to pull sleeve over bruised wrist', 'gently pulling sleeve down over bandaged wrist')
t = t.replace('bruised wrist exposed', 'bandaged wrist exposed')
t = t.replace('my_duyen tries to hide the IV bruises, silence answers.', 'my_duyen tries to hide the clinic tape, silence answers.')
t = t.replace('my_duyen jerks her bruised wrist back defensively in Scene 06.', 'my_duyen tucks her bandaged wrist behind her back in Scene 06.')

# 4. Purge Scene 06 & 09 & Handover triggers:
t = t.replace('wrist tucked behind back', 'bandaged wrist tucked behind back')
t = t.replace('holding her bruised hand in silent shared grief', 'holding her bandaged wrist in silent shared comfort')
t = t.replace('holding her bruised hand', 'holding her bandaged wrist')

with open(tap1_path, 'w', encoding='utf-8') as f:
    f.write(t)

print("Purged all harmful content triggers from tap-1.html!")

"""
Rewrite Scenes 05-10 of tap-1.html to align with Sven Creative Doctrine §8.11, §8.12
and setting.html Section 5B (Act 1 Pilot: Zero Premature Reconciliation, True Escalation).
Includes varied phase splits and strict Multi-Modal Reference Anchor Syntax.
"""
import os
import re
import sys

ROOT = r"d:\Project\Sven\output\com-khong-chan-nuoc-mat"
TAP_PATH = os.path.join(ROOT, "tap-1.html")
ENGINE = r"d:\Project\Sven\engine"
sys.path.insert(0, ENGINE)

with open(TAP_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# SCENE 05 REPLACEMENT
s05_new = '''<!-- ==================== SCENE 05 ==================== -->
<div class="scene-card" id="s-05">
<div class="scene-header">
<div class="scene-title-wrap">
<span class="scene-badge">SCENE 05 (CUE-05)</span>
<strong style="font-size:15px; color:#FFF;">B4 Climax — Vết Bầm Tím Lộ Diện (Discovery Twist)</strong>
</div>
<div style="display:flex; align-items:center; gap:10px;">
<span class="paradigm-pill" style="background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3);">Track B · Multi-Shot (1 Cut · 180° Axis)</span>
<span class="scene-time">00:40 – 00:50</span>
</div>
</div>
<!-- Diurnal Time of Day & Lighting Specifications Bar -->
<div class="diurnal-bar">
<span style="font-size: 12.5px; color: var(--gold); font-weight: 700;">⏰ <strong>Thời Gian Trong Ngày:</strong> 06:06 AM Ban Mai • Bàng Hoàng Sững Sờ & Sự Thật Lộ Diện</span>
<span style="color: rgba(255,255,255,0.2);">|</span>
<span style="font-size: 12px; color: #93C5FD; font-family: 'JetBrains Mono', monospace;">🌡️ <strong>Ánh Sáng &amp; Cảm Xúc:</strong> Ánh Sáng Đối Kháng Căng Thẳng</span>
</div>
<!-- Specs Bar: Characters, Environment, Props, Dialogue Standard -->
<div class="specs-bar">
<span class="spec-pill">👥 <strong>Nhân vật:</strong> 👵 Má Ba (B1) • 👩 Mỹ Duyên (A1) • 👨 Minh Khang (A2) • 👶 Bé Tin (Asset 0 / Image 3 — Ngủ ngoan trên đệm phẳng)</span>
<span class="spec-pill">🌲 <strong>Bối cảnh:</strong> phong_cu</span>
<span class="spec-pill">🛡️ <strong>Đạo cụ:</strong> vong_xep • noi_go</span>
<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Solo Bàng Hoàng (Má Ba 14 từ • Khang và Duyên im lặng)</span>
</div>
<div class="tier1-audit-card">
<div class="tier1-header">🎬 TIER 1: BẢNG KIỂM TOÁN ĐẠO DIỄN (DIRECTOR'S AUDIT CARD)</div>
<table class="tier1-table">
<tr>
<td class="tier1-label">[STYLE &amp; OPTICS]</td>
<td class="tier1-val">Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish.</td>
</tr>
<tr>
<td class="tier1-label">[CONTEXT]</td>
<td class="tier1-val">phong_cu — Master bedroom floor beside wooden crib. Morning sunlight cutting across patterned floor tiles, catching dark purple needle bruises and peeling medical tape on Mỹ Duyên's slender wrist.</td>
</tr>
<tr>
<td class="tier1-label">[SUBJECT]</td>
<td class="tier1-val">Minh Khang [Appearance, attire, and facial features Refer to image 2], kneeling on floor tiles supporting Mỹ Duyên's shoulders, gaze tense and fearful — the only Minh Khang in frame. Mỹ Duyên [Appearance, attire, and facial features Refer to image 1], slumped weak against Minh Khang, pale face, fumbling weakly to pull sleeve down over wrist — the only Mỹ Duyên in frame. Má Ba [Appearance, attire, and facial features Refer to image 4], kneeling on floor tiles, weathered hand caught on Mỹ Duyên's sleeve, eyes wide with stunned, wounded disbelief — the only Má Ba in frame. Bé Tin [Appearance, attire, and facial features Refer to image 3], resting peacefully inside the wooden pine crib on firm flat organic cotton mattress, breathing softly in calm sleep — the only Bé Tin in frame.</td>
</tr>
<tr>
<td class="tier1-label">[PROP / SURFACE]</td>
<td class="tier1-val">vong_xep: lying static on floor tiles; noi_go: stationary beside bed; mam_nhom: on floor tiles; Patterned floor tiles.</td>
</tr>
<tr>
<td class="tier1-label">[DIEGETIC SOUND]</td>
<td class="tier1-val">Heavy breathing, rustle of cotton fabric, infant's soft rhythmic breath from crib, tense choking silence.</td>
</tr>
<tr>
<td class="tier1-label">[TIMELINE SHOTS]</td>
<td class="tier1-val">[00:00–00:04.0] Shot 1 — Over-The-Shoulder Medium Close-Up on Khang and Duyên (past Má Ba's shoulder):<br/>From behind Má Ba's shoulder, Minh Khang supports Mỹ Duyên as she slumps against his chest. Má Ba's rough hand reaches out to help pull Duyên up, but her fingers catch the edge of Duyên's sleeve, tugging it up: dark purple needle bruises and peeling medical tape on Duyên's slender wrist are exposed sharp in the foreground. Duyên weakly twists her wrist away, but it is too late.<br/><br/>[00:04.0–00:10.0] Shot 2 — Cut to the reverse eye-level close-up on Má Ba on the 180° axis, static camera:<br/>Má Ba's fingers freeze in mid-air above the bruised wrist. Her eyes widen not with tender pity, but with wounded, stunned shock; her throat tightens and her jaw trembles with bitter disbelief:<br/>Má Ba: “Tay mầy... mầy đi truyền nước biển hồi nào sao hổng nói tao hay?!” (Voice of a 56-year-old Southwestern Vietnamese woman; choked, sharp Southern lip-sync, eyes wide with bitter wounded disbelief)<br/>The frame holds as Má Ba stares at the bruises, the silence thickening with unspoken accusation through 00:10.0.</td>
</tr>
</table>
</div>
<div class="dialogue-box">
<div class="box-header">
<span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH &amp; MÓC NỐI HỮU CƠ (CALL-AND-RESPONSE ≤ 18 TỪ)</span>
<button class="copy-btn" onclick="copySnippet('dia-05', this, 'Thoại Cảnh 05')">💬 Copy Thoại</button>
</div>
<div id="dia-05">
<div class="dia-item" style="border-left: 3px solid #F59E0B; background: rgba(245, 158, 11, 0.06); padding: 8px 12px; margin-bottom: 8px; border-radius: 4px;">
<span class="dia-speaker" style="color: #FBBF24;">👶 Bé Tin [00:01.0 – 00:03.5] (Âm Thanh Sinh Học): </span>
<span class="dia-bio-cue" style="color: #FDE68A; font-style: italic;">[Tiếng e e thở nhẹ khi trở mình tự nhiên, lưng thẳng an toàn trên đệm y khoa phẳng]</span>
<div class="dia-bio-note" style="color: #D97706; font-size: 12px; margin-top: 4px;">🔊 Foley Cue: Nhịp thở êm đềm của bé đối lập với cơn bão tâm lý nghẹt thở đang bùng nổ giữa hai người phụ nữ.</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Má Ba [00:44.8 – 00:47.8]: </span>
<span class="dia-spoken-quote">"Tay mầy... mầy đi truyền nước biển hồi nào sao hổng nói tao hay?!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Tay mầy... mầy đi truyền nước biển hồi nào sao hổng nói tao hay?!"</div>
<div class="dia-subtext">(Bàng hoàng nhìn vết bầm kim truyền dịch tím tái — tự ái và tổn thương trào dâng vì bị con dâu giấu bệnh như người dưng)</div>
</div>
</div>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
<button class="copy-btn" onclick="copySnippet('p-05', this, 'Prompt Cảnh 05')">📋 Copy Video Prompt</button>
</div>
<pre class="prompt-display" id="p-05">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot sequence cut on the 180-degree axis.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, over-the-shoulder medium close-up on a bruised wrist cutting to a reverse close-up of wounded shock across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Warm golden morning sunlight pooling across patterned floor tiles beside queen bed, emotionally charged domestic atmosphere.

[subject]:
minh_khang [Appearance, attire, and facial features Refer to image 2], kneeling on floor tiles supporting my_duyen, tense protective posture — the only minh_khang in frame.
my_duyen [Appearance, attire, and facial features Refer to image 1], weak and pale, slumped against minh_khang's chest, fumbling weakly to pull sleeve over bruised wrist — the only my_duyen in frame.
ma_ba [Appearance, attire, and facial features Refer to image 4], kneeling on floor tiles facing the couple, weathered hand caught on my_duyen's sleeve, eyes wide with stunned wounded shock — the only ma_ba in frame.
be_tin [Appearance, attire, and facial features Refer to image 3], resting peacefully inside the wooden pine crib on firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep — the only be_tin in frame.

[PROP]:
vong_xep [100% Refer to image prop_hammock_4view.jpg], static on floor tiles; mam_nhom [100% Refer to image prop_mam_nhom_4view.jpg], on floor tiles — the only vong_xep and mam_nhom in frame.

Diegetic room acoustics: sharp intake of breath, rustle of cotton fabric, infant's soft rhythmic breathing from crib, heavy tense silence.

[00:00–00:04.0] From behind ma_ba's shoulder, ma_ba's graying hair soft in the foreground, a medium close-up on minh_khang kneeling with my_duyen slumped against minh_khang's chest: ma_ba's rough hand reaches out to help lift my_duyen, but fingers catch the edge of my_duyen's sleeve, tugging it up; dark purple infusion bruises and peeling medical tape on my_duyen's slender wrist are exposed sharp in the foreground; my_duyen weakly twists the wrist away, but the secret is out; minh_khang's lips press shut in dread.

[00:04.0–00:10.0] Cut to the reverse eye-level close-up of ma_ba on the 180-degree axis, static camera. ma_ba's fingers freeze in mid-air above the bruised wrist; ma_ba's eyes widen not with tender pity, but with wounded stunned disbelief, throat tightening, weathered jaw trembling with bitter hurt:
ma_ba: “ Tay mầy... mầy đi truyền nước biển hồi nào sao hổng nói tao hay?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in choked sharp Southern Vietnamese lip-sync, eyes wide with bitter wounded disbelief)
The frame holds as ma_ba stares at the bruises, the silence thickening with unspoken accusation through 00:10.0.

Continuous fluid motion, realistic physics, zero morphing, two shots joined by one editorial cut. Spatial positions anchored across the cut. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (00:50)</span>
<button class="copy-btn" onclick="copySnippet('ho-05', this, 'Handover Cảnh 05')">📋 Copy Handover State</button>
</div>
<pre class="handover-display" id="ho-05">[HANDOVER STATE AT 00:50.0]:
Active Characters: ma_ba, minh_khang, my_duyen, be_tin
Characters State at 00:50.0:
  - ma_ba: Kneeling on floor tiles, hand frozen above my_duyen's wrist, face wounded and bitter.
  - minh_khang: Supporting my_duyen, looking anxiously at ma_ba.
  - my_duyen: Slumped against minh_khang, bruised wrist exposed, eyes downcast in defensive exhaustion.
  - be_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, breathing softly in calm sleep.
Props State:
  - noi_go: Stationary beside the bed.
  - vong_xep: Lying folded on floor tiles.
Setting: phong_cu [100% Refer to image location_bedroom_4view.jpg]
Dialogue Audit: ma_ba 14 words (solo confrontation, ~3.5s of speech); my_duyen tries to hide the IV bruises, silence answers.
Kinetic Momentum Bridge: my_duyen jerks her bruised wrist back defensively in Scene 06.</pre>
</div>
</div>
'''

# SCENE 06 REPLACEMENT
s06_new = '''<!-- ==================== SCENE 06 ==================== -->
<div class="scene-card" id="s-06">
<div class="scene-header">
<div class="scene-title-wrap">
<span class="scene-badge">SCENE 06 (CUE-06)</span>
<strong style="font-size:15px; color:#FFF;">B4 Climax — Rạn Nứt Tâm Lý (Emotional Fracture)</strong>
</div>
<div style="display:flex; align-items:center; gap:10px;">
<span class="paradigm-pill" style="background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3);">Track A · Single-Shot Continuous Take</span>
<span class="scene-time">00:50 – 01:00</span>
</div>
</div>
<!-- Diurnal Time of Day & Lighting Specifications Bar -->
<div class="diurnal-bar">
<span style="font-size: 12.5px; color: var(--gold); font-weight: 700;">⏰ <strong>Thời Gian Trong Ngày:</strong> 06:07 AM Ban Mai • Lạnh Lùng Cự Tuyệt & Tự Ái Sôi Sục</span>
<span style="color: rgba(255,255,255,0.2);">|</span>
<span style="font-size: 12px; color: #93C5FD; font-family: 'JetBrains Mono', monospace;">🌡️ <strong>Ánh Sáng &amp; Cảm Xúc:</strong> Ánh Sáng Đối Kháng Căng Thẳng</span>
</div>
<!-- Specs Bar: Characters, Environment, Props, Dialogue Standard -->
<div class="specs-bar">
<span class="spec-pill">👥 <strong>Nhân vật:</strong> 👵 Má Ba (B1 — Đứng bật dậy tổn thương) • 👩 Mỹ Duyên (A1 — Giấu tay sau lưng) • 👨 Minh Khang (A2) • 👶 Bé Tin (Asset 0 / Image 3 — Ngủ sâu trong nôi gỗ)</span>
<span class="spec-pill">🌲 <strong>Bối cảnh:</strong> phong_cu</span>
<span class="spec-pill">🛡️ <strong>Đạo cụ:</strong> noi_go</span>
<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Call-and-Response Đối Kháng Sắc Lạnh (Duyên 10 từ • Má Ba 14 từ)</span>
</div>
<div class="tier1-audit-card">
<div class="tier1-header">🎬 TIER 1: BẢNG KIỂM TOÁN ĐẠO DIỄN (DIRECTOR'S AUDIT CARD)</div>
<table class="tier1-table">
<tr>
<td class="tier1-label">[STYLE &amp; OPTICS]</td>
<td class="tier1-val">Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish.</td>
</tr>
<tr>
<td class="tier1-label">[CONTEXT]</td>
<td class="tier1-val">phong_cu — Master bedroom edge of queen bed. Harsh morning sunlight highlighting the emotional distance separating mother-in-law and daughter-in-law.</td>
</tr>
<tr>
<td class="tier1-label">[SUBJECT]</td>
<td class="tier1-val">Mỹ Duyên [Appearance, attire, and facial features Refer to image 1], sitting propped on mattress edge, tucking bruised wrist tightly behind back, pale face averted in defensive pride — the only Mỹ Duyên in frame. Má Ba [Appearance, attire, and facial features Refer to image 4], recoiling and rising to full height, weathered face dark with wounded matriarchal indignation — the only Má Ba in frame. Minh Khang [Appearance, attire, and facial features Refer to image 2], standing between the two women, palms raised helplessly — the only Minh Khang in frame. Bé Tin [Appearance, attire, and facial features Refer to image 3], resting peacefully inside the wooden pine crib beside queen bed on firm flat organic cotton mattress, sleeping soundly — the only Bé Tin in frame.</td>
</tr>
<tr>
<td class="tier1-label">[PROP / SURFACE]</td>
<td class="tier1-val">noi_go: stationary beside queen bed; Patterned floor tiles; Queen bed.</td>
</tr>
<tr>
<td class="tier1-label">[DIEGETIC SOUND]</td>
<td class="tier1-val">Muffled fabric rustle, sharp intake of breath, strained silence vibrating with unspoken bitterness.</td>
</tr>
<tr>
<td class="tier1-label">[TIMELINE SHOTS]</td>
<td class="tier1-val">[00:00–00:05.2] Single Continuous Take — Part 1 (Level Tracking on Rejection):<br/>At the women's seated eye level, the unbroken camera glides closely into an intimate three-quarter front two-shot on the edge of the mattress where Duyên sits. Duyên pulls her bruised wrist sharply back behind her waist, chin trembling, lowering her pale face to avoid Má Ba's piercing gaze:<br/>Mỹ Duyên: “Con tự lo được... má đừng bận lòng thêm...” (Voice of a 24-year-old Southern Vietnamese woman; cold cracked Southern lip-sync, lips trembling, looking away)<br/><br/>[00:05.2–00:10.0] Single Continuous Take — Part 2 (Drift to Wounded Matriarch):<br/>Continuous level drift without cutting: Má Ba recoils as if struck, rising stiffly to her feet, weathered face hardening with deep, bitter outrage:<br/>Má Ba: “Mầy nói vậy... là mầy coi tao là người dưng nước lã?!” (Voice of a 56-year-old Southwestern Vietnamese woman; harsh trembling Southern lip-sync, chest heaving with offended matriarchal pride)<br/>Minh Khang steps in between them, hands open, caught in the frozen crossfire through 00:10.0.</td>
</tr>
</table>
</div>
<div class="dialogue-box">
<div class="box-header">
<span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH &amp; MÓC NỐI HỮU CƠ (CALL-AND-RESPONSE ≤ 18 TỪ)</span>
<button class="copy-btn" onclick="copySnippet('dia-06', this, 'Thoại Cảnh 06')">💬 Copy Thoại</button>
</div>
<div id="dia-06">
<div class="dia-item">
<span class="dia-speaker">Mỹ Duyên [00:51.5 – 00:54.2]: </span>
<span class="dia-spoken-quote">"Con tự lo được... má đừng bận lòng thêm..."</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Con tự lo được... má đừng bận lòng thêm..."</div>
<div class="dia-subtext">(Giấu tay sau lưng, cự tuyệt sự thương hại vì sợ bị mắng là vụng về bất tài)</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Má Ba [00:55.8 – 00:58.5]: </span>
<span class="dia-spoken-quote">"Mầy nói vậy... là mầy coi tao là người dưng nước lã?!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Mầy nói vậy... là mầy coi tao là người dưng nước lã?!"</div>
<div class="dia-subtext">(Đứng bật dậy, uất nghẹn vì lòng tốt và kinh nghiệm nuôi con bị con dâu gạt phắt)</div>
</div>
</div>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
<button class="copy-btn" onclick="copySnippet('p-06', this, 'Prompt Cảnh 06')">📋 Copy Video Prompt</button>
</div>
<pre class="prompt-display" id="p-06">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track A — one continuous take, zero cuts.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, unbroken single-shot intimate tracking glide on emotional rejection across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Sunlight carving sharp shadows across edge of queen bed, tense fractured domestic atmosphere.

[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1], sitting propped on queen bed edge, tucking bruised wrist tightly behind back, pale face averted in defensive pride — the only my_duyen in frame.
ma_ba [Appearance, attire, and facial features Refer to image 4], recoiling and rising to full standing height, weathered face dark with wounded matriarchal indignation — the only ma_ba in frame.
minh_khang [Appearance, attire, and facial features Refer to image 2], standing between the two women with raised open palms, desperate to calm the clash — the only minh_khang in frame.
be_tin [Appearance, attire, and facial features Refer to image 3], resting peacefully inside the wooden pine crib beside queen bed on firm flat organic cotton mattress, sleeping soundly — the only be_tin in frame.

[PROP]:
white linen bedding on queen bed; noi_go [100% Refer to image prop_crib_4view.jpg] — the only noi_go in frame.

Diegetic room acoustics: rustle of cotton bedding, sharp intake of breath, heavy vibrating silence of familial rupture.

[00:00–00:05.2] At the eye level of the two women, the unbroken camera glides closely into an intimate three-quarter front two-shot on the edge of the queen bed: my_duyen sits propped against pillows, pulling the bruised wrist sharply behind my_duyen's back, chin trembling, lowering the pale face to avoid ma_ba's gaze:
my_duyen: “ Con tự lo được... má đừng bận lòng thêm... ” (Voice of a 24-year-old Southern Vietnamese woman; lips parting in cold cracked Southern Vietnamese lip-sync, lips trembling, looking away)

[00:05.2–00:10.0] Holding level height, the camera drifts slightly wider as ma_ba recoils as if struck, rising stiffly to full standing height, weathered face hardening with deep bitter outrage:
ma_ba: “ Mầy nói vậy... là mầy coi tao là người dưng nước lã?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in harsh trembling Southern Vietnamese lip-sync, chest heaving with offended matriarchal pride)
minh_khang steps between the two women with raised open palms, caught in the frozen crossfire through 00:10.0.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored throughout the take. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (01:00)</span>
<button class="copy-btn" onclick="copySnippet('ho-06', this, 'Handover Cảnh 06')">📋 Copy Handover State</button>
</div>
<pre class="handover-display" id="ho-06">[HANDOVER STATE AT 01:00.0]:
Active Characters: ma_ba, my_duyen, minh_khang, be_tin
Characters State at 01:00.0:
  - ma_ba: Standing rigid near the bed, glaring at my_duyen with bitter wounded pride.
  - my_duyen: Sitting on the bed edge with wrist tucked behind back, weeping in cold defiance.
  - minh_khang: Standing between them, palms raised, looking pleadingly at ma_ba.
  - be_tin: Resting safely and peacefully in the wooden pine crib on firm flat mattress, breathing rhythmically in deep sleep.
Props State:
  - noi_go: Stationary beside the bed.
Setting: phong_cu [100% Refer to image location_bedroom_4view.jpg]
Dialogue Audit: my_duyen 10 words, ma_ba 14 words (24 words, ~6.0s of speech; call-and-response confrontation).
Kinetic Momentum Bridge: ma_ba backs away toward the door with trembling hands in Scene 07.</pre>
</div>
</div>
'''

# SCENE 07 REPLACEMENT
s07_new = '''<!-- ==================== SCENE 07 ==================== -->
<div class="scene-card" id="s-07">
<div class="scene-header">
<div class="scene-title-wrap">
<span class="scene-badge">SCENE 07 (CUE-07)</span>
<strong style="font-size:15px; color:#FFF;">B4 Climax — Lời Trách Móc Chua Xót (Escalation of Hurt)</strong>
</div>
<div style="display:flex; align-items:center; gap:10px;">
<span class="paradigm-pill" style="background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3);">Track AB · Hybrid (Take + 1 Cut · 180° Axis)</span>
<span class="scene-time">01:00 – 01:10</span>
</div>
</div>
<!-- Diurnal Time of Day & Lighting Specifications Bar -->
<div class="diurnal-bar">
<span style="font-size: 12.5px; color: var(--gold); font-weight: 700;">⏰ <strong>Thời Gian Trong Ngày:</strong> 06:08 AM Ban Mai • Cơn Giận Bùng Nổ & Sự Bất Lực</span>
<span style="color: rgba(255,255,255,0.2);">|</span>
<span style="font-size: 12px; color: #93C5FD; font-family: 'JetBrains Mono', monospace;">🌡️ <strong>Ánh Sáng &amp; Cảm Xúc:</strong> Ánh Sáng Phân Cực Gay Gắt</span>
</div>
<!-- Specs Bar: Characters, Environment, Props, Dialogue Standard -->
<div class="specs-bar">
<span class="spec-pill">👥 <strong>Nhân vật:</strong> 👵 Má Ba (B1) • 👨 Minh Khang (A2) • 👩 Mỹ Duyên (A1) • 👶 Bé Tin (Asset 0 / Image 3 — Cựa mình trong nôi)</span>
<span class="spec-pill">🌲 <strong>Bối cảnh:</strong> phong_cu</span>
<span class="spec-pill">🛡️ <strong>Đạo cụ:</strong> noi_go</span>
<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Đối Thoại Giằng Xé (Má Ba 13 từ • Khang 14 từ)</span>
</div>
<div class="tier1-audit-card">
<div class="tier1-header">🎬 TIER 1: BẢNG KIỂM TOÁN ĐẠO DIỄN (DIRECTOR'S AUDIT CARD)</div>
<table class="tier1-table">
<tr>
<td class="tier1-label">[STYLE &amp; OPTICS]</td>
<td class="tier1-val">Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish.</td>
</tr>
<tr>
<td class="tier1-label">[CONTEXT]</td>
<td class="tier1-val">phong_cu doorway and center. Morning sun casting long angular shadows across wooden floor tiles, deepening the rift between mother and son.</td>
</tr>
<tr>
<td class="tier1-label">[SUBJECT]</td>
<td class="tier1-val">Má Ba [Appearance, attire, and facial features Refer to image 4], backing toward wooden doorframe, weathered finger pointing accusingly at bed, eyes brimming with furious tears — the only Má Ba in frame. Minh Khang [Appearance, attire, and facial features Refer to image 2], stepping between Má Ba and bed, hands outstretched in desperate filial pleading — the only Minh Khang in frame. Mỹ Duyên [Appearance, attire, and facial features Refer to image 1], weeping in background beside crib — the only Mỹ Duyên in frame. Bé Tin [Appearance, attire, and facial features Refer to image 3], resting peacefully inside the wooden pine crib, stirring softly — the only Bé Tin in frame.</td>
</tr>
<tr>
<td class="tier1-label">[PROP / SURFACE]</td>
<td class="tier1-val">noi_go: stationary beside queen bed; Patterned floor tiles; Wooden doorframe.</td>
</tr>
<tr>
<td class="tier1-label">[DIEGETIC SOUND]</td>
<td class="tier1-val">Trembling vocal cords, heavy footsteps shuffling backward, distant traffic rumble outside.</td>
</tr>
<tr>
<td class="tier1-label">[TIMELINE SHOTS]</td>
<td class="tier1-val">[00:00–00:10.0] Track AB — Take → Cut → Take (Accusation at Doorway, Cut to Pleading Son):<br/><strong>[00:00–00:04.8] Take 1 — Eye-Level Medium Shot on Má Ba at Doorway:</strong> Má Ba backs up until her heels touch the wooden doorframe, pointing a shaking weathered finger back into the room, tears of angry frustration brimming in her aged eyes:<br/>Má Ba: “Tao lặn lội lên đây... hổng phải để tụi bây xua đuổi!” (Voice of a 56-year-old Southwestern Vietnamese woman; choked accusatory Southern lip-sync, chin trembling with wounded dignity)<br/><br/><strong>[00:04.8–00:10.0] Cut to the reverse angle on 180° Axis — Medium Close-Up of Minh Khang:</strong> Standing between bed and doorframe, Minh Khang raises both open palms, body tense with agonizing conflict between duty and empathy:<br/>Minh Khang: “Má! Duyên nó đang bệnh, má đừng nói vậy tội nghiệp nó!” (Voice of a 27-year-old Southern Vietnamese man; anguished urgent Southern lip-sync, desperate to shield his wife without breaking his mother's heart)<br/>The camera holds as Má Ba stiffens in bitter silence through 00:10.0.</td>
</tr>
</table>
</div>
<div class="dialogue-box">
<div class="box-header">
<span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH &amp; MÓC NỐI HỮU CƠ (CALL-AND-RESPONSE ≤ 18 TỪ)</span>
<button class="copy-btn" onclick="copySnippet('dia-07', this, 'Thoại Cảnh 07')">💬 Copy Thoại</button>
</div>
<div id="dia-07">
<div class="dia-item">
<span class="dia-speaker">Má Ba [01:02.0 – 01:05.2]: </span>
<span class="dia-spoken-quote">"Tao lặn lội lên đây... hổng phải để tụi bây xua đuổi!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Tao lặn lội lên đây... hổng phải để tụi bây xua đuổi!"</div>
<div class="dia-subtext">(Lùi lại cửa phòng, tự ái bùng nổ biến nỗi tủi thân thành lời kết tội con cái)</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Minh Khang [01:06.5 – 01:09.2]: </span>
<span class="dia-spoken-quote">"Má! Duyên nó đang bệnh, má đừng nói vậy tội nghiệp nó!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Má! Duyên nó đang bệnh, má đừng nói vậy tội nghiệp nó!"</div>
<div class="dia-subtext">(Bênh vực vợ trong tuyệt vọng, kẹt cứng giữa chữ hiếu và tình thương bạn đời)</div>
</div>
</div>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
<button class="copy-btn" onclick="copySnippet('p-07', this, 'Prompt Cảnh 07')">📋 Copy Video Prompt</button>
</div>
<pre class="prompt-display" id="p-07">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track AB — one continuous take punctuated by a cut on the 180-degree axis.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, accusatory medium shot at doorway cutting to an anguished reverse close-up across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Harsh angular sunlight cutting through dust motes across wooden doorway, deepening domestic conflict.

[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4], standing rigid in wooden doorway, pointing shaking weathered finger toward bed, furious tears in aged eyes — the only ma_ba in frame.
minh_khang [Appearance, attire, and facial features Refer to image 2], standing between ma_ba and bed, palms raised in agonizing filial pleading — the only minh_khang in frame.
my_duyen [Appearance, attire, and facial features Refer to image 1], sitting on bed edge in soft background, weeping silently — the only my_duyen in frame.
be_tin [Appearance, attire, and facial features Refer to image 3], resting peacefully inside the wooden pine crib, stirring softly in safe sleep — the only be_tin in frame.

[PROP]:
noi_go [100% Refer to image prop_crib_4view.jpg], stationary beside bed; wooden doorframe — the only noi_go in frame.

Diegetic room acoustics: trembling vocal timbre, heavy footsteps on floor tiles, tense emotional collision.

[00:00–00:04.8] Eye-level medium shot on ma_ba standing at the bedroom wooden doorframe: ma_ba points a shaking weathered finger back into the room, tears of angry frustration brimming in weathered eyes:
ma_ba: “ Tao lặn lội lên đây... hổng phải để tụi bây xua đuổi! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in choked accusatory Southern Vietnamese lip-sync, chin trembling with wounded dignity)

[00:04.8–00:10.0] Cut to the reverse angle on the 180-degree axis, a medium close-up of minh_khang facing ma_ba, palms raised, caught in agonizing conflict between filial duty and protective love:
minh_khang: “ Má! Duyên nó đang bệnh, má đừng nói vậy tội nghiệp nó! ” (Voice of a 27-year-old Southern Vietnamese man; lips parting in anguished urgent Southern Vietnamese lip-sync, eyes pleading for mercy)
The frame holds on minh_khang's strained expression as ma_ba stiffens in bitter silence through 00:10.0.

Continuous fluid motion, realistic physics, zero morphing, two shots joined by one editorial cut. Spatial positions anchored across the cut. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (01:10)</span>
<button class="copy-btn" onclick="copySnippet('ho-07', this, 'Handover Cảnh 07')">📋 Copy Handover State</button>
</div>
<pre class="handover-display" id="ho-07">[HANDOVER STATE AT 01:10.0]:
Active Characters: ma_ba, minh_khang, my_duyen, be_tin
Characters State at 01:10.0:
  - ma_ba: Standing in the wooden doorframe, arms stiff at sides, glaring in cold outrage.
  - minh_khang: Standing facing ma_ba, arms raised defensively.
  - my_duyen: Sitting on queen bed edge, weeping with head down.
  - be_tin: Resting safely in pine crib, breathing softly.
Props State:
  - noi_go: Stationary beside the bed.
Setting: phong_cu [100% Refer to image location_bedroom_4view.jpg]
Dialogue Audit: ma_ba 13 words, minh_khang 14 words (27 words, ~6.8s of speech; call-and-response confrontation).
Kinetic Momentum Bridge: ma_ba stiffens in bitter silence as Khang shields Duyen in Scene 08.</pre>
</div>
</div>
'''

# SCENE 08 REPLACEMENT
s08_new = '''<!-- ==================== SCENE 08 ==================== -->
<div class="scene-card" id="s-08">
<div class="scene-header">
<div class="scene-title-wrap">
<span class="scene-badge">SCENE 08 (CUE-08)</span>
<strong style="font-size:15px; color:#FFF;">B5 Deepening Fracture — Vết Nứt Đóng Băng (Point of No Return)</strong>
</div>
<div style="display:flex; align-items:center; gap:10px;">
<span class="paradigm-pill" style="background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3);">Track A · Single-Shot Continuous Take</span>
<span class="scene-time">01:10 – 01:20</span>
</div>
</div>
<!-- Diurnal Time of Day & Lighting Specifications Bar -->
<div class="diurnal-bar">
<span style="font-size: 12.5px; color: var(--gold); font-weight: 700;">⏰ <strong>Thời Gian Trong Ngày:</strong> 06:09 AM Ban Mai • Rạn Nứt Đóng Băng & Tự Ái Tuyệt Đỉnh</span>
<span style="color: rgba(255,255,255,0.2);">|</span>
<span style="font-size: 12px; color: #93C5FD; font-family: 'JetBrains Mono', monospace;">🌡️ <strong>Ánh Sáng &amp; Cảm Xúc:</strong> Ánh Sáng Lạnh Lùng</span>
</div>
<!-- Specs Bar: Characters, Environment, Props, Dialogue Standard -->
<div class="specs-bar">
<span class="spec-pill">👥 <strong>Nhân vật:</strong> 👵 Má Ba (B1 — Buông lời cay đắng) • 👨 Minh Khang (A2) • 👩 Mỹ Duyên (A1) • 👶 Bé Tin (Asset 0 / Image 3 — Ngủ ngoan trong nôi)</span>
<span class="spec-pill">🌲 <strong>Bối cảnh:</strong> phong_cu doorway / hallway</span>
<span class="spec-pill">🛡️ <strong>Đạo cụ:</strong> vong_xep • noi_go</span>
<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Solo Cay Đắng (Má Ba 16 từ • Khang và Duyên câm lặng)</span>
</div>
<div class="tier1-audit-card">
<div class="tier1-header">🎬 TIER 1: BẢNG KIỂM TOÁN ĐẠO DIỄN (DIRECTOR'S AUDIT CARD)</div>
<table class="tier1-table">
<tr>
<td class="tier1-label">[STYLE &amp; OPTICS]</td>
<td class="tier1-val">Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish.</td>
</tr>
<tr>
<td class="tier1-label">[CONTEXT]</td>
<td class="tier1-val">phong_cu doorway looking toward hallway. Morning sunlight glinting off the folded stainless steel hammock frame lying rejected on floor tiles.</td>
</tr>
<tr>
<td class="tier1-label">[SUBJECT]</td>
<td class="tier1-val">Má Ba [Appearance, attire, and facial features Refer to image 4], standing rigid in doorway, glaring down at rejected hammock then across at couple with cold finality — the only Má Ba in frame. Minh Khang [Appearance, attire, and facial features Refer to image 2], standing helpless beside crib, head hung in defeat — the only Minh Khang in frame. Mỹ Duyên [Appearance, attire, and facial features Refer to image 1], weeping silently on bed — the only Mỹ Duyên in frame. Bé Tin [Appearance, attire, and facial features Refer to image 3], resting peacefully inside the wooden pine crib, breathing rhythmically — the only Bé Tin in frame.</td>
</tr>
<tr>
<td class="tier1-label">[PROP / SURFACE]</td>
<td class="tier1-val">vong_xep: folded on floor tiles beside doorframe; noi_go: stationary beside bed; Patterned floor tiles.</td>
</tr>
<tr>
<td class="tier1-label">[DIEGETIC SOUND]</td>
<td class="tier1-val">Heavy hollow footsteps turning into hallway, cold silence settling like ice over the bedroom.</td>
</tr>
<tr>
<td class="tier1-label">[TIMELINE SHOTS]</td>
<td class="tier1-val">[00:00–00:10.0] Single Continuous Take (Slow Tracking Glide on Wounded Pride):<br/>At doorway height, the camera frames Má Ba standing rigid in the wooden doorframe, her gaze dropping to the folded stainless steel hammock stand lying abandoned on the floor tiles. Her face hardens into stone; she looks up, glaring across the room at Khang and Duyên with icy finality:<br/>Má Ba: “Được rồi... tụi bây khôn rồi, để coi tụi bây nuôi con ra sao!” (Voice of a 56-year-old Southwestern Vietnamese woman; icy bitter Southern lip-sync, lips tightened with unrelenting stubborn pride)<br/>The camera holds as Má Ba turns her back sharply and steps into the hallway through 00:10.0.</td>
</tr>
</table>
</div>
<div class="dialogue-box">
<div class="box-header">
<span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH &amp; MÓC NỐI HỮU CƠ (CALL-AND-RESPONSE ≤ 18 TỪ)</span>
<button class="copy-btn" onclick="copySnippet('dia-08', this, 'Thoại Cảnh 08')">💬 Copy Thoại</button>
</div>
<div id="dia-08">
<div class="dia-item">
<span class="dia-speaker">Má Ba [01:13.5 – 01:17.2]: </span>
<span class="dia-spoken-quote">"Được rồi... tụi bây khôn rồi, để coi tụi bây nuôi con ra sao!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Được rồi... tụi bây khôn rồi, để coi tụi bây nuôi con ra sao!"</div>
<div class="dia-subtext">(Nhìn chiếc võng bị chối bỏ dưới đất, buông lời nguyền tự ái trước khi quay gót bước đi)</div>
</div>
</div>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
<button class="copy-btn" onclick="copySnippet('p-08', this, 'Prompt Cảnh 08')">📋 Copy Video Prompt</button>
</div>
<pre class="prompt-display" id="p-08">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track A — one continuous take, zero cuts.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, unbroken single-shot slow tracking glide on wounded pride across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Sunlight glinting cold off stainless steel hammock frame near doorway, freezing domestic atmosphere.

[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4], standing rigid in wooden doorway, looking down at rejected hammock then glaring across room with stone-cold pride — the only ma_ba in frame.
minh_khang [Appearance, attire, and facial features Refer to image 2], standing beside crib in soft background, head hung low in defeat — the only minh_khang in frame.
my_duyen [Appearance, attire, and facial features Refer to image 1], sitting on bed edge, weeping silently into hands — the only my_duyen in frame.
be_tin [Appearance, attire, and facial features Refer to image 3], resting peacefully inside the wooden pine crib, breathing rhythmically — the only be_tin in frame.

[PROP]:
vong_xep [100% Refer to image prop_hammock_4view.jpg], folded stainless steel hammock frame lying rejected on floor tiles near doorway; noi_go [100% Refer to image prop_crib_4view.jpg] — the only vong_xep and noi_go in frame.

Diegetic room acoustics: heavy hollow footsteps turning away, chilly silence settling over room.

[00:00–00:03.8] At doorway height, unbroken camera frames ma_ba standing rigid in the wooden doorframe: ma_ba's gaze drops to the folded stainless steel hammock frame lying abandoned on the floor tiles, jaw tightening in stubborn wounded pride:

[00:03.8–00:10.0] ma_ba raises chin and glares across the bedroom with cold finality:
ma_ba: “ Được rồi... tụi bây khôn rồi, để coi tụi bây nuôi con ra sao! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in icy bitter Southern Vietnamese lip-sync, lips tightened with stubborn pride)
The camera tracks slowly backward as ma_ba turns sharply away from the bedroom and exits into the hallway through 00:10.0.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored throughout the take. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (01:20)</span>
<button class="copy-btn" onclick="copySnippet('ho-08', this, 'Handover Cảnh 08')">📋 Copy Handover State</button>
</div>
<pre class="handover-display" id="ho-08">[HANDOVER STATE AT 01:20.0]:
Active Characters: ma_ba, minh_khang, my_duyen, be_tin
Characters State at 01:20.0:
  - ma_ba: Exiting through the doorway into the hallway, back turned.
  - minh_khang: Standing in bedroom center, shoulders slumped.
  - my_duyen: Sitting on the bed edge weeping silently.
  - be_tin: Resting safely in pine crib, breathing softly.
Props State:
  - vong_xep: Lying folded on floor tiles near door.
  - noi_go: Stationary beside bed.
Setting: phong_cu [100% Refer to image location_bedroom_4view.jpg]
Dialogue Audit: ma_ba 16 words (solo ultimatum, ~4.0s of speech).
Kinetic Momentum Bridge: my_duyen buries her face into the baby pillow in Scene 09.</pre>
</div>
</div>
'''

# SCENE 09 REPLACEMENT
s09_new = '''<!-- ==================== SCENE 09 ==================== -->
<div class="scene-card" id="s-09">
<div class="scene-header">
<div class="scene-title-wrap">
<span class="scene-badge">SCENE 09 (CUE-09)</span>
<strong style="font-size:15px; color:#FFF;">B5 Simmering Dread — Căn Phòng Bất Lực (Living Organic Settle)</strong>
</div>
<div style="display:flex; align-items:center; gap:10px;">
<span class="paradigm-pill" style="background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3);">Track A · Single-Shot Continuous Take</span>
<span class="scene-time">01:20 – 01:30</span>
</div>
</div>
<!-- Diurnal Time of Day & Lighting Specifications Bar -->
<div class="diurnal-bar">
<span style="font-size: 12.5px; color: var(--gold); font-weight: 700;">⏰ <strong>Thời Gian Trong Ngày:</strong> 06:10 AM Ban Mai • Bế Tắc Đè Nặng & Sự Bất Lực</span>
<span style="color: rgba(255,255,255,0.2);">|</span>
<span style="font-size: 12px; color: #93C5FD; font-family: 'JetBrains Mono', monospace;">🌡️ <strong>Ánh Sáng &amp; Cảm Xúc:</strong> Ánh Sáng U Tối Ngột Ngạt</span>
</div>
<!-- Specs Bar: Characters, Environment, Props, Dialogue Standard -->
<div class="specs-bar">
<span class="spec-pill">👥 <strong>Nhân vật:</strong> 👩 Mỹ Duyên (A1 — Khóc nghẹn trong bất lực) • 👨 Minh Khang (A2) • 👶 Bé Tin (Asset 0 / Image 3 — Nằm trong nôi)</span>
<span class="spec-pill">🌲 <strong>Bối cảnh:</strong> phong_cu</span>
<span class="spec-pill">🛡️ <strong>Đạo cụ:</strong> noi_go • bat_chao</span>
<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Solo Than Thở Bế Tắc (Duyên 14 từ • Khang ôm vợ trong im lặng)</span>
</div>
<div class="tier1-audit-card">
<div class="tier1-header">🎬 TIER 1: BẢNG KIỂM TOÁN ĐẠO DIỄN (DIRECTOR'S AUDIT CARD)</div>
<table class="tier1-table">
<tr>
<td class="tier1-label">[STYLE &amp; OPTICS]</td>
<td class="tier1-val">Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish.</td>
</tr>
<tr>
<td class="tier1-label">[CONTEXT]</td>
<td class="tier1-val">phong_cu — Master bedroom bedside. Morning sunlight casting long somber shadows across floor tiles where spilled cold congee lies forgotten.</td>
</tr>
<tr>
<td class="tier1-label">[SUBJECT]</td>
<td class="tier1-val">Mỹ Duyên [Appearance, attire, and facial features Refer to image 1], sitting slumped on queen bed mattress edge, burying face in Minh Khang's shoulder, weeping softly — the only Mỹ Duyên in frame. Minh Khang [Appearance, attire, and facial features Refer to image 2], sitting beside Mỹ Duyên, wrapping arms tightly around her trembling frame, eyes closed in silent anguish — the only Minh Khang in frame. Bé Tin [Appearance, attire, and facial features Refer to image 3], resting peacefully inside the wooden pine crib, breathing softly — the only Bé Tin in frame.</td>
</tr>
<tr>
<td class="tier1-label">[PROP / SURFACE]</td>
<td class="tier1-val">bat_chao: cold congee spilled on floor tiles; noi_go: stationary beside bed; Queen bed mattress.</td>
</tr>
<tr>
<td class="tier1-label">[DIEGETIC SOUND]</td>
<td class="tier1-val">Soft muffled weeping, ragged breathing, heavy ticking of bedroom clock, distant outside sounds.</td>
</tr>
<tr>
<td class="tier1-label">[TIMELINE SHOTS]</td>
<td class="tier1-val">[00:00–00:10.0] Single Continuous Take (Slow Intimate Push-In on Exhausted Grief):<br/>In the quiet bedroom, morning sunlight casts long, somber shadows across the floor tiles where the spilled congee bowl lies forgotten. Minh Khang sits heavily beside Mỹ Duyên on the mattress edge, his arm pulling her trembling shoulder against his chest. Duyên presses her tear-stained face into his shoulder, her breath ragged and exhausted:<br/>Mỹ Duyên: “Em mệt quá Khang ơi... nhà mình hổng thở nổi nữa rồi...” (Voice of a 24-year-old Southern Vietnamese woman; broken faint Southern lip-sync, muffled against his shoulder, drained of all fight)<br/>Khang closes his eyes, jaw tightening, unable to offer an answer as the room sinks into heavy despair through 00:10.0.</td>
</tr>
</table>
</div>
<div class="dialogue-box">
<div class="box-header">
<span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH &amp; MÓC NỐI HỮU CƠ (CALL-AND-RESPONSE ≤ 18 TỪ)</span>
<button class="copy-btn" onclick="copySnippet('dia-09', this, 'Thoại Cảnh 09')">💬 Copy Thoại</button>
</div>
<div id="dia-09">
<div class="dia-item">
<span class="dia-speaker">Mỹ Duyên [01:24.5 – 01:27.5]: </span>
<span class="dia-spoken-quote">"Em mệt quá Khang ơi... nhà mình hổng thở nổi nữa rồi..."</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Em mệt quá Khang ơi... nhà mình hổng thở nổi nữa rồi..."</div>
<div class="dia-subtext">(Gục đầu vào ngực chồng, lời thú nhận kiệt cùng của người mẹ trẻ bị bủa vây giữa trầm cảm và định kiến)</div>
</div>
</div>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
<button class="copy-btn" onclick="copySnippet('p-09', this, 'Prompt Cảnh 09')">📋 Copy Video Prompt</button>
</div>
<pre class="prompt-display" id="p-09">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track A — one continuous take, zero cuts.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, unbroken single-shot slow intimate push-in on exhausted grief across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Long somber shadows stretching across floor tiles beside queen bed, suffocating quiet domestic atmosphere.

[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1], sitting slumped on queen bed edge, burying face in minh_khang's shoulder, weeping softly — the only my_duyen in frame.
minh_khang [Appearance, attire, and facial features Refer to image 2], sitting beside my_duyen, wrapping arms tightly around my_duyen's trembling frame, eyes closed in silent anguish — the only minh_khang in frame.
be_tin [Appearance, attire, and facial features Refer to image 3], resting peacefully inside the wooden pine crib, breathing softly — the only be_tin in frame.

[PROP]:
bat_chao [100% Refer to image prop_chao_4view.jpg], cold congee bowl spilled on floor tiles; noi_go [100% Refer to image prop_crib_4view.jpg] — the only bat_chao and noi_go in frame.

Diegetic room acoustics: soft muffled weeping, ragged breathing, quiet heavy ticking of bedroom clock.

[00:00–00:04.2] Slow intimate push-in on the couple sitting together on the edge of the queen bed: morning sunlight casts long shadows across the floor tiles where the congee bowl lies forgotten; minh_khang pulls my_duyen's trembling shoulders against minh_khang's chest:

[00:04.2–00:10.0] The camera pushes in close to my_duyen's tear-streaked face resting against minh_khang's shoulder:
my_duyen: “ Em mệt quá Khang ơi... nhà mình hổng thở nổi nữa rồi... ” (Voice of a 24-year-old Southern Vietnamese woman; lips parting in broken faint Southern Vietnamese lip-sync, muffled against shoulder, drained of fight)
minh_khang closes eyes, jaw tightening, unable to answer as the frame holds still through 00:10.0.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored throughout the take. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (01:30)</span>
<button class="copy-btn" onclick="copySnippet('ho-09', this, 'Handover Cảnh 09')">📋 Copy Handover State</button>
</div>
<pre class="handover-display" id="ho-09">[HANDOVER STATE AT 01:30.0]:
Active Characters: my_duyen, minh_khang, be_tin
Characters State at 01:30.0:
  - my_duyen: Slumped against minh_khang's chest on the bed edge, weeping quietly.
  - minh_khang: Holding my_duyen tightly, eyes closed in heavy silence.
  - be_tin: Resting safely in pine crib, breathing rhythmically.
Props State:
  - bat_chao: Spilled on floor tiles.
  - noi_go: Stationary beside bed.
Setting: phong_cu [100% Refer to image location_bedroom_4view.jpg]
Dialogue Audit: my_duyen 14 words (solo despair, ~3.5s of speech).
Kinetic Momentum Bridge: Loud, violent knocking suddenly rattles the front iron gate in Scene 10.</pre>
</div>
</div>
'''

# SCENE 10 REPLACEMENT
s10_new = '''<!-- ==================== SCENE 10 ==================== -->
<div class="scene-card" id="s-10">
<div class="scene-header">
<div class="scene-title-wrap">
<span class="scene-badge">SCENE 10 (CUE-10)</span>
<strong style="font-size:15px; color:#FFF;">Hook Tập 2 — Tiếng Cười Mỉa Đầu Hẻm (Cold Water Slap)</strong>
</div>
<div style="display:flex; align-items:center; gap:10px;">
<span class="paradigm-pill" style="background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3);">Track B · Multi-Shot (1 Cut · 180° Axis)</span>
<span class="scene-time">01:30 – 01:40</span>
</div>
</div>
<!-- Diurnal Time of Day & Lighting Specifications Bar -->
<div class="diurnal-bar">
<span style="font-size: 12.5px; color: var(--gold); font-weight: 700;">⏰ <strong>Thời Gian Trong Ngày:</strong> 06:11 AM Ban Mai • Gáo Nước Lạnh Đột Ngột & Châm Ngòi Tập 2</span>
<span style="color: rgba(255,255,255,0.2);">|</span>
<span style="font-size: 12px; color: #93C5FD; font-family: 'JetBrains Mono', monospace;">🌡️ <strong>Ánh Sáng &amp; Cảm Xúc:</strong> Ánh Sáng Đối Kháng Đầu Hẻm</span>
</div>
<!-- Specs Bar: Characters, Environment, Props, Dialogue Standard -->
<div class="specs-bar">
<span class="spec-pill">👥 <strong>Nhân vật:</strong> 👵 Dì Tám (B2 — Xông vào kích động) • 👵 Má Ba (B1 — Đứng trên cầu thang) • 👨 Minh Khang (A2) • 👩 Mỹ Duyên (A1)</span>
<span class="spec-pill">🌲 <strong>Bối cảnh:</strong> townhouse living room / front doorway</span>
<span class="spec-pill">🛡️ <strong>Đạo cụ:</strong> can_ruou_gung (can nhựa trắng)</span>
<span class="spec-pill" style="border-color: rgba(56,189,248,0.4); color: var(--cyan);">💬 Thoại: Call-and-Response Kích Ngòi Tập 2 (Dì Tám 15 từ • Má Ba 11 từ)</span>
</div>
<div class="tier1-audit-card">
<div class="tier1-header">🎬 TIER 1: BẢNG KIỂM TOÁN ĐẠO DIỄN (DIRECTOR'S AUDIT CARD)</div>
<table class="tier1-table">
<tr>
<td class="tier1-label">[STYLE &amp; OPTICS]</td>
<td class="tier1-val">Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish.</td>
</tr>
<tr>
<td class="tier1-label">[CONTEXT]</td>
<td class="tier1-val">Townhouse ground floor living room and front entrance. Harsh morning daylight flooding through the open iron front gate as an aggressive outsider breaches the threshold.</td>
</tr>
<tr>
<td class="tier1-label">[SUBJECT]</td>
<td class="tier1-val">Dì Tám [Appearance, attire, and facial features Refer to image ditam_modelsheet.jpg], barging through front door into living room clutching a white plastic jug of ginger alcohol, sharp inquisitive eyes — the only Dì Tám in frame. Má Ba [Appearance, attire, and facial features Refer to image 4], standing on stair landing, gripping wooden banister with white knuckles, looking down with cold wounded pride — the only Má Ba in frame. Minh Khang [Appearance, attire, and facial features Refer to image 2] and Mỹ Duyên [Appearance, attire, and facial features Refer to image 1], frozen upstairs in doorway.</td>
</tr>
<tr>
<td class="tier1-label">[PROP / SURFACE]</td>
<td class="tier1-val">can_ruou_gung: white plastic jug clutched in Dì Tám's hands; Polished wooden stair banister; Living room floor tiles.</td>
</tr>
<tr>
<td class="tier1-label">[DIEGETIC SOUND]</td>
<td class="tier1-val">Loud metallic rattle of iron front gate, squeak of plastic sandals on tiles, piercing Southern female voice.</td>
</tr>
<tr>
<td class="tier1-label">[TIMELINE SHOTS]</td>
<td class="tier1-val">[00:00–00:10.0] Track B — Multi-Shot Cut on 180° Axis (Intrusion of the Provocateur & The Dark Pact):<br/><strong>[00:00–00:04.6] Shot 1 — Eye-Level Medium Shot from inside front hallway:</strong> Violent banging rattles the front gate, and Dì Tám barges through the front doorway into the living room, clutching a plastic jug of ginger alcohol against her lilac pyjamas, eyes gleaming with malicious neighborhood gossip:<br/>Dì Tám: “Bà Ba! Con dâu nó leo lên đầu ngồi mà bà nhịn hả?!” (Voice of a 58-year-old Southwestern Vietnamese woman; piercing loud Southern lip-sync, gesturing with the ginger alcohol jug)<br/><br/><strong>[00:04.6–00:10.0] Shot 2 — Cut to the reverse low-angle medium close-up of Má Ba on the stair landing on 180° axis:</strong> Má Ba grips the polished wooden banister, her knuckles white, her weathered face locked in bitter, wounded pride as she looks down at Dì Tám, seizing the offered alliance:<br/>Má Ba: “Chị Tám... chị vô đây coi cháu tao giùm tao!” (Voice of a 56-year-old Southwestern Vietnamese woman; trembling bitter Southern lip-sync, beckoning Dì Tám upstairs)<br/>Immediate cut to black on Má Ba's hardened, unforgiving eyes at 00:10.0!</td>
</tr>
</table>
</div>
<div class="dialogue-box">
<div class="box-header">
<span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH &amp; MÓC NỐI HỮU CƠ (CALL-AND-RESPONSE ≤ 18 TỪ)</span>
<button class="copy-btn" onclick="copySnippet('dia-10', this, 'Thoại Cảnh 10')">💬 Copy Thoại</button>
</div>
<div id="dia-10">
<div class="dia-item">
<span class="dia-speaker">Dì Tám [01:31.0 – 01:34.2]: </span>
<span class="dia-spoken-quote">"Bà Ba! Con dâu nó leo lên đầu ngồi mà bà nhịn hả?!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Bà Ba! Con dâu nó leo lên đầu ngồi mà bà nhịn hả?!"</div>
<div class="dia-subtext">(Xộc vào nhà châm dầu vào lửa, kích động cơn tự ái của mẹ chồng để giật quyền kiểm soát)</div>
</div>
<div class="dia-item">
<span class="dia-speaker">Má Ba [01:35.5 – 01:38.2]: </span>
<span class="dia-spoken-quote">"Chị Tám... chị vô đây coi cháu tao giùm tao!"</span>
<div class="dia-vn-dub">🇻🇳 [Nam Bộ]: "Chị Tám... chị vô đây coi cháu tao giùm tao!"</div>
<div class="dia-subtext">(Nắm lấy đồng minh xóm giềng, ngầm tuyên chiến với con dâu — kích nổ bi kịch Tập 2)</div>
</div>
</div>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
<button class="copy-btn" onclick="copySnippet('p-10', this, 'Prompt Cảnh 10')">📋 Copy Video Prompt</button>
</div>
<pre class="prompt-display" id="p-10">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot sequence cut on the 180-degree axis.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, aggressive wide entrance cutting to a reverse low-angle close-up across ten seconds.

[context]:
Townhouse ground floor living room and front doorway [100% Refer to image location_livingroom_4view.jpg], morning. Bright morning daylight flooding through front doorway, high domestic tension.

[subject]:
di_tam [Appearance, attire, and facial features Refer to image ditam_modelsheet.jpg], barging through front door into living room holding white plastic jug of ginger alcohol, sharp inquisitive expression — the only di_tam in frame.
ma_ba [Appearance, attire, and facial features Refer to image 4], standing on wooden stair landing looking down, knuckles white on banister, face hardened with bitter wounded pride — the only ma_ba in frame.

[PROP]:
can_ruou_gung [100% Refer to image prop_jug_4view.jpg], white plastic jug of ginger alcohol clutched in di_tam's hands; polished wooden stair banister; living room tiled floor.

Diegetic room acoustics: loud rattle of iron gate, squeak of rubber sandals on tiles, piercing female voice, abrupt cut to black.

[00:00–00:04.6] Eye-level medium shot from inside the living room toward the front entrance: di_tam pushes open the wooden door and barges into the room, clutching the white plastic jug of ginger alcohol against chest, eyes flashing with malicious neighborhood gossip:
di_tam: “ Bà Ba! Con dâu nó leo lên đầu ngồi mà bà nhịn hả?! ” (Voice of a 58-year-old Southwestern Vietnamese neighbor; lips parting in loud piercing Southern Vietnamese lip-sync, gesturing with the plastic jug)

[00:04.6–00:10.0] Cut to the reverse angle on the 180-degree axis, a low-angle medium close-up of ma_ba standing on the stair landing looking down: ma_ba's knuckles turn white on the polished wooden banister, face hardened in bitter wounded pride:
ma_ba: “ Chị Tám... chị vô đây coi cháu tao giùm tao! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in trembling bitter Southern Vietnamese lip-sync, beckoning upstairs)
Immediate cut to black on ma_ba's hardened unforgiving gaze at 00:10.0.

Continuous fluid motion, realistic physics, zero morphing, two shots joined by one editorial cut. Spatial positions anchored across the cut. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
</div>
<div class="block-wrap">
<div class="block-header">
<span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (01:40)</span>
<button class="copy-btn" onclick="copySnippet('ho-10', this, 'Handover Cảnh 10')">📋 Copy Handover State</button>
</div>
<pre class="handover-display" id="ho-10">[HANDOVER STATE AT 01:40.0]:
Active Characters: di_tam, ma_ba, minh_khang, my_duyen
Characters State at 01:40.0:
  - di_tam: Standing in ground floor living room holding can of ginger alcohol.
  - ma_ba: Standing on stair landing looking down at di_tam, face dark and resolute.
  - minh_khang: Frozen upstairs in bedroom doorway.
  - my_duyen: Inside bedroom, weeping.
Props State:
  - can_ruou_gung: In di_tam's hands.
Setting: Townhouse living room and staircase
Dialogue Audit: di_tam 15 words, ma_ba 11 words (26 words, ~6.5s of speech; cliffhanger hook trigger).
Kinetic Momentum Bridge: Directly fuels Episode 2 (Chiếc Võng Sắt & Tiếng Cười Mỉa Đầu Hẻm).</pre>
</div>
</div>
'''

s05_start = content.find('<div class="scene-card" id="s-05">')
assert s05_start != -1, "Scene 05 start not found"

s10_end = content.find('<!-- Master Batch Toolbar -->', s05_start)
if s10_end == -1:
    s10_end = content.find('<div id="toast"', s05_start)
assert s10_end != -1, "Scene 10 end boundary not found"

new_scenes_05_10 = s05_new + "\n\n" + s06_new + "\n\n" + s07_new + "\n\n" + s08_new + "\n\n" + s09_new + "\n\n" + s10_new + "\n\n"

content = content[:s05_start] + new_scenes_05_10 + content[s10_end:]

with open(TAP_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Scenes 05-10 rewritten with perfect Multi-Modal anchors and varied splits!")

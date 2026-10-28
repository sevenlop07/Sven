import re
import sys

# Define the 10 upgraded prompts
prompts = {}

prompts["p-01"] = """Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track A — one continuous take, zero cuts.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, unbroken single-shot pedestal lift from macro downward insert to a held medium close-up, easing back into an intimate two-shot across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], at dawn. Warm low golden morning sunlight filtering through sheer curtains, delicate airborne dust motes floating above patterned floor tiles, quiet intimate domestic postpartum atmosphere.

[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
minh_khang [Appearance, attire, and facial features Refer to image 2],
be_tin [Appearance, attire, and facial features Refer to image 3],

[PROP]:
bat_chao [100% Refer to image prop_chao_thit_4view.jpg]; binh_hut_sua [100% Refer to image prop_binh_sua_4view.jpg]; mam_nhom [100% Refer to image prop_mam_nhom_4view.jpg]; noi_go [100% Refer to image prop_crib_4view.jpg]

Diegetic room acoustics: thin hungry newborn whimper off-screen from wooden crib, heavy teardrop splashing onto congealed congee film, porcelain spoon resting on circular aluminum tray, soft choking sob, rustle of cotton fabric, peaceful distant morning room tone.

[00:00–00:03.0] The unbroken camera opens in a tight downward macro insert over the round aluminum tray on the floor tiles between the queen bed and the wooden pine crib: a bowl of cold postpartum congee displays a delicate congealed starch film skin, resting beside a bone-dry 0ml transparent breast pump bottle. my_duyen sits on the patterned floor tiles leaning back against the queen bed frame; in weakened physical state with trembling limbs, neat white medical clinic adhesive tape wrapped over the thin wrist, my_duyen's pale fingers lose grip on the white porcelain spoon as a heavy teardrop splashes down from above, puncturing the surface tension of the congealed congee film; a stifled sob escapes my_duyen's lips, overwhelmed by somatic exhaustion and maternal helplessness. In the background pine crib beside the bed, be_tin lies safely on the firm flat organic cotton mattress in undisturbed slumber, breathing softly with tiny fists curled beside rosy cheeks. On the spoon's rest the camera begins a slow pedestal lift, tracking upward toward my_duyen's face.

[00:03.0–00:08.0] The pedestal lift slows through the final third and lands before my_duyen speaks, at my_duyen's eye level on a frontal medium close-up, then the frame holds still: my_duyen is positioned at screen-left on patterned floor tiles with back resting against the wooden headboard of the queen bed; in an exhausted physical state with slumped posture, my_duyen's chest heaves with shallow breaths as morning sunlight catches streaming tears over hollow cheeks, lips parting in weeping vulnerability to deliver dialogue:
my_duyen: “ Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về... ” (Voice of a 24-year-old Southern Vietnamese woman; lips parting in trembling vulnerable Southern Vietnamese lip-sync, eyes streaming with tears of postpartum exhaustion)
In the soft-focus background inside the pine crib, be_tin rests safely on the flat mattress, shielded by sturdy vertical pine slats in serene tranquility.

[00:08.0–00:10.0] The camera glides back slightly into an intimate low-angle medium two-shot: minh_khang drops swiftly onto both knees on the patterned floor tiles facing my_duyen at the foot of the queen bed; in an upright kneeling posture with protective tension, minh_khang's broad warm palms reach out and clasp my_duyen's cold shaking hands against minh_khang's chest, then rests a forehead softly against the couple's joined hands; with unwavering devotion and silent sorrow, minh_khang's jaw sets with protective resolve. Supported against the bed frame, my_duyen slumps forward into minh_khang's clasp, weeping softly with quiet relief in minh_khang's warm embrace. Inside the background pine crib, be_tin lies peacefully under warm sunbeams, chest rising and falling rhythmically in undisturbed sleep through 00:10.0.

Continuous fluid motion, realistic physics, zero morphing, one unbroken take. Spatial positions anchored. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters."""

prompts["p-02"] = """Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot sequence cut on the 180-degree axis.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, low-angle over-the-shoulder entrance cutting to a rising reverse medium close-up across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Warm golden sunlight streaming through window, wooden doorframe leading to hallway, quiet domestic bedroom atmosphere broken by an arrival.

[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
be_tin [Appearance, attire, and facial features Refer to image 3],

[PROP]:
vong_xep [100% Refer to image prop_hammock_4view.jpg]; mam_nhom [100% Refer to image prop_mam_nhom_4view.jpg]; noi_go [100% Refer to image prop_crib_4view.jpg]

Diegetic room acoustics: sudden bang of the door against the wall, heavy footsteps on floor tiles, metallic clink of the folded hammock frame, infant's soft rhythmic breathing from crib.

[00:00–00:04.5] The door bangs open. From floor level, a low-angle over-the-shoulder medium shot: minh_khang kneels on the patterned floor tiles at screen-left in the foreground, shoulders rigid with protective dread; ma_ba stands upright at the bright wooden doorway at screen-right, clutching the folded stainless steel hammock frame against ma_ba's chest; in a rigid physical stance, ma_ba takes one resolute step across the threshold, eyes darting downward at the floor with brow furrowed in traditional anxiety and sharp protective frustration as ma_ba speaks:
ma_ba: “ Trời đất ơi! Thằng Tin khóc thấu trời... nuôi cháu tao kiểu gì vậy?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in sharp accusatory Southern Vietnamese lip-sync, brow furrowed with traditional anxiety)
Behind minh_khang's knee beside the pine crib, my_duyen sits on the floor tiles in a weak, curled posture, trembling in silent vulnerability as my_duyen slides the clinic-taped wrist out of sight with downcast eyes. Inside the pine crib, be_tin lies flat on the cotton mattress, sleeping peacefully with tiny soft breaths.

[00:04.5–00:10.0] Cut to the reverse angle from behind ma_ba's shoulder, ma_ba's shoulder and graying hair soft-blurred in the foreground at screen-right: a high-angle medium close-up looking down on minh_khang as minh_khang pushes up off the floor tiles. The camera rises and settles before minh_khang speaks, landing firmly at eye level: minh_khang stands firmly at screen-left between ma_ba and my_duyen; in an upright protective posture, minh_khang's open palms fill the space between ma_ba and the bed, brow furrowed with desperate filial pleading and urgent empathy as minh_khang speaks:
minh_khang: “ Con xin má nhỏ tiếng giùm... Duyên thức trắng ba đêm đuối lắm rồi má! ” (Voice of a 27-year-old Southern Vietnamese man; lips parting in breathless urgent Southern Vietnamese lip-sync, eyes pleading for empathy)
The frame holds still at eye level through 00:10.0: ma_ba stands rigid in the doorway holding the hammock stand, eyes narrowed in stern skepticism; in the soft-focus background, my_duyen sits on floor tiles clutching the pine crib rail with silent weeping distress; be_tin sleeps peacefully in the pine crib undisturbed.

Continuous fluid motion, realistic physics, zero morphing, two shots joined by one editorial cut. Spatial positions anchored across the cut. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters."""

prompts["p-03"] = """Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot coverage on the 180-degree axis.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, locked floor-level take on the accusation, cutting on the power shift to a level two-shot that drifts down to the witness across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Sunlight carving distinct warm highlights across floor tiles, bedroom center between wooden crib and doorway.

[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
be_tin [Appearance, attire, and facial features Refer to image 3],

[PROP]:
vong_xep [100% Refer to image prop_hammock_4view.jpg]; mam_nhom [100% Refer to image prop_mam_nhom_4view.jpg]; noi_go [100% Refer to image prop_crib_4view.jpg]

Diegetic room acoustics: metallic clang of steel hammock frame contacting floor tiles, infant's soft fussy coo from crib, tense familial confrontation.

[00:00–00:04.7] Locked frame, low at my_duyen's eye level on the floor beside the crib — the crib slats and my_duyen's trembling shoulder soft in the foreground: ma_ba stands erect at room center facing the pine crib; in a rigid physical stance, ma_ba sets the folded steel hammock stand onto floor tiles with a loud metallic clank, keeping one weathered palm on the frame while pointing an agitated finger toward the pine crib; with chin lifted in stubborn matriarchal pride and traditional conviction, ma_ba speaks:
ma_ba: “ Cái võng này ba mầy đưa từ đỏ hỏn, giờ tụi bây bỏ xó hả?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in proud unhurried Southern Vietnamese lip-sync, chin lifted, staking a claim on family history)
Beside the crib on the floor tiles, my_duyen sits propped against the wooden crib slats in a weakened state, trembling fingers gripping the vertical balusters with helpless sorrow. minh_khang stands near the doorway, alert and tense with anxious filial concern. Inside the pine crib, be_tin lies securely on the flat mattress, stirring gently with tiny soft coos in safe undisturbed slumber.

[00:04.7–00:09.1] Cut to a level three-quarter front two-shot at standing eye level, still on the crib side of the room, static camera: minh_khang steps into room center between ma_ba and the pine crib; in an upright stance facing ma_ba at eye level, minh_khang reaches out with both palms and gently clasps ma_ba's pointing hand, mother and son face to face; with lowered eyes and tender filial reverence wrapped in firm scientific conviction, minh_khang speaks:
minh_khang: “ Xương sống thằng Tin non xèo... nằm nôi phẳng mới êm dịu má! ” (Voice of a 27-year-old Southern Vietnamese man; lips parting in soft careful Southern Vietnamese lip-sync, eyes lowered, a refusal wrapped in tenderness)
Caught inside minh_khang's warm clasp, ma_ba stands motionless at screen-left, weathered expression flickering with startled hesitation as stubborn resistance wavers. In the soft background, my_duyen sits by the crib watching with held breath; be_tin sleeps peacefully on the flat crib mattress.

[00:09.1–00:10.0] In the same take, the camera drifts slowly down past the joined hands to floor level: my_duyen sits on the patterned floor tiles beside the pine crib; in a pale, physically strained condition, my_duyen grips the crib rail with whitening knuckles, pushing upward with desperate determination not to appear fragile; above, ma_ba stands in startled hesitation as ma_ba's gaze drops from minh_khang down to my_duyen with troubled suspicion through 00:10.0; minh_khang maintains gentle hold of ma_ba's hand with vigilant protective care; be_tin rests peacefully in the pine crib.

Continuous fluid motion, realistic physics, zero morphing, two takes joined by one editorial cut. Spatial positions anchored across the cut. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters."""

prompts["p-04"] = """Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track A — one continuous take, zero cuts.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, gentle level tracking shot settling on bedside care across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Dramatic morning sunbeams filtering across bedroom floor tiles, intimate domestic space.

[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
minh_khang [Appearance, attire, and facial features Refer to image 2],
ma_ba [Appearance, attire, and facial features Refer to image 4],
be_tin [Appearance, attire, and facial features Refer to image 3],

[PROP]:
white linen bedding on queen bed; bat_chao [100% Refer to image prop_chao_thit_4view.jpg]; vong_xep [100% Refer to image prop_hammock_4view.jpg]; noi_go [100% Refer to image prop_crib_4view.jpg]

Diegetic room acoustics: soft rustle of bedding fabric, gentle footstep on floor tiles, maternal voice of tender concern.

[00:00–00:04.0] At bed eye level, a three-quarter front medium shot on the queen bed: my_duyen sits propped on the queen bed mattress at screen-left, leaning back against the wooden headboard; in a pale, depleted physical condition with shallow breathing, my_duyen rests trembling hands over the white linen sheet, drained of physical stamina. minh_khang stands at the bedside beside the queen bed; in an attentive, forward-leaning posture, minh_khang places a soft cotton bolster pillow comfortably behind my_duyen's back and gently takes the empty pump bottle from my_duyen's fingers with loving care. ma_ba stands near the bedroom doorway at screen-right holding the warm congee bowl in both hands, the folded hammock already resting safely against the wall; observing my_duyen's pale exhaustion, ma_ba's weathered features soften with maternal concern. Inside the pine crib beside the bed, be_tin lies safely on the firm flat organic cotton mattress, shielded by sturdy pine slats in calm sleep.

[00:04.0–00:10.0] The camera lands and settles before ma_ba speaks, framing ma_ba standing beside the queen bed facing my_duyen: in an upright stance offering the warm porcelain congee bowl, ma_ba's stern demeanor gives way to instinctive parental compassion as ma_ba speaks:
ma_ba: “ Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in concerned maternal Southern Vietnamese lip-sync, stern tone softening into family care)
Resting back against the bolster pillow on the queen bed, my_duyen closes eyes gently, exhaling in quiet relief at the maternal tenderness. minh_khang turns quickly toward the doorway with eager filial relief to fetch warm water. Inside the crib, be_tin rests in serene comfort through 00:10.0.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored throughout the take. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters."""

prompts["p-05"] = """Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot sequence cut on the 180-degree axis.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, over-the-shoulder medium close-up on a bandaged wrist cutting to a reverse close-up of wounded shock across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Warm golden morning sunlight pooling across patterned floor tiles beside queen bed, emotionally charged domestic atmosphere.

[subject]:
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
ma_ba [Appearance, attire, and facial features Refer to image 4],
be_tin [Appearance, attire, and facial features Refer to image 3],

[PROP]:
vong_xep [100% Refer to image prop_hammock_4view.jpg]; mam_nhom [100% Refer to image prop_mam_nhom_4view.jpg]; noi_go [100% Refer to image prop_crib_4view.jpg]

Diegetic room acoustics: sharp intake of breath, rustle of cotton fabric, infant's soft rhythmic breathing from crib, heavy tense silence.

[00:00–00:04.0] From behind ma_ba's shoulder, ma_ba's graying hair soft in the foreground at screen-right, a medium close-up looking toward the floor tiles: minh_khang kneels on the patterned floor tiles firmly supporting my_duyen; my_duyen slumps against minh_khang's chest in a weakened physical condition with pale complexion; as ma_ba reaches forward to help lift my_duyen, ma_ba's weathered fingers catch the edge of my_duyen's sleeve, pulling it up; a neat white square of outpatient clinic adhesive tape on my_duyen's thin wrist is exposed in the foreground; my_duyen quickly turns the wrist inward with panicked embarrassment, but ma_ba's gaze has already locked onto the clinic tape; minh_khang's lips press shut in tense protective guilt. Beside the bed, be_tin lies peacefully inside the pine crib, chest rising and falling in rhythmic sleep.

[00:04.0–00:10.0] Cut to the reverse eye-level close-up of ma_ba on the 180-degree axis, static camera: ma_ba kneels upright facing the bed; in a stunned physical freeze with fingers hovering in mid-air beside the exposed medical tape, ma_ba's eyes widen in disbelief, throat tightening with acute hurt as injured matriarchal pride surges and ma_ba speaks:
ma_ba: “ Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in choked sharp Southern Vietnamese lip-sync, eyes wide with bitter wounded pride)
The frame holds as ma_ba stares at the clinic bandage: in the background, my_duyen sits curled against minh_khang's chest, tucking the wrist away in tearful shame; minh_khang holds my_duyen with defensive resolve as heavy silence thickens through 00:10.0; inside the pine crib, be_tin rests in calm safety.

Continuous fluid motion, realistic physics, zero morphing, two shots joined by one editorial cut. Spatial positions anchored across the cut. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters."""

prompts["p-06"] = """Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track A — one continuous take, zero cuts.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, unbroken single-shot intimate tracking glide on emotional rejection across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Sunlight carving sharp shadows across edge of queen bed, tense fractured domestic atmosphere.

[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
be_tin [Appearance, attire, and facial features Refer to image 3],

[PROP]:
white linen bedding on queen bed; noi_go [100% Refer to image prop_crib_4view.jpg]

Diegetic room acoustics: rustle of cotton bedding, sharp intake of breath, heavy vibrating silence of familial rupture.

[00:00–00:05.2] At the eye level of the two women, the unbroken camera glides closely into an intimate three-quarter front two-shot on the edge of the queen bed: my_duyen sits propped against pillows on the queen bed mattress at screen-left; in an upright posture with pale face and trembling chin, my_duyen pulls the bandaged wrist sharply behind back, lowering eyes to avoid ma_ba's gaze in cold, guarded defensive pride as my_duyen speaks:
my_duyen: “ Dạ con tự ráng được mà má... má bận lòng làm chi thêm nữa nè... ” (Voice of a 24-year-old Southern Vietnamese woman; lips parting in cold cracked Southern Vietnamese lip-sync, lips trembling, looking away)
Kneeling on the floor tiles at screen-right, ma_ba freezes in mid-motion, weathered face tightening as the cold words strike. minh_khang stands tense at the bedside, dread mounting. In the background crib, be_tin lies peacefully asleep on the firm flat mattress.

[00:05.2–00:10.0] Holding level height, the camera drifts slightly wider: ma_ba recoils as if struck, rising stiffly to full standing height beside the queen bed; in an erect, towering physical posture with chest heaving in offended matriarchal pride, ma_ba glares down at my_duyen, weathered face darkening with bitter outrage as ma_ba speaks:
ma_ba: “ Mèn đéc ơi... mầy coi tao như người dưng nước lã thiệt rồi hả?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in harsh trembling Southern Vietnamese lip-sync, chest heaving with offended matriarchal pride)
minh_khang steps directly between the two women at room center, raising open palms in frantic protective pleading to prevent a total rupture. On the queen bed, my_duyen sits with lowered head, biting trembling lips as silent tears fall. In the background pine crib, be_tin sleeps peacefully through 00:10.0.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored throughout the take. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters."""

prompts["p-07"] = """Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot coverage on the 180-degree axis.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, accusatory medium shot at doorway cutting to an anguished reverse close-up across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Harsh angular sunlight cutting through dust motes across wooden doorway, deepening domestic conflict.

[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
be_tin [Appearance, attire, and facial features Refer to image 3],

[PROP]:
wooden doorframe; white linen bedding on queen bed; noi_go [100% Refer to image prop_crib_4view.jpg]

Diegetic room acoustics: trembling vocal timbre, heavy footsteps on floor tiles, tense emotional collision.

[00:00–00:04.8] Eye-level medium shot on ma_ba standing at the bedroom wooden doorframe: ma_ba stands rigid at the wooden doorway threshold at screen-right; in a stiff erect posture with trembling shoulders, ma_ba points a shaking weathered finger back into the bedroom toward the queen bed, tears of angry frustration and wounded maternal dignity brimming in aged eyes as ma_ba speaks:
ma_ba: “ Trời ơi tao lặn lội lên đây... đâu phải để tụi bây xua đuổi tao?! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in choked accusatory Southern Vietnamese lip-sync, chin trembling with wounded dignity)
minh_khang stands in room center facing ma_ba at screen-left, leaning forward with palms open in desperate filial pleading. In the soft background on the queen bed edge, my_duyen sits curled inward, weeping silently. Inside the pine crib, be_tin rests safely on the flat mattress, stirring softly in undisturbed sleep.

[00:04.8–00:10.0] Cut to the reverse angle on the 180-degree axis, a medium close-up of minh_khang facing ma_ba: minh_khang stands in the bedroom doorway threshold at screen-left; in an upright stance with hands raised in desperate filial supplication, brow deeply knotted in anguish, minh_khang steps toward ma_ba, pleading for empathy and domestic mercy:
minh_khang: “ Con lạy má luôn đó! Duyên đuối sức lắm, má nói vậy tội nghiệp nó má! ” (Voice of a 27-year-old Southern Vietnamese man; lips parting in anguished urgent Southern Vietnamese lip-sync, eyes pleading for mercy)
The frame holds on minh_khang's strained expression: ma_ba stands opposite with back to camera, fists clenched in stony, unforgiving pride through 00:10.0; on the bed in background, my_duyen weeps silently; inside the pine crib, be_tin sleeps peacefully.

Continuous fluid motion, realistic physics, zero morphing, two shots joined by one editorial cut. Spatial positions anchored across the cut. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters."""

prompts["p-08"] = """Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track A — one continuous take, zero cuts.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, unbroken single-shot slow tracking glide on wounded pride across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Sunlight glinting cold off stainless steel hammock frame near doorway, freezing domestic atmosphere.

[subject]:
ma_ba [Appearance, attire, and facial features Refer to image 4],
minh_khang [Appearance, attire, and facial features Refer to image 2],
my_duyen [Appearance, attire, and facial features Refer to image 1],
be_tin [Appearance, attire, and facial features Refer to image 3],

[PROP]:
vong_xep [100% Refer to image prop_hammock_4view.jpg]; noi_go [100% Refer to image prop_crib_4view.jpg]

Diegetic room acoustics: heavy hollow footsteps turning away, chilly silence settling over room.

[00:00–00:03.8] At doorway height, the unbroken camera frames ma_ba standing rigid in the wooden doorframe at screen-right: ma_ba stands in an unyielding, erect physical posture with squared shoulders; ma_ba's gaze drops down to the folded stainless steel hammock frame lying rejected on the floor tiles, jaw tightening with stubborn wounded matriarchal pride and icy resentment. In the soft background beside the pine crib, minh_khang stands with head bowed low and shoulders slumped in helpless defeat. At screen-left on the queen bed edge, my_duyen sits bowed over, weeping silently into hands. Inside the pine crib, be_tin lies peacefully on the flat mattress, breathing softly in calm slumber.

[00:03.8–00:10.0] ma_ba raises chin and glares across the bedroom with cold finality: standing at the wooden threshold, ma_ba snaps gaze toward the queen bed, chin lifted high in defiant pride as lips tighten with bitter rebuke:
ma_ba: “ Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao! ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in icy bitter Southern Vietnamese lip-sync, lips tightened with stubborn pride)
The camera tracks slowly backward as ma_ba turns sharply away from the bedroom and exits down the hallway through 00:10.0. minh_khang stands frozen in place beside the crib, watching mother depart in heavy silence. On the queen bed, my_duyen weeps silently into hands. Inside the crib, be_tin sleeps peacefully.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored throughout the take. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters."""

prompts["p-09"] = """Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track A — one continuous take, zero cuts.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, unbroken single-shot slow intimate push-in on exhausted grief across ten seconds.

[context]:
phong_cu [100% Refer to image location_bedroom_4view.jpg], morning. Long somber shadows stretching across floor tiles beside queen bed, suffocating quiet domestic atmosphere.

[subject]:
my_duyen [Appearance, attire, and facial features Refer to image 1],
minh_khang [Appearance, attire, and facial features Refer to image 2],
be_tin [Appearance, attire, and facial features Refer to image 3],

[PROP]:
white linen bedding on queen bed; bat_chao [100% Refer to image prop_chao_thit_4view.jpg]; noi_go [100% Refer to image prop_crib_4view.jpg]

Diegetic room acoustics: soft muffled weeping, ragged breathing, quiet heavy ticking of bedroom clock.

[00:00–00:04.2] Slow intimate push-in on the couple sitting together on the edge of the queen bed: my_duyen sits slumped on the queen bed edge at screen-left; in a collapsed physical state, trembling with deep exhaustion, my_duyen buries face into minh_khang's chest, clutching minh_khang's shirt fabric with pale hands. minh_khang sits closely beside my_duyen on the bed mattress; in a protective seated posture, minh_khang wraps arms tightly around my_duyen's trembling shoulders, resting chin against my_duyen's hair with loving tenderness and silent sorrow; long somber morning shadows stretch across the floor tiles where the congee bowl sits on the tray. Inside the wooden pine crib beside the bed, be_tin lies safely on the organic cotton mattress, breathing softly in calm sleep.

[00:04.2–00:10.0] The camera pushes in close to my_duyen's tear-streaked face resting against minh_khang's shoulder: held in minh_khang's arms on the queen bed, my_duyen's pale hollow cheeks glisten with streaming tears; in total physical depletion, drained of all fight, my_duyen parts trembling lips to speak in a muffled, sorrowful whisper against minh_khang's chest:
my_duyen: “ Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này... ” (Voice of a 24-year-old Southern Vietnamese woman; lips parting in broken faint Southern Vietnamese lip-sync, muffled against shoulder, drained of fight)
minh_khang closes eyes, jaw clenching in silent heartache, arms tightening around my_duyen as the frame holds still through 00:10.0. Inside the background pine crib, be_tin sleeps peacefully under the warm morning sunbeams.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored throughout the take. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters."""

prompts["p-10"] = """Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot sequence cut on the 180-degree axis.

Modern K-Drama Premium Cinematography, high-key beauty illumination, luminescent skin rendering, soft pastel urban palette, creamy background bokeh, elegant tracking camera motion, romantic atmospheric glow, pristine digital finish, aggressive wide entrance cutting to a reverse low-angle close-up across ten seconds.

[context]:
Townhouse ground floor living room and front doorway [100% Refer to image location_livingroom_4view.jpg], morning. Bright morning daylight flooding through front doorway, high domestic tension.

[subject]:
di_tam [Appearance, attire, and facial features Refer to image ditam_modelsheet.jpg],
ma_ba [Appearance, attire, and facial features Refer to image 4],

[PROP]:
can_ruou_gung [100% Refer to image prop_jug_4view.jpg]; polished wooden stair banister; living room tiled floor

Diegetic room acoustics: loud rattle of iron gate, squeak of rubber sandals on tiles, piercing female voice, abrupt cut to black.

[00:00–00:04.8] Eye-level medium shot from inside the living room toward the front entrance: di_tam pushes open the wooden door and barges into the townhouse living room at screen-left; in an aggressive, energetic physical stance, di_tam marches across the tiled floor, clutching the white plastic jug of ginger alcohol firmly against chest with sharp, intrusive gestures; with eyes flashing in malicious neighborhood gossip and eager instigation, di_tam speaks in a loud piercing voice:
di_tam: “ Bà Ba ơi! Con dâu leo tuốt lên đầu ngồi, bà nhịn cho đặng hả?! ” (Voice of a 58-year-old Southwestern Vietnamese neighbor; lips parting in loud piercing Southern Vietnamese lip-sync, gesturing with the plastic jug)
On the wooden stair landing in the background, ma_ba stands unmoving, looking down toward the front entrance.

[00:04.8–00:10.0] Cut to the reverse angle on the 180-degree axis, a low-angle medium close-up of ma_ba standing on the stair landing looking down: ma_ba stands at screen-right on the polished wooden stair landing; in a rigid upright posture, ma_ba's weathered knuckles turn bone-white gripping the wooden banister, face hardened in bitter wounded pride and matriarchal defeat as ma_ba leans forward, beckoning upstairs with a bitter, trembling voice:
ma_ba: “ Chị Tám ơi... vô coi giùm thằng nhỏ, chớ tui bải hoải tay chân hết trơn... ” (Voice of a 56-year-old Southwestern Vietnamese mother; lips parting in trembling bitter Southern Vietnamese lip-sync, beckoning upstairs)
At the base of the stairs, di_tam looks up with eager, scheming satisfaction. Immediate cut to black on ma_ba's hardened, unforgiving gaze at 00:10.0.

Continuous fluid motion, realistic physics, zero morphing, two shots joined by one editorial cut. Spatial positions anchored across the cut. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters."""

# Read tap-1.html
with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace each prompt block
for p_id, p_text in prompts.items():
    pattern = rf'(<pre[^>]*id="{p_id}"[^>]*>).*?(</pre>)'
    if not re.search(pattern, content, re.DOTALL):
        print(f"ERROR: Could not find {p_id} in tap-1.html")
        sys.exit(1)
    content = re.sub(pattern, rf'\g<1>{p_text}\g<2>', content, flags=re.DOTALL)
    print(f"Successfully replaced {p_id}")

with open('output/com-khong-chan-nuoc-mat/tap-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved output/com-khong-chan-nuoc-mat/tap-1.html successfully!")

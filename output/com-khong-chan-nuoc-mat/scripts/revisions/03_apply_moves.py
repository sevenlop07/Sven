"""Apply §3.2.0 Movement Doctrine fixes + Track AB conversions (s03, s07) to tap-1.html.

Every edit is scoped to one scene card and must match exactly once.
"""
import os
import re
import shutil

PATH = r"d:\Project\Sven\output\com-khong-chan-nuoc-mat\tap-1.html"
BACKUP = r"C:\Users\adminb\.gemini\antigravity-ide\brain\675ad7a4-b5b9-44e1-8352-f5e3fb2587ea\scratch\tap-1.before-moves.html"
if not os.path.exists(BACKUP):
    shutil.copyfile(PATH, BACKUP)
h = open(PATH, encoding="utf-8", newline="").read()

A_BADGE = "Track A · Single-Shot Continuous Take"
AB_BADGE = "Track AB · Hybrid (Take + 1 Cut · 180° Axis)"
A_PREFIX = "Track A — one continuous take, zero cuts."
AB_PREFIX = "Track AB — one continuous take punctuated by a cut on the 180-degree axis."
A_CLOSE = "Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored throughout the take."

L_MABA_03 = "Má Ba: “Xưa giờ cả họ nằm võng! Nôi gỗ lạnh ngắt vầy sao ngủ?!” (Voice of a 56-year-old Southwestern Vietnamese woman; forceful traditional admonition lip-sync, eyes fiercely defending family customs)"
L_KHANG_03 = "Minh Khang: “Bác sĩ dặn nằm nôi phẳng cho thẳng lưng má.” (Voice of a 27-year-old Southern Vietnamese man; earnest medical pleading lip-sync, brow furrowed in loving worry)"
L_MABA_07 = "Má Ba: “Ầu ơ... có hơi bà nội đây, cháu ngủ ngoan như nằm võng nghen.” (Voice of a 56-year-old Southwestern Vietnamese woman; warm crooning lullaby Southern lip-sync, radiant grandmotherly smile)"

EDITS = {
    "global": [
        ('<span class="badge badge-gold">100% SINGLE-SHOT CONTINUOUS TAKE</span>',
         '<span class="badge badge-gold">TRACK A · B · AB — CHOSEN PER SCENE</span>'),
        ("theo Luật Single-Shot Tuyệt Đối (100% Unbroken Continuous Takes, Zero Mid-Scene Cuts).",
         "với ngôn ngữ máy quay chọn theo từng cảnh (Track A một hơi liền, Track B cắt trên trục 180°, Track AB lai take + cắt)."),
    ],
    # ---------------- SCENE 01: lift starts on the clatter, lands before the line ----------------
    "s-01": [
        ("as a stifled sob escapes trembling lips.",
         "as a stifled sob escapes trembling lips. On the spoon's clatter the camera begins a slow pedestal lift, following the tear's path upward toward its source."),
        ("[00:03.5–00:07.5] In an unbroken smooth pedestal lift and gentle push-in, the camera glides up to eye level, framing a frontal medium close-up of my_duyen leaning weakly against the bed frame",
         "[00:03.5–00:07.5] The pedestal lift slows through its final third and lands before my_duyen speaks, at my_duyen's eye level on a frontal medium close-up, then the frame holds still: my_duyen leaning weakly against the bed frame"),
        ("unbroken single-shot continuous push-in from macro downward insert to intimate medium two-shot across ten seconds.",
         "unbroken single-shot pedestal lift from macro downward insert to a held medium close-up, easing back into an intimate two-shot across ten seconds."),
        ("Single Continuous Take (Macro Push-In Rising to a Two-Shot Glide):",
         "Single Continuous Take (Macro Insert, Pedestal Lift Landing on Duyên, Easing Back to a Two-Shot):"),
        ("sending the porcelain spoon clattering loudly onto the aluminum tray.<br/>",
         "sending the porcelain spoon clattering loudly onto the aluminum tray. On the clatter the camera begins a slow pedestal lift, following the tear's path upward toward its source.<br/>"),
        ("In an unbroken smooth pedestal lift and gentle push-in, the camera rises to eye level, framing a frontal medium close-up of Mỹ Duyên leaning weakly against the bed frame.",
         "The pedestal lift slows and lands before she speaks, at Duyên's eye level on a frontal medium close-up, and the frame holds still: Mỹ Duyên leans weakly against the bed frame."),
        ("Mỹ Duyên [00:03.8 – 00:06.3]", "Mỹ Duyên [00:04.2 – 00:06.7]"),
    ],
    # ---------------- SCENE 02: the rise lands, then Khang speaks ----------------
    "s-02": [
        ("who weeps in soft focus behind minh_khang beside the pine crib:",
         "who weeps in soft focus behind minh_khang beside the pine crib; only once the camera settles does minh_khang speak:"),
        ("palms raised between his mother and Mỹ Duyên, who weeps in soft focus beside the pine crib.",
         "palms raised between his mother and Mỹ Duyên, who weeps in soft focus beside the pine crib. Only once the camera settles does he speak."),
        ("Minh Khang [00:14.8 – 00:17.3]", "Minh Khang [00:16.2 – 00:18.7]"),
    ],
    # ---------------- SCENE 03: Track AB — Take → Cut → Take ----------------
    "s-03": [
        (A_BADGE, AB_BADGE),
        (A_PREFIX, AB_PREFIX),
        ("unbroken single-shot steadycam arc orbit across ten seconds.",
         "locked floor-level take on the accusation, cutting on the power shift to a level two-shot that drifts down to the witness across ten seconds."),
        ("[00:00–00:05.0] The unbroken camera begins low at my_duyen's eye level on the floor beside the crib, the crib slats and my_duyen's trembling shoulder soft in the foreground, looking up at ma_ba",
         "[00:00–00:04.5] Locked frame, low at my_duyen's eye level on the floor beside the crib — the crib slats and my_duyen's trembling shoulder soft in the foreground, looking up at ma_ba"),
        ("[00:05.0–00:10.0] In one swift unbroken ninety-degree arc, the camera rises from the floor to standing eye level as minh_khang steps in and gently takes ma_ba's pointing hand; the arc lands on a level three-quarter front two-shot of mother and son, neither face above the other, and only once the camera settles does minh_khang speak with calm yet firm filial plea:",
         "[00:04.5–00:08.5] Cut to a level three-quarter front two-shot at standing eye level, still on the crib side of the room, static camera — minh_khang steps in between ma_ba and the crib and gently takes ma_ba's pointing hand in both palms, mother and son face to face, neither face above the other, and minh_khang speaks with calm yet firm filial plea:"),
        ("The camera glides into an over-the-shoulder frame holding ma_ba's startled hesitation as ma_ba looks from minh_khang to the pale trembling mother clinging to the crib rail through 00:10.0.",
         "\r\n[00:08.5–00:10.0] In the same take, the camera drifts slowly down past the joined hands to floor level — my_duyen clings to the crib rail in the foreground, knuckles whitening as my_duyen begins to push up, while ma_ba's startled hesitation stays soft above as ma_ba looks from minh_khang down to my_duyen through 00:10.0."),
        ("Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored throughout the take.",
         "Continuous fluid motion, realistic physics, zero morphing, two takes joined by one editorial cut. Spatial positions anchored across the cut."),
        # Tier 1 card (whole value)
        ("[00:00–00:10.0] Single Continuous Take (Ninety-Degree Arc Orbit Around the Confrontation):<br/>The unbroken camera begins low at Duyên's floor-level eyeline beside the crib, her trembling shoulder soft in the foreground, looking up at Má Ba slamming the folded steel hammock stand onto the bedroom tiles with a resounding metallic clank. Má Ba steps forward, pointing an agitated weathered finger directly toward the modern pine crib.<br/>"
         + L_MABA_03 +
         "<br/><br/>In one swift 90-degree arc the camera rises from the floor to standing eye level as Minh Khang steps in and gently takes his mother's pointing hand; the arc lands on a level three-quarter two-shot of mother and son before he speaks, calm yet firm.<br/>"
         + L_KHANG_03 +
         "<br/>The camera glides into an over-the-shoulder frame holding Má Ba's startled hesitation as she looks from her son to the pale trembling mother clinging to the crib rail.",
         "[00:00–00:10.0] Track AB — Take → Cut → Take (Floor-Level Accusation, Cut on the Power Shift, Drift Down to the Witness):<br/>"
         "<strong>[00:00–00:04.5] Take 1 — Locked Low Frame at Duyên's Eyeline:</strong> The camera holds low at Duyên's floor-level eyeline beside the crib, her trembling shoulder soft in the foreground, looking up at Má Ba slamming the folded steel hammock stand onto the bedroom tiles with a resounding metallic clank. Má Ba steps forward, pointing an agitated weathered finger directly toward the modern pine crib.<br/>"
         + L_MABA_03 +
         "<br/><br/><strong>[00:04.5–00:08.5] Cut on the 180° Axis — Level Two-Shot at Standing Eye Level:</strong> Staying on the crib side of the room, the cut lands on mother and son face to face as Minh Khang steps in and gently takes his mother's pointing hand in both palms — neither face above the other. The camera is static; he speaks, calm yet firm.<br/>"
         + L_KHANG_03 +
         "<br/><br/><strong>[00:08.5–00:10.0] Same Take — Drift Down to the Witness:</strong> The camera drifts slowly down past the joined hands to floor level: Duyên clings to the crib rail in the foreground, knuckles whitening as she begins to push up, while Má Ba's startled hesitation hangs soft above her."),
        ("Má Ba [00:20.8 – 00:24.0]", "Má Ba [00:20.5 – 00:23.7]"),
        ("Minh Khang [00:26.0 – 00:28.5]", "Minh Khang [00:25.0 – 00:27.5]"),
    ],
    # ---------------- SCENE 07: Track AB — Take → Button ----------------
    "s-07": [
        (A_BADGE, AB_BADGE),
        (A_PREFIX, AB_PREFIX),
        ("unbroken single-shot crane tilt across ten seconds.",
         "low crib-level take settling on a lullaby, cutting to a silent frontal close-up of the witness across ten seconds."),
        ("[00:00–00:05.5] The camera begins low at crib-mattress level beside be_tin, looking up past the folded silk at ma_ba's face as ma_ba leans gently across the railing, neatly folding the soft brown silk Ba Ba shirt and tucking the scented garment tenderly beside the sleeping newborn infant:",
         "[00:00–00:02.8] Low at crib-mattress level beside be_tin, slow lateral drift along the rail — the camera follows the soft brown silk Ba Ba shirt as ma_ba leans gently across the railing, neatly folds the garment and tucks the scented silk tenderly beside the sleeping newborn infant, and the drift settles on ma_ba's face above the rail.\r\n\r\n"
         "[00:02.8–00:07.5] In the same take, locked frame looking up past the folded silk at ma_ba's face, already settled before ma_ba sings — ma_ba rests both weathered hands on the rail and croons softly down to be_tin:"),
        ("[00:05.5–00:10.0] In the same unbroken take, the camera cranes up and glides across to the queen bed, settling on a frontal medium close-up of my_duyen at the bed edge, eyes shining with tears of deep gratitude and domestic peace; no words — trembling fingertips rise to closed lips as a silent tearful smile spreads across my_duyen's face.\r\n"
         "The camera slows to a gentle floating rest: the infant inhales the familiar scent of grandmotherly silk and sleeps serenely through 00:10.0.",
         "[00:07.5–00:10.0] Cut to a frontal medium close-up of my_duyen at the queen bed edge across the room, eye level, locked frame — eyes shining with tears of deep gratitude and domestic peace; no words — trembling fingertips rise to closed lips as a silent tearful smile spreads across my_duyen's face, minh_khang standing soft-focus beside the bed through 00:10.0."),
        ("Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored throughout the take.",
         "Continuous fluid motion, realistic physics, zero morphing, one continuous take closed by one editorial cut. Spatial positions anchored across the cut."),
        ("[00:00–00:10.0] Single Continuous Take (Low Crib-Level Angle Rising into a Crane Glide to the Bedside):<br/>The camera begins low at crib-mattress level, looking up at Má Ba's face as Má Ba leans gently across the railing, neatly folding her soft vintage brown silk Ba Ba shirt. With reverent maternal tenderness, she tucks the scented garment beside the sleeping newborn infant.<br/>"
         + L_MABA_07 +
         "<br/><br/>Continuous smooth camera crane tilting up and gliding across to the queen bed without cutting: Mỹ Duyên watches from the bed edge, her eyes shining with tears of deep gratitude and domestic peace, her lips parting in a serene smile.<br/>No words — Mỹ Duyên presses trembling fingertips to her lips, a tearful smile answering in silence.<br/>The camera slows to a gentle floating rest: the infant inhales the familiar scent of his grandmother's silk and sleeps serenely, uniting traditional maternal warmth with medical infant care.",
         "[00:00–00:10.0] Track AB — Take → Button (Crib-Level Lullaby Take, Cut to the Silent Witness):<br/>"
         "<strong>[00:00–00:02.8] Take — Slow Drift Along the Crib Rail:</strong> Low at crib-mattress level, the camera drifts along the railing following Má Ba's soft vintage brown silk Ba Ba shirt as she folds it and, with reverent maternal tenderness, tucks the scented garment beside the sleeping newborn — the drift settles on her face above the rail.<br/><br/>"
         "<strong>[00:02.8–00:07.5] Same Take — Locked Frame on the Lullaby:</strong> Already settled, the frame holds still, looking up past the folded silk as Má Ba rests both hands on the rail and croons down to her grandson.<br/>"
         + L_MABA_07 +
         "<br/><br/><strong>[00:07.5–00:10.0] Cut to the Witness — Frontal Medium Close-Up of Mỹ Duyên, Locked Frame:</strong> Across the room at the bed edge, Mỹ Duyên's eyes shine with tears of deep gratitude. No words — she presses trembling fingertips to her lips, a tearful smile answering in silence, Minh Khang soft beside the bed."),
        ("Má Ba [01:00.8 – 01:04.2]", "Má Ba [01:03.1 – 01:06.5]"),
    ],
    # ---------------- SCENE 08: motivated pivot, no trailing move ----------------
    "s-08": [
        ("[00:04.5–00:10.0] Without cutting, the camera pivots back toward the veranda doorway and settles before ma_ba speaks,",
         "[00:04.5–00:10.0] Without cutting, the camera follows minh_khang's glance and pivots back toward the veranda doorway, settling before ma_ba speaks,"),
        ("The camera slowly widens: potted palms sway in river breeze, casting morning shadows across veranda tiles in peaceful harmony through 00:10.0.",
         "The frame holds on ma_ba's amused face while potted palms sway in the river breeze behind ma_ba, casting morning shadows across veranda tiles through 00:10.0."),
        ("Without cutting, the camera pivots back to the veranda doorway and settles before she speaks,",
         "Without cutting, the camera follows Khang's glance and pivots back to the veranda doorway, settling before she speaks,"),
        ("The camera slowly widens: potted palms sway in the fresh river wind, casting playful morning shadows across the veranda tiles in peaceful family harmony.",
         "The frame holds on her amused face while potted palms sway in the fresh river wind behind her, casting playful morning shadows across the veranda tiles."),
    ],
    # ---------------- SCENE 09: one glide that lands on the tableau before the title line ----------------
    "s-09": [
        ("the camera glides sideways and slightly wider without cutting, turning my_duyen's face to three-quarter front: my_duyen swallows the warm soup,",
         "the camera glides sideways and slightly wider without cutting and comes to rest on a golden triangular family tableau before my_duyen speaks — ma_ba on the bed edge, minh_khang standing at my_duyen's shoulder, be_tin asleep in the sunlit crib, my_duyen's face now three-quarter front: my_duyen swallows the warm soup,"),
        ("Only after the line does the camera ease back into a golden triangular family tableau: ma_ba feeds",
         "The frame stays at rest on the tableau: ma_ba feeds"),
        ("the camera glides sideways and slightly wider without cutting, turning her face to three-quarter front: Mỹ Duyên swallows",
         "the camera glides sideways and slightly wider without cutting and comes to rest on the golden family triangle before she speaks, her face now three-quarter front: Mỹ Duyên swallows"),
        ("Only after her line does the camera ease back into a golden triangular family tableau: Má Ba feeds",
         "The frame stays at rest on the tableau: Má Ba feeds"),
        ("Mỹ Duyên [01:25.3 – 01:28.3]", "Mỹ Duyên [01:26.0 – 01:29.0]"),
    ],
    # ---------------- SCENE 10: write the stillness ----------------
    "s-10": [
        ("[00:04.5–00:10.0] Cut to the reverse angle from the doorway side: a low-angle medium close-up",
         "[00:04.5–00:10.0] Cut to the reverse angle from the doorway side, locked frame: a low-angle medium close-up"),
        ("Low-Angle Medium Close-Up as Má Ba pops up into frame:",
         "Locked Low-Angle Medium Close-Up as Má Ba pops up into frame:"),
    ],
}


def scene_span(text, sid):
    m = re.search(r'<div class="scene-card" id="%s">' % sid, text)
    assert m, f"scene {sid} not found"
    nxt = re.search(r'<div class="scene-card" id="s-\d+">|<div id="toast"', text[m.end():])
    end = m.end() + nxt.start() if nxt else len(text)
    return m.start(), end


total = 0
for sid, edits in EDITS.items():
    for old, new in edits:
        if sid == "global":
            a, b = 0, len(h)
        else:
            a, b = scene_span(h, sid)
        block = h[a:b]
        n = block.count(old)
        assert n == 1, f"{sid} COUNT {n}: {old[:100]}"
        h = h[:a] + block.replace(old, new) + h[b:]
        total += 1

open(PATH, "w", encoding="utf-8", newline="").write(h)
print(f"APPLIED {total} edits; backup -> {BACKUP}")

"""Apply the §3.0 Angle Decision Doctrine fixes to scenes 03, 04, 06, 08, 09 of tap-1.html."""
import re

PATH = r"d:\Project\Sven\output\com-khong-chan-nuoc-mat\tap-1.html"
h = open(PATH, encoding="utf-8", newline="").read()

EDITS = [
    # ---------------- SCENE 03 ----------------
    # Prompt phase 1: Duyén's floor-level eyeline looking up at Má Ba
    ("[00:00–00:05.0] The unbroken camera begins on ma_ba setting the folded steel hammock stand onto floor tiles with a loud metallic clank, pointing an agitated weathered finger toward the pine crib:",
     "[00:00–00:05.0] The unbroken camera begins low at my_duyen's eye level on the floor beside the crib, the crib slats and my_duyen's trembling shoulder soft in the foreground, looking up at ma_ba in three-quarter front as ma_ba sets the folded steel hammock stand onto floor tiles with a loud metallic clank, pointing an agitated weathered finger toward the pine crib:"),
    # Prompt phase 2: arc lands level BEFORE the line
    ("[00:05.0–00:10.0] Executing an unbroken ninety-degree arc orbit around the confrontation, the camera tracks minh_khang stepping in, gently taking ma_ba's pointing hand, speaking with calm yet firm scientific filial plea:",
     "[00:05.0–00:10.0] In one swift unbroken ninety-degree arc, the camera rises from the floor to standing eye level as minh_khang steps in and gently takes ma_ba's pointing hand; the arc lands on a level three-quarter front two-shot of mother and son, neither face above the other, and only once the camera settles does minh_khang speak with calm yet firm filial plea:"),
    # Tier 1
    ("The unbroken camera begins on Má Ba slamming the folded steel hammock stand",
     "The unbroken camera begins low at Duyên's floor-level eyeline beside the crib, her trembling shoulder soft in the foreground, looking up at Má Ba slamming the folded steel hammock stand"),
    ("Continuous unbroken camera orbit arcing 90 degrees around the confrontation without cutting: Minh Khang steps in, gently taking his mother's pointing hand, speaking with calm yet firm scientific filial plea.",
     "In one swift 90-degree arc the camera rises from the floor to standing eye level as Minh Khang steps in and gently takes his mother's pointing hand; the arc lands on a level three-quarter two-shot of mother and son before he speaks, calm yet firm."),
    ("Minh Khang [00:25.3 – 00:27.8]", "Minh Khang [00:26.0 – 00:28.5]"),

    # ---------------- SCENE 04 ----------------
    ("[00:00–00:04.0] The unbroken camera focuses closely on my_duyen attempting to push up from patterned floor tiles using the pine crib rail to apologize.",
     "[00:00–00:04.0] At my_duyen's own low eye level beside the crib rail, a three-quarter front close shot: my_duyen attempts to push up from patterned floor tiles using the pine crib rail to apologize."),
    ("only a thin, shaking exhale as the head tilts limp with postpartum exhaustion.",
     "only a thin, shaking exhale as the head tilts limp with postpartum exhaustion, and the camera sinks with my_duyen all the way down to floor level."),
    ("[00:04.0–00:10.0] The camera descends in a rapid tilt as ma_ba gasps in horror, hands unclamping as the steel hammock stand clatters onto floor tiles. ma_ba drops to both knees beside minh_khang who lunges forward, catching my_duyen's falling shoulders before contact with floor tiles:",
     "[00:04.0–00:10.0] The camera, already settled at floor level beside my_duyen, stays low and waits: above the frame ma_ba gasps in horror, hands unclamping as the steel hammock stand clatters onto floor tiles. ma_ba drops to both knees beside minh_khang, who lunges forward and catches my_duyen's falling shoulders before contact with floor tiles, and ma_ba's face comes down into the lens's eye line, three-quarter front:"),
    # Tier 1
    ("The unbroken camera focuses on Mỹ Duyên attempting to push up from the floor tiles using the crib rail to apologize.",
     "At Mỹ Duyên's own low eye level beside the crib rail, the unbroken camera frames her three-quarter front as she attempts to push up from the floor tiles using the crib rail to apologize."),
    ("Her lips part, but no apology comes — only a thin, shaking exhale.",
     "Her lips part, but no apology comes — only a thin, shaking exhale, and the camera sinks with her to floor level."),
    ("Continuous camera descent and whip tilt without cutting: Má Ba gasps in horror,",
     "The camera, already at floor level, stays low and waits: Má Ba gasps in horror,"),
    ("Má Ba drops to her knees beside Minh Khang who slides across the floor,",
     "Má Ba drops to her knees — down into the lens's eye line — beside Minh Khang, who slides across the floor,"),

    # ---------------- SCENE 06 ----------------
    ("[00:00–00:04.5] The unbroken camera glides closely into an intimate two-shot on the edge of the queen bed:",
     "[00:00–00:04.5] At the seated eye level of the two women, the unbroken camera glides closely into an intimate three-quarter front two-shot on the edge of the queen bed, neither face above the other:"),
    ("[00:04.5–00:10.0] The camera drifts slightly wider as my_duyen leans head softly against ma_ba's shoulder, weeping tears of deep relief and safety,",
     "[00:04.5–00:10.0] Holding the same level height, the camera drifts slightly wider as my_duyen rests a cheek on ma_ba's shoulder with face turned toward the lens, mouth clearly visible, weeping tears of deep relief and safety,"),
    # Tier 1
    ("The unbroken camera glides closely into an intimate two-shot on the edge of the mattress",
     "At the women's seated eye level, the unbroken camera glides closely into an intimate three-quarter front two-shot on the edge of the mattress"),
    ("Continuous camera arc without cutting: Mỹ Duyên breaks down, burying her face wet with tears against Má Ba's brown silk shoulder.",
     "Continuous level drift without cutting: Mỹ Duyên breaks down, resting her tear-wet cheek on Má Ba's brown silk shoulder, face still turned toward the lens."),

    # ---------------- SCENE 08 ----------------
    ("[00:00–00:04.5] The unbroken camera glides forward through sunlit glass doorway onto breezy veranda: minh_khang swiftly unfolds the stainless steel hammock stand with a satisfying metallic click, hanging green mesh canvas and giving gentle test sway:",
     "[00:00–00:04.5] The unbroken camera glides forward through sunlit glass doorway onto breezy veranda and settles at minh_khang's eye level on a three-quarter front medium shot: minh_khang swiftly unfolds the stainless steel hammock stand with a satisfying metallic click, hangs green mesh canvas, gives a gentle test sway, and glances back toward the doorway:"),
    ("[00:04.5–00:10.0] Continuous camera pan and pivot backward toward veranda doorway without cutting: ma_ba stands comfortably framed against door,",
     "[00:04.5–00:10.0] Without cutting, the camera pivots back toward the veranda doorway and settles before ma_ba speaks, at ma_ba's own eye level on a frontal medium shot — no looking up, no looking down; the fight is over: ma_ba stands comfortably framed against door,"),
    # Tier 1
    ("The unbroken camera glides forward through the sunlit glass doorway onto the breezy second-floor veranda:",
     "The unbroken camera glides forward through the sunlit glass doorway onto the breezy second-floor veranda and settles at Minh Khang's eye level, three-quarter front:"),
    ("Continuous camera pan and pivot backward toward the veranda doorway without cutting: Má Ba stands comfortably framed against the door,",
     "Without cutting, the camera pivots back to the veranda doorway and settles before she speaks, at Má Ba's own eye level — no looking up, no looking down; the fight is over: Má Ba stands comfortably framed against the door,"),
    ("Má Ba [01:14.8 – 01:17.6]", "Má Ba [01:15.5 – 01:18.3]"),

    # ---------------- SCENE 09 ----------------
    ("settling on a frontal medium close-up of ma_ba tenderly offering the spoonful to my_duyen. No words:",
     "settling from just beside my_duyen's shoulder, at seated eye level, on a frontal medium close-up of ma_ba tenderly offering the spoonful to my_duyen. No words:"),
    ("[00:05.0–00:10.0] Continuous camera glide upward and wider without cutting: my_duyen swallows the warm soup,",
     "[00:05.0–00:10.0] Staying at my_duyen's seated eye level, the camera glides sideways and slightly wider without cutting, turning my_duyen's face to three-quarter front: my_duyen swallows the warm soup,"),
    ("The camera settles into golden triangular family tableau: ma_ba feeds",
     "Only after the line does the camera ease back into a golden triangular family tableau: ma_ba feeds"),
    # Tier 1
    ("settling on a frontal medium close-up of Má Ba tenderly offering it to Mỹ Duyên.",
     "settling from beside Duyên's shoulder, at seated eye level, on a frontal medium close-up of Má Ba tenderly offering it to Mỹ Duyên."),
    ("Continuous camera glide upward and wider without cutting: Mỹ Duyên swallows the warm soup,",
     "Staying at Duyên's seated eye level, the camera glides sideways and slightly wider without cutting, turning her face to three-quarter front: Mỹ Duyên swallows the warm soup,"),
    ("The camera settles into a golden triangular family tableau: Má Ba feeds",
     "Only after her line does the camera ease back into a golden triangular family tableau: Má Ba feeds"),
]

for old, new in EDITS:
    n = h.count(old)
    assert n == 1, f"COUNT {n}: {old[:90]}"
    h = h.replace(old, new)

open(PATH, "w", encoding="utf-8", newline="").write(h)
print(f"APPLIED {len(EDITS)} edits")

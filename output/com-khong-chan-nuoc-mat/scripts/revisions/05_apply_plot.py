"""Apply Doctrine §9 (plot engine: plants, two-way misunderstanding, caused cold water, Prediction Ledger) to tap-1.html.
Scene-scoped, asserted edits. Backup is created once."""
import os
import re
import shutil

PATH = r"d:\Project\Sven\output\com-khong-chan-nuoc-mat\tap-1.html"
BACKUP = r"C:\Users\adminb\.gemini\antigravity-ide\brain\675ad7a4-b5b9-44e1-8352-f5e3fb2587ea\scratch\tap-1.before-plot.html"
if not os.path.exists(BACKUP):
    shutil.copyfile(PATH, BACKUP)
h = open(PATH, encoding="utf-8", newline="").read()

starts = [m.start() for m in re.finditer(r'<div class="scene-card" id="s-\d+">', h)]
end_main = h.find('<div id="toast"', starts[-1])
assert end_main > 0 and len(starts) == 10
bounds = starts + [end_main]
head, tail = h[:starts[0]], h[end_main:]
blocks = {f"{i+1:02d}": h[bounds[i]:bounds[i + 1]] for i in range(10)}


def rep(b, old, new, count=1, label=""):
    n = b.count(old)
    assert n == count, f"COUNT {n} != {count} [{label}]: {old[:90]}"
    return b.replace(old, new)


# ================= s01 — irony plant: the audience sees the IV tape first =================
b = blocks["01"]
b = rep(b, "Slender pale trembling fingers lose grip, sending",
        "Slender pale trembling fingers — white medical tape over a purple needle bruise on the thin wrist — lose grip, sending",
        label="s01 tier1")
b = rep(b, "Slender pale trembling fingers lose grip on the white porcelain spoon,",
        "Slender pale trembling fingers, white medical tape over a purple needle bruise on the thin wrist, lose grip on the white porcelain spoon,",
        label="s01 prompt")
b = rep(b, "beginning with slender trembling fingers visible in foreground lower-frame,",
        "beginning with slender trembling fingers visible in foreground lower-frame, white medical tape over a needle bruise on the wrist,",
        label="s01 subject")
blocks["01"] = b

# ================= s02 — misdirect: Má Ba's glance snags on the tape and reads as contempt =================
b = blocks["02"]
b = rep(b, "eyes dropping onto the couple on the floor.",
        "eyes dropping onto the couple on the floor and snagging for a heartbeat on Duyên's taped wrist as it slides out of sight behind Khang's knee — a flicker crosses her face, then her brow hardens.",
        label="s02 tier1")
b = rep(b, "eyes dropping down onto the couple on the floor:",
        "eyes dropping down onto the couple on the floor, where my_duyen's taped wrist slides out of sight behind minh_khang's knee; ma_ba's gaze snags on the wrist for a heartbeat, a flicker crossing the weathered face before the brow hardens:",
        label="s02 prompt")
b = rep(b, "sitting on floor tiles beside the pine crib, clutching the crib rail, weeping silently — the only my_duyen in frame.",
        "sitting on floor tiles beside the pine crib, clutching the crib rail, weeping silently, sliding the taped wrist out of sight — the only my_duyen in frame.",
        label="s02 subject")
blocks["02"] = b

# ================= s03 — second plant: Má Ba's own old needle scar =================
b = blocks["03"]
b = rep(b, "One weathered palm stays flat on the worn frame while her other hand points",
        "One weathered palm stays flat on the worn frame, an old faded needle scar pale on the inside of that wrist, while her other hand points",
        label="s03 tier1")
b = rep(b, "one weathered palm staying flat on the worn frame while the other hand points",
        "one weathered palm staying flat on the worn frame, an old faded needle scar pale on the inside of that wrist, while the other hand points",
        label="s03 prompt")
b = rep(b, "pointing agitated weathered finger toward pine crib — the only ma_ba in frame.",
        "pointing agitated weathered finger toward pine crib, an old faded needle scar on the inside of one wrist — the only ma_ba in frame.",
        label="s03 subject")
blocks["03"] = b

# ================= s05 — payoff: two wrists side by side; she already knew =================
b = blocks["05"]
b = rep(b, "Má Ba's weathered hand trembles into frame as her rough fingers lightly brush the bruised wrist. Her eyes widen in overwhelming maternal shock; tears instantly flood her wrinkled cheeks as memories of her own childbirth 30 years ago resurface.",
        "Má Ba's weathered hand trembles into frame beside the bruised wrist — two wrists side by side, her own old faded needle scar next to Duyên's fresh bruise — and her rough fingers lightly brush it. Her eyes do not widen in surprise; they close for a beat, as if at something already known, and tears flood her wrinkled cheeks as her own childbirth 30 years ago resurfaces.",
        label="s05 tier1")
b = rep(b, "ma_ba's weathered fingers rise trembling into frame and lightly brush the bruised wrist; ma_ba's eyes widen in overwhelming maternal shock as tears flood the wrinkled cheeks:",
        "ma_ba's weathered hand rises trembling into frame beside the bruised wrist, the old faded needle scar on the inside of ma_ba's own wrist lying right next to the fresh purple bruise, and the rough fingers lightly brush the bruise; ma_ba's eyes do not widen in surprise — the eyelids close for a beat, as if at something already known, and tears flood the wrinkled cheeks:",
        label="s05 prompt")
b = rep(b, "trembling fingers reaching for the bruised wrist,",
        "trembling fingers reaching for the bruised wrist, an old faded needle scar on the inside of ma_ba's own wrist,",
        label="s05 subject")
b = rep(b, "cutting to a reverse close-up of dawning remorse across ten seconds.",
        "cutting to a reverse close-up of recognition across ten seconds.", label="s05 style")
blocks["05"] = b

# ================= s08 — plant the cold water: Dì Tám waiting at the gate below =================
b = blocks["08"]
b = rep(b, "hanging the green mesh bed and giving it a gentle test sway.",
        "hanging the green mesh bed and giving it a gentle test sway. Beyond the railing, small and far below, Dì Tám stands at the iron courtyard gate peering up, an amber bottle glinting in her hand.",
        label="s08 tier1 a")
b = rep(b, "The frame holds on her amused face while potted palms sway",
        "The frame holds on her amused face; her gaze flicks once past the railing toward the gate below and the smile tightens for a beat before easing again, while potted palms sway",
        label="s08 tier1 b")
b = rep(b, "Second-floor balcony overlooking lush green potted tropical plants and river breeze,",
        "Second-floor balcony overlooking lush green potted tropical plants and river breeze, an iron courtyard gate visible far below beyond the railing,",
        label="s08 context")
b = rep(b, "chuckling with affectionate joy — the only ma_ba in frame.",
        "chuckling with affectionate joy — the only ma_ba in frame.\r\n"
        "di_tam [Appearance, attire, and facial features Refer to image 8], small and far below in the background at the iron courtyard gate, peering up at the veranda with an amber bottle of herbal ginger wine in one hand — the only di_tam in frame.",
        label="s08 subject")
b = rep(b, "green canvas mesh hammock hung securely; potted green plants on balcony — the only vong_xep in frame.",
        "green canvas mesh hammock hung securely; potted green plants on balcony; amber bottle of herbal ginger wine in di_tam's hand far below — the only vong_xep in frame.",
        label="s08 prop")
b = rep(b, "gives a gentle test sway, and glances back toward the doorway:",
        "gives a gentle test sway, and glances back toward the doorway; beyond the railing, small and far below in the background, di_tam stands at the iron courtyard gate peering up at the veranda, an amber bottle glinting in one hand:",
        label="s08 prompt a")
b = rep(b, "The frame holds on ma_ba's amused face while potted palms sway",
        "The frame holds on ma_ba's amused face; ma_ba's gaze flicks once past the railing toward the courtyard gate below and the smile tightens for a beat before easing again, while potted palms sway",
        label="s08 prompt b")
b = rep(b, "Active Characters: minh_khang, ma_ba\r\n", "Active Characters: minh_khang, ma_ba, di_tam\r\n", label="s08 ho active")
b = rep(b, "  - ma_ba: Walking back into the master bedroom toward the kitchen tray.\r\n",
        "  - ma_ba: Walking back into the master bedroom toward the kitchen tray.\r\n"
        "  - di_tam: Waiting at the iron courtyard gate below, amber bottle of ginger wine in hand, peering up at the veranda.\r\n",
        label="s08 ho state")
blocks["08"] = b

# ================= STORY SPINE — plot rows (Doctrine §9.9) =================
head = rep(head, "<!-- ==================== STORY SPINE (Creative Doctrine §8.10) ==================== -->",
           "<!-- ==================== STORY SPINE (Creative Doctrine §8.10 + §9.9) ==================== -->", label="spine comment")
head = rep(head, "5 IV tape and needle bruises hidden with the other hand ·",
           "5 IV tape and needle bruises hidden with the other hand — and the faded scar of the same on Má Ba's wrist ·", label="spine specific")
head = rep(head, "L4 Why is Má Ba so hard? s03 (palm on the frame, \"ba bây\") → s05",
           "L4 Why is Má Ba so hard? s02 (the glance at the tape), s03 (palm on the frame, the old scar) → s05", label="spine L4")
head = rep(head, "L6 Ginger wine vs. crib: s10 → Episode 2.",
           "L6 Ginger wine vs. crib: s08 (Dì Tám waiting at the gate) → s10, then Episode 2.", label="spine L6")
ROWS = (
    '<tr><td class="tier1-label">[PREDICT]</td><td class="tier1-val">'
    'P1 s01 | viewer predicts the mother-in-law will storm in and make it worse | → KEPT · '
    'P2 s02 | viewer predicts Má Ba never noticed the IV and her hardness is contempt | → BROKEN s05 | plant s01, s02, s03 · '
    'P3 s03 | viewer predicts Khang will fight his mother over the hammock | → BROKEN s03 | plant s01 · '
    'P4 s05 | viewer predicts Má Ba will apologize (A) or defend herself (B) | → BROKEN s05 | plant s03 — Option C: she confesses her own hidden collapse · '
    'P5 s09 | viewer predicts a closing line about no more tears (the title) | → BROKEN s09 | plant s06 · '
    'P6 s10 | viewer predicts the ginger-wine neighbor pulls Má Ba back to the old ways | → BROKEN s10 | plant s03, s07, s08 · '
    'P7 s10 | viewer predicts Bé Tin stays safe | → KEPT</td></tr>\r\n'
    '<tr><td class="tier1-label">[KNOW]</td><td class="tier1-val">'
    'From s01 the viewer knows about the IV tape and believes Má Ba does not (irony: we dread her mocking it). '
    'In s02 her gaze snags on the taped wrist and hardens — the camera withholds why, so it reads as contempt. '
    'In s03 her own old scar is on screen, unexplained (camouflaged inside the hammock fight). '
    'In s05 the mode flips: she knew, because she once hid the same thing — irony becomes recognition. '
    'In s08 only Má Ba and the viewer see Dì Tám at the gate (suspense for s10).</td></tr>\r\n'
    '<tr><td class="tier1-label">[MISREAD]</td><td class="tier1-val">'
    'Two-way. Duyên reads Má Ba\'s hardness as contempt for a "vụng" daughter-in-law; Má Ba reads Duyên\'s silence and the crib as a rejection of her ways. '
    'Blocked by Duyên\'s Lie ("a good daughter-in-law never complains") and Má Ba\'s denial (naming the tape means naming her own past). '
    'Each clarifying sentence costs a wound. Ends on screen in s05 by Má Ba\'s own choice to confess.</td></tr>\r\n'
    '<tr><td class="tier1-label">[TWIST]</td><td class="tier1-val">'
    'Major: s05 — TW-04 Perspective + TW-16 Secret Connection (the same hidden wound, thirty years apart); plants: s01 tape, s02 glance, s03 scar. · '
    'Minor: s10 — TW-12 Status Inversion (the former opponent defends the crib with Khang\'s own words). · '
    'Cold water: s10, caused by Dì Tám planted at the gate in s08; family-drama scale (a neighbor and a bottle).</td></tr>\r\n'
)
anchor = '<tr><td class="tier1-label">[COST]</td>'
head = rep(head, anchor, ROWS + anchor, label="spine rows")

new = head + "".join(blocks[k] for k in sorted(blocks)) + tail
open(PATH, "w", encoding="utf-8", newline="").write(new)
print("APPLIED OK; backup ->", BACKUP)

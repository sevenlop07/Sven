"""Apply Doctrine §8 (Story Spine + depth rewrites) to tap-1.html. Scene-scoped, asserted edits."""
import os
import re
import shutil

PATH = r"d:\Project\Sven\output\com-khong-chan-nuoc-mat\tap-1.html"
BACKUP = r"C:\Users\adminb\.gemini\antigravity-ide\brain\675ad7a4-b5b9-44e1-8352-f5e3fb2587ea\scratch\tap-1.before-story.html"
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


def rx(b, pattern, new, count=1, label=""):
    nb, n = re.subn(pattern, lambda m: new, b, flags=re.S)
    assert n == count, f"REGEX {n} != {count} [{label}]: {pattern[:90]}"
    return nb


def line(b, old, new, paren_prompt, paren_tier1, label):
    """Replace a spoken line in card + vn-dub + Tier 1 + prompt, and its two parentheticals."""
    b = rep(b, old, new, 4, label)
    b = rx(b, r'“ ' + re.escape(new) + r' ” \([^)]*\)', f'“ {new} ” ({paren_prompt})', 1, label + " prompt paren")
    b = rx(b, r'“' + re.escape(new) + r'” \([^)]*\)', f'“{new}” ({paren_tier1})', 1, label + " tier1 paren")
    return b


def subtext_after(b, quote, new_sub, label):
    pat = r'(<span class="dia-spoken-quote">"' + re.escape(quote) + r'"</span>\r?\n<div class="dia-vn-dub">[^\n]*\n<div class="dia-subtext">)\([^<]*\)(</div>)'
    nb, n = re.subn(pat, lambda m: m.group(1) + f"({new_sub})" + m.group(2), b)
    assert n == 1, f"SUBTEXT {n} [{label}]"
    return nb


def pill(b, new):
    return rx(b, r'(💬 Thoại: )[^<]*(</span>)', None, 1, "pill") if False else re.sub(
        r'(💬 Thoại: )[^<]*(</span>)', lambda m: m.group(1) + new + m.group(2), b, count=1)


def audit(b, new):
    return rx(b, r'Dialogue Audit: [^\r\n]*', 'Dialogue Audit: ' + new, 1, "audit")


V_MABA = "Voice of a 56-year-old Southwestern Vietnamese mother"
V_MABA_T = "Voice of a 56-year-old Southwestern Vietnamese woman"

# ================= SCENE 03 — claim by memory, refusal that honors it =================
b = blocks["03"]
b = line(b, "Xưa giờ cả họ nằm võng! Nôi gỗ lạnh ngắt vầy sao ngủ?!",
         "Cái võng này ba bây đưa bây ngủ từ hồi đỏ hỏn đó!",
         f"{V_MABA}; lips parting in proud unhurried Southern Vietnamese lip-sync, chin lifted, staking a claim on family history",
         f"{V_MABA_T}; proud unhurried Southern lip-sync, chin lifted, staking a claim on family history", "s03 ma_ba")
b = line(b, "Bác sĩ dặn nằm nôi phẳng cho thẳng lưng má.",
         "Con nhớ võng của ba... mà thằng Tin phải nằm nôi.",
         "Voice of a 27-year-old Southern Vietnamese man; lips parting in soft careful Southern Vietnamese lip-sync, eyes lowered, a refusal wrapped in tenderness",
         "Voice of a 27-year-old Southern Vietnamese man; soft careful Southern lip-sync, eyes lowered, a refusal wrapped in tenderness", "s03 khang")
b = rep(b, "ma_ba sets the folded steel hammock stand onto floor tiles with a loud metallic clank, pointing an agitated weathered finger toward the pine crib:",
        "ma_ba sets the folded steel hammock stand onto floor tiles with a loud metallic clank, one weathered palm staying flat on the worn frame while the other hand points toward the pine crib:")
b = rep(b, "Má Ba steps forward, pointing an agitated weathered finger directly toward the modern pine crib.",
        "One weathered palm stays flat on the worn frame while her other hand points toward the modern pine crib.")
b = rep(b, "Minh Khang [00:25.0 – 00:27.5]", "Minh Khang [00:25.0 – 00:27.7]")
b = subtext_after(b, "Cái võng này ba bây đưa bây ngủ từ hồi đỏ hỏn đó!",
                  "Một bàn tay vẫn đặt trên khung võng cũ của người chồng đã khuất — đòi lại chỗ đứng bằng ký ức, không bằng lý lẽ", "s03 ma_ba sub")
b = subtext_after(b, "Con nhớ võng của ba... mà thằng Tin phải nằm nôi.",
                  "Nắm bàn tay đang chỉ của mẹ, nhận lấy ký ức về ba trước rồi mới từ chối thật khẽ", "s03 khang sub")
b = pill(b, "Call-and-Response Móc Nối (Má Ba 13 từ • Khang 11 từ)")
b = audit(b, "ma_ba 13 words, minh_khang 11 words (24 words, ~5.9s of speech).")
blocks["03"] = b

# ================= SCENE 05 — silent reveal, Má Ba recognizes her younger self =================
b = blocks["05"]
KH05 = "Má coi nè... tay Duyên truyền dịch mấy bữa, sợ má buồn hổng dám than!"
b = rx(b, r'<div class="dia-item">\r?\n<span class="dia-speaker">Minh Khang \[00:40\.8 – 00:44\.4\]: </span>.*?<div class="dia-subtext">[^<]*</div>\r?\n</div>\r?\n', "", 1, "drop khang card")
b = rx(b, r'Khang weeps openly, gazing up at his mother\.<br/>Minh Khang: “' + re.escape(KH05) + r'” \([^)]*\)',
       "Mỹ Duyên's free hand fumbles weakly to cover the bruises; Khang gently moves it aside and holds the arm up, weeping, lips pressed shut — no words.", 1, "tier1 khang")
b = rx(b, r'tears running down minh_khang\'s face while looking up at ma_ba:\r?\nminh_khang: “ ' + re.escape(KH05) + r' ” \([^)]*\)',
       "tears running down minh_khang's face, lips pressed shut — no words.", 1, "prompt khang")
b = rep(b, "a medium close-up on minh_khang kneeling with my_duyen slumped against minh_khang's chest: minh_khang lifts my_duyen's limp arm up toward ma_ba and toward the lens, the dark purple needle bruises and peeling medical tape on the slender wrist sharp in the foreground,",
        "a medium close-up on minh_khang kneeling with my_duyen slumped against minh_khang's chest: my_duyen's free hand fumbles weakly to cover the dark purple needle bruises and peeling medical tape on the slender wrist; minh_khang gently moves that hand aside and lifts the arm up toward ma_ba and toward the lens, the bruises sharp in the foreground,")
b = rep(b, "pale face with faint fluttering eyelids — the only my_duyen in frame.",
        "pale face with faint fluttering eyelids, free hand weakly trying to cover the bruised wrist — the only my_duyen in frame.")
b = line(b, "Đau vậy... sao hổng nói má hay, con?",
         "Hồi đó má cũng giấu... giấu hoài tới ngất.",
         f"{V_MABA}; lips parting in choking low Southern Vietnamese lip-sync, gaze drifting into a thirty-year-old memory, a confession never spoken before",
         f"{V_MABA_T}; choking low Southern lip-sync, gaze drifting into a thirty-year-old memory, a confession never spoken before", "s05 ma_ba")
b = rep(b, "head bowing in profound repentance through 00:10.0.",
        "and bows over the hand as if over a younger self through 00:10.0.")
b = rep(b, "bowing her head in profound repentance.",
        "bowing over the hand as if over her own younger hand.")
b = rep(b, "Má Ba [00:45.3 – 00:47.4]", "Má Ba [00:45.3 – 00:47.6]")
b = subtext_after(b, "Hồi đó má cũng giấu... giấu hoài tới ngất.",
                  "Ngón tay run run chạm vết kim — thấy lại chính mình ba mươi năm trước; lần đầu tiên má nói ra bí mật đã giấu cả đời", "s05 sub")
b = pill(b, "Solo Thú Nhận (Má Ba 9 từ • Duyên cố che vết kim • Khang im lặng)")
b = audit(b, "ma_ba 9 words (solo confession, ~2.3s of speech); my_duyen tries to hide the IV bruises, minh_khang answers with his hands.")
blocks["05"] = b

# ================= SCENE 06 — Duyên confesses the secret lullaby practice =================
b = blocks["06"]
b = line(b, "Con cứ tưởng... má ghét con lắm.",
         "Con lén tập ầu ơ hoài... mà hổng giống giọng má.",
         "Voice of a 24-year-old Southern Vietnamese woman; lips parting in small cracked Southern Vietnamese lip-sync, a shy confession with half a laugh through the tears",
         "Voice of a 24-year-old Southern Vietnamese woman; small cracked Southern lip-sync, a shy confession with half a laugh through the tears", "s06 duyen")
b = rep(b, "Mỹ Duyên [00:54.8 – 00:56.7]", "Mỹ Duyên [00:54.8 – 00:57.5]")
b = subtext_after(b, "Con lén tập ầu ơ hoài... mà hổng giống giọng má.",
                  "Tựa má vào vai mẹ chồng, thú nhận đã lén tập câu ầu ơ cho giống má — nửa khóc nửa cười", "s06 sub")
b = pill(b, "Call-and-Response Móc Nối (Má Ba 13 từ • Duyên 11 từ)")
b = audit(b, "ma_ba 13 words, my_duyen 11 words (24 words, ~5.9s of speech).")
blocks["06"] = b

# ================= SCENE 09 — a request that gives Má Ba a new place; title kept by image =================
b = blocks["09"]
b = line(b, "Ngọt quá má... Từ nay cơm nhà mình hổng còn chan nước mắt nữa.",
         "Ngọt quá má... mai má dạy con ầu ơ nghen.",
         "Voice of a 24-year-old Southern Vietnamese woman; lips parting in soft shy Southern Vietnamese lip-sync, a request that hands ma_ba a new place in the family",
         "Voice of a 24-year-old Southern Vietnamese woman; soft shy Southern lip-sync, a request that hands Má Ba a new place in the family", "s09 duyen")
b = rep(b, "my_duyen swallows the warm soup, a radiant smile breaking through glistening tears, clasps ma_ba's wrist with overwhelming filial gratitude:",
        "my_duyen swallows the warm soup, eyes glistening yet not a single tear falling into the steaming bowl, and clasps ma_ba's wrist with overwhelming filial gratitude:")
b = rep(b, "Mỹ Duyên swallows the warm soup, a radiant smile breaking through glistening tears.",
        "Mỹ Duyên swallows the warm soup — eyes glistening, yet not a single tear falls into the steaming bowl.")
b = rep(b, "The frame stays at rest on the tableau: ma_ba feeds",
        "The frame stays at rest on the tableau: the spoon pauses in ma_ba's hand, weathered eyes brimming as ma_ba nods, then ma_ba feeds")
b = rep(b, "The frame stays at rest on the tableau: Má Ba feeds",
        "The frame stays at rest on the tableau: the spoon pauses in Má Ba's hand, her eyes brimming as she nods, then she feeds")
b = rep(b, "Mỹ Duyên [01:26.0 – 01:29.0]", "Mỹ Duyên [01:26.0 – 01:28.5]")
b = subtext_after(b, "Ngọt quá má... mai má dạy con ầu ơ nghen.",
                  "Nuốt muỗng canh bồ ngót nóng — không còn giọt nước mắt nào rơi vào bát; xin má dạy ầu ơ, trao lại cho má một chỗ đứng mới", "s09 sub")
b = pill(b, "Solo Lời Xin (Duyên 10 từ • Má Ba đáp bằng cái gật đầu và muỗng canh kế tiếp)")
b = audit(b, "my_duyen 10 words (solo request, ~2.5s of speech); ma_ba answers with a nod and the next spoonful.")
blocks["09"] = b

# ================= SCENE 10 — the former opponent repeats Khang's words =================
b = blocks["10"]
b = rep(b, "Bậy hén bà Tám! Da non vầy xức cay sao nổi? Nằm nôi!", "Bậy hén bà Tám! Thằng Tin phải nằm nôi!", 4, "s10 ma_ba")
b = rep(b, "Má Ba [01:34.8 – 01:38.0]", "Má Ba [01:34.8 – 01:37.1]")
b = subtext_after(b, "Bậy hén bà Tám! Thằng Tin phải nằm nôi!",
                  "Bật dậy dang tay chắn trước nôi — nói lại đúng câu của con trai lúc sáng, giờ là lời của chính má", "s10 sub")
b = pill(b, "Call-and-Response Móc Nối (Dì Tám 11 từ • Má Ba 9 từ)")
b = audit(b, "di_tam 11 words, ma_ba 9 words (20 words, ~5.0s of speech).")
blocks["10"] = b

# ================= STORY SPINE CARD (Doctrine §8.10) =================
SPINE = """<!-- ==================== STORY SPINE (Creative Doctrine §8.10) ==================== -->
<div class="spine-card" id="story-spine">
<div class="spine-title">📜 STORY SPINE — Tập 1: Bát Cháo Ở Cữ Chan Nước Mắt</div>
<table class="tier1-table">
<tr><td class="tier1-label">[QUESTION]</td><td class="tier1-val"><strong>Dramatic:</strong> Will Duyên admit how much she is hurting before her body admits it for her?<br/><strong>Thematic:</strong> Is love that refuses to listen still love? — <em>Side A (Má Ba):</em> the old ways carried this family through hard years; being present is love. <em>Side B (Duyên / Khang):</em> a newborn's spine and a mother's body need listening, not rules.</td></tr>
<tr><td class="tier1-label">[TRUTH]</td><td class="tier1-val"><strong>Má Ba</strong> — Wound: thirty years ago hid her own postpartum collapse from her mother-in-law; widowed early, raised Khang in the hammock his father hung → Lie: "being needed means being obeyed" → Want: keep the grandson in the family hammock → Need: be needed by listening → Fear: becoming a guest in her son's house | Paradox: the loudest voice in the room is the one most afraid of being left.<br/><strong>Mỹ Duyên</strong> — Wound: judged "vụng" from her first day as a daughter-in-law → Lie: "a good daughter-in-law never complains" → Want: keep the peace, hide the IV drip → Need: let the pain be seen → Fear: being the reason the family breaks | Paradox: hides the pain to protect the very bond the hiding is breaking.<br/><strong>Minh Khang</strong> — Wound: grew up as his widowed mother's only support → Lie: "if I am gentle enough, nobody gets hurt" → Want: protect wife and son without wounding his mother → Need: choose clearly and say it → Fear: becoming the son who turned his mother away | Paradox: his gentleness delays the collapse it is meant to prevent.</td></tr>
<tr><td class="tier1-label">[SPECIFIC]</td><td class="tier1-val">1 cold congee with a congealed skin · 2 a 0 ml pump bottle · 3 three nights without sleep · ★4 the folding hammock Khang's late father rocked him in · 5 IV tape and needle bruises hidden with the other hand · 6 Má Ba's brown silk áo bà ba folded into the crib so the baby sleeps in her scent · 7 the "ầu ơ" lullaby Duyên practices in secret · 8 katuk soup with minced pork (canh bồ ngót) for milk · 9 Dì Tám's ginger wine rubbed on newborns "to warm the bones" · 10 the belief that a crib "chills the baby's back" (nằm nôi lạnh lưng).</td></tr>
<tr><td class="tier1-label">[CLICHÉ]</td><td class="tier1-val">Villain mother-in-law → <strong>Subverted</strong>: her insistence grows from her own hidden collapse. · Husband fights his mother → <strong>Refused</strong>: Khang honors the memory, refuses in one line, then gives the hammock a new place. · Reconciliation by speech → <strong>Subverted</strong>: by recognition ("Hồi đó má cũng giấu…") and a scent in the crib. · Final line states the moral / title → <strong>Refused</strong>: Duyên asks to learn the lullaby; the title is kept by the image. · Cliffhanger = new villain → <strong>Kept, recast</strong>: the former opponent defends the crib with Khang's own words.</td></tr>
<tr><td class="tier1-label">[LOOPS]</td><td class="tier1-val">L1 Will help (and milk) come for Duyên? s01 → s09 · L2 Hammock or crib? s02–s03 → s07 (silk in the crib), s08 (hammock on the veranda) · L3 What is Duyên hiding? s01, s04 → s05 · L4 Why is Má Ba so hard? s03 (palm on the frame, "ba bây") → s05 · L5 Can Duyên ever sing like Má Ba? s06 → s07, s09 · L6 Ginger wine vs. crib: s10 → Episode 2.</td></tr>
<tr><td class="tier1-label">[COST]</td><td class="tier1-val">Má Ba gives up the hammock's place beside the crib and her authority as "the one who knows"; Duyên gives up the mask of never complaining.</td></tr>
<tr><td class="tier1-label">[DEBATE]</td><td class="tier1-val">Should Duyên have hidden her pain to keep the peace — and who was right about the hammock?</td></tr>
<tr><td class="tier1-label">[IMAGE]</td><td class="tier1-val">Open: a tear breaks the cold skin of congee beside an empty bottle. Close: a hot spoonful of katuk soup, eyes glistening, not one tear falls into the bowl — Má Ba's silk asleep in the crib.</td></tr>
</table>
</div>
"""
SPINE = SPINE.replace("\n", "\r\n")
CSS = (".spine-card { background: linear-gradient(135deg, rgba(251,191,36,0.07), rgba(56,189,248,0.05)); border: 1px solid rgba(251,191,36,0.35); "
       "border-radius: 14px; padding: 18px 20px; margin: 0 0 24px; box-shadow: 0 8px 30px rgba(0,0,0,0.25); }\r\n"
       ".spine-title { font-weight: 800; letter-spacing: 0.04em; color: var(--gold); margin-bottom: 10px; font-size: 14px; }\r\n")
assert head.count("<!-- Master Batch Toolbar -->") == 1 and 'id="story-spine"' not in head
head = head.replace("<!-- Master Batch Toolbar -->", SPINE + "<!-- Master Batch Toolbar -->")
assert head.count("</style>") >= 1
head = head.replace("</style>", CSS + "</style>", 1)

new = head + "".join(blocks[k] for k in sorted(blocks)) + tail
open(PATH, "w", encoding="utf-8", newline="").write(new)
for o in ["Xưa giờ cả họ", "Bác sĩ dặn", "sợ má buồn", "má ghét con", "chan nước mắt nữa", "Da non vầy"]:
    for m in re.finditer(re.escape(o), new):
        print(f"RESIDUAL '{o}' at line {new[:m.start()].count(chr(10)) + 1}")
print("APPLIED OK; backup ->", BACKUP)

"""Apply the Screenwriter dialogue rebalance to tap-1.html (scene-scoped, asserted replacements)."""
import re

PATH = r"d:\Project\Sven\output\com-khong-chan-nuoc-mat\tap-1.html"
h = open(PATH, encoding="utf-8", newline="").read()
NL = "\r\n" if "\r\n" in h else "\n"

# ---- split into scene blocks ----
starts = [m.start() for m in re.finditer(r'<div class="scene-card" id="s-\d+">', h)]
end_main = h.find('<div id="toast">', starts[-1])
assert end_main > 0
bounds = starts + [end_main]
head, tail = h[:starts[0]], h[end_main:]
blocks = {f"{i+1:02d}": h[bounds[i]:bounds[i + 1]] for i in range(len(starts))}
assert len(blocks) == 10


def rep(b, old, new, count=None, label=""):
    n = b.count(old)
    assert n > 0, f"NOT FOUND [{label}]: {old[:80]}"
    if count is not None:
        assert n == count, f"COUNT {n} != {count} [{label}]: {old[:80]}"
    return b.replace(old, new)


def rx(b, pattern, new, count=1, label=""):
    nb, n = re.subn(pattern, new, b, flags=re.S)
    assert n == count, f"REGEX {n} != {count} [{label}]: {pattern[:80]}"
    return nb


def quote(b, old, new, label):
    # card spoken quote + vn-dub + Tier 1 + prompt = 4 occurrences
    return rep(b, old, new, 4, label)


def stamp(b, name, old, new):
    return rep(b, f'{name} [{old}]', f'{name} [{new}]', 1, f"stamp {name}")


def pill(b, new):
    return rx(b, r'(💬 Thoại: )[^<]*(</span>)', r'\g<1>' + new + r'\g<2>', 1, "pill")


def audit(b, new):
    return rx(b, r'Dialogue Audit: [^\r\n]*', 'Dialogue Audit: ' + new, 1, "audit")


def split(b, old, new):
    b = rep(b, f'[00:00–00:{old}]', f'[00:00–00:{new}]', 1, "split1")
    b = rep(b, f'[00:{old}–00:10.0]', f'[00:{new}–00:10.0]', 1, "split2")
    return b


def drop_item(b, speaker_stamp):
    pat = (r'<div class="dia-item">\r?\n<span class="dia-speaker">' + re.escape(speaker_stamp)
           + r'.*?<div class="dia-subtext">.*?</div>\r?\n</div>\r?\n')
    return rx(b, pat, '', 1, f"drop {speaker_stamp}")


def drop_tier1(b, name, q, replacement):
    pat = r'<br/>' + re.escape(name) + r': “' + re.escape(q) + r'” \([^)]*\)'
    return rx(b, pat, replacement, 1, f"tier1 {name}")


def drop_prompt(b, lead_old, lead_new, pid, q):
    pat = re.escape(lead_old) + r'\r?\n' + re.escape(pid) + r': “ ' + re.escape(q) + r' ” \([^)]*\)'
    return rx(b, pat, lead_new, 1, f"prompt {pid}")


# ================= SCENE 01 — solo (Duyên) =================
b = blocks["01"]
b = quote(b, "Em mệt quá anh ơi... Em kiệt sức rồi, sữa hổng có về...",
          "Anh ơi... em kiệt sức rồi, sữa hổng chịu về...", "s01 duyen")
b = rep(b, "(12 từ)</div>", "(10 từ)</div>", 1)
b = stamp(b, "Mỹ Duyên", "00:03.5 – 00:07.0", "00:03.8 – 00:06.3")
b = drop_item(b, "Minh Khang [00:07.5 – 00:09.5]")
b = rep(b, "Minh Khang Urgent Comfort &amp; Organic Settle", "Minh Khang Wordless Comfort &amp; Organic Settle", 1)
b = drop_tier1(b, "Minh Khang", "Có anh đây... Vợ đừng sợ!", "")
b = rep(b, "leaning his forehead gently to their joined hands:",
        "leaning his forehead gently to their joined hands — no words, only the steady grip.", 1)
b = drop_prompt(b, "eyes locked onto my_duyen with unwavering devotion:",
                "eyes locked onto my_duyen with unwavering devotion, lips pressed together in silence — the grip says what words cannot.",
                "minh_khang", "Có anh đây... Vợ đừng sợ!")
b = pill(b, "Solo Một Lời Than (Duyên 10 từ • Khang im lặng, đáp bằng cái siết tay)")
b = audit(b, "my_duyen 10 words (solo, ~2.5s of speech); minh_khang answers wordlessly with the grip.")
blocks["01"] = b

# ================= SCENE 02 — dialogue =================
b = blocks["02"]
b = quote(b, "Trời đất ơi! Thằng Tin khóc thấu trời, dâu ơi... tính nuôi cháu tao kiểu Tây hả con?!",
          "Trời đất! Thằng Tin khóc thấu trời... nuôi cháu tao kiểu Tây hả?!", "s02 ma_ba")
b = quote(b, "Má ơi nhỏ tiếng giùm con... Duyên kiệt sức ba đêm rồi, má thương vợ con chút đi!",
          "Má nhỏ tiếng giùm con... Duyên kiệt sức ba đêm rồi!", "s02 khang")
b = stamp(b, "Má Ba", "00:10.8 – 00:14.5", "00:10.8 – 00:14.0")
b = stamp(b, "Minh Khang", "00:15.0 – 00:19.4", "00:14.8 – 00:17.3")
b = pill(b, "Call-and-Response Móc Nối (Má Ba 13 từ • Khang 10 từ)")
b = audit(b, "ma_ba 13 words, minh_khang 10 words (23 words, ~5.7s of speech; each line fits its shot).")
blocks["02"] = b

# ================= SCENE 03 — dialogue, split 5.0 =================
b = blocks["03"]
b = quote(b, "Xưa giờ cả họ nằm võng! Nôi gỗ lạnh ngắt vầy, sao thằng nhỏ ngủ yên hả Duyên?!",
          "Xưa giờ cả họ nằm võng! Nôi gỗ lạnh ngắt vầy sao ngủ?!", "s03 ma_ba")
b = quote(b, "Dạ má... Bác sĩ dặn nằm nôi phẳng cho thẳng lưng má ơi!",
          "Bác sĩ dặn nằm nôi phẳng cho thẳng lưng má.", "s03 khang")
b = split(b, "04.5", "05.0")
b = stamp(b, "Má Ba", "00:20.8 – 00:24.6", "00:20.8 – 00:24.0")
b = stamp(b, "Minh Khang", "00:25.2 – 00:29.2", "00:25.3 – 00:27.8")
b = pill(b, "Call-and-Response Móc Nối (Má Ba 13 từ • Khang 10 từ)")
b = audit(b, "ma_ba 13 words, minh_khang 10 words (23 words, ~5.7s of speech).")
blocks["03"] = b

# ================= SCENE 04 — solo (Má Ba), split 4.0 =================
b = blocks["04"]
b = quote(b, "Trời đất ơi Duyên! Con Duyên làm sao vậy con?! Khang ơi đỡ vợ mầy mau!",
          "Duyên! Duyên ơi, con sao vậy con?! Khang, đỡ vợ mầy mau!", "s04 ma_ba")
b = drop_item(b, "Mỹ Duyên [00:30.8 – 00:33.5]")
b = drop_tier1(b, "Mỹ Duyên", "Má ơi... con chóng mặt quá... con xin lỗi má...",
               "<br/>Her lips part, but no apology comes — only a thin, shaking exhale.")
b = drop_prompt(b, "sliding down the balusters toward floor tiles:",
                "sliding down the balusters toward floor tiles. Pale lips part, but no words come — only a thin, shaking exhale as the head tilts limp with postpartum exhaustion.",
                "my_duyen", "Má ơi... con chóng mặt quá... con xin lỗi má...")
b = split(b, "04.5", "04.0")
b = stamp(b, "Má Ba", "00:34.2 – 00:39.0", "00:34.3 – 00:37.0")
b = pill(b, "Solo Bùng Nổ (Má Ba 12 từ • Duyên ngất lịm, không thốt nổi một lời)")
b = audit(b, "ma_ba 12 words (solo, ~3.0s of speech); my_duyen collapses without a word.")
blocks["04"] = b

# ================= SCENE 05 — dialogue (Track B, split 5.0 kept) =================
b = blocks["05"]
b = quote(b, "Má coi nè... Tay Duyên dán băng truyền dịch mấy bữa, sợ má buồn hổng dám than!",
          "Má coi nè... tay Duyên truyền dịch mấy bữa, sợ má buồn hổng dám than!", "s05 khang")
b = quote(b, "Tổ cha mầy... Đau sao cắn răng nhịn hả dâu?! Má đâu có ép con...",
          "Đau vậy... sao hổng nói má hay, con?", "s05 ma_ba")
b = stamp(b, "Minh Khang", "00:40.8 – 00:45.0", "00:40.8 – 00:44.4")
b = stamp(b, "Má Ba", "00:45.6 – 00:49.6", "00:45.3 – 00:47.4")
b = pill(b, "Call-and-Response Móc Nối (Khang 15 từ • Má Ba 8 từ)")
b = audit(b, "minh_khang 15 words, ma_ba 8 words (23 words, ~5.7s of speech).")
blocks["05"] = b

# ================= SCENE 06 — dialogue (split 4.5 kept) =================
b = blocks["06"]
b = quote(b, "Nín đi dâu... Má thương còn hổng hết! Có má lo, hổng ai dám nói dâu vụng về!",
          "Nín đi con... có má đây, hổng ai dám chê con vụng nữa.", "s06 ma_ba")
b = quote(b, "Dạ má... Con đội ơn má dữ lắm... Con cứ sợ má ghét bỏ con...",
          "Con cứ tưởng... má ghét con lắm.", "s06 duyen")
b = stamp(b, "Má Ba", "00:50.8 – 00:54.6", "00:50.8 – 00:54.0")
b = stamp(b, "Mỹ Duyên", "00:55.2 – 00:59.0", "00:54.8 – 00:56.7")
b = pill(b, "Call-and-Response Móc Nối (Má Ba 13 từ • Duyên 7 từ)")
b = audit(b, "ma_ba 13 words, my_duyen 7 words (20 words, ~5.0s of speech).")
blocks["06"] = b

# ================= SCENE 07 — solo lullaby (Má Ba), split 5.5 =================
b = blocks["07"]
b = quote(b, "Má lót cái áo cũ vô nôi... Có hơi bà nội, cháu ngủ ngoan như nằm võng nghen!",
          "Ầu ơ... có hơi bà nội đây, cháu ngủ ngoan như nằm võng nghen.", "s07 ma_ba")
b = drop_item(b, "Mỹ Duyên [01:05.2 – 01:09.2]")
b = drop_tier1(b, "Mỹ Duyên", "Dạ má... Nôi êm lưng ấm hơi bà nội, thằng Tin ngủ ngon lành rồi má ơi!",
               "<br/>No words — Mỹ Duyên presses trembling fingertips to her lips, a tearful smile answering in silence.")
b = drop_prompt(b, "eyes shining with tears of deep gratitude and domestic peace, lips parting in serene gratitude:",
                "eyes shining with tears of deep gratitude and domestic peace; no words — trembling fingertips rise to closed lips as a silent tearful smile spreads across my_duyen's face.",
                "my_duyen", "Dạ má... Nôi êm lưng ấm hơi bà nội, thằng Tin ngủ ngon lành rồi má ơi!")
b = split(b, "04.5", "05.5")
b = stamp(b, "Má Ba", "01:00.8 – 01:04.6", "01:00.8 – 01:04.2")
b = pill(b, "Solo Ru Cháu (Má Ba 14 từ • Duyên đáp bằng nụ cười lặng lẽ)")
b = audit(b, "ma_ba 14 words (solo lullaby, ~3.4s of speech); my_duyen answers with a silent smile.")
blocks["07"] = b

# ================= SCENE 08 — dialogue (split 4.5 kept) =================
b = blocks["08"]
b = quote(b, "Võng của má con mắc ban công nè. Trưa má ra đây ngả lưng đón gió nghen má!",
          "Võng má con mắc đây rồi, trưa ra hóng gió nghen má!", "s08 khang")
b = quote(b, "Tổ cha mầy, khéo nịnh ghê hôn! Vô săn sóc con Duyên đi, để đó tao coi cho!",
          "Tổ cha mầy, bày đặt nịnh! Vô với vợ mầy đi.", "s08 ma_ba")
b = stamp(b, "Minh Khang", "01:10.8 – 01:14.6", "01:10.8 – 01:13.8")
b = stamp(b, "Má Ba", "01:15.2 – 01:19.2", "01:14.8 – 01:17.6")
b = pill(b, "Call-and-Response Móc Nối (Khang 12 từ • Má Ba 11 từ)")
b = audit(b, "minh_khang 12 words, ma_ba 11 words (23 words, ~5.7s of speech).")
blocks["08"] = b

# ================= SCENE 09 — solo title line (Duyên), split 5.0 =================
b = blocks["09"]
b = quote(b, "Dạ má... Canh ngọt lịm... Từ nay cơm nhà mình hổng còn chan nước mắt nữa má ơi!",
          "Ngọt quá má... Từ nay cơm nhà mình hổng còn chan nước mắt nữa.", "s09 duyen")
b = drop_item(b, "Má Ba [01:20.8 – 01:24.6]")
b = drop_tier1(b, "Má Ba", "Húp muỗng canh bồ ngót nóng cho ấm dạ dâu ơi! Mau về sữa cho con bú nghen!",
               "<br/>No words — Má Ba simply holds the spoon to Duyên's lips and waits, the steam saying everything.")
b = drop_prompt(b, "settling on a frontal medium close-up of ma_ba tenderly offering the spoonful to my_duyen:",
                "settling on a frontal medium close-up of ma_ba tenderly offering the spoonful to my_duyen. No words: ma_ba simply holds the spoon steady at my_duyen's lips and waits, weathered eyes soft and wet, lips closed in a quiet smile.",
                "ma_ba", "Húp muỗng canh bồ ngót nóng cho ấm dạ dâu ơi! Mau về sữa cho con bú nghen!")
b = split(b, "04.5", "05.0")
b = stamp(b, "Mỹ Duyên", "01:25.2 – 01:29.0", "01:25.3 – 01:28.3")
b = rep(b, "(Nuốt muỗng canh ấm bụng,", "(Nuốt muỗng canh bồ ngót ấm bụng,", 1)
b = pill(b, "Solo Tựa Đề (Duyên 12 từ • Má Ba bón canh không lời)")
b = audit(b, "my_duyen 12 words (solo title line, ~3.0s of speech); ma_ba feeds wordlessly.")
blocks["09"] = b

# ================= SCENE 10 — dialogue (Track B, split 4.5 kept) =================
b = blocks["10"]
b = quote(b, "Bà Ba ơi! Lấy rượu gừng xức cho ấm cốt, nằm nôi làm chi?!",
          "Bà Ba! Xức rượu gừng cho ấm cốt, nằm nôi chi?!", "s10 di_tam")
b = quote(b, "Bậy bạ hén bà Tám! Da non xức cay nóng cháu tao hả? Cứ để nôi êm!",
          "Bậy hén bà Tám! Da non vầy xức cay sao nổi? Nằm nôi!", "s10 ma_ba")
b = stamp(b, "Dì Tám", "01:30.8 – 01:34.2", "01:30.8 – 01:33.5")
b = stamp(b, "Má Ba", "01:34.8 – 01:39.0", "01:34.8 – 01:38.0")
b = pill(b, "Call-and-Response Móc Nối (Dì Tám 11 từ • Má Ba 13 từ)")
b = audit(b, "di_tam 11 words, ma_ba 13 words (24 words, ~5.9s of speech).")
blocks["10"] = b

new = head + "".join(blocks[k] for k in sorted(blocks)) + tail
open(PATH, "w", encoding="utf-8", newline="").write(new)

# Residual check: old lines anywhere else in the file (e.g. summaries outside scene cards)
OLD = ["Em mệt quá anh ơi", "Có anh đây... Vợ đừng sợ", "dâu ơi... tính nuôi", "má thương vợ con chút",
       "ngủ yên hả Duyên", "con xin lỗi má", "Tổ cha mầy... Đau", "Má thương còn hổng hết", "đội ơn má",
       "Má lót cái áo cũ", "Nôi êm lưng ấm", "ngả lưng đón gió", "để đó tao coi", "Húp muỗng canh",
       "Canh ngọt lịm", "Lấy rượu gừng", "Cứ để nôi êm", "00:04.5–00:10.0"]
for o in OLD:
    for m in re.finditer(re.escape(o), new):
        ln = new[:m.start()].count("\n") + 1
        print(f"RESIDUAL '{o}' at line {ln}")
print("APPLIED OK")

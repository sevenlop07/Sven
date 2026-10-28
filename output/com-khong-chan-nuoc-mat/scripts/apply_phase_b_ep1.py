"""Phase B for Episode 1 (workflow.md §8.5) + 10-scene episode override (workflow.md §2.4) in setting.html.

- Updates the series header from 9 x 10s = 90s to 10 x 10s = 100s per episode.
- Extends the per-episode scene template grid with Scene 10 (caused cold water / hook).
- Syncs the Episode 1 row of the Section 5 table with the approved tap-1.html.
- Inserts a scene-level Phase B table for Episode 1: beat, cast/location/props, compact Intent Card,
  voice mode, lines (pulled verbatim from tap-1.html), kinetic bridge.
Backup is written once to the conversation scratch folder. Every replacement is asserted.
"""
import html as html_lib
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTING = os.path.join(ROOT, "setting.html")
TAP = os.path.join(ROOT, "tap-1.html")
BACKUP = r"C:\Users\adminb\.gemini\antigravity-ide\brain\675ad7a4-b5b9-44e1-8352-f5e3fb2587ea\scratch\setting.before-phaseb.html"
if not os.path.exists(BACKUP):
    shutil.copyfile(SETTING, BACKUP)

s = open(SETTING, encoding="utf-8", newline="").read()
t = open(TAP, encoding="utf-8", newline="").read()
assert 'id="ep1-phase-b"' not in s, "Phase B already applied"


def rep(text, old, new, count=1):
    n = text.count(old)
    assert n == count, f"COUNT {n} != {count}: {old[:90]}"
    return text.replace(old, new)


# ---------- 1. Header: 10 scenes x 10s = 100s per episode ----------
s = rep(s, "(Đúng 9 Cảnh x 10s = 90s / Tập - 180 Cảnh)", "(10 Cảnh x 10s = 100s / Tập - 200 Cảnh)")
s = rep(s, "Chuẩn: 9 Cảnh x 10s = 90s / Tập", "Chuẩn: 10 Cảnh x 10s = 100s / Tập")
s = rep(s, "20 Tập · 90 Giây / Tập (180 Cảnh x 10s)", "20 Tập · 100 Giây / Tập (200 Cảnh x 10s)")
s = rep(s, "BẮT BUỘC 10 Giây / Cảnh (9 Cảnh = 90s)", "BẮT BUỘC 10 Giây / Cảnh (10 Cảnh = 100s)")
s = rep(s, "(Đúng 9 Cảnh x 10s = 90s / Tập - Tổng 180 Cảnh)", "(10 Cảnh x 10s = 100s / Tập - Tổng 200 Cảnh)")
s = rep(s, "Hóa Giải Khoa Học &amp; Tình Cảm (60-90s)", "Hóa Giải Khoa Học &amp; Tình Cảm (60-100s)") if "&amp; Tình Cảm (60-90s)" in s \
    else rep(s, "Hóa Giải Khoa Học & Tình Cảm (60-90s)", "Hóa Giải Khoa Học & Tình Cảm (60-100s)")
s = rep(s, "/* 9 Scene Grid (10s each) */", "/* Scene Grid (10s each; 10 scenes per episode, project_rules.json episode_scenes) */")

# ---------- 2. Template grid: Scene 9 becomes the closing image, Scene 10 the caused cold water ----------
OLD9 = ("<h4>Warm Echo & Hook Tập Sau</h4>\r\n"
        "          <p>Mâm cơm ấm cúng, tiếng cười rộn rã của cả nhà và câu buông lời tếu táo gieo mầm tò mò cho tập kế tiếp.</p>\r\n"
        "        </div>\r\n")
NEW9 = ("<h4>Warm Echo &amp; Closing Image</h4>\r\n"
        "          <p>Hình ảnh khép lại trả lời hình ảnh mở đầu (không nhân vật nào nói ra bài học hay tên phim — Doctrine §8.8).</p>\r\n"
        "        </div>\r\n"
        "\r\n"
        "        <!-- Cảnh 10 -->\r\n"
        "        <div class=\"scene-card-10s\">\r\n"
        "          <span class=\"scene-time-badge\">Cảnh 10 · 90s – 100s (10s)</span>\r\n"
        "          <h4>Gáo Nước Lạnh Có Nguyên Nhân &amp; Hook Tập Sau</h4>\r\n"
        "          <p>Cú xoay cuối do một người, vật hoặc lựa chọn đã được cài từ trước trong tập gây ra (Doctrine §9.8) — mở vòng lặp sang tập kế, không có nhân vật lạ từ trên trời rơi xuống.</p>\r\n"
        "        </div>\r\n")
s = rep(s, OLD9, NEW9)

# ---------- 3. Episode 1 row synced with the approved tap-1 ----------
s = rep(s, "<td><strong>Bát Cơm Ở Cữ Chan Nước Mắt</strong></td>", "<td><strong>Bát Cháo Ở Cữ Chan Nước Mắt</strong></td>")
s = rep(s,
        "Cú hook 3s: Duyên kiệt sức sau sinh làm rơi muỗng sứ, nước mắt rơi vào bát cơm nguội; Má Ba xách võng xếp lên gay gắt đòi cho cháu nằm võng cong lưng thay vì nôi gỗ; Duyên kiệt sức ngã quỵ bên nôi.",
        "Cú hook 3s: nước mắt Duyên rơi vào bát cháo nguội cạnh bình sữa 0 ml, băng keo truyền dịch trên cổ tay; Má Ba xách võng xếp vào, ánh mắt vướng vào cổ tay con dâu rồi cau lại; Má đòi võng bằng ký ức \"ba bây đưa bây ngủ\" (vết sẹo kim cũ trên cổ tay Má); Khang từ chối nhẹ; Duyên gượng đứng rồi ngã quỵ bên nôi.")
s = rep(s,
        "Má Ba thấy vết bầm kim truyền dịch và vết mổ thức tỉnh tình mẫu tử, lau nước mắt ôm con dâu; lót áo bà ba vào nôi ru cháu; Khang dời võng ra ban công; Má bón canh bồ ngót nóng; Dì Tám bất ngờ đập cổng kéo sang Tập 2.",
        "Hai cổ tay cạnh nhau — Má Ba thú nhận \"Hồi đó má cũng giấu... giấu hoài tới ngất\"; ôm con dâu; lót áo bà ba vào nôi ru cháu; Khang mắc võng ra hiên (Dì Tám đã đứng chờ dưới cổng); Má bón canh bồ ngót, không giọt nước mắt nào rơi vào bát, Duyên xin học ầu ơ; Dì Tám xông vào với rượu gừng, Má Ba chắn nôi bằng chính câu của con trai → Tập 2.")

# ---------- 4. Phase B scene-level table, lines pulled verbatim from tap-1 ----------
starts = [m.start() for m in re.finditer(r'<div class="scene-card" id="s-\d+">', t)]
end_main = t.find('<div id="toast"', starts[-1])
assert len(starts) == 10 and end_main > 0
blocks = [t[starts[i]:(starts[i + 1] if i < 9 else end_main)] for i in range(10)]


def lines_of(b):
    out = []
    for m in re.finditer(r'<span class="dia-speaker">([^<\[]+)\[([^\]]+)\]:\s*</span>\s*<span class="dia-spoken-quote">"?(.*?)"?</span>', b, re.S):
        out.append(f"<strong>{m.group(1).strip()}</strong> [{m.group(2).strip()}]: “{m.group(3).strip().strip(chr(34))}”")
    return out


def bridge_of(b):
    m = re.search(r'(?:Kinetic Momentum Bridge|Cliffhanger Binge Loop):\s*([^\r\n<]+)', b)
    return html_lib.unescape(m.group(1).strip()) if m else "—"


def track_of(b):
    m = re.search(r'paradigm-pill[^>]*>(.*?)</span>', b)
    return html_lib.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else "—"


SCENES = [
    ("B1 Hook", "Duyên, Khang, Bé Tin · phòng cữ · bát cháo, bình hút sữa, mâm nhôm",
     "Duyên → được đỡ mà không phải than; Khang → giữ vợ đứng vững", "gồng → vỡ", "\"Em không làm nổi vai người mẹ tốt\"",
     "Hồi hộp: khán giả thấy băng keo truyền dịch, nhà chồng chưa thấy", "Solo + người nghe im lặng — lời than đầu tiên phải đơn độc"),
    ("B2 Setup", "Má Ba, Khang, Duyên, Bé Tin · cửa phòng cữ · võng xếp",
     "Má Ba → giành lại quyền chăm cháu; Khang → che chắn vợ", "riêng tư → bị xâm nhập", "Má thấy vết kim nhưng chối bỏ điều mình nhận ra",
     "Kịch tính trớ trêu + đánh lạc hướng: cái nhìn đọc như khinh, thật ra là nhận ra", "Đối thoại — hai mong muốn va nhau"),
    ("B3 Drama", "Má Ba, Khang, Duyên, Bé Tin · giữa phòng · võng xếp, nôi gỗ",
     "Má Ba → đòi chỗ đứng bằng ký ức; Khang → từ chối mà không làm má đau", "má chắc chắn → khựng lại", "Sợ thành người thừa trong nhà con trai",
     "Gieo bí ẩn: vết sẹo kim cũ trên cổ tay Má, chưa giải thích", "Đối thoại Track AB — lời từ chối phải lịch sự mới đau"),
    ("B3 Drama (exits sealed)", "Duyên, Má Ba, Khang, Bé Tin · bên nôi",
     "Duyên → chứng minh mình vẫn ổn; cơ thể → phản bội", "giấu → lộ", "Tiếng gọi \"con\" bật ra trước mọi định kiến",
     "Đồng cảm: cú ngã đến cùng lúc với nhân vật", "Solo Má Ba — một câu bật ra khi con dâu ngã"),
    ("B4 Climax (major twist TW-04 + TW-16)", "Khang, Duyên, Má Ba, Bé Tin · sàn phòng cữ",
     "Khang → cho má thấy; Duyên → vẫn cố che; Má Ba → đối diện chính mình", "chối bỏ → nhận ra chính mình", "\"Má đã biết, vì má từng giấu y như vậy\"",
     "Đổi chế độ: trớ trêu → nhận ra (hai cổ tay cạnh nhau)", "Solo thú nhận + Khang im lặng — sự thật chỉ một người nói được"),
    ("B5 Release", "Má Ba, Duyên, Khang, Bé Tin · giường",
     "Má Ba → giữ con dâu lại; Duyên → được thương mà không phải xin", "xa cách → gần gũi", "Duyên lén tập ầu ơ để được Má nhận",
     "Đồng cảm", "Đối thoại — hai lời thú nhận nhỏ đổi chỗ cho nhau"),
    ("B5 Release", "Má Ba, Bé Tin, Duyên · nôi gỗ · áo bà ba lót nôi",
     "Má Ba → còn được cần, theo cách mới", "võng → nôi mang hơi bà", "Nhượng bộ mà không thua",
     "Đồng cảm", "Solo hát ru — lời ru thay cho lời xin lỗi"),
    ("B6 Echo (false dawn + plant)", "Khang, Má Ba, Dì Tám (dưới cổng) · hiên tầng hai · võng xếp",
     "Khang → trả cho võng một chỗ mới; Má Ba → nhận món quà mà không mất mặt", "tranh chấp → hòa; nụ cười khựng một nhịp", "Má đã thấy Dì Tám đứng chờ dưới cổng",
     "Hồi hộp: chỉ Má Ba và khán giả thấy Dì Tám", "Đối thoại — trêu nhau để khỏi phải nói lời làm lành"),
    ("B6 Echo (closing image)", "Má Ba, Duyên, Bé Tin · giường · bát canh bồ ngót",
     "Duyên → trao cho Má một vai mới", "người ngoài → người được nhờ", "Xin học ầu ơ = mời Má ở lại",
     "Đồng cảm — hình ảnh khép trả lời hình ảnh mở", "Solo lời xin — Má đáp bằng cái gật đầu"),
    ("Hook Tập 2 (cold water caused by s08, minor twist TW-12)", "Dì Tám, Má Ba, Duyên, Bé Tin · cửa phòng cữ · chai rượu gừng",
     "Dì Tám → kéo Má về lối cũ; Má Ba → bảo vệ cháu bằng lời của con trai", "đồng minh cũ → người chắn cửa", "Má vừa đổi phe, và biết điều đó",
     "Hồi hộp được trả: người đã cài ở s08 bước vào", "Đối thoại — đối thủ cũ nói lại đúng câu của Khang"),
]
rows = []
for i, (beat, cast, want, shift, sub, gap, voice) in enumerate(SCENES):
    b = blocks[i]
    lines = lines_of(b) or ["IM LẶNG — cơ thể nói thay"]
    a, z = i * 10, i * 10 + 10
    rows.append(
        "          <tr>\r\n"
        f"            <td style=\"text-align: center;\"><strong>Cảnh {i + 1:02d}</strong><br><span style=\"font-size: 11px; color: var(--muted);\">{a // 60:02d}:{a % 60:02d}–{z // 60:02d}:{z % 60:02d}</span></td>\r\n"
        f"            <td style=\"font-size: 12px;\">{beat}<br><span style=\"color: var(--muted);\">{html_lib.escape(track_of(b))}</span></td>\r\n"
        f"            <td style=\"font-size: 12px; color: var(--muted);\">{cast}</td>\r\n"
        f"            <td style=\"font-size: 12px;\"><strong>Want:</strong> {want}<br><strong>Shift:</strong> {shift}<br><strong>Subtext:</strong> {sub}<br><strong>Gap:</strong> {gap}</td>\r\n"
        f"            <td style=\"font-size: 12px;\"><em>{voice}</em><br>{'<br>'.join(lines)}</td>\r\n"
        f"            <td style=\"font-size: 12px; color: var(--muted);\">{html_lib.escape(bridge_of(b))}</td>\r\n"
        "          </tr>\r\n")

PHASE_B = (
    "\r\n      <!-- SECTION 5B: EPISODE 1 SCENE-LEVEL ROADMAP (Phase B, workflow.md §8.5) -->\r\n"
    "      <div id=\"ep1-phase-b\" style=\"margin-top: 28px;\">\r\n"
    "        <h3 class=\"section-title\" style=\"font-size: 18px;\"><span>🎬</span> 5B. Tập 1 — Lộ Trình Cấp Cảnh (Phase B · 10 Cảnh x 10s = 100s)</h3>\r\n"
    "        <p style=\"font-size: 12px; color: var(--muted);\">SSOT cho Stage 4: lời thoại khớp nguyên văn với tap-1.html. Story Spine đầy đủ (QUESTION … TWIST) nằm trong tap-1.html (id=\"story-spine\").</p>\r\n"
    "        <table class=\"ep-table\">\r\n"
    "          <thead>\r\n"
    "            <tr>\r\n"
    "              <th style=\"width: 70px; text-align: center;\">Cảnh</th>\r\n"
    "              <th style=\"width: 150px;\">Beat · Track</th>\r\n"
    "              <th style=\"width: 170px;\">Cast · Bối cảnh · Đạo cụ</th>\r\n"
    "              <th>Intent Card (Want · Shift · Subtext · Gap)</th>\r\n"
    "              <th>Voice Mode · Lời thoại</th>\r\n"
    "              <th style=\"width: 170px;\">Kinetic Bridge</th>\r\n"
    "            </tr>\r\n"
    "          </thead>\r\n"
    "          <tbody>\r\n" + "".join(rows) +
    "          </tbody>\r\n"
    "        </table>\r\n"
    "      </div>\r\n")

r0 = s.find('<section id="roadmap">')
r1 = s.find("</table>", r0)
assert r0 > 0 and r1 > r0
s = s[:r1 + len("</table>")] + PHASE_B + s[r1 + len("</table>"):]

open(SETTING, "w", encoding="utf-8", newline="").write(s)
print("PHASE B APPLIED; rows:", len(rows), "; backup ->", BACKUP)
for i in range(10):
    print(f"  s{i + 1:02d}: {len(lines_of(blocks[i]))} line(s)")

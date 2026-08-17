# SVEN RULES — Tóm lược prompt-sven.txt v3 (Omni Flash Prompt System + Dialogue Architecture)

> File gốc đầy đủ: `d:\Project\Short-karma\prompt-sven.txt`  
> Đây là bản TÓM LƯỢC cấu trúc để agent tra cứu nhanh. Khi cần quy tắc chi tiết, ĐỌC FILE GỐC.  
> **v3**: Tích hợp toàn bộ Dialogue Architecture (§D) — thoại điện ảnh theo nguyên tắc Show Don't Tell.

---

## § NGUYÊN TẮC NỀN TẢNG

**3 bên:** User ↔ Agent (tiếng Việt, nhãn nội bộ tự do) | Agent ↔ Omni Flash (chỉ hình ảnh cụ thể)

**Omni Flash**: stateless — mỗi Cảnh là lần gọi độc lập, **không nhớ** Cảnh trước, không hiểu `[Final State]`, `Scene 2`, `as established`, `tiếp nối`.

**PHÉP THỬ DUY NHẤT** (áp mọi câu trước khi đưa vào output):
> *"Người không biết gì về kịch bản, chưa đọc Cảnh trước, chỉ đọc đúng câu này — có hình dung ra chính xác khung hình không?"*

Nếu **KHÔNG** (chứa số Cảnh/Shot, "đã thiết lập", "as established", câu phủ định "không xuất hiện") → **viết lại** thành chi tiết vật lý quan sát được.

**Phân vùng nội dung:**
| Vùng | Đối tượng | Nhãn |
|---|---|---|
| Nội bộ: `[Final State]`, Beat Breakdown, Checklist | Chỉ Agent | Tự do |
| Output thực: `[Subject]`, `[Prop Profile]`, `[Context]`, Shots | Omni Flash | **TUYỆT ĐỐI KHÔNG nhãn tham chiếu** |

---

## § VISUAL STYLE SYSTEM

**DEFAULT (system-wide): `Pixar 3D`** — Pixar · DreamWorks · Disney · Family  
↳ Áp dụng cho mọi prompt trừ khi user chọn style khác tại Bước 1A.

**Propagation Rule — BẮT BUỘC:**  
`[visual style]` được set 1 lần tại `1A` → inject vào **mọi** prompt downstream:

| Prompt | Vị trí inject |
|---|---|
| Character reference grid | Cuối prompt, trước `Negative:` |
| Prop reference grid | Cuối prompt, trước `Negative:` |
| Environment reference grid | Cuối prompt, trước `Negative:` |
| Clip A & B (Quality block) | Dòng cuối trong Quality block |

**Style library đầy đủ (39 styles):** xem `workflow.md § 1A — VISUAL STYLE LIBRARY`



## § [0] DIRECTOR'S INTENTION LOCK — Chạy TRƯỚC Beat Breakdown, nội bộ

Với **mỗi Cảnh**, trước khi viết Shot breakdown, phải xác định:

1. **MỘT chức năng kịch tính**: Cảnh này đang LÀM GÌ cho câu chuyện? (ai vừa mất quyền kiểm soát / vừa giành được, quyền lực nghiêng về đâu, ẩn ý gì bên dưới)
2. **MỘT giọng đạo diễn**: `lạnh lùng-quan sát-từ-xa` | `ngột ngạt-áp sát` | `hỗn loạn-mất-phương-hướng` | `tĩnh lặng-chờ-đợi`
3. Giọng này chi phối camera / ánh sáng / body-state / sound — **giữ xuyên suốt cả Cảnh** (trừ khi Cảnh thuộc TWIST — cho phép đổi giọng đúng 1 lần tại shot cao trào)
4. **Nếu Cảnh có thoại**: Xác định thêm — thoại này TIẾT LỘ hay GIẤU CẢM XÚC? Nhân vật nói điều gì nhưng cơ thể đang phản bội điều ngược lại? (Subtext > Explicit)
5. **KHÔNG xuất ra Omni Flash** — chỉ là bộ lọc nội bộ

**Test nhanh:** *"Nếu bỏ nhãn kỹ thuật, Cảnh này khiến khán giả cảm thấy điều gì? Mọi lựa chọn camera/ánh sáng/thoại có cùng kéo về hướng đó không?"*

---

## § ONE-MOVE RULE

Mỗi Shot chỉ mang **đúng MỘT ý đồ camera**: một chuyển động, một tốc độ, một quan hệ với chủ thể. Không xếp chồng nhiều chuyển động trong 1 Shot ngắn 2-3s.

---

## § [3] NHÂN VẬT & ĐẠO CỤ

### Naming Convention (§3.0)
- Tên nhân vật Code block 1: **tên riêng tiếng Anh 1 âm tiết, không có nghĩa từ vựng, không dấu Việt** (`Lok`, `Vin`, `Ren`, `Keth`, `Tor`, `Mael`, `Ryn`)
- Tên Việt → lập **Bảng Ánh Xạ Tên** nội bộ ở Giai đoạn 1 & 2, dùng xuyên suốt, KHÔNG xuất ra Omni Flash
- Nhân vật tâm linh: giữ danh xưng gốc (Quan Âm, Địa Tạng Vương) + mô tả ngoại hình đầy đủ
- Cấm tuyệt đối: tên ≥2 âm tiết (`Helen`, `Elena`), tên có nghĩa tiếng Anh (`Grace`, `Hope`), tên Latinh hóa (`Tran`, `Lien`)


### [Subject] — §3.2

**MODE A — Không có ảnh tham chiếu (mô tả đầy đủ):**
- Đoạn văn liền ~120 từ mỗi nhân vật A/B
- Thứ tự: Name → Age → Gender → Height → Head-body ratio → Skin → Build → Hair → Facial features → Clothing & props gốc
- **Facial features**: hành vi quan sát được (micro-expression), KHÔNG trừu tượng
- Tuyến C: ~30-40 từ

**MODE B — Có ảnh tham chiếu từ Bước 1 Pre-Production (image-anchored):**
- Chỉ cần: **Tên code (1 âm tiết)** + **đặc tính vật lý neo** (chiều cao, vóc dáng) + **trạng thái hiện tại** + `[Character Reference attached]`
- Bỏ toàn bộ mô tả khuôn mặt, tóc, trang phục — ảnh tham chiếu đã khóa những thứ đó
- Tuyến C: chỉ tên + vai trò + `[Reference attached]`

```
[MODE B — Format nhân vật khi có ảnh tham chiếu]
Lok, 38-year-old male, tall broad-shouldered build. [Character Reference attached]
Initial pose: {tư thế camera-anchored}.
```

### [Prop Profile] — §3.4

**MODE A — Không có ảnh tham chiếu:**
- Tầng 1: tên định danh ngắn gọn (Bamboo Basket, Ledger, Bowl...)
- Tầng 2: vật liệu → hình dạng/kích thước → màu/hoa văn → trọng lượng/cách cầm → **trạng thái HIỆN TẠI tại khung mở đầu Cảnh này**
- Thêm `"the only [tên] in frame"` để chống nhân bản

**MODE B — Có ảnh tham chiếu từ Bước 1:**
- Chỉ cần: **Tên đạo cụ** + **trạng thái HIỆN TẠI** (drawn / sheathed / broken / held / resting) + vị trí camera-anchored + `[Prop Reference attached]`
- Bỏ mô tả vật liệu, màu sắc, hình dạng — ảnh tham chiếu đã khóa

```
[MODE B — Format đạo cụ khi có ảnh tham chiếu]
The Dagger [Prop Reference attached], currently {drawn/sheathed/resting on floor beside Lok's right foot — ZERO hand contact}.
```

### [Environment / Context] — §3.6

**MODE A — Không có ảnh tham chiếu:**
- Mô tả đầy đủ kiến trúc, bề mặt sàn, màu sắc, nguồn sáng, atmosphere

**MODE B — Có ảnh tham chiếu từ Bước 1:**
- Chỉ cần: **Tên địa điểm** + **thời gian trong ngày** + **lighting condition ngắn gọn** + `[Environment Reference X attached]`
- User tự add ảnh tham chiếu vào tool trước khi gửi prompt

```
[MODE B — Format bối cảnh khi có ảnh tham chiếu]
Athena Abandoned Forest [Environment Reference 1 attached], golden hour, low warm side-light from west.
```

### Anti-Duplication — §3.5
- **§3.5b** (Wide/Full shot): thêm `"the only [two] figures in the [empty] space"` khi ít người
- **§3.5e** (Prop): thêm `"the only [prop] in frame"`

> **Quy tắc chọn Mode:** Nếu Bước 1 Pre-Production đã hoàn thành và ảnh tham chiếu đã được tạo → **BẮT BUỘC dùng Mode B** để tránh conflict giữa mô tả text và ảnh. Nếu chưa có ảnh → dùng Mode A.

---

## § [4] CONTINUITY — FINAL STATE

**Final State Gate (§4):** Trước khi viết `[Subject]`/`[Prop Profile]` của Cảnh mới, đọc `[Final State]` của Cảnh trước — vẽ lại trạng thái kế thừa bằng **chi tiết vật lý cụ thể**, không tham chiếu.

**Handoff Frame (§4):** Shot sau mở ĐÚNG tại khoảnh khắc Shot trước kết thúc — vật lý liên tục.

**Single Action Rule (§4):** 1 Shot = 1 hành động chính, không ghép 2 beat độc lập bằng "rồi/sau đó" trong cùng 1 Shot.

**Bảng Trạng Thái Nội Cảnh (§4b):** Theo dõi trạng thái prop thay đổi trong các Shot của cùng 1 Cảnh.

---

## 🛡️ QUY TRÌNH 4 BƯỚC KHÓA BẢO TOÀN THỰC THỂ (THE 4-STEP ENTITY LOCK METHOD)
1. **Bước 1: Single Anchor Dictionary**: Khóa 1 cụm từ định danh duy nhất cho Bối cảnh (`mossy stone floor`), Góc máy (`Shot Medium-Close-up`), Đạo cụ (`Wooden Bowl`), và Âm thanh. Dùng nguyên xi 100% từ đầu đến cuối prompt, CẤM đổi từ đồng nghĩa.
2. **Bước 2: Behavioral Handoff Bridge**: Mọi chuyển dịch tọa độ/trạng thái đạo cụ phải mô tả qua 3 mốc: *Vị trí ban đầu ➔ Hành vi thò tay cúi người nhặt/tác động ➔ Vị trí mới*. CẤM lỗi tự nhảy vị trí (dịch chuyển tức thời / teleportation artifact).
3. **Bước 3: Single Camera Continuum**: 1 Clip 10s BẮT BUỘC giữ ĐÚNG 1 góc máy cố định và bối cảnh liên tục không đổi từ 00:00 đến 00:10 (Beat 1, 2, 3 dùng cùng thông số camera). CẤM đổi góc máy/cắt shot phông nền trong 1 clip 10s để triệt tiêu lỗi méo bối cảnh (*Background Morphing Artifact*).
4. **Bước 4: Entity State Audit**: Chạy phép thử thực thể kiểm tra 3 điểm (từ khóa bối cảnh thống nhất, cầu nối nhặt đạo cụ trực tiếp, đồng bộ ngôn ngữ thoại & acoustic) trước khi xuất code block.

---

📌 **QUY TẮC THỜI LƯỢNG & NHỊP ĐIỆU HÀNH ĐỘNG ĐỘNG (DYNAMIC DURATION & KINETIC ACTION PROTOCOL)**
- **Tổng thời lượng MỖI CẢNH**: BẮT BUỘC bằng **ĐÚNG 10 GIÂY (10s)** cho 100% Cảnh (kể cả Cảnh 1 Hook).
- **Phân bổ Beat Linh Hoạt (Elastic Beat Division)**: AI Agent được TỰ DO SÁNG TẠO phân chia Cảnh 10s thành **2 đến 4 Beat** (Shot) linh hoạt theo nhịp kịch tính của câu chuyện (VD: `4s-3s-3s`, `3s-4s-3s`, `2s-3s-3s-2s`, hoặc `5s-5s`), miễn là **TỔNG = ĐÚNG 10S**.

| Độ dài Beat | Ngân sách Hành động Kịch tính (Biomechanical Action Budget) | Ví dụ ứng dụng linh hoạt |
|---|---|---|
| **Beat 2s** | 1 chuyển động bộc phát ngắn / phản ứng nhân quả giật mình | Giật phắt người, đập bàn, lùi 1 bước. |
| **Beat 3s – 4s** | 2–3 giai đoạn chuyển động liên hoàn có tính nhân quả | Bước đi 3 bước + hạ chân + giơ cuộn thư lên. |
| **Beat 5s (Kinetic Glide)** | Chuyển động trôi mượt kéo dài + camera tracking liên tục | Cam lùi 2m song song với đà bước đi 5 bước. |

**Quy tắc Hành động theo Giây & Đóng Cảnh:**
- **Ngân sách 1 Giây (1s)**: AI render tối đa 1 chuyển động vi mô hoặc 1 nấc gia tốc. CẤM nhồi 2 hành động lớn độc lập vào chung 1s.
- **Dừng Dật Cấp Cuối Cảnh (Terminal Deceleration Hold)**: Beat cuối cùng của Cảnh (dù kết thúc ở 07-10s hay 08-10s) **BẮT BUỘC 0.5s CUỐI CÙNG [09.5s - 10s]** triệt tiêu vận tốc về 0 (`zero-velocity freeze hold`), khóa tư thế tĩnh hoàn toàn (chỉ static hoặc push-in mượt — **CẤM** crane/orbit/arc giật cục).
- **Tổng thời lượng các Beat/Shot trong Cảnh = ĐÚNG 10s TRỌN VẸN (§12.9)**.


---

## § [6] NAMED OBJECT ANCHORING

- **§6a**: Mọi dòng Shot phải có `on {Tên cụ thể}` — KHÔNG `on him/her/it`
- **§6b (TUYỆT ĐỐI)**: Toàn bộ `[Global Shot]` và mọi Shot trong Code block 1 **KHÔNG được có** `he/she/it/his/her/its/they/their/them` — LUÔN lặp tên riêng, kể cả khi đã nêu ở câu trước

---

## § [7] CONCRETE VISUAL RULE

Mọi câu trong output thực phải là **chi tiết vật lý quan sát được**:
- KHÔNG: "cảm thấy sợ hãi", "không khí căng thẳng", "a scene about power"
- ĐÚNG: "gân cổ nổi, đồng tử co lại, môi mím không hoàn toàn"
- ĐÚNG: "Lok's jaw tightens, Lok's right fist curling slowly at Lok's side"

---

## § [1.D] FILMSTOCK — Từ khóa output an toàn (không dùng tên hãng)

| Phong cách (nội bộ) | Từ khóa OUTPUT an toàn |
|---|---|
| Ấm vàng, đêm/nội thất | `warm tungsten-balanced amber glow, deep rich shadow blacks, dramatic low-light contrast, subtle fine grain` |
| Tươi sáng, ngày | `natural daylight-balanced tones, true-to-life skin rendering, high dynamic range, fine grain` |
| Mơ màng, Á Đông | `low-contrast dreamy tone, muted desaturated palette, soft nostalgic haze, gentle melancholic mood` |
| Siêu rực, cổ tích | `hyper-saturated vivid color palette, fairy-tale intensity, rich glossy tone` |
| Đen trắng gai góc | `high-contrast black-and-white, gritty visible grain, stark noir shadow texture` |

---

## § [1.E] TIME OF DAY — Bảng Khai Báo Thời Gian Bắt Buộc Trong Bối Cảnh

> **Bắt buộc**: Mọi Cảnh phải khai báo thời điểm trong ngày bằng cụm từ chuẩn bên dưới — nhúng trực tiếp vào đoạn mô tả bối cảnh của Code Block 1, TRƯỚC phần nguồn sáng.

| Thời điểm | Cụm từ khai báo chuẩn | Màu ánh sáng chủ đạo | Nguồn sáng tự nhiên |
|---|---|---|---|
| **Sáng sớm** (5–7h) | `early morning, pre-sunrise blue hour` | Cool blue-grey, first amber on horizon | Diffused sky glow, no direct sun |
| **Bình minh** (6–8h) | `dawn golden hour, low sun just above horizon` | Warm golden-orange 2200–3000K, long shadows | Low-angle raking sunlight from east |
| **Buổi sáng** (8–11h) | `mid-morning, clear daylight` | Neutral warm white 4500–5500K | Overhead sunlight at 30–45° angle |
| **Trưa** (11h–13h) | `midday harsh sunlight, overhead sun` | Hard white 6000–6500K, minimal shadows | Vertical overhead sun, strong shadows beneath |
| **Chiều** (13–16h) | `afternoon light, soft directional sun` | Warm white 4500K, long fill shadows | Angled sunlight from south-west |
| **Hoàng hôn** (16–18h) | `golden hour, low warm sun before sunset` | Deep amber-gold 2000–2500K, long raking shadows | Low-angle side/back light from west |
| **Hoàng hôn muộn** (18–19h) | `sunset, sun at horizon, warm dusk glow` | Orange-red 1800–2200K, silhouette potential | Sun at or below horizon, skyline glow |
| **Chạng vạng** (19–20h) | `blue hour dusk, post-sunset twilight` | Deep blue-purple sky, warm artificial light contrast | No direct sun, ambient sky + practical lights |
| **Tối** (20–23h) | `nighttime, artificial light only` | Warm tungsten 2700–3000K interior / cool moonblue exterior | Practical lamps, candles, streetlights |
| **Đêm khuya** (23h–3h) | `late night, deep darkness` | Near-black with isolated warm pools of light | Candle / single lamp / moonlight only |

**Cách nhúng vào Code Block 1:**

```
Child's bedroom interior, nighttime — bedside table lamp (practical, frame-right) casts...
             ↑ thời gian khai báo ngay sau tên bối cảnh, trước dấu —
```

**Ví dụ đầy đủ cho mỗi thời điểm:**

```
Bamboo forest path exterior, dawn golden hour, low sun just above the eastern ridge —
open sky casting warm 2400K amber raking light from east-right at 10° angle...

Stone courtyard interior, midday harsh sunlight, overhead sun —
vertical sunlight entering through open roof, hard white 6200K, deep shadow pools directly beneath pillars...

Village road exterior, golden hour, low warm sun before sunset —
warm 2100K amber sidelight from frame-right at 15° angle, long stretched shadows pointing left...

Bedroom interior, nighttime, artificial light only —
bedside table lamp (practical, frame-right, bed-height) casts warm 2800K amber pool across the bed...
```

---



## § [1.F] BODY-STATE COMPATIBILITY CHECK

Trước khi chốt `[Subject]`, kiểm tra:
- **Tay**: nếu nhân vật cầm/thao tác đạo cụ ở bất kỳ Shot nào → KHÔNG khóa cả 2 tay ở tư thế nền (arms crossed, hands in pockets...) → dùng mô tả thân trên trung tính
- **Miệng**: không chồng 2 hoạt động (nhai + nói, uống + nói)
- **Chân**: tư thế nền không mâu thuẫn với hành động chân trong Shot
- **Đầu/mắt**: không mô tả 2 hướng nhìn đồng thời không có chuyển tiếp
- Luôn ghi rõ **tường minh TAY TRÁI hay TAY PHẢI** khi cầm/thao tác đạo cụ (VD: `held in Dax's right hand with Dax's right thumb pressed along the upper edge`). Nếu đạo cụ chưa được cầm, BẮT BUỘC ghi rõ `resting on the floor beside Vin's right foot — ZERO hand contact — the only [prop] in frame`.

### 📌 CẤU TRÚC HEADER SHOT & VĂN XUÔI HÀNH ĐỘNG THUẦN TÚY (PURE CINEMATIC SHOT SPEC)
1. **Định Dạng Header Shot Chuẩn Ống Kính & Camera**:
   ```
   [{timestamp}] Shot {scale} | {lens}mm f/{aperture} | {camera movement & angle} on {Subject}
   ```
2. **Loại Bỏ Hoàn Toàn Từ Nối Rác KHIẾN PROMPT BỊ CỨNG**: CẤM TUYỆT ĐỐI các cụm từ nối gượng gạo như `Driven by the stillness...`, `As Dax halts...`, `Continuing the reach...`. 1 Cảnh 10s là dòng chảy hình ảnh liên tục, hãy tả **TRỰC TIẾP HÀNH ĐỘNG VẬT LÝ NHÌN THẤY ĐƯỢC**.
3. **Mô Tả Chuẩn Xuyên Suốt Timeline**:
   - `[00:00-00:03]`: Tả chuyển động mở đầu của nhân vật + vị trí ống kính.
   - `[00:03-00:07]`: Tả diễn biến tiếp nối của hành động + phản ứng trực tiếp của đối phương.
   - `[00:07-00:10]`: Tả trạng thái khựng tĩnh cuối cảnh (`holds motionless`) + camera push-in nhẹ.

* **✅ ĐÚNG (Tự nhiên, dứt khoát, chuẩn camera & ống kính, KHÔNG từ nối rác)**:  
  `[00:00-00:03] Shot Medium | 50mm f/1.4 | static eye-level on Dax and Vin`  
  `Dax steps forward on the wet granite floor and extends Dax's right hand holding the Debt Scroll toward Vin.`  

  `[00:03-00:07] Shot Medium Close-up | 50mm f/1.4 | low-angle tilt-up on Vin`  
  `Dax thrusts the Debt Scroll downward, causing Vin to recoil and press Vin's palms flat against the stone.`  

  `[00:07-00:10] Shot Close-up | 50mm f/1.4 | slow optical push-in on the Debt Scroll`  
  `Dax holds the Debt Scroll motionless above Vin's head while Vin stays prostrated on the granite floor.`

* **❌ SAI (Dùng từ nối gượng gạo, thiếu thông số camera)**:  
  `Driven by the stillness...` / `As Dax halts...` (thừa thải, gượng gạo, làm sương mù prompt).

---

## § [D] DIALOGUE ARCHITECTURE — Kiến Trúc Lời Thoại Điện Ảnh (v3 Tích Hợp)

> Áp dụng khi Cảnh có thoại. Thoại không phải công cụ giải thích — thoại là **vũ khí tâm lý** và **bề mặt vật lý của cảm xúc**.

### 🔑 §D.0 TRIẾT LÝ NỀN TẢNG — SHOW DON'T TELL QUA THOẠI

Thoại điện ảnh đỉnh cao **KHÔNG BAO GIỜ** nói thẳng cảm xúc. Thoại chỉ là **lớp nổi** — cái chìm bên dưới mới là thứ khán giả cảm thấy:

| TRÁNH (Nói thẳng) | DÙNG (Subtext qua vật lý + thoại gián tiếp) |
|---|---|
| "Tao ghét mày!" | Câu thoại về chủ đề trung lập nhưng giọng siết lại, tay siết chặt vật đang cầm |
| "Tao sợ chết." | "Ngọn nến vẫn còn cháy..." — giọng run nhẹ, mắt nhìn ngọn lửa không nhìn đối phương |
| "Mày phản bội tao." | "Tao nhớ mày thích trà ngọt." — giọng phẳng, không nhìn mặt, tay đẩy tách trà sang |
| "Tao yêu mày." | Im lặng + bàn tay chạm nhẹ vật kỷ niệm + nhìn đi chỗ khác |

**Nguyên tắc vàng**: Nếu xóa câu thoại đi mà cảnh vẫn hiểu được → thoại đó thừa. Nếu giữ thoại mà xóa hành động vật lý thì cảnh mất chiều sâu → thoại + cơ học PHẢI cộng hưởng, không trùng lặp.

---

### 🚨 §D.1 HARD-CAP 160 KÝ TỰ / 10S CLIP

Trong mỗi Clip AI Video 10 giây, **tổng thời lượng toàn bộ câu thoại BẮT BUỘC KHÔNG VƯỢT QUÁ 160 KÝ TỰ TIẾNG ANH** (bao gồm cả dấu câu và khoảng trắng, tương đương 25–30 từ / 3–4 giây phát âm).

> **LÝ DO VẬT LÝ AI**: Phát âm quá 160 ký tự trong 10s sẽ làm AI bị méo cơ mặt (facial distortion artifact), lệch nhịp khớp môi (lip-sync lag), và cướp mất quỹ thời gian dành cho chuyển động cơ thể kịch tính.

**Phân bổ khuyến nghị trong 10s:**
- **1 lượt thoại**: ≤ 160 ký tự — dùng toàn bộ sức nặng vào 1 câu duy nhất
- **2 lượt thoại**: ≤ 80 ký tự/câu — mỗi câu phải bắt từ khóa của câu trước
- **3 lượt thoại**: ≤ 50 ký tự/câu — dạng súng bắn nhanh, mỗi câu là 1 vết cắt tâm lý

---

### 🎯 §D.2 MẠCH THOẠI NHÂN QUẢ BẮT TỪ KHÓA (LOGICAL CAUSALITY CHAIN)

CẤM TUYỆT ĐỐI viết các câu thoại rời rạc. Mọi lượt thoại BẮT BUỘC tuân thủ **Mạch Nhân Quả Bắt Từ Khoá**:

* **Nguyên tắc**: Câu thoại sau BẮT BUỘC bắt lấy **1 Từ khóa chính** hoặc **1 Hành động** của câu thoại trước để bóp nghẹt hoặc bẻ lái tâm lý đối phương.

**Ví dụ chuỗi nhân quả 3 lượt:**
- A: `"Ten years."` (giọng thấp, không giải thích)
- B: `"Ten years... and you come back for THIS?"` (bắt "ten years", bẻ sang ý định)
- A: `"I came back for YOU."` (bắt "come back", lật subtext hoàn toàn)

**5 kiểu bẻ lái tâm lý:**
| Kiểu | Cơ chế | Hiệu ứng |
|---|---|---|
| **Bóp nghẹt** | Lặp lại từ khóa nhưng hạ giọng | Dập tắt không khí |
| **Lật nghĩa** | Dùng từ khóa đó nhưng ý hoàn toàn ngược | Sốc tâm lý nhẹ |
| **Mở rộng** | Kéo từ khóa ra thành hệ quả lớn hơn | Leo thang căng thẳng |
| **Cắt bỏ** | Không trả lời trực tiếp, nói chủ đề khác | Bất an, mất phương hướng |
| **Câu hỏi phản** | Biến lời thoại của đối phương thành câu hỏi ngược | Quyền lực đảo chiều |

---

### 🔥 §D.3 GIA VỊ BẮT BUỘC — SUBTEXT + CƠ HỌC VẬT LÝ

Thoại trong điện ảnh **KHÔNG BAO GIỜ đứng yên**. Mỗi câu thoại BẮT BUỘC được nêm chặt 2 gia vị:

1. **❤️ Cảm Xúc Nội Tâm (Internal Subtext)**: Khai báo tâm trạng thật ẩn bên dưới câu nói — thứ nhân vật KHÔNG NÓI RA nhưng đang cảm.
2. **💥 Hành Động Cơ Học Vật Lý (Micro-Biomechanics)**: Chuyển toàn bộ subtext đó thành cơ học quan sát được — PHẢI khác với ý nghĩa câu thoại bề mặt để tạo chiều sâu:
   - Gân cổ nổi rõ dù giọng nhẹ
   - Nắm đấm siết trắng bệch khớp tay dù miệng đang cười
   - Đồng tử giãn rộng dù mắt đang nhìn xuống
   - Ánh mắt nheo mỉa mai dù câu thoại là lời khen

**Bảng Subtext-to-Physics (thoại điện ảnh):**

| Subtext thật | Câu thoại bề mặt | Cơ học đi kèm |
|---|---|---|
| Kiêu ngạo coi thường | "Anh không cần phải làm vậy." | Giọng nhẹ như giải thích cho trẻ con, mắt nhìn qua vai đối phương |
| Tàn nhẫn không khoan nhượng | "Tôi hiểu." | Giọng phẳng không biến thiên, tay gấp giấy tờ lại chậm rãi |
| Tuyệt vọng giấu kín | "Không sao đâu." | Hơi thở vào qua mũi quá sâu, cơ hàm siết nhẹ |
| Sợ hãi đội lốt hung hăng | "Mày dám làm gì tao?" | Giọng to hơn bình thường, bước chân lùi nhỏ không nhận ra |
| Phẫn nộ bùng nổ sắp vỡ | "Ngươi nợ ta một mạng!" | Nắm đấm nện thẳng xuống sàn đá, bụi nổ vỡ tung, gân cổ nổi rõ |
| Lạnh lùng coi thường | "Vậy tới mà lấy!" | Vung rìu khỏi vai vào thế thủ, môi nheo cười nhếch mỉa mai |

---

### 📌 §D.4 SCRIPTING BRACKET SYNTAX (Cú Pháp Chuẩn Code Block 1)

Mọi dòng thoại trong Code Block 1 BẮT BUỘC áp dụng cú pháp sau — **100% tiếng Anh**:

```text
[Subject English Name] : "[English Dialogue Line ≤ 160 chars]" ([Voice tone & acoustics], [Lips parting in lip-sync], [Physical micro-biomechanics matching subtext])
```

**Ví dụ chuẩn — subtext tương phản với câu thoại bề mặt:**
- `Dax : "Ten years... how much do you owe me?" (voice low and arrogant as if explaining arithmetic, eyes narrowing into a cold sneer, lips parting dynamically in precise lip-sync, right hand thrusting the Debt Scroll downward)`
- `Keth : "I owe you... with my very life!" (voice raw and booming, pupils dilating in burning rage, lips parting dynamically in precise lip-sync, fists white-knuckling on thighs — knuckles visibly pale)`
- `Vin : "Of course." (voice flat and unhurried, lips parting in minimal precise lip-sync, left hand folding the document closed with deliberate slowness — not looking at Dax)`

**⚠️ Camera bị CẤM khi có thoại:** `Crane`, `Orbit`, `Arc`, `Whip pan`, `Handheld mạnh` — chỉ dùng `Static`, `Push-in chậm`, `Pull-out chậm` để bảo vệ lip-sync.

---

### 🎥 §D.5 NGUYÊN TẮC CAMERA-SPEAKER BINDING (Ống Kính Phải Theo Người Nói)

Hướng ống kính camera khi có thoại BẮT BUỘC tuân thủ 4 quy tắc:

#### 🔴 Quy Tắc 1 (Mặc Định Bắt Buộc): AI NÓI — CAMERA CẮT VỀ NGƯỜI ĐÓ
- Bất kỳ nhân vật nào cất tiếng nói (đấu sĩ, nạn nhân, hay **khán giả trên khán đài**) ➔ Camera BẮT BUỘC phải `focus locked on [Speaker Name]`, tả rõ khuôn mặt và biểu cảm nhép môi trực tiếp (`lips parting dynamically in precise lip-sync`).
- **Khán giả phát biểu**: Shot BẮT BUỘC quay trực diện khán giả đó đang đứng/rướn người nhô ra lan can đá cất tiếng.

#### 🔵 Quy Tắc 2 (Chỉ Dùng Cảnh Nội Tâm): THOẠI VỌNG NGOÀI KHUNG HÌNH (OFF-SCREEN VOICEOVER)
- **CHỈ DÙNG CHO CẢNH NỘI TÂM** (nhân vật đang trốn/ẩn náu, giọng đe dọa vọng từ bên ngoài).
- **CẤM TUYỆT ĐỐI** dùng cho cảnh đấu trường hay môi trường mở.
- Cơ chế: Nhân vật A trong phòng giữ miệng đóng chặt (`lips remain closed`), mắt trừng sợ hãi.

#### 👥 Quy Tắc 3: KHÁN GIẢ — ĐẠI DIỆN TÂM LÝ ĐÁM ĐÔNG
- Khán giả trong điện ảnh KHÔNG BAO GIỜ trung lập — đại diện **Mob Bias** (đứng về phía quyền lực, chế diễu nhân vật yếu thế).
- **Đám đông nghìn người nhưng chỉ 1 khán giả cất tiếng**: Định danh 1 người đại diện ở tiền cảnh, shot quay trực diện người đó.
- Ví dụ: `Vane : "Look at the fool! Kneel and beg for mercy!"` (voice loud and mocking, Vane leaning forward over the stone balcony rail, lips parting dynamically in precise lip-sync, background crowd figures cheering behind Vane)

#### 📱 Quy Tắc 4: SELFIE VLOG — FACE ANCHOR LIÊN TỤC
- **CẤM TUYỆT ĐỐI**: KHÔNG để khuôn mặt nhân vật rời khỏi khung hình, không quay lưng bước đi rời camera.
- Máy quay di chuyển đồng bộ với nhân vật (`selfie camera arm locked continuously in right hand, walking forward with background moving behind`).
- Beat cuối: Nhân vật vừa bước tiến vừa nhìn camera tươi cười — khuôn mặt neo 100% ở trung tâm khung hình.

---

### 🚨 §D.6 100% ENGLISH DIALOGUE IN CODE BLOCK 1

Để triệt tiêu 100% lỗi AI Video Model (Omni Flash, Kling, Veo, Sora) bị hoang mang token ngôn ngữ, méo tiếng hoặc tự render chữ phụ đề tiếng Việt trên màn hình:

- **Code Block 1 (Omni Flash Prompt)**: **100% LỜI THOẠI BẰNG TIẾNG ANH**.
- **Code Block 2 (Nội bộ) & Kịch bản Giai đoạn 1**: Giữ nguyên bản dịch **TIẾNG VIỆT** để User & Diễn viên lồng tiếng đọc.

---

### 🗣️ §D.7 DUAL DIALOGUE OUTPUT — Định Dạng Xuất Kép

Mọi lời thoại BẮT BUỘC xuất ra ở **2 định dạng**:

#### Định dạng A — Code Block 1 (Gửi Omni Flash):
```text
[Subject English Name] : "[English Dialogue Line ≤ 160 chars]" (voice tone, lips parting in precise lip-sync, physical micro-biomechanics)
```
- Đầu prompt: `Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Hyper-realistic, ultra-high-definition masterwork. Cinematic 9:16 vertical...`
- Cuối prompt: `Do not generate subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.`

#### Định dạng B — Code Block 2 Nội bộ (Bảng Kịch Bản Thoại):
```text
🗣️ BẢNG KỊCH BẢN THOẠI ĐIỆN ẢNH (EMOTIONAL & PHYSICAL DIALOGUE MANIFEST):
- Cảnh [N] [{timestamp}] | Nhân vật: [Tên Việt] ([Tên English]) | Loại: [Direct / V.O / Monologue / Subtext / Burst]
  💬 Bản dịch tiếng Việt: "[Câu thoại tiếng Việt]"
  🔤 Prompt English AI: "[English Dialogue Line in Code Block 1]"
  ❤️ Subtext nội tâm: [Thứ nhân vật KHÔNG NÓI RA nhưng đang cảm]
  💥 Cơ học vật lý: [Vi cơ học cơ thể — phải TƯƠNG PHẢN hoặc CỘI RỄ subtext, không trùng câu thoại]
```

---

## § [2b] MA TRẬN CẢNH SVEN (MẶC ĐỊNH 7 CẢNH / QUY MÔ 2 — PHÂN BỔ DYNAMIC THEO % KHI N > 7)

- **Mặc định hệ thống**: **7 Cảnh (Quy mô 2: 70s)**: Cảnh 1 (Hook), Cảnh 2-3 (Setup A/B), Cảnh 4-5 (Escalation A/B), Cảnh 6 (Twist), Cảnh 7 (Karma & Aftermath).
- **Quy tắc phân bổ theo % khi N > 7 Cảnh**: Khi kịch bản mở rộng hơn 7 cảnh ($N > 7$), số Cảnh BẮT BUỘC phân bổ lại theo Tỷ lệ % Thời lượng:

| Giai đoạn kịch tính | Tỷ lệ % Thời lượng | Quy tắc phân bổ khi N > 7 Cảnh | Ví dụ N = 10 Cảnh | Ví dụ N = 14 Cảnh |
|---|---|---|---|---|
| **1. HOOK** | **~10%** | Luôn giữ đúng **1 Cảnh 10s** (Hook #4 Motion Freeze) | Cảnh 1 (10s) | Cảnh 1 (10s) |
| **2. SETUP / PLOT** | **25 – 30%** | Mở Visual Anchor từ Hook, gieo Vật biểu tượng, thiết lập bối cảnh & mầm mống mâu thuẫn | Cảnh 2, 3, 4 | Cảnh 2, 3, 4, 5 |
| **3. ESCALATION** | **25 – 30%** | Nén cảm xúc nhiều nấc (Bậc 1 ➔ Bậc 2 ➔ Bậc 3 Peak Tension), đẩy ác nghiệp/thử thách lên đỉnh | Cảnh 5, 6, 7 | Cảnh 6, 7, 8, 9 |
| **4. TWIST / REVEAL** | **15 – 20%** | Insert-shot vật biểu tượng + Lộ diện danh tính thật / Bồ Tát / Chứng nhân | Cảnh 8 | Cảnh 10, 11 |
| **5. KARMA & AFTERMATH** | **15 – 20%** | Quả báo biểu tượng gián tiếp (phần đầu) + Dư âm tĩnh đọng bài học & siêu thoát (phần sau) | Cảnh 9, 10 | Cảnh 12, 13, 14 |

| Giai đoạn | Quy tắc chi tiết triển khai SVEN |
|---|---|
| **HOOK** | Shot 1 (3s): chỉ hé 1 chi tiết gây tò mò, KHÔNG giới thiệu nhân vật. **BẮT BUỘC chứa ≥1 Visual Anchor** tái xuất ở Scene 2 |
| **SETUP/PLOT** | **Shot 1 đầu Scene 2 PHẢI mở bằng Visual Anchor từ Hook** — cùng vật thể/chi tiết, mô tả lại đủ vật lý. Mỗi cảnh tiếp hé lộ 1 lớp thông tin |
| **ESCALATION** | Nén cảm xúc theo từng nấc, đẩy hành vi tàn nhẫn/oán thán nhắm vào đối tượng yếu thế |
| **TWIST/REVEAL** | ≥1 Shot biểu cảm nhận ra (sốc/vỡ lẽ) + 1 **insert-shot** bắt buộc (Close-up/ECU tĩnh, 1-2s) |
| **KARMA + AFTERMATH** | Karma: ĐÚNG vật nhân vật từng tự hào ➔ Aftermath: tĩnh, cấm cường điệu (gào thét...) |


### 8 Kỹ Thuật Hook — Triển Khai SVEN

> Chọn 1 kỹ thuật theo Scoring Framework (story-rules.md § HOOK). Ghi vào metadata: `KỸ THUẬT HOOK: #N — [tên]`.

| # | Kỹ thuật | Shot 1 (3s) — mở | Shot 2-3 — giữ | Shot cuối (2s) — đóng |
|---|---|---|---|---|
| **#1** | **Nghịch lý thị giác** | Wide/Full: 2 hình ảnh mâu thuẫn cùng khung — cắt cứng giữa 2 thế giới | Medium: kéo dần để lộ tương phản | ECU chi tiết nhỏ nối 2 thế giới — đóng băng |
| **#2** | **In medias res** | Close-up: bàn tay/bộ phận cơ thể đang trong hành động chưa rõ nguyên nhân | Medium: pull back nhẹ hé lộ một phần bối cảnh | ECU: biểu cảm hoặc vật — freeze |
| **#3** | **Vật thể/dấu hiệu lạ** | ECU: vật bất thường static — không giải thích | Slow push-in hoặc tilt reveal thêm 1 lớp context | Close-up: vật + bàn tay chạm/không chạm — freeze |
| **#4** | **Khung hình "đóng băng"** | Medium/Close-up: hành động đang dở — vật đang rơi/bay/vỡ | Static hoặc push-in cực chậm giữ khoảnh khắc | ECU phần duy nhất đang chuyển động — freeze |
| **#5** | **Đối lập không khí** | Wide: bối cảnh vui/bình thường rõ ràng | Rack focus hoặc pull back hé lộ chi tiết lạc điệu | Close-up: chi tiết lạc điệu đó — freeze |
| **#6** | **Chi tiết cơ thể/biểu cảm** | ECU: mắt/tay/môi với micro-expression bất thường | Slow push-in hoặc static giữ biểu cảm | Cut to ECU bộ phận khác xác nhận cảm xúc — freeze |
| **#7** | **Sai chỗ/đảo lộn trật tự** | Medium/Wide: vật/người ở vị trí sai quy luật — không giải thích | Tilt down/up hoặc slow pan hé thêm sai lệch | ECU: điểm tiếp xúc sai chỗ — freeze |
| **#8** | **Dấu vết thời gian chồng lấp** | Close-up: bề mặt có dấu vết cũ + dấu vết mới cùng lúc | Slow pull back hé bối cảnh hoang tàn/lịch sử | ECU: điểm giao nhau cũ-mới — freeze |

### HOOK-SETUP BRIDGE — Triển Khai SVEN cho Scene 2 Sau Hook

> **Vấn đề render:** Omni Flash stateless — không biết Scene 1 (Hook) có gì. Nếu Scene 2 không mô tả lại visual anchor bằng chi tiết vật lý đầy đủ, AI video sẽ render 2 cảnh không liên quan nhau.

**Bắt buộc khi viết Scene 2 (SETUP) ngay sau Scene 1 (HOOK):**
1. **`[Prop Profile]` hoặc `[Subject]`**: Visual anchor từ Hook PHẢI có mặt — mô tả lại đầy đủ (kích thước, vật liệu, màu, tình trạng) — KHÔNG tham chiếu Scene 1
2. **`[Global Shot]`**: Câu mở đầu mô tả visual anchor TRƯỚC → mở rộng ra bối cảnh + nhân vật
3. **Beat 1 (3s đầu)**: Camera bắt đầu tại/gần visual anchor → pull back/pan/tilt để reveal nhân vật + bối cảnh — tạo "à-ha moment" cho người xem

---

## § [10] CẤU TRÚC ĐẦU RA — 2 CODE BLOCK VẬT LÝ

### Code block 1 (Phần COPY gửi Omni Flash):

> 🚨 **PRE-FLIGHT — BẮT BUỘC TRƯỚC KHI COPY PROMPT:**
> Agent PHẢI liệt kê rõ các ảnh cần attach, ví dụ:
> ```
> 📎 ATTACH BEFORE SENDING TO OMNI FLASH:
> ① [Tên nhân vật A] — Character Reference (from 1B)
> ② [Tên nhân vật B] — Character Reference (from 1B) ← nếu có
> ③ [Tên đạo cụ] — Prop Reference (from 1C) ← mỗi prop STABLE đã có reference
> ④ [Tên location] — Environment Reference (from 1D)
> ```
> **Nếu Phase 1 đã có reference → BẮT BUỘC dùng Mode B** (không mô tả lại toàn bộ — ảnh đã khóa).
> **Nếu Phase 1 chưa có reference → dùng Mode A** (mô tả đầy đủ ~120 từ/nhân vật).

```
Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Hyper-realistic, ultra-high-definition masterwork. Cinematic 9:16 vertical, {style reference}. Shot on {lens}mm prime lens, f/{aperture}, film grain. {time of day — cụm từ chuẩn từ §[1.E]: e.g. "golden hour, low warm sun before sunset" / "nighttime, artificial light only" / "midday harsh sunlight, overhead sun"}.

▼ CONTEXT (chọn Mode):
[MODE A — chưa có ref] {Mô tả bối cảnh đầy đủ, camera THẤY ĐƯỢC} — {key practical light source} {direction & height} casts {color temperature} light {across/over area} while {atmosphere}; {shadow behavior}; {light transition}.
[MODE B — có ref]      {Tên location} [Environment Reference attached], {time of day phrase} — {key light source + color temp, 1 line only}.

▼ LINE A — NHÂN VẬT CHÍNH (tối đa 2 nhân vật Line A+B cùng lúc trong 1 clip):
[MODE A — chưa có ref] {Tên A}, {tuổi}-year-old {gender}, {chiều cao}cm, {skin tone}, {build}, wearing {costume — NO detached props}. Initial pose: {tư thế camera-anchored, weight bearing}.
[MODE B — có ref]      {Tên A}, {chiều cao}cm, {build}. [Character Reference attached]
                       Initial pose: {tư thế camera-anchored, weight bearing — Tên A's hands empty / hoặc right/left hand tiếp xúc prop}.

▼ LINE B — NHÂN VẬT PHỤ CÓ ARC (nếu xuất hiện clip này, chọn Mode):
[MODE A] {Tên B}, {tuổi}-year-old {gender}, {chiều cao}cm, wearing {costume}. {Camera-relative position.}
[MODE B] {Tên B}, {chiều cao}cm, {build}. [Character Reference attached]. {Camera-relative position.}

▼ LINE C — QUẦN CHÚNG / ĐÁM ĐÔNG / KHÁN GIẢ (KHÔNG cần ảnh tham chiếu — mô tả nhóm):

[CHỈ KHI CÓ MẶT] {Mô tả nhóm ngắn: số lượng ước tính, trang phục chung, hành động tập thể, vị trí camera-anchored}.
Quy tắc Line C: KHÔNG đặt tên cá nhân. KHÔNG tạo ảnh reference. KHÔNG cận mặt. Hành động tập thể.

── GREEK CHORUS FUNCTION (kỹ thuật tuyến C nâng cao) ──────────────────────
Line C là TIẾNG VỌNG CỦA XÃ HỘI — họ nhìn bằng thông tin không đầy đủ.
Cái họ thấy: bề mặt. Cái khán giả thật biết: chiều sâu.
Khoảng cách đó = DRAMATIC IRONY → cảm xúc mạnh nhất trong drama.

NGUYÊN TẮC PHÁN XÉT CỦA TUYẾN C:
  ① Họ LUÔN nhìn bằng góc nhìn bề mặt — không có context nội tâm nhân vật chính
  ② Họ thường PHÁN SAI — chê nhân vật chính, khen nhân vật phản diện
  ③ Phán xét của họ phản ánh thiên kiến xã hội thật (tiền = giỏi, im lặng = yếu, nước mắt = thừa)
  ④ Khán giả thật đau thay nhân vật chính vì THẤY SỰ THẬT mà Line C không thấy
  ⑤ Line C KHÔNG BAO GIỜ biết mình đang sai — họ nói chắc chắn, tự nhiên, không ác ý

── LINE C CÓ THOẠI (Greek Chorus Dialogue) ────────────────────────────────
Khi Line C có thoại → linh động mô tả người nói theo ngữ cảnh. Không cần tên.

  GIỌNG    : Thì thầm xã giao, buôn chuyện tự nhiên — KHÔNG dramatic, KHÔNG to
  NỘI DUNG : Phán xét bề mặt — đúng với thông tin họ có, SAI với sự thật thật sự
  CAMERA   : KHÔNG cut về mặt Line C — bắt tiếng vọng qua shot nhân vật chính
              (nghe tiếng mà không thấy mặt → nhân vật chính bị phán xét mà không được bào chữa)
  ĐỘ DÀI  : ≤ 80 ký tự/câu

Cú pháp thoại Line C — LINH ĐỘNG theo ngữ cảnh:
  [1 male villager, ~27] : "{thoại}" (trạng thái cảm xúc, cách nói)
  [3 frightened villagers] : "{thoại}" (nói đồng thanh nhỏ hoặc tiếng xì xào)
  [elderly woman nearby] : "{thoại}" (lẩm bẩm, không nhìn lên)
  [a group of onlookers] : "{thoại}" (tiếng xôn xao trong đám đông)

Ví dụ — chê nhân vật chính, xã hội nhìn sai bề mặt:
  [1 male vendor, ~40] : "Empty hands. Typical." (flat, matter-of-fact, eyes on his own stall)
  [2 women whispering] : "She should just kick him out." (disapproving click of tongue, not looking)
  [elderly woman nearby] : "That man left. Fifteen years. And now this." (murmured to herself, shaking head)

Ví dụ — khen phản diện vì thấy bề ngoài đẹp:
  [a group of onlookers] : "He's so generous. Always smiling. Nothing like his brother." (admiring, sincere)

Ví dụ — sợ hãi, hỗn loạn:
  [3 frightened villagers] : "Run — just run!" (scattered panic, no one looking at each other)


── NHỊP XUẤT HIỆN CỦA LINE C THEO BEAT ───────────────────────────────────
  Beats căng thẳng (conflict, reveal) : KHÔNG có hoặc im lặng — nhường không gian A+B
  Beats bình thường (setup, daily life): Có mặt, vô tình, không nhìn thẳng
  Beat twist/reveal                    : RÚT ĐI — khoảng yên tĩnh cho moment quan trọng
  Beat catharsis                       : Xa, mờ, tiếp diễn — thế giới không quan tâm, chỉ A biết

▼ GIỚI HẠN CỨNG PER CLIP:
  Nhân vật Line A+B         : tối đa 2 (nếu cần 3 nhân vật có arc → chia 2 clip riêng)
  Nhân vật Line C           : tối đa 1 nhóm mô tả + tối đa 2 câu thoại/clip
  Đạo cụ STABLE có ref      : tối đa 2 props/clip (3+ → dùng wide shot, không cận từng cái)
  Đạo cụ DESTRUCTIBLE       : mô tả trạng thái hiện tại trong text, không cần ref


▼ PROP (chọn Mode — chỉ với STABLE props đã có reference):
[MODE A — chưa có ref / DESTRUCTIBLE state] {Tên prop}, {kích thước}, {material}, {màu}, {condition hiện tại tại khung mở đầu}, resting {camera-anchored position — ZERO hand assignment — "the only [prop] in frame"}.
[MODE B — STABLE, có ref]                  {Tên prop} [Prop Reference attached], currently {drawn/worn/resting — current state + position} — the only {prop} in frame.

▼ ACOUSTIC (nếu có):
Diegetic room acoustics: {tiếng động nền liên tục}.

[{timestamp beat 1}] Shot {scale: Wide/Medium/Close-up} | {lens}mm f/{aperture} | {camera movement & angle} on {Subject}
{1-2 câu văn xuôi — TÊN RIÊNG + Action Verb + Object — Pure Cinematic Spec — KHÔNG TỪ NỐI RÁC.}
{Nếu Beat có thoại (Scripting Bracket Format): [Subject] : "{câu thoại ≤ 160 ký tự}" (voice tone & acoustics, lips parting in precise lip-sync, physical micro-biomechanics — cơ học PHẢI phản ánh subtext, không chỉ lặp lại câu thoại)}

[— BEAT GIỮA NẾU 3-4 BEAT LINH HOẠT —]
[{timestamp beat giữa}] Shot {scale} | {lens}mm f/{aperture} | {camera movement & angle} on {Subject}
{Direct physical action — prop state persistent — costume damage unchanged/progressed — TÊN RIÊNG không đại từ.}
{Nếu Beat có thoại: [Subject] : "{câu thoại ≤ 160 ký tự}" (voice tone, lips parting in precise lip-sync, physical action — cơ học bẻ lái hoặc cộng hưởng subtext)}

[{timestamp beat cuối}] Shot {scale: Medium/Close-up} | {lens}mm f/{aperture} | {static / push-in nhẹ — KHÔNG crane/orbit/arc} on {Subject}
{Câu cuối: frozen pose + prop rests in final condition — 0.5s zero-velocity freeze hold — TÊN RIÊNG.}

Continuous fluid motion, realistic physics, zero morphing. Sharp optical focus locked on active speaker throughout shot.

Do not generate subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video. Do not render duplicate characters, extra background characters, or duplicate props.
```


> ⚠️ **KHÔNG dùng `NEGATIVE PROMPT:`** — đó là cú pháp Stable Diffusion, không hợp lệ với Omni Flash (model đọc toàn bộ prompt như positive text).  
> ⚠️ **KHÔNG dùng lệnh dương** cho audio (`Audio must be fully generated as native spoken dialogue...`) — AI sẽ hiểu đó là lệnh tạo thoại dù kịch bản không có thoại. Toàn bộ clause cuối **phải là `Do not...`**.


### Sau Code block 1 — 🔒 Nội bộ (KHÔNG copy):
```
[Final State — 5 nhóm:
  tên đang dùng: {Bảng Ánh Xạ Tên hiện hành}
  nhân vật: {tư thế/vị trí/biểu cảm từng nhân vật A/B}
  trang phục: {tình trạng từng nhân vật}
  đạo cụ: {tên — hình dạng/vị trí/hướng}
  bối cảnh & không-thời gian: {Location/Time hiện tại}
  → đây là khung hình [Global Shot] Cảnh sau phải neo vào]

🗣️ BẢNG KỊCH BẢN THOẠI (nếu Cảnh có thoại):
- Beat [N] [{timestamp}] | [Tên Việt] ([Tên English])
  💬 Tiếng Việt: "[...]"  🔤 English AI: "[...]"
  ❤️ Subtext: [...]  💥 Cơ học: [...]

📋 Tài nguyên Cảnh [X]:
Nhân vật: {Tên — mới/tái sử dụng}
Bối cảnh: {Tên location — mới/tái sử dụng}
Đạo cụ: {Tên — mốc Roadmap hiện tại}
```

---

## § [10c] BẢNG RỦI RO NEGATIVE PROMPT ĐẶC THÙ CẢNH (12.8)


| Đặc điểm cảnh | Từ khóa bổ sung |
|---|---|
| Nguồn sáng phát quang mạnh (hào quang, lửa) | `overexposed highlights, blown-out light source, washed-out detail` |
| ≥3 nhân vật cùng khung, Tuyến C đông | `extra people, incorrect head count, merged figures, repeated identical background figures` |
| Nước/mưa/gương/bề mặt phản chiếu | `warped reflection, distorted water surface, duplicated reflection` |
| Chuyển động nhanh (chạy, va chạm, vỡ) | `motion smear artifacts, ghosting, unnatural motion blur` |
| Cận tay thao tác đạo cụ | `malformed hands, extra fingers, wrong hand grip` |
| Đám đông Tuyến C | `cloned crowd, uniform identical faces in background` |
| Cảnh có thoại | `subtitles, on-screen captions, dialogue text overlaid on video` |

---

## § [11] CHECKLIST 3 TẦNG — Chạy trước khi xuất mỗi Cảnh

### 🔴 CORE (luôn chạy đủ — sai = video hỏng):
1. ☑ An toàn nội dung qua — không bạo lực/thương tích trực tiếp
2. ☑ Mọi câu trong output thực pass Phép Thử Duy Nhất
3. ☑ Không đại từ (`he/she/it/his/her`) trong toàn Code block 1 — 100% tên riêng
4. ☑ Mọi dòng Shot có `on {Tên cụ thể}`
5. ☑ Đoạn văn `[Subject]` giữ nguyên văn ngoại hình GỐC (không cập nhật trạng thái hiện tại vào đây)
6. ☑ `[Prop Profile]` phản ánh trạng thái HIỆN TẠI tại khung mở đầu Cảnh (đọc Final State trước)
7. ☑ Tổng giây các Shot = đúng 10s (§12.9)
8. ☑ Cảnh ≥2: `[Global Shot]` mở bằng Scene Bridge mô tả đủ 5 nhóm Final State — không tham chiếu
9. ☑ **[Thoại]** Tổng ký tự thoại tiếng Anh trong Cảnh ≤ 160 ký tự
10. ☑ **[Thoại]** Mọi câu thoại Code Block 1 là 100% tiếng Anh, Scripting Bracket Format
11. ☑ **[Thoại]** Camera cut về đúng người nói (Camera-Speaker Binding — §D.5)
12. ☑ **[Thoại]** Cơ học vật lý đi kèm thoại phản ánh subtext, KHÔNG chỉ lặp lại ý câu thoại

### 🟠 QUAN TRỌNG (chạy nếu còn):
13. ☑ `[Global Shot]` không lặp y nguyên câu chữ của Shot bên dưới
14. ☑ Prop thay đổi trạng thái trong Cảnh được vẽ lại đầy đủ ở Shot tương ứng
15. ☑ Body-State Compatibility qua (tay/miệng/chân không xung đột)
16. ☑ Shot cuối và Shot 3: KHÔNG crane/orbit/arc
17. ☑ Negative Prompt bổ sung theo bảng 12.8 nếu Cảnh có đặc điểm rủi ro
18. ☑ Director's Intention Lock nhất quán xuyên suốt Cảnh (giọng đạo diễn không đổi)
19. ☑ **[Thoại]** Mạch nhân quả bắt từ khóa giữa các lượt thoại (§D.2)
20. ☑ **[Thoại]** Subtext nội tâm đã khai báo & cơ học vật lý TƯƠNG PHẢN câu thoại bề mặt (§D.3)

### 🟡 NICE-TO-HAVE (được bỏ nếu thiếu thời gian):
21. ☑ Không lặp cùng góc máy/tiêu cự 3 Shot liên tiếp
22. ☑ Âm thanh dòng Sound theo thứ tự thời gian khớp từng Shot (12.5)
23. ☑ Chi tiết nhận diện nhân vật được nhắc lại ở Shot Close-up liên quan (12.6)
24. ☑ Blocking & Eyeline Match rõ cho ≥2 nhân vật: vị trí frame-left/right, chỉ định rõ eyeline ai nhìn ai khi có ≥3 người (12.3)
25. ☑ Causal Reaction Rule: hành động của người B là phản ứng nhân quả trực tiếp từ hành động của người A
26. ☑ Delta-Only Discipline: Trạng thái kế thừa giữ đúng Single Source of Truth từ `[Subject]` gốc, chỉ ghi nhận biến đổi Delta
27. ☑ Single Ground Plane Rule: 100% nhân vật tương tác đứng/quỳ trên CÙNG 1 MẶT PHẲNG SÀN
28. ☑ Absolute Camera-Anchored Positional Lock: Định vị tọa độ X-Y-Z trước khi render chuyển động
29. ☑ 4 Camera-Subject Coupling Modes: Chọn 1 trong 4 chế độ
30. ☑ Biomechanical Velocity Budget: Di chuyển max 1-1.5m/s (3-5 bước/beat 3-4s)
31. ☑ Terminal Deceleration Protocol: Giây 09-10 (0.5s cuối) triệt tiêu vận tốc về 0

---

## § XÁC NHẬN TIẾN ĐỘ

Sau mỗi Cảnh, in ra:
```
✅ Cảnh [X]/[N] hoàn thành. Bạn có muốn tiếp tục sang Cảnh [X+1] không?
```
Khi đủ N Cảnh:
```
🎬 Hoàn thành toàn bộ [N] Cảnh.
```

---

## § [1] CAMERA / LENS / MOVEMENT — Bảng Tra Cứu Nhanh

### A. Camera Angles (góc máy)
| Tên | Mô tả | Dùng khi |
|---|---|---|
| ECU (Extreme Close-up) | Chỉ 1 chi tiết: mắt, tay, môi | Cảm xúc kìm nén, vật biểu tượng then chốt |
| CU (Close-up) | Khuôn mặt từ vai trở lên | Reveal danh tính, cảm xúc rõ |
| MCU (Medium Close-up) | Ngực trở lên | Hội thoại, tương tác nhân vật |
| MS (Medium Shot) | Eo trở lên | Hành động tay + phản ứng mặt |
| MLS (Medium Long) | Đùi trở lên | Tương tác 2 nhân vật |
| LS (Long Shot) | Toàn thân + bối cảnh | Thiết lập không gian, cô đơn/cô lập |
| ELS (Extreme Long) | Toàn cảnh rộng | Bối cảnh thiên nhiên, scale nhỏ bé |
| OTS (Over-the-shoulder) | Qua vai A nhìn B | Đối thoại quyền lực |
| POV | Góc nhìn nhân vật | Nhập vai, tension cao |
| Dutch Angle | Nghiêng | Bất ổn tâm lý, sắp xảy ra biến cố |
| Bird's-eye / Top-down | Từ trên nhìn xuống | Nhân vật bất lực, bị quan sát |
| Worm's-eye | Từ dưới nhìn lên | Quyền lực, đe dọa |

### B. Lens (ống kính)
| mm | Đặc điểm | Dùng khi |
|---|---|---|
| 14-24mm | Wide cực rộng, biến dạng nhẹ | Kiến trúc, không gian rộng lớn |
| 35mm | Góc rộng nhẹ, tự nhiên | Thiết lập cảnh, môi trường |
| 50mm | Gần mắt người nhất | Trung tính, chân thực |
| 85mm | Portrait đẹp, nén nhẹ | Nhân vật, cảm xúc |
| 135mm | Nén không gian, tách nền | Drama, nhân vật nổi bật trên nền mờ |
| 200mm+ | Nén mạnh, bokeh sâu | Surveillance, khoảng cách tâm lý |

### C. Camera Movements (chuyển động máy)
| Tên | Cách dùng | Dùng khi |
|---|---|---|
| Static | Máy cố định | Tĩnh lặng, quan sát lạnh |
| Push-in (Dolly in) | Tiến vào chủ thể chậm | Leo thang căng thẳng, reveal cảm xúc |
| Pull-out (Dolly out) | Rút xa chủ thể | Cô đơn, mất mát, bị bỏ lại |
| Pan | Xoay ngang | Theo dõi chuyển động, reveal không gian |
| Tilt up/down | Xoay dọc | Reveal từ chi tiết ra toàn cảnh |
| Tracking (Follow) | Bám sát nhân vật | Chuyển động liên tục |
| Crane up/down | Lên/xuống cao | Mở đầu/kết thúc hoành tráng |
| Orbit/Arc | Vòng quanh chủ thể | Nhấn mạnh, thần thánh hóa |
| Handheld | Rung nhẹ tự nhiên | Chaos, khẩn cấp, thực tế thô |
| Zoom (Push-in optical) | Zoom ống kính vào | Surprise, shock moment |

**⚠️ Camera bị CẤM khi có thoại:** `Crane`, `Orbit`, `Arc`, `Whip pan`, `Handheld mạnh` — chỉ dùng `Static`, `Push-in chậm`, `Pull-out chậm` để bảo vệ lip-sync.

---

## § [3.4b] PHYSICAL PRECONDITION RULE — Vật thể Phá vỡ/Biến đổi

**Vấn đề:** Omni Flash không tự suy luận "quá trình vật lý" dẫn đến vỡ/gãy/sập. Nếu `[Prop Profile]` mô tả vật nguyên vẹn → Shot sau yêu cầu vỡ → model vẽ nguyên vẹn hoặc hư hại mơ hồ.

**Quy tắc bắt buộc:**
1. Mọi đạo cụ sẽ gãy/vỡ/rách/sập ở BẤT KỲ Shot nào → `[Prop Profile]` mở Cảnh BẮT BUỘC có ≥1 dấu hiệu suy yếu sẵn (vết nứt, dây sờn, mối nối lỏng, gỗ mục...)
2. Mức suy yếu ban đầu tỉ lệ với số giây cho phép — Shot 2s cần dấu hiệu gần điểm gãy hơn Shot 3s
3. Nếu chưa có tiền đề → phải mô tả tác động ngoại lực rõ ràng ở Shot ngay trước khi vỡ
4. **Test nhanh:** đọc `[Prop Profile]` mở Cảnh — nếu vật "hoàn hảo" nhưng Shot sau yêu cầu vỡ → SAI, bổ sung tiền đề

**Ví dụ:**
- ❌ SAI: Prop Profile: "a massive wooden plaque, bright red" → Shot 2: "the plaque snaps in half"
- ✅ ĐÚNG: Prop Profile: "a massive wooden plaque...a hairline crack running diagonally, supporting ropes visibly frayed" → Shot 2: "the crack widens and splits fully, both halves tearing free from the frayed ropes"

---

## § [3.4c] MOTION-STATE VOCABULARY — Từ Vựng Hành Động Phá Vỡ

**Vấn đề:** Dùng động từ hoàn thành đơn (`snaps`, `shatters`, `collapses`) không kèm trạng thái trung gian → model "nhảy cóc" từ nguyên vẹn sang kết quả, bỏ qua quá trình.

**Quy tắc:**
1. KHÔNG dùng 1 động từ hoàn thành đơn làm toàn bộ mô tả phá vỡ — phải kèm ≥1 cụm trạng thái TRUNG GIAN (phân từ/tính từ: `-ing`, `already`, `tilted`, `suspended`, `frozen mid-`)
2. Shot 2s: ưu tiên tuyệt đối từ vựng trạng thái/lơ lửng — mô tả "đóng băng" tại 1 khoảnh khắc duy nhất
3. Shot 3s: được phép chuỗi động từ tiến triển MỀN LÀ mỗi giai đoạn nối bằng phân từ/mệnh đề quan hệ

**Từ vựng NÊN dùng:**
`already split/torn/collapsed`, `frozen mid-air`, `caught in the instant of`, `suspended`, `mid-collapse`, `mid-fall`, `hanging at an angle`, `tilted`, `scattered`, `still falling`, `half-buried`, `at the exact halfway point of vanishing`

**Từ vựng TRÁNH** (khi dùng đơn lẻ): `snaps`, `crashes`, `breaks apart`, `collapses`, `tears open`, `explodes`, `dissolves`

---

## § [3.5] ANTI-DUPLICATION — Chống Nhân Bản

**a) Singularity Lock** — bắt buộc với cảnh rủi ro cao (Wide/Establishing/Crane/Orbit):
- Nhân vật: `"the only {Tên} in frame"`, `"a single figure"`, `"no other person resembling {Tên} visible"`
- Đạo cụ: `"the single {tên đạo cụ} on the table, no duplicate nearby"`

**b) Wide/Crane/Orbit shots:** BẮT BUỘC mô tả toàn bộ nội dung khung hình còn lại — không để khoảng trống mô tả (model sẽ tự lấp bằng cách nhân bản chủ thể chính):
- ❌ SAI: `Wide Shot on Minh | Minh stands in the empty field.`
- ✅ ĐÚNG: `Wide Shot on Minh | Minh stands alone in the empty field, the only figure in frame; rows of dry rice stalks stretch behind Minh to an empty horizon.`

**c) ≥2 nhân vật cùng Cảnh:** `[Subject]` của mỗi người phải khác nhau ≥3 trục: chiều cao, tông da/tóc, vóc dáng, độ tuổi cảm nhận, màu trang phục.

**d) Tuyến C / đám đông:** Không dùng số nhiều chung chung (`"villagers"`, `"a crowd"`). 2-3 người: mô tả ngắn nhưng khác ≥1 chi tiết mỗi người. >3 người: nhóm hóa bằng mô tả tổng thể có biến thiên rõ.

**e) Đạo cụ phổ biến** (bát, ly, dao...): Phải định vị + định lượng rõ: `"the only bowl on the table"` hoặc `"two bowls: one chipped near Lien, one full near Minh"`.

---

## § [4b] INTRA-SCENE HANDOFF GATE — Continuity Nội Cảnh

**Vấn đề:** Agent dùng "tự hỏi trong đầu" trước mỗi Shot → bỏ sót thực thể không phải trọng tâm camera.

**Giải pháp bắt buộc: Bảng Trạng Thái Nội Cảnh** (nội bộ, KHÔNG xuất ra Omni Flash):

Ngay trước Shot 1, lập bảng liệt kê MỌI thực thể có mặt: `{Tên thực thể} | Trạng thái đầu Shot 1`

Sau khi viết xong mỗi Shot → cập nhật ngay dòng tương ứng → mới sang Shot tiếp theo.

**4 nhóm đối chiếu bắt buộc giữa Shot [N] → Shot [N+1]:**
1. Trạng thái mọi nhân vật có mặt (kể cả không phải chủ thể chính của Shot)
2. Trạng thái mọi đạo cụ có mặt (kể cả đạo cụ vừa được tác động lên vật/người khác)
3. Nhân vật phụ (Tuyến B/C) và vật nuôi đang được tương tác — nhắc lại trạng thái bằng 1 mệnh đề ngắn
4. Không gian & thời gian — vị trí tương đối giữa các thực thể, dấu vết vừa để lại

**Test nhanh:** đọc liên các Shot như 1 đoạn văn xuôi — nếu 1 thực thể "biến mất trạng thái" hoặc "reset về gốc" mà không có hành động giải thích → SAI.

---

## § [4.5] QUY TẮC 2 NHÂN VẬT / ĐÁM ĐÔNG / NHÂN CHỨNG

### a) Active/Passive Rule
Trong mỗi Beat (2-4s), **CHỈ 1 nhân vật** thực hiện Hành động chính (Chủ động). Nhân vật còn lại CHỈ Phản ứng thụ động.

**Vị trí neo bắt buộc khi 2 nhân vật cùng Shot:**
`Subject A at frame-left facing frame-right; Subject B at frame-right facing frame-left`

**Prop Intermediary — chặn hand-merging:**
- KHÔNG BAO GIỜ cho tay 2 nhân vật đan/chạm trực tiếp → dùng đạo cụ làm vật thể trung gian
- ✅ ĐÚNG: `Lok snatches the cloth pouch from Ren's trembling palms — the pouch the only contact point`
- ❌ SAI: `Lok grabs Ren's hands and pulls.`

### b) Emotion Physics — ZERO từ cảm xúc trừu tượng

| Cảm xúc (KHÔNG dùng) | Cơ học thay thế (DÙNG) |
|---|---|
| `fearful` / `scared` | Đồng tử co nhỏ, hai vai rụt tensed, hơi thở dồn dập qua môi hé mở |
| `angry` / `furious` | Gân thái dương nổi rõ, hàm răng mím chặt, ánh mắt trừng rực lửa |
| `sad` / `sorrowful` | Bàn tay run rẩy với vào khoảng không, giọt nước mắt lăn qua vết bùn trên gò má |
| `desperate` / `pleading` | Đầu gập xuống, đầu gối chạm sàn, bàn tay xòe ngửa chưa với tới đối phương |
| `shocked` / `stunned` | Bước chân khựng giữa chừng, tay buông lơi vật đang cầm, miệng hé mở không thành tiếng |
| `relieved` | Vai tụt xuống từ từ, hơi thở dài ra qua mũi, cơ hàm thả lỏng |

### c) Đám Đông "1 + Nền Mờ"
- **1 nhân vật chính nét căng** ở tiêu cự (`sharp optical focus`)
- Đám đông phía sau: `out-of-focus background blurred silhouettes moving as a unified mass`
- KHÔNG tả nét nhiều khuôn mặt cùng lúc — AI không render đồng đều, sinh artifact

### d) Cảnh Nhân Chứng (Witness Reaction Shot)
- **Tách Shot riêng** — không nhét thủ ác + nhân chứng vào cùng 1 Shot 3s
- **Chọn 1 người đại diện** và dùng phản ứng khựng: `steps frozen mid-stride, hands releasing the carried object, eyes wide in shock`

---

## § [4.6] KIẾN TRÚC ĐỒNG BỘ KHÔNG-THỜI GIAN (SPATIOTEMPORAL SYNCHRONIZATION MASTER SPEC)

Toàn bộ quá trình đồng bộ 10s nội cảnh và xuyên cảnh tuân thủ **Bộ 4 Thước Đo Vật Lý Bất Biến**:

### 1. Đồng Bộ Không Gian (Spatial Topology Lock)
- **Single Floor Plane Lock**: 100% nhân vật tương tác BẮT BUỘC quỳ/đứng trên cùng 1 mặt phẳng sàn (`on the same timber floor/dirt ground`), cách nhau 1.5m – 3m.
- **Neo Tọa Độ Camera-Anchored**: Khai báo tọa độ X-Y-Z ngay câu đầu tiên: `Subject A at frame-left facing frame-right; Subject B at frame-right facing frame-left on the same timber floor, 2 meters apart`.
- **Tách Scene Khi Đổi Cao Độ**: CẤM nhét hành trình leo dốc/tháp vào 10s. Tách Scene A (chân dốc 10s) ➔ Scene B (đã trên đỉnh tháp 10s).

### 2. Đồng Bộ Thời Gian & Động Học (Temporal Kinetic Bridging)
- **Cầu Nối Động Học (Kinetic Bridge Connector)**: Đầu Beat 2/Beat 3 BẮT BUỘC mở bằng từ nối động học nối tiếp đà quán tính từ Beat trước (`As Lok halts an arm's length from Keth...` / `Driven by the same stillness...` / `Continuing the forward momentum...`).
- **1 Cause ➔ 2-3 Effects**: 1 Shot là một chuỗi phản ứng vật lý liên hoàn nối tiếp: `Lok steps forward (cause) ➔ dust motes swirl (effect 1) ➔ Keth's eyes flick downward (effect 2)`. CẤM nhồi 2 hành động lớn độc lập bằng từ "rồi/sau đó".

### 3. Bảo Toàn Trạng Thái Nhân Vật (Character State Persistence)
- **Single Source of Truth**: `[Subject]` gốc quy định ngoại hình, tuổi, vết sẹo, màu áo. Mọi Beat BẮT BUỘC dùng **TÊN RIÊNG** (`Lok`, `Keth`), CẤM TUYỆT ĐỐI dùng đại từ `he/she/it/his/her`.
- **Tích Lũy Tổn Thất (Costume Damage Persistence)**: Vết rách/bẩn ở Cảnh trước BẮT BUỘC được duy trì vẹn nguyên ở Cảnh sau (`left shoulder tear intact`).
- **Phản Ứng Vi Cơ Học (Micro-Biomechanics)**: Chuyển toàn bộ cảm xúc thành cơ học vật lý (`jaw tightening`, `pupils dilating`, `knuckles whitening`).

### 5. Triệt Lỗi Không-Thời Gian Giữa Các Beat (Motion-Spatial Discontinuity Rules)
- **Target Distance Lock (Cấm Đi Quá Vị Trí Mục Tiêu)**: Nếu khoảng cách ban đầu giữa A và B là 1.5m – 2m, A chỉ được bước **ĐÚNG 1 BƯỚC NGẮN** (0.5m) ở Beat 1 (00:00-00:03). CẤM tả "A sải bước sải dài" làm A đi vượt qua mặt B (Overshooting artifact).
- **Temporal Handoff Continuity (CẤM Giật Lùi Thời Gian giữa các Beat)**: Beat 2 BẮT BUỘC tiếp nối ĐÚNG vị trí và mốc thời gian Beat 1 dừng lại. CẤM Beat 1 tả A đã tiến tới sát B, sang Beat 2 lại tả "Khi A dừng cách B 2 bước" (lỗi tua lùi thời gian / lùi vị trí).
- **Single Primary Prop Discipline (Chống Thừa Đạo Cụ / Trôi Đạo Cụ Rác)**: Trong 1 Cảnh 10s, CHỈ Khai báo **ĐÚNG 1 ĐẠO CỤ CHÍNH** trong `[Prop Profile]`. Các chi tiết kiến trúc/bối cảnh khác thuộc về `[Context]`. CẤM khai báo tràn lan 3-4 đạo cụ phụ làm AI hoang mang tự nhân bản đạo cụ.

---

## § [10c] 12 LỖI THƯỜNG GẶP (Framework Kiểm Lỗi Cross-cutting)

| # | Tên lỗi | Dấu hiệu nhận biết | Cách sửa |
|---|---|---|---|
| 12.1 | Profile-Action Conflict | `[Subject]` tay khóa nhưng Shot cần cầm đạo cụ | Bỏ khóa tay trong `[Subject]`, dùng mô tả thân trên trung tính |
| 12.2 | Causal Motivation Gap | Nhân vật đổi ý/hành động mà không có kích thích quan sát được trước đó | Thêm 1 chi tiết vật lý kích hoạt trước hành động đổi ý |
| 12.3 | Spatial Overcrowding | ≥2 nhân vật nhưng không khai báo vị trí frame-left/right/tiền-hậu cảnh | Thêm `Subject A at frame-left... Subject B at frame-right...` |
| 12.4 | Unmotivated Camera Jump | Nhảy từ ECU sang Wide không có lý do kịch tính | Thêm 1 Shot trung gian hoặc giải thích lý do đổi cỡ cảnh |
| 12.5 | Sound-Shot Mismatch | Âm thanh trong dòng Sound không khớp với hành động/thời điểm Shot | Sắp xếp lại dòng Sound theo thứ tự thời gian, khớp từng Shot |
| 12.6 | Identity Loss at Close-up | Close-up bỏ qua chi tiết nhận diện (màu áo, sẹo, phụ kiện) | Nhắc lại ≥1 chi tiết nhận diện rõ trong câu mở đầu Shot |
| 12.7 | Number/Pronoun Agreement | Dùng số nhiều nhưng chủ thể là số ít, hoặc `he/she/it` thay tên | Thay tất cả đại từ nhân xưng bằng tên riêng trong output thực |
| 12.8 | Missing Scene-Specific Safety | Cảnh có đặc điểm rủi ro (đám đông, nước, tay cận) nhưng thiếu `Do not...` phù hợp | Thêm cụm Nhóm C từ bảng Negative Prompt (§ Negative Prompt Tổng) |
| 12.9 | Total Duration Mismatch | Tổng giây các Shot ≠ thời lượng ghi đầu Cảnh | Cộng lại, sửa Shot linh hoạt nhất (thường Shot cuối) |
| 12.10 | Active/Passive Violation | 2 nhân vật cùng Beat đều có hành động chủ động, hoặc tay chạm trực tiếp | Xác định Active/Passive, thêm Prop Intermediary |
| 12.11 | Crowd/Witness Artifact | Nhiều khuôn mặt đám đông rõ nét, hoặc thủ ác + nhân chứng cùng 1 Shot | Áp "1 + Nền Mờ"; tách Witness thành Shot riêng |
| 12.1b | Motion-in-Static Conflict | Động từ hoàn thành đơn (`snaps`, `explodes`) không có trạng thái trung gian | Thay bằng phân từ/trạng thái lơ lửng (xem § [3.4c]) |
| **D.1** | **Dialogue Over-Explicit** | Câu thoại nói thẳng cảm xúc (`"I am afraid"`, `"I hate you"`) | Thay bằng câu thoại gián tiếp + cơ học phản bội subtext (§D.0, §D.3) |
| **D.2** | **Dialogue Causality Break** | Câu thoại sau không bắt từ khóa của câu thoại trước | Áp Mạch Nhân Quả Bắt Từ Khoá (§D.2) |
| **D.3** | **Camera-Speaker Mismatch** | Camera không cut về người đang nói | Áp Camera-Speaker Binding §D.5 Rule 1 |
| **D.4** | **Lip-sync Camera Violation** | Beat có thoại nhưng dùng Crane/Orbit/Arc | Đổi sang Static hoặc Push-in chậm |

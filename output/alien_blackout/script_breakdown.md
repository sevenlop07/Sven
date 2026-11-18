# PRODUCTION BIBLE & SHOT BREAKDOWN — "Mất Điện Khu Phố" (`alien_blackout`)

- **Format:** `9:16` (`1080x1920`, `30 fps`, tổng thời lượng `52.85s` theo `voice.mp3`)
- **Engine & Look:** Blender 5.3 Cycles GPU (`real_outdoor` ban đêm/nhá nhem ẩm ướt sau mưa + đèn đường/ánh sáng xanh Neon) · Bộ mặt `Cartoon` (`assets/faces_cartoon/`)

---

## I. THỜI GIAN & ĐỊA ĐIỂM (`[context]`)

- **Thời gian câu chuyện:** `20:00 – 20:03 tối Thứ Bảy`. Đường xá và sân gạch vừa tạnh mưa nên còn ẩm ướt, phản chiếu ánh đèn đường và ánh sáng xanh lá từ cuối hẻm.
- **LOC_01 — Phòng Khách Nhà Minh (Căn số 01 đầu hẻm):**
  - Tài nguyên: `Set_LivingRoom.glb`, `Prop_OfficeDeskLaptop.glb`, `Prop_BankersLamp.glb`, `Nature_PottedMonstera.glb`.
  - Bố cục: Bàn làm việc kê sát cửa sổ tối nhìn ra dọc con hẻm về phía căn phòng cuối dãy.
  - Ánh sáng: Ban đầu đèn bàn (`Prop_BankersLamp`) sáng vàng ấm (`3200K`) + màn hình laptop xanh dương; tới `08.9s` tắt phụt tối om, chỉ còn ánh trăng xám xanh và tia xanh lá từ cửa sổ cuối hẻm hắt vào.
- **LOC_02 — Con Hẻm Khu Phố Bình Minh (3 lớp chiều sâu):**
  - **Tiền cảnh:** Cột đèn đường, bờ rào gỗ, vũng nước mặt đường hẻm phản chiếu ánh sáng.
  - **Trung cảnh:** Dãy 4 căn nhà mái ngói san sát (Nhà số 01 của Minh $\to$ Nhà số 02 của Cô Hoa $\to$ Nhà số 03 của Chú Tư $\to$ Phòng trọ số 04 cuối hẻm), ô tô `Prop_Car_RobloxResources.glb` đậu bên lề, cây sồi/bụi hoa `Nature_OakPinePack_CS.glb` + `Nature_BushFlowers.glb`.
  - **Hậu cảnh:** Hàng cây xa và dãy núi tối dưới bầu trời mây đêm `real_outdoor`.
  - Ánh sáng: `00.00s–02.20s` đèn đường & cửa sổ các nhà sáng ấm $\to$ `02.20s` sập tối đồng loạt, riêng **Phòng 04 cuối hẻm** sáng rực ánh xanh lá (`#33FF55`) qua cửa sổ kính tối $\to$ `40.90s` toàn bộ khu phố bật sáng vàng ấm rực rỡ trở lại!
- **LOC_03 — Bên Trong Phòng Trọ Số 04 Cuối Hẻm:**
  - Tài nguyên: `Set_LivingRoom.glb` (biến thể phòng trọ), `Prop_InteriorDoor.glb`, `Prop_DiningChair.glb` + bàn gỗ nhỏ.
  - Ánh sáng: Tối âm u trừ nguồn sáng cực mạnh màu xanh lá từ **Lõi Pin Vũ Trụ** giữa phòng (rọi bóng gắt lên trần và mặt các nhân vật). Từ `40.90s` bật sáng đèn trần trắng ấm bình thường.

---

## II. HỒ SƠ NHÂN VẬT (`[subject]`)

1. **`Minh` (24 tuổi — Người kể chuyện / Dân IT nhà số 01):**
   - **Ngoại hình Core:** `boy_athletic`, da tự nhiên, tóc `Hair_ClassicSpiky_CS.glb` (nâu đen), áo hoodie vàng `shirt_me.png` (`#F5D66E`), quần xanh than `pants_me.png` (`#3D4A6B`).
   - **Tính cách:** Hay để ý xung quanh, phản ứng nhanh (`shocked` $\to$ `angry` $\to$ `pop_eyes`), đi cùng xóm sang gõ cửa tìm hiểu ngọn ngành.
2. **`Cô Hoa` (45 tuổi — Hàng xóm nhà số 02):**
   - **Ngoại hình Core:** `girl_slim`, tóc `long_ponytail` (nâu sẫm gọn gàng), áo tím `shirt_mom.png` (`#B7A3E6`), quần `pants_mom.png` (`#5A4A7A`).
   - **Tính cách:** Dễ hoảng hốt, cưng mèo như con, hay báo động cho cả hẻm (`scared` $\to$ `pop_eyes` $\to$ `happy`).
3. **`Chú Tư` (52 tuổi — Tổ trưởng tổ dân phố nhà số 03):**
   - **Ngoại hình Core:** `stocky_boss`, tóc `slick_part`, râu `mustache` rậm, áo cổ bẻ xanh đậm `shirt_dad.png` (`#2F3E63`), quần tối `pants_dad.png` (`#2B2B33`).
   - **Tính cách:** Nóng tính, nghiêm nghị (`steam_angry` $\to$ `shocked` $\to$ `happy`), là người đi đầu kéo cả đám tới Phòng 04.
4. **`Zor-7` (Người ngoài hành tinh ngụy trang — Khách mới thuê Phòng 04):**
   - **Ngoại hình Core:** `tall_lanky`, da xanh ngọc nhạt (`#7BD8A8`), tóc dựng ngược quái dị `Hair_CrazyDev_CS.glb`, áo cổ bẻ xanh cổ vịt `shirt_c7.png` (`#2C7A78`), quần tối `pants_dad.png`.
   - **Tính cách:** Tỉnh bơ, thực dụng, lén câu điện xóm sạc pin đĩa bay; khi bị bắt quả tang liền cười gượng xin lỗi rồi chuồn cực nhanh (`shocked` $\to$ `smirk` $\to$ `silly_tongue`).

---

## III. DANH MỤC ĐẠO CỤ (`[prop]`)

- **`PROP_01` — Laptop (`Prop_OfficeDeskLaptop.glb`):** Đặt trên bàn nhà Minh (`LOC_01`), màn hình sáng xanh ban đầu, tắt đen ở `08.9s`.
- **`PROP_02` — Đèn bàn (`Prop_BankersLamp.glb`):** Đặt cạnh laptop, tắt phụt đồng bộ ở `08.9s`.
- **`PROP_03` — Điện thoại thông minh:** Gắn tay phải Minh (`bake_prop_follow`), sáng rực thông báo nhóm chat ở `11.24s–15.84s`.
- **`PROP_04` — Mèo Tuxedo (`Pet_Cat_Tuxedo.glb`):** Con mèo của Cô Hoa, gắn hai tay Cô Hoa khi bế chạy ra ngõ (`18.10s–22.56s`), cử động đầu/đuôi.
- **`PROP_05` — Cửa gỗ Phòng 04 (`Prop_InteriorDoor.glb`):** Ban đầu đóng kín (`0°`), mở hé (`35°`) ở `26.58s` rồi mở toang (`85°`) ở `29.5s`.
- **`PROP_06` — Lõi Pin Vũ Trụ + Dây Cáp Trần Nhà:** Khối trụ công nghệ phát sáng xanh Neon to bằng nồi cơm đặt trên sàn Phòng 04, nối 1 sợi dây cáp thẳng lên trần nhà; ở `38.56s` bị Zor-7 giật rời khỏi ổ cắm trần, tắt sáng ngay lập tức.
- **`PROP_07` — Bàn gỗ + 2 Ổ Bánh Mì Vàng Giòn:** Đặt trên bàn cạnh ghế `Prop_DiningChair.glb` trong Phòng 04; ở `47.46s` gắn theo 2 tay Zor-7 bay thẳng lên trời.

---

## IV. KỊCH BẢN PHÂN CẢNH CHI TIẾT (21 BEAT · `00:00.00 – 00:52.85`)

| Beat | Thời Gian | Địa Điểm & Ánh Sáng | Nhân Vật & Mặt (`Cartoon`) | Đạo Cụ | Cốt Truyện Cảnh & Hành Động (`State A ➔ State B`) | Góc Máy (`Director Plan`) | Lời Thoại (`SRT`) |
|---|---|---|---|---|---|---|---|
| **01** | `0.00–3.50s` | `LOC_02` Con hẻm · Trời tối ẩm, đèn đường sáng rồi sập tắt ở `2.2s` | Chưa lộ mặt (dãy nhà + xe cộ yên ắng) | Đèn đường, dãy nhà, `Prop_Car` | **Hook toàn khu phố mất điện:** Toàn bộ con hẻm đang sáng đèn sinh hoạt bình thường (`State A`), tới đúng giây `2.20` đồng loạt các ô cửa và đèn đường tắt phụt tối đen như mực (`State B`). | `WS · Eye · Push-in` dọc trục con hẻm | *"Đúng 8 giờ tối, cả xóm tôi tắt phụt hết đèn."* |
| **02** | `3.50–5.60s` | `LOC_02` Hẻm tối đen · Ánh sáng xanh lá Neon hắt từ cuối hẻm | Chưa có người | Cửa sổ Phòng 04 | **Điểm bất thường duy nhất:** Giữa con hẻm tối om (`State A`), ánh sáng xanh lá rực rỡ bất ngờ hắt mạnh qua cửa sổ kính căn phòng trọ cuối dãy, phản chiếu xuống mặt đường ướt (`State B`). | `MCU · Low · Static` khóa vào góc tường căn Phòng 04 | *"Trừ đúng căn phòng cuối dãy, vẫn sáng rực"* |
| **03** | `5.60–7.70s` | `LOC_02` Sát cửa sổ Phòng 04 · Tia sáng xanh rọi chói | Bóng mờ sau rèm | Cửa sổ Phòng 04 | **Nhấn mạnh nghi vấn:** Cận cảnh ô cửa kính Phòng 04 nhấp nháy tia sáng xanh Neon quái dị, sau rèm lướt qua bóng cao gầy của `Zor-7`. | `CU · High · Push-in` vào khung kính | *"màu xanh lá."* |
| **04** | `7.70–11.24s` | `LOC_01` Phòng Minh · Vàng ấm chuyển sang tối om ở `8.9s` | `Minh` (`neutral` ➔ `angry`) | `Prop_OfficeDeskLaptop`, `Prop_BankersLamp` | **Thiệt hại trực tiếp của Minh:** Minh đang gõ phím lia lịa (`State A`), ở `8.9s` đèn bàn + màn hình laptop tắt phụt khiến Minh giật nảy người, hai tay vỗ mạnh lên bàn bực bội (`State B`). | `MCU · Low · Truck` lướt ngang bàn làm việc | *"Tôi đang gõ dở máy tính thì sập nguồn tối om."* |
| **05** | `11.24–13.66s` | `LOC_01` Phòng Minh tối · Màn hình điện thoại hắt sáng mặt | `Minh` (`angry` ➔ `shocked`) | `PROP_03` Điện thoại | **Bùng nổ nhóm chat:** Minh rút phắt điện thoại từ túi quần giơ lên ngang ngực (`State A`), màn hình sáng bừng nhấp nháy tin nhắn dồn dập khiến Minh trố mắt (`State B`). | `MS · Low · Pull-out` lùi nhẹ lấy hết dáng Minh đứng bật dậy | *"Nhóm chat khu phố lập tức nổ tung."* |
| **06** | `13.66–15.84s` | `LOC_01` Cận màn hình điện thoại hắt sáng xanh dương | Tay `Minh` cầm máy | `PROP_03` Điện thoại | **Bằng chứng xóm náo loạn:** Đặc tả ngón tay cái của Minh lướt nhanh màn hình điện thoại đang nhảy bong bóng chat liên hồi (`"Mất điện?"`, `"Phòng cuối sáng kìa"`). | `INSERT · Dutch · Orbit-arc` nghiêng kịch tính | *"Ai cũng hỏi sao mất điện hết mà nhà cuối"* |
| **07** | `15.84–18.10s` | `LOC_01` Sát mặt Minh quay ra cửa sổ | `Minh` (`pop_eyes`) | Khung cửa sổ | **Minh quyết định ra ngõ:** Minh ngoái cổ nhìn qua khung cửa sổ phòng mình (`State A`), ánh sáng xanh lá từ cuối hẻm hắt thẳng vào mắt tròn xoe của Minh (`State B`). | `CU · Dutch · Static` góc nghiêng cận mặt Minh | *"vẫn sáng xanh lè?"* |
| **08** | `18.10–20.14s` | `LOC_02` Ngõ trước nhà số 02 · Tối + ánh xanh hắt xa | `Cô Hoa` (`scared`) + `Minh` (`shocked`) | `Pet_Cat_Tuxedo` trên tay Cô Hoa | **Nhân chứng đầu tiên chạy ra:** Cô Hoa ôm chặt con mèo `Miu` chạy vội từ hiên nhà số 02 ra đầu ngõ (`State A`), đứng khựng lại đối diện Minh trên trục 180° (`State B`). | `OTS · Low · Static` qua vai Minh nhắm sang Cô Hoa | *"Cô hàng xóm bế con mèo chạy ra ngõ,"* |
| **09** | `20.14–22.56s` | `LOC_02` Đầu ngõ hẹp · Ánh xanh hắt nghiêng | `Cô Hoa` (`pop_eyes`) + `Miu` | `Pet_Cat_Tuxedo` | **Hoảng loạn tột độ:** Cô Hoa run lẩy bẩy một tay giữ mèo, tay kia chỉ thẳng về cuối dãy phòng trọ (`State A ➔ State B`), con mèo cũng giật tai dựng đuôi nhìn theo. | `CU · High · Push-in` đặc tả gương mặt hoảng hốt của Cô Hoa | *"mặt cắt không còn giọt máu."* |
| **10** | `22.56–24.58s` | `LOC_02` Dọc con hẻm đi về Phòng 04 | `Chú Tư` (`steam_angry`), `Minh` (`shocked`), `Cô Hoa` (`scared`) | Cây cối & xe `Prop_Car` bên đường | **Hội đồng xóm tiến quân:** Chú Tư dẫn đầu bước rón rén cúi thấp người dọc tường hẻm (`Walking`), theo sát sau là Minh và Cô Hoa ôm mèo tiến về phía ánh sáng xanh (`State A ➔ State B`). | `MCU · High · Truck` lia ngang theo bước chân rón rén | *"Mấy nhà kéo nhau rón rén đi tới trước"* |
| **11** | `24.58–26.58s` | `LOC_02` Ngay trước bậc thềm Phòng 04 · Ánh xanh hắt qua khe cửa | `Chú Tư` (`steam_angry`), `Minh` | `PROP_05` Cửa gỗ Phòng 04 | **Áp sát cửa nghi phạm:** Cả nhóm dừng sát mép cửa Phòng 04, Chú Tư giơ tay gõ gắt 2 cái rồi vặn nắm đấm cửa (`State A ➔ State B`). | `CU · Low · Push-in` sát tay nắm cửa và mặt căng thẳng | *"cửa căn phòng đó."* |
| **12** | `26.58–30.00s` | `LOC_02 / LOC_03` Ngưỡng cửa Phòng 04 · Luồng sáng xanh phụt ra ngoài | `Minh`, `Cô Hoa`, `Chú Tư` (`pop_eyes` đồng loạt) | `PROP_05` Cửa mở hé `0° ➔ 35°` | **Khoảnh khắc đóng băng:** Cánh cửa kẽo kẹt hé mở, luồng sáng xanh lá chói lòa rọi thẳng ra ngoài khiến cả 3 người há hốc miệng đứng chôn chân như tượng (`State A ➔ State B`). | `CU · Dutch · Orbit-arc` xoay qua biểu cảm 3 người | *"Cửa vừa hé mở, cả đám đứng hình luôn."* |
| **13** | `30.00–33.22s` | `LOC_03` Bên trong Phòng 04 · Tối mịt trừ cột sáng xanh lá ở giữa | `Zor-7` (`smirk` tập trung), lưng/nghiêng góc 3/4 | Dây điện từ trần nhà | **Lộ diện hung thủ:** Camera đẩy thẳng qua khe cửa vào giữa phòng — thấy `Zor-7` tóc dựng ngược đang giơ hai tay giữ mối nối dây điện câu thẳng từ ổ trần xuống. | `MS · Eye · Push-in` tiến vào trong phòng | *"Một gã tóc dựng đứng đang cắm dây thẳng từ trần nhà vào cục"* |
| **14** | `33.22–36.30s` | `LOC_03` Trung tâm Phòng 04 · Sáng xanh rực | Tay `Zor-7` + `PROP_06` | **Lõi Pin Vũ Trụ** (to bằng nồi cơm) | **Vật chứng phi lý:** Đặc tả cục pin trụ kim loại tỏa quầng sáng xanh lá cực mạnh đặt giữa sàn, kim đồng hồ/vòng sáng quay tít khi hút điện xóm. | `CU · Low · Push-in` góc thấp vào Cục Pin Vũ Trụ | *"pin phát sáng to bằng cái nồi cơm."* |
| **15** | `36.30–38.56s` | `LOC_03` Phòng 04 · Ánh xanh rọi ngược cằm `Zor-7` | `Zor-7` (`shocked` ➔ `smirk`) | Dây điện & Pin | **Bắt quả tang:** Nghe tiếng thở hổn hển ở cửa, `Zor-7` giật nảy (`Jump`), quay phắt đầu lại đối diện nhóm Chú Tư rồi nhăn răng cười gượng (`smirk`). | `MCU · Eye · Push-in` vào mặt `Zor-7` | *"Hắn giật mình quay lại, cười gượng"* |
| **16** | `38.56–40.90s` | `LOC_03` Sát tay `Zor-7` và ổ dây | `Zor-7` (`smirk`) | `PROP_06` Dây điện & Pin | **Ngắt kết nối:** Không nói nhiều, tay `Zor-7` giật phịch phích nối ra khỏi cục pin — tia sáng xanh lá vụt tắt phụt ngay lập tức (`State A ➔ State B`). | `CU · Low · Static` khóa tay giật dây | *"rồi rút phịch dây điện ra."* |
| **17** | `40.90–42.94s` | `LOC_02` Toàn cảnh con hẻm · Đèn đường & cả 4 căn nhà đồng loạt sáng ấm `3500K` | Cả xóm đứng trước Phòng 04 | Dãy nhà, đèn đường, xe `Prop_Car` | **Cả xóm có điện lại:** Khoảnh khắc dây rút ra, từ Phòng 04 lan dọc cả con hẻm, mọi bóng đèn đường và cửa sổ đồng loạt bật sáng vàng rực rỡ (`State A ➔ State B`). | `WS · Low · Pull-out` lùi rộng ra toàn cảnh con hẻm | *"Ngay lập tức, đèn cả khu phố"* |
| **18** | `42.94–44.92s` | `LOC_03 / Cửa Phòng 04` Đèn trần bật sáng ấm | `Cô Hoa`, `Chú Tư`, `Minh` (`happy`) | Đèn phòng sáng ấm | **Nhẹ nhõm tưởng xong chuyện:** Ba hàng xóm thở phào, nét mặt rạng rỡ tươi cười sắp đưa tay lên định vỗ tay hoan hô (`State A ➔ State B`). | `CU · Low · Push-in` vào phản ứng vui mừng của xóm | *"bật sáng rực rỡ."* |
| **19** | `44.92–47.46s` | `LOC_03` Phòng 04 · Ánh đèn sáng trưng | `Minh/Chú Tư` (vai tiền cảnh) $\leftrightarrow$ `Zor-7` (`smirk`) | `PROP_07` Bàn ăn & `Prop_DiningChair` | **Cú lật bất ngờ:** Khi hàng xóm vừa giơ tay định vỗ, `Zor-7` xoay người cực nhanh lao về phía bàn ăn cuối góc phòng (`State A ➔ State B`). | `OTS · Eye · Push-in` từ phía hàng xóm hướng vào `Zor-7` | *"Cả xóm còn chưa kịp vỗ tay, hắn đã vơ"* |
| **20** | `47.46–49.98s` | `LOC_03` Cận mặt bàn ăn Phòng 04 | Hai tay `Zor-7` | `PROP_07` **2 ổ bánh mì** | **Cướp đồ lộ phí:** Hai bàn tay xanh của `Zor-7` quơ gọn cả 2 ổ bánh mì vàng giòn trên đĩa (`bake_prop_follow`) kẹp chặt vào nách trước khi hàng xóm kịp ú ớ. | `CU · Low · Push-in` vào 2 ổ bánh mì biến mất khỏi bàn | *"lẹ hai ổ bánh mì trên bàn."* |
| **21** | `49.98–52.85s` | `LOC_02` Ngoài sân Phòng 04 hướng lên trời đêm | `Zor-7` (`silly_tongue` + `Cheering`), bên dưới là `Minh`, `Cô Hoa`, `Chú Tư` (`pop_eyes`) | `2 ổ bánh mì` + `Pin Vũ Trụ` trên tay | **Kết lầy lội bay về hành tinh:** `Zor-7` nháy mắt thè lưỡi (`silly_tongue`), ôm 2 ổ bánh mì + cục pin phi thẳng qua cửa sổ/hiên nhà bay vút lên trời đêm (`Cheering`), bỏ lại cả xóm ngước cổ nhìn theo không nói nên lời! | `WS · High · Pull-out` theo `Zor-7` vút lên cao | *"\"Cảm ơn hàng xóm nhé, tôi bay về hành tinh đây!\""* |

---

### ✋ Chờ Bạn Duyệt Production Bible Này Trước Khi Chạy Dựng 3D Blender (`Stage R4`)
Mình đã lưu bản đầy đủ vào [script_breakdown.md](file:///d:/Project/Sven/output/alien_blackout/script_breakdown.md).
Bạn xem 4 phần (**Địa điểm – Thời gian – 4 Nhân vật + Mèo – 7 Đạo cụ – Chi tiết hành động 21 Beat**) đã rõ ràng, đúng ý bạn chưa?
- Nếu cần đổi tên nhân vật, sửa quần áo/kiểu tóc, thêm/bớt đạo cụ hay đổi hành động ở Beat nào, bạn nhắn ngay.
- Nếu đã chuẩn hết, nhắn **`OK dựng 3D`** để mình tiến hành dựng 3D trong Blender Cycles (`real_outdoor`), chạy audit không xuyên vật thể và xuất **Preview Check Sheet** từng cảnh cho bạn duyệt trước khi render full 30fps!

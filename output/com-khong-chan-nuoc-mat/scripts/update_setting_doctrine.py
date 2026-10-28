"""
Update setting.html to comply with Sven Creative Doctrine §8.11, §8.12 and 4-Act Architecture.
- Section 4: Refactor generic 10-scene template to Format B Serialized Episodic Engine.
- Section 5A: Replace 20-episode sitcom formula with true 4-Act Continuous Escalation Ladder.
- Section 5B: Update Episode 1 scene breakdown to match Act 1 Pilot standard (no rushed reconciliation).
"""
import os
import re

SETTING_PATH = r"d:\Project\Sven\output\com-khong-chan-nuoc-mat\setting.html"

with open(SETTING_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Section 4 text and scene cards
sec4_old_pattern = r'(<section id="structure-10s">.*?)(<section id="roadmap">)'
sec4_match = re.search(sec4_old_pattern, html, re.DOTALL)
assert sec4_match, "Section 4 not matched"

new_sec4 = '''<section id="structure-10s">
      <div class="section-header">
        <h2 class="section-title"><span>⏱️</span> 4. Cấu Trúc Bắt Buộc: Chuẩn Single-Shot Liên Tục 100% (Unbroken 10s Take) & Động Cơ Phim Bộ (Format B)</h2>
      </div>
      <p style="font-size: 14.5px; color: #E2E8F0; margin-bottom: 20px;">
        Khóa chặt quy chuẩn kỹ thuật: <strong>100% Cú Máy Đơn Liền Mạch Dài Đúng 10.0 Giây (Unbroken Single-Shot Master Take)</strong>. Tuyệt đối cấm cắt cảnh giữa chừng (Zero Mid-Scene Cuts) trong từng cảnh 10s. Trong phim bộ nhiều tập (Format B), mỗi tập là một <strong>chương kịch tính không khép kín</strong> (Act-Bound Chapter), tuân thủ định luật <em>Anti-Sitcom / Anti-Vignette Continuum Law</em> — không giải tỏa cảm xúc sớm ở Hồi 1 & Hồi 2:
      </p>

      <div class="scene-grid-90s">
        <!-- Cảnh 1 -->
        <div class="scene-card-10s">
          <span class="scene-time-badge">Cảnh 1 · 00s – 10s (10s)</span>
          <h4>Disruptive Hook / Handoff</h4>
          <p>Kế thừa trực tiếp đà động lực học từ tập trước hoặc mở màn bằng cú sốc thị giác / nghịch lý con người nhức nhối trong 3 giây đầu.</p>
        </div>

        <!-- Cảnh 2 -->
        <div class="scene-card-10s">
          <span class="scene-time-badge">Cảnh 2 · 10s – 20s (10s)</span>
          <h4>Kinetic Momentum & Confrontation</h4>
          <p>Kế thừa đà chuyển động từ Cảnh 1, thế lực đối lập ập vào chiếm lĩnh không gian, đẩy mức cược kịch tính lên cao.</p>
        </div>

        <!-- Cảnh 3 -->
        <div class="scene-card-10s">
          <span class="scene-time-badge">Cảnh 3 · 20s – 30s (10s)</span>
          <h4>Ideological Collision & Subtext</h4>
          <p>Va chạm hệ tư tưởng qua hành động vật lý cụ thể (giằng co đạo cụ); đối thoại mang tầng nghĩa ngầm (Subtext), né tránh đòn trực diện.</p>
        </div>

        <!-- Cảnh 4 -->
        <div class="scene-card-10s">
          <span class="scene-time-badge">Cảnh 4 · 30s – 40s (10s)</span>
          <h4>Tactile Prop Fracture / Sealed Exits</h4>
          <p>Hành động va chạm làm tổn hại đạo cụ hoặc bịt kín đường lùi; cơ thể phản bội ý chí, bộc lộ sự bất lực sâu sắc.</p>
        </div>

        <!-- Cảnh 5 -->
        <div class="scene-card-10s">
          <span class="scene-time-badge">Cảnh 5 · 40s – 50s (10s)</span>
          <h4>Micro-Crisis Peak (Cực Hạn Tập)</h4>
          <p>Điểm bùng nổ xung đột lớn nhất trong tập: Sự thật bị xé rách, che giấu thất bại, nỗi đau thể xác chạm đỉnh điểm.</p>
        </div>

        <!-- Cảnh 6 -->
        <div class="scene-card-10s">
          <span class="scene-time-badge">Cảnh 6 · 50s – 60s (10s)</span>
          <h4>Subtext Shock & Stunned Reaction</h4>
          <p>Phản ứng bàng hoàng nghẹn đắng trước sự thật vừa lộ diện; nhân vật tự ái hoặc tổn thương, phòng vệ tâm lý cứng rắn hơn.</p>
        </div>

        <!-- Cảnh 7 -->
        <div class="scene-card-10s">
          <span class="scene-time-badge">Cảnh 7 · 60s – 70s (10s)</span>
          <h4>Flawed Defense & Deepening Divide</h4>
          <p>Nỗ lực tự vệ bằng thói quen cũ khiến vết nứt trầm trọng hơn; từ chối sự giúp đỡ hoặc hiểu lầm đào sâu khoảng cách.</p>
        </div>

        <!-- Cảnh 8 -->
        <div class="scene-card-10s">
          <span class="scene-time-badge">Cảnh 8 · 70s – 80s (10s)</span>
          <h4>Point of No Return (Lằn Ranh Đứt Gãy)</h4>
          <p>Hành động dứt khoát xác nhận sự rạn nứt; chiếc khiên kiêu ngạo siết chặt; sự bất lực của nhân vật trung gian (Khang).</p>
        </div>

        <!-- Cảnh 9 -->
        <div class="scene-card-10s">
          <span class="scene-time-badge">Cảnh 9 · 80s – 90s (10s)</span>
          <h4>Simmering Dread & Living Settle</h4>
          <p>Khoảng lặng nặng nề trước cơn bão; không gian đông cứng trong sự xa cách; nhịp thở nghẹn uất handed qua cảnh cuối.</p>
        </div>

        <!-- Cảnh 10 -->
        <div class="scene-card-10s">
          <span class="scene-time-badge">Cảnh 10 · 90s – 100s (10s)</span>
          <h4>Cold Water Slap & Cliffhanger</h4>
          <p>Gáo nước lạnh chấn động do nhân tố cài cắm gây ra (Dì Tám xông vào, đơn ly hôn, tin cấp cứu) — đóng tập ở thế kẹt bế tắc ép xem tập sau!</p>
        </div>
      </div>
    </section>

    '''

# 2. Update Section 5 Roadmap (Master Table 20 Episodes + Section 5B Scene-Level Table)
new_sec5 = '''<section id="roadmap">
      <div class="section-header">
        <h2 class="section-title"><span>📜</span> 5. Lộ Trình Tuyển Chọn 20 Tập Phim (10 Cảnh x 10s = 100s / Tập - Tổng 200 Cảnh)</h2>
      </div>
      <p style="font-size: 13.5px; color: var(--muted); margin-bottom: 18px;">
        Áp dụng chuẩn <strong>Format B: Multi-Episode Series</strong> (Creative Doctrine §8.12 & workflow.md §7.3). Toàn bộ 20 tập là một <strong>Chuỗi Leo Thang Bất Khả Nghịch 4 Hồi</strong> (20% / 45% / 25% / 10%). Tuyệt đối không có hòa giải sớm ở Hồi 1 & Hồi 2; Catharsis và Chuyển hóa Đạo cụ (Echo Rebirth) chỉ xuất hiện trọn vẹn ở Hồi 4:
      </p>
      <table class="ep-table">
        <thead>
          <tr>
            <th style="width: 55px; text-align: center;">Tập</th>
            <th style="width: 75px; text-align: center;">Hồi</th>
            <th style="width: 210px;">Tên Tập & Hook Kịch Tính (00-10s)</th>
            <th style="width: 170px;">Tuyến Nhân Vật & Đạo Cụ</th>
            <th>Xung Đột & Bước Ngoặt Bất Khả Nghịch</th>
            <th>Hậu Quả & Gáo Nước Lạnh (Cold Water Cliffhanger)</th>
            <th style="width: 130px; text-align: center;">Điểm Chạm PR</th>
          </tr>
        </thead>
        <tbody>
          <!-- HỒI 1: TẬP 1 - 4 (SETUP & CẠM BẪY BẤT KHẢ NGHỊCH · 20%) -->
          <tr>
            <td style="text-align: center;"><strong>Tập 1</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-1">Hồi 1</span></td>
            <td><strong>Bát Cháo Ở Cữ Nguội Ngắt</strong><br><span style="font-size:11px; color:var(--rose);">The Inciting Trap</span></td>
            <td style="font-size: 12px; color: var(--muted);">Mỹ Duyên, Minh Khang, Má Ba, Dì Tám · <em>Bát cháo nguội, võng xếp, bình sữa 0ml</em></td>
            <td style="font-size: 13px;">Duyên kiệt sức sau sinh mất sữa, nước mắt rơi làm nứt màng cháo nguội. Má Ba xách khung võng inox vào phòng cữ áp đặt nếp xưa. Duyên gượng dậy cản thì ngã quỵ bên nôi; Má Ba lao tới đỡ làm tuột tay áo để lộ vết bầm kim truyền dịch tím tái.</td>
            <td style="font-size: 13px;">Má Ba không ôm khóc mà sững sờ nghẹn đắng: <em>"Mầy giấu tao đi truyền nước biển... mầy coi tao là người ngoài trong nhà này hả Duyên?!"</em>. Dì Tám xộc vào đập cổng châm dầu vào lửa $\\rightarrow$ Cắt đen bế tắc.</td>
            <td style="text-align: center;"><span class="tag-pr">Nỗi Đau Trầm Cảm</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 2</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-1">Hồi 1</span></td>
            <td><strong>Chiếc Võng Sắt & Tiếng Cười Mỉa Đầu Hẻm</strong><br><span style="font-size:11px; color:var(--cyan);">Neighbor Poison</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Dì Tám, Khang, Duyên · <em>Võng xếp inox, can rượu gừng</em></td>
            <td style="font-size: 13px;">Dì Tám xúi bẩy: <em>"Dâu Sài Gòn khinh mẹ chồng nhà quê, mày hổng dạy nó leo lên đầu mày ngồi!"</em>. Má Ba tự ái sôi sục, xách tô canh chân giò hầm mắm nhĩ ép Duyên ăn cho bằng được. Duyên nhìn tô mỡ ngấy buồn nôn, Khang bênh vợ giành lấy ăn giùm.</td>
            <td style="font-size: 13px;">Má Ba đập bàn rớt đôi đũa: <em>"Tổ cha mầy, đội vợ lên đầu, để coi vợ mầy nuôi cháu tao ra cái giống gì!"</em>. Vết nứt giữa mẹ chồng - nàng dâu chính thức biến thành chiến tranh lạnh.</td>
            <td style="text-align: center;">—</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 3</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-1">Hồi 1</span></td>
            <td><strong>Chiếc Cân Nhơn Hòa & Cơn Sốt Nửa Đêm</strong><br><span style="font-size:11px; color:var(--cyan);">Flawed Defense</span></td>
            <td style="font-size: 12px; color: var(--muted);">Dì Tám, Má Ba, Duyên, Khang, Bé Tin · <em>Chiếc cân Nhơn Hòa, chén nước cơm</em></td>
            <td style="font-size: 13px;">Dì Tám đặt cái cân Nhơn Hòa đập uỳnh xuống bàn mỉa mai: <em>"5 tháng 6 kí lô, mẹ ăn hết phần con!"</em>. Má Ba xấu hổ với xóm giềng, lén quấy nước cơm đặc nêm đường đút cho bé Tin để cháu "chắc dạ". Duyên bắt gặp hoảng hốt giật lại.</td>
            <td style="font-size: 13px;">01:00 đêm, bé Tin sốt cao co giật nhẹ, nôn ộc dính đầy ngực áo Duyên. Khang hốt hoảng mở cửa xe cấp cứu giữa cơn mưa rào Sài Gòn.</td>
            <td style="text-align: center;"><span class="tag-pr">Áp Lực Cân Nặng</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 4</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-1">Hồi 1</span></td>
            <td><strong>Lằn Ranh Bệnh Viện & Bức Tường Im Lặng</strong><br><span style="font-size:11px; color:var(--rose);">Act 1 Climax</span></td>
            <td style="font-size: 12px; color: var(--muted);">Duyên, Bác sĩ, Má Ba, Khang, Bé Tin · <em>Bệnh viện Nhi Đồng, hồ sơ bệnh án</em></td>
            <td style="font-size: 13px;">Bác sĩ cảnh báo hội chứng nhiễm khuẩn đường ruột cấp do ăn dặm thô sớm và đường muối quá tải. Duyên như hóa đá, quay sang nhìn mẹ chồng với ánh mắt căm hờn lạnh buốt; Má Ba run rẩy định chạm vào cháu thì bị Duyên gạt tay ra: <em>"Má đừng đụng vô con con nữa!"</em>.</td>
            <td style="font-size: 13px;">Má Ba đứng chôn chân giữa hành lang trắng toát, nước mắt già nua rơi xuống đôi bàn tay thô ráp. Lằn ranh chia rẽ chính thức không thể đảo ngược.</td>
            <td style="text-align: center;"><span class="tag-pr">Cảnh Báo Nhiễm Khuẩn</span></td>
          </tr>

          <!-- HỒI 2: TẬP 5 - 13 (LEO THANG XUNG ĐỘT & MIDPOINT TWIST · 45%) -->
          <tr>
            <td style="text-align: center;"><strong>Tập 5</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-2">Hồi 2</span></td>
            <td><strong>Bát Canh Bồ Ngót Bị Bỏ Quên</strong><br><span style="font-size:11px; color:var(--gold);">The Silent Cold War</span></td>
            <td style="font-size: 12px; color: var(--muted);">Duyên, Má Ba, Khang · <em>Cửa phòng đóng kín, bát canh bồ ngót nguội</em></td>
            <td style="font-size: 13px;">Duyên bế con xuất viện về nhà, bế thẳng vào phòng khóa chặt cửa then cài. Má Ba lặng lẽ nấu bát canh bồ ngót nóng đặt trước cửa phòng; Duyên kiệt quệ ngồi ôm con bên trong, để bát canh nguội ngắt đóng váng ngoài hành lang không đụng đến.</td>
            <td style="font-size: 13px;">Má Ba lên lấy bát canh, thấy còn nguyên vẹn, cắn môi không khóc nhưng bàn tay run lẩy bẩy làm rớt vỡ chiếc đĩa lót gốm sứ.</td>
            <td style="text-align: center;">—</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 6</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-2">Hồi 2</span></td>
            <td><strong>Cuộc Chiến Chiếc Ghế Ăn Dặm</strong><br><span style="font-size:11px; color:var(--gold);">Battle of Will</span></td>
            <td style="font-size: 12px; color: var(--muted);">Duyên, Má Ba, Bé Tin, Khang · <em>Ghế ăn dặm, chén cháo yến mạch đổ</em></td>
            <td style="font-size: 13px;">Duyên kiên trì đặt bé Tin vào ghế ăn dặm; bé ngậm chặt miệng, quay mặt đi quấy khóc. Má Ba xót cháu lao vào giật bé ra: <em>"Mày hành hạ cháu tao hả, để tao bế đi ăn rong!"</em>. Duyên chặn cửa: <em>"Con đang tập cho con con tự lập!"</em>.</td>
            <td style="font-size: 13px;">Giằng co làm chén cháo văng tung tóe lên sàn nhà; bé Tin khóc thét lạc giọng, Má Ba ôm cháu lùi lại: <em>"Mày độc ác vừa thôi Duyên!"</em>.</td>
            <td style="text-align: center;"><span class="tag-pr">Nỗi Đau Ăn Rong</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 7</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-2">Hồi 2</span></td>
            <td><strong>Tiếng Xì Xào Đầu Hẻm</strong><br><span style="font-size:11px; color:var(--gold);">Community Judgment</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Dì Tám, Chị Diễm, Duyên · <em>Quán tạp hóa, điện thoại rỉ tai</em></td>
            <td style="font-size: 13px;">Má Ba ra quán tạp hóa đầu hẻm, Dì Tám và chòm xóm xì xào: <em>"Dâu nó cấm bà Ba bế cháu, đuổi bà ra khỏi phòng ngủ kìa!"</em>. Má Ba nuốt nghẹn đắng cúi gằm mặt bước nhanh về nhà.</td>
            <td style="font-size: 13px;">Má Ba về đến hiên nhà, thấy Duyên đang khóc trong điện thoại với mẹ ruột ở quê: <em>"Con mệt mỏi quá má ơi, chắc con bế cháu về quê..."</em>. Má Ba chết lặng sau bức tường.</td>
            <td style="text-align: center;">—</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 8</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-2">Hồi 2</span></td>
            <td><strong>Cú Trượt Chân Lúc Tinh Mơ</strong><br><span style="font-size:11px; color:var(--gold);">Hidden Sacrifice</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Khang, Duyên · <em>Bậc thềm bếp ướt, mớ tép đồng rớt</em></td>
            <td style="font-size: 13px;">04:30 sáng trời mưa lất phất, Má Ba lọ mọ đi chợ đầu mối mua mớ tép đồng tươi nấu cháo cho cháu. Bậc thềm trơn trượt, Má Ba ngã nhào, đầu gối dập tím rách da rớm máu; nhưng bà vội kéo ống quần che lại, gượng dậy rửa tép.</td>
            <td style="font-size: 13px;">Duyên bước xuống bếp thấy Má Ba đi cà nhắc nhưng lạnh lùng quay đi; Khang cúi xuống phát hiện vệt máu trên bậc thềm bếp, lòng quặn thắt.</td>
            <td style="text-align: center;">—</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 9</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-2">Hồi 2</span></td>
            <td><strong>Ống Kính Của Út Huy</strong><br><span style="font-size:11px; color:var(--gold);">Observer's Mirror</span></td>
            <td style="font-size: 12px; color: var(--muted);">Út Huy, Khang, Má Ba, Duyên · <em>Điện thoại quay phim, video clip lén</em></td>
            <td style="font-size: 13px;">Út Huy cầm điện thoại vô tình quay lại được: Cảnh Duyên một mình thức trắng đêm ôm ngực khóc nức nở vì tắc sữa, và cảnh Má Ba ngồi ở chân cầu thang đếm từng tiếng thở dài của con dâu mà không dám gõ cửa.</td>
            <td style="font-size: 13px;">Út Huy cho Khang xem clip; Khang gục đầu vào vai em trai bật khóc: <em>"Nhà mình nát thiệt rồi Huy ơi..."</em>.</td>
            <td style="text-align: center;"><span class="tag-pr">Tấm Gương Cảm Xúc</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 10</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-2">Hồi 2</span></td>
            <td><strong>Khang Quỳ Dưới Mưa</strong><br><span style="font-size:11px; color:var(--gold);">Breaking Pillar</span></td>
            <td style="font-size: 12px; color: var(--muted);">Khang, Má Ba, Duyên · <em>Phòng khách tối, mưa giông xối xả</em></td>
            <td style="font-size: 13px;">Khang đi làm về kiệt quệ áp lực viện phí và công việc, quỳ sụp xuống giữa phòng khách trước mặt mẹ và vợ: <em>"Má ơi... Duyên ơi... con lạy má, con lạy vợ... hai người giết con đi chứ đừng xé nát cái nhà này nữa!"</em>.</td>
            <td style="font-size: 13px;">Cả phòng khách im phăng phắc như tờ. Má Ba quay mặt vào tường, Duyên ôm con siết chặt; không ai bước tới đỡ Khang dậy.</td>
            <td style="text-align: center;">—</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 11</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-2">Hồi 2</span></td>
            <td><strong>MIDPOINT TWIST: CHIẾC GIỎ ĐỆM CỦA MÁ BA</strong><br><span style="font-size:11px; color:var(--rose);">50% Midpoint Twist</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Khang, Duyên, Bé Tin · <em>Chiếc giỏ đệm cũ, xe đò Bến Tre, chuông điện thoại</em></td>
            <td style="font-size: 13px;">Má Ba gom đồ vào giỏ đệm bỏ về quê vì thấy mình thừa thãi. Khang níu áo má bị gạt tay. Nhưng xe đò vừa lăn bánh ra bến thì điện thoại reo dồn dập: Tiếng Khang gào khóc: <em>"Má ơi quay lại cứu thằng Tin... nó sốt co giật tím tái rồi má ơi!"</em>.</td>
            <td style="font-size: 13px;">Má Ba quăng giỏ đệm giữa bến xe, lao thục mạng ngược về bệnh viện giữa cơn mưa xối xả. Đỉnh điểm đảo chiều toàn bộ cục diện series.</td>
            <td style="text-align: center;"><span class="tag-pr">Cú Lật Giữa Phim</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 12</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-2">Hồi 2</span></td>
            <td><strong>Sự Thật Tại Phòng Xét Nghiệm</strong><br><span style="font-size:11px; color:var(--gold);">Diagnostic Truth</span></td>
            <td style="font-size: 12px; color: var(--muted);">Bác sĩ Nhi, Má Ba, Duyên, Bé Thư, Bé Tin · <em>Kết quả xét nghiệm máu vi chất</em></td>
            <td style="font-size: 13px;">Bác sĩ công bố kết quả: Bé Tin biếng ăn do <strong>thiếu hụt vi chất Kẽm & Lysine sinh lý sau đợt viêm ruột</strong>, teo gai vị giác gây chán ăn bệnh lý, hoàn toàn không phải do mẹ thiếu sữa hay bà chăm vụng.</td>
            <td style="font-size: 13px;">Bác sĩ cảnh báo: Càng ép ăn càng làm bé sang chấn tâm lý. Má Ba và Duyên ngồi cạnh nhau, bàng hoàng nhận ra bấy lâu nay họ đã giày vò nhau vô lý.</td>
            <td style="text-align: center;"><span class="tag-pr">Khoa Học Vi Chất</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 13</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-2">Hồi 2</span></td>
            <td><strong>Hộp Siro Màu Xanh Ngọc</strong><br><span style="font-size:11px; color:var(--gold);">Seed of Hope</span></td>
            <td style="font-size: 12px; color: var(--muted);">Bé Thư, Duyên, Má Ba, Dì Tám · <em>Hộp siro Japa Kids xanh ngọc, tem Bộ Y Tế</em></td>
            <td style="font-size: 13px;">Bé Thư mang hộp siro vi chất Japa Kids do bác sĩ khuyên dùng về. Duyên muốn cho con uống, nhưng Má Ba vẫn rụt rè sợ thuốc tây hại thận. Dì Tám đứng ngoài cửa hóng chuyện nhảy vào xúi: <em>"Thuốc kích ăn đó, uống vô mục xương!"</em>.</td>
            <td style="font-size: 13px;">Má Ba giằng lấy hộp siro cất vào tủ khóa lại: <em>"Để tao hỏi cho kỹ, hổng ai được cho cháu tao uống bậy!"</em>.</td>
            <td style="text-align: center;"><span class="tag-pr">Khóa Định Kiến</span></td>
          </tr>

          <!-- HỒI 3: TẬP 14 - 18 (CAO TRÀO, SỤP ĐỔ BẢN NGÃ & THỨC TỈNH · 25%) -->
          <tr>
            <td style="text-align: center;"><strong>Tập 14</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-3">Hồi 3</span></td>
            <td><strong>Lọ Siro Rơi Vỡ</strong><br><span style="font-size:11px; color:var(--rose);">All Hope Is Lost</span></td>
            <td style="font-size: 12px; color: var(--muted);">Dì Tám, Má Ba, Duyên, Khang · <em>Chai siro vỡ trên sàn gạch bông</em></td>
            <td style="font-size: 13px;">Dì Tám sang nhà xúi giục giằng lấy chai siro kiểm tra; trong lúc xô đẩy, chai siro rớt xuống nền gạch vỡ toang, dòng siro vàng óng chảy lênh láng. Duyên gào lên trong uất nghẹn: <em>"Má tin người ngoài hơn tin con đúng không?!"</em>.</td>
            <td style="font-size: 13px;">Khang nổi giận chỉ tay đuổi Dì Tám ra khỏi nhà: <em>"Bà cút khỏi nhà tôi ngay!"</em>. Đáy sâu tuyệt vọng và sự đổ vỡ chạm cực hạn 10/10.</td>
            <td style="text-align: center;"><span class="tag-pr">Chạm Đáy Đổ Vỡ</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 15</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-3">Hồi 3</span></td>
            <td><strong>Lời Trần Tình Của Chị Diễm Tạp Hóa</strong><br><span style="font-size:11px; color:var(--rose);">Unbiased Proof</span></td>
            <td style="font-size: 12px; color: var(--muted);">Chị Diễm, Ba Bảy, Má Ba, Bé Thư · <em>Hồ sơ kiểm nghiệm GMP, bé Bo chạy nhảy</em></td>
            <td style="font-size: 13px;">Chị Diễm tạp hóa dắt con trai chạy sang: Kể chuyện con chị hồi xưa biếng ăn còi cọc, nhờ bổ sung đúng Kẽm Gluconat & Lysine từ Nhật Bản trong Japa Kids mà nay khỏe mạnh. Ba Bảy quát lớn răn đe hủ tục xóm hẻm.</td>
            <td style="font-size: 13px;">Má Ba nhìn giấy chứng nhận Bộ Y Tế và nhìn bé Bo phổng phao, đôi bàn tay run rẩy sờ ngực áo, chiếc khiên gia trưởng bắt đầu sụp đổ.</td>
            <td style="text-align: center;"><span class="tag-pr">Minh Bạch Kiểm Nghiệm</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 16</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-3">Hồi 3</span></td>
            <td><strong>Giọt Siro Lúc 2 Giờ Sáng</strong><br><span style="font-size:11px; color:var(--rose);">Secret Awakening</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Bé Tin, Duyên (sau rèm) · <em>Cốc đong 5ml, ánh đèn ngủ 3000K</em></td>
            <td style="font-size: 13px;">02:00 đêm, Má Ba lọ mọ cầm chai siro mới Khang mua về, rót đúng 5ml, nếm thử: Vị dưa lưới thơm dịu, thanh mát. Bà nghẹn ngào đưa cốc vào khóe môi bé Tin; bé mút chùn chụt rồi cười trong mơ.</td>
            <td style="font-size: 13px;">Duyên đứng sau rèm cửa nhìn thấy hết, đưa tay che miệng khóc không thành tiếng vì cảm động.</td>
            <td style="text-align: center;"><span class="tag-pr">Khoảnh Khắc Cảm Xúc</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 17</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-3">Hồi 3</span></td>
            <td><strong>ĐẠI CAO TRÀO: EGO DEATH CỦA MÁ BA</strong><br><span style="font-size:11px; color:var(--rose);">Ego Death</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Duyên, Khang, Bé Tin · <em>Bát cháo loãng, muỗng sứ rơi trên mâm</em></td>
            <td style="font-size: 13px;">Sáng hôm sau, bé Tin tự giác há miệng đòi ăn thìa cháo đầu tiên. Má Ba sụp đổ bản ngã kiêu ngạo, quỳ sụp xuống nắm tay con dâu khóc nức nở: <em>"Duyên ơi... má có tội với con... má cứ tưởng thương cháu là ép cháu, má làm khổ con rồi con ơi!"</em>.</td>
            <td style="font-size: 13px;">Căn phòng chìm trong sự chấn động; 17 tập đè nén vỡ òa thành tiếng khóc ăn năn chân thành của người mẹ già.</td>
            <td style="text-align: center;"><span class="tag-pr">Đỉnh Điểm Thức Tỉnh</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 18</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-3">Hồi 3</span></td>
            <td><strong>Sự Tha Thứ Khoan Dung Của Duyên</strong><br><span style="font-size:11px; color:var(--emerald);">Stunned Mercy PEAK 10/10</span></td>
            <td style="font-size: 12px; color: var(--muted);">Duyên, Má Ba, Khang, Bé Tin · <em>Đôi bàn tay chai sần, ánh ban mai</em></td>
            <td style="font-size: 13px;">Duyên vội quỳ xuống ôm má chồng: <em>"Má đừng nói vậy... con cũng sai vì đã không mở lòng... Từ nay má dạy con làm mẹ nghen má!"</em>. Khang bước tới ôm trọn hai người phụ nữ vào lòng.</td>
            <td style="font-size: 13px;">Ba thế hệ ôm nhau rơi nước mắt trong ánh nắng ban mai ấm áp; mọi hận thù, định kiến tan biến hoàn toàn.</td>
            <td style="text-align: center;"><span class="tag-pr">Hòa Giải Triệt Để</span></td>
          </tr>

          <!-- HỒI 4: TẬP 19 - 20 (HÒA GIẢI, CATHARSIS & TÁI SINH TRẬT TỰ MỚI · 10%) -->
          <tr>
            <td style="text-align: center;"><strong>Tập 19</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-4">Hồi 4</span></td>
            <td><strong>Bữa Cơm Không Chan Nước Mắt</strong><br><span style="font-size:11px; color:var(--emerald);">Echo Prop Rebirth</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Duyên, Dì Tám, Khang, Bé Tin · <em>Võng inox ngoài hiên, mâm cơm đầm ấm</em></td>
            <td style="font-size: 13px;">Chiếc võng inox ngày nào nay được Khang dựng ngoài hiên hóng mát ru cháu; bé Tin ngồi ghế dặm tự xúc ăn trong 20 phút. Dì Tám sang nhà cúi đầu xin lỗi và học cách chăm cháu văn minh.</td>
            <td style="font-size: 13px;">Má Ba cười xòa bưng bát canh bồ ngót chia đều cho cả nhà: <em>"Cơm nhà mình từ nay chỉ chan tình thương, hổng chan nước mắt nữa!"</em>.</td>
            <td style="text-align: center;"><span class="tag-pr">Đổi Cực Ân Sủng</span></td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Tập 20</strong></td>
            <td style="text-align: center;"><span class="tag-act tag-act-4">Hồi 4</span></td>
            <td><strong>Đại Đoàn Viên Rặng Dừa Bến Tre</strong><br><span style="font-size:11px; color:var(--emerald);">Closing Image Echo</span></td>
            <td style="font-size: 12px; color: var(--muted);">Đại gia đình 3 thế hệ hai bên Nội - Ngoại · <em>Rặng dừa Bến Tre, chõng tre sum vầy</em></td>
            <td style="font-size: 13px;">Con đò rẽ sóng đưa cả nhà về quê ngoại Bến Tre sum vầy. Má Ba và Má Tư ngồi bên chõng tre cười rạng rỡ đút cháo cho cháu; Ba Bảy và Ba Bốn đối ẩm chén rượu sen ân tình.</td>
            <td style="font-size: 13px;">Closing Image: Ánh mắt lấp lánh hạnh phúc của Duyên nhìn con trai chạy tung tăng trên sân gạch đỏ dưới nắng sớm Bến Tre — đối xứng tuyệt đối với giọt nước mắt khổ đau ở Cảnh 1 Tập 1.</td>
            <td style="text-align: center;"><span class="tag-pr">Đại Kết Viên Mãn</span></td>
          </tr>
        </tbody>
      </table>

      <!-- SECTION 5B: EPISODE 1 SCENE-LEVEL ROADMAP (Phase B, workflow.md §8.5) -->
      <div id="ep1-phase-b" style="margin-top: 28px;">
        <h3 class="section-title" style="font-size: 18px;"><span>🎬</span> 5B. Tập 1 — Lộ Trình Cấp Cảnh (Phase B · 10 Cảnh x 10s = 100s · Act 1 Pilot)</h3>
        <p style="font-size: 12px; color: var(--muted);">SSOT cho Stage 4: lời thoại khớp nguyên văn với tap-1.html. Tuyệt đối không có hòa giải sớm (Act 1 duty: Thiết lập cạm bẫy & Vết rạn nứt không thể quay đầu).</p>
        <table class="ep-table">
          <thead>
            <tr>
              <th style="width: 70px; text-align: center;">Cảnh</th>
              <th style="width: 150px;">Beat · Track</th>
              <th style="width: 170px;">Cast · Bối cảnh · Đạo cụ</th>
              <th>Intent Card (Want · Shift · Subtext · Gap)</th>
              <th>Voice Mode · Lời thoại</th>
              <th style="width: 170px;">Kinetic Bridge</th>
            </tr>
          </thead>
          <tbody>
          <tr>
            <td style="text-align: center;"><strong>Cảnh 01</strong><br><span style="font-size: 11px; color: var(--muted);">00:00–00:10</span></td>
            <td style="font-size: 12px;">B1 Hook<br><span style="color: var(--muted);">Track A · Single-Shot Continuous Take</span></td>
            <td style="font-size: 12px; color: var(--muted);">Duyên, Khang, Bé Tin · phòng cữ · bát cháo, bình hút sữa 0ml, mâm nhôm</td>
            <td style="font-size: 12px;"><strong>Want:</strong> Duyên → được đỡ mà không phải than; Khang → giữ vợ đứng vững<br><strong>Shift:</strong> gồng nén → vỡ òa<br><strong>Subtext:</strong> "Em bất lực, em làm mẹ dở quá"<br><strong>Gap:</strong> Hồi hộp: Khán giả thấy băng keo truyền dịch, nhà chồng chưa ai biết</td>
            <td style="font-size: 12px;"><em>Solo + người nghe im lặng</em><br><strong>Mỹ Duyên</strong> [00:04.2 – 00:06.7]: “Anh ơi... em kiệt sức rồi, sữa hổng chịu về...”</td>
            <td style="font-size: 12px; color: var(--muted);">The bedroom door suddenly swings open in Scene 02 as heavy footsteps approach.</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Cảnh 02</strong><br><span style="font-size: 11px; color: var(--muted);">00:10–00:20</span></td>
            <td style="font-size: 12px;">B2 Setup<br><span style="color: var(--muted);">Track B · Multi-Shot (1 Cut · 180° Axis)</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Khang, Duyên, Bé Tin · cửa phòng cữ · khung võng xếp inox</td>
            <td style="font-size: 12px;"><strong>Want:</strong> Má Ba → giành quyền chăm cháu bằng nếp xưa; Khang → che chắn vợ<br><strong>Shift:</strong> riêng tư → bị xâm lăng<br><strong>Subtext:</strong> Má Ba bất an vì thấy con dâu không theo ý mình<br><strong>Gap:</strong> Kịch tính trớ trêu: Tình thương độc đoán biến thành sự xâm lấn</td>
            <td style="font-size: 12px;"><em>Đối thoại — hai mong muốn va nhau</em><br><strong>Má Ba</strong> [00:10.8 – 00:14.0]: “Trời đất! Thằng Tin khóc thấu trời... nuôi cháu tao kiểu Tây hả?!”<br><strong>Minh Khang</strong> [00:16.2 – 00:18.7]: “Má nhỏ tiếng giùm con... Duyên kiệt sức ba đêm rồi!”</td>
            <td style="font-size: 12px; color: var(--muted);">ma_ba takes two heavy steps forward into the room in Scene 03.</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Cảnh 03</strong><br><span style="font-size: 11px; color: var(--muted);">00:20–00:30</span></td>
            <td style="font-size: 12px;">B3 Drama<br><span style="color: var(--muted);">Track AB · Hybrid (Take + 1 Cut · 180° Axis)</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Khang, Duyên, Bé Tin · giữa phòng · võng xếp inox, nôi gỗ</td>
            <td style="font-size: 12px;"><strong>Want:</strong> Má Ba → đòi chỗ đứng bằng ký ức; Khang → từ chối mà không làm má đau<br><strong>Shift:</strong> chắc chắn → khựng lại tức tối<br><strong>Subtext:</strong> Má Ba sợ bị coi thường, sợ thành người thừa<br><strong>Gap:</strong> Bí ẩn: Vết sẹo kim cũ trên cổ tay Má, chưa giải thích</td>
            <td style="font-size: 12px;"><em>Đối thoại Track AB — từ chối lịch sự càng gây tự ái</em><br><strong>Má Ba</strong> [00:20.5 – 00:23.7]: “Cái võng này ba bây đưa bây ngủ từ hồi đỏ hỏn đó!”<br><strong>Minh Khang</strong> [00:25.0 – 00:27.7]: “Con nhớ võng của ba... mà thằng Tin phải nằm nôi.”</td>
            <td style="font-size: 12px; color: var(--muted);">my_duyen tries to stand up in Scene 04 but suddenly collapses.</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Cảnh 04</strong><br><span style="font-size: 11px; color: var(--muted);">00:30–00:40</span></td>
            <td style="font-size: 12px;">B3 Drama (exits sealed)<br><span style="color: var(--muted);">Track A · Single-Shot Continuous Take</span></td>
            <td style="font-size: 12px; color: var(--muted);">Duyên, Má Ba, Khang, Bé Tin · bên nôi · bát cháo rơi vỡ</td>
            <td style="font-size: 12px;"><strong>Want:</strong> Duyên → chứng minh mình tự lo được; cơ thể → phản bội sụp đổ<br><strong>Shift:</strong> gượng gạo → quỵ ngã<br><strong>Subtext:</strong> Tiếng kêu cứu nghẹn trong cổ họng<br><strong>Gap:</strong> Đồng cảm: Cú ngã giải phẫu học không kịch tính hóa</td>
            <td style="font-size: 12px;"><em>Solo Má Ba — tiếng hốt hoảng bản năng</em><br><strong>Má Ba</strong> [00:34.3 – 00:37.0]: “Duyên! Duyên ơi, con sao vậy con?! Khang, đỡ vợ mầy mau!”</td>
            <td style="font-size: 12px; color: var(--muted);">minh_khang and ma_ba catch Duyen as her sleeve rolls up in Scene 05.</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Cảnh 05</strong><br><span style="font-size: 11px; color: var(--muted);">00:40–00:50</span></td>
            <td style="font-size: 12px;">B4 Climax (Discovery Twist)<br><span style="color: var(--muted);">Track B · Multi-Shot (1 Cut · 180° Axis)</span></td>
            <td style="font-size: 12px; color: var(--muted);">Khang, Duyên, Má Ba, Bé Tin · sàn phòng cữ · vết bầm kim truyền dịch</td>
            <td style="font-size: 12px;"><strong>Want:</strong> Má Ba → đỡ con dâu; mắt → chạm vết kim tím tái; Duyên → giấu giếm thất bại<br><strong>Shift:</strong> hoảng loạn → bàng hoàng sững sờ<br><strong>Subtext:</strong> Sự thật bóc trần: Duyên kiệt quệ đến mức phải truyền dịch lén lút<br><strong>Gap:</strong> Đổi trạng thái: Từ giấu giếm sang đối mặt trực diện</td>
            <td style="font-size: 12px;"><em>Solo Má Ba — câu hỏi nghẹn đắng</em><br><strong>Má Ba</strong> [00:44.8 – 00:47.8]: “Tay mầy... mầy đi truyền nước biển hồi nào sao hổng nói tao hay?!”</td>
            <td style="font-size: 12px; color: var(--muted);">my_duyen jerks her bruised wrist back defensively in Scene 06.</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Cảnh 06</strong><br><span style="font-size: 11px; color: var(--muted);">00:50–01:00</span></td>
            <td style="font-size: 12px;">B4 Climax (Emotional Fracture)<br><span style="color: var(--muted);">Track A · Single-Shot Continuous Take</span></td>
            <td style="font-size: 12px; color: var(--muted);">Duyên, Má Ba, Khang · giường ngủ</td>
            <td style="font-size: 12px;"><strong>Want:</strong> Duyên → giữ lại chút tự trọng cuối cùng; Má Ba → một lời giải thích<br><strong>Shift:</strong> chịu đựng → cự tuyệt lạnh lùng<br><strong>Subtext:</strong> "Nói ra để má lại mắng con vụng về sao?"<br><strong>Gap:</strong> Đau đớn: Sự im lặng làm tổn thương sâu sắc hơn lời mắng</td>
            <td style="font-size: 12px;"><em>Đối thoại sắc lạnh — không hòa giải</em><br><strong>Mỹ Duyên</strong> [00:51.5 – 00:54.2]: “Con tự lo được... má đừng bận lòng thêm...”<br><strong>Má Ba</strong> [00:55.8 – 00:58.5]: “Mầy nói vậy... là mầy coi tao là người dưng nước lã?!”</td>
            <td style="font-size: 12px; color: var(--muted);">ma_ba backs away toward the door with trembling hands in Scene 07.</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Cảnh 07</strong><br><span style="font-size: 11px; color: var(--muted);">01:00–01:10</span></td>
            <td style="font-size: 12px;">B4 Climax (Escalation of Hurt)<br><span style="color: var(--muted);">Track AB · Hybrid (Take + 1 Cut · 180° Axis)</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Khang, Duyên · cửa phòng cữ · nôi gỗ thông</td>
            <td style="font-size: 12px;"><strong>Want:</strong> Má Ba → giải tỏa cơn tự ái nghẹn ứ; Khang → dập tắt ngọn lửa<br><strong>Shift:</strong> lo lắng → giận dữ phòng vệ<br><strong>Subtext:</strong> Nỗi sợ bị con trai và con dâu gạt ra rìa cuộc sống<br><strong>Gap:</strong> Khang bất lực kẹt giữa hai dòng nước</td>
            <td style="font-size: 12px;"><em>Đối thoại giằng xé</em><br><strong>Má Ba</strong> [01:02.0 – 01:05.2]: “Tao lặn lội lên đây... hổng phải để tụi bây xua đuổi!”<br><strong>Minh Khang</strong> [01:06.5 – 01:09.2]: “Má! Duyên nó đang bệnh, má đừng nói vậy tội nghiệp nó!”</td>
            <td style="font-size: 12px; color: var(--muted);">ma_ba stiffens in bitter silence as Khang shields Duyen in Scene 08.</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Cảnh 08</strong><br><span style="font-size: 11px; color: var(--muted);">01:10–01:20</span></td>
            <td style="font-size: 12px;">B5 Deepening Fracture<br><span style="color: var(--muted);">Track A · Single-Shot Continuous Take</span></td>
            <td style="font-size: 12px; color: var(--muted);">Má Ba, Khang, Duyên · hành lang tầng 2 · khung võng inox chỏng chơ</td>
            <td style="font-size: 12px;"><strong>Want:</strong> Má Ba → một sự nhượng bộ; Khang → bảo vệ sự bình yên mong manh<br><strong>Shift:</strong> gia đình quây quần → rạn nứt đóng băng<br><strong>Subtext:</strong> Chiếc võng xếp chỏng chơ như biểu tượng của sự chối bỏ<br><strong>Gap:</strong> Khoảng cách thế hệ không thể lấp đầy bằng lời dỗ dành</td>
            <td style="font-size: 12px;"><em>Solo Má Ba — nhát dao tự ái</em><br><strong>Má Ba</strong> [01:13.5 – 01:17.2]: “Được rồi... tụi bây khôn rồi, để coi tụi bây nuôi con ra sao!”</td>
            <td style="font-size: 12px; color: var(--muted);">my_duyen buries her face into the baby pillow in Scene 09.</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Cảnh 09</strong><br><span style="font-size: 11px; color: var(--muted);">01:20–01:30</span></td>
            <td style="font-size: 12px;">B5 Simmering Dread<br><span style="color: var(--muted);">Track A · Single-Shot Continuous Take</span></td>
            <td style="font-size: 12px; color: var(--muted);">Duyên, Khang, Bé Tin · giường ngủ · ánh nắng gắt xiên chéo</td>
            <td style="font-size: 12px;"><strong>Want:</strong> Duyên → được thở trong im lặng; Khang → gánh vác nhưng cạn sức<br><strong>Shift:</strong> căng thẳng ồn ào → im lặng ngột ngạt<br><strong>Subtext:</strong> Cơn trầm cảm đang nuốt chửng ngôi nhà<br><strong>Gap:</strong> Không có bài học nào được rút ra, chỉ có bế tắc tích tụ</td>
            <td style="font-size: 12px;"><em>Solo Duyên — tiếng nấc nghẹn giữa phòng</em><br><strong>Mỹ Duyên</strong> [01:24.5 – 01:27.5]: “Em mệt quá Khang ơi... nhà mình hổng thở nổi nữa rồi...”</td>
            <td style="font-size: 12px; color: var(--muted);">Loud, violent knocking suddenly rattles the front iron gate in Scene 10.</td>
          </tr>
          <tr>
            <td style="text-align: center;"><strong>Cảnh 10</strong><br><span style="font-size: 11px; color: var(--muted);">01:30–01:40</span></td>
            <td style="font-size: 12px;">Hook Tập 2 (Cold Water Slap)<br><span style="color: var(--muted);">Track B · Multi-Shot (1 Cut · 180° Axis)</span></td>
            <td style="font-size: 12px; color: var(--muted);">Dì Tám, Má Ba, Khang, Duyên · cửa chính · can rượu gừng</td>
            <td style="font-size: 12px;"><strong>Want:</strong> Dì Tám → can thiệp, phán xét; Má Ba → đồng minh củng cố tự ái<br><strong>Shift:</strong> bế tắc nội bộ → bị người ngoài giáng thêm đòn hiểm<br><strong>Subtext:</strong> Ngòi nổ của bi kịch tập 2 đã được châm ngòi<br><strong>Gap:</strong> Gáo nước lạnh: Khán giả thấy Dì Tám ập vào, drama không lối thoát</td>
            <td style="font-size: 12px;"><em>Đối thoại đập tan hy vọng làm lành</em><br><strong>Dì Tám</strong> [01:31.0 – 01:34.2]: “Bà Ba! Con dâu nó leo lên đầu ngồi mà bà nhịn hả?!”<br><strong>Má Ba</strong> [01:35.5 – 01:38.2]: “Chị Tám... chị vô đây coi cháu tao giùm tao!”</td>
            <td style="font-size: 12px; color: var(--muted);">Directly fuels Episode 2 (Chiếc Võng Sắt &amp; Tiếng Cười Mỉa Đầu Hẻm).</td>
          </tr>
          </tbody>
        </table>
      </div>

    </section>'''

# Perform the replacements
sec4_and_sec5_pattern = r'<section id="structure-10s">.*?</section>\s*<!-- SECTION 5: ROADMAP -->\s*<section id="roadmap">.*?</section>'
match = re.search(sec4_and_sec5_pattern, html, re.DOTALL)
if match:
    full_new = new_sec4 + '\n    <!-- SECTION 5: ROADMAP -->\n    ' + new_sec5
    html = html[:match.start()] + full_new + html[match.end():]
    with open(SETTING_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: setting.html Section 4 and Section 5 updated perfectly!")
else:
    print("ERROR: Regex did not match the combined section pattern.")

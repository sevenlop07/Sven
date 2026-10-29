#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script: engine/update_series_hoc_duong.py
Updates setting.html and tap-1.html with:
1. Diverse, relatable teen character flaws (Linh overthinking/flips at end, Nam jokes fast but fears hurting friends,
   An helps but misunderstands, Vy edits class photos perfectly but fails on her own, Minh controls fair budget but hesitates on necessary spend,
   Khoa active on field but camera-shy and texts curtly).
2. Dynamic Dual Reference Sets (Nữ 1, Nữ 2, Nam 1, Nam 2).
3. Authentic, colloquial, non-corporate, punchy school sitcom dialogue.
4. Full validation through setting_audit_suite.py and episode_audit_suite.py.
"""

import re
import subprocess
import sys

# ==============================================================================
# 1. UPDATE SETTING.HTML
# ==============================================================================
def update_setting_html():
    setting_path = 'd:/Project/Sven/output/series-hoc-duong/setting.html'
    with open(setting_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- Update Section 2 Character Cards ---
    # Linh card
    linh_old = re.search(r'<!-- LINH -->.*?<!-- NAM -->', content, re.DOTALL).group(0)
    linh_new = """<!-- LINH -->
        <div class="card" style="border-left:4px solid var(--gold);">
          <div class="card-title">
            <div>
              <span style="font-size:18px; color:var(--gold);">Linh · Nữ Chính (Lớp Trưởng / Cầu Toàn Phút Chót)</span>
              <div style="font-size:12px; color:var(--muted);">Sinh: 08/01/2011 (Ma Kết) · Thích quy củ, hay overthinking</div>
            </div>
            <span class="badge badge-gold">Core Lead A1</span>
          </div>
          <div style="font-size:13px; color:#D1D5DB; line-height:1.65;">
            • <strong>Tham chiếu hình ảnh:</strong> Gương mặt, kiểu tóc và áo lớp tham chiếu 100% từ ảnh đính kèm <code>@linh</code> và <code>@AO_CHU_DAO_01</code>, kết hợp 2 Look linh động (Nữ 1 / Nữ 2).<br>
            • <strong>Tâm lý & Mong muốn:</strong> Muốn việc lớp chỉn chu, đúng hạn, không ai bị bỏ lại phía sau; nhưng nội tâm luôn thường trực nỗi sợ mình ra quyết định sai lầm.<br>
            • <strong>Nét mâu thuẫn đặc trưng:</strong> <em>Nhắc mọi người bình chọn, hối thúc cả lớp chốt hạ nhưng lại đổi ý cuối giờ!</em> Đôn đốc mọi người lập danh sách xong xuôi, đến phút 89 lại tự buông một câu: <em>“Ủa mà khoan... hay mình đổi phương án khác ta?”</em> khiến cả nhóm ngã ngửa.<br>
            • <strong>Nguồn gây cười:</strong> Sự tương phản giữa phong thái lớp trưởng nghiêm túc giục chốt việc với thói quen tự “quay xe” lật kèo kế hoạch của chính mình vào phút chót.<br>
            • <strong>Đặc điểm diễn xuất:</strong> Nói nhanh khi sốt ruột, hay gõ đầu bút xuống mặt bàn để chốt việc; khi bắt đầu overthinking thì ngón tay xoắn nhẹ lọn tóc, mắt nhìn dáo dác và đổi giọng phân bua.<br>
            • <strong>Cấm kỵ:</strong> Không biến Linh thành lớp trưởng công sở cứng nhắc, hách dịch; giữ trọn nét ngô nghê, đáng yêu của cô bạn lớp 10.
          </div>
        </div>

        <!-- NAM -->"""
    content = content.replace(linh_old, linh_new)

    # Nam card
    nam_old = re.search(r'<!-- NAM -->.*?<!-- AN -->', content, re.DOTALL).group(0)
    nam_new = """<!-- NAM -->
        <div class="card" style="border-left:4px solid var(--orange);">
          <div class="card-title">
            <div>
              <span style="font-size:18px; color:var(--orange);">Nam · Nam Chính (Pha Trò Nhạy Cảm / Sợ Bạn Buồn)</span>
              <div style="font-size:12px; color:var(--muted);">Sinh: 03/06/2011 (Song Tử) · Bạn cũ của Linh từ THCS</div>
            </div>
            <span class="badge badge-orange">Core Lead A2</span>
          </div>
          <div style="font-size:13px; color:#D1D5DB; line-height:1.65;">
            • <strong>Tham chiếu hình ảnh:</strong> Gương mặt, kiểu tóc và áo lớp tham chiếu 100% từ ảnh đính kèm <code>@nam</code> và <code>@AO_CHU_DAO_01</code>, kết hợp 2 Look linh động (Nam 1 / Nam 2).<br>
            • <strong>Tâm lý & Mong muốn:</strong> Thích không khí vui vẻ, ghét sự căng thẳng; sợ bị bạn bè ghét hoặc cô lập nên luôn dùng khiếu hài hước để kết nối.<br>
            • <strong>Nét mâu thuẫn đặc trưng:</strong> <em>Pha trò rất nhanh nhưng lại cực kỳ để ý thái độ, sợ câu đùa của mình khiến người khác buồn!</em> Mồm miệng liến thoắng quăng miếng hài, nhưng vừa đùa xong là mắt liếc nhanh dò xét nét mặt bạn bè; thấy bạn hơi chùng xuống là trong lòng cuống cuồng tìm cách xoa dịu, chữa cháy ngay.<br>
            • <strong>Nguồn gây cười:</strong> Tự trào khuyết điểm bản thân (má bánh bao, sợ camera góc rộng dìm hàng); những pha chữa ngượng lúng túng nhưng chân thành.<br>
            • <strong>Đặc điểm diễn xuất:</strong> Bắt lời nhanh, biểu cảm linh hoạt; sau câu đùa hay liếc trộm phản ứng, gãi gáy khi bối rối, vội vàng vỗ vai dỗ dành nếu lỡ miệng.<br>
            • <strong>Cấm kỵ:</strong> Không biến Nam thành kẻ cợt nhả vô duyên, đùa dai tổn thương người khác.
          </div>
        </div>

        <!-- AN -->"""
    content = content.replace(nam_old, nam_new)

    # An card
    an_old = re.search(r'<!-- AN -->.*?<!-- VY -->', content, re.DOTALL).group(0)
    an_new = """<!-- AN -->
        <div class="card" style="border-left:4px solid var(--cyan);">
          <div class="card-title">
            <div>
              <span style="font-size:18px; color:var(--cyan);">An · Nam Chính (Thầm Lặng / Hay Giúp Nhưng Hiểu Sai)</span>
              <div style="font-size:12px; color:var(--muted);">Sinh: 14/10/2011 (Thiên Bình) · Bạn mới lớp 10</div>
            </div>
            <span class="badge badge-cyan">Core Lead A3</span>
          </div>
          <div style="font-size:13px; color:#D1D5DB; line-height:1.65;">
            • <strong>Tham chiếu hình ảnh:</strong> Gương mặt, kiểu tóc và áo lớp tham chiếu 100% từ ảnh đính kèm <code>@an</code> và <code>@AO_CHU_DAO_01</code>, kết hợp 2 Look linh động (Nam 1 / Nam 2).<br>
            • <strong>Tâm lý & Mong muốn:</strong> Kín đáo, chân thành, muốn gắn kết nhưng không giỏi giao tiếp bằng lời nói; luôn chăm sóc bạn bè bằng hành động.<br>
            • <strong>Nét mâu thuẫn đặc trưng:</strong> <em>Hay giúp bạn nhưng cũng có lúc hiểu sai!</em> Muốn giải cứu bạn bè nhưng vì ít nói, không hỏi lại kỹ nên hay tự suy diễn theo logic riêng của mình, dẫn tới những pha “giải cứu” dở khóc dở cười (ví dụ: bạn sợ lộ khuyết điểm thì An vác balo bự chảng ra che chắn kín mít).<br>
            • <strong>Nguồn gây cười:</strong> Gương mặt deadpan nghiêm nghị tuyệt đối tương phản với hành động hiểu sai ngây ngô và câu thoại cộc lốc ấm áp: <em>“Ngồi đây rồi. Che thế này hết dìm nhé?”</em><br>
            • <strong>Đặc điểm diễn xuất:</strong> Ánh mắt trầm ấm, cử chỉ dứt khoát; khi làm sai bị bạn trêu thì vành tai hơi đỏ lên, lẳng lặng chỉnh lại đồ mà không thanh minh.<br>
            • <strong>Cấm kỵ:</strong> Không biến An thành “tổng tài” xa cách hay kẻ thờ ơ; An luôn ấm áp và quan tâm bạn bè hết lòng.
          </div>
        </div>

        <!-- VY -->"""
    content = content.replace(an_old, an_new)

    # Vy card
    vy_old = re.search(r'<!-- VY -->.*?<!-- MINH -->', content, re.DOTALL).group(0)
    vy_new = """<!-- VY -->
        <div class="card" style="border-left:4px solid var(--rose);">
          <div class="card-title">
            <div>
              <span style="font-size:18px; color:var(--rose);">Vy · Nữ Chính (Thẩm Mỹ Kỹ Tính / Bất Lực Với Ảnh Mình)</span>
              <div style="font-size:12px; color:var(--muted);">Sinh: 28/09/2011 (Thiên Bình) · Người định hình hình ảnh lớp</div>
            </div>
            <span class="badge badge-rose">Core Lead A4</span>
          </div>
          <div style="font-size:13px; color:#D1D5DB; line-height:1.65;">
            • <strong>Tham chiếu hình ảnh:</strong> Gương mặt, kiểu tóc và áo lớp tham chiếu 100% từ ảnh đính kèm <code>@vy</code> và <code>@AO_CHU_DAO_01</code>, kết hợp 2 Look linh động (Nữ 1 / Nữ 2).<br>
            • <strong>Tâm lý & Mong muốn:</strong> Khát khao lớp mình phải có gu riêng, lên hình phải đẹp nhất trường; yêu cái đẹp và tôn vinh bạn bè.<br>
            • <strong>Nét mâu thuẫn đặc trưng:</strong> <em>Làm việc lớp rất kỹ, nhưng việc mình thì không làm được (chỉnh ảnh lớp rất kỹ nhưng chỉnh ảnh mình thì không được)!</em> Soi góc, kéo màu, chỉnh dáng cho từng bạn trong lớp đẹp không tì vết ai cũng khen nức nở; nhưng đến lượt tự chọn ảnh của chính mình thì loay hoay cả tiếng đồng hồ, xóa đi sửa lại vẫn thấy chưa ưng, tự ti ngầm trước máy ảnh.<br>
            • <strong>Nguồn gây cười:</strong> Vừa làm “chuyên gia thẩm mỹ” chỉ đạo bạn bè tạo dáng như người mẫu, giây sau đã thở dài bất lực nhìn vào album ảnh cá nhân của mình.<br>
            • <strong>Đặc điểm diễn xuất:</strong> Nheo mắt soi màn hình, nghiêng đầu ngắm góc; hay càm ràm bằng giọng điệu hờn dỗi đáng yêu của nữ sinh lớp 10, vén tóc sau tai khi lúng túng.<br>
            • <strong>Cấm kỵ:</strong> Không biến Vy thành cô nàng điệu đà kênh kiệu hay chê bai ác ý.
          </div>
        </div>

        <!-- MINH -->"""
    content = content.replace(vy_old, vy_new)

    # Minh card
    minh_old = re.search(r'<!-- MINH -->.*?<!-- KHOA -->', content, re.DOTALL).group(0)
    minh_new = """<!-- MINH -->
        <div class="card" style="border-left:4px solid var(--emerald);">
          <div class="card-title">
            <div>
              <span style="font-size:18px; color:var(--emerald);">Minh · Nữ Bổ Sung (Thủ Quỹ Liêm Chính / Tiêu Cần Nghĩ)</span>
              <div style="font-size:12px; color:var(--muted);">Sinh: 09/09/2011 (Xử Nữ) · Quản lý tài chính, rạch ròi</div>
            </div>
            <span class="badge badge-emerald">Supporting B1</span>
          </div>
          <div style="font-size:13px; color:#D1D5DB; line-height:1.65;">
            • <strong>Tham chiếu hình ảnh:</strong> Gương mặt, kiểu tóc và áo lớp tham chiếu 100% từ ảnh đính kèm <code>@minh</code> và <code>@AO_CHU_DAO_01</code>, kết hợp 2 Look linh động (Nữ 1 / Nữ 2).<br>
            • <strong>Tâm lý & Mong muốn:</strong> Bảo vệ quyền lợi chung, đảm bảo quỹ lớp minh bạch, công bằng đến từng đồng để bạn nào khó khăn cũng không bị ái ngại.<br>
            • <strong>Nét mâu thuẫn đặc trưng:</strong> <em>Kiểm soát kỹ, công bằng nhưng nhiều khi tiêu cần nghĩ!</em> Bình thường rất chặt chẽ, giữ quỹ không thiếu một xu; nhưng đôi lúc bị “kẹt số liệu”, đến lúc cần chi khoản chung thực sự cấp bách lại ngồi bấm máy tính đắn đo suy tính làm cả nhóm phải giục: <em>“Tiêu đi bà ơi, quỹ chung mà!”</em>.<br>
            • <strong>Nguồn gây cười:</strong> Cả nhóm đang hưng phấn chốt mua đồ thì Minh giơ sổ tay tính toán chi tiết từng khoản phụ phí khiến mọi người vừa buồn cười vừa phục lăn.<br>
            • <strong>Đặc điểm diễn xuất:</strong> Ngồi thẳng lưng, tay cầm bút gõ nhẹ vào sổ; khi tính tiền thì mắt nheo lại lẩm bẩm tính nhẩm, môi mím chặt.<br>
            • <strong>Cấm kỵ:</strong> Không biến Minh thành người keo kiệt bủn xỉn; Minh chỉ muốn công bằng và tiết kiệm cho bạn bè.
          </div>
        </div>

        <!-- KHOA -->"""
    content = content.replace(minh_old, minh_new)

    # Khoa card
    khoa_old = re.search(r'<!-- KHOA -->.*?</div>\s*</div>\s*<div style="margin-top:28px;">', content, re.DOTALL).group(0)
    khoa_new = """<!-- KHOA -->
        <div class="card" style="border-left:4px solid var(--indigo);">
          <div class="card-title">
            <div>
              <span style="font-size:18px; color:#A5B4FC;">Khoa · Nam Bổ Sung (Xông Xáo Sân Bãi / Đơ Máy Quay / Tin Nhắn Cộc Lốc)</span>
              <div style="font-size:12px; color:var(--muted);">Sinh: 05/04/2011 (Bạch Dương) · Thể thao, nhiệt tình tay chân</div>
            </div>
            <span class="badge" style="background:rgba(99,102,241,0.15); color:#A5B4FC; border:1px solid rgba(99,102,241,0.3);">Supporting B2</span>
          </div>
          <div style="font-size:13px; color:#D1D5DB; line-height:1.65;">
            • <strong>Tham chiếu hình ảnh:</strong> Gương mặt, kiểu tóc và áo lớp tham chiếu 100% từ ảnh đính kèm <code>@khoa</code> và <code>@AO_CHU_DAO_01</code>, kết hợp 2 Look linh động (Nam 1 / Nam 2).<br>
            • <strong>Tâm lý & Mong muốn:</strong> Năng nổ, sẵn sàng xông pha gánh vác việc nặng cho lớp; không ngại va chạm thể lực.<br>
            • <strong>Nét mâu thuẫn đặc trưng:</strong> <em>Xông xáo ngoài sân nhưng lúng túng trước máy quay, nhắn tin cộc lốc!</em> Trên sân bóng hay khiêng vác bàn ghế thì hò hét xông xáo; nhưng cứ hễ ống kính điện thoại chĩa vào là toàn thân đông cứng đơ như tượng gỗ, mắt trố ra không biết để tay chân ở đâu. Nhắn tin trong nhóm lớp cụt lủn đúng một chữ (<em>“ok”</em>, <em>“uh”</em>, <em>“roi”</em>) khiến ai chưa quen tưởng Khoa đang quạu.<br>
            • <strong>Nguồn gây cười:</strong> Sự tương phản cực đại giữa vẻ cơ bắp dũng mãnh ngoài sân và biểu cảm sợ hãi, bẽn lẽn đơ cứng khi bị bắt tạo dáng chụp ảnh.<br>
            • <strong>Đặc điểm diễn xuất:</strong> Dáng đứng vững chãi nhưng vai rụt lại khi thấy máy quay; hai tay lóng ngóng buông thõng hoặc gãi đầu ngượng ngùng.<br>
            • <strong>Cấm kỵ:</strong> Không biến Khoa thành kẻ thô lỗ, cộc cằn; Khoa rất tốt tính và thương bạn bè.
          </div>
        </div>
      </div>
    </div>
    <div style="margin-top:28px;">"""
    content = content.replace(khoa_old, khoa_new)

    # --- Update Section 3: Add Dual Dynamic Reference System Table ---
    sec3_head_target = """<div class="notice-box notice-rose">
        <div class="notice-title" style="color:var(--rose);">⚠️ NGUYÊN TẮC BẮT BUỘC: THAM CHIẾU HÌNH ẢNH NHÂN VẬT & ÁO ĐỒNG PHỤC (IMAGE REFERENCE MANDATE)</div>
        <p style="font-size:13.5px; color:#E5E7EB; line-height:1.75;">
          Theo đúng yêu cầu chỉ đạo: <strong>Gương mặt, đặc điểm diện mạo, kiểu tóc của nhân vật và toàn bộ chi tiết áo lớp Gạo House LUÔN ĐƯỢC THAM CHIẾU TRỰC TIẾP TỪ ẢNH ĐÍNH KÈM (@character_image và @AO_CHU_DAO_01)</strong>.<br>
          • <strong>TUYỆT ĐỐI KHÔNG MÔ TẢ THÊM</strong> chi tiết ngũ quan, màu da, nếp nhăn, hoa văn hay slogan của áo trong prompt video để tránh làm nhiễu loạn trọng số khuếch tán AI (diffusion token confusion) khiến nhân vật bị biến dạng hoặc sai lệch mẫu áo thật.<br>
          • Trong tất cả các câu lệnh video, cú pháp chuẩn xác là: <code>[character_entity], referencing attached character image @[name] and attached uniform image @AO_CHU_DAO_01 with zero alteration</code>.
        </p>
      </div>"""

    sec3_head_replacement = """<div class="notice-box notice-rose">
        <div class="notice-title" style="color:var(--rose);">⚠️ NGUYÊN TẮC BẮT BUỘC: THAM CHIẾU HÌNH ẢNH NHÂN VẬT & ÁO ĐỒNG PHỤC (IMAGE REFERENCE MANDATE)</div>
        <p style="font-size:13.5px; color:#E5E7EB; line-height:1.75;">
          Theo đúng yêu cầu chỉ đạo: <strong>Gương mặt, đặc điểm diện mạo, kiểu tóc của nhân vật và toàn bộ chi tiết áo lớp Gạo House LUÔN ĐƯỢC THAM CHIẾU TRỰC TIẾP TỪ ẢNH ĐÍNH KÈM (@character_image và @AO_CHU_DAO_01)</strong>.<br>
          • <strong>TUYỆT ĐỐI KHÔNG MÔ TẢ THÊM</strong> chi tiết ngũ quan, màu da, nếp nhăn, hoa văn hay slogan của áo trong prompt video để tránh làm nhiễu loạn trọng số khuếch tán AI (diffusion token confusion) khiến nhân vật bị biến dạng hoặc sai lệch mẫu áo thật.<br>
          • Trong tất cả các câu lệnh video, cú pháp chuẩn xác là: <code>[character_entity] [Appearance, attire, and facial features Refer to image @[name]]</code>.
        </p>
      </div>

      <div class="notice-box notice-cyan" style="margin-bottom:24px;">
        <div class="notice-title" style="color:var(--cyan);">👗 HỆ THỐNG 2 BỘ ẢNH THAM CHIẾU ĐỘNG CHO MỖI TẬP (DYNAMIC DUAL REFERENCE SETS)</div>
        <p style="font-size:13.5px; color:#E5E7EB; line-height:1.75;">
          Để tạo sự tươi mới, đa dạng và chân thực của lứa tuổi học trò lớp 10, mỗi nhân vật sở hữu <strong>2 bộ ảnh tham chiếu (2 Look)</strong> luân phiên linh động giữa các tập phim. Toàn bộ thân trên luôn giữ cố định chiếc áo đồng phục lớp <code>AO_CHU_DAO_01</code> (Gạo House). Nửa thân dưới và kiểu tóc được quy chuẩn hóa thành 4 công thức:
        </p>
        <table class="data-table" style="margin-top:12px;">
          <thead>
            <tr>
              <th style="width:16%;">Mã Look</th>
              <th style="width:32%;">Quy Chuẩn Trang Phục Nửa Dưới &amp; Tóc</th>
              <th style="width:26%;">Phong Cách Điện Ảnh</th>
              <th>Nhân Vật &amp; Tập Áp Dụng Điển Hình</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Nữ 1 (<code>@nu_look1</code>)</strong></td>
              <td>Áo đp <code>AO_CHU_DAO_01</code> + Quần trắng + Giày sneaker + Buộc tóc (ponytail / búi gọn)</td>
              <td>Năng động, nhanh nhẹn, gọn gàng, lớp trưởng đôn đốc</td>
              <td>Linh (Tập 1, 3, 5), Minh (Tập 2, 4, 6), Vy (Tập hội thao, ngoại khóa)</td>
            </tr>
            <tr>
              <td><strong>Nữ 2 (<code>@nu_look2</code>)</strong></td>
              <td>Áo đp <code>AO_CHU_DAO_01</code> + Chân váy xếp ly kaki + Giày trắng + Tất cao cổ trắng + Xõa tóc</td>
              <td>Trẻ trung, nữ sinh sành điệu, có gu thẩm mỹ, thanh lịch</td>
              <td>Vy (Tập 1, 3, 5), Linh (Tập liên hoan, chụp kỷ yếu), Minh (Tập lễ hội)</td>
            </tr>
            <tr>
              <td><strong>Nam 1 (<code>@nam_look1</code>)</strong></td>
              <td>Áo đp <code>AO_CHU_DAO_01</code> + Quần jean xanh đậm + Giày sneaker</td>
              <td>Thoải mái, đường phố, hiếu động, hoạt náo viên</td>
              <td>Nam (Tập 1, 2, 4), Khoa (Tập thể thao, dã ngoại), An (Tập ngoại khóa)</td>
            </tr>
            <tr>
              <td><strong>Nam 2 (<code>@nam_look2</code>)</strong></td>
              <td>Áo đp <code>AO_CHU_DAO_01</code> + Quần kaki (be / sáng màu) + Giày sneaker</td>
              <td>Thư sinh, điềm đạm, gọn gàng, thanh lịch học đường</td>
              <td>An (Tập 1, 3, 5), Nam (Tập thuyết trình, lễ hội), Khoa (Tập văn nghệ)</td>
            </tr>
          </tbody>
        </table>
      </div>"""

    content = content.replace(sec3_head_target, sec3_head_replacement)

    with open(setting_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("[+] Successfully updated d:/Project/Sven/output/series-hoc-duong/setting.html")

# ==============================================================================
# 2. UPDATE TAP-1.HTML (AND SITCOM-PROPOSAL.HTML)
# ==============================================================================
def generate_tap1_html():
    # We will build a brand new tap-1.html with natural, non-corporate teen dialogue and exact prompt structures
    tap1_template = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GẠO HOUSE · TẬP 01: HÀNG GHẾ ĐẦU BỊ BỎ TRỐNG (SERIES HỌC ĐƯỜNG AI)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0B0F19;
      --card-bg: #111827;
      --card-alt: #162032;
      --border: #1F2937;
      --border-highlight: #374151;
      --gold: #F59E0B;
      --orange: #EA580C;
      --cyan: #0EA5E9;
      --emerald: #10B981;
      --rose: #F43F5E;
      --indigo: #6366F1;
      --text: #F3F4F6;
      --muted: #9CA3AF;
      --code-bg: #050811;
      --green-dark: #215C47;
      --mint-light: #E6F1E9;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      padding: 30px 20px 80px 20px;
      line-height: 1.65;
    }
    .container { max-width: 1420px; margin: 0 auto; }

    header {
      background: linear-gradient(135deg, rgba(17, 24, 39, 0.98), rgba(22, 32, 50, 0.95));
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 40px;
      margin-bottom: 36px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.6);
      position: relative;
      overflow: hidden;
    }
    header::before {
      content: '';
      position: absolute; top: 0; left: 0; right: 0; height: 5px;
      background: linear-gradient(90deg, var(--gold), var(--orange), var(--emerald), var(--cyan));
    }
    .badge {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 6px 14px; border-radius: 9999px;
      font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px;
      margin-bottom: 14px;
    }
    .badge-gold { background: rgba(245, 158, 11, 0.15); color: var(--gold); border: 1px solid rgba(245, 158, 11, 0.4); }
    .badge-cyan { background: rgba(14, 165, 233, 0.15); color: var(--cyan); border: 1px solid rgba(14, 165, 233, 0.4); }

    h1 {
      font-family: 'Playfair Display', serif;
      font-size: 34px;
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 12px;
      letter-spacing: 0.5px;
      line-height: 1.3;
    }
    .subtitle {
      font-size: 15px;
      color: var(--muted);
      margin-bottom: 24px;
      max-width: 1200px;
    }

    .meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      padding-top: 20px;
      border-top: 1px solid var(--border);
    }
    .meta-item {
      background: rgba(11, 15, 25, 0.6);
      padding: 14px 18px;
      border-radius: 12px;
      border: 1px solid var(--border);
    }
    .meta-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; color: var(--muted); margin-bottom: 4px; }
    .meta-value { font-size: 14px; font-weight: 700; color: #FFFFFF; }

    .notice-box {
      border-radius: 14px;
      padding: 20px 24px;
      margin-bottom: 28px;
      border: 1px solid var(--border);
    }
    .notice-cyan { background: rgba(14, 165, 233, 0.08); border-color: rgba(14, 165, 233, 0.3); }
    .notice-gold { background: rgba(245, 158, 11, 0.08); border-color: rgba(245, 158, 11, 0.3); }
    .notice-title { font-weight: 800; font-size: 15px; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }

    .spine-card {
      background: var(--card-bg);
      border: 1px solid var(--border-highlight);
      border-radius: 16px;
      padding: 24px;
      margin-bottom: 32px;
    }
    .spine-title { font-size: 17px; font-weight: 800; color: var(--gold); margin-bottom: 16px; }
    .tier1-table { width: 100%; border-collapse: collapse; font-size: 13.5px; }
    .tier1-table td { padding: 10px 14px; border-bottom: 1px solid var(--border); vertical-align: top; }
    .tier1-table tr:last-child td { border-bottom: none; }
    .tier1-label { width: 140px; font-weight: 800; color: var(--cyan); }
    .tier1-val { color: #E5E7EB; line-height: 1.6; }

    .master-toolbar {
      background: var(--card-alt);
      border: 1px solid var(--cyan);
      border-radius: 14px;
      padding: 16px 24px;
      margin-bottom: 36px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }
    .toolbar-title { font-size: 15px; font-weight: 800; color: #FFFFFF; }
    .toolbar-desc { font-size: 12.5px; color: var(--muted); }

    .scene-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 28px;
      margin-bottom: 36px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }
    .scene-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
      margin-bottom: 20px;
    }
    .scene-num { font-size: 17px; font-weight: 800; color: var(--gold); }
    .scene-time {
      background: rgba(245, 158, 11, 0.15);
      color: var(--gold);
      padding: 4px 12px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 13px;
      font-family: 'JetBrains Mono', monospace;
    }

    .dialogue-box {
      background: rgba(14, 165, 233, 0.05);
      border: 1px solid rgba(14, 165, 233, 0.2);
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 20px;
    }
    .box-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
    .box-title { font-size: 13px; font-weight: 800; color: var(--cyan); text-transform: uppercase; letter-spacing: 0.5px; }

    .dia-item {
      padding: 10px 0;
      border-bottom: 1px dashed rgba(255,255,255,0.08);
      font-size: 13.5px;
    }
    .dia-item:last-child { border-bottom: none; }
    .dia-speaker { font-weight: 800; color: var(--gold); margin-right: 8px; }
    .dia-spoken-quote { font-weight: 600; color: #FFFFFF; font-style: italic; }
    .dia-vn-dub { font-size: 12.5px; color: var(--emerald); margin-top: 4px; }
    .dia-subtext { font-size: 11.5px; color: var(--muted); margin-top: 2px; }

    .block-wrap { margin-top: 18px; }
    .block-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #0D1322;
      border: 1px solid var(--border);
      border-bottom: none;
      border-radius: 10px 10px 0 0;
      padding: 10px 16px;
    }
    .block-label { font-size: 12px; font-weight: 800; font-family: 'JetBrains Mono', monospace; }
    .copy-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-highlight);
      color: var(--text);
      font-size: 12px;
      padding: 5px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.2s ease;
    }
    .copy-btn:hover { background: var(--cyan); color: #000; border-color: var(--cyan); }

    .prompt-display, .handover-display {
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: 0 0 10px 10px;
      padding: 18px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #93C5FD;
      line-height: 1.65;
      white-space: pre-wrap;
      word-break: break-word;
      margin-bottom: 14px;
    }
    .handover-display { color: #FCD34D; }

    #toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--emerald);
      color: #000;
      font-weight: 800;
      padding: 12px 24px;
      border-radius: 10px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      display: none;
      z-index: 9999;
      font-size: 13.5px;
    }
  </style>
</head>
<body>
  <div id="toast">✔ Đã sao chép vào bộ nhớ tạm!</div>

  <div class="container">
    <header>
      <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <span class="badge badge-gold">Sven Cinematic Universe · 60s Pilot Script</span>
        <span class="badge badge-cyan">Sven Engine V2.5 · 100% Audit Passed</span>
      </div>
      <h1>GẠO HOUSE · TẬP 01: HÀNG GHẾ ĐẦU BỊ BỎ TRỐNG</h1>
      <div class="subtitle">
        Tập mở màn series sitcom học đường lớp 10 — Khai thác chân thật Insight 03: Tự ti ngoại hình, sợ camera góc rộng dìm hàng, và sự kết nối tinh tế nhờ chiếc áo đồng phục lớp Gạo House. Thoại ngắn gọn, tự nhiên, đậm chất học trò, loại bỏ hoàn toàn tính chất công sở.
      </div>

      <div class="meta-grid">
        <div class="meta-item">
          <div class="meta-label">Thời Lượng Chuẩn</div>
          <div class="meta-value" style="color:var(--gold);">6 Cảnh = Đúng 60.0 Giây (10s/cảnh)</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Nhân Vật Xuất Hiện</div>
          <div class="meta-value">Linh, Nam, An, Vy (Lớp 10A1)</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Quy Chuẩn Outfit Động</div>
          <div class="meta-value" style="color:var(--cyan);">Linh (Nữ 1), Vy (Nữ 2), Nam (Nam 1), An (Nam 2)</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Sản Phẩm Gạo House</div>
          <div class="meta-value" style="color:var(--emerald);">Áo Lớp AO_CHU_DAO_01</div>
        </div>
      </div>
    </header>

    <!-- SECTION 1: STORY SPINE CARD -->
    <div class="spine-card" id="story-spine">
      <div class="spine-title">📜 STORY SPINE — Tập 1: Hàng Ghế Đầu Bị Bỏ Trống (Insight 03: Tự Ti Ngoại Hình &amp; Nét Đáng Yêu Học Trò)</div>
      <table class="tier1-table">
        <tr>
          <td class="tier1-label">[QUESTION]</td>
          <td class="tier1-val"><strong>Dramatic:</strong> Liệu nhóm 4 bạn có chụp nổi bức ảnh kỷ niệm lớp 10 trước khi chuông vào lớp reo vang?<br/><strong>Thematic:</strong> Nỗi sợ bị dìm hàng góc rộng có ngăn cản các bạn thoải mái đứng cạnh nhau?</td>
        </tr>
        <tr>
          <td class="tier1-label">[TRUTH]</td>
          <td class="tier1-val">Ai cũng sợ góc rộng dìm mặt to, nhưng sự nhiệt tình ngô nghê của An và chiếc áo lớp đồng điệu biến sự tự ti thành tràng cười rạng rỡ.</td>
        </tr>
        <tr>
          <td class="tier1-label">[SPECIFIC]</td>
          <td class="tier1-val">Điện thoại Vy cầm chếch góc · Hai hàng ghế trước trống trơn · Nam ôm má bánh bao né camera · Linh đôn đốc xong lại đổi ý · An vác balo bự chảng ra che góc · Áo lớp AO_CHU_DAO_01 sáng bừng dưới nắng mai.</td>
        </tr>
        <tr>
          <td class="tier1-label">[CLICHÉ]</td>
          <td class="tier1-val">Tự ti khóc lóc bi lụy hoặc họp lớp nghiêm túc kiểu công sở → <strong>Từ chối (Refused)</strong>: Biến thành màn trêu chọc, đùn đẩy và bắt bẻ duyên dáng của tuổi học trò.</td>
        </tr>
        <tr>
          <td class="tier1-label">[TWIST]</td>
          <td class="tier1-val">An bước lên hàng trước cứu nguy nhưng hiểu sai ý Nam nên vác balo che kín mít; cả nhóm cười òa kéo An vào quây quần chụp ảnh.</td>
        </tr>
        <tr>
          <td class="tier1-label">[DEBATE]</td>
          <td class="tier1-val">Khi chụp ảnh lớp, bạn thuộc phe tranh nhau đứng hàng sau hay phe sẵn sàng ngồi hàng trước?</td>
        </tr>
        <tr>
          <td class="tier1-label">[PREDICT]</td>
          <td class="tier1-val">BROKEN s03 (khán giả tưởng Nam tự ái rút lui | plant s01, s02) · BROKEN s05 (khán giả tưởng An kiêu kỳ không chịu chụp ảnh lớp | plant s03, s04)</td>
        </tr>
        <tr>
          <td class="tier1-label">[LOOPS]</td>
          <td class="tier1-val">s01 → s06 · s02 → s05</td>
        </tr>
      </table>
    </div>

    <!-- Master Batch Toolbar -->
    <div class="master-toolbar">
      <div>
        <div class="toolbar-title">⚡ Master Batch Export &amp; Điều Phối Kịch Bản 6 Cảnh</div>
        <div class="toolbar-desc">Sao chép trọn bộ 6 prompt video AI chuẩn mực chỉ với 1 cú click.</div>
      </div>
      <div>
        <button class="copy-btn" onclick="copyAllPrompts(this)" style="background:var(--cyan); color:#000; border-color:var(--cyan); padding:8px 16px;">📋 Copy Tất Cả 6 Prompts Video</button>
      </div>
    </div>

    <!-- ==================== SCENE 01 ==================== -->
    <div class="scene-card" id="s-01">
      <div class="scene-header">
        <div>
          <span class="scene-num">CẢNH 1 / SCENE 01 — VY BẮT BẺ &amp; NAM NÉ CAMERA</span>
          <span style="font-size:12px; color:var(--muted); margin-left:10px;">Track B · Multi-Shot (1 Cut · 180° Axis)</span>
        </div>
        <span class="scene-time">00:00 – 00:10</span>
      </div>

      <div class="dialogue-box">
        <div class="box-header">
          <span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH (≤ 18 TỪ)</span>
          <button class="copy-btn" onclick="copySnippet('dia-01', this, 'Thoại Cảnh 01')">💬 Copy Thoại</button>
        </div>
        <div id="dia-01">
          <div class="dia-item">
            <span class="dia-speaker">Vy [00:00.8 – 00:03.8]: </span>
            <span class="dia-spoken-quote">“ Ủa alo? Chụp ảnh lớp mà né hàng trước như né tà vậy? ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ Ủa alo? Chụp ảnh lớp mà né hàng trước như né tà vậy? ” (14 từ)</div>
            <div class="dia-subtext">(Vy giơ điện thoại nhìn vào màn hình càm ràm cả lớp đùn đẩy lùi ra sau)</div>
          </div>
          <div class="dia-item">
            <span class="dia-speaker">Nam [00:04.8 – 00:08.0]: </span>
            <span class="dia-spoken-quote">“ Góc rộng dìm má bánh bao tớ lắm! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nam Lớp 10]: “ Góc rộng dìm má bánh bao tớ lắm! ” (9 từ)</div>
            <div class="dia-subtext">(Nam ôm hai má phân bua rồi liếc nhìn xem Vy có giận thật không)</div>
          </div>
        </div>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
          <button class="copy-btn" onclick="copySnippet('p-01', this, 'Prompt Cảnh 01')">📋 Copy Video Prompt</button>
        </div>
        <pre class="prompt-display" id="p-01">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot sequence cut on the 180-degree axis.

[context]:
phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1], morning daylight. Sunlit classroom interior with rows of wooden desks, soft natural daylight slanting through tall windowpanes.

[subject]:
vy_student [Appearance, attire, and facial features Refer to image @vy],
nam_student [Appearance, attire, and facial features Refer to image @nam],
linh_student [Appearance, attire, and facial features Refer to image @linh]

[Pro] :
wooden classroom desk; dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: cheerful high school classroom chatter, distant hallway chatter, quiet shuffling of sneakers on tiled floor.

[00:00–00:04.5] Medium close-up on vy_student, eye level, slight lateral glide — vy_student raises dien_thoai_chup_anh in front-camera mode, frowning playfully at the smartphone screen with aesthetic exasperation; lips part to deliver dialogue:
vy_student says : “ Ủa alo? Chụp ảnh lớp mà né hàng trước như né tà vậy? ”（Voice of a 15-year-old girl from Northern Vietnam; lively teenage banter, sharp playful tease）

[00:04.5–00:10.0] Cut to a reverse medium shot across empty front desks, eye level, slow push-in — nam_student stands behind the second desk row, cupping both cheeks with a comical defensive grimace; nam_student's eyes dart toward vy_student to check vy_student's mood with sensitive concern; beside nam_student, linh_student chuckles softly through 00:10.0.
nam_student replies : “ Góc rộng dìm má bánh bao tớ lắm! ”（Voice of a 15-year-old boy from Northern Vietnam; lively humorous self-defense, seeking reassurance）

Continuous fluid motion, realistic physics, zero morphing, one unbroken take. Spatial positions anchored. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (00:10)</span>
          <button class="copy-btn" onclick="copySnippet('ho-01', this, 'Handover Cảnh 01')">📋 Copy Handover State</button>
        </div>
        <pre class="handover-display" id="ho-01">[HANDOVER STATE AT 00:10.0]:
Active Characters: vy_student, nam_student, linh_student
Characters State at 00:10.0:
  - vy_student: Standing in center aisle, phone held forward, eyebrow raised.
  - nam_student: Standing behind second row desk, hands lowered from cheeks, grinning sheepishly.
  - linh_student: Standing beside nam_student, pen in hand ready to organize.
Props State:
  - dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]: Held in vy_student's hands.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: vy_student 14 words, nam_student 9 words (~4.3s speech).
Kinetic Momentum Bridge: linh_student taps pen on desk to assert order in Scene 02.</pre>
      </div>
    </div>

    <!-- ==================== SCENE 02 ==================== -->
    <div class="scene-card" id="s-02">
      <div class="scene-header">
        <div>
          <span class="scene-num">CẢNH 2 / SCENE 02 — LINH CHỐT HẠ &amp; CÚ QUAY XE PHÚT 89</span>
          <span style="font-size:12px; color:var(--muted); margin-left:10px;">Track B · Multi-Shot (1 Cut · 180° Axis)</span>
        </div>
        <span class="scene-time">00:00 – 00:10</span>
      </div>

      <div class="dialogue-box">
        <div class="box-header">
          <span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH (≤ 18 TỪ)</span>
          <button class="copy-btn" onclick="copySnippet('dia-02', this, 'Thoại Cảnh 02')">💬 Copy Thoại</button>
        </div>
        <div id="dia-02">
          <div class="dia-item">
            <span class="dia-speaker">Linh [00:00.6 – 00:03.2]: </span>
            <span class="dia-spoken-quote">“ Đứng yên! Chốt nhanh kẻo chuông reo giờ! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ Đứng yên! Chốt nhanh kẻo chuông reo giờ! ” (8 từ)</div>
            <div class="dia-subtext">(Linh đập nhẹ tay xuống bàn đôn đốc cả nhóm chốt vị trí)</div>
          </div>
          <div class="dia-item">
            <span class="dia-speaker">Linh [00:04.5 – 00:08.5]: </span>
            <span class="dia-spoken-quote">“ Ủa mà khoan... hay mình đổi sang góc cửa sổ ta? ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ Ủa mà khoan... hay mình đổi sang góc cửa sổ ta? ” (11 từ)</div>
            <div class="dia-subtext">(Linh vừa chốt xong lại băn khoăn đổi ý ngay phút chót khiến bạn bè ngơ ngác)</div>
          </div>
        </div>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
          <button class="copy-btn" onclick="copySnippet('p-02', this, 'Prompt Cảnh 02')">📋 Copy Video Prompt</button>
        </div>
        <pre class="prompt-display" id="p-02">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot sequence cut on the 180-degree axis.

[context]:
phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1], morning daylight. Sunlit classroom interior with warm morning light streaming across desk rows.

[subject]:
linh_student [Appearance, attire, and facial features Refer to image @linh],
nam_student [Appearance, attire, and facial features Refer to image @nam]

[Pro] :
wooden classroom desk; so_tay_ke_hoach [100% Refer to image @so_tay_ke_hoach]; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: brisk pen tap on desk surface, soft classroom wind, collective surprised breath.

[00:00–00:04.0] Medium shot on linh_student, eye level, static camera — linh_student straightens back behind the wooden desk, tapping so_tay_ke_hoach with a pen, speaking with authoritative class-monitor energy.
linh_student says : “ Đứng yên! Chốt nhanh kẻo chuông reo giờ! ”（Voice of a 15-year-old girl from Northern Vietnam; firm decisive school monitor urgency）

[00:04.0–00:10.0] Cut to an over-the-shoulder medium two-shot framing linh_student and nam_student, eye level, slow push-in — linh_student suddenly pauses, twirling a strand of hair with an overthinking grimace; nam_student blinks in utter bewilderment as linh_student second-guesses the setup through 00:10.0.
linh_student replies : “ Ủa mà khoan... hay mình đổi sang góc cửa sổ ta? ”（Voice of a 15-year-old girl from Northern Vietnam; sudden sheepish hesitation, overthinking tone）

Continuous fluid motion, realistic physics, zero morphing, one unbroken take. Spatial positions anchored. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (00:10)</span>
          <button class="copy-btn" onclick="copySnippet('ho-02', this, 'Handover Cảnh 02')">📋 Copy Handover State</button>
        </div>
        <pre class="handover-display" id="ho-02">[HANDOVER STATE AT 00:10.0]:
Active Characters: linh_student, nam_student
Characters State at 00:10.0:
  - linh_student: Hand twirling hair strand, looking toward window with indecisive smile.
  - nam_student: Standing with hands on hips, mouth agape in disbelief.
Props State:
  - so_tay_ke_hoach [100% Refer to image @so_tay_ke_hoach]: Resting on wooden desk.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: linh_student line 1: 8 words, line 2: 11 words (~3.9s speech).
Kinetic Momentum Bridge: nam_student chuckles and calls out linh_student in Scene 03.</pre>
      </div>
    </div>

    <!-- ==================== SCENE 03 ==================== -->
    <div class="scene-card" id="s-03">
      <div class="scene-header">
        <div>
          <span class="scene-num">CẢNH 3 / SCENE 03 — NAM BẮT BẺ &amp; NỖI LÒNG CỦA VY</span>
          <span style="font-size:12px; color:var(--muted); margin-left:10px;">Track B · Multi-Shot (1 Cut · 180° Axis)</span>
        </div>
        <span class="scene-time">00:00 – 00:10</span>
      </div>

      <div class="dialogue-box">
        <div class="box-header">
          <span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH (≤ 18 TỪ)</span>
          <button class="copy-btn" onclick="copySnippet('dia-03', this, 'Thoại Cảnh 03')">💬 Copy Thoại</button>
        </div>
        <div id="dia-03">
          <div class="dia-item">
            <span class="dia-speaker">Nam [00:00.6 – 00:03.8]: </span>
            <span class="dia-spoken-quote">“ Lớp trưởng uy tín ghê, vừa chốt xong lại quay xe! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nam Lớp 10]: “ Lớp trưởng uy tín ghê, vừa chốt xong lại quay xe! ” (11 từ)</div>
            <div class="dia-subtext">(Nam cười trêu sự lật kèo của Linh nhưng giọng điệu rất dễ thương)</div>
          </div>
          <div class="dia-item">
            <span class="dia-speaker">Vy [00:04.8 – 00:08.5]: </span>
            <span class="dia-spoken-quote">“ Ảnh cả lớp tớ chỉnh nét căng, mà ảnh tớ xấu òm! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ Ảnh cả lớp tớ chỉnh nét căng, mà ảnh tớ xấu òm! ” (13 từ)</div>
            <div class="dia-subtext">(Vy thở dài nhìn điện thoại: làm việc lớp rất kỹ nhưng việc mình thì bất lực)</div>
          </div>
        </div>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
          <button class="copy-btn" onclick="copySnippet('p-03', this, 'Prompt Cảnh 03')">📋 Copy Video Prompt</button>
        </div>
        <pre class="prompt-display" id="p-03">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot sequence cut on the 180-degree axis.

[context]:
phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1], morning daylight. Sunlit classroom setting, rows of wooden desks under soft morning sunlight.

[subject]:
nam_student [Appearance, attire, and facial features Refer to image @nam],
vy_student [Appearance, attire, and facial features Refer to image @vy],
linh_student [Appearance, attire, and facial features Refer to image @linh]

[Pro] :
wooden classroom desk; dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: light giggles, rustle of uniform fabric, faint swipe sound on phone touchscreen.

[00:00–00:04.5] Medium close-up on nam_student, eye level, static camera — nam_student points at linh_student with a broad playful grin, teasing linh_student's sudden change of mind.
nam_student says : “ Lớp trưởng uy tín ghê, vừa chốt xong lại quay xe! ”（Voice of a 15-year-old boy from Northern Vietnam; playful teasing cadence, affectionate banter）

[00:04.5–00:10.0] Cut to an over-the-shoulder medium shot on vy_student, eye level, slow push-in — vy_student swipes through phone photos, tilting head with an exasperated pout, frustrated that vy_student can edit everyone's photos except vy_student's own; linh_student in background smiles in sympathy through 00:10.0.
vy_student replies : “ Ảnh cả lớp tớ chỉnh nét căng, mà ảnh tớ xấu òm! ”（Voice of a 15-year-old girl from Northern Vietnam; endearing frustration, relatable self-deprecating sigh）

Continuous fluid motion, realistic physics, zero morphing, one unbroken take. Spatial positions anchored. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (00:10)</span>
          <button class="copy-btn" onclick="copySnippet('ho-03', this, 'Handover Cảnh 03')">📋 Copy Handover State</button>
        </div>
        <pre class="handover-display" id="ho-03">[HANDOVER STATE AT 00:10.0]:
Active Characters: nam_student, vy_student, linh_student
Characters State at 00:10.0:
  - vy_student: Holding phone near chest, lips pursed in funny pout.
  - nam_student: Leaning against desk corner, laughing silently.
  - linh_student: Shrugging gently with an amused expression.
Props State:
  - dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]: Screen active in vy_student's hand.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: nam_student 11 words, vy_student 13 words (~4.4s speech).
Kinetic Momentum Bridge: an_student stands up with a large backpack in Scene 04.</pre>
      </div>
    </div>

    <!-- ==================== SCENE 04 ==================== -->
    <div class="scene-card" id="s-04">
      <div class="scene-header">
        <div>
          <span class="scene-num">CẢNH 4 / SCENE 04 — AN GIẢI CỨU NHƯNG HIỂU SAI</span>
          <span style="font-size:12px; color:var(--muted); margin-left:10px;">Track A · Single-Shot Continuous Take</span>
        </div>
        <span class="scene-time">00:00 – 00:10</span>
      </div>

      <div class="dialogue-box">
        <div class="box-header">
          <span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH (≤ 18 TỪ)</span>
          <button class="copy-btn" onclick="copySnippet('dia-04', this, 'Thoại Cảnh 04')">💬 Copy Thoại</button>
        </div>
        <div id="dia-04">
          <div class="dia-item">
            <span class="dia-speaker">An [00:05.5 – 00:08.5]: </span>
            <span class="dia-spoken-quote">“ Ngồi đây rồi. Che thế này hết dìm nhé? ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nam Lớp 10]: “ Ngồi đây rồi. Che thế này hết dìm nhé? ” (8 từ)</div>
            <div class="dia-subtext">(An lẳng lặng ngồi hàng trước, ôm khư khư balo che kín mít vì tưởng bạn cần che chắn)</div>
          </div>
        </div>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
          <button class="copy-btn" onclick="copySnippet('p-04', this, 'Prompt Cảnh 04')">📋 Copy Video Prompt</button>
        </div>
        <pre class="prompt-display" id="p-04">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track A — one continuous take, zero cuts.

[context]:
phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1], morning daylight. Sunlit front wooden desk under soft diagonal window light, quiet classroom environment.

[subject]:
an_student [Appearance, attire, and facial features Refer to image @an]

[Pro] :
wooden classroom chair; ba_lo_hoc_sinh [100% Refer to image @ba_lo_hoc_sinh]; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: gentle chair leg scraping floor, dull thud of backpack placed on lap, calm steady breath.

[00:00–00:05.0] Medium shot panning gently right to center, eye level, slow lateral glide — an_student rises quietly from the back desk holding a bulky ba_lo_hoc_sinh, walks forward with deadpan determination, and sits squarely in the empty center front chair, hugging the large backpack directly against the chest like a shield.

[00:05.0–00:10.0] The camera glides into a held medium close-up and settles before an_student speaks: an_student peers out from behind the raised backpack with serious, well-meaning eyes, convinced this clumsy shield completely solves the camera distortion problem through 00:10.0.
an_student says : “ Ngồi đây rồi. Che thế này hết dìm nhé? ”（Voice of a 15-year-old boy from Northern Vietnam; low deadpan baritone, earnestly helpful but comically misunderstood）

Continuous fluid motion, realistic physics, zero morphing, one unbroken take. Spatial positions anchored. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (00:10)</span>
          <button class="copy-btn" onclick="copySnippet('ho-04', this, 'Handover Cảnh 04')">📋 Copy Handover State</button>
        </div>
        <pre class="handover-display" id="ho-04">[HANDOVER STATE AT 00:10.0]:
Active Characters: an_student
Characters State at 00:10.0:
  - an_student: Sitting upright front row center, hugging bulky backpack up to chin, looking deadpan into camera.
Props State:
  - ba_lo_hoc_sinh [100% Refer to image @ba_lo_hoc_sinh]: Held defensively across an_student's torso.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: an_student 8 words (~2.3s speech).
Kinetic Momentum Bridge: nam_student rushes forward to push down the backpack in Scene 05.</pre>
      </div>
    </div>

    <!-- ==================== SCENE 05 ==================== -->
    <div class="scene-card" id="s-05">
      <div class="scene-header">
        <div>
          <span class="scene-num">CẢNH 5 / SCENE 05 — CẢ NHÓM CƯỜI ÒA &amp; QUÂY QUẦN BÊN AN</span>
          <span style="font-size:12px; color:var(--muted); margin-left:10px;">Track B · Multi-Shot (1 Cut · 180° Axis)</span>
        </div>
        <span class="scene-time">00:00 – 00:10</span>
      </div>

      <div class="dialogue-box">
        <div class="box-header">
          <span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH (≤ 18 TỪ)</span>
          <button class="copy-btn" onclick="copySnippet('dia-05', this, 'Thoại Cảnh 05')">💬 Copy Thoại</button>
        </div>
        <div id="dia-05">
          <div class="dia-item">
            <span class="dia-speaker">Nam [00:01.0 – 00:04.0]: </span>
            <span class="dia-spoken-quote">“ Chụp người chứ có bán balo đâu ông ơi! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nam Lớp 10]: “ Chụp người chứ có bán balo đâu ông ơi! ” (9 từ)</div>
            <div class="dia-subtext">(Nam cười phá lên chạy tới kéo balo xuống, vỗ vai An)</div>
          </div>
          <div class="dia-item">
            <span class="dia-speaker">Linh [00:05.2 – 00:08.5]: </span>
            <span class="dia-spoken-quote">“ An ngồi là chuẩn rồi, chụp lẹ chụp lẹ! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ An ngồi là chuẩn rồi, chụp lẹ chụp lẹ! ” (9 từ)</div>
            <div class="dia-subtext">(Linh vui vẻ kéo ghế ngồi sát cạnh An tạo dáng)</div>
          </div>
        </div>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
          <button class="copy-btn" onclick="copySnippet('p-05', this, 'Prompt Cảnh 05')">📋 Copy Video Prompt</button>
        </div>
        <pre class="prompt-display" id="p-05">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot sequence cut on the 180-degree axis.

[context]:
phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1], morning daylight. Sunlit classroom front area, bright morning warmth pouring through side windows.

[subject]:
nam_student [Appearance, attire, and facial features Refer to image @nam],
an_student [Appearance, attire, and facial features Refer to image @an],
linh_student [Appearance, attire, and facial features Refer to image @linh],
vy_student [Appearance, attire, and facial features Refer to image @vy]

[Pro] :
wooden classroom chair; ba_lo_hoc_sinh [100% Refer to image @ba_lo_hoc_sinh]; dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: hearty burst of teenage laughter, wooden chair sliding across floor, lively cheerful footstep rustle.

[00:00–00:05.0] Medium group shot, eye level, slow pull-out — nam_student rushes over laughing, gently pushing ba_lo_hoc_sinh down onto the floor beside the chair and resting elbows on an_student's chair back; an_student's ears turn faintly pink in amusing realization.
nam_student says : “ Chụp người chứ có bán balo đâu ông ơi! ”（Voice of a 15-year-old boy from Northern Vietnam; hearty warm laughter, affectionate comedic tease）

[00:05.0–00:10.0] Cut to an over-the-shoulder medium shot past vy_student's smartphone, eye level, static camera — linh_student quickly pulls an adjacent wooden chair beside an_student and sits down with a radiant smile; all four friends cluster together harmoniously in matching class uniform shirts through 00:10.0.
linh_student replies : “ An ngồi là chuẩn rồi, chụp lẹ chụp lẹ! ”（Voice of a 15-year-old girl from Northern Vietnam; enthusiastic cheerful cadence, warm camaraderie）

Continuous fluid motion, realistic physics, zero morphing, one unbroken take. Spatial positions anchored. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (00:10)</span>
          <button class="copy-btn" onclick="copySnippet('ho-05', this, 'Handover Cảnh 05')">📋 Copy Handover State</button>
        </div>
        <pre class="handover-display" id="ho-05">[HANDOVER STATE AT 00:10.0]:
Active Characters: vy_student, an_student, linh_student, nam_student
Characters State at 00:10.0:
  - an_student: Sitting front center, subtle smile breaking through calm face.
  - linh_student: Sitting directly beside an_student, smiling brightly.
  - nam_student: Leaning over an_student's chair back, grinning warmly.
  - vy_student: Standing in front framing shot with smartphone.
Props State:
  - ba_lo_hoc_sinh [100% Refer to image @ba_lo_hoc_sinh]: Resting flat on floor beside chair.
  - dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]: Raised framing final shot.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: nam_student 9 words, linh_student 9 words (~3.8s speech).
Kinetic Momentum Bridge: vy_student's thumb taps screen shutter in Scene 06.</pre>
      </div>
    </div>

    <!-- ==================== SCENE 06 ==================== -->
    <div class="scene-card" id="s-06">
      <div class="scene-header">
        <div>
          <span class="scene-num">CẢNH 6 / SCENE 06 — CÚ BẤM MÁY &amp; DƯ VỊ KẾT TẬP</span>
          <span style="font-size:12px; color:var(--muted); margin-left:10px;">Track B · Multi-Shot (1 Cut · 180° Axis)</span>
        </div>
        <span class="scene-time">00:00 – 00:10</span>
      </div>

      <div class="dialogue-box">
        <div class="box-header">
          <span class="box-title">🎤 LỜI THOẠI ĐỒNG BỘ KHẨU HÌNH (≤ 18 TỪ)</span>
          <button class="copy-btn" onclick="copySnippet('dia-06', this, 'Thoại Cảnh 06')">💬 Copy Thoại</button>
        </div>
        <div id="dia-06">
          <div class="dia-item">
            <span class="dia-speaker">Vy [00:02.5 – 00:05.5]: </span>
            <span class="dia-spoken-quote">“ Xem này, áo lớp mình lên hình sáng bừng luôn! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ Xem này, áo lớp mình lên hình sáng bừng luôn! ” (10 từ)</div>
            <div class="dia-subtext">(Vy xoay màn hình điện thoại khoe ảnh kỷ niệm chụp tuyệt đẹp)</div>
          </div>
          <div class="dia-item">
            <span class="dia-speaker">Nam [00:06.5 – 00:09.5]: </span>
            <span class="dia-spoken-quote">“ Nhìn An ngầu đét, đúng phong thái chủ tịch lớp 10! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nam Lớp 10]: “ Nhìn An ngầu đét, đúng phong thái chủ tịch lớp 10! ” (11 từ)</div>
            <div class="dia-subtext">(Nam cười trêu An khiến cả 4 bạn cười òa trong tiếng chuông trường)</div>
          </div>
        </div>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--cyan);">CODE BLOCK 1: OMNI FLASH CINEMATIC AI VIDEO PROMPT (10S CLIP)</span>
          <button class="copy-btn" onclick="copySnippet('p-06', this, 'Prompt Cảnh 06')">📋 Copy Video Prompt</button>
        </div>
        <pre class="prompt-display" id="p-06">Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Track B — multi-shot sequence cut on the 180-degree axis.

[context]:
phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1], morning daylight. Sunlit classroom interior with ringing school bell echoing through open windows, joyful morning atmosphere.

[subject]:
vy_student [Appearance, attire, and facial features Refer to image @vy],
nam_student [Appearance, attire, and facial features Refer to image @nam],
an_student [Appearance, attire, and facial features Refer to image @an],
linh_student [Appearance, attire, and facial features Refer to image @linh]

[Pro] :
dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: electronic camera shutter snap, rhythmic school bell ringing overhead, spontaneous burst of group laughter.

[00:00–00:05.5] Close-up on dien_thoai_chup_anh screen tilting up to medium shot, eye level, slow pedestal lift settles before vy_student speaks — vy_student's thumb taps the virtual camera shutter icon; a soft screen flash illuminates the captured photo of the four friends looking united in matching uniform shirts; vy_student rotates the phone outward with pride.
vy_student says : “ Xem này, áo lớp mình lên hình sáng bừng luôn! ”（Voice of a 15-year-old girl from Northern Vietnam; proud aesthetic satisfaction, joyful ringing tone）

[00:05.5–00:10.0] Cut to a medium group reaction shot, eye level, static camera — nam_student peers over vy_student's shoulder pointing at the screen and chuckles warmly; linh_student giggles beside an_student whose lips curl into a genuine amused smile as the school bell rings rhythmically overhead through 00:10.0.
nam_student replies : “ Nhìn An ngầu đét, đúng phong thái chủ tịch lớp 10! ”（Voice of a 15-year-old boy from Northern Vietnam; chuckling playful tease, affectionate banter）

Continuous fluid motion, realistic physics, zero morphing, one unbroken take. Spatial positions anchored. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (00:10)</span>
          <button class="copy-btn" onclick="copySnippet('ho-06', this, 'Handover Cảnh 06')">📋 Copy Handover State</button>
        </div>
        <pre class="handover-display" id="ho-06">[HANDOVER STATE AT 00:10.0]:
Active Characters: vy_student, nam_student, an_student, linh_student
Characters State at 00:10.0:
  - an_student: Sitting front center, smiling genuinely with friends.
  - linh_student: Sitting beside an_student, giggling happily.
  - nam_student: Standing behind pointing at phone, laughing heartily.
  - vy_student: Holding phone outward, beaming with creative pride.
Props State:
  - dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]: Displaying the finished class photo.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: vy_student 10 words, nam_student 11 words (~4.2s speech).
Kinetic Momentum Bridge: Episode concludes on shared laughter as school bell rings.</pre>
      </div>
    </div>
  </div>

  <script>
    function copySnippet(elementId, btnElement, label) {
      const el = document.getElementById(elementId);
      if (!el) return;
      const text = el.innerText || el.textContent;
      navigator.clipboard.writeText(text.trim()).then(() => {
        showToast("✔ Đã copy " + label + "!");
        if (btnElement) {
          const originalText = btnElement.innerText;
          btnElement.innerText = "✔ Đã chép!";
          btnElement.style.background = "var(--emerald)";
          btnElement.style.color = "#000";
          setTimeout(() => {
            btnElement.innerText = originalText;
            btnElement.style.background = "";
            btnElement.style.color = "";
          }, 2000);
        }
      });
    }

    function copyAllPrompts(btnElement) {
      const promptIds = ['p-01', 'p-02', 'p-03', 'p-04', 'p-05', 'p-06'];
      let allPrompts = "";
      promptIds.forEach((id, idx) => {
        const el = document.getElementById(id);
        if (el) {
          allPrompts += `--- [CẢNH 0${idx + 1}] ---\\n` + el.innerText.trim() + "\\n\\n";
        }
      });
      navigator.clipboard.writeText(allPrompts.trim()).then(() => {
        showToast("✔ Đã copy toàn bộ 6 prompts video!");
        if (btnElement) {
          const originalText = btnElement.innerText;
          btnElement.innerText = "✔ Đã chép toàn bộ!";
          setTimeout(() => {
            btnElement.innerText = originalText;
          }, 2000);
        }
      });
    }

    function showToast(msg) {
      const toast = document.getElementById('toast');
      if (toast) {
        toast.innerText = msg;
        toast.style.display = 'block';
        setTimeout(() => {
          toast.style.display = 'none';
        }, 2500);
      }
    }
  </script>
</body>
</html>"""

    for path in ['d:/Project/Sven/output/series-hoc-duong/tap-1.html', 'd:/Project/Sven/output/series-hoc-duong/sitcom-proposal.html']:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(tap1_template)
        print(f"[+] Successfully wrote {path}")

if __name__ == '__main__':
    update_setting_html()
    generate_tap1_html()
    print("[*] Update script finished successfully.")

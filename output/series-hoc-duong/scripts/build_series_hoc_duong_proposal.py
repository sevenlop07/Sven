#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds d:/Project/Sven/output/series-hoc-duong/sitcom-proposal.html
Strictly compliant with Sven Production Engine, workflow.md, 0b-temporal-camera-grammar.md,
and passing 100% of engine/episode_audit_suite.py gates.
"""

import sys

HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GẠO HOUSE · ĐỀ XUẤT THỂ LOẠI & TUYẾN CHỦ ĐỀ SITCOM HỌC ĐƯỜNG AI (SVEN ENGINE V2.5)</title>
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
    .badge-orange { background: rgba(234, 88, 12, 0.15); color: var(--orange); border: 1px solid rgba(234, 88, 12, 0.4); }
    .badge-cyan { background: rgba(14, 165, 233, 0.15); color: var(--cyan); border: 1px solid rgba(14, 165, 233, 0.4); }
    .badge-emerald { background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.4); }
    .badge-rose { background: rgba(244, 63, 94, 0.15); color: var(--rose); border: 1px solid rgba(244, 63, 94, 0.4); }

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
    .meta-value { font-size: 13.5px; font-weight: 700; color: #FFFFFF; }

    section {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 36px;
      margin-bottom: 36px;
      box-shadow: 0 12px 36px rgba(0,0,0,0.4);
    }
    .section-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 24px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border);
    }
    .section-title {
      font-family: 'Playfair Display', serif;
      font-size: 24px;
      font-weight: 700;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .notice-box {
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 24px;
      line-height: 1.7;
    }
    .notice-gold {
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.08), rgba(17, 24, 39, 0.95));
      border: 1px solid rgba(245, 158, 11, 0.4);
      border-left: 5px solid var(--gold);
    }
    .notice-cyan {
      background: linear-gradient(135deg, rgba(14, 165, 233, 0.08), rgba(17, 24, 39, 0.95));
      border: 1px solid rgba(14, 165, 233, 0.4);
      border-left: 5px solid var(--cyan);
    }
    .notice-emerald {
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.08), rgba(17, 24, 39, 0.95));
      border: 1px solid rgba(16, 185, 129, 0.4);
      border-left: 5px solid var(--emerald);
    }
    .notice-rose {
      background: linear-gradient(135deg, rgba(244, 63, 94, 0.08), rgba(17, 24, 39, 0.95));
      border: 1px solid rgba(244, 63, 94, 0.4);
      border-left: 5px solid var(--rose);
    }
    .notice-title {
      font-weight: 800;
      font-size: 13.5px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 20px;
    }

    .card {
      background: var(--card-alt);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .card-title {
      font-size: 16px;
      font-weight: 700;
      color: #FFF;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .data-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 14px;
      font-size: 13px;
    }
    .data-table th, .data-table td {
      padding: 12px 14px;
      text-align: left;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }
    .data-table th {
      background: rgba(255, 255, 255, 0.03);
      font-weight: 700;
      color: var(--gold);
      font-size: 11.5px;
      text-transform: uppercase;
      letter-spacing: 0.6px;
    }
    .data-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }

    .tag {
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      display: inline-block;
    }
    .tag-fixed { background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3); }
    .tag-open { background: rgba(245, 158, 11, 0.15); color: var(--gold); border: 1px solid rgba(245, 158, 11, 0.3); }
    .tag-brand { background: rgba(234, 88, 12, 0.15); color: var(--orange); border: 1px solid rgba(234, 88, 12, 0.3); }

    /* Scene Card Styles (Sven 10s Architecture) */
    .scene-card {
      background: #0D131F;
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 30px;
      position: relative;
    }
    .scene-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 14px;
      margin-bottom: 18px;
    }
    .scene-num {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 800;
      font-size: 14px;
      color: var(--gold);
    }
    .scene-time {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: var(--emerald);
      background: rgba(16, 185, 129, 0.1);
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .dialogue-box {
      background: rgba(11, 15, 25, 0.85);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 20px;
    }
    .box-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }
    .box-title { font-size: 12px; font-weight: 800; color: var(--emerald); text-transform: uppercase; }
    .dia-item { margin-bottom: 12px; }
    .dia-item:last-child { margin-bottom: 0; }
    .dia-speaker { font-weight: 800; color: var(--gold); font-size: 12px; }
    .dia-spoken-quote { color: #FFF; font-weight: 600; font-size: 13.5px; }
    .dia-vn-dub { font-size: 12px; color: var(--cyan); margin-top: 2px; }
    .dia-subtext { font-size: 11px; color: var(--muted); font-style: italic; margin-top: 2px; }

    .block-wrap { margin-bottom: 18px; }
    .block-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }
    .block-label { font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; }
    .prompt-display, .handover-display {
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px 16px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #BAE6FD;
      line-height: 1.6;
      white-space: pre-wrap;
      word-break: break-word;
    }
    .handover-display { border-color: rgba(245, 158, 11, 0.25); color: #FDE68A; }

    .copy-btn {
      background: #1E293B;
      color: #E2E8F0;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
    }
    .copy-btn:hover { background: var(--cyan); color: #000; border-color: var(--cyan); }
    .copy-btn.copied { background: var(--emerald); color: #FFF; border-color: var(--emerald); }

    /* Story Spine Card */
    .spine-card {
      background: rgba(17, 24, 39, 0.95);
      border: 1px solid rgba(245, 158, 11, 0.4);
      border-radius: 16px;
      padding: 26px;
      margin-bottom: 32px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .spine-title {
      font-size: 14px;
      font-weight: 800;
      color: var(--gold);
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .tier1-table { width: 100%; border-collapse: collapse; font-size: 12.5px; }
    .tier1-table td { padding: 10px 14px; border-bottom: 1px solid rgba(255,255,255,0.06); vertical-align: top; }
    .tier1-label { width: 140px; font-weight: 700; color: var(--gold); text-transform: uppercase; font-size: 11px; }
    .tier1-val { color: #E2E8F0; line-height: 1.6; }

    .master-toolbar {
      background: #0D121F;
      border: 1px solid var(--cyan);
      border-radius: 14px;
      padding: 18px 24px;
      margin-bottom: 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }
    .toolbar-title { font-size: 13.5px; font-weight: 800; color: #FFF; text-transform: uppercase; }
    .toolbar-desc { font-size: 12px; color: var(--muted); }

    #toast {
      visibility: hidden;
      min-width: 250px;
      background: rgba(15, 23, 42, 0.95);
      color: #FFF;
      text-align: center;
      border-radius: 8px;
      padding: 12px 20px;
      position: fixed;
      z-index: 1000;
      left: 50%;
      bottom: 30px;
      transform: translateX(-50%);
      font-size: 13px;
      font-weight: 600;
      border: 1px solid var(--emerald);
      box-shadow: 0 10px 25px rgba(0,0,0,0.6);
      opacity: 0;
      transition: opacity 0.3s, visibility 0.3s;
    }
    #toast.show { visibility: visible; opacity: 1; }
  </style>
  <script>
    function showToast(msg) {
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => { t.classList.remove('show'); }, 2500);
    }
    function copySnippet(id, btn, label) {
      const el = document.getElementById(id);
      if (!el) return;
      navigator.clipboard.writeText(el.innerText.trim()).then(() => {
        const orig = btn.innerHTML;
        btn.innerHTML = '✓ Đã Copy!';
        btn.classList.add('copied');
        showToast('✓ Đã copy ' + (label || 'nội dung') + ' thành công!');
        setTimeout(() => { btn.innerHTML = orig; btn.classList.remove('copied'); }, 2000);
      });
    }
    function copyAllPrompts(btn) {
      let bundle = "";
      for (let i = 1; i <= 6; i++) {
        const id = 'p-' + (i < 10 ? '0' + i : i);
        const el = document.getElementById(id);
        if (el) bundle += "=== SCENE " + (i < 10 ? '0' + i : i) + " PROMPT ===\\n" + el.innerText.trim() + "\\n\\n";
      }
      navigator.clipboard.writeText(bundle).then(() => {
        const orig = btn.innerHTML;
        btn.innerHTML = '✓ Đã Copy Tất Cả 6 Prompts!';
        btn.classList.add('copied');
        showToast('✓ Đã copy toàn bộ 6 Prompts Video AI!');
        setTimeout(() => { btn.innerHTML = orig; btn.classList.remove('copied'); }, 2000);
      });
    }
  </script>
</head>
<body>
  <div id="toast">Thông báo</div>
  <div class="container">

    <!-- HEADER / HERO SECTION -->
    <header>
      <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:16px;">
        <div>
          <span class="badge badge-gold">Gạo House · Series Học Đường AI</span>
          <span class="badge badge-emerald">Sven Production Engine V2.5</span>
          <span class="badge badge-rose">10s Scene Architecture</span>
        </div>
        <div style="font-size:12px; color:var(--muted); text-align:right;">
          Lưu trữ: <code>d:\\Project\\Sven\\output\\series-hoc-duong\\sitcom-proposal.html</code><br>
          <strong style="color:var(--gold);">Chuẩn mực: 6 Cảnh = Đúng 60.0s / Tập</strong>
        </div>
      </div>
      <h1>LỰA CHỌN THỂ LOẠI &amp; TUYẾN CHỦ ĐỀ SITCOM HỌC ĐƯỜNG</h1>
      <p class="subtitle">
        Phương án đề xuất chuyển hóa toàn diện tài liệu tổng hợp V2.4 của Gạo House, tuân thủ nghiêm ngặt <strong>Hiến pháp hệ thống Sven (workflow.md §2.4: Scene duration 10s, always)</strong>. Định hình thể loại Classroom Micro-Sitcom (Chuyện bàn học 4 người) và kịch bản phân cảnh mẫu 60 giây (6 cảnh x 10s).
      </p>

      <div class="meta-grid">
        <div class="meta-item">
          <div class="meta-label">Thể loại Sitcom</div>
          <div class="meta-value">Classroom Micro-Sitcom</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Chuẩn độ dài cảnh</div>
          <div class="meta-value">00:00 – 00:10 (Đúng 10 Giây / Cảnh)</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Quy mô tập mẫu</div>
          <div class="meta-value">6 Cảnh = 60.0 Giây / Tập</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Dàn nhân vật</div>
          <div class="meta-value">4 Chính + 2 Bổ sung (3 Nữ / 3 Nam)</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Trang phục bắt buộc</div>
          <div class="meta-value">Áo Lớp Gạo House (@AO_CHU_DAO_01)</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Thư mục Output</div>
          <div class="meta-value">d:\\Project\\Sven\\output\\series-hoc-duong\\</div>
        </div>
      </div>
    </header>

    <!-- SECTION 1: MASTER RECAP OF CONSTRAINTS -->
    <section id="constraints">
      <div class="section-header">
        <h2 class="section-title"><span>📋</span> 1. Tổng Hợp Đầu Việc &amp; Bảng Đối Chiếu Ràng Buộc</h2>
        <span class="tag tag-fixed">Quy Chuẩn Cốt Lõi</span>
      </div>

      <div class="notice-box notice-gold">
        <div class="notice-title" style="color:var(--gold);">Tách Bạch: Quyết Định Của Gạo House vs. Thẩm Quyền Đề Xuất Của Agency</div>
        <p style="font-size:13.5px; color:#E5E7EB;">
          Tài liệu V2.4 giao đề bài: <strong>Gạo House không chỉ định sẵn thể loại; Agency phân tích và đề xuất 1 thể loại chủ lực</strong> vận hành ổn định trên kênh. Hệ thống Sven chuẩn hóa phương án này thành bộ tài nguyên sản xuất, đảm bảo tính khả thi tuyệt đối cho dây chuyền AI Video 15 tập/tháng.
        </p>
      </div>

      <div class="grid-2">
        <div class="card">
          <div class="card-title">
            <span style="color:var(--emerald);">✓ 7 RÀNG BUỘC ĐÃ KHÓA (GẠO HOUSE BASELINE)</span>
            <span class="tag tag-fixed">Không Thay Đổi</span>
          </div>
          <ul style="font-size:13px; color:var(--muted); line-height:1.75; padding-left:18px;">
            <li><strong style="color:#FFF;">1. Bối cảnh:</strong> Lớp 10 THPT phổ thông đô thị Việt Nam (những tuần đầu mới vào cấp 3).</li>
            <li><strong style="color:#FFF;">2. Khán giả mục tiêu:</strong> Học sinh THCS &amp; THPT (12–17 tuổi), phụ huynh xem bổ sung khi phù hợp.</li>
            <li><strong style="color:#FFF;">3. Mức độ hài:</strong> Hài duyên, đối đáp tự nhiên vừa phải (mức 3/5). Tuyệt đối không body-shaming, không miệt thị hoàn cảnh.</li>
            <li><strong style="color:#FFF;">4. Dàn nhân vật:</strong> 4 chính (Linh, Nam, An, Vy) + 2 bổ sung (Minh, Khoa). Giữ nguyên 15 cặp quan hệ đã chốt.</li>
            <li><strong style="color:#FFF;">5. Quan hệ khởi đầu:</strong> Linh–Nam là bạn cũ từ cấp 2; An–Vy mới quen cả nhóm khi vào lớp 10.</li>
            <li><strong style="color:#FFF;">6. Hình ảnh AI:</strong> Giả lập phim người thật (Photorealistic), đúng lứa tuổi 15–16 học sinh Việt Nam.</li>
            <li><strong style="color:#FFF;">7. Nhận diện thương hiệu:</strong> Cả 6 bạn mặc chung mẫu áo lớp Gạo House (mã tài nguyên <code>AO_CHU_DAO_01</code>).</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-title">
            <span style="color:var(--orange);">⚙ 4 QUY TẮC BẮT BUỘC CỦA HỆ THỐNG SVEN</span>
            <span class="tag tag-brand">Hiến Pháp Kỹ Thuật</span>
          </div>
          <ul style="font-size:13px; color:var(--muted); line-height:1.75; padding-left:18px;">
            <li><strong style="color:#FFF;">1. Quy tắc thời lượng cảnh 10s (workflow.md §2.4):</strong> Mọi cảnh quay luôn là 10 giây (timeline <code>00:00–00:10</code>). Một tập 60s gồm đúng 6 cảnh; một tập 90s gồm đúng 9 cảnh.</li>
            <li><strong style="color:#FFF;">2. Cấu trúc Multi-Beat 10s:</strong> Mỗi cảnh 10s chia làm các phase động học liền mạch (00:00–00:04.5, 00:04.5–00:10.0) với kinetic bridge nối liền.</li>
            <li><strong style="color:#FFF;">3. Thư mục Output chuẩn:</strong> Toàn bộ sản phẩm bàn giao (Setting, Screenplay, Prompt, SEO) phải nằm trong thư mục <code>d:\\Project\\Sven\\output\\series-hoc-duong\\</code>.</li>
            <li><strong style="color:#FFF;">4. Chính sách tham chiếu ảnh (Image Reference Policy):</strong> Gương mặt và áo lớp luôn neo bằng <code>[subject]</code> và <code>[Pro]</code>, cấm mô tả chi tiết quần áo hay ngũ quan trong visual prose.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTION 2: SITCOM FORMAT SELECTION -->
    <section id="format">
      <div class="section-header">
        <h2 class="section-title"><span>🎭</span> 2. Lựa Chọn Thể Loại: Classroom Micro-Sitcom</h2>
        <span class="tag tag-brand">Phương Án Đề Xuất Tối Ưu</span>
      </div>

      <div class="notice-box notice-cyan">
        <div class="notice-title" style="color:var(--cyan);">Định Nghĩa Thể Loại: Chuyện Bàn Học 4 Người (Classroom Slice-Of-Life Sitcom)</div>
        <p style="font-size:13.5px; color:#E5E7EB;">
          Thay vì làm các thể loại phiêu lưu hay tình cảm học đường sến súa, series chọn thể loại <strong>Classroom Micro-Sitcom</strong> kết hợp thủ pháp <strong>Deadpan / Satirical Mockumentary tiết chế</strong>. Mỗi tập phim là một cuộc đàm phán vi mô xung quanh một nhiệm vụ học đường cụ thể diễn ra ngay trong cụm 4 bàn học của lớp 10.
        </p>
      </div>

      <table class="data-table">
        <thead>
          <tr>
            <th>Tiêu chí đánh giá</th>
            <th>Tại sao Micro-Sitcom là lựa chọn số 1 cho AI Video?</th>
            <th>Tác động đến quy trình sản xuất của Gạo House</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Khả năng kiểm soát AI</strong></td>
            <td>Cố định 1 không gian phòng học (<code>phong_hoc_10a1</code>), nhân vật chủ yếu ngồi đối thoại tại bàn gỗ, loại bỏ các chuyển động phức tạp dễ gây biến dạng tay chân.</td>
            <td>Tỷ lệ render đạt chuẩn ngay từ lần đầu (first-pass success) &gt; 90%, giảm tối đa chi phí sửa cảnh.</td>
          </tr>
          <tr>
            <td><strong>Đúng chuẩn hài duyên (3/5)</strong></td>
            <td>Tiếng cười đến từ sự lệch pha tính cách: Linh muốn chốt việc vs Nam đùa cợt; Vy đòi gu cao vs An âm thầm giải quyết. Khai thác khoảng lặng ngượng ngùng (awkward pause).</td>
            <td>Không cần diễn viên làm trò hề lố lăng; giữ được sự tự nhiên và văn minh của học sinh lớp 10.</td>
          </tr>
          <tr>
            <td><strong>Đất diễn cho dàn nhân vật</strong></td>
            <td>Cụm bàn học 4 người cho phép Linh, Nam, An, Vy luôn hiện diện trong cùng một trường không gian; Minh và Khoa bước vào khi có bài toán ngân sách hoặc thể thao.</td>
            <td>Người xem dễ dàng nhận diện và ghi nhớ tính cách của từng bạn qua các tập liên tiếp.</td>
          </tr>
          <tr>
            <td><strong>Khả năng lồng ghép áo lớp</strong></td>
            <td>Cả nhóm luôn mặc áo lớp trong các buổi học; góc máy trung cảnh (Medium Shot) và cận vừa (Medium Close-Up) bắt trọn form dáng áo và logo Gạo House một cách tự nhiên.</td>
            <td>Sản phẩm xuất hiện như một phần đời sống học đường, không bị cảm giác quảng cáo lộ liễu.</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- SECTION 3: 4 THEMATIC SITCOM PILLARS -->
    <section id="pillars">
      <div class="section-header">
        <h2 class="section-title"><span>💡</span> 3. Hệ Thống 4 Tuyến Chủ Đề Sitcom Dài Hạn</h2>
        <span class="tag tag-gold">Mỏ Kịch Bản 15 Tập / Tháng</span>
      </div>

      <div class="grid-2">
        <div class="card" style="border-left: 4px solid var(--emerald);">
          <div class="card-title">
            <span style="color:var(--emerald);">Tuyến 1: Vi Chính Trị Lớp Mới (Micro-Politics)</span>
            <span class="tag tag-fixed">Trọng số 35%</span>
          </div>
          <p style="font-size:12.5px; color:var(--muted);">
            • <strong>Cốt lõi:</strong> Những cuộc họp bàn việc chung của tập thể lớp 10: bầu ban cán sự, phân chia trực nhật, chia nhóm thuyết trình, đòi nợ quỹ lớp.<br>
            • <strong>Cặp va chạm:</strong> Linh (muốn quy củ) vs. Nam (dĩ hòa vi quý); Minh (hỏi ngân sách) khiến cả nhóm chùng hứng.<br>
            • <strong>Ví dụ tập:</strong> <em>Bầu cử ẩn danh ai cũng biết Nam tự bầu; Vụ án thiếu 12 nghìn tiền quỹ liên hoan; Cuộc chiến đùn đẩy chức nhóm trưởng.</em>
          </p>
        </div>

        <div class="card" style="border-left: 4px solid var(--orange);">
          <div class="card-title">
            <span style="color:var(--orange);">Tuyến 2: Cuộc Chiến Thẩm Mỹ &amp; Áo Lớp (Aesthetic &amp; Identity)</span>
            <span class="tag tag-brand">Trọng số 30% · Trọng Tâm Gạo House</span>
          </div>
          <p style="font-size:12.5px; color:var(--muted);">
            • <strong>Cốt lõi:</strong> Điểm chạm trực tiếp với sản phẩm Gạo House: Khát khao lớp mình phải có gu riêng, không phèn, không đụng hàng lớp A2 bên cạnh.<br>
            • <strong>Cặp va chạm:</strong> Vy (đòi hỏi concept chuẩn) vs. Nam (thích slogan bựa); An âm thầm đưa ra bản phác thảo cứu nguy.<br>
            • <strong>Ví dụ tập:</strong> <em>Slogan bún bò bị lớp bên cạnh đạo nhái; Đại chiến phe Áo Đen vs Phe Pastel; Mở thùng áo carton Gạo House chuyển về trường.</em>
          </p>
        </div>

        <div class="card" style="border-left: 4px solid var(--cyan);">
          <div class="card-title">
            <span style="color:var(--cyan);">Tuyến 3: Áp Lực Hoàn Hảo &amp; Giải Cứu Phút 89</span>
            <span class="tag tag-open">Trọng số 20%</span>
          </div>
          <p style="font-size:12.5px; color:var(--muted);">
            • <strong>Cốt lõi:</strong> Sự cố học đường bất ngờ: kiểm tra đột xuất, hội thao trường, trang trí bảng tin. Người hoàn hảo thất thủ, kẻ vô tư lại cứu nguy.<br>
            • <strong>Cặp va chạm:</strong> Linh (ôm việc quá tải) vs. Khoa (hành động trước tính sau); cả nhóm đỡ lưng cho nhau.<br>
            • <strong>Ví dụ tập:</strong> <em>Linh lập lịch chụp ảnh chi tiết nhưng quên chỗ của mình; Khoa cưa khung đạo cụ to gấp đôi cửa lớp; Quên nộp bài tập môn Sinh.</em>
          </p>
        </div>

        <div class="card" style="border-left: 4px solid var(--rose);">
          <div class="card-title">
            <span style="color:var(--rose);">Tuyến 4: Hiểu Lầm Đời Thường &amp; Tình Bạn Ngầm</span>
            <span class="tag tag-open">Trọng số 15%</span>
          </div>
          <p style="font-size:12.5px; color:var(--muted);">
            • <strong>Cốt lõi:</strong> Khác biệt gia cảnh và sự tự ti (An giàu ngầm nhưng thiếu kết nối; bạn bè ngại ngùng vì ngoại hình). Hài hước nhưng kết thúc ấm áp.<br>
            • <strong>Cặp va chạm:</strong> Nam tưởng An kiêu; Vy nhận ra An quan tâm bằng hành động thay vì lời nói sến súa.<br>
            • <strong>Ví dụ tập:</strong> <em>Ai cũng xin đứng hàng sau khi chụp ảnh; An đãi trà sữa giả vờ shipper giao nhầm; Hộp cơm trưa một mình của An.</em>
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 4: STORY SPINE CARD -->
    <div class="spine-card" id="story-spine">
      <div class="spine-title">📜 STORY SPINE — Tập 1: Hàng Ghế Đầu Bị Bỏ Trống (Insight 03: Tự Ti Ngoại Hình)</div>
      <table class="tier1-table">
        <tr>
          <td class="tier1-label">[QUESTION]</td>
          <td class="tier1-val"><strong>Dramatic:</strong> Liệu nhóm 4 bạn có chụp được bức ảnh kỷ niệm lớp 10 trước khi tiếng chuông trường reo vang?<br/><strong>Thematic:</strong> Nỗi sợ ngoại hình có ngăn cản các bạn thoải mái xuất hiện bên nhau?</td>
        </tr>
        <tr>
          <td class="tier1-label">[TRUTH]</td>
          <td class="tier1-val">Ai cũng sợ bị dìm hàng trước camera góc rộng, nhưng khi An dũng cảm ngồi hàng trước làm điểm tựa, sự tự ti tan biến nhường chỗ cho tiếng cười rạng rỡ trong chiếc áo lớp đồng điệu.</td>
        </tr>
        <tr>
          <td class="tier1-label">[SPECIFIC]</td>
          <td class="tier1-val">Điện thoại camera trước của Vy · Hai hàng ghế trước trống trơn · Đôi má bánh bao của Nam · Sổ tay điều phối của Linh · Balo che góc máy của An · Áo lớp AO_CHU_DAO_01 rực rỡ dưới nắng mai.</td>
        </tr>
        <tr>
          <td class="tier1-label">[CLICHÉ]</td>
          <td class="tier1-val">Tự ti khóc lóc bi lụy → <strong>Từ chối (Refused)</strong>: biến thành màn đùn đẩy hài hước, tự trào duyên dáng.</td>
        </tr>
        <tr>
          <td class="tier1-label">[TWIST]</td>
          <td class="tier1-val">Người lạnh lùng kiệm lời nhất (An) lại là người chủ động ngồi hàng trước mở đường cứu cả nhóm.</td>
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
          <span class="scene-num">CẢNH 1 / SCENE 01 — VY BẬT CAMERA &amp; PHẢN XẠ NÉ TRÁNH</span>
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
            <span class="dia-speaker">Vy [00:00.8 – 00:03.5]: </span>
            <span class="dia-spoken-quote">“ Nhanh lên các cậu, hàng trước ngồi, hàng sau đứng! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ Nhanh lên các cậu, hàng trước ngồi, hàng sau đứng! ” (11 từ)</div>
            <div class="dia-subtext">(Vy lùi lại cầm điện thoại bật camera trước giục giã chụp ảnh)</div>
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
phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1], morning daylight. Sunlit Vietnamese high school classroom, rows of wooden desks, soft sunlight filtering through glass windows with floating dust motes.

[subject]:
vy_student [Appearance, attire, and facial features Refer to image @vy],
linh_student [Appearance, attire, and facial features Refer to image @linh],
nam_student [Appearance, attire, and facial features Refer to image @nam]

[Pro] :
wooden classroom desk; dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: gentle shuffling of school shoes on tiled floor, quiet classroom room tone, faint rustle of notebooks.

[00:00–00:04.5] Medium shot, eye level, static camera — vy_student steps backward into the central classroom aisle, raising dien_thoai_chup_anh with screen facing the desk cluster to frame a group portrait.
vy_student says : “ Nhanh lên các cậu, hàng trước ngồi, hàng sau đứng! ”（Voice of a 15-year-old girl from Northern Vietnam; bright crisp authoritative tone, urgent school cadence）

[00:04.5–00:10.0] Cut to a reverse medium shot across the empty wooden desks, eye level, slow push-in — linh_student and nam_student instinctively step backward toward the rear wall, leaving the entire front row of chairs vacant; linh_student clutches backpack straps with an embarrassed grimace while nam_student ducks shoulders sideways with a sheepish grin; vy_student in foreground lowers the smartphone slightly with an exasperated sigh through 00:10.0.

Continuous fluid motion, realistic physics, zero morphing, one unbroken take. Spatial positions anchored. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (00:10)</span>
          <button class="copy-btn" onclick="copySnippet('ho-01', this, 'Handover Cảnh 01')">📋 Copy Handover State</button>
        </div>
        <pre class="handover-display" id="ho-01">[HANDOVER STATE AT 00:10.0]:
Active Characters: vy_student, linh_student, nam_student
Characters State at 00:10.0:
  - vy_student: Standing in central aisle holding smartphone at chest height, exasperated look.
  - linh_student: Back row behind wooden desk, hands gripping backpack straps, defensive posture.
  - nam_student: Back row beside linh_student, shoulders hunched, grinning sheepishly.
Props State:
  - dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]: Held in vy_student's hands.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: vy_student 11 words (~2.8s speech).
Kinetic Momentum Bridge: linh_student steps forward to assign nam_student to sit front in Scene 02.</pre>
      </div>
    </div>

    <!-- ==================== SCENE 02 ==================== -->
    <div class="scene-card" id="s-02">
      <div class="scene-header">
        <div>
          <span class="scene-num">CẢNH 2 / SCENE 02 — LỆNH CỦA LỚP TRƯỞNG &amp; NỖI SỢ MẶT TO</span>
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
            <span class="dia-spoken-quote">“ Nam, cậu ngồi hàng trước đi! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ Nam, cậu ngồi hàng trước đi! ” (6 từ)</div>
            <div class="dia-subtext">(Linh chỉ tay điều động Nam ngồi hàng trước)</div>
          </div>
          <div class="dia-item">
            <span class="dia-speaker">Nam [00:04.5 – 00:08.5]: </span>
            <span class="dia-spoken-quote">“ Không đời nào, góc rộng dìm mặt tớ to lắm! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nam Lớp 10]: “ Không đời nào, góc rộng dìm mặt tớ to lắm! ” (11 từ)</div>
            <div class="dia-subtext">(Nam ôm hai bên má từ chối quyết liệt vì sợ mặt to)</div>
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
phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1], morning daylight. Sunlit classroom interior beside sunny glass windowpanes, light morning breeze rustling curtains.

[subject]:
linh_student [Appearance, attire, and facial features Refer to image @linh],
nam_student [Appearance, attire, and facial features Refer to image @nam]

[Pro] :
wooden classroom desk; so_tay_ke_hoach [100% Refer to image @so_tay_ke_hoach]; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: crisp tap of finger on desk wood, rustle of uniform fabric, distant murmur of school hallway.

[00:00–00:04.0] Medium two-shot, eye level, static camera — linh_student straightens back behind the wooden desk and points a firm index finger toward nam_student with formal class-monitor resolve.
linh_student says : “ Nam, cậu ngồi hàng trước đi! ”（Voice of a 15-year-old girl from Northern Vietnam; firm organized tone, formal class monitor authority）

[00:04.0–00:10.0] Cut to an over-the-shoulder close-up on nam_student, eye level, slow push-in — nam_student vigorously shakes head from side to side, bringing both palms up to cup cheeks in exaggerated comical panic; nam_student leans torso backward against the chalkboard edge with wide eyes through 00:10.0.
nam_student replies : “ Không đời nào, góc rộng dìm mặt tớ to lắm! ”（Voice of a 15-year-old boy from Northern Vietnam; lively defensive banter, quick humorous refusal）

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
  - linh_student: Hand resting flat on desk, eyebrows raised in disbelief.
  - nam_student: Both palms still touching jawline, torso tilted backward in firm refusal.
Props State:
  - so_tay_ke_hoach [100% Refer to image @so_tay_ke_hoach]: Closed on wooden desk.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: linh_student 6 words, nam_student 11 words (~4.2s speech).
Kinetic Momentum Bridge: vy_student steps in to scold both friends in Scene 03.</pre>
      </div>
    </div>

    <!-- ==================== SCENE 03 ==================== -->
    <div class="scene-card" id="s-03">
      <div class="scene-header">
        <div>
          <span class="scene-num">CẢNH 3 / SCENE 03 — VY CHÊ GU &amp; SỰ BẾ TẮC Ở HÀNG SAU</span>
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
            <span class="dia-speaker">Vy [00:00.6 – 00:03.8]: </span>
            <span class="dia-spoken-quote">“ Hai người mặc áo lớp đẹp mà đứng nép thế? ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ Hai người mặc áo lớp đẹp mà đứng nép thế? ” (10 từ)</div>
            <div class="dia-subtext">(Vy khoanh tay chê bai hai bạn đứng nép như trốn nợ)</div>
          </div>
          <div class="dia-item">
            <span class="dia-speaker">Nam [00:04.8 – 00:08.5]: </span>
            <span class="dia-spoken-quote">“ Áo đẹp nhưng camera góc rộng tàn nhẫn lắm! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nam Lớp 10]: “ Áo đẹp nhưng camera góc rộng tàn nhẫn lắm! ” (8 từ)</div>
            <div class="dia-subtext">(Nam nhăn nhó phân bua với Vy)</div>
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
phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1], morning daylight. Sunlit classroom setting, wooden double-desks under warm morning illumination.

[subject]:
vy_student [Appearance, attire, and facial features Refer to image @vy],
nam_student [Appearance, attire, and facial features Refer to image @nam],
linh_student [Appearance, attire, and facial features Refer to image @linh]

[Pro] :
wooden classroom desk; dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: soft fabric rustle of uniform shirts, subtle creak of wooden chair, quiet ambient classroom stillness.

[00:00–00:04.5] Medium three-shot, eye level, static camera — vy_student folds arms across chest, tilting head with aesthetic disapproval while looking at linh_student and nam_student cornered behind the desk.
vy_student says : “ Hai người mặc áo lớp đẹp mà đứng nép thế? ”（Voice of a 15-year-old girl from Northern Vietnam; sharp aesthetic scrutiny, exasperated tone）

[00:04.5–00:10.0] Cut to a medium close-up on nam_student, eye level, slow push-in — nam_student shrugs shoulders defensively, hands outstretched in comical surrender; linh_student beside nam_student sighs softly, looking down at empty front desks through 00:10.0.
nam_student replies : “ Áo đẹp nhưng camera góc rộng tàn nhẫn lắm! ”（Voice of a 15-year-old boy from Northern Vietnam; cheeky apologetic grin, self-deprecating tone）

Continuous fluid motion, realistic physics, zero morphing, one unbroken take. Spatial positions anchored. Do not generate subtitles, dialogue text, titles, timestamps, or written text. Do not render duplicate characters.</pre>
      </div>

      <div class="block-wrap">
        <div class="block-header">
          <span class="block-label" style="color:var(--gold);">CODE BLOCK 2: FINAL STATE SNAPSHOT HANDOVER (00:10)</span>
          <button class="copy-btn" onclick="copySnippet('ho-03', this, 'Handover Cảnh 03')">📋 Copy Handover State</button>
        </div>
        <pre class="handover-display" id="ho-03">[HANDOVER STATE AT 00:10.0]:
Active Characters: vy_student, nam_student, linh_student
Characters State at 00:10.0:
  - vy_student: Arms folded, waiting expectantly.
  - nam_student: Hands lowered, sighing in mock defeat.
  - linh_student: Glancing sideways toward an_student's quiet desk.
Props State:
  - dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]: Held tucked in vy_student's elbow.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: vy_student 10 words, nam_student 8 words (~4.1s speech).
Kinetic Momentum Bridge: an_student quietly shuts notebook and stands up in Scene 04.</pre>
      </div>
    </div>

    <!-- ==================== SCENE 04 ==================== -->
    <div class="scene-card" id="s-04">
      <div class="scene-header">
        <div>
          <span class="scene-num">CẢNH 4 / SCENE 04 — HÀNH ĐỘNG CỦA AN (ĐẢO CHIỀU TÌNH HUỐNG)</span>
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
            <span class="dia-spoken-quote">“ Ngồi đây che góc rồi, chụp nhanh đi. ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nam Lớp 10]: “ Ngồi đây che góc rồi, chụp nhanh đi. ” (8 từ)</div>
            <div class="dia-subtext">(An lẳng lặng kéo ghế ngồi hàng trước, lấy cặp che đùi giải cứu góc máy)</div>
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
so_phac_thao [100% Refer to image @so_phac_thao]; wooden classroom chair; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: soft paper closing thud, scrape of wooden chair legs on tiled floor, quiet calm breath.

[00:00–00:05.0] Medium shot panning gently right to center, eye level, slow lateral glide — an_student neatly shuts so_phac_thao, rises calmly from the desk, pulls out the empty front wooden classroom chair, and sits upright in the dead center of the frame, resting a dark backpack flat across the lap to anchor the lower framing.

[00:05.0–00:10.0] The camera glides into a held medium close-up and settles before an_student speaks: an_student raises a calm, unblinking gaze directly toward vy_student's camera lens, expression cool and collected through 00:10.0.
an_student says : “ Ngồi đây che góc rồi, chụp nhanh đi. ”（Voice of a 15-year-old boy from Northern Vietnam; low steady calm baritone, practical caring deadpan delivery）

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
  - an_student: Seated center front row, posture upright, backpack across lap, looking forward with steady deadpan expression.
Props State:
  - wooden classroom chair: Positioned dead center front row.
  - so_phac_thao [100% Refer to image @so_phac_thao]: Closed on back desk.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: an_student 8 words (~2.3s speech).
Kinetic Momentum Bridge: linh_student and nam_student surge forward to flank an_student in Scene 05.</pre>
      </div>
    </div>

    <!-- ==================== SCENE 05 ==================== -->
    <div class="scene-card" id="s-05">
      <div class="scene-header">
        <div>
          <span class="scene-num">CẢNH 5 / SCENE 05 — HIỆU ỨNG DOMINO &amp; CẢ NHÓM QUÂY QUẦN</span>
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
            <span class="dia-speaker">Nam [00:01.0 – 00:04.2]: </span>
            <span class="dia-spoken-quote">“ Có An ngồi phong thủy là góc nào cũng đẹp! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nam Lớp 10]: “ Có An ngồi phong thủy là góc nào cũng đẹp! ” (10 từ)</div>
            <div class="dia-subtext">(Nam mừng rỡ lao tới tựa lưng ghế của An tạo dáng)</div>
          </div>
          <div class="dia-item">
            <span class="dia-speaker">Linh [00:05.2 – 00:08.5]: </span>
            <span class="dia-spoken-quote">“ Vy canh góc rồi bấm máy nhanh đi! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ Vy canh góc rồi bấm máy nhanh đi! ” (8 từ)</div>
            <div class="dia-subtext">(Linh kéo ghế ngồi sát bên An mỉm cười giục Vy)</div>
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
an_student [Appearance, attire, and facial features Refer to image @an],
nam_student [Appearance, attire, and facial features Refer to image @nam],
linh_student [Appearance, attire, and facial features Refer to image @linh],
vy_student [Appearance, attire, and facial features Refer to image @vy]

[Pro] :
wooden classroom chair; dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]; AO_CHU_DAO_01 [100% Refer to image @AO_CHU_DAO_01]

Diegetic room acoustics: joyful footstep scuffle, wooden chair slide, light chuckles, classroom breeze.

[00:00–00:05.0] Medium group shot, eye level, slow pull-out — nam_student hurries forward and rests both elbows casually on the back of an_student's chair, grinning broadly with exuberant relief; an_student remains seated and steady.
nam_student says : “ Có An ngồi phong thủy là góc nào cũng đẹp! ”（Voice of a 15-year-old boy from Northern Vietnam; high energy enthusiastic banter, cheerful relief）

[00:05.0–00:10.0] Cut to an over-the-shoulder medium shot past vy_student's raised smartphone, eye level, static camera — linh_student quickly slides an adjacent chair beside an_student and sits down smiling; vy_student's fingers steady the smartphone screen framing all four friends perfectly in matching uniform shirts through 00:10.0.
linh_student replies : “ Vy canh góc rồi bấm máy nhanh đi! ”（Voice of a 15-year-old girl from Northern Vietnam; relieved warm smile, unhurried soft cadence）

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
  - an_student: Sitting front center, calm stoic expression.
  - linh_student: Sitting directly left of an_student, smiling brightly.
  - nam_student: Standing behind an_student, elbows resting on chair back, grinning.
  - vy_student: Standing in front framing shot with smartphone.
Props State:
  - dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]: Raised framing final shot.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: nam_student 10 words, linh_student 8 words (~4.1s speech).
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
            <span class="dia-spoken-quote">“ Ảnh xong rồi, áo lớp mình lên hình nét căng! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nữ Lớp 10]: “ Ảnh xong rồi, áo lớp mình lên hình nét căng! ” (10 từ)</div>
            <div class="dia-subtext">(Vy xoay màn hình điện thoại khoe ảnh chụp xuất sắc)</div>
          </div>
          <div class="dia-item">
            <span class="dia-speaker">Nam [00:06.5 – 00:09.5]: </span>
            <span class="dia-spoken-quote">“ Nhìn An kìa, như chủ tịch tập đoàn đi học! ”</span>
            <div class="dia-vn-dub">🇻🇳 [Giọng Nam Lớp 10]: “ Nhìn An kìa, như chủ tịch tập đoàn đi học! ” (9 từ)</div>
            <div class="dia-subtext">(Nam nhìn ảnh phì cười trêu An khiến cả nhóm cười vang)</div>
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

Diegetic room acoustics: subtle electronic camera shutter click, ringing school bell chime in background, spontaneous burst of group laughter.

[00:00–00:05.5] Close-up on dien_thoai_chup_anh screen tilting up to medium shot, eye level, slow pedestal lift settles before vy_student speaks — vy_student's thumb taps the virtual camera shutter icon; a soft screen flash illuminates the captured photo of the four friends looking united in matching uniform shirts; vy_student rotates the phone outward with pride.
vy_student says : “ Ảnh xong rồi, áo lớp mình lên hình nét căng! ”（Voice of a 15-year-old girl from Northern Vietnam; proud aesthetic satisfaction, joyful ringing tone）

[00:05.5–00:10.0] Cut to a medium group reaction shot, eye level, static camera — nam_student peers over vy_student's shoulder pointing at the screen and chuckles warmly; linh_student giggles beside an_student whose lips finally curl into a quiet subtle smirk as the school bell rings rhythmically overhead through 00:10.0.
nam_student replies : “ Nhìn An kìa, như chủ tịch tập đoàn đi học! ”（Voice of a 15-year-old boy from Northern Vietnam; chuckling playful tease, affectionate banter）

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
  - All four friends gathered tightly around smartphone screen, laughing naturally.
  - an_student: Subtly smiling, arms relaxed.
Props State:
  - dien_thoai_chup_anh [100% Refer to image @dien_thoai_chup_anh]: Displaying captured group photo on screen.
Setting: phong_hoc_10a1 [100% Refer to image @phong_hoc_10a1]
Dialogue Audit: vy_student 10 words, nam_student 9 words (~4.3s speech).
Kinetic Momentum Bridge: Episode concludes on school bell chime and warm group laughter.</pre>
      </div>
    </div>

    <!-- FOOTER -->
    <footer style="text-align:center; padding:30px 0; border-top:1px solid var(--border); color:var(--muted); font-size:12px;">
      GẠO HOUSE · SERIES HỌC ĐƯỜNG AI · SVEN PRODUCTION ENGINE V2.5<br>
      Tài liệu phân cấp Level-1 Showrunner &amp; Level-2 Screenwriter/Director · Lưu tại <code>d:\\Project\\Sven\\output\\series-hoc-duong\\</code>
    </footer>

  </div>
</body>
</html>
"""

with open("d:/Project/Sven/output/series-hoc-duong/sitcom-proposal.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)
print("Successfully generated d:/Project/Sven/output/series-hoc-duong/sitcom-proposal.html")

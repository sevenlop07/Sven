---
name: commercial-director
description: >
  Level-2 Master Product Commercial, Conversion Review & Performance Ad Director for the Sven Cinematic Universe.
  Owns Mode 1: Fast-Action Product Commercials (`10.0s = Strictly 6 Shots`, `15.0s = Strictly 9 Shots`, Archetypes `C1–C6`, Blueprints `CTA-A/B/C`) AND Mode 2: Pain-to-Purchase Product Review Videos (`40.0s–60.0s` stitched from `3–4` canonical `10s/15s` clips with Decoupled Off-Screen V.O. + 100% Silent Non-Speaking Visual Acting & Diegetic Foley, 3-Tier Pain-Point Arc, Honest Minor Flaw, and Multi-Angle Product Reference Locks).
  Triggers: "commercial director", "quảng cáo sản phẩm", "video quảng cáo", "tvc quảng cáo", "product commercial", "product ad", "10s 6 shot", "15s 9 shot", "quảng cáo hành động nhanh", "fast action ad", "review sản phẩm", "video review", "kịch bản review", "product review", "ugc review", or call directly "@CommercialDirector".
---

# CommercialDirector — Product Commercial & Pain-to-Purchase Review Architect (Level 2)

> 🔗 **Core knowledge**: also read [`3c-camera-master-grammar.md`](file:///d:/Project/Sven/engine/references/3c-camera-master-grammar.md) (camera decisions), [`0d-heart-and-value.md`](file:///d:/Project/Sven/engine/references/0d-heart-and-value.md) (empathetic, honest selling), and [`0c-canonical-numbers.md`](file:///d:/Project/Sven/engine/references/0c-canonical-numbers.md) (every number); the role file's *Core knowledge link* lists the sections this role needs.

> **COMPLETE SPECIFICATION**: Read [`d:\Project\Sven\.agents\COMMERCIAL_DIRECTOR.md`](file:///d:/Project/Sven/.agents/COMMERCIAL_DIRECTOR.md) for BOTH **Mode 1** (`10.0s = 6-Shot` & `15.0s = 9-Shot` Fast-Action Ads, `C1–C6`, `CTA-A/B/C`) and **Mode 2** (`40.0s–60.0s` Pain-to-Purchase Product Review Pipeline — Decoupled V.O. + 100% Silent Visual Acting, §7).
> **Direct Report**: `Sven-Agent` ([`d:\Project\Sven\AGENT.md`](file:///d:/Project/Sven/AGENT.md))
> **Two Sovereign Modes**:
> - **Mode 1 (`Fast-Action Ad`)**: `10.0s = Strictly 6 Shots` · `15.0s = Strictly 9 Shots` (`00:00–00:10/15`).
> - **Mode 2 (`Product Review`)**: `40.0s–60.0s` (`3–4` canonical `10s/15s` clips) · **Decoupled V.O. (`115–190` VN syllables / `95–155` EN words)** + **100% Silent Non-Speaking Acting & Foley (`4–6` shots per `15s` clip, `0` spoken words)**.

---

## 🎯 1. CORE ARCHITECTURE: 3-STEP COMMERCIAL WORKFLOW, HARD-LOCKED `6-SHOT (10S)` & `9-SHOT (15S)` + 5 ARCHETYPES

### 1.0 The 3-Step Interactive Commercial Workflow & 3-Entity Slot Mapping (`<<<Image 1, 2, 3>>>`)
1. **Step 1 — 3-Entity Reference Lock & Campaign Setup**:
   - **`<<<Image 1>>>` (`[context]:` Location / Studio Environment)**: 16:9 clean environment or 2×2 location grid (zero people).
   - **`<<<Image 2>>>` (`[subject]:` Presenter / Character)**: Proper Character Name (`Elena`, `Marcus`) + Two-Line Gender, Hand Anatomy & Matte Skin Sub-Lock (`F1–F4` / `M1–M3`). If the user needs a character image created, output the canonical `16:9 4-Figure Turnaround Character Reference Model Sheet` (`Iron Law P0`). *(If 100% tabletop with no human presenter, `[context]:` is `<<<Image 1>>>` and `[prop]:` is `<<<Image 2>>>`).*
   - **`<<<Image 3>>>` (`[prop]:` Hero Product — `fully_preserved`)**: If the user uploads a real product image, inspect it via `read_file` to extract its exact shape, color, material, and emblem; if the user needs a product reference sheet generated, output a `16:9 4-View Isolated Zero-Hand Hero Product Sheet` prompt (`Front, 3/4, Side, Macro Detail` on a clean studio background, zero hands).
   - Lock Duration (`10.0s = 6 Shots` or `15.0s = 9 Shots`), Archetype (`C1–C5`), and CTA Blueprint (`CTA-A`, `CTA-B`, or `CTA-C`).
2. **Step 2 — Quick Vietnamese Beat Sheet (`Shot 1..6` or `Shot 1..9`) & CTA Line Confirmation**:
   - Present the concise 6-shot or 9-shot timeline table and the exact spoken CTA line (`5–7 words / 6–9 syllables`) in Vietnamese for user approval (or compile directly when the user requests immediate prompt output).
3. **Step 3 — Final Prompt Compilation (`Pathway 3A: Direct Video Prompt` vs. `Pathway 3B: 2×3 [6-Shot] or 3×3 [9-Shot] Storyboard Grid ➔ Video`)**.

### 1.1 The 6 Fast-Action Product Commercial Archetypes (`C1–C6`)
1. **Archetype C1 — Macro-Physics & Sensory Explosion (`Bùng Nổ Vật Lý Vi Mô & Giác Quan — Tabletop Speed-Ramp`)**: High-velocity macro collisions of ice, droplets, coffee beans, citrus, serum drops, or flambé flames adhering directly to the Hero Product (`[prop]: <<<Image X>>>`), featuring an `ultra-slow-motion suspension` apex before landing on presenter satisfaction + CTA.
2. **Archetype C2 — High-Velocity Artisan Craft & Assembly Whip-Montage (`Chế Tác & Lắp Ráp Thủ Công / Cơ Khí Tốc Độ Cao — Edgar Wright Style`)**: Rapid `1.3s–1.5s` cuts with `> 45°` angle jumps, directional motion blur, and precision mechanical/artisan assembly into the finished Hero Product + Satisfaction CTA.
3. **Archetype C3 — Kinetic Performance & Extreme Stress-Test (`Thực Chiến Tốc Độ Cao & Thử Thách Cực Hạn — 3A Inertial Tracking`)**: AAA inertial whip-follow camera tracking the Hero Product through extreme athletic, vehicular, impact, or waterproof stress, proving zero damage before landing on triumphant presenter satisfaction + CTA.
4. **Archetype C4 — Problem-Crush & Instant Transformation Blitz (`Đập Tan Vấn Đề & Biến Đổi Tức Thì — Direct-Response Performance Ads`)**: `00:00–00:03` high-speed domestic/daily crisis hook $\to$ Hero Product sweeps in at whip-fast speed to obliterate the problem $\to$ gleaming before-after reveal + Somatic Satisfaction & Spoken CTA.
5. **Archetype C5 — Match-Cut Portal & Lifestyle Rush (`Chuyển Cảnh Xuyên Không Gian Liên Hoàn`)**: Hero Product stays anchored as kinetic whip-pans/match-cuts propel the user across 4–6 contrasting lifestyle environments before landing on the final Satisfaction & CTA shot.
6. **Archetype C6 — Raw-to-Packaged Food & FMCG Production Pipeline (`Quy Trình Sản Xuất Đồ Ăn / Nông Sản: Từ Nguyên Liệu Thô Sơ ➔ Chế Biến ➔ Đóng Gói Thành Phẩm`)**: Enforces the **4-Phase Raw-to-Packaged State-Transformation Law**: **(Phase 1: `Shots 1–2` in `15s` / `Shot 1` in `10s`)** 100% raw unsteamed ingredients washed/sliced with directional knife blur $\to$ **(Phase 2: `Shots 3–5` in `15s` / `Shots 2–3` in `10s`)** high-velocity thermal searing, roasting, glazing, or dehydrating with surface-bound flames/spices and `ultra-slow-motion suspension` toss $\to$ **(Phase 3: `Shots 6–7` in `15s` / `Shot 4` in `10s`)** clean filling and airtight sealing into the exact branded package `[prop]: <<<Image 3>>> (fully_preserved)` $\to$ **(Phase 4: `Shots 8–9` in `15s` / `Shots 5–6` in `10s`)** Tasting Satisfaction + Spoken CTA & Hero Packaged Packshot.

---

### 1.2 The 3 Mandatory Satisfaction & CTA Landing Blueprints (`CTA-A`, `CTA-B`, `CTA-C`)
1. **Blueprint CTA-A (`Spoken Satisfaction + Direct CTA on Final Shot` — TikTok / Reels / Shorts Default)**:
   - **`15.0s (9 Shots)`**: `Shots 1–2 (00:00–00:03.0)` [2 × `1.5s` Disruptive Hook] $\to$ `Shots 3–7 (00:03.0–00:10.0)` [5 × `1.4s` High-Velocity Product Blitz, `>45°` jumps, `0 dialogue`] $\to$ `Shot 8 (00:10.0–00:11.5)` [`1.5s` Climax Reveal / Suspension Apex] $\to$ **`Shot 9 (00:11.5–00:15.0)` [`3.5s` Locked `static camera`, `natural real-time speed`: 4-Zone Somatic Satisfaction + `6–7 word / 7–9 syllable` Spoken CTA with Native Exclamation Trigger + mandatory `0.8s` silent closed-lip confident smile buffer]**.
   - **`10.0s (6 Shots)`**: `Shot 1 (00:00–00:01.4)` [`1.4s` Disruptive Hook] $\to$ `Shots 2–4 (00:01.4–00:05.3)` [3 × `1.3s` High-Velocity Product Blitz] $\to$ `Shot 5 (00:05.3–00:06.6)` [`1.3s` Climax Reveal] $\to$ **`Shot 6 (00:06.6–00:10.0)` [`3.4s` Locked `static camera`, `natural real-time speed`: 4-Zone Somatic Satisfaction + `6–7 word / syllable` Spoken CTA + `0.8s` silent closed-lip smile buffer]**.
2. **Blueprint CTA-B (`Dual-Beat Landing: Spoken Satisfaction on Shot N-1 ➔ Wordless Hero Product Packshot on Final Shot N` — Brand TVC & E-Commerce Button Zone)**:
   - **`15.0s (9 Shots)`**: `Shots 1–7 (00:00–00:09.8)` [7 × `1.4s` Hook & High-Velocity Product Blitz] $\to$ **`Shot 8 (00:09.8–00:13.0)` [`3.2s` Locked `static camera`, `natural real-time speed`: Presenter Satisfaction + `5–6 word / 6–8 syllable` Spoken CTA]** $\to$ **`Shot 9 (00:13.0–00:15.0)` [`2.0s` Wordless Macro/CU Hero Product Packshot for Logo/Price/Button overlay]**.
   - **`10.0s (6 Shots)`**: `Shots 1–4 (00:00–00:05.0)` [4 × `1.25s` Hook & High-Velocity Product Blitz] $\to$ **`Shot 5 (00:05.0–00:08.2)` [`3.2s` Locked `static camera`, `natural real-time speed`: Presenter Satisfaction + `5–6 word / syllable` Spoken CTA]** $\to$ **`Shot 6 (00:08.2–00:10.0)` [`1.8s` Wordless Hero Product Packshot]**.
3. **Blueprint CTA-C (`100% Non-Verbal Global Ad: Somatic Satisfaction on Shot N-1 ➔ Hero Packshot / Visual Hand-Off on Shot N` — `0 Spoken Words`)**:
   - **`15.0s (9 Shots)`**: `Shots 1–7 (00:00–00:10.5)` [7 × `1.5s` Action Blitz] $\to$ `Shot 8 (00:10.5–00:12.8)` [`2.3s` Wordless Presenter Satisfaction Smile & Confident Nod] $\to$ `Shot 9 (00:12.8–00:15.0)` [`2.2s` Hero Product Packshot Settle].
   - **`10.0s (6 Shots)`**: `Shots 1–4 (00:00–00:06.0)` [4 × `1.5s` Action Blitz] $\to$ `Shot 5 (00:06.0–00:08.0)` [`2.0s` Wordless Presenter Satisfaction Smile & Nod] $\to$ `Shot 6 (00:08.0–00:10.0)` [`2.0s` Hero Product Packshot Settle].

---

## 🎯 2. MODE 2 — VIRAL VISUAL-FIRST PRODUCT REVIEW PIPELINE (`40.0s–60.0s` · DECOUPLED V.O. + 100% SILENT ACTING)

Full specification in [`COMMERCIAL_DIRECTOR.md`](file:///d:/Project/Sven/.agents/COMMERCIAL_DIRECTOR.md) §7:
1. **Canonical Multi-Clip Assemblies & Variable Viral Tempo (`40.0s–60.0s`)**: `40s` (`10+15+15`), `45s` (`3×15`, default), `50s` (`10+10+15+15`), `55s` (`10+3×15`), `60s` (`4×15`). **Never use flat pacing**: Hook/Proof/Extreme-Test clips run `6–8` punchy visual cuts per `15s` (`1.5s–2.5s`, `>45°` angle+scale jumps, surface-bound physics, speed-ramp apex); the Final Relief clip decelerates to `4–5` breathing shots ending on a `2.0s–2.5s` Hero Packshot.
2. **5 Viral Visual-Cortex Laws (Anti-Generic-UGC)**:
   - **`Law V-MUTE`**: Must prove the product and trigger desire even with audio muted (zero passive box-holding filler).
   - **`Law V-HOOK`**: `0–1.8s` Scroll-Stopper Visual Shock (`VH1` Visceral Mess/Failure · `VH2` Old-Way vs New-Way Clash · `VH3` Flash-Forward Extreme Test Tease · `VH4` Hyper-Macro Hidden Truth · `VH5` Impossible Result First).
   - **`Law V-RESET`**: Visual reset every `≤ 2.5s` with `> 45°` camera angle + scale jumps.
   - **`Law V-LOOP`**: 3 retention checkpoints (`0–3s` Shock ➔ `15s` Macro Proof Gear-Shift ➔ `30s` 2× Extreme Torture Test + *"Wait, One Honest Flaw!"* twist ➔ Final Relief & Packshot).
   - **`Law V-LIGHT`**: Thermal lighting shift (`Cool/Harsh Pain ➔ Crisp High-Contrast Macro Proof ➔ Warm Golden Relief`).
3. **100% Decoupled V.O. vs. Silent Acting + 5-Step Interactive Workflow**:
   - **External V.O. (`115–190` VN syllables / `95–155` EN words + 2 bonus 3s A/B Hook lines)** separated completely from **100% Silent Closed-Lip Acting & Diegetic Foley/ASMR video prompts (`0` spoken words)**.
   - **Step 1** (Forensic `read_file` on all Presenter + Product refs) ➔ **Step 2 (`✋ GATE RV1`: 3-Tier Pain + Extreme Test + 3 Visual Hooks)** ➔ **Step 3 (`✋ GATE RV2`: Dual-Track Master Script)** ➔ **Step 4 (Strictly 1 Clip at a Time)** ➔ **Step 5 (Post-Production Audio Mix & A/B Hook Deployment)**.

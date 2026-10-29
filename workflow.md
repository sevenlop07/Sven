# WORKFLOW — Sven Production Engine (Master Operating Pipeline)

> ⚠️ **READ THIS ENTIRE FILE FIRST — EVERY SESSION, BEFORE ANY ACTION.**
> This file is the pipeline coordinator. Detailed craft rules live ONLY in the 4 Master Pillars; this file links to them instead of copying them.

---

## §0 — FILE READING ORDER (SINGLE CANONICAL LIST)

```
[1] workflow.md                                   ← This file (pipeline, System Defaults, checkpoints)
[2] AGENT.md                                      ← Level 1: Executive Producer & Showrunner (identity, routing, compliance)
[2b] engine/runbooks.json                         ← Production Presets & Runbooks Catalog (1-click project initialization)
[3] history-registry.json                         ← 14-axis anti-repetition memory
[4] .agents/SCREENWRITER.md                       ← Level 2: Screenwriter (load at Stages 0–3)
[5] .agents/DIRECTOR.md                           ← Level 2: Director (load at Stage 4)
[6] .agents/skills/youtube-growth-architect/SKILL.md ← Growth Architect (load at Stages 0 and 5)
─── THE THINKING LAYER (load at Stages 0 and 2–4, BEFORE any Pillar) ───
[7]  engine/references/0-creative-doctrine.md                   ← Creative Doctrine: intent → choice → reason
[7b] engine/references/0b-temporal-camera-grammar.md            ← Temporal & Camera Grammar: every timing number + canonical prompt syntax
─── THE 4 MASTER PILLARS & SPECIALIZED DIRECTORIAL ASSISTANTS ───
[8]   engine/references/1-narrative-screenplay-architecture.md   ← Pillar 1 SSOT
[9]   engine/references/2-casting-worldbuilding-specification.md ← Pillar 2 SSOT
[10]  engine/references/3-cinematography-3d-staging.md           ← Pillar 3 SSOT (incl. Music Video rules)
[10b] engine/references/3b-lighting-atmospheric-physics.md       ← Assistant: 6-Point Lighting Contract & Atmosphere
[11]  engine/references/4-ai-video-prompt-compiler.md            ← Pillar 4 SSOT
[11b] engine/references/4b-diegetic-foley-sound-design.md        ← Assistant: Code Block 2 Diegetic Foley & Sound Design
```

> **Golden Rule of Pre-Flight Verification**: never draft a stage output from memory. Open the Creative Doctrine and the Temporal & Camera Grammar (Stages 2–4), then the governing Pillar with `view_file` first.

---

## §1 — AUTHORITY MATRIX (ONE OWNER PER DOMAIN)

| Domain | File | Owns | Stages |
|---|---|---|---|
| Pipeline | [`workflow.md`](file:///d:/Project/Sven/workflow.md) | Stages 0–5, checkpoints, System Defaults (§2) | All |
| Showrunner | [`AGENT.md`](file:///d:/Project/Sven/AGENT.md) | Identity, delegation, compliance gatekeeping | All |
| Registry | [`history-registry.json`](file:///d:/Project/Sven/history-registry.json) | 14-axis anti-repetition memory | K1, CP1, CP5 |
| Doctrine | [`0-creative-doctrine.md`](file:///d:/Project/Sven/engine/references/0-creative-doctrine.md) | Story Spine (§8), Plot Engine (§9), 4 Cinema Tiers & 12 Master Devices (§10), Dynamic Script Calibration Protocol (§10.4), Scene Intent Engine, directing from intent (scale / angle / movement / action), Action↔Line relationships, per-scene Voice Mode Palette, Creative Review | 0, 2, 3, 4 |
| Grammar | [`0b-temporal-camera-grammar.md`](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md) | Speech rate (VN syllables / EN words per second), lip-sync windows, action capacity, camera-move durations and lip-sync safety, shots per clip, clip density, canonical prompt syntax, 10s / 15s / 30s duration modes | 3, 4 |
| Pillar 1 | [`1-narrative-screenplay-architecture.md`](file:///d:/Project/Sven/engine/references/1-narrative-screenplay-architecture.md) | 6-Beat / 18 sub-beats, 12 hooks, 20 twists (TW-01–TW-20), 3-wave climax, 8-model dialogue suite, WPS cadence, 4-in-1 parentheticals, Positive & Zero-Fatality Mandate | 0, 2, 3 |
| Pillar 2 | [`2-casting-worldbuilding-specification.md`](file:///d:/Project/Sven/engine/references/2-casting-worldbuilding-specification.md) | Cast topology (A1/A2/B/C), archetypes, naming matrix, Living Continuum, **model / prop / location sheet templates**, `setting.html` sections, visual style encyclopedia | 1, 3 |
| Pillar 3 | [`3-cinematography-3d-staging.md`](file:///d:/Project/Sven/engine/references/3-cinematography-3d-staging.md) | 14 scales, 6 angles, 7 combos, 3D staging, elastic deformation, 180° axis, continuity ledgers, Music Video architecture | 4 |
| Pillar 4 | [`4-ai-video-prompt-compiler.md`](file:///d:/Project/Sven/engine/references/4-ai-video-prompt-compiler.md) | 10s kinetic unit, Track A/B, Mode B laws, Code Block 1/2 spec, `tap-X.html` spec, minor-safety protocol | 4 |
| Growth | [`SKILL.md`](file:///d:/Project/Sven/.agents/skills/youtube-growth-architect/SKILL.md) | Niche validation, entity clusters, titles, thumbnails, `seo-youtube.html` | 0, 5 |
| Engine | `engine/prompt_compiler.py`, `engine/episode_audit_suite.py`, `engine/setting_audit_suite.py` | Deterministic compile + automated gates | 1, 4 |

### Role Assignment per Stage (RACI)

| Stage | Responsible (executes) | Accountable (approves before user) | Deliverable |
|---|---|---|---|
| 0 — Concepts | Screenwriter + Growth Architect | Sven-Agent | 5 concepts |
| 1 — Pre-Production | Screenwriter (Director reviews location staging) | Sven-Agent | `setting.html` Phase A |
| 2 — Blueprint | Screenwriter | Sven-Agent | Short-film spine or series 4-act blueprint |
| 3 — Screenplay + Roadmap | Screenwriter | Sven-Agent | Episode screenplay + `setting.html` Phase B (Section 5 scene roadmap) |
| 4 — Prompt Production | Director | Sven-Agent | `tap-X.html` (full episode) |
| 5 — Distribution | Growth Architect | Sven-Agent | `seo-youtube.html` |

> **Legacy label mapping**: role files and skills may still use older labels. Map them as follows: "Stage 1B Casting" → Stage 1 (§6.2); "Stage 1C Screenplay" → Stage 3; "Stage 1E setting.html" → Stage 1 + Stage 3 Phase B; "Stage 2 10s Breakdown" and "Stage 3 3D Blocking" (Director) → Stage 4 internal steps. The Story Spine is written at Stage 2 (series / short-film Spine) and refreshed per episode at Stage 3. **This file's numbering wins.**

---

## §2 — SYSTEM DEFAULTS (THE CONSTITUTION)

> These decisions override any conflicting text in Pillars, role files, skills, or examples. If you find a conflict, follow this section and report the conflicting file to the user for cleanup.

### 2.1 Rule Precedence
1. Explicit user instruction in the current session
2. `workflow.md` §2 System Defaults (Hard Constraints never yield to anything below this line)
3. `engine/references/0-creative-doctrine.md` — decides HOW craft tools are chosen. It overrides fixed timings, word budgets, shot quotas, mandatory address words, and "always / strictly" craft language in Pillars, role files, and skills. It never overrides a Hard Constraint (§2.10). `engine/references/0b-temporal-camera-grammar.md` sits at the same level and is the only source for timing numbers and prompt syntax.
4. Pillars 1–4 (each within its own domain, §1) — catalogs of tools and examples
5. Role files (`AGENT.md`, `.agents/DIRECTOR.md`, `.agents/SCREENWRITER.md`)
6. Skills, examples, legacy templates

### 2.2 Language Protocol (3 Layers)
- **User communication**: always Vietnamese; direct, decisive, executive tone.
- **System files** (`.md` rules, skills, references, code comments): always professional English.
- **Inside deliverables** (`setting.html`, `tap-X.html`, `seo-youtube.html`):
  - **Layer 1 — UI and informational content**: Vietnamese. This covers titles, Director's Lock, scene audit cards, dialogue breakdown cards, buttons, toasts, and the Code Block 2 handover.
  - **Layer 2 — Technical visual prose in Code Block 1**: technical cinematic English.
  - **Layer 3 — Spoken dialogue**: English by default. When the user targets a country or language (e.g., a Vietnamese family drama), dialogue switches 100% to that language and regional dialect. The parenthetical then directs the matching visemes.
- **Character naming**:
  - English-dialogue productions: 1-syllable English proper nouns with no vocabulary meaning (`Lok`, `Keth`, `Mael`).
  - Target-language productions: culturally native names drawn from the Pillar 2 6-Cultural Naming Matrix (e.g., `Má Ba`, `Tư Lành`).
  - Stage 0 always shows Vietnamese names for readability.

### 2.2b Aspect Ratio Sovereignty Law (Quyền Tối Thượng Của Người Dùng Về Khung Hình)
- **100% User-Governed**: The aspect ratio (16:9 widescreen, 9:16 vertical, 4:3, 1:1, or 2.39:1 anamorphic) is ALWAYS dictated by the user's explicit preference and target distribution channel.
- **Zero Rigid Binding**: Strictly ban hard-coding or locking an aspect ratio to any genre. A microdrama can be shot in 16:9 for YouTube/OTT; a cinematic healing drama can be shot in 9:16 for mobile vertical platforms. Presets in `engine/runbooks.json` suggest defaults, but the Director and Screenwriter must adapt camera staging, optical headroom, and blocking dynamically to ANY frame ratio the user selects.

### 2.3 Project Mode & Per-Scene Voice Mode
| Project mode | Activation | Rule |
|---|---|---|
| ⭐ **Dialogue-Driven Drama** | **DEFAULT** for every film and series | Spoken drama is the backbone, but the **voice mode is chosen per scene** from the Creative Doctrine §4 palette: dialogue, ensemble, solo line, direct monologue, inner V.O., hybrid spoken + V.O., off-screen voice, whisper, interrupted, direct address, or silence. Each choice carries a one-clause reason in the Scene Intent Card (§8.3). Drama beats stay conflict-dense; monologue and silence are used where they hit harder. |
| 🤫 Silent Film (Show, Don't Tell) | ONLY when the user explicitly chooses silent / "không thoại" for the whole project | Zero dialogue in every scene, amplified micro-biomechanics, diegetic Foley, silent negative clause (§9.4) |
| 🎵 Music Video | User provides lyrics, a song duration, or "MV mode" | Pillar 3 Music Video architecture |

- A silent scene, a monologue scene, or a V.O. scene inside a dialogue project is a normal creative choice, not a project-mode change. It needs only its one-clause reason.
- Episode rhythm (Doctrine §4.1): avoid 3+ consecutive scenes in the same voice mode, or every scene with the same turn count, unless the repetition is the point.

### 2.3b Master Genre Library (`engine/genres/`)
In addition to the overarching Project Mode (Dialogue vs. Silent vs. MV), productions can invoke specialized genres from the Master Genre Library (`engine/genres/README.md`):
- **Sitcom Engine ([`sitcom.md`](file:///d:/Project/Sven/engine/genres/sitcom.md))**: Trapped Circumstance + Amplified Petty Conflict + Character-Flaw Comedy, Status Quo Reset Law, Multi-Plot A/B/C Weave, 10 Classical Comedy Weapons, Scene Buttons, and Standard Sitcom Script Formatting.
- **Social & Healing Drama Engine ([`drama.md`](file:///d:/Project/Sven/engine/genres/drama.md))**: Real Societal Pain + Internal Metamorphosis Arc (The Lie Believed ➔ The Truth Learned) + Costly Moral Choice, 5 Pillars of an Earned Ending (Sweet-and-Bitter Equilibrium, Human-Scale Resolution, Transforming Motifs), Subtext-First Dialogue, and Sensitive Topic Safeguards.
- **Viral Microdrama Engine ([`microdrama.md`](file:///d:/Project/Sven/engine/genres/microdrama.md))**: Hyper-Concentrated Stakes + High-Velocity Escalation (3s Hook / 30s Beat / Tail Cliffhanger) + Dopamine Face-Slap Reversal, Asymmetrical 13-Beat Retention Curve, Staccato Dialogue Fencing (≤ 12 words), 7 Master Cliffhangers (C1–C7), and 100% Filter-Proof Cinematic Status Proxies.
When a genre module is activated, its specific narrative conventions, structural pacing, and screenplay formatting take precedence over generic serial drama rules.

### 2.4 Scene Duration Policy & The Third-Party AI Render Mandate
- **DEFAULT — 10s scene, always.** Every scene is a 10.0s clip with a local clip timeline `00:00–00:10`. The agent never chooses 15s or 30s on its own, not even for a climax.
  - Episode runtimes: 60s = 6 scenes, 90s = 9 scenes, 120s = 12 scenes.
  - **Project scene-count override**: when the user approves another count per episode (e.g., 10 scenes = 100s), record it as `"episode_scenes"` in `output/<slug>/project_rules.json` and in the `setting.html` header. The audit warns when an episode's scene count differs from it. Scale the §8.1 beat map proportionally.
- **15s / 30s — only on explicit user request** (for a named scene, an episode, or the whole project). Gate 3M accepts clips ending at 10, 15, or 30s.
  - When requested, write one single prompt of that length. The macro scene architecture (`[context]`, `[subject]`, `[Pro]`, acoustics, closing line) is 100% identical to a 10s scene; duration is expanded simply by adding shots/phases (15s: 3–5 phases / 2–5 shots; 30s: 5–8 phases / 4–8 shots in three mini acts).
  - **Chained** 30s (three stateless 10s prompts joined through Code Block 2 handovers): ONLY if the user specifically requests chaining or reports generator crash.
  - Shapes, phase counts, and density per duration: `0b-temporal-camera-grammar.md` §6, §7, §9. State the duration on the scene card (`00:00 – 00:15` or `00:00 – 00:30`).
- No other durations (no 12s, no 20s).
- ⚠️ **The Third-Party AI Render Engine Law (Zero Cumulative Timestamps)**:
  - Generative video tools (Runway Gen-3, Kling 1.5, Sora, Hailuo, Wan 2.1) render each scene as an **INDEPENDENT CLIP** from second 0.
  - Inside Code Block 1 of EVERY scene, the timeline **MUST ALWAYS START AT `00:00`** (`00:00–00:10.0`, `00:00–00:15.0`, or `00:00–00:30.0`).
  - **NEVER write cumulative episode timestamps** (such as `[00:10–00:20]`, `[00:20–00:30]`) inside Code Block 1 or scene directing breakdowns. Cumulative timestamps confuse third-party AI models and corrupt video generation.
- ⚓ **Track A-Locked Rhythmic Quota & Gravitational Anchor Law**:
  - Strictly capped at **1–2 scenes maximum per 9–10 scene episode (~15–20% ratio)**.
  - Serves as the emotional Gravitational Anchor at 4 Golden Positions: (1) Emotional Climax / Vulnerability Breakdown, (2) Intimate Refuge / Tender Aftermath, (3) Claustrophobic Standoff, (4) Somatic Shockwave Silence.
  - 80–85% of scenes must utilize dynamic multi-angle cutting (Track B) or kinetic camera movement (Track A/AB).
- ⚡ **The Multi-Duration Scaling Law for Confrontational Cadences (Định Luật Điểm Rơi Giật Sốc 5%–10%)**:
  * Khi triển khai phân cảnh đối đầu nổ bom sự thật (`CADENCE: TRUTH_BOMB_SHOCK`) ở bất kỳ độ dài nào (10s, 15s, 30s hoặc dưới 30s), cú cắt cận cảnh phản ứng cuối cùng (Shot 3) **LUÔN LUÔN là cú Snap-Cut Choker chiếm đúng 5% đến 10% thời lượng cảnh**:
    - **10s**: `4.5s / 4.5s / 1.0s` ➔ Shot 3 Snap-cut đúng **1.0s** (`00:09.0–00:10.0`).
    - **15s**: `6.5s / 7.0s / 1.5s` ➔ Shot 3 Snap-cut đúng **1.5s** (`00:13.5–00:15.0`).
    - **30s**: Setup 11s ➔ Truth Bomb 17s (thoại dứt ở 00:28.0) ➔ Snap-cut Choker đúng **2.0s** (`00:28.0–00:30.0`).
  * Tuyệt đối cấm để shot phản ứng cuối kéo dài 3–5 giây làm chết nhịp phim. 90%–95% thời lượng trước đó dành cho hành động và lời thoại phản đòn.
- ⚡ **The Zero Dead Air Law (Gate 3O)**:
  - Prohibits all dead-air phrases: `the frame holds still`, `stands rigid through 00:10`, `blinks quietly in background`.
  - 100% of the clip duration (10s, 15s, or 30s) must be densely packed with continuous living micro-actions (respiration, weight shifts, finger flexes, tactile prop contact).

### 2.5 Image Reference Policy (ALWAYS ON)
Every Code Block 1 binds each location, character, and interactive prop to its uploaded reference image, using the exact syntax enforced by Gates 3J/3K/3L:
- `[context]:` → `[Location Name] [100% Refer to image <location_ref>], [time of day]. [5-Vector Environmental Specification: architectural landmarks & comprehensive physical furniture/textile inventory ("có cái gì ở đó": bed type, mattress, coarse blankets, tables, chairs, lamps, windows, steam/particulates), lighting physics & direction without Kelvin, atmospheric medium & mood]`. Barren declarations are strictly banned. **The Zero Ghost Object Law**: Any object touched, pulled, or manipulated in the action timeline (e.g. pulling up a wool blanket, gripping a bedpost) MUST already be grounded and established in `[context]:`.
- `[subject]:` → **The 4-Part Sovereign Subject Formula & Absolute Prop-Free Law**:
  `[name] [100% Appearance, attire, and facial features Refer to image <N>], [initial spatial anchor to in-scene architectural fixture], [initial physical posture, hands naturally free of props/weapons] — the only [name] in frame.`
  (Strictly enforces zero clone duplicates, anchors zero-frame spatial positioning, and prevents baking props into character anatomy. TUYỆT ĐỐI CẤM nhồi đạo cụ cầm nắm vào khối `[subject]:`!).
- `[Pro] :` (or `[PROP]:`) → **The Two-Tier Prop Protocol (Production Velocity Law)**:
  * **Tier 1: Đạo Cụ Linh Hồn & Phương Tiện Bất Ly Thân (Signature Hero Props & Vehicles — CẦN ẢNH THAM CHIẾU / Max 1–2 per series)**: Những vật phẩm rất quan trọng, xuất hiện liên tục đi liền với nhân vật qua nhiều cảnh (vũ khí, xe máy, xe ô tô, kỷ vật trung tâm, bản di chúc, hợp đồng chứng cứ sống còn). BẮT BUỘC có ảnh Model Sheet 16:9 trong Section 4A và gắn thẻ `[Prop Name] [100% Refer to image <prop_ref>], [physical state], [resting place or holder + grip] — the only [prop noun] in frame`.
  * **Tier 2: Đồ Đạc Sinh Hoạt Căn Bản (Everyday Living Items — CHỈ CẦN TEXT CHI TIẾT LÀ ĐỦ)**: Bát đĩa, đôi đũa, ly nước, chổi quét nhà, sổ tay, then cửa. **TUYỆT ĐỐI KHÔNG TẠO SHEET ẢNH**. Chỉ cần mô tả bằng văn bản thật chi tiết trong `[PROP]:` hoặc `action`.
  * **The Sovereign Hero Prop Law (Đạo Luật Đạo Cụ Linh Hồn & Phân Tách Tuyệt Đối Khỏi Đồ Đạc Bối Cảnh)**: Thẻ `[PROP]:` trong prompt được dành RIÊNG BIỆT cho Đạo cụ Linh hồn / Xúc tác kịch tính. Các vật dụng sinh hoạt thường nhật, đồ nội thất gia dụng, chăn gối nệm, bàn ghế, tủ giường, rèm cửa, quạt máy, đèn ngủ... **TUYỆT ĐỐI CẤM ĐƯA VÀO `[PROP]:`**. Toàn bộ đồ đạc này thuộc 100% về phần mô tả bối cảnh `[context]:` (Location Set Dressing). Nếu một cảnh không có đạo cụ linh hồn, khai báo `[PROP]: none (pure environmental and somatic staging)`.
  * **Meaningful English Naming Standard & Zero-Underscore Law (Quy Chuẩn Tên Nhân Vật `ho_ten` vs Địa Điểm & Đạo Cụ Tiếng Anh Tự Nhiên Không Gạch Dưới)**:
    - **Tên nhân vật (Characters)**: BẮT BUỘC tuân thủ **unique `ho_ten`** (snake_case không dấu: `hoang_nam`, `mai_anh`, `my_duyen`, `minh_khang`, `cu_tin`) để làm Token định danh thực thể độc nhất vô nhị chống nhân bản sinh đôi.
    - **Tên địa điểm (Locations)**: BẮT BUỘC viết bằng **tiếng Anh có nghĩa, gợi cảm và tự nhiên không dùng dấu gạch dưới `_`** (e.g. `sunlit townhouse open kitchen`, `intimate Southern Vietnamese master bedroom`, `sunlit high school classroom`). Tuyệt đối CẤM dùng tiếng Việt bồi không nghĩa với AI (`phong_cu`, `nha_bep`, `lop_hoc`, `san_truoc`) hoặc snake_case thô kệch (`modern_townhouse_kitchen`).
    - **Tên đạo cụ (Props)**: **TUYỆT ĐỐI KHÔNG DÙNG DẤU GẠCH DƯỚI `_` (NO UNDERSCORES)**! Viết bằng **tiếng Anh tự nhiên (Natural English Prose)** (e.g. `black cast-iron skillet`, `white ceramic coffee mug`, `pine wood crib`, `steaming bowl of ginger congee`, `carved walking cane`) để AI video text encoders (CLIP, T5) kích hoạt đúng ma trận trọng số vật lý của đồ vật.
    - Tên file ảnh tham chiếu (Location & Hero Prop): Viết bằng tiếng Anh có nghĩa (`location_kitchen_morning.jpg`, `pine_crib.jpg`, `ginger_tea_bowl.jpg`). Tuyệt đối CẤM đặt tên theo kiểu phiên âm bồi tiếng Việt (`phong_ngu_01`, `chao_pancake`, `bat_tra_gung`, `nha_bep`).
- Blocks are separated by blank lines. Legacy free-text tags (`[Character Reference attached]`, `[Mode A Anchor]`) are banned.
- Fixtures already visible in the location sheet (beds, cribs, tables) belong to `[context]`. Never re-declare them in `[Pro] :`, because that produces ghost duplicates.

### 2.6 Age & Appearance Policy
- **Numeric age appears ONLY in the voice parenthetical**: `（Voice of a 24-year-old woman from Southern Vietnam, ...）`. Gate 3A strips this pattern before scanning.
- Visual prose never contains a numeric age (`34-year-old`, `aged 34`). For minor-safety anchoring, use non-numeric adult terms: `young woman`, `adult craftsman`, `young adult weaver`.
- Visual prose never describes clothing. Wardrobe, face, and age appearance are locked by the 16:9 model sheet.
- Model sheets themselves (Stage 1) DO state an exact integer age (`aged 34`, never a range).

### 2.7 Spatial Anchoring & The Kinetic Handshake Protocol
- In `[subject]:`, anchor characters to physical architectural landmarks (`kneeling beside the pine crib near the queen bed`) and always conclude with the Anti-Duplication Seal (`— the only [name] in frame`). Never use 2D frame labels (`frame-left`, `screen-right`).
- Never write Cartesian math (`X: +0.8m`) anywhere in a deliverable (Gate 3H scans the whole document). Code Block 2 records positions in the same architectural prose.
- **The Kinetic Handshake Protocol (`[subject]:` ➔ `Action`)**:
  * **Biomechanical Launchpad (T0 ➔ T0+)**: The first action in `[00:00–00:XX]` must originate directly from the contact point established in `[subject]:` (e.g. sitting at desk ➔ slamming palms onto desk; kneeling ➔ reaching for prop). Teleportation or starting from a contradictory pose is strictly banned.
  * **Zero Redundancy**: Action prose never repeats clothing or static poses locked in `[subject]:`. Focus 100% on motion verbs, camera moves, prop interactions, and spoken dialogue.
  * **Frame Capacity Enforcement**: For single-subject shots (`CU`, `MCU`), action prose directs only the framed character; others are `O.S.`
  * **Cross-Scene Handover Bridge**: `[subject]:` of Scene N+1 inherits from `[HANDOVER STATE AT 00:10.0]` of Scene N.

### 2.8 The Pre-Production First Standard & Delivery Cadence (Bỏ Việc Trả Full Tập Đột Ngột — Bắt Đầu Bằng `setting.html` & Đạo Diễn Từng Cảnh)
To eliminate catastrophic AI hallucinations, rushed prompt writing, and optical framing contradictions (such as directing background characters in single-person close-ups), the Sven production engine strictly enforces **The Pre-Production First Standard**:

1. **Pre-Production Master Deliverable (`setting.html`)**:
   Before generating video scene prompts, the ONLY approved initial deliverable is `setting.html` (The Production Bible). It consolidates all 5 mandatory pillars to prepare the entire universe:
   - **(1) Các nhân vật (Characters & Full Cast Topology)**: Complete casting profiles (A1 Protagonist, A2 Antagonist, Tier B Satellites), wounds, psychological depth, flaws, wants vs needs, and kinship networks.
   - **(2) Ảnh tham chiếu (Reference Images & Multi-Angle Model Sheets)**: Exact image generation prompts for 16:9 4-view model sheets and explicit image reference tags (`image_1.jpg`, `image_2.jpg`, `cu_tin.jpg`).
   - **(3) Đạo cụ quan trọng (Key Interactive Props & Chekhov State Chains)**: Prop universe, dimensions, physical transformation states (Ready ➔ Under Load ➔ Broken/Landed), and reference image prompts (`prop_1.jpg`).
   - **(4) Địa điểm (Locations & 5-Vector Environmental Staging)**: 5-vector environmental staging (Time of day, Fixed architecture & furniture, Key lighting & shadow physics, Atmospheric medium) and 4-view grid prompts (`location_1.jpg`).
   - **(5) Cốt truyện chính của mỗi tập & Roadmap chi tiết (Main Storylines & Scene Roadmap per Episode)**: The macro storyline of the series + detailed narrative breakdown of each episode (Tập 1, Tập 2...) with Section 5 Scene Roadmap detailing all 10 scenes:
     * **Mandatory Episode Dramatic Spine**: Central Dramatic Question (CDQ) = $\mathbf{Want} + \mathbf{Deadly\ Obstacle} + \mathbf{Ticking\ Clock\ Stakes}$.
     * **Per-Scene Connective Matrix**: Scene Title, Timeline, Cast, Location, Props, Beat Function, Tactical Action Subtext (`[ATTACK]`, `[DEFEND]`, `[PROBE]`, `[BARGAIN]`, `[TRAP]`), **Inbound Dialogue Baton** (inherited keyword/aftershock from scene N-1), **Core Action Line (≤18w)**, and **Outbound Dialogue Baton** (momentum hook/question thrown to scene N+1).

2. **Abolition of Blind Full-Episode Dumps (Xóa Bỏ Việc Trả Full Tập Đột Ngột)**:
   - Dumping an entire 10-scene episode prompt file (`tap-X.html`) in one blind pass without prior setting sign-off and scene review is **STRICTLY PROHIBITED**. Blind dumps cause optical framing contradictions, flat prompts, and AI hallucinations.
   - In Stage 4, production proceeds **scene-by-scene directly on chat** (Interactive Chat Co-Pilot): The Assistant / Co-Director guides the user through each scene (framing scale, camera angle, kinematics, somatic action, speech-action fusion, cross-scene dialogue baton verification), verifying 0 errors and incorporating user feedback before compiling into the final `tap-X.html`.

| Feature | Pre-Production Deliverable (`setting.html`) | Episode Directing (`tap-X.html`) |
|---|---|---|
| **Role & Purpose** | Complete Pre-Production Foundation (Characters, Props, Locations, 5-Pillar World, Episode Roadmaps) | Scene-by-scene collaborative directing in chat, then compiled into verified final HTML |
| **User Experience** | Comprehensive review of the visual and narrative foundation | Hands-on film directing ("cảm nhận làm phim luôn"), zero blind dumps |
| **AI Role** | Worldbuilding Architect & Screenwriter | Executive Production Assistant & Co-Director |
| **Output Deliverable** | `output/<slug>/setting.html` (verified via `setting_audit_suite.py`) | Scene-by-scene chat review ➔ `output/<slug>/tap-X.html` (verified via `episode_audit_suite.py`) |


### 2.9 Story Ethics
Every story ends positive and hopeful: growth, redemption, truth exposure, justice, restorative grace. Zero fatalities, zero executions, zero gore.

### 2.10 Hard Constraints vs Craft Defaults vs Project Rules
**Hard Constraints** (never break; most are enforced by the audit gates):
- Clip duration strictly 10s (default), 15s or 30s only on explicit user request; ≥ 2 contiguous, non-overlapping phases from 00:00 to the clip end (Gate 3M)
- **Zero Cumulative Timestamps**: Every scene prompt MUST start at 00:00 for third-party AI generators; NEVER use cumulative episode timestamps like [00:10–00:20] in prompts (Gate 3M)
- **Zero Dead Air Law**: continuous micro-action density spanning 100% of the clip duration; zero "holds still", "stands rigid", or idle buffers (Gate 3O)
- **The Dramatic Spine & 4-Way Dialogue Relay Mandate (Zero Bubble Dialogue)**: Ban on isolated, disconnected scenes. Every episode must be driven by an active Dramatic Spine (CDQ). Every scene's dialogue must be an organic link in the 4-way relay (Cause-and-Effect, Keyword Echo, Emotional Inertia, Prop Anchor), moving the CDQ forward with explicit tactical subtext.
- **The Anti-Curtness & 3-Layer Organic Dialogue Law (Zero Robotic Commands)**: Ban on dry, curt, naked commands ("Đưa tiền đây", "Phải ăn nhiều"). Every spoken line must employ the 3-Layer Organic Formula ([Acoustic Inception/Address: *Má ơi...*, *Trời ơi...*] + [Dramatic Core] + [Sentence-Final Modal Particle: *...nghen*, *...chớ bộ*, *...hả trời?*]) and target the 8–14 word emotional sweet spot with organic respiration.
- Canonical phase-line syntax (`0b-temporal-camera-grammar.md` §8); no lip-synced line while the camera is in fast travel (whip, crane travel, fast orbit)
- Image references and 3-block labels (§2.5; Gates 3J/3K/3L)
- Numeric age only in the voice parenthetical; no clothing in visual prose (§2.6; Gates 3A/3E)
- No freeze holds; no camera hardware, lens, fps, or Kelvin terms (Gates 3B/3D)
- No pronouns in visual prose; stateless prompts; no coordinate math (Gates 3C/3I/3H)
- Dialogue Word Cap: Single-Speaker Shot target 25–30 words (hard cap ≤ 32w); Two-Shot exchange ≤ 15w/speaker (Gate 4B); no lip-synced line during a downward POV; V.O. with lips sealed
- Dialogue ↔ prompt verbatim parity wherever lines exist (Gate 4)
- Minor safety and cu_tin Somatic Sleep Staging Protocol (Gate 3F; Pillar 4 §[10d] & DIRECTOR.md §6; zero-minor lexicon, low-velocity sleep whitelist); no combat, chases, or brawls (§2.3)
- One primary move + one reaction per phase; one physical instance per prop
- **The Master Directorial Symphony Law & Kinetic Baton Relay**: Anti-fragmented flow across scenes. Exit vector of Scene N = Entry vector of Scene N+1. Strict prohibition on isolated, siloed prompt cards, spatial amnesia, and monotonic identical dialogue templates across scenes (Dynamic Voice Mode progression required; DIRECTOR.md §4c & SCREENWRITER.md Rule 9)
- Positive ending, zero fatalities (§2.9)

**Craft Defaults** (use by default; break when the scene needs it and write `BREAK: <default> — <reason>` in that scene's screenplay block):
- Thermal polarity shock cold → warm at B4.3 → B5.1
- Wound Prop (B2) → 180° Echo Prop (B6)
- Cast rotation per beat (B1 … B6 dynamics, §7.2)
- Beat 3 ≥ 60% spoken conflict (the real requirement is "conflict-dense"; this counts the beat's scenes that carry dialogue — it is unrelated to the W5 limit of speech ≤ ~60% of one clip)
- ~14–18 spoken words per 10s clip; Track A ≤ 10–12 words
- Timing blueprints and word budgets of the Pillar 1 dialogue models (Models 0–8)
- The 3-phase breath (lead-in → peak → settle) and any fixed phase split
- Emotion-arc numbers per beat
- The 3-wave climax (Trap / Identity → Loss → Ego Death) and the Stage 0 four-step twist chain — always inside the Doctrine §9.7 twist budget (one major + one or two minor reversals per ~100s episode)
- The beat-to-scene map percentages (§8.1)

**Closing line rule (Doctrine §8.8, audit W9)**: the ending answers the thematic question with a closing image. No character speaks the moral or the title. A spoken closing line is allowed only when it is an action (a request, a promise, a joke) rather than a maxim; a true maxim needs a `BREAK:` line.

**Project Rules** (kinship-address ladder, recurring meals, dialect lexicon) live in `output/<slug>/project_rules.json` and are enforced by Gates 4D/4E/4F only when that file exists. Never hard-code one film's rules into the engine or the Pillars.

---

## §3 — STARTUP STEPS

### K0 — Project State Detection (Resume Protocol)
If the user references an existing project or `output/` contains a matching slug, scan `output/<slug>/` before anything else:

| Found | Resume at |
|---|---|
| No folder | K1 → Stage 0 or Stage 1 |
| `setting.html` without scene-level Section 5 | Stage 2 (or CP1 if not yet approved) |
| `setting.html` with scene-level roadmap for Ep N, no `tap-N.html` | Stage 4 for Ep N |
| `tap-1..N.html` complete, no `seo-youtube.html` | Stage 5 |
| All deliverables present | Revision mode |

Report the detected state in one line, then continue. Never regenerate approved artifacts unless asked.

### K1 — Read History Registry (14-Axis Anti-Repetition Scan)
Load `history-registry.json` and avoid recent values on all 14 axes:

| Axis | Field | Rule |
|---|---|---|
| 1–2 | Character names (EN / VN) | No reuse |
| 3 | Karma direction | Alternate retribution / reward |
| 4 | Story tracks A–H | No consecutive repeat |
| 5 | Symbolic prop groups | No consecutive repeat |
| 6 | Hook techniques | No repeat within the session |
| 7 | Visual styles | No consecutive repeat |
| 8 | Genres & backgrounds | Avoid repeating recent ones |
| 9 | Escalation variants | Avoid repeating recent ones |
| 10 | Twist types | No consecutive repeat |
| 11 | Cliffhanger types | Cycle C1–C7 |
| 12 | Tropes stacked | Avoid repeating recent ones |
| 13 | Time of day & lighting | Avoid repeating recent ones |
| 14 | Narrative mode | Avoid repeating recent ones |

### K2 — Identify Request Type
| Signal | Action |
|---|---|
| Missing ≥ 2 of {specific character, setting, plot, karma type} | Stage 0 (5 concepts) |
| Concrete idea provided | Skip to Stage 1 (or Phase A if Genre Track) |
| Sitcom request / "viết sitcom" / "sitcom format" | Route to Sitcom Engine ([`sitcom.md`](file:///d:/Project/Sven/engine/genres/sitcom.md)). Follow 4-Phase Sitcom Lifecycle (Bible ➔ A/B/C Plots ➔ Outlines ➔ Script Format with Buttons). Bridge to Track Alpha if AI video prompts are requested. |
| Drama request / "drama chữa lành" / "phim xã hội" | Route to Social & Healing Drama Engine ([`drama.md`](file:///d:/Project/Sven/engine/genres/drama.md)). Follow 4-Phase Drama Lifecycle (Foundation ➔ 3-Act Outlines ➔ Earned Ending ➔ Script Format with Subtext). Bridge to Track Alpha if AI video prompts are requested. |
| Feedback on an artifact | Revise that artifact directly, then re-run its audit gate |
| "prompt for scene N" on an existing episode | Stage 4 revision of that scene inside `tap-X.html` |
| Lyrics / MV | Music Video track (Pillar 3) |
| Buddha protagonist / Buddha statue triggers | Special modes (§5.3) |

### K3 — Delivery Mode Selection (Dual Choice Handshake)
Confirm or query the user's preferred operational mode before starting production:
- **Pre-Production Phase**: Strictly delivers `setting.html` (The Master Pre-Production Bible) as the sole initial artifact before scene prompts.
- **Stage 4 Directing Delivery Mode**:
  - **Lựa chọn 1 (Option 1: One-Shot Full-Package File — `mode-batch`)**: Sau khi duyệt `setting.html`, biên dịch toàn bộ các cảnh vào `tap-X.html` qua một lượt audit tự động.
  - **Lựa chọn 2 (Option 2: Interactive Chat Co-Pilot — `mode-copilot`)**: Sau khi duyệt `setting.html`, làm từng cảnh một trực tiếp trên chat (Scene-by-Scene Directing), AI đóng vai trò **Trợ lý Sản xuất & Đồng Đạo diễn** đồng hành cùng người dùng duyệt từng góc máy, cỡ cảnh, diễn xuất cơ thể và lời thoại để trải nghiệm làm phim thực thụ, loại bỏ 100% lỗi trước khi xuất file.
If the user did not specify the mode in their initial message, present both choices clearly in the startup greeting or at Checkpoint 0.

---

## §4 — MASTER PIPELINE

The Sven ecosystem operates across two seamlessly bridged production tracks and two delivery modes:

```
[INPUT] → K0 Resume → K1 Registry → K2 Request Type → K3 Mode Selection
   │
   ├────────────────────────────────────────────────────────────────────────┐
   ▼                                                                        ▼
TRACK ALPHA: AI VIDEO PRODUCTION PIPELINE                TRACK BETA: GENRE SCREENPLAY PIPELINE
(Target: Kling / Runway / Sora / Wan AI Prompts)         (Target: Standard Industry Screenplay)
   │                                                                        │
STAGE 0  Concepts (5 ideas)           → ✋ CP0           PHASE A  Logline & Series Bible
   │                                                                        │
STAGE 1  setting.html (MASTER PRE-PROD BIBLE) → ✋ CP1   PHASE B  A/B/C Multi-Plot Weave
         • Characters & Casting Topology                                    │
         • Reference Image Prompts & Anchors             PHASE C  Beat Sheet & Scene Outlines
         • Key Props & Chekhov State Chains                       (Buttons & Emotional Shifts)
         • Locations & 5-Vector Staging                                     │
         • Episode Storylines & Scene Roadmap            PHASE D  Standard Screenplay Script
         (Passes setting_audit_suite.py)                          (Sluglines, Action, Dialogue)
   │                                                                        │
STAGE 2  Narrative Blueprint (2S/2)   → ✋ CP2           PRE-FLIGHT 10-Point Genre Audit Gate
   │                                                                        │
STAGE 3  Episode Screenplay           → ✋ CP3           [OPTIONAL HANDOFF TO TRACK ALPHA]
         (Scene-level polish & intent)                   (Convert script scenes to setting.html
   │                                                      and compile tap-X.html AI prompts)
STAGE 4  Scene-by-Scene Directing     → ✋ CP4
         (Co-Pilot on chat: scene by scene;
          Zero Blind Full-Episode Dumps;
          Passes episode_audit_suite.py)
   │
STAGE 5  seo-youtube.html             → ✋ CP5
   │
[🎬 DONE]
`**Checkpoint rule**: at every ✋, STOP and wait. Accepted replies: `ok` / `continue` (approve), `edit [content]` (revise), plus stage-specific commands listed in each section.

---

## §5 — STAGE 0: CONCEPT GENERATION

> Load the Creative Doctrine §8.1 and §9.2–§9.3 (the questions behind a concept and how it breaks predictions), then Pillar 1 (§ HOOK TECHNIQUES, § TWIST ARCHETYPES) and the Growth Architect niche-validation section.

### 5.1 Hard Rules
- Output 5 fully distinct ideas. They must differ in genre, conflict type, character arc, target emotion, and hook technique (5 different hooks from the 12-Hook library).
- Spread: ≥ 3 eras/settings; at least 3 story tracks; alternate retribution and reward; no 2 ideas share the same karmic behavior or the same outcome.
- Every lesson is tied to a specific action in the story, never generic.
- Positive ending is mandatory (§2.9).

### 5.2 Output Template (per idea — user-facing, Vietnamese labels)
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Ý TƯỞNG #[N] — [Tên Ý Tưởng]   `[Retribution / Reward | Genre]`
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎭 1. LOGLINE: [2–3 sentences: premise + moral stakes]
🧲 2. HOOK 3 GIÂY: Visual paradox | Cognitive gap question | Visual anchor bridge into Setup
🎲 3. BẺ GÃY DỰ ĐOÁN: Audience assumes [A] → Reality is [C, planted on screen — Doctrine §9.2]
⚡ 4. CHUỖI TWIST: T1 Hook Reveal [TW-xx] → T2 Midpoint [TW-xx] → T3 Climax [TW-xx] → T4 Payoff [TW-xx]  (series: spread across episodes; short film: within the §9.7 budget)
🏛️ 5. NHÂN VẬT: A1 [name — trade + wound + want vs need] | A2 [name — own ambition + "where A2 is right"]
               B1/B2/... [relation to A1 + relation to A2 + twist role] | C [community & public opinion]
📦 6. ĐẠO CỤ KÍCH NỔ TWIST: [Prop + archetype] — [physical action that detonates the twist]
🔗 7. MỒI GIỮ CHÂN: [Open loop / ticking clock]
🎣 Hook đề xuất: #[N] — [technique]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.3 Special Modes
- **🪷 Buddha as Protagonist** (triggers: "Đức Phật làm nhân vật chính", "Buddha protagonist"): all 5 ideas keep Buddha as Observer / Guide / Awakener, built on 3 canonical types:
  1. Transformation of Evil (Angulimala)
  2. Consolation of Grief (Kisa Gotami)
  3. Humbling of Ego (Ajatasattu)

  Each idea outputs: Buddha's role and who he awakens / Setting / Journey / Hook / Lesson.
- **🗿 Buddha Statue Veneration** (triggers: "tượng Phật", "sửa tượng", "lau tượng", "thắp hương", "dâng đồ cúng"): build on the 4-Pillar Veneration Framework. The statue is the symbolic prop with its own state chain. Pillars → karmic rewards:
  1. Repair → healed relationships
  2. Clean → illness healed / beauty restored
  3. Offer incense, water, flowers → water source / good name
  4. Offer food when hungry → abundance / benefactor

  Details: Pillar 1 § STATUE VENERATION MOTIF LIBRARY.
- **🎵 Music Video**: input = lyrics, genre, duration T, and MV mode (A Pure Story / B Hybrid Performance / C Visual Metaphor). The 6 beats sync to song sections at 3% / 12% / 35% / 30% / 12% / 8% of T. Follow Pillar 3 Music Video architecture.

### 5.4 ✋ CHECKPOINT 0
```
👉 Gõ số ý tưởng để chọn (mặc định CÓ THOẠI) — ví dụ "2"
   Thêm "S" nếu muốn bản KHÔNG THOẠI (Show, Don't Tell) — ví dụ "2S"
   "sửa ý tưởng N: [yêu cầu]" | "ý tưởng mới" | hoặc mô tả ý tưởng riêng
```
`N` or `ND` → Dialogue track. `NS` → Silent track. "ý tưởng mới" → 5 new ideas with zero overlap.

---

## §6 — STAGE 1: PRE-PRODUCTION → `setting.html` PHASE A

> Load Pillar 2 in full for this stage. All sheet templates are copied from Pillar 2, never from memory.

### 6.1 — 1A Format & Visual Style
```
VISUAL STYLE  : Pixar 3D (DEFAULT) — override only on user request
EPISODE MODE  : Short Film (1 ep) / Multi-Episode Series (N eps)
RATIO         : 9:16 vertical / 16:9 horizontal
DURATION/EP   : 60s (6×10s) / 90s (9×10s) / 120s (12×10s)
GENRE / BACKGROUND / TROPE (max 2 stacked)
DIALOGUE LANG : English (default) / [target language + dialect]
```
The visual style is set once. Its exact header (from the Pillar 2 style encyclopedia) propagates into every model, prop, and location sheet, and into every Code Block 1 `Style:` line.

**Style library** (full headers in Pillar 2):
- **Live action**: Theatrical Cinematic, Modern Microdrama, French Arthouse, Monumental Epic, Bollywood, Nordic Noir, Golden Western, Pop Dystopia, Prestige HBO, Gritty Desert, Wes Anderson, David Lynch, Quentin Tarantino, Christopher Nolan, Blade Runner, Modern K-Drama, Crime Drama, Game of Thrones, European Epic.
- **Animation**: ★ Pixar 3D (default), Cinematic 3D, Soft Contemporary, Monochrome Manga, Mature Western Animation, Spider-Verse, 3D Cyberpunk, Cthulhu, Color Ink Wash, Junji Ito, Thriller Folklore, Clay Stop-Motion, Felt Stop-Motion, Ghibli, Korean Webtoon, Retro 90s Cel-Shaded, High-Energy Action, Chinese Xianxia, Next-Gen Cel-Shaded, Painterly Cel-Shaded.

**Genres**: Billionaire Romance, CEO Workplace Romance, Mafia Romance, Werewolf Fantasy, Vampire Supernatural, Royal Romance, Historical Romance, K-Drama Romance, J-Drama Healing, Telenovela Melodrama, SEA Family Drama, BL Romance, Revenge Drama, Family Secrets, Youth Campus, Entertainment Industry, Medical Drama, Legal / Crime, Thriller Mystery, Urban Fantasy, Survival Adventure, Light Comedy.

**Backgrounds**: Modern City, Luxury Mansion, Corporate Office, University Campus, Hospital, Courtroom, Entertainment Set, Small Town, Island Resort, Royal Court, Historical Palace, Mafia Underworld, Supernatural Realm.

**Tropes**: Contract Marriage, Secret Baby, Hidden Identity, Enemies to Lovers, Second Chance, Revenge Comeback, Forbidden Love, Love Triangle, Forced Proximity, Heir Reveal, Cinderella Rise, Fake Relationship, Fated Mates, Amnesia, Time Travel, Rebirth, Found Family, Redemption Arc.

### 6.2 — 1B Cast Architecture & 16:9 Model Sheets
- Build the cast per Pillar 2 (A1, A2, Tier B satellites with the dual-relationship mandate, Tier C chorus). Output:
  - **4-Pillar Character-to-Plot Binding Matrix**: occupation and arena, relationship stakes, moral stance, 6-beat through-line.
  - **3-layer relationship web** for every pair: surface label, real dynamic, wound connection. For A2 / B1, include "where they are right".
- **Sheet allocation**: A1, A2, and every Tier B appearing in ≥ 2 scenes get a 16:9 Multi-Angle Model Sheet (Zero-Text Standard). Tier C gets none (text-only, described collectively).
- **Model sheet invariants** (template: Pillar 2 Part III-B):
  1. Style header = the project's visual style header. Use the photoreal portrait header only for live-action styles.
  2. Layout (Sovereign Multi-Angle Composition — Zero-Text Standard): Strictly zero text, zero typography, zero metadata card on canvas (100% visual imagery, zero text labels). Left and center area (~55–60% canvas) = Three-angle full-body turnaround in relaxed, natural standing posture with arms resting naturally and loosely beside the torso, feet naturally grounded on floor: 1) Headless neck-down front view (strictly zero head and zero face); 2) Headless neck-down 90-degree lateral side profile view (strictly zero head and zero face); 3) Full-length rear back view INCLUDING complete back of head and rear hairstyle showing hair strands, nape of neck, rear garment tailoring, and footwear down to floor. Right area (~40–45% width) = Dominant High-Definition Cinematic Chest-Up Portrait in strictly direct frontal eye-level view facing camera directly. **The Headroom & Full-Cranial Retention Law**: Portrait MUST be framed with generous headroom margin above the hair crown, ensuring the entire head, complete hairstyle volume, and cranial curve are 100% visible inside the frame with clear breathing margin below top canvas border (strictly zero cropped head, no cut-off hair, no truncated hair crown, no out-of-frame head, strictly zero three-quarter view, strictly zero profile view, strictly zero tilted angle) to prevent flat skull and hair flickering hallucinations in downstream AI video.
  3. **Optical Contrast Inversion backdrop**: dark attire → solid pure white `#FFFFFF`; light attire → solid dark neutral grey. Zero scenery, zero mist or bokeh, zero environment.
  4. Seven fields: height (cm), head-to-body ratio, ethnicity & skin, build, hair (strands), facial bone structure + unique mark, baseline costume (explicit fabrics).
  5. Exact integer age (`aged 34`).
  6. Consistency rule: same face, hair, and outfit across all views. Strictly zero background scenery, zero furniture, zero watermark.

### 6.3 — 1C Props (Two-Tier Architecture & Production Velocity Law)
To optimize production velocity and eliminate massive wasted rendering time, Sven strictly categorizes all in-universe objects into **Two Tiers**:
1. **Tier 1: Đạo Cụ Linh Hồn & Phương Tiện Bất Ly Thân (Signature Hero Props & Vehicles — CẦN ẢNH THAM CHIẾU / Quota: Strict Max 1–2 per series)**:
   - **Định nghĩa**: Những vật phẩm rất quan trọng trong phim, gắn liền với nhân vật và xuất hiện liên tục xuyên suốt câu chuyện:
     * *Vũ khí & Công cụ*: Con dao găm gia truyền, thanh kiếm, khẩu súng, cây gậy ba-toong, hộp đồ nghề đặc thù.
     * *Phương tiện di chuyển*: Chiếc xe máy Cub 50 cà tàng của shipper, chiếc ô tô bán tải cũ, chiếc xe đạp mini gắn giỏ sắt.
     * *Kỷ vật kịch tính*: Chiếc quạt máy cổ tháo tung ruột của mẹ, bức thư di chúc của cha, chiếc đồng hồ quả quýt, chiếc nôi gỗ thông khắc tên con.
   - **MANDATORY 16:9 Model Sheet**: BẮT BUỘC có câu lệnh tạo ảnh 16:9 Model Sheet (4-view Prop Design Sheet) trong `setting.html` Section 4A để khóa chặt kiểu dáng, màu sơn, chi tiết; ngăn AI video đổi loại xe, đổi màu xe hay biến dạng vũ khí giữa các góc máy. Gắn thẻ `[100% Refer to image prop_X_4view.jpg]`.
   - **Bifurcation Law for Destructible Props**: State 0 intact entity (own sheet) → State 1 kinetic break (causal participles) → State 2 derived entity with an INDEPENDENT noun (own sheet if shown repeatedly). Never attach the intact reference to a broken-state prompt.
2. **Tier 2: Đồ Đạc Sinh Hoạt Căn Bản (Everyday Living Items — CHỈ CẦN TEXT CHI TIẾT LÀ ĐỦ)**:
   - **Định nghĩa**: Những đồ đạc thông thường dùng cho sinh hoạt căn bản hàng ngày: bát cơm, đôi đũa, cốc nước lọc, ấm trà, cái thìa sứ, chiếc ghế nhựa, cuốn sổ tay, cây chổi, bao diêm, điếu thuốc.
   - **STRICTLY ZERO IMAGE GENERATION SHEETS**: TUYỆT ĐỐI KHÔNG TẠO CÂU LỆNH TẠO ẢNH REFERENCE SHEET (tiết kiệm tối đa thời gian vẽ ảnh và dung lượng). Pre-trained video diffusion models đã nhận thức cực tốt các đồ vật này.
   - **Hyper-Clear Text Description Standard**: Chỉ cần mô tả bằng văn bản thật chi tiết, rõ ràng (chất liệu, màu sắc, tình trạng cũ/mới, vị trí đặt) ngay trong prompt `[PROP]:` hoặc `[context]:` (ví dụ: `white porcelain soup spoon resting on round aluminum tray; standard blue plastic stool; worn hardcover accounting ledger`).
- Interaction rules (grip contract, causal ripple, 3-step anti-teleport handoff): Pillar 4 §3.4. Props take ≤ 5–10% of narrative attention. Never title scenes after props.

### 6.4 — 1D Locations
Each primary location gets an environment profile (era, time and weather, palette, textures, atmospheric medium) and a 16:9 2×2 grid sheet. Panels: wide establishing, reverse angle, overhead, ground-level low angle. No people, no text. Template: Pillar 2 / Pillar 4 §3.6.

### 6.5 — 1E Initial Setting Declaration
Lock the starting state: time, location, lighting (source, direction, natural color tone — no Kelvin), weather, floor surface, each character's architectural position, pose and gaze, each prop's position, state and holder, plus series-wide consistency notes.

### 6.6 — `setting.html` Architecture (Phase A now, Phase B in Stage 3)
Governing spec: Pillar 2. Required sections (IDs must match `setting_audit_suite.py`):

| Section | Content | Phase |
|---|---|---|
| 1 `story` | Master arc, thematic core, Zero-Fatality resolution | A |
| 1B | Diurnal timeline & living realism (clock, meals, sleep, fatigue, light progression) | A (outline) → B (per-scene detail) |
| 1C | Inter-episode causality matrix & kinetic bridges | B |
| 1D | Scene typology & 8-model dialogue matrix | B |
| 2 `cast` | Canonical cast + Mode B video prompt snippets | A |
| 3 `modelsheets` | 16:9 model sheet prompts + copy buttons | A |
| 4A `props` | Prop universe, state chains, sheet prompts, Mode B snippets | A |
| 4B `locations` | Location universe, lighting contracts, grid prompts, Mode B snippets | A |
| 5 `roadmap` | Phase A: episode/beat-level rows (≥ 6). Phase B: every 10s scene (title, time, cast, location, props, beat, intent, dialogue model, kinetic bridge) | A → B |
| 6 | SOP for downstream production | A |

### 6.7 — 🛡️ Gate 1.5 (Hard Block) and ✋ CHECKPOINT 1
```bash
python engine/setting_audit_suite.py output/<slug>/setting.html
```
- If any gate fails, the Screenwriter fixes the file and re-runs. Never present a failing file.
- On pass: write a **registry draft** (§11) for names, style, genre and background, tropes, and the prop group. This prevents silent loss if the project is abandoned.
- Then present CP1:
```
✋ CHECKPOINT 1 — setting.html (Phase A) đã qua audit
File: output/<slug>/setting.html
→ "ok" để sang Stage 2 Blueprint | "edit [nội dung]" để chỉnh cast / bối cảnh / đạo cụ
```

---

## §7 — STAGE 2: NARRATIVE BLUEPRINT

> Load the Creative Doctrine §8 (Story Spine) and §9 (Plot Engine) first, then Pillar 1. Short film → 2S. Series → 2.

### 7.0 Story Spine (before the blueprint)
Write the Story Spine Card (Doctrine §8.10 + §9.9): QUESTION, TRUTH (Wound → Lie → Want → Need → Fear for every principal), SPECIFIC (10 details), CLICHÉ (≥ 2 subverted or refused), LOOPS, COST, DEBATE, IMAGE, plus PREDICT, KNOW, MISREAD, TWIST. Series: one series Spine here; each episode refreshes its own Spine at Stage 3. The blueprint below is chosen to serve the Spine, never the reverse.

### 7.1 Hook Selection (internal)
1. Identify plot features: karma type, escalation behavior, structure (A–G), prop role, target first-3-second emotion.
2. Score the 12 hooks with Pillar 1 "Trigger when…". Pick a primary and a backup.
3. Check session history (Axis 6). If the primary was used, take the backup; otherwise take any unused hook.

Output line: `HOOK: #[N] — [name] | Reason: [1 sentence]`. If it differs from the Stage 0 suggestion, mark `🔄 Hook adjusted`.

### 7.2 — 2S Short Film Blueprint
Determine:
1. Scene count (§2.4)
2. Beat-to-scene map (§8.1)
3. Hook
4. Wound Prop (B2) → 180° Echo Prop (B6) (craft default)
5. Beat 3 conflict type (conflict-dense; ≥ 60% spoken by default)
6. Major twist + minor reversals within the Doctrine §9.7 budget, each planted ≥ 2 times; the 3-wave climax (Trap/Identity → Loss → Ego Death) is the craft default shape
7. Thermal polarity shock B4.3 → B5.1 (craft default)
8. B6 = transformed community + Echo Prop + a closing image that answers the opening image (no spoken moral or title — §2.10 closing line rule), no cliffhanger
9. Emotion arc 6–7 → 6–7 → 7–9 → 10 → 7–8 → 6–7 (guidance)
10. Voice-mode rhythm sketch across the scenes (Doctrine §4.1), e.g. `dialogue → spoken+V.O. → ensemble → silence → monologue → dialogue`

```
SHORT FILM BLUEPRINT — [Title]
STORY SPINE: [§7.0 card]
FORMAT: 1 ep — [N] scenes × 10.0s | HOOK: #N | CONFLICT: [...] | TWIST: [major TW-xx + minor TW-xx, plants]
WOUND PROP (B2) → ECHO PROP (B6): [...] → [...]
THERMAL POLARITY: [cold state B4.3] → [warm state B5.1]
CAST DYNAMICS: B1 [...] | B2 [...] | B3 A vs B1 | B4 [...] | B5 [...] | B6 A + C
18 SUB-BEATS:
  B1 HOOK: 1.1 Cognitive Gap | 1.2 Frozen Potential | 1.3 Anchor Bridge
  B2 SETUP: 2.1 Old Equilibrium | 2.2 Backstory Wound | 2.3 Wound Prop Plant
  B3 DRAMA: 3.1 Flawed Tactics | 3.2 Ideological Clash (≥60% spoken) | 3.3 Exits Sealed
  B4 CLIMAX: 4.1 Wave 1 Trap | 4.2 Wave 2 Loss | 4.3 Wave 3 Ego Death   (default shape)
  B5 RELEASE: 5.1 Thermal Shock | 5.2 Reverse Rescue | 5.3 Concrete Proof
  B6 ECHO: 6.1 Transformed World | 6.2 180° Echo Prop | 6.3 Closing Image
```

### 7.3 — 2 Series Blueprint (4-Act: 20% / 45% / 25% / 10%)
```
Act 4 = 1 ep (N ≤ 8) or round(N×0.10) (N ≥ 10)
Act 1 = max(1, round(N×0.20))   Act 3 = max(1, round(N×0.25))   Act 2 = remainder (holds Midpoint at 50%)
```
| N | Act 1 | Act 2 | Act 3 | Act 4 | Midpoint |
|:-:|:-:|:-:|:-:|:-:|---|
| 4 | 1 | 2 | 3 | 4 | Middle of Ep 2 |
| 5 | 1 | 2–3 | 4 | 5 | End Ep 2 → start Ep 3 |
| 6 | 1 | 2–3 | 4–5 | 6 | End Ep 3 |
| 7 | 1 | 2–4 | 5–6 | 7 | Middle Ep 3 |
| 8 | 1–2 | 3–5 | 6–7 | 8 | Ep 4 |
| 10 | 1–2 | 3–6 | 7–9 | 10 | End Ep 5 |
| 12 | 1–2 | 3–7 | 8–11 | 12 | Ep 6 |
| 16 | 1–3 | 4–10 | 11–14 | 15–16 | Ep 8 |
| 20 | 1–4 | 5–13 | 14–18 | 19–20 | Ep 11 |

| Act | Duty | Cliffhanger |
|---|---|---|
| 1 Setup | World, root wound, core conflict, Wound Prop. **Strictly NO early victory, NO premature reconciliation.** | C1 Mystery / C2 Threat (6–7) |
| 2 Escalation | Stakes multiply, first failure, Midpoint reversal, betrayal, false dawn | C3 Betrayal / C4 Revelation / C7 Return (7–8) |
| 3 Climax | All hope lost → Ego Death, 8-beat showdown, unmerited grace | C5 Loss / C6 Decision (9–10) |
| 4 Resolution | Echo Prop payoff, earned reconciliation, catharsis | NONE (finale) |

**Anti-Sitcom / Anti-Vignette Continuum Law**: A multi-episode series is NEVER a sequence of disconnected "Problem-of-the-Week" sketches where characters fight over an arbitrary folk myth and make up 100 seconds later. Characters possess unbroken psychological continuity: their relationships permanently alter at each checkpoint, and core emotional wounds escalate across acts rather than resetting.

```
SERIES BLUEPRINT — [Title]
SERIES SPINE: [§7.0 card]
TOTAL: [N] eps × [S] scenes × 10s | SERIES ARC: [...] | OVERARCHING TWIST: [...]
WOUND → ECHO PROP: [...]
ACT 1: Ep 1 [duty] | Cliffhanger C1 — [...] ...
ACT 2 / ACT 3 / ACT 4 (Ep N finale, cliffhanger NONE)
```

### 7.4 ✋ CHECKPOINT 2
`ok` → Stage 3 | `edit [content]` → revise blueprint.

---

## §8 — STAGE 3: EPISODE SCREENPLAY + ROADMAP PHASE B

> Load the Creative Doctrine (§8 Story Spine, §8.12 Format Law, §9 Plot Engine, §10 4 Cinema Tiers & 12 Devices, §10.4 Dynamic Script Calibration, §1 Intent, §3.8 Subtext, §4 Voice Modes) first, then Pillar 1 (dialogue-model catalog, 4-in-1 parentheticals, WPS) and Pillar 2 (Living Continuum). Write ONE episode per checkpoint.

### 8.1 Beat-to-Scene Map (10s atoms; a craft default — the Spine and the beats may move a boundary by one scene with a `BREAK:` line)

#### Format A — Standalone Short Film (60s–120s; Closed Narrative Arc)
| Beat | 60s (6) | 90s (9) | 100s (10, project override) | 120s (12) | Function |
|---|---|---|---|---|---|
| 1 Hook | Sc 01 | Sc 01 | Sc 01 | Sc 01 | Visual paradox, 3s cognitive gap |
| 2 Setup | Sc 02 | Sc 02 | Sc 02 | Sc 02–03 | Old world, root wound, Wound Prop, first plants |
| 3 Drama | Sc 03–04 | Sc 03–05 | Sc 03–04 | Sc 04–07 | Ideological clash, conflict-dense, sealed exits |
| 4 Climax | Sc 05 | Sc 06–07 | Sc 05 | Sc 08–10 | Major twist paid off from its plants (3-wave by default) → Ego Death |
| 5 Release | Sc 06 (first half) | Sc 08 | Sc 06–07 | Sc 11 | Thermal shock, grace |
| 6 Echo | Sc 06 (second half) | Sc 09 | Sc 08–10 | Sc 12 | Transformed world, Echo Prop, closing image |

#### Format B — Multi-Episode Series (N Episodes; Act-Bound Episodic Engine)
> In a multi-episode series, an individual episode **NEVER** runs the closed 6-beat resolution arc of a short film. Each episode executes its designated **Act Function** (§7.3 & Doctrine §8.12):
> - **Act 1 Episodes (Setup, Inciting Crisis & Trap)**:
>   - *Sc 01–02*: Hook & Sensory Crisis (Immediate high stakes, psychological vulnerability).
>   - *Sc 03–05*: Inciting Clash & Entrenched Worldviews (Old habits clash; friction mounts).
>   - *Sc 06–08*: The Trap Tightens & Failed Resistance (Stakes escalate; exits sealed).
>   - *Sc 09–10*: The Fracture & Cold Water Cliffhanger (Status quo shatters; point of no return; **STRICTLY NO reconciliation, NO early release**).
> - **Act 2 Episodes (Complications, Outside Scrutiny & Midpoint Break)**:
>   - Focuses on escalating stakes, social judgment, worsening misunderstandings, culminating in the Midpoint rupture.
> - **Act 3 Episodes (The Abyss, Direct Showdown & Ego Death)**:
>   - Focuses on Rock Bottom, the truth bomb confrontation, genuine Ego Death, and Anagnorisis.
> - **Act 4 Episodes (Transcendence, Catharsis & Restorative Feast)**:
>   - Focuses on earned reconciliation, restorative actions, and the genuine transformed feast ("Cơm Không Chan Nước Mắt").

### 8.2 Script Continuity Law (3 Tiers & The 4 Cinematic Continuity Locks)
1. **Macro (season)**: irreversible escalation ladder (personal → family → institutional → ego death → transcendent redemption). Each episode ends on a point of no return.
2. **Meso (episode to episode)**: the end of Ep N runs False Dawn → Cold Water Slap (open loop). The slap is caused by a person, object or choice planted earlier in the episode, at the genre's scale (Doctrine §9.8). The final frame of Ep N is the opening frame of Ep N+1 (zero temporal gap). Held props, marks, and fatigue carry over.
3. **Micro (10s Scene-to-Scene & Sequence Stitching)**:
   - **"Therefore / But" law**: never "and then". Every cut advances power, knowledge, or emotional cost.
   - **The 4 Cinematic Continuity Locks (Grammar §1.3 & Compiler §4.5)**:
     - *Lock 1 (180° Axis & Gaze Vector)*: Characters maintain invariant screen left/right gaze alignment across shot-reverse-shot cuts.
     - *Lock 2 (Kinetic Baton Relay / Action Match-Cut)*: Scene N ends on an unfinished physical motion (`08.5–10.0s`); Scene N+1 catches and completes it (`00.0–01.5s`) from the new angle with zero action repetition.
     - *Lock 3 (Auditory Suture)*: L-Cut dialogue tails and uniform diegetic Foley/room tone bridge the cut, eliminating fragmented seams.
     - *Lock 4 (Physical Handover Ledger)*: Code Block 2 records the exact 00:10.0 snapshot inherited 1:1 by Scene N+1.
   - **Multi-Spatial Sequence Architecture (The Anti-Box Mandate)**:
     - An episode of 100s–120s is structured into **2–3 distinct physical or psychological Sequences** (Setup/Tension $\to$ Sensory Match-Cut $\to$ Collision Core $\to$ Aftermath Resonance).
     - Strictly ban trapping all 10 scenes in a single bedroom/box to prevent sterile, static sitcom syndrome.

### 8.3 Output Template (per episode)
```
EPISODE [N] — [Title] | ACT [X] | DUTY: [1 sentence]
STORY SPINE (Doctrine §8.10 + §9.9): QUESTION | TRUTH | SPECIFIC | CLICHÉ | LOOPS | COST | DEBATE | IMAGE | PREDICT | KNOW | MISREAD | TWIST
HOOK #N | CONFLICT [...] | TWIST [major + minor, plants] | WOUND→ECHO [...] | CLIFFHANGER [C1–C7 / NONE] | EMOTION ARC [...]

--- SCENE 01 (10.0s) — BEAT 1: HOOK | Emotion 6–7 ---
Function: [...]
INTENT: Want A → [...]; B → [...] | Obstacle: [...] | Tactic: A [...] / B [...]
SHIFT: [value at 00:00] → [value at 00:10] | SUBTEXT: [...] | GAP: [suspense / mystery / empathy]
VOICE MODE: [Doctrine §4 mode] — because [one clause]
CADENCE: [RAPID_SPARRING / ASYMMETRIC_DOMINANCE / TRUTH_BOMB_SHOCK / PURE_VISUAL_STEALTH / COLD_WATER_CLIFFHANGER / INTIMATE_REFUGE / VULNERABILITY_BREAKDOWN / CLAUSTROPHOBIC_STANDOFF / SOMATIC_AFTERSHOCK]
ACTION FRAMEWORK: [Tier 1: reinforce / contradict / replace / reveal] + [Tier 2: Stichomythia / Dominance / Aftershock / Covert / False Dawn Cold Water]
Cast & positions: [architectural anchors]
Track: [A dynamic single-shot / A-Locked static performance / B multi-shot / AB mixed] — because [one clause]
Action: [beats in order, one primary move per phase; phase count and splits follow the beats, not a template]
Lines: [Speaker (spoken / V.O. / O.S.): line ≤ 32 words single speaker / ≤ 15 words per speaker in a two-shot (Gate 4B Hard Cap)] + VN dub line + hidden verb + Action↔Line [reinforce / contradict / replace / reveal]
       or: SILENCE — [what the body says instead]
Sound: [diegetic Foley, room tone]
BREAK: [craft default broken — reason]   (only when a default is broken)
HANDOFF @00:10: [characters / props / setting]
... (repeat for every scene of the episode)
```

### 8.4 Per-Beat Micro-Check
- **Format A (Short Film)**: Hook plants visual anchor; Setup plants Wound Prop; Drama is conflict-dense; Climax pays off major twist to Ego Death; Release lands thermal shock + grace; Echo shows transformed world.
- **Format B (Series Episode)**: Verifies against its Act duty (§8.1 Format B). In Act 1/2: strictly verifies that NO unearned reconciliation, NO therapeutic confessions, and NO premature endings occur. Ensures ending lands a caused Cold Water cliffhanger.
- **Two-Tier Action & Cadence Check (Doctrine §3.3)**: Verifies that every scene orchestrates Action via `[Tier 1 Relationship] + [Tier 2 Dynamic]` and declares its `CADENCE:` tag. Confirms that rapid sparring scenes contain zero dead-air buffers and that somatic shocks have earned silence. Verifies that `Track A-Locked` static performance scenes are strictly capped at 1–2 scenes per 9–10 scene episode (~15–20% ratio) as the emotional Gravitational Anchor.
- **Dialogue & Subtext Check (Doctrine §3.8)**: Verifies zero psychological self-diagnosis, zero symmetrical ping-pong debates, and zero cliché fainting spells used as instant reversal devices.
- Every scene has a value shift; voice modes and turn counts vary across the episode (Doctrine §4.1); no line restates what the frame shows (Doctrine §3.2).
- The Prediction Ledger has ≥ 2 BROKEN predictions with earlier plants, some KEPT; every misunderstanding passes the idiot-plot test (Doctrine §9).

### 8.5 Roadmap Phase B
After drafting, write this episode's scene rows into `setting.html` Section 5 (plus the 1B / 1C / 1D details). Each row carries the scene's Intent Card in compact form (want, shift, subtext, gap, voice mode). Re-run `setting_audit_suite.py`. Section 5 now becomes the SSOT for Stage 4: titles, times, cast, props, beats, and lines must match verbatim.

### 8.6 ✋ CHECKPOINT 3
```
✋ CHECKPOINT 3 — Kịch bản Tập [N] hoàn tất
→ "ok" để biên dịch tap-[N].html | "edit [nội dung]" | "scene [K]" để sửa một cảnh
```

---

## §9 — STAGE 4: FULL-EPISODE PROMPT PRODUCTION (`tap-X.html`)

> Delegated to the Director (`.agents/DIRECTOR.md`). Load the Creative Doctrine (§2 Directing from Intent, §5 Creative Review) first, then Pillar 3 and Pillar 4. Delivery = one complete episode per checkpoint (§2.8).

### 9.1 Handshake (Producer → Director)
1. Approved episode screenplay
2. `setting.html` Section 5 rows for this episode
3. Model sheet, prop, and location reference slots, plus the Mode B snippets
4. The previous episode's final handover (series)

### 9.2 Director's Execution Protocol (Option 1 Batch vs Option 2 Chat Co-Pilot)

- **Under Option 1 (One-Shot Full-Package Mode — `mode-batch`)**:
  The Director executes this entire loop internally without pausing scene by scene, compiling all scenes into `tap-X.html` in one single audited pass.

- **Under Option 2 (Interactive Chat Co-Pilot Mode — `mode-copilot`)**:
  The Director and Showrunner Assistant present each scene **interactively in the chat window** for the user (Executive Director):
  1. Present the **Scene Directorial Card**:
     - *Dramaturgical Intent & Spine Progress*: What value shifts (`00:00 → 00:10`), whose power changes, how this scene advances the Episode Dramatic Spine (CDQ).
     - *Cross-Scene Dialogue Relay*: Inbound Baton received from Scene N-1 (keyword echo, emotional aftershock, causal retaliation), Tactical Action Subtext (`[ATTACK]`, `[DEFEND]`, `[PROBE]`, `[BARGAIN]`, `[TRAP]`), Spoken line (Gate 4B: ≤32w single / ≤15w per speaker in a two-shot), and Outbound Baton thrown to Scene N+1.
     - *Camera Choreography & 3D Staging*: Scale (CU, OTS, M2S, etc.), Angle, Camera Movement motive, 180° axis alignment.
     - *Actor Micro-Biomechanical Acting*: Breathing, eyelines, tactile prop handling, somatic reactions.
     - *Dialogue Delivery & Foley*: Spoken lines with vocal timbre & parentheticals + Diegetic room Foley.
     - *AI Video Prompt Preview*: Code Block 1 (Visual Latent Prose) & Code Block 2 (Handover State).
  2. Ask for the user's directorial review:
     - *"Đạo diễn đánh giá phân cảnh này thế nào? Có cần tinh chỉnh góc máy, diễn xuất hay câu thoại nào trước khi chốt sang cảnh tiếp theo?"*
  3. Seamlessly apply adjustments, lock the Kinetic Baton Relay (`00:08.5–00:10.0` exit vector → `00:00.0–00:01.5` entry vector), and move to Scene N+1 upon user signal.
  4. Once all scenes are approved in chat, automatically trigger deterministic compile into `tap-X.html` and run `episode_audit_suite.py`.

#### Director's Core Craft Steps per Scene:
For each scene in order:
1. Read the scene's Intent Card (§8.3) and locate the value shift: the moment power, knowledge, or feeling flips. Verify that dialogue is locked into the 4-Way Dialogue Relay (never bubble dialogue) and actively serves the Episode Dramatic Spine (CDQ). The shot plan turns at that moment.
2. Pick a track with the Doctrine §2.5 question: **A** single continuous take (one unbroken breath; camera transitions in-camera) or **B** multi-shot cuts on the 180° axis (both sides of a collision). Shot count and phase splits follow the beats; there is no fixed 3-shot quota and no fixed split.
3. Choose scale, angle, and movement per shot from intent (Doctrine §2.1–2.3). Every camera move names its motive: follow attention, reveal information, or inner shift. Static is a valid choice. Write a one-clause reason per shot in the `[TIMELINE SHOTS]` row of the scene audit card.
4. **The 3-Tier Spatial Staging & Interpersonal Grounding Law (DIRECTOR.md §1c & Pillar 4 §2.1)**:
   - **Tier 1 (Context 3D Architecture)**: Never write a superficial 1-line context. Enforce the 5-Vector standard: room boundaries, key fixed landmarks and relative distances between them, directional lighting physics, and atmospheric medium.
   - **Tier 2 (Zero-Frame Interpersonal Grounding at $t=0.0\text{s}$)**: In multi-character scenes, define initial physical coordinates, relative proximity (e.g. 1.5m apart), 180° Action Axis & eyeline vectors (who is looking where), operational relationship/dynamic, and tactile prop/fixture contact at $t=0$.
   - **Tier 3 (The Biomechanical Action Launchpad at $t>0$)**: Author timeline actions strictly launching from the Tier 2 zero-frame postures and contacts, preserving established 3D geometry and 180° eyelines. Zero teleportation, zero spatial chaos.
5. Block in 3D (Pillar 3 & DIRECTOR.md §3b): architectural anchors, eyelines (speaker locks on listener, listener reacts, height delta), 180° axis, and the Multi-Character Blocking Matrix (Solo CU = 1 face; OTS/M2S = 2 persons; Triangular M3S/Master = 3 persons; passive child anchor). For falls or collisions, apply the vector-to-plane law and 5-step elastic deformation.
6. Write Code Block 1 (§9.3) and Code Block 2 (§9.5).
7. Use Code Block 2 as the launchpad for the next scene. Apply the **Inter-Clip 10s Continuity & Temporal Handshake Protocol** (Compiler §4.5 & Grammar §1.3): the terminal vector at `[00:08.5–00:10.0]` of Scene N forms the Outbound Baton, caught and completed seamlessly by the Inbound Baton at `[00:00.0–00:01.5]` of Scene N+1 from the new camera angle/subject. Strictly enforce zero action repetition across the cut, 180° screen direction invariance, and auditory suture (L-cuts and uniform diegetic Foley).

### 9.3 Code Block 1 — Canonical Syntax Template
```
Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Style: [project visual style header]. [Track A — one continuous take, zero cuts | Track B — multi-shot sequence cut on the 180-degree axis].

[context]:
[evocative location name in natural English without underscores] [100% Refer to image <location_ref>], [exact time of day]. [5-Vector Environmental Specification: full physical architectural layout, inventory of all key fixed furniture and room landmarks ("có cái gì ở đó"); key light source, angle/direction, natural color tone without Kelvin, shadow behavior; atmospheric medium (dust motes, humidity) and emotional climate].

[subject]:
[ho_ten_A] [100% Appearance, attire, and facial features Refer to image 1], [initial architectural spatial anchor and physical posture, hands naturally free of props/weapons] — the only [ho_ten_A] in frame.
[ho_ten_B] [100% Appearance, attire, and facial features Refer to image 2], [initial architectural spatial anchor and physical posture, relative distance to ho_ten_A (e.g. 1.5m across aisle), 180° Action Axis & eyeline vector facing ho_ten_A, hands naturally free of props/weapons] — the only [ho_ten_B] in frame.

[PROP]:
[hero prop name in natural English without underscores] [100% Refer to image <prop_ref>], [physical state], [resting place on in-scene fixture independent of character hands] — the only [prop noun] in frame.
[everyday prop name in natural English without underscores], [hyper-clear material & visual text description], [resting place on in-scene fixture independent of character hands] — the only [prop noun] in frame.

Diegetic room acoustics: [room tone and Foley].

[00:00–00:03.5] [Scale framing ho_ten_A], [angle], [camera move / optical focal depth (e.g. shallow depth of field holding sharp focus on ho_ten_A with background softly falling into bokeh)] — [ho_ten_A] [bodily movement and visceral somatic prelude], [expressive action-verb: furiously snapping / breathlessly pleading / etc.] : “ [line] ”（Voice of a [N]-year-old [man/woman] from [region]; [vocal timbre: trầm hay bổng], [cảm xúc khi nói], [audio tag]）; [ho_ten_B] [one synchronized reaction].

[00:03.5–00:07.5] [Track B: Cut to] [scale framing ho_ten_B], [angle], [camera move / optical focal depth] — [ho_ten_B] [somatic physical reaction], [expressive action-verb] : “ [line] ”（Voice of a [N]-year-old [man/woman] from [region]; [vocal timbre: trầm hay bổng], [cảm xúc khi nói], [audio tag]）; [ho_ten_A] [reaction].

[00:07.5–00:10.0] [Scale], [angle], [camera move] — [terminal beat: micro-expressions, breathing, natural deceleration handing momentum to the next scene; never a frozen frame].

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored to the architecture; characters move only where the action says they move.
Do not generate subtitles, dialogue text, titles, timestamps, or written text anywhere in the video. Do not render duplicate characters or extra props.
```
Template notes:
- The template shows syntax, not rhythm. Phases are contiguous and non-overlapping; use ≥ 2 (Gate 3M). Phase count, split points, which phases carry lines, and which carry silence all come from the scene's beats. Fewer than half the scenes of an episode should share the same split (the audit warns).
- Voice modes: one speaker, V.O. (parenthetical states `inner voice-over, lips remain sealed`), O.S., or no lines at all are all valid inside this template (Doctrine §4.2). A reply never needs to open with an address word.
- Never write lens millimeters, f-stops, fps, camera brands, or Kelvin.
- Use proper names only; no pronouns in visual prose (Gate 3C).
- Gate 4B word cap per spoken line (Hard Constraint): ≤ 32 words single speaker, ≤ 15 words per speaker in a two-shot. Clip density is a craft default (`0b` §7: 10s ≈ 12–24 Vietnamese syllables or 8–13 English words; 15s ≈ 18–36 syl; 30s ≈ 35–70 syl); peak scenes often need far fewer.
- Syntax (`0b` §8): one time bracket + one short camera clause (scale, angle, move, optical focus) + `—` + prose. Dialogue lines use the **Somatic Action-Speech Fusion Standard**: dialogue is an organic physical action integrated into bodily movement and breathing, using expressive speech-action verbs with adverbs (`furiously snapping :`, `breathlessly pleading :`, `icily hissing :`) rather than sterile, detached statements. No `△`, no `|` pipes, no `Shot 1` / `Phase 1` labels (audit warning W6). The track is declared in the style line; Track B phases after the first open with `Cut to`.
  * **The Optical Camera Clause Law (Quy Chuẩn Quang Học Camera Trước Dấu Gạch Ngang — Banning Dangling "Focus on [name]")**:
    - Mọi thông số về chủ thể được đóng khung (Subject Framing), mặt phẳng tiêu cự quang học (Focal plane), và độ sâu trường ảnh (Depth of field / bokeh) BẮT BUỘC được khai báo trực tiếp trong phần Camera Clause (trước dấu gạch ngang `—`), ví dụ: `Medium close-up framing ho_ten_A at eye level, shallow depth of field holding sharp optical focus on ho_ten_A's facial features with background softly falling into bokeh, slow push-in — [action]`.
    - Trong cảnh qua vai (OTS): `Over-the-shoulder medium shot framing ho_ten_B past ho_ten_A's soft-focus foreground shoulder, razor-sharp optical focus locked on ho_ten_B at eye level, static camera — [action]`.
    - **TUYỆT ĐỐI CẤM** viết câu đuôi cô độc `Focus on [name].` ở cuối đoạn văn mô tả hành động. Thao tác này là lỗi kiến trúc câu lệnh cẩu thả làm phân mảnh prompt và khiến AI video diffusion model bị loạn tiêu cự.
  * **The Two-Shot Profile Stagnation Law (Luật Chống Bẫy Nhìn Nhau Bất Động Trong Two-Shot Profile 90°)**:
    - **CẤM TUYỆT ĐỐI giữ Two-Shot Profile tĩnh > 2.5–3.0 giây**: Hai người đứng đối mặt ngang 90° nhìn sang hai mép màn hình suốt 10s là bẫy đạo diễn tai hại khiến nhân vật nói xong 1 câu thì 7 giây sau đứng chết lặng nhìn nhau đờ đẫn, mặt nghiêng mất khối cơ và méo khẩu hình.
    - **Chỉ cho phép Two-Shot Profile trong 3 trường hợp**:
      1. *Thiết lập xung đột ngắn (< 3s)*: Đứng ngang gườm nhau 2s trong Track B rồi lập tức cắt (`Cut to`) sang OTS hoặc CU trên trục 180°.
      2. *Va chạm giằng co vật lý liên tục*: Hai người trực tiếp vật lộn cơ học (kéo giằng chiếc túi, bẻ cổ tay, níu vạt áo), động lực chuyển động không ngắt quãng một giây nào.
      3. *Cú máy lướt vòng cung (In-Camera Orbital Glide)*: Máy quay di chuyển lướt vòng cung từ góc nghiêng 90° vòng sang góc 3/4 trực diện để bắt trọn ánh mắt và khẩu hình.
  * **The Master Camera Model Architecture (Hệ Thống Phân Loại Mô Hình Máy Quay)**:
    - **Track A — Single Shot Continuous Take**: 1 camera duy nhất, 0 nhát cắt (0 cuts), biến thiên cỡ cảnh và góc nhìn hoàn toàn qua chuyển động camera (`slow push-in`, `tracking`, `pedestal`, `arc`) hoặc sự di chuyển của nhân vật.
    - **Track B — Multi Shot / Multi-Camera Coverage**: 2 đến 4 nhát cắt biên tập (`Cut to`) khóa chặt trên Trục Hành Động 180°. Mỗi nhát cắt đổi góc $\ge 30^\circ$ hoặc đổi cỡ cảnh. Thích hợp cho đấu khẩu dồn dập và nhịp điệu hài hước sitcom.
    - **Track AB — Kép / Hybrid Take**: 1 cú máy dài (Master Take $\ge 5.0\text{s}$, trải qua 2+ micro-phases) + 1 đến 2 nhát cắt sắc lẹm (`Cut to`) bộc phá ở thời điểm chuyển giao quyền lực hoặc va chạm đỉnh điểm.
    - **Special Directorial Sub-Types**:
      - `Track A-Locked`: Khóa cứng camera 100%, 0 di chuyển, 0 cắt, làm Mỏ Neo Hấp Dẫn (Gravitational Anchor), giới hạn nghiêm ngặt $\le 1\text{–}2$ cảnh/tập. Tuyệt đối cấm từ "tripod".
      - `Single-Take Rack Focus & Tracking`: Chuyển dịch mặt phẳng nét quang học từ tiền cảnh sang hậu cảnh không qua nhát cắt.
      - `In-Camera Dynamic Transition`: Chuyển từ góc nhìn thứ nhất (P.O.V) sang góc nhìn khách quan (MCU) bằng chuyển động nâng (pedestal) + lướt vòng cung (arc).
      - `Dynamic Re-Framing`: Tự động tái đóng khung theo chuyển động đứng/ngồi của nhân vật.
  * *Special Track A-Locked Exception (Exclusive)*: For locked-off static performance takes (`Track A-Locked`), shot scale, angle, optical framing, and camera stability are invariant across the entire take. The camera setup is declared directly in natural prose once at the head of the action section (immediately after audio, declaring scale, subject framing, optical focus, angle, and simply `static camera` without any `[camera]:` tag and strictly banning the word "tripod" to avoid physical equipment hallucination, e.g. `Eye-level medium close-up framing ho_ten_A, shallow depth of field holding razor-sharp optical focus on ho_ten_A's face with background softly falling into bokeh, static camera.`). The sub-timeline brackets (`[00:00–00:03.5]`, `[00:03.5–00:07.0]`, etc.) are dedicated 100% to character somatic performance, speech-action fusion, and living environmental physics without repeating camera clauses and with ZERO dangling `Focus on [name].` tags.
     - **The Sovereign Hero Prop Law**: Thẻ `[PROP]:` is strictly for Tier 1 Hero Props; everyday domestic items (blankets, pillows, chairs, beds) belong 100% to `[context]:`. If no hero prop: `[PROP]: none (pure environmental and somatic staging)`.
     - **Natural Somatic-Speech-Physics Fusion**: Strictly ban hollow adjectives ("lấp lánh yêu thương", "nũng nịu"); anchor acting to physical causality, tactile friction, and breath exhalation.
- Timing (`0b` §2–§5): time every line in seconds (calm speech ≈ 3.5–4.5 Vietnamese syllables/s or 2.0–2.5 English words/s). A phase that carries a lip-synced line lasts ≥ line + 1.0s, starts the line ≥ 0.3s in, and ends it ≥ 0.8s before the cut (audit W4). Each camera move gets at least its §5 duration; never lip-sync while a crane, orbit, arc, or whip is traveling. Speech stays ≤ ~60% of the clip (audit W5).
- Duration: 10s always; 15s / 30s only on explicit user request (§2.4), with the last bracket ending at `00:15` or `00:30`.
- Never give lip-synced dialogue during a downward POV shot. Transition to a frontal MCU/MS first.
- Minor-safety lexicon and cu_tin Somatic Sleep Staging Protocol: Pillar 4 §[10d] & DIRECTOR.md §6.

### 9.4 Silent Scenes & Silent Film
Applies to every scene of a Silent Film and to any individual silent scene inside a dialogue project. Remove every dialogue line and voice parenthetical from that prompt. Amplify micro-biomechanics and Foley. Replace the final negative line with:
```
Do not generate subtitles, dialogue text, titles, timestamps, or written text anywhere in the video. Do not generate spoken dialogue, lip movement matching speech, or voiceover. Do not render duplicate characters or extra props.
```
> Gate 4 accepts prompts without lines; verbatim parity is checked only where lines exist (card → prompt and prompt → card). Never add filler dialogue to satisfy a gate.

### 9.5 Code Block 2 — Handover @00:10 (Vietnamese)
Covers: active characters with architectural position, posture, and gaze; props with state and holder; lighting and atmosphere (no Kelvin); a dialogue word audit; the kinetic bridge to the next scene. No coordinates (Gate 3H).

### 9.6 Tier 1 Scene Audit Card (Vietnamese, inside `tap-X.html`)
Labels: `[STYLE & OPTICS]`, `[CONTEXT]`, `[SUBJECT]`, `[PROP / SURFACE]`, `[DIEGETIC SOUND]`, `[TIMELINE SHOTS]` (time window + scale + angle + move per phase, same split as Code Block 1), and a Track badge (Director's Lock). The badge, the Code Block 1 header, and the timeline all declare the same track.

Above the scene cards, `tap-X.html` publishes the episode's Story Spine card (`id="story-spine"`, Doctrine §8.10 + §9.9). The audit reads it for W9 and W10.

### 9.7 Compile & Audit (Mandatory)
0. Run the Creative Review (Doctrine §5) on the drafted episode before compiling.
1. Build the episode through `engine/prompt_compiler.py` (`compile_and_validate_episode()`): sanitize → assemble → audit → write. Never hand-type the HTML.
2. Project-specific build scripts live in `output/<slug>/scripts/` (not the workspace root).
   - **Revision mode** (an existing, approved `tap-X.html`): write a scene-scoped patch script in `output/<slug>/scripts/` (backup first; every replacement asserted by count), then pass the result through `compile_and_validate_episode()`. Never edit the HTML by hand.
3. Re-run standalone: `python engine/episode_audit_suite.py output/<slug>/tap-X.html`. Any failure blocks delivery.
4. The audit also prints non-blocking warnings. Fix each one, or justify it in one line in the CP4 summary:
   - **W1–W3 monotony**: repeated phase splits, repeated reply openers, voice-mode runs, uniform turn counts
   - **W4–W6 timing and syntax**: lip-sync window, speech share ≤ ~60% of the clip, legacy syntax
   - **W8 camera**: a lip-sync-unsafe move under a line without a "settles before" clause; track label mismatch
   - **W9 story depth**: title spoken, feelings labelled, Story Spine missing
   - **W10 plot engine**: < 2 BROKEN predictions, a plant not earlier than its payoff, a loop paid before its plant
   - **Scene count**: an episode that differs from `project_rules.json` → `episode_scenes`
   - (W7 is reserved.)

### 9.8 Pre-Flight Checklist (automated gate → manual check)
| Check | Gate |
|---|---|
| No freeze holds | 3B |
| No hardware / Kelvin jargon | 3D |
| No clothing in prose | 3E |
| No numeric age outside the voice parenthetical | 3A |
| No pronouns in prose | 3C |
| No minor lexicon | 3F |
| Master prefix present | 3G |
| No coordinate math document-wide | 3H |
| Stateless (no cross-scene references) | 3I |
| 3-block labels | 3J |
| Reference anchor syntax | 3K |
| Blank-line spacing | 3L |
| No `[camera]:` tag (natural prose line declaration) | 3P |
| No `tripod` word in prompt prose (Hardware Literalization Bug immunity) | 3Q |
| Meaningful English asset naming (Locations & Props) | 3R |
| Sovereign Hero Prop Law (No domestic furnishings in `[PROP]:`) | 3S |
| Zero ghost objects (Comprehensive In-Context Setting Inventory) | 3T |
| Track A-Locked Quota (Strictly <= 2 scenes per 9–10 scene episode) | 3U |
| ≥ 2 phases, contiguous from 00:00 to a 10 / 15 / 30s end | 3M |
| Stability + negative clause | 3N |
| Dialogue ↔ prompt verbatim parity (where lines exist; silent scenes allowed) | 4 |
| Single-Speaker 25–30w (cap ≤ 32w); Two-Shot ≤ 15w/speaker | 4B |
| Line causality: back-to-back lines by one speaker inside an exchange (warning) | 4C |
| Kinship address ladder (`project_rules.json`, if present) | 4D |
| Meal continuity (`project_rules.json`, if present) | 4E |
| Colloquial grammar (`project_rules.json`, if present) | 4F |
| Copy buttons + copy-all + toast | 5 |
| Monotony warnings: phase splits, reply openers, voice-mode runs, turn counts | W (non-blocking) |
| Timing warnings: lip-sync window per phase (W4), speech share ≤ ~60% (W5), canonical syntax (W6) | W (non-blocking) |
| Camera under a line / track label (W8); story depth and Spine present (W9); prediction ledger and plant order (W10) | W (non-blocking) |
| **Creative Review**: Story Spine + plot rows, Intent Card per scene, value shift, Action↔Line relation per line, motive per camera move, voice-mode rhythm | Doctrine §5 |
| **Manual**: one-move rule per phase; multi-character blocking matrix sync (CU=1 face, OTS/M2S=2, M3S/Master=3; DIRECTOR.md §3b); anti-ghost prop (one instance, surface cleared, fixtures never teleport); eyeline & 180° axis; architectural anchoring (no frame labels); track declared in 3 places; dialogue language matches §2.2; 16:9 sheet prompts with copy buttons embedded | — |

### 9.9 ✋ CHECKPOINT 4 (per episode)
```
✋ CHECKPOINT 4 — tap-[N].html hoàn tất ([S] cảnh × [D]s) — Audit: ALL GATES PASSED
File: output/<slug>/tap-[N].html
Tóm tắt: [bảng 1 dòng/cảnh: cảnh | track | chế độ thoại | người nói | số từ | bridge] + cảnh báo rập khuôn còn lại (nếu có) kèm lý do
→ "ok" sang Tập [N+1] (hoặc Stage 5) | "edit [nội dung]" | "scene [K]: [chỉnh sửa]"
```

---

## §10 — STAGE 5: DISTRIBUTION (`seo-youtube.html`)

> Load the Growth Architect skill. Mandatory for every project.

- **Tier 1 — Omnibus (full movie)**:
  - 5 A/B title formulas, 50–65 characters each
  - 4 thumbnail prompts on the 4 Sovereign Pillars: suspended catastrophe, extreme duality, embedded 3D title, mobile safe zones
  - 4-tier description with 10s chapters for every scene
  - Master tag string ≤ 500 characters
  - Polarizing pinned comment
- **Tier 2 — Per episode**: `[Ep N/T]` title with a cliffhanger hook, a dedicated thumbnail prompt, a description with that episode's chapters, and a pinned comment linking to the next episode.
- **Binge funnel**: daily premieres at 19:30, the omnibus 24h after the finale, end screens chaining Ep N → N+1. If CTR < 6.5% after 3h, swap the title/thumbnail variant.

✋ **CHECKPOINT 5** → on approval, run §11 finalize → 🎬 DONE.

---

## §11 — REGISTRY UPDATE (MANDATORY)

- **Draft at CP1**: append names, visual style, genre and background, tropes, prop group, and narrative mode.
- **Finalize at CP5** (or when the user abandons the project): add the hook, karma direction, track, escalation variant, twist type, cliffhangers, and lighting. Append `story_history` and increment `total_stories_produced`.
- Also refresh `session_log` (recent hooks, names, props, locations, styles, cliffhangers).

```json
"story_history": [{ "slug": "kebab-case", "title": "...", "format": "Short Film | Series | Music Video",
  "theme": "...", "lesson": "...", "episodes": 1, "date": "YYYY-MM-DD", "visual_style": "...", "status": "draft | complete" }]
```

---

## §12 — ABSOLUTE RULES

| ✅ Do | ❌ Never |
|---|---|
| Infer and state assumptions | Ask about things already clear |
| Stop at every checkpoint | Jump stages without approval |
| Deliver one full episode per CP3 / CP4 | Drip scenes one at a time, or dump all episodes unasked |
| Follow §2 when files conflict, and report the conflict | Guess between conflicting rules silently |
| Run Gate 1.5 and the episode audit before presenting | Present an unaudited file |
| Run the Dialogue Pre-Flight (relationship, power dynamic, address forms A→B / B→A, shift this beat) before writing dialogue | Change address forms without a declared shift |
| Write the Story Spine (with the Prediction Ledger) before any scene | Assemble a story only from catalog entries |
| Choose voice mode, scale, angle, and camera movement per scene from intent, each with a one-clause reason (Doctrine) | Lock one voice mode, one rhythm, or one phase split for every scene |
| Break a Craft Default when the scene needs it, with a `BREAK:` line | Break a Hard Constraint (§2.10) |
| Enforce Directorial Symphony & Kinetic Baton Relay (Exit vector = Entry vector, dynamic voice modes) | Write isolated, fragmented prompt cards or monotonic identical dialogue templates |
| Follow modular genre specifications (`engine/genres/`) when activated | Force serial drama cliffhangers onto a sitcom or cheat an earned healing drama resolution |
| Update the registry at CP1 and CP5 | Skip the registry |
| Write system files in English | Edit system files in Vietnamese or mixed language |

---

## §13 — WORKSPACE FILE MAP

```
d:\Project\Sven\
├── AGENT.md                    ← Level 1 Showrunner (identity, routing, compliance)
├── workflow.md                 ← This file (pipeline + System Defaults)
├── history-registry.json       ← 14-axis anti-repetition registry
├── README.md
├── .agents\
│   ├── SCREENWRITER.md         ← Level 2 Screenwriter (Pillars 1–2)
│   ├── DIRECTOR.md             ← Level 2 Director (Pillars 3–4)
│   └── skills\ director\ · screenwriter\ · youtube-growth-architect\
├── engine\
│   ├── prompt_compiler.py      ← Deterministic tap-X.html compiler
│   ├── episode_audit_suite.py  ← Stage 4 gates
│   ├── setting_audit_suite.py  ← Gate 1.5
│   └── references\  0-creative-doctrine.md · 0b-temporal-camera-grammar.md · 1-narrative-screenplay-architecture.md
│                    2-casting-worldbuilding-specification.md · 3-cinematography-3d-staging.md · 4-ai-video-prompt-compiler.md
└── output\<slug>\  setting.html · tap-1..N.html · seo-youtube.html · scripts\
```

# WORKFLOW — Sven Production Engine (Master Operating Pipeline)

> ⚠️ **READ THIS ENTIRE FILE FIRST — EVERY SESSION, BEFORE ANY ACTION.**
> This file is the **Constitutional Pipeline Coordinator (SSOT)**. It governs the 6-Stage Master Production Pipeline (`Stages 0–5`, `Checkpoints CP0–CP5`), System Defaults (§2), and Stage-Gated Just-In-Time (JIT) context loading. Detailed craft catalogs reside in the Thinking Layer (`0`, `0b`), the 4 Master Pillars (`1–4`), and the Genre Modules (`engine/genres/*.md`).

---

## §0 — CANONICAL FILE READING ORDER & JIT LOADING PROTOCOL

```text
[1]   workflow.md                                           ← Pipeline Coordinator, System Defaults (§2), Checkpoints (CP0–CP5)
[2]   AGENT.md                                              ← Level 1: Executive Producer & Showrunner (routing & gatekeeping)
[2b]  engine/runbooks.json                                  ← Production Presets Catalog (1-click project initialization)
[3]   history-registry.json                                 ← 14-Axis Anti-Repetition Memory
[4]   .agents/SCREENWRITER.md                               ← Level 2: Master Screenwriter (active at Stages 0, 1, 2, 3)
[5]   .agents/DIRECTOR.md                                   ← Level 2: Film Director (active at Stage 2 spatial review & Stage 4)
[5b]  .agents/skills/combat-director/SKILL.md               ← Level 2: Combat Director (active at Stage 4 for Action/Chase/Combat)
[6]   .agents/skills/youtube-growth-architect/SKILL.md      ← Level 2: Growth Architect (active at Stages 0 and 5)
─── THE THINKING LAYER (load BEFORE any Pillar at Stages 1–4) ───
[7]   engine/references/0-creative-doctrine.md              ← Creative Doctrine: Two-Layer Core, 6 Anti-Shallow Depth Laws, Spine & Plot Engine
[7b]  engine/references/0b-temporal-camera-grammar.md       ← Temporal & Camera Grammar: speech rates, lip-sync windows, canonical syntax
─── THE 4 MASTER PILLARS & SPECIALIZED DIRECTORIAL ASSISTANTS ───
[8]   engine/references/1-narrative-screenplay-architecture.md   ← Pillar 1 SSOT: Narrative, Twist Catalog (TW-01..20) & 8 Dialogue Models
[9]   engine/references/2-casting-worldbuilding-specification.md ← Pillar 2 SSOT: Cast Topology, 16:9 Model Sheets, setting.html Spec
[10]  engine/references/3-cinematography-3d-staging.md           ← Pillar 3 SSOT: 14 Shot Scales, 4-Axis Angles, 3D Staging, 180° Axis
[10b] engine/references/3b-lighting-atmospheric-physics.md       ← Assistant 3B: 6-Point Lighting Contract & Atmospheric Mediums
[11]  engine/references/4-ai-video-prompt-compiler.md            ← Pillar 4 SSOT: Stateless Prompts, Code Blocks 1/2, Minor Safety
[11b] engine/references/4b-diegetic-foley-sound-design.md        ← Assistant 4B: 4-Layer Diegetic Foley & Soundscape Continuity
```

> **Stage-Gated Just-In-Time (JIT) Loading Law & Anti-Truncation Line-Range Protocol (`≤ 800-Line Single-Call Guarantee`)**:
> Because the `read_file` tool returns at most **800 lines per call**, calling a blind `read_file` from line 1 on a 2,000–3,000-line Pillar file will truncate the bottom 70% of the file and cause the AI to improvise! Therefore:
> 1. **Self-Contained `< 700-Line` Execution Cores First**: All mandatory execution rules, decision matrices, and output schemas are consolidated inside **`workflow.md` (read by stage slice)**, **`.agents/SCREENWRITER.md` (`407 lines` — 100% read in 1 call)**, **`.agents/DIRECTOR.md` (`699 lines` — 100% read in 1 call)**, and **`0b-temporal-camera-grammar.md` (`491 lines` — 100% read in 1 call)**.
> 2. **Exact `StartLine–EndLine` Coordinates for Large Catalog Pillars**: Whenever consulting a Pillar catalog (`1–4`), ALWAYS pass the exact `StartLine` and `EndLine` listed below (never read blindly from line 1 to 3000):
>    - **Startup (`K0–K3`)**: `workflow.md` (`StartLine: 1, EndLine: 295`) + `AGENT.md` (`StartLine: 1, EndLine: 90`) + `engine/runbooks.json` + `history-registry.json`
>    - **Stage 0 (`Concepts → CP0`)**: `workflow.md` (`StartLine: 292, EndLine: 345`) + `.agents/SCREENWRITER.md` (`StartLine: 1, EndLine: 410`) + `0-creative-doctrine.md` (`StartLine: 170, EndLine: 215` & `StartLine: 536, EndLine: 635`)
>    - **Stage 1 (`Master Storyline & Blueprint → CP1`)**: `workflow.md` (`StartLine: 341, EndLine: 440`) + `1-narrative-screenplay-architecture.md` (`StartLine: 850, EndLine: 1055` — **20/80 Structural Law: 6 Genre Engines & 5 Episode Archetypes**; `StartLine: 1445, EndLine: 1515` — **20 Twists Catalog**) + active `engine/genres/*.md` (`100% read in 1 call`)
>    - **Stage 2 (`Pre-Production Resource File setting.html → CP2`)**: `workflow.md` (`StartLine: 435, EndLine: 505`) + `2-casting-worldbuilding-specification.md` (`StartLine: 390, EndLine: 720` — **16:9 Model Sheets Mẫu 1A/1B/2/2B/3**; `StartLine: 1410, EndLine: 1746` — **`setting.html` 10-Section Spec**; `StartLine: 1770, EndLine: 2215` — **50 Master Visual Styles**)
>    - **Stage 3 (`Episode N Rough Script & Deep Per-Scene Breakdown in Chat → CP3`)**: `workflow.md` (`StartLine: 500, EndLine: 680`) + `.agents/SCREENWRITER.md` (`StartLine: 1, EndLine: 410`) + `0b-temporal-camera-grammar.md` (`StartLine: 1, EndLine: 491`) + `1-narrative-screenplay-architecture.md` (`StartLine: 1307, EndLine: 1415` — **12 Hooks & 5 Bridges**; `StartLine: 1865, EndLine: 2265` — **WPS, 3-Layer Cadence & 9 Voice Modes**)
>    - **Stage 4 (`Interactive Scene-by-Scene Prompt Production & Visual Cross-Check in Chat → CP4`)**: `workflow.md` (`StartLine: 675, EndLine: 830`) + `.agents/DIRECTOR.md` (`StartLine: 1, EndLine: 705`) + `0b-temporal-camera-grammar.md` (`StartLine: 218, EndLine: 415` — **Canonical Prompt Syntax & 10s/15s Modes**) + (`combat-director/SKILL.md` for `Seedance` Action/Chase scenes)
>    - **Stage 5 (`Distribution Packaging → CP5`)**: `workflow.md` (`StartLine: 825, EndLine: 895`) + `.agents/skills/youtube-growth-architect/SKILL.md` (`StartLine: 1, EndLine: 500`)

---

## §1 — AUTHORITY MATRIX & STAGE RACI GOVERNANCE

### 1.1 Single Owner per Knowledge Domain

| Domain | Canonical File | Exclusive Authority Scope | Active Stages |
|---|---|---|---|
| **Pipeline** | [`workflow.md`](file:///d:/Project/Sven/workflow.md) | Master 6-Stage Pipeline (`Stages 0–5`), Checkpoints (`CP0–CP5`), System Defaults (§2) | All (`0–5`) |
| **Showrunner** | [`AGENT.md`](file:///d:/Project/Sven/AGENT.md) | Crew routing, Runbook locking, Checkpoint enforcement, Quality Gate execution | All (`0–5`) |
| **Registry** | [`history-registry.json`](file:///d:/Project/Sven/history-registry.json) | 14-Axis Anti-Repetition Memory (names, props, hooks, twists, visual styles) | `K1`, `CP2`, `CP5` |
| **Doctrine** | [`0-creative-doctrine.md`](file:///d:/Project/Sven/engine/references/0-creative-doctrine.md) | Two-Layer Architecture (§0.05), 6 Root-Cause Anti-Shallow Laws (§1.2), Story Spine (§8), Plot Engine (§9), 4 Cinema Tiers (§10), Scene Intent Engine (§1), Directing from Intent (§2), Action↔Line Synergies (§3), Voice Mode Palette (§4), Creative Review (§5) | `0`, `1`, `3`, `4` |
| **Grammar** | [`0b-temporal-camera-grammar.md`](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md) | Speech rates (VN syllables/s, EN words/s), lip-sync windows, camera-move durations, lip-sync safety, phase density, canonical prompt syntax, 10s / 15s / 30s modes | `3`, `4` |
| **Pillar 1** | [`1-narrative-screenplay-architecture.md`](file:///d:/Project/Sven/engine/references/1-narrative-screenplay-architecture.md) | 6-Beat Short Film vs. 4-Act Series (`20%/45%/25%/10%`), Triple-Helix `A/B/C-Plot` Weave, 12 Hooks, 20 Twists (`TW-01..20`), 8 Dialogue Models, 4-in-1 Parentheticals, Genre-Calibrated Resolution | `0`, `1`, `3` |
| **Pillar 2** | [`2-casting-worldbuilding-specification.md`](file:///d:/Project/Sven/engine/references/2-casting-worldbuilding-specification.md) | Cast topology (`A1/A2/Tier B/Tier C`), Dynamic Cast Sizing, 6-Cultural Naming Matrix, Living Continuum, 16:9 Model/Prop/Location Sheet Templates (`Mẫu 1A/1B`, `Mẫu 2`, `Mẫu 2B 3D Semi-Real`, `Mẫu 3`), `setting.html` 10-Section Spec, 50 Visual Styles (`25 Live Action + 25 Animation`), 30 Genres | `1`, `2`, `3` |
| **Pillar 3** | [`3-cinematography-3d-staging.md`](file:///d:/Project/Sven/engine/references/3-cinematography-3d-staging.md) | 14 Shot Scales, 4-Axis Angles, Camera Combos, 3D Spatial Staging, Elastic Deformation, 180° Action Axis, Continuity Ledgers, Music Video Architecture | `2`, `4` |
| **Pillar 4** | [`4-ai-video-prompt-compiler.md`](file:///d:/Project/Sven/engine/references/4-ai-video-prompt-compiler.md) | Stateless 10s/15s Kinetic Units (`Standard 10.0s` & `Seedance 10.0s / 15.0s`), 3-Case Continuity Reference Law (`TH1 / TH2 / TH3`), Track A/B/AB/A-Locked, Mode B Reference Laws, Code Blocks 1 & 2, Minor Protection Protocol (§[10d]) | `4` |
| **Combat** | [`combat-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md) | All scenes flagged `[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s]` across all genres: high-velocity chases, pursuits, ambushes, struggles, martial arts & supernatural combat, 5–6 Shot Kinetic Contrast Storyboard (zero `→` arrows), Weapon Hand-Grip & Empty-Hand Locks | `3`, `4` |
| **Growth** | [`youtube-growth-architect/SKILL.md`](file:///d:/Project/Sven/.agents/skills/youtube-growth-architect/SKILL.md) | Niche validation, Semantic Entity Clusters, High-CTR Titles, 4-Pillar Thumbnails, SEO Packaging | `0`, `5` |
| **Automation** | `engine/setting_audit_suite.py`, `engine/runbook_manager.py` | Pre-production `setting.html` resource linting & project initialization | `2` |

### 1.2 Role Assignment per Stage (RACI & User Collaboration Matrix)

> **SINGLE-HTML RESOURCE RULE (`setting.html` ONLY)**: The system generates **ONLY ONE HTML file (`output/<slug>/setting.html`)** at Stage 2 to prepare all pre-production visual resources (Character 16:9 Model Sheets, Tier-1 Prop Sheets, Location 2×2 Grids). **Never generate `tap-1.html ... tap-N.html` episode HTML files.** All subsequent stages (Stage 3 Episode Rough Scripts and Stage 4 Scene-by-Scene Prompts) are executed **100% interactively in chat**, one episode at a time and one scene at a time, with mandatory cross-checking alongside the User.

| Stage | Checkpoint | Responsible (Executes) | Accountable (Approves) | Consulted & User Visual Input | Mandatory Deliverable & Audit Gate |
|---|---|---|---|---|---|
| **0 — Concepts** | `✋ CP0` | `@Screenwriter` + `@GrowthArchitect` | `Sven-Agent` + **User** | `@Director` | 5 High-Concept Pitches in chat (3-Layer Stakes + Option C Twist) |
| **1 — Master Storyline & Blueprint (`Kịch bản chính`)** | `✋ CP1` | `@Screenwriter` | `Sven-Agent` + **User** | `@Director`, `@CombatDirector` | Interactive in chat: 12-Row Story Spine Card + Dynamic Cast Topology + Short-Film 6-Beat or Series 4-Act (`A/B/C-Plot`, 5 Convergence Nodes, Inter-Episode Bridges & **Cross-Genre Action/Chase `10s/15s` Slots**) Blueprint |
| **2 — Pre-Production Resource File (`setting.html` — Duy Nhất 1 File HTML)** | `✋ CP2` | `@Screenwriter` | `Sven-Agent` + **User** | `@Director` (3D spatial review) + **User** (renders & supplies Character/Prop/Location reference images) | **The SOLE HTML Deliverable**: `output/<slug>/setting.html` (Passes `setting_audit_suite.py` **🛡️ Gate 1.5**) + Registry Draft |
| **3 — Episode Rough Script & Per-Scene Breakdown (`Kịch bản thô từng tập & đi sâu từng cảnh`)** | `✋ CP3` | `@Screenwriter` | `Sven-Agent` + **User** | `@Director`, `@CombatDirector` | **Interactive in Chat (1 Episode at a Time)**: Episode N Rough Script & Deep Per-Scene Breakdown (`Scene 01..M` with 2–3 Smart Location Sequences, 3-Wall Escalation, **Per-Scene `📌 [CHỈ DẪN SẢN XUẤT & THAM CHIẾU CHO USER]` declaring `TH1/TH2/TH3` + `Standard 10s / Seedance 10s-15s`**, Scene Intent Cards, Clean Terminal Landing, & Verbatim Dialogue) |
| **4 — Interactive Scene-by-Scene Directing & Prompt Cross-Check (`Làm từng cảnh 1 & Đối chiếu`)** | `✋ CP4` | `@Director` (+ `@CombatDirector` for all `[⚡ SEEDANCE · 10s/15s]` action/chase scenes) | `Sven-Agent` + **User** | `@Screenwriter` (dialogue parity) + **User** (**ONLY sends `TH1/TH3` Static Terminal Frames `@00:10.0 / @00:15.0`** when connecting same-location scenes; for `TH2` new locations, Agent reads directly from `setting.html` without asking User for images) | **Interactive in Chat (Strictly 1 Scene at a Time — Zero `tap-X.html`)**: `setting.html` / `Last Frame` Cross-Check + 14-Gate Pre-Flight Verification + `Scene K` Code Block 1 & Code Block 2 + Next-Scene Handoff |
| **5 — Distribution & Packaging** | `✋ CP5` | `@GrowthArchitect` | `Sven-Agent` + **User** | `@Screenwriter`, `@Director` | Interactive SEO & Thumbnail Package + `history-registry.json` Finalized |

---

## §2 — SYSTEM DEFAULTS (THE CONSTITUTION)

> **THE TWO-LAYER ARCHITECTURE (`0-creative-doctrine.md` §0.05)**: Every Sven production locks **Layer 1: The Universal 4-Tier Core (50%)** (Tier I Great Screenplay ➔ Tier II Great Film ➔ Tier III Great Multi-Episode Series ➔ Tier IV Addictive Individual Episodes) and dynamically mounts **Layer 2: The Genre & Cultural Adapter (50%)** (`drama.md`, `action.md` + `@CombatDirector`, `microdrama.md`, `sitcom.md`, or `thriller`). Never force one genre's or one region's conventions onto another.

### 2.1 Rule Precedence Hierarchy
When rules appear to conflict, resolve them strictly in this order and report any file discrepancy to the user:
1. **Explicit User Instruction** in the current session (sovereign over aspect ratio, duration, delivery mode, and creative direction).
2. **`workflow.md` §2 System Defaults** (Hard Constraints in §2.11 never yield to any lower layer).
3. **`engine/references/0-creative-doctrine.md` & `0b-temporal-camera-grammar.md`** — `0-creative-doctrine.md` governs *how* narrative and directorial tools are chosen from dramatic intent (overriding fixed word budgets, shot quotas, or mechanical templates in Pillars/Skills); `0b-temporal-camera-grammar.md` is the sole authority for speech rates, timing numbers, and canonical prompt syntax.
4. **Master Pillars 1–4 & Active Genre Modules (`engine/genres/*.md`)** — domain-specific catalogs and genre conventions.
5. **Role Specifications (`AGENT.md`, `.agents/SCREENWRITER.md`, `.agents/DIRECTOR.md`)**.
6. **Skills, Examples, and Legacy Templates**.

### 2.2 Three-Layer Language & Entity Naming Protocol
1. **Language Separation**:
   - **User Communication**: Always Vietnamese; direct, decisive, executive tone.
   - **System Documentation & Codebase** (`.md` rules, skills, references, Python scripts): **100% standard professional English**.
   - **Deliverable Files (`setting.html`, `seo-youtube.html`) & Interactive Chat Outputs**:
     * *Layer 1 — UI, Analysis & Handover Cards*: Vietnamese (titles, Story Spine display, Scene Audit Cards, dialogue breakdown notes, buttons, toasts, and Code Block 2 handover summaries).
     * *Layer 2 — Visual Prompt Prose (Code Block 1)*: Technical cinematic English.
     * *Layer 3 — Spoken Dialogue*: English by default; switches 100% to the target language and regional dialect when specified by the user or preset (e.g., Southern or Northern Vietnamese).
2. **The Triad Entity Naming Standard (Anti-Cloning & Token Clarity)**:
   - **Characters (`[subject]:`, `Shot 1..N` & Speaker Headers)**: Must use **fixed Proper Character Names** (e.g., `Bradley`, `Harold`, `Elena`, `Dante`, `Kael`, `Martha`) across all headers, shots, and dialogue lines to prevent diffusion twin-cloning and enforce the singularity seal (`— the only [Proper_Name] in frame`). Never use `snake_case` tokens (`hoang_nam`, `my_duyen`) or generic nouns (`Woman`, `Man`, `the father`, `the hunter`).
   - **Locations (`[context]:`)**: Must use **evocative, meaningful natural English without underscores** (e.g., `sunlit townhouse open kitchen`, `grand mansion mahogany dining room`, `rain-lashed imperial courtyard`). Transliterated Vietnamese tokens (`phong_cu`, `nha_bep`, `phong_hoc_11a1`) and `snake_case` location names are strictly banned in prompt prose.
   - **Props (`[prop]:`, `[context]:` & `Shot 1..N`)**: Must use **natural English noun phrases strictly without underscores** (e.g., `silver dragon-hilted longsword`, `imperial white jade seal`, `tarnished brass truck keyring`, `leather-bound transfer contract`) so text encoders activate accurate physical weights.
   - **Reference Image Filenames (Ultra-Simple Standardized Naming Law)**: Always use short, intuitive, hyphenated filenames without convoluted prefixes:
     * **Character Outfit Sheets**: `[first_name]-home.jpg`, `[first_name]-work.jpg`, `[first_name]-date.jpg`, `[first_name]-outing.jpg` (e.g., `evan-home.jpg`, `evan-work.jpg`, `evan-date.jpg`, `bradley-outing.jpg`).
     * **Location 2×2 Grids**: `loc-home.jpg`, `loc-work-office.jpg`, `loc-work-port.jpg`, `loc-date.jpg`, `loc-outing.jpg`, `loc-work-bank.jpg`.
     * **Tier-1 Hero Prop, Weapon & Artifact Sheets**: `prop-[short_noun].jpg` (e.g., `prop-sword.jpg`, `prop-jadeseal.jpg`, `prop-keyring.jpg`, `prop-contract.jpg`).

### 2.3 Aspect Ratio Sovereignty & Project Voice Modes
1. **Aspect Ratio Sovereignty Law**:
   - Aspect ratio (`16:9` widescreen, `9:16` vertical, `4:3`, `1:1`, or `2.39:1` anamorphic) is **100% governed by the user's explicit choice and target platform**.
   - Never hard-lock an aspect ratio to a genre. Runbook presets suggest defaults, but the Screenwriter and Director dynamically adapt framing, headroom, and horizontal/vertical blocking to any user-selected ratio.
2. **Project Mode & Per-Scene Voice Mode Palette**:

| Project Mode | Activation | Operational Rule |
|---|---|---|
| ⭐ **Dialogue-Driven Drama** | **DEFAULT** for all films and series | Spoken conflict drives the narrative, while each scene selects its specific **Voice Mode** from `0-creative-doctrine.md` §4 (`Dialogue`, `Rapid Fencing`, `Ensemble`, `Solo + Silent Listener`, `Direct Monologue`, `Inner V.O.`, `Hybrid Spoken + V.O.`, `Off-Screen O.S.`, `Proximity Whisper`, `Interrupted Speech`, `Direct Address`, or `Model 0 Silence`) with a one-clause reason in the Scene Intent Card. Avoid $\ge 3$ consecutive scenes in the same voice mode or identical turn counts across an episode. |
| 🤫 **Silent Film (`Show, Don't Tell`)** | Explicit user request (`"không thoại"` / `"silent mode"`) | Zero spoken dialogue across all scenes; amplified somatic micro-biomechanics, tactile prop friction, diegetic Foley, and the silent negative directive (§9.5). |
| 🎵 **Music Video (`MV Mode`)** | User provides lyrics, song duration, or `"MV mode"` | Governed by Pillar 3 Music Video Architecture (6 beats synced to song structure at `3% / 12% / 35% / 30% / 12% / 8%`). |

### 2.4 Master Genre Library & The 4-Regime Genre Authenticity Firewall (`Tường Lửa 4 Hệ Quy Chiếu Thể Loại Sống Còn`)
To guarantee every script matches its target audience's exact expectations (`"Đúng thể loại mới có khán giả"`), the system enforces a strict **4-Regime Genre Authenticity Firewall (`Zero Cross-Genre Contamination`)**:

| Regime (Hệ Quy Chiếu) | Target Genres & Modules | Core World Rules & Dramatic Engine (Cách Làm Đúng Bản Chất Thể Loại) | Strict Contamination Ban (Tường Lửa Cấm Pha Tạp) |
|---|---|---|---|
| **1. Drama Thực Tế (`Grounded Real-World Drama`)** | Gia đình, Thừa kế, Tỷ phú đời thực, Hôn nhân, Thương trường, Pháp lý, Chữa lành ([`drama.md`](file:///d:/Project/Sven/engine/genres/drama.md), Realistic [`microdrama.md`](file:///d:/Project/Sven/engine/genres/microdrama.md)) | • **100% Quy luật đời thực & Tâm lý con người thật**: Mâu thuẫn xoay quanh tình thân, lòng tham, sự phản bội, di chúc, quỹ tín thác, hợp đồng tiền hôn nhân, sao kê ngân hàng, tranh tụng tại tòa/HĐQT.<br>• **Quy mô tài chính & doanh nghiệp sát thực tế**: Chuỗi khách sạn, bệnh viện tư, bất động sản, logistics (`$50M–$800M` tổng tài sản, `$10M–$50M` quỹ tiền mặt/nợ).<br>• **Cao trào (`15.0s`)**: Đối chất tâm lý liên hoàn, lật tẩy chứng cứ trước đám đông, giằng xé nội tâm trực diện. | **CẤM TUYỆT ĐỐI** đưa thiết bị viễn tưởng (*đồng hồ thần kinh, AI tự động*), phép thuật/siêu nhiên, con số trăm tỷ đô ảo tưởng, hoặc **ép nhân vật đời thường (luật sư, bác sĩ, doanh nhân) đi đột nhập kho cảng, leo trèo parkour hay đánh võ như điệp viên**! |
| **2. Khoa Học Viễn Tưởng (`Speculative Sci-Fi`)** | Công nghệ tương lai, AI/Cyber, Đột biến Y sinh giả tưởng, Hậu tận thế, Sinh tồn không gian | • **Tiền đề Giả định ("What If?") + 3 Quy Luật Cứng**: (1) *Cơ chế khoa học/công nghệ cốt lõi*, (2) *Giới hạn vật lý / Điều kiện sập hệ thống*, (3) *Cái giá đạo đức & sinh tồn của con người*.<br>• Đạo cụ Tier-1 là thiết bị công nghệ cao/mẫu vật sinh học quyết định vận mệnh; rượt đuổi/đột kích công nghệ cao điều phối qua `Seedance (10s/15s)`. | **CẤM** biến phim Sci-Fi thành cãi vã gia đình vụn vặt không gắn với quy luật công nghệ, và **CẤM** dùng phép thuật không giải thích bằng cơ chế khoa học của thế giới đó. |
| **3. Siêu Nhiên, Huyền Huyễn & Xuyên Không (`Supernatural / Fantasy`)** | Tu tiên (`Xianxia`), Huyền huyễn, Dị năng đô thị, Xuyên không, Trùng sinh, Linh dị ([`fantasy.md`](file:///d:/Project/Sven/engine/genres/fantasy.md)) | • **Khế ước Hệ thống Sức mạnh / Thời Không (`Trigger – Ceiling – Cost`)**: Rõ nguồn gốc dị năng/tu vi/trùng sinh và phản phệ cơ thể.<br>• **Tiến hóa Linh Vật Tier-1 (`State 0 Phong ấn ➔ State 1 Thức tỉnh ➔ State 2 Bùng nổ/Vỡ vụn`)**.<br>• **Kết nối `TH3` (`Xuyên Không / Biến đổi không gian giữ nguyên đà nhân vật`)** + Giao chiến tốc độ cao (`2.3x–10x` trên `Seedance`) qua [`@CombatDirector`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md). | **CẤM** làm loãng phim siêu nhiên/tu tiên bằng thủ tục hành chính đời thường tẻ nhạt, và **CẤM** đem yếu tố siêu nhiên/huyền ảo cài lậu vào kịch bản `Regime 1 (Drama Thực Tế)`. |
| **4. Hành Động Võ Thuật & Trinh Thám Hình Sự (`Action & Crime Thriller`)** | Võ thuật, Kiếm hiệp, Điệp viên, Trinh thám phá án, Đấu trí mật thất ([`action.md`](file:///d:/Project/Sven/engine/genres/action.md), [`thriller.md`](file:///d:/Project/Sven/engine/genres/thriller.md)) | • **Action (`action.md`)**: Cấu trúc `3-Zone (40% Nén tâm lý 1.0x ➔ 40% Truy đuổi/Thực chiến 2.3x Seedance ➔ 20% Hệ quả)`; `Adaptive Triad` (`Địa hình ↔ Kỹ năng nhân vật ↔ Cọc cược`).<br>• **Thriller (`thriller.md`)**: Bất đối xứng thông tin (`Suspense ↔ Mystery`), cài cắm **$\ge 2$ manh mối thị giác công bằng (`Fair-Play Visual Clues`)**, đấu trí sắc lạnh + truy đuổi sinh tử. | **CẤM** đánh đấm vô nghĩa không có nén tâm lý, **CẤM** phá án nhờ ăn may/trùng hợp ngẫu nhiên mà không có manh mối cài cắm từ trước. |

*(Lưu ý riêng cho **Sitcom / Hài Tình Huống [`sitcom.md`](file:///d:/Project/Sven/engine/genres/sitcom.md)**: Vận hành bằng `Tình huống trớ trêu + Nói dối dây chuyền (Snowball Lie) + Va chạm 3 tuyến + Reset trạng thái cuối tập`, tuyệt đối không bi kịch hóa nặng nề).*

### 2.5 Scene Duration, Dynamic Storyboard Pacing & Agent Routing Policy (`Mặc Định 10.0s @Director` vs. `Cảnh 15.0s Chuyển Qua @CombatDirector`)
1. **Default `10.0s` Standard Scenes (`@Director` · Dynamic `1–4 Shots` by Dramatic Intent) vs. Exclusive `15.0s` Action/Combat Scenes (`@CombatDirector` · Dynamic `3–6 Shots`)**:
   - **All Standard Dialogue, Emotional Drama, Confrontation & Twist Scenes (`10.0s` Default — Routed to `@Director`)**: Every normal scene (conversation, emotional confession, psychological confrontation, truth-bomb reveal, role reversal) defaults strictly to **`10.0s`** (`00:00–00:10`), tagged **`[🎭 MODEL TIÊU CHUẨN / LIP-SYNC · 10.0s]`**, and compiled by **`@Director`** using the **Unified Storyboard Format** (`Style:` ➔ `[context]: <<<Image X>>> (...)` ➔ `[subject]: <<<Image Y>>> (...)` ➔ `[prop]: <<<Image Z>>> (...)` [when Tier-1 prop/weapon is present] ➔ `[sound]:` ➔ `Shot 1..N` with 1–2 short natural sentences/shot and `12–22 words` dialogue total). **Never hard-lock every `10.0s` scene to `3s–2s–3s–2s`** — select the shot count and rhythm organically from the scene's dramatic intent:
     * *`1 Continuous Shot (10s)` or `2 Slow Shots (6s–4s / 5s–5s)`*: For deep emotional intimacy, grief, confession, or 3–4 simultaneous characters in a group frame.
     * *`3 Escalating / Shock Shots (4s–3.5s–2.5s or 2s–5s–3s)`*: For interpersonal `Action ➔ Reaction ➔ Turn` or a `2s` sudden physical disruption followed by a `5s` tracking/absorption shot and `3s` resolve.
     * *`4 Tactical/Clue Shots (3s–2s–3s–2s)`*: Specifically when the scene hinges on a `2s` macro prop/lock/clue insert (`Shot 2`) + Off-Screen `L-Cut` dialogue + `Shot 3` realization + `Shot 4` calm `2–6w` checkmate.
   - **High-Motion Action, Chase, Physical Struggle, Ambush & Supernatural Combat Scenes (`15.0s` Exclusive — Routed to `@CombatDirector` `[⚡ SEEDANCE · 15.0s]`)**:
     * **All `15.0s` scenes (`00:00–00:15`) — as well as any `10.0s` high-motion action/chase/combat scene — are tagged `[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s]` and routed exclusively to Agent `@CombatDirector` ([`combat-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md))!**
     * **In `Regime 2 (Sci-Fi)`, `Regime 3 (Supernatural/Fantasy)`, and `Regime 4 (Action/Crime Thriller)`**: Every episode weaves high-stakes physical kinetic sequences (tactical pursuit, alley chase, rune/array trap ambush, martial combat, or supernatural clash) sized at **`15.0s` (`3–6 Shots`, e.g., `3s–3s–4s–3s–2s` or `3s–3s–2s–2s–3s–2s`)** and compiled by **`@CombatDirector`** using **1–2 short natural sentences per shot (`15–30w`)** along the **Kinetic Contrast Curve** (`Calm/Setup ➔ Snap Freeze ➔ 3–4s Long Tracking Follow Shot [0 dialogue] ➔ Hard Stop + VFX/Trap on Fixed Frame [0 dialogue] ➔ Rear-Angle Spin into Boss Ambush + 2–5w Checkmate Line`).
     * **In `Regime 1 (Grounded Realistic Drama)`**: **STRICTLY DO NOT force artificial spy break-ins, parkour chases, or martial arts fights!** Every standard scene in `Regime 1` stays at **`10.0s` (`@Director`)**; only route a scene to **`15.0s` (`@CombatDirector` `[⚡ SEEDANCE · 15.0s]`)** when the plot naturally calls for an intense physical commotion (e.g., security guards forcibly escorting someone out, a physical struggle over a document/suitcase, or rushing through a rainstorm to stop a departing car).
   - **30.0s (`00:00–00:30`) Clips**: Activated ONLY on explicit user request (`8–10 Shots` across three mini-acts per `0b` §9). No arbitrary durations (no 12s, no 20s) are permitted.
2. **The Third-Party AI Render Engine Law (Zero Cumulative Timestamps — Gate 3M)**:
   - Generative video models (Sora, Runway, Kling, Veo, Wan, Hailuo, Seedance) render each scene as a standalone clip from second zero.
   - Every Code Block 1 storyboard **MUST start at `00:00`** (`Shot 1 (00:00-00:XX)`) and run contiguously to `00:10`, `00:15`, or `00:30`. Cumulative episode timestamps (`(00:10-00:20)`) inside prompts are strictly prohibited.
3. **Zero Dead Air & State-Transition Law (Gate 3O)**:
   - Strictly bans static filler phrases (`the frame holds still`, `stands rigid through 00:10`, `blinks quietly in background`). Every shot (`Shot 1..N`) must express **1 clear observable state transition (`State A ➔ State B`)** in 1–2 short natural sentences.

### 2.6 Double-Lock 100% Reference Image Fidelity Protocol (`<<<Image X>>>` + Parenthetical Lock) & Two-Tier Prop Architecture
Every Code Block 1 binds locations, characters, and Tier-1 hero props/weapons using the **Unified Storyboard Header Standard (`Style:`, `[context]:`, `[subject]:`, `[prop]:` [when Tier-1 prop/weapon is present], `[sound]:`)** separated by blank lines:
1. **The Single-Declaration `<<<Image X>>>` & Double-Lock 100% Reference Fidelity Law (`Khóa Kép 100% Ảnh Tham Chiếu`)**:
   - **Keep `<<<Image X>>>` Intact**: Never insert descriptive words *inside* the `<<<...>>>` brackets (which breaks multimodal token parsing). Instead, place the explicit **100% reference lock parenthetical** immediately *after* `<<<Image X>>>` inside `[context]:`, `[subject]:`, and `[prop]:`.
   - **Declare `<<<Image X>>>` ONLY ONCE**: Declare `<<<Image 1>>>`, `<<<Image 2>>>`, `<<<Image 3>>>`, `<<<Image 4>>>` **ONLY ONCE** inside `[context]:`, `[subject]:`, and `[prop]:`. **STRICTLY NEVER repeat `<<<Image X>>>` inside `Shot 1..N` or speaker headers!** Once declared in the headers, `Shot 1..N` refers to characters and props exclusively by their clean proper/canonical names (`Bradley`, `Harold`, `Kael`, `silver dragon-hilted longsword`).
   - **Closing Visual Consistency Lock (In Footer)**: Every Code Block 1 footer includes:
     `Strict visual consistency: maintain 100% identical facial features, beauty, hairstyle, exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.`
2. **`[context]:` (5-Vector Environmental Staging & 100% Location Reference Lock)**:
   - Format: `[Evocative English Location Name] <<<Image 1>>> (100% architectural layout, furniture, and lighting strictly refer to this reference image), [time of day]. [5-Vector Specification: architectural layout & full fixed furniture/prop/textile inventory, key lighting source & direction without Kelvin, shadow behavior, atmospheric medium & mood]`.
   - **Zero Ghost Object Law**: Every fixed architectural element, door lock, table, or key interactive prop touched in `Shot 1..N` MUST be pre-declared in `[context]:`, `[subject]:`, or `[prop]:`.
3. **`[subject]:` (Proper Character Names Only, 100% Appearance/Outfit Lock, Zero-Costume/Zero-Age & Initial $t=0.0\text{s}$ Anchor)**:
   - Format: `[Proper_Name] <<<Image 2>>> (100% facial features, beauty/handsome appearance, hairstyle, body proportions, and exact outfit strictly refer to this reference image): [Initial 3D architectural anchor and posture], [initial hand/prop contact state at 00:00 — or (No objects should appear in the character's hands) when unarmed in action/hunter scenes], [eyeline toward counterpart or landmark] — the only [Proper_Name] in frame.`
   - Always use fixed **Proper Names** (`Bradley`, `Harold`, `Elena`, `Dante`, `Kael`, `Martha`) — never generic labels (`Woman`, `Man`, `the father`).
4. **`[prop]:` & End-to-End Two-Tier Prop / Weapon Consistency Protocol (`Stage 1 ➔ Stage 2 setting.html ➔ Stage 3 Rough Script ➔ Stage 4 [prop]: <<<Image X>>>`)**:
   - **Tier 1 — Signature Hero Props, Weapons & Key Artifacts (`Mandatory 16:9 4-View Isolated Prop Sheet in setting.html` + Dedicated `[prop]: <<<Image X>>>` Header)**:
     * **What Qualifies as Tier 1**: Any signature weapon (sword, dagger, spear, firearm, talisman), family/imperial heirloom (jade seal, brass keyring, pendant), or decisive forensic/legal artifact (transfer contract, ledger) that **(a) recurs across multiple scenes/episodes**, OR **(b) is featured in a `Shot 2` macro close-up reveal**, OR **(c) undergoes a 3-state physical transformation (`State 0 Intact ➔ State 1 Activated/Cracked ➔ State 2 Shattered/Reforged`)**.
     * **Format in Code Block 1 (`[prop]:` Block — Included Whenever a Tier-1 Prop/Weapon Appears in the Scene)**:
       `[Canonical Prop/Weapon Name] <<<Image 4>>> (100% shape, material, engravings, proportions, and visual details strictly refer to this reference image): [Exact 00:00 resting placement OR character hand-grip state (e.g., gripped firmly in Kael's right hand while his left hand remains empty)] — the only [Canonical Prop/Weapon Name] in frame.`
   - **Tier 2 — Everyday Single-Scene Handheld Items (`Zero Image Sheet` | Pure Rich Text)**:
     * Common single-use items (`crystal red wine glass`, `ceramic teacup`, `smartphone`) that do not require cross-scene macro design lock. Integrated directly into `[context]:` and `[subject]:` initial hand/table states without a separate `<<<Image X>>>` sheet or `[prop]:` block.

### 2.7 Zero-Age & Zero-Costume Law, Context-Driven Multi-Outfit System & Minor Protection Protocol
- **Strict Zero-Age, Zero-Costume & Single Vocal-Timbre Tag Law in Video Prompts (`Gates 3A & 3E`)**:
  * **STRICTLY ZERO clothing/garment words (`in a black leather jacket`, `in a dark suit`, `skirt`, `dress`, `coat`) and ZERO numeric ages or age/hair/beard words (`32-year-old`, `young blonde`, `silver-bearded`, `aged weathered hand`) anywhere in the video prompt!** Wardrobe and physical appearance are locked 100% by `<<<Image X>>>`.
  * **Single Vocal-Timbre & Tone Tag (`Cách 1`)**: Express vocal age/maturity and emotional delivery inside **ONE single compact parenthetical (`4–6 words`) immediately after `[Proper_Name]`** (zero trailing `(Voice of a ...)` tags):
    - *Young Female / Male*: `Sophia (clear youthful alto, low steely tone): "..."` · `Bradley (smooth tenor, confident warm tone): "..."`
    - *Mature / Elder Female / Male*: `Martha (warm maternal alto, soft affectionate tone): "..."` · `Harold (deep weathered baritone, calm tone): "..."`
  * **Context- & Episode-Driven Wardrobe Evolution (`Trang Phục Thay Đổi Theo Tập & Bối Cảnh: -home / -work / -date / -outing`), Adult Female Hourglass & High-Fashion Dress Law (`Setting Gate 3C`) & 100% Standalone Prompt Law (`Setting Gate 3D`)**: In `setting.html` (`Section 2 #cast` & `Section 3 #modelsheets`), characters lock 100% Invariant Identity DNA while defining Context-Matched Outfit Variants (`[name]-home.jpg`, `[name]-work.jpg`, `[name]-date.jpg`, `[name]-outing.jpg`). Adult females (`>= 18` years old — `Setting Gate 3C`) are designed in `setting.html` with 8-head high-fashion hourglass proportions and flattering context-matched dresses, and every outfit filename in `Section 2 (#cast)` has its own standalone 16:9 4-Figure Turnaround Prompt in `Section 3 (#modelsheets)` (`Setting Gate 3D`).
- **Minor Protection Protocol (Gate 3F & Setting Gate 3B; Pillar 4 §[10d])**: Under-18 characters carry their true integer age and developmental band (`Band I: 0–3`, `Band II: 4–12`, `Band III: 13–17`), are registered in `project_rules.json` → `"minor_characters"`, use Minor-Safe Model Sheet `Mẫu 0B` (intact heads, neutral studio lighting, zero glamour/beauty/body lexicon), and are strictly protected from any sexualization, violence, abuse, chases, or physical danger.

### 2.8 3D Spatial Anchoring, Selective Face Obscuration & Empty-Hand Lock
- **Observable Architectural Anchoring (Gate 3H)**: Anchor characters to 3D physical landmarks (`Seated at the head chair in front of the marble fireplace`). Frame-edge labels (`frame-left`, `screen-right`) inside `[subject]:` and raw Cartesian coordinates (`X: +0.8m`) anywhere in a deliverable are strictly prohibited.
- **Selective Face Obscuration (Anti-Face-Blending & Mystery Booster)**: Actively use partial-face and silhouette shots (`The camera avoids [Name]'s full face, showing only [Name]'s lower face, jawline, firm mouth, and index finger...` or `showing only his back and shoulders in silhouette`) to heighten dramatic intrigue and prevent multi-character face-blending.
- **Empty-Hand Anti-Glitch Lock**: Whenever an unarmed character or hunter stands or moves empty-handed in a tense/action shot, include `(No objects should appear in the character's hands)` so the AI never hallucinates random objects.

### 2.9 Narrative Depth, Anti-Shallow Script Mandate & The 5 Psychological Subversion Laws
To permanently eradicate shallow, predictable, or flat scripts (`"lỗi kịch bản nông, thiếu chiều sâu"`), every concept (`Stage 0`), blueprint (`Stage 1`), world bible (`Stage 2`), and screenplay (`Stage 3`) MUST enforce the **6 Root-Cause Depth Laws (`0-creative-doctrine.md` §1.2)** PLUS the **5 Psychological Subversion & Storytelling Laws (`100% Phương Án Mới`)**:
1. **The 3-Layer Stakes & Zero-Triviality Law**: Lock **External Stakes** (concrete goal + ticking clock), **Internal Psychological Stakes** (`Wound ➔ Lie` under threat), and **Philosophical/Moral Stakes** (two competing human truths).
2. **Law 1 of Subversion — The Mask & Role-Reversal Curve (`Mặt Nạ Ngụy Trang ➔ Vết Nứt ➔ Đảo Chiều Vai Trò`)**:
   - Ban flat, one-note scenes where characters state their true motives from second zero. Every scene must follow a 3-beat psychological curve: **Beat 1 (`0–3s`): False Calm / Social Mask / Disguise** (*intimate lean, polite toast, desperate plea for help*) ➔ **Beat 2 (`3–6s`): The Crack / Micro-Trigger** (*expression freezes abruptly, brass keyring blocks the signature line, door locks from the inside*) ➔ **Beat 3 (`6–10s / 10–15s`): Role Reversal / Double Twist** (*the hunter becomes the hunted; the polite son is checkmated by his father*).
3. **Law 2 of Subversion — Micro-Visual Reveal Over Verbal Exposition (`1 Cận Cảnh Chi Tiết Nhỏ Lật Bài Thay Cho Thoại Giải Thích`)**:
   - Strictly ban characters explaining their secret scheme, identity, or power in dialogue. Reveal hidden truths exclusively through **1 sharp close-up visual detail in `Shot 2` or `Shot 4`** (*two sharp fangs flashing during an embrace behind someone's back*, *black-painted nails revealed while unwinding white hand wraps*, *faint pale red ancient runes glowing beneath a runner's feet*, *an index finger tapping twice on a tarnished brass keyring blocking a contract*).
4. **Law 3 of Subversion — Calm Understatement Dialogue (`Câu Chốt Sắc Lạnh 2–6 Từ — Quyền Lực Càng Cao Nói Càng Dịu & Ngắn`)**:
   - While panicked or disguised characters plead urgently, the dominant/predator/authority character at the decisive moment ALWAYS speaks the **shortest, calmest, most polite or understated line in the scene (`2–6 words`)** (*`"I'm sorry."`*, *`"Miss, you seem lost."`*, *`"Alright. I'll grant you salvation."`*, *`"Because you secretly sold Warehouse Four."`*).
5. **Law 4 of Subversion — Curiosity Gap & Delayed Threat Reveal (`Giấu Mặt / Giấu Mối Đe Dọa Đến Giây Cuối`)**:
   - Do not show everything at once. When a character freezes in panic (`Shot 2`), withhold what they saw until they flee and get trapped (`Shot 4–5`); or obscure the authority character's full face (`showing only his back and shoulders in silhouette` / `showing only lower face and jawline`) until the checkmate line lands.
6. **Law 5 of Subversion — Strict 1–2 Active Characters per Shot Window & Zero Fatality**:
   - Stage scenes so that at any given shot window (`Shot 1..N`), only **`1–2` characters** interact directly in frame (if a 3rd character is in the scene, stage them sequentially in `Shot 1` before the protagonist moves/flees in `Shot 3` and confronts the boss in `Shot 5`). Maintain **Zero Fatalities / Zero Gore** system-wide.

### 2.10 Single-HTML Resource Law (`setting.html` Only) & 100% Interactive Step-by-Step Visual Execution
1. **Single-HTML Resource Rule (`Chỉ xuất duy nhất file setting.html — Bỏ toàn bộ file tap-1.html ... tap-N.html`)**:
   - The system generates **ONLY ONE HTML file per project: `output/<slug>/setting.html`** at Stage 2 so the user can prepare all pre-production visual resources (Character 16:9 Model Sheets, Tier-1 Hero Prop Sheets, and Location 2×2 Grids).
   - **Strictly DO NOT generate `tap-1.html`, `tap-2.html`, or `tap-N.html` files, and DO NOT use batch episode compilation (`mode-batch`).**
   - Every stage before and after `setting.html` works **100% interactively in chat with the user, step-by-step**:
     * **Step 1 (`Stage 1 — Kịch bản chính`)**: Align on the Master Storyline, 12-Row Story Spine, Cast Topology, and Episode-by-Episode Arc (`✋ CP1`).
     * **Step 2 (`Stage 2 — File tài nguyên setting.html`)**: Deliver `output/<slug>/setting.html` (`🛡️ Gate 1.5 ➔ ✋ CP2`) so the user generates Character, Prop, and Location reference images.
     * **Step 3 (`Stage 3 — Kịch bản thô từng tập & đi sâu từng cảnh`)**: Work **one episode at a time** in chat (`Tập 1`, then `Tập 2`...). Present the complete **Episode Rough Script & Deep Per-Scene Breakdown (`Scene 01 ➔ Scene M`)** directly in chat, cross-checking every scene's plot beat, dialogue, Continuity Reference Case (`TH1 / TH2 / TH3`), and Model routing (`Standard 10s @Director` vs. `Seedance 15s @CombatDirector`) with the user (`✋ CP3`).
     * **Step 4 (`Stage 4 — Làm từng cảnh 1 & Đối chiếu trực quan với User`)**: Work **strictly ONE SCENE AT A TIME (`Scene 01` $\to$ `Scene 02` $\to$ ...)** in chat.
       - **For `🔵 TH2` Scenes (Scene 01 or switching to a New Location / Time Jump / Character Lineup)**: The Agent **reads all 5-Vector location, character, and Tier-1 prop specifications directly from `output/<slug>/setting.html` and the Stage 3 Rough Script** to write the prompt immediately — **NEVER ask the user to upload location/character reference images in chat for `TH2`!**
       - **For `🟢 TH1` (Same-Location Continuation) & `🟣 TH3` Scenes**: The user **ONLY sends the extracted Static Terminal Frame (`Last Frame @00:10.0 / @00:15.0`) of Scene $K-1$** so the Agent cross-checks the exact rendered ending pose, hand-grip, and gaze before writing `Scene K` (or uses `Code Block 2 [HANDOVER STATE]` if the user says `"ok"` without uploading a frame).
2. **The 3-Case Continuity Reference Point Law (`Điểm Nối Tham Chiếu Giữa 2 Cảnh`) & Seedance Model Routing**:
   - In every Episode Rough Script (Stage 3) and Scene Prompt Compilation (Stage 4), explicitly identify for the user both the **Continuity Reference Point Status (`TH1 / TH2 / TH3`)** between Scene $K-1$ and Scene $K$ and the **Recommended Render Model (`Standard 10s @Director` vs. `Seedance 15s @CombatDirector`)**:
     * **🟢 Case 1 — Same Time & Same Location (`[ĐIỂM NỐI THAM CHIẾU: CÓ (TH1) — Cùng Thời Điểm & Cùng Bối Cảnh: User gửi Ảnh Tĩnh Cuối Cảnh K-1 để nối chuẩn sang 00:00 Cảnh K]`)**: Scene $K$'s `00:00.0` locks 100% to Scene $K-1$'s terminal frame (`Last Frame @00:10.0 / @00:15.0`), while `[context]:` / `[subject]:` / `[prop]:` reference tags come from `setting.html`.
     * **🔵 Case 2 — Different Location, Different Time, or New Character Lineup (`[ĐIỂM NỐI THAM CHIẾU: KHÔNG NỐI KHUNG HÌNH CŨ (TH2) — Agent tự động lấy thông số Bối cảnh / Nhân vật / Đạo cụ từ file setting.html, User KHÔNG cần gửi ảnh vào chat]`)**: Scene $K$'s spatial frame is terminated; the Agent reads `setting.html` directly to anchor the new location, characters, and props.
     * **🟣 Case 3 — Supernatural, Time-Travel (`Xuyên Không`), Portal, or Reality Shift (`[ĐIỂM NỐI ĐẶC BIỆT (TH3): SIÊU NHIÊN / XUYÊN KHÔNG — User gửi Ảnh Tĩnh Cuối Cảnh K-1 để giữ đà nhân vật, Agent tự lấy Bối cảnh Mới từ setting.html]`)**: Lock character posture, momentum, and held prop from Scene $K-1$'s terminal frame at `00:00.0`, while replacing `[context]:` with the New World/Era Location from `setting.html`.
     * **⚡ High-Motion Model Flag (`Seedance` Routing)**: Any `15.0s` scene (or `10.0s` high-motion action/chase/ambush/combat scene) MUST be marked **`[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s · @CombatDirector]`** and compiled using `@CombatDirector`'s `5–6 Shot` Kinetic Contrast Storyboard architecture.

### 2.11 Summary Matrix: Hard Constraints vs. Craft Defaults vs. Project Rules

| Rule Category | Enforcement | Canonical Scope |
|---|---|---|
| **Hard Constraints** *(Never break; enforced by automated Python gates & Pre-Flight Linter)* | **Blocking Error** (`setting_audit_suite.py` & Pre-Flight Linter) | • **5-Tier Series, Dialogue & 5 Psychological Subversion Laws (`Gate 2B`)**: Tier 1 Series Core + Tier 1 Voice Profiles (`Blind Voice Test`) + *Mask & Role-Reversal Curve*, *Micro-Visual Reveal over Exposition*, *Calm Understatement `2–6w` Closing Line*, *Curiosity Gap*, and *Max 1–2 Active Characters per Shot Window*.<br>• **Clip Duration, Dynamic Storyboard Pacing & Agent Routing (`Gate 3M`)**: **`10.0s` (`1–4 Shots` chosen organically by dramatic intent: `6s–4s`, `5s–5s`, `2s–5s–3s`, `4s–3.5s–2.5s`, `3s–2s–3s–2s`, or `10s` Single-Shot) Default for all standard dialogue/drama scenes (`@Director`)** and **`15.0s` (`3–6 Shots`: `3s–3s–4s–3s–2s` or `3s–3s–2s–2s–3s–2s`) Reserved Exclusively for High-Motion Action/Chase/Ambush/Combat scenes (`@CombatDirector` `[⚡ SEEDANCE · 15.0s]`)**; every clip starts at `00:00`.<br>• **Double-Lock 100% Reference Image Fidelity & Single `<<<Image X>>>` Declaration Law (`Gates 3J, 3K, 3L`)**: Declare `<<<Image X>>>` **ONLY ONCE** inside `[context]:`, `[subject]:`, and `[prop]:`, immediately followed by the explicit `(100% ... strictly refer to this reference image)` lock parenthetical; **strictly NEVER repeat `<<<Image X>>>` inside `Shot 1..N`**; close with the `Strict visual consistency: ...` footer.<br>• **Zero-Costume, Zero-Age & Single Vocal-Timbre Tag Law (`Gates 3A, 3E`)**: Strictly **ZERO clothing/garment words** (`jacket`, `suit`, `skirt`, `dress`) and **ZERO numeric ages or age/hair/beard words** (`32-year-old`, `young`, `blonde`, `silver-bearded`) anywhere in the prompt; encode voice maturity & delivery tone inside **ONE single compact parenthetical (`[Proper_Name] ([vocal timbre/maturity], [tone]): "..."`)**.<br>• **1–2 Short Natural Sentences per Shot (`Gate 3R`)**: `15–30 words` per shot expressing 1 clear state transition `A ➔ B`; strictly zero `→` arrows.<br>• **Minor Protection Protocol (`Gate 3F` & `Setting Gate 3B`)**: Truthful age/band in `setting.html`, zero sexual/body/violence lexicon, `Mẫu 0B` sheets.<br>• **5-Tier Dialogue Economy (`Gates 4, 4B, 4G, 4H`)**: Default `10.0s` clip (`@Director`) = `12–22 words total`; `15.0s` Action/Combat clip (`@CombatDirector`) = `0` spoken words during chase/VFX shots (`Shot 3 & Shot 4`) + `2–5w` boss checkmate line; Code Block 2 handover.<br>• **Zero-Fatality & Positive/Earned Resolution (§2.9)**. |
| **Craft Defaults** *(Use by default; override when dramatic intent requires via `BREAK: <default> — <reason>`)* | **Creative Review & Non-Blocking Warnings (`W1–W11`)** | • **4-Beat Episode Allocation (§8.1)**: `Open/Hook 15–20% (in Scenes 1–2) ➔ Develop 40–50% ➔ Climax 20–25% ➔ Close 10%` across `12–18 scenes` (~3 min/ep; default `10.0s` `@Director`, with `15.0s` routed to `@CombatDirector` for Action/Combat).<br>• **Selective Face Obscuration & Off-Screen `L-Cut` Dialogue**: Use partial-face/silhouette shots (`avoids full face, showing only jawline and hand...`) and off-screen `L-Cut` lines over `2s` prop inserts.<br>• **Inter-Scene Causality**: Every pair of scenes connects via `"Therefore (Vì vậy)"` or `"But (Nhưng)"` — never `"And then (Và rồi)"`. |
| **Project Rules** *(Film-specific rules)* | **Conditional Gates (`Gates 4D, 4E, 4F`)** | Stored exclusively in `output/<slug>/project_rules.json` (`episode_scenes`, `kinship_ladder`, `meal_terms`, `bookish_terms`, `minor_characters`). Never hard-code one film's rules into core engine files. |

---

## §3 — STARTUP PROTOCOL (`K0–K3`)

### K0 — Project State Detection (Resume Protocol)
Before taking any action, scan `output/<slug>/` if the user references an existing project:

| Detected Workspace State | Resume Point |
|---|---|
| No project folder | Run `K1 ➔ K2 ➔ K3`, then start at **Stage 0** (5 concepts) or **Stage 1** (Master Storyline & Blueprint if user provided a concrete premise) |
| Stage 1 Blueprint approved in chat, no `setting.html` | **Stage 2** (`output/<slug>/setting.html` — The Sole Pre-Production Resource HTML File) |
| `setting.html` present, ready for Episode N | **Stage 3** (Interactive Episode N Rough Script & Deep Per-Scene Breakdown in chat) |
| Episode N Rough Script approved in chat (`CP3`) | **Stage 4** (Interactive Scene-by-Scene Prompt Production & Visual Cross-Check in chat: `Scene 01 ➔ Scene 02...`) |
| All Episode Scenes completed in chat (`CP4`) | **Stage 5** (Interactive Distribution & SEO Packaging + Registry Finalize) |
| Revision requested on a specific scene or resource | **Revision Mode** (Cross-check & update the targeted scene prompt in chat or `setting.html`) |

Report the detected state in one concise line and proceed. Never overwrite approved deliverables unless requested.

### K1 — History Registry Scan (14-Axis Anti-Repetition)
Read `history-registry.json` and ensure zero collision across all 14 axes:
1–2. Character Names (`EN` / `VN`) | 3. Narrative Polarity | 4. Story Tracks (`A–H`) | 5. Symbolic Prop Groups | 6. Hook Archetypes (`#1–#12`) | 7. Visual Styles | 8. Genres & Arenas | 9. Escalation Variants | 10. Twist Archetypes (`TW-01..20`) | 11. Cliffhanger Archetypes (`C1–C7`) | 12. Stacked Tropes | 13. Diurnal Lighting | 14. Narrative Mode.

### K2 — Request Classification & Genre Routing
| User Input Signal | Routing Action |
|---|---|
| Broad topic or missing $\ge 2$ of `{character, arena, core conflict, genre}` | **Stage 0**: Pitch 5 distinct high-depth concepts (`✋ CP0`). |
| Concrete story premise provided | Skip Stage 0 ➔ Start directly at **Stage 1: Story Spine & Master Narrative Blueprint (`✋ CP1`)**. |
| Social / Family / Healing Drama (`"drama"`, `"chữa lành"`, `"gia đình"`) | Mount [`engine/genres/drama.md`](file:///d:/Project/Sven/engine/genres/drama.md) (`Two Honest Sides`, `Internal Metamorphosis`, `Earned Ending`). |
| Viral Microdrama (`"microdrama"`, `"phim tổng tài"`, `"phim ngắn kịch tính"`) | Mount [`engine/genres/microdrama.md`](file:///d:/Project/Sven/engine/genres/microdrama.md) (`13-Beat Retention Curve`, `Status Proxies`, `Staccato ≤12w`). |
| Action / Martial Arts / Chase / Xianxia (`"hành động"`, `"võ thuật"`, `"kiếm hiệp"`) | Mount [`engine/genres/action.md`](file:///d:/Project/Sven/engine/genres/action.md) + [`@CombatDirector`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md) (`3-Zone 40/40/20`, `2.3x–10x`, `→` syntax). |
| Sitcom / Comedy (`"sitcom"`, `"hài tình huống"`, `"học đường vui nhộn"`) | Mount [`engine/genres/sitcom.md`](file:///d:/Project/Sven/engine/genres/sitcom.md) (`Amplified Stakes`, `Snowball Lie`, `Status Quo Reset`, `Scene Buttons`). |
| Lyrics or Music Video request | Mount Pillar 3 Music Video Architecture. |
| Buddha Protagonist or Statue Veneration trigger | Activate Special Spiritual Modes (§5.3). |

### K3 — Parameter Lock & Interactive Step-by-Step Handshake
Lock project parameters (`Aspect Ratio`, `Visual Style`, `Episode Count`, `Clip Duration`, `Dialect`) via `engine/runbooks.json` (`output/<slug>/project_rules.json`) and enforce the **Single-HTML (`setting.html` Only) + 100% Interactive Step-by-Step Execution Mode**:
- **Sole HTML Resource File**: Generate **only `output/<slug>/setting.html`** in Stage 2 so the user can prepare Character, Prop, and Location reference images. Never generate `tap-1.html ... tap-N.html`.
- **Interactive Episode-by-Episode & Scene-by-Scene Co-Pilot (`mode-copilot` — Mandatory Standard)**: Execute Stage 3 (Episode Rough Script & Per-Scene Breakdown) one episode at a time in chat, and execute Stage 4 (Directing & Video Prompts) **strictly one scene at a time (`Scene 01 ➔ Scene 02...`) in chat**, cross-checking every scene against the Stage 3 Rough Script and the user's supplied reference images/frames (`TH1 / TH2 / TH3`) before outputting the prompt.

---

## §4 — MASTER 6-STAGE INTERACTIVE PRODUCTION PIPELINE

```text
[USER INPUT] ──▶ K0 Resume Scan ──▶ K1 14-Axis Registry ──▶ K2 Genre Routing ──▶ K3 Parameter Lock
   │
   ▼
STAGE 0  5 High-Concept Pitches (Interactive in Chat)                                   ──▶ ✋ CP0
   │     • 3-Layer Stakes, Core Wound/Lie, Option C Twist
   ▼
STAGE 1  Master Storyline & Blueprint ("Kịch bản chính" — Interactive in Chat)          ──▶ ✋ CP1
   │     • 12-Row Story Spine & Prediction Ledger
   │     • Dynamic Cast Sizing & 6-Layer Psychology
   │     • Short 6-Beat OR Series 4-Act (A/B/C-Plot + Action/Chase 10s/15s Slots)
   ▼
STAGE 2  Pre-Production Resource Bible (output/<slug>/setting.html — DUY NHẤT 1 FILE HTML)──▶ ✋ CP2
   │     • Prepares all visual asset prompts: 16:9 Character Model Sheets (Mẫu 1A/1B/2/2B/3),
   │       Tier-1 Hero Prop Sheets, and 2×2 Location Grids
   │     • Passes setting_audit_suite.py (Gate 1.5)
   │     • User renders & shares Character / Prop / Location images for visual alignment
   ▼
STAGE 3  Episode N Rough Script & Deep Per-Scene Breakdown (Interactive in Chat, 1 Ep)  ──▶ ✋ CP3
   │     • 2–3 Smart Location Sequences & 3-Wall Escalation
   │     • 📌 Per-Scene User Reference Guide: TH1 (Last Frame) | TH2 (New Asset) | TH3 (Spatial Shift)
   │     • Model Routing: [🎭 Standard 10.0s] vs. [⚡ Seedance 10.0s / 15.0s Action/Chase]
   │     • Scene Intent Cards, Verbatim Dialogue & Clean Terminal Keyframe Landing
   │     • Cross-checked & approved with User in chat before writing any video prompt
   ▼
STAGE 4  Interactive Scene-by-Scene Prompt Production & Cross-Check (In Chat, 1 Scene)  ──▶ ✋ CP4
   │     • Strictly ONE SCENE AT A TIME (Scene 01 ➔ Scene 02 ➔ ... ➔ Scene M) — ZERO tap-X.html
   │     • Step 4.1: Cross-check User's Reference Image (TH1 Last Frame / TH2 New Ref / TH3 Split)
   │       + Cross-check against Stage 3 Rough Script (Dialogue, Prop State Case A/B, Landmarks)
   │     • Step 4.2: Run 14-Gate Pre-Flight Self-Audit (Zero Ghost Objects, Gate 3Q/3R/3S, Clean Landing)
   │     • Step 4.3: Deliver Scene K (Code Block 1 + Code Block 2) in chat & request Scene K+1 ref
   │     • [Loop Stage 3 ➔ Stage 4 interactively for Episode N+1..M]
   ▼
STAGE 5  Distribution & SEO Packaging (Interactive in Chat + Finalize Registry)         ──▶ ✋ CP5
```
   ▼
[🎬 PRODUCTION COMPLETE]
```

> **Checkpoint Rule**: At every `✋ CP0–CP5`, **STOP and wait for user approval**. Accepted commands: `ok` / `continue` (approve and advance), `edit [instructions]` (revise current stage), or stage-specific shortcuts.

---

## §5 — STAGE 0: CONCEPT GENERATION (`✋ CP0`)

> **JIT Load**: `.agents/SCREENWRITER.md` + `0-creative-doctrine.md` (§1.2, §8.1, §9.2).

### 5.1 Anti-Shallow Concept Rules, Market Alignment, Vocation Creativity & Full Multi-Polar Cast
- Generate **5 distinct concepts** differing across arena, conflict architecture, hook archetype (`#1–#12`), and emotional trajectory.
- **Real-World Grounded Plausibility & Financial/Legal Realism (`Liên Hệ Thực Tế — Cấm Con Số Ảo Tưởng & Cấm Sci-Fi Hóa Drama Gia Đình`)**:
  * **Grounded Business Models & Believable Valuation Scale**: In billionaire, corporate, and inheritance dramas, anchor family enterprises to **tangible, real-world industries** (e.g., 5-star hotel & resort chains, commercial real-estate holdings, private hospital networks, national logistics/shipping lines, retail/food empires, private investment firms) with **realistic, relatable financial figures** (e.g., `$150M–$1.2B` total enterprise valuation, `$15M–$80M` liquid trust accounts, `$10M–$25M` family estates, `$5M–$20M` debt/tax/bailout deadlines)—strictly banning absurd, inflated `$50B–$100B` fantasy numbers or sci-fi gadgets (`neuro-watches`, `AI brain protocols`) inside family dramas.
  * **Relatable Real-Life Family & Legal Friction**: Ground conflicts in real human relationships and actual US probate/corporate law: contested wills (*Undue Influence*), prenuptial & morality clauses, nursing-home/hospital neglect vs. bedside devotion, embezzlement of company/pension funds, tax fraud audits, and real family betrayals between parents, siblings, and in-laws.
- **Zero Real-World Celebrity / Public Figure Name Ban**: Strictly NEVER use names of real-world singers, actors, celebrities, politicians, or famous billionaires (e.g., no `Lâm Chấn Khang`, no `Rockefeller`, `Walton`, `Musk`, `Bezos`, etc.) in any language.
- **Anti-Artisan Cliché & Arena-True High-Caliber Vocations**: Strictly NEVER default characters to repetitive manual/artisan/handicraft/blue-collar trades (*nghệ nhân chế tác, thợ mộc, thợ thủ công, ủ rượu, sửa ống nước, cơ khí*) unless explicitly requested by the user. Vocations must be creative, high-stakes, and calibrated to the story's arena (e.g., for Billionaire / Inheritance Drama: *Wall Street Short-Seller, Corporate Crisis Fixer, Offshore Trust Attorney, Biotech Chief Medical Officer, Defense Systems Heiress, Private Equity Raider, Forensic Art Authenticator*).
- **Deep Multi-Polar Character Web in Stage 0 (Never Sketchy 3-Line Summaries)**: Scale the character ecosystem in each concept to the format quota (`3–4` Short Film, `5–6` Mini-Series, **`7–9` Full Series [6–10+ Episodes]**). Present the cast in a **clean, scannable Markdown Table** mapping `A1`, `A2` (`Where A2 Is Right`), and all **`Tier B` Dual-Tether Satellites (`A1 ⇄ B ⇄ A2`: `B-Heart`, `B-Judas`, `B-Guardian`, `B-Blackmailed Accomplice`, `B-Shadow Keymaker`, `B-Arbiter`)** + **`Tier C` Chorus**, including explicit family/relational bindings (`Father/Mother–Child`, `Husband–Wife`, `Siblings`).
- **Clean, Spacious & Readable Presentation**: Present concepts with generous whitespace, structured tables, short scannable lines, and clear visual hierarchy—never dump dense, cramped walls of text.
- **Zero Shallow Fables / Zero Triviality**: Every concept must establish **3-Layer Stakes** (External deadline/loss + Internal Wound/Lie + Moral dilemma), an active protagonist whose flawed choice or costly stand drives the plot, an opponent with a real point of truth (`Where A2 Is Right`), and a planted **Option C Reversal**.
- Resolution must calibrate strictly to the genre (§2.9) while respecting the Zero-Fatality Guardrail.

### 5.2 Stage 0 Output Template (User-Facing, Vietnamese — Clean & Spacious Layout)
```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Ý TƯỞNG #[N] — [Tên Dự Án]   `[Genre | Format | Aspect Ratio]`
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎭 1. LOGLINE & CỌC CƯỢC 3 TẦNG (3-LAYER STAKES):
   • Bề nổi (External + Ticking Clock): [Mục tiêu sống còn & thời hạn đếm ngược]
   • Nội tâm (Wound ➔ Lie): [Vết thương quá khứ & vỏ bọc ngụy tạo của A1]
   • Tư tưởng (Thematic Question): [Câu hỏi đạo đức 2 chiều sắc bén]

🧲 2. HOOK 3 GIÂY (#[N] — [Tên Kỹ Thuật Hook]):
   • Nghịch lý thị giác (0–3s) ➔ Câu hỏi bỏ ngỏ ➔ Cầu nối vào bối cảnh

🎲 3. BẺ GÃY DỰ ĐOÁN (OPTION C REVERSAL) & CHUỖI TWIST 10 TẬP:
   • Khán giả đoán [Phương án A hoặc B] ➔ Sự thật xảy ra là [Phương án C cài cắm từ đầu]
   • Lực cản 3 tầng & Twist: T1 [TW-xx] ➔ T2 Midpoint [TW-xx] ➔ T3 Climax [TW-xx]

🏛️ 4. HỆ SINH THÁI NHÂN VẬT ĐA CỰC (MULTI-POLAR CAST MATRIX — ĐẦY ĐỦ THEO QUOTA DỰ ÁN):
   | Vai trò / Tuyến | Nhân vật & Nghề nghiệp (Sáng tạo, xứng tầm Arena) | Quan hệ ràng buộc & Móc xích kép (A1 ⇄ B ⇄ A2) | Động cơ / Vũ khí kịch tính & Twist nắm giữ |
   |---|---|---|---|
   | **A1 (Chính diện)** | [Tên — Nghề nghiệp] | [Quan hệ gia tộc/hôn nhân với A2 & Tuyến B] | [Wound ➔ Lie + Đòn phản công chủ động] |
   | **A2 (Đối đầu)** | [Tên — Nghề nghiệp] | [Quan hệ gia tộc với A1] | [Mục tiêu + "Điểm A2 hoàn toàn có lý" (Where A2 Is Right)] |
   | **B1 (B-Heart / Moral Anchor)** | [Tên — Nghề nghiệp] | [Móc xích kép A1 ⇄ B1 ⇄ A2] | [Lương tri / Điểm yếu cảm xúc] |
   | **B2 (B-Judas / Kẻ phản bội vùng xám)** | [Tên — Nghề nghiệp] | [Móc xích kép A1 ⇄ B2 ⇄ A2] | [Nỗi sợ / Lợi ích khiến B2 đâm sau lưng ở Midpoint] |
   | **B3 (B-Guardian / Lá chắn đồng minh)** | [Tên — Nghề nghiệp] | [Móc xích kép A1 ⇄ B3 ⇄ A2] | [Vũ khí chuyên môn hỗ trợ A1 & bí mật riêng] |
   | **B4 (B-Blackmailed / Con tin bị thao túng)** | [Tên — Nghề nghiệp] | [Móc xích kép A1 ⇄ B4 ⇄ A2] | [Bị A2 nắm thóp ➔ Chìa khóa lật kèo Hồi 3] |
   | **B5 (B-Shadow / Người giữ chìa khóa)** | [Tên — Nghề nghiệp] | [Móc xích kép A1 ⇄ B5 ⇄ A2] | [Nắm giữ di chúc gốc / chứng cứ Option C] |
   | **B6 (B-Arbiter / Trọng tài thực thi)** | [Tên — Nghề nghiệp] | [Trục quyền lực độc lập] | [Cán cân pháp lý / Hội đồng quản trị / SEC / Tòa án] |
   | **Tuyến C (Chorus linh động)** | [Đám đông / Cổ đông / Truyền thông / Nhân viên] | [Áp lực xã hội bao quanh gia tộc] | [Đổi chiều từ vùi dập sang sụp đổ định kiến] |

📦 5. ĐẠO CỤ TRUNG TÂM (WOUND ➔ ECHO PROP) & KẾT CỤC ĐẮT GIÁ:
   • Đạo cụ Tier 1: [Tên đạo cụ] ([Trạng thái Hồi 1] ➔ [Biến đổi 180° ở Kết cục])
   • Cái giá phải trả & Câu hỏi tranh luận: [...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.3 Special Narrative Modes
- **🪷 Buddha as Protagonist**: Triggered by explicit request (`"Đức Phật làm nhân vật chính"`). Keeps Buddha as Awakener/Guide across 3 canonical arcs: (1) *Transformation of Destruction (Angulimala)*, (2) *Healing of Grief (Kisa Gotami)*, or (3) *Humbling of Sovereign Pride (Ajatasattu)*.
- **🗿 Buddha Statue Veneration**: Triggered by statue restoration/offering prompts. Applies the 4-Pillar Veneration Framework (Pillar 1 § Statue Veneration Motif Library) where the statue's physical state chain mirrors the protagonist's internal moral restoration.
- **🎵 Music Video (`MV Mode`)**: Maps the 6 narrative beats to song sections (`3% / 12% / 35% / 30% / 12% / 8%` of duration $T$) per Pillar 3.

### 5.4 ✋ CHECKPOINT 0
```text
👉 Gõ số ý tưởng để chọn (mặc định CÓ THOẠI) — ví dụ: "2" (hoặc "2S" nếu muốn bản KHÔNG THOẠI)
   "edit [yêu cầu]" để tinh chỉnh | "ý tưởng mới" để tạo 5 concept khác | hoặc nhập cốt truyện riêng
```

---

## §6 — STAGE 1: TIER 1 SERIES MASTER STORYLINE, VOICE PROFILES & TIER 3 EPISODE TRACKING TABLE (`✋ CP1`)

> **Top-Down 5-Tier Law (`Series ➔ Tập ➔ Liên Kết Tập ➔ Cảnh ➔ Liên Kết Cảnh`)**: **ALWAYS lock Tier 1 (Series Storyline + Character Voice Profiles) and Tier 3 (Inter-Episode Tracking Table) at Stage 1 (`§6 → CP1`) BEFORE generating `setting.html` (`§7 → CP2`) and BEFORE writing individual episodes (`§8 → CP3`).** Locking the upper tier first ensures individual 10s/15s scenes never drift from the master story.

### 6.1 Tier 1 — Series Master Storyline (`Cốt Truyện Cả Bộ — Viết 1 Lần, Hiếm Khi Đổi`)
Lock the **8 Mandatory Series Foundations**:
1. **Logline**: Who wants what, obstructed by what, and the concrete price if they fail.
2. **Central Question (`Câu hỏi trung tâm`)**: The overarching question the audience wants answered across the entire series.
3. **Protagonist & Dual Goal (`Nhân vật chính và mục tiêu`)**: What they **Want** externally (`cái muốn bên ngoài`) vs. what they **Need** internally (`cái cần bên trong`), in direct conflict.
4. **Antagonist / Opposing Force (`Phản diện hoặc lực cản`)**: Has their own independent goal and logic (`Where A2 Is Right`), not merely existing to block the protagonist.
5. **The Master Secret (`Bí mật lớn`)**: What is hidden and **when it is revealed (typically at ~2/3 of the series — strictly never spoiled in Episode 1)**. Each episode only peels back one small layer.
6. **Transformation Arc (`Đường biến đổi A ➔ B`)**: How the protagonist transforms from State A (beginning of series) to State B (end of series).
7. **Episode Count & Act Division (`Số tập và cung chia`)**: E.g., 10 or 12 episodes divided into 4 Acts (2–3 episodes per Act).
8. **Known Ending (`Kết`)**: Known in advance, even while details remain open.
> **Core Rule**: Every episode must serve either the **Central Question** or the **Transformation Arc**. Any episode that advances neither must be cut.

### 6.1b Tier 1 Dialogue — Series-Wide Character Voice Profiles (`Hồ Sơ Giọng Nói — Lập 1 Lần Cho Cả Bộ`)
Establish a locked **Voice Card** for every character so any line is recognizable even when speaker names are hidden (**The Blind Voice Test**):
- **Sentence Rhythm (`Cách nói`)**: Long or clipped sentences, frequent pauses, counter-questions, or strategic silence.
- **Vocabulary (`Từ vựng`)**: Signature words, kinship pronouns (`bố/ông già`, `em/tôi/tao`), politeness level, regional cadence.
- **Verbal Habit (`Thói quen thoại`)**: Sarcasm, understatement, or changing the subject.
- **What They NEVER Say Straight (`Điều không bao giờ nói thẳng`)**: Every character has one thing they always avoid stating directly (e.g., Harold never says *"Bố xin lỗi"*).
- **Kinship & Address Card (`Thẻ xưng hô`)**: Who calls whom what, and how it changes when the relationship shifts (e.g., shifting from *"bố"* to *"ông"* marks a major rupture).
- **Fixed AI Video Voice Spec (`Thông số giọng cho AI video`)**: Age, vocal timbre, and baseline tone (reused verbatim in every prompt for that character).

### 6.1c Tier 3 — Inter-Episode Links & Master Tracking Table (`Liên Kết Giữa Các Tập & Bảng Theo Dõi`)
Every episode in the series must connect to surrounding episodes using **at least two of the four inter-episode connectors**:
1. **Cliffhanger**: End the episode with an unresolved question or danger (*write the cliffhanger BEFORE writing the next episode, and open the next episode with its direct consequence*).
2. **Setup (`Mồi`) & Payoff (`Trả`)**: Plant a detail in Episode $n$, pay it off in Episode $n+2$ or later. Every setup must have a payoff; every payoff must have a prior setup.
3. **Visible Consequence (`Hậu quả`)**: An action in Episode $n$ causes a concrete, visible consequence in Episode $n+1$.
4. **Recurring Motif (`Motif lặp`)**: An image, sound, prop (like the old brass keyring), or echo line that reappears with a new meaning each time.

| Tập | Mục tiêu tập (Nhỏ hơn mục tiêu cả bộ) | Chuyển biến chính (Đổi ≥1 thứ không quay lại được) | Lớp thông tin mới về Bí mật lớn (Mở 1 lớp) | Mồi cài (Setup) | Trả mồi (Payoff) | Cliffhanger cuối tập |
|---|---|---|---|---|---|---|
| **1** | ... | ... | ... | ... | ... | ... |

### 6.2 High-Precision Input Design: Cast Sizing, Per-Scene Line A/B Cap (`≤ 4`) + Flexible Line C & Story-Bound Locations/Wardrobe
1. **Reference Cast Scales by Format (`2-casting-worldbuilding-specification.md` STEP 0)**:
   - **Short Film (`1 Episode / 6–12 scenes`)**: **`3–4` named characters** (`A1` Protagonist + `A2` Opposing Force + `1–2 Tier B` Satellites) + flexible `Tier C Chorus`.
   - **Mini-Series (`3–5 Episodes / 30–50 scenes`)**: **`5–6` named characters** (`A1` + `A2` + `3–4 Tier B` Satellites across dual tethers) + flexible `Tier C Chorus`.
   - **Full Series (`6–10+ Episodes / 60–100 scenes`)**: **`7–9` named characters** (`A1` + `A2` + `5–7 Tier B` Satellites: `B-Heart`, `B-Judas`, `B-Guardian`, `B-Arbiter`) + flexible `Tier C Chorus`.
   - **Mega Series (`12–20+ Episodes`)**: **`10–14` named characters** organized into rotating faction arcs + flexible `Tier C Chorus`.
2. **Stage 3 Rough Script Per-Scene Character Rule (`Tuyến A & B Tối Đa 4 Người / Cảnh — Tuyến C Linh Động`)**:
   - **Line A (`A1/A2`) + Line B (`Tier B` Satellites)**: Strictly **`1 to maximum 4 named characters per scene` (`tối đa 4 người / cảnh`)**, selected and staged 100% according to the dramatic requirement of that scene's plot beat.
   - **Line C (`Tier C` Chorus / Extras)**: **Completely flexible (`linh động`)** according to the setting and plot context (e.g., `0` in a private bedroom at home; a few coworkers/patrons in an office or date café; a lively crowd during an outing, school assembly, or public confrontation).
3. **Story-Bound Locations & Episode/Context Wardrobe Matrix (`Bối Cảnh & Trang Phục Gắn Chặt Cốt Truyện`)**:
   - **Locations (`Ở nhà / Công việc / Đi chơi / Hẹn hò / Sự kiện...`)**: Every location in the input (`Stage 1 ➔ Stage 2 ➔ Stage 3`) must be deeply designed and directly tied to the plot conflict—never generic filler backdrops.
   - **Wardrobe Progression Across Episodes & Arenas**: Characters change outfits naturally across episodes and social arenas (*at home, at work, casual outing, romantic date, crisis/rain*) while preserving 100% identical facial and bodily identity across their 16:9 Outfit Model Sheets.
4. **Twist-Driven Casting Mandate**: Zero ornamental characters. Every Tier B character holds an explicit plot/twist function (`TW-01..20`), dual relationships (`A1 ⇄ B ⇄ A2`), and an independent moral dilemma.

### 6.3 Format A Blueprint — Standalone Short Film (`65s–135s` Closed Arc · `6–12 Scenes`)
For a 1-episode standalone film, lock:
1. **Elastic Dual-Atom Scene Count & Duration (`10.0s` Standard + `15.0s` Extended Peaks)**: `6–12` scenes (`75s–135s`), combining `10.0s` Standard clips with `1–3` strategic `15.0s` Extended clips at the Climax or Action/Chase peaks (§2.5).
2. **6-Beat / 18-Sub-Beat Architecture (With Strict 15–20% Coda Cap)**:
   - `B1 Hook (1 Sc · 10s)`: `1.1 Cognitive Gap` | `1.2 Frozen Potential` | `1.3 Anchor Bridge`
   - `B2 Setup (1–2 Sc · 10s)`: `2.1 Old Equilibrium` | `2.2 Backstory Wound` | `2.3 Wound Prop Plant`
   - `B3 Drama (2–4 Sc · 10s/15s)`: `3.1 Tactic 1 Backfires` | `3.2 Ideological Clash` | `3.3 Exits Sealed`
   - `B4 Climax (2–3 Sc · 15s)`: `4.1 Wave 1 Trap` | `4.2 Wave 2 Loss` | `4.3 Wave 3 Ego Death / Breakthrough`
   - `B5 Release & B6 Echo (1–2 Sc max · 10s/15s)`: `5.1 Thermal Polarity Shift` | `5.2 Earned Cost` | `6.2 180° Echo Prop` | `6.3 Closing Image Symmetry`
3. **Multi-Sequence Spatial Map**: Partition into `2–3 distinct spatial sequences` so the film breathes across rooms/zones.
4. **Voice-Mode Rhythm Sketch**: Plan the voice-mode progression across scenes (`O.S./Interrupt ➔ Subtext Duel ➔ Contradicting V.O. ➔ Rapid Fencing ➔ Silence ➔ Solo Verdict`).

### 6.4 Format B Blueprint — Multi-Episode Series (`20/80 Structural Law: 6 Genre Act Engines + 5 Act-Specific Episode Archetypes`)
For a multi-episode series ($N$ episodes), **NEVER force every genre or every episode into a uniform structure or uniform `10 scenes × 10s` duration** (`1-narrative-screenplay-architecture.md` Part II §5). Lock:
1. **Select 1 of the 6 Genre-Specific Macro Act & Meso Episode Engines (`80% Genre Architecture`)**:
   - **Engine 1 — Social, Family, Historical & Palace Drama (`Pressure-Cooker 4-Act Engine`)**: Slow-burn cumulative tension across `Act I Ignition ➔ Act IIA False Dawn ➔ Act IIB Midpoint Betrayal ➔ Act IIIA Dark Night ➔ Act IIIB+IV Showdown & Restorative Coda`. Zero early reconciliation in Acts I–II (`75% 10s : 25% 15s`).
   - **Engine 2 — Viral Microdrama, CEO, Rebirth & Revenge (`3-Tier Dopamine & Every-Episode Face-Slap Engine`)**: Viewers never wait 4 episodes for a payoff. `Act I (Ep 1)` ends with a **Mandatory First Mini-Slap**; **every `Act II` episode** executes an internal `Spring Compression (30%) ➔ Baiting (30%) ➔ In-Episode Dopamine Face-Slap (30%) ➔ Higher Boss Arrival (10%)` loop; `Act III+IV Finale` delivers total public unmasking + a crisp 1-scene sovereign walk-away (`90% 10s : 10% 15s`).
   - **Engine 3 — Action, Martial Arts, Wuxia, Xianxia & Survival (`4-Act Gauntlet & Breakthrough Engine`)**: `Act I` Ambush/Heavy Loss ➔ `Act IIA` Gauntlet Trials (`40% Drama : 40% Seedance Combat/Chase : 20% Fallout`) ➔ `Act IIB Midpoint` Broken Weapon (`State 2`) & Martial/Tactical Epiphany ➔ `Act III+IV Finale` (`60–70%` continuous `15.0s Seedance` Apex Boss Showdown + `1–2` scene Coda; `60% 10s : 40% 15s`).
   - **Engine 4 — Detective Mystery, Crime Thriller & Horror (`4-Act Onion-Peel & Checkmate Engine`)**: `Act I` Impossible Crime & $\ge 2$ silent visual clues ➔ `Act IIA` Red Herring alibi collapse ➔ `Act IIB Midpoint` Hunter Becomes Hunted (`Mystery ➔ Suspense` switch) ➔ `Act III+IV Finale` Prestige Flashback Montage + Forensic Checkmate (`75% 10s : 25% 15s`).
   - **Engine 5 — Situation Comedy, Rom-Com & School Comedy (`Episodic 4-Phase Snowball Farce & Reset Engine`)**: Rejects tragic serial acts; every episode is a crisp `6–8 scene (60s–80s)` self-contained loop: `Phase 1 Petty Spark ➔ Phase 2 Cover-Up Lie ➔ Phase 3 Farce Collision ➔ Phase 4 Status Quo Reset & Punchline Button` (`90% 10s : 10% 15s`).
   - **Engine 6 — Healing, Slice-of-Life, Poetic Romance & Spiritual (`4-Movement Kishōtenketsu Engine`)**: Zero cartoon villains; progresses across `Movement I Ki (Quiet Solitude)` ➔ `Movement II Shō (Warm Connection)` ➔ `Movement III Ten (Sudden Rainstorm/Test)` ➔ `Movement IV Ketsu (Wordless Resonance)` (`65% 10s : 35% 15s` with rich Foley & `Model 0 / 3A`).
2. **Assign the 5 Act-Specific Episode Archetypes & Dynamic Scene/Duration Scaling (Anti-Dead-Finale Law)**:
   - **CRITICAL FINALE LAW**: For all series with $N \le 12$, **Act IV (`Resolution / Coda`) NEVER stands alone as a full separate episode** (which causes an 80% post-climax viewer drop-off). Instead, the **Finale Episode fuses `70–75% Act IIIB (The 3-Wave Grand Showdown)` + `25–30% Act IV (Earned Cost, 180° Echo Prop & Bookend Closing Image)`**.

| Total Eps ($N$) | Act I (`Archetype 1: Ignition & Trap` · `6–8 Sc` · `65s–85s`) | Act IIA (`Archetype 2: Counter & False Dawn` · `8–9 Sc` · `85s–100s`) | Act IIB (`Archetype 3: Midpoint Shatter` · `9–11 Sc` · `100s–125s`) | Act IIIA (`Archetype 4: Siege & Dark Night` · `8–10 Sc` · `95s–115s`) | Act IIIB + IV Finale (`Archetype 5: 75% Showdown + 25% Coda` · `10–14 Sc` · `115s–155s`) |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **3** *(Mini)* | **Ep 1** (`6–8 Sc`) | *(Fused into Ep 1/2)* | **Ep 2** (`8–10 Sc` · *Midpoint + Dark Night*) | *(Tail of Ep 2)* | **Ep 3 (Finale)** (`10–12 Sc` · *75% Showdown + 25% Coda*) |
| **4** *(Mini)* | **Ep 1** (`6–8 Sc`) | **Ep 2 (1st Half)** | **Ep 2 (2nd Half)** (`8–10 Sc` · *Midpoint*) | **Ep 3** (`8–10 Sc` · *Dark Night*) | **Ep 4 (Finale)** (`10–13 Sc` · *75% Showdown + 25% Coda*) |
| **5** *(Mini)* | **Ep 1** (`6–8 Sc`) | **Ep 2** (`8–9 Sc`) | **Ep 3** (`9–11 Sc` · *Midpoint*) | **Ep 4** (`8–10 Sc` · *Dark Night*) | **Ep 5 (Finale)** (`10–13 Sc` · *75% Showdown + 25% Coda*) |
| **6** *(Standard)* | **Ep 1** (`6–8 Sc`) | **Ep 2** (`8–9 Sc`) | **Ep 3–4** (`9–11 Sc` · *Midpoint*) | **Ep 5** (`8–10 Sc` · *Dark Night*) | **Ep 6 (Finale)** (`10–14 Sc` · *75% Showdown + 25% Coda*) |
| **8** *(Standard)* | **Ep 1–2** (`6–8 Sc`) | **Ep 3–4** (`8–9 Sc`) | **Ep 5** (`9–11 Sc` · *Midpoint*) | **Ep 6–7** (`8–10 Sc` · *Dark Night*) | **Ep 8 (Finale)** (`11–14 Sc` · *75% Showdown + 25% Coda*) |
| **10** *(Full)* | **Ep 1–2** (`6–8 Sc`) | **Ep 3–4** (`8–9 Sc`) | **Ep 5–6** (`9–11 Sc` · *Midpoint*) | **Ep 7–8** (`8–10 Sc` · *Dark Night*) | **Ep 9** (*Showdown Pt 1*) + **Ep 10** (*70% Showdown + 30% Coda*) |
| **12** *(Full)* | **Ep 1–2** (`6–8 Sc`) | **Ep 3–5** (`8–9 Sc`) | **Ep 6–7** (`9–11 Sc` · *Midpoint*) | **Ep 8–10** (`8–10 Sc` · *Dark Night*) | **Ep 11** (*Showdown Pt 1*) + **Ep 12** (*70% Showdown + 30% Coda*) |
| **16–20** *(Mega)* | **First 15–20%** | **Next 25%** | **Center 25%** (*Midpoint at 50%*) | **Next 20%** | **Final 10–15%** (*Two-Part Showdown & Coda*) |

3. **The Triple-Helix Plot Weave (`A-Plot + B-Plot + C-Plot`)**:
   - **`A-Plot` (`55–65%` | External Spine / `Want`)**: High-stakes clash between `A1` and `A2` under a ticking clock.
   - **`B-Plot` (`25–30%` | Relational Heart / `Need`)**: Intimate bond (`A1 ⇄ B-Heart`) challenging `A1`'s protective Lie.
   - **`C-Plot` (`10–15%` | Subterranean Time-Bomb / `Twist`)**: Covert thread (`B-Judas` betrayal, `B-Guardian` secret investigation, or `Tier C` vise) planting clues in Acts I–II and detonating at the Midpoint / Act III boundary.
   - **5 Mandatory Convergence Nodes**: Lock where `A/B/C-Plot` intersect at (1) *Inciting Incident (~15%)*, (2) *Midpoint Reversal (~50%)*, (3) *All Hope Is Lost / Judas Detonation (~75%)*, (4) *Climax Crucible (~85–90%)*, and (5) *180° Echo Resolution (100%)*.
4. **Episode-by-Episode Escalation, Location, Participating Cast & Cluster Matrix (`Bắt Buộc Làm Rõ Địa Điểm & Nhân Vật Tham Gia Từng Tập`)**:
   - Never present vague 2-line episode summaries where the user cannot grasp where the episode takes place or who participates.
   - For **every single episode (`Ep 1 .. Ep N`)** in Stage 1 (chat), Stage 2 (`setting.html` Section 5 `#roadmap`), and Stage 3, explicitly lock and display **3 Mandatory Per-Episode Blocks**:
     1. **`📍 1. Địa Điểm, Khung Giờ & Đạo Cụ Trong Tập`**: Explicit Vietnamese & English location names, exact location reference files (`loc-home.jpg`, `loc-work-office.jpg`, `loc-work-port.jpg`, `loc-date.jpg`, `loc-outing.jpg`, `loc-work-bank.jpg`), diurnal time (`AM/PM`), and active Tier-1 props (`prop-*.jpg`).
     2. **`👥 2. Các Nhân Vật Tham Gia Trong Tập (Tên + Quan Hệ + Vai Trò Trong Tập + File Trang Phục)`**: Numbered list of every named character appearing in that episode (`A1`, `A2`, `Tier B`), their exact relationship (`Cha`, `Con út`, `Anh cả`, `Vị hôn thê`, `Chị hai`, `Anh rể`, `Chị dâu cả`...), their exact outfit file for that episode (`[name]-home/work/date/outing.jpg`), what they do in that episode, plus `Tier C` background extras.
     3. **`🎬 3. Chia Cụm Cảnh (Sequences) & Quân Số (≤ 4 Người Định Danh / Cảnh)`**: Group the episode's scenes into `2–3` clear location sequences (`Cụm 1: Cảnh 01–04`, `Cụm 2: Cảnh 05–08`...), explicitly naming the `1–4` characters on screen in each cluster, the central conflict (`Xung đột / Bước ngoặt`), and the ending consequence (`Hậu quả / Cliffhanger`).

### 6.5 ✋ CHECKPOINT 1
```text
✋ CHECKPOINT 1 — Story Spine (12 Hàng) & Master Narrative Blueprint hoàn tất
→ "ok" để sang Stage 2 (Khởi tạo setting.html Pre-Production Bible) | "edit [nội dung]" để chỉnh sửa cấu trúc cốt truyện / nhân vật
```

---

## §7 — STAGE 2: PRE-PRODUCTION WORLD BIBLE → `setting.html` PHASE A (`🛡️ Gate 1.5 ➔ ✋ CP2`)

> **JIT Load**: `2-casting-worldbuilding-specification.md`. Copy all model, prop, and location sheet templates directly from Pillar 2.

### 7.1 Visual Style & Format Lock
Lock the production header in `setting.html` and `output/<slug>/project_rules.json`:
- **Visual Style Header**: Selected from the **50 Master Styles** in Pillar 2 Part VI (`25 Live Action + 25 Animation`, featuring **`3D Semi-Realistic Animation (Hoạt Hình 3D Bán Chân Thực — Light Chaser & Blur Studio Style, Mẫu 2B)`**, `Vietnamese Poetic & Tropical Realism`, `Oriental Wuxia & Imperial Period`, `Hyper-Kinetic Tactical Neo-Noir`, `Pixar 3D`, `Theatrical Live Action`, `Makoto Shinkai 2D Anime`, etc.). Propagates verbatim into every 16:9 Character/Prop/Location sheet prompt and every Code Block 1 `Style:` header:
  * **3D Semi-Realistic Animation (`3d-semi-real` — Signature Stylized 3D Realism)**: `3D Semi-Realistic Cinematic Animation, high-end stylized 3D realism in the signature style of Light Chaser Animation and Blur Studio, Unreal Engine 5 and Octane Render, ray-traced global illumination, physically based rendering textures, refined subsurface scattering skin shader with smooth natural satin complexion and expressive luminous eyes, strand-based 3D hair grooming, rich volumetric atmospheric lighting.`
- **Format Parameters**: `Episode Mode` (`Short Film` vs. `Series`), `Aspect Ratio` (§2.3), `Scene Count & Clip Duration` (§2.5), `Genre / Arena / Stacked Tropes (≤ 2)`, and `Spoken Language & Regional Dialect` (§2.2).

### 7.2 Cast Profiles & 16:9 Sovereign Multi-Angle Model Sheets
1. **Deep Character Profiles (Section 2 `#cast`)**:
   - Build full profiles for `A1`, `A2`, all `Tier B` satellites, and `Tier C` chorus per Pillar 2 STEP 1–3.
   - **Mandatory Depth Fields (`Setting Gate 2B`)**: Every principal profile MUST explicitly document:
     * **6-Layer Internal Landscape**: `Core Wound` ➔ `The Lie Believed` ➔ `Surface Want` ➔ `Underlying Need` ➔ `Core Fear` ➔ `Internal Paradox`.
     * **Living Continuum**: `Baseline Presence` (unobserved rhythm) vs. `Dynamic Fluidity` (deflections/reactions under pressure).
     * **Anti-Caricature Polarity**: For `A2`, explicitly state **`Where They Are Right`** (the legitimate grievance or objective truth in their stance) and verify their scheme's real-world logic. For `Tier B`, explicitly state their dual tether (`Relation to A1` + `Relation to A2` + `Twist Role TW-xx`).
2. **Sovereign 16:9 Multi-Angle Model Sheet Prompts (Section 3 `#modelsheets` — Zero-Text Standard)**:
   - Every `A1`, `A2`, and `Tier B` character appearing in $\ge 2$ scenes receives a dedicated 16:9 Model Sheet Prompt + Double-Lock Mode B Video Reference Snippet (`[Proper_Name] <<<Image Y>>> (100% facial features, beauty/handsome appearance, hairstyle, body proportions, and exact outfit strictly refer to this reference image): ...`).
   - **Classification & Layout Invariants (`Setting Gates 3, 3B, 3C` & Pillar 2 Part III)**:
     * **Zero-Text Canvas**: 100% visual imagery; strictly zero text labels, zero typography, zero metadata cards, zero watermarks.
     * **Optical Contrast Inversion Backdrop**: Dark attire $\to$ solid pure white `#FFFFFF` studio backdrop; light attire $\to$ solid dark neutral grey studio backdrop. Zero environmental scenery.
     * **Adult Human (`≥ 18` — 4-Figure 1:1 Horizontal Alignment Spec)**: Declares `4 figures arranged from left to right across two zones`: **Left & Center Zone (55% width)** = 3 compact full-body turnaround figures (`Figure 1` front view with clean mannequin-style neck termination at collar, `Figure 2` 90° lateral profile with clean mannequin-style neck termination, `Figure 3` full-length rear view INCLUDING complete back of head and hairstyle) standing on the exact same floor baseline at **identical 1:1 anatomical body scale with aligned horizontal shoulder lines, waistlines, garment hems, and heels**; **Right Zone (45% width)** = `Figure 4` Dominant High-Definition Chest-Up Direct Frontal Portrait at eye level with safe headroom above the hair crown, locking exact integer age (`aged 34`), 7 physical attributes, skin complexion finish, and persona-calibrated female makeup or male grooming (banning legacy `"thin natural nude lips"` boilerplate).
     * **Human Minor (`< 18` — Minor-Safe `Mẫu 0B`)**: 3 full-length turnaround views WITH HEAD INTACT + right-zone frontal head-and-shoulders portrait; truthful integer age (`aged 14`); neutral studio casting; zero glamour, beauty, makeup, or body-shaping lexicon (`Setting Gate 3B`).
     * **Non-Human Entity (`Mẫu 3`)**: 3 full-body turnaround views WITH COMPLETE HEAD/CRANIUM + right-zone upper-torso-to-head portrait.

### 7.3 Two-Tier Prop & Weapon Universe (Section 4A `#props` — End-to-End Prop Image Generation & Consistency Standard)
- **Tier 1 — Signature Hero Props, Weapons & Key Artifacts (`Mandatory 16:9 4-View Isolated Prop Model Sheet in setting.html`)**:
  1. **Scope**: Any weapon (`silver dragon-hilted longsword`, `tactical dagger`), sacred/family artifact (`imperial white jade seal`, `tarnished brass truck keyring`), or decisive legal/forensic prop (`leather-bound transfer contract`, `black debt ledger`) that recurs across multiple scenes/episodes, OR is featured in a `Shot 2` macro close-up reveal, OR undergoes a physical state transformation.
  2. **100% Isolated Zero-Hand / Zero-Text 16:9 4-View Prop Sheet Law (`prop-[short_noun].jpg`)**:
     - **4 Orthogonal & Macro Views on 1 Widescreen 16:9 Canvas**: `View 1` Full-Length Front View, `View 2` 90° Side Profile View, `View 3` Back / Top View, and `View 4` 45° Macro Close-Up of the signature detail (e.g., dragon guard with ruby eye, carved `'04'` brass tag, red wax seal).
     - **STRICT ZERO HUMAN HANDS / BODY PARTS LAW**: The prop or weapon MUST be rendered **100% isolated on a clean studio background (`#FFFFFF` for dark/metal props; dark neutral charcoal for glowing/white/jade props) with ZERO human hands, fingers, or arms holding it** and **ZERO text/labels**. *(If a reference sheet shows a disembodied hand gripping the sword, feeding `<<<Image 4>>>` into an AI video generator causes extra phantom hands to spawn in the video!)*
     - **Locked Proportions, Material & Mutability Lifecycle**: Explicitly lock exact dimensions (`e.g., 110cm total length, 85cm blade, 25cm hilt`), material finish, and the **3-Stage Mutability Lifecycle (`State 0 Intact` ➔ `State 1 Activated / Glowing / Cracked` ➔ `State 2 Shattered / Renamed Fragment Entity` or `180° Echo Rebirth`)**. If a Tier-1 prop transforms visually mid-series, generate a dedicated sheet per visual state (`prop-seal-intact.jpg`, `prop-seal-cracked.jpg`).
     - **Double-Lock Mode B `[prop]:` Snippet**: `[Canonical Prop/Weapon Name] <<<Image 4>>> (100% shape, material, engravings, proportions, and visual details strictly refer to this reference image): [Exact 00:00 placement or hand-grip state] — the only [Canonical Prop/Weapon Name] in frame.`
- **Tier 2 — Everyday Single-Scene Handheld Items (`Zero Image Sheet` | Pure Rich Text)**:
  - Common single-use items (`crystal red wine glass`, `ceramic teacup`, `smartphone`) described with rich material/tactile English text (`no underscores`, `zero image generation sheets`) inside `[context]:` and `[subject]:`.
- **Furniture & Fixtures Exclusion**: Beds, cribs, tables, chairs, blankets, and doors are strictly excluded from `#props` and cataloged inside `#locations`.

### 7.4 Location Universe & 5-Vector Environmental Staging (Section 4B `#locations`)
- Every primary location features a **5-Vector Environmental Profile** (1. Evocative natural English name + image ref, 2. Diurnal time/weather, 3. Comprehensive fixed architecture, furniture & textile inventory `"what is physically there"`, 4. Lighting source, direction & shadow behavior without Kelvin, 5. Atmospheric medium & emotional climate).
- **16:9 2×2 Architectural Grid Prompt**: 4 spatial angles of the exact same uninhabited room (`Top-Left`: Wide Establishing; `Top-Right`: 180° Reverse Angle; `Bottom-Left`: Overhead Bird's-Eye Layout; `Bottom-Right`: Ground-Level Key Landmark), plus the Mode B `[context]:` snippet.

### 7.5 `setting.html` 10-Section Contract & Phase A Roadmap
Compile `output/<slug>/setting.html` containing all mandatory sections verified by `setting_audit_suite.py`:

| Section Number & ID | Mandatory Content Contract | Phase |
|---|---|---|
| **Section 1 (`id="story"`)** | Master Narrative Arc, 12-Row Story Spine Summary, **3-Layer Stakes**, **Triple-Helix `A/B/C-Plot` Architecture** (or 6-Beat Short Arc), and Genre-Calibrated Zero-Fatality Resolution (`Gate 1C`). | Phase A |
| **Section 1B (`id="diurnal"`)** | 24-Hour Biological & Diurnal Lighting Timeline (`AM/PM` progression, fatigue/meal continuity, sensory color tones). | Phase A ➔ B |
| **Section 1C (`id="causality"`)** | Inter-Episode Causality Matrix (`Ep N` False Dawn / Cold Water $\to$ `Ep N+1` Opening Trigger & Bridge Type). | Phase A ➔ B |
| **Section 1D (`id="dialogue-matrix"`)** | Scene Typology, Voice Mode Distribution & 8-Model Dialogue Suite Calibration. | Phase A ➔ B |
| **Section 2 (`id="cast"`)** | Canonical Cast Cards (`A1`, `A2`, `Tier B`, `Tier C`) with **6-Layer Psychology (`Wound/Lie/Want/Need/Fear/Paradox`)**, **`Where A2 Is Right`**, Living Continuum, and Mode B Snippets (`Gate 2B`). | Phase A |
| **Section 3 (`id="modelsheets"`)** | 16:9 Multi-Angle Character Model Sheet Prompts + Copy Buttons + Mode B Snippets (`Gates 3, 3B, 3C`). | Phase A |
| **Section 4A (`id="props"`)** | Two-Tier Prop Universe (Tier 1 16:9 4-View Sheet Prompts + Lifecycle Table + Mode B Snippets; Tier 2 Text Inventory) (`Gate 4`). | Phase A |
| **Section 4B (`id="locations"`)** | Location Universe (5-Vector Inventories + 16:9 2×2 Grid Prompts + Mode B `[context]:` Snippets) (`Gate 5`). | Phase A |
| **Section 5 (`id="roadmap"`)** | **Phase A**: Episode/Act Master Breakdown ($\ge 6$ items with Conflict, 3-Wall Escalation, and Cliffhanger/Consequence). **Phase B (Stage 3)**: Granular 10s Scene-by-Scene Connective Matrix (`Gates 6, 6B`). | Phase A ➔ B |
| **Section 6 (`id="operations"`)** | Downstream Production SOP, Aspect Ratio Lock & Quality Gate Verification Summary. | Phase A |

### 7.6 🛡️ Gate 1.5 Execution, Pre-Production Visual Asset Calibration & ✋ CHECKPOINT 2
Run the automated Pre-Production Linter before presenting `setting.html`:
```bash
python engine/setting_audit_suite.py output/<slug>/setting.html
```
- Fix any failing gate internally until `ALL PRE-CHECKPOINT 1 GATES PASSED` prints.
- Save a **Registry Draft** (§11) in `history-registry.json` to lock character names, visual style, genre, arena, tropes, and hero prop group.
- **Pre-Production Visual Asset Calibration (`Real-Image Spatial Sync`)**: Whenever the user generates the actual reference images from `setting.html` (16:9 Character Model Sheets, 2×2 Location Grids, Tier-1 Prop Sheets) and shares them in chat, the Agent MUST visually inspect the rendered images to calibrate actual furniture positions, doorways, lighting directions, and spatial landmarks before locking Stage 3/4 scene staging.
- Present `CP2` to the user:
```text
✋ CHECKPOINT 2 — setting.html (Phase A) đã vượt qua toàn bộ kiểm định (Gate 1.5 PASSED)
File: output/<slug>/setting.html
→ "ok" để sang Stage 3 (Biên kịch chi tiết Tập 1) | Gửi ảnh Nhân vật / Bối cảnh đã tạo để đồng bộ tọa độ thực tế | "edit [nội dung]" để tinh chỉnh
```

---

## §8 — STAGE 3: EPISODE SCREENPLAY & ROADMAP PHASE B (`🛡️ Gate 1.5 ➔ ✋ CP3`)

> **JIT Load**: `0b-temporal-camera-grammar.md` + `1-narrative-screenplay-architecture.md` (Part III–VIII) + `0-creative-doctrine.md` (§1–§5). Author **ONE episode screenplay per checkpoint**.

### 8.1 Tier 2, Tier 4 & Tier 5 Episode Architecture (`12–18 Scenes` of `10s / 15s` per ~3-Minute Episode)

#### 1. Tier 2 — Episode Storyline Rules (`Cốt Truyện Mỗi Tập`)
Every episode is **one complete mini-story PLUS one piece of the macro story** (watching a single episode alone still has a clear beginning, middle, and end):
1. **Episode Goal (`Mục tiêu tập`)**: What the character wants to achieve *in this episode* (smaller than the series goal).
2. **Obstacle (`Trở ngại`)**: What blocks them in this episode.
3. **One Main Shift (`Một chuyển biến chính`)**: By the end of the episode, the situation or understanding must differ from the start, changing **at least one thing that can never go back to how it was** (*quan hệ vỡ, bí mật lộ, người rời đi*).
4. **One New Information Layer on the Master Secret (`Một thông tin mới về bí mật lớn`)**: Opens **one new layer only** — never exposing the whole secret early.
5. **4-Beat Episode Structure (`Cấu trúc 4 nhịp`)**:
   - **Open / Hook (`Mở`: `15–20%`, within Scenes 1–2 — never drag out introductions)**
   - **Develop (`Phát triển`: `40–50%`)**
   - **Climax (`Cao trào`: `20–25%`)**
   - **Close (`Kết`: `10%` — cliffhanger or resonant aftermath)**
6. **One Memorable Visual or Prop Detail (`Một chi tiết hình ảnh hoặc đạo cụ đáng nhớ`)**: Used as the connector in Tier 3.

#### 2. Tier 4 — Per-Scene Rough Prose, 5 Psychological Subversion Laws & Duration Routing (`Mặc Định 10.0s @Director — Cảnh 15.0s Chuyển Qua @CombatDirector`)
An episode (~3 minutes) is divided into **`12–18 scenes`**, written in **continuous present-tense prose (without splitting seconds)** before any video prompt is compiled:
- **By Duration & Agent Owner**:
  * **Default `10.0s` Scene (ALL Standard Dialogue, Psychological Drama, Confrontation & Twist Scenes — Routed to `@Director` `[🎭 MODEL TIÊU CHUẨN · 10.0s]`)**: **1 moment, 1 role-reversal/shift**, **`3–5 sentences` of continuous prose** structured around the **3-Beat Subversion Curve (`False Calm / Mask ➔ Micro-Visual Reveal / Crack ➔ Role Reversal`)**, dialogue **`0–2` short sentences** (**`12–22 words total`**, ending on a **Calm Understatement closing line `2–6 words`**).
  * **Extended `15.0s` Scene (Reserved EXCLUSIVELY for High-Motion Action, Chase, Ambush, Physical Struggle & Combat — Routed to `@CombatDirector` `[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s]`)**: **`5–7 sentences` of continuous kinetic action prose** structured around the **Kinetic Contrast Curve (`Calm/Setup ➔ Snap Freeze ➔ Full-Speed Flight/Pursuit [0 dialogue] ➔ Hard Stop + VFX/Trap [0 dialogue] ➔ Rear-Angle Boss Ambush + 2–5w Checkmate Line`)**. Never assign `15.0s` to standard conversational scenes.
- **Scene Division & Pacing Rules**:
  * **One Job per Scene**: Each scene does **strictly ONE thing**. If a scene requires two purposes, split it into two scenes.
  * **Rhythmic Variety**: Never allow three consecutive scenes to share the same emotion, tempo, or dialogue density. Include at least one silent or sparse-dialogue scene per episode.
  * **Mandatory 2-Step Approval inside Stage 3 (`1-Line Scene List First ➔ Continuous Rough Prose Second`)**:
    1. **Write the 1-Line Rough Scene List FIRST**: Each scene is 1 line: `"Địa điểm, ai, làm gì, để làm gì"` (`Location, who, doing what, for what purpose`), verified with **`"Vì vậy (Therefore)"` / `"Nhưng (But)"`**.
    2. **Review/Approve the entire 1-Line Scene List** before writing the detailed continuous prose for each scene.

#### 3. Tier 5 — Inter-Scene Connection Rules (`Liên Hệ Giữa Các Cảnh & Nối Thoại`)
1. **Causality Over Listing (`"Vì vậy" / "Nhưng"` — Ban `"Và rồi"`)**: Two consecutive scenes must connect via *"therefore (`vì vậy`)"* or *"but (`nhưng`)"*, never *"and then (`và rồi`)"*. If a scene only connects via *"and then"*, it is redundant and must be cut.
2. **Action–Reaction Chain**: Scene $K$ ends with an action, question, or emotion; Scene $K+1$ opens with its direct consequence or reaction (which may be a physical action instead of words).
3. **Visual, Acoustic, or Word Bridge (`Cầu nối hình ảnh / âm thanh / chữ`)**: A prop, color, sound (e.g., glass touching table $\to$ glass shattering), or final keyword (`Word Hook`, e.g., ending Scene $K$ on *"anh cả"* and opening Scene $K+1$ repeating *"anh cả"*) carries across the cut.
4. **Alternating Emotional & Dialogue Rhythm**: Tense/dense scenes alternate with quiet/sparse scenes to avoid flat pacing.
5. **Immediate Visual Cue on Space/Time Jumps (`TH2`)**: When jumping location or time, the opening second of the new scene shows it through a visual detail (never text overlays).
6. **Information Flow & Chekhov's Payoff**: Track who heard what (characters never react to information they haven't heard), and any prop or line emphasized in Scene $K$ must have a concrete effect in a later scene.

### 8.2 Macro, Meso & Micro Continuity Architecture & Screenplay Optimization for Visual Relay
1. **Meso Continuity (`Ep N ↔ Ep N+1`)**: Driven by 3 Cross-Episode Threads (*Question Escalation $Q_1 \to Q_2$*, *Irreversible Power/Address Ledger*, *Prop/Injury State Ledger*) and connected via one of the **4 Episode Bridges** (`Bridge 1` Zero-Gap Relay, `Bridge 2` Causal Time-Jump, `Bridge 3` Parallel POV Counter-Strike, or `Bridge 4` Sitcom Reset).
2. **Micro Continuity (`Sc K ↔ Sc K+1`), Smart Sequence Clustering & Clean Terminal Keyframe Law**:
   - **Optimization Law 1 — Smart Sequence Clustering (Gom Cụm Bối Cảnh Thông Minh)**:
     * Partition every 6–12 scene episode into **2–3 cohesive Location Sequences** (`W11` check), grouping **2–4 consecutive scenes inside the same physical location** before switching to the next location (e.g., `Sequence 1 [Scenes 01–04: Living Room]` ➔ `Sequence 2 [Scenes 05–07: Kitchen]` ➔ `Sequence 3 [Scenes 08–10: Ancestral Courtyard]`).
     * Never ping-pong erratically across different rooms every single 10s scene; clustering consecutive scenes in the same space maximizes **Case 1 Static-Frame Continuation** and builds sustained dramatic pressure.
   - **Optimization Law 2 — Clean Terminal Keyframe Landing (`Shot 4 / Shot 5` I2V-Ready Pose)**:
     * Every scene screenplay MUST engineer the final `2.0s` shot (`Shot 4` in 10s or `Shot 5/6` in 15s) so that characters resolve their primary movement into a **Clean Dynamic Landing Pose (Điểm Đỗ Khung Hình Tĩnh Sắc Nét)**: clear orientation, grounded hand/prop contact, and zero wild mid-swing motion blur.
     * This ensures that when the user renders Scene $K$, its terminal frame (`Last Frame @00:10.0 / @00:15.0`) is crisp, well-composed, and immediately usable as the exact `First Frame (00:00.0)` reference image for Scene $K+1$.
   - **Optimization Law 3 — 10-Second Psychological Subversion Economy & Zero Semantic Repetition**:
     * Each 10s scene focuses on **1 razor-sharp psychological reversal (`Mask ➔ Crack/Micro-Visual Reveal ➔ Role Reversal`) + 1 close-up tactile/visual detail + 1–2 spoken lines ending on a calm `2–6w` understatement**.

### 8.3 Canonical 5-Tier & 7-Step Episode Rough Script Template (`Tầng 1–5 Cốt Truyện & Đối Thoại` + `5 Quy Tắc Đảo Chiều Tâm Lý` + `Sổ Liên Tục & Sổ Thoại`)
To eradicate technical bloat during screenwriting and guarantee deep storytelling art, Stage 3 separates **Screenwriting (`Stage 3: 1-Line Scene List + Continuous Present-Tense Rough Prose`)** from **Directorial Prompting (`Stage 4: Multi-Shot Storyboard Prompts`)** and executes the **5-Tier Series & 5-Tier Dialogue Rules + 5 Psychological Subversion Laws**:
1. **Tier 1 Character Voice Profile (`Hồ Sơ Giọng Nói — Blind Test`)**: Every character has a distinct sentence rhythm, vocabulary, kinship address card (`Bố–Con`, `Anh cả–Chú em`, `Tôi–Ông` + shift threshold), verbal habit, **one thing they NEVER say straight**, and a fixed AI voice parenthetical. **Blind Test**: If speaker names are hidden on any two lines, the reader must still know immediately who is speaking.
2. **Tier 4 Safe AI Video Dialogue Standard (`~2.5 words/s` + Calm Understatement `2–6w` Closing Line & `10.0s` Default vs. `15.0s` Combat Routing)**:
   - **Default `10.0s` Scene (`@Director` — All Standard Dialogue, Drama, Confrontation & Twist Beats)**: **`0–2 sentences`** (up to 3 short lines with Off-Screen `L-Cut`), **`12–22 words total`** across the entire clip, ending on a **Calm Understatement closing line (`2–6 words`)**.
   - **Exclusive `15.0s` Scene (`@CombatDirector` `[⚡ SEEDANCE · 15.0s]` — High-Motion Action, Chase, Ambush, Struggle & Combat Only)**: **`0` spoken words during high-speed chase (`Shot 3`) & VFX trap (`Shot 4`)**, paired with a brief setup line (`Shot 1–2`) and an **Ice-Cold Boss Checkmate closing line (`2–5 words`)** in `Shot 5/6`.
   - **9 Golden Scene Dialogue & Subversion Rules**: (i) Every line does at least 1 job; (ii) Authentic spoken sentences (short, elliptical, zero greetings/prefaces); (iii) Enter in the middle of conflict (*In medias res*); (iv) **Mask & Role-Reversal Curve** in every scene; (v) **Micro-Visual Reveal over Verbal Exposition** (reveal hidden identity/scheme via 1 close-up visual detail like fangs, black nails, glowing runes, or keyring tap — never verbal explanation); (vi) **Image speaks first, dialogue speaks second**; (vii) Max 1–2 characters interacting directly per shot window; (viii) Finish speech $\ge 0.8\text{s}$ before the shot ends; (ix) **Calm Understatement Closing Line (`2–6 words`)** (*`"I'm sorry."`*, *`"Miss, you seem lost."`*, *`"Because you secretly sold Warehouse Four."`*).
3. **The 7-Step Episode Screenwriting Order (Stage 3 Output Structure)**:

```text
================================================================================
TẬP [N]: [Tên Tập] | CUNG CHIA: [Hồi I / II / III / IV] | THỜI LƯỢNG: [12–18 Cảnh · Mặc Định 10s (@Director · Linh Hoạt 1–4 Shots) | 15s Hành Động/Combat (@CombatDirector · 3–6 Shots)]
================================================================================

📌 PHẦN 1 — CỐT TRUYỆN TẬP (TẦNG 2), ĐẠO CỤ TIER-1 & LIÊN KẾT TẬP (TẦNG 3):
• 1. Mục tiêu tập (nhỏ hơn mục tiêu cả bộ): [...]
• 2. Trở ngại trong tập: [...]
• 3. Chuyển biến chính (đổi ít nhất 1 thứ không quay lại được): [Đầu tập: ... ──▶ Cuối tập: ...]
• 4. Một lớp thông tin mới về Bí mật lớn (chỉ mở 1 lớp, KHÔNG lộ hết): [...]
• 5. Đạo cụ / Vũ khí / Vật phẩm Tier-1 xuất hiện trong tập (Kèm file ảnh tham chiếu 4 góc độc lập không dính tay người & trạng thái):
  - `[Tên đạo cụ tiếng Anh chuẩn]` (`prop-[name].jpg` ➔ `<<<Image X>>>`): [Trạng thái State 0 / State 1 / State 2 | Chi tiết khắc/dấu hiệu nhận diện sẽ zoom cận cảnh ở Shot 2]
• 6. Bảng theo dõi liên kết tập (Tầng 3 — Dùng ít nhất 2 trong 4 mối nối):
  | Tập | Hậu quả từ Cliffhanger tập trước | Mục tiêu & Chuyển biến | Mồi cài mới (Trả ở tập N+2+) | Trả mồi từ tập trước | Cliffhanger cuối tập |
  |---|---|---|---|---|---|
  | [N] | [...] | [...] | [...] | [...] | [...] |

🎙️ PHẦN 2 — HỒ SƠ GIỌNG NÓI & THẺ XƯNG HÔ TRONG TẬP (TẦNG 1 ĐỐI THOẠI — CHE TÊN VẪN NHẬN RA):
| Nhân vật (Proper Name & Ảnh) | Cách nói & Nhịp câu | Từ vựng & Thẻ xưng hô (Kèm điểm đổi) | Điều KHÔNG BAO GIỜ nói thẳng | Tag Giọng & Cảm Xúc Duy Nhất (Cách 1 — Không ghi số tuổi) |
|---|---|---|---|---|
| [Proper_Name] (<ref.jpg>) | [Câu ngắn cụt / Dài trau chuốt / Hỏi ngược...] | [Xưng - Gọi | Đổi khi...] | [...] | `([vocal timbre/maturity], [baseline tone])` (VD: `(deep weathered baritone, calm unhurried tone)`) |

📋 PHẦN 3 — DANH SÁCH CẢNH THÔ 1 DÒNG & KIỂM TRA NHÂN QUẢ "VÌ VẬY / NHƯNG" (TẦNG 4 & TẦNG 5):
(Phân bổ nhịp: Mở 15–20% [Hook ngay cảnh 1–2] ➔ Phát triển 40–50% ➔ Cao trào/Cú đảo 20–25% ➔ Kết 10%. Mặc định toàn bộ cảnh tâm lý/thoại là 10s [@Director · linh hoạt 1–4 shots]; chỉ cảnh Hành động/Rượt đuổi/Combat mới dùng 15s chuyển qua [@CombatDirector · 3–6 shots]. Mỗi cảnh chỉ làm ĐÚNG 1 VIỆC):
• Cảnh 01 [10s | Mở | @Director | Đạo cụ Tier-1: <prop-*.jpg / Không>]: [Địa điểm, ai, làm gì, để làm gì]
  ↳ [NHƯNG / VÌ VẬY]
• Cảnh 02 [10s | Mở | @Director | Đạo cụ Tier-1: <prop-*.jpg / Không>]: [Địa điểm, ai, làm gì, để làm gì]
  ↳ [NHƯNG / VÌ VẬY]
• Cảnh 03 [10s (hoặc 15s @CombatDirector nếu là cảnh Hành động/Rượt đuổi/Combat) | Đạo cụ Tier-1: <prop-*.jpg / Không>]: [Địa điểm, ai, làm gì, để làm gì]
  ...

🎬 PHẦN 4 — CỐT TRUYỆN THÔ VĂN XUÔI TỪNG CẢNH (VIẾT LIỀN MẠCH Ở THÌ HIỆN TẠI, KHÔNG CHIA GIÂY — LÀM RÕ NHÂN VẬT, BỐI CẢNH & ĐẠO CỤ TIER-1):

--- CẢNH [K] ([10s @Director / 15s @CombatDirector]) — [Tên Cảnh Ngắn Gọn] ---
• Mục đích cảnh & Nhịp tâm lý / Nhịp cắt máy dự kiến (VD: 2 shots chậm 6s-4s sâu lắng / 3 shots 2s-5s-3s đột ngột / 4 shots 3s-2s-3s-2s cận cảnh đạo cụ lật kèo): [1 câu ngắn]
• Địa điểm, Thời điểm & Nhân vật: [Địa điểm (<loc_ref.jpg>), thời điểm | Nhân vật có mặt (<char_ref.jpg>) | Điểm nối: TH1 / TH2 / TH3]
• Đạo cụ / Vũ khí Tier-1 & Phương án cầm/đặt tại 00:00 (Để khóa `[prop]: <<<Image X>>>` chuẩn 100%): [Nếu có: Tên đạo cụ tiếng Anh chuẩn (<prop_ref.jpg>) | Đặt ở đâu hoặc Ai cầm bằng tay nào tại 00:00 (VD: tay phải cầm chuôi kiếm, tay trái để trống / đặt trên mặt bàn cạnh hợp đồng) | Chi tiết nào sẽ lên cận cảnh]
• Văn xuôi hành động & Thoại (Hình ảnh nói trước – Thoại nói sau | Cảnh 10s @Director = 12–22 từ | Cảnh 15s @CombatDirector = Tương phản động năng Tĩnh ➔ Khựng ➔ Chạy/Đánh 0 thoại ➔ Bẫy VFX/Va chạm ➔ Chốt 2–5 từ):
  [3–5 câu văn xuôi liền mạch cho cảnh 10s (hoặc 5–7 câu cho cảnh 15s Hành động/Combat) tả hành động nhìn thấy được ở thì hiện tại, tương tác đạo cụ rõ ràng, kèm câu thoại tự nhiên.]
• Chi tiết đáng nhớ & Cầu nối sang Cảnh [K+1] (Tầng 5): [Cầu nối hình ảnh/âm thanh/đạo cụ hoặc Cầu nối từ khóa Word Hook / Câu hỏi – Đáp án]

📓 PHẦN 5 — CẬP NHẬT SỔ LIÊN TỤC & SỔ THOẠI SAU TẬP [N] (CONTINUITY & DIALOGUE BIBLE):
• 1. Ai biết gì (Who Knows What) sau Tập [N]: [...]
• 2. Chuỗi bàn giao Đạo cụ Tier-1 & Nhân vật (Prop Custody & State): [Đạo cụ/vũ khí đang ở trạng thái nào (State 0/1/2), đặt ở đâu hoặc ai đang giữ; trang phục/thương tích/quan hệ nào đã đổi]
• 3. Sổ thoại (Câu lặp Echo line, Lời hứa, Lời đe dọa, Lời nói dối đã nói & Tập cần trả): [...]
================================================================================
```

### 8.4 Stage 3 Pre-Flight Verification (`Đối Chiếu 5 Tầng & 5 Quy Tắc Đảo Chiều Trước Khi Viết Prompt`)
Before presenting the Episode N Rough Script in chat (`✋ CP3`), verify:
1. **Tier 1 & 2 Check**: Does the episode serve the Central Question / Transformation Arc, reveal **only 1 layer** of the Master Secret (zero full spoilers), and change **at least 1 thing irreversibly**?
2. **Tier 3 Check**: Are at least 2 inter-episode connectors used (`Cliffhanger`, `Setup/Payoff`, `Visible Consequence`, `Recurring Motif`), opening directly on the consequence of Episode $N-1$'s cliffhanger?
3. **Tier 4 & 5 Scene & Subversion Check**: Does each scene do **strictly ONE job**, connect via **`"Vì vậy"` / `"Nhưng"`** (zero `"Và rồi"`), follow the **Mask ➔ Micro-Visual Reveal ➔ Role Reversal** curve, and default standard scenes to `10s` (`@Director`) while routing `15s` Action/Chase/Combat scenes to `@CombatDirector`?
4. **Tier 1–5 Dialogue Check**: Does every line pass the **Blind Voice Test**, obey **Micro-Visual Reveal Over Verbal Exposition**, stay within **`12–22 words` (`10s`)**, and end on a **Calm Understatement closing line (`2–6 words`)**?
5. **Continuity & Dialogue Bible Check**: Are Character/Location/Prop tags synced with `setting.html` and is the Post-Episode Ledger updated?

Present `CP3` directly in chat:
```text
✋ CHECKPOINT 3 — Kịch bản thô chi tiết Tập [N] (Đi sâu từng cảnh 01..[M] kèm Chỉ dẫn Tham chiếu TH1/TH2/TH3 & Model Seedance) đã đối chiếu hoàn tất
→ Gõ "ok" để bắt đầu Stage 4 ngay với Cảnh 01 (Agent tự lấy thông số Bối cảnh / Nhân vật / Đạo cụ từ file setting.html; bạn chỉ cần gửi Ảnh Tĩnh Cuối Cảnh trước ở các cảnh nối tiếp TH1/TH3)
→ "edit [nội dung]" | "cảnh [K]: [yêu cầu]" để tinh chỉnh kịch bản thô trước khi tạo prompt
```

---

## §9 — STAGE 4: INTERACTIVE SCENE-BY-SCENE DIRECTING, VISUAL CROSS-CHECK & MULTI-SHOT STORYBOARD PROMPT COMPILATION (`Làm Từng Cảnh 1 & Đối Chiếu Trực Quan — Zero tap-X.html ➔ ✋ CP4`)

> **JIT Load**: `.agents/DIRECTOR.md` (+ `combat-director/SKILL.md` for `[⚡ SEEDANCE · 15s]` Action/Chase/Combat scenes) + `0b-temporal-camera-grammar.md`.
> **ABSOLUTE RULE**: Never generate `tap-1.html ... tap-N.html` files and never dump all scenes of an episode at once. Stage 4 is executed **100% interactively in chat, strictly ONE SCENE AT A TIME (`Scene 01` $\to$ `Scene 02` $\to$ ... $\to$ `Scene M`)**, cross-checking with the user at every single scene.

### 9.1 Producer-to-Director Handshake
`@Director` (and `@CombatDirector` for `15.0s` scenes) receives: (1) Approved Episode N Rough Script & Per-Scene Breakdown from Stage 3 (`CP3`), (2) `output/<slug>/setting.html` (containing all 5-Vector Location inventories, Character profiles, and Tier-1 Prop specs), and (3) for `TH1 / TH3` continuation scenes only, the user's extracted **Static Terminal Frame (`Last Frame @00:10.0 / @00:15.0`)** from Scene $K-1$.

### 9.2 The Interactive Scene-by-Scene Co-Pilot Loop (`Scene K` Execution & Cross-Check Protocol)
For each individual scene $K \in \{1..M\}$, execute a strict **4-Step Interactive Loop** with the user:
1. **Step 1 — Continuity & `setting.html` Cross-Check (`Đối Chiếu Đầu Vào Cảnh K`)**:
   - Cross-check `Scene K` according to its **Continuity Reference Case (`TH1`, `TH2`, or `TH3`)**:
     * **🟢 Case 1 (`TH1 — Cùng Thời Điểm & Cùng Bối Cảnh: User gửi Ảnh Tĩnh Cuối Cảnh K-1`)**: Inspect the user-supplied **Static Terminal Frame (`Last Frame @00:10.0` or `@00:15.0`)** from Scene $K-1$ and lock `[subject]:` and `[prop]:` at `00:00.0` of Scene $K$ to match that ending frame **100% verbatim in physical reality** (while keeping the `setting.html` `<<<Image X>>>` reference tags in `[context]:`, `[subject]:`, and `[prop]:`). *(If the user types `"ok"` without sending an image, use `Code Block 2 [HANDOVER STATE]` from Scene $K-1$).*
     * **🔵 Case 2 (`TH2 — Mở Đầu Tập, Đổi Bối Cảnh, Nhảy Thời Gian Hoặc Đổi Tuyến Nhân Vật: Agent Tự Đọc Từ setting.html — KHÔNG Bắt User Gửi Ảnh`)**: Do **NOT** ask the user to send location or character images in chat! Read the New Location's 5-Vector inventory, Character sheets, and Tier-1 Prop specs **directly from `output/<slug>/setting.html` and the Stage 3 Rough Script** to populate `[context]:`, `[subject]:`, and `[prop]:` immediately.
     * **🟣 Case 3 (`TH3 — Ngoại Lệ Siêu Nhiên / Xuyên Không / Dịch Chuyển Không Gian`)**: Lock `[subject]:` and `[prop]:` at `00:00.0` to the exact body posture, forward momentum, and hand grip from Scene $K-1$'s user-supplied terminal frame, while reading the New World/Era Location's `[context]:` directly from `output/<slug>/setting.html`.
2. **Step 2 — Unified Multi-Shot Storyboard Compilation & Agent Routing (`Mặc Định 10.0s @Director` vs. `Cảnh 15.0s Chuyển Qua @CombatDirector`)**:
   - **For Default `10.0s` Scenes (`[🎭 MODEL TIÊU CHUẨN / LIP-SYNC · 10.0s]` — Compiled by `@Director`)**:
     * Structure into **`3–4 Shots` (`3s–2s–3s–2s`: `00:00-00:03`, `00:03-00:05`, `00:05-00:08`, `00:08-00:10`)** using `1–2` short natural sentences per shot (`15–30w`), Selective Face Obscuration (`The camera avoids [Name]'s full face, showing only [Name]'s lower face, jawline...`), a `2s` close-up prop/micro-reveal insert (`Shot 2` + optional Off-Screen `L-Cut`), and a **Calm Understatement closing line (`2–6 words`)** in `Shot 4`.
   - **For All `15.0s` Scenes & High-Motion Action/Chase/Ambush/Combat (`[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s]` — Routed Exclusively to `@CombatDirector`)**:
     * Structure into **`5–6 Shots` (`3s–3s–4s–3s–2s` or `3s–3s–2s–2s–3s–2s`)** using `1–2` short natural sentences per shot (strictly zero `→` arrows) along the **Kinetic Contrast Curve**: `Shot 1 (00:00-00:03)` Calm/Setup $\to$ `Shot 2 (00:03-00:06)` Snap Freeze (`expression freezes abruptly... all warmth fading from her eyes, replaced by pure panic`) $\to$ `Shot 3 (00:06-00:10 · 4s)` `Exterior/Interior, long tracking follow shot` (**strictly `0` spoken words**) $\to$ `Shot 4 (00:10-00:13 · 3s)` `Wide shot transitioning to fixed frame` (`stops sharply, her body going rigid` + VFX/trap activation; **`0` spoken words**) $\to$ `Shot 5 (00:13-00:15 · 2s)` `Medium shot, rear camera angle` (target spins around to find the hunter/boss standing silently in the shadows with `(No objects should appear in the character's hands)` + `2–5w` checkmate line).
3. **Step 3 — Mandatory Pre-Flight Self-Audit (`Đối Chiếu Chống Sai Sót Trước Khi Xuất Cảnh K`)**:
   - Verify: (i) **`<<<Image X>>>` declared ONLY ONCE** in `[context]:` and `[subject]:` (0 times inside `Shot 1..N`), (ii) **100% Zero-Costume & Zero-Age compliance** in `[subject]:` and `Shot 1..N`, (iii) **Proper Character Names Only** (no generic `Woman`, `Man`), (iv) **1–2 short natural sentences per shot** (`15–30w`, zero `→` arrows), and (v) Clean Terminal Keyframe Landing in the final shot.
4. **Step 4 — Deliver the 4-Part Interactive Scene Card in Chat & Wait for User Confirmation**:
   - Output directly in chat: **👁️ Phần 1 (Đối Chiếu Tham Chiếu & Đầu Cảnh)**, **🎭 Phần 2 (Tóm Tắt `Shot 1..N` & Điểm Đỗ Cuối Cảnh)**, **🎬 Phần 3 (Code Block 1 Multi-Shot Storyboard Prompt & Code Block 2 Handover)**, and **⏭️ Phần 4 (Chỉ Dẫn Bước Tiếp Theo Cho `Cảnh K+1`)**. STOP and wait for user confirmation before generating `Scene K+1`.

### 9.3 Code Block 1 — Canonical Unified Storyboard Prompt Template (`10.0s @Director` & `15.0s @CombatDirector` With Double-Lock Reference & `[prop]:` Block)
```text
Night · Interior · Mansion Dining Room (Night)
Style: 3D Semi-Realistic Cinematic Animation, Unreal Engine 5 and Octane Render style, detailed skin shaders, soft subsurface scattering, warm amber volumetric lighting.

[context]:
Grand mansion mahogany dining room <<<Image 1>>> (100% architectural layout, furniture, and lighting strictly refer to this reference image), night. Spacious formal dining room featuring a long polished walnut dining table set with crystal red wine glasses, a glowing black marble fireplace behind the head chair, and mahogany-paneled walls. Warm amber light from an overhead crystal chandelier casts soft reflections across the tabletop in the heavy aristocratic atmosphere.

[subject]:
Bradley <<<Image 2>>> (100% facial features, handsome appearance, hairstyle, body proportions, and exact outfit strictly refer to this reference image): Seated at the side of the polished walnut dining table, right hand holding a crystal red wine glass, eyeline toward Harold — the only Bradley in frame.
Harold <<<Image 3>>> (100% facial features, dignified appearance, hairstyle, body proportions, and exact outfit strictly refer to this reference image): Seated at the head chair in front of the marble fireplace, right hand resting beside a leather-bound transfer contract and the tarnished brass truck keyring, eyeline toward Bradley — the only Harold in frame.

[prop]:
Tarnished brass truck keyring <<<Image 4>>> (100% shape, weathered brass material, carved '04' warehouse tag, and visual details strictly refer to this reference image): Resting on the polished walnut tabletop beside Harold's right hand at 00:00 — the only tarnished brass truck keyring in frame.

[sound]:
Warm dining room ambiance, soft fireplace crackle, heavy metallic clink of a brass keyring striking polished walnut wood, subtle crystal glass tension, and two firm finger taps on brass.

Shot 1 (00:00-00:03) - Interior, medium close-up, slow push-in
Bradley raises his crystal red wine glass toward the head of the table with a polite, confident smile, though his eyes gleam with quiet greed.
Bradley (smooth tenor, warm overly polite tone): "Rest easy, Dad. The company is safe with me."

Shot 2 (00:03-00:05) - Close-up, fixed shot
On the polished walnut tabletop, Harold's right hand firmly sets the tarnished brass truck keyring right on top of the leather-bound transfer contract with a heavy metallic clink, blocking the signature line.
Bradley (across the table, smooth tenor, voice tightening): "Why bring out that old junk tonight?"

Shot 3 (00:05-00:08) - Interior, medium close-up, over-the-shoulder perspective from behind Harold
Seen past Harold's shoulder in the foreground, Bradley freezes mid-sip.
Bradley's polite smile fades into a tense stare as his fingers tighten around the crystal wine stem.

Shot 4 (00:08-00:10) - Medium close-up, side slider shot
The camera avoids Harold's full face, showing only Harold's lower face, jawline, firm mouth, and index finger tapping twice on the tarnished brass truck keyring.
A cold, knowing half-smile tugs at the corner of Harold's lips.
Harold (deep weathered baritone, calm unhurried tone): "Because you secretly sold Warehouse Four."

Master-level cinematography and composition, smooth dynamic camera pacing, atmospheric sound design.
Strict visual consistency: maintain 100% identical facial features, beauty, hairstyle, exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.
Do not generate subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.
```

### 9.4 Silent Scene & Silent Film Directive
For any silent scene (`Model 0`) or full Silent Film, omit all spoken dialogue blocks, amplify tactile Foley and micro-visual reveals across `Shot 1..N`, and end with:
```text
Master-level cinematography and composition, smooth dynamic camera pacing, atmospheric sound design.
Strict visual consistency: maintain 100% identical facial features, beauty, hairstyle, exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.
Do not generate subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video. Do not generate spoken dialogue, lip movement matching speech, or voiceover.
```

### 9.5 Interactive Scene-by-Scene Cross-Check Matrix (No `tap-X.html` Generation)
Every single scene prompt (`Scene K`) delivered in chat MUST pass the following **7-Point Cross-Check**:
1. **Double-Lock 100% Reference & Single `<<<Image X>>>` Declaration Law**: Are `<<<Image X>>>` tags declared **ONLY ONCE** in `[context]:`, `[subject]:`, and `[prop]:` with the explicit `(100% ... strictly refer to this reference image)` parenthetical right after each tag, **never repeated** inside `Shot 1..N`, and sealed with the `Strict visual consistency: ...` footer?
2. **Zero-Costume, Zero-Age & Single Vocal-Timbre Tag Law (`Gates 3A & 3E`)**: Are all clothing words (`in a black jacket`, `in a dark suit`, `skirt`) and numeric ages / age/hair/beard words (`32-year-old`, `young blonde`, `silver-bearded`) 100% purged from the entire prompt, with voice maturity and emotion encoded in **ONE single parenthetical (`[Proper_Name] ([vocal timbre/maturity], [tone]): "..."`)**?
3. **Proper Names & Continuity Grounding (`TH1 / TH2 / TH3`)**: Are all characters named with fixed proper names (`Bradley`, `Harold`, `Elena`, `Dante`) and anchored to 100% real visible landmarks from the reference image?
4. **Tier-1 Prop & Weapon Consistency (`[prop]: <<<Image X>>>`)**: If a Tier-1 Hero Prop, Weapon, or Key Artifact appears in the scene, is it declared in `[prop]: <<<Image X>>>` with its exact `00:00` resting placement or hand-grip (`right hand` with `left hand empty`, or `spaced two-handed grip`), and referenced by its exact canonical noun phrase in `Shot 1..N`?
5. **Dynamic Shot Pacing & Shot Economy (`1–2 Short Natural Sentences / Shot`)**: Is the shot rhythm (`1–4 shots` in `10s`; `3–6 shots` in `15s`) chosen organically by dramatic intent, and does each `Shot N` express 1 clear state transition `A ➔ B` in 15–30 words without `→` arrows?
6. **Selective Directorial Toolkit**: Are *Micro-Visual Reveals*, *Selective Face Obscuration*, *Off-Screen `L-Cut` audio*, *Empty-Hand Lock* `(No objects should appear in the character's hands)`, and *Calm Understatement (`2–6w`) closing lines* deployed purposefully where the scene demands them?
7. **Clean Terminal Keyframe Landing**: Does the final shot guide characters into a stable, zero-motion-blur pose recorded in `Code Block 2 ([HANDOVER STATE])`?

### 9.7 Master Pre-Flight Gate Matrix (Interactive Stage 4 Scene Linter)

| Gate / Check | Classification | Enforcement Rule |
|---|---|---|
| **Gate 1 (Single-HTML Law)** | Hard Gate | Only `output/<slug>/setting.html` is generated as an HTML file; Stage 3 & Stage 4 execute 100% interactively in chat (`Zero tap-X.html`). |
| **Gate 2** | Hard Gate | Explicit clip duration (`10.0s` Default `@Director` vs. `15.0s` Action/Combat `@CombatDirector`), starting at `00:00` and ending at `00:10` / `00:15` / `00:30`. |
| **Gate 2B** | **Hard Gate** | **Mandatory 12-Row Story Spine & 5-Tier Series/Dialogue Architecture** locked before scene compilation. |
| **Gate 3A** | Hard Gate | **Zero numeric ages and zero age/hair/beard words** anywhere in Code Block 1; vocal maturity and tone encoded via **Method 1 (`[Proper_Name] ([vocal timbre/maturity], [tone]): "..."`)**. |
| **Gate 3B** | Hard Gate | Zero freeze-frame holds (`freeze frame`, `frozen frame`, `zero-velocity`). |
| **Gate 3C** | Hard Gate | **Proper Character Names Only** (`Bradley`, `Harold`, `Elena`, `Dante`) across `[subject]:`, `Shot 1..N`, and speaker headers; zero generic `Woman`, `Man`, `the father`, and zero `snake_case` `ho_ten`. |
| **Gate 3D** | Hard Gate | Zero camera hardware, lens mm, f-stop, ISO, fps, or numeric Kelvin jargon document-wide. |
| **Gate 3E** | Hard Gate | **Zero clothing/wardrobe descriptions** (`jacket`, `suit`, `skirt`, `dress`, `coat`) anywhere in Code Block 1 (`[subject]:` or `Shot 1..N`). |
| **Gate 3F** | Hard Gate | Minor Protection Protocol: zero generic minor nouns; zero sexual, body-focused, violence, or adult-label lexicon with registered `minor_characters`. |
| **Gate 3G** | Hard Gate | Mandatory Header (`[Time] · [Interior/Exterior] · [Location]` + `Style:`) and Footer (`Master-level cinematography...` + `Strict visual consistency: ...` + `Do not generate subtitles...`) on every Code Block 1. |
| **Gate 3H** | Hard Gate | Zero Cartesian math coordinates (`X: +0.8m`) and zero 2D frame-edge tokens (`screen-left`, `frame-right`) in Code Block 1. |
| **Gate 3I** | Hard Gate | 100% Stateless prompts (zero `from Scene N` or `previous scene` references in Code Block 1). |
| **Gates 3J, 3K, 3L** | Hard Gate | **Double-Lock 100% Reference & Single `<<<Image X>>>` Declaration Law**: `[context]:`, `[subject]:`, and `[prop]:` (when Tier-1 prop/weapon is present) declare `<<<Image X>>>` **ONLY ONCE** followed immediately by `(100% ... strictly refer to this reference image)`, with **ZERO `<<<Image X>>>` repetition inside `Shot 1..N`**. |
| **Gate 3M** | Hard Gate | Dynamic contiguous shots (`Shot 1 (00:00-00:XX)` .. `Shot N`) starting at `00:00` and ending at `00:10` (`1–4 shots` `@Director`) or `00:15` (`3–6 shots` `@CombatDirector`). |
| **Gate 3N** | Hard Gate | Mandatory `Strict visual consistency: maintain 100% identical facial features, beauty, hairstyle, exact outfit, and exact weapon/prop design...` and negative subtitle/text directives at the tail of every Code Block 1. |
| **Gate 3O** | Hard Gate | Zero Dead Air phrases (`holds still`, `stands rigid through`, `blinks quietly`). |
| **Gate 3P** | Hard Gate | Zero literal placeholder tokens (`audio tag`, `cảm xúc khi nói`, `LÀM GÌ`) in prompts. |
| **Gate 3Q & 3R** | Hard Gate | **1–2 Short Natural Sentences per Shot (`15–30 Words`)**: Each `Shot N` expresses 1 clear state transition `A ➔ B` in natural cinematic prose; strictly zero mechanical `→` arrows. |
| **Gate 3S** | Hard Gate | **180° Axis, Clean Spatial Grouping (`1–2` active characters per shot in Multi-Shot, or `1 Continuous Shot` for 3–4 simultaneous characters) & Zero Ghost Fixtures**: All landmarks and Tier-1/Tier-2 props touched in `Shot 1..N` must be pre-declared in `[context]:`, `[subject]:`, or `[prop]:`. |
| **Gate 4 & 4B** | Hard Gate | 100% Verbatim dialogue sync with Stage 3 Rough Script; `12–22 words` total for `10.0s` scenes (`@Director`); `0` spoken words during high-speed chase/VFX shots (`Shot 3 & Shot 4`) in `15.0s` scenes (`@CombatDirector`). |
| **Gates 4D, 4E, 4F** | Project Gate | Enforces `kinship_ladder`, `meal_terms`, and `bookish_terms` when defined in `output/<slug>/project_rules.json`. |
| **Gate 4G** | Hard Gate | Separated Speaker Dialogue Line (`[Proper_Name] ([spatial anchor if off-screen], [vocal timbre/maturity], [tone]): "[Spoken line]"`) placed cleanly on its own line below the shot's action prose. |
| **Gate 4H** | Hard Gate | Mandatory Code Block 2 (`HANDOVER STATE AT 00:10.0 / 00:15.0`) + `Outbound Continuity Reference Case (TH1 / TH2 / TH3)` + `Kinetic Momentum Bridge` in every scene card. |

### 9.8 ✋ CHECKPOINT 4 (End of Episode N Scene-by-Scene Loop)
Once the final scene (`Scene M`) of Episode $N$ is delivered and verified in chat with the user:
```text
✋ CHECKPOINT 4 — Hoàn tất toàn bộ [M]/[M] cảnh của Tập [N] (Đã đối chiếu trực quan từng cảnh 100%)
Tóm tắt Tập [N]: [Bảng 1 dòng/cảnh: Cảnh | Bối cảnh | TH1/TH2/TH3 | Model (Standard/Seedance) | Điểm nối cuối cảnh]
→ "ok" để sang Tập [N+1] (Stage 3: Kịch bản thô Tập [N+1]) hoặc Stage 5 (Đóng gói SEO & Thumbnail)
→ "cảnh [K]: [chỉnh sửa]" nếu muốn tinh chỉnh lại bất kỳ cảnh nào
```

---

## §10 — STAGE 5: DISTRIBUTION & PACKAGING (`seo-youtube.html` — `✋ CP5`)

> **JIT Load**: `.agents/skills/youtube-growth-architect/SKILL.md`. Mandatory for every completed project.

Compile `output/<slug>/seo-youtube.html` containing:
- **Tier 1 — Omnibus (Full Movie / Series Compilation)**:
  1. **5 High-CTR Title Variants** (`50–65` characters) using the 4 Universal Title Formulas + Narrative POV Invariance.
  2. **4 Sovereign Thumbnail Prompts** enforcing the 4 Pillars: *Suspended Catastrophe*, *Extreme Duality & Somatic Delta*, *Embedded 3D Text ($\le 4$ words)*, and *Mobile Safe Zones*.
  3. **4-Tier NLP Description** inside copy-paste blocks with cumulative `10s` scene chapters.
  4. **7-Cluster Audience Tag String** ($\le 500$ characters) + Polarizing Debate Pinned Comment (seeded from the Story Spine `[DEBATE]` row).
- **Tier 2 — Per-Episode Packaging**: Dedicated `[Ep N/T]` cliffhanger titles, episode thumbnail prompts, episode chapters, and next-episode binge-funnel pinned comments.

✋ **CHECKPOINT 5**: Present `output/<slug>/seo-youtube.html`, finalize `history-registry.json` (§11), and conclude production (`🎬 DONE`).

---

## §11 — HISTORY REGISTRY PROTOCOL (MANDATORY)

- **Draft at `CP2` (after `setting.html` passes Gate 1.5)**: Record character names, visual style, genre, arena, tropes, hero prop group, and narrative mode in `history-registry.json` with `"status": "draft"`.
- **Finalize at `CP5`**: Record hook archetype, narrative polarity, story track, escalation variant, twist codes (`TW-xx`), cliffhanger codes (`C1–C7`), and diurnal lighting; set `"status": "complete"`, append to `story_history`, increment `total_stories_produced`, and refresh `session_log`.

---

## §12 — CONSTITUTIONAL DO / NEVER MATRIX

| ✅ ALWAYS DO | ❌ NEVER DO |
|---|---|
| Write and maintain all system `.md` files and code comments in 100% professional English | Mix Vietnamese rules into system documentation or leave broken markdown fences |
| Generate **ONLY ONE HTML file (`output/<slug>/setting.html`)** at Stage 2 to prepare pre-production visual resources, and execute all subsequent stages (`Stage 3` Episode Rough Script & `Stage 4` Scene-by-Scene Prompts) **100% interactively in chat**, one episode and one scene at a time | Generate `tap-1.html ... tap-N.html` files, dump all episode prompts at once in batch mode, or skip interactive per-scene cross-checking with the user |
| Enforce the **3-Case Continuity Reference Point Law (`TH1 / TH2 / TH3`) & `Seedance` Model Routing**: (`TH1`) build Intra-Location Scene $K+1$ directly from Scene $K$'s user-supplied **Static Terminal Frame (`@00:10.0 / @00:15.0`)** (`100% Zero-Drift` at `00:00.0`); (`TH2`) re-anchor Inter-Location / Time-Jump / Character-Switch scenes directly to the user-supplied **New Location & Character Reference Images**; (`TH3`) preserve character posture/momentum/prop grip while swapping `[context]:` in Supernatural/`Xuyên Không` shifts; weave $\ge 1\text{–}2$ **`Seedance (10.0s / 15.0s)` Action/Chase scenes** per episode, and design a **Clean Terminal Keyframe Pose (`@00:08.5–00:10.0` / `@00:13.5–00:15.0`)** at the end of every scene | Guess spatial coordinates blindly in text when user reference images/frames are provided, apply `TH1` static frames across a `TH2` location cut, or end a clip in wild mid-swing motion blur that ruins next-scene I2V continuation |
| Enforce the **6 Root-Cause Depth Laws** (3-Layer Stakes, 3-Wall Escalation, Iceberg Subtext, Anti-Caricature & Forensic Logic, Multi-Sequence Partitioning, Genre-True Resolution) | Write trivial 90-second single-room chit-chat, passive weeping victims, Scene-2 self-diagnoses, or 5-second moral sermon villain conversions |
| Pass `setting_audit_suite.py` (`Gate 1.5`) on `setting.html` at Stage 2 and perform the **6-Point & 14-Gate Pre-Flight Cross-Check** on every scene in chat at Stage 4 | Present an unaudited `setting.html` or output a scene prompt without cross-checking against the Stage 3 Rough Script and user's reference image |
| Choose Voice Mode, Shot Scale, Camera Angle, and Camera Movement per scene from the Scene Intent Card with a one-clause reason | Copy-paste the same phase split (`4.5s/4.5s/1.0s`), voice mode, or 2-turn ping-pong dialogue across every scene |
| Enforce the Single Focal Action Law (`Gate 3R`), Optical Camera Clause Law (`Gate 3Q`), and Scale/Angle Purity Law (`Gate 3S`) | Stack multiple sequential macro-verbs in one phase or append dangling `. Focus on [name].` tags |
| Respect the user's Aspect Ratio (`16:9`, `9:16`, etc.) and Visual Style preset (`3d-semi-real`, etc.) | Hard-lock an aspect ratio to a genre or ignore `project_rules.json` |

---

## §13 — CANONICAL WORKSPACE FILE MAP

```text
d:\Project\Sven\
├── AGENT.md                                              ← Level 1 Showrunner (orchestration router & JIT loader)
├── workflow.md                                           ← Master Pipeline Coordinator & Constitutional SSOT (this file)
├── history-registry.json                                 ← 14-Axis Anti-Repetition Registry
├── README.md                                             ← Repository Architecture & Operational Overview
├── .agents\
│   ├── SCREENWRITER.md                                   ← Level 2 Master Screenwriter (Stages 0–3, Pillars 1 & 2)
│   ├── DIRECTOR.md                                       ← Level 2 Film Director (Stage 4 Interactive Scene Co-Pilot, Pillars 3 & 4)
│   ├── hooks.json                                        ← Autonomous Quality Gate Hooks
│   └── skills\
│       ├── combat-director\SKILL.md                      ← High-Velocity Action, Chase & Martial Combat Director
│       ├── director\SKILL.md                             ← Director Operational Skill
│       ├── screenwriter\SKILL.md                         ← Screenwriter Operational Skill
│       └── youtube-growth-architect\SKILL.md             ← Stage 0 & Stage 5 YouTube Growth & SEO Architect
├── engine\
│   ├── runbooks.json                                     ← Genre & Production Presets Catalog (8 Runbooks + 12 Style Presets)
│   ├── runbook_manager.py                                ← Preset Loader & Project Initializer
│   ├── setting_audit_suite.py                            ← Stage 2 Pre-Production Resource Linter (Gate 1.5: Gates 1–6B)
│   ├── genres\                                           ← Modular Genre Adapters (Layer 2)
│   │   ├── README.md
│   │   ├── action.md                                     ← Action, Martial Arts, Chase & Supernatural Combat
│   │   ├── drama.md                                      ← Social, Family & Healing Drama
│   │   ├── fantasy.md                                    ← Time-Travel, Portal Isekai, Xianxia & Supernatural Fantasy (TH3)
│   │   ├── microdrama.md                                 ← High-Velocity Viral Microdrama
│   │   ├── sitcom.md                                     ← Situation Comedy
│   │   └── thriller.md                                   ← Detective Mystery, Folk Suspense & Survival Mind-Games
│   └── references\                                       ← The Cinematic Knowledge Engine (SSOT)
│       ├── 0-creative-doctrine.md                        ← Thinking Layer: Two-Layer Core, 6 Depth Laws, Spine & Plot Engine
│       ├── 0b-temporal-camera-grammar.md                 ← Temporal & Camera Grammar: Timing Numbers & Canonical Syntax
│       ├── 1-narrative-screenplay-architecture.md        ← Pillar 1: Narrative Structure, 20 Twists & 8 Dialogue Models
│       ├── 2-casting-worldbuilding-specification.md      ← Pillar 2: Cast Topology, 16:9 Sheets (Mẫu 1–3, 2B), 50 Styles, 30 Genres
│       ├── 3-cinematography-3d-staging.md                ← Pillar 3: 14 Scales, 4-Axis Angles & 3D Spatial Staging
│       ├── 3b-lighting-atmospheric-physics.md            ← Assistant 3B: 6-Point Lighting Contract & Atmosphere
│       ├── 4-ai-video-prompt-compiler.md                 ← Pillar 4: Stateless Prompt Compiler, Handover Ledger & Minor Protection
│       └── 4b-diegetic-foley-sound-design.md             ← Assistant 4B: 4-Layer Diegetic Soundscape & Foley
└── output\<slug>\                                        ← Project Deliverables Package
    ├── project_rules.json                                ← Project-Specific Rules & Overrides
    └── setting.html                                      ← Stage 2 SOLE HTML Deliverable: Pre-Production Resource Preparation File
```

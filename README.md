# SVEN — Autonomous Cinematic Video Generation Engine

> **Hollywood-Grade Storytelling, 3D Spatial Geometry & Physics-Driven AI Video Architecture**  
> Operating standard for high-retention generative cinema (`Seedance 2.5 Pro`, `Sora`, `Runway Gen-3`, `Kling`, `Wan 2.1`, `Hailuo`, `Veo`).

---

## 🏛️ Repository Architecture

The Sven engine is organized into modular layers: autonomous talent personas, deep cinematic knowledge references (The Thinking Layer, The 4 Master Pillars, Directorial Assistants), deterministic compilation and audit engines, and final production deliverables.

```text
d:\Project\Sven\
├── .agents\                                     ← LEVEL 2 TALENT PERSONAS & SKILLS
│   ├── DIRECTOR.md                              ← Level 2: Creative & Technical Film Director (Pillars 3 & 4)
│   ├── SCREENWRITER.md                          ← Level 2: Master Screenwriter & Worldbuilder (Pillars 1 & 2)
│   ├── hooks.json                               ← Autonomous Workflow Hooks & Session Lifecycles
│   └── skills\
│       ├── combat-director\                     ← High-Velocity Action, Chase & Martial Combat Skill
│       ├── director\                            ← Director Operational Skill
│       ├── screenwriter\                        ← Screenwriter Operational Skill
│       └── youtube-growth-architect\            ← Growth Architect Skill (Packaging, SEO, Retention)
│
├── engine\                                      ← PRODUCTION AUTOMATION & SSOT KNOWLEDGE CORE
│   ├── runbooks.json                            ← Production Presets Catalog (Microdrama, Drama, Sitcom, etc.)
│   ├── runbook_manager.py                       ← CLI Manager for Production Presets & Aspect Ratio Config
│   ├── prompt_compiler.py                       ← Deterministic Episode HTML Compiler
│   ├── episode_audit_suite.py                   ← Master Episode Linter & Quality Gates (Gates 1–5, 2B, 3A–3S, 4A–4H)
│   ├── setting_audit_suite.py                   ← Pre-Production Linter & Gate 1.5 Validator
│   │
│   ├── genres\                                  ← Specialized Genre Blueprints & Dialectical Matrices
│   │   ├── action.md                            ← High-Stakes Action, Martial Arts, Chase & Combat
│   │   ├── drama.md                             ← Social & Healing Drama (Subtext, Micro-Sacrifices)
│   │   ├── fantasy.md                           ← Time-Travel, Portal Isekai, Xianxia & Supernatural Fantasy (TH3)
│   │   ├── microdrama.md                        ← High-Tension Viral Microdrama (Cliffhangers, Reversals)
│   │   ├── sitcom.md                            ← Situational Comedy (Fast Banter, Comic Mechanics)
│   │   └── thriller.md                          ← Detective Mystery, Folk Suspense & Survival Mind-Games
│   │
│   └── references\                              ← THE CINEMATIC KNOWLEDGE ENGINE (SSOT)
│       ├── 0-creative-doctrine.md               ← The Thinking Layer: Intent → Choice → Reason (Spine & Plot)
│       ├── 0b-temporal-camera-grammar.md        ← Temporal & Camera Grammar: Timing Numbers & Prompt Syntax
│       │
│       ├── 1-narrative-screenplay-architecture.md   ← Pillar 1: 6 Beats, 20 Twists, Dialogue Geometries, WPS
│       ├── 2-casting-worldbuilding-specification.md ← Pillar 2: Cast Topology, 16:9 Sheets (Mẫu 1–3, 2B), 50 Visual Styles, 30 Genres
│       ├── 3-cinematography-3d-staging.md          ← Pillar 3: 14 Scales, 4-Axis Angle Architecture, Camera Combos, 3D Spatial Staging
│       ├── 3b-lighting-atmospheric-physics.md      ← Directorial Assistant 3B: 6-Point Lighting & Atmosphere
│       ├── 4-ai-video-prompt-compiler.md            ← Pillar 4: Prompt Compilers, Handover States, Mode B Laws
│       └── 4b-diegetic-foley-sound-design.md        ← Directorial Assistant 4B: Code Block 2 Soundscape & Foley
│
├── AGENT.md                                     ← Level 1: Executive Producer & Showrunner Bible
├── workflow.md                                  ← Master Production Pipeline Bible & Constitutional SSOT
├── history-registry.json                        ← 14-Axis Anti-Repetition Registry (Names, Props, Plots, Arenas)
├── README.md                                    ← Workspace Architecture & Operational Guide
├── .gitignore                                   ← System & Temporary Scratch Exclusion Rules
│
└── output\                                      ← 🎬 FINAL PRODUCTION DELIVERABLES DIRECTORY
    └── {project-slug}\                          ← Standalone Project Package
        ├── project_rules.json                   ← Project-Specific Rule Overrides & Constraints
        └── setting.html                         ← SOLE HTML DELIVERABLE: Pre-Production Resource Bible (Characters, Props, Locations)
```

---

## ⚙️ Core Operational Engine

### 1. Step-by-Step Interactive Hierarchy & Single-HTML Resource Law (`setting.html` Only)
To eliminate optical hallucinations, character drift, and mechanical prompt spamming, Sven strictly enforces the **Single-HTML Resource Rule (`Chỉ xuất duy nhất file setting.html — Bỏ toàn bộ file tap-1.html ... tap-N.html`)** and **100% Interactive Step-by-Step Execution**:
- **Step 1 — Master Storyline (`Stage 1: Kịch bản chính ➔ ✋ CP1`)**: Interactive in chat: Locks the 12-Row Story Spine, 3-Layer Stakes, Dynamic Cast Sizing, 6-Beat Short Film or 4-Act Series (`A/B/C-Plot`) Master Blueprint, Inter-Episode Relay Bridges (`Ep N ↔ Ep N+1`), and **Cross-Genre Kinetic Action / High-Tension Chase Slots (`10.0s` or `15.0s` `Seedance`)**.
- **Step 2 — Pre-Production Resource Bible (`Stage 2: output/<slug>/setting.html — DUY NHẤT 1 FILE HTML ➔ 🛡️ Gate 1.5 ➔ ✋ CP2`)**: Before any scene prompt generation, `@Screenwriter` and `@Director` deliver **the sole HTML file `setting.html`** so the user can prepare all visual reference assets: (1) 3-Layer Story Architecture, (2) 6-Layer Character Psychology & 16:9 Multi-Angle Model Sheets (`Mẫu 1A/1B, 2, 2B 3D Semi-Real, 3` — Zero-Text Standard), (3) Two-Tier Props (Tier 1 Hero Props with 16:9 sheets vs. Tier 2 everyday items text-only), and (4) 5-Vector Locations (`16:9 2×2 Grids`). Verified via `python engine/setting_audit_suite.py output/<slug>/setting.html`.
- **Step 3 — Episode Rough Script & Deep Per-Scene Breakdown (`Stage 3: Kịch bản thô từng tập & đi sâu từng cảnh ➔ ✋ CP3`)**: Interactive in chat (one episode at a time), grouping scenes into **2–3 Smart Location Sequences**, engineering a **Clean Terminal Keyframe Landing Pose (`@00:08.5–00:10.0` / `@00:13.5–00:15.0`)** at the tail of every scene, and explicitly declaring **`📌 [CHỈ DẪN SẢN XUẤT & THAM CHIẾU CHO USER]`** at the top of every scene:
  1. **The 3-Case Continuity Reference Point Law (`Điểm Nối Tham Chiếu Giữa 2 Cảnh`)**:
     - **`TH1 (Case 1 — CẦN THAM CHIẾU Khung Hình Cuối Cảnh Trước: Same Time & Same Location)`**: Scene $K$ continues at the exact same moment and location as Scene $K-1$; User extracts Scene $K-1$'s **Static Terminal Frame (`Last Frame @00:10.0 / @00:15.0`)** as Scene $K$'s exact `00:00.0` continuity reference point.
     - **`TH2 (Case 2 — KHÔNG THAM CHIẾU Khung Hình Cảnh Trước: Different Location, Time Jump, or Character Switch)`**: Scene $K$ shifts location, jumps time, or switches cast; User provides **New Location Reference Image (`<location_ref>`) + Active Character Sheets (`<char_ref>`)**.
     - **`TH3 (Case 3 — THAM CHIẾU NGOẠI LỆ Siêu Nhiên / Xuyên Không / Dịch Chuyển Không Gian: Same Moment + Spatial Shift)`**: Preserves exact character body posture, momentum, and held prop from Scene $K-1$'s terminal frame in `[subject]:` & `[PROP]:`, while swapping `[context]:` to the **New World/Era Location Reference Image (`<new_location_ref>`)**.
  2. **AI Video Model & Duration Recommendation Tag**:
     - **`[🎭 MODEL TIÊU CHUẨN / LIP-SYNC · 10.0s]`**: Standard `1.0x` dramatic dialogue, subtext, and emotional acting clips.
     - **`[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE (High-Motion Action Engine) · 10.0s hoặc 15.0s]`**: Mandatory flag for high-velocity action, chase, pursuit, ambush, physical struggle, or martial/supernatural combat scenes (`≥ 1–2` scenes woven into every episode and inter-episode bridge).

### 2. Stage 4 Interactive Scene-by-Scene Execution & Cross-Check Protocol (`Làm từng cảnh 1 & Đối chiếu — Zero tap-X.html`)
- **Strictly 1 Scene at a Time in Chat**: `@Director` (and `@CombatDirector` for `Seedance` scenes) collaborates step-by-step with the user (`Scene 01` $\to$ `Scene 02` $\to$ ... $\to$ `Scene M`) directly in chat (**never generating `tap-1.html ... tap-N.html` or dumping batch episodes**).
- **Mandatory Per-Scene Cross-Check**: Before outputting `Scene K`, `@Director` inspects the user-supplied visual reference (`TH1/TH3` Static Terminal Frame or `TH2` New Location/Character Sheets), cross-checks 100% alignment with the Stage 3 Rough Script (`Case A` vs. `Case B` prop state, verbatim dialogue, landmarks), runs the 14-Gate Pre-Flight Self-Audit, and outputs the **4-Part Interactive Scene Card** (`👁️ Đối Chiếu Tham Chiếu & Đầu Cảnh`, `🎭 Diễn Hoạt & Điểm Đỗ Cuối Cảnh`, `🎬 Code Blocks 1 & 2`, `⏭️ Chỉ Dẫn Tham Chiếu Cảnh K+1`), waiting for the user before proceeding to `Scene K+1`.

### 3. Production Presets & Aspect Ratio Sovereignty Law
- **Production Presets Catalog ([`engine/runbooks.json`](file:///d:/Project/Sven/engine/runbooks.json))**: 1-click initialization of project parameters (pacing, word caps, `10.0s / 15.0s` scene durations, `mode-copilot` default, camera quotas) via `python engine/runbook_manager.py init <preset> <slug>`.
- **Aspect Ratio Sovereignty Law (`workflow.md` §2.3)**: Aspect ratio (16:9 widescreen, 9:16 vertical, 4:3 classic, or 2.39:1 anamorphic) is **100% user-governed**. Genres suggest defaults, but the user's explicit preference is sovereign.

### 4. The Autonomous Talent Ecosystem & Role Allocation
- **👤 User (Executive Co-Producer & Visual Asset Partner)**: Approves `CP0–CP5`, supplies rendered Character/Prop/Location reference images (`Stage 2/3`), supplies extracted Static Terminal Frames (`@00:10.0 / @00:15.0`) for `TH1/TH3` scenes or New Location/Character Refs for `TH2` scenes (`Stage 4`), and renders clips on `Standard Lip-Sync` or `Seedance`.
- **👑 Sven-Agent ([`AGENT.md`](file:///d:/Project/Sven/AGENT.md))**: Level-1 Executive Producer & Showrunner. Owns macro pipeline (`K0–K3`, `Stages 0–5`), anti-spam step-by-step gatekeeping, automated Python audit execution, and registry sync.
- **🖋️ Master Screenwriter ([`.agents/SCREENWRITER.md`](file:///d:/Project/Sven/.agents/SCREENWRITER.md))**: Master of Pillar 1 (Narrative & Dialogue) and Pillar 2 (Cast & Worldbuilding). Authors Stage 0 Concepts, Stage 1 Master Storyline (`A/B/C-Plot` + Action/Chase Slots), Stage 2 `setting.html`, and Stage 3 Episode Rough Scripts & Deep Per-Scene Breakdowns (`TH1/TH2/TH3` + `Standard/Seedance` routing).
- **🎬 Creative & Technical Film Director ([`.agents/DIRECTOR.md`](file:///d:/Project/Sven/.agents/DIRECTOR.md))**: Master of Pillar 3 (Cinematography & 3D Staging) and Pillar 4 (AI Video Prompt Compiler). Executes `TH1/TH2/TH3` visual grounding, directs Golden Triangle optics, 3D spatial staging, Clean Terminal Keyframe Landing, and compiles `tap-X.html`. Supported by Specialized Directorial Assistants (3B Lighting & 4B Sound Design).
- **⚔️ Combat & Action Director ([`SKILL.md`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md))**: Co-directs **all scenes flagged `[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 10.0s / 15.0s]` across all genres** — high-tension chases, pursuits, ambushes, physical struggles, martial arts (`2.3x`), and superhuman blink-speed (`10x`), enforcing the 5 Biomechanical Hand-Grip Laws and micro-timeline arrow (`→`) prompt compilation.
- **📈 YouTube Growth Architect ([`SKILL.md`](file:///d:/Project/Sven/.agents/skills/youtube-growth-architect/SKILL.md))**: Master of Stage 0 Niche Validation and Stage 5 Distribution (`seo-youtube.html`), high-CTR packaging, thumbnail visual tension, and entity SEO.

---

## 🎥 Cinematographic & AI Prompt Compiler Standards

### 1. The Optical Camera Clause Law & Gates 3Q / 3R / 3S
- **Upfront Optical Declaration**: In every timeline beat (`[start–end]`), camera framing, focal plane, vertical/horizontal angle, and camera move MUST be declared inside the **Camera Clause before the em-dash `—`** (e.g., `Medium close-up framing ho_ten_A, shallow depth of field holding sharp optical focus on ho_ten_A's facial features with background softly falling into bokeh, eye level, slow push-in — [action]`).
- **Strict Prohibition of Trailing Tags & Action Compounding (`Standard` vs. `Seedance`)**: Tacking isolated, dangling sentences like `. Focus on [name].` at the tail of action prose is strictly banned (**Gate 3Q**). In `Standard 10.0s` scenes, each character is limited to 1 primary macro action per phase (**Gate 3R**); in **`Seedance (10.0s / 15.0s)` Action/Chase scenes**, `@CombatDirector` chains `2–3` tightly coupled causal action-impact-recoil nodes inside `2.0s–3.5s` micro-phases using the **Kinetic Arrow (`→`)**. Optical ray-tracing, posture-to-angle verticality, OTS lip-sync visibility, and `Cut to` 30°/180° rules are strictly enforced (**Gate 3S**).
- **Automated Enforcement**: Enforced by **Gates 3Q, 3R, and 3S** in `engine/episode_audit_suite.py` as blocking errors.

### 2. The 3 Camera Shot Architectures
- **Track A (Single-Shot Continuous Take)**: 1 single camera, unbroken take, **0 cuts**. Scale and angle change strictly through physical camera trajectory (`slow push-in`, `tracking`, `pedestal up`).
- **Track B (Multi-Shot Cut Sequence)**: Multi-camera coverage cut on the **180° Action Axis** (2–4 shots per 10s clip). Every subsequent shot begins with `Cut to`. Enforces the 5 Continuity Locks (Gaze Vector, Kinetic Baton & Clean Landing Relay, Audio Suture, Static-Frame Handover Ledger, Rhythmic Contrast).
- **Track AB (Hybrid Take + Cut)**: One continuous take (≥ 5s holding 2+ phases) punctuated by 1–2 decisive cuts on the power shift (Take ➔ Button, Trigger ➔ Take, Take ➔ Cut ➔ Take).
- **Track A-Locked Performance Take (Golden Quota §9.8)**: Fixed static camera (0 cuts, 0 camera moves; the word "tripod" is banned in prompt prose). Camera setup declared once in prose header; timeline brackets dedicated 100% to somatic micro-acting and environmental physics. Strictly capped at 1–2 scenes per 9–10 scene episode (~15–20% ratio).

### 3. Subject & Prop Governance (`Initial Prop State Bifurcation` & `3-Case Continuity`)
- **Sovereign `[subject]:` Formula with Initial Prop State Bifurcation (`Case A` vs. `Case B`)**:
  - *Case A (Unheld Prop at $t=0.0\text{s}$ — Default)*: `{ho_ten} [100% Appearance, attire, and facial features Refer to image X], {architectural anchor}, {body posture}, hands free of props, {eyeline toward a character or landmark} — the only {ho_ten} in frame.`
  - *Case B (Actively Held Prop at $t=0.0\text{s}$ — `TH1/TH3` In-Hand Continuation or In Medias Res Opening)*: `{ho_ten} [100% Appearance, attire, and facial features Refer to image X], {architectural anchor}, {body posture}, {explicit t=0.0s hand-grip on the declared prop synchronized 100% with [PROP]:}, {eyeline toward a character or landmark} — the only {ho_ten} in frame.`
- **Biomechanical Launchpad & Kinetic Handshake Protocol**: Action prose emerges directly from the physical posture and hand state declared in `[subject]:`.
- **The Two-Tier `[PROP]:` Scope Law**: `[PROP]:` holds every handheld item, one per line in natural English without underscores, each declaring its $t=0.0\text{s}$ placement (resting on a surface or held in `[ho_ten]`'s hands). Tier 1 hero props (max 1–2 per series) carry `[100% Refer to image …]`; Tier 2 everyday items are text only. Furniture and fixtures (blankets, pillows, chairs, beds, cribs) belong 100% to `[context]:` as rich set dressing inventory.
- **Zero Ghost Object Law**: Any object touched in action must be pre-declared in `[context]:` or `[PROP]:`.

### 4. Zero Dead Air, Clean Terminal Keyframe Landing & Independent Render Atoms
- **Zero Dead Air Law (Gate 3O) & Clean Terminal Keyframe Landing (`@00:08.5–00:10.0` / `@00:13.5–00:15.0`)**: Continuous micro-action density spanning 100% of the clip duration. Phrases that freeze characters (`the frame holds still`, `stands rigid through 00:10`) are strictly banned. Every scene's final `1.0s–1.5s` guides characters into a crisp, zero-motion-blur **Clean Dynamic Landing Pose** ready for `TH1/TH3` static last-frame extraction.
- **Zero Cumulative Timestamps (Gate 3M)**: Third-party AI video tools render each scene as an independent atom (`10.0s` or `15.0s`). Prompts must always start at `00:00` (e.g., `[00:00–00:03.5]`), never cumulative episode stamps like `[00:10–00:20]`.

---

## 🚀 Production Deliverables & Quality Gates

All final outputs are stored under `output/{project-slug}/`:

| Deliverable / Milestone | Stage | Delivery Format & Key Contents | Quality Verification Gate |
|---|---|---|---|
| **Master Storyline & Blueprint (`Kịch bản chính`)** | Stage 1 | **Interactive in Chat**: 12-Row Story Spine Card, 3-Layer Stakes, Dynamic Cast Sizing, Short Film 6-Beat / Series 4-Act (`A/B/C-Plot`) Blueprint, Inter-Episode Bridges & Cross-Genre Action/Chase Slots (`10.0s / 15.0s`). | **✋ CP1** Narrative Depth & Spine Lock |
| **`setting.html` (Duy Nhất 1 File HTML Chuẩn Bị Tài Nguyên)** | Stage 2 | **The Sole HTML File (`output/<slug>/setting.html`)**: 6-Layer Character Psychology, 16:9 Model Sheets (`Mẫu 1A/1B, 2, 2B, 3`), Tier-1 Hero Props, 5-Vector Locations (`2×2 Grids`), and Master Storylines. | `python engine/setting_audit_suite.py output/<slug>/setting.html` (Gate 1.5 + Gates 1C/2B/6B) ➔ **✋ CP2** |
| **Episode Rough Script & Per-Scene Breakdown (`Kịch bản thô Tập N & đi sâu từng cảnh`)** | Stage 3 | **Interactive in Chat (1 Episode at a Time)**: 2–3 Smart Location Sequences, 3-Wall Escalation, **Per-Scene `📌 [CHỈ DẪN SẢN XUẤT & THAM CHIẾU CHO USER]` (`TH1/TH2/TH3` + `Standard 10s / Seedance 10s-15s`)**, Scene Intent Cards, Verbatim Dialogue, and Clean Terminal Landing. | 7-Point Stage 3 Cross-Check with User ➔ **✋ CP3** |
| **Interactive Scene-by-Scene Prompts (`Làm từng cảnh 1 & Đối chiếu`)** | Stage 4 | **Interactive in Chat (Strictly 1 Scene at a Time — Zero `tap-X.html`)**: Visual Input Cross-Check (`TH1/TH2/TH3`), 14-Gate Pre-Flight Audit, `Scene K` Code Block 1 & Code Block 2 (`HANDOVER STATE`), and Next-Scene Reference Prompt. | 6-Point & 14-Gate Per-Scene Cross-Check with User ➔ **✋ CP4** |
| **Distribution & SEO Packaging** | Stage 5 | **Interactive in Chat**: 4 Universal Title Formulas, 4-Pillar Thumbnails, 4-Tier NLP Descriptions, 7 Tag Clusters, Pinned Debate Comment. | **✋ CP5** Final Review & History Registry Sync |

---

## 🛡️ Best Practices & Quality Control

1. **Constitutional SSOT Hierarchy**: Explicit user instructions > `workflow.md` §2 (Hard Constraints) > Creative Doctrine (`0`) & Grammar (`0b`) > Master Pillars 1–4 > Role files (`AGENT.md`, `DIRECTOR.md`, `SCREENWRITER.md`).
2. **Anti-Repetition Engine**: Check `history-registry.json` prior to initiating any new production to ensure character names, hero props, and plot twists remain 100% unique across the universe.
3. **Clean Workspace Standard**:
   - Temporary scripts and test files belong strictly in `scratch/` (auto-ignored by Git).
   - Core talent agents and skills reside exclusively in `.agents/`.
   - All completed production packages reside in `output/{project-slug}/`.

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
[5c]  .agents/PHOTO_DIRECTOR.md                             ← Level 2: Single-Frame Still Image & Keyframe Prompt Architect (@PhotoDirector)
[5d]  .agents/STORYBOARD_DIRECTOR.md                        ← Level 2: 2-Phase Storyboard Grid (9/12/15/25 Shots) & Storyboard-to-Video Architect (@StoryboardDirector)
[5e]  .agents/REF_VIDEO_DIRECTOR.md                         ← Level 2: Source-Video Reference (<<<Video 1>>>) & Entity-Swap Architect (@RefVideoDirector)
[5f]  .agents/ROBLOX_DIRECTOR.md                            ← Level 2: Generalized Roblox 3D Film, R15 Blender & Studio MCP Architect (@RobloxDirector)
[5g]  .agents/COMMERCIAL_DIRECTOR.md                        ← Level 2: Fast-Action Product Commercial & Performance Ad Director (@CommercialDirector: 10.0s = 6 Shots, 15.0s = 9 Shots)
[6]   .agents/skills/youtube-growth-architect/SKILL.md      ← Level 2: Growth Architect (active at Stages 0 and 5)
─── THE THINKING LAYER (load BEFORE any Pillar at Stages 1–4) ───
[7]   engine/references/0-creative-doctrine.md              ← Creative Doctrine: Two-Layer Core, 6 Anti-Shallow Depth Laws, Spine & Plot Engine
[7b]  engine/references/0b-temporal-camera-grammar.md       ← Temporal & Camera Grammar: speech rates, lip-sync windows, canonical syntax
[7c]  engine/references/0c-canonical-numbers.md             ← Canonical Numbers: the ONLY source for counts, durations, word budgets & engagement budgets
[7d]  engine/references/0d-heart-and-value.md               ← Heart & Value North Star: what every story is FOR (moving, positive, valuable), Value Card, Dignity Firewall, Heart & Value Scorecard /8
─── THE 4 MASTER PILLARS & SPECIALIZED DIRECTORIAL ASSISTANTS ───
[8]   engine/references/1-narrative-screenplay-architecture.md   ← Pillar 1 SSOT: Narrative, Twist Catalog (TW-01..20) & 8 Dialogue Models
[9]   engine/references/2-casting-worldbuilding-specification.md ← Pillar 2 SSOT: Cast Topology, 16:9 Model Sheets, setting.html Spec
[9b]  engine/references/2b-character-lines.md                ← Character Lines: role vocabulary, satellite crosswalk, genre cast topologies, arcs, Arc Map, introductions
[10]  engine/references/3-cinematography-3d-staging.md           ← Pillar 3 SSOT: 14 Shot Scales, 4-Axis Angles, 3D Staging, 180° Axis
[10b] engine/references/3b-lighting-atmospheric-physics.md       ← Assistant 3B: 6-Point Lighting Contract & Atmospheric Mediums
[10c] engine/references/3c-camera-master-grammar.md          ← Camera Master Grammar: 8 Questions, 15 sizes, angles & power, moves, lens, focus, 9:16 composition, cuts, genre & scene recipes
[11]  engine/references/4-ai-video-prompt-compiler.md            ← Pillar 4 SSOT: Stateless Prompts, Code Blocks 1/2, Minor Safety
[11b] engine/references/4b-diegetic-foley-sound-design.md        ← Assistant 4B: 4-Layer Diegetic Foley & Soundscape Continuity
```

> **Stage-Gated Just-In-Time (JIT) Loading Law & Anti-Truncation Line-Range Protocol (`≤ 800-Line Single-Call Guarantee`)**:
> Because the `read_file` tool returns at most **800 lines per call**, calling a blind `read_file` from line 1 on a 2,000–3,000-line Pillar file will truncate the bottom 70% of the file and cause the AI to improvise! Therefore:
> 1. **Self-Contained `< 700-Line` Execution Cores First**: All mandatory execution rules, decision matrices, and output schemas are consolidated inside **`workflow.md` (read by stage slice)**, **`.agents/SCREENWRITER.md`**, **`.agents/DIRECTOR.md`**, **`.agents/PHOTO_DIRECTOR.md`**, **`.agents/STORYBOARD_DIRECTOR.md`**, **`0b-temporal-camera-grammar.md`** and **`0c-canonical-numbers.md`** (each read in full in one call). Line counts are not written here because they drift; `python engine/doc_range_check.py` verifies every range below and `--map <file>` prints current section lines.
> 2. **Exact `StartLine–EndLine` Coordinates for Large Catalog Pillars**: Whenever consulting a Pillar catalog (`1–4`), ALWAYS pass the exact `StartLine` and `EndLine` listed below (never read blindly from line 1 to 3000):
>    - **Startup (`K0–K3`)**: `workflow.md` (`StartLine: 1, EndLine: 409`) + `AGENT.md` (`StartLine: 1, EndLine: 90`) + `0c-canonical-numbers.md` (`StartLine: 1, EndLine: 148`) + `0d-heart-and-value.md` (`StartLine: 1, EndLine: 138`) + `engine/runbooks.json` + `history-registry.json`
>    - **Stage 0 (`Concepts → CP0`)**: `workflow.md` (`StartLine: 413, EndLine: 496 · §5`) + `.agents/SCREENWRITER.md` (`StartLine: 1, EndLine: 135`) + `0c-canonical-numbers.md` (`StartLine: 1, EndLine: 148`) + `youtube-growth-architect/references/keyword-niche-discovery-matrix.md` (`StartLine: 1, EndLine: 192` — niche & hook validation by `@GrowthArchitect`) + `0-creative-doctrine.md` (`StartLine: 177, EndLine: 224 · §1.2` & `StartLine: 505, EndLine: 685 · §8–§9`)
>    - **Stage 1 (`Master Storyline & Blueprint → CP1`)**: `workflow.md` (`StartLine: 500, EndLine: 614 · §6`) + `0c-canonical-numbers.md` (`StartLine: 1, EndLine: 148`) + `2b-character-lines.md` (`StartLine: 1, EndLine: 156`) + `1-narrative-screenplay-architecture.md` (`StartLine: 850, EndLine: 1055` — **20/80 Structural Law: 6 Genre Engines & 5 Episode Archetypes**; `StartLine: 1445, EndLine: 1515` — **20 Twists Catalog**) + active `engine/genres/*.md` (`100% read in 1 call`)
>    - **Stage 2 (`Pre-Production Resource File setting.html → CP2`)**: `workflow.md` (`StartLine: 618, EndLine: 689 · §7`) + `2-casting-worldbuilding-specification.md` (`StartLine: 390, EndLine: 720` — **16:9 Model Sheets Mẫu 1A/1B/2/2B/3**; `StartLine: 1410, EndLine: 1746` — **`setting.html` 10-Section Spec**; `StartLine: 1770, EndLine: 2215` — **50 Master Visual Styles**)
>    - **Stage 3 (`Episode N Rough Script & Deep Per-Scene Breakdown in Chat → CP3`)**: `workflow.md` (`StartLine: 693, EndLine: 887 · §8`) + `.agents/SCREENWRITER.md` (`StartLine: 1, EndLine: 135`) + `0c-canonical-numbers.md` (`StartLine: 1, EndLine: 148`) + `0-creative-doctrine.md` (`StartLine: 132, EndLine: 151 · §1` & `StartLine: 505, EndLine: 685 · §8–§9`) + `0b-temporal-camera-grammar.md` (`StartLine: 1, EndLine: 282`) + `1-narrative-screenplay-architecture.md` (`StartLine: 1307, EndLine: 1415` — **12 Hooks & 5 Bridges**; `StartLine: 1865, EndLine: 2265` — **WPS, 3-Layer Cadence & 9 Voice Modes**)
>    - **Stage 4 (`Interactive Scene-by-Scene Prompt Production & Visual Cross-Check in Chat → CP4`) & Turn-1 Direct Prompt Shortcut**: `workflow.md` (`StartLine: 891, EndLine: 1033 · §9`) + `.agents/DIRECTOR.md` (`StartLine: 1, EndLine: 452`) + `3c-camera-master-grammar.md` (`StartLine: 1, EndLine: 321`) + `0c-canonical-numbers.md` (`StartLine: 1, EndLine: 148`) + `0-creative-doctrine.md` (`StartLine: 1, EndLine: 152` — **Scene Intent & Directing from Intent**) + `0b-temporal-camera-grammar.md` (`StartLine: 1, EndLine: 282` — **Speech Physics, One-Move Rule, Zero Tail-Cut Law & 10s/15s Templates**) + `4-ai-video-prompt-compiler.md` (`StartLine: 160, EndLine: 285` & `StartLine: 630, EndLine: 715` — **Temporal-Kinetic-Vocal Equilibrium, `3.2s–4.5s` Spoken Shot Formula & Terminal Settle**) + `1-narrative-screenplay-architecture.md` (`StartLine: 1865, EndLine: 2150` — **WPS & 3-Layer Vietnamese Relational Dialogue**) + (`combat-director/SKILL.md` for `Seedance` Action/Chase/Combat scenes; `.agents/PHOTO_DIRECTOR.md` for Single-Frame Still Images/Keyframes; `.agents/STORYBOARD_DIRECTOR.md` for `9/12/15/25-Shot` Storyboard Grids & `Storyboard-to-Video`)
>    - **Stage 5 (`Distribution Packaging → CP5`)**: `workflow.md` (`StartLine: 1037, EndLine: 1067 · §10–§11`) + `.agents/skills/youtube-growth-architect/SKILL.md` (`StartLine: 1, EndLine: 482`)

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
| **Numbers** | [`0c-canonical-numbers.md`](file:///d:/Project/Sven/engine/references/0c-canonical-numbers.md) | The only source of counts, durations, word budgets, motion density, engagement budgets, cast sizes and retention targets | `0`–`5` |
| **Character Lines** | [`2b-character-lines.md`](file:///d:/Project/Sven/engine/references/2b-character-lines.md) | Role vocabulary, satellite crosswalk, genre cast topologies, arc types, Character Arc Map, introductions (wins over Pillar 1–2 cast tables) | `0`, `1`, `3` |
| **Camera Grammar** | [`3c-camera-master-grammar.md`](file:///d:/Project/Sven/engine/references/3c-camera-master-grammar.md) | The Director's 8 Questions, sizes, angles & power, moves, lens, focus, composition (incl. 9:16), cuts, genre & scene camera recipes (working reference over Pillar 3) | `4` |
| **Pillar 1** | [`1-narrative-screenplay-architecture.md`](file:///d:/Project/Sven/engine/references/1-narrative-screenplay-architecture.md) | 6-Beat Short Film vs. 4-Act Series (`20%/45%/25%/10%`), Triple-Helix `A/B/C-Plot` Weave, 12 Hooks, 20 Twists (`TW-01..20`), 8 Dialogue Models, 4-in-1 Parentheticals, Genre-Calibrated Resolution | `0`, `1`, `3` |
| **Pillar 2** | [`2-casting-worldbuilding-specification.md`](file:///d:/Project/Sven/engine/references/2-casting-worldbuilding-specification.md) | Cast topology (`A1/A2/Tier B/Tier C`), Dynamic Cast Sizing, 6-Cultural Naming Matrix, Living Continuum, 16:9 Model/Prop/Location Sheet Templates (`Mẫu 1A/1B`, `Mẫu 2`, `Mẫu 2B 3D Semi-Real`, `Mẫu 3`), `setting.html` 10-Section Spec, 50 Visual Styles (`25 Live Action + 25 Animation`), 30 Genres | `1`, `2`, `3` |
| **Pillar 3** | [`3-cinematography-3d-staging.md`](file:///d:/Project/Sven/engine/references/3-cinematography-3d-staging.md) | 14 Shot Scales, 4-Axis Angles, Camera Combos, 3D Spatial Staging, Elastic Deformation, 180° Action Axis, Continuity Ledgers, Music Video Architecture | `2`, `4` |
| **Pillar 4** | [`4-ai-video-prompt-compiler.md`](file:///d:/Project/Sven/engine/references/4-ai-video-prompt-compiler.md) | Stateless 10s/15s Kinetic Units (`Standard 10.0s` & `Seedance 10.0s / 15.0s`), 3-Case Continuity Reference Law (`TH1 / TH2 / TH3`), Track A/B/AB/A-Locked, Mode B Reference Laws, Code Blocks 1 & 2, Minor Protection Protocol (§[10d]) | `4` |
| **Combat** | [`combat-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md) | All scenes flagged `[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s]` across all genres (5 Core Kinetic Archetypes): martial arts & supernatural combat, high-velocity chases/ambushes, rapid-cut professional craft/culinary/medical whip-montages, split-second physical rescues, and relic detonations (`5–9 Shot` High-Density Rapid-Cut Storyboard with `1.5s–2.0s` micro-strikes, zero `→` arrows, Weapon Hand-Grip & Empty-Hand Locks) | `3`, `4` |
| **Product Commercials & Conversion Reviews (`commercial`)** | [`.agents/COMMERCIAL_DIRECTOR.md`](file:///d:/Project/Sven/.agents/COMMERCIAL_DIRECTOR.md) & [`commercial-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/commercial-director/SKILL.md) | Exclusive owner of **(Mode 1)** Fast-Action Product Commercials (`10.0s = 6 Shots`, `15.0s = 9 Shots`, `C1–C6`, `CTA-A/B/C`) AND **(Mode 2)** Pain-to-Purchase Product Review Videos (`40.0s–60.0s` = `3–4` stitched `10s/15s` clips with **Decoupled Off-Screen V.O.** + **100% Silent Non-Speaking Visual Acting & Diegetic Foley**, forensic Product/Presenter ref lock, 3-Tier Pain + Honest Minor Flaw 5-Beat Conversion Arc, delivered 1 clip at a time) | `Stage 4`, `All Product Commercials (10s/15s) & Conversion Product Review Videos (40s–60s)` |
| **Photo / Still Keyframes** | [`.agents/PHOTO_DIRECTOR.md`](file:///d:/Project/Sven/.agents/PHOTO_DIRECTOR.md) & [`photo-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/photo-director/SKILL.md) | All Single-Frame Still Scene Keyframe Prompts (`Unified Still Image Architecture`: Static Shot Scale, 4-Axis Camera Angle & Optical Focus + 5-Point Anatomical Pose Lock + Captured Instant Action + Mandatory 4-Zone Facial Micro-Expression `brows/eyes/lips/jaw` + Gender/Style Skin & Makeup Sub-Lock `F1–F4 / M1–M3 / A1–A3`, zero video motion/timeline/audio) and Standalone/Pre-Production Image Prompts | `2`, `4`, `All Single-Frame Still Image Requests` |
| **Storyboard Grid & Storyboard-to-Video** | [`.agents/STORYBOARD_DIRECTOR.md`](file:///d:/Project/Sven/.agents/STORYBOARD_DIRECTOR.md) & [`storyboard-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/storyboard-director/SKILL.md) | Exclusive owner of the 2-Phase Storyboard Pipeline (synthesizing `@PhotoDirector` + `@Director` + `@CombatDirector`): **(Phase A)** Multi-Panel Storyboard Grid Image Prompts (`9 [3×3]`, `12 [3×4]`, `15 [3×5]`, `25 [5×5]` Shots divisible by `3` or `5`, with 100% static pose/angle/4-zone expression per panel) and **(Phase B)** Storyboard-Driven Video Prompts (`[storyboard]: <<<Image 1>>>` + `[subject]: <<<Image 2>>>` + `[sound]:` + explicit 1:1 `Shot 1 (00:XX-00:YY) - Panel 1 ([Grid Position])...` through `Shot N` timeline blocks) | `Stage 4`, `All Storyboard Grid & Storyboard-to-Video Requests` |
| **Source-Video Reference & Entity Swap (`ref-video`)** | [`.agents/REF_VIDEO_DIRECTOR.md`](file:///d:/Project/Sven/.agents/REF_VIDEO_DIRECTOR.md) & [`ref-video-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/ref-video-director/SKILL.md) | Exclusive owner of Source-Video Reference (`<<<Video 1>>>`) & Entity-Swap Prompts (`Mode V1–V4`): Mandatory `0.5s/frame` Contact-Sheet Forensic Extraction before writing, Single `<<<Video 1>>>` & `<<<Image X>>>` Declaration (with explicit source-target visual identification in `[video reference]:`), 100% Canonical Entity Naming Consistency (`Elena`, `V-Rex`, `Kong`) across `[subject]:`, `[sound]:`, and `Shot 1..N`, Timestamped Diegetic Audio & Open-Mouth Vocal Sync, and High-Contrast Optical Boost | `Stage 4`, `All Source-Video Reference (<<<Video 1>>>) & Entity-Swap Requests` |
| **Roblox 3D Film, Series & Blender Animation (`roblox`)** | [`.agents/ROBLOX_DIRECTOR.md`](file:///d:/Project/Sven/.agents/ROBLOX_DIRECTOR.md) & [`roblox-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/roblox-director/SKILL.md) | Exclusive owner of the **Generalized 5-Stage Audio-First & SRT-Driven Roblox 3D Filmmaking Pipeline (`16:9` Widescreen & `9:16` Vertical across All Genres)**: (R1) Concept & Format Lock, (R2) Story & Clean Voice Script for User `.mp3`, (R3) Automated MP3-to-SRT & Sven Core Director Blueprint (`tools/audio_to_srt.py` + `tools/srt_to_director_plan.py`), (R4) SRT-to-Sven-Core 6-Pillar 3D Scene Build on Local PC, Portable `scene_built.blend` Lock & Preview Gate (`Law R0` via **Blender 5.3 + Local MCP [`blender_roblox_kit.py` + `blender_auto_director.py` + `blender_roblox_anim.py` + `blender_env_lighting.py` + `make_faces_expressive.py` [Law R-ANIM, R-LOOK, R-COLLIDE & R-WORLD]]** and/or **Roblox Studio MCP** + `studio_kit/checks.py` + `audit_scene_collisions` + `audit_camera_plan`), and (R5) **Dual-Mode `30 fps` `16:9`/`9:16` Master Render Dispatch (`tools/render_dispatcher.py`: Mode R5-A Local GPU `--target local` when the PC is free/powerful enough vs. Mode R5-B Third-Party External GPU Offload `--target pack / external` to any 3rd-party provider specified by the user)** + Final Mix (`tools/compile_video.py` + `make_caps*.py`) + AI Roblox GFX (`School A4`) | `All Roblox 3D Films, Series, Animations (16:9 & 9:16), Roblox Studio MCP, Headless Blender 5.3 & Roblox AI GFX Requests` |
| **Growth** | [`youtube-growth-architect/SKILL.md`](file:///d:/Project/Sven/.agents/skills/youtube-growth-architect/SKILL.md) | Niche validation, Semantic Entity Clusters, High-CTR Titles, 4-Pillar Thumbnails, SEO Packaging | `0`, `5` |
| **Automation** | `engine/setting_audit_suite.py`, `engine/screenplay_audit.py`, `engine/prompt_audit.py`, `engine/doc_range_check.py`, `engine/runbook_manager.py` | `setting.html` linting (Stage 2), saved episode script linting (Stage 3), saved scene prompt linting (Stage 4), JIT line-range integrity, project initialization | `2`, `3` |

### 1.2 Role Assignment per Stage (RACI & User Collaboration Matrix)

> **SINGLE-HTML RESOURCE RULE (`setting.html` ONLY)**: The system generates **ONLY ONE HTML file (`output/<slug>/setting.html`)** at Stage 2 to prepare all pre-production visual resources (Character 16:9 Model Sheets, Tier-1 Prop Sheets, Location 2×2 Grids). **Never generate `tap-1.html ... tap-N.html` episode HTML files.** All subsequent stages (Stage 3 Episode Rough Scripts and Stage 4 Scene-by-Scene Prompts) are executed **100% interactively in chat**, one episode at a time and one scene at a time, with mandatory cross-checking alongside the User.

| Stage | Checkpoint | Responsible (Executes) | Accountable (Approves) | Consulted & User Visual Input | Mandatory Deliverable & Audit Gate |
|---|---|---|---|---|---|
| **0 — Concepts** | `✋ CP0` | `@Screenwriter` + `@GrowthArchitect` | `Sven-Agent` + **User** | `@Director` | 5 High-Concept Pitches in chat (3-Layer Stakes + Option C Twist) |
| **1 — Master Storyline & Blueprint (`Kịch bản chính`)** | `✋ CP1` | `@Screenwriter` | `Sven-Agent` + **User** | `@Director`, `@CombatDirector` | Interactive in chat: 12-Row Story Spine Card + Dynamic Cast Topology + Short-Film 6-Beat or Series 4-Act (`A/B/C-Plot`, 5 Convergence Nodes, Inter-Episode Bridges & **Cross-Genre Action/Chase `10s/15s` Slots**) Blueprint |
| **2 — Pre-Production Resource File (`setting.html` — Duy Nhất 1 File HTML)** | `✋ CP2` | `@Screenwriter` (+ `@PhotoDirector` for standalone asset prompts) | `Sven-Agent` + **User** | `@Director` (3D spatial review) + **User** (renders & supplies Character/Prop/Location reference images) | **The SOLE HTML Deliverable**: `output/<slug>/setting.html` (Passes `setting_audit_suite.py` **🛡️ Gate 1.5**) + Registry Draft |
| **3 — Episode Rough Script & Per-Scene Breakdown (`Kịch bản thô từng tập & đi sâu từng cảnh`)** | `✋ CP3a` ➔ `✋ CP3b` | `@Screenwriter` | `Sven-Agent` + **User** | `@Director`, `@CombatDirector` | **Interactive in Chat (1 Episode at a Time)**: Episode N Rough Script & Deep Per-Scene Breakdown (`Scene 01..M` with 2–3 Smart Location Sequences, 3-Wall Escalation, **Per-Scene `📌 [CHỈ DẪN SẢN XUẤT & THAM CHIẾU CHO USER]` declaring `TH1/TH2/TH3` + `Standard 10s / Seedance 10s-15s`**, Scene Intent Cards, Clean Terminal Landing, & Verbatim Dialogue) |
| **4 — Interactive Scene-by-Scene Directing & Prompt Cross-Check (`Làm từng cảnh 1 & Đối chiếu`)** | `✋ CP4` | `@Director` (`10s/15s` Dialogue/Drama) · `@CombatDirector` (`15s` Action/Combat/Montage) · `@PhotoDirector` (Single Still Frame) · `@StoryboardDirector` (`9/12/15/25` Storyboard Grid & `Storyboard-to-Video`) | `Sven-Agent` + **User** | `@Screenwriter` (dialogue parity) + **User** (**ONLY sends `TH1/TH3` Static Terminal Frames `@00:10.0 / @00:15.0`** when connecting same-location scenes; for `TH2` new locations, Agent reads directly from `setting.html` without asking User for images) | **Interactive in Chat (Strictly 1 Scene at a Time — Zero `tap-X.html`)**: `setting.html` / `Last Frame` Cross-Check + Pre-Flight Verification + `Scene K` Code Block 1 & Code Block 2 + Next-Scene Handoff |
| **5 — Distribution & Packaging** | `✋ CP5` | `@GrowthArchitect` | `Sven-Agent` + **User** | `@Screenwriter`, `@Director` | Interactive SEO & Thumbnail Package + `history-registry.json` Finalized |

---

## §2 — SYSTEM DEFAULTS (THE CONSTITUTION)

> **THE TWO-LAYER ARCHITECTURE (`0-creative-doctrine.md` §0.05)**: Every Sven production locks **Layer 1: The Universal 4-Tier Core (50%)** (Tier I Great Screenplay ➔ Tier II Great Film ➔ Tier III Great Multi-Episode Series ➔ Tier IV Addictive Individual Episodes) and dynamically mounts **Layer 2: The Genre & Cultural Adapter (50%)** (`drama.md`, `action.md` + `@CombatDirector`, `microdrama.md`, `sitcom.md`, or `thriller`). Never force one genre's or one region's conventions onto another.
>
> **THE NORTH STAR ABOVE BOTH LAYERS (`0d-heart-and-value.md`)**: every Sven story — film, series, episode, scene, ad or Roblox short — exists to **move the viewer and leave them with something good**: an earned heart moment, a positive human value shown through a costly choice, and an unspoken takeaway they carry into their own life. Engagement (hooks, loops, twists, reversals, cliffhangers) is the vehicle; value is the destination. Every story checkpoint shows the **Engagement Scorecard** and the **Heart & Value Scorecard** (`0d` §8: `≥ 6/8`, no `0`), and every reversal obeys the **Dignity & Value Firewall** (`0d` §5): justice restores, never degrades.

### 2.1 Rule Precedence Hierarchy
When rules appear to conflict, resolve them strictly in this order and report any file discrepancy to the user:
1. **Explicit User Instruction** in the current session (sovereign over aspect ratio, duration, delivery mode, and creative direction).
2. **`workflow.md` §2 System Defaults** (Hard Constraints in §2.11 never yield to any lower layer).
2b. **`engine/references/0d-heart-and-value.md` — the Heart & Value North Star**: overrides every engagement craft default below it (hook, face-slap, cold water, cliffhanger, debate seed, genre payoff). When a retention tool collides with the story's heart or value, change the tool, never the value.
3. **`engine/references/0-creative-doctrine.md`, `0b-temporal-camera-grammar.md` & `0c-canonical-numbers.md`** — `0c-canonical-numbers.md` is the single table of every count, duration and budget (any differing number elsewhere is stale); `0-creative-doctrine.md` governs *how* narrative and directorial tools are chosen from dramatic intent (overriding fixed word budgets, shot quotas, or mechanical templates in Pillars/Skills); `0b-temporal-camera-grammar.md` is the sole authority for speech rates, timing numbers, and canonical prompt syntax.
4. **Working references, then Master Pillars 1–4 & Active Genre Modules (`engine/genres/*.md`)** — `2b-character-lines.md` wins over Pillar 1–2 cast rules and `3c-camera-master-grammar.md` over Pillar 3 when they disagree; then the domain-specific catalogs and genre conventions.
5. **Role Specifications (`AGENT.md`, `.agents/SCREENWRITER.md`, `.agents/DIRECTOR.md`)**.
6. **Skills, Examples, and Legacy Templates**.

### 2.2 Three-Layer Language & Entity Naming Protocol
1. **Language Separation**:
   - **User Communication**: Always Vietnamese; direct, decisive, executive tone.
   - **System Documentation & Codebase** (`.md` rules, skills, references, Python scripts): **100% standard professional English**.
   - **Deliverable Files (`setting.html`, `seo-package.md`) & Interactive Chat Outputs**:
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
| **1. Drama Thực Tế (`Grounded Real-World Drama`)** | Gia đình, Thừa kế, Tỷ phú đời thực, Hôn nhân, Thương trường, Pháp lý, Chữa lành, Tình cảm ([`drama.md`](file:///d:/Project/Sven/engine/genres/drama.md), [`healing.md`](file:///d:/Project/Sven/engine/genres/healing.md), [`romance.md`](file:///d:/Project/Sven/engine/genres/romance.md), Realistic [`microdrama.md`](file:///d:/Project/Sven/engine/genres/microdrama.md)) | • **100% Quy luật đời thực & Tâm lý con người thật**: Mâu thuẫn xoay quanh tình thân, lòng tham, sự phản bội, di chúc, quỹ tín thác, hợp đồng tiền hôn nhân, sao kê ngân hàng, tranh tụng tại tòa/HĐQT.<br>• **Quy mô tài chính & doanh nghiệp sát thực tế**: Chuỗi khách sạn, bệnh viện tư, bất động sản, logistics (quy mô tiền theo `0c` §8: `$50M–$1.2B` tổng tài sản, `$5M–$80M` quỹ tiền mặt/nợ/hạn chót).<br>• **Cao trào (`15.0s`)**: Đối chất tâm lý liên hoàn, lật tẩy chứng cứ trước đám đông, giằng xé nội tâm trực diện. | **CẤM TUYỆT ĐỐI** đưa thiết bị viễn tưởng (*đồng hồ thần kinh, AI tự động*), phép thuật/siêu nhiên, con số trăm tỷ đô ảo tưởng, hoặc **ép nhân vật đời thường (luật sư, bác sĩ, doanh nhân) đi đột nhập kho cảng, leo trèo parkour hay đánh võ như điệp viên**! |
| **2. Khoa Học Viễn Tưởng (`Speculative Sci-Fi`)** | Công nghệ tương lai, AI/Cyber, Đột biến Y sinh giả tưởng, Hậu tận thế, Sinh tồn không gian ([`scifi.md`](file:///d:/Project/Sven/engine/genres/scifi.md)) | • **Tiền đề Giả định ("What If?") + 3 Quy Luật Cứng**: (1) *Cơ chế khoa học/công nghệ cốt lõi*, (2) *Giới hạn vật lý / Điều kiện sập hệ thống*, (3) *Cái giá đạo đức & sinh tồn của con người*.<br>• Đạo cụ Tier-1 là thiết bị công nghệ cao/mẫu vật sinh học quyết định vận mệnh; rượt đuổi/đột kích công nghệ cao điều phối qua `Seedance (10s/15s)`. | **CẤM** biến phim Sci-Fi thành cãi vã gia đình vụn vặt không gắn với quy luật công nghệ, và **CẤM** dùng phép thuật không giải thích bằng cơ chế khoa học của thế giới đó. |
| **3. Siêu Nhiên, Huyền Huyễn & Xuyên Không (`Supernatural / Fantasy`)** | Tu tiên (`Xianxia`), Huyền huyễn, Dị năng đô thị, Xuyên không, Trùng sinh, Linh dị ([`fantasy.md`](file:///d:/Project/Sven/engine/genres/fantasy.md), kinh dị [`horror.md`](file:///d:/Project/Sven/engine/genres/horror.md)) | • **Khế ước Hệ thống Sức mạnh / Thời Không (`Trigger – Ceiling – Cost`)**: Rõ nguồn gốc dị năng/tu vi/trùng sinh và phản phệ cơ thể.<br>• **Tiến hóa Linh Vật Tier-1 (`State 0 Phong ấn ➔ State 1 Thức tỉnh ➔ State 2 Bùng nổ/Vỡ vụn`)**.<br>• **Kết nối `TH3` (`Xuyên Không / Biến đổi không gian giữ nguyên đà nhân vật`)** + Giao chiến tốc độ cao (`2.3x–10x` trên `Seedance`) qua [`@CombatDirector`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md). | **CẤM** làm loãng phim siêu nhiên/tu tiên bằng thủ tục hành chính đời thường tẻ nhạt, và **CẤM** đem yếu tố siêu nhiên/huyền ảo cài lậu vào kịch bản `Regime 1 (Drama Thực Tế)`. |
| **4. Hành Động Võ Thuật & Trinh Thám Hình Sự (`Action & Crime Thriller`)** | Võ thuật, Kiếm hiệp, Điệp viên, Trinh thám phá án, Đấu trí mật thất ([`action.md`](file:///d:/Project/Sven/engine/genres/action.md), [`thriller.md`](file:///d:/Project/Sven/engine/genres/thriller.md)) | • **Action (`action.md`)**: Cấu trúc `3-Zone (40% Nén tâm lý 1.0x ➔ 40% Truy đuổi/Thực chiến 2.3x Seedance ➔ 20% Hệ quả)`; `Adaptive Triad` (`Địa hình ↔ Kỹ năng nhân vật ↔ Cọc cược`).<br>• **Thriller (`thriller.md`)**: Bất đối xứng thông tin (`Suspense ↔ Mystery`), cài cắm **$\ge 2$ manh mối thị giác công bằng (`Fair-Play Visual Clues`)**, đấu trí sắc lạnh + truy đuổi sinh tử. | **CẤM** đánh đấm vô nghĩa không có nén tâm lý, **CẤM** phá án nhờ ăn may/trùng hợp ngẫu nhiên mà không có manh mối cài cắm từ trước. |

*(Lưu ý riêng cho **Sitcom / Hài Tình Huống [`sitcom.md`](file:///d:/Project/Sven/engine/genres/sitcom.md)**: Vận hành bằng `Tình huống trớ trêu + Nói dối dây chuyền (Snowball Lie) + Va chạm 3 tuyến + Reset trạng thái cuối tập`, tuyệt đối không bi kịch hóa nặng nề).*

### 2.5 Scene Duration, Intent-First Agent Routing & Temporal-Kinetic-Vocal Equilibrium (`@Director 10.0s & 15.0s Dialogue/Sitcom/Drama` vs. `@CombatDirector 15.0s Action/Chase/Combat`)
1. **Intent-First Routing (`@Director` vs. `@CombatDirector`) & Temporal-Kinetic-Vocal Equilibrium (`Pillar 4` `L160-285` & `0b` `§1–§8`)**:
   - **Never route by clip duration (`15s`) alone**: Route strictly by **Dramatic & Kinetic Intent**.
   - **All `10.0s` AND `15.0s` Dialogue, Sitcom, Comedy, Emotional Drama, Confrontation & Twist Scenes (`Routed to @Director` — Governed by the 6 Golden Dialogue Laws `Law D1–D6`)**:
     * **`Law D1` (100% Static Camera for Continuous Dialogue — Mode D1-A Single Shared Camera Header vs. Mode D1-B Multi-Cut Static Scale Escalation)**: In continuous dialogue, confrontation, and high-emotion or comedic acting scenes, lock **`static camera`** so 100% of the AI's latent motion budget goes to lip-sync, expressive gestures, and 4-zone facial acting (`brows, eyes/moisture, lips, jaw`). Deploy either **(Mode D1-A: Fixed-Camera, Fixed-Angle & Fixed-Scale Continuous Dialogue — Ghi Chung Camera, Cỡ Cảnh & Góc Quay 1 Lần Duy Nhất)** declaring Camera, Shot Scale, and Angle **ONLY ONCE** at the top (`Shot 1 (00:00-00:15) - [Fixed Shot Scale], [Fixed Static Camera & Angle], natural real-time speed`) and underneath focusing purely on the turn-by-turn Action/Emotion + Dialogue exchange (`(00:00-00:03.5) A acts/speaks ➔ (00:03.5-00:07.0) B waves hand/replies ➔ (00:07.0-00:10.5) A counters ➔ (00:10.5-00:15.0) B answers`), OR **(Mode D1-B: Multi-Cut Static Scale Escalation)** stepping closer across distinct static cuts (`Static MCU OTS` $\to$ `Static Reverse MCU` $\to$ `Static Tight CU`).
     * **`Law D2` (Rationed Native Exclamation Trigger at Line Start)**: Open emotional, comedic, or confrontational spoken lines with a **Native Biological Vocal Interjection / Exclamation** (`"Huh?..."`, `"Whoa! Uh..."`, `"Hah! Really?..."`, `"Oh god..."`, `"Hửm?..."`, `"Á! Ối trời..."`, `"Hơ!..."`, `"Ủa?..."`) followed by `?`, `!`, or `...` to prevent monotone text-reading. **Ration it** (`0c` §2): at most 1 in 3 spoken lines per clip, never the same interjection twice in a row, never on calm/authority checkmate lines — an interjection on every line sounds formulaic.
     * **`Law D3` (Expressive Vocal-Behavior Performance Tags Over Dry Musical Jargon)**: Purge clinical musical register labels (`clear velvety alto`, `deep resonant baritone`, `smooth tenor`, `soft airy soprano`) and replace with active vocal-behavior tags (`[Proper_Name] (expressive female/male voice, [scoffing playfully / gasping in panic and stammering / chuckling in disbelief / breath hitching with choked tears / speaking with calm icy authority] in a [delivery tone]): "[Interjection]! ..."`), synchronized with `[sound]:` and `Shot K` action prose.
     * **`Law D4` (`3.2s–4.5s` Spoken Shot Window — Strict Ban on `< 3.0s` Spoken Cuts)**: Every shot containing spoken dialogue MUST be sized to **`3.2s–4.5s`** ($\mathbf{T_{shot}} = 0.4\text{s} + \frac{\text{Words}}{2.5} + 0.5\text{s}–0.8\text{s}$) and paired with **1 simple primary gesture (`One-Move Rule`)**. Maximum spoken shot density is **`3 Shots` in `10.0s` (`3.2s–3.2s–3.6s`)** and **`4 Shots` in `15.0s` (`3.5s–3.5s–3.5s–4.5s`)**. **Mode 2 exception** (`0c` §2): in 100%-dialogue ping-pong, a turn of `≤ 8` EN words / `≤ 10` VN syllables fits a `3.2s–3.5s` window, and the final turn of `6–8` words fits `≥ 3.4s` with its `~0.8s` closed-lip tail — the formula applies to every other spoken shot.
     * **`Law D5` (Two Valid Terminal Modes & Mandatory `0.5s–1.0s` Final Tail Buffer)**:
       - **Terminal Mode 1 (Wordless Final Payoff Shot — Default)**: Finish all spoken lines inside `Shot 1..N-1` (by `00:08` in `10s` or `00:12` in `15s`), reserving the final `2.0s–3.0s` shot (`Shot N`) 100% for the Wordless Visual Payoff / Physical Comedy Button / Somatic Reaction Settle (`0 spoken words`).
       - **Terminal Mode 2 (100%-Dialogue Continuous Ping-Pong — When All Shots Speak, e.g., `3.2s–3.2s–3.6s` in `10s` or `3.5s–3.5s–3.5s–4.5s` in `15s`)**: Keep `Shot 1..N-1` lines concise (**`7–8 EN words` / `8–10 VN syllables` $\approx 2.3\text{s}–2.5\text{s}$**) inside `3.2s–3.5s` windows (`0.5s` buffer per shot to prevent cumulative delay across cuts), and give the final `Shot N` a wider window (**`3.6s` in `10s`; `4.2s–4.5s` in `15s`**) with a short **`6–8 word/syllable`** line so speech finishes `0.8s–1.0s` early, leaving a **mandatory `0.5s–1.0s` (`~0.8s`) silent closed-lip tail buffer (`holding a silent closed-lip expression for the final 0.8 seconds`)** so the last 1–2 words are never cut off!
     * **`Law D6` (The 4-Point Cross-Scene Dialogue & Posture Handover Law — `Scene N ➔ Scene N+1` Seamless Suture)**:
       - **(1) `~1.2s` Golden Breath Bridge & Closed-Lip `Last Frame`**: The `0.8s` closed-lip tail buffer at the end of Scene $N$ + the `0.4s` vocal interjection lead-in at `00:00` of Scene $N+1$ prevents audio clashing across the cut and guarantees a clean closed-mouth `Last Frame` for `TH1`.
       - **(2) 100% `[subject]:` Posture & Prop Inheritance (`TH1`)**: Under `TH1` (same time & location), `[subject]:` at `00:00` of Scene $N+1$ MUST copy 100% of the updated hand, prop, and facial posture reached at `00:10.0` / `00:15.0` of Scene $N$ (never resetting to Scene $N$'s initial `00:00` posture).
       - **(3) Cross-Scene Speaker & 180° Axis Flip (`Anti-Jump-Cut`)**: If the final shot of Scene $N$ frames Speaker A speaking (`OTS targeting A`), `Shot 1` of Scene $N+1$ MUST flip the 180° axis to frame Speaker B (`Reverse OTS targeting B`) responding.
       - **(4) Keyword Baton & Vocal Inertia Relay**: `Shot 1` of Scene $N+1$ directly echoes/inverts the key word or answers the cliffhanger question from Scene $N$'s final line (`"...And left a receipt?"` $\to$ `"Uh—what?! That receipt isn't mine, honey!"`) while preserving biological vocal inertia.
   - **High-Motion Action, Chase, Combat, Vehicle Drift, Sports Climax, Split-Second Rescue & High-Velocity Craft Scenes (`15.0s` / `10.0s` `[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s]` — Routed Exclusively to `@CombatDirector`)**:
     * **First-Principles Kinetic Physics Over Fixed Shot Quotas (`combat-director/SKILL.md`)**: Never force every fast scene into a fixed shot count or rigid template! `@CombatDirector` selects the **Shot Topology** organically from the scene's dramatic & spatial intent:
       - **Topology 1 (`1–2 Shots` — Unbroken 3A Inertial Long-Take)**: Continuous immersive camera tracking (`Black Myth / Sekiro / The Raid` style) with internal time-ramping and hit-stop impact pauses inside the take.
       - **Topology 2 (`3–5 Shots` — Asymmetric Dynamic Contrast)**: Combining a sustained `4s–5s` tracking sprint/exchange with sharp impact cuts and a decelerated reversal/checkmate.
       - **Topology 3 (`6–9 Shots` — Staccato Multi-Shot Rapid-Cut Blitz)**: Fracturing multi-step craft processes (*The Bear / Edgar Wright* culinary, trauma surgery, assembly) or chaotic multi-angle blitzes into `1.5s–2.0s` cuts on peak action (`1 focused action per short cut`, `>45°` angle jumps).
     * **The 4 Core Kinetic Physics Levers**: Across all topologies (both Combat and Non-Combat), velocity and visual weight are driven by: **(1) Surface-Bound Material & VFX Physics** (binding elemental auras/lightning/slash streaks, real-world fire/smoke/sparks/water, or pure tactile deformation directly to host surfaces rather than floating 2D overlays); **(2) Camera Inertia & Relative Velocity** (`AAA action-game inertial whip-follow camera` & impact recoil); **(3) Directional Motion Blur & Trajectory Release** (`strong directional motion blur` freeing the AI from sluggish slow-motion); and **(4) Time-Ramp Modulation & Hit-Stop Weight** (`Acceleration ↔ Hit-Stop Impact Snap / Selective Suspension ↔ Clean Terminal Settle`).
     * **In `Regime 1 (Grounded Realistic Drama)`**: **STRICTLY DO NOT force artificial spy break-ins, parkour chases, or martial arts fights!** Route to `@CombatDirector` in `Regime 1` ONLY when the plot naturally features **Non-Combat High-Velocity Beats** (e.g., High-Velocity Culinary / Emergency Medical sequences, Split-Second Domestic Physical Rescues, or Sports / Musical Virtuosity).
   - **30.0s (`00:00–00:30`) Clips**: Activated ONLY on explicit user request (`8–10 Shots` across three mini-acts per `0b` §9). No arbitrary durations (no 12s, no 20s) are permitted.
2. **The Third-Party AI Render Engine Law (Zero Cumulative Timestamps — Gate 3M)**:
   - Generative video models (Sora, Runway, Kling, Veo, Wan, Hailuo, Seedance) render each scene as a standalone clip from second zero.
   - Every Code Block 1 storyboard **MUST start at `00:00`** (`Shot 1 (00:00-00:XX)`) and run contiguously to `00:10`, `00:15`, or `00:30`. Cumulative episode timestamps (`(00:10-00:20)`) inside prompts are strictly prohibited.
3. **The Motion Density Law (`Vừa đủ chữ — hành động vừa khít thời lượng`) — reconciles the One-Move Rule with Zero Dead Air**:
   - **Two banned failures**: **(a) action overload** — two or three independent primary actions crammed into one shot (`sets the cup down, stands up and walks to the door` in `4s`) ➔ morphing limbs, phantom hands or duplicate props, skipped or reordered actions, jerky speed, broken lip-sync, no clean landing frame; **(b) time underload** — a long shot carrying an action that takes a second (`sets the cup down` for `4s`) ➔ the model invents the rest: frozen stares, unintended slow motion, random or unrequested actions.
   - **The fit**: fill the duration with the **length and depth of one primary action** (preparation ➔ execution ➔ after-beat) + **one biological reaction** (exhale, eye lock, jaw tightening) + **continuous micro-motion** (breath, fingers, fabric, rain, steam, flicker). Never fill it with a second independent primary action. Counts per director: `0c` §1 *Motion density*.
   - *Example (4s)*: ❌ `Lan sets the cup down.` · ❌ `Lan sets the cup down, stands, grabs her bag and walks to the door.` · ✅ `Lan slowly lowers the cup to the table, her fingers lingering on the handle a beat before letting go, her eyes never leaving Minh.`
4. **Zero Dead Air & State-Delta Directing Law (Gate 3O)**:
   - Maintain **100% active physical or vocal occupancy across every shot (`Zero Dead Air`)**. Never leave a conversational character standing mute for `5–7s` while nothing happens.
   - `[subject]:` locks the static `00:00` posture; `Shot 1..N` describes strictly the **state transition (`State A ➔ State B`)** in 1–2 short natural sentences (`15–30w`), **never repeating `[subject]:`'s static posture** and **strictly banning prompt-engineering meta-instructions** (*"speaking immediately from the opening second"*, *"finishes his sentence early"*, *"holds still"*).

### 2.6 Double-Lock `fully_preserved` Reference Image Fidelity Protocol (`<<<Image X>>> (fully_preserved - ...)` Lock) & Two-Tier Prop Architecture
Every Code Block 1 binds locations, characters, and Tier-1 hero props/weapons using the **Unified Storyboard Header Standard (`Style:`, `[context]:`, `[subject]:`, `[prop]:` [when Tier-1 prop/weapon is present], `[sound]:`)** separated by blank lines:
1. **The Single-Declaration `<<<Image X>>>` & `fully_preserved` Reference Fidelity Law (`Khóa Bảo Toàn Thực Thể fully_preserved`)**:
   - **Keep `<<<Image X>>>` Intact**: Never insert descriptive words *inside* the `<<<...>>>` brackets (which breaks multimodal token parsing). Instead, place the **`(fully_preserved - ...)` reference lock parenthetical** immediately *after* `<<<Image X>>>` inside `[context]:`, `[subject]:`, and `[prop]:`.
   - **Declare `<<<Image X>>>` ONLY ONCE**: Declare `<<<Image 1>>>`, `<<<Image 2>>>`, `<<<Image 3>>>`, `<<<Image 4>>>` **ONLY ONCE** inside `[context]:`, `[subject]:`, and `[prop]:`. **STRICTLY NEVER repeat `<<<Image X>>>` inside `Shot 1..N` or speaker headers!** Once declared in the headers, `Shot 1..N` refers to characters and props exclusively by their clean proper/canonical names (`Bradley`, `Harold`, `Kael`, `silver dragon-hilted longsword`).
   - **The Canonical 3-Line Footer (single source — every Code Block 1 ends with exactly these three lines, clauses chosen by condition)**:
     * **Line 1 — `Master-level cinematography and composition, [one clause naming the camera approach of this clip], atmospheric sound design.`** (e.g., `locked static camera framing for maximum facial and vocal acting clarity` for dialogue; `fast-paced shot variation` for montage; `unbroken AAA action-game camera inertia` for a long-take fight).
     * **Line 2 — `Strict visual consistency: maintain 100% identical facial features, [hand clause], matte skin texture, hair color, [makeup,] exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.`** Hand clause: `slender feminine hand proportions` (female only), `strong masculine hand proportions` (male only), `slender feminine and strong masculine hand proportions` (mixed); include `makeup,` only when a female adult is on screen.
     * **Line 3 — `Do not generate duplicate props or utensils, [conditional clauses], oily sweat shine, greasy forehead or nose glare, waxy plastic skin, subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.`** Conditional clauses: `rough masculine hands on female characters, thick knuckles` (female on screen) · `product or label morphing, deformed labels` (product/commercial) · `floating detached VFX, sluggish unintentional slow motion` (action/VFX) · `spoken dialogue, lip movement matching speech, or voiceover` (silent scenes, §9.4).
2. **`[context]:` vs. `[subject]:` — The Location-Prop vs. Character-Prop Separation Law (`Phân Định Rạch Ròi Đạo Cụ Thuộc Bối Cảnh Địa Điểm vs. Đạo Cụ Dành Cho Nhân Vật — Zero Duplicate Props`)**:
   - Format for `[context]:`: `[Evocative English Location Name] <<<Image 1>>> (fully_preserved - same architectural layout, fixed furniture and lighting throughout), [time of day]. [5-Vector Specification: architectural layout & permanent stationary furniture/appliances/set-dressing belonging to the location, physical key lighting source & direction without Kelvin, shadow behavior, atmospheric medium & mood]`.
   - **1. Location / Environmental Props (`Đạo cụ thuộc Bối cảnh Địa điểm` $\to$ Declared EXCLUSIVELY in `[context]:`)**:
     * Only fixed architectural structures, stationary furniture, built-in appliances, and permanent untouched background set-dressing that belong to the location itself (`marble kitchen island, built-in gas stove, built-in stainless steel oven, oak cabinetry, walnut desk, chandelier, windows`) and are **NEVER picked up, wielded, or transformed by a character**.
   - **2. Character-Owned / Interactive Action Props (`Đạo cụ dành cho Nhân vật cầm nắm / thao tác` $\to$ Declared EXCLUSIVELY in `[subject]:`, `[prop]:`, and `Shot 1..N` — STRICTLY BANNED from `[context]:`)**:
     * Any handheld tool, utensil, weapon, glass, document, or mutable item meant for a character to hold, manipulate, cook, or sabotage (`wooden rolling pin, chef knife, electric hand mixer, soup ladle, pizza cutter, sword, wine glass, raw ingredient being worked on`) belongs to the **Character (`[subject]:` / `[prop]:` / `Shot 1..N`)**, **NEVER to the Location (`[context]:`)**!
     * **Root Cause of the Duplicate-Prop Bug**: Everything listed inside `[context]:` under `fully_preserved` is treated by the AI video generator as permanent static set-dressing glued to the room/table. If a character's utensil or interactive prop is listed in `[context]:` AND also held/used by the character in `[subject]:` or `Shot 1..N`, the AI keeps the static copy glued to the table while spawning a second copy in the character's hand!
     * **Execution Rule**: Keep `[context]:` 100% pure location architecture and fixed furniture matching `<<<Image 1>>>`. Bind the character's initial `00:00` tool/item directly to the character in `[subject]:` (`gripping his single wooden rolling pin over the raw pizza dough`), and when switching to a new handheld tool in a later shot, explicitly release the first tool (`Having set his [Tool A] aside, [Name] uses his [Tool B]...`).
3. **`[subject]:` (Proper Character Names Only, 4-Layer Gender & Hand/Limb Anatomy Lock, `fully_preserved` Identity + Motion-Scope Lock, Gender-Calibrated Skin/Hands/Makeup Sub-Lock, Zero-Costume/Zero-Age & Initial $t=0.0\text{s}$ Anchor)**:
   - **Line 1 — Identity, Explicit Gender, Hand/Limb Proportions & Motion-Scope Lock (`Adaptive after semicolon ;` — Include `makeup` for Female; Omit `makeup` for Male & `< 18` Minors)**:
     * **Female (`Nữ giới` — Locks `same female face, slender feminine body proportions, delicate wrists, long tapering fingers` + `A graceful woman`)**:
       `[Proper_Name] <<<Image 2>>> (fully_preserved - same female face, slender feminine body proportions, delicate wrists, long tapering fingers, hair color, makeup and outfit throughout; only her head, eyes, mouth and expressions move.): A graceful woman [Initial 3D architectural anchor and posture], [initial hand/prop contact state at 00:00], [eyeline toward counterpart or landmark] — the only [Proper_Name] in frame.`
     * **Male (`Nam giới` — Locks `same male face, masculine body proportions, broad shoulders, well-defined masculine hands` + `A composed man`; Omit `makeup`)**:
       `[Proper_Name] <<<Image 3>>> (fully_preserved - same male face, masculine body proportions, broad shoulders, well-defined masculine hands, hair color and outfit throughout; only his head, eyes, mouth and expressions move.): A composed man [Initial 3D architectural anchor and posture], [initial hand/prop contact state at 00:00], [eyeline toward counterpart or landmark] — the only [Proper_Name] in frame.`
     * *(Motion-Scope Adaptation after `;`: Use `; only her/his head, eyes, mouth and expressions move.` when torso/hands remain anchored; use `; only her/his head, eyes, mouth, hands and expressions move.` when hands manipulate a prop; use `; natural head, eye, expression, hand and body movement.` when sprinting, fighting, or moving across the space).*
   - **Line 2 — Gender- & Aesthetic-Calibrated Skin, Hands & Makeup Sub-Lock (`[Proper_Name]'s skin, hands and makeup:` for Female vs. `[Proper_Name]'s skin and hands:` for Male)**:
     Immediately below each character's main `[subject]:` line, declare their skin, hand-anatomy, and makeup preservation sub-line matched to the reference image's aesthetic school (and in any close-up hand shot inside `Shot 1..N`, always qualify hands as `[Name]'s slender feminine hands with delicate wrists and long tapering fingers` for Female or `[Name]'s strong well-defined masculine hands` for Male so close-up hand inserts never default to rough masculine hands):
     * **4 Female Skin, Hands & Makeup Schools (`[Proper_Name]'s skin, hands and makeup: fully_preserved - ...`)**:
       - **School F1 (`Douyin Jiejie / High-Fashion Asian Glam`)**: `[Name]'s skin, hands and makeup: fully_preserved - flawless porcelain velvet-matte skin across her face, neck, arms, and slender feminine hands, with delicate wrists, long tapering fingers, clean manicured nails, soft rosy blush on the cheeks and nose tip, crisp wispy eyelashes, natural watery eye reflection, and soft gradient rose lips; no rough masculine hands, no thick knuckles, no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
       - **School F2 (`K-Drama Clean Satin-Matte Natural Glow`)**: `[Name]'s skin, hands and makeup: fully_preserved - clean smooth satin-matte skin across her face, neck, arms, and slender feminine hands, with delicate wrists, long tapering fingers, a subtle natural warm flush, delicate crisp eyelashes, clear moist eyes, and soft coral-pink tinted lips; no rough masculine hands, no thick knuckles, no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
       - **School F3 (`Classical / Xianxia Jade-Porcelain`)**: `[Name]'s skin, hands and makeup: fully_preserved - flawless jade-porcelain matte skin across her face, neck, and slender feminine hands, with delicate wrists, long tapering fingers, refined classical eye definition, crisp eyelashes, luminous moist eyes, and classic vermilion-rose lips; no rough masculine hands, no thick knuckles, no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
       - **School F4 (`Grounded Western / Realistic Cinema Natural Matte`)**: `[Name]'s skin, hands and makeup: fully_preserved - real unretouched dry matte skin across her face, neck, and slender feminine hands, with delicate wrists, long tapering fingers, understated makeup, crisp individual eyelashes, natural moisture in her eyes, and soft natural lips; no rough masculine hands, no thick knuckles, no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
     * **3 Male Skin & Hands Schools (`[Proper_Name]'s skin and hands: fully_preserved - ...` — strictly NO `and makeup`, NO `blush`, NO `lip gloss`; locks `natural matte lips`)**:
       - **School M1 (`Asian Male Lead / CEO Clean Velvet-Matte`)**: `[Name]'s skin and hands: fully_preserved - clean smooth velvet-matte masculine skin across his face, jawline, and strong well-defined masculine hands, with crisp eyebrows and eyelashes, natural moisture in his eyes, and natural healthy matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
       - **School M2 (`Grounded Masculine Dry Matte`)**: `[Name]'s skin and hands: fully_preserved - real unretouched dry matte masculine skin across his face, jawline, and strong well-defined masculine hands, with natural fine pores, crisp eyebrows and eyelashes, natural moisture in his eyes, and natural matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
       - **School M3 (`Rugged Warrior / Mature Patriarch Matte`)**: `[Name]'s skin and hands: fully_preserved - rugged dry matte masculine skin across his face and strong masculine hands, preserving natural facial lines and texture, crisp eyebrows, clear natural eye moisture, and natural matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
     * **3 Animation Skin, Hands & Shader Schools (`A1–A3` — Mandatory When `Style:` Is Animation so `Style:` and `[subject]:` Never Conflict)**:
       - **School A1 (`3D Semi-Real CGI / Unreal Engine 5 / 3D Donghua`)**:
         * *Female*: `[Name]'s skin, hands and makeup: fully_preserved - smooth 3D satin-matte skin shader across her face, neck, and slender feminine hands with delicate wrists and long tapering fingers, soft subsurface scattering, delicate rosy blush, crisp 3D eyelashes, luminous expressive eyes, and soft gradient lips; no rough masculine hands, no glossy plastic doll sheen, no oily specular glare, not waxy.`
         * *Male*: `[Name]'s skin and hands: fully_preserved - clean 3D satin-matte masculine skin shader across his face, sculpted jawline, and strong well-defined masculine hands, with natural subsurface scattering, crisp eyebrows and eyelashes, clear expressive eyes, and natural matte lips; no glossy plastic doll sheen, no oily specular glare, not waxy.`
       - **School A2 (`3D Stylized Pixar / Disney Animation`)**:
         * *Female*: `[Name]'s skin, hands and makeup: fully_preserved - soft stylized 3D velvet-matte skin across her face and slender feminine hands with a warm subsurface glow, gentle rosy cheeks, crisp stylized eyelashes, expressive glossy eyes, and clean soft lips; no rough masculine hands, no hard plastic toy shine, no greasy glare, no photorealistic rough pores.`
         * *Male*: `[Name]'s skin and hands: fully_preserved - soft stylized 3D matte skin across his face and clean masculine hands with a warm subsurface glow, clean sculpted features, expressive eyes, and natural matte lips; no hard plastic toy shine, no greasy glare, no photorealistic rough pores.`
       - **School A3 (`2D Anime / Manga / Webtoon / Ghibli Cel-Shaded`)**:
         * *Female*: `[Name]'s skin, hands and makeup: fully_preserved - clean 2D cel-shaded skin tones across her face and slender feminine hands with crisp hand-drawn line art, soft anime cheek blush, sharp expressive anime eyes with crisp catchlights, and clean tinted lips; no rough masculine hands, no 3D plastic shading, no photorealistic pores, no smudged linework.`
         * *Male*: `[Name]'s skin and hands: fully_preserved - clean 2D cel-shaded masculine skin tones across his face and well-defined masculine hands with crisp hand-drawn jaw and facial line art, sharp expressive anime eyes, and clean natural lips; no 3D plastic shading, no photorealistic pores, no smudged linework.`
     * **Minors (`< 18` years old — Gate 3F)**: `[Name]'s skin: fully_preserved - clean natural matte skin throughout; no oily shine, not plastic, not waxy.`
   - Always use fixed **Proper Names** (`Bradley`, `Harold`, `Elena`, `Dante`, `Kael`, `Martha`) as subject headers — never standalone generic labels (`Woman:`, `Man:`, `the father:`).
4. **`[prop]:` & End-to-End Two-Tier Prop / Weapon Consistency Protocol (`Stage 1 ➔ Stage 2 setting.html ➔ Stage 3 Rough Script ➔ Stage 4 [prop]: <<<Image X>>>`)**:
   - **Tier 1 — Signature Hero Props, Weapons & Key Artifacts (`Mandatory 16:9 4-View Isolated Prop Sheet in setting.html` + Dedicated `[prop]: <<<Image X>>>` Header)**:
     * **What Qualifies as Tier 1**: Any signature weapon (sword, dagger, spear, firearm, talisman, chef knife/cleaver), family/imperial heirloom (jade seal, brass keyring, pendant), or decisive forensic/legal artifact (transfer contract, ledger) that **(a) recurs across multiple scenes/episodes**, OR **(b) is featured in a macro close-up reveal**, OR **(c) undergoes a 3-state physical transformation (`State 0 Intact ➔ State 1 Activated/Cracked ➔ State 2 Shattered/Reforged`)**.
     * **Format in Code Block 1 (`[prop]:` Block — Zero Redundant Shape/Material Re-Description Inside Parenthetical)**:
       `[Canonical Prop/Weapon Name] <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): [Exact 00:00 resting placement OR character hand-grip state (e.g., gripped firmly in Kael's right hand while his left hand remains empty)] — the only [Canonical Prop/Weapon Name] in frame.`
   - **Tier 2 — Everyday Single-Scene Handheld Items (`Zero Image Sheet` | Pure Rich Text)**:
     * Common single-use items (`crystal red wine glass`, `ceramic teacup`, `smartphone`) that do not require cross-scene macro design lock. Integrated directly into `[context]:` and `[subject]:` initial hand/table states without a separate `<<<Image X>>>` sheet or `[prop]:` block.

### 2.7 Zero-Age & Zero-Costume Law, `fully_preserved` Meta-Token Exemption & Minor Protection Protocol
- **Strict Zero-Age, Zero-Costume & Single Vocal-Timbre Tag Law in Video Prompts (`Gates 3A & 3E`)**:
  * **STRICTLY ZERO specific clothing/garment words (`in a black leather jacket`, `in a dark suit`, `skirt`, `dress`, `coat`) and ZERO numeric ages or specific hair/beard color words (`32-year-old`, `young blonde`, `silver-bearded`, `aged weathered hand`) anywhere in `[subject]:` or `Shot 1..N`!** *(Note: The generic preservation meta-tokens `same face, hair color, makeup and outfit throughout` inside `(fully_preserved - ...)` are mandatory identity-lock tokens, never specific appearance descriptions).*
  * **Expressive Vocal-Behavior Tag & Native Exclamation Trigger (`Laws D2 & D3` — Zero Musical Register Jargon `alto/baritone/tenor/soprano`)**: Purge dry musical register labels and encode active vocal behavior + delivery tone inside **ONE single compact parenthetical immediately after `[Proper_Name]`**, opening emotional/comedic/confrontational lines with a **Native Biological Vocal Interjection**:
    - *Female / Male Examples*: `Elena (expressive female voice, scoffing playfully in a suspicious teasing tone): "Huh?... Why is your wallet empty, honey?"` · `Bradley (expressive male voice, chuckling smugly in a warm overly polite tone): "Hah... Rest easy, Dad. The company is safe."` · `Harold (expressive male voice, speaking with calm icy authority in a low unhurried tone): "Hmm... Then why sell Warehouse Four?"`
  * **Context- & Episode-Driven Wardrobe Evolution (`Trang Phục Thay Đổi Theo Tập & Bối Cảnh: -home / -work / -date / -outing`), Adult Female Hourglass & High-Fashion Dress Law (`Setting Gate 3C`) & 100% Standalone Prompt Law (`Setting Gate 3D`)**: In `setting.html` (`Section 2 #cast` & `Section 3 #modelsheets`), characters lock 100% Invariant Identity DNA while defining Context-Matched Outfit Variants (`[name]-home.jpg`, `[name]-work.jpg`, `[name]-date.jpg`, `[name]-outing.jpg`). Adult females (`>= 18` years old — `Setting Gate 3C`) are designed in `setting.html` with 8-head high-fashion hourglass proportions and flattering context-matched dresses, and every outfit filename in `Section 2 (#cast)` has its own standalone 16:9 4-Figure Turnaround Prompt in `Section 3 (#modelsheets)` (`Setting Gate 3D`).
- **Minor Protection Protocol (Gate 3F & Setting Gate 3B; Pillar 4 §[10d])**: Under-18 characters carry their true integer age and developmental band (`Band I: 0–3`, `Band II: 4–12`, `Band III: 13–17`), are registered in `project_rules.json` → `"minor_characters"`, use `(fully_preserved - same face, hair color and outfit throughout; only her/his head, eyes, mouth and expressions move.)` (omitting `makeup`), use Minor-Safe Model Sheet `Mẫu 0B`, and are strictly protected from any sexualization, violence, abuse, chases, or physical danger.

### 2.8 3D Spatial Anchoring, Selective Face Obscuration & Empty-Hand Lock
- **Observable Architectural Anchoring (Gate 3H)**: Anchor characters to 3D physical landmarks (`Seated at the head chair in front of the marble fireplace`). Frame-edge labels (`frame-left`, `screen-right`) inside `[subject]:` and raw Cartesian coordinates (`X: +0.8m`) anywhere in a deliverable are strictly prohibited.
- **Selective Face Obscuration (Anti-Face-Blending & Mystery Booster)**: Actively use partial-face and silhouette shots (`The camera avoids [Name]'s full face, showing only [Name]'s lower face, jawline, firm mouth, and index finger...` or `showing only his back and shoulders in silhouette`) to heighten dramatic intrigue and prevent multi-character face-blending.
- **Empty-Hand Anti-Glitch Lock**: Whenever an unarmed character or hunter stands or moves empty-handed in a tense/action shot, include `(No objects should appear in the character's hands)` so the AI never hallucinates random objects.

### 2.9 Narrative Depth, Anti-Shallow Script Mandate, 5 Scene Action Structures & Selective Subversion Toolkit
To permanently eradicate shallow, predictable, or monotonous scripts (`"lỗi kịch bản nông, thiếu chiều sâu hoặc lặp công thức một màu"`), every concept (`Stage 0`), blueprint (`Stage 1`), world bible (`Stage 2`), and screenplay (`Stage 3`) MUST enforce the **6 Root-Cause Depth Laws (`0-creative-doctrine.md` §1.2)** PLUS the **5 Hollywood Scene Action Structures (`0b-temporal-camera-grammar.md` §1.1)** and **Selective Subversion Toolkit**:
1. **The 3-Layer Stakes & Zero-Triviality Law**: Lock **External Stakes** (concrete goal + ticking clock), **Internal Psychological Stakes** (`Wound ➔ Lie` under threat), and **Philosophical/Moral Stakes** (two competing human truths).
2. **The 5 Scene Action Structures Across the 4-Stage Episode Symphony (`Never Force Every Scene Into One Formula`)**:
   - Weave 5 distinct scene structures across each episode with **Rhythmic Contrast (`Compress ↔ Release`)**: **(1) Opening / Atmospheric Hook Scene** (`In Medias Res Motion ➔ Anomaly ➔ Curiosity Hook`), **(2) Storytelling / Narrative / `V.O.` Scene** (`Visual Emotion First ➔ Vocal/Inner Thought on Ocular Shift ➔ Tactile Settle`), **(3) Dialogue / Banter / Confrontation Scene** (`Opening Probe ➔ Counter-Action on Target Axis ➔ Checkmate Turn ➔ Wordless Payoff Button`), **(4) Clue Discovery / Micro-Visual Twist Scene** (`Normal Facade ➔ Macro/Close-Up Tactile Insert ➔ Attitude Reversal`), and **(5) High-Velocity Action / Chase / Combat Scene (`@CombatDirector`)** (`Tension Ignition ➔ Pure Kinetic Tracking [0 dialogue] ➔ Hard Stop/VFX ➔ Dominance & Fallout`).
3. **Subversion Tool 1 — The Mask & Role-Reversal Curve (Applied to Confrontation & Twist Scenes)**:
   - In confrontation and twist scenes, progress from **False Calm / Social Mask** ➔ **The Crack / Micro-Trigger** ➔ **Role Reversal / Double Twist**.
4. **Subversion Tool 2 — Micro-Visual Reveal Over Verbal Exposition (`Show, Don't Tell`)**:
   - Strictly ban characters explaining their secret scheme, identity, or power in dialogue. Reveal hidden truths through **1 sharp close-up visual detail** (*two sharp fangs flashing during an embrace*, *black-painted nails revealed while unwinding white hand wraps*, *faint pale red ancient runes glowing beneath a runner's feet*, *an index finger tapping twice on a tarnished brass keyring blocking a contract*).
5. **Subversion Tool 3 — Calm Understatement Dialogue (`2–6 Words` Checkmate Line)**:
   - At decisive power reversals, the dominant/authority character speaks a **short, calm, understated line (`2–6 words`)** (*`"I'm sorry."`*, *`"Miss, you seem lost."`*, *`"Because you secretly sold Warehouse Four."`*).
6. **Subversion Tool 4 — 1–2 Active Characters per Shot Window & Platform Safety**:
   - Stage scenes so that at any given shot window (`Shot 1..N`), only **`1–2` characters** interact directly in frame. **Zero gore and zero graphic/on-screen death are Hard Constraints**; zero fatalities and a positive ending are the default `ending_mode` / `fatality_policy`, which the user may change per project (e.g., an off-screen death in a thriller, a bittersweet ending in a tragedy).
   - **Selectivity rule**: Tools 1–3 are a menu chosen from each scene's Intent Card, not a formula. Never give two consecutive confrontation scenes the same Mask ➔ Crack ➔ Reversal shape or the same 2–6-word checkmate.

### 2.10 Single-HTML Resource Law (`setting.html` Only) & 100% Interactive Step-by-Step Visual Execution
1. **Single-HTML Resource Rule (`Chỉ xuất duy nhất file setting.html — Bỏ toàn bộ file tap-1.html ... tap-N.html`)**:
   - The system generates **ONLY ONE HTML file per project: `output/<slug>/setting.html`** at Stage 2 so the user can prepare all pre-production visual resources (Character 16:9 Model Sheets, Tier-1 Hero Prop Sheets, and Location 2×2 Grids).
   - **Strictly DO NOT generate `tap-1.html`, `tap-2.html`, or `tap-N.html` files, and DO NOT use batch episode compilation (`mode-batch`).**
   - **Allowed working file (not a deliverable)**: after `CP3b`-ready Pass B, the approved chat script is saved verbatim as Markdown `output/<slug>/ep-NN-script.md` so `engine/screenplay_audit.py` can audit it (§8.4) and the next episode can be checked for repetition. It is never an HTML file and never batches more than one episode. Likewise each approved Stage 4 scene prompt is saved as `output/<slug>/prompts/ep-NN-scene-KK.md` and audited by `engine/prompt_audit.py` (§9.3).
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
     * **⚡ High-Motion Model Flag (`Seedance` Routing)**: Any `15.0s` scene (or `10.0s` high-motion action/chase/ambush/combat scene) MUST be marked **`[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s · @CombatDirector]`** and compiled by `@CombatDirector` with the shot topology chosen by intent (`1–2` long-take · `3–5` exchange · `6–9` rapid-cut — `0c` §1).

### 2.11 Summary Matrix: Hard Constraints vs. Craft Defaults vs. Project Rules

| Rule Category | Enforcement | Canonical Scope |
|---|---|---|
| **Hard Constraints** *(Never break; enforced by automated Python gates & Pre-Flight Linter)* | **Blocking Error** (`setting_audit_suite.py` & Pre-Flight Linter) | • **Story Depth Anchors (`Gate 2B`)**: Tier 1 Series Core, 6-Layer Character Psychology, 12-Row Story Spine and Tier 1 Voice Profiles (`Blind Voice Test`) exist before scenes are written; Stage 3 scripts pass the Engagement Scorecard (§8.4).<br>• **Clip Duration, Dynamic Storyboard Pacing & Agent Routing (`Gate 3M`)**: **`10.0s` (`1–4 Shots/Turns`) & `15.0s` (`1 Shared Fixed-Camera Header with 3–4 Turns in Mode D1-A` OR `3–4 Cuts in Mode D1-B/D1-C`) for Dialogue/Drama/Sitcom scenes (`@Director`)** and **`15.0s` (`Flexible Topology: 1–2 Shot Inertial Long-Take ↔ 3–5 Shot Asymmetric Exchange ↔ 6–9 Shot Rapid-Cut Blitz`) Reserved Exclusively for High-Motion Action/Chase/Ambush/Combat/Rapid-Cut Montage scenes (`@CombatDirector` `[⚡ SEEDANCE · 15.0s]`)**; every clip starts at `00:00`.<br>• **Double-Lock `fully_preserved` Reference Fidelity, 4-Layer Gender & Hand/Limb Anatomy Lock, Skin/Makeup Sub-Lock & Single `<<<Image X>>>` Declaration Law (`Gates 3J, 3K, 3L`)**: Declare `<<<Image X>>>` **ONLY ONCE** inside `[context]:`, `[subject]:`, and `[prop]:`, immediately followed by the explicit `(fully_preserved - same female/male face, slender feminine / masculine body proportions...)` lock parenthetical + Line 2 `<Name>'s skin, hands (and makeup): fully_preserved - ...`; **strictly NEVER repeat `<<<Image X>>>` inside `Shot 1..N`**; close with the `Strict visual consistency: ...` footer.<br>• **Zero-Costume, Zero-Age & Expressive Vocal-Behavior Tag Law (`Laws D2 & D3` · `Gates 3A, 3E`)**: Strictly **ZERO specific clothing/garment words** (`jacket`, `suit`, `skirt`, `dress`), **ZERO numeric ages or specific hair/beard words** (`32-year-old`, `young`, `blonde`, `silver-bearded`), and **ZERO dry musical register terms (`alto`, `baritone`, `tenor`, `soprano`)** anywhere in the prompt; encode vocal behavior & delivery tone inside **ONE single compact parenthetical (`[Proper_Name] (expressive female/male voice, [vocal behavior] in a [tone]): "[Interjection]! ..."`)**.<br>• **1–2 Short Natural Sentences per Shot/Turn (`Gate 3R`)**: `12–30 words` per shot (`Mode D1-B/C`) or per `(00:XX-00:YY)` turn under a single shared fixed-camera header (`Mode D1-A`) expressing 1 clear state transition `A ➔ B`; strictly zero `→` arrows.<br>• **Minor Protection Protocol (`Gate 3F` & `Setting Gate 3B`)**: Truthful age/band in `setting.html`, zero sexual/body/violence lexicon, `Mẫu 0B` sheets.<br>• **The 6 Golden Dialogue Laws (`Law D1–D6` · `Gates 4, 4B, 4G, 4H`)**: (`D1`) Lock `static camera` across continuous dialogue (`Mode D1-A` Single Shared Fixed-Camera Header `Shot 1 (00:00-00:10/15)` + `(00:XX-00:YY)` turns vs. `Mode D1-B` Multi-Cut Static Scale Escalation); (`D2 & D3`) Open emotional/comedic/confrontational lines with native vocal interjections and expressive vocal-behavior tags; (`D4`) Spoken turns/shots sized to `3.2s–4.5s` (`natural real-time speed`); (`D5`) Final turn/shot obeys either **Mode 1 (`0 spoken words` in final `2.0s–3.0s` window)** OR **Mode 2 (`100%-Dialogue Ping-Pong` with mandatory `0.5s–1.0s` [`~0.8s`] silent closed-lip tail buffer)**; (`D6`) 4-Point Cross-Scene Dialogue & Posture Handover (`~1.2s` Golden Breath Bridge, 100% `[subject]:` posture inheritance, 180° axis flip, and keyword baton relay).<br>• **Platform Safety (§2.9)**: zero gore, zero graphic violence or on-screen death, and the Minor Protection Protocol.<br>• **Heart & Value North Star (`0d`)**: Value Card in every Spine (`VALUE · HEART · TAKEAWAY · SHADOW`), the Dignity & Value Firewall (no humiliation, cruelty or revenge as the payoff; a door left open; every ending leaves a light), and the Heart & Value Scorecard `≥ 6/8` with no `0` at `CP0`, `CP1`, `CP3a`, `CP3b` (`screenplay_audit.py` blocks a script without it). |
| **Craft Defaults** *(Use by default; override when dramatic intent requires via `BREAK: <default> — <reason>`)* | **Creative Review & Non-Blocking Warnings (`W1–W11`)** | • **Selective Subversion Toolkit (§2.9)**: *Mask & Role-Reversal Curve*, *Micro-Visual Reveal over Exposition*, *Calm Understatement `2–6w` Line*, *Curiosity Gap* — chosen per scene intent, never stamped onto every confrontation.<br>• **Ending Mode & Fatality Policy (§2.9)**: earned positive ending and zero fatalities by default; a bittersweet/tragic ending or an off-screen death is allowed when the user chooses it or the genre needs it (thriller, horror, war, tragedy), recorded in `project_rules.json` (`ending_mode`, `fatality_policy`).<br>• **4-Beat Episode Allocation (§8.1)**: `Open/Hook 15–20% (in Scenes 1–2) ➔ Develop 40–50% ➔ Climax 20–25% ➔ Close 10%` across `12–18 scenes` (~3 min/ep; default `10.0s` `@Director`, with `15.0s` routed to `@CombatDirector` for Action/Combat).<br>• **Selective Face Obscuration & Off-Screen `L-Cut` Dialogue**: Use partial-face/silhouette shots (`avoids full face, showing only jawline and hand...`) and off-screen `L-Cut` lines over `2s` prop inserts.<br>• **Inter-Scene Causality**: Every pair of scenes connects via `"Therefore (Vì vậy)"` or `"But (Nhưng)"` — never `"And then (Và rồi)"`. |
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
| Episode N structure approved (`CP3a`), prose not yet written | **Stage 3 Pass B** (prose, dialogue, ledgers; save `ep-NN-script.md` + audit) |
| Episode N Rough Script approved in chat (`CP3b`) | **Stage 4** (Interactive Scene-by-Scene Prompt Production & Visual Cross-Check in chat: `Scene 01 ➔ Scene 02...`) |
| All Episode Scenes completed in chat (`CP4`) | **Stage 5** (Interactive Distribution & SEO Packaging + Registry Finalize) |
| `output/<slug>/ep-NN-script.md` exists without the Pass B prose blocks | **Stage 3 Pass B** of Episode NN (structure already approved at `CP3a`) |
| `ep-NN-script.md` complete and `prompts/ep-NN-scene-KK.md` saved up to scene K | **Stage 4, Scene K+1** of Episode NN (re-read Scene K's Code Block 2 handover) |
| All scenes of the last episode saved, no `seo-package.md` | **Stage 5** packaging |
| `seo-package.md` saved, episode published, no `performance_log` entry | Ask for the analytics and run the **feedback loop** (§10.1) |
| Revision requested on a specific scene or resource | **Revision Mode** (Cross-check & update the targeted scene prompt in chat or `setting.html`) |

Detect the state from these files first (they are the source of truth over chat memory); report the detected state in one concise line and proceed. Never overwrite approved deliverables unless requested.

### K1 — History Registry Scan (14-Axis Anti-Repetition)
Read `history-registry.json`, ensure zero collision across all 14 axes, and read the latest `performance_log` lessons (§10.1) so new concepts favour what actually retained viewers:
1–2. Character Names (`EN` / `VN`) | 3. Narrative Polarity | 4. Story Tracks (`A–H`) | 5. Symbolic Prop Groups | 6. Hook Archetypes (`#1–#12`) | 7. Visual Styles | 8. Genres & Arenas | 9. Escalation Variants | 10. Twist Archetypes (`TW-01..20`) | 11. Cliffhanger Archetypes (`C1–C7`) | 12. Stacked Tropes | 13. Diurnal Lighting | 14. Narrative Mode.

### K2 — Request Classification & Genre Routing
| User Input Signal | Routing Action |
|---|---|
| Broad topic or missing $\ge 2$ of `{character, arena, core conflict, genre}` | **Stage 0**: Pitch 5 distinct high-depth concepts (`✋ CP0`). |
| Concrete story premise provided | Skip Stage 0 ➔ Start directly at **Stage 1: Story Spine & Master Narrative Blueprint (`✋ CP1`)**. |
| Social / Family Drama (`"drama"`, `"gia đình"`, `"thừa kế"`) | Mount [`engine/genres/drama.md`](file:///d:/Project/Sven/engine/genres/drama.md) (`Two Honest Sides`, `Internal Metamorphosis`, `Earned Ending`). |
| Healing / Slice-of-Life (`"chữa lành"`, `"đời thường"`, `"nhẹ nhàng"`) | Mount [`engine/genres/healing.md`](file:///d:/Project/Sven/engine/genres/healing.md) (`Kishōtenketsu`, no villains, hands-at-work scenes). |
| Viral Microdrama (`"microdrama"`, `"phim tổng tài"`, `"phim ngắn kịch tính"`) | Mount [`engine/genres/microdrama.md`](file:///d:/Project/Sven/engine/genres/microdrama.md) (`13-Beat Retention Curve`, `Status Proxies`, `Staccato ≤12w`). |
| Action / Martial Arts / Chase / Xianxia (`"hành động"`, `"võ thuật"`, `"kiếm hiệp"`) | Mount [`engine/genres/action.md`](file:///d:/Project/Sven/engine/genres/action.md) + [`@CombatDirector`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md) (`3-Zone 40/40/20`, `2.3x–10x`, zero `→` arrows in prompts). |
| Sitcom / Comedy (`"sitcom"`, `"hài tình huống"`, `"học đường vui nhộn"`) | Mount [`engine/genres/sitcom.md`](file:///d:/Project/Sven/engine/genres/sitcom.md) (`Amplified Stakes`, `Snowball Lie`, `Status Quo Reset`, `Scene Buttons`). |
| Thriller / Mystery / Folk Suspense (`"trinh thám"`, `"phá án"`, `"giật gân"`, `"linh dị"`) | Mount [`engine/genres/thriller.md`](file:///d:/Project/Sven/engine/genres/thriller.md) (`Knowledge Matrix Switch`, `≥ 2 Fair-Play Visual Clues`, `Option C Culprit`). |
| Fantasy / Time-Travel / Rebirth (`"xuyên không"`, `"trùng sinh"`, `"tu tiên"`, `"huyền huyễn"`) | Mount [`engine/genres/fantasy.md`](file:///d:/Project/Sven/engine/genres/fantasy.md) (`World-Law Contract`, `3-State Relic`, `TH3`). |
| Sci-Fi / AI / Future Tech / Post-Apocalypse (`"khoa học viễn tưởng"`, `"sci-fi"`, `"tương lai"`, `"AI"`) | Mount [`engine/genres/scifi.md`](file:///d:/Project/Sven/engine/genres/scifi.md) (`3 Hard World Rules`, `rule planted before payoff`). |
| Horror / Folk Dread (`"kinh dị"`, `"ma"`, `"rùng rợn"`, `"tâm linh"`) | Mount [`engine/genres/horror.md`](file:///d:/Project/Sven/engine/genres/horror.md) (`Rules of the haunting`, `build ➔ false release ➔ shock`, zero gore). |
| Romance (`"ngôn tình"`, `"tình cảm"`, `"lãng mạn"`, `"hợp đồng hôn nhân"`) | Mount [`engine/genres/romance.md`](file:///d:/Project/Sven/engine/genres/romance.md) (`two Lies`, `distance changes every episode`, idiot-plot test). |
| Lyrics or Music Video request | Mount Pillar 3 Music Video Architecture. |
| Buddha Protagonist or Statue Veneration trigger | Activate Special Spiritual Modes (§5.3). |

### K2b — Request Router (Which Agent, Which Pipeline, Which First Gate)
K2 picks the **genre module**; K2b picks the **agent and pipeline**. Route every request here first; when a request matches two rows, the more specific row wins (e.g., "Roblox series" ➔ RobloxDirector, not the film pipeline).

| Request signal | Agent | Pipeline | First gate | Load before writing |
|---|---|---|---|---|
| A film, series, episode, story or script (`"phim"`, `"series"`, `"kịch bản"`, `"tập"`, `"ý tưởng phim"`) | `@Screenwriter` ➔ `@Director` / `@CombatDirector` | Stages 0–5 (this file) | `✋ CP0` (or `✋ CP1` with a concrete premise) | `AGENT.md` §3 stage map |
| One scene or video prompt without the full pipeline (`"viết prompt cảnh"`, `"prompt video"`) | `@Director` (dialogue/drama) or `@CombatDirector` (kinetic) | Standalone Stage 4 shortcut | Scene prompt saved + `prompt_audit.py` | `AGENTS.md` §1.3 shortcut reads |
| Fight, chase, rescue, sport, high-speed craft (`"đánh nhau"`, `"rượt đuổi"`, `"giao đấu"`, `"nấu ăn tốc độ cao"`) | `@CombatDirector` | Stage 4 mode (inside a series) or standalone | Combat Intent Card ➔ prompt audit | `combat-director/SKILL.md` |
| Product ad, brand TVC, performance ad, or product review (`"quảng cáo sản phẩm"`, `"video quảng cáo"`, `"tvc"`, `"10s 6 shot"`, `"review sản phẩm"`, `"video review"`, `"product review"`) | `@CommercialDirector` | Standalone commercial pipeline: **Mode 1** (`10s=6 / 15s=9` fast-action `C1–C6` + CTA) OR **Mode 2** (`40s–60s` multi-clip pain-to-purchase review: decoupled V.O. + 100% silent acting) | Mode 1: Archetype + CTA ➔ prompt audit · Mode 2: `✋ GATE RV1` (pain/hooks) ➔ `✋ GATE RV2` (dual-track script) ➔ 1 clip at a time | `.agents/COMMERCIAL_DIRECTOR.md` |
| Character reference sheet, outfit change, keyframe, still (`"tạo ảnh nhân vật"`, `"ảnh tham chiếu"`, `"keyframe"`) | `@PhotoDirector` | Standalone, or Stage 2 asset prompts inside `setting.html` | Sheet/keyframe template chosen (Iron Law P0) | `2-casting-worldbuilding-specification.md` (`L390–720`) + `.agents/PHOTO_DIRECTOR.md` |
| Storyboard grid or storyboard-to-video (`"storyboard"`, `"lưới 9/12/15/25 shot"`) | `@StoryboardDirector` | Standalone, or a Stage 4 mode | Phase A grid approved before Phase B | `.agents/STORYBOARD_DIRECTOR.md` |
| Swap characters/props/locations in a source video (`<<<Video 1>>>`, `"đổi nhân vật trong video"`) | `@RefVideoDirector` | Standalone (`Mode V1–V4`) | Contact sheet extracted and read first | `.agents/REF_VIDEO_DIRECTOR.md` |
| Roblox film, series, animation, Studio/Blender build, Roblox GFX (`"roblox"`, `"phim roblox"`) | `@RobloxDirector` (Claude Code: the real subagent `.claude/agents/roblox-director.md` for R3–R5) | Its own `R1–R5` pipeline | `✋ GATE R1` | `.agents/ROBLOX_DIRECTOR.md` |
| Titles, thumbnails, descriptions, tags, niche research, analytics (`"seo"`, `"tiêu đề"`, `"thumbnail"`, `"số liệu"`) | `@GrowthArchitect` | Stage 0 support, Stage 5, or standalone; analytics feed `performance_log` (§10.1) | `✋ CP5` (or a direct answer when standalone) | `youtube-growth-architect/SKILL.md` |

**Hand-offs inside the film pipeline** (Stages 2–4): asset prompts for `setting.html` ➔ `@PhotoDirector` templates; a kinetic scene flagged `[⚡ SEEDANCE]` ➔ `@CombatDirector`; an in-episode product or sponsor moment ➔ `@CommercialDirector` writes that one scene; a user request for a storyboard grid of a scene ➔ `@StoryboardDirector`. The scene still follows the episode script, the continuity case (`TH1/TH2/TH3`) and `prompt_audit.py`. Standalone pipelines (Commercial, RefVideo, Roblox) keep their own gates but share `0c`, `3c`, the dialogue laws and the safety rules.

### K3 — Parameter Lock & Interactive Step-by-Step Handshake
Lock project parameters (`Aspect Ratio`, `Visual Style`, `Episode Count`, `Episode Runtime` → `episode_runtime_s` [`0c` §4], `Clip Duration`, `Dialect`, `Ending Mode` → `ending_mode` [positive / bittersweet / tragic; positive by default], `Fatality Policy` → `fatality_policy` [none by default; off-screen allowed on user request]) via `engine/runbooks.json` (`output/<slug>/project_rules.json`) and enforce the **Single-HTML (`setting.html` Only) + 100% Interactive Step-by-Step Execution Mode**:
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
STAGE 3  Episode N Rough Script (Interactive in Chat, 1 Ep) Pass A ──▶ ✋ CP3a · Pass B ──▶ ✋ CP3b
   │     • Pass A: Episode Spine, Retention Map, 1-Line Scene List, Engagement Scorecard ≥ 12/16
   │     • Pass B: Prose + Dialogue + Ledgers → output/<slug>/ep-NN-script.md → screenplay_audit.py
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
   ▼
[🎬 PRODUCTION COMPLETE]
```

> **Checkpoint Rule**: At every `✋ CP0–CP5`, **STOP and wait for user approval**. Accepted commands: `ok` / `continue` (approve and advance), `edit [instructions]` (revise current stage), or stage-specific shortcuts.

---

## §5 — STAGE 0: CONCEPT GENERATION (`✋ CP0`)

> **JIT Load**: `.agents/SCREENWRITER.md` + `0-creative-doctrine.md` (§1.2, §8.1, §9.2).

### 5.1 Anti-Shallow Concept Rules, Market Alignment, Vocation Creativity & Full Multi-Polar Cast
- Generate **5 distinct concepts** differing across arena, conflict architecture, hook archetype (`#1–#12`), and emotional trajectory.
- **Premise Promise & Episode-1 Payoff (`Lời hứa của tiền đề`)**: Every concept states the specific experience it promises the viewer (a status reversal, a fair-play mystery, a forbidden love, a survival gauntlet…) and **what Episode 1 already pays on that promise** (a first mini-payoff, not only setup). A concept whose first episode is pure setup is rejected.
- **Novelty Check (`Khác gì dự án trước`)**: Compare each concept against `history-registry.json` (K1 axes: arena, polarity, hook type, twist code, tropes) and state in one line what is new. Never let the 5 concepts share the same arena or the same engine; at least 2 of the 5 must come from different Genre Engines unless the user locked the genre.
- **Genre-Calibrated Realism**: Each concept obeys its Regime (§2.4). Grounded drama follows `engine/genres/drama.md` §0.2 (real industries, believable money per `0c` §8, real legal friction of the story's country); speculative regimes follow their world-law contracts. Never transplant one regime's furniture (inheritance law, corporate boards) into a concept that does not need it.
- **Zero Real-World Celebrity / Public Figure Name Ban**: Strictly NEVER use names of real-world singers, actors, celebrities, politicians, or famous billionaires (e.g., no `Lâm Chấn Khang`, no `Rockefeller`, `Walton`, `Musk`, `Bezos`, etc.) in any language.
- **Anti-Artisan Cliché & Arena-True High-Caliber Vocations**: Strictly NEVER default characters to repetitive manual/artisan/handicraft/blue-collar trades (*nghệ nhân chế tác, thợ mộc, thợ thủ công, ủ rượu, sửa ống nước, cơ khí*) unless explicitly requested by the user. Vocations must be creative, high-stakes, and calibrated to the story's arena — they give the character leverage inside the conflict (e.g., inheritance drama: *corporate crisis fixer, trust attorney*; thriller: *forensic linguist, insurance fraud investigator*; romance: *wedding-contract negotiator, night-shift ER triage nurse*; sci-fi: *memory-archive auditor*; fantasy: *talisman appraiser*). Never reuse the same vocation set across projects.
- **Deep Multi-Polar Character Web in Stage 0 (Never Sketchy 3-Line Summaries)**: Scale the character ecosystem in each concept to the format quota (`0c` §6: `3–4` Short Film, `5–6` Mini-Series, **`7–9` Full Series**, `10–14` Mega). Present the cast in a **clean, scannable Markdown Table** mapping `A1`, `A2` (`Where A2 Is Right`), and only the **`Tier B` Dual-Tether Satellites the story needs**, each picking a role from the menu (`B-Heart`, `B-Judas`, `B-Guardian`, `B-Blackmailed Accomplice`, `B-Shadow Keymaker`, `B-Arbiter`, or a genre-specific role such as a sitcom foil, a rival suitor, a mentor with a secret) + **`Tier C` Chorus**, including explicit family/relational bindings (`Father/Mother–Child`, `Husband–Wife`, `Siblings`).
- **Clean, Spacious & Readable Presentation**: Present concepts with generous whitespace, structured tables, short scannable lines, and clear visual hierarchy—never dump dense, cramped walls of text.
- **Zero Shallow Fables / Zero Triviality**: Every concept must establish **3-Layer Stakes** (External deadline/loss + Internal Wound/Lie + Moral dilemma), an active protagonist whose flawed choice or costly stand drives the plot, an opponent with a real point of truth (`Where A2 Is Right`), and a planted **Option C Reversal**.
- Resolution must calibrate strictly to the genre (§2.9) and to the project's `ending_mode` / `fatality_policy` (positive, zero-fatality by default).
- **Heart & Value First (`0d`)**: every concept names the positive value its hero will choose at a cost (`VALUE`) and the takeaway a viewer carries home (`TAKEAWAY`), and its premise promise includes the heart it delivers, not only the reversal. Concepts whose payoff is humiliation, cruelty or revenge for its own sake are reshaped into dignity, truth and repair before they are pitched (`0d` §5–§6).

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

🎯 3. LỜI HỨA CỦA TIỀN ĐỀ & TẬP 1 TRẢ GÌ:
   • Người xem đến để được: [trải nghiệm cụ thể — lật kèo địa vị / phá án công bằng / tình yêu cấm đoán / sinh tồn ...]
   • Tập 1 đã trả trước: [mini-payoff cụ thể trong tập 1]
   • Khác gì dự án gần nhất trong registry: [1 dòng]

🎲 4. BẺ GÃY DỰ ĐOÁN (OPTION C REVERSAL) & CHUỖI TWIST ([N] TẬP — phim ngắn: 1 twist chính):
   • Khán giả đoán [Phương án A hoặc B] ➔ Sự thật xảy ra là [Phương án C cài cắm từ đầu]
   • Lực cản 3 tầng & Twist: T1 [TW-xx] ➔ T2 Midpoint [TW-xx] ➔ T3 Climax [TW-xx]

🏛️ 5. HỆ SINH THÁI NHÂN VẬT ĐA CỰC (ĐÚNG QUOTA 0c §6 — CHỈ GIỮ VAI CỐT TRUYỆN CẦN):
   | Vai trò / Tuyến | Nhân vật & Nghề nghiệp (Sáng tạo, xứng tầm Arena) | Quan hệ ràng buộc & Móc xích kép (A1 ⇄ B ⇄ A2) | Động cơ / Vũ khí kịch tính & Twist nắm giữ |
   |---|---|---|---|
   | **A1 (Chính diện)** | [Tên — Nghề nghiệp] | [Quan hệ với A2 & Tuyến B] | [Wound ➔ Lie + Đòn phản công chủ động] |
   | **A2 (Đối đầu)** | [Tên — Nghề nghiệp] | [Quan hệ với A1] | [Mục tiêu + "Điểm A2 hoàn toàn có lý" (Where A2 Is Right)] |
   | **B[n] ([Vai + mã B-01…B-20 + phe, theo bảng quy đổi `2b-character-lines.md` §1 — ví dụ B-Judas = B-01; hoặc vai riêng của thể loại theo `2b` §2])** | [Tên — Nghề nghiệp] | [Móc xích kép A1 ⇄ B ⇄ A2] | [Muốn gì / Bí mật / Chức năng twist] |
   | *(thêm hàng B cho đến đủ quota — phim ngắn thường chỉ 1–2 hàng B)* | | | |
   | **Tuyến C (Chorus linh động)** | [Nhóm phù hợp bối cảnh: hàng xóm / đồng nghiệp / khách quen / đám đông mạng ...] | [Áp lực xã hội quanh A1] | [Đổi chiều thế nào ở kết] |

📦 6. ĐẠO CỤ TRUNG TÂM (WOUND ➔ ECHO PROP) & KẾT CỤC ĐẮT GIÁ:
   • Đạo cụ Tier 1: [Tên đạo cụ] ([Trạng thái Hồi 1] ➔ [Biến đổi 180° ở Kết cục])
   • Cái giá phải trả & Câu hỏi tranh luận: [...]

💗 7. GIÁ TRỊ & ĐIỀU KHÁN GIẢ MANG VỀ (0d §3):
   • Giá trị tích cực (chọn bằng hành động, có cái giá): [...]
   • Khoảnh khắc chạm dự kiến: [chi tiết cụ thể sẽ làm người xem rưng rưng]
   • Điều khán giả mang về (không nhân vật nào nói ra): "[...]"

📊 8. ĐỘ CUỐN Ý TƯỞNG: Hook [ ]/2 · Lời hứa [ ]/2 · Mới lạ [ ]/2 · Cọc cược [ ]/2 · Tranh luận [ ]/2 · Muốn xem tập 2 [ ]/2 = [ ]/12
💗 9. BẢNG CHẤM GIÁ TRỊ — Giá trị [ ]/2 · Khoảnh khắc chạm [ ]/2 · Phẩm giá [ ]/2 · Mang về [ ]/2 = [ ]/8
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.3 Special Narrative Modes
- **🪷 Buddha as Protagonist**: Triggered by explicit request (`"Đức Phật làm nhân vật chính"`). Keeps Buddha as Awakener/Guide across 3 canonical arcs: (1) *Transformation of Destruction (Angulimala)*, (2) *Healing of Grief (Kisa Gotami)*, or (3) *Humbling of Sovereign Pride (Ajatasattu)*.
- **🗿 Buddha Statue Veneration**: Triggered by statue restoration/offering prompts. Applies the 4-Pillar Veneration Framework (Pillar 1 § Statue Veneration Motif Library) where the statue's physical state chain mirrors the protagonist's internal moral restoration.
- **🎵 Music Video (`MV Mode`)**: Maps the 6 narrative beats to song sections (`3% / 12% / 35% / 30% / 12% / 8%` of duration $T$) per Pillar 3.

### 5.4 Concept Engagement Scorecard & ✋ CHECKPOINT 0
Score every concept on **two cards** and show both in its card: the Engagement Scorecard below (`0`, `1` or `2` each; never present a concept below `7 / 12`) and the **Heart & Value Scorecard** (`0d` §8; never below `6 / 8` or with a `0`). Recommend the concept with the best combined score — a gripping concept with no heart is not the winner:

| # | Criterion | 2 points when… |
|---|---|---|
| 1 | **Hook** | the first 3 seconds are a concrete visual anomaly a viewer cannot scroll past |
| 2 | **Premise promise** | the promised experience is specific and Episode 1 already pays part of it |
| 3 | **Novelty** | arena, engine, hook and twist differ from the last projects in `history-registry.json`, and at least 2 clichés are subverted |
| 4 | **Stakes** | all 3 layers (external + clock, internal wound, moral two-sided question) are concrete |
| 5 | **Debate seed** | reasonable viewers would take opposite sides in the comments |
| 6 | **Binge question** | the end of Episode 1 leaves a question the viewer needs answered |

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
9. **Value & Takeaway (`Giá trị & Điều mang về` — `0d` §2–§3)**: the positive value the ending affirms through `A1`'s costly choice (usually `A1`'s Need), the heart moment the finale is built around, the unspoken takeaway, and the `SHADOW` the story depicts without glorifying.
> **Core Rule**: Every episode must serve either the **Central Question** or the **Transformation Arc** — and every episode moves the viewer one step toward the series takeaway. Any episode that advances neither must be cut.

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
4. **Twist-Driven Casting Mandate**: Zero ornamental characters. Every Tier B character holds an explicit plot/twist function (`TW-01..20`), dual relationships (`A1 ⇄ B ⇄ A2`) when A2 is a person, and an independent moral dilemma.
5. **Character Lines (`2b-character-lines.md`)**: use one role vocabulary (`A1` protagonist, `A2` always the antagonistic force, `B# · B-XX · side`, `C` chorus — §0–§1), pick the cast topology for the genre (§2), declare each principal's arc type (§3), and lock **series arc points + the Character Arc Map** (episodes × characters: want, knows, relationship, Lie status, present/absent — §4–§5) at `CP1`. Introduce characters per §6.

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
   - **Engine 2 — Viral Microdrama, CEO, Rebirth & Second Chance (`3-Tier Every-Episode Dignity Reversal Engine`)**: Viewers never wait 4 episodes for a payoff. `Act I (Ep 1)` ends with a **Mandatory First Mini-Reversal** (the overlooked hero's worth glimpsed); **every `Act II` episode** executes an internal `Spring Compression (30%) ➔ Baiting (30%) ➔ In-Episode Dignity Reversal — truth revealed by planted proof, the hero's worth recognized (30%) ➔ Higher Boss Arrival (10%)` loop; `Act III+IV Finale` delivers the public truth, a fair self-caused consequence for the main wrongdoer and **one act of grace** from the hero (`0d` §5–§6; never kneeling, begging or humiliation as the reward shot) (`90% 10s : 10% 15s`).
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

### 6.5 Series Engagement Scorecard & ✋ CHECKPOINT 1
Before `CP1`, score the series blueprint (`0`, `1` or `2` each; pass `≥ 9 / 12` with no `0`) **and** the **Heart & Value Scorecard** for the whole story (`0d` §8; pass `≥ 6 / 8` with no `0`), and show both:

| # | Criterion | 2 points when… |
|---|---|---|
| 1 | **Premise promise** | the logline promises a specific experience (a status reversal, a mystery, a forbidden love…) and Episode 1 already delivers a first taste of it (a mini-payoff, not only setup) |
| 2 | **Central question pull** | one yes/no series question a viewer can repeat after Episode 1, kept open until the finale |
| 3 | **Irreversible escalation** | every episode row in the Tracking Table changes something that cannot go back, and stakes rise episode to episode |
| 4 | **Twist architecture** | the Master Secret has `≥ 3` plants mapped to episodes before its reveal (`~2/3`), plus one Option C nobody is predicting |
| 5 | **Character engine** | `A1` drives the plot through a flawed choice; `A2` is right about something; every Tier B has a want that collides with `A1` |
| 6 | **Rotation** | hook types, twist codes and cliffhanger types vary across episodes (no type twice in a row) and differ from the last projects in `history-registry.json` |

```text
✋ CHECKPOINT 1 — Story Spine (12 Hàng) + Thẻ Giá Trị & Master Narrative Blueprint hoàn tất — Độ cuốn series: [ ]/12 · Giá trị: [ ]/8
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
   - Every `A1`, `A2`, and `Tier B` character appearing in $\ge 2$ scenes receives a dedicated 16:9 Model Sheet Prompt + Double-Lock Mode B Video Reference Snippet (`[Proper_Name] <<<Image Y>>> (fully_preserved - same female/male face, slender feminine body proportions, delicate wrists, long tapering fingers [Female] / masculine body proportions, broad shoulders, well-defined masculine hands [Male], hair color, makeup [Female only; omit makeup for Male] and outfit throughout; only her/his head, eyes, mouth and expressions move.): A graceful woman / A composed man ...` + Line 2 `[Proper_Name]'s skin, hands (and makeup): fully_preserved - ...`).
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
     - **Double-Lock Mode B `[prop]:` Snippet**: `[Canonical Prop/Weapon Name] <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): [Exact 00:00 placement or hand-grip state] — the only [Canonical Prop/Weapon Name] in frame.`
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

## §8 — STAGE 3: EPISODE SCREENPLAY & ROADMAP PHASE B (`✋ CP3a Structure ➔ ✋ CP3b Prose`)

> **JIT Load**: `0b-temporal-camera-grammar.md` + `1-narrative-screenplay-architecture.md` (Part III–VIII) + `0-creative-doctrine.md` (§1–§5). Author **ONE episode screenplay per checkpoint**.

### 8.1 Tier 2, Tier 4 & Tier 5 Episode Architecture (Scene Count & Runtime per `0c-canonical-numbers.md` §4)

#### 1. Tier 2 — Episode Storyline Rules (`Cốt Truyện Mỗi Tập`)
Every episode is **one complete mini-story PLUS one piece of the macro story** (watching a single episode alone still has a clear beginning, middle, and end):
1. **Episode Goal (`Mục tiêu tập`)**: What the character wants to achieve *in this episode* (smaller than the series goal).
2. **Obstacle (`Trở ngại`)**: What blocks them in this episode.
3. **One Main Shift (`Một chuyển biến chính`)**: By the end of the episode, the situation or understanding must differ from the start, changing **at least one thing that can never go back to how it was** (*quan hệ vỡ, bí mật lộ, người rời đi*).
4. **One New Information Layer on the Master Secret (`Một thông tin mới về bí mật lớn`)**: Opens **one new layer only** — never exposing the whole secret early.
4b. **The Crisis Choice (`Lựa chọn khó ở cao trào`)**: The episode turns on **one choice between two goods or two evils** made by `A1` (doctrine §9.1). Build the episode backwards from this choice; luck or a stranger never turns the episode.
5. **4-Beat Episode Structure (`Cấu trúc 4 nhịp`)**:
   - **Open / Hook (`Mở`: `15–20%`, within Scenes 1–2 — never drag out introductions)**
   - **Develop (`Phát triển`: `40–50%`)**
   - **Climax (`Cao trào`: `20–25%`)**
   - **Close (`Kết`: `10%` — cliffhanger or resonant aftermath)**
6. **One Memorable Visual or Prop Detail (`Một chi tiết hình ảnh hoặc đạo cụ đáng nhớ`)**: Used as the connector in Tier 3.
7. **One Heart Moment & One Value Step (`Một khoảnh khắc chạm & một bước giá trị` — `0d` §3–§4)**: at least one planted, specific, restrained moment that moves the viewer (marked `💗` in the scene list), and one step of the series value made visible through a choice. Even a dark episode keeps a seed of hope (`0d` §7).

#### 2. Tier 4 — Per-Scene Rough Prose, 5 Scene Action Structures & Intent-First Routing (`@Director 10.0s & 15.0s` vs. `@CombatDirector 15.0s`)
An episode is divided into the scene count set by its Act Archetype or locked runtime (`0c` §4 — `12–18` scenes only for an opted-in `~3-minute` episode), written in **continuous present-tense prose (without splitting seconds)** before any video prompt is compiled:
- **By Duration, Scene Action Structure & Agent Owner**:
  * **Default `10.0s` Scene (Opening Hooks, Storytelling/`V.O.`, Standard Dialogue, Confrontation & Clue Twists — Routed to `@Director` `[🎭 MODEL TIÊU CHUẨN · 10.0s]`)**: **1 dramatic beat**, **`3–5 sentences` of continuous prose** structured by its **Scene Action Structure** (*Opening Hook*, *Storytelling/V.O.*, *Dialogue/Confrontation*, or *Clue Discovery*), dialogue **`0–2` short sentences** (**`0–22 words total`**).
  * **Extended `15.0s` Dialogue / Sitcom / Climax Showdown Scene (`@Director` `[🎭 MODEL TIÊU CHUẨN · 15.0s]`)**: **`4–6 sentences` of continuous prose** for multi-turn banter or high-voltage boardroom/family showdowns (**`2–4` turns, `18–32 words total`** — `0c` §2).
  * **High-Velocity `15.0s` Action / Chase / Combat Scene (Routed Exclusively to `@CombatDirector` `[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s]`)**: **`5–7 sentences` of continuous kinetic action prose** structured around the **Kinetic Contrast Flow (`Tension Ignition / Snap Freeze ➔ Full-Speed Flight/Pursuit [0 dialogue] ➔ Hard Stop + VFX/Trap [0 dialogue] ➔ Dominance / Checkmate Line ➔ Terminal Fallout [0 dialogue]`)**.
- **Scene Division & Pacing Rules**:
  * **One Job per Scene**: Each scene does **strictly ONE thing**. If a scene requires two purposes, split it into two scenes.
  * **Rhythmic Variety Across the 4-Stage Episode Symphony**: Never allow three consecutive scenes to share the same Scene Action Structure, emotion, tempo, or dialogue density. Include at least one silent/visual or `V.O.` reflective scene per episode.
  * **Mandatory 2-Pass Approval inside Stage 3 (`✋ CP3a` Structure ➔ `✋ CP3b` Prose — §8.3)**:
    1. **Pass A (`CP3a`)**: Episode story, voice profiles, Retention Map and the 1-Line Scene List (`"Địa điểm, ai, làm gì, để làm gì"`, each link verified with **`"Vì vậy (Therefore)"` / `"Nhưng (But)"`**), scored with the Engagement Scorecard (§8.4). **Stop for approval.**
    2. **Pass B (`CP3b`)**: Only after `CP3a` approval, write the continuous rough prose, dialogue and ledgers. Fixing structure at `CP3a` costs one line; fixing it after the prose costs a rewrite.

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
     * Partition every episode into **2–4 (typically 2–3) cohesive Location Sequences** (`0c` §4) (`W11` check), grouping **2–4 consecutive scenes inside the same physical location** before switching to the next location (e.g., `Sequence 1 [Scenes 01–04: Living Room]` ➔ `Sequence 2 [Scenes 05–07: Kitchen]` ➔ `Sequence 3 [Scenes 08–10: Ancestral Courtyard]`).
     * Never ping-pong erratically across different rooms every single 10s scene; clustering consecutive scenes in the same space maximizes **Case 1 Static-Frame Continuation** and builds sustained dramatic pressure.
   - **Optimization Law 2 — Clean Terminal Keyframe Landing (Final-Shot I2V-Ready Pose)**:
     * Every scene screenplay MUST engineer the final shot (or the final `~2.0s` of a single-take clip) so that characters resolve their primary movement into a **Clean Dynamic Landing Pose (Điểm Đỗ Khung Hình Tĩnh Sắc Nét)**: clear orientation, grounded hand/prop contact, and zero wild mid-swing motion blur.
     * This ensures that when the user renders Scene $K$, its terminal frame (`Last Frame @00:10.0 / @00:15.0`) is crisp, well-composed, and immediately usable as the exact `First Frame (00:00.0)` reference image for Scene $K+1$.
   - **Optimization Law 3 — Scene Action Structural Variety & Zero Semantic Repetition**:
     * Each scene focuses on **1 clear structural flow (`Opening Hook`, `Storytelling/V.O.`, `Dialogue/Confrontation`, `Clue Discovery`, or `Action`)**, avoiding repetitive conversational points across consecutive clips.

### 8.3 Canonical Episode Rough Script Template — Two Passes (`✋ CP3a` Structure ➔ `✋ CP3b` Prose)

Stage 3 separates **screenwriting** (scene list + continuous present-tense prose) from **directorial prompting** (Stage 4) and runs in **two approved passes** so structural problems are fixed while they are cheap. All counts and budgets come from `0c-canonical-numbers.md` (§2 dialogue, §3 prose, §4 runtime, §5 engagement).

**Golden Scene Dialogue & Storytelling Rules** (apply in both passes): (i) every line does at least one job; (ii) authentic spoken sentences — short, elliptical, zero greetings/prefaces; (iii) enter in the middle of conflict; (iv) weave the 5 Scene Action Structures across the 4-stage episode symphony; (v) Micro-Visual Reveal over verbal exposition; (vi) image speaks first, dialogue second; (vii) `1–2` characters actively interacting per shot window; (viii) end every clip per **Law D5** (Mode 1 wordless final shot by default, or Mode 2 ping-pong with a `~0.8s` closed-lip tail); (ix) at a decisive reversal, a calm understatement line (`2–6` words) is one option — vary it, never stamp it on every confrontation; (x) native interjections are rationed (`0c` §2).

#### Pass A — Structure (`✋ CP3a`)

```text
================================================================================
TẬP [N]: [Tên Tập] | CUNG CHIA: [Hồi I/II/III/IV · Archetype 1–5] | ENGINE: [1–6] | THỜI LƯỢNG: [M cảnh · ~T giây — 0c §4]
================================================================================

📌 PHẦN 1 — CỐT TRUYỆN TẬP (TẦNG 2), ĐẠO CỤ TIER-1, LIÊN KẾT TẬP (TẦNG 3) & SPINE CỦA TẬP:
• 1. Mục tiêu tập (nhỏ hơn mục tiêu cả bộ): [...]
• 2. Trở ngại trong tập: [...]
• 3. Lựa chọn khó ở cao trào (giữa 2 điều tốt hoặc 2 điều xấu — dựng ngược tập từ đây): [...]
• 4. Chuyển biến chính (đổi ít nhất 1 thứ không quay lại được): [Đầu tập: ... ──▶ Cuối tập: ...]
• 5. Một lớp thông tin mới về Bí mật lớn (chỉ mở 1 lớp, KHÔNG lộ hết): [...]
• 6. Đạo cụ / Vũ khí / Vật phẩm Tier-1 trong tập (file 4 góc không dính tay người & trạng thái):
  - `[Tên đạo cụ tiếng Anh chuẩn]` (`prop-[name].jpg` ➔ `<<<Image X>>>`): [State 0 / 1 / 2 | chi tiết sẽ zoom cận cảnh]
• 7. Bảng theo dõi liên kết tập (dùng ít nhất 2 trong 4 mối nối):
  | Tập | Hậu quả từ Cliffhanger tập trước | Mục tiêu & Chuyển biến | Mồi cài mới (Trả ở tập N+2+) | Trả mồi từ tập trước | Cliffhanger cuối tập |
  |---|---|---|---|---|---|
  | [N] | [...] | [...] | [...] | [...] | [...] |
• 8. Spine của tập (Doctrine §8.10 + §9.9):
  PREDICT | P1 Cảnh [NN]: khán giả đoán [...] → GIỮ | P2 Cảnh [NN]: khán giả đoán [...] → BẺ ở Cảnh [MM] | cài ở Cảnh [AA], [BB]
  KNOW    | Khán giả so với từng nhân vật chính; chỗ đổi chế độ (hồi hộp ↔ bí ẩn ↔ đồng cảm) ở Cảnh [NN] vì [...]
  MISREAD | [Ai hiểu lầm ai, qua Lời nói dối nào; điều gì chặn câu nói làm rõ; kết thúc ở cảnh nào] — hoặc "Không có"
  TWIST   | Lớn: Cảnh [NN], TW-[xx], cài ở Cảnh [..] · Nhỏ: Cảnh [NN], TW-[xx] · Gáo nước lạnh: Cảnh [NN], do cài ở Cảnh [..]
  VALUE   | Giá trị tích cực của tập: [...] — thể hiện qua lựa chọn của [Tên] ở Cảnh [NN], cái giá: [...]
  HEART   | Khoảnh khắc chạm: Cảnh [NN] — [hành động / đồ vật / khoảnh khắc nhận ra cụ thể] — cài ở Cảnh [AA]
  TAKEAWAY| Điều khán giả mang về (không nhân vật nào nói ra): "[...]"
  SHADOW  | Điều tập này có thể hiện nhưng KHÔNG cổ xúy (bẽ mặt, trả thù, lừa dối, bạo lực...) và cách xử lý: [...] — hoặc "Không có"
• 9. Nhân vật trong tập (2b §5–§6): [Tên (vai · mã)], [Tên (vai · mã)], [Tên (vai · mã) (mới)] — vắng: [Tên (lý do đã cài)]

🎙️ PHẦN 2 — HỒ SƠ GIỌNG NÓI & THẺ XƯNG HÔ TRONG TẬP (CHE TÊN VẪN NHẬN RA):
| Nhân vật (Proper Name & Ảnh) | Cách nói & Nhịp câu | Từ vựng & Thẻ xưng hô (kèm điểm đổi) | Điều KHÔNG BAO GIỜ nói thẳng | Câu mẫu (Blind Test) | Thẻ Hành Vi Giọng Nói (`Laws D2 & D3` — không số tuổi, không `alto/baritone`) |
|---|---|---|---|---|---|
| [Proper_Name] (<ref.jpg>) | [...] | [Xưng - Gọi | Đổi khi...] | [...] | "[1 câu chỉ người này mới nói]" | `(expressive female/male voice, [vocal behavior] in a [baseline tone])` |

🧲 PHẦN 3A — BẢN ĐỒ GIỮ CHÂN (RETENTION MAP — 0c §5):
• Hook 3 giây Cảnh 01: [#1–#12 tên loại hook] — [khung hình cụ thể khán giả thấy trong 3 giây đầu] ➔ câu hỏi nó mở: [...]
• Câu hỏi của tập (có/không): [...?]
• Đường cường độ (1–10 mỗi cảnh): 01:[ ] 02:[ ] 03:[ ] ... — đỉnh ở Cảnh [..]; cảnh lặng ở Cảnh [..]
• Đổi nhịp (ít nhất mỗi 2–3 cảnh): Cảnh [..], [..], [..] (đổi cấu trúc / giọng / tốc độ / không gian)
• Cliffhanger cuối tập: C[1–7] — [mô tả] (tập trước dùng: C[ ])
• Chống lặp: hook #[..] (tập trước #[..]) · TW-[..] (tập trước TW-[..]) · đối chiếu history-registry.json
• Bài học từ số liệu tập trước (performance_log, §10.1): [1–2 bài học áp dụng cho tập này — hoặc "Chưa có số liệu"]

📋 PHẦN 3B — DANH SÁCH CẢNH 1 DÒNG + CỘT GIỮ CHÂN (Mở 15–20% ➔ Phát triển 40–50% ➔ Cao trào 20–25% ➔ Kết 10%; mỗi cảnh ĐÚNG 1 VIỆC):
• Cảnh 01 [10s | Hook | @Director | Tier-1: <prop-*.jpg / Không> | TH2]: [Địa điểm, ai, làm gì, để làm gì]  (thêm 💗 ở cuối dòng nếu là cảnh chạm)
    Giá trị: [tin ➔ ngờ] (−) | Vòng lặp: mở L1 | Khán giả: [bí ẩn] | Cường độ: [7]
  ↳ [NHƯNG / VÌ VẬY]
• Cảnh 02 [10s | Kể chuyện/V.O. hoặc Đối thoại | @Director | Tier-1: ... | TH1/TH2/TH3]: [...]
    Giá trị: [...] (+/−) | Vòng lặp: [mở L# / đẩy L# / trả L#] | Khán giả: [hồi hộp / bí ẩn / đồng cảm] | Cường độ: [ ]
  ↳ [NHƯNG / VÌ VẬY]
• Cảnh [K] [10s/15s @Director hoặc 15s @CombatDirector | ...]: [...]
  ...

📊 BẢNG CHẤM ĐỘ CUỐN (§8.4) — Hook [ ]/2 · Vòng lặp [ ]/2 · Đổi giá trị [ ]/2 · Bẻ dự đoán [ ]/2 · Nhịp [ ]/2 · Nhân vật chủ động [ ]/2 · Thoại [ ]/2 · Cliffhanger [ ]/2 = [ ]/16
💗 BẢNG CHẤM GIÁ TRỊ (0d §8) — Giá trị [ ]/2 · Khoảnh khắc chạm [ ]/2 · Phẩm giá [ ]/2 · Mang về [ ]/2 = [ ]/8
================================================================================
```

#### Pass B — Prose & Ledgers (`✋ CP3b`, only after `CP3a` approval)

```text
🎬 PHẦN 4 — VĂN XUÔI THÔ TỪNG CẢNH (THÌ HIỆN TẠI, KHÔNG CHIA GIÂY):

--- CẢNH [K] ([10s/15s @Director hoặc 15s @CombatDirector]) — [Tên Cảnh Ngắn Gọn] ---
• Loại cấu trúc cảnh & nhịp cắt dự kiến (Hook / Kể chuyện V.O. / Đối thoại / Phát hiện manh mối / Hành động): [1 câu]
• Thẻ ý đồ: Muốn: A → [...]; B → [...] | Cản: [...] | Chiến thuật: A [...] / B [...] | Ẩn ý: [điều không nói ra] | Đổi giá trị: [đầu cảnh] → [cuối cảnh] | Khán giả: [hồi hộp / bí ẩn / đồng cảm]
• Địa điểm, Thời điểm & Nhân vật: [Địa điểm (<loc_ref.jpg>), thời điểm | Nhân vật (<char_ref.jpg>) | Điểm nối: TH1 / TH2 / TH3]
• Đạo cụ Tier-1 & cách cầm/đặt tại 00:00: [Tên tiếng Anh (<prop_ref.jpg>) | ở đâu / ai cầm tay nào | chi tiết lên cận cảnh] — hoặc "Không"
• Văn xuôi hành động & Thoại (Hình ảnh nói trước – Thoại nói sau; số câu và số từ theo 0c §2–§3):
  [Văn xuôi liền mạch tả hành động nhìn thấy được, tương tác đạo cụ rõ ràng, kèm thoại dạng `Tên (thẻ giọng): "..."`.]
• Chi tiết đáng nhớ & Cầu nối sang Cảnh [K+1] (Tầng 5): [cầu nối hình ảnh / âm thanh / đạo cụ / từ khóa / câu hỏi – đáp án]

📓 PHẦN 5 — SỔ LIÊN TỤC & SỔ THOẠI SAU TẬP [N]:
• 1. Ai biết gì sau Tập [N]: [...]
• 2. Bàn giao Đạo cụ Tier-1 & trạng thái nhân vật: [State 0/1/2, ai giữ; trang phục / thương tích / quan hệ đã đổi]
• 3. Sổ thoại (Echo line, Lời hứa, Lời đe dọa, Lời nói dối & tập cần trả): [...]
• 4. Sổ vòng lặp: L1 [câu hỏi] mở Cảnh [..] → trả Cảnh [..] / còn mở sang Tập [N+1]
• 5. Bản đồ hành trình nhân vật — cột Tập [N] (2b §5):
  | Nhân vật (vai · mã) | Muốn | Biết | Quan hệ | Lời nói dối | Có mặt |
  |---|---|---|---|---|---|
  | [Tên] | [...] | [...] | [...] | [nguyên / nứt / vỡ / chấp nhận sự thật] | [có / vắng: lý do] |

📊 BẢNG CHẤM ĐỘ CUỐN (chấm lại sau khi viết văn xuôi) = [ ]/16
💗 BẢNG CHẤM GIÁ TRỊ (chấm lại sau khi viết văn xuôi) — Giá trị [ ]/2 · Khoảnh khắc chạm [ ]/2 · Phẩm giá [ ]/2 · Mang về [ ]/2 = [ ]/8
```

### 8.4 Engagement Scorecard, Stage 3 Pre-Flight & Script Audit (`Chấm Độ Cuốn & Đối Chiếu Trước Khi Viết Prompt`)

**1. Engagement Scorecard (`Bảng Chấm Độ Cuốn`)** — score honestly at the end of Pass A and again at the end of Pass B. Each criterion scores `0`, `1` or `2`. **Pass mark: `≥ 12 / 16` with no criterion at `0`** (`0c` §5). Then answer the 5 questions of the mounted genre's **Mastery Playbook P7** (`engine/genres/<genre>.md`); any "no" is fixed before the checkpoint. Below the mark, rewrite the weakest criteria **before** presenting the checkpoint, and show the scores in chat.

**1b. Heart & Value Scorecard (`Bảng Chấm Giá Trị` — `0d` §8)** — scored at the same two moments. **Pass mark: `≥ 6 / 8` with no criterion at `0`.** Then answer the 5 pre-flight questions of `0d` §9. A script that is gripping but gives the viewer nothing, or whose payoff is humiliation, cruelty or revenge, is rewritten before the checkpoint: change the route, keep the value.

| # | Criterion | 2 points when… |
|---|---|---|
| 1 | **Giá trị tích cực qua lựa chọn** | a positive value is shown through a character's costly choice, never stated in dialogue |
| 2 | **Khoảnh khắc chạm** | `≥ 1` specific, planted, restrained heart moment (`💗`, `0d` §4 H1–H5) |
| 3 | **Phẩm giá & công bằng** | dignity restored, consequences fair and self-caused, the opponent humanized with a door left open (`0d` §5) |
| 4 | **Điều mang về & hy vọng** | a clear, unspoken takeaway; the ending or cliffhanger keeps a light of hope (`0d` §7) |

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Hook 3 giây** | Scene 01 opens on setup, greeting or explanation | intriguing but abstract or slow | a concrete visual anomaly that raises a question inside `3s` |
| 2 | **Vòng lặp mở** (open loops) | cuts with no open question | a loop is live at most cuts | `≥ 1` loop live at every cut; every payoff has a plant |
| 3 | **Đổi giá trị** (value shift) | `≥ 3` scenes with no shift | `1–2` flat scenes | every scene flips a value |
| 4 | **Bẻ dự đoán** (prediction breaks) | none, or a twist with no plant | `1` broken prediction, or plants after the payoff | `≥ 2` broken predictions with earlier plants; the major twist is an Option C |
| 5 | **Nhịp** (rhythm) | `3` same-type scenes in a row or a flat intensity curve | some variety, weak peak or no lull | pattern shift every `2–3` scenes, `≥ 1` silent scene, a clear peak and a lull |
| 6 | **Nhân vật chủ động & có giá** | `A1` reacts; luck or a stranger turns the episode | `A1` acts but pays nothing | `A1`'s own choice turns the episode, it costs something, `A2` has a point |
| 7 | **Thoại tự nhiên** | exposition, feeling labels or one shared voice | mostly natural, a few on-the-nose lines | Blind Voice Test passes, subtext over statement, interjections rationed, budgets kept |
| 8 | **Cliffhanger & mồi** | the episode closes everything | an open question of the same kind as last episode | a new-layer question or danger that forces the next episode, different type from the last, `≥ 2` connectors |

**2. Stage 3 Pre-Flight** — verify before each checkpoint:
1. **Tier 1 & 2**: the episode serves the Central Question / Transformation Arc, reveals **only 1 layer** of the Master Secret, turns on `A1`'s crisis choice, changes **at least 1 thing irreversibly**, and carries its Value Card (`VALUE · HEART · TAKEAWAY`, plus `SHADOW` when it shows cruelty or revenge).
2. **Tier 3**: at least 2 inter-episode connectors are used, and the episode opens directly on the consequence of Episode $N-1$'s cliffhanger.
3. **Tier 4 & 5**: each scene does **strictly ONE job**, links via **`"Vì vậy"` / `"Nhưng"`** (zero `"Và rồi"`), and routes `10s/15s` narrative/dialogue scenes to `@Director` and high-velocity scenes to `@CombatDirector`.
4. **Dialogue**: every line passes the **Blind Voice Test**, obeys **Micro-Visual Reveal Over Verbal Exposition**, stays within `0c` §2 budgets and ends each clip per Law D5.
5. **Continuity**: Character/Location/Prop tags match `setting.html`; the Post-Episode Ledger and Loop Ledger are updated (Pass B).

**3. Save & Audit (Pass B)** — after writing Pass B, save the complete Episode N script (Pass A + Pass B, exactly as shown in chat) to **`output/<slug>/ep-NN-script.md`** (Markdown working file — not an HTML deliverable, so the Single-HTML Law still holds) and run:

```bash
python engine/screenplay_audit.py output/<slug>/ep-NN-script.md
```

The audit checks the Retention Map, the scene-list columns, `Vì vậy / Nhưng` links, the PREDICT ledger (`≥ 2` BROKEN with earlier plants — W10), loop plants before payoffs, feeling-label lines (W9), single-location stagnation (W11), word budgets, interjection rationing, hook/twist/cliffhanger repetition against the previous episode's script, and the character lines (`2b`): new named characters per episode, A1 presence, Arc Map rows for every character on screen, and characters absent more than 2 episodes in a row, and the **Heart & Value** layer (`0d`): the `💗 = N/8` scorecard (pass `≥ 6/8`, no `0`), the `VALUE / HEART / TAKEAWAY` rows, a heart plant before its payoff, and humiliation-as-payoff wording in the climax without a `SHADOW` row. Fix every `ERROR`; justify or fix every `WARN` before `CP3b`.

**4. Checkpoints** — present in chat:
```text
✋ CHECKPOINT 3A — Cấu trúc Tập [N] (Cốt truyện tập, Spine + Thẻ Giá Trị, Bản đồ giữ chân, Danh sách cảnh 1 dòng) — Độ cuốn: [ ]/16 · Giá trị: [ ]/8
→ "ok" để viết văn xuôi và thoại từng cảnh (Pass B) | "edit [nội dung]" | "cảnh [K]: [yêu cầu]" để chỉnh cấu trúc

✋ CHECKPOINT 3B — Kịch bản thô chi tiết Tập [N] đã lưu output/<slug>/ep-NN-script.md và qua screenplay_audit.py — Độ cuốn: [ ]/16 · Giá trị: [ ]/8
→ "ok" để bắt đầu Stage 4 với Cảnh 01 (Agent tự lấy thông số Bối cảnh / Nhân vật / Đạo cụ từ setting.html; bạn chỉ gửi Ảnh Tĩnh Cuối Cảnh trước ở các cảnh nối tiếp TH1/TH3)
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
2. **Step 2 — Unified Multi-Shot Storyboard Compilation & Intent-First Agent Routing (`@Director 10.0s & 15.0s Dialogue/Sitcom/Drama` vs. `@CombatDirector 15.0s Action/Chase/Combat`)**:
   - **For `10.0s` AND `15.0s` Opening Hook, Storytelling/`V.O.`, Dialogue, Sitcom, Confrontation & Clue Twist Scenes (`Compiled by @Director`)**:
     * **Enforce Temporal-Kinetic-Vocal Equilibrium & Zero Tail-Cut Law**: Allocate **`3.2s–4.5s`** to every shot containing spoken dialogue (`1 simple action + 1 spoken line`) and end the clip per **Law D5**: **Mode 1 (default)** keeps the final `2.0s–3.0s` shot wordless for the **Visual Payoff / Curiosity Hook / Physical Comedy Button / Somatic Settle**; **Mode 2** (all shots speak) keeps the final line to `6–8` words with a `~0.8s` silent closed-lip tail (`0c` §2).
     * **Default `10.0s` Scene (`Flexible 1–4 Shots` by Scene Action Structure — `0b` §1.1)**: Flex shot count and durations organically by scene structure (*Opening Hook*, *Storytelling/V.O.*, *Dialogue/Confrontation*, or *Clue Insert*), e.g., `10s` continuous take, `5s–5s`, `4s–4s–2s`, or `3.5s–2s–2.5s–2s`.
     * **Conversational `15.0s` Sitcom / Comedy / Multi-Turn Drama Scene (`Flexible 3–4 Shots`, e.g., `4s–4s–4s–3s` or `4.5s–4s–3.5s–3s`)**: `2–3` active turns across `Shot 1..N-1` $\to$ Final Shot (`2.5s–3.0s`) Wordless Physical Comedy Button / Visual Payoff (`0 spoken words`).
   - **For High-Motion `15.0s` / `10.0s` Action, Chase, Combat, Vehicle Drift, Sports, Split-Second Rescue & High-Velocity Craft Scenes (`[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s]` — Routed Exclusively to `@CombatDirector`)**:
     * Governed from First-Principles Kinetic Physics (`combat-director/SKILL.md` §1–§2) rather than fixed shot quotas: choose the **Shot Topology** organically from scene intent (**`Topology 1`: `1–2 Shot` Unbroken 3A Inertial Long-Take**; **`Topology 2`: `3–5 Shot` Asymmetric Dynamic Exchange**; or **`Topology 3`: `6–9 Shot` Staccato Rapid-Cut Blitz**), apply the **4 Core Kinetic Physics Levers** (*Surface-Bound Material & VFX Physics*, *AAA Camera Inertia*, *Directional Motion Blur Release*, and *Time-Ramp & Hit-Stop Weight*), zero `→` arrows, and end on a wordless `1.5s–3.0s` clean composed landing pose (`0 spoken words`).
   - **For Single-Frame Still Image / Keyframe Requests (`Routed Exclusively to @PhotoDirector` — `.agents/PHOTO_DIRECTOR.md`)**:
     * Whenever the user requests a single still image, portrait, or keyframe for `Scene K`, compile using the **Unified Still Image Architecture** (`Style:` ➔ `[context]:` ➔ `[subject]:` [5-Point Anatomical Pose Lock + Gender/Style Skin & Makeup Sub-Lock `F1–F4 / M1–M3 / A1–A3`, omitting `; only head/eyes move`] ➔ `[prop]:` ➔ `[shot & action]:` [Static Shot Scale, 4-Axis Camera Angle, Optical Focus + Captured Instant Action + Mandatory 4-Zone Facial Micro-Expression `brows, eyes/moisture, lips, jaw`] ➔ `Footer`), stripping 100% of dynamic video elements.
   - **For 2-Phase Multi-Panel Storyboard Grid (`9/12/15/25 Shots`) & `Storyboard-to-Video` Requests (`Routed Exclusively to @StoryboardDirector` — `.agents/STORYBOARD_DIRECTOR.md`)**:
     * **Phase A (`Storyboard Grid Image Prompt`)**: Map `Scene K` across `9 (3×3)`, `12 (3×4)`, `15 (3×5)`, or `25 (5×5)` static panels (divisible by `3` or `5`) with a **small clean rounded number badge (`1` to `N`) in the top-left corner of each panel**, enforcing 100% static pose/angle/4-zone expression per panel (`Shot 1..N`), `>45°` scale/angle jumps, and pre-designed speaking (`lips parted slightly`) vs. silent (`composed closed lips`) panels.
     * **Phase B (`Storyboard-to-Video Prompt — Strict 1:1 Shot & Timeline Mapping`)**: Take the rendered Storyboard Grid Image as `<<<Image 1>>>` + Character Refs `<<<Image 2, 3>>>`, and write out **every single `Shot 1` through `Shot N` individually with exact contiguous `(00:XX-00:YY)` timelines matched 1:1 to `Panel 1..N`** (`Shot K (00:XX-00:YY) - Panel K ([Grid Position]), [Shot Scale], [Angle/Move], [Shot Speed]` + 1 sentence of dynamic motion + separated dialogue line on `3.2s–4.5s` speaking shots + `Final Shot` obeying Law D5) + Anti-Split-Screen/Anti-Badge Footer.
3. **Step 3 — Mandatory Pre-Flight Self-Audit (`Đối Chiếu Chống Sai Sót Trước Khi Xuất Cảnh K`)**:
   - Verify: (i) **`<<<Image X>>>` declared ONLY ONCE** in `[context]:`, `[subject]:`, and `[prop]:` (0 times inside `Shot 1..N`), (ii) **100% Zero-Costume & Zero-Age compliance** in `[subject]:` and `Shot 1..N`, (iii) **Proper Character Names Only** (no generic `Woman`, `Man`), (iv) **1–2 short natural sentences per shot** (`15–30w`, zero `→` arrows, zero static `[subject]:` repetition, zero meta-instructions), and (v) **Zero Tail-Cut Law (`0 spoken words` in the final `2.0s–3.0s` shot)** + Clean Terminal Keyframe Landing.
4. **Step 4 — Deliver the 4-Part Interactive Scene Card in Chat & Wait for User Confirmation**:
   - Output directly in chat: **👁️ Phần 1 (Đối Chiếu Tham Chiếu & Đầu Cảnh)**, **🎭 Phần 2 (Tóm Tắt `Shot 1..N` & Điểm Đỗ Cuối Cảnh)**, **🎬 Phần 3 (Code Block 1 Multi-Shot Storyboard Prompt & Code Block 2 Handover)**, and **⏭️ Phần 4 (Chỉ Dẫn Bước Tiếp Theo Cho `Cảnh K+1`)**. STOP and wait for user confirmation before generating `Scene K+1`.

### 9.3 Code Block 1 — Canonical Unified Storyboard Prompt (Skeleton + Fully Compliant `10.0s @Director` Example)

**Skeleton** (blocks in this order, separated by one blank line; numbers from `0c`, camera choices from `3c`):

| Block | Rule |
|---|---|
| `Style:` | one line: medium, look, palette, light quality — no camera hardware numbers |
| `[context]:` | `[Evocative English location] <<<Image 1>>> (fully_preserved - same architectural layout, fixed furniture and lighting throughout), [time of day]. [5-vector description: layout + permanent furniture/fixtures, key light source & direction, shadows, atmosphere, mood]` — **location-owned items only**; anything a character holds, uses or changes belongs to `[subject]:` / `[prop]:` (§2.6 Separation Law) |
| `[subject]:` | per character: line 1 `Name <<<Image N>>> (fully_preserved - …gender/hand lock…; motion scope): A graceful woman / A composed man [00:00 anchor to a landmark], [00:00 hand/prop state], [eyeline] — the only Name in frame.` + line 2 skin/hands(/makeup) sub-lock (§2.6 schools). Zero clothing, zero age, zero hair colour words |
| `[prop]:` | only for Tier-1 props: `Prop name <<<Image N>>> (fully_preserved - same shape, material, surface finish and proportions throughout): [00:00 placement or hand grip] — the only [prop] in frame.` |
| `[sound]:` | room tone + timestamped Foley; state music policy |
| `Shot K (MM:SS-MM:SS) - [Shot scale], [angle/move targeting Name], [speed tag]` | timeline starts at `00:00`, contiguous, ends at `00:10` / `00:15`; speed tag from `0b` §4.2 |
| shot prose | `1–2` sentences, `12–30` words, one action (`State A ➔ State B`), no repetition of `[subject]:`, no meta-instructions |
| dialogue line | `Name (expressive female/male voice, [vocal behaviour] in a [tone]): "…"` — window `≥ 0.4s + words/2.5 + 0.5s` inside `3.2s–4.5s`; interjections on at most 1 in 3 lines, never on a calm authority line |
| final shot | Law D5: Mode 1 wordless `2.0s–3.0s` payoff (default) or Mode 2 short final line + `~0.8s` closed-lip tail |
| footer | the canonical 3-line footer (§2.6) |

After writing, save the prompt to `output/<slug>/prompts/ep-NN-scene-KK.md` and run `python engine/prompt_audit.py <file>` (§9.7); fix every `ERROR` before presenting `Scene K`.

**Example** (Mode 1; one female and one male character; a Tier-2 handheld cup assigned to the character, not the location):

```text
Style: Grounded live-action cinema, natural muted palette, soft overcast window light, fine film grain, realistic matte skin.

[context]:
Narrow riverside apartment kitchen <<<Image 1>>> (fully_preserved - same architectural layout, fixed furniture and lighting throughout), late afternoon. A small square wooden table stands under a rain-streaked window, with two chairs facing each other and a tall refrigerator against the tiled wall behind the far chair. Grey daylight from the window falls sideways across the tabletop, leaving the refrigerator side in soft shadow; the air is still and damp.

[subject]:
Iris <<<Image 2>>> (fully_preserved - same female face, slender feminine body proportions, delicate wrists, long tapering fingers, hair color, makeup and outfit throughout; only her head, eyes, mouth, hands and expressions move.): A graceful woman seated in the chair nearest the window, both slender feminine hands wrapped around a warm ceramic teacup on the table, eyeline toward Theo — the only Iris in frame.
Iris's skin, hands and makeup: fully_preserved - real unretouched dry matte skin across her face, neck, and slender feminine hands, with delicate wrists, long tapering fingers, understated makeup, crisp individual eyelashes, natural moisture in her eyes, and soft natural lips; no rough masculine hands, no thick knuckles, no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.
Theo <<<Image 3>>> (fully_preserved - same male face, masculine body proportions, broad shoulders, well-defined masculine hands, hair color and outfit throughout; only his head, eyes, mouth, hands and expressions move.): A composed man seated in the chair opposite Iris with his back to the refrigerator, his right hand resting flat on the table beside a closed silver pocket watch, eyeline lowered to the watch — the only Theo in frame.
Theo's skin and hands: fully_preserved - real unretouched dry matte masculine skin across his face, jawline, and strong well-defined masculine hands, with natural fine pores, crisp eyebrows and eyelashes, natural moisture in his eyes, and natural matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.

[prop]:
Closed silver pocket watch <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): Lying closed on the tabletop beside Theo's right hand at 00:00 — the only silver pocket watch in frame.

[sound]:
Light rain tapping the window, a refrigerator hum, a chair creaking as Iris leans in at 00:01, the metallic snap of the watch lid opening at 00:05, then silence. No background music.

Shot 1 (00:00-00:04) - Medium close-up, static over-the-shoulder camera from behind Theo targeting Iris's face, natural real-time speed
Iris leans forward over her teacup, her eyes searching Theo's lowered face.
Iris (expressive female voice, asking softly with rising suspicion in a quiet tone): "Huh? You kept his watch all along?"

Shot 2 (00:04-00:07.6) - Medium close-up, static reverse over-the-shoulder camera from behind Iris targeting Theo's face, natural real-time speed
Theo flips the watch lid open with his strong masculine hand, his eyes still lowered to it.
Theo (expressive male voice, speaking with calm quiet certainty in a low tone): "He asked me to stop it."

Shot 3 (00:07.6-00:10) - Close-up, static camera targeting Iris's face, natural real-time speed
Iris's lips part without a sound as her gaze drops to the open watch, her slender feminine fingers slowly releasing the teacup.

Master-level cinematography and composition, locked static camera framing for maximum facial and vocal acting clarity, atmospheric sound design.
Strict visual consistency: maintain 100% identical facial features, slender feminine and strong masculine hand proportions, matte skin texture, hair color, makeup, exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.
Do not generate duplicate props or utensils, rough masculine hands on female characters, thick knuckles, oily sweat shine, greasy forehead or nose glare, waxy plastic skin, subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.
```

*Why it passes*: the teacup and watch are owned by characters (`[subject]:` / `[prop]:`), not the kitchen; Shot 1 carries 7 words in a `4.0s` window (needs `≥ 3.7s`), Shot 2 carries 6 words in `3.6s` (needs `≥ 3.3s`); one interjection in two lines and none on Theo's calm line; each shot has one action in `12–30` words; Shot 3 is the wordless `2.4s` Mode 1 payoff; footer follows §2.6.

### 9.4 Silent Scene & Silent Film Directive
For any silent scene (`Model 0`) or full Silent Film, omit all spoken dialogue blocks, amplify tactile Foley and micro-visual reveals across `Shot 1..N`, and end with:
```text
Master-level cinematography and composition, smooth dynamic camera pacing, atmospheric sound design.
Strict visual consistency: maintain 100% identical facial features, matte skin texture, hair color, makeup, exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.
Do not generate oily sweat shine, greasy forehead or nose glare, waxy plastic skin, subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video. Do not generate spoken dialogue, lip movement matching speech, or voiceover.
```

### 9.5 Interactive Scene-by-Scene Cross-Check Matrix (No `tap-X.html` Generation)
Every single scene prompt (`Scene K`) delivered in chat MUST pass the following **7-Point Cross-Check**:
1. **Double-Lock `fully_preserved` Reference, 4-Layer Gender & Hand/Limb Anatomy Lock, Skin/Makeup Sub-Lock & Single `<<<Image X>>>` Declaration Law**: Are `<<<Image X>>>` tags declared **ONLY ONCE** in `[context]:`, `[subject]:`, and `[prop]:` with the explicit `(fully_preserved - same female/male face, slender feminine / masculine body proportions...)` parenthetical right after each tag + Line 2 `<Name>'s skin, hands (and makeup): fully_preserved - ...`, **never repeated** inside `Shot 1..N`, and sealed with the `Strict visual consistency: ...` footer?
2. **Zero-Costume, Zero-Age & Expressive Vocal-Behavior Tag Law (`Laws D2 & D3` · `Gates 3A & 3E`)**: Are all specific clothing words (`in a black jacket`, `in a dark suit`, `skirt`), numeric ages / specific hair/beard words (`32-year-old`, `young blonde`, `silver-bearded`), and dry musical register terms (`alto`, `baritone`, `tenor`, `soprano`) 100% purged from the entire prompt, with vocal behavior encoded in **ONE single parenthetical (`[Proper_Name] (expressive female/male voice, [vocal behavior] in a [tone]): "[Interjection]! ..."`)**?
3. **Proper Names & Continuity Grounding (`TH1 / TH2 / TH3`)**: Are all characters named with fixed proper names (`Bradley`, `Harold`, `Elena`, `Dante`) and anchored to 100% real visible landmarks from the reference image?
4. **Tier-1 Prop & Weapon Consistency (`[prop]: <<<Image X>>>`)**: If a Tier-1 Hero Prop, Weapon, or Key Artifact appears in the scene, is it declared in `[prop]: <<<Image X>>>` with its exact `00:00` resting placement or hand-grip (`right hand` with `left hand empty`, or `spaced two-handed grip`), and referenced by its exact canonical noun phrase in `Shot 1..N`?
5. **Dynamic Shot Topology & Shot Economy (`Topology Follows Intent`)**: Is the shot topology (`1–4 shots` in `10s/15s` `@Director`; `1–2 Shot` Inertial Long-Take $\leftrightarrow$ `3–5 Shot` Asymmetric Exchange $\leftrightarrow$ `6–9 Shot` Rapid-Cut Blitz in `@CombatDirector`) chosen organically from dramatic intent without fixed shot quotas, and does each `Shot N` express its state transition `A ➔ B` in natural causal prose without `→` arrows?
6. **Target-First Camera Axis, Optical Prop Vector & Selective Directorial Toolkit**: Does every shot explicitly lock its camera axis and optical focus onto the **Primary Target Subject (`targeting [Proper_Name]` / `with focus locked on [Proper_Name]'s face`)** along the 180° interpersonal line of force? Are handheld props (mirrors, receipts, phones, contracts) physically oriented toward the Target Character rather than cheated flat toward the audience, and are full faces/eyes kept visible on the Target Axis in comedy, sitcom, and direct showdowns?
7. **Clean Terminal Keyframe Landing**: Does the final shot guide characters into a stable, zero-motion-blur pose recorded in `Code Block 2 ([HANDOVER STATE])`?

### 9.7 Master Pre-Flight Gate Matrix (Interactive Stage 4 Scene Linter)

| Gate / Check | Classification | Enforcement Rule |
|---|---|---|
| **Gate 1 (Single-HTML Law)** | Hard Gate | Only `output/<slug>/setting.html` is generated as an HTML file; Stage 3 & Stage 4 execute 100% interactively in chat (`Zero tap-X.html`). |
| **Gate 2** | Hard Gate | Explicit clip duration (`10.0s` Default `@Director` vs. `15.0s` Action/Combat `@CombatDirector`), starting at `00:00` and ending at `00:10` / `00:15` / `00:30`. |
| **Gate 2B** | **Hard Gate** | **Mandatory 12-Row Story Spine & 5-Tier Series/Dialogue Architecture** locked before scene compilation. |
| **Gate 3A** | Hard Gate | **Zero numeric ages, zero age/hair/beard words, and zero dry musical register terms (`alto/baritone/tenor/soprano`)** anywhere in Code Block 1; vocal behavior and tone encoded via **`Laws D2 & D3` (`[Proper_Name] (expressive female/male voice, [vocal behavior] in a [tone]): "[Interjection]! ..."`)**. |
| **Gate 3B** | Hard Gate | Zero freeze-frame holds (`freeze frame`, `frozen frame`, `zero-velocity`). |
| **Gate 3C** | Hard Gate | **Proper Character Names Only** (`Bradley`, `Harold`, `Elena`, `Dante`) across `[subject]:`, `Shot 1..N`, and speaker headers; zero generic `Woman`, `Man`, `the father`, and zero `snake_case` `ho_ten`. |
| **Gate 3D** | Hard Gate | Zero camera hardware, lens mm, f-stop, ISO, fps, or numeric Kelvin jargon document-wide. |
| **Gate 3E** | Hard Gate | **Zero clothing/wardrobe descriptions** (`jacket`, `suit`, `skirt`, `dress`, `coat`) anywhere in Code Block 1 (`[subject]:` or `Shot 1..N`). |
| **Gate 3F** | Hard Gate | Minor Protection Protocol: zero generic minor nouns; zero sexual, body-focused, violence, or adult-label lexicon with registered `minor_characters`. |
| **Gate 3G** | Hard Gate | Mandatory Header (`Style:` ➔ `[context]:` — zero redundant top slugline) and Footer (`Master-level cinematography...` + `Strict visual consistency: ...` + `Do not generate oily sweat shine...`) on every Code Block 1. |
| **Gate 3H** | Hard Gate | Zero Cartesian math coordinates (`X: +0.8m`) and zero 2D frame-edge tokens (`screen-left`, `frame-right`) in Code Block 1. |
| **Gate 3I** | Hard Gate | 100% Stateless prompts (zero `from Scene N` or `previous scene` references in Code Block 1). |
| **Gates 3J, 3K, 3L** | Hard Gate | **Double-Lock `fully_preserved` Reference, Gender Skin/Makeup Sub-Lock & Single `<<<Image X>>>` Declaration Law**: `[context]:`, `[subject]:`, and `[prop]:` (when Tier-1 prop/weapon is present) declare `<<<Image X>>>` **ONLY ONCE** followed immediately by `(fully_preserved - ...)` + Line 2 `<Name>'s skin (and makeup): fully_preserved - ...`, with **ZERO `<<<Image X>>>` repetition inside `Shot 1..N`**. |
| **Gate 3M** | Hard Gate | Dynamic contiguous shots (`Shot 1 (00:00-00:XX)` .. `Shot N`) starting at `00:00` and ending at `00:10` or `00:15` (`@Director` for `10.0s` & `15.0s` Dialogue/Sitcom/Drama; `@CombatDirector` for `15.0s` Action/Chase/Combat). |
| **Gate 3N** | Hard Gate | Mandatory `Strict visual consistency: maintain 100% identical facial features, matte skin texture, hair color, makeup, exact outfit, and exact weapon/prop design...` and negative oily-shine/subtitle/text directives at the tail of every Code Block 1. |
| **Gate 3O** | Hard Gate | **Zero Dead Air & State-Delta Directing Law**: 100% active physical or vocal occupancy across every shot; zero static filler phrases (`holds still`, `stands rigid through`, `blinks quietly`), zero repetition of `[subject]:` initial posture inside `Shot 1..N`, and zero meta-instructions (*"speaking immediately from the opening second"*, *"finishes his sentence early"*). |
| **Gate 3P** | Hard Gate | Zero literal placeholder tokens (`audio tag`, `cảm xúc khi nói`, `LÀM GÌ`) in prompts. |
| **Gate 3Q & 3R** | Hard Gate | **1–2 Short Natural Sentences per Shot (`15–30 Words`)**: Each `Shot N` expresses 1 clear state transition `A ➔ B` in natural cinematic prose; strictly zero mechanical `→` arrows. |
| **Gate 3S** | Hard Gate | **Target-First Camera Axis, Optical Prop Vector Law, 180° Axis & Zero Ghost Fixtures**: Every shot explicitly locks focus onto its Primary Target Subject (`targeting [Proper_Name]` / `with focus locked on [Proper_Name]'s face`) with `1–2` active characters per shot (banning passive audience-spectator side-by-side framing); handheld props (mirrors, receipts, phones, contracts) physically face the Target Character rather than the audience; full faces/eyes stay visible on the Target Axis in comedy/drama; all landmarks and props touched in `Shot 1..N` must be pre-declared in `[context]:`, `[subject]:`, or `[prop]:`. |
| **Gate 4 & 4B** | Hard Gate | **The 6 Golden Dialogue Laws (`Law D1–D6`, D6 = cross-scene handover)**: (`D1`) Lock `static camera` across continuous dialogue shots; (`D2`) Open emotional/comedic/confrontational lines with a native vocal interjection (`"Huh?..."`, `"Whoa! Uh..."`, `"Hửm?..."`, `"Á! Ối trời..."`); (`D3`) Use Expressive Vocal-Behavior Tags (`(expressive female/male voice, [scoffing / gasping / chuckling / speaking with calm authority] in a [tone])` — zero `alto/baritone/tenor/soprano`); (`D4`) Size spoken shots to `3.2s–4.5s` (`One-Move Rule`, max `3` spoken shots in `10s`, max `4` spoken shots in `15s`); (`D5`) Enforce either **Terminal Mode 1 (`0 spoken words` in final `2.0s–3.0s` shot)** OR **Terminal Mode 2 (`100%-Dialogue Ping-Pong` with `7–8w` in `Shot 1..N-1` and `6–8w` + mandatory `0.5s–1.0s` [`~0.8s`] silent closed-lip tail buffer in final `Shot N`)** so the last 1–2 words are never cut off. |
| **Gates 4D, 4E, 4F** | Project Gate | Enforces `kinship_ladder`, `meal_terms`, and `bookish_terms` when defined in `output/<slug>/project_rules.json`. |
| **Gate 4G** | Hard Gate | Separated Speaker Dialogue Line (`[Proper_Name] ([off-screen/voice-over if applicable], expressive female/male voice, [vocal behavior] in a [tone]): "[Native Interjection]! [Spoken line]"`) placed cleanly on its own line below the shot's action prose. |
| **Gate 4H** | Hard Gate | Mandatory Code Block 2 (`HANDOVER STATE AT 00:10.0 / 00:15.0`) + `Outbound Continuity Reference Case (TH1 / TH2 / TH3)` + **`Law D6` 4-Point Cross-Scene Dialogue & Posture Handover Bridge** in every scene card. |

### 9.8 ✋ CHECKPOINT 4 (End of Episode N Scene-by-Scene Loop)
Once the final scene (`Scene M`) of Episode $N$ is delivered and verified in chat with the user:
```text
✋ CHECKPOINT 4 — Hoàn tất toàn bộ [M]/[M] cảnh của Tập [N] (Đã đối chiếu trực quan từng cảnh 100%)
Tóm tắt Tập [N]: [Bảng 1 dòng/cảnh: Cảnh | Bối cảnh | TH1/TH2/TH3 | Model (Standard/Seedance) | Điểm nối cuối cảnh]
→ "ok" để sang Tập [N+1] (Stage 3: Kịch bản thô Tập [N+1]) hoặc Stage 5 (Đóng gói SEO & Thumbnail)
→ "cảnh [K]: [chỉnh sửa]" nếu muốn tinh chỉnh lại bất kỳ cảnh nào
```

---

## §10 — STAGE 5: DISTRIBUTION & PACKAGING (`seo-package.md` — `✋ CP5`)

> **JIT Load**: `.agents/skills/youtube-growth-architect/SKILL.md`. Mandatory for every completed project.

Deliver the package **in chat as copy-paste blocks** and save the same content to `output/<slug>/seo-package.md` (Markdown working file — the project's only HTML file remains `setting.html`, §2.10) containing:
- **Tier 1 — Omnibus (Full Movie / Series Compilation)**:
  1. **5 High-CTR Title Variants** (`50–65` characters) using the 4 Universal Title Formulas + Narrative POV Invariance.
  2. **4 Sovereign Thumbnail Prompts** enforcing the 4 Pillars: *Suspended Catastrophe*, *Extreme Duality & Somatic Delta*, *Embedded 3D Text ($\le 4$ words)*, and *Mobile Safe Zones*.
  3. **4-Tier NLP Description** inside copy-paste blocks with cumulative `10s` scene chapters.
  4. **7-Cluster Audience Tag String** ($\le 500$ characters) + Polarizing Debate Pinned Comment (seeded from the Story Spine `[DEBATE]` row).
- **Tier 2 — Per-Episode Packaging**: Dedicated `[Ep N/T]` cliffhanger titles, episode thumbnail prompts, episode chapters, and next-episode binge-funnel pinned comments.

✋ **CHECKPOINT 5**: Present the package in chat (saved as `output/<slug>/seo-package.md`), finalize `history-registry.json` (§11), and conclude production (`🎬 DONE`).

### 10.1 Post-Release Performance Feedback Loop (`Vòng Phản Hồi Số Liệu Thật`)
Retention data is the only honest judge of the Engagement Scorecard. After each episode has been public for `48–72h`, ask the user for its analytics (YouTube Studio / TikTok / Facebook — the user reads them; the agent never logs in) and record them:
1. **Collect** (user-supplied numbers): viewers still watching at `3s` and `30s`, average percentage viewed, the second of the steepest drop, next-episode click-through (series), and `1–3` representative comments.
2. **Compare** against the short-form targets in `0c-canonical-numbers.md` §9 and against the episode's own Scorecard: a criterion scored `2` whose metric missed the target is a calibration error, not bad luck.
3. **Diagnose the drop**: map the drop second to the scene in `output/<slug>/ep-NN-script.md` (scene index ≈ drop second ÷ `~11s`) and name the cause in one line (slow hook, dead cut with no open loop, repeated scene type, exposition line, weak cliffhanger).
4. **Record** one entry per episode in `history-registry.json → performance_log` (§11).
5. **Apply** before writing the next episode: Stage 3 Pass A of Episode `N+1` lists the `1–2` lessons from the latest entries in its Retention Map ("Bài học từ số liệu tập trước"), and Stage 0 of a new project reads the cross-project lessons (K1).

---

## §11 — HISTORY REGISTRY PROTOCOL (MANDATORY)

- **Draft at `CP2` (after `setting.html` passes Gate 1.5)**: Record character names, visual style, genre, arena, tropes, hero prop group, and narrative mode in `history-registry.json` with `"status": "draft"`.
- **Finalize at `CP5`**: Record hook archetype, narrative polarity, story track, escalation variant, twist codes (`TW-xx`), cliffhanger codes (`C1–C7`), and diurnal lighting; set `"status": "complete"`, append to `story_history`, increment `total_stories_produced`, and refresh `session_log`.
- **Performance log (after release, §10.1)**: append one object per published episode to `performance_log`:
  `{"slug": "...", "episode": N, "published": "YYYY-MM-DD", "platform": "youtube|tiktok|facebook", "hook_type": "#N", "cliffhanger": "C#", "twist": "TW-xx", "scorecard": 14, "retention_3s": 0.82, "retention_30s": 0.61, "avg_pct_viewed": 0.57, "next_ep_ctr": 0.27, "drop_second": 24, "drop_scene": 3, "diagnosis": "...", "lesson": "..."}`.
  K1 reads the latest `performance_log` lessons alongside the 14 anti-repetition axes; hook/twist/cliffhanger types with repeatedly weak retention are deprioritised in new concepts.

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
| Route every request with **K2b** and load the named agent file before writing | Answer a Roblox, commercial or source-video request with the film pipeline |
| Score concepts, series and episodes with the **Engagement Scorecards** (§5.4, §6.5, §8.4) and rewrite below the pass mark | Present a checkpoint below the pass mark or hide the scores |
| Save `ep-NN-script.md` and pass `screenplay_audit.py` before `CP3b`; save `prompts/ep-NN-scene-KK.md` and pass `prompt_audit.py` before presenting a scene | Present an unaudited script or scene prompt |
| Fit action to duration with the **Motion Density Law** (§2.5) and end every prompt with the **canonical 3-line footer** (§2.6) | Cram several primary actions into one shot, or leave a long shot under-filled for the model to improvise |
| Take every count, duration and budget from `0c-canonical-numbers.md`, character labels from `2b`, camera choices from `3c` | Copy numbers into other files or invent role labels |

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
│   ├── screenplay_audit.py                               ← Stage 3 Script Linter (Retention Map, Scorecard, W9/W10/W11, budgets)
│   ├── prompt_audit.py                                   ← Stage 4 Scene Prompt Linter (blocks, locks, separation, shots, D2–D5, footer); --docs lints core examples
│   ├── doc_range_check.py                                ← Keeps JIT StartLine/EndLine maps inside the referenced files
│   ├── genres\                                           ← Modular Genre Adapters (Layer 2)
│   │   ├── README.md
│   │   ├── action.md                                     ← Action, Martial Arts, Chase & Supernatural Combat
│   │   ├── drama.md                                      ← Social, Family & Healing Drama
│   │   ├── healing.md                                    ← Healing & Slice-of-Life (Engine 6, no villains)
│   │   ├── fantasy.md                                    ← Time-Travel, Portal Isekai, Xianxia & Supernatural Fantasy (TH3)
│   │   ├── microdrama.md                                 ← High-Velocity Viral Microdrama
│   │   ├── sitcom.md                                     ← Situation Comedy
│   │   ├── thriller.md                                   ← Detective Mystery, Folk Suspense & Survival Mind-Games
│   │   ├── scifi.md                                      ← Speculative Sci-Fi (Regime 2)
│   │   ├── horror.md                                     ← Horror & Folk Dread (zero gore)
│   │   └── romance.md                                    ← Romance & Romantic Drama
│   └── references\                                       ← The Cinematic Knowledge Engine (SSOT)
│       ├── 0-creative-doctrine.md                        ← Thinking Layer: Two-Layer Core, 6 Depth Laws, Spine & Plot Engine
│       ├── 0b-temporal-camera-grammar.md                 ← Temporal & Camera Grammar: Timing Physics & Canonical Syntax
│       ├── 0c-canonical-numbers.md                       ← Canonical Numbers: every count, duration, word & engagement budget
│       ├── 1-narrative-screenplay-architecture.md        ← Pillar 1: Narrative Structure, 20 Twists & 8 Dialogue Models
│       ├── 2-casting-worldbuilding-specification.md      ← Pillar 2: Cast Topology, 16:9 Sheets (Mẫu 1–3, 2B), 50 Styles, 30 Genres
│       ├── 2b-character-lines.md                         ← Character Lines (canonical cast system: roles, topologies, arcs, Arc Map)
│       ├── 3-cinematography-3d-staging.md                ← Pillar 3: 14 Scales, 4-Axis Angles & 3D Spatial Staging
│       ├── 3b-lighting-atmospheric-physics.md            ← Assistant 3B: 6-Point Lighting Contract & Atmosphere
│       ├── 3c-camera-master-grammar.md                   ← Camera Master Grammar (Director's working reference, read in full at Stage 4)
│       ├── 4-ai-video-prompt-compiler.md                 ← Pillar 4: Stateless Prompt Compiler, Handover Ledger & Minor Protection
│       └── 4b-diegetic-foley-sound-design.md             ← Assistant 4B: 4-Layer Diegetic Soundscape & Foley
└── output\<slug>\                                        ← Project Deliverables Package
    ├── project_rules.json                                ← Project-Specific Rules & Overrides (episode_runtime_s, ending_mode, fatality_policy…)
    ├── ep-NN-script.md                                   ← Saved Stage 3 script per episode (Markdown working file, audited by screenplay_audit.py)
    ├── prompts/ep-NN-scene-KK.md                         ← Saved Stage 4 scene prompt (Markdown working file, audited by prompt_audit.py)
    └── setting.html                                      ← Stage 2 SOLE HTML Deliverable: Pre-Production Resource Preparation File
```

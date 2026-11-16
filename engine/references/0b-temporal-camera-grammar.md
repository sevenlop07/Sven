# TEMPORAL & CAMERA GRAMMAR — The Single Source of Every Number
# (Speech rate, lip-sync windows, action and camera-move durations, clip density, canonical prompt syntax, 10s / 15s / 30s)

> **SINGLE SOURCE OF TRUTH FOR TIMING NUMBERS AND PROMPT SYNTAX.**
> Read together with `0-creative-doctrine.md` (which decides *what* a scene needs). This file decides *how long* things take and *how the prompt is written*.
> Any number elsewhere (Pillars 1, 3, 4, role files, skills) that conflicts with this file is superseded by this file.
> The numbers are **working assumptions calibrated for AI video generators**. Refine them with real generations and record each refinement in §11.

---

## §0 — WHAT IS A HARD CONSTRAINT HERE

| Item | Status |
|---|---|
| **Temporal-Kinetic-Vocal Equilibrium & Zero Tail-Cut Law (`~2.5 words/s` Safe AI Lip-Sync Standard)**: Every shot containing spoken dialogue MUST be sized to **`3.5s–4.5s`** ($\mathbf{T_{shot}} = \mathbf{T_{lead\text{-}in}} + \frac{\text{Words}}{2.5} + \mathbf{T_{followthrough}}$) and pair speech with at most **1 simple primary action (`One-Move Rule`)**. **STRICT BAN on placing spoken dialogue in the final `2.0s–3.0s` shot of any clip (`00:08-00:10` in `10s`; `00:12-00:15` / `00:13-00:15` in `15s`)!** All spoken dialogue MUST finish before the final shot so the terminal shot (`0 spoken words`) delivers a clean Visual Payoff / Physical Button / Somatic Reaction Settle without ever cutting off audio at the end of the video | Hard Constraint |
| **Zero Dead Air & State-Delta Directing Law (`100% Active Occupancy`)**: Every shot across the clip MUST maintain continuous purposeful physical action or interaction (never leave characters standing idle waiting out the clock). `[subject]:` locks the static `00:00` posture; `Shot 1..N` describes strictly the **state transition (`State A ➔ State B`)** in 1–2 natural observable sentences (`15–30w`), never repeating `[subject]:`'s static posture and strictly banning meta-instructions (*"speaking immediately from the opening second"*, *"finishes his sentence early"*) | Hard Constraint |
| Shots contiguous, non-overlapping, start at `00:00`, end at the clip duration `10s / 15s / 30s` (`Shot 1 (00:00-00:XX)` ... `Shot N`) | Hard Constraint |
| **Zero Cumulative Timestamps**: Every scene prompt MUST start at `00:00` for third-party AI generators; NEVER use cumulative episode timestamps like `(00:10-00:20)` in prompts | Hard Constraint |
| **Single `<<<Image X>>>` Declaration Law**: Declare `<<<Image X>>>` **ONLY ONCE** inside `[context]:`, `[subject]:`, and `[prop]:`. **NEVER repeat `<<<Image X>>>` inside `Shot 1..N`** | Hard Constraint |
| **Zero-Costume, Zero-Age & Minor Protection Policy (`Gates 3A, 3E & 3F` · `Pillar 4 §[10d]`)**: Strictly ZERO clothing/garment words (`in a black jacket`, `in a dark suit`, `skirt`) and ZERO numeric ages or age/hair/beard words (`32-year-old`, `young blonde`, `silver-bearded`) in visual prose; voice maturity and emotion are encoded in **ONE single parenthetical (`[Proper_Name] ([vocal timbre/maturity], [tone]): "..."`)**. Under the **Minor Protection Policy (`§[10d]`)**, when a character is under 18 or has child/teen proportions, omit adult glamour/body terms (`beauty/handsome appearance`, `body proportions`, `chest`, `shins`, `blush/flush`), adult marital roles, and child-abuse/intimidation triggers (`trembling`, `cowering`, `high-angle looming down`, punishment threats) | Hard Constraint |
| **1–2 Short Natural Sentences per Shot (`15–30w`)**: Each `Shot N` describes 1 clear state transition (`A ➔ B`) in natural prose; strictly zero mechanical `→` arrows | Hard Constraint |
| **Target-First Camera Grammar & Optical Prop Vector Law (`Quay Khóa Mục Tiêu Vào Đối Tượng Chính — Không Quay Theo Góc Nhìn Khán Giả`)**: Every shot MUST lock its camera axis and optical focus onto the **Primary Target Subject (`targeting [Proper_Name]` / `with focus locked on [Proper_Name]'s face`)** along the active line of interpersonal force (`Over-the-shoulder perspective from behind [Trigger] targeting [Target]`, `Reverse OTS from behind [Target] targeting [Trigger]`, or `Tight angled two-shot with focus locked on [Target]`). **STRICT BAN** on passive "Audience-Spectator" staging (lining characters up flat facing the viewer) and **STRICT BAN** on cheating/turning handheld props (mirrors, receipts, phone screens, contracts) toward the camera/audience instead of facing the Target Character who is looking at them! Keep full faces and eyes on the Target Axis in comedy, sitcom, romance, and direct confrontation (`Selective Face Obscuration` is an optional specialist tool for mysterious thriller silhouettes only, never forced into direct confrontations) | Hard Constraint |
| Canonical Unified Multi-Shot Storyboard syntax (§8) | Hard Constraint |

---

## §1 — CINEMATIC MENTAL MODEL, THE 5 SCENE ACTION STRUCTURES & EPISODE ORCHESTRATION

### 1.1 The 5 Hollywood Scene Action Structures (`10.0s` & `15.0s` — Driven by Structural Flow, NEVER a Rigid Single Timeline)
> **ANTI-FORMULA MANDATE**: A master film director NEVER forces every scene into a mechanical timestamp grid (`4s–4s–2s` or `3s–2s–3s–2s`). Shot count and individual shot duration flex organically according to the weight of the physical action and the exact length of any spoken line (while keeping the **final settle beat wordless [`0 spoken words`]** so audio never cuts off). Every `10.0s` or `15.0s` clip is architected from one of the **5 Core Dramatic Scene Structures**:

| Scene Type | Core Dramatic Flow Structure (`Macro-Flow Across the Clip`) | Flexible Adaptation (`10.0s` vs. `15.0s` — Never Fixed to 1 Timeline) |
|---|---|---|
| **1. Opening / Atmospheric Hook Scene (`Cảnh Mở Đầu & Gieo Mồi Tò Mò`)** | **`In Medias Res Motion ➔ Anomaly / Focus Narrowing ➔ Open Curiosity Hook`**:<br>• **Beat 1 (`Active Entry`)**: Open inside an ongoing physical action or environmental motion (headlights sweeping across blinds, a hand concealing an object, a character listening to a sound outside) — never a static character waiting for the camera.<br>• **Beat 2 (`The Anomaly / Trigger`)**: The camera narrows focus (`slow push-in` or `cut`) along the character's eyeline toward an unexpected stimulus (footsteps halting outside, a cast shadow, a misplaced item).<br>• **Beat 3 (`The Question Hook`)**: Close on a sharp somatic reaction or a concise spoken / `V.O.` question that pulls the viewer directly into Scene 02. | Can execute as **1 unbroken gliding push-in (`Continuous Take`)** narrowing from environment to eyes, or **2–3 fluid beats** narrowing from medium staging to close-up realization. |
| **2. Storytelling / Narrative / Internal Monologue Scene (`Cảnh Kể Chuyện / Tự Sự / Nội Tâm V.O.`)** | **`Visual Emotion Leads First ➔ Vocal / V.O. Lands on Ocular Shift ➔ Tactile Settle`**:<br>• **Beat 1 (`Image Leads`)**: The character interacts quietly with the space or a meaningful object (gazing through rain-streaked glass, fingers tracing an old keepsake, letting out a quiet breath) so visual emotion is felt before a word is heard.<br>• **Beat 2 (`Vocal / Inner Thought + Eye Shift`)**: As the camera holds close on the face, the narrative voice (`Inner Voice V.O.` with closed lips, or a calm spoken reflection paired with 1 gentle gesture) lands alongside a subtle shift in the eyes or brow.<br>• **Beat 3 (`Tactile / Somatic Landing`)**: Voice ceases; a small physical gesture (resting chin on arms, closing a notebook, looking toward the light) lets the emotion resonate. | Prefers **longer, unhurried takes (`1 continuous take` or `2–3 gentle shots`)** so the narrative voice has room to breathe without frantic cutting. |
| **3. Dialogue / Banter / Confrontation Scene (`Cảnh Đối Thoại / Tung Hứng / Đấu Trí`)** | **`Opening Probe/Mask ➔ Counter-Action / Evidence on Target Axis ➔ Checkmate Turn ➔ Wordless Somatic Payoff`**:<br>• **Beat 1 (`Probe / Social Mask`)**: Camera targets Speaker A (`OTS` past B). Speaker A pairs an initiating gesture (leaning in, offering a flattering smile, pressing a question) with the opening line.<br>• **Beat 2 (`Counter-Turn`)**: Axis flips along the 180° line to target the recipient. Speaker B counters with both a physical move (presenting evidence oriented directly at Speaker A's eyes, stepping closer) and a verbal reply.<br>• **Beat 3 (`Checkmate Turn` — expanded in multi-turn `15s` scenes)**: The decisive verbal or visual turn flips the power balance.<br>• **Beat 4 (`Silent Payoff Button`)**: Final beat (`0 spoken words`) captures the defeated/stunned/comedic physical reaction while protecting the prior line from audio tail-cut. | Shot durations flex to match **actual line length** (a 4-word barb needs a shorter window; a 10-word line needs a wider `3.5s–4.5s` window). `10s` typically carries `1–2` spoken turns + reaction; `15s` carries `2–3` rapid Ping-Pong turns + physical button. |
| **4. Clue Discovery / Micro-Visual Twist Scene (`Cảnh Phát Hiện Manh Mối / Lật Bài`)** | **`Normal Facade ➔ Macro / Close-Up Tactile Insert [Show, Don't Tell] ➔ Attitude Reversal`**:<br>• **Beat 1 (`Surface Routine`)**: A seemingly ordinary interaction (reaching to sign a deed, an embrace, reaching for a door handle).<br>• **Beat 2 (`Tactile Detail Insert`)**: Camera cuts to a close-up of the physical detail that exposes the truth (a finger tapping a brass keyring blocking the signature line, a deadbolt turning from the inside, a hidden mark).<br>• **Beat 3 (`Mask Drop & Reversal`)**: Cut back to the face as the social mask drops into cold clarity or shock, paired with a concise scalpel line or silent realization. | The insert shot is sized purely to the visual action (`~1.5s–2.5s`), framed between the setup beat and the psychological reversal beat. |
| **5. High-Velocity Action, Chase, Combat & Rapid-Cut Craft Montage (`Cảnh Hành Động / Truy Đuổi / Thực Chiến / Chuyển Cảnh Kỹ Năng Tốc Độ Cao` — `@CombatDirector`)** | **`Tension Ignition / High-Density Rapid Cuts (1.5s–2.0s) [0 Dialogue] ➔ Hard Stop / Impact / VFX ➔ Dominance / Precision Command ➔ Terminal Settle [0 Dialogue]`**:<br>• Covers **5 Kinetic Archetypes (`combat-director/SKILL.md` §1.1)**: *(1) Martial Arts & Duels (`6–8 Shots`)*, *(2) High-Speed Chases & Ambushes (`5–7 Shots`)*, *(3) High-Velocity Professional Craft & Hyper-Cut Whip-Montages (`7–9 Shots` of `1.5s–2.0s` — culinary flambé, emergency surgery, blacksmithing, bartending)*, *(4) Split-Second Rescues & Physical Crises (`6–8 Shots`)*, and *(5) Power Awakening & Relic Detonations (`6–8 Shots`)*.<br>• **High-Density Rapid-Cut Law (`1.5s–2.0s / shot`)**: Increase shot count (`5–9 Shots` in `15.0s`; `4–6 Shots` in `10.0s`) where each `1.5s–2.0s` rapid cut is written as **1 single punchy sentence (`12–22 words`) executing 1 single physical micro-strike (`1 verb + 1 impact/splash/spark`)** with **`>45°` scale/angle jumps** and **strictly `0 spoken dialogue`**.<br>• **Deceleration & Terminal Settle**: Hard stop into dominance or precision finish (optional short `2–6w` line in a `3.0s–3.5s` decelerated shot), followed by a wordless final settle shot (`0 spoken words`). | Routed to `@CombatDirector` (`Seedance 10s/15s`), scaling up to **`5–9 Shots` in `15.0s`** (`6 × 1.5s + 3 × 2.0s = 9 Shots` for Hyper-Cut Craft Montage; `6–8 Shots` for Rapid-Cut Martial Combat; `5–6 Shots` when pairing a long tracking sprint with rapid cuts). |

### 1.1b The 3-Part Micro-Structure Inside Every Shot (`Cấu Trúc Vi Mô Bên Trong Mỗi Shot — Zero Redundancy & Cross-Threshold Rule`)
Regardless of scene type or timestamp split, every `Shot N` inside the Action block is constructed from **3 Causal Layers** with **strictly zero token duplication between headers and prose**:
1. **Layer 1 — Target-Locked Camera & Speed Header (`Zero Top Slugline & Conditional Interior/Exterior Rule`)**:
   - **Zero Redundant Top Slugline**: Prompts start **directly with `Style:` ➔ `[context]:`**. Do NOT place a redundant `[Time] · [Int/Ext] · [Location]` slugline above `Style:`, because `[context]:` already defines the location, reference image (`<<<Image 1>>>`), time of day, and 5-vector environment, and a fixed top `Interior/Exterior` tag conflicts whenever a scene transitions between outdoors and indoors.
   - **Case A — Single-Space Scene (`Cùng 1 bối cảnh xuyên suốt clip` — Default)**: Because `[context]:` already locks the space, **omit `Interior,` / `Exterior,` from `Shot 1..N` headers**:
     `Shot N (00:XX-00:YY) - [Shot Scale], [Angle + Movement locked onto the Primary Target Subject], [Shot Speed]`
   - **Case B — Cross-Threshold Transition Scene (`Chuyển tiếp từ ngoài đường bước vào nhà / từ bối cảnh A sang bối cảnh B trong cùng 1 clip`)**: **ONLY when characters physically cross between `Exterior` and `Interior` (or between two distinct spaces) across shots within the same clip**, prefix each `Shot N` header with its active zone (`Exterior, [Shot Scale]...` $\to$ `Interior, [Shot Scale]...`) so the AI renders the spatial transition accurately.
2. **Layer 2 — State-Delta Action Prose (`Initiating Action ➔ Resulting Reaction / State Shift` in 1–2 natural sentences — `Zero Speed/Angle Repetition`)**:
   - Launch directly from the end-state of the previous beat (or `[subject]:` for `Shot 1`) without repeating static clothing/posture from `[subject]:` and **without repeating the `[Shot Speed]` phrase (`At blistering whip-fast speed...`, `At natural real-time speed...`) already declared in the `Shot N` header**.
   - Write `[Concrete physical trigger / action by Character A] ➔ [Immediate visible shift on Character A's expression, prop state, or Character B's reaction]`.
   - When a character speaks in that shot, pair speech with **1 simple primary gesture (`One-Move Equilibrium`)**; when the shot is silent, drive emotion through richer somatic and ocular movement.
3. **Layer 3 — Matched Vocal Line (Only on Beats With Speech)**:
   - `[Proper_Name / Audio Mode] ([vocal timbre/maturity], [delivery tone]): "[Concise line matched to the shot's time window]"`. Ensure vocal mode (`On-Screen`, `off-screen`, or `voice-over`) matches the on-screen mouth state and obeys conversational causality (`Gate 4C`).

### 1.1c Episode-Level Storytelling Orchestration (`Phối Hợp Các Loại Cảnh Để Dệt Thành 1 Tập Phim Hay`)
Individual scenes are only bricks; a Hollywood-caliber episode weaves the 5 Scene Structures above across a **4-Stage Episode Emotional Arc** governed by **3 Showrunner Orchestration Laws**:
1. **The 4-Stage Episode Symphony (`Đường Cong Phối Cảnh Trong 1 Tập Phim`)**:
   - **Stage I — Hook & Atmospheric Entry (`Opening 15–20%`)**: Combine **Type 1 (`Opening Hook`)** + **Type 2 (`Storytelling / V.O.`)** to plunge the viewer *in medias res* and plant the episode's burning question.
   - **Stage II — Escalating Friction & Investigation (`Middle 40–50%`)**: Alternate **Type 3 (`Dialogue Confrontation`)** with **Type 4 (`Clue Discovery / Micro-Visual Insert`)** so characters test tactics, hit obstacles, and uncover physical truths rather than talking in circles.
   - **Stage III — Peak Reckoning or Kinetic Climax (`Climax 20–25%`)**: Unleash an extended **`15.0s` Type 3 (`Multi-Turn Showdown / Sitcom Climax`)** or **`15.0s` Type 5 (`Action / Chase / Combat`)** where all accumulated pressure detonates.
   - **Stage IV — Aftermath Resonance & Cliffhanger (`Closing 10%`)**: Drop tempo into a brief **Type 2 (`Emotional Settle`)** so the climax lands emotionally, then pivot on a final **Type 4 (`Twist Reveal / Cliffhanger`)** that propels the viewer into the next episode.
2. **The 3 Showrunner Orchestration Laws**:
   - **Law A — Rhythmic & Structural Contrast (`Nén ↔ Xả` & `Động ↔ Tĩnh`)**: Never stack 3–4 consecutive scenes of the same structure or tempo. Follow a dialogue-dense scene with a visual/clue or internal `V.O.` scene; follow rapid multi-cut exchanges with a slow push-in take so compression makes the release hit harder.
   - **Law B — Causal Baton Relay (`"Vì Vậy / Nhưng Mà"` Across Every Scene Boundary)**: The closing image, question, or prop state of Scene $K$ MUST directly trigger the opening beat of Scene $K+1$ (`Therefore / But` — strictly zero disconnected `"And then"` filler scenes).
   - **Law C — Multi-Sequence Spatial Progression**: Move characters organically across `2–3` distinct spatial zones or perspectives across the episode (`TH1` for same-space continuation; `TH2` for purposeful location shifts).

### 1.2 Counting Units
- **Vietnamese** dialogue is counted in **syllables** (every whitespace token is one syllable: `Em mệt quá anh ơi` = 5 syllables).
- **English** dialogue is counted in **words**.
- Plan lines in **seconds and dramatic beats**, not just raw mechanical tokens.

### 1.3 The 4 Cinematic Continuity Locks & The 3-Case Continuity Reference Point Law (`TH1 / TH2 / TH3`)
When assembling discrete `10.0s` or `15.0s` AI video shots into a seamless cinematic sequence, every scene transition (`Sc K-1 ➔ Sc K`) is governed first by the **3-Case Continuity Reference Point Law (`workflow.md` §2.10, §8.3, §9.2)**:
- **Case 1 (`TH1 — CẦN THAM CHIẾU Khung Hình Cuối Cảnh Trước`: Same Continuous Moment in Time + Same Physical Location)**:
  The user sends the extracted **Static Terminal Frame (`Last Frame @00:10.0` or `@00:15.0`)** from Scene $K-1$ in chat so the Agent locks `00:00.0` of Scene $K$ (`[subject]:` and `[prop]:`) **100% verbatim** to the exact physical posture, hand-prop grip, eyeline, and architectural landmark visible in that ending frame.
- **Case 2 (`TH2 — KHÔNG THAM CHIẾU Khung Hình Cảnh Trước`: Scene 01, Different Location, Time Jump, or Character Lineup Switch)**:
  Scene $K$ does **NOT** reference Scene $K-1$'s spatial frame, and the Agent **NEVER asks the user to upload location/character reference images in chat**. Instead, the Agent reads all 5-Vector location, character, and Tier-1 prop specifications **directly from `output/<slug>/setting.html`** to write `[context]:`, `[subject]:`, and `[prop]:` (`<<<Image X>>>`), bridged via a Mode B Sequence Bridge (Match-Cut, Question Hook, Prop/Emotional Carry-Over, or Parallel Cross-Cut).
- **Case 3 (`TH3 — THAM CHIẾU NGOẠI LỆ Siêu Nhiên / Xuyên Không / Dịch Chuyển Không Gian`: Same Continuous Moment in Time + Instant Spatial Shift)**:
  In supernatural, portal, or time-travel (`xuyên không`) transitions, the user sends Scene $K-1$'s terminal frame so `[subject]:` and `[prop]:` at `00:00.0` preserve 100% of the character's exact body posture, mid-step momentum, and hand grip, while the Agent reads the New World/Era Location's `[context]:` directly from `output/<slug>/setting.html`.

Within any **Case 1 (`TH1`)** same-location sequence, four mandatory continuity locks guarantee that cuts feel natural, fluid, and coherent:

1. **Lock 1: Spatial & 180° Axis Gaze Vector Lock (Khóa Trục Không Gian & Đường Mắt Bất Biến)**:
   - *Screen-Direction Invariance*: If Character A is framed on Screen-Left looking toward Screen-Right, and Character B is on Screen-Right looking toward Screen-Left, this geometry **must never flip** across shot-reverse-shot cuts unless the camera physically orbits across the axis on screen. Record it in the Audit Card; inside Code Block 1 express it through architecture and eyelines (e.g. `Bradley at the side of the table facing Harold at the head chair`).
   - *Ground & Architectural Anchor*: Every shot within the same sequence must cite the identical floor/surface noun phrase and directional key light source to prevent AI latent background hallucinations.
2. **Lock 2: Kinetic Momentum Baton Relay & Clean Terminal Keyframe Landing (`Shot 4 / Shot 5`)**:
   - *The Relay & Clean Landing Principle*: In the final shot of the clip (`00:08-00:10` or `00:13-00:15`), the active character settles into a **Clean Dynamic Landing Pose** (clear orientation, grounded hand/prop contact, zero wild mid-swing motion blur) so the user can extract a razor-sharp terminal frame for Scene $K+1$ (`Case 1` or `Case 3`).
3. **Lock 3: Auditory Suture & Off-Screen `L-Cut` Dialogue**:
   - *Off-Screen `L-Cut` Dialogue Over Visual Inserts*: An off-screen speaker (`[Name] (outside the door / across the table / from behind, [tone])`) can deliver a short line over an interior tracking shot or a `2s` prop/lock close-up (`Shot 2`), suturing shots seamlessly.
4. **Lock 4: Physical Handover Ledger (Sổ Bàn Giao Trạng Thái Vật Lý & Đạo Cụ)**:
   - Recorded strictly in Code Block 2: Character 3D positions, facial expression at `00:10.0` (or `00:15.0`), prop physical states transfer 1:1 into the opening frame of Scene $K+1$.

### 1.4 Multi-Spatial Sequence Architecture (Giải Thoát Khỏi Chiếc Hộp Một Phòng)
- **The Anti-Box Mandate**: Sticking 10 consecutive scenes into a single cramped room destroys cinematic scale. Partition every episode into **2 to 3 dynamic physical Sequences** connected by Sensory Match-Cuts or Question Hooks.

---

## §2 — SPEECH RATE, TEMPORAL-KINETIC-VOCAL EQUILIBRIUM & ZERO TAIL-CUT LAW

Safe speech for AI video lip-sync operates at **`~2.5 words/second` (`~3.0 Vietnamese syllables/second`)**, governed by the mathematical formula from `Pillar 4 §1`:
$$\mathbf{T_{shot}} = \mathbf{T_{lead\text{-}in}} + \left(\frac{\text{Spoken Word Count}}{2.5\text{ wps}}\right) + \mathbf{T_{followthrough}}$$
Every shot containing spoken dialogue MUST be sized to **`3.5s – 4.5s`** (flexing with line length) and pair speech with at most **1 simple primary action (`One-Move Rule`)**, while the **final `2.0s – 3.0s` settle beat of every clip MUST have `0 spoken words` (`Zero Tail-Cut Law`)**. The timings below are **illustrative reference proportions (never a rigid mechanical grid)** — actual shot counts (`1–4 shots` in `10s`; `3–5 shots` in `15s`) and durations flex organically according to the **5 Scene Action Structures (§1.1)**:

| Clip Duration & Engine | Flexible Storyboard Flow (Reference Proportions Only) | Spoken / Vocal Window (`3.5s–4.5s / turn`) | Terminal Settle Beat (`0 Spoken Words`) | Total Spoken Budget |
|---|---|---|---|---|
| **`10.0s` Scene (`@Director` — Opening, Narrative/V.O., Dialogue, or Clue Twist)** | **`1–4 Shots`** flexing by scene structure (e.g., `10s` continuous take, `5s–5s`, `4s–4s–2s`, or `3.5s–2s–2.5s–2s`) | Opening / middle turns (`On-Screen`, `Off-Screen L-Cut`, or `V.O.`), finishing by `~00:08.0` | **Final `2.0s` (`~00:08.0-00:10.0` = `0 spoken words`)**: Visual Payoff / Curiosity Hook / Somatic Settle | **`0 – 22 words total`** (`0–2` turns; `0w` in final beat) |
| **`15.0s` Dialogue / Sitcom / Showdown (`@Director`)** | **`3–4 Shots`** flexing by turn length (e.g., `4s–4s–4s–3s` or `4.5s–4s–3.5s–3s`) | `2–3` conversational / confrontation turns across `Shot 1..N-1` (finishing by `~00:12.0`) | **Final `2.5s–3.0s` (`~00:12.0-00:15.0` = `0 spoken words`)**: Physical Comedy Button / Visual Fallout | **`18 – 34 words/syllables total`** (`2–3` turns; `0w` in final shot) |
| **`15.0s` Action / Combat / Rapid-Cut Montage (`@CombatDirector` `[⚡ SEEDANCE]`)** | **`5–9 Shots`** scaling up for high-velocity cuts (e.g., `9 Shots` [`6 × 1.5s + 3 × 2.0s`] for Hyper-Cut Craft; `7 Shots` for Martial Combat; `5 Shots` with long tracking chase) | `0w` across all `1.5s–2.5s` rapid cuts (optional `2–6w` line in a `3.0s–3.5s` decelerated shot before final cut) | **Final `1.5s–2.5s` (`0 spoken words`)**: Terminal Visual Fallout / Masterpiece Settle | **`0 – 14 words total`** (`0w` in rapid cuts & final shot) |

**Core Spoken & Timing Laws**:
- **Zero Tail-Cut Law (Hard Constraint)**: Never place spoken dialogue inside the final `2.0s–3.0s` shot of a clip (`00:08-00:10` in `10s`; `00:12-00:15` / `00:13-00:15` in `15s`). Completing all speech before the final shot guarantees zero mid-word audio truncation and a clean mouth-closed terminal frame (`Last Frame`).
- **Zero Dead Air & Continuous Ping-Pong (`100% Active Occupancy`)**: Never leave middle shots silent in a conversational or sitcom scene, and never leave characters standing idle after finishing a short line. Every shot must maintain active physical or vocal momentum.
- **Zero Meta-Instructions in Action Prose**: Regulate speech timing through shot duration (`3.5s–4.5s`) and concise line length (`8–12 words/syllables`), strictly banning meta-phrases like *"speaking immediately from the opening second"* or *"finishes his sentence early"*.

---

## §3 — LIP-SYNC WINDOWS & OFF-SCREEN `L-CUT` DIALOGUE

### 3.1 Lip-Sync Timing Windows, Clean Terminal Frame Mouth-Closure & Action Vocal Economy
- A spoken line **starts ≥ 0.5 s** after its shot begins and **ends ≥ 0.8 s** before the shot ends so lips close cleanly before the cut.
- **Zero Dialogue in the Final Shot (`00:08-00:10` in `10s`; `00:12-00:15` / `00:13-00:15` in `15s`) & During High-Speed Chase/VFX Shots**: Keep speech strictly inside `3.5s–4.5s` opening and middle turn windows (`00:00-00:08` in `10s`; `00:00-00:12/13` in `15s`), leaving the final `2.0s–3.0s` shot 100% wordless (`0 spoken words`) for the visual payoff / somatic reaction settle.

### 3.2 Target-First Camera Axis, Off-Screen `L-Cut` & When (Not) to Use Selective Face Obscuration
1. **Target-First Camera Axis & Optical Prop Vector Law (`Primary Default Across All Genres`)**:
   - Before writing any shot header, ask: **"Who is the Primary Target Subject receiving or delivering the psychological/physical force in this beat?"**
   - Anchor the camera directly along the **Target Axis (`OTS from behind [A] targeting [B]`, `Reverse OTS from behind [B] targeting [A]`, or `Tight angled two-shot with focus locked on [Target]'s face`)**.
   - **Optical Prop Orientation**: Whenever Character A holds up a prop (a compact mirror, a store receipt, a phone screen, a document) to confront Character B, the active surface of the prop and Character A's eyeline MUST point physically at Character B — **never rotate the prop flat toward the audience/lens** (which causes optical reflection paradoxes where a mirror faces the viewer instead of the character looking into it).
2. **Off-Screen `L-Cut` & `Voice-Over (V.O.)` Audio**:
   - Allows an off-screen speaker (`[Name] (off-screen, [vocal timbre], [tone]): "..."`) or an internal monologue (`Inner Voice (voice-over, [vocal timbre], [tone]): "..."`) to play while the camera holds on the on-screen character's non-speaking expression or a tactile prop insert, ensuring vocal mode and mouth state never conflict and conversational causality (`Gate 4C`) remains natural.
3. **Selective Face Obscuration (`Optional Specialist Tool — NEVER Force Into Comedy or Direct Showdowns`)**:
   - Using `The camera avoids [Name]'s full face, showing only [Name]'s lower face, jawline...` or `back silhouette` is reserved **exclusively** for mysterious/unseen crime-lords or cold thriller scenes where hiding a predator's identity is the dramatic point. **Strictly do NOT cut away to a disembodied chin or tabletop during comedy, sitcom, or direct interpersonal showdowns** where the clash between full faces and eyes on the Target Axis carries the emotional punch!

---

## §4 — SHOT CAPACITY BY WINDOW (`1.5s` · `2s` · `3s` · `4s`) & THE 5-TIER `[Shot Speed]` TAXONOMY

### 4.1 Shot Capacity by Window
| Shot Window | Typical Role in Storyboard | Action Capacity (`Natural Prose — Zero → Arrows`) | Spoken Capacity |
|---|---|---|---|
| **`1.5s – 2.0s` Rapid-Cut Micro-Strike Shot** (`@CombatDirector` `5–9 Shot` Montages & Martial Exchanges) | **High-Velocity Rapid Cut (`Cut on Kinetic Peak`)** (e.g., blade mince, pepper grind, gas ignite, parry, rib strike, mid-air toss) | **1 single punchy sentence (`12–22 words`) executing 1 single physical micro-strike (`1 verb + 1 immediate physical impact/splash/spark`)** | **Strictly `0 spoken words`** (100% kinetic speed & percussive Foley) |
| **`2.0s – 3.0s` Shot** (`00:08-00:10`, `00:12.5-00:15`, or mid-clip `Prop/VFX Insert`) | **Terminal Visual Payoff / Reaction Settle (`Final Shot`)** OR Mid-Clip Tactile Prop/VFX/Flame Insert | **1 crisp physical payoff, flambé burst, slice reveal, or somatic reaction transition** (`15–26 words` of natural prose) | **Strictly `0 spoken words`** (100% visual payoff, Foley & mouth-closed settle) |
| **`3.5s – 4.5s` Shot** (`00:00-00:04`, `00:04-00:08`, `00:08-00:12`) | **Primary Spoken Turn + Active Gesture (`One-Move Rule`)** OR Full-Speed Long Tracking Chase | **1 primary physical action + 1 facial transition (`State A ➔ State B`)** (`18–30 words` of natural prose; zero static repetition from `[subject]:`) | **`1 natural spoken line` (`6–12 words` / `8–13 VN syllables`)** (`0 words` if pure tracking chase) |

### 4.2 The 5-Tier `[Shot Speed]` Taxonomy (`5 Cấp Độ Tốc Độ Video Khóa Trực Tiếp Trên Tiêu Đề Shot N`)
Every `Shot N` header MUST end with one of the **5 Canonical `[Shot Speed]` Tags** (`Shot N (00:XX-00:YY) - [Shot Scale], [Angle/Move Targeting Subject], [Shot Speed]`). Never use numeric multipliers (`1.0x`, `2.3x`), frame rates (`24fps`, `120fps`), or camera hardware names (`Phantom`) in Code Block 1 (`Gate 3D`), and never repeat the speed tag at the start of the action sentence below the header:

| Speed Tier | Canonical `[Shot Speed]` Tag in `Shot N` Header | Physical & Temporal Behavior | Mandatory Usage & Vocal Rule |
|---|---|---|---|
| **Tier 1 (Baseline Real-Time)** | **`natural real-time speed`** | Natural human biological cadence (`~2.5 words/s`), organic breathing, smooth facial and hand transitions, zero time-warping. | **Mandatory for 100% of shots with spoken dialogue (`lip-sync`)**, conversational reactions (`@Director`), checkmate lines, and final settle shots (`Final Shot`). |
| **Tier 2 (Decisive / Snappy Real-Time)** | **`snappy real-time speed`** / **`crisp real-time speed`** | Brisk, decisive, zero-hesitation real-time execution (snapping a burner knob, dropping butter into a pan, slicing steak in one clean stroke, tapping a keyring). | Tactile prop/clue inserts, precision craft steps, and the **real-time snap-back cut** immediately following a slow-motion shot (`0 spoken words`). |
| **Tier 3 (High-Impact Real-Time)** | **`explosive real-time speed`** | Sudden high-force physical collision, recoil, or combustion burst (pressing steak into smoking oil with splatter, pommel strike to ribs, wrist-lock throw into steel shutter, rune trap halt). | Heavy martial arts impacts, physical collisions, door breaches, and sudden fire/VFX eruptions (`Strictly 0 spoken words`). |
| **Tier 4 (Hyper-Fast Whip Velocity)** | **`blistering whip-fast speed`** | Peak human kinetic velocity with natural motion blur on rapid hands/weapons/legs (blade mincing garlic in a rhythmic blur, wrist-snap skillet toss, rapid parry flurry, full-speed alley sprint). | `1.5s–2.0s` rapid-cut whip-montage beats (`@CombatDirector`) and full-speed tracking chases (`Strictly 0 spoken words`). |
| **Tier 5 (Time-Dilated Suspension)** | **`ultra-slow-motion suspension`** | Time-dilated mid-air suspension capturing micro-fluid, flame, and particle physics (translucent amber flambé fire ribbons, rotating Wagyu steak, floating butter droplets, rain droplets sliced by a blade). | Selective `2.0s–3.5s` mid-clip visual peaks inside a **Speed-Ramp Curve (`Tier 4/2 Launch ➔ Tier 5 Ultra-Slow-Motion Peak ➔ Tier 2/1 Real-Time Settle`)**. **Strictly `0 spoken words`!** |

---

## §5 — CAMERA MOVES: DURATION AND DIALOGUE COMPATIBILITY

Every move needs a motive (Doctrine §2.3). These are the **minimum stable durations** for AI generators.

| Move | Minimum stable duration | Lip-sync during the move? | Typical motive |
|---|---|---|---|
| Static (locked frame, living subjects) | any | ✅ | Gravity, witness, the peak |
| Slow push-in, MS → MCU | 3 – 5 s | ✅ | Pressure, realization |
| Slow push-in, MS → CU | 5 – 8 s | ✅ | Deep realization |
| Slow pull-out, CU → MS / MS → WS | 3 – 5 s / 5 – 8 s | ✅ / ⚠️ voice only once the face is small | Isolation, judgment |
| Pan or tilt reveal | 2 – 4 s | ✅ after the reveal lands | Reveal information |
| Truck / lateral glide | 3 – 5 s | ✅ when slow | Follow attention, parallax |
| Arc 90° | ≥ 3 s | ⚠️ only in the slow final third | Power shift, re-framing |
| Arc 180° | ≥ 5 s | ⚠️ lines only at the start or after the arc settles | Shot / reverse without a cut |
| Orbit 360° | whole clip | ❌ except in the final locked segment | Encirclement |
| Pedestal / crane | 3 – 5 s | ❌ while traveling; ✅ once it lands | Power shift, grand reveal |
| Rack focus | 1 – 2 s | ✅ | Shift attention between planes |
| Gentle handheld drift | any | ✅ (gentle only) | Intimacy, documentary closeness |
| Violent handheld shake | any | ❌ | Panic, chaos |
| Whip pan | 0.3 – 0.5 s | ❌ | Shock redirection, transition |
| Dolly zoom, crash zoom | 1.5 – 3 s | ❌ | Seismic shock |

Limits:
- **Track A**: at most **2 chained moves per 10 s** (for example, a push-in followed by an arc).
- **Track B**: at most **1 move per shot**; static shots are welcome.
- **Track AB (hybrid)**: the continuous take may chain up to **2 moves**; every other shot carries at most **1 move**.

---

## §6 — SHOTS AND CUTS (`10.0s` & `15.0s` BY DRAMATIC ENGINE — FLEXIBLE TIMESTAMPS & ZERO TAIL-CUT LAW)

> **Structural Flow Over Fixed Timelines**: Shot counts and timestamp splits in the table below are **illustrative reference proportions, NEVER a fixed mechanical template**. Always size each shot dynamically to its action weight and spoken line length per the **5 Scene Action Structures (§1.1)** while keeping the final `2.0s–3.0s` settle beat wordless (`0 spoken words`).

| Clip Duration & Engine | Flexible Multi-Shot Storyboard Range | Reference Timing Examples (Flex by Beat & Line Length) | Key Camera, Action & Vocal Rhythm |
|---|---|---|---|
| **`10.0 s` Standard Scene (`@Director` — Opening, V.O., Dialogue, Clue Twist)** | **`1 – 4 Shots`** (`Shot 1..N`) | e.g., `10s` continuous take, `5s–5s`, `4s–4s–2s`, or `3.5s–2s–2.5s–2s` | • Structure follows Scene Type (§1.1): *Opening Hook*, *Storytelling/V.O.*, *Dialogue*, or *Clue Insert*<br>• Spoken/V.O. turns finish by `~00:08.0`<br>• **Final Beat (`~00:08-00:10` · `2.0s` = `0 spoken words`)**: Visual Payoff / Curiosity Hook / Somatic Settle |
| **`15.0 s` Dialogue / Sitcom / Dramatic Showdown (`@Director`)** | **`3 – 4 Shots`** (`Shot 1..N`) | e.g., `4s–4s–4s–3s` or `4.5s–4s–3.5s–3s` | • **Continuous Ping-Pong (`Zero Dead Air`)**: `2–3` active turns across `Shot 1..N-1` (finishing by `~00:12.0`) $\to$ **Final Shot (`2.5s–3.0s`) Wordless Visual Payoff / Physical Comedy Button (`0 spoken words`)** |
| **`15.0 s` High-Velocity Action / Combat / Rapid-Cut Montage (`@CombatDirector` `[⚡ SEEDANCE · 15.0s]`)** | **`5 – 9 Shots`** (`Shot 1..N`) | • **Hyper-Cut Craft / Culinary (`9 Shots`)**: `6 × 1.5s + 3 × 2.0s`<br>• **Rapid-Cut Combat (`7 Shots`)**: `4 × 1.5s + 2.5s + 4s + 2.5s`<br>• **Tracking Chase (`5 Shots`)**: `3.5s–4s–2.5s–3s–2s` | • **High-Density Cut-on-Peak**: Each `1.5s–2.0s` rapid cut executes **1 single micro-strike sentence (`12–22w`, `0 dialogue`)** with `>45°` scale/angle jumps $\to$ Optional decelerated checkmate shot $\to$ **Final Shot (`1.5s–2.5s`) Wordless Visual Settle (`0 spoken words`)** |
| **`30.0 s` (Explicit User Request Only)** | **`8 – 10 Shots`** (`Shot 1..10`) | `3.0s – 4.0s` per shot across 3 mini-acts | Full 3-act sequence ending on a `2.5s–3.0s` wordless visual payoff shot |

- Minimum shot length: **≥ 1.5 s** (`1.5s–2.0s`) for `@CombatDirector` rapid-cut micro-strike shots (`1 single sentence of 12–22w`, `0 spoken words`); **≥ 2.0 s** for standard silent inserts and terminal visual payoff shots; **≥ 3.5 s** (`3.5s–4.5s`) for any shot containing spoken dialogue.
- Never repeat the exact same shot scale and angle in two consecutive shots; derive every scale (distance/information), angle (power balance), and movement (motive) from dramatic intent along the 180° axis.
- **1–2 Short Natural Sentences per Shot (`12–22w` single sentence for `1.5s–2.0s` rapid cuts; `15–30w` for `3.0s–4.5s` shots)**: Each `Shot N` describes **1 clear state transition (`State A ➔ State B`)** in natural cinematic prose. Strictly ban mechanical `→` arrows, static `[subject]:` repetition, and meta-instructions.

---

## §7 — DENSITY PER CLIP (BY DURATION & ENGINE)

| Clip Type & Owner | Flexible Shot Range | Spoken / Vocal Lines | Total Spoken Word Budget | Terminal Beat Law (`Final 1.5s–3s`) |
|---|---|---|---|---|
| **`10.0s` Scene (`@Director` — Opening, V.O., Dialogue, Twist)** | `1 – 4 Shots` (flex by structure) | `0 – 2` lines (`On-Screen`, `O.S.`, or `V.O.`) | **`0 – 22 words total`** | **Strictly `0 spoken words`** in `~00:08-00:10` (Visual/Somatic Settle) |
| **`15.0s` Sitcom / Dialogue / Showdown (`@Director`)** | `3 – 4 Shots` (flex by turn length) | `2 – 3` lines (`Shot 1..N-1`) | **`18 – 34 words/syllables total`** | **Strictly `0 spoken words`** in `~00:12-00:15` (Physical Button / Payoff) |
| **`15.0s` Action / Combat / Rapid-Cut Montage (`@CombatDirector`)** | **`5 – 9 Shots`** (`1.5s–2.0s` rapid cuts) | `0 – 1` short line (`0w` in pure `9-Shot` whip-montage) | **`0 – 14 words total`** (`0w` in rapid cuts & final shot) | **Strictly `0 spoken words`** in final `1.5s–2.5s` shot (Terminal Fallout / Masterpiece Settle) |
| **Pure Visual / Atmospheric Hook or Insert Scene (`Model 0`)** | `1 – 4 Shots` (`10s`) | `0` lines | **`0 words`** (100% visual discovery & Foley) | Pure visual payoff |

---

## §8 — CANONICAL UNIFIED MULTI-SHOT STORYBOARD PROMPT SYNTAX (`100% PHƯƠNG ÁN MỚI` — DOUBLE-LOCK `<<<Image X>>> (fully_preserved - ...)` + GENDER SKIN/MAKEUP SUB-LOCK & ZERO TAIL-CUT LAW)

> **Important Note on Shot Timestamps in Templates 8.1 & 8.2**: The timestamp splits shown below (`00:00-00:04`, `00:04-00:08`, `00:08-00:10`, etc.) are **illustrative reference examples for a Confrontation/Dialogue scene and an Action scene**. When compiling an **Opening Hook Scene**, a **Storytelling / `V.O.` Scene**, or a **Clue Discovery Scene**, adapt the shot count (`1–4 shots` in `10s`; `3–5 shots` in `15s`) and durations organically to fit the **5 Scene Action Structures (§1.1)** while keeping the headers, footer, and `0 spoken words` in the final settle beat invariant.

### 8.1 Template A — Default `10.0s` Scene (`@Director` · `3–4 Shots` With `0 Spoken Words` in Final Shot)
> **Anti-Plastic AI Optical Standard (`3b-lighting-atmospheric-physics.md` §1.1), Zero Top Slugline & Per-Shot Speed Parameter (`[Shot Speed]`)**:
> 1. **Erase the Fake AI Look (`Khử Mùi Nhựa AI` — Strictly ZERO `35mm` / Lens / Hardware Numbers per `Gate 3D`)**: In Live-Action `Style:`, lock **`Realistic Live-Action Film, matte skin and surface finish with zero plastic or oily sheen, subtle organic film grain, muted natural color tones, physical light falloff`** (in 3D Semi-Real CGI, lock **`satin-matte skin shader with zero plastic doll sheen, balanced muted tones`**), and always declare **real physical light sources** in `[context]:` (`harsh overhead fluorescent tube`, `direct tungsten desk lamp`, `filtered window daylight`) instead of vague `"cinematic lighting"`. **STRICTLY BAN `35mm`, `50mm`, `24fps`, `1.0x`, or camera names (`Phantom`, `Arri`), as `35mm` triggers framing distortion and film-border artifacts!**
> 2. **Zero Redundant Top Slugline & Conditional `Interior / Exterior` Shot Prefix Law**:
>    - **Start Directly with `Style:` ➔ `[context]:`**: Never put a `[Time] · [Int/Ext] · [Location]` line above `Style:`. `[context]:` is the sole authority for location name, `<<<Image 1>>>`, time of day (`, night.` / `, morning.`), and environment.
>    - **Single-Space Clip (`Default — 95% of scenes`)**: Omit `Interior,` / `Exterior,` from `Shot 1..N` headers (`Shot N (00:XX-00:YY) - [Shot Scale], [Angle/Move Targeting Subject], [Shot Speed]`).
>    - **Cross-Threshold Transition Clip (`Moving from Exterior street into Interior room or vice versa within the same clip`)**: Include `Exterior,` or `Interior,` on each `Shot N` header (`Shot 1 (00:00-00:04) - Exterior, ...` $\to$ `Shot 2 (00:04-00:08) - Interior, ...`) ONLY when shots cross between distinct spaces.
>    - **Per-Shot Speed (`[Shot Speed]`)**: Declare the playback velocity once at the tail of the `Shot N` header (never repeat `At real-time speed...` inside the action sentence below):
>      * **`natural real-time speed`**: Mandatory for **100% of spoken dialogue shots (`lip-sync`)**, dramatic reactions, and terminal settle shots.
>      * **`blistering whip-fast speed` / `snappy real-time speed` / `explosive real-time speed`**: Used for rapid-cut cooking prep, martial strikes, and fast chases (`@CombatDirector`).
>      * **`ultra-slow-motion suspension`**: Used selectively for `0-dialogue` mid-air fluid/flame/raindrop suspension shots in a **3-Stage Speed-Ramp Curve (`blistering whip-fast speed [Shot 1] ➔ ultra-slow-motion suspension [Shot 2, 0 spoken words] ➔ crisp/natural real-time speed [Final Shot, 0 spoken words]`)**.

```text
Style: [Visual Style Specification — e.g., Realistic Live-Action Film, flawless velvet-matte or natural matte skin finish with zero plastic or oily sheen, subtle organic film grain, muted natural color tones, physical light falloff, crisp real-time motion, zero slow-motion].

[context]:
[Evocative Location Name in Natural English] <<<Image 1>>> (fully_preserved - same architectural layout, furniture, props and lighting throughout), [time of day]. [5-Vector Environmental Specification: architectural layout & full fixed furniture inventory, physical key lighting source & direction without Kelvin, shadow behavior, and atmospheric mood].

[subject]:
[Proper_Name_Female] <<<Image 2>>> (fully_preserved - same face, hair color, makeup and outfit throughout; only her head, eyes, mouth and expressions move.): [Initial 3D architectural anchor and posture], [hand/prop contact state at 00:00 — strictly ZERO specific clothing/garment words and ZERO numeric ages or specific hair/beard words], [eyeline toward counterpart or landmark] — the only [Proper_Name_Female] in frame.
[Proper_Name_Female]'s skin and makeup: fully_preserved - [Select 1 of 4 Female Skin & Makeup Schools matching the reference image: e.g., flawless porcelain velvet-matte skin throughout with soft rosy blush on the cheeks and nose tip, crisp wispy eyelashes, natural watery eye reflection, and soft gradient rose lips]; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.
[Proper_Name_Male] <<<Image 3>>> (fully_preserved - same face, hair color and outfit throughout; only his head, eyes, mouth, hands and expressions move.): [Initial 3D architectural anchor and posture within arm's reach if interacting physically], [hand/prop contact state at 00:00 — strictly ZERO specific clothing/garment words and ZERO numeric ages or specific hair/beard words], [eyeline toward counterpart or landmark] — the only [Proper_Name_Male] in frame.
[Proper_Name_Male]'s skin: fully_preserved - [Select 1 of 3 Male Skin Schools matching the reference image: e.g., clean smooth velvet-matte / real unretouched dry matte masculine skin throughout with sharp jawline definition, crisp eyebrows and eyelashes, natural moisture in his eyes, and natural matte lips]; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.
*(Gender, Skin/Makeup School & Motion-Scope Rules in `[subject]:`:
  1. **Motion-Scope Adaptation (after `;`)**: Use `; only her/his head, eyes, mouth and expressions move.` when torso/hands stay anchored; use `; only her/his head, eyes, mouth, hands and expressions move.` when hands manipulate a prop; use `; natural head, eye, expression and body movement.` for full-body motion.
  2. **4 Female Skin & Makeup Schools (`[Name]'s skin and makeup: fully_preserved - ...`)**:
     • **School F1 (Douyin Jiejie / High-Fashion Asian Glam)**: `flawless porcelain velvet-matte skin throughout with soft rosy blush on the cheeks and nose tip, crisp wispy eyelashes, natural watery eye reflection, and soft gradient rose lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
     • **School F2 (K-Drama Clean Satin-Matte Natural Glow)**: `clean smooth satin-matte skin throughout with a subtle natural warm flush, delicate crisp eyelashes, clear moist eyes, and soft coral-pink tinted lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
     • **School F3 (Classical / Xianxia Jade-Porcelain)**: `flawless jade-porcelain matte skin throughout with refined classical eye definition, crisp eyelashes, luminous moist eyes, and classic vermilion-rose lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
     • **School F4 (Grounded Western / Realistic Cinema Matte)**: `real unretouched dry matte skin throughout with natural skin texture, understated makeup, crisp individual eyelashes, natural moisture in her eyes, and soft natural lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
  3. **3 Male Skin Schools (`[Name]'s skin: fully_preserved - ...` — omit `makeup` from Line 1 and omit `blush/gloss` from Line 2)**:
     • **School M1 (Asian Male Lead / CEO Clean Velvet-Matte)**: `clean smooth velvet-matte masculine skin throughout with sharp jawline definition, crisp eyebrows and eyelashes, natural moisture in his eyes, and natural healthy matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
     • **School M2 (Grounded Masculine Dry Matte)**: `real unretouched dry matte masculine skin throughout with natural fine pores, crisp eyebrows and eyelashes, natural moisture in his eyes, and natural matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
     • **School M3 (Rugged Warrior / Mature Patriarch Matte)**: `rugged dry matte masculine skin throughout preserving natural facial lines and texture, crisp eyebrows, clear natural eye moisture, and natural matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
  4. **3 Animation Skin & Shader Schools (`A1–A3` — Mandatory When `Style:` Is 3D CGI, Pixar, or 2D Anime so AI Never Mixes Real Human Pores Into Animation or Turns 2D Into 3D)**:
     • **School A1 (3D Semi-Real CGI / Unreal Engine 5 / 3D Donghua)**:
       - *Female*: `[Name]'s skin and makeup: fully_preserved - smooth 3D satin-matte skin shader throughout with soft subsurface scattering, delicate rosy blush, crisp 3D eyelashes, luminous expressive eyes, and soft gradient lips; no glossy plastic doll sheen, no oily specular glare, not waxy.`
       - *Male*: `[Name]'s skin: fully_preserved - clean 3D satin-matte masculine skin shader throughout with natural subsurface scattering, sharp sculpted jawline, crisp eyebrows and eyelashes, clear expressive eyes, and natural matte lips; no glossy plastic doll sheen, no oily specular glare, not waxy.`
     • **School A2 (3D Stylized Pixar / Disney Animation)**:
       - *Female*: `[Name]'s skin and makeup: fully_preserved - soft stylized 3D velvet-matte skin throughout with a warm subsurface glow, gentle rosy cheeks, crisp stylized eyelashes, expressive glossy eyes, and clean soft lips; no hard plastic toy shine, no greasy glare, no photorealistic rough pores.`
       - *Male*: `[Name]'s skin: fully_preserved - soft stylized 3D matte skin throughout with a warm subsurface glow, clean sculpted features, expressive eyes, and natural matte lips; no hard plastic toy shine, no greasy glare, no photorealistic rough pores.`
     • **School A3 (2D Anime / Manga / Webtoon / Ghibli Cel-Shaded)**:
       - *Female*: `[Name]'s skin and makeup: fully_preserved - clean 2D cel-shaded skin tones throughout with crisp hand-drawn line art, soft anime cheek blush, sharp expressive anime eyes with crisp catchlights, and clean tinted lips; no 3D plastic shading, no photorealistic pores, no smudged linework.`
       - *Male*: `[Name]'s skin: fully_preserved - clean 2D cel-shaded masculine skin tones throughout with crisp hand-drawn jaw and facial line art, sharp expressive anime eyes, and clean natural lips; no 3D plastic shading, no photorealistic pores, no smudged linework.`
  5. **Minor Protection (`< 18` years old — `§[10d]`)**: Omit `makeup` in Line 1 and use `[Name]'s skin: fully_preserved - clean natural matte skin throughout; no oily shine, not plastic, not waxy.`)*

[prop]:
[Canonical Tier-1 Prop/Weapon Name] <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): [Exact 00:00 resting placement OR character hand-grip state] — the only [Canonical Tier-1 Prop/Weapon Name] in frame. *(Omit `[prop]:` if the scene has no Tier-1 Hero Prop/Weapon)*

[sound]:
[Ambient room/outdoor tone, synchronized tactile Foley sounds tied to shots, and acoustic tension. Strictly zero background music].

Shot 1 (00:00-00:04) - [Medium close-up], [over-the-shoulder perspective from behind Proper_Name_B targeting Proper_Name_A], [natural real-time speed]
[1–2 short natural sentences (15–30w) describing Proper_Name_A's active physical gesture and expression shift (State Delta) locked on the Target Axis — NO static [subject]: repetition, NO speed/camera repetition, NO <<<Image X>>> tag repeated here, NO clothing/age/skin-texture words].
[Proper_Name_A] ([vocal timbre/maturity], [delivery tone]): "[Line 1: 6–12 words/syllables]"

Shot 2 (00:04-00:08) - [Medium close-up], [reverse over-the-shoulder perspective from behind Proper_Name_A targeting Proper_Name_B], [natural real-time speed]
[1–2 short natural sentences describing Proper_Name_B's decisive prop action aimed directly at Proper_Name_A along the Target Axis (e.g., sliding the tarnished brass truck keyring onto the contract toward Proper_Name_A and tapping it twice while locking a cold gaze on Proper_Name_A)].
[Proper_Name_B] ([vocal timbre/maturity], [calm understated tone]): "[Checkmate Line 2: 5–12 words/syllables]"

Shot 3 (00:08-00:10) - [Medium close-up], [over-the-shoulder perspective from behind Proper_Name_B targeting Proper_Name_A's face], [natural real-time speed]
[1–2 short natural sentences describing the wordless terminal visual payoff / somatic reaction settle locked on the Target Subject (0 spoken words): e.g., "Seen past Proper_Name_B's shoulder in the foreground, Proper_Name_A's polite smile drains completely as Proper_Name_A's throat tightens in a hard swallow and fingers slowly release the pen."].

Master-level cinematography and composition, smooth dynamic camera pacing, atmospheric sound design.
Strict visual consistency: maintain 100% identical facial features, matte skin texture, hair color, makeup, exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.
Do not generate oily sweat shine, greasy forehead or nose glare, waxy plastic skin, subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.
```

### 8.2 Template B — `15.0s` Scenes: Mode B1 (`@Director` Target-First Dialogue/Sitcom Ping-Pong `4s–4s–4s–3s`) & Mode B2 (`@CombatDirector` Action/Chase `3.5s–4s–2.5s–3s–2s`)

#### Mode B1 — `15.0s` Target-First Dialogue / Sitcom / Dramatic Showdown (`@Director` · `4 Shots: 4s–4s–4s–3s` · `0 Spoken Words` in `Shot 4`)
```text
Style: [Visual Style Specification].

[context]:
[Evocative Location Name in Natural English] <<<Image 1>>> (fully_preserved - same architectural layout, furniture, props and lighting throughout), [time of day]. [5-Vector Environmental Specification].

[subject]:
[Proper_Name_A] <<<Image 2>>> (fully_preserved - same face, hair color, makeup and outfit throughout; only her head, eyes, mouth, hands and expressions move.): [Initial 3D architectural anchor, posture, hand state, and eyeline at 00:00 — ZERO specific clothing/age words] — the only [Proper_Name_A] in frame.
[Proper_Name_A]'s skin and makeup: fully_preserved - [Female Skin & Makeup School F1/F2/F3/F4 matching reference image]; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.
[Proper_Name_B] <<<Image 3>>> (fully_preserved - same face, hair color and outfit throughout; only his head, eyes, mouth, hands and expressions move.): [Initial 3D architectural anchor within arm's reach, posture, hand state, and eyeline at 00:00 — ZERO specific clothing/age words] — the only [Proper_Name_B] in frame.
[Proper_Name_B]'s skin: fully_preserved - [Male Skin School M1/M2/M3 matching reference image]; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.

[sound]:
[Diegetic room acoustics and synchronized tactile Foley across Shot 1..4. Strictly zero background music].

Shot 1 (00:00-00:04) - [Medium close-up], [over-the-shoulder perspective from behind Proper_Name_B targeting Proper_Name_A], [natural real-time speed]
[1–2 short natural sentences of Proper_Name_A's opening gesture and expression directed at Proper_Name_B].
[Proper_Name_A] ([vocal timbre/maturity], [tone]): "[Spoken Turn 1: 8–12 words/syllables]"

Shot 2 (00:04-00:08) - [Tight medium two-shot], [angled toward Proper_Name_A with focus locked on Proper_Name_A's face], [natural real-time speed]
[1–2 short natural sentences where Proper_Name_B raises/aims the tactile evidence directly at Proper_Name_A's eye level facing Proper_Name_A while glaring at Proper_Name_A, causing Proper_Name_A to flinch and scramble to defend].
[Proper_Name_A] ([vocal timbre/maturity], [tone]): "[Spoken Turn 2: 8–12 words/syllables]"

Shot 3 (00:08-00:12) - [Medium close-up], [reverse over-the-shoulder perspective from behind Proper_Name_A targeting Proper_Name_B], [natural real-time speed]
[1–2 short natural sentences framing Proper_Name_B's full face, piercing eyes, and decisive gesture on the prop held in front of Proper_Name_A as Proper_Name_B delivers the checkmate].
[Proper_Name_B] ([vocal timbre/maturity], [calm razor-sharp tone]): "[Checkmate Turn 3: 6–12 words/syllables]"

Shot 4 (00:12-00:15) - [Medium shot], [focus locked on Proper_Name_A], [natural real-time speed]
[1–2 short natural sentences of continuous wordless physical payoff / comedic button through 00:15 locked on the Target Subject (0 spoken words — e.g., Proper_Name_B pulls the prop cleanly out of Proper_Name_A's hands and tucks it under her arm, leaving Proper_Name_A frozen in center frame with both hands clasped in a silent pleading pout)].

Master-level cinematography and composition, smooth dynamic camera pacing, atmospheric sound design.
Strict visual consistency: maintain 100% identical facial features, matte skin texture, hair color, makeup, exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.
Do not generate oily sweat shine, greasy forehead or nose glare, waxy plastic skin, subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.
```

#### Mode B2 — `15.0s` High-Velocity Action / Chase / Ambush / Combat (`@CombatDirector` `[⚡ SEEDANCE · 15.0s]` · `5 Shots: 3.5s–4s–2.5s–3s–2s` · `0 Spoken Words` in `Shot 5`)
```text
Style: [Visual Style Specification].

[context]:
[Evocative Location Name in Natural English] <<<Image 1>>> (fully_preserved - same architectural layout, furniture, props and lighting throughout), [time of day]. [5-Vector Tactical Environment: architectural corridor/street/arena layout, lighting, shadows, and interactive/VFX surface details].

[subject]:
[Proper_Name_A] <<<Image 2>>> (fully_preserved - same face, hair color, makeup and outfit throughout; natural head, eye, expression and body movement.): [Initial spatial anchor and posture at 00:00 — ZERO specific clothing/age words] — the only [Proper_Name_A] in frame.
[Proper_Name_A]'s skin and makeup: fully_preserved - [Female Skin & Makeup School F1/F2/F3/F4 matching reference image]; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.
[Proper_Name_B] <<<Image 3>>> (fully_preserved - same face, hair color and outfit throughout; only his head, eyes, mouth and expressions move.): [Initial spatial anchor and posture at 00:00 — ZERO specific clothing/age words] — the only [Proper_Name_B] in frame.
[Proper_Name_B]'s skin: fully_preserved - [Male Skin School M1/M2/M3 matching reference image]; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.
[Proper_Name_C] <<<Image 4>>> (fully_preserved - same face, hair color and outfit throughout; only his head, eyes, mouth and expressions move.): [Staged at the interception point, (No objects should appear in the character's hands) if unarmed OR holding Tier-1 weapon in right hand with left hand empty — ZERO specific clothing/age words] — the only [Proper_Name_C] in frame.
[Proper_Name_C]'s skin: fully_preserved - [Male Skin School M1/M2/M3 matching reference image]; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.

[prop]:
[Canonical Tier-1 Weapon/Artifact Name] <<<Image 5>>> (fully_preserved - same shape, material, surface finish and proportions throughout): [Exact 00:00 hand-grip state or resting placement] — the only [Canonical Tier-1 Weapon/Artifact Name] in frame. *(Omit `[prop]:` if unarmed)*

[sound]:
[Ambient night/interior tone, rapid footsteps, sudden stop friction, low energy/rune hum, and cold vocal resonance. Strictly zero background music].

Shot 1 (00:00-00:03.5) - [Medium close-up], [slight handheld camera shake / slow push-in targeting Proper_Name_A], [natural real-time speed]
[1–2 short natural sentences establishing the false-calm opening beat and sudden snap-freeze realization as Proper_Name_A spots danger past Proper_Name_B's shoulder].
[Proper_Name_A] ([vocal timbre/maturity], [low abrupt tone]): "[Short setup/realization line: 3–6 words]"

Shot 2 (00:03.5-00:07.5) - [Wide tracking shot], [long follow shot targeting Proper_Name_A], [blistering whip-fast speed]
[1–2 short natural sentences of full-speed locomotion/flight/pursuit with 0 spoken dialogue: Proper_Name_A turns and flees at full speed through the empty alley].

Shot 3 (00:07.5-00:10.0) - [Wide shot transitioning to fixed frame], [middle of the street targeting Proper_Name_A], [explosive real-time speed]
[1–2 short natural sentences executing the Hard Stop + VFX/Trap activation with 0 spoken dialogue: Proper_Name_A stops sharply as pale red ancient rune patterns ignite across the road beneath her feet].

Shot 4 (00:10.0-00:13.0) - [Medium shot], [rear camera angle targeting Proper_Name_C], [natural real-time speed]
[1–2 short natural sentences revealing the Hunter/Boss blockade: Proper_Name_A spins around to find Proper_Name_C standing silently in the middle of the road (No objects should appear in the character's hands) with an overwhelming aura].
[Proper_Name_C] ([vocal timbre/maturity], [deep calm tone]): "[Checkmate line: 2–5 words, e.g., Miss, you seem lost.]"

Shot 5 (00:13.0-00:15.0) - [Close-up], [over-the-shoulder perspective from behind Proper_Name_C targeting Proper_Name_A], [natural real-time speed]
[1–2 short natural sentences of wordless terminal fallout / reaction settle (0 spoken words): Seen past Proper_Name_C's shadowed shoulder, Proper_Name_A steps back half a pace as the glowing ground runes lock around her boots and her breath catches in silent dread].

Master-level cinematography and composition, smooth dynamic camera pacing, atmospheric sound design.
Strict visual consistency: maintain 100% identical facial features, matte skin texture, hair color, makeup, exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.
Do not generate oily sweat shine, greasy forehead or nose glare, waxy plastic skin, subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.
```

### 8.3 The 10 Non-Negotiable Technical Laws of the Unified Multi-Shot Storyboard Format
1. **Double-Lock `fully_preserved` Reference, Gender-Calibrated Skin/Makeup Sub-Lock & Single `<<<Image X>>>` Declaration Law**: Keep `<<<Image X>>>` intact and place `(fully_preserved - ...)` immediately after it in `[context]:`, `[subject]:`, and `[prop]:`. Immediately below each character's main `[subject]:` line, include their gender- and aesthetic-matched skin lock (`[Name]'s skin and makeup: fully_preserved - ...` for Female `F1–F4`; `[Name]'s skin: fully_preserved - ...` for Male `M1–M3` with `natural matte lips` and zero `makeup/blush`). Declare `<<<Image X>>>` **ONLY ONCE** in the headers — **NEVER repeat `<<<Image X>>>` or skin descriptions inside `Shot 1..N`**, and seal the prompt with the `Strict visual consistency: ...` + anti-oily/anti-plastic negative footer.
2. **Temporal-Kinetic-Vocal Equilibrium & Zero Tail-Cut Law (`Zero Spoken Words in the Final Shot`)**: Size every shot containing dialogue to **`3.5s–4.5s`** ($\mathbf{T_{shot}} = \mathbf{T_{lead\text{-}in}} + \frac{\text{Words}}{2.5} + \mathbf{T_{followthrough}}$) and pair speech with 1 simple action (`One-Move Rule`). **Strictly ban spoken dialogue in the final `2.0s–3.0s` shot of any clip (`00:08-00:10` in `10s`; `00:12-00:15` / `00:13-00:15` in `15s`)** so the ending shot (`0 spoken words`) delivers a clean visual payoff / somatic settle with zero audio cut-off.
3. **Zero Dead Air & State-Delta Directing Law**: Maintain 100% active physical or vocal occupancy across every shot (`Zero Dead Air`). `[subject]:` locks the static `00:00` posture; `Shot 1..N` describes strictly the **state transition (`State A ➔ State B`)** in 1–2 short natural sentences (`15–30w`), never repeating `[subject]:`'s static posture and strictly banning meta-instructions (*"speaking immediately from the opening second"*, *"finishes his sentence early"*).
4. **Dedicated `[prop]: <<<Image X>>>` Block for Tier-1 Hero Props, Weapons & Key Artifacts**: Whenever a Tier-1 weapon, heirloom, seal, or key contract appears in a scene, bind its isolated 4-view reference sheet (`prop-[name].jpg` $\to$ `<<<Image X>>>`) inside `[prop]:` with its exact `00:00` resting placement or hand-grip.
5. **Proper Character Names Only**: Never use generic labels (`Woman`, `Man`, `Girl`, `Boy`, `the father`, `the hunter`) as subject headers or speakers.
6. **Zero-Costume, Zero-Age & Single Vocal-Timbre Tag Law (`Gates 3A & 3E`)**: Strictly ZERO clothing/garment words and ZERO numeric ages or age/hair/beard adjectives anywhere in the prompt. Encode vocal maturity and emotion inside **ONE single compact parenthetical right after `[Proper_Name]`** (`[Proper_Name] ([vocal timbre/maturity], [tone]): "..."`), and enforce complete relational kinship pronouns (`Vợ–Anh`, `Chồng–Em`, `Bố–Con`) in spoken lines.
7. **Target-First Camera Grammar (`Distance – Power – Target Subject`) & Optical Prop Vector Law**: Every shot MUST explicitly lock focus onto its **Primary Target Subject (`targeting [Proper_Name]` / `with focus locked on [Proper_Name]'s face`)** along the 180° interpersonal line of force rather than filming from a passive "Audience-Spectator" seat. Handheld props (mirrors, receipts, phones, contracts) MUST face the Target Character looking at them — never rotate a prop flat toward the audience/camera.
8. **Full-Face Target Lock vs. Optional Selective Face Obscuration**: Keep full faces and eyes visible on the Target Axis in comedy, sitcom, romance, and direct showdowns (`Selective Face Obscuration` is an optional specialist tool for mysterious thriller silhouettes only, never forced into direct confrontations).
9. **Empty-Hand Anti-Glitch Lock**: Whenever an unarmed character or hunter stands/moves empty-handed in a tense or action shot, append `(No objects should appear in the character's hands)`.
10. **Intent-First Routing (`@Director`, `@CombatDirector`, `@PhotoDirector`, `@StoryboardDirector`)**: Route `10.0s` and `15.0s` Dialogue/Sitcom/Drama scenes to `@Director` (continuous Ping-Pong + silent visual payoff button), route `15.0s` / `10.0s` High-Velocity Action/Chase/Combat scenes to `@CombatDirector` (`Kinetic Contrast` + silent terminal fallout), route Single-Frame Still Image / Keyframe requests to `@PhotoDirector`, and route `9 / 12 / 15 / 25 Shot` Multi-Panel Storyboard Grid & `Storyboard-to-Video` requests to `@StoryboardDirector`.

### 8.4 Canonical 2-Phase Multi-Panel Storyboard Grid & `Storyboard-to-Video` Workflow (`@StoryboardDirector` — `.agents/STORYBOARD_DIRECTOR.md`)
When the user requests a **Multi-Panel Storyboard Grid Image (`9 [3×3]`, `12 [3×4]`, `15 [3×5]`, or `25 [5×5]` Shots — divisible by `3` or `5`)** and/or a **Video Prompt driven by that Storyboard Grid Image (`<<<Image 1>>>`)**, execute the 2-Phase `@StoryboardDirector` workflow:
1. **🖼️ Phase A — Multi-Panel Storyboard Grid Image Prompt (`100% Static Keyframes + Top-Left Rounded Number Badges "1".."N"`)**:
   - **Header & Matrix**: `Style: Cinematic [9/12/15/25]-panel storyboard grid sheet arranged in a strict [3x3 / 3x4 / 3x5 / 5x5] matrix ([R] rows by [C] columns of [N] equal rectangular frames separated by thin clean black borders, reading sequentially left-to-right from top-left Shot 1 to bottom-right Shot [N], with a small clean rounded badge in the top-left corner of each panel displaying its sequential number 1 through [N])...`
   - **Per-Panel Static Spec (`[storyboard grid]:`)**: Every `Shot K` is a frozen still photograph (`zero camera movement verbs`, `zero timestamp digits`, `zero [Shot Speed]`, `zero dialogue quotes`):
     `Shot K (Panel K - [Grid Position], rounded top-left badge "K") - [Static Shot Scale], [Static 4-Axis Camera Angle targeting Subject/Prop]: [Frozen anatomical pose & hand/prop state + captured instant physical action + concrete 4-Zone facial micro-expression (brows, eyes/moisture, lips, jaw; use "lips parted slightly in natural speech" for speaking panels and "composed closed lips" for silent/final panels)].`
2. **🎬 Phase B — Storyboard-Driven Video Prompt (`Strict 1:1 Shot 1..N (00:XX-00:YY) - Panel 1..N Mapping`)**:
   - Bind the rendered Storyboard Grid Image to `<<<Image 1>>>` inside `[storyboard]:` and Character References to `<<<Image 2, 3>>>` inside `[subject]:` (with Line 2 `<Name>'s skin (and makeup): fully_preserved - ...`).
   - **Write Out Every Single `Shot 1..N` Individually With Contiguous Timestamps**: Never lump panels into vague summaries (`Panels 4–9`). Write every `Shot 1` through `Shot N` 1:1 with `Panel 1` through `Panel N`:
     `Shot K (00:XX-00:YY) - Panel K ([Grid Position]), [Shot Scale], [Camera Angle & Dynamic Move Targeting Subject/Prop], [Shot Speed]`
     `[1 concise sentence (12–22w) converting Panel K's static keyframe into living motion across (00:XX-00:YY)]`
     `[Proper_Name] ([vocal timbre/maturity], [delivery tone]): "[Spoken Line — on 3.5s–4.5s speaking shots at natural real-time speed; Final Shot N = 0 spoken words]"`
   - **Anti-Split-Screen & Anti-Badge Footer**: Close Phase B with `Render strictly as sequential full-screen video shots. Do not show the 3x3 grid layout, panel borders, corner number badges, split-screen mosaic, oily sweat shine, greasy forehead glare, waxy plastic skin, subtitles, text overlays, or watermarks in the video.`

---

## §9 — DURATION MODES: `10.0s` VS. `15.0s` (`@DIRECTOR` DIALOGUE/SITCOM VS. `@COMBATDIRECTOR` ACTION) VS. `30.0s`

| Mode | Owner & When | Flexible Storyboard Shot Range & Timing Principles |
|---|---|---|
| **`10.0 s` (Default Standard)** | **`@Director`**: Opening hooks, storytelling/`V.O.` reflections, standard dialogue/confrontations, and clue-discovery twists (`[🎭 MODEL TIÊU CHUẨN · 10.0s]`) | **`1 – 4 Shots`** flexing by scene structure (§1.1), `3.5s–4.5s` per spoken turn, `0–22w` dialogue total, **`0 spoken words` in the final `2.0s` settle beat (`~00:08-00:10`)** |
| **`15.0 s` (Extended Dialogue / Sitcom / Showdown)** | **`@Director`**: Multi-turn comedy/sitcom banter, high-voltage boardroom/family showdowns, or user-requested `15s` dialogue scenes | **`3 – 4 Shots`** flexing by turn length (e.g., `4s–4s–4s–3s` or `4.5s–4s–3.5s–3s`), continuous Ping-Pong across `Shot 1..N-1`, **`0 spoken words` in the final `2.5s–3.0s` shot (`~00:12-00:15`)** |
| **`15.0 s` (High-Velocity Action / Combat / Rapid-Cut Montage)** | **`@CombatDirector`**: High-motion action, chase, martial arts combat, split-second rescue, and rapid-cut professional craft/culinary whip-montages (`[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s]`) | **`5 – 9 Shots`** (`6 × 1.5s + 3 × 2.0s = 9 Shots` for Hyper-Cut Craft Montage; `7 Shots` for Rapid-Cut Combat; `5 Shots` with long tracking chase), `1 single punchy sentence (12–22w, 0 dialogue)` per `1.5s–2.0s` rapid cut, **`0 spoken words` in the final `1.5s–2.5s` settle shot** |
| **`30.0 s` (Explicit User Request Only)** | **`@Director` / `@CombatDirector`**: Extended 3-act sequence when explicitly requested | **`8 – 10 Shots`** across `00:00-00:30`, ending on a `2.5s–3.0s` wordless visual payoff shot |

---

## §10 — QUICK PRE-FLIGHT CHECKLIST (PER SCENE)

1. **Zero Top Slugline & Anti-Plastic `Style:`**: Opens directly with `Style: ...` (matte finish, subtle organic film grain, muted tones; strictly zero `35mm`, `50mm`, `24fps`, `8K`, `Kelvin`, or camera hardware names per `Gate 3D`) followed by `[context]:`?
2. **Single `<<<Image X>>>` Lock**: Are `<<<Image X>>>` tags declared **ONLY ONCE** in `[context]:`, `[subject]:`, and `[prop]:`, and **0 times** inside `Shot 1..N`?
3. **Zero-Costume & Zero-Age**: Are all clothing words (`jacket`, `suit`, `skirt`, `dress`) and age/hair/beard words (`young`, `blonde`, `silver-bearded`) 100% purged from `[subject]:` and `Shot 1..N`?
4. **3-Parameter `Shot N` Header & 5-Tier `[Shot Speed]`**: Does every `Shot N` header follow `Shot N (00:XX-00:YY) - [Shot Scale], [Angle/Move Targeting Subject], [Shot Speed]` (omitting `Interior/Exterior` unless crossing between spaces in the same clip, and locking `[Shot Speed]` to one of the 5 tiers in `§4.2` without repeating it in the sentence below)?
5. **Temporal-Kinetic-Vocal Equilibrium & Zero Tail-Cut Law**: Is every spoken shot sized to **`3.5s–4.5s`** with **`natural real-time speed`** and **1 simple primary action (`One-Move Rule`)**, and does the **final `2.0s–3.0s` shot (`00:08-00:10` or `00:12-00:15`) have strictly `0 spoken words`**?
6. **Zero Dead Air & State-Delta Prose**: Does every shot maintain 100% active occupancy (`Zero Dead Air`), express 1 state transition `A ➔ B` in **1–2 short natural sentences (`12–30w`)** without repeating `[subject]:`'s static posture, and contain **0 meta-instructions**?
7. **Target-First Camera Axis & Optical Prop Vector**: Does every shot explicitly target its Primary Subject (`targeting [Proper_Name]` / `with focus locked on [Proper_Name]'s face`) along the 180° axis instead of passive audience-spectator framing, and are handheld props physically oriented toward the Target Character rather than rotated flat toward the audience?
8. **Footer Lock**: Ends with `Master-level cinematography and composition, smooth dynamic camera pacing, atmospheric sound design.` + `Strict visual consistency: ...` + `Do not generate subtitles...`?

# CREATIVE DOCTRINE — Intent Before Tools
# (The thinking layer that sits above the 4 Master Pillars)

> **READ THIS BEFORE ANY PILLAR, AT STAGES 0, 1, 2, 3, AND 4.** Story level first (§8 Story Spine Card + §9 plot engine, once per project at Stage 1 and refreshed per episode at Stage 3), scene level second (§1 Intent Card, once per scene).
> The Pillars are catalogs: scales, angles, combos, dialogue models, timings, word budgets, examples. This doctrine decides **which tool a scene needs and why**. When a Pillar number (seconds, words, shot counts, "always", "strictly") collides with the dramatic need of a specific scene, the dramatic need wins — unless the number is a **Hard Constraint** listed in `workflow.md` §2.
> Rule of thumb: **understand the scene first, then choose the tools, then state the reason in one clause.** A choice without a reason is decoration; decoration is cut.
> **Examples are illustrations, not templates.** Most examples in the engine come from a few sample projects (a patriarch with a brass keyring, a postpartum family drama, a boardroom inheritance fight). Never reuse their names, props, premises or lines in a new project — the registry (K1) treats them as already used. Build every new story from its own Specific Truth Inventory (§8.5).

---

## §0 — THREE KINDS OF RULES (KNOW WHICH ONE YOU ARE HOLDING)

| Kind | What it is | Examples | How to treat it |
|---|---|---|---|
| **Hard Constraint** | A technical limit of AI video generation, a safety rule, or a delivery format rule | Zero Dead Air (no "holds still", continuous micro-actions); Zero Cumulative Timestamps (prompts MUST start at 00:00 for third-party AI generators); clip duration 10s / 15s / 30s; no freeze frames; no camera hardware/Kelvin; no clothing in prose; image references; Dialogue word caps and spoken windows exactly as listed in `0c-canonical-numbers.md` §2; no pronouns in visual prose; minor safety; no lip-sync during a downward POV; ≥ 2 contiguous time phases; zero gore / on-screen death | **Never break.** The linter blocks delivery. |
| **Craft Default** | A habit that usually produces good results | Earned positive ending & zero fatalities (project `ending_mode` / `fatality_policy` may change them); Thermal shock cold→warm in Release; Wound Prop → Echo Prop; cast rotation per beat; conflict-dense Beat 3; ~14–18 spoken words per clip; the timing blueprints of the 8 dialogue models; the 3-phase "breath" (lead-in → peak → settle) | **Use by default. Break when the scene needs it**, and write a one-line reason (`BREAK: <default> — <why>`). |
| **Project Rule** | A rule that belongs to one film, not to the system | A family's kinship-address ladder; a recurring meal; a dialect lexicon | Lives in `output/<slug>/project_rules.json` and in that project's `setting.html`. Never hard-code it into the engine or the Pillars. |

If you cannot tell which kind a rule is, treat it as a Craft Default and give a reason when you deviate.

---

## §0.05 — THE TWO-LAYER MASTER ARCHITECTURE: UNIVERSAL CORE (50%) + GENRE ADAPTER (50%)

> **CORE OPERATING PRINCIPLE**: Never confuse a genre-specific convention (e.g., Southern domestic family reconciliation, or sitcom episodic reset) with the universal laws of cinema. Every project in Sven is engineered by locking **Layer 1 (The Universal 4-Tier Core — invariant across 100% of films)** and dynamically mounting **Layer 2 (The Genre & Cultural Adapter — calibrated per genre)**.
> **Layer 0 — the North Star above both ([`0d-heart-and-value.md`](file:///d:/Project/Sven/engine/references/0d-heart-and-value.md))**: Layers 1 and 2 make a story gripping; Layer 0 decides what it is *for*. Every story must move the viewer (an earned, planted heart moment), affirm a positive value through a costly choice, and leave an unspoken takeaway — and every reversal obeys the Dignity & Value Firewall (justice restores, never degrades). When a Layer 1 or Layer 2 tool collides with Layer 0, the tool changes.

### Layer 1: The Universal 4-Tier Core (Invariant Across All Genres)
1. **Tier I — Core of a Great Screenplay (Lõi Kịch Bản Hay)**:
   - **Central Thematic Question & Genre-True Opposition**: A real conflict driven by either Two Honest Sides (Social/Family Drama), Existential/Ideological Antagonism (Action/Thriller/Microdrama), or Amplified Character Flaws (Sitcom).
   - **6-Layer Character Psychology (`Wound ➔ Lie ➔ Want ➔ Need ➔ Fear ➔ Paradox`)**: Every principal character operates from an internal wound and a protective Lie.
   - **Protagonist Gravitational Agency (`Active A1` — §1.1)**: `A1` is never a passive victim; `A1` pursues an active Want with concrete Tactics in every scene, and the escalating crisis is caused by `A1`'s own flawed choices.
   - **Specific Truth Inventory (§8.5) & Subtext-First Action↔Line Synergy (§3.3)**: Concrete, lived-in details over generic explanation; speech paired with physical action (`Reinforce`, `Contradict`, `Replace`, `Reveal`).
2. **Tier II — Core of a Great Film (Lõi Bộ Phim Hay)**:
   - **Dialogue-Driven Somatic Fusion (§0.1.5)**: Emotion deforms physical matter under the character's hands; zero motionless talking mannequins; strictly **1 primary macro physical action per phase** (Single Focal Action Law, Gate 3R).
   - **3D Spatial Geometry of Power (§2.7b)**: Blocking tells 80% of the story (doorway thresholds, vertical posture shifts, proxemic breaches).
   - **Intent-Driven Camera & Dynamic Editing Rhythm (§2 & §0.1.6)**: `Shot Scale = Psychological Distance`, `Camera Angle = Power at This Instant`, `Camera Move = Motive (a/b/c)`. Alternate Track A, Track B 2-phase, Track B 3-phase rapid sparring, Track AB sudden fracture, and Track A-Locked gravitational anchor (≤ 1–2 scenes/ep).
   - **Earned Ending & Opening↔Closing Image Symmetry (§8.8)**: Resolution costs someone something real (a mask, pride, status, sacrifice) and answers the opening image visually without preachy dialogue.
3. **Tier III — Core of a Great Multi-Episode Series (Lõi Phim Dài Tập Hay)**:
   - **Continuum Engine vs. Reset Engine**: Continuous Pressure-Cooker Escalation for Serial Drama, Action, Thriller, and Microdrama (zero premature resolution in Acts 1–2; every solved surface problem exposes a deeper wound) vs. Status Quo Reset for Episodic Sitcom (`sitcom.md`).
   - **Triple-Helix Subplot Weaving (`A-Plot` 55–65% + `B-Plot` 25–30% + `C-Plot` 10–15%)**: Governed by the **Thematic Mirror Law** (all 3 threads answer the same thematic question from different angles) and the **Domino Ripple Law** (`A1`'s flawed choice in A-Plot directly impacts B-Plot and triggers the C-Plot bomb).
   - **Dynamic Cast Sizing & Twist-Driven Casting**: Short Film = `3–4` named chars; Mini-Series (3–5 eps) = `5–6`; Full Series (6–10+ eps) = `7–9`; Mega Series (12–20+ eps) = `10–14`. Every Tier B character holds a twist function (`TW-01..20`) and moral dilemma.
   - **4-Act Macro Arc (`20% Setup ➔ 45% Escalation & Midpoint Reversal ➔ 25% Abyss & Climax ➔ 10% Resolution`)**.
4. **Tier IV — Core of Every Addictive Episode Inside a Series (Lõi Từng Tập Trong Series)**:
   - **Causal Chain (`Therefore / But`) + Expectation↔Result Gap + Value Shift (§1 & §9.1)**: Every scene flips a value (`+` to `-` or `-` to `+`) because a character's tactic backfires or escalates.
   - **Audience Prediction Ledger & Option C (§9.2)**: Break ≥ 2 viewer predictions per episode using a planted **Option C** (surprising at first, inevitable on rewatch).
   - **Knowledge Matrix Switching (`Suspense ↔ Mystery ↔ Empathy` — §9.4)**: Switch who knows what at least once per episode.
   - **Multi-Sequence Spatial Partitioning (§10.3)**: Partition each episode into `2–4 distinct spatial/temporal sequences` (`0c` §4) connected by Sensory Match-Cuts or Parallel Cross-Cutting to eradicate the "trapped in one room" disease.
   - **Genre-Calibrated Episode Tail, Kinetic/Dramatic `10s`/`15s` Peaks & The 3-Case Scene Continuity Reference Law (`workflow.md` §2.4, §2.5, §8.2, §8.3)**:
     * *Genre-Calibrated `10.0s` / `15.0s` Peaks & The 4-Regime Genre Authenticity Firewall (`Zero Cross-Genre Contamination`)*:
       1. **Regime 1 — Grounded Real-World Drama (`Gia đình, Thừa kế, Tỷ phú đời thực, Hôn nhân, Thương trường, Pháp lý, Chữa lành`)**: Strictly obeys 100% real-world human psychology, real legal/financial mechanics (realistic enterprise scale per `0c` §8), and everyday physical reality. **STRICT BAN** on sci-fi gadgets (*biometric brain watches, AI protocols*), supernatural powers, or forcing doctors/lawyers/executives into spy break-ins, parkour chases, or martial arts fights! In Realistic Drama, `15.0s` clips are primarily routed to **`[🎭 RECOMMENDED MODEL: STANDARD / LIP-SYNC · 15.0s]`** for high-voltage boardroom/courtroom showdowns, truth-bomb reckonings, and unbroken emotional acting takes (`Seedance` is used ONLY when a grounded physical commotion naturally occurs, such as security escorting a character out or rushing into the rain).
       2. **Regime 2 — Speculative Sci-Fi (`Khoa học viễn tưởng, Công nghệ tương lai, AI, Đột biến sinh học, Hậu tận thế`)**: Built on a clear speculative *"What If?"* premise governed by **3 Hard Scientific/System Rules** (*Mechanism – Failure Limit – Ethical/Survival Cost*). High-tech devices, automated protocols, containment breaches, and tactical pursuits (`[⚡ RECOMMENDED MODEL: SEEDANCE · 10s/15s]`) drive the plot.
       3. **Regime 3 — Supernatural, Fantasy, Xianxia & Time-Travel (`Siêu nhiên, Huyền huyễn, Tu tiên, Xuyên không, Trùng sinh, Linh dị`)**: Governed by the **Concrete World-Law Contract (`Trigger – Ceiling – Somatic/Karmic Cost`)**, **3-State Tier-1 Soul Relic Evolution (`State 0 ➔ 1 ➔ 2`)**, native **`TH3` Spatial-Temporal Continuity**, and high-velocity martial/supernatural clashes (`2.3x–10x` on `Seedance 10s/15s`) directed via `@CombatDirector`.
       4. **Regime 4 — Action, Martial Arts & Crime/Detective Thriller (`Hành động võ thuật, Trinh thám hình sự, Đấu trí mật thất`)**: Driven by life-or-death stakes, **$\ge 2$ Fair-Play Non-Verbal Visual Clues**, `Suspense ↔ Mystery` switches, and the `3-Zone (40% Setup ➔ 40% Seedance Pursuit/Combat ➔ 20% Fallout)` architecture.
     * *Between Episodes (`Ep N ↔ Ep N+1`)*: Driven by 3 Cross-Episode Threads (*Question Escalation Relay $Q_1 \to Q_2$*, *Irreversible Relationship/Power Ledger*, *Physical & Prop State Ledger*) and connected via 1 of **4 Flexible Episode Bridges**: (1) *Zero-Gap Cliffhanger / Chase Relay* (`00:10.0`/`00:15.0` of Ep N = `00:00.0` of Ep N+1, launching directly into a tense pursuit, ambush, or confrontation), (2) *Causal Aftermath Ellipsis* (hours/days later inside the consequence), (3) *Parallel/POV Counter-Strike* (opening Ep N+1 in `A2`/`B1`'s space), or (4) *Episodic Reset* (`sitcom.md`).
     * *Between Scenes Inside an Episode (`Sc K ↔ Sc K+1`) — The 3-Case Continuity Reference Point Law (`Điểm Nối Tham Chiếu Giữa 2 Cảnh`)*: Every Scene Rough Script MUST explicitly declare its **Continuity Reference Point Status** for the user before prompt writing begins:
       1. **🟢 CASE 1 — SAME TIME & SAME LOCATION (`[ĐIỂM NỐI THAM CHIẾU: CÓ — Nối Trực Tiếp Khung Hình Cuối Cảnh Trước]`)**: When Scene $K$ and Scene $K+1$ occur at the **exact same continuous time and physical location**, the terminal state (`00:10.0` / `00:15.0`) of Scene $K$ is the **mandatory Continuity Reference Point** for `00:00.0` of Scene $K+1$. The user supplies the **Static Terminal Frame (`Last Frame`)** of Scene $K$, and Scene $K+1$'s prompt locks 100% to that frame's character positions, postures, hand-prop grips, and room state.
       2. **🔵 CASE 2 — DIFFERENT LOCATION, DIFFERENT TIME, OR CHARACTER SWITCH (`[ĐIỂM NỐI THAM CHIẾU: KHÔNG NỐI KHÔNG GIAN CŨ — Dùng Ảnh Bối Cảnh / Nhân Vật Mới]`)**: When Scene $K+1$ moves to a **new physical location**, **jumps in time**, or **switches to a different character group** (including a multi-zone chase crossing from an interior room out into an alley/street), do NOT reference Scene $K$'s spatial frame. The Agent reads the **new location, character and prop specifications directly from `setting.html`** (the user does not upload images in chat — `workflow.md` §2.10) to establish fresh spatial positions at `00:00.0` (preserving only held props and running/emotional momentum if the same character just crossed into the new space).
       3. **🟣 CASE 3 — SUPERNATURAL, TIME-TRAVEL, PORTAL, OR REALITY SHIFT (`[ĐIỂM NỐI ĐẶC BIỆT: SIÊU NHIÊN / XUYÊN KHÔNG — Giữ Đà Nhân Vật, Thay Mới Toàn Bộ Không Gian]`)**: In supernatural, time-travel (`xuyên không`), teleportation, illusion-shattering, or dimension-shift scenes where the character's action is continuous in time (e.g., stepping through a portal or unleashing a space-shattering strike at the end of Scene $K$), **preserve the character's exact body posture, kinetic vector, and held weapon/prop from Scene $K$'s terminal point, while completely discarding Scene $K$'s background and anchoring `[context]:` to the New World/Era Location Reference Image**.

### Layer 2: The Dynamic Genre & Cultural Adapter Matrix
| Dimension | Social & Family Drama (`drama.md`) | Action, Martial Arts & Chase (`action.md`) | Viral Microdrama (`microdrama.md`) | Thriller, Mystery & Crime (`thriller`) | Situation Comedy (`sitcom.md`) |
|---|---|---|---|---|---|
| **Antagonist Nature** | Two Honest Sides (love/duty pointed the wrong way) | Lethal Rival, Syndicate, or Supernatural Threat | Hypocrite, Usurper, or Status Oppressor | Hidden Mastermind or Institutional Trap | Eccentric Flaw Collision (`Odd-Couple`) |
| **Core Audience Payoff** | Emotional Catharsis & Earned Empathy | Kinetic Adrenaline (`2.3x–10x`) & Tactical Victory | Dignity Reversal: the overlooked hero's worth recognized | Intellectual Shock (`The Prestige`) & Dread | Laugh-Out-Loud Escalation & Punchline |
| **Heart & Value Payoff (`0d` §6)** | Reconciliation that costs pride; love & responsibility across generations | Courage used to protect; restraint & mercy toward the beaten | Integrity outlasts arrogance; one act of grace in the crown | Truth & justice; protecting the vulnerable; the cost of a lie | Warmth: the group stays a family; a small kindness in the tag |
| **Action / Dialogue Ratio** | `50% Domestic/Tactile Labor : 50% Subtext Dialogue` | `3-Zone (40% Drama : 40% Pure Combat/Chase : 20% Fallout)` | `40% Status Proxies : 60% Staccato Fencing (≤12w)` | `70% Suspense Visuals & O.S. Sound : 30% Scalpel Lines` | `30% Physical Slapstick : 70% Rapid Ping-Pong` |
| **Episode Ending** | `False Dawn ➔ Cold Water Cliffhanger` | `Weapon Break / Boss Arrival / Lethal Strike Cut` | `Zeigarnik Unmasking / Seal Reveal` | `Clue Reversal (Trusted Ally = Suspect)` | `Status Quo Reset + Comedic Scene Button` |
| **Series Climax** | Ego Death & Costly Moral Reconciliation | Martial/Supernatural Breakthrough & Boss Defeat (mercy offered) | Public Truth, Fair Consequence & Dignity Restored (+ one act of grace) | Mastermind Exposed via Planted Trap | Snowball Lie Collapse & Warm Group Reset |

---

## §0.1 — THE 6 SOVEREIGN FIRST-PRINCIPLES LAWS OF THE SVEN CORE ENGINE (UNIVERSAL ACROSS ALL AGENTS & GENRES)

> 🎬 **MASTER FIRST-PRINCIPLES MANDATE (`KNOWLEDGE OVER TEMPLATES · ZERO FIXED SHOT QUOTAS`)**:
> The downfall of amateur AI filmmaking is **"Breathing Mannequin Syndrome"**, **"Cheap Floating Overlays"**, **"Unintentional Slow-Motion"**, and **"Cookie-Cutter Template Monotony"**.
> Across **100% of agents (`@Screenwriter`, `@Director`, `@CombatDirector`, `@PhotoDirector`, `@StoryboardDirector`, `@RefVideoDirector`, `@RobloxDirector`) and all genres**, every scene and prompt is governed by **6 Universal First-Principles Laws**:

### 1. The Anti-Plastic Optical Standard & Host-Surface Physical Attachment Law (`Khử Mùi Nhựa AI & Định Luật Vật Lý Bám Dính Vật Chủ [死死贴附]`)
- **The Root Cause of "Fake AI Look" & "Cheap VFX/Details"**:
  1. When prompts stack hollow buzzwords (`photorealistic`, `cinematic 8k`, `cinematic lighting`, `vibrant`, `masterpiece`), AI models default to an over-saturated filter with waxy, oily plastic skin sheen.
  2. When any visual detail — whether a supernatural aura, fire, smoke, rain, sweat, tears, or light reflection — is described as a loose ambient noun (*"tears fall"*, *"lightning surrounds her"*, *"fire fills the pan"*), the AI renders a detached 2D screen-space overlay floating in front of the subject.
- **The First-Principle Core Law**:
  1. **Real Physical Light, Matte Finish, Fine Grain & Muted Tones (`Zero 35mm / Hardware Jargon — Gate 3D`)**: Lock a real physical light emitter in `[context]:` (`harsh overhead fluorescent tube`, `direct warm tungsten desk lamp`, `overcast window daylight`), and lock **`matte skin and surface finish with zero plastic or oily sheen, subtle organic film grain, muted natural color tones`** in `Style:` (or `satin-matte finish with zero plastic doll sheen` in 3D Semi-Real). Strictly ban `35mm`, `50mm`, `24fps`, `Kelvin`, or camera brand names.
  2. **Host-Surface Physical Attachment (`Surface-Bound Material & Somatic Physics`)**: Every secondary detail, emotion, fluid, particle, or aura across ALL genres MUST be physically bound to its **host surface** so the AI computes real interactive lighting, reflection, and material deformation:
     * *Drama / Romance / Sitcom / Still Portraits (`@Director` & `@PhotoDirector`)*: Bind moisture, light, and touch directly to anatomy and materials (`tears clinging to her lower lashes and tracing down her cheek`, `cold sweat adhering to his temple`, `warm chandelier light catching the bridge of her nose`, `fingertips pressing into the paper edge / gripping the condensation-beaded crystal glass`).
     * *Weather & Environment (`[context]:`)*: Bind rain, mist, neon reflections, and dust to architectural surfaces (`rain droplets clinging to the glass pane`, `neon reflections sliding across the wet asphalt`).
     * *Action, Combat, Culinary & Vehicles (`@CombatDirector`)*: Bind elemental energy, slash streaks, fire, foam, smoke, or sparks directly to the moving host (`silver-white moonlight, cyan electric arcs, and cold-white calligraphic dry-brush slash streaks tightly clinging and physically adhered to her garment hems and sword blade`; `amber flambé fire and foaming herb butter clinging to the seared steak crust and skillet rim`; `white tire smoke and sparks hugging the spinning rear tire tread`). In pure grounded physical scenes without VFX, apply surface-bound physics via **tactile deformation** (knuckles compressing ribs, cloth pulling taut, boots skidding on wet stone) — never invent fake sparks where none belong.

### 2. The Latent Pixel-Budget & Motion-Release Law (`Định Luật Bảo Toàn Ngân Sách Pixel & Giải Phóng Chuyển Động`)
- **The Root Cause of "Warped Mouths During Speech" & "Sluggish Slow-Motion During Fast Action"**:
  Generative video diffusion models have a finite per-frame pixel-detail budget. If a prompt forces the AI to render **100% razor-sharp detail on a moving camera, a speaking mouth, rapidly swinging limbs, and a shifting background all at the same time**, the model either warps the face/lips OR automatically stretches time into sluggish slow-motion to keep fast objects sharp!
- **The First-Principle Core Law**:
  1. **When Prioritizing Vocal Lip-Sync & Facial/Hand Acting (`@Director` Continuous Dialogue — `Law D1`)**: Lock **`static camera`** so 100% of the latent motion budget is dedicated to **accurate lip-sync, expressive hand/body gestures, and 4-Zone Facial Micro-Expressions (`brows, eyes/moisture, lips, jaw`)**. In **`Mode D1-A` (`Fixed-Camera, Fixed-Angle & Fixed-Scale Continuous Dialogue — Ghi Chung Camera, Cỡ Cảnh & Góc Quay 1 Lần`)**, declare the Camera, Shot Scale, and Angle **ONLY ONCE** at the top (`Shot 1 (00:00-00:15) - [Fixed Shot Scale], [Fixed Static Camera & Angle], natural real-time speed`) without repeating camera headers, and underneath write purely the turn-by-turn **Action/Emotion + Dialogue exchange (`A acts & speaks ➔ B waves hand / reacts & replies ➔ A counters ➔ B answers`)**. In **`Mode D1-B` (`Multi-Cut Static Scale Escalation`)**, step closer across distinct static cuts (`Static MCU OTS` $\to$ `Static Reverse MCU` $\to$ `Static Tight CU`).
  2. **When Prioritizing High-Velocity Physical Motion (`@CombatDirector` & Sudden Physical Impulses in `@Director`)**: Release the AI from rendering sharp mid-trajectory extremities by explicitly authorizing **`strong directional motion blur`** (and trajectory streaks such as `calligraphic dry-brush slash streaks` in blade combat) on fast-moving hands, weapons, tools, or wheels, and **suspend spoken dialogue (`0 spoken words`) during the high-velocity burst**.

### 3. The Time-Ramp Contrast & Dramatic Hit-Stop Law (`Định Luật Biến Tốc Tương Phản & Điểm Khựng Trọng Lượng [变速卡点]`)
- **The Root Cause of "Floaty Action" & "Flat Monotone Drama"**:
  When a clip runs at a uniform, unvarying tempo from `00:00` to `00:10 / 00:15` — whether in a sword fight or a living-room confrontation — movements feel weightless and emotional turns feel robotic.
- **The First-Principle Core Law (`Velocity ↔ Hit-Stop Compression ↔ Release`)**:
  True physical force and true emotional weight both require a **Hit-Stop / Micro-Pause at the exact point of impact or realization**:
  * **In Physical & Kinetic Scenes (`@CombatDirector`)**: Contrast rapid acceleration (`blistering whip-fast speed`) with a sharp **`time-ramp impact snap / hit-stop pause`** (`explosive real-time speed`) at the exact millisecond blades lock, a punch lands, or a steak hits hot iron, plus selective `ultra-slow-motion suspension` only when a mid-air apex genuinely earns it.
  * **In Dramatic, Sitcom & Thriller Scenes (`@Director` & `@Screenwriter`)**: Build **Dramatic Hit-Stops (`Snap-Freeze Realizations`)** into the acting flow — e.g., a character is moving or smiling naturally $\to$ **freezes dead for a split-second (`abrupt micro-pause / breath catching in the throat`) the instant their eyes hit the incriminating evidence or hear the fatal keyword** $\to$ before pivoting into the counter-action or checkmate line.

### 4. The Embodied Camera Inertia & Target-First Axis Law (`Định Luật Quán Tính Máy Quay Có Trọng Lượng & Khóa Trục Mục Tiêu`)
- **The Root Cause of "Passive Surveillance Camera" Framing**:
  Lining characters up side-by-side facing the viewer or floating the camera at a uniform, unmotivated glide makes scenes feel staged and slow.
- **The First-Principle Core Law**:
  1. **Target-First Camera Axis & Optical Prop Vector**: Every shot locks its camera axis and optical focus onto the **Primary Target Subject (`targeting [Proper_Name]` / `with focus locked on [Proper_Name]'s face`)** along the 180° interpersonal line of force. Handheld props (mirrors, receipts, phones, contracts) held up in confrontation MUST physically face the Target Character looking at them — never rotate a prop flat toward the audience.
  2. **Embodied Camera Inertia (Whenever the Camera Moves)**: When a shot is static (`Law D1`), the frame is an unshakable witness. Whenever a scene calls for camera movement (an opening hook push-in, a clue reveal whip-pan, a shocked pull-back, or a 3A action chase), the camera moves with **physical mass and inertia (`AAA inertial whip-follow / inertial push-in`)** — accelerating with the directional force of the subject and **snapping to a locked focus (`impact recoil / hard stop`)** at the exact point of discovery or collision.

### 5. Targeted Action Verbs, Clean Prop Economy & State-Delta Directing (`100% Active Occupancy — Zero Dead Air`)
- **The Stagnation Trap**: Abstract emotional adjectives (`she looks sad`, `tense atmosphere`), repeating `[subject]:`'s static `00:00` posture inside `Shot 1..N`, or leaving characters standing idle waiting out the clock.
- **The First-Principle Core Law**:
  1. **Observable Verbs Over Adjectives**: Translate every emotion into concrete anatomical and material verbs (`slams`, `clenches`, `recoils`, `taps`, `whips`).
  2. **State-Delta Directing (`State A ➔ State B`)**: `[subject]:` anchors the initial `00:00` posture and hand state; each `Shot N` describes strictly the **state transition (`Initiating Action ➔ Immediate Visible Reaction/Shift`)** in natural cinematic prose (strictly zero mechanical `→` arrows, zero static repetition, and zero meta-instructions).

### 6. Topology Follows Intent — Total Abolition of Fixed Shot Quotas (`Cấu Trúc Shot Sinh Ra Từ Ý Đồ — Xóa Bỏ Mọi Con Số Đóng Khung`)
- **The Formulaic Trap**: Forcing every dialogue scene into `3 shots (4s–4s–2s)` or forcing every fast action scene into `7–9 shots × 1.5s`.
- **The First-Principle Core Law**: **Shot count and shot durations are NEVER a fixed quota.** Both `@Director` and `@CombatDirector` select the **Shot Topology** organically from the specific scene's dramatic, spatial, and kinetic intent:
  1. **Topology 1 — The Unbroken Continuous / Inertial Long-Take (`1 to 2 Shots` across `10.0s` or `15.0s`)**:
     * *In `@Director`*: A single unbroken push-in on an intimate confession, an atmospheric opening hook, or a 3–4 character table scene where cutting would break spatial unity.
     * *In `@CombatDirector`*: An unbroken **3A Action-Game Inertial Long-Take** (*Black Myth / Sekiro / The Raid* style) where the inertial camera whips behind the launch, snaps into an internal time-ramp hit-stop on blade impact, orbits the counter-flurry, and settles without cutting every 1.5 seconds.
  2. **Topology 2 — Asymmetric Dynamic Contrast (`2 to 5 Shots` across `10.0s` or `15.0s`)**:
     * Contrasting a sustained take (`4s–6s` of building pressure, dialogue probing, or full-speed tracking pursuit) with a sharp `1.5s–2.5s` macro clue insert, trap activation, or checkmate reversal.
  3. **Topology 3 — Staccato Multi-Shot Rapid-Cut Blitz (`6 to 9 Shots` in `15.0s` / `4 to 6 Shots` in `10.0s`)**:
     * Chosen specifically when fracturing a multi-step high-velocity skill sequence (*The Bear / Edgar Wright* culinary, trauma surgery, mechanical assembly) or a multi-angle chaotic crisis/blitz into `1.5s–2.0s` peak-action cuts with `>45°` angle jumps.


---

## §1 — SCENE INTENT ENGINE (MANDATORY BEFORE WRITING OR SHOOTING ANY SCENE)

Answer six questions for every scene. The answers are short — one line each — and they are the source of every later choice.

1. **Want** — What does each on-screen character try to get *in this scene*? (A concrete verb + object: "make Khang choose her", "keep the baby asleep", "get the deed signed".)
2. **Obstacle** — What stops them: the other person, themselves, or circumstance?
3. **Tactic** — How do they pursue the want right now? (plead, attack, deflect, test, bribe, charm, shame, withdraw, stay silent). Tactics change when they fail; a tactic change is a beat.
4. **Value shift** — What flips between the first and the last frame? (trust → doubt, strong → weak, distant → close, hidden → exposed). **No shift = no scene.** Merge it or cut it.
5. **Subtext** — What does the character refuse to say aloud? This is what the actor plays.
6. **Audience gap** — Does the audience know more than the character (suspense), less (mystery), or the same (empathy)? The gap decides what the camera shows first.

**Scene Intent Card** (written in the Stage 3 screenplay, one per scene):
```
INTENT  | Want: A → [...]; B → [...] | Obstacle: [...] | Tactic: A [...] / B [...]
SHIFT   | [value at 00:00] → [value at 00:10]
SUBTEXT | [what is not said]
GAP     | [suspense / mystery / empathy: ...]
VOICE   | Mode: [§4 mode] — because [one clause]
LINK    | Action↔Line: [reinforce / contradict / replace / reveal] — [which line, which action]
```

---

## §1.1 — THE PROTAGONIST-CENTRIC GRAVITATIONAL LAW (ANTI-PASSIVE CHARACTER MANDATE)

> **CORE LAW: THE PROTAGONIST (A1) IS THE SOLE ENGINE OF THE NARRATIVE.**  
> A shallow script treats the protagonist as a passive punching bag or a spectator in their own story (events just happen to them, they cry or endure, while secondary characters drive all the action, make all the discoveries, and make all the choices). This makes characters superficial, hollow, and unengaging.
> **Masterclass cinema demands that the plot revolves 100% around the Protagonist's Active Agency, Internal Dilemma, Flawed Choices, and Transformational Arc.**

### 1. The 4 Laws of Protagonist-Centric Narrative
1. **Active Agency Over Passive Victimhood (Chủ Động Vượt Trên Nạn Nhân Thụ Động)**:
   - A1 is NEVER a helpless victim waiting for pity, rescue, or miraculous resolution.
   - In EVERY scene, A1 must have an **Active Want** and execute a **Concrete Tactic** (defending, concealing, counter-attacking, bargaining, protecting a loved one). If A1 is suffering, it must be the **consequence of their own active, flawed choice** (e.g. stubbornly hiding an illness to protect a family member's pride), not random misfortune.
2. **Gravitational Orbit: Secondary Characters Serve A1's Crucible (Mọi Tuyến Nhân Vật Phải Quay Quanh A1)**:
   - Antagonists (A2) and Satellites (Tier B) do NOT exist to steal the spotlight or run independent errands detached from A1.
   - Every action, threat, or discovery made by secondary characters MUST directly strike A1's **Root Wound**, challenge A1's **Lie**, and force A1 into an unbearable moral choice.
3. **The Flawed Choice Engine (Nhân Quả Từ Quyết Định Sai Lầm Của A1)**:
   - The escalating crisis of the story is NOT caused by bad luck or villainous magic; it is caused by **A1's desperate effort to solve a problem using their old, flawed worldview (The Lie)**.
   - Because A1 refuses to show vulnerability or ask for help, their tactical choices inadvertently tighten the trap around themselves and their family.
4. **Earned Metamorphosis & Sovereign Anagnorisis (Tự Thức Tỉnh & Tự Chuyển Hóa)**:
   - The climax is won because **A1 undergoes an internal Ego Death and consciously breaks their own Lie**.
   - A1 makes the costly choice, speaks the painful truth, or pays the ultimate moral price. The resolution belongs to A1's spiritual courage.

---

## §1.2 — THE 6 ROOT-CAUSE ANTI-SHALLOW SCRIPT LAWS (THE DEPTH CRUCIBLE)

> **ARCHITECTURAL MANDATE**: A screenplay fails at the root when a 10-second mundane whim is padded across 90 seconds of single-room small talk, when characters diagnose their own insecurities in Scene 2, or when saintly protagonists defeat cartoonishly stupid villains via a 5-second moral sermon. Every Stage 0 concept, Stage 1 Story Spine, Stage 2 World Bible (`setting.html`), and Stage 3 Episode Screenplay MUST enforce these **6 Root-Cause Depth Laws**:

### 1. Law 1: The 3-Layer Stakes & Zero-Triviality Law (`External × Internal × Philosophical Stakes`)
- **The Shallow Trap**: Building an entire episode around a trivial domestic or schoolroom whim (e.g., arguing for 90 seconds over whether to stand by a window or a podium for a casual photo, or chatting about what to eat) where failure carries zero real cost.
- **The Core Fix**: Every story and episode MUST lock **3 Simultaneous Stake Layers** before writing a single scene:
  1. **External Stakes (Concrete Consequence & Ticking Clock)**: What tangible loss, exposure, expulsion, financial ruin, physical danger, or permanent severance happens if `A1` fails before the deadline?
  2. **Internal Stakes (Wound & Identity Threat)**: What cherished relationship, dignity, or protective mask (`The Lie`) is on the verge of being shattered?
  3. **Philosophical Stakes (Two Honest Sides)**: What clash of valid human values (`Duty vs. Truth`, `Protection vs. Autonomy`, `Survival vs. Integrity`, `Justice vs. Mercy`) makes reasonable viewers debate who is right?

### 2. Law 2: The Micro-Beat Sequence Architecture & 3-Wall Escalation Law (`1 Clip = 1 Psychological Beat; 3–4 Clips = 1 Dramatic Situation`)
- **The Two Shallow Traps**:
  1. *The Padding Trap*: Taking a single trivial beat and stretching it across 8–10 scenes of polite small talk.
  2. *The 10-Second Plot-Summary Trap*: Treating a `10.0s` AI clip (one psychological beat) as an entire macro plot scene, cramming 7–8 massive plot events (reunion, bank foreclosure, betrayal, company mortgage, secret trust reveal) into one 120-second episode so every 10s clip becomes a rushed, superficial summary with zero psychological buildup.
- **The Core Fix (`Micro-Beat Sequence Unpacking`)**:
  - Because each `10.0s` clip carries **one psychological beat** (its internal shot topology follows §0.1.6 and `0c` §1), **one Dramatic Situation must be unpacked across a 3–4 Shot Psychological Sequence (`30s–40s`)** so the audience experiences genuine tension, subtext, and emotional resonance:
    * **Shot/Clip 1 (`10s — 3-Second Curiosity Hook & Veiled Power Push`)**: Open with a visual anomaly, a tactile prop anchor, or a polite-on-the-surface power probe that makes the viewer immediately suspect a hidden agenda.
    * **Shot/Clip 2 (`10s — Perspective Shift / Threshold POV & Atmosphere`)**: Use a purposeful angle shift (such as a doorway POV or over-the-shoulder reveal) to let the audience feel the room's unspoken hostility and power geometry before the collision.
    * **Shot/Clip 3 (`10s — Velvet-Dagger Probe vs. Specific Human Detail`)**: The antagonist strikes using a polite social mask (`dao găm bọc mật`), while the protagonist counters not with a preachy slogan, but with a hyper-specific lived detail (`chi tiết chạm tim đen`) that quietly pierces the emotional core.
    * **Shot/Clip 4 (`10s — Somatic Betrayal & Irreversible Value Shift`)**: A concrete prop action or involuntary physical leak exposes the truth beneath the mask and locks an irreversible shift (`+` to `-` or `-` to `+`).
  - Across every episode, these sequences escalate through **3 Distinct Walls of Progressive Complication** (*Wall 1: Opening Tactic & Veiled Friction ➔ Wall 2: B/C-Plot Pressure & Mask Crack ➔ Wall 3: Costly Choice & Point-of-No-Return Hook*).

### 3. Law 3: The Iceberg Subtext, Velvet-Dagger Mask & Anti-Spoiler Law
- **The Three Shallow Traps**:
  1. *Early Self-Diagnosis*: Characters blurting out their exact psychological wound in Scene 1 or 2.
  2. *The Premature Master-Twist Spoiler (`Lộ Bài Sớm`)*: Characters explaining the overarching series secret aloud in Episode 1 dialogue (e.g., *"The $150M trust fund is safe, I'm only faking bankruptcy for 10 days to test my children!"*), which destroys 90% of the audience's curiosity and suspense for the remaining episodes.
  3. *Blunt Cartoon Dialogue & Repetitive Moral Slogans*: Antagonists barking crude villain lines (*"Give me the company!"*, *"You came back for money!"*) and protagonists repeating flat defensive slogans across consecutive scenes (*"I only came to visit Dad, I don't care about money"*).
- **The Core Fix**:
  - **Progressive Unveiling & Anti-Spoiler Law**: Never spoil the series' master secret via flat exposition in Episode 1. Plant **Visual & Behavioral Paradoxes** (e.g., an aging patriarch whose "frail, trembling hand" suddenly turns steady and iron-fisted when gripping an old keyring or locking a drawer) so the audience senses a deeper psychological game without having the plot lectured to them.
  - **The Velvet-Dagger Social Mask (`Dao Găm Bọc Mật`)**: Calculating antagonists in grounded drama NEVER attack with crude, obvious insults in opening scenes. They weaponize **polite concern, filial care, or sympathetic pity** to assert dominance (e.g., smiling warmly while expressing "worry" that a father's aging hands are too tired to run the corporation, or praising a sibling's "simple, stress-free life" at a small port garage to belittle them).
  - **Specific Lived-In Detail Over Moral Slogans (`Chi Tiết Đời Thực Chạm Tim Đen`)**: Protagonists NEVER preach their own virtue or repeat the same defensive statement across consecutive clips. Instead, they speak through **one concrete, intimate human observation** (e.g., noticing a parent's cold knuckles in the rain, remembering the exact sound or weight of a worn family heirloom) that proves genuine love and triggers a visceral reaction in the listener.
  - **Zero Semantic Repetition Across Consecutive Clips**: Two consecutive 10s clips must NEVER repeat the same conversational point; each clip must advance to a new psychological layer.

### 4. Law 4: The Anti-Caricature & Forensic Antagonist Logic Law
- **The Shallow Trap**: Writing `A1` as a 100% spotless, passive saint and `A2` as a 1-dimensional, moustache-twirling idiot whose scheme violates basic common sense (e.g., forging a fatal poison or stealing an exam in a way that immediately incriminates themselves), followed by `A2` weeping and repenting after a 5-second moral lecture.
- **The Core Fix**:
  - **Flawed Active Protagonist (`A1`)**: `A1` MUST possess an active flaw, blind spot, stubborn pride, or protective `Lie` whose tactical choices directly worsen the crisis (§1.1).
  - **Forensic Antagonist Logic & "Where A2 Is Right" (`A2`)**: `A2`'s scheme MUST pass the **Real-World Forensic & Idiot-Plot Test** (§9.5) — every move must be calculated, plausible, and protected by an alibi or institutional leverage. Furthermore, `A2` MUST hold a coherent worldview with at least one grain of objective truth (`Where A2 Is Right`).
  - **Ban on 5-Second Sermon Conversions**: Antagonists NEVER collapse into tearful remorse simply because `A1` gave a polite speech. Any breakdown or defeat must be forced by undeniable forensic checkmate, irreversible leverage loss, or a direct strike to `A2`'s own deepest `Wound` (`B-V2 Achilles' Heel`).

### 5. Law 5: The Multi-Sequence Spatial Breathing Law (`W11`)
- **The Shallow Trap**: Trapping 8–10 consecutive scenes inside a single static room or corner where characters merely stand around talking.
- **The Core Fix**: Every episode MUST partition into **2–4 Sequences** (`0c` §4) across distinct architectural spaces, sub-zones, or temporal beats (`Mode B Inter-Sequence Cuts`: *Sensory Match-Cut*, *Question-to-Answer Hook Cut*, or *Parallel Cross-Cut*), unless the premise is an explicit locked-room thriller survival test declared with a `BREAK:` reason.

### 6. Law 6: Mandatory 12-Row Story Spine Lock (`Gate 2B` & `W9`)
- **The Shallow Trap**: Skipping Stage 1 (`CP1`) or writing a superficial 4-row Story Spine that omits specific lived-in details, cliché subversions, ending cost, and misread mechanics.
- **The Core Fix**: Every episode MUST be anchored by the **complete 12-Row Story Spine Card** (§8.10 + §9.9: `QUESTION`, `TRUTH`, `SPECIFIC`, `CLICHÉ`, `LOOPS`, `COST`, `DEBATE`, `IMAGE`, `PREDICT`, `KNOW`, `MISREAD`, `TWIST`). `setting.html` (`Gate 1C` / `Gate 2B`) and each saved Stage 3 script `output/<slug>/ep-NN-script.md` (`engine/screenplay_audit.py`: `W9`, `W10`) enforce these depth anchors.

---

## §2 — DIRECTING FROM INTENT (SCALE, ANGLE, CAMERA WORK, ACTION)

The camera is the audience's attention. Every choice answers: *where should the viewer's feeling be, at this second?*

### 2.1 Shot Scale = Psychological Distance, Moment by Moment
- Ask: **"Whom must the viewer feel with, and how close, right now?"**
- Move closer as the inner stakes rise; pull back when the viewer should **judge**, see **isolation**, or read the **power geometry** of the room.
- A wide shot at the emotional peak can be stronger than a close-up: it shows the character alone with the consequence.
- Inserts (hands, props) are for moments when **the object carries the meaning** — the prop is the subtext made visible. Never insert a prop just to "add variety".

### 2.2 Angle = Power at This Instant
- Low angle grants dominance; high angle takes it away; eye level is negotiation between equals.
- **Change the angle when power changes.** The value shift from §1 is filmed as an angle change, a scale change, or both.
- Do not tilt every shot. An unchanged eye level across a whole scene says "nobody wins yet" — that is also a statement.

### 2.3 Camera Movement Needs One of Three Motives
Move the camera only when you can name the motive:
- **(a) Follow attention** — the camera goes where the character's eyes or body go.
- **(b) Reveal information** — the move uncovers something the viewer did not have (a hidden listener, a prop, a reaction).
- **(c) Express an inner shift** — a slow push-in on realization, a drift away on abandonment, a handheld tremor on panic.

**Static is a valid and often superior choice.** A locked frame at the peak lets the actor's micro-physics carry the scene. "Static" still means living subjects and living light — never a freeze frame (Hard Constraint). Orbits, cranes and arcs without motive (a), (b) or (c) are cut.

### 2.4 Action = The Want Expressed Through the Body
- Every primary action is a tactic: the character *does* something to get what they want (hands the bowl over to win favor, turns the crib away to refuse).

### 2.5 Target-First Camera Grammar & Optical Prop Vector Law (Quay Khóa Mục Tiêu Vào Đối Tượng Chính — Không Quay Theo Góc Nhìn Khán Giả)
- **Target-Subject Identification Over Audience-Spectator Framing**: Never place the camera in a passive "theater spectator" seat lining characters up flat side-by-side (`medium two-shot` / `side slider`). Every shot MUST answer **"Who is the Primary Target Subject receiving or delivering the psychological/physical force right now?"** and lock the camera axis directly onto that target (`over-the-shoulder perspective from behind [A] targeting [B]`, `reverse over-the-shoulder perspective from behind [B] targeting [A]`, or `tight medium two-shot angled toward [Target] with focus locked on [Target]'s face`).
- **Optical Prop Vector Law (`Đạo Cụ Hướng Vào Đối Tượng Mục Tiêu`)**: When Character A confronts Character B with a handheld prop (a compact mirror, a store receipt, a phone screen, a contract), both Character A's eyeline AND the active face of the prop MUST point physically at Character B — **never rotate or cheat a mirror/receipt/screen flat toward the audience/lens** (which creates optical reflection paradoxes and breaks spatial reality).
- **Full-Face Target Lock vs. Optional Selective Obscuration**: Keep full faces and eyes clearly visible on the Target Axis in comedy, sitcom, romance, and direct interpersonal showdowns so the clash between the Trigger's piercing gaze and the Target's stunned/flinching expression lands directly. Use *Selective Face Obscuration* (`showing only lower face, jawline...`) only when hiding a mysterious thriller predator's expression is the specific dramatic goal.
- **One primary action per phase** keeps AI motion clean; the reaction of the other body is the second layer.
- Prefer actions that **change the state of the world** (a door closed, an object moved, a distance crossed). Actions that only illustrate a line ("nods while agreeing") are filler.
- Small, tactile, readable actions beat big choreography in domestic drama (Hard Constraint for Minors: zero fights, chases, or danger involving minors per Gate 3F; for adult characters, high-velocity martial arts, chases, and supernatural combat are governed by [`engine/genres/action.md`](file:///d:/Project/Sven/engine/genres/action.md) and [`@CombatDirector`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md)).

### 2.5b Track A or Track B — Decide by Question, Not by Habit
- **Track A (one continuous take):** the viewer must stay inside one breath, one body, one unbroken pressure — confessions, realization, intimacy, dread.
- **Track B (cuts on the 180° axis):** the viewer must see both sides of a collision — whose move lands, who absorbs it.
- The number of phases and where they split come from the scene's beats. A scene may be 2 phases or 4; one line may take 6 seconds while the silence after it takes 4.

### 2.6 The "Why" Test (one clause per choice)
Before compiling, every shot carries a rationale the Director could defend aloud:
```
Shot 2 — OTS past Má Ba, eye level, cut on the axis — power passes to Khang; the viewer must see her face receive it.
```
If the only reason is "looks cinematic", "adds variety" or "the model blueprint says so", change the choice.

### 2.7 Scene Action Structural Intelligence & Episode-Level Storytelling Symphony
1. **Structure Over Fixed Timeline Numbers (`5 Core Scene Action Flows`)**:
   - Never reduce scene directing to a single mechanical timestamp grid. Design the `Action / Shots` flow of each `10.0s` or `15.0s` clip according to its dramatic job (see [`0b-temporal-camera-grammar.md` §1.1](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md)):
     * **Opening / Hook Scene**: *In Medias Res Motion ➔ Anomaly / Focus Narrowing ➔ Open Curiosity Hook*.
     * **Storytelling / Narrative / `V.O.` Scene**: *Visual Emotion Leads First ➔ Vocal / Inner Thought Lands on Ocular Shift ➔ Tactile Settle*.
     * **Dialogue / Confrontation Scene**: *Opening Probe/Mask ➔ Counter-Action / Evidence on Target Axis ➔ Checkmate Turn ➔ Wordless Somatic Payoff*.
     * **Clue Discovery / Micro-Visual Twist Scene**: *Normal Facade ➔ Macro / Close-Up Tactile Insert (Show, Don't Tell) ➔ Attitude Reversal*.
     * **High-Velocity Action / Combat Scene (`@CombatDirector`)**: *Tension Ignition / Snap Freeze ➔ Pure Kinetic Tracking/Clash (0 Dialogue) ➔ Hard Stop / Impact / Trap ➔ Dominance & Fallout*.
   - Inside every individual `Shot`, write a **3-Layer Causal Micro-Structure**: `(1) Target-Locked Camera Header` $\to$ `(2) State-Delta Initiating Action + Immediate Visible Reaction/Shift` $\to$ `(3) Matched Vocal Line (when speech is present, sized to the shot's duration)`.
2. **Episode-Level Storytelling Symphony (`How Scenes Form a Great Episode`)**:
   - An episode is a complete emotional journey, never 12 identical scenes strung together. Orchestrate the 5 Scene Structures across the **4-Stage Episode Arc** (*Stage I: Opening Hook + V.O./Atmosphere ➔ Stage II: Alternating Dialogue Probe ↔ Clue Discovery ➔ Stage III: 10s/15s Climax Showdown or Action Burst ➔ Stage IV: Emotional Settle + Cliffhanger*), governed by **Rhythmic Contrast (`Compress ↔ Release`, `Dense Dialogue ↔ Visual/Silent`)** and **Causal Baton Relay (`"Therefore / But"` from Scene $K$ tail to Scene $K+1$ head)**.

### 2.7b Spatial Geometry of Power & Proxemics (Blocking as Subtext)
Blocking (the placement and movement of bodies in 3D space) tells 80% of the story before anyone speaks:
- **The Topography of Power**:
  - *The Threshold / Doorway*: Represents dominance, external intrusion, or the power to trap/exit. The character commanding the doorway controls access to the outside world.
  - *The Ground / Bed Edge*: Represents vulnerability, defensive retreat, and emotional collapse. Sitting on the floor leaning against a bed frame is the posture of a subject pushed to the absolute psychological wall.
  - *The Center / Trench*: The neutral or disputed zone. Standing in the center makes a character vulnerable to multi-directional pressure or positions them as an active human shield.
- **Vertical Axis = The Axis of Dominance**:
  - Standing tall grants authoritative judgment; kneeling or crouching reflects desperate defense or filial supplication; sitting flat signals physical/emotional exhaustion.
  - *A change in vertical posture is an earthquake in power*: When a character rises from the floor to eye level with an elder, the balance of power permanently flips.
- **Proxemic Breaches (< 45cm Intimate Zone)**:
  - Moving into another character's intimate zone is either an act of profound tenderness or aggressive intimidation. When an elder storms directly to the crib rail, it is an aggressive breach that triggers an involuntary biological retreat in the mother.

### 2.8 Active vs. Supporting Motion Budget (`≤ 2 Moving Characters per Phase`)
To keep multi-character scenes stable and natural in AI video generation:
- **One Primary Action for the Active Subject; Static State for Supporting Characters**: Never force 3 or 4 characters to move, lean, and gesture simultaneously in the same phase. The active character performs **1 clear movement** (`sets the brass keyring onto the walnut table`, `walks to the foot of the table and stops`), while supporting characters hold a **clean static state** with an explicit eyeline (`monica_thornton sits still with eyes fixed on harold_thornton`).
- **Observable Facial Reaction**: When Character A speaks or acts, the listener (Character B) reacts through **1 clear visible facial change** (`bradley_thornton's smile hardens into a cold stare toward evan_thornton`) placed at the end of the sequential sentence (`then ... as ...`).

---

## §3 — SCREENPLAY DEPTH: ACTING AND DIALOGUE LOCKED TOGETHER

### 3.1 Dialogue Is Action
A line is something one character **does to another**: presses, soothes, tests, dismisses, begs, traps, confesses. If you cannot name the hidden verb of a line, cut the line.

### 3.2 Never Say What the Image Already Shows
If the frame shows the baby sleeping, nobody says "the baby is sleeping well". Dialogue carries what the camera cannot: intention, history, threat, a lie.

### 3.3 The Two-Tier Cinematic Action Framework

In Sven's cinematic architecture, **Action** is orchestrated across two interdependent operational tiers. Every scene's action is governed by the universal formula:
> **Scene Action Formula = [Tier 1: Relationship] + [Tier 2: 10s Kinetic Dynamic]**

#### Tier 1: The Four Action ↔ Line Relationships
Every spoken line or character exchange MUST select exactly one of these four fundamental body-word relationships:

| Relationship | Mechanism | Application & Example |
|---|---|---|
| **1. REINFORCE (Tương hỗ / Cùng chiều)** | Body and speech drive in the exact same vector. Long-suppressed energy explodes outward simultaneously. | *Best for*: Climax eruptions, shouting while slamming a table, collapsing to embrace knees in desperate weeping. (Rare in dialogue, powerful in explosion). |
| **2. CONTRADICT (Phản đề / Nghịch chiều)** | Speech claims one thing; somatic body betrayals reveal the exact opposite. **The Primary Engine of Subtext (70% of Drama)**. | *Best for*: Pride, guilt, suppression. E.g., saying *"I can handle it myself, mother"* while trembling fingers claw the iron bedframe until knuckles turn white; smiling weakly while avoiding eye contact. |
| **3. REPLACE (Câm lặng tuyệt đối / Thay thế)** | **Complete deletion of speech**. Tactile friction with props, spatial repositioning, and somatic shock carry 100% of the narrative weight. | *Best for*: Climax peaks (Anagnorisis), devastating truth bombs where spoken words would diminish the gravity of trauma. E.g., standing frozen, swallowing hard, picking up a torn slip, walking away in silence. |
| **4. REVEAL (Bóc trần / Lật tẩy bí mật)** | Covert physical action unmasks a secret that the spoken line is actively trying to camouflage. | *Best for*: Deception, investigation, conspiracy, betrayal. E.g., speaking cheerfully on the phone with a spouse while quietly sliding an DNA test envelope under the sofa cushion. |

#### Tier 2: The Five 10s / 15s Scene Rhythms (One Dramatic Beat per Clip — Image Speaks First, Dialogue Speaks Second)
Depending on dramatic tension and narrative role, each `10.0s` scene (1 moment, 1 emotion, `0–22 words total`) or `15.0s` key turning-point/climax scene (1 moment + 1 small shift, `18–32 words total`; budgets per `0c` §2) is directed as **one dramatic beat** — its shot topology chosen by intent (§0.1.6) — in one of these 5 rhythms:

| Rhythm | Mechanism & Physical Action | Dialogue Economy (`~2.5 words/s` + `1.0s` Buffer) |
|---|---|---|
| **1. In-Medias-Res Probe & Counter (`10s` — 2 Beats: `00:00–00:05.0` & `00:05.0–00:10.0`)** | Enters directly in the middle of conflict (zero greetings). Beat 1: Character A performs a concrete tactile action and delivers a veiled probe. Beat 2: Character B reacts physically first, then lands the shortest closing line. | `1–2` lines (`15–22 words total`). Max 1 speaker per 5s beat. Final line is the **shortest line in the scene** (`4–7 words`), ending by `00:08.8`. |
| **2. Authority Verdict / Single-Speaker Weight (`10s`)** | High-status character or emotional lead performs 1 decisive prop action and speaks 1 weighty line while the counterpart absorbs in visible somatic silence (`jaw clench, fingers tightening on glass`). | `1` line (`8–15 words total`). Listener speaks `0 words` — physical reaction replaces speech. |
| **3. Turning-Point & Subtext Reversal (`15s` — 3 Beats: `0–5s`, `5–10s`, `10–15s`)** | Reserved for key turning points and climaxes (`20–25%` of episode). Beat 1: Provocation/obstacle. Beat 2: Unexpected specific detail or prop reveal shifts leverage. Beat 3: Shortest closing line + irreversible somatic fallout. | `2–3` lines (`18–32 words total`). Max 1 speaker per 5s beat. Finishes speech by `00:13.8`. |
| **4. Pure Visual & Tactile Silence (`10s` — `Model 0`)** | Every episode includes at least 1 silent or near-silent scene so dialogue-heavy scenes hit harder. Pure action, prop friction, and facial transition carry 100% of the turn. | `0 words spoken`. 100% visual storytelling and diegetic Foley. |
| **5. False Dawn to Cliffhanger Hook (`10s` or `15s`)** | First two-thirds appear to settle the beat; final beat introduces an unexpected visual/auditory clue or unfinished question that propels directly into the next scene or episode. | `1–2` lines (`15–22 words`), ending on a sharp hook or interrupted revelation. |

### 3.4 Fewer Words Near the Peak & Shortest Closing Line Law
Lines shorten as stakes rise. High-power characters speak less than low-power characters, and **the closing line of a scene MUST be the shortest line in that scene** to land with maximum impact and pull the viewer into the next scene.

### 3.5 The 5-Tier Dialogue Architecture: Voice Profiles (`Blind Test`), Natural Spoken Ellipsis & Kinship Shifts
1. **Tier 1 — Individual Voice Profile (`Hồ Sơ Giọng Nói — Che Tên Vẫn Đoán Được Ai Nói`)**:
   - Every character has a locked **Voice Card** established once for the entire series:
     * **Sentence Rhythm (`Cách nói`)**: Long polished upper-class sentences vs. clipped authoritative commands vs. quiet observational statements vs. defensive questions.
     * **Vocabulary & Kinship Register Card (`Từ vựng & Thẻ xưng hô`)**: Signature words and exact relational address (`Bố – Con`, `Anh cả – Chú em`, `Tôi – Ông`), plus the exact threshold where address shifts (`from "Bố" to "Ông"` signals an irreversible relationship rupture).
     * **Verbal Habit (`Thói quen thoại`)**: Sarcasm, understatement, changing the subject, or answering a question with an action.
     * **What They NEVER Say Straight (`Điều không bao giờ nói thẳng`)**: Every character has one emotional truth they always avoid stating directly (e.g., Harold never says *"Bố xin lỗi"* or *"Bố nhớ con"*).
     * **Fixed AI Voice Spec (`Thông số giọng AI cố định`)**: Age, vocal timbre, and baseline tone copied identically across all prompts for that character.
   - **The Blind Voice Test**: If you hide the speaker names on any two lines and cannot tell who spoke which line, the dialogue is too generic and must be rewritten.
2. **Tier 4 — Natural Spoken Vietnamese Economy (Purging Artificial Formulaic Padding)**:
   - Write authentic spoken language: **short, elliptical sentences (dropping redundant pronouns/subjects when natural in speech), zero greetings (`"Chào bố con mới về"`), zero introductory fluff, and zero forced modal-particle formulas** that make every character sound identical.
   - **Image Speaks First, Dialogue Speaks Second**: Never repeat in dialogue what the camera already shows (*if the character opens the door on screen, never let them say `"Tôi mở cửa đây"`*). Let a hand tightening or an eye shift replace an entire spoken sentence.
   - **Indirect Subtext Over Emotion Labels**: Never state feelings directly (*`"Tôi ghen tị với em vì bố thương em hơn"`*). Express the emotion through a concrete comparative fact (*`"Bố gọi cho em mỗi tuần. Còn tôi? Tôi nghe tin bố ốm từ người giúp việc."`*).
3. **Tier 3 & Tier 5 — Inter-Episode Dialogue Ledger (`Sổ Thoại`) & Inter-Scene Dialogue Bridges**:
   - Track **Echo Lines (`Câu lặp` returning 2–3 episodes later with inverted meaning)**, **Promises & Threats**, **Spoken Lies**, **Unfinished Lines**, and **Who Knows What (`Ai biết gì`)** after each episode.
   - Bridge consecutive scenes via **Question in Scene N → Answer/Action in Scene N+1**, **Word Hooks (`Cầu nối bằng chữ` — repeating a key word from the end of Scene N at the start of Scene N+1)**, and **Rhythmic Alternation** (dense dialogue scene followed by a quiet or silent scene).

### 3.6 The Three Analytical Tiers of Dialogue
1. **Tier 1: Optical & Acoustic Source**:
   - *Spoken In-Frame*: Mouth moves with synchronous lip-sync; requires visible lips and frontal-to-three-quarter camera angle.
   - *Voice-Over (V.O.)*: Internal subconscious voice; **lips remain 100% sealed** while eyes/hands betray internal conflict.
   - *Off-Screen (O.S.)*: Voice penetrates from outside the frame (staircase, hallway); camera captures the listener's visceral recoil.
   - *Intimate Whisper*: Low-volume, breathy sibilance (1.1–1.3 WPS), minimal lip travel; head-to-head proximity.
   - *Silence (Model 0)*: Exactly 0 words; pure physical eloquence where words would shrink the moment.
2. **Tier 2: The 8 Interaction Geometries (Pillar 1 Master Models)**:
   - Model 1 (Binary Duel), Model 1B (Rapid Staccato), Model 2 (Ensemble), Model 3 (Solo Lead + Silent Absorber), Model 4 (Contradicting V.O.), Model 5 (O.S. Intrusion), Model 6 (Proximity Whisper), Model 7 (Kinetic Interruption), Model 8 (Direct P.O.V.).
3. **Tier 3: Subtext & Tactical Function**:
   - *The Scalpel Line*: Strips the counterpart's pride without raising the voice ("This bottle... doesn't even wet the bottom").
   - *The Deflection Mask*: Talks about domestic trivia to evade an unbearable truth ("The soup is a bit salty today").
   - *The Ultimatum*: Terminates compromise and permanently alters the balance ("One more step... and I carry my wife away").
   - *The Anagnorisis Reveal*: The instant entrenched pride shatters upon physical evidence ("Good God... your wrist... when did you get an IV without telling me?!").

---

## §4 — VOICE MODE PALETTE (CHOSEN PER SCENE, NOT PER PROJECT)

The Screenwriter chooses the voice mode for **each scene** from the dramatic need and records it in the Scene Intent Card with a one-clause reason.

| Mode | Dramatic need that calls for it | Pillar 1 catalog entry |
|---|---|---|
| **Dialogue (2 voices)** | Two wants collide; power is contested | Model 1 (measured) / Model 1B (rapid volleys) |
| **Ensemble** | Collective pressure, judgment, public opinion | Model 2 |
| **Solo line + silent listener** | A verdict, a confession, a deadpan that the other must absorb | Model 3 |
| **Direct monologue** (spoken aloud to someone who cannot answer: a photo, a grave, a sleeping baby, an empty chair) | A truth the character can only say to someone who cannot reply | Model 3 variant (single speaker, Track A) |
| **Inner monologue (V.O.)** | Thoughts the character will never voice; lips stay sealed | Model 4 |
| **Hybrid: spoken line + contradicting V.O.** | Saying one thing while thinking the opposite — betrayal, hidden pain, polite lies | Model 1/3 + Model 4 |
| **Off-screen voice (O.S.)** | The outside world breaks into the room | Model 5 |
| **Whisper** | Secrecy, intimacy, danger of being overheard | Model 6 |
| **Interrupted** | An action or event cuts a line off; the cut itself is the meaning | Model 7 |
| **Direct address / POV** | The viewer is placed inside the relationship | Model 8 |
| **Silence** | The peak, where words would be smaller than the moment | Model 0 |

**Timings and word budgets in the Pillar 1 models are calibrated to the 2.5 words/s AI Video Lip-Sync Standard**: `10s` scene = `0–2` lines (`15–22 words total`, max 2 turns); `15s` scene = `0–3` lines (`25–35 words total`, max 3 turns); max 1 speaker per timestamp beat; closing line is the shortest line in the scene; no lip-sync during a downward POV; V.O. with lips sealed.

### 4.1 Episode Rhythm
- Avoid **3 or more consecutive scenes in the same mode or same emotion/tempo**.
- Every episode MUST include **at least 1 silent or sparse-dialogue scene** so dialogue-heavy scenes hit with full weight.
- High-status characters speak fewer words with heavier gravity.

### 4.2 Writing V.O. and Monologue Inside Code Block 1
- **Spoken monologue / single line**: same syntax as dialogue: `Name says : “ line ” (...)`; only one speaker in that beat. The listener reacts through visible physical action (`then / as`).
- **V.O.**: same `Name says : “ line ” (...)` (or `inner voice`) syntax; the parenthetical states `inner voice-over, lips remain sealed` and still begins with `Voice of a [N]-year-old ...`. The prose shows the face doing something the voice does not say.
- **Silent scene**: no quoted lines in that prompt; the dialogue card for that scene states the silence.

### 4.3 One Dramatic Beat per 10s / 15s Clip (Topology Follows Intent)
Every `10.0s` clip carries **one dramatic beat** and every `15.0s` clip one beat plus one small shift. Whether that beat is shot as one continuous take (`Track A`, `Mode D1-A` shared fixed-camera header) or as `2–4` static cuts (`Mode D1-B / D1-C / D1-D`) is decided by intent (§0.1.6) within the shot counts of `0c-canonical-numbers.md` §1. When a scene needs a second beat (a new want, a new reveal), give it its own clip instead of cramming it into this one.
---

## §5 — CREATIVE REVIEW (SELF-CHECK BEFORE COMPILE)

Run this after drafting the 1-line scene list and continuous rough prose of the episode:

**Story & 5-Tier Series Architecture (§8)**
- [ ] Tier 1 (Series) is locked: Logline, Central Question, Want vs. Need, Antagonist with own goal, Master Secret (hidden until ~2/3 of series), Transformation Arc (A→B), Episode/Act Map, and Ending.
- [ ] Tier 2 (Episode) has: Episode Goal, Obstacle, 1 Irreversible Shift, 1 New Layer of the Master Secret (never spoiling the whole secret early), 4-Beat Rhythm (`Open 15–20% ➔ Develop 40–50% ➔ Climax 20–25% ➔ Close 10%`), and 1 Memorable Visual/Prop Motif.
- [ ] Tier 3 (Inter-Episode Links) uses at least 2 of the 4 connectors (`Cliffhanger`, `Setup & Payoff [Ep n → Ep n+2+]`, `Visible Consequence [Ep n → Ep n+1]`, `Recurring Motif`) and updates the Tracking Table & Continuity Bible (`Who knows what, prop custody, status changes`).

**Scene & Inter-Scene Links (Tiers 4 & 5)**
- [ ] The 1-Line Scene List (`Địa điểm, ai, làm gì, để làm gì`) was verified first, and every pair of scenes connects via **"Therefore (`Vì vậy`)"** or **"But (`Nhưng`)"** — never *"And then (`Và rồi`)"*.
- [ ] Each scene does **strictly ONE thing** (`10s` = 1 moment/emotion; `15s` = 1 moment + 1 shift for turning points/climaxes).

**Dialogue (5-Tier Dialogue Architecture)**
- [ ] **Blind Voice Test (Tier 1)**: With speaker names hidden, any two lines are still immediately distinguishable by rhythm, vocabulary, kinship address, and *What They Never Say Straight*.
- [ ] **Image Speaks First, Dialogue Speaks Second (Tier 4)**: No line repeats what the camera already shows; physical reaction replaces redundant lines.
- [ ] **Word & Turn Economy (Tier 4)**: `10s` = `0–2` lines (`15–22 words total`, max 2 turns); `15s` = `0–3` lines (`25–35 words total`, max 3 turns); max 1 speaker per beat; natural spoken Vietnamese (elliptical/short sentences allowed); **closing line is the shortest line in the scene**.
- [ ] **Inter-Scene Dialogue Bridges (Tier 5)**: Consecutive scenes link via Question → Answer/Action, Word Hooks (`Cầu nối bằng chữ`), and tracked information flow (`Who heard what`).

**Direction**
- [ ] Every camera move names its motive (a / b / c). Unmotivated orbits and cranes are removed.
- [ ] Angle or scale changes where power changes.
- [ ] At least one static frame is considered for the peak of the episode.
- [ ] Phase splits differ across scenes; fewer than half the scenes share the same split.

**Rhythm**
- [ ] No 3 consecutive scenes share a voice mode without a stated reason.
- [ ] Turn counts vary across scenes.
- [ ] Every broken Craft Default carries a `BREAK:` line.

---

## §6 — WORKED EXAMPLE (BEFORE / AFTER)

**Situation**: the grandmother (Má Ba) brings an old hammock into the young couple's bedroom; the couple use a crib on the doctor's advice.

### Before (mechanical)
> Má Ba: "Xưa giờ cả họ nằm võng! Nôi gỗ lạnh ngắt vầy, sao thằng nhỏ ngủ yên hả Duyên?!"
> Khang: "Dạ má... Bác sĩ dặn nằm nôi phẳng cho thẳng lưng má ơi!"
> Camera: orbit 90°. Split: 00:00–04.5 / 04.5–10.

Problems: both characters **explain their arguments**; the action illustrates the words; the reply opens with the reflex "Dạ má..."; the orbit has no motive; nothing flips between the first and last frame.

### Intent first
```
INTENT  | Want: Má Ba → stay needed as grandmother; Khang → protect wife and baby without wounding his mother
SHIFT   | Má Ba: certain → emptied
SUBTEXT | Má Ba fears she has become unnecessary
GAP     | Empathy — the viewer sees both are right
VOICE   | Mode: Dialogue, two lines, landing in silence — because the refusal must be polite to hurt
LINK    | Action↔Line: Khang CONTRADICTS — gentle words, hands carrying the hammock out of the room
```

### After (Track B, three phases with uneven splits)
```
[00:00–00:04.5] Over-the-shoulder medium shot framing ma_ba past minh_khang's foreground shoulder, shallow depth of field holding sharp optical focus on ma_ba, slight low angle, static camera — ma_ba sets the folded steel hammock frame onto the floor tiles with a sharp metallic clang, standing tall with assertive authority; inside the pine crib a soft blanket rustles.
ma_ba says : “ Võng này ba thằng Khang nằm lớn đó, để đây cho cháu tao! ”（Voice of a 56-year-old woman from the Mekong Delta; proud unhurried tone, firm traditional claim staking family history）

[00:04.5–00:09.0] Cut to an over-the-shoulder shot framing minh_khang past ma_ba along the 180-degree axis, sharp optical focus locked on minh_khang at eye level, static camera — minh_khang steps in firmly, crouches to grip the hammock frame with both hands, lifting it decisively off the tiles as minh_khang's voice tightens with calm defiance.
minh_khang replies : “ Bác sĩ dặn nôi phẳng mới tốt, con mang ra sau hè má nằm nghen! ”（Voice of a 27-year-old Southern Vietnamese man; warm low firm baritone, polite but unyielding filial pushback）

[00:09.0–00:10.0] Snap-cut to an intimate close-up framing ma_ba along the 180-degree axis, shallow depth of field holding razor-sharp optical focus on ma_ba's contracting pupils with background falling into soft blur, eye level, static camera — ma_ba's jaw drops slightly, pupils contracting as ma_ba's assertive smirk instantly freezes, taking in a sharp ragged breath at 00:10.0.
```

**Rationale**
- Shot 1, slight low angle, static — Má Ba holds the power; the clang is her claim.
- Shot 2, OTS at eye level, cut on the axis — power passes to Khang; the viewer must see the gift that is really a refusal.
- Shot 3, close-up, slow push-in — motive (c): the moment she realizes she is not needed. No line, because any line would shrink it (relationship: **replace**).
- Neither character mentions "crib versus hammock". The conflict lives in the objects and the hands.

### Same character, different mode (direct monologue)
That night Má Ba sits alone on the porch, stroking the old hammock rope, speaking to the empty space where her late husband used to lie:
> "Ông coi, giờ tụi nhỏ hổng cần tui nữa."

Why monologue: this truth can only be said to someone who cannot answer. Why Track A with a static frame: the viewer must stay inside one unbroken breath with her.

---

## §7 — HOW TO USE THE PILLARS AFTER THIS DOCTRINE

| Document & Pillar | Authority Domain | Precedence & Usage Standard |
|---|---|---|
| [`0-creative-doctrine.md`](file:///d:/Project/Sven/engine/references/0-creative-doctrine.md) | Story spine, thematic core, scene intent card, creative review | Single Source of Truth for dramatic intent, subtext, and creative direction. |
| [`0b-temporal-camera-grammar.md`](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md) | Quantitative timing grammar, wps, word caps, lip-sync capacity, buffer laws | **Master SSOT for all numerical figures and word budgets** (trumps all narrative suggestions). |
| [`1-narrative-screenplay-architecture.md`](file:///d:/Project/Sven/engine/references/1-narrative-screenplay-architecture.md) (Pillar 1) | Beat curves, 12 hooks, 20 twists, dialogue interaction suites (Models 0–8), parentheticals | Menu of dramatic patterns. Timings and word budgets defer to `0b`. |
| [`2-casting-worldbuilding-specification.md`](file:///d:/Project/Sven/engine/references/2-casting-worldbuilding-specification.md) (Pillar 2) | Casting archetypes, Model Sheets (Human Adult, Minor Mẫu 0B, Non-Human Mẫu 3), Prop & Location Universes, `setting.html` | **Master SSOT for all pre-production Model Sheets and entity specifications**. |
| [`3-cinematography-3d-staging.md`](file:///d:/Project/Sven/engine/references/3-cinematography-3d-staging.md) (Pillar 3) | 14 shot scales, 4-axis angle architecture, camera combos, 3D spatial staging, 180° action axis, continuity ledger | Master cinematic visual staging vocabulary. |
| [`3b-lighting-atmospheric-physics.md`](file:///d:/Project/Sven/engine/references/3b-lighting-atmospheric-physics.md) | 6-point lighting contract, atmospheric medium, sensory color temperature | Master SSOT for lighting physics; raw numeric Kelvin is banned system-wide. |
| [`4-ai-video-prompt-compiler.md`](file:///d:/Project/Sven/engine/references/4-ai-video-prompt-compiler.md) (Pillar 4) | Prompt block architecture (Code Blocks 1/2/3), Track A/B syntax, Minor Protection Protocol (§[10d]), HTML delivery spec | **Master SSOT for prompt compilation syntax, safety, and audit gate enforcement**. |
| [`4b-diegetic-foley-sound-design.md`](file:///d:/Project/Sven/engine/references/4b-diegetic-foley-sound-design.md) | 4-layer diegetic soundscape, acoustic spatialization, Foley handover | Master SSOT for audio and foley sound design. |

**Order of thought at Stages 2, 3 and 4**: Story Spine Card (§8, once per episode) → plot engine: Prediction Ledger, Knowledge Matrix, twist plants (§9) → Intent Card (§1, per scene) → voice mode (§4) → Action↔Line pairing (§3) → scale / angle / movement with reasons (§2) → Pillar syntax → Creative Review (§5) → compile and audit.

---

## §8 — STORY-LEVEL DEPTH & ORIGINALITY (BEFORE ANY SCENE)

§1–§7 make a **scene** good. §8 decides whether the **story** deserves telling and whether it is told the way only this film could tell it. Pillar 1 catalogs (6-beat, 8-beat curve, 20 twists, 12 hooks, addiction engines) are menus of patterns; a script assembled only from catalog entries is correct and forgettable. Depth comes from truth, originality from specificity, pull from open questions.

### 8.1 Three Questions Before Opening Any Catalog
1. **What is this story about underneath the plot?** (the thematic question, §8.3)
2. **Why this family, this place, this object — and not any other?** (the specific truth, §8.5)
3. **What will viewers argue about after the last frame?** (the debate seed, §8.7)
4. **What will viewers carry home — and which moment will move them?** (the value, the heart moment and the takeaway, `0d` §2–§4)

If any answer is generic ("family love", "tradition vs. modernity", "it is touching"), keep digging before writing scenes: "touching" must become one specific planted moment, and "family love" one costly choice.

### 8.2 The Dramatic Question (plot level)
One yes/no question the viewer holds from the hook to the climax ("Will Duyên say how much she is hurting before her body says it for her?"). Every scene raises or lowers the odds of the answer. An episode may answer its own question while the series question stays open.

### 8.3 The Thematic Argument (meaning level)
- State the theme as a **question with two honest answers**, not as a slogan: "Is love that refuses to listen still love?"
- Each answer is embodied by a character who is **right about something**. The opponent holds the strongest version of the other side.
- **No strawmen.** If the opposing character can be dismissed in one line, deepen them until the viewer hesitates.
- The story **answers with an action or an image**, never with a sentence of dialogue.

### 8.4 Character Truth (every principal, not only the protagonist)
| Layer | Question | Example |
|---|---|---|
| **Wound** | What happened to them before the story? | Widowed young; once hid her own postpartum collapse from her mother-in-law |
| **Lie** | What belief did the wound teach? | "If they no longer need my ways, they no longer need me." |
| **Want** | What do they consciously chase in this story? | Keep the grandson in the family hammock |
| **Need** | What truth does the Lie hide? | Be needed through listening, not through rules |
| **Fear** | What exposure do they protect against? | Becoming a guest in her son's house |
| **Paradox** | Which contradiction do they carry? | The harshest voice in the room is the one most afraid of being left |

- In domestic drama the "antagonist" is usually **love pointed the wrong way**. Write that character's Wound first.
- A reversal (forgiveness, change of side, confession) must be powered by **the character's own Wound being touched**, not only by an external event.

### 8.5 The Specific Truth Inventory (the source of originality)
- Before the roadmap, list **10 concrete details only someone who lived inside this world would know**: objects with a history, rituals, food, sayings, sounds, bodily experiences, small humiliations.
- Put **at least 5 on screen**. Mark with ★ the detail that carries the theme; it usually becomes the Wound / Echo prop or the key line.
- Replace every generic argument with a specific one: "tradition says so" → "your father rocked you in this hammock"; "the doctor said" → the IV tape she hid under the blanket.
- If the world is unfamiliar, consult the workspace knowledge first; never invent rituals that misrepresent a real culture.

### 8.6 The Cliché Audit (originality engine)
1. List the **5 choices the audience expects**: character type, conflict path, reconciliation method, final line, cliffhanger.
2. For each: **Keep / Subvert / Refuse**. Subvert or refuse **at least 2**, and record what replaces them.
3. Fresh choices usually come from: (a) a new point of view on a familiar situation; (b) the specific truth; (c) a reversal that recasts a character (the former opponent becomes the defender); (d) a structure from the Pillar 1 "Narrative Structure — 7 Types" menu.
4. Across episodes, never use the same catalog entry (twist type, hook type, cliffhanger type) twice in a row.

### 8.7 Pull: Open Loops and the Debate Seed
- **Open-Loop Ledger** — every scene opens a question, raises its stakes, or pays one off. Record each loop as `L# question — plant sN → pay sM`.
- At least one loop is open at every cut. No loop is paid without a plant. **Plant early the detail that makes the late reversal inevitable** (surprising, then inevitable).
- **Debate seed** — one moral question on which reasonable viewers take opposite sides ("Should she have hidden her pain to keep the peace?"). It drives comments; never settle it with a lecture.

### 8.8 The Earned Ending
- The ending (positive by default; bittersweet or tragic when the project's `ending_mode` says so) must **cost someone something**: who gives up what — a role, a certainty, a mask.
- The ending answers the thematic question with an **action or image**.
- **Every ending leaves a light** (`0d` §7): even a bittersweet or tragic ending hands the viewer something to carry — a lesson owned, a relationship mended, a promise kept. Despair is never the last image.
- **The title is a promise kept by images, not spoken by characters.** Pair an opening image with a closing image that answers it (tears falling into cold congee ↔ a hot spoonful with no tear).

### 8.9 Line-Level Depth Tests (on-the-nose)
Before keeping a line, ask:
1. **Does it label a feeling?** ("I hate…", "I'm afraid…", `ghét`, `sợ`, `buồn`, `thương`) → replace with an action, a memory, or a request.
2. **Does it argue the theme or explain a motive?** ("tradition matters", "the doctor said") → replace with a specific claim rooted in history.
3. **Does it speak the title or the moral?** → cut it; let the image say it.
4. **Could another character in another film say it?** → make it belong to this person (history, object, dialect).

Exception: naming a feeling is valid when the naming *is* the act — a first-ever admission, a lie, a weapon. Write a `BREAK:` line. The audit prints these as **W9** warnings.

### 8.10 Story Spine Card (once per episode; once more for the series)
```
STORY SPINE — [title / episode]
QUESTION | Dramatic: [...?] | Thematic: [...?] (side A: ... / side B: ...)
TRUTH    | [Name]: Wound … → Lie … → Want … → Need … → Fear … | Paradox …   (one row per principal)
SPECIFIC | 1 … 10 (★ = carries the theme)
CLICHÉ   | Expected → Keep / Subvert / Refuse (≥ 2 subverted or refused)
LOOPS    | L1 [question] plant sN → pay sM; L2 …
COST     | Who gives up what at the end
DEBATE   | The question viewers will argue in the comments
IMAGE    | Opening image ↔ closing image (how the ending answers without words)
VALUE    | Positive value affirmed through [Name]'s costly choice (0d §2–§3)
HEART    | Heart moment: scene, specific act/object/recognition, plant scene (0d §4)
TAKEAWAY | What the viewer carries home — never spoken on screen
SHADOW   | What the story depicts but must not glorify, and how (0d §5)
```
It is written at Stage 1 (series or short-film Spine, `CP1`), embedded in `setting.html` (`id="story-spine"`, enforced as a hard blocker by **Gate 2B** and audited across all 12 rows by **W9**), and refreshed per episode in the interactive Stage 3 Rough Script (`CP3`). Scene Intent Cards (§1) inherit from it: each scene's want, subtext, and value shift serve one row of the Spine. §9.9 adds four plot rows (`PREDICT`, `KNOW`, `MISREAD`, `TWIST`).

### 8.11 Worked Example (Authentic Serialization vs. Flawed Melodrama)
- ❌ **Flawed Rushed Melodrama (Banned Pattern)**:
  - Episode 1 opens with conflict ➔ Duyên faints ➔ Má Ba confesses her 30-year-old trauma in tears ➔ cuddle & forgive ➔ Má Ba sings a lullaby ➔ total reconciliation in 100 seconds.
  - *Why it fails*: Characters feel emotionally bipolar. A 30-year entrenched belief is erased by a convenient faint. Conflict is resolved without cost or time to breathe, leaving Episode 2 with nowhere to go except inventing random meddling neighbors.
- ✅ **Authentic Serialized Architecture (Mandatory Standard)**:
  - **Episode 1 (The Inciting Trap & Silent Fracture)**: Duyên’s postpartum exhaustion and dry pump trigger Má Ba’s deep-seated fear of obsolescence. When Má Ba brings the steel hammock, Khang’s gentle refusal lands as rejection. As Duyên’s trembling hands spill the congee and expose the hidden, bruised IV needle marks, Má Ba does NOT deliver a therapeutic confession or offer a warm hug. She freezes in stunned, choking disbelief: *"Tay mầy... mầy vô nước biển hồi nào sao hổng nói tao hay?..."*. The episode cuts to black on the unresolved shockwave—no easy answers, no lullabies, forcing the viewer to binge Episode 2.
  - **Episodes 2–4 (Escalation & Hardening)**: The wound is exposed, but defense mechanisms harden before they soften. Khang is torn between duty and love. Healing is earned across the full multi-act architecture, culminating in the unified Finale.

### 8.12 The 20/80 Structural Law: Standalone Short Film vs. Multi-Episode Series
The structure catalog lives in one place: **Pillar 1 Part II §5** (6 Genre Engines × 5 Act-Specific Episode Archetypes) and its stage instructions in **`workflow.md` §6.3–§6.4**; scene counts and runtimes in **`0c-canonical-numbers.md` §4**. The doctrine only adds the thinking rules:
1. **Format A (standalone short film)** completes the whole 6-beat transformation inside one runtime; Release + Echo stay short (`15–20%`).
2. **Format B (series)** never repeats a closed 6-beat film per episode and never uses a uniform `10 scenes × 10s` length: each episode takes the shape of its Act Archetype, and the finale fuses showdown and coda so Act IV never sags as a separate episode.
3. Choose the Genre Engine from what the audience came for (catharsis, dopamine reversal, adrenaline, intellectual shock, laughter, quiet resonance — §0.05 Layer 2), not from habit.

---

## §9 — PLOT ENGINE & UNPREDICTABILITY (TWIST, MISUNDERSTANDING, COLD WATER)

§8 gives the story truth. §9 makes the viewer **unable to stop guessing and unable to guess right**. Pillar 1 holds the catalogs (3-step twist formula, TW-01…TW-20, False Dawn / Cold Water / Double Twist / Noble Lie, near-miss, five reversals, 13-beat map). §9 decides **when a twist is earned, how the viewer is led, and how surprise survives a mandated positive ending**.

### 9.1 Plot = Choices Under Pressure
- Plot is not a list of events; it is a chain of **choices forced by pressure**, each choice creating the next pressure ("therefore / but", never "and then").
- **Expectation ↔ result gap:** in every scene a character acts expecting one result and gets another. No gap = the scene only confirms; confirmations are merged or cut.
- **Progressive complication:** each gap narrows the options. By the crisis, the protagonist faces **one choice between two goods or two evils** (keep the peace vs. tell the truth). The episode is built backwards from that choice.
- External events may raise pressure, but **the turn of the episode is caused by a character's choice**, never by luck.

### 9.2 Audience Prediction Ledger (the core tool of unpredictability)
At each key scene, write what a typical viewer predicts next — then decide to keep or break it.
```
P# sNN | viewer predicts … | → KEPT
P# sNN | viewer predicts … | → BROKEN sMM | plant sAA, sBB
```
- **≥ 2 BROKEN per episode**, each with plants in scenes **before** the payoff (W10 checks the order).
- **Keep some predictions.** Breaking everything trains the viewer to expect randomness, which is as predictable as a cliché. Kept predictions buy trust; broken ones spend it.
- **Option C rule:** when the viewer is choosing between A and B ("will she obey or rebel?"), the strongest break is a C that was on screen all along and that both A and B ignored. A or B wearing a surprise costume is not a twist.
- Break predictions about **what a character will do or reveal**, not about physics or tone. A broken tone (a slapstick beat in a grief scene) is a mistake, not a twist.

### 9.3 Surprise Under a Positive-Ending Default
When the project keeps the default positive `ending_mode`, the viewer of a short drama senses the ending will be good. Surprise therefore lives in:
1. **How** — the route to the ending is not the expected route (not a collapse, not a lecture, not a stranger's intervention).
2. **At what cost** — someone pays something the viewer did not expect them to pay (§8.8).
3. **Who changes** — the character expected to change stays; the one expected to stay changes.
4. **Fear of the B ending** — make the bad outcome feel truly possible for at least one scene. A happy ending only satisfies if the viewer stopped believing in it for a moment.

### 9.4 Knowledge Matrix (who knows what, when)
| Mode | Audience knows… | Produces | Camera shows first |
|---|---|---|---|
| **Suspense / dramatic irony** | more than the character | dread, "don't do it", protective tension | the hidden thing, then the unaware face |
| **Mystery** | less than the character | curiosity, re-reading of earlier scenes | the reaction, withholding its cause |
| **Empathy** | the same as the character | shock shared at the same instant | the character's face as the truth lands |

- Track per principal: what each character knows at each scene, and what the audience knows.
- **Switch modes at least once per episode.** The strongest switch: irony turns into mystery when the viewer learns a character **knew all along** ("we thought she didn't see — she saw").
- Never reveal the same information twice; the second time is exposition.

### 9.5 Misunderstanding Engine
A misunderstanding is believable only if all six conditions hold:
1. **Plausible evidence** — the wrong reading is the reasonable one from what the character saw.
2. **A reason not to ask** — pride, fear, a Lie (§8.4), status, custom.
3. **A cost of clarifying** — saying the truth would expose a wound.
4. **Escalation** — each act based on the misreading confirms the other side's misreading.
5. **Audience position chosen** — the viewer either knows (irony) or shares the misreading (mystery); decide which.
6. **Resolution by choice** — it ends because someone chooses to expose themselves, not because a third party explains.

- **Idiot-plot test:** if one honest sentence would end the conflict and nothing makes that sentence costly, the plot is idiotic. Add a cost or cut the misunderstanding.
- **Lifespan:** a misunderstanding lives for one act at most inside a 100 s episode; dragging it past the point where the viewer is frustrated with the character breaks empathy.
- The best misunderstandings are **two-way**: each side misreads the other through their own Lie.

### 9.6 Misdirection Toolkit
- **The camera may withhold, never lie.** It may frame away, cut early, or show a reaction without its cause. It may not show an event that did not happen. A rewatch must find every clue on screen.
- **Red herrings pay off.** A suspicious object or person that leads nowhere is a cheat; it must turn out to mean something else.
- **Double-meaning lines** — a line that reads one way now and another way after the twist ("I know that look").
- **Emotional camouflage** — hide a plant inside a stronger emotional moment so the viewer feels it and does not analyze it.
- **Genre expectation** — let the genre's habit (the cruel mother-in-law) do the misleading; the truth is the character the genre forgot.

### 9.7 Twist Quality Tests
1. **Rewatch test** — on a second viewing, the twist looks inevitable; every clue was visible.
2. **Plant count** — ≥ 2 plants per twist; ≥ 3 for the major twist of the series. Plants appear in different scenes and different forms (image, line, action).
3. **Character test** — the twist reveals who someone is; it does not change who they were. A twist that contradicts established behavior without a planted reason is a cheat.
4. **Budget** — one major twist and one or two minor reversals per ~100 s episode. More twists cancel each other.
5. **Rotation** — the TW code of the major twist differs from the previous episode's (§8.6.4).
6. **Moral test** — the twist deepens the thematic question (§8.3); it does not dodge it.

### 9.8 Cold Water Done Right
- Cold water (the slap after the false dawn) must be **caused** — by a planted person or object, or by a character's earlier choice. A stranger who appears from nowhere is a random shock, not cold water.
- **Genre scale:** in family drama, cold water is a neighbor's sentence, a returned object, an overheard phone call — not a gun, an arrest or an accident. The Pillar 1 examples are thriller scale.
- **Placement:** a mid-episode false dawn (an early, premature reconciliation) makes the final dawn earned; the closing cold water becomes the cliffhanger.
- Rotate the trigger across episodes (a person arrives, an object returns, a call or message lands, a truth is overheard, a promise is broken, a body gives out); never the same trigger twice in a row.

### 9.9 Spine Additions (append to the §8.10 card)
```
PREDICT  | P1 sNN viewer predicts … → KEPT; P2 sNN … → BROKEN sMM | plant sAA, sBB; …
KNOW     | Audience vs. each principal; where the mode switches and why
MISREAD  | Who misreads whom, through which Lie; what blocks the clarifying sentence; where it ends
TWIST    | Major: scene, TW code, plants · Minor: scene, TW code · Cold water: scene, caused by plant in scene …
```
The audit (**W10**) parses PREDICT rows and loop arrows inside `id="story-spine"`: it warns when fewer than 2 BROKEN rows exist or when a plant scene is not earlier than its payoff.

---

## §10 — THE 4 CINEMA ARCHITECTURAL TIERS & THE 12 MASTER STORYTELLING DEVICES (HOLISTIC ORCHESTRATION ENGINE)

> **CORE LAW: NEVER DEPLOY STORYTELLING DEVICES MECHANICALLY.**  
> A shallow script treats storytelling devices as a flat checklist (forcing a flashback into scene 1, cramming a symbolic speech into dialogue, or stuffing all 12 devices into a 60-second runtime). This shatters narrative organic flow and produces stiff, artificial video.
> **True mastery means understanding that the 12 Master Storytelling Devices operate across 4 Distinct Architectural Tiers**—from global macro-timeline sequencing, to inter-sequence tension hinges, to viewer perspective channels, down to non-verbal visual semiotics.

### 10.1 The 4 Architectural Tiers

| Tier | Architectural Layer | Primary Function & Psychological Impact | The Master Devices | Operational Rule |
|---|---|---|---|---|
| **Tier 1** | **Macro-Timeline Architecture** (Trục Thời Gian Toàn Tập) | Governs the global chronological spine of the entire episode. Replaces linear monotony with intellectual intrigue or cross-space tension. | **1. Non-Linear Narrative**<br>**2. Parallel Storylines**<br>**3. Frame Narrative** | **Choose ONE macro-structure per episode based on the story's soul.** Never mix or switch mid-stream without structural purpose. |
| **Tier 2** | **Temporal & Tension Hinges** (Bản Lề Xoay Chuyển Thời Gian & Độ Căng) | Regulates the openings, inter-sequence bridges, and cliffhangers. Liberates characters from the "single-room 100-second spatial trap." | **4. In Medias Res**<br>**5. Flashback**<br>**6. Flashforward**<br>**7. Cliffhanger** | **Operates at the Sequence Boundary.** In AI video, flashbacks/flashforwards must be discrete sequences connected by visual/auditory Match-Cuts, never crammed inside a single 10s shot. |
| **Tier 3** | **Perspective & Meta-Voices** (Kênh Điểm Nhìn & Giao Tiếp Khán Giả) | Determines how the film converses with the viewer's subconscious mind and creates subtext. | **8. Voiceover Narration (Counterpoint V.O.)**<br>**9. Breaking the Fourth Wall** | **Strictly avoid redundant V.O.** Voiceover must create a *Visual-Vocal Counterpoint* (words express denial/justification while visuals expose raw loneliness or guilt). Fourth Wall breaks are reserved for satirical or profound awakening gazes. |
| **Tier 4** | **Visual Semiotics & The Silent Nervous System** (Hệ Thần Kinh Thị Giác Ngầm) | Runs continuously beneath the surface, allowing cinematography, mise-en-scène, and physical props to tell the story without spoken words. | **10. Foreshadowing**<br>**11. Motif**<br>**12. Symbolism** | **Dialogue steps back; visuals step forward.** Foreshadowing is caught by an incidental camera rack focus; Motifs transform across 3 appearances; Symbolism is embedded in spatial blocking and architectural light. |

---

### 10.2 Deep Dive: The 12 Master Storytelling Devices

#### 1. Non-Linear Narrative (Tự sự phi tuyến tính)
- **Psychological Essence**: Inverts the conventional `Cause ➔ Consequence` timeline into `Consequence ➔ Unraveling the Hidden Cause`. Transforms the audience from passive spectators into active mystery decoders (*"Why is this gentle mother standing in front of charred hospital receipts?"*).
- **Execution Mandate**: Used only when the *internal why* behind an action is vastly more shocking than the action itself. Avoid arbitrary timeline scrambling.

#### 2. Parallel Storylines (Tuyến truyện song hành & Cross-Cutting)
- **Psychological Essence**: Intercuts two simultaneous narrative lines unfolding in two separate spatial locations, generating thematic irony, ticking-clock acceleration, or contrasting emotional temperatures before colliding at the climax.
- **Execution Mandate**: The sovereign antidote to the **"trapped in one room for 100s"** disease. Line A (mother packing her belongings in silence) cross-cuts with Line B (son celebrating his corporate promotion), converging when the son opens the front door to an empty foyer.

#### 3. Frame Narrative (Truyện lồng trong truyện)
- **Psychological Essence**: Uses a present-day framing situation (an interrogation, a letter, an old diary, a confession) to enclose an inner re-enacted truth. When returning to the frame in the final scene, the listener's (and viewer's) understanding is fundamentally overturned.
- **Execution Mandate**: Open in Scene 1 (Present Frame) $\rightarrow$ Plunge into the Embedded Truth $\rightarrow$ Close in Final Scene (Present Frame with altered stakes and moral epiphany).

#### 4. In Medias Res (Mở màn giữa tâm bão)
- **Psychological Essence**: Eliminates throat-clearing exposition. Drops the viewer directly into the epicenter of a high-stakes physical action already in motion at second `00:00` (sprinting through driving rain, stuffing money into a hidden compartment, holding a cracked door).
- **Execution Mandate**: The visual and kinetic consequence forces the subconscious question *"What catastrophic event just occurred?"* before a single line of explanatory dialogue is spoken.

#### 5. Flashback (Lát cắt quá khứ) & 6. Flashforward (Lát cắt tương lai)
- **Psychological Essence**:
  - `Flashback`: Never a biographical dump. Appears strictly as a sharp visceral trigger touching the character's *Root Wound* right before a life-altering choice in the present.
  - `Flashforward`: Grants the audience a fleeting glimpse of an impending tragic outcome, establishing suffocating *Dramatic Irony* and dread because the audience sees the trap the character is walking into.
- **AI Video Stateless Rule**: Never blend past and present inside a single 10-second prompt. A Flashback/Flashforward MUST be an independent scene atom or sequence, bridged by a sensory **Match-Cut** (e.g., trembling fingers touching an old scar $\rightarrow$ hard cut to cold operating room tiles in monochrome desaturation).

#### 7. Cliffhanger (Điểm treo đỉnh điểm / Zeigarnik Effect)
- **Psychological Essence**: Exploits the human brain's craving for narrative closure by cutting at the precise moment a devastating truth is revealed or an irreversible physical threshold is crossed, before the reaction completes.
- **Execution Mandate**: Placed at sequence junctions to propel viewers into the next act, or at the final second of an episode in multi-episode series.

#### 8. Voiceover Narration (Vocal-Visual Counterpoint V.O.)
- **Psychological Essence**: Amateur V.O. narrates what the eyes already see. Masterclass V.O. establishes **Counterpoint Tension**: the voice claims emotional detachment or victory, while the camera exposes physical devastation and isolation.

#### 9. Breaking the Fourth Wall (Phá vỡ bức tường thứ tư)
- **Psychological Essence**: The character turns their gaze directly down the camera barrel, making the viewer an accomplice or a moral judge.
- **Execution Mandate**: Used sparingly. In domestic drama, often executed as a silent, searing 2-second direct gaze into the lens at the moment of moral awakening, shattering fictional safety.

#### 10. Foreshadowing (Điềm báo thị giác)
- **Psychological Essence**: Plants an innocuous physical detail early (a frayed hammock cord, a cracked tea cup, a clinical appointment card tucked under congee) so that when tragedy strikes, the outcome feels shocking yet mathematically inevitable.
- **Execution Mandate**: The camera captures it incidentally via a rack focus or passing glide while characters remain unaware. Strictly forbidden for characters to point at or explain the foreshadowing.

#### 11. Motif (Điệp khúc thị giác & âm thanh)
- **Psychological Essence**: A signature visual object, camera angle, or auditory refrain that repeats 2–3 times across the narrative, with its **meaning undergoing radical transformation** each time in alignment with character evolution.
- **Execution Mandate**:
  - *Appearance 1 (Setup)*: Pristine, hopeful, or oppressive.
  - *Appearance 2 (Crisis)*: Damaged, neglected, or contested.
  - *Appearance 3 (Resolution)*: Restored, released, or transcended with new sacred meaning.

#### 12. Symbolism (Biểu tượng hóa không gian & vật thể)
- **Psychological Essence**: Externalizes abstract psychological states (entrapment, purification, severance) into physical set architecture, lighting temperature, and proxemic blocking.
- **Execution Mandate**: Concrete physical mise-en-scène—doorway thresholds dividing estranged family members, window grill shadows casting cage bars across a guilty face, washing ink-stained hands under a clean stream of water in a ceramic basin.

---

### 10.3 The 3-Step Holistic Storytelling Engine (Workflow Protocol)

When authoring a script at Stage 2 and Stage 3, the Screenwriter and Director execute this three-step orchestration:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ STEP 1: MACRO-ARCHITECTURE SELECTION (CHỌN KIẾN TRÚC TỰ SỰ TOÀN TẬP)          │
│ Grounded in the Story Soul (Doctrine §8). Select ONE global spine:           │
│ • Linear Multi-Spatial (Parallel Storylines + Cross-Cutting)                 │
│ • In Medias Res + Reverse Decryption (Non-Linear + Flashback Match-Cuts)    │
│ • Embedded Frame Narrative (Present Frame ➔ Core Journey ➔ Epiphany Frame)   │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STEP 2: MULTI-SEQUENCE PARTITIONING & TEMPORAL HINGES (CHIA TRƯỜNG ĐOẠN)     │
│ Partition the episode into 3–4 distinct SEQUENCES (different spaces/times):  │
│ • Within a Sequence (same room/time): Enforce the 2s Kinetic Baton Relay.    │
│ • Across Sequence Boundaries: Bridge via Sensory Match-Cuts (auditory /      │
│   visual momentum) or deliberate Temporal Ellipsis.                          │
│ • Eliminate the single-room 100s trap. Give the camera air to breathe.       │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STEP 3: EMBED VISUAL SEMIOTICS (CÀI ĐẶT MẠCH NGẦM THỊ GIÁC & HÀNH ĐỘNG THUẦN)│
│ • Design 1 Signature Motif that transforms across 3 appearances.             │
│ • Embed at least 1 Pure Visual Action Sequence where physical blocking,      │
│   props, and camera movement tell the entire story with ZERO DIALOGUE.       │
│ • Plant Foreshadowing details that pay off the major twist organically.      │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### 10.4 The Dynamic Script Calibration Protocol (Adapting Dialogue & Safety Metaphors by Film Genre)

> **CORE LAW: NEVER FALL INTO MECHANICAL EXTREMES.**  
> A system that replaces "talking heads in one room" with "isolated characters speaking monologues into the void" has merely traded one amateur trap for another. 
> Real cinematic drama is the **living friction between human beings**. The Screenwriter and Director must calibrate the storytelling devices, dialogue distribution, and safety metaphors dynamically based on **Film Genre, Premise, and Dramatic DNA**.

#### 1. Dynamic Dialogue Distribution Matrix by Genre
Never enforce a static dialogue formula across all genres. Calibrate the vocal palette according to the story's emotional physiology:

| Film Genre & Dramatic DNA | Dialogue Density & Primary Vocal Mode | Interaction Dynamic (Call-and-Response) | Visual Action vs. Dialogue Ratio |
|---|---|---|---|
| **Domestic & Family Melodrama** | Moderate (10–14 words/scene). Modes: Model 1B (Rapid Fencing), Model 4 (Counterpoint V.O.), Model 0 (Silence). | **Adversarial Friction & Protective Lies**: One attacks/queries, the other deflects/lies to protect. Climax features tearful Anagnorisis exchange. | 50% Somatic Action / 50% Dialogue |
| **Psychological Thriller & Mystery** | Low-to-Moderate (8–12 words/scene). Modes: Model 7 (Interrupted), Model 5 (O.S. Intrusion), Model 6 (Whisper). | **Power Interrogation & Trapped Evasion**: Loaded one-sentence scalpels, long suffocating silences, sudden auditory shocks from outside the frame. | 70% Suspense Visuals / 30% Dialogue |
| **Sitcom & Light Social Comedy** | Snappy (14–24 words/shot; 5–10w volleys, hard cap ≤ 32w; punchline in last 2–3s). Modes: Model 1B (Rapid Volleys), Model 2 (Ensemble Overlap), Model 8 (Direct 4th Wall). | **Eccentric Ping-Pong & Mutual Misunderstanding**: Rapid rhythmic volleys, unexpected punchlines, characters talking over each other. | 30% Physical Comedy / 70% Dialogue |
| **Art-House & Healing Drama** | Sparse (0–8 words/scene). Modes: Model 0 (Pure Eloquence), Model 3 (Silent Absorber), Model 6 (Tender Whisper). | **Somatic Resonance & Reverence**: Extended silences, tactile caretaking (serving tea, wrapping a shawl), gentle shared breath. | 80% Pure Visuals / 20% Dialogue |
| **Workplace & High-Stakes Corporate** | Sharp & Compact (12–16 words/scene). Modes: Model 1 (Status Duel), Model 1B (Ultimatum). | **Hierarchical Leverage**: Dominant executive issues a mandate; subordinate counter-attacks with hidden contract evidence. | 40% Blocking & Props / 60% Dialogue |

#### 2. The Contextual Safety Metaphor Engine (Zero-Flag Guarantee)
AI video diffusion models strictly enforce automated bans on bodily harm, self-harm, medical trauma, weapons, and blood. Every premise must translate sensitive conflicts into **Safe Cinematic Proxies**:

| Sensitive Premise | Banned / Moderation Trigger Lexicon | Contextual Safe Cinematic Metaphor (100% Filter-Proof) |
|---|---|---|
| **Medical Emergency & Severe Illness** | `blood`, `bleeding`, `needle`, `IV drip puncture`, `bruise`, `dying`, `faint` | **Institutional / Clinical Artifacts**: White patient paper wristband with barcode (`vòng giấy viện phí`), stamped clinical discharge certificate, folded medical fee receipts, empty blister pack beside a warm ceramic cup, pale translucent skin with visible delicate veins. |
| **Debt Collection & Underground Coercion** | `beat up`, `punch`, `knife`, `stab`, `blood`, `kill`, `extort` | **Architectural & Legal Confinement**: Padlocked iron security chain on the door, folded promissory note with thumbprint seal, heavy silhouette blocking window daylight, shattered porcelain cup on floor tiles, slammed fist rattling table ceramics. |
| **Betrayal & Marital Infidelity** | `naked`, `sexual`, `affair`, `screaming curses` | **Sensory Evidence of Deception**: Unfamiliar floral perfume trace on a tailored jacket collar, forgotten embroidered silk handkerchief in a briefcase pocket, illuminated smartphone screen lighting up an empty nightstand with an unsent text. |
| **Generational Trauma & Filial Neglect** | `curse words`, `wishing death`, `abandon to die` | **Kinetic Refusal & Relocated Belongings**: Untouched covered dinner bowl going cold, packed vintage leather suitcase resting by the porch threshold, refusal to accept an envelope of money pushed across the table. |

#### 3. The 3-Point Pre-Flight Screenplay Vitality Gate
Before compiling a script into video prompts, the Screenwriter must audit:
1. **The Interpersonal Vitality Test**: Are characters actually sparring, reacting, and catching each other's emotional batons, or is a single character delivering isolated monologues? If 2+ characters are in conflict, enforce two-way dialogue fencing (Track B) or dynamic action-reaction blocking.
2. **The Contextual Filter Audit**: Does any line or visual description contain literal trigger words (blood, needles, violence)? If yes, translate immediately to an institutional prop or lighting metaphor.
3. **The Genre DNA Alignment**: Does the rhythm, word count, and silence distribution match the true soul of the film's genre, rather than a generic template?

---

### 10.5 The Two-Tier Prop Implementation Standard (Phân Tầng Đạo Cụ: Text-Described vs. Image-Anchored)

In cinematic generative AI production, **props must be strategically bifurcated based on their visual entropy, cultural ubiquity, and semantic complexity**. Forcing 4-view turnaround reference images for mundane objects is a catastrophic waste of compute, memory, and cognitive focus. Conversely, relying on text alone for idiosyncratic, high-concept artifacts triggers uncontrollable visual hallucinations across scenes. Numbering follows `workflow.md` §6.3: **Tier 1 = image-anchored hero props; Tier 2 = text-only everyday handheld items.** Furniture and fixtures are never props.

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE TWO-TIER PROP IMPLEMENTATION STANDARD                                 │
├────────────────────────────────────────┬───────────────────────────────────────────────────────────────┤
│ TIER 2: EVERYDAY HANDHELD ITEMS        │ TIER 1: SIGNATURE HERO / SOUL / WEAPON PROPS                  │
│ (Đạo cụ Đời thường & Vật dụng Sinh hoạt)│ (Đạo cụ Linh hồn, Vũ khí Đặc chế & Cổ vật Biểu tượng)         │
├────────────────────────────────────────┼───────────────────────────────────────────────────────────────┤
│ • Scope: Household, culinary, office,  │ • Scope: Custom weapons, ancestral talismans, intricate       │
│   and everyday items (rice bowl, tea   │   puzzle mechanisms, runic blades, glowing sci-fi cores,      │
│   cup, pen, envelope, key, wrench,     │   dynastic signets, idiosyncratic heirlooms with rare runes.  │
│   phone; never furniture or fixtures). │                                                               │
│ • Implementation: 100% PURE TEXT       │ • Implementation: MANDATORY 16:9 4-VIEW MODEL SHEET           │
│   PROMPTING (Mode A).                  │   (Mode B — Step 1C).                                         │
│ • Rationale: AI diffusion models       │ • Rationale: Text alone cannot maintain geometric consistency │
│   already possess deep semantic weights│   or ornamental precision; without an image reference,        │
│   for standard items; zero drift risk. │   diffusion models drift uncontrollably between scenes.       │
│ • Production Rule: BAN on generating   │ • Production Rule: Reference asset generated in Step 1C       │
│   16:9 Model Sheets or visual assets.  │   and strictly bound in prompts: `<<<Image X>>> (fully_preserved - ...)`.│
└────────────────────────────────────────┴───────────────────────────────────────────────────────────────┘
```

#### 1. Tier 2 (Everyday Handheld Items) — Mode A (Pure Text Specification)
- **Zero Pre-Production Visual Burden**: Never generate a 16:9 turnaround sheet or Midjourney/Flux image prompt for everyday domestic items (rice bowl, water glass, chopsticks, wrench, envelope, hospital bill). Furniture and fixtures (beds, cribs, folding hammocks, chairs) are never props; describe them in `[context]:`. AI generative models possess vast pre-trained weights for these objects.
- **In-Prompt Anchor Formula**:
  Integrated directly into `[context]:` (Vector 3 inventory) and `[subject]:` (initial hand/table state at `00:00`, e.g., `chipped white ceramic rice bowl steaming with hot jasmine rice resting on the worn mahogany table beside Elena's left wrist`) without a separate `<<<Image X>>>` sheet.
- **Mechanical Continuity Invariance**: The Single Instance Lock, Resting Surface Clearance, and Prop Mutability Lifecycle (Intact ➔ Kinetic Fracture ➔ Inert Fragments) apply identically to Tier 2 items via pure text cues.

#### 2. Tier 1 (Signature Hero / Soul / Weapon Props) — Mode B (Image-Anchored Specification)
- **Mandatory Pre-Production Visual Asset (Step 1C)**: At most 1–2 master hero props per series. Rendered as a standardized 16:9 Four-View Turnaround Model Sheet (Hero 3D perspective + 3 orthographic views: front, side profile, back) on a pure white `#FFFFFF` studio backdrop with zero human hands.
- **In-Prompt Anchor Formula**:
  Line inside `[prop]:`: `[Canonical Prop/Weapon Name] <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): [Exact 00:00 resting placement or character hand-grip state] — the only [Canonical Prop/Weapon Name] in frame.`
  *Example*: `Obsidian phoenix hairpin <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): Resting on the lacquered dressing table at 00:00 — the only obsidian phoenix hairpin in frame.`

---

### 10.6 The Cinematic 10s Integration Manifesto (Stitching Shots into a Living Film)

> **CORE LAW: A CINEMATIC FILM ASSEMBLED FROM 10S SHOTS MUST NEVER FEEL LIKE 10 DISJOINTED SKETCHES.**  
> When editing together discrete 10-second generations into a coherent 100s–120s master film, the illusion of cinematic continuity relies on four unbreakable authorial principles:

1. **Abolition of Symmetrical "Ping-Pong" Debate Chains**:
   - Trading balanced two-line volleys (A attacks, B replies) across 10 consecutive scenes is mechanical radio drama, not cinema.
   - Masterclass film directing uses **Asymmetrical Cinematic Geometry**:
     - *Shot N (The Accusation / Action)*: Dominant character delivers a devastating 10–14 word verdict or physical gesture.
     - *Shot N+1 (The Reaction Shot / Model 0 Silence)*: The camera cuts to the victim. ZERO words spoken. 10.0 seconds of suffocating silence, trembling throat muscles, moistening eyelids, or whitening knuckles gripping a doorway.
     - *Shot N+2 (The Tactical Deflection)*: A third character intervenes, or the subject changes the physical state of the room (slamming a window shut, turning on a faucet).
2. **Explicit Kinetic Baton Handoff in the Screenplay**:
   - The Stage 3 Screenwriter must explicitly script the **Physical Baton Transfer**:
     - *Scene N closing beat*: "Khang begins to turn toward the hallway door, his hand reaching for the knob..."
     - *Scene N+1 opening beat*: "Cut to reverse angle from the dark hallway: Khang's hand completes turning the knob, pushing the door open into the light..."
   - When cut on action in NLE software, the transition feels like one seamless, continuous multi-camera shoot.
3. **Auditory Suture (L-Cuts & Room Tone Consistency)**:
   - Dialogue should not stop abruptly at 00:10.0. The Screenwriter and Director script deliberate L-cuts: the final words of an elder's admonition reverberate into the opening seconds of the next shot over the daughter-in-law's bowed head.
   - The diegetic Foley contract (`Diegetic room acoustics: ...`) must maintain acoustic continuity across all shots sharing the same physical realm.
4. **Genre-True Filmic Aesthetics (Banning Generic Beauty Prompt Bloat)**:
   - Mindlessly injecting `"Modern K-Drama Premium Cinematography, high-key beauty illumination, soft pastel urban palette, romantic atmospheric glow"` into gritty domestic conflict or tragedy is amateur visual dissonance.
   - Direct the lighting and color palette to match the psychological reality of the scene:
     - *Grief & Postpartum Isolation*: Low-key naturalistic daylight, cool muted slate-grey shadows, warm domestic tungsten rim, tactile film grain, unvarnished realistic skin texture with visible fatigue.
     - *Historical Mystery / Courtroom*: Chiaroscuro single-source candle/lantern illumination, deep rich shadows, atmospheric incense smoke particles, polished timber sheen.
     - *Social Satire / Sitcom*: Crisp natural high-key balanced light, vibrant localized color accents, clean spatial separation.





# PILLAR 4: AI VIDEO PROMPT COMPILER & QUALITY ASSURANCE (SSOT)
# (ĐẠO TRÌNH BIÊN DỊCH PROMPT OMNI FLASH, 10S KINETIC UNIT & KIỂM ĐỊNH LINTER)

> 📚 **CATALOG NOTICE** — This Pillar is a catalog of tools, patterns, and examples. Timings, word budgets, shot counts, and combos are illustrative Craft Defaults unless listed as Hard Constraints in `workflow.md` §2.10. Choose among them through [`0-creative-doctrine.md`](file:///d:/Project/Sven/engine/references/0-creative-doctrine.md): intent first, tool second, reason always.

> **SINGLE SOURCE OF TRUTH (SSOT) FOR PROMPT COMPILATION & QUALITY CONTROL**  
> **Master Authority**: Level-2 Film Director (`.agents/skills/director/` & `.agents/DIRECTOR.md`)  
> **Direct Stakeholders**: Level-1 Executive Producer (`AGENT.md`), Level-2 Master Screenwriter (`.agents/skills/screenwriter/`)  
> **Consolidation Note**: This document fuses, streamlines, and replaces legacy references: `4-ai-video-prompt-compiler.md`, `4-ai-video-prompt-compiler.md`, and `4-ai-video-prompt-compiler.md`. All prompt syntax, Mode B Zero-Costume & Zero-Age laws, the 10s kinetic unit breath cycle, organic continuous motion & zero freeze holds, the 4 neural continuity bridges, Code Block 1 & 2 handover protocols, `tap-X.html` episode specifications, and the 6-Point Pre-Flight Linter reside here as the single source of truth with zero contradiction.

---

## 🏛️ TABLE OF MASTER CONTENTS

- **PART I: FOUNDATIONAL PROMPT ARCHITECTURE & STATELESS GENERATION**
  - § 0. The 4 Sovereign Anti-Stagnation Laws (Buzzword Purge, Action Verbs, Tactile Props, Editing Rhythm)
  - § 1. Stateless Prompt Architecture & One-Move Rule
  - § 2. Singularity Lock & Anti-Duplication Directives
  - § 3. The 6-Point Lighting Contract (Key, Direction, Natural Color Tone, Medium, Shadow, Transitions)
  - § 4. Silent Mode Prompt Syntax Engine (Visual Replacements for Dialogue)
- **PART II: MODE B ASSET ANCHORING & ZERO-COSTUME / ZERO-AGE LAWS**
  - § 1. The Mode B Initial Opening State Protocol at `[00:00]`
  - § 2. Strict Ban on Costume & Clothing Descriptions in Video Prompts
  - § 3. Strict Ban on Age Numbers in Video Prompts
  - § 4. 5-Point Opening Anchor Anatomy (Name, Staging/Posture, Somatic Tension, Gaze, Surface Textures)
- **PART III: THE 10-SECOND KINETIC UNIT & DYNAMIC TEMPORAL KINETICS**
  - § 1. The Dynamic Temporal Law & Flexible Timing Formula (Anti-Rigid Timestamp Mandate)
  - § 2. The 3-Phase Breath Cycle: Ignition, Collision, and Psychological Arrest
  - § 3. Second-by-Second Micro-Action Breakdown Anatomy (0.5s–1.0s Resolution)
  - § 4. Terminal Cadence & Organic Motion (STRICT ZERO FREEZE HOLDS; Script-Driven Pacing)
  - § 5. The 4 Emotional Landing Destinations of Phase 3 (A1, A2, Tier B, Tier C)
- **PART IV: THE 4 CONTINUITY NEURAL BRIDGES (MULTI-SHOT CONTINUITY)**
  - § 1. Spatial Vector & 180° Axis Lock
  - § 2. Kinetic Momentum Handoff (STRICT ZERO ACTION REPETITION)
  - § 3. Chekhov Prop State Machine & The Prop Bifurcation Law (Intact ➔ Kinetic Fracture ➔ Inert Fragment)
  - § 4. Cinematic Scale Progression & In-Line Cut Protocol
- **PART V: TWO-TIER PHYSICAL OUTPUT SPECIFICATION & HANDOVER LEDGER**
  - § 1. Code Block 1: Omni Flash Video Prompt in 100% English Natural Prose
  - § 2. Code Block 2: Physical Handover State Ledger at 00:10.0 (5 Physical Fields)
  - § 3. Standard Dual Prompt Templates: Track A (Single-Shot Continuous Take) & Track B (Multi-Shot Cut Sequence)
- **PART VI: MASTER PER-EPISODE PRODUCTION SPECIFICATION (`tap-X.html`)**
  - § 1. 100% Verbatim Roadmap Inheritance & Zero Narrative Drift
  - § 2. 1:1 Roadmap-to-Execution Dialogue Parity Standard
  - § 3. Lore-Bound Asset Naming Mandate
  - § 4. Absolute Pronoun Ban in Prompt Prose
  - § [10d]. Minor Protection Protocol (Under-18 Characters)
- **PART VII: THE CINEMATIC METAPHORICAL SAFETY TRANSLATION ENGINE**
  - § 1. Universal Safety Filter Immunity Contract (Kling, Runway, Sora, Midjourney)
  - § 2. Metaphorical Translation Lexicon: Violence, Trauma & Weaponry
  - § 3. Metaphorical Translation Lexicon: Sensuality & Vulnerability
- **PART VIII: THE CORE PRE-FLIGHT DIRECTORIAL LINTER (SUBSET OF DIRECTOR.md 13-POINT LINTER) & 12 COMMON ERRORS**
  - § 1. The Core Pre-Flight Directorial Linter Gate
  - § 2. The 12 Cross-Cutting Directorial Errors Audit Table
  - § 3. The 3-Layer Check System (Core, Important, Nice-to-Have)

---


## § MANDATORY MASTER PROMPT PREFIX LAW (LỆNH TIỀN TỐ PROMPT BẤT BIẾN)

> [!IMPORTANT]
> **THE MANDATORY MASTER PROMPT PREFIX LAW**:
> 100% of generative AI Video Prompts (Code Block 1) MUST begin with the invariant master cinematic quality modifier:
> Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design.
> - **Directorial Rationale**:
>   1. *Master-level cinematography and composition*: Sets golden-ratio framing prior, rule of thirds, deep focal separation, and cinematic camera aesthetics.
>   2. *fast-paced shot variation*: Forces generative diffusion models to support multi-shot variation dynamics across 10 seconds (Track B cuts and Track A dynamic moves) without latent degradation.
>   3. *atmospheric sound design*: Activates native diegetic Foley, room tone, and acoustic synthesis in multimodal video generation models (Sora, Omni, Kling Audio).

---

## § FOUNDATIONAL PRINCIPLES

**3 parties:** User ↔ Agent (Vietnamese, free internal labels) | Agent ↔ Omni Flash (specific images only)

**Omni Flash**: stateless — each Scene is an independent call, it **does NOT remember** previous Scenes, does not understand `[Final State]`, `Scene 2`, `as established`, or "continuing from".

**THE SINGLE TEST** (apply to every sentence before including in output):
> *"A person who knows nothing about the script, hasn't read the previous Scene, only reads this one sentence — can they accurately visualize the exact frame?"*

If **NO** (contains Scene/Shot numbers, "as established", "as seen before", negative sentences like "does not appear") → **rewrite** as observable physical detail.

**Content zones:**
| Zone | Audience | Labels & Multi-Modal Structure |
|---|---|---|
| Internal: `[Final State]`, Beat Breakdown, Checklist | Agent only | Free |
| Actual output: Code Block 1 (Omni Flash / Sora / Kling / Runway) | Machine Prompt | **Mandatory 3-Block Structure**: `[context]:`, `[subject]:`, `[PROP]:` separated by blank lines with full reference bindings |

---

## ⚡ § 0. THE 4 SOVEREIGN ANTI-STAGNATION LAWS (BỐN NGUYÊN TẮC CỐT LÕI CHỐNG ĐƠ & BỆNH ĐẸP ĐỀU)

> [!CRITICAL]
> **ANTI-MANNEQUIN & ANTI-AESTHETIC-TRAP MANDATE**:
> Video diffusion models (Sora, Kling, Runway Gen-3, Wan 2.1, Luma) naturally default to motionless hovering mannequins when fed static descriptive adjectives and unanchored subjects.
> **Every compiled prompt in Code Block 1 MUST pass the 4 Sovereign Anti-Stagnation Laws:**

### 1. Purge Hollow Beauty Buzzwords (Triệt Tiêu Từ Khóa Làm Đẹp Vô Nghĩa)
- 🚫 **BANNED BUZZWORDS**: `photorealistic`, `cinematic 8k`, `hyper-realistic`, `masterpiece`, `dramatic lighting`, `moody atmospheric`, `unreal engine 5`, `gorgeous depth of field`.
  - Stacking these words destroys prompt attention budgets and forces AI into a generic, blurry cosmetic filter.
- ✅ **PHYSICAL OPTICAL GROUNDING**: Replace buzzwords with **tangible optical physics**:
  - Exact key light trajectory: `low-angle amber late-afternoon sunlight cutting diagonally across the room`.
  - Atmospheric particulates: `floating dust motes illuminated in the light beam`, `rising steam from a hot teacup`.
  - Surface wear & texture: `peeling lime plaster wall`, `beads of cold sweat along the temple`, `worn varnished tabletop with scratches`.

### 2. Concrete Observable Verbs & Visible Facial Changes Over Passive Adjectives
- 🚫 **BANNED PASSIVE ADJECTIVES & BUNDLED MULTI-STEP VERBS**: `looks sad`, `is angry`, `feels betrayed`, or bundling multiple steps (`steps in with an overwhelming aura and claims the space`).
- ✅ **ONE ACTION = ONE CONCRETE OBSERVABLE VERB**:
  - Express action via 1 concrete visible verb (`sets the vintage tarnished brass truck keyring onto the walnut tabletop`, `walks to the foot of the walnut dining table and stops`) and emotion via 1 visible facial change (`smile hardens into a cold stare`).

### 3. Minimal Prop Interaction, Speech Motion-Budget Priority & Static Supporting States
- 🚫 **BANNED MOTION OVERLOAD & REDUNDANT PROP CLUTTER**: Never force all characters to move simultaneously, never stack complex gestures onto the speaking character, and never write auxiliary phrases like `"leaving the tabletop spot clear"`.
- ✅ **CLEAN SEQUENTIAL MOTION (`then`) & STATIC SUPPORTING ANCHORS**:
  - Limit each small prop to **1 interaction per clip** (setting down OR lifting) using **1 fixed short noun phrase**.
  - Chain actions sequentially with `then` (`≤ 2` moving bodies per phase), keep the speaker to at most **1 simple gesture**, and hold supporting characters in a **clean static state** (`monica_thornton sits still with eyes fixed on harold_thornton`).

### 4. Dynamic Editing Rhythm & Sequence Assembly Over Monolithic Takes (Dựng Phim Bằng Nhịp Cắt — Editing Rhythm)
- 🚫 **BANNED MONOLITHIC RUN-ON PROMPTS**: Never attempt to cram a multi-beat 20s–30s dramatic scene into a single unbroken prompt. AI models lose temporal coherence and freeze after 5–8 seconds without a cut.
- ✅ **MULTI-SHOT TIMELINE BREAKDOWN (Track B Sequence)**:
  - Any scene exceeding 10s MUST be partitioned into a dynamic editing sequence:
    * **Shot 1 (In Medias Res Opening Action, 4s–6s)**: Fast momentum, establishing spatial power.
    * **Cut to Shot 2 (Reverse Reaction & Somatic Shock, 6s–8s)**: Shift camera >30° across 180° line.
    * **Cut to Shot 3 (Tactile Prop Detail / ECU Cutaway, 3s–5s)**: Physical object bearing the dramatic subtext.
    * **Cut to Shot 4 (Resolving Climax / Power Shift, 6s–10s)**: Emotional landing or sharp cliffhanger cut.

---

## § VISUAL STYLE SYSTEM

**DEFAULT (system-wide): `Pixar 3D`** — Pixar · DreamWorks · Disney · Family
↳ Applied to all prompts unless user selects a different style at Step 1A.

**Propagation Rule — MANDATORY:**
`[visual style]` is set once at `1A` → inject into **every** downstream prompt:

| Prompt | Injection position |
|---|---|
| Character reference grid | End of prompt, before `Negative:` |
| Prop reference grid | End of prompt, before `Negative:` |
| Environment reference grid | End of prompt, before `Negative:` |
| Clip A & B (Quality block) | Last line in Quality block |

**Full style library (39 styles):** see `2-casting-worldbuilding-specification.md` and `workflow.md § 1A — VISUAL STYLE LIBRARY`



## § [0] DIRECTOR'S INTENTION LOCK — Run BEFORE Beat Breakdown, internal only

For **each Scene**, before writing the Shot breakdown, determine:

1. **ONE dramatic function**: What is this scene DOING for the story? (who just lost control / just gained it, where power shifts, what lies beneath)
2. **ONE directorial tone**: `cold-observational-from-distance` | `suffocating-close` | `chaotic-disoriented` | `still-waiting`
3. This tone governs camera / lighting / body-state / sound — **held throughout the entire Scene** (unless the Scene is TWIST — allowed to shift tone exactly once at the climax shot)
4. **If the Scene has dialogue**: Also determine — does this dialogue REVEAL or HIDE emotion? What is the character saying while their body betrays the opposite? (Subtext > Explicit)
5. **DO NOT output to Omni Flash** — internal filter only

**Quick test:** *"If I strip the technical labels, what does this Scene make the audience feel? Do all camera/lighting/dialogue choices pull in the same direction?"*

---

## § ONE-MOVE RULE (CAMERA & CHARACTER KINETICS)

1. **Camera Kinetics**: Each Shot carries **exactly ONE camera intention**: one movement, one speed, one relationship to the subject. Do not stack multiple camera movements in one short 2–3s Shot.
2. **Character Kinetics (Anti-Compounded Action Law)**: In any 3–4 second shot window, characters are strictly limited to **ONE primary kinetic momentum + ONE secondary biological reaction**.
   - *Primary kinetic move*: e.g., turning a bolt, reaching for a hand, setting down a cup, taking two steps forward.
   - *Secondary biological reaction*: e.g., sharp exhalation, locked jaw, widened eyes, temple pulse.
   - Compounding multiple independent tasks ("vừa làm A vừa làm B vừa làm C") is strictly forbidden to prevent AI limb morphing and phantom hands.

---

## § [3] CHARACTERS & PROPS

### Naming Convention (§3.0) — The Triad Entity Naming Standard (Proper Character Names Only — Zero `snake_case`)
- **Mandatory Proper Character Names (`Gate 3C`)**: All character identifiers in AI Video Prompts (Code Block 1) MUST use **fixed Proper Character Names** (`Bradley`, `Harold`, `Marcus`, `Elena`, `Kael`, `Dante`, `Martha`) across `[subject]:`, `Shot 1..N`, and speaker headers.
  - **STRICT BAN**: Legacy `snake_case` tokens (`my_duyen`, `minh_khang`, `ho_ten`) and generic nouns (`Woman`, `Man`, `the father`, `the chef`, `the hunter`) are strictly prohibited in Code Block 1.
- **The Triad Entity Architecture (Characters vs. Locations & Props)**:
  - **Characters (Fixed Proper Names)**: Written as clean proper names (`Bradley`, `Harold`, `Marcus`, `Elena`) to bind `<<<Image X>>>` reference sheets and enforce the singularity seal (`— the only [Proper_Name] in frame`).
  - **Locations (Evocative Natural English — Zero Underscores `_`)**: Written in descriptive natural English without underscores (`Professional restaurant open kitchen`, `Grand mansion mahogany dining room`, `Narrow brick alley and urban street`). Banned: Vietnamese pinyin (`phong_cu`, `nha_bep`) and programmer `snake_case` (`modern_townhouse_kitchen`).
  - **Props (Natural English Prose — Zero Underscores `_`)**: Written in natural English words without underscores (`Damascus steel chef knife`, `tarnished brass truck keyring`, `silver dragon-hilted longsword`, `matte black cast-iron skillet`).
- **Atomic Entity Lock, 4-Layer Gender & Hand/Limb Anatomy Lock, Skin/Makeup Sub-Lock & Singularity (`Single <<<Image X>>> Declaration & fully_preserved Law`)**:
  - Declaration in `[subject]:` (declared **ONLY ONCE** in `[subject]:`, never repeated in `Shot 1..N`; include explicit gender, limb/hand anatomy, and `makeup` in Line 1 for Female and omit `makeup` for Male, followed immediately by Line 2 `<Name>'s skin, hands (and makeup): fully_preserved - ...`):
    * *Male Example (`Bradley` — School M2 Grounded Dry Matte)*:
      `Bradley <<<Image 2>>> (fully_preserved - same male face, masculine body proportions, broad shoulders, well-defined masculine hands, hair color and outfit throughout; only his head, eyes, mouth, hands and expressions move.): A composed man seated at the side of the polished walnut dining table, right hand holding a crystal red wine glass, eyeline toward Harold — the only Bradley in frame.`
      `Bradley's skin and hands: fully_preserved - real unretouched dry matte masculine skin across his face, jawline, and strong well-defined masculine hands, with natural fine pores, crisp eyebrows and eyelashes, natural moisture in his eyes, and natural matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
    * *Female Example (`Elena` — School F1 Douyin Velvet-Porcelain)*:
      `Elena <<<Image 2>>> (fully_preserved - same female face, slender feminine body proportions, delicate wrists, long tapering fingers, hair color, makeup and outfit throughout; only her head, eyes, mouth, hands and expressions move.): A graceful woman seated in the dark velvet armchair beside the window, slender hands resting calmly on the armrest, eyeline toward Marcus — the only Elena in frame.`
      `Elena's skin, hands and makeup: fully_preserved - flawless porcelain velvet-matte skin across her face, neck, arms, and slender feminine hands, with delicate wrists, long tapering fingers, clean manicured nails, soft rosy blush on the cheeks and nose tip, crisp wispy eyelashes, natural watery eye reflection, and soft gradient rose lips; no rough masculine hands, no thick knuckles, no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
  - Action prose in `Shot 1..N` (always qualifying close-up hands as `slender feminine hands / long tapering fingers` for Female or `strong masculine hands` for Male): `In a locked static frame, seen past Harold's shoulder in the foreground, Bradley lets out a smug chuckle and raises his crystal red wine glass toward the head of the table with a polite, confident smile.`
  - Spoken dialogue vector (`Expressive Vocal-Behavior Tag + Native Interjection — Laws D2 & D3`): `Bradley (expressive male voice, chuckling smugly in a warm overly polite tone): "Hah... Rest easy, Dad. The company is safe."`


### [Subject] & Costume Directing Protocol — §3.2

**MODE A — No reference image (full description):**
- Continuous paragraph ~120 words per character A/B
- Order: Name → Age → Gender → Height → Head-body ratio → Skin → Build → Hair → Facial features → Baseline clothing & original props
- **Facial features**: observable bone structure and distinct expressions.

**MODE B — Reference image exists from Step 2 Pre-Production (`setting.html` — DEFAULT):**
- **CORE PRINCIPLE 1: NEVER WRITE SPECIFIC CLOTHING OR STATIC MAKEUP DESCRIPTIONS IN THE VIDEO PROMPT (`Gate 3E`)!**
  The 16:9 Character Reference Model Sheet (`<<<Image X>>>`) already defines 100% of the character's clothing, silhouette, fabrics, colors, baseline skin finish, and grooming. Re-describing specific garments (`jacket`, `suit`, `apron`, `dress`, `skirt`) or specific makeup colors in the video prompt forces the AI text encoder to compete with the image anchor, triggering clothing mutations and face morphing! *(Note: The generic preservation meta-tag `(fully_preserved - same face, hair color, makeup and outfit throughout; ...)` is the mandatory identity lock, never a specific garment/makeup description).*
- **CORE PRINCIPLE 2: NEVER WRITE CHARACTER AGE, SPECIFIC HAIR/BEARD COLOR, OR DRY MUSICAL REGISTER TERMS IN THE VIDEO PROMPT (`Gate 3A` & `Law D3`)!**
  Age, facial bone structure, skin maturity, and hair are 100% locked by `<<<Image X>>>`. Writing `"26-year-old"`, `"50-year-old"`, `"young blonde"`, `"silver-bearded"`, or dry musical register labels (`alto`, `baritone`, `tenor`, `soprano`) in the prompt causes diffusion text encoders to fight the visual reference or read dialogue like a flat robot. Express vocal behavior and emotion exclusively inside the **Expressive Vocal-Behavior Tag (`[Proper_Name] (expressive female/male voice, [vocal behavior] in a [tone]): "[Interjection]! ..."`)**.
- **CORE PRINCIPLE 3: SINGLE `<<<Image X>>>` DECLARATION & `fully_preserved` SLOT MATCHING (`Gates 3J, 3K, 3L`)**:
  Bind each location, character, and Tier-1 prop once in `[context]:`, `[subject]:`, and `[prop]:` using `<<<Image 1>>>`, `<<<Image 2>>>`, `<<<Image 3>>>`, `<<<Image 4>>>` followed immediately by `(fully_preserved - ...)`:
  - `[context]:`: `[Location Name] <<<Image 1>>> (fully_preserved - same architectural layout, furniture, props and lighting throughout), [time of day].`
  - `[subject]:`: `[Proper_Name] <<<Image 2>>> (fully_preserved - same female/male face, slender feminine body proportions, delicate wrists, long tapering fingers [Female] / masculine body proportions, broad shoulders, well-defined masculine hands [Male], hair color, makeup [Female only] and outfit throughout; only her/his head, eyes, mouth and expressions move.): A graceful woman / A composed man ...` + Line 2 `[Proper_Name]'s skin, hands (and makeup): fully_preserved - ...`.
  - `[prop]:`: `[Prop Name] <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): ...`
  **Strictly NEVER repeat `<<<Image X>>>` inside `Shot 1..N`!**
- **CORE PRINCIPLE 4: ZERO METRIC MEASUREMENTS (`cm`, `kg`, `metres`) OR LENS/HARDWARE NUMBERS (`35mm`, `24fps`, `Kelvin`) IN VIDEO PROMPTS (`Gate 3D`)!**
  Diffusion models do NOT have a ruler, thermometer, or physical lens rack. Writing `85cm`, `3200K`, `35mm`, `50mm`, `24fps`, or camera hardware names (`Phantom`, `Arri`) distorts framing and triggers film-border artifacts. Always use natural optical and physical prose (`matte skin and surface finish with zero plastic or oily sheen, subtle organic film grain, muted natural color tones, harsh overhead tungsten hood lamp light`).

---

### 🎭 THE DUAL-TRACK CHARACTER SPECIFICATION PROTOCOL (QUY CHUẨN ĐẶC TẢ NHÂN VẬT 2 TUYẾN)

To eliminate all contradictions between visual diffusion stability (Mode B) and multi-modal audio/lip-sync generation, character information is split into two non-overlapping operational tracks:

#### TRACK 1: THE SOVEREIGN `[subject]:` PROTOCOL & STATE-DELTA TIMELINE DIRECTING
To anchor character identity, eliminate AI duplicate clones, and prevent spatial amnesia, character specification follows a rigorous two-tier division:

1. **The `[subject]:` Declaration Block (The Two-Line Sovereign Subject Formula: Identity + Gender Skin/Makeup Sub-Lock & Initial Prop State Bifurcation Law)**:
   In Code Block 1, every participating character in `[subject]:` MUST be declared using **2 Lines** (Line 1: Sovereign Identity + Motion-Scope + $t=0.0\text{s}$ Spatial/Hand State; Line 2: Gender- & School-Calibrated Skin/Makeup Sub-Lock):
   $$\mathbf{[subject]:} = \mathbf{[Line\ 1:\ Proper\_Name\ +\ \lll Image\ X\ggg\ (fully\_preserved\ -\ ...)\ +\ Spatial/Hand/Eyeline\ +\ Singularity\ Seal]} + \mathbf{[Line\ 2:\ Proper\_Name's\ skin\ (and\ makeup):\ fully\_preserved\ -\ ...]}$$
   
   - **Syntax Contract (`Initial Prop State Bifurcation + 4-Layer Gender/Hand Anatomy & Skin/Makeup Sub-Lock`)**:
     * **Case A — Unheld Prop / Empty Hands at $t=0.0\text{s}$**:
       - *Line 1*: `[Proper_Name] <<<Image X>>> (fully_preserved - same female/male face, slender feminine body proportions, delicate wrists, long tapering fingers [Female] / masculine body proportions, broad shoulders, well-defined masculine hands [Male], hair color, makeup [Female only; omit makeup for Male] and outfit throughout; only her/his head, eyes, mouth and expressions move.): A graceful woman / A composed man [initial spatial anchor to in-scene architectural fixture], [initial physical posture], hands empty at sides [or (No objects should appear in the character's hands) in unarmed action/hunter scenes], [eyeline toward counterpart or landmark] — the only [Proper_Name] in frame.`
       - *Line 2 (Female `F1–F4` vs. Male `M1–M3`)*: `[Proper_Name]'s skin, hands and makeup: fully_preserved - [Female School F1/F2/F3/F4]; no rough masculine hands, no thick knuckles, no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.` *(or for Male: `[Proper_Name]'s skin and hands: fully_preserved - [Male School M1/M2/M3 with natural matte lips]; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`)*.
     * **Case B — Actively Held Prop/Weapon at $t=0.0\text{s}$**:
       - *Line 1*: `[Proper_Name] <<<Image X>>> (fully_preserved - same female/male face, slender feminine body proportions, delicate wrists, long tapering fingers [Female] / masculine body proportions, broad shoulders, well-defined masculine hands [Male], hair color, makeup [Female only; omit makeup for Male] and outfit throughout; only her/his head, eyes, mouth, hands and expressions move.): A graceful woman / A composed man [initial spatial anchor to in-scene architectural fixture], [initial physical posture], [explicit t=0.0s hand-grip on the declared prop/weapon, e.g., strong right hand gripping the Damascus steel chef knife poised above the garlic cloves while his left hand rests steady on the edge of the oak chopping board], [eyeline toward counterpart or landmark] — the only [Proper_Name] in frame.` (Synchronized 100% with `[prop]: <<<Image Y>>> (fully_preserved - same shape, material, surface finish and proportions throughout)` when holding a Tier-1 Prop/Weapon).
       - *Line 2*: `[Proper_Name]'s skin, hands (and makeup): fully_preserved - ...; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
   - **The 3 Directorial Functions of `[subject]:`**:
     * **Function 1: Multi-Modal Identity Lock**: Binds character Proper Name to the 16:9 Model Sheet (`<<<Image X>>>`).
     * **Function 2: Zero-Frame Spatial & Tactile Grounding**: Anchors character physically to an architectural fixture or furniture at Frame 0 (`00:00.0`), preventing floating bodies or deformed ghost hands.
     * **Function 3: The Mandatory Anti-Duplication Seal (`— the only [Proper_Name] in frame`)**: Explicitly blocks diffusion text encoders from generating twin/clone duplicates of the same character in one room.
   - **Subject-to-Scale Invariance & Emotional Solo vs. Physical Contact Phase Separation Law**:
     * *Character Declarations in `[subject]:`*: Declare every character who participates in the clip on separate lines. When 2 characters physically interact (handing an object, parrying, grabbing a wrist), anchor BOTH at the **exact same architectural landmark within arm's reach** with direct mutual eyelines. **STRICTLY FORBIDDEN** to split two physically interacting characters onto two distant landmarks across the room!
     * *Emotional Solo Shot (`CU`, `MCU`, `ECU`)*: Reserved strictly for 1 character's internal emotional acting or solo dialogue.
     * *Physical Contact / Collision Shot*: The shot scale MUST frame **both the initiator and the target** (`Medium two-shot`, `OTS`, `Tight close-up targeting Kael's forearm deflecting Vance's wrist`). **NEVER use a 1-person `CU / MCU` for an action that strikes or touches another character!**
     * *The 3-Tier Staging Hierarchy (Mandatory Order of Compilation)*:
       1. **Tier 1 (`[context]:`)**: Location name + `<<<Image 1>>> (fully_preserved - same architectural layout, furniture, props and lighting throughout), [time of day].` + 5-Vector 3D physical stage architecture, full interactive prop/tool inventory, real physical lighting source, shadow behavior, and atmospheric medium (zero redundant `[Time] · [Int/Ext] · [Location]` slugline above `Style:`).
       2. **Tier 2 (`[subject]:` & `[prop]:`)**: Zero-frame ($t=0.0\text{s}$) architectural anchors, proximity, eyelines, gender-calibrated `<Name>'s skin (and makeup): fully_preserved - ...` sub-line, and synchronized $t=0.0\text{s}$ prop/hand state.
       3. **Tier 3 (`Shot 1..N`)**: `Shot N (00:XX-00:YY) - [Shot Scale], [Angle/Move Targeting Subject], [Shot Speed]` followed by 1–2 natural sentences of State-Delta action (`State A ➔ State B`) and optional separated dialogue line.

2. **The State-Delta Directing Protocol in Storyboard Shots (`Shot 1..N` — Zero `[subject]:` Posture Repetition & Zero `[Shot Speed]` Repetition)**:
   While `[subject]:` locks the **static spatial grounding, posture, and hand state at 00:00.0** and the `Shot N` header locks `[Shot Scale], [Angle/Move], [Shot Speed]`, the action sentence below `Shot N` directs **ONLY the state delta ($\Delta$)** across time — **NEVER repeating static positions from `[subject]:` and NEVER repeating the `[Shot Speed]` phrase (`At blistering whip-fast speed...`) already declared in the `Shot N` header**:
   - **State-Transition Action (1–2 Short Natural Sentences, `12–30w`)**: E.g., `In a locked static frame, seen past Bradley's shoulder, Harold lets out a cold breath and locks his unblinking gaze straight into Bradley's eyes as Harold's strong right hand sets the tarnished brass truck keyring onto the leather-bound transfer contract and taps the brass tag twice.`
   - **Separated Spoken Line (`Expressive Vocal-Behavior Tag + Native Interjection — Laws D2 & D3`)**: Placed on its own line immediately below the action sentence:
     `Harold (expressive male voice, speaking with calm icy authority in a low unhurried tone): "Hmm... Then why sell Warehouse Four?"`

3. **The Kinetic Handshake Protocol (Giao Thức Bắt Tay Động Học giữa `[subject]:` và `Shot 1..N`)**:
   Để triệt tiêu hoàn toàn hiện tượng lệch pha (motion glitch, jump artifacts, hoặc subject teleportation) giữa điểm định vị tĩnh tại `00:00.0` và hành động diễn ra từ `00:00` đến `00:10.0` / `00:15.0`, AI Agent phải tuân thủ **4 Tiên Đề Bắt Tay Bất Biến**:
   - **Tiên đề 1: Bệ phóng Cơ sinh học (The Biomechanical Launchpad Law: T0 $\to$ T0+)**:
     * `[subject]:` là **Bệ phóng (Launchpad)** (tọa độ không gian và điểm tựa xúc giác lúc `00:00`).
     * Hành động đầu tiên trong `Shot 1` BẮT BUỘC phải là chuyển động cất cánh phát triển trực tiếp từ bệ phóng đó.
   - **Tiên đề 2: Luật Phân Tách Trách Nhiệm 1 Chiều (The One-Way Responsibility Separation & Zero Redundancy)**:
     * `[subject]:` độc quyền chịu trách nhiệm về: **Định danh `<<<Image X>>>` + Khóa da/makeup `fully_preserved` + Tọa độ neo tĩnh kiến trúc + Tư thế xúc giác xuất phát + Seal chống nhân bản**.
     * `Shot 1..N` độc quyền chịu trách nhiệm về: **Tiêu đề 3 tham số (`[Shot Scale], [Angle/Move Targeting Subject], [Shot Speed]`) + Động từ chuyển động (`State A ➔ State B`) + Thoại tách dòng**.
   - **Tiên đề 3: Luật Phân Tách Shot Cảm Xúc 1 Mình vs. Shot Va Chạm Vật Lý 2 Người**:
     * **Shot Cảm Xúc 1 Mình (`CU`, `MCU`)**: Chỉ chỉ đạo cơ thể, nhịp thở, ánh mắt và môi của nhân vật được đóng khung.
     * **Shot Va Chạm Vật Lý 2 Người**: Khung hình BẮT BUỘC phải chứa cả người tác động lẫn mục tiêu bị tác động (`Medium two-shot`, `OTS`, `Tight close-up`).
   - **Tiên đề 4: Cầu Nối Động Lượng & Hội Thoại Xuyên Cảnh (`TH1 / TH2 / TH3` & `Law D6` 4-Point Cross-Scene Handover Protocol)**:
     * Dưới `TH1` (cùng thời điểm & cùng bối cảnh), `[subject]:` tại `00:00.0` của Cảnh $N+1$ kế thừa **100% trạng thái tay, đạo cụ và biểu cảm khép môi tại `00:10.0 / 00:15.0` của Cảnh $N$** (ví dụ: nếu cuối Cảnh $N$ đã rút tờ hóa đơn giơ lên trước ngực thì `[subject]:` đầu Cảnh $N+1$ phải neo tay đang cầm tờ hóa đơn ở trước ngực — tuyệt đối không reset về tư thế đầu Cảnh $N$!).
     * **Luật Lật Trục 180° & Trao Gậy Từ Khóa Qua Biên Cảnh (`Law D6`)**: Nếu `Shot cuối` của Cảnh $N$ quay Nhân vật A nói câu chốt (`OTS targeting A`), thì `Shot 1` của Cảnh $N+1$ BẮT BUỘC lật trục 180° sang quay Nhân vật B (`Reverse OTS targeting B`) bật thán từ và lặp lại/phản박 đúng từ khóa ở cuối Cảnh $N$ (tránh Jump-Cut và tránh thoại rời rạc).
     * Dưới `TH2` (chuyển bối cảnh mới hoặc nhảy thời gian), Agent đọc trực tiếp thông số từ `output/<slug>/setting.html` mà không yêu cầu User gửi ảnh tham chiếu vào chat.
     * **Clean Terminal Keyframe Landing & `0.8s` Closed-Lip Buffer Mandate (`Law D5`)**: Cuối mọi clip (`00:08-00:10` ở `Mode 1`, hoặc `0.8s` cuối `00:09.2-00:10.0` / `00:14.0-00:15.0` ở `Mode 2`) nhân vật bắt buộc khép môi tự nhiên (`holding a silent closed-lip expression for the final 0.8 seconds`) ở tốc độ `natural real-time speed` để tạo cầu nối nhịp thở `~1.2s` sang Cảnh $N+1$ và trích xuất `Last Frame` không bị há miệng.

---

#### TRACK 2: THE 5 GOLDEN DIALOGUE LAWS (`LAW D1–D5`), EXPRESSIVE VOCAL-BEHAVIOR TAGS & SPOKEN SHOT ARCHITECTURE (`3.2s–4.5s`)
> **MANDATORY EXPRESSIVE VOCAL-BEHAVIOR TAG + NATIVE EXCLAMATION TRIGGER (`LAWS D2 & D3` — `Gates 3A & 3E`)**:
> Every spoken line in `Shot 1..N` is placed on its own line below the shot's action prose using **ONE single compact parenthetical immediately after `[Proper_Name]`** (strictly zero numeric ages like `24-year-old` and **strictly ZERO dry musical register terms like `alto`, `baritone`, `tenor`, `soprano`**, which cause flat robotic newsreader TTS):
> - **Canonical Spoken Line Formula (`Laws D2 & D3`)**:
>   `[Proper_Name] (expressive female/male voice, [active vocal behavior: scoffing playfully / gasping in panic and stammering / chuckling in disbelief / breath hitching with choked tears / whining pitifully / speaking with calm icy authority] in a [delivery tone]): "[Native Interjection Trigger: Huh?... / Whoa! Uh... / Hah!... / Hửm?... / Á! Ối trời...] [Spoken Line]"`
>   *Examples*:
>   - `Bradley (expressive male voice, chuckling smugly in a warm overly polite tone): "Hah... Rest easy, Dad. The company is safe."`
>   - `Harold (expressive male voice, speaking with calm icy authority in a low unhurried tone): "Hmm... Then why sell Warehouse Four?"`
>   - `Elena (expressive female voice, breath hitching with choked emotion in a soft aching whisper): "Oh god... I'm sorry."`
> - **Mandatory Camera, Timing & Tail-Buffer Rules for Spoken Shots (`0b-temporal-camera-grammar.md` §2 & §3)**:
>   1. **100% Static Camera for Continuous Dialogue (`Law D1`)**: Lock **`static camera`** (`static over-the-shoulder camera`, `static reverse over-the-shoulder camera`, `static eye-level camera`) across speaking shots (`In a locked static frame...`) so 100% of latent motion capacity goes to lip-sync and 4-Zone Facial Micro-Expressions (`brows, eyes/moisture, lips, jaw`).
>   2. **Shot Window & Speed (`Law D4`)**: Every shot containing spoken dialogue MUST be sized to **`3.2s–4.5s`** ($\mathbf{T_{shot}} = 0.4\text{s} + \frac{\text{Words}}{2.5} + 0.5\text{s}–0.8\text{s}$, max `3` spoken shots in `10s`, max `4` spoken shots in `15s`) with **`natural real-time speed`** and paired with **1 simple primary gesture (`One-Move Rule`)**.
>   3. **Two Valid Terminal Modes & Mandatory `0.5s–1.0s` Tail Buffer (`Law D5`)**: Either **(Mode 1)** finish all dialogue in `Shot 1..N-1` and keep the final `2.0s–3.0s` shot wordless (`0 spoken words`), OR **(Mode 2: 100%-Dialogue Ping-Pong)** keep `Shot 1..N-1` lines to `7–8 EN words` (`8–10 VN syllables`) inside `3.2s–3.5s` windows (`0.5s` buffer/shot to prevent cumulative delay) and give the final `Shot N` a wider window (`3.6s` in `10s`; `4.2s–4.5s` in `15s`) with a short `6–8 word/syllable` line so a **mandatory `0.5s–1.0s` (`~0.8s`) silent closed-lip tail buffer** (`holding a silent closed-lip expression for the final 0.8 seconds`) remains at the end of the clip!

**Directing Syntax for the 4 Master Cinematic Dialogue Modes in Storyboard Shots (`Shot 1..N`):**
1. **Standard On-Screen Spoken Shot (`Static Shot - Reverse Shot` — `3.2s–4.5s` Window)**:
   ```text
   Shot 1 (00:00-00:04) - Tight close-up, static over-the-shoulder camera from behind Marcus targeting Elena's face, natural real-time speed
   In a locked static frame, Elena tilts her chin up slightly toward Marcus, a bittersweet half-smile touching her lips as her eyes glisten with held-back emotion and her breath hitches softly.
   Elena (expressive female voice, breath hitching with bittersweet emotion in a soft aching tone): "Huh... You really thought I'd forget everything?"
   ```
2. **Wordless Terminal Reaction / Settle Shot (`Model 0 / Terminal Mode 1` — `0 Spoken Words`, Final `2.0s–3.0s` Shot)**:
   ```text
   Shot 3 (00:08-00:10) - Extreme close-up, static eye-level camera targeting Marcus's eyes and composed expression, natural real-time speed
   In a locked static frame, Marcus's lips close naturally as he lets out a slow, silent breath, the warm side light catching the quiet emotion in his eyes without a trace of shine on his forehead or nose.
   ```
3. **Off-Screen `L-Cut` Dialogue Over Visual Insert or Listener Reaction (`Model 5 O.S.`)**:
   ```text
   Shot 2 (00:04-00:08) - Medium close-up, static camera with focus locked on Bradley's face as he stares at the brass keyring, natural real-time speed
   In a locked static frame, Bradley's strong fingers freeze on the crystal glass stem as his eyes drop to the carved tag on the tarnished brass truck keyring.
   Harold (off-screen, expressive male voice, speaking with calm icy authority in a low unhurried tone): "Hmm... Then why sell Warehouse Four?"
   ```
4. **Internal Monologue / Voice-Over (`Model 4 V.O.` — Lips 100% Closed On Screen)**:
   ```text
   Shot 1 (00:00-00:04.5) - Close-up, static camera targeting Elena's eyes beside the rain-streaked glass, natural real-time speed
   In a locked static frame, Elena gazes silently through the rain-streaked glass with her lips softly closed, her slender fingers resting lightly against the cool windowpane.
   Elena (voice-over, expressive female voice, speaking in a hushed reflective tone): "Sigh... If I turn back now, nothing will remain."
   ```

### Master 16:9 Multi-Angle Character Model Sheet Prompt Architecture (Step 1B — Zero-Text Standard)

> **CINEMATIC STYLE & 16:9 RATIO INHERITANCE LAW (MANDATORY)**: Every character reference asset (Step 1B) MUST inherit 100% of the project's designated Master Cinematic Visual Style (`Style: [Visual Style Name]`) AND MUST be standardized strictly to **16:9 Landscape aspect ratio**.

#### 1. Mandatory 7 Character Physical Attributes Checklist (with Skin Complexion & Makeup / Grooming Architecture):
- **Height**: `[Specific cm — e.g. 170cm]`
- **Head-to-body ratio**: `[Specific ratio — e.g. 1:7.5 to 1:8 heads]`
- **Ethnicity, Skin Complexion & Subsurface Finish**: `[Specific ethnicity + undertone + surface finish — e.g. East Asian, luminous porcelain fair skin with a smooth satin-dewy finish, fine natural micro-pores, and subtle rosy undertones]`
- **Build**: `[Specific silhouette & frame — e.g. athletic, slim and toned, defined waistline, agile tactical curves]`
- **Hair**: `[Color, cut, texture, strands, styling — e.g. layered chin-length bob in dark espresso brown with subtle caramel highlights]`
- **Facial Features & Makeup / Grooming**: `[3D facial bone structure, eye sockets, iris color, nose bridge + Female Makeup Spec (brow arch, eyeliner/eyeshadow, blush/contour, lip color/finish) OR Male Grooming Spec (chiseled jaw contour, groomed sword/structured brows, clean-shaven or 1mm designer stubble, healthy natural muted-rose lip tone) — see Pillar 2 §1B 4 Female + 4 Male Archetypes; strictly ban generic "no heavy makeup, thin natural nude lips" boilerplate]`
- **Clothing & props**: `[Pristine baseline costume: cropped dark maroon leather moto jacket, form-fitting bodysuit, tactical shorts, thigh holsters, thigh-high boots]`

#### 2. Cấu trúc bố cục đa góc nhìn của câu lệnh tham chiếu 16:9 (The Sovereign Multi-Angle Composition — Zero-Text Standard):
1. **Tuyệt Đối Bãi Bỏ Chữ / Metadata Trên Ảnh (The Zero-Text Mandate)**:
   > [!IMPORTANT]
   > **QUY CHUẨN THỊ GIÁC THUẦN KHIẾT 100% (THE ZERO-TEXT MANDATE)**:
   > 1. Khung hình 16:9 dành trọn vẹn 100% diện tích cho dữ liệu hình ảnh nhân vật. **Nghiêm cấm chèn bất kỳ thẻ chữ, tiêu đề tên, metadata card hay nhãn thông số nào lên canvas** để loại trừ triệt để nguy cơ AI sinh chữ rác hoặc loạn font.
   > 2. Các thông số nhân vật (chiều cao, tính cách, đặc tính giải phẫu) được mô tả đầy đủ trong prompt văn bản gửi tới model AI, không in đè lên bề mặt hình ảnh.

2. **Khu Vực Trái & Giữa (55% Canvas Width - Three Compact Full-Body Turnaround Figures at Identical 1:1 Body Scale)**:
   > [!IMPORTANT]
   > **QUY CHUẨN THÂN HÌNH TOÀN THÂN: PHÂN KHU 4 HÌNH (55% / 45%), THẾ ĐỨNG TỰ NHIÊN & LUẬT ĐỒNG NHẤT TỶ LỆ 1:1 GIÓNG NGANG VAI - EO - GÓT GIÀY**:
   > 1. **KHAI BÁO RÕ 4 HÌNH CHIA 2 PHÂN KHU (55% TRÁI & GIỮA + 45% PHẢI)**: Khung hình 16:9 BẮT BUỘC mở đầu bằng khai báo rõ `containing 4 figures arranged from left to right across two zones` (55% bên trái cho 3 hình toàn thân thu gọn + 45% bên phải cho 1 chân dung cận ngực phóng to) để Hình thứ 4 không bao giờ bị đẩy tràn ra ngoài mép phải.
   > 2. **BÃI BỎ A-POSE ➔ CHUYỂN SANG DÁNG ĐỨNG THẢ LỎNG TỰ NHIÊN (RELAXED NATURAL STANCE LAW)**: Cả 3 thân hình toàn thân BẮT BUỘC ở tư thế **đứng thẳng tự nhiên, thả lỏng** (`natural, relaxed standing posture with arms resting loosely beside the torso, feet grounded on the exact same horizontal floor baseline`). Tuyệt đối không dùng tư thế A-pose giương tay cứng nhắc.
   > 3. **LUẬT SỐNG CÒN — ĐỒNG NHẤT TỶ LỆ CƠ THỂ 1:1 & GIÓNG NGANG VAI - EO - GÓT GIÀY (1:1 BODY SCALE & HORIZONTAL SHOULDER-WAIST-HEEL ALIGNMENT LAW)**:
   >    - Cả 3 hình toàn thân (Figure 1, Figure 2, Figure 3) BẮT BUỘC có **cùng một kích thước cơ thể 1:1 tuyệt đối (`exact same 1:1 anatomical body scale`)**. Đường ngang vai (`shoulder lines`), đường ngang ngực (`chest lines`), gấu áo (`garment hems`), vòng eo (`waistlines`) và gót giày chạm sàn (`shoe heels on the floor baseline`) của cả 3 hình BẮT BUỘC **nằm trên cùng các đường thẳng nằm ngang song song tuyệt đối**!
   >    - **Figure 1 (Far Left — Front Full-Body View, Clean Mannequin Neck Cut at Shared Shoulder Line)**: Toàn thân nhìn thẳng từ chân cổ xuống gót giày ở đúng tỷ lệ 1:1 và đúng độ cao ngang vai với Figure 3, kết thúc gọn tại cổ theo kiểu ma-nơ-canh với **khoảng nền studio trống rộng rãi phía trên cổ** (`clean mannequin-style neck termination at the collar with wide empty studio background space above the neck; strictly zero head, zero face, and never stretching the headless body to touch the top border`).
   >    - **Figure 2 (Center-Left — 90-Degree Lateral Side Profile Full-Body View, Clean Mannequin Neck Cut at Shared Shoulder Line)**: Toàn thân nhìn nghiêng 90° từ chân cổ xuống gót giày ở đúng tỷ lệ 1:1 và đúng độ cao ngang vai với Figure 3, kết thúc gọn tại cổ với **khoảng nền studio trống rộng rãi phía trên cổ** (`strictly zero head, zero face, and never stretching the headless body to touch the top border`).
   >    - **Figure 3 (Center — Rear Back Full-Body View WITH Head & Hair at Shared Shoulder Line)**: Toàn thân từ đỉnh đầu xuống gót giày **BẮT BUỘC CÓ ĐẦU VÀ TÓC PHÍA SAU**, đứng cùng tỷ lệ cơ thể 1:1 với vai, eo, gấu áo và gót giày gióng thẳng hàng ngang tuyệt đối với Figure 1 và Figure 2; chỉ duy nhất phần đầu và tóc phía sau nhô cao lên khoảng không phía trên đường ngang vai chung.
   > 4. **Lý do kỹ thuật cốt tử**:
   >    - Triệt tiêu hoàn toàn lỗi AI tự ý kéo giãn 2 hình không đầu chạm mép trên canvas làm lệch chiều cao cơ thể ~20% so với hình có đầu.
   >    - Mặt trước và mặt nghiêng 90° loại bỏ đầu để triệt tiêu lỗi dị tật khuôn mặt ở độ phân giải nhỏ và chống xung đột nhận diện đa mặt (*Multi-face identity conflict*), trong khi mặt sau CÓ ĐẦU khóa chặt form tóc sau gáy khi nhân vật quay lưng bước đi.

3. **Khu Vực Nửa Phải (45% Canvas Width - Figure 4: Prominent Direct Frontal Full-Head Portrait)**:
   - Chiếm trọn 45% chiều ngang bên phải khung hình: Ảnh chân dung điện ảnh từ ngực trở lên, đóng vai trò là mỏ neo khuôn mặt, làn da, trang điểm/grooming, mắt, tóc duy nhất.
   - **QUY CHUẨN CHÂN DUNG PHÓNG TO RÕ NÉT, CHÍNH DIỆN 100% & BẢO TOÀN TRỌN VẸN HỘP SỌ (PROMINENT DIRECT FRONTAL & FULL-CRANIAL LAW)**:
     > [!CRITICAL]
     > **ZOOM TO RÕ NÉT, CHÍNH DIỆN 100% & CẤM MỌI GÓC QUAY KHÁC**:
     > 1. **Zoom to rõ nét khuôn mặt trong phân khu 45% bên phải**: Chân dung ngực trở lên (chest-up portrait) được phóng to nổi bật (`prominent zoomed-in framing`) để thấy rõ từng chi tiết ngũ quan, mống mắt, làn da, trang điểm/grooming, sẹo/băng dán, khuyên tai và đường lọn tóc, nằm trọn 100% trong khung hình 16:9.
     > 2. **Đảm bảo full 100% head & face - Không cắt xén**: BẮT BUỘC giữ khoảng thở an toàn (*safe headroom breathing space*) phía trên đỉnh tóc. Toàn bộ hộp sọ và lọn tóc phải nằm trọn vẹn 100% trong khung hình, cách mép trên một khoảng thở rõ ràng, không chạm mép hay bị cắt cụt.
     > 3. **Chính diện 100% (Strictly Direct Frontal Eye-Level View)**: Khuôn mặt và ánh mắt nhìn thẳng trực diện vào tâm ống kính máy quay.
     > 4. **CẤM TUYỆT ĐỐI TẤT CẢ CÁC GÓC QUAY KHÁC**: CẤM góc nghiêng 3/4 (`strictly zero three-quarter angle`), CẤM góc nhìn nghiêng sườn (`strictly zero side profile`), CẤM góc máy chéo (`strictly zero oblique view`), CẤM góc ngửa hay góc chúi (`strictly zero low or high tilt angles`).
     > 5. **Cú pháp đóng khung cận ngực chính diện chuẩn mực**:
     >    `RIGHT ZONE (occupying the right 45% of the canvas width — Figure 4: One Large Frontal Chest-Up Portrait): Features a prominent, zoomed-in high-definition chest-up portrait filling the right 45% of the frame with impactful facial clarity while maintaining safe headroom margin above the hair crown, entire head, full cranium, and voluminous layered hairstyle 100% fully visible inside the canvas with clear breathing space below top border, in strictly direct frontal eye-level view facing camera directly`.
     > 6. **Chuỗi Negative Directives bắt buộc**:
     >    `strictly zero text, zero typography, zero labels, strictly zero height mismatch between the three full-body turnaround figures, strictly no enlarged or stretched headless bodies, headless necks must never touch the top canvas border, all three turnaround bodies must align horizontally at the shoulders, waist, and heels, all 4 figures 100% fully visible inside the 16:9 frame, strictly zero cropped head, strictly no cut-off hair, no truncated hair crown, no hair touching canvas borders, safe headroom margin above skull, strictly zero out-of-frame head, no chopped skull, portrait strictly frontal view only`.

#### 3. Luật tương phản đối ứng độ sáng (The Optical Value Contrast Inversion Law):
- **Trang phục TỐI MÀU (Đen, xanh đậm, than, da sẫm, nâu đỏ)** ➔ BẮT BUỘC dùng **Hậu cảnh MÀU SÁNG (Nền trắng tinh khiết `solid pure white studio background` hoặc xám sáng)** để thấy rõ từng đường may vai áo, nếp gấp cánh tay, triệt tiêu lỗi chìm màu (Black-on-Black).
- **Trang phục SÁNG MÀU (Trắng, kem, be, pastel, linen sáng)** ➔ BẮT BUỘC dùng **Hậu cảnh MÀU TỐI (Nền xám tối trung tính `solid dark neutral grey studio background` hoặc đen tuyền)** để nổi bật viền áo sáng, triệt tiêu lỗi lóa mép vải (White-on-White).
- **TUYỆT ĐỐI CẤM MỌI BỐI CẢNH NGOẠI CẢNH / NỘI THẤT** (không đường phố, không nhà cửa, không cây cối, không đồ đạc) để chống lem bối cảnh sang video.

#### 4. Golden Reference Templates (Mẫu chuẩn thực chiến):

> [!NOTE]
> **Single Source of Truth for Character Model Sheets**: To avoid desynchronization, all canonical 16:9 Character Model Sheet prompt templates reside exclusively in [`2-casting-worldbuilding-specification.md`](file:///d:/Project/Sven/engine/references/2-casting-worldbuilding-specification.md) §3:
> - **Mẫu 0 / 1A**: Human Adult Dark Wardrobe ➔ Solid Pure White Studio Backdrop (Three-angle headless turnaround + prominent frontal chest-up portrait).
> - **Mẫu 1B**: Human Adult Light Wardrobe ➔ Solid Dark Neutral Grey Studio Backdrop.
> - **Mẫu 0B**: Human Minor-Safe Benchmark (< 18 years old — Rin Morita; three full-length views with head + head-and-shoulders portrait; zero glamour/beauty, zero adult-labeling).
> - **Mẫu 3**: Non-Human Entity Benchmark (Robot, Creature, Beast — 3 full-body views with head intact + 1 upper torso & head medium shot).
> - **Mẫu 2**: 3D Animation & Unreal Engine PBR Model Sheet.

### [Prop Profile] & Physical Anchor Protocol — §3.4

> **CINEMATIC STYLE & 16:9 RATIO INHERITANCE LAW (MANDATORY)**: Every single pre-production reference asset (Character Model Sheets §1B, Prop Design Sheets §1C, Location Design Sheets §1D) MUST inherit 100% of the project's designated Master Cinematic Visual Style (`Style: [Visual Style Name]`) AND MUST be standardized strictly to **16:9 Landscape aspect ratio**. Mixing visual styles or aspect ratios across assets is strictly prohibited.

> 🌟 **THE TWO-TIER PROP IMPLEMENTATION STANDARD (DOCTRINE §10.5)**:
> - **Tier 1 (Signature Hero Props & Vehicles, max 1–2 per series)**: Custom weapons, ancestral talismans, heirloom relics, dynastic seals, signature vehicles, intricate puzzle boxes. **MANDATORY 16:9 4-VIEW MODEL SHEET (Mode B)**. Text alone cannot maintain geometric consistency; a visual reference is required to prevent drift.
> - **Tier 2 (Everyday Handheld Items)**: Rice bowls, tea cups, chopsticks, pens, paper envelopes, wrenches, keys, phones. **100% PURE TEXT PROMPTING (Mode A)**; generating 16:9 turnaround sheets for these items is STRICTLY FORBIDDEN. Furniture and fixtures (beds, cribs, tables, hammocks, curtains) are never props; they belong to `[context]:`.
> - *Numbering note*: Tier 1 = image-anchored hero props, Tier 2 = text-only everyday handheld items, matching `workflow.md` §6.3 and DIRECTOR.md §1c.

**MASTER 16:9 FOUR-VIEW PROP DESIGN SHEET PROMPT STRUCTURE (Step 1C — TIER 1 HERO PROPS ONLY):**
```
Style: [Movie Master Visual Style Name — e.g. Pixar & DreamWorks 3D Biblical Realism / Theatrical Live-Action Realism...].

Name: [Prop Name]. Category: [Weapon / Relic / Artifact / Complex Mechanism / Symbolic Heirloom]. Description: [A cross-shaped blade forged in aged silver with a cool metallic patina. The ornate handguard is intricately carved with ancient runes and vampire-hunting inscriptions. The handle is wrapped in dark leather and engraved with a vampire hunter emblem. Stored in a waist leather sheath. The blade emits a sharp, cold glint under porch night light. Upon piercing a vampire, it reduces the target to fine ash — a symbol of faith-driven ultimate judgment].

Format: Prop design sheet, 16:9 landscape. Strictly four views of the same prop only: one primary hero perspective view on the left, plus exactly three parallel orthographic views (front view, side profile view, back view) on the right. Exactly four views in total, zero extra panels or fifth view. Pure white background.

Rules: Strictly four views only. Do not include any fifth view, extra detail insets, text, letters, numbers, annotations, captions, material swatches, dimension lines, arrows, close-up detail panels, or exploded views. The prop must remain completely consistent across all four views. No environmental elements, no characters, no watermark.
```

---

#### PROMPT COMPILATION: MODE A VS. MODE B

**MODE A — TIER 2: EVERYDAY HANDHELD ITEMS (Pure Text — Zero Reference Image):**
- **Trigger**: Handheld domestic items, tools, ordinary paper, tableware. Furniture and fixtures are described in `[context]:`, never here.
- **Formula**:
  One line inside `[PROP]:`: `{material/texture} {prop noun}, {state/wear}, {resting place independent of character hands} — the only {prop noun} in frame`
- **Examples**:
  ```text
  chipped white ceramic rice bowl, steaming with hot jasmine rice, resting at the center of the wooden dining table — the only rice bowl in frame
  dented aluminum kettle, soot-blackened base, resting on the clay stove ledge with a thin thread of steam rising from the spout — the only kettle in frame
  folded kraft paper envelope with faded red ink hospital seal, resting on the wooden side table beside the doorway — the only envelope in frame
  ```

**MODE B — TIER 1: SIGNATURE HERO / SOUL / WEAPON PROPS (Image-Anchored — Reference Image Exists):**
- **Trigger**: Custom weapons, soul props, ancestral relics, complex mechanisms with unique runes/inscriptions.
- **Formula**:
  One line inside `[prop]:`: `[Canonical Prop/Weapon Name] <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): [Exact 00:00 resting placement or character hand-grip state] — the only [Canonical Prop/Weapon Name] in frame.`
- **Examples**:
  ```text
  Sharp triangular cobalt porcelain shard <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): Resting on the dusty limestone flagstones below the altar step at 00:00 — the only sharp triangular cobalt porcelain shard in frame.
  Forged terracotta tablet <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): Resting at the center of the timber ledger table at 00:00 — the only forged terracotta tablet in frame.
  Obsidian phoenix hairpin <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): Resting on the lacquered dressing table beside the bronze mirror at 00:00 — the only obsidian phoenix hairpin in frame.
  ```


### [Environment / Context] — §3.6

**MASTER LOCATION / ENVIRONMENT REFERENCE PROMPT STRUCTURE (Step 1D):**
```
Style: [Visual Style Name — e.g. Pixar\Disney 3D animation style / Theatrical film reference, live-action style, DaVinci grading...].

Name: [Location Name]. Description: [A broad, detailed multi-sensory environmental description: architectural structure, exterior/interior materials, structural frame, wall coverings, smoldering light sources casting deep shadows and colored illumination, crude totems or functional artifacts hanging from overhead, floor textures, weather elements, light bleed through entrances, and overall emotional atmosphere and ritualistic/cinematic tone].

Format: Location concept design sheet, 16:9 landscape, 4-panel grid layout. Exactly four panels showing the same location from four distinct camera angles: top-left wide establishing shot, top-right reverse angle (180° opposite wall and depth), bottom-left overhead bird's-eye view (spatial layout of fixtures), and bottom-right ground-level key-landmark view (the fixture where the main action happens). Uniform lighting across all four panels. Strictly four views only, zero extra sub-panels, no fifth angle. Focus entirely on full location views, with no written descriptions, detail labels, or floor plans.

Rules: Strictly four panels only (2x2 grid with exactly 4 camera angles). No characters or people - environment only. The location must look consistent and recognizable across all 4 panels, with the same buildings, props, and layout. Do not include any fifth panel, extra insets, text, letters, numbers, annotations, captions, dimension lines, arrows, labels, legends, zoning notes, or watermarks.
```

**MODE A — No reference image (full description in clip):**
- Full description of architecture, floor surface, colors, light source, atmosphere (~50-70 words).

**MODE B — Reference image exists from Step 1D (image-anchored — DEFAULT):**
- **CORE PRINCIPLE: 5-VECTOR ENVIRONMENTAL STAGING WITH `<<<Image 1>>> (fully_preserved - ...)`!**
  Bind the location to its uploaded reference slot with `<<<Image 1>>> (fully_preserved - same architectural layout, furniture, props and lighting throughout), [time of day].` followed by the 5-Vector inventory (enforced by Gate 3K). Legacy free-text tags (`[Environment Reference attached]`) remain banned.
- **MANDATORY FORMULA (CÔNG THỨC BẮT BUỘC)**:
  `[Location Name] <<<Image 1>>> (fully_preserved - same architectural layout, furniture, props and lighting throughout), [time of day]. [5-Vector Specification: architectural layout & full fixed furniture/prop inventory, physical key light source & direction (STRICTLY NO KELVIN NUMBERS), shadow behavior, and atmospheric mood].`
- **THE 4 ESSENTIAL ENVIRONMENT ELEMENTS**:
  1. **Location Name + Reference Anchor**: `[Location Name] <<<Image 1>>> (fully_preserved - same architectural layout, furniture, props and lighting throughout)` (slot must match the image uploaded in the AI tool UI).
  2. **Time of Day (Thời gian trong ngày)**: e.g., `deep night`, `early morning sunrise`, `high noon`, `late dusk`
  3. **Atmosphere / Mood (Bầu không khí ra sao)**: e.g., `tense and desolate atmosphere with howling wind`, `solemn judicial atmosphere under heavy silence`, `warm tranquil atmosphere with soft evening breeze`
  4. **Key Light & Natural Color Tone (NO KELVIN)**: Diffusion AI text encoders (T5, CLIP) confuse Kelvin numbers (e.g. `cool daylight`) with 8K resolution! ALWAYS describe the natural light source and sensory color: e.g., `key light from a single flickering warm golden oil lamp casting trembling shadows, intersected by an icy-blue moonlight beam` (BANNED: `amber warmth`, `cool daylight`, `cool daylight`).

```
[MODE B — Correct Environment Format: Clean, Atmospheric, Zero Architecture Bloat, Zero Kelvin Numbers]
The Weaver's Stone Cottage & Hearth Workshop, deep night, tense and desolate atmosphere with howling wind — key light from a single flickering warm golden oil lamp casting trembling shadows, intersected by an icy-blue pale moonlight beam.
```

### Anti-Duplication & Anti-Ghost Prop Law (Single Instance Lock) — §3.5
- **§3.5b** (Wide/Full shot): add `"the only [two] figures in the [empty] space"` when few people
- **§3.5e** (Prop): add `"the only [prop] in frame"`
- **Anti-Ghost Prop Law (Single Instance Lock)**:
  - Generative diffusion models (Kling, Runway, Sora) render all prompt tokens in a single semantic pass.
  - If a prop is introduced at Location A at 00:00 and then handled at Location B in Shot 2 without clearing Location A, the diffusion model renders **two simultaneous copies of the prop** (one on the ground, one in the hand).
  - **Single Interaction, Fixed Noun Phrase & Zero Surface-Clearance Clutter**: Each small prop has at most **1 interaction per clip** (either setting down OR lifting) using **1 fixed short noun phrase**, and **NEVER adds auxiliary phrases like `"leaving the floor tiles/tabletop clear"`**.
  - **Stationary Spatial Anchor Law**: Heavy fixtures (Pine Crib, Bed, Dining Table, Altar) are permanently locked to their designated room/space coordinates across all scenes. They CANNOT teleport between rooms across scenes.
  - **Scene-to-Scene Chain of Custody**: The resting state of every prop at `00:10.0` of Scene N is the exact physical opening state at `00:00.0` of Scene N+1.

> **Mode selection rule:** If Step 1 Pre-Production is complete and reference images have been created → **MANDATORY use Mode B** to avoid conflict between text description and image. If no image → use Mode A.

---

## § [4] CONTINUITY — FINAL STATE

**Final State Gate (§4):** Before writing `[Subject]`/`[Prop Profile]` of a new Scene, read `[Final State]` of the previous Scene — redraw inherited state using **specific physical detail**, no references.

**Handoff Frame (§4):** Next Shot opens EXACTLY at the moment the previous Shot ended — physical continuity.

**Sequential Action Rule (§4):** 1 Shot = 1 primary action per active character; when 2 characters act in turn within a phase, chain them sequentially with `"then"` / `"after that"` rather than running parallel simultaneous clauses.

**Intra-Scene State Table (§4b):** Track prop state changes across Shots within the same Scene.

---

## 🛡️ 4-STEP ENTITY LOCK METHOD

1. **Step 1: Single Anchor Dictionary**: Lock 1 unique identifier phrase for Setting (`mossy stone floor`), Camera angle (`Shot Medium-Close-up`), Prop (`Wooden Bowl`), and Sound. Use word-for-word 100% from start to end of prompt, FORBIDDEN to swap synonyms.
2. **Step 2: Behavioral Handoff Bridge**: Every coordinate/prop state transition must be described through 3 anchors: *Initial position ➔ Reach/bend/pick-up behavior ➔ New position*. FORBIDDEN: position teleportation artifact.
3. **Step 3: Single-Shot Continuum**: 1 Clip of 10s MUST hold an unbroken spatiotemporal setting and continuous camera trajectory from 00:00 to 00:10 (Beats 1, 2, 3 share the same scene continuum). FORBIDDEN: hard cuts or background regeneration within a Single-Shot clip, to eliminate Background Morphing Artifacts.
4. **Step 4: Entity State Audit**: Run entity test checking 3 points (unified setting keyword, direct prop pickup bridge, dialogue & acoustic sync) before outputting code block.

---

📌 **DYNAMIC DURATION & KINETIC ACTION PROTOCOL**
- **Total duration PER SCENE**: MUST be **EXACTLY 10 SECONDS (10s)** for 100% of Scenes (including Scene 1 Hook).
- **Elastic Beat Division**: AI Agent has FULL CREATIVE FREEDOM to divide the 10s Scene into **2 to 4 Beats** (Shots) flexibly following the dramatic rhythm of the story (e.g., `4s-3s-3s`, `3s-4s-3s`, `2s-3s-3s-2s`, or `5s-5s`), as long as **TOTAL = EXACTLY 10s**.

| Beat Length | Biomechanical Action Budget | Flexible Application Example |
|---|---|---|
| **Beat 2s** | 1 short explosive movement / startle causal reaction | Jerk away, slap the table, step back 1 step. |
| **Beat 3s – 4s** | 2–3 causally linked sequential movement phases | Walk 3 steps + lower foot + raise scroll up. |
| **Beat 5s (Kinetic Glide)** | Extended smooth sustained movement + continuous camera tracking | Camera pulls back a few paces in parallel with a 5-step stride. |

**Per-Second Action and Scene Closing Rules:**
- **1-Second Budget**: AI renders maximum 1 micro-movement or 1 acceleration increment. FORBIDDEN to cram 2 independent large actions into 1 second.
- **Terminal Deceleration Hold**: The final Beat of any Scene (whether ending at 07-10s or 08-10s) **MANDATORY LAST 0.5s [09.5s - 10s]** decelerates smoothly into a stable resting frame, maintaining continuous biological micro-motion (breathing, ambient drift), strictly zero frozen frames (only static or smooth push-in — **FORBIDDEN** crane/orbit/arc jerks).
- **Total duration of all Beats/Shots in Scene = EXACTLY 10s COMPLETE (§12.9)**.


---

## § [6] NAMED OBJECT ANCHORING

- **§6a**: Every Shot line must have `on {Specific Name}` — NOT `on him/her/it`
- **§6b (ABSOLUTE)**: All `[Global Shot]` and every Shot in Code Block 1 **MUST NOT have** `he/she/it/his/her/its/they/their/them` — ALWAYS repeat the proper name, even if it was mentioned in the previous sentence

---

## § [7] CONCRETE VISUAL RULE

Every sentence in actual output must be **observable physical detail**:
- NOT: "feels afraid", "tense atmosphere", "a scene about power"
- CORRECT: "neck vein rising, pupils contracting, lips pressing not quite closed"
- CORRECT: "Lok's jaw tightens, Lok's right fist curling slowly at Lok's side"

---

## § [1.D] FILMSTOCK — Safe output keywords (no brand names)

| Style (internal) | Safe OUTPUT keywords |
|---|---|
| Warm amber, night/interior | `warm tungsten-balanced amber glow, deep rich shadow blacks, dramatic low-light contrast, subtle fine grain` |
| Bright, daylight | `natural daylight-balanced tones, true-to-life skin rendering, high dynamic range, fine grain` |
| Dreamy, East Asian | `low-contrast dreamy tone, muted desaturated palette, soft nostalgic haze, gentle melancholic mood` |
| Hyper-vivid, fairytale | `hyper-saturated vivid color palette, fairy-tale intensity, rich glossy tone` |
| Stark black-and-white | `high-contrast black-and-white, gritty visible grain, stark noir shadow texture` |

---

## § [1.E] TIME OF DAY — Mandatory Time Declaration Table for Setting

> **Mandatory**: Every Scene must declare the time of day using the standard phrases below — embedded directly in the setting description of Code Block 1, BEFORE the light source information.

| Time | Standard declaration phrase | Dominant light color | Natural light source |
|---|---|---|---|
| **Early morning** (5–7h) | `early morning, pre-sunrise blue hour` | Cool blue-grey, first amber on horizon | Diffused sky glow, no direct sun |
| **Dawn** (6–8h) | `dawn golden hour, low sun just above horizon` | Warm golden-orange glow, long dramatic shadows | Low-angle raking sunlight from east |
| **Morning** (8–11h) | `mid-morning, clear daylight` | Crisp natural warm white daylight | Overhead sunlight at 30–45° angle |
| **Noon** (11h–13h) | `midday harsh sunlight, overhead sun` | Harsh glaring white light, minimal sharp shadows | Vertical overhead sun, strong shadows beneath |
| **Afternoon** (13–16h) | `afternoon light, soft directional sun` | Soft warm afternoon sunlight, long fill shadows | Angled sunlight from south-west |
| **Golden hour** (16–18h) | `golden hour, low warm sun before sunset` | Deep glowing amber-gold light, long raking shadows | Low-angle side/back light from west |
| **Dusk** (18–19h) | `sunset, sun at horizon, warm dusk glow` | Fiery orange-red twilight glow, silhouette potential | Sun at or below horizon, skyline glow |
| **Blue hour** (19–20h) | `blue hour dusk, post-sunset twilight` | Deep blue-purple sky, warm artificial light contrast | No direct sun, ambient sky + practical lights |
| **Night** (20–23h) | `nighttime, artificial light only` | Warm glowing tungsten interior / cool silvery moonblue exterior | Practical lamps, candles, streetlights |
| **Late night** (23h–3h) | `late night, deep darkness` | Near-black with isolated warm pools of light | Candle / single lamp / moonlight only |

**How to embed in Code Block 1:**

```
Master bedroom interior, nighttime — bedside table lamp (practical, on the nightstand beside the bed) casts...
              ↑ time declared immediately after setting name, before the em dash —
```

**Full example for each time of day:**

```
Bamboo forest path exterior, dawn golden hour, low sun just above the eastern ridge —
open sky casting warm amber raking light from east-right at 10° angle...

Stone courtyard interior, midday harsh sunlight, overhead sun —
vertical sunlight entering through open roof, hard brilliant white light, deep shadow pools directly beneath pillars...

Village road exterior, golden hour, low warm sun before sunset —
warm rich amber sidelight raking low from the western fields at 15° angle, long stretched shadows reaching east across the road...

Bedroom interior, nighttime, artificial light only —
bedside table lamp (practical, on the nightstand at bed height) casts warm soft amber pool across the bed...
```

---



## § [1.F] BODY-STATE COMPATIBILITY CHECK

Before finalizing `[Subject]`, check:
- **Hands**: if character holds/handles a prop in any Shot → DO NOT lock both hands in a base pose (arms crossed, hands in pockets...) → use neutral upper-body description
- **Mouth**: do not stack 2 activities (chewing + talking, drinking + talking)
- **Legs**: base pose must not conflict with leg action in any Shot
- **Head/eyes**: do not describe 2 gaze directions simultaneously without a transition
- Always explicitly state **LEFT HAND or RIGHT HAND** when holding/handling a prop (e.g.: `held in Dax's right hand with Dax's right thumb pressed along the upper edge`). If prop is not being held, MANDATORY state `resting on the floor beside Vin's right foot — ZERO hand contact — the only [prop] in frame`.

### 📌 PHASE LINE STRUCTURE & PURE CINEMATIC ACTION PROSE

> [!IMPORTANT]
> **Syntax and timing SSOT**: [`0b-temporal-camera-grammar.md`](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md) §8 (canonical syntax) and §2–§7 (speech rate, lip-sync windows, action capacity, camera-move durations, shots per clip, clip density). The former `△ … | … |` beat header and the fixed Templates 1A / 1B / 2 are retired.

1. **One phase line = one time bracket + one short camera clause + prose**:
   `[00:00–00:03.5] Medium shot framing [name], slight low angle, shallow depth of field holding sharp optical focus on [name], static camera — [one primary action + one reaction, observable physics].`
   Track B phases after the first open with `Cut to …`. The track itself is declared once, in the style line of the prefix (`Track A — one continuous take, zero cuts` or `Track B — multi-shot sequence cut on the 180-degree axis`).
2. **Describe the observable physical action directly.** No filler connectors such as `Driven by the stillness...`, `As Dax halts...`, `Continuing the reach...`.
3. **Split points come from the beats** (Doctrine §2; grammar §3–§6), never from a fixed template. Phases run contiguously from 00:00 to the clip end, 10 s by default, 15 s or 30 s when requested (Gate 3M).
4. **Pure visual optics only**: never write lens millimeters, f-stops, fps, camera brands, Kelvin, or frame coordinates (Gates 3D / 3H). Characters are anchored to architecture, never to `frame-left` / `screen-right`.
5. **The Optical Camera Clause Law (Banning Dangling "Focus on [name]")**: All subject framing, optical focal depth, and depth of field (shallow DoF, bokeh, rack focus) MUST be integrated into the camera clause before the em-dash `—`. NEVER tack an isolated `Focus on [name].` sentence to the tail of action prose.

* **✅ CORRECT (10 s, Track B, English dialogue):**
```text
[00:00–00:04.0] Medium two-shot framing Dax and Vin, slight low angle, slow push-in, deep depth of field holding sharp optical focus on Dax — Dax thrusts the debt scroll across the anvil, then Dax speaks with a cold smirk as Vin stands still watching Dax.
Dax snaps : “ Ten years of hiding ends today. ”（Voice of a 45-year-old man from the northern highlands, low and arrogant, precise lip-sync, cold forge light on the cheekbone, savoring the threat）

[00:04.0–00:07.8] Cut to a medium close-up framing Vin at eye level, shallow depth of field holding razor-sharp focus on Vin's face with background softly falling into bokeh, static camera — Vin brings the blackened hammer down onto the anvil, sparks scattering; Dax recoils half a step.
Vin replies : “ Your armor came from this anvil. ”（Voice of a 50-year-old man from the northern highlands, deep and unhurried, precise lip-sync, ember glow along the jaw, a quiet reminder of who holds the power）

[00:07.8–00:10.0] Cut to a close-up framing Dax along 180-degree axis, eye level, static camera — the smirk drains from Dax's face and the throat tightens in a hard swallow; lips stay closed, breathing slows, embers drift past.
```
Timing check (grammar §2–§3): each line is 6 words ≈ 2.7–3.0 s inside a ≥ 3.8 s phase (starts ≥ 0.3 s in, ends ≥ 0.8 s before the cut). Speech ≈ 5.5 s of 10 s.

* **❌ WRONG (legacy, retired):**
  `△ [00:00–00:04.0] Shot Medium Two-Shot | Shallow depth of field | Slow push-in:` — symbol, pipes, and a metadata header instead of prose.
  `Dax at frame-right …` — frame coordinates instead of architectural anchors.
  `Vin slams his hammer …` — pronoun in visual prose (Gate 3C).
  Overlapping brackets such as `[00:04.5–00:10.0]` followed by `[00:06.0–00:10.0]` (Gate 3M).
  `Driven by the stillness...` / `As Dax halts...` — stiff connectors that haze the prompt.

---

## 🏛️ § 1. THE DYNAMIC TEMPORAL LAW & 3-PHASE BREATH CYCLE

> ⏱️ **NUMBERS SUPERSEDED** — The breath-cycle philosophy below stays valid. Every number in this section (the 2.5 wps formula, phase ranges, terminal minimums) is superseded by [`0b-temporal-camera-grammar.md`](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md) §2–§4. A terminal settle of 1.0–2.5 s suits scenes that end on a held emotion; a scene may also end on momentum (Doctrine).

In masterclass cinema, a 10-second scene is **A SINGLE KINETIC AND EMOTIONAL BREATH (Một Nhịp Thở Động Lực & Cảm Xúc Khép Kín)**.

> [!IMPORTANT]
> **THE ANTI-RIGID TIMESTAMP MANDATE (ĐỊNH LUẬT THỜI GIAN ĐỘNG HỌC)**:
> - **STRICTLY PROHIBITED**: Hardcoding rigid, mechanical timestamps like `[00:00–04.0s]`, `[04.5–10.0s]`, `[Terminal Beat]` across all prompts!
> - The duration of each shot is a **dynamic physical variable** calculated mathematically from:
>   $$\mathbf{T_{shot}} = \mathbf{T_{lead\text{-}in}} + \left(\frac{\text{Spoken Word Count}}{2.5\text{ wps}}\right) + \mathbf{T_{followthrough}}$$
>   * $\mathbf{T_{lead\text{-}in}}$ (0.5s–1.2s): Time for physiological preparation (turning head, shifting weight, drawing breath).
>   * $\mathbf{T_{dialogue}}$: Measured at standard Hollywood natural speaking cadence ($\approx 2.5 \text{ words/sec}$).
>   * $\mathbf{T_{followthrough}}$ (0.8s–1.5s): Physical recoil, reaction absorption, and kinetic momentum handoff.

```
       PHASE 1: TENSION IGNITION               PHASE 2: CLIMAX COLLISION             PHASE 3: PSYCHOLOGICAL ARREST (EXHALE)
     [00:00 ────────► 00:XX.Xs]              [00:XX.X ────────► 00:YY.Ys]                 [00:YY.Y ────────► 10.0s]
 ┌──────────────────────────────────┐    ┌──────────────────────────────────┐        ┌──────────────────────────────────┐
 │ • Potential kinetic energy builds│    │ • THE POINT OF NO RETURN         │        │ • THE EMOTIONAL STRIKE LANDS     │
 │ • 180° spatial & gaze vector lock│    │ • The verbal or physical blow    │        │ • Emotional resonance & settle   │
 │ • Breath cadence: INHALE         │    │ • Breath cadence: HOLD & DISCHARGE        │ • Living Organic Settle (0.5s)   │
 └──────────────────────────────────┘    └──────────────────────────────────┘        └──────────────────────────────────┘
```

### 1. Phase 1 (`00:00` to `00:XX.Xs`): Tension Ignition (Tụ Lực & Nén Áp Suất Tâm Lý — Inhale)
- **Directorial Intent**: Spatial tension is established. Two human souls or opposing wills are locked in place.
- **Dynamic Duration**: Flexible range (typically `2.0s` to `4.5s`). If dialogue starts immediately, Phase 1 is short (`1.5s–2.5s`). If establishing deep atmospheric tension or tactile preparation, it extends to `4.0s–4.5s`.
- **Micro-Biomechanics**: Potential energy builds internally. Chest expands with drawn breath, fingers tighten imperceptibly, eyes narrow into unblinking trajectory, swallow catches in the throat.
- **The Mindset**: *Loading the emotional spring.*

### 2. Phase 2 (`00:XX.X` to `00:YY.Ys`): Climax Collision (Bùng Nổ / Nhát Dao Cảm Xúc — Hold & Discharge)
- **Directorial Intent**: The verbal accusation, painful truth, decisive strike, or sacrificial act crosses the **Point of No Return**.
- **Dynamic Duration**: Flexible range (typically `3.5s` to `5.5s`), calibrated to the exact word count of the spoken line:
  - *Short sharp barb (4–6 words)*: $\approx 2.0\text{s} - 2.5\text{s}$.
  - *Full dramatic counter-strike (8–12 words)*: $\approx 3.5\text{s} - 4.8\text{s}$.
- **Dynamics**: Peak intensity. The words cut deeper than steel; the physical strike makes impact; the secret is torn open. Momentum is at maximum velocity.
- **The Mindset**: *The irreversible blow is struck.*

### 3. Phase 3 (`00:YY.Y` to `00:10.0s`): Psychological Arrest & Resonance (Dư Chấn Cảm Xúc & Đóng Băng — Exhale)
- **Directorial Intent**: **WHERE DOES THE BLOW LAND IN THE HUMAN SOUL?**
  This terminal buffer (minimum `1.0s` to `2.5s`, typically landing between a natural clearance point before 00:10.0) is the most sacred moment in cinema: **spoken dialogue ceases completely**, lips press firmly closed, noise recedes into diegetic room tone, and the camera scrutinizes raw, unfiltered human vulnerability.
- **The Living Organic Settle Gate (Mandatory Terminal Buffer)**:
  Macroscopic camera movement decelerates smoothly (0.5s smooth deceleration) into a **stable resting frame**. The character and environment maintain **living biological and atmospheric micro-motion** (deep chest respiration, vapor drifting, subtle eye moisture, wind-drifted dust or embers), strictly prohibiting artificial frozen frames or dead static holds.
- **The Mindset**: *The emotional shockwave penetrates to the bone. Total, suffocating stillness.*

---

## 🔬 § 1.1. SECOND-BY-SECOND MICRO-ACTION BREAKDOWN ANATOMY

To eliminate stiff, generic character animations, every shot within the 10-second timeline must be authored with **second-by-second observable biological biomechanics (0.5s–1.0s resolution)**:

1. **Gaze & Saccadic Micro-Movements (0.0s–0.5s increments)**:
   - Pupils contracting under lantern light; eyelids fluttering in suppressed tears; gaze darting from weapon to opponent's eyes.
2. **Neurological Somatic Tension (0.5s–1.0s increments)**:
   - Masseter jaw muscles bunching under the cheekbone; Adam's apple bobbing in a strained swallow; tendons in the neck tightening into visible relief.
3. **Tactile & Mechanical Propulsion (1.0s increments)**:
   - Weight shifting from back foot to ball of front foot; fingernails blanching white against wood; fingers curling around a prop hilt.
4. **Respiration Cadence Match**:
   - Chest expanding on inhale during lead-in; ribcage heaving during spoken line; slow trembling exhale during terminal settle.

---

## ⚖️ § 1.2. THE UNIFIED MULTI-SHOT STORYBOARD SHOT STANDARD & TEMPORAL-PHYSICS BUDGET LAW (NGUYÊN TẮC SỐ S)

> ⏱️ **SYNTAX & BUDGET SSOT** — The canonical shot structure and 5-Tier `[Shot Speed]` taxonomy are governed by [`0b-temporal-camera-grammar.md`](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md) §4 & §8.

> [!IMPORTANT]
> **THE UNIFIED MULTI-SHOT STORYBOARD SPECIFICATION (QUY CHUẨN SHOT 3 TẦNG — ZERO REDUNDANCY)**:
> In generative video prompts (Code Block 1), every shot (`Shot 1..N`) is structured into **3 Clean Layers**:
> 1. **Layer 1 (`3-Parameter Shot Header`)**: `Shot N (00:XX-00:YY) - [Shot Scale], [Camera Angle & Movement Targeting Subject], [Shot Speed]` *(Omit `Interior,` / `Exterior,` unless the clip physically crosses between spaces; lock `[Shot Speed]` to one of the 5 Canonical Speed Tiers: `natural real-time speed`, `snappy real-time speed` / `crisp real-time speed`, `explosive real-time speed`, `blistering whip-fast speed`, or `ultra-slow-motion suspension`)*.
> 2. **Layer 2 (`State-Delta Action Prose`)**: 1–2 short natural sentences (`12–30w`) describing 1 clear state transition (`State A ➔ State B`) without repeating `[subject]:`'s static posture and without repeating `[Shot Speed]` at the start of the sentence.
> 3. **Layer 3 (`Separated Spoken Line — Only on Spoken Shots`)**: `[Proper_Name] (expressive female/male voice, [active vocal behavior] in a [delivery tone]): "[Native Interjection]! [Spoken Line]"` (`Strictly 0 spoken words` in `1.5s–2.5s` rapid cuts and slow-motion shots; final `Shot N` obeys `Law D5`: either `0 spoken words` in `Mode 1` OR a short `6–8w` line with a mandatory `0.5s–1.0s` [`~0.8s`] silent closed-lip tail buffer in `Mode 2`).

### The Temporal-Physics Budget Matrix (Nguyên Tắc Ngân Sách Giây & Động Lực Học Vật Lý)
Diffusion text encoders (T5, CLIP) and latent physical transformers (Sora, Kling, Runway, Hailuo, Seedance) generate unnatural morphing, phantom limbs, or frozen mannequins when the physical action exceeds the temporal capacity of the shot. Every second must be calibrated against real-world human biomechanics:

| Temporal Duration & `[Shot Speed]` | Physical Action Capacity (Hành Động Vật Lý) | Observable Biomechanical Emotion (Cơ Sinh Học) | Spoken Lip-Sync Budget (Thoại Khẩu Hình) |
| :--- | :--- | :--- | :--- |
| **`1.5s – 2.0s` Rapid Cut** *(`blistering whip-fast speed` / `snappy real-time speed` / `explosive real-time speed`)* | **1 Single Micro-Strike Sentence (`12–22w`)**: Blade mincing, pepper grinding, gas knob snap, forearm parry, pommel strike, or skillet toss. Compounding multiple moves is forbidden. | Razor-sharp ocular focus, wrist snap, or impact recoil. | **Strictly `0 spoken words`** (100% kinetic speed & percussive Foley). |
| **`2.0s – 3.5s` Visual / Slow-Mo Insert** *(`ultra-slow-motion suspension` / `explosive real-time speed`)* | **1 Single Visual Peak or Tactile Clue Insert (`15–26w`)**: Mid-air flambé fire ribbons and floating droplets, rune circle ignition, or slicing steak in one stroke. | Unblinking eyes reflecting flame or sudden rigid halt. | **Strictly `0 spoken words`** (never speak during slow-motion or VFX peaks). |
| **`3.5s – 4.5s` Spoken / Tracking Shot** *(`natural real-time speed` / `blistering whip-fast speed` for chase)* | **1 Primary Kinetic Move (`One-Move Rule`, `18–30w`)**: Raising a wine glass, setting a brass keyring onto a contract and tapping twice, or stepping forward. | Masseter jaw clenching, visible throat swallow, shifting eyeline, smile hardening into cold stare. | **`6 to 12 words`** (`8–13 VN syllables` at `~2.5 words/s` with `natural real-time speed`; `0 words` if tracking chase). |
| **`2.0s – 3.0s` Final Shot (`Terminal Settle`)** *(`natural real-time speed`)* | **Wordless Visual Payoff / Somatic Reaction Settle**: Hands and feet ground into a Clean Dynamic Landing Pose (`0 motion blur`) ready for `Last Frame` extraction. | Polite smile draining, fingers locking on glass stem, rising steam, or rhythmic chest respiration. | **Strictly `0 spoken words` (`Zero Tail-Cut Law`)**: Protects clean audio landing and mouth-closed final frame. |

---

## 🌐 § 1.3. THE UNIVERSAL SPATIAL DYNAMICS ENGINE (INTERIOR, EXTERIOR & CROSS-SPACE TRANSITIONS)

Generative AI diffusion engines risk catastrophic latent distortion (severe blooming, exposure clipping, architectural warping) when transitioning between environments. The director must enforce explicit spatial rules:

### 1. Pure Interior Architecture (INT.)
- **Lighting & Physics**: Controlled directional sources (recessed LED strips, tungsten desk lamps, soft window bounce). High-contrast specular reflections on polished floors (epoxy, terrazzo, dark hardwood).
- **Acoustics & Diegetics**: Enclosed reverberant room tone, footstep squeaks, air circulation hum.
- **Prompt Mandate**: Rigidly anchor room geometry and bounding planes (`polished epoxy floor`, `far wall glass panels`).

### 2. Pure Exterior Environments (EXT.)
- **Lighting & Physics**: Infinite depth of field, directional celestial lighting (midday sun, golden hour angle, diffuse overcast sky). Aerodynamic forces must be observable (wind catching coat lapels, hair strands fluttering, foliage sway).
- **Acoustics & Diegetics**: Unbounded ambient audio (distant urban traffic, open-air wind whistle, rustling leaves).

### 3. Cross-Space & Threshold Transitions (Giao Thoa Hai Không Gian Khác Nhau)
- **Track A (Single-Shot Threshold Push-Through)**:
  - *Mechanism*: Camera moves with subject from an interior corridor/room directly through open sliding glass doors or a threshold onto an outdoor terrace/courtyard.
  - *Exposure Adaptation Mandate*: Prompt MUST explicitly describe camera exposure adjustment: `gliding from the cool interior hallway through the open glass doorway into blazing midday sunlight, the exposure adapting smoothly to natural exterior illumination`.
  - *Context Declaration*: Declare unified linked space: `linked interior-to-terrace living space [100% Refer to...] spanning from the interior room through floor-to-ceiling glass doors onto the sunlit exterior terrace`.
- **Track B (Multi-Shot Cross-Space Intercut)**:
  - *Mechanism*: Shot 1 frames Subject A indoors looking outward through a transparent glass divider; Shot 2 cuts across the 180° action axis framing Subject B outdoors looking back inward.
  - *Eyeline & Lighting Delta Lock*:
    - Subject A indoors looks out through the glass toward Subject B, under dim interior lighting, with bright outdoor sky visible beyond the glass.
    - Subject B outdoors looks back in toward Subject A, buffeted by exterior wind and drenched in direct sunlight, with the dim interior room reflected in the glass pane. Screen direction (who holds screen-left / screen-right) is recorded in the Audit Card; Code Block 1 expresses it only through these architecture-anchored eyelines.
    - Eyeline matching through the physical divider is 100% mandatory.

### 4. Confined & Intimate Spaces (Không Gian Hẹp: Ngôi Nhà Nhỏ, Hang Động, Cabin, Ngưỡng Cửa)
> [!IMPORTANT]
> **THE CONFINED SPACE PARADOX IN GENERATIVE AI**:
> When staging in physically tight environments (small rustic house, narrow cave mouth, compact kitchen, small wooden cabin), wide shots trigger catastrophic diffusion failures: the AI hallucinates unnatural cavernous dimensions, distorts walls with fisheye warping, or merges characters into background clutter.
> Directing in confined spaces requires **Intelligent Focal Depth, Progressive Shot Scaling, and Spatial Framing**:

#### A. The 3 Golden Rules of Confined Space Staging:
1. **Ban Unmotivated Wide Shots**: Never use an Extreme Wide Shot inside a small cramped room or narrow cave. Use **Medium Close-Up (MCU)**, **Tight Medium (MS)**, and **Tactile Inserts (CU/ECU)** to convey intimacy, claustrophobia, or rustic coziness without exposing AI boundary limitations.
2. **Frame-Within-a-Frame (Khung Hình Trong Khung Hình)**: Utilize natural architectural apertures (doorframes, low cave ceilings, wooden lintels, window mullions) as foreground silhouettes. This anchors depth and prevents wall warping.
3. **The Reverse Threshold Looking-Out Angle (Góc Nhìn Ngược Từ Trong Nhìn Ra)**: Position the camera INSIDE the darker compact space looking out through the door/mouth at the brightly lit exterior. The subject enters as a dramatic silhouette catching sharp separation rim light, creating maximum dynamic contrast without needing massive room volume.

#### B. The Threshold Access Action Chain (Case Study: Unlocking & Entering a Small House):
To depict a character approaching, unlocking, and entering a small house or cavern without AI hand-morphing or spatial jumps:
- **Track A: Single-Shot Unbroken Steadicam Follow (00:00–00:10)**:
  * `[00:00–00:04.0]`: Medium three-quarter tracking shot following the character up the porch steps, closing distance to the wooden door. The camera tilts subtly down to frame the hand raising brass keys toward the keyhole.
  * `[00:04.0–00:07.0]`: Smooth push-in to an intimate close-up as the key inserts into the brass lock with a crisp mechanical snap, the hand turning the latch and pushing the heavy timber door inward. Outdoor light slices across the narrow interior entrance.
  * `[00:07.0–00:10.0]`: Camera glides forward across the raised wooden threshold behind the character's shoulder, entering the compact interior. Exposure adapts to warm ambient indoor shadow; the character pulls the door half-closed behind her, settling into a deep, relieved biological breath.
- **Track B: Multi-Shot Kinetic Threshold Montage (3 Beats)**:
  * `Beat 1 [00:00–00:03.5] (EXT)`: Eye-level Medium Tracking shot on the exterior porch: The woman advances briskly to the weathered door frame under natural daylight.
  * `Beat 2 [00:03.5–00:06.5] (THRESHOLD INSERT)`: Low-angle Extreme Close-Up on the door lock: Slender fingers slide a brass key into the keyway, twisting 90 degrees with an audible metallic click, pushing the lock bolt back as the door unlatches.
  * `Beat 3 [00:06.5–00:10.0] (INT)`: Low-angle Interior Reverse Shot looking out: Positioned inside the dim small room looking out the open doorway. The woman crosses the threshold as a rim-lit silhouette against the sunlit porch, stepping onto the floorboards and pulling the wooden door shut behind her, ambient room dust settling in the light shaft right to 00:10.0, zero frozen frames.

---

## 🧭 § 2. THE DUAL SCENE PARADIGM: SINGLE-SHOT VS. MULTI-SHOT TAXONOMY

Before crafting any 10-second scene, the director must resolve the foundational cinematic fork:  
**"Does this scene demand the accumulative pressure of an unbroken temporal stream (Single-Shot), or the violent dialectic collision of editorial cuts (Multi-Shot)?"**

Both tracks are governed by **Elastic Montage & Temporal Physics (1 to 5 dynamic shots/beats)**, preserving kinetic momentum and biological realism without forcing rigid 3-phase templates or artificial bracket headers.

> 🔀 **THIRD OPTION — TRACK AB (HYBRID TAKE + CUT)**: when pressure must accumulate in one unbroken breath **but the landing must be seen through another eye** (the witness, the prop, the reverse), combine them: one continuous take ≥ 5 s holding 2+ phases, punctuated by 1–2 cuts on the 180° axis. Selection table, hybrid shapes, shot counts, and syntax (`In the same take` / `Cut to`): [`0b-temporal-camera-grammar.md` §6.1, §8, §12](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md).

---

### 🅰️ TRACK A: SINGLE-SHOT CONTINUOUS TAKE (Unbroken Cinematic Take)
* **Core Directorial Philosophy**: *"Spatiotemporal Preservation & Accumulative Pressure (Bảo Toàn Không-Thời Gian & Tích Tụ Áp Suất)"*.
* **Camera Mechanics**: One continuous, motivated trajectory across all 10 seconds (Slow Dolly Push-in, Dynamic Velocity Tracking, Orbital Arc, Focus Pull, Revealing Pan). **STRICTLY ZERO HARD CUTS**.
* **Dialogue Architecture**: Single-speaker dominance is the typical shape; budget lines in seconds, not words (grammar §2–§3, §7). Two speakers fit when the camera is static or slow and the lines do not overlap. The opposing character reacts purely through physical micro-biomechanics and silent gaze. 100% clean lip-sync focus.
* **Terminal Cadence & Kinetic Handoff**: The camera and subject complete the beat organically—either gliding into a natural emotional pause or sustaining physical momentum into the next cut, with continuous living motion and strictly zero artificial frozen frames.
* **AI Diffusion Advantage**: Maximum spatiotemporal stability (95%+ success rate). Zero facial morphing, zero costume drift, zero background latent regeneration.

#### The 5 Generalized Directorial Archetypes for Single-Shot:
1. **Intimate Psychological Immersion (Thâm Nhập Nội Tâm & Biến Chuyển Cảm Xúc Đơn Tuyến)**:
   * *Dramatic Nature*: Gradual internal transition from one emotional state to another on a single human face (e.g. from numb shock to welling tears, or from trembling fear to rock-solid defiance).
   * *Scenarios*: Solemn vows, private confessions, prayer, bereavement beside a sacred relic, internal monologues.
   * *Camera Trajectory*: Slow eye-level dolly push-in, intimate macro tracking, gentle orbital spiral.
2. **Continuous Kinetic Physics & High-Speed Trajectories (Bảo Toàn Động Năng & Quán Tính Vật Lý Cao Tốc)**:
   * *Dramatic Nature*: High-velocity directional momentum where a camera cut would disorient the AI diffusion latent space and destroy kinetic continuity.
   * *Scenarios*: Vertical plummet into a chasm (-Y vector), sprinting through a collapsing corridor, aerial dive, slipping on mud, vaulting over a threshold.
   * *Camera Trajectory*: Synchronized velocity descent ($V_{cam} = V_{subj}$), dynamic forward tracking lead/follow, whip-pan trajectory lock.
3. **Tactile Micro-Mechanics & Delicate Prop Interaction (Thao Tác Xúc Giác & Cơ Sinh Học Vi Mô)**:
   * *Dramatic Nature*: Intimate contact between human hands and a high-stakes object where geometric stability is mandatory to eliminate hand-merging and prop morphing.
   * *Scenarios*: Trembling fingers breaking a royal wax seal, slipping a vial of poison into wine, unrolling a frayed map, drawing a concealed dagger, stroking a dying ember.
   * *Camera Trajectory*: Low-angle tight push, macro glide across surface, focus pull from prop to eyes.
4. **Atmospheric Space Discovery & Spatial Reveal (Khám Phá Bối Cảnh & Mở Rộng Không Gian)**:
   * *Dramatic Nature*: Expanding audience awareness from an intimate tactile detail outward into the broader environment, or vice versa.
   * *Scenarios*: Camera gliding from a pool of spilled ink on the floor upward to reveal the assassin waiting in the shadows; or starting tight on a trembling flame and pulling back to reveal an empty ruined cathedral.
   * *Camera Trajectory*: Crane down-and-track, revealing pan, continuous pull-back reveal.
5. **Asymmetrical Dominance & Static Confrontation (Đối Thoại Bất Đối Xứng & Áp Đảo Quyền Lực)**:
   * *Dramatic Nature*: Two characters share the frame, but the power dynamic is totally skewed (100% vs 0%). One dominant figure delivers an unyielding verdict while the subordinate absorbs the blow in suffocating silence.
   * *Scenarios*: Judge condemning a prisoner, ruthless creditor cornering a debtor, military commander issuing an ultimatum.
   * *Camera Trajectory*: Deep-staging medium two-shot with subtle continuous push-in, shallow focus isolating the speaker or rack-focusing to the terrified listener.

---

### 🅰️-LOCKED: TRACK A-LOCKED — THE LOCKED-OFF PERFORMANCE VARIANT (Cú Máy Tĩnh Khóa Cố Định Tập Trung Diễn Hoạt)
* **Core Directorial Philosophy**: *"Stillness As Magnitude (Sự Tĩnh Lặng Tạo Nên Sức Nặng)"*.
* **Camera Mechanics**: The camera is **100% stationary on a fixed static mount** (prose bans the word "tripod"). Zero panning, zero tilting, zero tracking, zero zooming, strictly zero camera drift.
* **The Problem in Generative Diffusion Models**: If a prompt simply writes `static camera`, AI video engines (Kling, Runway, Wan 2.1, Sora) tend to render a lifeless still photo or freeze the actor into an emotionless wax mannequin.
* **The Dedicated Prompt Optimization Protocol (Exclusive to Track A-Locked)**:
  1. **Pure Natural Optical Declaration (Khai Báo Cỡ Cảnh, Góc Quay & Camera Tĩnh Trực Tiếp — Bỏ Thẻ `[camera]:` & Bỏ Từ Khóa `tripod`) — Applied Exclusively to Track A-Locked**: Because shot scale, angle, and camera stability are 100% invariant across the entire 10s take, declare the optical setup as a clean natural prose sentence **strictly once** at the head of the action section (immediately after audio and before timeline brackets), completely omitting any `[camera]:` bracket.
     *(Anti-Hardware Hallucination Rule: Strictly ban the word "tripod" or "camera locked on tripod" in prompt prose, because diffusion models mistake it as a literal physical 3-legged tripod apparatus standing inside the room! Simply declare `static camera`)*:
     `[Shot scale, e.g. Medium close-up], [angle, e.g. eye level], static camera.`
     *(Note: This direct natural prose declaration applies EXCLUSIVELY to Track A-Locked; standard Track A moving takes and Track B cuts retain their phase-by-phase camera clauses).*
  2. **Timeline Brackets Dedicated 100% to Character Acting & Environmental Physics**: With the optical anchor fixed at the head, the sub-timeline brackets (`[00:00–00:03.5]`, `[00:03.5–00:07.0]`, `[00:07.0–00:10.0]`) are **100% stripped of repetitive camera clauses**. Every token inside the brackets is dedicated strictly to somatic micro-acting, biological reactions, speech-action delivery, and living atmospheric physics:
     - `[00:00–00:03.5]`: Initial tension (shallow rapid chest heaving, masseter muscle twitching, eyes locked down, fingers clutching prop; dust motes dancing).
     - `[00:03.5–00:07.0]`: Somatic rupture or spoken delivery (eyes welling with unshed tears catching the light, throat swallowing down a choke, knuckles whitening).
     - `[00:07.0–00:10.0]`: Emotional aftermath (chin trembling, single tear spilling down cheek, eyelids fluttering half-closed as shoulders slowly slump; curtain rippling).
  3. **Living Environmental Micro-Dynamics (Anti-Freeze Insurance)**: Mandate continuous physical motion in the background (dust motes drifting lazily through diagonal sunbeams, a delicate curl of steam rising steadily from a teacup, loose strands of hair fluttering in a draft, sheer curtains rippling).
  4. **Tactile Prop Friction & Internal Staging**: The character maintains a physical tactile anchor (fingers clutching wooden rail, twisting ring, pressing palm to table). Movements are internal (head lowering 2 inches, gaze shifting from floor to doorway).
  5. **Clean Single-Subject Frame**: Single-subject framing (CU, MCU, or Dirty Single) ensures the DiT latent space focuses 100% of its parameters on facial musculature and eye expression.

#### Canonical Prompt Syntax for Track A-Locked:
```text
Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Style: [Visual Style Header]. Track A — one continuous take, zero cuts, static camera.

[context]:
[Location Name in English] [100% Refer to image <location_ref_4view.jpg>], [time of day]. [Complete 5-vector physical architectural specification: full fixed furniture inventory, in-scene textiles/bedding, key lighting direction, and continuous environmental micro-motion: dust motes dancing in sunbeams, steam curling steadily].

[subject]:
[character_name] [100% Appearance, attire, and facial features Refer to image X], [architectural anchor], [body posture], hands free of props, [eyeline toward a character or landmark] — the only [character_name] in frame.

[PROP]:
[hero prop in natural English] [100% Refer to image <prop_ref.jpg>], [physical state], [resting place] — the only [prop noun] in frame.  (Tier 2 everyday handheld items: same line without the image tag. No handheld item in the scene: "none (pure environmental and somatic staging)")

Diegetic sound of [room tone], accompanied by [specific Foley: creak of wood, rustle of linen, choked breathing].

Eye-level [Shot scale, e.g. medium close-up] framing [character_name], shallow depth of field holding razor-sharp optical focus on [character_name]'s face with background softly falling into cinematic bokeh, static camera.

[00:00–00:03.5] [actor initial posture, rapid chest breathing, jaw clenched, fingers gripping prop rail; microscopic dust motes swirl in sunbeams].

[00:03.5–00:07.0] [actor swallows hard, jaw quivering, eyes welling with tears, delivers line with breathy choke].
[character_name] [expressive verb] : “ [spoken line within Gate 4B: ≤ 32 words solo, ≤ 15 words per speaker in a two-shot] ”（Voice of [demographic]; [acoustic paralinguistic tags]）

[00:07.0–00:10.0] [lips seal tightly, single tear spills down cheek, chin trembles, head lowers slightly, shoulders slump under invisible weight; background curtains ripple faintly].

Consistent character, lighting, and environmental physics maintained through 00:10.0. No subtitles, no watermark, no text overlays, no duplicate subjects.
```

---

### 🅱️ TRACK B: MULTI-SHOT CUT SEQUENCE (Kinetic Montage)
* **Core Directorial Philosophy**: *"Adversarial Dialectics & Cognitive Shock (Biện Chứng Đối Kháng & Cú Sốc Nhận Thức)"*.
* **Camera Mechanics**: Flexible shot breakdown dictated entirely by the screenplay (Single-shot continuous take, 2 dynamic shots, or rapid cuts as required by narrative tension; strictly NO mandatory 3-shot quota). Governed strictly by the 180° Action Axis, Invariant Screen Directions, and continuous kinetic momentum handoff.
* **Dialogue Architecture**: Governed by the **10-Second Shot Mental Model** ([`0b-temporal-camera-grammar.md`](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md) §1.1). Standard cinematic dialogue achieves **Shot - Reverse Shot across consecutive 10s shot prompts** (Shot 1: Speaker A ➔ Shot 2: Speaker B or Reaction B). Within a single 10s Track B cut sequence, dialogue is permitted ONLY under the **Two-Shot Exception & 15-Word Split Law**: rapid, high-tension staccato sparring where each speaker delivers 5–10 words (hard cap ≤ 15 words per speaker, total ≤ 32w). If any speaker exceeds 15 words, the scene MUST be split into separate solo shots.
* **Phase 3 Arrest Mechanics (`[Terminal Beat]`)**: **Hard Editorial Cut to Choker/Macro (Cắt máy sang cận cảnh Choker)**. The camera cuts decisively to a tight portrait of the character bearing the psychological shockwave, settling into a stable resting frame with continuous subtle biological breathing and atmospheric drift from `terminal seconds right to 00:10.0`, with strictly zero frozen frames.
* **AI Diffusion Advantage**: High-velocity narrative momentum, sharp pacing, classic Hollywood shot/reverse-shot dramatic friction.

#### The 5 Generalized Directorial Archetypes for Multi-Shot:
1. **Adversarial Verbal Sparring & Ping-Pong Clash (Đấu Kiếm Tư Tưởng Ngang Tài Ngang Sức)**:
   * *Dramatic Nature*: Two opposing wills of equal intensity collide face-to-face. Words act as kinetic blades parried and returned.
   * *Scenarios*: Moral disputes, ideological showdowns, courtroom cross-examinations, betrayal confrontations.
   * *Camera Execution*: Shot 1 (Speaker A MCU, anchored by the window) ➔ Cut to Shot 2 (Speaker B counter MCU, anchored by the doorway) ➔ Cut to Shot 3 (Reaction Choker). Screen direction is recorded in the Audit Card only.
2. **The Truth Bomb & Mask Shattering / Anagnorisis (Cú Lật Mặt Nạ & Bộc Lộ Chân Tướng)**:
   * *Dramatic Nature*: Sudden reversal of psychological dominance when devastating evidence or identity is revealed.
   * *Scenarios*: The villain gloats over a forged will ➔ Hero pulls out the authentic royal decree ➔ Villain's smug grin collapses into paralyzed shock.
   * *Camera Execution*: Shot 1 (Arrogant Medium on Antagonist) ➔ Cut to Shot 2 (Tight Insert on Proof held by Hero) ➔ Cut to Shot 3 (Macro Choker on Antagonist's trembling pupil).
3. **Protagonist vs. Greek Chorus / Living Society (Cá Nhân Đối Đầu Áp Lực Xã Hội)**:
   * *Dramatic Nature*: High-contrast friction between an isolated individual and the crushing weight of collective public judgment.
   * *Scenarios*: A mob screaming insults in a public square ➔ Hero stands tall, raising their voice in fearless truth ➔ The crowd falls into collective, stunned silence.
   * *Camera Execution*: Shot 1 (Wide Mob framing) ➔ Cut to Shot 2 (Low-Angle MCU Hero) ➔ Cut to Shot 3 (Wide Living Society in stunned breathless silence).
4. **Cause-and-Effect Spatial Dispersion (Nhân - Quả Phân Tán Không Gian)**:
   * *Dramatic Nature*: An action initiated in one spatial quadrant detonates an immediate physical consequence in another quadrant within the 10-second breath.
   * *Scenarios*: Cutting a rope beside the gate winch ➔ Heavy portcullis slams into the stone threshold ➔ Trapped infiltrator halts rigidly against the bars on the far side of the gate.
   * *Camera Execution*: Shot 1 (Tight Trigger Action) ➔ Cut to Shot 2 (Medium Impact Event) ➔ Cut to Shot 3 (Standoff Arrest).
5. **Emotional Witnessing & Third-Party Stake (Phản Ứng Đa Chiều Của Nhân Chứng Thứ Ba)**:
   * *Dramatic Nature*: The catastrophic weight of a clash lands hardest not on the two combatants, but on an innocent third party observing from the sidelines.
   * *Scenarios*: Two brothers drawing daggers against each other ➔ Flash of clashing blades ➔ Cut to their elderly mother watching from the doorway, hand clutching her throat in silent heartbreak.
   * *Camera Execution*: Shot 1 (Two-Shot Tension) ➔ Cut to Shot 2 (Clash Collision) ➔ Cut to Shot 3 (Choker on Witness Grief).

---

### 📊 COMPARATIVE DIRECTORIAL MATRIX

| Directorial Parameter | Track A: Single-Shot Continuous Take | Track B: Multi-Shot Cut Sequence |
| :--- | :--- | :--- |
| **Camera Cuts** | **Zero Cuts** (1 Unbroken Take across 10.0s) | **1 to 4 shots per 10 s** (grammar §6); each later phase opens with `Cut to …` |
| **Camera Trajectory** | Continuous motivated glide (Dolly, Pan, Track, Orbit) | Discrete angle shifts anchored to the 180° Action Axis |
| **Dialogue Capacity** | **Single Speaker Focus** (Sitcom: 14–24w, cap ≤ 32w; Drama: 8–14w, cap ≤ 20w; craft target 8–14w; timed by grammar §2–§3) | **Rapid Sparring Volleys** (Two-shot exception: ≤ 15w per speaker, total ≤ 32w; standard dialogue uses Shot-Reverse-Shot across consecutive shots) |
| **Phase 3 Arrest Method** | **Deceleration, Settle & Static Lock** | **Hard Editorial Cut to Choker/Macro** |
| **AI Latent Stability** | **Maximum (95%+)**: Zero morphing, zero garment drift | High narrative friction; requires strict 4-Bridge locks |
| **Hollywood Purpose** | Intimate psychological truth, raw physical momentum | Fast-paced conflict, shock revelations, societal friction |

---

## 🎭 § 3. THE 4 EMOTIONAL DESTINATIONS OF PHASE 3 (NƠI DƯ CHẤN HẠ CÁNH)

> 💡 **DIRECTORIAL MANDATE**: In the Terminal Resolution Beat, whether executing a **Hard Editorial Cut** (Multi-Shot) or a **Camera Settle & Static Lock** (Single-Shot), the director must answer: **"Whose heart is broken? Whose world just shattered?"**

```
                                  PHASE 3: WHERE DOES THE BLOW LAND?
                                                  │
          ┌───────────────────────────┬───────────┴───────────┬───────────────────────────┐
          ▼                           ▼                       ▼                           ▼
    [TIER A1: PROTAGONIST]      [TIER A2: ANTAGONIST]   [TIER B: SATELLITE WITNESS] [TIER C: GREEK CHORUS]
    • Moral cost / self-horror  • Broken arrogance/mask • Devastated mentor/mother  • Society arrested in judgment
    • Unblinking tear settle    • Cold predatory smirk  • Accomplice terror         • Market chatter dying
    • Trembling jaw / defiance  • Hollow shock of defeat • Heartbroken companion    • Stunned collective silence
```

### Destination 1: Tier A1 Protagonist (Nỗi Đau, Sự Trả Giá & Thần Thái Bất Khuất)
- **When to Use**: When the protagonist bears the direct moral cost, sacrifice, or heartbreaking realization of their choice.
- **Master Directorial Framings**:
  1. **The Unshed Tear Settle (Choker / Macro on Eyes)**:
     - Tight on A1's eyes: A single heavy tear wells at the eyelid, shimmering in the side-light but held back by sheer willpower; pupils tremble faintly before locking into an unblinking, burning stare of defiance at 09.5s.
  2. **The Horror of One's Own Hands (MCU / Choker)**:
     - A1 looks down at their own trembling hands, breathing shallow and ragged, realizing they have crossed a line they can never uncross; face pale, lips slightly parted in silent shock, freezing dead-still.
  3. **The Unbroken Spine (Low-Angle MCU)**:
     - Even while bleeding or condemned, A1's chin lifts upward, jaw muscles locking into iron resolve, eyes fixed on the horizon with absolute fearlessness.

### Destination 2: Tier A2 Antagonist (Mặt Nạ Sụp Đổ hoặc Nụ Cười Băng Giá)
- **When to Use**: When the confrontation shatters the villain's certainty, or conversely, exposes their chilling lack of humanity.
- **Master Directorial Framings**:
  1. **The Mask Cracking (Tight Close-Up on A2)**:
     - The condescending smirk slowly drains from A2's lips; the corners of the mouth twitch in sudden disbelief, eyes flickering with the first crack of genuine vulnerability or terror, defeated in breathless shock.
  2. **The Predatory Silence (Choker on A2)**:
     - A2 does not shout or rage. A2 tilts their head half an inch, eyes turning pitch-black with murderous calm, breath steadying into a chilling stillness that promises retribution.

### Destination 3: Tier B Satellites (Nỗi Đau Người Quan Sát — Mẹ, Thầy, Bạn Thân, Đồng Minh)
- **When to Use**: The most devastating emotional blows are often felt most acutely by those who love the protagonist or share their guilt.
- **Master Directorial Framings**:
  1. **Maternal / Mentor Heartbreak (Medium Close-Up on B)**:
     - Cut or settle to Tier B (e.g. Milcah or an old mentor): Frail hand clutched against collarbone, eyes wide with unbearable grief as she watches A1 make the ultimate sacrifice. Lips parted in a silent, soundless gasp, paralyzed in breathless grief.
  2. **The Shattered Illusion (Over-The-Shoulder on B)**:
     - B stands in doorway shadows, watching A1 lie or commit violence; B's eyes fill with devastating realization that their hero is flawed, tears glistening in dim light without spilling.
  3. **Complicity & Dread (Choker on B)**:
     - An accomplice or secret-keeper realizes they are trapped in the same doomed fate, swallowing hard as cold sweat beads on their temple, eyes darting to A1 in shared terror.

### Destination 4: Tier C Greek Chorus (Sự Câm Lặng Của Xã Hội & Sự Phán Xét)
- **When to Use**: To show the immense social weight of the personal conflict — how one act of courage or betrayal silences an entire room, street, or army.
- **Master Directorial Framings**:
  1. **The Collective Breath Held (Wide Angle on Living Society)**:
     - Cut or pan to tavern patrons, weavers, or villagers: The bustling noise, clinking tankards, and laughter **CUT TO A COMPLETE, EERIE STILLNESS**. Every single head is turned toward the combatants, eyes wide, paralyzed in mid-motion.
  2. **The Moral Rejection (Medium Shot on Crowd)**:
     - Townsfolk quietly, instinctively step backward into the shadows, leaving A1 and A2 isolated in a circle of empty space, casting heavy, judging gazes.

---

## 🔗 § 4. THE 4 CONTINUITY NEURAL BRIDGES (FOR MULTI-SHOT CUT SEQUENCE)

> 💡 **THE ROOT CAUSE OF FRAGMENTATION ("CHẮP VÁ")**:  
> Multi-shot prompts look "stitched together" and stutter when Shot 2 does not know what Shot 1 just did, or when Shot 3 suddenly jumps to an unrelated spatial dimension.  
> To weave cuts into an unbroken, silk-smooth kinetic ribbon, four neural continuity bridges must be locked:

```
  SHOT 1 [00:00–00:XX.X] ══════════════► SHOT 2 [00:XX.X–00:YY.Y] ══════════════► SHOT 3 [00:YY.Y–00:10.0]
          │                                           │                                           │
          ├──── 1. Spatial Vector & 180° Lock ────────┴──── Invariant Screen Left / Right ────────┤
          ├──── 2. Kinetic Momentum Handoff ──────────┴──── Inherit Velocity; STRICT ZERO REPEAT ─┤
          ├──── 3. Chekhov Prop State Machine ────────┴──── Ready ➔ Under Load ➔ Transformed ─────┤
          └──── 4. Terminal Living Organic Settle ────┴──── 0 Spoken Dialogue; Biomechanics ──────┘
```

### 1. Spatial Vector & 180° Axis Lock (Khóa Không Gian & Đường Trục 180°)
- **The Invariant Screen-Direction Law**:
  - If in Shot 1, **Subject A is on Screen-Left looking toward Screen-Right, and Subject B is on Screen-Right looking toward Screen-Left**, then across all cuts:
  - Even when switching to an Over-the-Shoulder, Low-Angle, or Tight Choker in Shot 2 and Shot 3: **A MUST maintain left-to-right gaze/vector, and B MUST maintain right-to-left gaze/vector**. (Record screen direction in the Audit Card only; Code Block 1 anchors gaze to characters and architecture, with zero frame-left / frame-right words).
  - The 180° action line is sacred and must never be crossed without an explicit in-camera tracking orbit.
- **The Invariant Ground/Floor Anchor (Mặt Sàn Bất Biến)**:
  - All shots within a 10s prompt must use the exact identical noun phrase for the floor/ground surface (e.g., `packed earthen floor`, `mossy stone flagstones`, `sun-baked red clay soil`).
  - Switching descriptions mid-scene causes the AI diffusion latent space to regenerate the environment entirely.

### 2. Kinetic Momentum Handoff (Khóa Quán Tính Động Năng — STRICT ZERO ACTION REPETITION)
- Each shot inherits the forward kinetic momentum of the preceding shot. **Never repeat an action beat across cuts**:
  - ❌ *Broken*: Shot 1 shows character beginning to unsheathe dagger. Shot 2 shows character unsheathing dagger again.
  - ✅ *Kinetic Handoff*: Shot 1 shows dagger clearing scabbard; Shot 2 inherits velocity into a gleaming steel arc whistling through air; Shot 3 embeds point into timber or levels it at opponent's throat!

### 3. The Chekhov Prop State Machine & The Mandatory Entity Re-Naming Law (Khóa Trạng Thái Đạo Cụ & Đổi Tên Thực Thể)

The prompt compiler tracks props across a 3-phase kinetic state machine, governed by the **Prop Mutability Lifecycle**:
- **Shot 1 (Ready)**: Prop rests in an intact, poised state (resting in hand / resting on table / sheathed).
- **Shot 2 (Under Load)**: Prop absorbs or delivers force (swung through air / struck / flexing under strain / liquid splashing).
- **Shot 3 (Landed / Transformed)**: Prop reaches final altered state (embedded in wood / shattered shards / clutched tightly to sternum).

#### ⚠️ The Mandatory Entity Re-Naming Law for Structural Fractures (Luật Đổi Tên Tránh Ảo Giác AI):
When a prop undergoes structural destruction (torn, shattered, incinerated, severed), **PROMPT COMPILERS ARE STRICTLY FORBIDDEN FROM RETAINING THE ORIGINAL INTACT ENTITY NAME**:
- **Surface Weathering (Level 1)**: Topology intact. Retain original name with surface modifier (`[The mud-stained Debt Ledger]`, `[The rain-soaked Letter]`).
- **Structural Fracture (Level 2 — Anti-Hallucination Mandate)**: Topology destroyed. **PROMPT MUST RE-NAME TO THE NEW PHYSICAL FRAGMENTS**:
  - `The Book / Ledger` $\longrightarrow$ **`Torn Parchment Shreds`** (Prevents AI from rendering an intact falling book!).
  - `The Porcelain Teacup` $\longrightarrow$ **`Jagged Ceramic Shards`** (Prevents AI from rendering an unbroken teacup on the floor!).
  - `The Letter / Contract` $\longrightarrow$ **`Smoldering Ash Flakes`** (Forces AI to render drifting glowing embers instead of flat paper).
  - `The Heirloom Mirror` $\longrightarrow$ **`Fractured Silver Glass Splinters`**.
  - `The Broadsword` $\longrightarrow$ **`Broken Sword Hilt`** & **`Snapping Blade Tip`**.

### 4. Cinematic Scale Progression (Logic Biến Thiên Cỡ Cảnh)
- **Model A: Dynamic Two-Shot (Action ➔ Reaction)**: `Shot 1 Medium / Tracking` ➔ `Shot 2 Counter-Angle / Close-Up` (pacing governed by dramatic tension).
- **Model B: Outward Explosion (For Revelations & Shockwaves)**: `Shot 1 Tight Choker` ➔ `Shot 2 Medium Action Clash` ➔ `Shot 3 Wide Living Society in Stunned Silence`.

### 5. Inter-Clip 10s Continuity & Temporal Handshake Protocol (Cầu Nối Ghép Nối 10s Giữa Scene N và Scene N+1)

> 🎬 **THE MASTER STITCHING MANDATE (QUY CHUẨN GHÉP PHIM ĐIỆN ẢNH TỪ CÁC CLIP 10S)**:
> In third-party AI video generation (Sora, Runway, Kling, Veo), each 10-second scene is rendered as an isolated, stateless file. When imported into an NLE editor (Premiere, DaVinci, CapCut) and assembled sequentially, the edit must look like **one continuous, seamless cinematic film** rather than 10 disconnected clips.
> This seamless flow is achieved through the **Inter-Clip Handshake Protocol**:

```
SCENE N (10.0s Clip)                                SCENE N+1 (10.0s Clip)
┌─────────────────────────────────────────┐         ┌─────────────────────────────────────────┐
│ [00:08.5–00:10.0] Terminal Outbound     │ ──────► │ [00:00.0–00:01.5] Inbound Ingestion     │
│ Active character initiates a physical   │  MATCH  │ Reverse angle or new shot catches and   │
│ vector (turns head, reaches out, drops  │   CUT   │ completes that exact physical vector,   │
│ an object, begins stepping forward).    │  RELAY  │ inheriting velocity with ZERO restart.  │
└─────────────────────────────────────────┘         └─────────────────────────────────────────┘
```

1. **The Inbound/Outbound Kinetic Baton**:
   - **Outbound Baton (Scene N, 00:08.5–00:10.0)**: The prompt MUST direct a micro-action that carries unfinished kinetic momentum into the cut (e.g. `Ma Ba turns sharply toward the door frame, right hand reaching out for the latch...`).
   - **Inbound Baton (Scene N+1, 00:00.0–00:01.5)**: The opening line of the next prompt MUST catch this exact motion from the new camera angle (e.g. `Cut to reverse shot from the dim corridor: Ma Ba's hand pushes the latch downward, stepping across the wooden threshold...`).
   - **Editing Impact**: When cut together on the action (Action Match-Cut), the camera switch feels intentional and cinematic, erasing the AI clip boundary completely.
2. **Invariant Spatial & Gaze Geometry (The Screen Direction Law)**:
   - If Character A faces Screen-Right and Character B faces Screen-Left in Scene N, Scene N+1 MUST strictly maintain this gaze vector across all reverse shots, close-ups, and over-the-shoulders. (Record screen direction in the Audit Card only; Code Block 1 anchors eyelines to characters and landmarks).
   - The floor material (`[context]` ground phrase) and key light orientation MUST remain 100% identical across consecutive scenes in the same setting.
3. **Auditory Suture (L-Cut & Diegetic Foley Continuity)**:
   - In Code Block 1: `Diegetic room acoustics:` must use the same ambient texture (e.g. `steady ceiling fan drone, rain patter against corrugated tin`) across all contiguous scenes in that space.
   - In dialogue delivery: The Director may script an **L-Cut Audio Tail**, where Scene N's closing line resonates over Scene N+1's opening silent reaction shot.
4. **Prop & Posture Handover Ledger (Code Block 2 Synchronization)**:
   - Code Block 2 of Scene N records the **Exact Physical Coordinate Snapshot** at `00:10.0` (Character positions, hands holding props, facial tension).
   - Scene N+1's `[subject]` and `[PROP]` sections must inherit this exact physical state at `00:00.0` with zero discrepancies.
5. **Aesthetic Specificity Over Boilerplate Beauty Phrases**:
   - Strictly ban the copy-pasting of generic `"Modern K-Drama Premium Cinematography, high-key beauty illumination, soft pastel urban palette"` across all scenes regardless of genre.
   - The style line must reflect the **film's psychological reality**: naturalistic contrast, atmospheric grain, chiaroscuro shadows, tactile surfaces, and genuine human skin tones.

---

## 📋 § 5. PRODUCTION TEMPLATES & REFERENCE DEMOS

> [!IMPORTANT]
> **THE ZERO-CONFLICT MULTI-MODAL PROMPT ARCHITECTURE (2026 MANDATE)**:
> Code Block 1 MUST BE STRUCTURED INTO EXACT THREE EXPLICIT MULTI-MODAL REFERENCE BLOCKS:
> 1. `[context]:` Evocative natural-English Location Name (no underscores) with `[100% Refer to image ...]` + Time of Day, Atmosphere, and Key Lighting.
> 2. `[subject]:` The Sovereign Formula (`[ho_ten + Image Anchor]` + `[Architectural Anchor (same landmark within arm's reach for physical contact)]` + `[Body Posture + hands free of props if unheld at 0.0s OR explicit hand-grip if already holding a prop at 0.0s]` + `[Eyeline]` + `[— the only [name] in frame]`). No frame-edge directions, no metre figures.
> 3. `[PROP]:` Handheld items only, one prop per line, each declaring its $t=0.0\text{s}$ state (resting on a surface if unheld at $0.0\text{s}$, or held in `[ho_ten]`'s hands if already held at $0.0\text{s}$, synchronized with `[subject]:`): Tier 1 hero props with `[100% Refer to image ...]`, Tier 2 everyday items as natural-English text only. Furniture and fixtures stay in `[context]:`.
> **BLANK LINE SPACING LAW**: Each section MUST be separated by an empty line (`\n\n`) for visual clarity and token parsing isolation.
> **THE STATE-DELTA DIRECTING PROTOCOL (ZERO `[subject]:` REPETITION & ZERO STATE CONTRADICTION)**: In every timeline shot (`[00:00–00:XX]`), NEVER repeat static positions or furniture anchors already declared in `[subject]:`, and NEVER command a character to re-execute a posture/hand state they already hold in `[subject]:`. Direct only: (1) 1 Concrete Transition Verb, `then` (2) Speaker + 1 simple gesture, `as` (3) Supporting character's static watch or visible facial shift.
> **THE 5-POINT `[context]` ↔ `[subject]` ↔ `[timeline]` OPTICAL CROSS-CHECK**:
> 1. **Full Sovereign `[subject]:` & Two-Tier `[PROP]:` Parity**: Never strip `[subject]:` or `[PROP]:` in Code Block 1 down to bare tags; preserve architectural anchor, vertical posture, $t=0.0\text{s}$ hand state, eyeline, and `— the only {name} in frame`.
> 2. **Optical Ray-Tracing (`FG / MG / BG`)**: Trace `Camera ➔ FG ➔ MG ➔ BG` against `[context]:` and `[subject]:`. If A stands in front of B facing B, then in a frontal shot of B, A is in `FG` (back to lens) or `Off-Screen` behind the lens—NEVER `"in the background"` or `"behind B"`.
> 3. **Vertical Posture-to-Angle Match**: Cross-check whether framed subjects are `standing`, `sitting`, or `kneeling`. Never frame a standing adult and a floor-seated/kneeling character in a flat `eye-level medium two-shot`.
> 4. **Single-Subject Scale FoV & OTS Speaker Visibility**: In `MCU / CU / Choker`, direct strictly ONE character (never place secondary character actions in the background of a `CU`). In `Over-the-shoulder [scale] framing B past A's shoulder`, only `B` (facing lens) can speak with on-screen lip-sync; `A` (back to lens) MUST NOT deliver lip-synced dialogue.
> 5. **Motivated `Cut to` & Canonical `—` Separator**: Every phase in Track A (moving), Track B, and Track AB separates its camera clause from action prose with ` — `. Every `Cut to` shifts subject, scale, or angle ($\ge 30^\circ$) and flips the architectural background along the 180° axis.
> Timeline phases follow beneath in canonical syntax terminating in standard stability and negative lines.

> [!NOTE]
> Every demo below passes `engine/episode_audit_suite.py` with zero warnings. Syntax and timing follow [`0b-temporal-camera-grammar.md`](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md). In real deliverables, Code Block 2 is written in Vietnamese (`workflow.md` §9.5); it is shown in English here for reference.

### 🎬 DEMO 1: TRACK A — 10 s SINGLE-SHOT CONTINUOUS TAKE (SOLO VOW & MOTIVATED PUSH-IN)

Intent: Noa promises more than Noa can deliver. The camera stays still while the empty jar is discovered (witness), then pushes in only when Noa decides (motive: inner shift).

#### Code Block 1 (Track A — 10 s)
```text
Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Style: 3D animation masterwork in a Pixar and DreamWorks studio style. Track A — one continuous take, zero cuts.

[context]:
Rustic limestone kitchen [100% Refer to image location_kitchen_4view.jpg], at dusk. Warm amber embers glow low inside the stone hearth, balanced by pale blue twilight slanting through the open doorway; fine dust motes hang in the light shafts.

[subject]:
Milcah [100% Appearance, attire, and facial features Refer to image 2], resting on the low wooden cot against the back wall, head on a straw pillow, frail right hand resting on the blanket edge, eyes half-closed, breathing slowly in shallow exhaustion — the only Milcah in frame.
Noa [100% Appearance, attire, and facial features Refer to image 1], kneeling on the packed earthen floor beside the hearth, right hand gripping the worn wooden scoop inside the mouth of the empty terracotta grain jar, chest rising in guarded breaths, gaze on the cot — the only Noa in frame.

[PROP]:
empty terracotta grain jar, cracked rim, lying on its side on the earthen floor beside Noa's left knee, hollow mouth facing the hearth — the only grain jar in frame.
worn wooden scoop, gripped in Noa's right hand inside the mouth of the terracotta grain jar — the only scoop in frame.

Diegetic room acoustics: muffled desert wind outside, crackle of dying coals, soft scrape of wood against clay.

[00:00–00:03.0] Medium two-shot framing Noa and Milcah, low angle, static camera — Noa scrapes the worn wooden scoop along the inside of the grain jar finding nothing, as Milcah's frail right hand slides limply from the blanket edge.

[00:03.0–00:07.5] Slow push-in to a medium close-up framing Noa at eye level, shallow depth of field holding sharp optical focus on Noa's face — Noa sets down the worn wooden scoop and turns toward Milcah, jaw setting.
Noa whispers : “ Rest, Mother. The loom will feed us. ”（Voice of a 20-year-old woman from the Judean hills, steady and fervent, precise lip-sync, warm hearth light across the cheek, a promise Noa is not sure of）

[00:07.5–00:10.0] The push-in settles into a close-up framing Noa at eye level, shallow depth of field with warm hearth embers softly blurred behind Noa — lips press together, the chest rises in one deep silent breath, and Noa's eyes glisten in the amber light as fine dust motes drift across the light shaft.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored to the architecture; characters move only where the action says they move.
Do not generate subtitles, dialogue text, titles, timestamps, or written text anywhere in the video. Do not render duplicate characters or extra props.
```
Timing: line = 7 words ≈ 3.1 s inside a 4.5 s phase; push-in MS → MCU over 4.5 s (grammar §5: 3–5 s). Speech ≈ 31 % of the clip.

#### Code Block 2 (Handover @00:10)
```text
[HANDOVER STATE AT 00:10.0]:
- Noa: kneeling beside the hearth, torso turned toward the cot, wooden scoop resting on the floor beside the right knee, jaw set, eyes wet.
- Milcah: lying on the cot against the back wall, right hand fallen from the blanket edge, eyes half-closed.
- Prop: empty grain jar on its side beside Noa's left knee, mouth toward the hearth.
- Light: embers fading in the hearth, blue twilight from the doorway now dominant.
- Camera: settled in a close-up on Noa, static.
- Dialogue audit: 7 words, one speaker.
```

---

### 🎬 DEMO 2: TRACK B — 10 s MULTI-SHOT CUT SEQUENCE (ADVERSARIAL PING-PONG)

Intent: Eleazar springs a trap; Noa reverses it with proof. Each cut lands on a change of power (grammar §6), the angle on Noa rises as Noa takes control.

#### Code Block 1 (Track B — 10 s)
```text
Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Style: 3D animation masterwork in a Pixar and DreamWorks studio style. Track B — multi-shot sequence cut on the 180-degree axis.

[context]:
Limestone debt-collector's alcove [100% Refer to image location_alcove_4view.jpg], at nightfall. A heavy iron brazier beside the ledger table throws harsh orange charcoal light upward; cold moonlight slants through a high barred window; charcoal haze hangs under the low ceiling.

[subject]:
Eleazar [100% Appearance, attire, and facial features Refer to image 4], standing behind the timber ledger table on the brazier side, upright posture, hands free of props at sides, eyeline fixed on Noa — the only Eleazar in frame.
Noa [100% Appearance, attire, and facial features Refer to image 1], standing erect on the doorway side of the table, empty hands clenched at the sides, facing Eleazar — the only Noa in frame.

[PROP]:
forged debt tablet [100% Refer to image prop_tablet_4view.jpg], cracked terracotta with a dove wax seal, resting at the center of the ledger table — the only debt tablet in frame.
copper family seal [100% Refer to image prop_seal_4view.jpg], worn green-tinged copper, resting at the doorway-side edge of the table within Noa's reach — the only seal in frame.

Diegetic room acoustics: crackling brazier coals, wind whistling through the window bars, heavy breathing.

[00:00–00:03.8] Medium close-up framing Eleazar, low angle, slow push-in, sharp optical focus on Eleazar — Eleazar slaps a flat palm down beside the forged debt tablet and glares toward Noa.
Eleazar snaps : “ Your father's debt is due tonight. ”（Voice of a 55-year-old man from Jerusalem, harsh and gravelly, precise lip-sync, brazier glow under the brow, savoring the trap）

[00:03.8–00:07.6] Cut to a medium close-up framing Noa, slight low angle, sharp optical focus on Noa, static camera — Noa presses a palm onto the copper family seal, chin lifting in defiance toward Eleazar.
Noa replies : “ That seal is forged. Father paid. ”（Voice of a 22-year-old woman from the Judean hills, ringing and fierce, precise lip-sync, moonlight across the eyes, refusing to be afraid）

[00:07.6–00:10.0] Cut to an extreme close-up on Eleazar's eyes, eye level, static camera — the condescending smirk drains, pupils contract under the moonlight; lips stay sealed, breath catches, charcoal haze drifts across the frame.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored to the architecture; characters move only where the action says they move.
Do not generate subtitles, dialogue text, titles, timestamps, or written text anywhere in the video. Do not render duplicate characters or extra props.
```
Timing: two 6-word lines ≈ 2.7 s each inside 3.8 s phases; 3 shots in 10 s (grammar §6: 2–4); speech ≈ 54 %.

#### Code Block 2 (Handover @00:10)
```text
[HANDOVER STATE AT 00:10.0]:
- Eleazar: behind the ledger table on the brazier side, right palm flat beside the tablet, eyes wide, lips parted.
- Noa: doorway side of the table, right hand pinning the copper seal to the wood, chin raised, gaze on Eleazar.
- Props: forged debt tablet at the table center; copper seal beside the tablet under Noa's right hand.
- Light: orange brazier glow from below, moonlight across Noa's jaw and Eleazar's temple.
- Camera: settled on an extreme close-up of Eleazar's eyes, static.
- Dialogue audit: 12 words (Eleazar 6, Noa 6).
```

---

### 🎬 DEMO 3: TRACK A — 15 s TAKE (USER-REQUESTED) (VIETNAMESE, TWO SPEAKERS, ONE SLOW MOVE)

Use only when the user explicitly asks for 15 s (`workflow.md` §2.4). Intent: Hạnh brings a letter from the estranged son; Bà Tư hides years of hurt behind a dry joke. One continuous slow push-in carries the pressure; both lines are spoken while the camera moves slowly, which is lip-sync safe (grammar §5).

#### Code Block 1 (Track A — 15 s)
```text
Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Style: cinematic live-action realism, warm Mekong Delta palette, gentle film grain. Track A — one continuous take, zero cuts.

[context]:
Riverside wooden kitchen [100% Refer to image location_kitchen_ref.jpg], late afternoon. Low sun enters through the slatted bamboo wall behind the clay stove, laying warm stripes across the floorboards; wood smoke hangs under the thatch.

[subject]:
ba_tu [100% Appearance, attire, and facial features Refer to image 1], seated on a low wooden stool beside the clay stove, both hands resting on the knees, shoulders rounded, gaze on the fire — the only ba_tu in frame.
hanh [100% Appearance, attire, and facial features Refer to image 2], standing in the kitchen doorway with one shoulder against the frame, hands free of props at the sides, gaze on ba_tu — the only hanh in frame.

[PROP]:
blackened clay pot, lid ticking with steam, resting on the clay stove beside ba_tu — the only clay pot in frame.
folded letter [100% Refer to image prop_letter_ref.jpg], creased cream paper, resting on the low bamboo shelf just inside the doorway beside hanh — the only letter in frame.

Diegetic room acoustics: crackling firewood, a pot lid ticking with steam, river water lapping under the stilts.

[00:00–00:04.0] Wide shot framing hanh and ba_tu, eye level, deep depth of field, static camera — hanh lifts the folded letter as ba_tu sits still watching the stove fire.

[00:04.0–00:08.0] Slow push-in to a slight low-angle medium two-shot framing hanh and ba_tu, optical focus holding on hanh — hanh steps toward the clay stove, then hanh holds out the folded letter and speaks.
hanh says : “ Thư của anh Hai gửi về nè má. ”（Voice of a 30-year-old woman from the Mekong Delta; soft high-pitched hesitant tone, anxious filial vulnerability）

[00:08.0–00:12.5] The push-in continues to a medium close-up framing ba_tu at eye level, shallow depth of field holding sharp focus on ba_tu — ba_tu lets go of the pot handle and stares at the letter without taking it.
ba_tu says : “ Nó còn nhớ đường về cái nhà này hả con? ”（Voice of a 68-year-old woman from the Mekong Delta; low raspy dry timbre, bitter defensive hurt masking sorrow）

[00:12.5–00:15.0] The camera settles into a static medium close-up — ba_tu's fingers curl slowly toward the letter and stop a hand's width short; smoke drifts across the frame, breathing slows.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored to the architecture; characters move only where the action says they move.
Do not generate subtitles, dialogue text, titles, timestamps, or written text anywhere in the video. Do not render duplicate characters or extra props.
```
Timing: 8 + 10 = 18 syllables (grammar §7: 18–36 for 15 s); line 2 ≈ 2.9 s inside 4.5 s; one push-in, wide → medium close-up across 8.5 s; living settle 2.5 s. Speech ≈ 31 %.

---

### 🎬 DEMO 4: TRACK B — 30 s SINGLE PROMPT (USER-REQUESTED) (EXPANDED SHOTS, THREE-ACT MINI SCENE)

Use when the user explicitly requests 30s. The macro scene architecture (`[context]`, `[subject]`, `[PROP]`, acoustics, closing line) is **identical to a 10s or 15s scene**. Duration is expanded simply by **adding shots on the 180° axis** (Act I Setup → Act II Collision & Power Shifts → Act III Decision & Settle).

#### Code Block 1 (Track B — 30 s Single Prompt)
```text
Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Style: cinematic live-action realism, warm Mekong Delta palette, gentle film grain. Track B — multi-shot sequence cut on the 180-degree axis.

[context]:
Riverside wooden kitchen [100% Refer to image location_kitchen_ref.jpg], late afternoon. Low sun enters through the slatted bamboo wall behind the clay stove, laying warm stripes across the floorboards; wood smoke hangs under the thatch.

[subject]:
ba_tu [100% Appearance, attire, and facial features Refer to image 1], seated on a low wooden stool beside the clay stove, both hands resting on the knees, shoulders rounded, gaze on the fire — the only ba_tu in frame.
hanh [100% Appearance, attire, and facial features Refer to image 2], standing in the kitchen doorway with one shoulder against the frame, hands free of props at the sides, gaze on ba_tu — the only hanh in frame.

[PROP]:
blackened clay pot, lid ticking with steam, resting on the clay stove beside ba_tu — the only clay pot in frame.
folded letter [100% Refer to image prop_letter_ref.jpg], creased cream paper, resting on the low bamboo shelf just inside the doorway beside hanh — the only letter in frame.

Diegetic room acoustics: crackling firewood, a pot lid ticking with steam, river water lapping under the stilts.

[00:00–00:05.5] Wide shot framing hanh and ba_tu, eye level, slow push-in — hanh lifts the folded letter, looking at ba_tu, as ba_tu sits still without turning around.

[00:05.5–00:11.0] Cut to a slight low-angle over-the-shoulder shot framing hanh past ba_tu's foreground silhouette, sharp optical focus on hanh, static camera — hanh steps toward the clay stove, then hanh extends the folded letter and speaks.
hanh says : “ Thư của anh Hai gửi về từ thành phố nè má. ”（Voice of a 30-year-old woman from the Mekong Delta; soft high-pitched hesitant tone, earnest filial vulnerability）

[00:11.0–00:17.5] Cut to a slight high-angle medium close-up framing ba_tu along the 180-degree axis, shallow depth of field holding sharp focus on ba_tu's weathered face, static camera — ba_tu tightens her jaw and speaks without looking at the folded letter.
ba_tu says : “ Mày cất đi. Tao không có đứa con nào thứ hai hết. ”（Voice of a 68-year-old woman from the Mekong Delta; low raspy dry timbre, stubborn pride masking deep hurt）

[00:17.5–00:24.0] Cut to a medium shot framing hanh, eye level, slow push-in, sharp optical focus on hanh — hanh crouches down onto one knee beside the stove, placing the creased letter gently onto the dry timber beside ba_tu's stool; hanh's gaze holds ba_tu's eyes.
hanh says : “ Anh Hai nói tháng sau anh về giỗ ba. ”（Voice of a 30-year-old woman from the Mekong Delta; warm mellow gentle cadence, earnest emotional plea to heal the family）

[00:24.0–00:30.0] Cut to an extreme close-up on ba_tu's right hand and the letter, eye level, static camera — the gnarled fingers hover over the paper for two seconds, touch the creased edge without picking it up, then press flat against the warm floorboards; wood smoke drifts across the edge of the frame, breathing slows to a living rhythm.

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored to the architecture; characters move only where the action says they move.
Do not generate subtitles, dialogue text, titles, timestamps, or written text anywhere in the video. Do not render duplicate characters or extra props.
```
Timing: 12 + 14 + 10 = 36 syllables (grammar §7: 35–70 for 30 s); 5 shots across 3 acts (Act I: 0–5.5s, Act II: 5.5–17.5s, Act III: 17.5–30s); each shot ≥ 5.5s; terminal settle 2.5s. Speech ≈ 35 %.

---

### 🎬 DEMO 4B: 30 s CHAINED (ALTERNATIVE FALLBACK ONLY)

Use only when the user explicitly requests chaining or reports that the generator cannot hold 30 s in a single prompt.
- **Part 1 (00:00–00:10)** — Act I, arrival and trigger: a complete Code Block 1 like Demo 1, ending on momentum rather than a full settle.
- **Part 2 (00:00–00:10)** — Act II, the exchange where power shifts: a complete Code Block 1 like Demo 2. Its `[subject]` and `[PROP]` blocks restate the exact positions and prop states from Part 1's Code Block 2; nothing refers to "the previous scene" (Gate 3I).
- **Part 3 (00:00–00:10)** — Act III, the reveal or decision, closing on a living settle ≥ 2 s.
- Keep the camera on the same side of the axis across the three parts unless a part crosses it with a visible move.

---

## 🛡️ § 6. THE 9-POINT CORE PRE-FLIGHT LINTER (SUBSET OF THE DIRECTOR.md 13-POINT LINTER)

Before approving any 10-second prompt, the Director MUST verify all 9 points of the Pre-Flight Linter:
1. **[ ] Zero Freeze Holds & Organic Motion**: STRICTLY BAN `freeze hold` or `zero-velocity`. Maintain continuous natural motion throughout the 10s clip without forcing repetitive boilerplate settle text.
2. **[ ] Zero Camera Hardware & Lighting Jargon Gate**: STRICTLY BAN `24fps`, `18mm`, `35mm`, `50mm`, `f/1.4`, `ISO`, `Arri Alexa`, `Panavision`, and raw Kelvin numbers (`2800K`, `3200K`). Translate into evocative sensory optical prose.
3. **[ ] Zero Clothing & Demographic Age in Initial State (Mode B Gate)**: Wardrobe 100% governed by the 16:9 Model Sheet. Strictly zero numerical age/gender descriptors in prompt initial state (belongs exclusively to voice directing parentheticals).
4. **[ ] Two-Tier Completeness Gate**: Tier 1 Director's Audit Card (with explicit technical labels) MUST precede Tier 2 Machine Execution Blocks (Code Block 1 Prompt + Code Block 2 Handover).
5. **[ ] Anti-Math Vector Law Gate (Gate 3H)**: STRICTLY BAN `X:`, `Y:`, `Z:` coordinates and raw meter numbers `(X:+0.8m, Y:0.0m, Z:2.0m)` in Code Block 1. Pure natural prose only.
6. **[ ] Stateless Prompt Law Gate (Gate 3I)**: STRICTLY BAN `from Scene XX` or cross-scene dependencies in Code Block 1. Diffusion engines render each 10s clip statelessly; all action sequences within the clip must be self-contained.
7. **[ ] Single Instance Lock & Minimal Prop Interaction Gate**: Exactly ONE physical instance of any interactive prop exists (`— the only [prop] in frame`), limited to at most 1 interaction per clip with 1 fixed noun phrase and zero surface-clearance clutter (`leaving the spot clear`). Heavy fixtures (Pine Crib, Bed, Table) declared in `[context]:` and permanently anchored to their room landmarks with zero teleportation.
8. **[ ] The 10 Natural AI Video Action Laws Gate (Anti-Overload Law)**: Strictly `≤ 2` moving characters per phase; 1 concrete observable verb per active character chained sequentially with `then`; speaking character performs at most 1 simple gesture; supporting characters hold a clean static state (`sits still with eyes fixed on...`); story-critical action front-loaded immediately after `—`.
9. **[ ] Dialogue Word Count Hard Cap (Gate 4B) & 10s Shot Allocation**: STRICTLY adhere to the 10s Shot Word Budget: Single-speaker solo shots are budgeted at 14–24 words (Sitcom/Slice-of-Life, hard cap ≤ 32w; craft target 8–14w; Microdrama ≤ 12w) or 8–14 words (Psychological Drama, cap ≤ 20w). Two-speaker shots are strictly limited to rapid volleys of 5–10 words each (hard cap ≤ 15 words per speaker, total ≤ 32w). If any speaker exceeds 15 words, the shot MUST be split into separate solo shots.

## 🏛️ PART VI: MASTER PER-EPISODE PRODUCTION SPECIFICATION (`tap-X.html`) & QUALITY GATES

## 🏛️ 1. ARCHITECTURAL PHILOSOPHY: ZERO DRIFT & SINGLE SOURCE OF TRUTH (SSOT)

A per-episode production file (`tap-X.html`) is **NEVER** an independent creative sandbox where an agent or screenwriter re-imagines the plot, invents new actions, or alters dialogue. It is an **exact engineering translation** of the pre-production blueprint locked inside `setting.html`.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                             CANONICAL INHERITANCE PIPELINE                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│  [SOURCE OF TRUTH: setting.html]                                                            │
│  • Section 5: Scene-by-Scene Production Roadmap (12 Scenes / Episode)                       │
│  • Section 1D: Master Dialogue Architecture & 5 Timeline Production Templates               │
│  • Section 2 & 3: Mode B Character Anchors (No Clothing)                                    │
│  • Section 4A: Mode B Prop Anchors (Stability & Bifurcation Laws)                           │
│  • Section 4B: Mode B Location Anchors (Lighting Atmosphere & Environmental Medium)                      │
│                                      │                                                      │
│                                      ▼ (Programmatic 1:1 Ingestion)                         │
│  [EXECUTION FILE: tap-X.html]                                                               │
│  • Card UI: Verbatim Story Beat, Dramatic Intent, Bridge, Dialogue Breakdown                │
│  • Code Block 1: Video Prompt, 10s default (Timed Phases, In-Line Dialogue, Zero §6b)       │
│  • Handover State: Exact Spatial, Posture, Lighting coordinate lock at 00:10.0              │
│                                      │                                                      │
│                                      ▼ (Automated Audit)                                    │
│  [5-GATE PRE-DELIVERY AUDIT PROTOCOL] ➔ PASS (0 Errors) ➔ User Delivery                     │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## ⚖️ 2. THE 5 IMMUTABLE LAWS OF EPISODE PRODUCTION

### Law 1: Verbatim Roadmap Inheritance (Zero Drift)
The following fields in `tap-X.html` MUST match Section 5 of `setting.html` **verbatim (word-for-word, 100% character identity)**:
1. **Scene Title (`title`):** Exact string as registered in Roadmap.
2. **Diurnal Time & Lighting:** Exact 12-Hour AM/PM notation and natural lighting progression (e.g. `05:50 PM Hoàng Hôn Tắt Nắng (Sunset Edge) • cool daylight U Tối ➔ cool daylight Ánh Vuốt Thép`).
3. **Cast, Environment, Props, Typology:** Exact canonical names (`🐉 Faelen Bramble (A1)`, `ENV-02`, `PROP-01`, etc.).
4. **Diễn Biến Cốt Truyện Bám Sát Trục Chính (Story Beat & Causality):** Exact Vietnamese text. No rewriting, rephrasing, or condensing.
5. **Ý Đồ Kịch Tính & Cung Bậc Cảm Xúc (Dramatic Intent):** Exact Vietnamese text.
6. **Mắt Xích Kế Thừa & Cầu Nối Động Năng (Kinetic Continuity Bridge):** Exact Vietnamese text.

---

### Law 2: Multi-Turn Dialogue Parity & The Universal Interaction Suite (Roadmap-to-Execution Parity)
In high-end cinematic video generation, dialogue and interaction are governed by the **Universal Multi-Genre Interaction Meta-Framework** (SSOT: [`1-narrative-screenplay-architecture.md`](file:///d:/Project/Sven/engine/references/1-narrative-screenplay-architecture.md)). **Dialogue Parity does NOT mean forcing every scene into a rigid drama ping-pong.** It mandates **100% 1:1 Roadmap-to-Execution Parity** between Section 5 Roadmap of `setting.html` and Episode Execution (`tap-X.html`), seamlessly adapting across **Drama, Romance, Comedy, Action/Sci-Fi, Horror, Mystery, Fantasy, and Animation**.

#### 1. The 8 Universal Interaction Geometries (+ Model 0) Across All Genres:
* **Group 1: Multi-Speaker Volleys (Pure Track B: Multi-Shot Montage trục 180°)**:
  - **Model 1: Symmetrical Binary Exchange (5s – 4s – 1s • 2 Volleys • ~16–18w)**:
    - *Drama*: Duel of Truths (Ultimatum ➔ Retort ➔ Stunned shock).
    - *Romance*: Flirtatious Banter (Teasing poke ➔ Melted witty retort ➔ Shy blush).
    - *Comedy*: Setup ➔ Punchline / Sarcastic Deadpan.
    - *Sci-Fi / Tactical*: Status Check ➔ Direct Order.
  - **Model 1B: Rapid-Fire Staccato Volleys (2s – 2s – 2s – 3s – 1s • 4 Volleys • ~16–18w)**:
    - *Drama*: High-Velocity Stichomythia (Verbal swordplay).
    - *Rom-Com*: Cute Rapid Bickering (Tung hứng chọc ghẹo té tát).
    - *Action / War*: Adrenaline Combat Callouts (Tactical team directives under fire).
    - *Comedy*: Escalating Absurdity Chain.
  - **Model 2: Group / Ensemble Exchange (3s – 3s – 3s – 1s • 3 Volleys • ~15–18w)**:
    - *Drama*: Council / Mob Accusation ➔ Hero Defiant Defense.
    - *Sitcom / Comedy*: Friends gang-up mockery ➔ Protagonist indignance ➔ Group laughter.
    - *Heist / Team*: Hacker ➔ Driver ➔ Leader "Execute!"
    - *Family / Animation*: Excited children ➔ Warm parent guidance.
  - **Model 7: Kinetic Interruption / Decapitation (3.5s – 1.5s – 4.0s – 1.0s • ~12–15w)**:
    - *Drama*: Arrogant threat cut short mid-syllable by dagger slammed through deed.
    - *Romance*: Nervous babble gently silenced by an unexpected tender kiss or hand placed on lips.
    - *Comedy*: Pompous boast abruptly interrupted by slipping on a floor or a door opening.
    - *Action*: Tactical radio sentence severed by an incoming blast shockwave.
* **Group 2: Asymmetrical & Perspective Geometries (Track A or Track B)**:
  - **Model 3: Solo Lead & Somatic Settle (4s – 5s – 1s • 1 Volley • ~7–9w)**:
    - *Drama*: Authoritarian Verdict / Sentence (Listener absorbs shock in silence).
    - *Romance*: Vulnerable Romantic Confession (Speaker confesses deep love ➔ Listener's breath catches, tear forms, sweet stunned silence).
    - *Comedy*: Speechless Dumbfounded Beat (Absurd claim ➔ Counterpart stares deadpan, takes off glasses).
    - *Horror*: Whispered Question into Dark Basement ➔ Heavy creeping silence.
  - **Model 6: Proximity Whisper & Intimate Sibilance (4s – 4.5s – 1.5s • 1.2–1.5 WPS • ~10–13w)**:
    - *Romance*: Pillow-talk intimacy, promises whispered under an umbrella in the rain.
    - *Horror / Survival*: Hiding in a closet while monster stalks past outside.
    - *Drama*: Conspiratorial shadow plotting, poison trade.
    - *Mystery*: Confidential archive discovery in hushed tones.
  - **Model 8: Subjective P.O.V. Direct Address (4.5s – 4.5s – 1.0s • ~14–17w)**:
    - *Romance*: Lover looking directly down camera lens with fond adoration, hand reaching out.
    - *Action*: Fallen soldier looks up as teammate reaches down to pull them up.
    - *Comedy*: Direct 4th-wall address to audience (*Fleabag*, *The Office*).
    - *Drama*: Interrogator leaning down directly into lens axis.
* **Group 3: Sonic-Decoupled & External Audio (Track A Single-Shot Continuous Dominance)**:
  - **Model 4: Internal Monologue / Voice of Thought (V.O. • 12–16w • Lips 100% Sealed)**:
    - *Romance*: Secret unspoken longing and heart flutter.
    - *Noir / Mystery*: Gritty detective deduction on rain-slicked street.
    - *Fantasy*: Ancient telepathic voice / ancestral communion.
    - *Drama*: Hidden strategic calculations behind a polite smile.
  - **Model 5: Off-Screen Authority / Ambient Comms (O.S. • 14–18w)**:
    - *Sci-Fi*: Ship AI / Mission Control emergency broadcast.
    - *Slice-of-Life*: Parent calling dinner from downstairs / train announcement.
    - *Action*: Police megaphone surround order.
    - *Drama*: Courtroom gavel or herald summons outside closed doors.
* **Baseline Exception: Pure Physical & Atmospheric Eloquence**:
  - **Model 0: Pure Action Kinetics & Silent Settle (0 Words • 100% Body Language)**:
    - *Action*: High-octane martial arts clash, dodge, and strike.
    - *Romance*: The Electric Gaze (Two lovers' eyes locking across a ballroom in silence).
    - *Horror*: Paralyzed dread watching doorknob turn.
    - *Comedy*: Classic silent physical slapstick gag.

#### 2. The 4 Invariant Dialogue Parity Standards:
1. **UI Card Parity (`.dialogue-breakdown-box`)**:
   - Number of Turn Cards MUST exactly match the number of volleys in the chosen Model (1 Card for Model 3/4; 2 Cards for Model 1/6; 3 Cards for Model 2/7; 4 Cards for Model 1B; Zero Dialogue Banner for Model 0).
   - Each Turn Card displays: Speaker Tag, English Spoken Line, Vietsub Translation, and 4-in-1 Acting Direction.
   - Dynamic Timeline Progression: Each Turn Card displays its natural temporal window with seamless kinetic continuation to 00:10.0 (strictly BAN rigid '00:08.5' cutoff dogma).
2. **Prompt Injection Parity (Code Block 1 Omni Flash Prompt)**:
   - Every spoken volley MUST have its own dedicated, non-overlapping timestamp.
    - Standard In-Line 4-in-1 Directing Parenthetical Syntax (Bám Sát 100% Casting Section 3):
      `{Speaker} {speech_action_verb} : “{Spoken Line}” (Voice of a [Age]-year-old [Gender] from [Region / Dialect]; [Lip-sync & facial micro-expression]; [Tactile gesture / prop interaction]; [Gaze & Subtext / Emotional intent])`
      *Exemplar:* `my_duyen says : “ A bamboo cradle, a bolster for the back, and a soft bed-edge to cradle you gently, Mama! ” (Voice of a 24-year-old woman from Southern Vietnam; lips parted in a sweet, affectionate smile; slender fingers caressing the cotton fabric; gentle brown eyes conveying a tender plea for reconciliation—and filial devotion.)`
   - For Model 4 (V.O.): Explicitly declare `lips remain 100% firmly sealed, zero mouth movement, internal voiceover echoes in mind`.
3. **The Words-Per-Second (WPS) Physics Law**:
   - Speech rates and clip density: grammar §2 and §7 (authoritative). The 1.1–2.4 WPS table in Pillar 1 describes English emotional cadence including pauses.
   - Clip density is governed by [`0b-temporal-camera-grammar.md`](file:///d:/Project/Sven/engine/references/0b-temporal-camera-grammar.md) §7 and Gate 4B: Single-speaker solo shots allow 14–24 words (Sitcom/Slice-of-Life, hard cap ≤ 32w; craft target 8–14w; speech share up to 75% of the 10s clip) or 8–14 words (Psychological Drama, cap ≤ 20w). Two-shot volleys are strictly ≤ 15 words per speaker (total ≤ 32w). Buffer law preserves 0.5–1.0s at head and 0.5–1.5s at tail.
   - Zero micro-snippets (< 3 words) unless intentional Model 7 interruption.
4. **The Prop-Speech Tactile Locking Law & Living Settle**:
   - Peak spoken keywords synchronize with observable physical actions (tender touch, coffee spill, lever switch, ledger slam).
   - Dynamic Kinetic Flow & Organic Resolution: Dialogue timing is motivated by scene beats. When spoken words finish, facial subtext and physical motion flow naturally through continuous biological respiration and camera momentum right to 00:10.0, strictly zero frozen frames and zero artificial cutoff dogmas.

---

### Law 3: Mode B Asset Anchoring & Lore-Bound Asset Naming Mandate (Section 2, 4A, 4B)
* **Subject Declarations in `[subject]:` (The Sovereign Subject Formula & Initial Prop State Bifurcation Law):**
  - In `[subject]:`, declare every participating character using the Sovereign Subject Formula: `{ho_ten} [100% Appearance, attire, and facial features Refer to image X], {initial spatial anchor to architectural fixture}, {initial physical posture}, {hands free of props if unheld at 0.0s OR explicit t=0.0s hand-grip if already holding a prop at 0.0s}, {eyeline toward a character or landmark} — the only {ho_ten} in frame.`
  - *Function at 00:00.0:* Establishes identity lock, zero-frame architectural grounding (at the exact same landmark within arm's reach when 2 characters physically interact), initial physical posture and hand state, and the mandatory negative anti-duplication seal.
  - *The State-Delta Character Directing Protocol in Timeline Shots:* While `[subject]:` locks the initial position, posture, and hand state at 00:00.0, timeline shots (`[00:00–00:XX]`) direct ONLY the state transition: (1) 1 Concrete Action Verb, `then` (2) Sequential Speaker, `as` (3) Supporting character's facial shift or static watch — NEVER repeating `[subject]:` positions and NEVER contradicting `[subject]:` postures.
  - *Negative Rule 1 (Zero-Costume Law):* **NEVER describe clothing or costumes in prompt lines** (costume is 100% locked by the 16:9 Model Sheet).
  - *Negative Rule 2 (Zero-Age Law):* **NEVER describe age or numerical ages in visual narrative prose** (age is 100% locked by the Model Sheet; numeric age appears ONLY inside voice parentheticals).
* **Prop Declarations in `[PROP]:` (The Two-Tier Prop Architecture & Production Velocity Law):**
  - In `[PROP]:`, list one handheld item per line, each declaring its $t=0.0\text{s}$ state (resting on a surface when unheld at $0.0\text{s}$, or held in `{ho_ten}`'s hands when already held at $0.0\text{s}$, synchronized with `[subject]:`). Furniture and fixtures stay in `[context]:`. Enforce Two Tiers:
    * **Tier 1 (Soul & Catalyst Hero Props — Max 1–2 per series)**: Objects carrying the narrative soul or activating the twist. MUST have a 16:9 four-view Model Sheet in Section 4A and bind with `[100% Refer to image prop_X_4view.jpg]`.
    * **Tier 2 (Everyday Ambient & Common Hand Props)**: Ordinary items (ceramic spoons, plastic stools, tea cups, brooms, ledgers). **STRICTLY ZERO IMAGE MODEL SHEETS** (saving massive pre-production time). Handled 100% via rich, unambiguous physical tactile descriptions inside `[PROP]:` without image tags.
  * **Prop Naming Formula (Tier 1 Hero Props):** `[CANONICAL-ID: PROP-XX] + [Owner / Clan / Origin] + [Unique Physical Trait] + [Object Type]` *(Registry format for `setting.html` only; inside Code Block 1 write the natural-English name without the canonical ID or underscores, e.g. `Kaya bone dagger`.)*
    - *Examples:* `PROP-01: Dao găm Kaya (The Kaya Bone Dagger)`, `PROP-02: Vò nước linh tuyền Bramble (The Bramble Glazed Spring-Urn)`, `PROP-03: Chuông bạc trừ tà Maya (Maya's Silver Warding Bell)`, `PROP-04: Móng vuốt báo xám Korr (Korr's Grey-Leopard Talons)`.
  * *Negative Rule:* **STRICTLY BANNED: generic names for Tier 1 Props** like "a water jar", "a dagger", "an ancient bowl", "a stick", "a sword".
* **Environment Descriptions (The Lore-Bound Canonical ID Mandate):** ALWAYS prefix with the registered Canonical ID and a specific mythological/world-tied proper noun.
  * **Environment Naming Formula:** `[CANONICAL-ID: ENV-XX] + [Legendary Region / Clan / Realm] + [3D Spatial/Physical Landmark] + [Setting Type]` *(Registry format only; in Code Block 1 use the natural-English location name, e.g. `Alaka whispering garden`.)*
    - *Examples:* `ENV-01: Khu vườn Alaka (The Alaka Whispering Garden)`, `ENV-02: Tổ tùng la ngàn năm Faelen (Faelen's Ancient Cedar Canopy Nest)`, `ENV-03: Đàn tế đá rêu phong Eldoria (The Eldoria Moss-Stone Altar)`, `ENV-04: Hẻm đá chênh vênh Cự Thần (The Titan-Spire Wind Chasm)`.
  * *Negative Rule:* **STRICTLY BANNED: generic phrases** like "the village", "a room", "the forest", "the market", "crossroads".
* **The Dual Operational Pillars of Lore-Bound Naming:**
  1. **The Human Asset-Matching Pillar (UX):** The user generates reference sheets named `PROP-01_Dao_Gam_Kaya.png` or `ENV-01_Khu_Vuon_Alaka.png`. Tying every asset directly to a character/location name guarantees instantaneous, zero-confusion drag-and-drop into image-to-video slots (Kling, Sora, Runway Gen-3).
  2. **The AI Latent Semantic Binding Pillar:** Generic nouns cause diffusion models to pull random internet noise. Unique proper nouns bound to lore anchor the latent semantic vectors, preventing geometry and texture drift across multi-shot sequences.

---

### Law 4: Absolute Pronoun Ban (§6b of `4-ai-video-prompt-compiler.md`)
In generative AI video models, third-person pronouns (`he, she, it, his, her, its, him, they, their, them`) cause acute subject ambiguity, cross-character body morphing, and limb duplication.
* **PROHIBITION:** Zero third-person pronouns in action prose across every scene of the episode.
* **MANDATE:** Always repeat the proper character name (e.g. `Faelen's neck`, `Korr's steel claws`, `Pip's brass tooth`).

---

### Law 5: Complete Handover State Continuity (§4 Final State Gate)
At timestamp `00:10.0`, every scene must deliver an explicit `[HANDOVER STATE AT 00:10.0]` capturing:
1. Spatial coordinate of all subjects at frame-end.
2. Exact physical resting posture and eye gaze vector (living settle, zero frozen frames).
3. Prop position and contact state.
4. Lighting atmosphere, natural color quality, and key source direction.
5. Camera angle, shot scale, and cinematic framing.
This ensures the opening frame `00:00.0` of Scene N+1 connects with **zero spatial or kinetic jump-cuts**.

---

### Law 6: 3D Spatial Vector & Translation to Cinematic Natural Prose (`3-cinematography-3d-staging.md`)
In physical action, collision, and falling sequences, the prompt MUST adhere to the **Vector-to-Plane Law** and the **Translation Law**:
1. **Vertical Descent ($-Y$ Vector):** Catching surfaces (spiderwebs, nets, trampolines, awnings, ground) MUST be explicitly anchored to the **Horizontal Plane ($X-Z$)** (e.g. `horizontal circular web hammock spanning flat across the open chasm directly beneath descent path`). BANNED: Placing a vertical catching plane parallel to a vertical fall.
2. **5-Step Mechanical Deformation:** Explicitly depict Contact ➔ Funnel Sag ➔ Radial Harmonic Vibration ➔ Viscous Adhesive Bonding ➔ Rebound Equilibrium.
3. **Camera Descent Setups:** Employ Low-Angle Under-Mesh, God's-Eye Nadir, or Synchronized Relative Velocity to prevent subjects from exiting frame in 0.2s.
4. **THE TRANSLATION LAW (MANDATORY PURGE OF RAW MATH & KELVIN IN OUTPUT PROMPTS):**
   * *Diffusion models (Kling, Runway, Sora) have NO math or physics engine.* Text encoders (T5, CLIP) confuse Kelvin numbers (`cool daylight`) with 8K resolution, and treat vectors (`[+X, -Y]`) as junk noise.
   * **STRICTLY BANNED in video prompts:** Raw vectors (`[+X, -Y, +Z]`), velocity formulas (`V_cam = -8m/s`, `at 15m/s`), setup tags (`Setup A/C`), Kelvin numbers (`cool daylight`, `amber warmth`), shutter angles (`45-deg`), and audio Hz (`[140Hz]`).
   * **MANDATORY:** Always translate into **Vivid, Observable Cinematic Natural Prose** (e.g. `Camera dollies backward rapidly at full sprint speed, staying locked at eye level`, `cool icy-blue moonlight`, `warm amber lantern glow`).

---

### Law 7: Minor Protection (canonical spec: §[10d])
Every character under 18 follows the Minor Protection Protocol in §[10d]: truthful age and age band, identity by approved `ho_ten` + reference image, zero sexualization, zero violence or danger involving a minor, band-based actions, and protective staging. If a platform blocks a scene that involves a minor, restage it (Option B, or frame only the adults) or cut it. Never relabel, rename, or disguise the minor to get past the block.
1. **Fixture integration**: the crib or bed holding a sleeping Band I/II character is furniture described in `[context]:` (e.g. `a light pine wood crib placed firmly beside the queen bed with a firm flat organic cotton mattress`). Never declare it in `[PROP]:` and never generate a separate crib prop sheet.
2. **Adult age anchor (true adults only)**: a character who really is 18 or older may be anchored with non-numeric adult terms (`young woman`, `adult craftsman`, `young adult weaver`) to avoid ambiguity. Never apply adult terms to a character under 18. Numeric age stays inside the voice parenthetical (Gate 3A).

---

### Law 8: The Minimalist Twist-Catalyst Prop Law & Human Emotion Primacy
1. **Absolute Ban on Localized Prop Titles & Clutter:**
   - STRICTLY FORBIDDEN: Titling scenes after props (e.g. "Hũ Bột Rỗng Đáy", "Mảnh Sứ Men Lam"). Scene titles and dramatic intents MUST reflect **Human Drama, Psychological States, and Interpersonal Conflicts** (e.g. "Bản Năng Sinh Tồn", "Cạm Bẫy Nợ Nần", "Lời Thề Trong Bóng Tối").
   - STRICTLY FORBIDDEN: Forcing an "Đạo Cụ Linh Hồn" or exhaustive prop inventory into episode meta headers. Props occupy strictly **≤ 5% to 10%** of narrative focus.
2. **Terminal Emotional Resonance (Human Drama over Mechanical Buffers):**
   - The final beat of the scene belongs to genuine dramatic impact and character reaction, without forcing an artificial 3-shot structure or mechanical silence buffer.
   - The camera lens MUST lock onto the **Human Face**: pupil contraction, tight jaw, unshed tear freezing on the eyelid, or heavy ragged breathing.
   - **STRICTLY FORBIDDEN:** Defaulting to inanimate broken objects (shattered bowls, falling coins, bouncing shards) replacing the emotional reaction of the human characters.
3. **Restricted Foregrounding at Twist Points Only:**
   - In all normal scenes, everyday objects remain subtle background texture.
   - A registered Master Prop is ONLY brought to the foreground optical center when executing an authorized **Twist Point** (revealing hidden evidence, exposing a forgery, or sealing a covenant).

---

## 🛡️ 3. THE AUTOMATED PRE-DELIVERY AUDIT SUITE (`episode_audit_suite.py`)

> The authoritative gate code is `engine/episode_audit_suite.py`. Code snippets in this section are historical illustrations; some still parse the retired `△` syntax.

Before delivering ANY episode file (`tap-X.html`) to the user, the agent MUST run the automated audit suite:
`python engine/episode_audit_suite.py output/<project-slug>/tap-X.html`
Delivery is STRICTLY BLOCKED unless all gates pass with exit code 0.

### Complete Gate Architecture:
- **Gate 1A / 1B: DOM Integrity**: balanced `<div>` and `<pre>` tags.
- **Gate 2: Scene Count & Clip Duration**: every scene states its clip duration (10s default; 15s / 30s on request); scene count vs `project_rules.json` → `episode_scenes` (warning).
- **Gate 2B: Mandatory 12-Row Story Spine Card Lock**: verifies `<div id="story-spine">` is present before scenes with core rows `[QUESTION]`, `[TRUTH]`, `[LOOPS]`, `[PREDICT]` (and warns in `W9` if any of the 12 canonical depth rows are missing).
- **Gate 3: Prompt Quality & Safety Enforcement** (one `p-XX` prompt per scene):
  - *Gate 3A*: No numeric age in visual prose (voice parenthetical exempt).
  - *Gate 3B*: No freeze frames / freeze holds.
  - *Gate 3C*: Absolute pronoun ban (`he`, `she`, `his`, `her`, `him`, `they`, `their`, `them`, `herself`, `himself`, `themselves`).
  - *Gate 3D*: No hardware or Kelvin jargon (`24fps`, `35mm`, `f/1.4`, `ARRI`, Kelvin numbers).
  - *Gate 3E*: No costume words in Mode B prose (wardrobe is locked by the model sheet).
  - *Gate 3F*: **Minor Protection Protocol** (§[10d]): no generic minor nouns or retired aliases in visual prose; for prompts naming a `minor_characters` entry, no sexual, body-focused, or violence lexicon and no adult label on the minor.
  - *Gate 3G*: Mandatory Master Prompt Prefix (`Master-level cinematography...`).
  - *Gate 3H*: **Total Mathematical Purge Law**: zero Cartesian coordinates `[XYZ]:\s*[-+]?\d`, zero degree/metric math, zero frame-edge tokens (`screen-left/right`, `frame-left/right`), and zero raw `[timeline]:` tags in Code Block 1.
  - *Gate 3I*: **Stateless Prompt Law**: zero cross-scene references (`from Scene XX`) in Code Block 1.
  - *Gate 3J–3L*: 3-block labels (`[context]:` / `[subject]:` / `[PROP]:`), Sovereign 5-part `[subject]:` and Two-Tier `[PROP]:` completeness (`Gate 3K`), and blank-line spacing (`Gate 3L`).
  - *Gate 3M–3N*: ≥ 2 contiguous phases from 00:00 to a 10 / 15 / 30s end; standard stability + negative clause.
  - *Gate 3O–3Q*: zero dead air; zero literal placeholder tokens; zero dangling `Focus on [name].`
  - *Gate 3R*: **Single Focal Action Law & Action Compounding Purge**: bans chaining sequential macro-actions or prop-juggling inside a single phase.
  - *Gate 3S*: **Optical Ray-Tracing, Scale, Angle & `Cut to` Cross-Reference Gate (`3S-1` to `3S-6`)**: enforces scale vs. angle terminology (`3S-1`), canonical `—` separator (`3S-2`), zero OTS back-of-head lip-sync (`3S-3`), zero behind-the-lens optical inversions / tight-scale overcrowding / undeclared timeline subjects (`3S-4`), standing-vs-floor vertical angle accuracy (`3S-5`), and zero unmotivated jump cuts (`3S-6`).
- **Gate 4: Dialogue & Continuity**:
  - *Gate 4*: dialogue ↔ prompt verbatim parity where lines exist.
  - *Gate 4B*: **Dialogue Word Count Hard Cap**: single speaker ≤ 32 words; two-shot ≤ 15 words per speaker (total ≤ 32). Craft target 8–14 words (Microdrama ≤ 12).
  - *Gate 4C* (warning): line causality. *Gate 4D–4F*: project rules (`kinship_ladder`, `meal_terms`, `bookish_terms`) when defined.
  - *Gate 4G*: speech-action verb on every spoken line. *Gate 4H*: Code Block 2 handover + Kinetic Momentum Bridge per scene.
- **Gate 5: Copy UX**: copy buttons, copy-all, toast.
- **Creative Review Warnings (`W1–W11`)**: non-blocking checks for repeated phase splits (`W1`), Track A-Locked quota (`W2`), voice mode runs (`W3`), reply opener monotony (`W4`), solo line runs (`W5`), speech timing fit (`W6`), lip-sync unsafe camera moves (`W8`), 12-row Story Spine & emotion-label check (`W9`), plot prediction ledger (`W10`), and single-location stagnation (`W11`).

## § [10c] 12 COMMON ERRORS (Cross-cutting Error Check Framework)

| # | Error Name | Identifying Signs | How to Fix |
|---|---|---|---|
| 12.1 | Profile-Action Conflict | `[Subject]` locks hands but Shot needs to hold prop | Remove hand-lock from `[Subject]`, use neutral upper-body description |
| 12.2 | Causal Motivation Gap | Character changes mind/action without observable stimulus before it | Add 1 physical trigger detail before the change-of-mind action |
| 12.3 | Spatial Overcrowding | ≥ 2 characters but no architectural anchors, relative distance, or foreground/background declared | Anchor each character to architecture and to each other (`ho_ten_A behind the counter`, `ho_ten_B across the aisle from ho_ten_A`); record screen direction in the Audit Card only |
| 12.4 | Unmotivated Camera Jump | Jump from ECU to Wide with no dramatic reason | Add 1 intermediate Shot or explain reason for scale change |
| 12.5 | Sound-Shot Mismatch | Sound line doesn't match action/timing of Shot | Rearrange Sound line chronologically to match each Shot |
| 12.6 | Identity Loss at Close-up | Close-up omits identifying detail (costume color, scar, accessory) | Restate ≥ 1 clear identifying detail in opening sentence of Shot |
| 12.7 | Number/Pronoun Agreement | Plural used but subject is singular, or `he/she/it` instead of name | Replace all personal pronouns with proper names in actual output |
| 12.8 | Missing Scene-Specific Safety | Scene has risky characteristics (crowd, water, close-up hand) but lacks appropriate `Do not...` | Add Group C phrases from Negative Prompt table (§ Negative Prompt Master List) |
| 12.9 | Total Duration Mismatch | Total seconds of Shots ≠ duration stated at Scene head | Re-add and fix the most flexible Shot (usually the final one) |
| 12.10 | Solo-Frame Strike Bug ("Punching the Air") | Directing Character A to hit, slap, knock a prop from, or touch Character B inside a 1-person `CU / MCU`, or anchoring them at two separate landmarks | Anchor both at the **same landmark within arm's reach**, and frame **both striker and target** (`Low-angle medium shot framing A towering over B`, `M2S`, or `Contact Close-Up framing A's boot on B's hand`) |
| 12.11 | Crowd/Witness Artifact | Multiple clear crowd faces, or perpetrator + witness in same Shot | Apply "1 + Blurred Background"; split Witness into separate Shot |
| 12.1b | Motion-in-Static Conflict | Single completion verb (`snaps`, `explodes`) with no intermediate state | Replace with participle/suspended state (see § [3.4c]) |
| **D.1** | **Dialogue Over-Explicit** | Dialogue states emotion directly (`"I am afraid"`, `"I hate you"`) | Replace with indirect dialogue + body betraying subtext (§D.0, §D.3) |
| **D.2** | **Dialogue Causality Break** | Next dialogue line does not pick up keyword from previous line | Apply Logical Causality Chain — Keyword Handoff (§D.2) |
| **D.3** | **Camera-Speaker Mismatch** | Camera does not cut to the speaker | Apply Camera-Speaker Binding §D.5 Rule 1 |
| **D.4** | **Lip-sync Camera Violation** | A lip-synced line is spoken while a crane, orbit, arc, whip, or crash zoom is traveling | Place the line before the move or after it lands (grammar §5), or use a static frame / slow push-in |
| **12.12** | **Minor Policy Block** | Prompt blocked for 'harmful content related to minors' | **Adult character**: remove ambiguous nouns (`girl`, `boy`, `kid`) and anchor adult status (`young woman`, `adult craftsman`). **Under-18 character**: do NOT relabel or rephrase to evade; check the scene against §[10d], then restage (Option B or adults-only framing) or cut the beat. Remove wet/torn clothing and vulnerable postures. |


---

## § [10d] MINOR PROTECTION PROTOCOL — UNDER-18 CHARACTERS (GATE 3F + SETTING GATE 3B)

> **Purpose.** Protect every character under 18 (children and teenagers) and the audience. This protocol governs what we write. It is never a technique for slipping content past a platform's safety system. If a platform blocks a scene that involves a minor, restage it (Option B: off-screen, or frame only the adults) or cut it. Never relabel, rename, or disguise the minor to bypass the block.

### 1. Registration & Truthful Age (Hard Constraint)
- Every under-18 character is registered in `setting.html` with true age and age band, and the `ho_ten` is listed in `output/<project>/project_rules.json` → `minor_characters` (this activates the Gate 3F minor checks).
- Age bands: **Band I — Infant/Toddler (0–3)** · **Band II — Child (4–12)** · **Band III — Teen (13–17)**.
- Never relabel a minor as an adult (`adult`, `young woman`, `young man`, `aged 18`) and never move a minor's age up or down to pass a filter.
- A character who needs romance, sexuality, graphic violence, substance use, or another adult storyline is written as an adult (18+) from Stage 0, in an adult setting (university, workplace). Never dress an "18-year-old" in a school uniform as a stand-in for a minor.
- Retired child aliases go in `project_rules.json` → `minor_character_names`; Gate 3F blocks them.

### 2. Identity in Prompts
- A minor is referenced only by approved `ho_ten` + reference image, like every character: `{minor_ho_ten} [100% Appearance, attire, and facial features Refer to image {minor_ho_ten}_4view.jpg]`.
- Generic nouns (`child`, `kid`, `boy`, `girl`, `teen`, `baby`) stay out of visual prose because they spawn unanchored duplicate figures (Gate 3C/3F), not to hide the age.
- Visual prose carries no numeric age (Gate 3A). The voice parenthetical states the true age: `（Voice of a 14-year-old girl from Southern Vietnam; ...）`.

### 3. Model Sheets for Characters (`setting.html` Section 3: Adult Human, Minor Mẫu 0B, Non-Human Mẫu 3)
- **Style**: neutral casting / continuity reference. Banned: fashion, editorial, commercial, beauty, or glamour photography; beauty lighting.
- **Allowed descriptors (including Healthy Child/Teen Natural Skin Complexion)**: true age, height in cm, a build word (`small`, `average`, `stocky`), face shape, **healthy age-appropriate natural skin complexion** (`healthy warm-ivory natural skin`, `smooth fair child complexion`, `healthy sun-kissed tan skin`, `soft natural rosy cheeks`, `faint childhood freckles`, `healthy natural pink lips`), eyes, hair, expression, age-appropriate wardrobe.
- **Banned descriptors (Adult Glamour/Cosmetic Lexicon)**: physique, figure, curves, toned, slender, hourglass; adult skin sensuality (`dewy`, `glowing skin`, `porcelain`, `luminous skin`, `micro-pores`); adult makeup (`lipstick`, `eyeliner`, `mascara`); `seductive`, `sultry`, `alluring`, `sexy`, `attractive`.
- **Wardrobe**: fully covering and age-appropriate. Banned: form-fitting, skin-tight, cropped, mini, low-cut, sheer, see-through, bodysuit, swimwear, underwear, sleepwear as a sheet outfit.
- **Layout**: three full-length views WITH the head (front, 90° side, back) plus a head-and-shoulders portrait. No headless neck-down crops, no chest-up glamour portrait.

### 4. Content Boundaries (Screenplay & Prompts)
| Area | Never | Allowed |
|---|---|---|
| Sexual / romantic | Any sexual content or innuendo; kissing, caressing, intimate touch, undressing, bathing, changing involving a minor | Band III crushes through glances, a passed note, a shared umbrella, walking side by side |
| Violence | Hitting, slapping, shoving, dragging, shaking, restraining, locking in; any weapon held by or near a minor; a minor in the path of adult aggression | Verbal conflict (Band III may argue); aftermath shown through an adult's reaction |
| Danger | Fire, boiling liquid, deep water, heights, traffic, blades, medication, imitable stunts | Safe everyday environments |
| Abuse, neglect, self-harm | Depicted or described (starvation, wounds, bruises, any method) | Implied off-screen only, through an adult's discovery or a closed door; no method, no injury detail |
| Distress | Terror screaming, crying in agony | Quiet sadness, a held hand, comfort from an adult |
| Adult contact | Intimate or restraining touch | Caring and non-intimate: holding hands, a side hug, carrying a sleeping Band I character, tucking a blanket, a hand on the shoulder, a parent's kiss on the forehead or hair (Band I/II) |
| Dialogue | Remarks on a minor's body or looks; sexual jokes near a minor; slurs or body-shaming aimed at a minor | Age-appropriate speech; Band I has no lip-synced lines; Band II keeps lines short |

### 5. Action by Age Band
- **Band I (0–3)** — Simple Action Whitelist only: sleeping in a crib or bed declared in `[context]:`, resting on a parent's shoulder, curling fingers around an adult's finger, a slow blink or soft smile, hugging a soft toy. Always a flat, firm sleeping surface; never shaken, tossed, or laid on a soft or curved surface.
  `Beside the queen bed, {minor_ho_ten} rests peacefully inside the pine crib on the firm flat organic cotton mattress, chest rising and falling in calm rhythmic sleep, tiny fists curled gently beside soft cheeks through 00:10.0.`
- **Band II (4–12)** — calm, low-velocity everyday actions: sitting, walking beside an adult, drawing, eating, holding an adult's hand, short lines. No running near hazards, no climbing.
- **Band III (13–17)** — ordinary school and home life: walking, studying, talking, cooking under supervision; full dialogue within Gate 4B. Never fights, stunts, alcohol, smoking, or driving.
- Complex fast kinetics on young bodies also break diffusion anatomy (extra fingers, melting faces) — another reason to keep Band I/II actions simple.

### 6. Staging & Camera (Pillar 3 §4)
- Sanctuary zone and protective buffer apply to every minor.
- In adult conflict scenes, Band I/II use Option A (present and asleep, far from the conflict, a crib the screenplay says is occupied is never shown empty) or Option B (off-screen, never mentioned). Band III may be present and awake during verbal family conflict, positioned out of the path of any aggressive movement.
- The camera never lingers on or isolates a minor's body: ECU only on the face or hands for emotion; no low angle up the body, no voyeur or POV gaze at a minor, no slow pan along the body. Prefer eye-level medium and wide framing.
- No violence lexicon in any prompt where a minor is present (Gate 3F).
- Diegetic sound: no distressed child vocalizations (`infant's crying`); use neutral room tone (`soft room tone`, `gentle cotton rustle from the bedside crib`).

### 7. Enforcement
- **Gate 3F** (`episode_audit_suite.py`): generic minor nouns and retired aliases in visual prose; for every prompt that names a `minor_characters` entry: sexual lexicon anywhere in the prompt, body-focused lexicon in any sentence naming the minor, violence lexicon anywhere in the prompt, and adult labels attached to the minor.
- **Setting Gate 3B** (`setting_audit_suite.py`): every model sheet that declares an age under 18 is scanned against §3.
- **Manual (Creative Review, Doctrine §5)**: the §4 table, §5 band actions, and §6 camera rules.

---

## 🛡️ PART VII: THE CINEMATIC METAPHORICAL SAFETY TRANSLATION ENGINE

> When compiling generative video prompts into Code Block 1, the AI Prompt Architect must ensure **100% prompt acceptance by content moderation filters** across all major generative models (Kling, Runway, Sora, Midjourney, Pika).
>
> **Never applies to minors**: violence or sensual content involving an under-18 character is removed, not translated into metaphor (§[10d]).

### 1. The Safety Paradox Law
Never dilute dramatic tension by removing conflict. Instead, **translate physical violence and sensitive concepts into high-contrast cinematic, atmospheric, and kinetic metaphors**. The output retains 100% dramatic friction while guaranteeing 0% account moderation flags.

### 2. Mandatory Metaphorical Replacement Lexicon

| Blocked Concept | Forbidden Lexicon | Mandatory Metaphorical Prose Replacement |
|---|---|---|
| **Blade Trauma** | `stab`, `slash`, `slit throat`, `blood` | `gleaming steel arc whistles through dim air, driving opponent backward against stone wall; deep crimson lantern flare casts long shadow across floor` |
| **Gunfire** | `shoot`, `gunshot`, `bullet wound` | `explosive flash of incandescent sparks detonates, concussive air shockwave blowing hair backward` |
| **Fatal Strike** | `corpse`, `dead body`, `kill him` | `figure collapses motionless upon shadow-draped earthen floor, breathless under cold moonlight` |
| **Strangulation** | `choke`, `strangle`, `suffocate` | `iron-clad fingers pin collar firmly against rough oak timber, veins visibly bulging along tense neck` |
| **Physical Assault** | `beat up`, `punch in face` | `violent physical impact rattles heavy wooden partition, jarring ceramic vessels off wall shelves` |
| **Sensual Content** | `sexy`, `naked`, `bare skin`, `cleavage` | `dignified silhouette stands framed in backlight, draped in raw linen fabric; regal poise, articulate composure` |

### 3. Integrated Safety Linter Protocol
Every compiled prompt in Code Block 1 must pass the **Metaphorical Translation Gate**: zero instances of explicit banned keywords; all conflict physicalized through lighting flares, air displacement, shattered stone/timber textures, and biological somatic tension (clenched jaws, dilated pupils, ragged breathing).

### 4. The Lip-Sync Visibility & Dynamic Perspective Law (Anti-Static P.O.V Trap)
- **Zero Lip-Sync in Blind Perspectives**: Never assign spoken dialogue with lip-sync to a character whose perspective is currently Subjective First-Person P.O.V. or Macro Prop Insert. Generative models cannot animate invisible lips and hallucinate facial morphing in hands.
- **Mandatory In-Camera Transition**: Prompts starting in P.O.V. must transition to a Frontal Medium Close-Up (MCU) or Medium Shot (MS) before that character speaks.
- **Minor Protection (§[10d])**: an under-18 character present in the scene is declared in `[subject]:` by approved `ho_ten` + reference image and staged by age band (Band I/II asleep or off-screen in adult conflict). Never rephrase or relabel a minor to pass a moderation filter; restage or cut instead. Retired aliases (`project_rules.json` → `minor_character_names`) and project-specific distress vocabulary (`output/<project>/project_staging_rules.md`) stay out of prompts.

---

## ⚡ § 6. ZERO-CONFLICT MULTI-MODAL PROMPT ARCHITECTURE & KINETIC GOVERNANCE (2026 CODIFIED SSOT)

To completely eliminate spatiotemporal morphing, background drift, lip-sync hallucination, and action compounding across all AI video generation pipelines, the Sven Production Engine mandates the following **Zero-Conflict Protocols**:

### 1. The 3-Block Label Standard (`[context]:`, `[subject]:`, `[PROP]:`)
Every video prompt in **Code Block 1** MUST be partitioned into exactly three explicit structural blocks separated by blank lines (`\n\n`):
- **`[context]:` (The Master 5-Vector Location & Environmental Staging Standard)**
  - **Meaningful English Naming Standard**: Location names and image references MUST use meaningful, evocative English (e.g. `rustic wooden bedroom [100% Refer to image rustic_bedroom_4view.jpg]`, `humble dining kitchen [100% Refer to image dining_kitchen_4view.jpg]`). Transliterated Vietnamese aliases (`phong_ngu_01`, `nha_bep_01`) are strictly prohibited because AI text-encoders (T5, CLIP) parse English tokens for materials, lighting, and spatial geometry.
  - Syntax: `[Location Name in English] [100% Refer to image [filename/ref]], [exact time of day]. [Complete 5-vector physical architectural specification: full fixed furniture inventory ("có cái gì ở đó"), lighting physics, and atmospheric medium].`
  - Function: Permanently locks spatial boundaries, architecture, fixed furniture landmarks, daylight progression, and atmospheric physics before subjects are parsed, completely immunizing against AI spatial amnesia and environment hallucination.
  - **The Zero Ghost Object Law (Quy Chuẩn Bối Cảnh Chi Tiết & Chống Đồ Vật Tự Sinh)**:
    * `[context]:` MUST provide a complete, rich physical inventory of all setting structures, furniture, and domestic elements present in the staging zone (e.g. the weathered wooden bed, the flat cotton mattress, the coarse woven wool blanket resting folded across the lower bed, the bedside nightstand with the amber tungsten lamp).
    * **STRICT BAN ON GHOST OBJECTS**: Any fixture that characters touch, lean on, or pull in the Action timeline (`[00:00–00:XX]`) — such as pulling a blanket, leaning against a wooden headboard, or touching a lamp — **MUST ALREADY BE FULLY ESTABLISHED AND GROUNDED IN TEXT INSIDE `[context]:`**, and any handheld item they lift or carry MUST already be declared in `[PROP]:`. It is strictly forbidden for an everyday object to suddenly materialize in Action if it was omitted from `[context]:`.
  - **The 5 Mandatory Physical Vectors in `[context]:`**:
    * **Vector 1 (Image Anchor & Meaningful English Name)**: `[Location Name] [100% Refer to image <ref>]`.
    * **Vector 2 (Biological Time of Day)**: Exact natural daylight phase (`early dawn`, `golden morning`, `harsh midday`, `amber late afternoon`, `blue hour dusk`, `dim midnight lamp-lit`).
    * **Vector 3 (Fixed Architectural & Furniture Inventory — "Có cái gì ở đó")**: Complete inventory of physical structures and major fixed furniture mirroring the 4-View Location Sheet (e.g. for the rustic wooden bedroom: patterned encaustic cement floor tiles, sturdy dark wooden queen bed with white linen, coarse woven wool blanket spread over lower mattress, light pine wood crib placed firmly directly beside bed, wooden doorway leading to hallway). Barren 5-word declarations (`bedroom, morning.`) are strictly banned.
    * **Vector 4 (Lighting Physics & Direction)**: Key light source, angle/direction (diagonal 45° from window, overhead downward), natural color tone (warm golden amber, cool blue morning light; strictly zero Kelvin), and shadow behavior (long soft diagonal shadows).
    * **Vector 5 (Atmospheric Medium & Emotional Climate)**: Physical medium (floating dust motes in sunbeams, stagnant domestic air, humidity) and psychological mood (suffocating confinement, tense silence, protective warmth).
- **`[subject]:` (The Sovereign Subject Protocol & Initial Prop State Bifurcation)**
  - Syntax: each character in the scene is declared with the Sovereign Formula:
    `[ho_ten] [100% Appearance, attire, and facial features Refer to image X], [architectural anchor (same landmark within arm's reach when physically interacting)], [body posture], [hands free of props if unheld at 0.0s OR explicit t=0.0s hand-grip if already holding a prop at 0.0s], [eyeline toward a character or landmark] — the only [ho_ten] in frame.`
    ```text
    [subject]:
    my_duyen [100% Appearance, attire, and facial features Refer to image 1], sitting propped up against the dark wooden headboard on the queen bed, fingers clutching the edge of the linen sheet — the only my_duyen in frame.
    minh_khang [100% Appearance, attire, and facial features Refer to image 2], standing in the wooden bedroom doorway with one palm pressed flat against the jamb, chest held taut — the only minh_khang in frame.
    cu_tin [100% Appearance, attire, and facial features Refer to image cu_tin_4view.jpg], resting peacefully on the flat mattress inside the pine crib, chest rising with calm rhythmic breathing — the only cu_tin in frame.
    ```
  - Directorial Law: `[subject]:` establishes the zero-frame (00:00.0) spatial grounding to architecture, initial bodily posture and hand state, and the negative anti-duplication seal. All dynamic character actions, kinetic transitions, and emotional evolutions are directed within the Timeline Shots.
  - Minor entities (§[10d]): an under-18 character present in the scene is declared by approved `ho_ten` + reference image and staged by age band; Band I/II in adult conflict scenes are asleep (Option A) or omitted entirely (Option B). Retired aliases in `project_rules.json` → `minor_character_names` are banned.
- **`[PROP]:` (The Two-Tier `[PROP]:` Scope Law — mirrors DIRECTOR.md §1c & §5b)**
  - **Core Directorial Distinction: Handheld Props vs. Set Dressing**:
    * **`[PROP]:` holds every handheld item a character will lift, carry, or manipulate**, one per line, each declaring its $t=0.0\text{s}$ state (resting on a surface when unheld at $0.0\text{s}$, or held in `[ho_ten]`'s hands when already held at $0.0\text{s}$, synchronized with `[subject]:`): Tier 1 Signature Hero Props (Chekhov catalyst, heirloom, decisive proof; max 1–2 per series; bound with `[100% Refer to image ...]`) and Tier 2 everyday handheld items (bowls, cups, keys, phones; natural-English text only, no image tag).
    * **Furniture, fixtures, and bedding (beds, cribs, tables, chairs, curtains, fans, lamps, blankets, pillows) ARE STRICTLY FORBIDDEN IN `[PROP]:`**. They are Set Dressing described 100% via rich text inside `[context]:`; duplicating them in `[PROP]:` causes ghost duplicates and mesh clashing.
  - **Natural English Naming**: Prop names use natural English without underscores (e.g. `steaming ceramic ginger tea bowl`, `brass house key bundle`). Reference image filenames may keep underscores (`ginger_tea_bowl.jpg`).
  - **Syntax**:
    * *Tier 1 hero prop*:
      ```text
      [PROP]:
      brass house key bundle [100% Refer to image brass_keys.jpg], three tarnished keys on a frayed red cord, resting on the wooden bedside table — the only key bundle in frame.
      ```
    * *Tier 2 everyday handheld item*:
      ```text
      [PROP]:
      steaming ceramic ginger tea bowl, chipped white glaze, resting on the wooden bedside table with hot aromatic steam curling upward — the only bowl in frame.
      ```
    * *When the scene has no handheld item (pure somatic or fixture interaction)*:
      ```text
      [PROP]:
      none (pure environmental and somatic staging)
      ```

### 1b. The State-Delta Character Directing Protocol in Timeline Shots (`[00:00–00:XX]` — Zero `[subject]:` Redundancy)
While `[subject]:` locks the `00:00.0` static position, posture, hand-prop state, and anti-duplication seal, **timeline shots (`[00:00–00:XX]`) direct ONLY what changes (`Delta Δ`) after `00:00.0`**.
In every timeline shot (`[00:00–00:04.5]`, etc.), strictly enforce:
1. **Zero Static Position Repetition**: Never re-describe where characters are sitting or standing (`at the head chair`, `at the foot of the table`, `in front of the fireplace`) in the Camera Clause or Action prose when they remain at their `[subject]:` anchor.
2. **Zero `[subject]:` State Contradiction**: Never command a character to perform a transition into a state they ALREADY hold in `[subject]:` (e.g., if `seated` in `[subject]:`, never write `sits down` or `walks in from the door`; if `hands resting on the chair back` in `[subject]:`, never write `rests hand on the chair back` in `Action`).
3. **Zero Intra-Sentence Role Clash**: If Character A performs an active verb in the first half of a phase sentence, never append `as Character A sits/stands still` at the end of that same sentence.

### 2. Spacing Integrity Law (Khoảng Trống Phân Tách Bắt Buộc)
- There MUST be an explicit blank line (`\n\n`) between the Visual Style Header and `[context]:`, between `[context]:` and `[subject]:`, between `[subject]:` and `[PROP]:`, and between `[PROP]:` and `Diegetic room acoustics:`.
- This guarantees clean token chunking for LLM parsers and eliminates multi-modal conditioning bleed in diffusion models.

### 3. Track A (Single-Shot) Kinetic Governance (Quy Chuẩn Cú Máy Đơn)
- **Sub-Timeline Phase Division Law (Gate 3M)**:
  - Even though Track A has **0 CUTS** (unbroken camera trajectory), it is **STRICTLY FORBIDDEN to lump the entire 10 seconds into a single un-subdivided `[00:00–00:10.0]` paragraph**.
  - Lumping 10 seconds causes AI video models (Kling, Sora, Runway) to trigger all actions and dialogues simultaneously at second 0, resulting in catastrophic dual-speaker lip-sync overlap and action compounding.
  - Track A MUST be explicitly partitioned into 2 to 3 chronological phase brackets:
    * `[00:00.0 – 00:04.5]` [SINGLE CONTINUOUS TAKE - PHASE 1: INITIATION & OPENING TRAJECTORY]
    * `[00:04.5 – 00:10.0]` [SINGLE CONTINUOUS TAKE - PHASE 2: UNBROKEN GLIDE & RESOLUTION BEAT]
    *(Or dynamic 3-phase progression tailored to dramatic beats, with unbroken camera and acting flowing naturally to 00:10.0; strictly BAN rigid '00:08.5' cutoff dogma)
- **Single-Speaker Dominance (typical; timed by grammar §2–§3)**: In an unbroken take, primary dominance usually belongs to ONE character speaking. If an exchange occurs, lines must be strictly quarantined into non-overlapping phase windows.
- **The One-Move Rule & Action Compounding Purge (Gate 3R SSOT)**: Maximum 1 primary kinetic movement + 1 biological reaction per 3–4 second window. Never compound actions ("vừa làm A vừa làm B vừa làm C" e.g., snatching towel AND wiping hands AND stepping). Multi-task prop juggling and rapid sequential physical transitions are strictly banned by Gate 3R in `episode_audit_suite.py`.
- **Phase 3 Settle & Static Lock `[Terminal Beat]`**: Camera decelerates smoothly to an organic rest. Spoken dialogue is **strictly 0 words**. Subtle biological respiration only (zero frozen frames).

### 4. Track B (Multi-Shot) 180° Action Axis Governance (Quy Chuẩn Cắt Đa Cú Máy)
- **Explicit Time Brackets**: Every shot boundary states its exact second window in the canonical syntax (e.g., `[00:00–00:04.5] Medium shot on Eleazar, low angle, static camera — …`, `[00:04.5–00:08.8] Cut to a reverse medium close-up on Noa, eye level, static camera — …`, `[00:08.8–00:10.0] Cut to a close-up on Eleazar, eye level, static camera — …`).
- **Invariant Screen Directions**: Characters locked on screen-left MUST continue looking toward screen-right across all cuts; characters on screen-right MUST look toward screen-left. (Record screen direction in the Audit Card; inside Code Block 1, express it through architecture-anchored eyelines, never `screen-left` / `frame-right` words.)
- **Kinetic Momentum Handoff**: Strict zero action repetition across cuts.
- **Chekhov Prop State Machine**: Broken or severed props MUST be re-named to their derived physical fragments in subsequent cuts (`Jagged Ceramic Shards`, `Torn Parchment Shreds`).
- **Terminal Cut / Reaction or Parting Climax**: Final shot resolves naturally to 00:10.0 (whether holding an emotional reaction shockwave or delivering a parting cliffhanger retort), ensuring camera and character physics complete their arc cleanly into the cut (strictly BAN dogmatic cutoffs like 'cấm thoại sau 00:08.5').

### 4b. The Single Focal Action Law & Action Compounding Purge (Gate 3R SSOT)
To eliminate AI video diffusion errors (limb morphing, phantom hands, melting props, facial desync):
1. **The 1-Phase = 1-Move Rule**: Within any given time bracket (2.5s to 5.0s), a character performs **EXACTLY ONE primary physical macro-action beat** (e.g. holding paper down, slamming table, pressing clay, clutching chest).
2. **Strict Ban on Verb Stacking**: Prompts MUST NOT string together multiple sequential active verbs for a single character (e.g., "wiping knuckles AND throwing contract AND leaning forward" or "striking match AND slamming desk AND sweeping papers").
3. **Acting Depth via Biomechanical Micro-Reactions**: Acting complexity and emotional tension MUST be delivered through Observable Biomechanical Micro-Reactions (jaw clenching, shallow breathing, dilating pupils, sweat drops, throat swallowing) rather than chaotic physical stunts. Gate 3R in `episode_audit_suite.py` strictly blocks delivery if action compounding is detected.

### 4c. The Camera Scale & Angle Purity Law (Gate 3S SSOT)
To eliminate AI spatial disorientation, erratic framing, and visual incoherence across shots:
1. **The Single Scale & Angle Purity Standard**: Every shot or cut phase MUST declare its distinct **Shot Scale** (ELS, LS/WS, MLS, MS, MCU, CU, ECU/Macro, OTS, M2S) AND **Camera Angle / Perspective** (eye-level, low-angle, high-angle, dutch angle, overhead, etc.) inside the Camera Clause before `—`.
2. **Strict Ban on Semantic Confusion**: It is strictly forbidden to equate a Shot Scale with a Camera Angle (e.g. calling a close-up an 'angle', writing 'angle: close-up' or 'scale is low-angle'). Gate 3S in `episode_audit_suite.py` strictly blocks delivery if semantic confusion is detected.
3. **Strict Ban on Angle Conflicts**: A single shot cannot contain conflicting camera angles simultaneously (e.g., low-angle and high-angle in the same camera clause).
4. **Master 3-Beat Shot Progression**: Complex dialogue scenes should progress logically from establishing context (FS/M2S) to interpersonal tension (OTS/MCU) to emotional climax (CU/ECU).

### 4d. The 3-Case Continuity Reference Point Protocol (`TH1 / TH2 / TH3`) & `Seedance` High-Motion Compilation Mechanics (`workflow.md` §2.10, §8.3, §9.2)
Every scene compiled in Stage 4 MUST strictly execute its declared **Continuity Reference Case** and **Model Tier** from the Stage 3 Scene Rough Script:
1. **Case 1 (`TH1 — CẦN THAM CHIẾU Khung Hình Cuối Cảnh Trước`: Same Time & Same Location)**:
   - When Scene $K$ occurs at the exact same continuous moment in time and inside the same physical location as Scene $K-1$, the user provides the extracted **Static Terminal Frame (`Last Frame @00:10.0` or `@00:15.0`)** from Scene $K-1$.
   - The Prompt Compiler inspects that image and locks `[subject]:` and `[PROP]:` at `00:00.0` of Scene $K$ to match the static frame **100% verbatim in physical reality** (character position, posture, hand-prop grip, eyeline, and visible landmarks). Phase 1 (`[00:00–00:XX]`) launches directly from that exact static pose (`Sub-Case 1A` Direct I2V Continuation or `Sub-Case 1B` Intra-Location Camera Angle Switch paired with the 4-View Location Sheet).
2. **Case 2 (`TH2 — KHÔNG THAM CHIẾU Khung Hình Cảnh Trước`: Different Location, Time Jump, or Character Lineup Switch)**:
   - When Scene $K$ changes location, jumps in time, or switches active characters, do **NOT** reference Scene $K-1$'s spatial frame.
   - Instead, inspect the user-supplied **New Location Reference Image (`<location_ref>`)** + **Active Character Sheets (`<char_ref>`)** to inventory **only the real architectural landmarks, furniture positions, light direction, and surface textures visibly present in that image** into `[context]:` (zero ghost fixtures), anchor characters in `[subject]:` to actual visible landmarks on the image, and bridge the cut via a **Mode B Sequence Bridge**.
3. **Case 3 (`TH3 — THAM CHIẾU NGOẠI LỆ Siêu Nhiên / Xuyên Không / Dịch Chuyển Không Gian`: Same Continuous Moment in Time + Instant Spatial Shift)**:
   - In supernatural, portal, or time-travel (`xuyên không`) transitions where the spatial environment shifts at the exact same continuous second, lock `[subject]:` and `[PROP]:` at `00:00.0` of Scene $K$ to the **exact body posture, mid-step momentum, and hand grip from Scene $K-1$'s terminal frame**, while completely replacing `[context]:` with the 5-Vector architecture and lighting of the **New World/Era Location Reference Image (`<new_location_ref>`)**, and directing the physical impact/shockwave of landing in the new environment in Phase 1 (`[00:00–00:03]`).
4. **Model Tier Compilation (`Standard Lip-Sync 10.0s` vs. `Seedance High-Motion Action/Chase 10.0s / 15.0s`)**:
   - **Standard Dialogue / Drama Scenes (`[🎭 MODEL TIÊU CHUẨN / LIP-SYNC · 10.0s]`)**: Compile at `1.0x` natural pace, 1 primary macro action per character per phase (`Gate 3R`), stable camera during lip-sync speech, and a calm/locked **Clean Dynamic Landing Pose** at `@00:08.5–00:10.0`.
   - **High-Tension Action, Chase, Struggle & Combat Scenes (`[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 10.0s / 15.0s]`)**: Invoke `@CombatDirector` high-velocity syntax (`combat-director/SKILL.md`), structuring `2.0s–3.5s` micro-phases (`3–4` phases for `10.0s`; `4–6` phases for `15.0s`) linked by causal arrows (`Action A → Impact/Reaction B → Secondary Environmental Debris/Recoil C`), pairing with dynamic tracking/whip-pan camera moves along the `180° Action Axis`, and locking into a sharp **Action-Relay Terminal Keyframe (`@00:09.0–00:10.0` or `@00:13.5–00:15.0`)** free of motion blur whenever Scene $K+1$ is `Case 1` or `Case 3`.

### 5. Interactive 16:9 Model Sheet Deliverable Standard
In all deliverables (`setting.html` and `tap-X.html`):
- Every referenced character, prop, and location MUST have its complete, ready-to-run 16:9 Model Sheet prompt displayed inside a dedicated prompt code box.
- Every asset card MUST be equipped with an interactive `📋 Copy Prompt` button for instant copy-paste execution in Midjourney, Flux, or Leonardo.

### 6. The Dual Taxonomy Law: Fixed Location Fixtures vs. Dynamic Kinetic Props
(ĐỊNH LUẬT PHÂN ĐỊNH BỐI CẢNH CỐ ĐỊNH & ĐẠO CỤ ĐỘNG CẦM NẮM)

> [!CRITICAL]
> **QUY TẮC CỐT LÕI: CỐ ĐỊNH TẠO 1 LẦN TRONG BỐI CẢNH — ĐỘNG MỚI TẠO PROP RIÊNG BIỆT.**
> 
> 1. **Vật thể Cố định (Fixed Set Dressing & Architectural Fixtures)**: Mọi đồ đạc nội thất gắn liền với không gian phòng ốc hoặc địa điểm (Ví dụ: Giường ngủ, Nôi thông kê sát giường, Tủ đầu giường, Tủ quần áo, Rèm cửa, Lò than sưởi ấm, Cột lều, Bàn làm việc, Khiên dựa cột...) PHẢI ĐƯỢC THIẾT KẾ 1 LẦN DUY NHẤT VÀ NẰM TRỌN VẸN TRONG **Location Concept Design Sheet**.
>    - **TUYỆT ĐỐI CẤM**: Không được tạo thêm ảnh tham chiếu đạo cụ riêng lẻ cho vật cố định (ví dụ: đã có nôi gỗ nằm trong phòng ngủ thì **CẤM** tạo thêm `prop_crib_4view.jpg`).
>    - **Khi biên dịch prompt video**: Chỉ cần gọi `[context]: intimate Southern Vietnamese master bedroom [100% Refer to image location_bedroom_4view.jpg]` kèm mô tả nội thất. Toàn bộ giường, nôi, tủ, rèm tự động đồng bộ theo bối cảnh. **CẤM** khai báo lại chiếc nôi (`pine wood crib [100% Refer to image ...]`) trong `[PROP]:` vì sẽ khiến AI model sinh ra chiếc nôi thứ hai (Ghost Duplicate) hoặc xung đột hình học (Mesh Clashing).
> 
> 2. **Đạo cụ Động (Handheld Kinetic Props)**: Những vật thể được nhân vật trực tiếp cầm nắm, thao tác, di chuyển, vung đập, biến đổi trạng thái được khai báo trong `[PROP]:`. **Chỉ Tier 1 Hero Props (tối đa 1–2 mỗi series: vũ khí gia truyền, kỷ vật, hợp đồng sống còn) mới được tạo Prop Design Sheet riêng.** Tier 2 vật dụng cầm tay đời thường (bát, cốc, mâm, khăn) chỉ mô tả bằng văn bản, không tạo sheet.
> 
> 3. **Luật Đạo Cụ Độc Lập — Tuyệt Đối Không Tạo Gộp (Isolated Clean Prop Law)**:
>    - Khi tạo Prop Sheet cho đạo cụ động, **CHỈ CÓ DUY NHẤT 1 ĐẠO CỤ ĐÓ** trên nền trắng thuần studio (`#FFFFFF`).
>    - Tuyệt đối không được tạo gộp búa với khiên giáp, chìa khóa với hộp gỗ. Zero environmental elements, zero human hands, zero text overlays, zero clutter.

---

### 7. Directorial Master Prompt Templates (Mẫu Prompt Chuẩn Hóa Theo Phong Cách)

#### TEMPLATE A: LOCATION CONCEPT DESIGN SHEET (16:9 Landscape · Multi-Angle Layout)
*Áp dụng cho mọi bối cảnh nội thất hẹp (căn phòng, ngôi nhà, lều quân sự) lẫn ngoại cảnh rộng (đấu trường, sân vườn, thung lũng):*
```text
Style: [Visual Style, e.g., Modern K-Drama Premium Cinematography / Pixar\Disney 3D animation style]

Name: [Location Name, e.g., Human War Pavilion / The Arena of Reckoning / Intimate Master Bedroom at Dawn]
Description: [Mô tả chi tiết không gian kiến trúc, kết cấu vật liệu, nguồn sáng, bầu không khí và TOÀN BỘ ĐỒ ĐẠC CỐ ĐỊNH (giường nệm, nôi gỗ thông, tủ đầu giường, đèn ngủ, tủ áo, rèm voan, cờ hiệu, lò than, khiên dựa cột...)]

Format: Location concept design sheet, 16:9 landscape, multi-angle layout. Exactly 4 panels showing the same location: top-left wide establishing shot, top-right reverse angle (180° opposite wall and depth), bottom-left overhead bird's-eye view (spatial layout of fixtures), and bottom-right ground-level key-landmark view (the fixture where the main action happens). Uniform lighting across all four panels; time of day is set per scene in `[context]:`. Focus entirely on full location views, with no written descriptions, detail labels, or floor plans.

Rules: No characters or people - environment only. The location must look consistent and recognizable across all panels, with the same buildings, props, and layout. Do not include any text, letters, numbers, annotations, captions, dimension lines, arrows, labels, legends, zoning notes, or watermarks.
```

#### TEMPLATE B: DYNAMIC PROP DESIGN SHEET (Strictly for Tier 1 Hero Props · Complete Isolation)
*Applies strictly to Tier 1 hero props (heirloom weapons, narrative relics, forged deeds, signature vehicles). Do not create sheets for everyday Tier 2 items. Never combine multiple props onto one sheet:*
```text
Style: [Visual Style, e.g., Modern K-Drama Premium Cinematography / Pixar\Disney 3D animation style]

Name: [Prop Name in natural English, e.g., Kael's warhammer / heirloom pocket watch / forged land deed]
Category: [Category: Weapon / Culinary / Medical / Tool / Relic]
Description: [Detailed physical dimensions, material composition, time-worn weathering, usage marks, and mechanical behavior when dropped or set down]

Format: Prop design sheet, 16:9 landscape (or 4:3). Show only four views of the same prop: one main view that best presents its visual features, plus front, side, and back views. The main view must be the largest and clearest; the three orthographic views must fully show the prop shape and structure. Pure white background (#FFFFFF).

Rules: Do not include any text, letters, numbers, annotations, captions, material swatches, dimension lines, arrows, close-up detail panels, or exploded views. The prop must remain completely consistent across all views. No environmental elements, no characters, no watermark.
```

---

### 8. Directorial Interaction Syntax for In-Scene Location Fixtures

When a character needs to **use, grip, lean against, touch, or detach an object ALREADY PRESENT** in a location reference sheet (e.g., gripping pine crib balusters, sitting on a bed edge, parting curtains, detaching a shield leaning against a tent post), the Director enforces the **In-Scene Spatial Anchoring Protocol**:

#### 1. The 3-Block Binding Protocol:
- **`[context]:` Block (Stage Zone Anchor)**:
  - Explicitly declare the interaction zone around the fixed fixture in the reference sheet:
  - Syntax: `[Evocative location name in natural English] [100% Refer to image [location_ref]], [focal staging zone anchored near the in-scene [fixture_name]].`
  - *Example*: `intimate Southern Vietnamese master bedroom [100% Refer to image location_bedroom_4view.jpg], at dawn. Staging focused on the intimate floor area between the queen bed and the adjacent pine wood crib.`
- **`[subject]:` Block (Somatic Fixture Lock)**:
  - Never leave characters floating in empty space; lock their posture directly to the fixed architectural fixture:
  - Syntax: `[ho_ten] [100% Appearance, attire, and facial features Refer to image X], [posture anchored directly to in-scene fixture: e.g. sitting on floor tiles leaning back against the queen bed edge, slender fingers gripping the vertical pine balusters of the in-scene pine crib, gaze on the crib — the only [ho_ten] in frame].`
- **`[PROP]:` Block (Clean Separation)**:
  - **Static In-Place Contact** (sitting on a bed, gripping crib rails, leaning on a wall, parting curtains): **DO NOT list in `[PROP]:`**. The fixture belongs 100% to `[context]:`.
  - **Kinetic Detachment from Set** (lifting a shield leaning on a tent post, taking a pitcher off a shelf, unhooking a storm lantern): Declare as an **In-Scene Derived Prop**:
    - Syntax: `[item name in natural English] [In-scene fixture of [location_ref]], [initial state resting on/against [fixture]] — the only [item] in frame`. The detachment action is directed inside the timeline (`[00:00–00:XX]`).

#### 2. Timeline Action Prose `[00:00–00:10.0]` (State-Delta Physical Causality Chain — Zero `[subject]:` Position Repetition):
In the timeline phases, direct ONLY the new transition action from the `[subject]:` posture behind the canonical `—` camera clause separator (never repeating static positions from `[subject]:` inside the Camera Clause or Action):
- **Case A: In-Place Tactile Transition**:
  - *Example (Bedroom — where `[subject]:` already anchored `my_duyen` sitting beside the pine crib)*: `[00:00–00:03.5] High-angle medium close-up, static camera with shallow depth of field holding sharp focus on my_duyen — my_duyen rests her forehead against the pine crib rail as her shoulders tremble slightly.`
- **Case B: Kinetic Detachment from Set**:
  - *Example (War Tent — where `[subject]:` already anchored `kael` standing beside the timber tent post)*: `[00:00–00:04.0] Medium shot, slight low angle, slow push-in with sharp optical focus framing kael — kael unhooks the battered steel shield from the timber post and raises it into a defensive guard.`


---

## 🎭 § [1.G] THE SVEN DIRECTORIAL TEMPORAL INTELLIGENCE ARCHITECTURE
### (HIỂU KIẾN THỨC ĐIỆN ẢNH ĐỂ ĐIỀU PHỐI THỜI GIAN — CHỐNG RẬP KHUÔN CÔNG THỨC)

A master film director does not impose arbitrary mathematical boxes onto living cinema. A 10-second scene is a dramatic canvas whose internal temporal pacing is determined 100% by the **Dramatic Intent & Scene Archetype**.

The Director MUST consciously classify each scene into one of the **6 Directorial Archetypes** and apply its native temporal physics:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        THE 6 DIRECTORIAL ARCHETYPES & NATIVE TEMPORAL CADENCE                          │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. HIGH-TENSION INTRUSION (CẮT ĐỘT NGỘT & XUNG ĐỘT BÙNG PHÁT):                                         │
│    • Pacing: Fast, explosive 0–4s opening shock; 4–10s sustained confrontational standoff.             │
│    • Structure: Multi-Shot (Track B). Hard cut on physical door slam / vocal intrusion.               │
│    • Dialogue: Aggressive, sharp, rapid (~3.0–3.5s per line).                                          │
│    • Example: [00:00–00:04.2] Intrusion burst ➔ [00:04.2–00:10.0] Low-angle counter-thrust & standoff. │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. PHYSICAL BREAKDOWN / COLLAPSE (SỤP ĐỔ THỂ XÁC & CỨU NGUY):                                          │
│    • Pacing: 0–4.5s faltering effort; 4.5–10s accelerated freefall and emergency catch.                │
│    • Structure: Single Continuous Tracking Take or Dynamic Two-Shot.                                   │
│    • Dialogue: Fading breathless whisper; dialogue ceases before the body hits the floor.              │
│    • Example: [00:00–00:04.6] Weak apology & slipping grip ➔ [00:04.6–00:10.0] Panic dive & catch.     │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. EMOTIONAL CLIMAX / EXPOSURE (ĐỈNH ĐIỂM NƯỚC MẮT & BỘC LỘ SỰ THẬT):                                  │
│    • Pacing: 0–5.5s heavy, weeping plea; 5.5–10s crane upward to crushing remorse & maternal silence.   │
│    • Structure: Single Unbroken Master Take (Track A). Intimate macro gliding to wide remorse.         │
│    • Dialogue: Trembling, broken, sobbing cadence (~4.0–4.5s).                                         │
│    • Example: [00:00–00:05.4] Macro bruise reveal & plea ➔ [00:05.4–00:10.0] Crane to remorse kneel.   │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. DOMESTIC RECONCILIATION & HEALING (HÀN GẮN TÌNH THÂN & VỖ VỀ):                                      │
│    • Pacing: Lingering, tender, slow emotional warmth throughout all 10 seconds.                       │
│    • Structure: Single Continuous Take (Track A). Gentle push-in to touch and forehead lean.           │
│    • Dialogue: Soft repentant whisper, followed by quiet emotional relief.                             │
│    • Example: [00:00–00:04.8] Warm herbal compress & apology ➔ [00:04.8–00:10.0] Forehead lean & rest. │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 5. DOMESTIC ROUTINE & SERENE BREEZE (NHỊP SỐNG GIA ĐÌNH BÌNH THẢN):                                    │
│    • Pacing: Relaxed, unhurried, rhythmic domestic blocking.                                           │
│    • Structure: Multi-Shot (Track B) or Gentle Gliding Master Take.                                    │
│    • Dialogue: Conversational, lighthearted, warm family banter.                                       │
│    • Example: [00:00–00:05.2] Setting the dinner mat ➔ [00:05.2–00:10.0] Reverse angle to river breeze.│
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 6. CLIFFHANGER SUSPENSE SNAP (ĐỨNG HÌNH NGHẸT THỞ CUỐI TẬP):                                          │
│    • Pacing: 0–4s sudden external disruption; 4–10s unyielding defensive shield, sharp snap cut.       │
│    • Structure: Rapid 180° Reverse Cut.                                                                │
│    • Dialogue: Menacing intrusion line ➔ Sharp unyielding counter-bark.                                │
│    • Example: [00:00–00:04.2] Intruder with scissors ➔ [00:04.2–00:10.0] Protective barrier & cut.     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

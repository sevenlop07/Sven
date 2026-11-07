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
| **5-Tier Dialogue Word Cap & Calm Understatement Law (`~2.5 words/s` Safe AI Lip-Sync Standard)**: **Default `10s` clip (`@Director`)** = `3–4 Shots` (`3s–2s–3s–2s`), `1–2` spoken lines (`12–22 words total`); **Exclusive `15s` Action/Chase/Combat clip (`@CombatDirector`)** = `5–6 Shots` (`3s–3s–4s–3s–2s`), `0` spoken words during chase/VFX shots (`Shot 3 & Shot 4`) and **Calm Understatement Closing Line (`2–6 words`)** | Hard Constraint |
| Shots contiguous, non-overlapping, start at `00:00`, end at the clip duration `10s / 15s / 30s` (`Shot 1 (00:00-00:03)` ... `Shot N`) | Hard Constraint |
| **Zero Cumulative Timestamps**: Every scene prompt MUST start at `00:00` for third-party AI generators; NEVER use cumulative episode timestamps like `(00:10-00:20)` in prompts | Hard Constraint |
| **Single `<<<Image X>>>` Declaration Law**: Declare `<<<Image X>>>` **ONLY ONCE** inside `[context]:` and `[subject]:`. **NEVER repeat `<<<Image X>>>` inside `Shot 1..N`** | Hard Constraint |
| **Zero-Costume & Zero-Age Law (`Gates 3A & 3E`)**: Strictly ZERO clothing/garment words (`in a black jacket`, `in a dark suit`, `skirt`) and ZERO numeric ages or age/hair/beard words (`32-year-old`, `young blonde`, `silver-bearded`) anywhere in the video prompt; voice maturity and emotion are encoded in **ONE single parenthetical (`[Proper_Name] ([vocal timbre/maturity], [tone]): "..."`)** | Hard Constraint |
| **1–2 Short Natural Sentences per Shot (`15–30w`)**: Each `Shot N` describes 1 clear state transition (`A ➔ B`) in natural prose; strictly zero mechanical `→` arrows | Hard Constraint |
| Canonical Unified Multi-Shot Storyboard syntax (§8) | Hard Constraint |

---

## §1 — CINEMATIC MENTAL MODEL & DYNAMIC SHOT PACING ARCHITECTURE

### 1.1 Dynamic Shot Pacing by Dramatic Intent (`10.0s @Director` vs. `15.0s @CombatDirector` — Zero Cookie-Cutter Grids)
> **ANTI-FORMULA MANDATE**: A master film editor NEVER cuts every `10.0s` scene into the exact same `3s–2s–3s–2s` grid! Shot count (`1 to 4 shots` in `10s`; `3 to 6 shots` in `15s`) and shot duration (`1.5s to 10.0s`) MUST be chosen organically from the **emotional and dramatic purpose of each specific scene**:

| Scene Dramatic Archetype (`10.0s @Director`) | Optimal Shot Count & Rhythm | Why This Rhythm Serves the Scene (Directorial Expertise) |
|---|---|---|
| **1. Deep Intimacy, Grief, Confession, or Unbroken Tension** | **`1 Continuous Shot (`00:00-00:10`)` OR `2 Slow Shots (`5s–5s` / `6s–4s`)`** | Cutting rapidly during a heartfelt confession, quiet grief, or a suffocating 1-on-1 stare breaks emotional immersion. Let the camera hold or push in slowly (`4s–6s` per shot) so the viewer feels every breath and micro-expression. |
| **2. Escalating Confrontation or Action ➔ Reaction ➔ Turn** | **`3 Shots (`4s–3.5s–2.5s` or `3s–4s–3s`)`** | `Shot 1 (3–4s)` establishes the interpersonal action and opening line $\to$ `Shot 2 (3.5–4s)` captures the counterpart's counter-move or emotional shift $\to$ `Shot 3 (2.5–3s)` lands the decisive turn or parting shot. |
| **3. Sudden Disruption / Shock Opening ➔ Lingering Aftermath** | **`3 Shots (`2s–5s–3s`)`** | `Shot 1 (2s)` opens with a sudden physical disruption (door bursts open, glass shatters, hand grabs a wrist) $\to$ `Shot 2 (5s)` tracks the character stepping into the space and absorbing the revelation $\to$ `Shot 3 (3s)` settles on the emotional fallout. |
| **4. Tactical Clue / Prop Insert & Psychological Reversal** | **`4 Shots (`3s–2s–3s–2s` or `2.5s–2s–3s–2.5s`)`** | Used **specifically** when the scene turns on a hidden tactile detail (`Shot 2: 2s` macro insert of a brass keyring, deadbolt lock, hidden fangs, or trembling hand) paired with an Off-Screen `L-Cut` line, followed by `Shot 3` realization and `Shot 4` checkmate. |

- **Exclusive `15.0s` Action/Chase/Ambush/Combat Scenes (`00:00–00:15` on `@CombatDirector` — Flexible `3–6 Shots`)**:
  * Vary shot lengths based on **Kinetic Contrast**: use **longer `3.5s–5.0s` tracking shots** for uninterrupted full-speed sprints or continuous martial exchanges (`0` dialogue), **`2.0s–3.0s` fixed-frame wide shots** when ground VFX or heavy environmental impacts trigger, and **`1.5s–2.5s` tight close-ups** for sudden freezes, parries, or the final boss checkmate (`e.g., 3s–3s–4s–3s–2s`, `4s–5s–3s–3s`, or `3s–3s–2s–2s–3s–2s`).

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

## §2 — SPEECH RATE & `10S / 15S` WORD BUDGET (`~2.5 WORDS/S` + CALM UNDERSTATEMENT CLOSING LINE)

Safe speech for AI video lip-sync operates at **`~2.5 words/second`**, leaving `~1.0s` buffer for facial acting (`Image Speaks First, Dialogue Speaks Second`):

| Clip Duration & Owner | Storyboard Structure | Sentence Count | Total Word Budget (Whole Clip) | Closing Line Law |
|---|---|---|---|---|
| **Default `10.0s` Scene (`@Director`)** | **`3 – 4 Shots`** (`3s–2s–3s–2s`) | **`0 – 2 sentences`** (up to 3 short lines with `L-Cut`) | **`12 – 22 words total`** (`6–10w` setup + `2–6w` closing line; `0w` for silent scenes) | **Calm Understatement (`2–6 words`)** in `Shot 4` |
| **Exclusive `15.0s` Scene (`@CombatDirector`)** | **`5 – 6 Shots`** (`3s–3s–4s–3s–2s`) | **`0 – 3 ultra-short lines`** (`0w` during `Shot 3` chase & `Shot 4` VFX) | **`6 – 18 words total`** (`0w` in pure combat) | **Ice-Cold Checkmate (`2–5 words`)** in `Shot 5/6` |

**Buffer & Psychological Subversion Spoken Rules**:
- **Enter in the middle of the situation (*In medias res*)**: Zero greetings, zero plot-summary exposition.
- **Micro-Visual Reveal Over Verbal Exposition**: Never let characters explain their secret identity, power, or scheme in words; reveal it via **1 close-up visual detail (`Shot 2 / Shot 4`)**.
- **Calm Understatement Closing Line (`2–6 words`)**: At the decisive turn (`Shot 4` in 10s or `Shot 5/6` in 15s), the dominant/predator/authority character speaks the **shortest, calmest, most understated line in the scene (`2–6 words`)** (*`"I'm sorry."`*, *`"Miss, you seem lost."`*, *`"Because you secretly sold Warehouse Four."`*).

---

## §3 — LIP-SYNC WINDOWS & OFF-SCREEN `L-CUT` DIALOGUE

### 3.1 Lip-Sync Timing Windows, Clean Terminal Frame Mouth-Closure & Action Vocal Economy
- A spoken line **starts ≥ 0.5 s** after its shot begins and **ends ≥ 0.8 s** before the shot ends so lips close cleanly before the cut.
- **Zero Dialogue During High-Speed Locomotion & VFX Shots (`Shot 3 & Shot 4` in `15s` `@CombatDirector` Scenes)**: Never place spoken dialogue inside a `3–4s` long tracking chase shot (`Shot 3`) or a wide-to-fixed hard-stop/VFX trap shot (`Shot 4`). Keep speech strictly in the calm setup (`Shot 1`), the snap-freeze realization (`Shot 2`: `"I'm sorry."`), and the final boss confrontation (`Shot 5`: `"Miss, you seem lost."`).

### 3.2 Off-Screen `L-Cut` & Selective Face Obscuration
1. **Off-Screen `L-Cut` Audio (`[Name] (outside the door / across the table / from behind, [tone])`)**:
   - Allows a character outside the current shot's frame to speak while the camera stays on a `2s` prop/lock close-up (`Shot 2`) or tracks the protagonist's movement (`Shot 1`), maintaining tension without unnecessary face cuts.
2. **Selective Face Obscuration (Lower-Face / Back Silhouette Shots)**:
   - Using `The camera avoids [Name]'s full face, showing only [Name]'s lower face, jawline, firm mouth, and hand...` or `showing only his back and shoulders in silhouette` prevents multi-character face-blending and amplifies mystery.

---

## §4 — SHOT CAPACITY BY WINDOW (`2s` · `3s` · `4s`)

| Shot Window | Typical Role in Storyboard | Action Capacity (`1–2 Short Natural Sentences`) | Spoken Capacity |
|---|---|---|---|
| **`2.0 s` Shot** (`00:03-00:05`, `00:08-00:10`, `00:13-00:15`) | Prop/Lock Insert (`Shot 2`), Micro-Visual Reveal (fangs, black nails, keyring tap), or Terminal Payoff (`Shot 4 / Shot 5/6`) | **1 crisp micro-action or state flip** (`15–25 words` of natural prose; zero `→` arrows) | `0 words` OR `2–6 words` calm understatement / `L-Cut` line |
| **`3.0 s` Shot** (`00:00-00:03`, `00:05-00:08`, `00:10-00:13`) | Opening Setup/Mask (`Shot 1`), Snap-Freeze Close-Up (`Shot 2` in 15s), OTS Reaction (`Shot 3`), or Hard-Stop + VFX (`Shot 4` in 15s) | **1 clear state transition `A ➔ B`** (`18–30 words` of natural prose: e.g., gentle smile freezes into pure panic; runner stops sharply as runes glow beneath feet) | `1 short line` (`3–10 words`) OR `0 words` in VFX/reaction shot |
| **`4.0 s` Shot** (`00:06-00:10` in 15s) | Full-Speed Flight / Pursuit / Tracking Action (`Shot 3` in 15s) | **1 continuous locomotion trajectory** (`Exterior, long tracking follow shot` — turns and flees through empty alleyways) | **Strictly `0 words`** (100% kinetic motion & footsteps Foley) |

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

## §6 — SHOTS AND CUTS (`10.0s` DEFAULT ON `@DIRECTOR` VS. `15.0s` ACTION/COMBAT ON `@COMBATDIRECTOR`)

| Clip Duration & Owner | Canonical Multi-Shot Storyboard Structure | Shot Timing Breakdown | Key Camera & Action Rhythm |
|---|---|---|---|
| **10.0 s (Default for ALL Standard Dialogue / Drama / Twist Scenes — `@Director`)** | **`3 – 4 Shots`** (`Shot 1` .. `Shot 4`) | **`3s – 2s – 3s – 2s`**<br>(`00:00-00:03`, `00:03-00:05`, `00:05-00:08`, `00:08-00:10`)<br>or **`3s – 4s – 3s`** | • `Shot 1 (3s)`: Setup / Social Mask + Line 1<br>• `Shot 2 (2s)`: Close-up Prop/Lock/Micro-Detail Insert (+ optional Off-Screen `L-Cut` line)<br>• `Shot 3 (3s)`: OTS / Reaction / State-Transition (`A ➔ B`)<br>• `Shot 4 (2s)`: Selective Face / Lower-Face / Payoff Close-up + Calm `2–6w` Closing Line |
| **15.0 s (Reserved EXCLUSIVELY for High-Motion Action / Chase / Ambush / Combat — `@CombatDirector` `[⚡ SEEDANCE · 15.0s]`)** | **`5 – 6 Shots`** (`Shot 1` .. `Shot 5/6`) | **`3s – 3s – 4s – 3s – 2s`** (5 shots)<br>or **`3s – 3s – 2s – 2s – 3s – 2s`** (6 shots) | • **Kinetic Contrast Curve**: `Shot 1 (3s)` Calm/Setup $\to$ `Shot 2 (3s)` Snap Freeze / Threat Spotted $\to$ `Shot 3 (4s)` Full-Speed Long Tracking Follow Shot (**0 dialogue**) $\to$ `Shot 4 (3s)` Hard Stop + VFX/Trap on Fixed Frame (**0 dialogue**) $\to$ `Shot 5 (2s)` Rear-Angle Spin into Boss Ambush + `2–5w` Checkmate Line |
| **30.0 s (Explicit User Request Only)** | **`8 – 10 Shots`** (`Shot 1` .. `Shot 10`) | `2.5s – 4.0s` per shot across 3 mini-acts | Full 3-act sequence inside a single storyboard prompt |

- Minimum shot length: **≥ 2.0 s** (`2s` for crisp prop inserts, micro-reveals, and terminal payoff shots; `3s–4s` for dialogue, tracking locomotion, and state transitions).
- Never repeat the exact same shot scale and angle in two consecutive shots; alternate smoothly between `medium close-up`, `close-up, fixed shot`, `over-the-shoulder perspective`, `long tracking follow shot`, `wide shot transitioning to fixed frame`, and `medium shot, rear camera angle`.
- **1–2 Short Natural Sentences per Shot (`15–30 words`)**: Each `Shot N` describes **1 clear state transition (`State A ➔ State B`)** in natural cinematic prose. Strictly ban mechanical `→` arrows and `[00:00–00:05.0] —` single-paragraph walls.

---

## §7 — DENSITY PER CLIP (BY DURATION & OWNER)

| Clip Type & Owner | Total Shots | Spoken Lines | Total Spoken Word Budget | Closing Line Law |
|---|---|---|---|---|
| **Default `10.0s` Drama / Dialogue / Twist (`@Director`)** | `3 – 4 Shots` (`3s–2s–3s–2s`) | `1 – 2` lines (or `3` short lines with `L-Cut`) | **`12 – 22 words total`** (`~6–10w` setup line + `2–6w` closing line) | **Calm Understatement (`2–6 words`)** |
| **Exclusive `15.0s` Action / Chase / Ambush / Combat (`@CombatDirector`)** | `5 – 6 Shots` (`3s–3s–4s–3s–2s`) | `1 – 3` ultra-short lines (`0` words during `Shot 3` chase & `Shot 4` VFX) | **`6 – 18 words total`** (`0w` in pure combat, or brief setup + `2–5w` boss checkmate line) | **Ice-Cold Checkmate (`2–5 words`)** |
| **Silent Reaction / Pure Visual Scene (`Model 0`)** | `3 – 4 Shots` (`10s`) | `0` lines | **`0 words`** (100% visual micro-reveal & Foley) | Pure visual payoff |

---

## §8 — CANONICAL UNIFIED MULTI-SHOT STORYBOARD PROMPT SYNTAX (`100% PHƯƠNG ÁN MỚI` — DOUBLE-LOCK `<<<Image X>>> (100% ...)` & `[prop]:` BLOCK)

### 8.1 Template A — Default `10.0s` Scene (`@Director` · Dynamic `1–4 Shots` Chosen by Dramatic Intent)
```text
[Time of Day] · [Interior / Exterior] · [Location Title]
Style: [Visual Style Specification — e.g., 3D Semi-Realistic Cinematic Animation, Unreal Engine 5 and Octane Render style, detailed skin shaders, soft subsurface scattering, volumetric lighting].

[context]:
[Evocative Location Name in Natural English] <<<Image 1>>> (100% architectural layout, furniture, and lighting strictly refer to this reference image), [time of day]. [5-Vector Environmental Specification: architectural layout & full fixed furniture inventory, key lighting source & direction without Kelvin, shadow behavior, and atmospheric mood].

[subject]:
[Proper_Name_A] <<<Image 2>>> (100% facial features, beauty/handsome appearance, hairstyle, body proportions, and exact outfit strictly refer to this reference image): [Initial 3D architectural anchor and posture], [hand/prop contact state at 00:00 — strictly ZERO clothing/garment words and ZERO numeric ages or age/hair/beard words], [eyeline toward Proper_Name_B or landmark] — the only [Proper_Name_A] in frame.
[Proper_Name_B] <<<Image 3>>> (100% facial features, beauty/handsome appearance, hairstyle, body proportions, and exact outfit strictly refer to this reference image): [Initial 3D architectural anchor and posture], [hand/prop contact state at 00:00 — strictly ZERO clothing/garment words and ZERO numeric ages or age/hair/beard words], [eyeline toward Proper_Name_A or landmark] — the only [Proper_Name_B] in frame.

[prop]:
[Canonical Tier-1 Prop/Weapon Name] <<<Image 4>>> (100% shape, material, engravings, proportions, and visual details strictly refer to this reference image): [Exact 00:00 resting placement OR character hand-grip state] — the only [Canonical Tier-1 Prop/Weapon Name] in frame. *(Omit `[prop]:` if the scene has no Tier-1 Hero Prop/Weapon)*

[sound]:
[Ambient room/outdoor tone, synchronized tactile Foley sounds tied to shots, and acoustic tension].

Shot 1 (00:00-00:03) - [Interior/Exterior], [shot scale], [camera angle / movement]
[1–2 short natural sentences (15–30w) describing Proper_Name_A's initial action/mask and micro-expression — NO <<<Image X>>> tag repeated here, NO clothing/age words].
[Proper_Name_A] ([vocal timbre/maturity], [delivery tone]): "[Line 1: 4–10 words]"

Shot 2 (00:03-00:05) - [Close-up / Insert], [fixed shot / subtle movement]
[1–2 short natural sentences describing the decisive prop action, lock/latch, or micro-visual reveal].
[Proper_Name_A] ([spatial anchor if off-screen], [vocal timbre/maturity], [delivery tone]): "[Optional short reaction/question: 4–8 words]"

Shot 3 (00:05-00:08) - [Interior/Exterior], [shot scale], [over-the-shoulder perspective / tracking / angle]
[1–2 short natural sentences describing the state transition from False Calm to Freeze/Shock: e.g., "Seen past Proper_Name_B's shoulder in the foreground, Proper_Name_A freezes mid-action. Proper_Name_A's polite smile fades into a tense stare..."].

Shot 4 (00:08-00:10) - [Medium close-up / Close-up], [side slider shot / low angle / fixed frame]
[1–2 short natural sentences using Selective Face Obscuration or Full-Face Emotional Acting payoff: e.g., "The camera avoids Proper_Name_B's full face, showing only Proper_Name_B's lower face, jawline, firm mouth, and index finger tapping twice on the tarnished brass truck keyring. A cold, knowing half-smile tugs at the corner of Proper_Name_B's lips."].
[Proper_Name_B] ([vocal timbre/maturity], [calm understated tone]): "[Closing Line: 2–6 words]"

Master-level cinematography and composition, smooth dynamic camera pacing, atmospheric sound design.
Strict visual consistency: maintain 100% identical facial features, beauty, hairstyle, exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.
Do not generate subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.
```

### 8.2 Template B — Exclusive `15.0s` Action / Chase / Ambush / Combat Scene (`@CombatDirector` · `5–6 Shots`)
```text
[Time of Day] · [Interior / Exterior] · [Location Title]
Style: [Visual Style Specification].

[context]:
[Evocative Location Name in Natural English] <<<Image 1>>> (100% architectural layout, furniture, and lighting strictly refer to this reference image), [time of day]. [5-Vector Tactical Environment: architectural corridor/street/arena layout, lighting, shadows, and interactive/VFX surface details].

[subject]:
[Proper_Name_A] <<<Image 2>>> (100% facial features, beauty/handsome appearance, hairstyle, body proportions, and exact outfit strictly refer to this reference image): [Initial spatial anchor and posture at 00:00 — ZERO clothing/age words] — the only [Proper_Name_A] in frame.
[Proper_Name_B] <<<Image 3>>> (100% facial features, beauty/handsome appearance, hairstyle, body proportions, and exact outfit strictly refer to this reference image): [Initial spatial anchor and posture at 00:00 — ZERO clothing/age words] — the only [Proper_Name_B] in frame.
[Proper_Name_C] <<<Image 4>>> (100% facial features, beauty/handsome appearance, hairstyle, body proportions, and exact outfit strictly refer to this reference image): [Staged at the ambush/interception point, (No objects should appear in the character's hands) if unarmed OR holding Tier-1 weapon in right hand with left hand empty — ZERO clothing/age words] — the only [Proper_Name_C] in frame.

[prop]:
[Canonical Tier-1 Weapon/Artifact Name] <<<Image 5>>> (100% shape, material, engravings, proportions, and visual details strictly refer to this reference image): [Exact 00:00 hand-grip state (e.g., gripped firmly in Proper_Name_A's right hand while left hand remains empty) or resting placement] — the only [Canonical Tier-1 Weapon/Artifact Name] in frame. *(Omit `[prop]:` if unarmed)*

[sound]:
[Ambient night/interior tone, rapid footsteps, sudden stop friction, low energy/rune hum, and cold vocal resonance].

Shot 1 (00:00-00:03) - [Exterior/Interior], [medium close-up], [slight handheld camera shake / slow push-in]
[1–2 short natural sentences establishing the calm or tense opening beat between Proper_Name_A and Proper_Name_B].
[Proper_Name_A] ([vocal timbre/maturity], [soft tone]): "[Short setup line: 3–6 words]"

Shot 2 (00:03-00:06) - [Close-up], [side face shot / fixed shot]
[1–2 short natural sentences executing the Snap Freeze: Proper_Name_A wears a gentle smile, then her expression freezes abruptly. She glances past Proper_Name_B's shoulder toward behind them, all warmth fading from her eyes, replaced by pure panic].
[Proper_Name_A] ([vocal timbre/maturity], [low abrupt tone]): "[2–4 words, e.g., I'm sorry.]"

Shot 3 (00:06-00:10) - [Exterior/Interior], [long tracking follow shot]
[1–2 short natural sentences of full-speed locomotion/flight/pursuit with 0 spoken dialogue: Proper_Name_A turns and hurries away, looking frantic. She flees through the empty alley, evading the danger she spotted].

Shot 4 (00:10-00:13) - [Wide shot transitioning to fixed frame], [middle of the street / corridor]
[1–2 short natural sentences executing the Hard Stop + VFX/Trap activation with 0 spoken dialogue: Proper_Name_A stops sharply, her body going rigid. Faint pale red ancient rune patterns glow faintly and flow across the empty road beneath her feet].

Shot 5 (00:13-00:15) - [Medium shot], [rear camera angle]
[1–2 short natural sentences revealing the Hunter/Boss blockade: Proper_Name_A instantly spins around to run back, only to find Proper_Name_C standing silently in the middle of the road (No objects should appear in the character's hands), shrouded in shadows with overwhelming oppressive aura].
[Proper_Name_C] ([vocal timbre/maturity], [deep calm tone]): "[2–5 words checkmate line, e.g., Miss, you seem lost.]"

Master-level cinematography and composition, smooth dynamic camera pacing, atmospheric sound design.
Strict visual consistency: maintain 100% identical facial features, beauty, hairstyle, exact outfit, and exact weapon/prop design from the reference images across all shots without morphing or wardrobe changes.
Do not generate subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.
```

### 8.3 The 9 Non-Negotiable Technical Laws of the Unified Multi-Shot Storyboard Format
1. **Double-Lock 100% Reference & Single `<<<Image X>>>` Declaration Law**: Keep `<<<Image X>>>` intact and place `(100% ... strictly refer to this reference image)` immediately after it in `[context]:`, `[subject]:`, and `[prop]:`. Declare `<<<Image X>>>` **ONLY ONCE** in the headers — **NEVER repeat `<<<Image X>>>` inside `Shot 1..N` or speaker headers**, and seal the prompt with the `Strict visual consistency: ...` footer.
2. **Dedicated `[prop]: <<<Image X>>>` Block for Tier-1 Hero Props, Weapons & Key Artifacts**: Whenever a Tier-1 weapon, heirloom, seal, or key contract appears in a scene, bind its isolated 4-view reference sheet (`prop-[name].jpg` $\to$ `<<<Image X>>>`) inside `[prop]:` with its exact `00:00` resting placement or hand-grip (`right hand` with `left hand empty`, or `spaced two-handed grip`).
3. **Proper Character Names Only**: Never use generic labels (`Woman`, `Man`, `Girl`, `Boy`, `the father`, `the hunter`) as subject headers or speakers. Every character uses their fixed proper name from `setting.html`.
4. **Zero-Costume, Zero-Age & Single Vocal-Timbre Tag Law (`Gates 3A & 3E`)**: Because `<<<Image X>>>` locks wardrobe and physical appearance 100%, **strictly ZERO clothing/garment words (`in a black leather jacket`, `in a dark suit`, `skirt`, `coat`) and ZERO numeric ages or age/hair/beard adjectives (`32-year-old`, `young blonde`, `silver-bearded`, `aged weathered hand`)** anywhere in the prompt. Encode vocal maturity and emotion inside **ONE single compact parenthetical right after `[Proper_Name]`**:
   - *Young Adult Female*: `Elena (soft airy soprano, breathless tone): "..."` / `Sophia (clear youthful alto, low steely tone): "..."`
   - *Young Adult Male*: `Bradley (smooth tenor, confident warm tone): "..."` / `Kael (crisp tenor, calm steady tone): "..."`
   - *Mature / Elder Female*: `Martha (warm maternal alto, soft affectionate tone): "..."`
   - *Mature / Elder Male*: `Harold (deep weathered baritone, calm unhurried tone): "..."` / `Dante (deep resonant baritone, calm tone): "..."`
5. **1–2 Short Natural Sentences per Shot (`15–30 Words`)**: Express **1 clear state transition (`State A ➔ State B`)** per shot in natural cinematic English. Strictly ban mechanical `→` arrows, clinical muscle jargon (`masseter`, `orbicularis`), and bloated multi-clause paragraphs.
6. **Selective Face Obscuration (Deploy When Mystery or Tactile Focus Calls For It)**:
   - *Back/Silhouette*: `The camera avoids [Name]'s full face, showing only his back and shoulders in silhouette.`
   - *Lower-Face / Hand Micro-Acting*: `The camera avoids [Name]'s full face, showing only [Name]'s lower face, jawline, Adam's apple, and index finger tapping twice on the brass keyring.`
7. **Off-Screen `L-Cut` Dialogue Over Visual Inserts**: Allow an off-screen character (`[Name] (outside the door / across the table / from behind, [vocal timbre], [tone])`) to speak over an interior tracking shot or a `2s` prop/lock close-up (`Shot 2`), keeping pacing tight without wasting a cut.
8. **Empty-Hand Anti-Glitch Lock**: Whenever an unarmed character or hunter stands/moves empty-handed in a tense or action shot, append `(No objects should appear in the character's hands)` so the AI video model never hallucinates random weapons or props.
9. **Kinetic Contrast in `15.0s` Action/Chase (`@CombatDirector`)**: Alternate camera and body velocity across `Shot 1..5`: *Intimate Handheld (`Shot 1`) ➔ Fixed Snap-Freeze Close-Up (`Shot 2`) ➔ 4s Long Tracking Follow Shot with 0 Dialogue (`Shot 3`) ➔ Wide-to-Fixed Hard Stop + Ground/Environmental VFX (`Shot 4`) ➔ Rear-Angle Spin into Immovable Boss (`Shot 5`)*.

---

## §9 — DURATION MODES: `10.0s` (`@DIRECTOR`) VS. `15.0s` (`@COMBATDIRECTOR`) VS. `30.0s`

| Mode | Owner & When | Storyboard Shot Count & Timing |
|---|---|---|
| **`10.0 s` (Default Standard)** | **`@Director`**: All standard dialogue, psychological drama, confrontation, and twist scenes (`[🎭 MODEL TIÊU CHUẨN · 10.0s]`) | **`3 – 4 Shots`** (`00:00-00:03`, `00:03-00:05`, `00:05-00:08`, `00:08-00:10`), `1–2` short sentences/shot, `12–22w` dialogue total, `2–6w` closing line |
| **`15.0 s` (Exclusive Action / Chase / Ambush / Combat)** | **`@CombatDirector`**: All high-motion action, chase, pursuit, supernatural trap, and combat scenes (`[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 15.0s]`) | **`5 – 6 Shots`** (`00:00-00:03`, `00:03-00:06`, `00:06-00:10`, `00:10-00:13`, `00:13-00:15` or `3s-3s-2s-2s-3s-2s`), `1–2` short sentences/shot, `0` dialogue in chase/VFX shots, `2–5w` checkmate line |
| **`30.0 s` (Explicit User Request Only)** | **`@Director` / `@CombatDirector`**: Extended 3-act sequence when explicitly requested | **`8 – 10 Shots`** across `00:00-00:30` |

---

## §10 — QUICK PRE-FLIGHT CHECKLIST (PER SCENE)

1. **Header & Style**: Opens with `[Time] · [Interior/Exterior] · [Location Title]` and `Style: ...`?
2. **Single `<<<Image X>>>` Lock**: Are `<<<Image X>>>` tags declared **ONLY ONCE** in `[context]:` and `[subject]:` and **0 times** inside `Shot 1..N`?
3. **Zero-Costume & Zero-Age**: Are all clothing words (`jacket`, `suit`, `skirt`, `dress`) and age/hair/beard words (`young`, `blonde`, `silver-bearded`) 100% purged from `[subject]:` and `Shot 1..N`?
4. **Shot Format & Economy**: Does each shot follow `Shot N (00:XX-00:YY) - [Interior/Exterior], [scale], [angle/move]` with **1–2 short natural sentences (`15–30w`)** and separated speaker dialogue block?
5. **Psychological Subversion & Closing Line**: Does the scene follow the *Mask ➔ Crack/Micro-Visual Reveal ➔ Role Reversal* curve and end on a calm **`2–6 word` understatement line**?
6. **Footer Lock**: Ends with `Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design.` + `Do not generate subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.`?

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
| Dialogue Word Cap (Gate 4B): Single-Speaker Shot target 25–30 words (hard cap ≤ 32w); Two-Shot exchange ≤ 15 words per speaker (total ≤ 32w) | Hard Constraint |
| Phases contiguous, non-overlapping, start at 00:00, end at the clip duration 10s / 15s / 30s (Gate 3M) | Hard Constraint |
| **Zero Cumulative Timestamps**: Every scene prompt MUST start at 00:00 for third-party AI generators; NEVER use cumulative episode timestamps like [00:10–00:20] in prompts (Gate 3M) | Hard Constraint |
| **Zero Dead Air Law**: continuous micro-action density spanning 100% of the clip duration; zero "holds still", "stands rigid", or idle buffers (Gate 3O) | Hard Constraint |
| Clip duration strictly 10s, 15s, or 30s per scene (Gate 3M accepts 10 / 15 / 30) | Hard Constraint |
| No lip-synced line during a downward POV; no lip-sync while the camera is in fast travel (whip, crane travel, fast orbit) | Hard Constraint |
| **Subject-to-Scale Invariance (Frame Capacity Law)**: Single-subject scales (MCU, CU, Choker, Head-On, ECU) strictly direct ONLY the primary in-frame subject; secondary characters MUST NOT have facial biomechanics, expressions, or physical reactions described within that phase (Gate 3P) | Hard Constraint |
| Canonical prompt syntax (§8) | Hard Constraint for new deliverables (the audit warns on legacy syntax) |
| Speech rates, lip-sync windows, move durations, density tables | Craft Defaults; break them with a `BREAK:` line |

---

## §1 — CINEMATIC MENTAL MODEL & COUNTING UNITS

### 1.1 The Invariant 10-Second Shot Mental Model (10s Là Một Cú Máy / Shot, Không Phải Một Cảnh)
- **A 10-second clip is a SHOT (cú máy), not an entire scene.** A dramatic scene consists of multiple shots stitched together (e.g., 9 shots = 90s sequence).
- **Primary Rule: One Speaker Per Shot via Shot - Reverse Shot**:
  - In cinema, dialogue is edited via shot-reverse-shot across consecutive shots:
    - *Shot 1 (10s)*: Character A speaks (Camera on A; medium close-up or close-up).
    - *Shot 2 (10s)*: Character B speaks or reacts (Camera on B; reverse angle or over-the-shoulder).
    - *Shot 3 (10s)*: Returns to Character A.
  - *Why this is essential for AI Video (Veo, Sora, Kling)*: Each shot features only one active speaking face. Lip-sync, facial coherence, and vocal timbre remain 100% stable with zero voice bleeding or cross-talk morphing.
- **The Two-Shot Exception (When 2 Speakers Are Allowed in a Single 10s Shot)**:
  - Allowed ONLY when:
    1. Each person speaks at most 1–2 short volleys (**5–10 words each**) for rapid Q&A, snappy bickering, or urgent interruptions.
    2. Framed as a **Two-shot / Three-shot** (both in frame simultaneously) to deliberately evoke high tension, frantic bickering, or raw everyday realism.
    3. **The 15-Word Shot-Split Law**: If any single speaker speaks **> 15 words** in that shot $\to$ **MUST SPLIT THE SHOT**.

### 1.2 Counting Units
- **Vietnamese** dialogue is counted in **syllables** (every whitespace token is one syllable: `Em mệt quá anh ơi` = 5 syllables).
- **English** dialogue is counted in **words**.
- Plan lines in **seconds and dramatic beats**, not just raw mechanical tokens.

### 1.3 The 4 Cinematic Continuity Locks for Stitching 10s Shots (Bộ Tứ Khóa Xuyên Suốt)
When assembling discrete 10-second AI video shots into a seamless cinematic sequence on an NLE timeline (Premiere, DaVinci, CapCut), four mandatory continuity locks guarantee that cuts feel natural, fluid, and coherent rather than fragmented or jarring:

1. **Lock 1: Spatial & 180° Axis Gaze Vector Lock (Khóa Trục Không Gian & Đường Mắt Bất Biến)**:
   - *Screen-Direction Invariance*: If Character A is framed on Screen-Left looking toward Screen-Right, and Character B is on Screen-Right looking toward Screen-Left, this geometry **must never flip** across shot-reverse-shot cuts unless the camera physically orbits across the axis on screen.
   - *Ground & Architectural Anchor*: Every shot within the same sequence must cite the identical floor/surface noun phrase (`encaustic cement tiles`, `packed earthen floor`) and directional key light source to prevent AI latent background hallucinations.
2. **Lock 2: Kinetic Momentum Baton Relay (Gậy Tiếp Sức Động Năng & Action Match-Cut)**:
   - *The Relay Principle*: In the final 1.0s–1.5s of Shot N (`[00:08.5–00:10.0]`), the active character begins an observable physical movement (raising a hand to wipe a tear, turning a head toward the door, letting a utensil slip).
   - *The Catch*: In the opening 1.0s–1.5s of Shot N+1 (`[00:00–00:01.5]`), from the new camera angle or reverse shot, that physical movement is **caught in mid-motion and completed**, or its impact lands on the counterpart's reaction.
   - *Result*: When cut on action in the edit, the cut point disappears completely, creating an unbroken ribbon of physical kinetic energy. Zero action restarts; zero frozen frames.
3. **Lock 3: Auditory Suture & Continuity Bridges (Cầu Nối Âm Thanh Điện Ảnh: L-Cut, J-Cut & Room Tone)**:
   - Cinema uses sound to suture visual cuts together so the audience perceives one continuous world.
   - *L-Cut (Split Audio Tail)*: Character A's final spoken words or a decisive sound in Shot N spill 1.0s–1.5s into Shot N+1 over Character B's silent reaction face.
   - *J-Cut (Pre-Lap Sound)*: An approaching footstep, door opening creak, or urgent breath from Shot N+1 begins 1.0s before the visual cut occurs.
   - *Diegetic Room Tone Suture*: The atmospheric background sound (rain on corrugated tin, steady ceiling fan thrum, distant wind) remains uniform across all contiguous shots within the space.
4. **Lock 4: Physical Handover Ledger (Sổ Bàn Giao Trạng Thái Vật Lý & Đạo Cụ)**:
   - Recorded strictly in Code Block 2: Character 3D positions, facial expression at `00:10.0`, prop physical states (held in left hand, placed on shelf, shattered into fragments) transfer 1:1 into the opening frame of Shot N+1.

### 1.4 Multi-Spatial Sequence Architecture (Giải Thoát Khỏi Chiếc Hộp Một Phòng)
- **The Anti-Box Mandate**: Sticking 10 consecutive shots into a single 15m² room to maintain easy continuity destroys cinematic scale and creates stagey, sterile melodrama.
- **Cinematic Sequence Breakdown**: A 100s–120s production must be organized into **2 to 3 dynamic physical or psychological Sequences**:
  - *Sequence 1 (Shots 1–3 — Atmospheric Setup & Compressed Tension)*: Intimate tactile space (hallway, quiet room corner, balcony, kitchen hearth) where the protagonist's dilemma is established through physical action and visual metaphor with minimal or zero dialogue.
  - *Sequence Boundary Transition*: Connected to Sequence 2 via a **Sensory Match-Cut** (sound bridge, door threshold crossing, or visual graphic match), moving the narrative forward in space and time.
  - *Sequence 2 (Shots 4–7 — High-Stakes Collision Core)*: The central clash or revelation in the main narrative space, alternating dominant shots and reaction shots.
  - *Sequence 3 (Shots 8–10 — Aftermath & Transformative Resonance)*: A shift in perspective, isolation, or the morning light settling over the consequence, leaving the audience with an unforgettable cinematic image.

---

## §2 — SPEECH RATE & 10S WORD BUDGET BY GENRE

| Delivery Mode | Vietnamese (syl / s) | English (words / s) | 10s Single-Speaker Word Budget | Target Genres & Pacing |
|---|---|---|---|---|
| **Sitcom / Comedy / Fast Banter** | 3.8 – 5.0 | 2.2 – 2.8 | **25 – 30 words** (Single speaker) or **25–30w total** (Two-shot split 5–10w each) | High-energy, snappy pacing. Structure: Setup ➔ Reaction ➔ Punchline in final 2–3s. |
| **Calm Conversation / Everyday Slice-of-Life** | 3.5 – 4.5 | 2.0 – 2.5 | **25 – 30 words** | Natural conversational cadence with breathing room (6.5s – 7.5s speech). |
| **Psychological Drama / Heavy Emotion / Melodrama** | 2.5 – 3.5 | 1.3 – 1.8 | **15 – 20 words** | The unspoken matters more than the spoken. 4–5s pregnant pauses, trembling breaths, eye shifts. |
| **Panic / Emergency Command / Stichomythia** | 4.5 – 6.0 | 2.5 – 3.3 | **20 – 28 words** (staccato volleys) | Rapid adrenaline pacing, clipped consonants, urgent interruptions. |

**Buffer Law for 10s Shots**:
- Always leave **0.5s – 1.0s buffer at the head** of the shot (establishing subject, breath intake before speech).
- Always leave **0.5s – 1.5s buffer at the tail** of the shot (clean mouth closure, living somatic reaction/settle before cut).

---

## §3 — LIP-SYNC WINDOWS & THE 3 CINEMATIC DIALOGUE CONTINUITY TECHNIQUES

### 3.1 Lip-Sync Timing Windows
- A spoken line **starts ≥ 0.5 s** after its phase begins (face established, breath drawn).
- A spoken line **ends ≥ 0.8 s – 1.0 s** before the shot ends (mouth closes cleanly on screen).
- A phase that carries a line lasts **≥ line duration + 1.0 s**.

### 3.2 The 3 Advanced Techniques for Seamless Multi-Shot Dialogue Continuity
1. **L-Cut (Split Audio Tail)**:
   - Visual cuts to Character B, but Character A's voice continues for 1.0s – 2.0s into the new shot.
   - The audience hears A finish the line while observing B's immediate somatic reaction (hurt, guilt, shock). This is the hallmark of professional cinema editing.
2. **J-Cut (Pre-Lap Dialogue)**:
   - Character B's voice ignites 0.5s – 1.5s BEFORE the visual cut to Character B occurs.
   - Creates fluid narrative propulsion, pulling the audience into the next shot.
3. **The Reaction Shot (Shot Phản Ứng — Zero Words Spoken)**:
   - Character B speaks strictly ZERO words.
   - The shot is dedicated entirely to silence, breathing, moistening eyes, a tightening jaw, or an averted gaze. In drama, silence is often far more devastating than a spoken line.
4. **Voice-Over (V.O.) / Internal Monologue**:
   - Character on screen remains physically silent with sealed lips, while internal thought audio plays. Perfect for 10s shots without lip-sync stress.

### 3.3 Genre Execution: Sitcom vs. Psychological Drama
- **Sitcom Architecture**:
  - Pacing is rapid; two-shots and three-shots are encouraged.
  - Setup ➔ Reaction ➔ Punchline: Deliver the punchline in the last 2–3s and cut immediately on the laugh. Never let visual dead air linger after the punchline.
  - The Reaction Shot (looking at camera, breaking 4th wall, deadpan eye-roll) is the primary engine of comedy.
- **Psychological Drama Architecture**:
  - Subtext over exposition: What is unsaid is paramount.
  - Stick strictly to one speaker per 10s shot (15–20 words), leaving generous space for hesitation, broken sentences, and swallows.
  - Pair with L-cuts to let devastating accusations linger over the victim's silent face.

---

## §4 — ACTION CAPACITY PER SECOND

| Window | Body capacity | Visible emotion | Spoken capacity |
|---|---|---|---|
| 1.0 – 2.0 s (micro-beat, insert, reaction) | One micro-action: head turn, jolt, hand slam, grip | Pupil, swallow, nostril, lip | 0–5 counted words |
| 2.5 – 4.5 s (standard beat) | One primary move: 3 steps and stop, hand an object across, turn around | Jaw clench, throat swallow, breath change | One line (VN ≤ 14 syl, EN ≤ 9 words) |
| 5.0 – 7.0 s (extended beat) | One cause-and-effect chain: walk, meet obstacle, stop, face | Two-stage shift (shock → resolve) | One full line + reaction, or two short lines |
| 1.0 – 2.5 s (terminal settle) | No gross motor movement; contact points hold | Breathing, eye moisture, drifting air | 0 words |

**One primary move + one reaction per phase** remains a Hard Constraint (limb morphing otherwise).

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

## §6 — SHOTS AND CUTS

| Clip | Track B shots | Track A phases | Track AB (hybrid) |
|---|---|---|---|
| 10 s | 2 – 4 | 2 – 4 | 2 – 3 shots, one of them a take ≥ 5 s holding 2+ phases |
| 15 s | 2 – 5 | 3 – 5 | 2 – 4 shots, take ≥ 7 s |
| 30 s | 4 – 8 | 5 – 8 | 3 – 6 shots, take ≥ 10 s |

- Minimum shot length: **≥ 2.0 s**, or **≥ line duration + 1.0 s** when the shot carries a line. Inserts ≥ 1.5 s. Reactions ≥ 1.5 s.
- Never cut between two identical scales of the same character without changing the angle by ≥ 30°.
- Cut on a change: a line landing, a look, an action completing (the Blinking Eye Law).
- Change scale or angle where power changes (Doctrine §2.2).

### 6.1 Choosing the track (A / B / AB)

| Track | Choose it when… | Shape inside 10 s |
|---|---|---|
| **A — one continuous take** | The viewer must stay inside one breath, one body, one unbroken pressure (confession, realization, intimacy, dread, a fall). | 2–4 phases, zero cuts; scale and angle change only through camera movement. |
| **A-Locked — locked-off static take** | The acting reaches maximum emotional truth; camera motion would dilute empathy (wordless weeping, razor confession, truth-bomb shock). | 2–3 phases in one fixed setup; camera is 100% stationary on a tripod; 100% of motion comes from somatic micro-acting and living atmosphere. |
| **B — multi-shot** | The viewer must see both sides of a collision: whose move lands, who absorbs it. | 1–4 shots on the 180° axis; each later shot opens with `Cut to`. |
| **AB — hybrid take + cut** | Pressure accumulates in one breath, **but the landing must be seen through another eye** — the witness, the prop, the reverse. The cut is the punctuation mark of the take. | One take ≥ 5 s carrying 2+ phases, plus 1–2 cuts. |

Hybrid shapes (illustrative, not templates):
- **Take → Button** — a moving take builds the beat (0–7 s), then one cut to a reaction or insert lands it (7–10 s).
- **Trigger → Take** — a short insert or reaction fires the scene (0–2 s), then a cut into one continuous take lets the pressure accumulate (2–10 s).
- **Take → Cut → Take** — two takes, one cut placed exactly on the power shift.

Each added cut raises the risk of identity and costume drift in AI generation, so a hybrid keeps the cut count low and every shot fully re-anchored in prose (names, positions, light).

---

## §7 — DENSITY PER 10S SHOT (BY GENRE & VOICE MODE)

| Shot Type & Genre | Mode | Spoken Word Budget (VN) | Spoken Word Budget (EN) | Speech Share (% of 10s) |
|---|---|---|---|---|
| **Single-Speaker (Sitcom / Slice-of-Life)** | 1 Active Speaker | **25 – 30 syllables** | 12 – 16 words | ~65 % – 75 % |
| **Single-Speaker (Psychological Drama / Heavy)** | 1 Active Speaker | **15 – 20 syllables** | 8 – 12 words | ~40 % – 55 % |
| **Two-Shot / Multi-Speaker (Sitcom Fast Banter)** | 2 Speakers (Two-Shot) | **25 – 30 syllables total** (5–10w each; cap ≤ 15w/speaker) | 12 – 16 words total | ~60 % – 70 % |
| **Reaction Shot / Pure Physical Silence** | Model 0 (Silence) | **0 syllables** | 0 words | 0 % (100% Visual) |
| **Voice-Over (V.O.) / Inner Monologue** | V.O. (Sealed Lips) | **20 – 30 syllables** | 12 – 18 words | ~60 % – 75 % |

The upper bounds preserve the 0.5s–1.0s lead-in breath and 0.5s–1.5s mouth closure / reaction settle. Lower bounds apply to scenes that use dialogue; silent reaction scenes (Model 0) and pure visual action shots are 100% first-class citizens. The linter permits up to 75% speech share for single-speaker 10s shots.

---

## §8 — CANONICAL PROMPT SYNTAX (ONE SYNTAX FOR ALL DURATIONS)

```
Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Style: [visual style header]. [Track A — one continuous take, zero cuts | Track B — multi-shot sequence cut on the 180-degree axis | Track AB — one continuous take punctuated by a cut on the 180-degree axis].

[context]:
[Location] [100% Refer to image <location_ref>], [time of day]. [Key light source, direction, natural color tone; atmospheric medium].

[subject]:
[name_a] [100% Appearance, attire, and facial features Refer to image 1], [initial spatial anchor to in-scene architectural fixture], [initial physical posture & tactile contact] — the only [name_a] in frame.
[name_b] [100% Appearance, attire, and facial features Refer to image 2], [initial spatial anchor to in-scene architectural fixture], [initial physical posture & tactile contact] — the only [name_b] in frame.

[PROP]:
[key_fixture_description]; [prop_name] [100% Refer to image <prop_ref>]

Diegetic room acoustics: [room tone and Foley].

[00:00–00:03.5] [Scale], [angle], [camera move] — [Directing participating characters across the 4 Vectors: (1) State/Posture, (2) Action, (3) Emotion/Expression, (4) Spatial Location]. Focus on [name].
[name] says : “ [line] ”（Voice of a [N]-year-old [man/woman] from [region]; [vocal timbre], [cảm xúc khi nói]）

[00:03.5–00:07.0] Cut to [scale], [angle], [move] — [Directing participating characters across 4 Vectors: State, Action, Emotion, Spatial Location]. Focus on [name].

[00:07.0–00:10.0] [Scale], [angle], [move] — [terminal beat: 4 Vectors for characters in frame, breathing, micro-expression, deceleration; never a frozen frame].

Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored to the architecture; characters move only where the action says they move.
Do not generate subtitles, dialogue text, titles, timestamps, or written text anywhere in the video. Do not render duplicate characters or extra props.
```

Rules:
- A phase line = `[start–end]` + **one short camera clause** (scale, angle, move) + `—` + prose. Track B phases after the first start with `Cut to`. In Track AB, only a phase that begins a new shot starts with `Cut to`; a phase that continues the take starts with `In the same take`.
- **Subject-to-Scale Invariance & Frame Capacity Law (Single-Subject Framing Constraint)**: Single-person scales (`Medium close-up`, `Close-up`, `Choker`, `Head-on`, `Extreme close-up`) strictly frame and direct **ONE human subject**. Secondary characters are spatially Off-Screen (`O.S.`) and MUST NOT have their actions, gestures, breathing, or facial expressions described within that phase (doing so triggers severe AI spatial hallucinations and mutant anatomy). To direct two interacting characters simultaneously, the shot MUST be declared as a `Medium two-shot (M2S)`, `Over-the-shoulder (OTS)`, or `Two-shot profile`. Non-character inserts (`Macro insert`) strictly forbid facial acting and dialogue.
- **Somatic Action-Speech Fusion Standard (Organic Speech Action)**: Dialogue is an organic physical action, never a detached mechanical block. While `says :` is supported, dialogue lines are encouraged to dynamically incorporate bodily prelude and expressive speech-action verbs: `[name] [bodily prelude / emotional physical action], [expressive action-verb] : “ [line] ”（Voice of [demographic]; [vocal timbre: trầm hay bổng], [cảm xúc khi nói], [inferred paralinguistic acoustic emotion tags: e.g. sharp staccato delivery, strained rasp, explosive consonants]）`. Examples of expressive verbs: `furiously snapping :`, `breathlessly pleading :`, `harshly barking :`, `bitterly hissing :`, `softly murmuring :`, `icily retorting :`. This binds facial micro-muscles, chest respiration, and vocal articulation into a single unified physical tensor for DiT diffusion models, eliminating rigid "puppet mouth" artifacts.
- **STRICT PROHIBITION OF LITERAL PLACEHOLDERS**: NEVER write the literal string `"audio tag"` or `"cảm xúc khi nói"` into prompts. The system must always infer authentic paralinguistic acoustic tags (e.g. `[commanding harsh bark, impatient ragged breath, sharp staccato delivery]`).
- **No** `△`, **no** `|` pipes, **no** `Shot 1` / `Phase 1` labels inside Code Block 1. The audit warns on legacy syntax.
- The track is declared in the style line; the same track appears on the scene badge and in the `[TIMELINE SHOTS]` card. **Label must match content:** Track A contains no `Cut to`; Track B and Track AB contain at least one; Track AB also contains one take of ≥ 5 s holding 2+ phases.
- Use the generator's vocabulary for moves: `slow push-in`, `slow pull-out`, `lateral glide`, `90-degree arc`, `pedestal up`, `rack focus`, `static camera`. Never lens millimeters, f-stops, fps, brands, Kelvin, or coordinates.

### 8.1 Worked Examples across Action Dynamics Archetypes (Track B, Vietnamese)

> ⚡ **CRITICAL DIRECTORIAL MANDATE**: Track B multi-shot cuts MUST NOT be treated as a rigid 3-phase template ending in an automatic silent reaction shot. The phase layout and timing are strictly governed by the **Tier 2 Action Dynamic Archetype** (Doctrine §3.3):

#### Example 1: High-Velocity Stichomythia (Dạng 1: Đấu kiếm leo thang 3 nhịp — Zero Dead Air)
*Cadence: Rapid Sparring. Verbal and physical clash volleys continuously up to 00:09.5. STRICTLY ZERO IDLE BUFFER.*
```text
[00:00–00:03.5] Over-the-shoulder shot past minh_khang, slight low angle, fast track-in — ma_ba steps forward aggressively, thrusting a crumpled hospital receipt into the air inches from his face. Focus on ma_ba.
ma_ba harshly barks : “ Mầy nói cho rõ, tiền nằm ở đâu?! ”（Voice of a 56-year-old Southern Vietnamese woman; sharp piercing shout, impatient ragged breath, explosive consonants）

[00:03.5–00:07.0] Cut to reverse over-the-shoulder past ma_ba, eye level, static camera — minh_khang snatches the receipt mid-air, ripping it in half with trembling violent hands. Focus on minh_khang.
minh_khang bitterly snarls : “ Tiền con trả viện phí cho vợ con hết rồi! ”（Voice of a 27-year-old Southern Vietnamese man; breathless fierce defense, strained rasp, desperate defiance）

[00:07.0–00:10.0] Cut to close-up on ma_ba, low angle, fast push-in — ma_ba’s palm whips across in a sharp slap gesture that halts inches from minh_khang’s cheek; chest heaving violently, eyes blazing.
ma_ba furiously hisses : “ Mầy muốn chọc chết tao hả?! ”（Voice of a 56-year-old Southern Vietnamese woman; venomous breathless whisper, trembling rage）
```
*Timing check: Line 1 ≈ 2.5s (inside 3.5s phase); Line 2 ≈ 3.0s (inside 3.5s phase); Line 3 ≈ 2.4s (inside 3.0s phase). Speech fills active beats without dead air; physical action carries every cut.*

#### Example 2: The Somatic Aftershock (Dạng 3: Dư chấn câm lặng & Vi phản ứng sinh học)
*Cadence: Truth Bomb Shock. Speech terminates early at ~00:04.5; the second half is dedicated exclusively to somatic biological shock.*
```text
[00:00–00:03.5] Medium shot, slight low angle, static camera — ma_ba sets the folded steel hammock frame onto the floor tiles with a sharp clang; inside the pine crib a soft blanket rustles. Focus on ma_ba.
ma_ba says : “ Võng này ba thằng Khang nằm lớn đó. ”（Voice of a 56-year-old woman from the Mekong Delta; proud unhurried tone, firm traditional claim staking family history）

[00:03.5–00:07.0] Cut to an over-the-shoulder shot past ma_ba, eye level, static camera — minh_khang crouches, lifts the hammock frame with both hands and turns toward the doorway, leaving the floor tiles clear. Focus on minh_khang.
minh_khang says : “ Để con mang ra sau hè treo cho má mát. ”（Voice of a 27-year-old Southern Vietnamese man; warm low gentle baritone, soft filial placation masking guilt）

[00:07.0–00:10.0] Cut to a close-up on ma_ba, eye level, slow push-in — the emptied right hand hangs in the air, fingers curling slowly inward as the gaze drifts to the crib; lips stay closed, breathing slows.
```
*Timing check: Dialogue ends at 00:06.5; 00:07.0–00:10.0 is pure somatic reaction, letting the truth sink into the character's body.*

#### Example 3: Track A-Locked — The Locked-Off Performance Take (Diễn Hoạt Tĩnh Siêu Đậm Đặc, Zero Camera Move)
*Cadence: Intimate Confession / Somatic Agony. The camera is 100% stationary on a tripod; 100% of the movement is driven by micro-acting, tear physics, and dancing sunbeams.*
```text
[00:00–00:03.5] Medium close-up, eye level, completely stationary static camera on locked tripod, zero camera movement — my_duyen kneels motionless beside the pine crib, right hand gripping the top wooden rail until knuckles whiten; shallow rapid breaths heave her chest as her gaze fixes downward on the woven blanket; microscopic dust motes drift lazily through the warm diagonal sunbeam. Focus on my_duyen.

[00:03.5–00:07.0] In the same locked static frame, eye level — my_duyen swallows hard against a tight throat, her jaw quivering; she lifts her gaze slowly toward the doorway, tears catching the golden morning light, and whispers with trembling defiance. Focus on my_duyen.
my_duyen softly whispers : “ Má ơi, con tự ráng gượng được mà má... má bận lòng làm chi... ”（Voice of a 24-year-old Southern Vietnamese woman; choked fragile whisper, strained breathy rasp, suppressed weeping）

[00:07.0–00:10.0] In the same locked static frame, eye level — lips seal tightly as a single tear spills silently down her left cheek; her head lowers two inches, shoulders slumping as she curls her trembling fingers inward against the wooden bar; in the background, sheer window curtains ripple faintly in a gentle draft. Focus on my_duyen.
```
*Directorial check: Zero cuts, zero camera translation. High-density somatic verbs (knuckles whitening, throat swallowing, jaw quivering, tear spilling, head lowering) and environmental motion (drifting dust motes, rippling sheer curtains) prevent the DiT diffusion model from freezing into a still mannequin.*

---

## §9 — DURATION MODES: 10s, 15s, 30s
> **Core Principle**: A scene's macro architecture (`[context]`, `[subject]`, `[Pro]`, acoustics, closing stability) is **100% INVARIANT** across 10s, 15s, and 30s.
> Extending duration from 10s to 15s or 30s is simply **adding shots (Track B/AB) or phases (Track A)** within the same single prompt.
>
> ⚠️ **THE THIRD-PARTY AI RENDER ENGINE LAW (ZERO CUMULATIVE TIMESTAMPS)**:
> In generative video tools (Runway, Kling, Sora, Hailuo, Wan 2.1), **EVERY SCENE IS AN INDEPENDENT RENDER ATOM**.
> The prompt submitted to the third-party AI tool MUST ALWAYS START AT `00:00` (e.g., `[00:00–00:03.5]`, `[00:03.5–00:07.0]`, `[00:07.0–00:10.0]`).
> **NEVER write cumulative episode timestamps** (such as `[00:10–00:20]` or `[00:20–00:30]`) inside the Video Prompt (Code Block 1) or its directing phases! Third-party AI video models render each clip from second 0, and cumulative offsets will confuse the model and destroy temporal coherence.

| Mode | When | How |
|---|---|---|
| **10 s (standard default)** | Standard scene atom. Contiguous 10.0s clip | One prompt, 2–4 phases (Track B: 2–4 shots), internal timeline `00:00–00:10` |
| **15 s** | Extended dramatic scene atom | One prompt, 3–5 phases (Track B: 2–5 shots), internal timeline `00:00–00:15` |
| **30 s** | Commercial / Master long-form scene atom | One prompt, 5–8 phases (Track B: 4–8 shots), internal timeline `00:00–00:30`, built as 3 mini acts (§9.2) |
| **30 s chained** | ONLY if the user specifically requests chaining or generator limits | Three 10 s scenes joined through Code Block 2 handovers |

### 9.1 15 s shape (Single Prompt, expanded shots)
`[00:00–00:04.0]` establish + first move → `[00:04.0–00:09.0]` main exchange / action → `[00:09.0–00:12.5]` turn (the value shift lands) → `[00:12.5–00:15.0]` settle.
Density: Vietnamese 18–36 syllables, English 12–21 words (SSOT: §7). Track A ≤ 3 chained moves.

### 9.2 30 s shape (Single Prompt, expanded shots) — a mini three-act scene
Authored as a single prompt with 5–8 shots/phases, keeping the exact same scene structure as 10s:
- **Act I `[00:00–00:08]`**: arrival and trigger (1–2 shots).
- **Act II `[00:08–00:22]`**: 2–3 exchanges where power shifts at least once (2–4 shots, changing scale or angle on each shift).
- **Act III `[00:22–00:30]`**: the reveal or decision, close shot, then a living settle ≥ 2 s (1–2 shots).

Density: Vietnamese 35–70 syllables, English 25–38 words, ≤ 55 % speech (SSOT: §7).

### 9.3 30 s chained (Alternative fallback only)
- Used only if the user explicitly asks for chaining or generator engine limits prevent 30s single-clip rendering.

### 9.4 Engine support
- `episode_audit_suite.py` reads each prompt's duration from its last time bracket and accepts 10, 15, or 30 s. It checks that phases are contiguous from 00:00 to that duration.
- Show the duration on the scene card (`00:00 – 00:15`).

---

## §10 — QUICK TIMING CHECKLIST (PER SCENE)

1. Duration mode chosen (§9) and stated on the card.
2. Each line timed with §2; each line's phase passes the §3 window.
3. Each camera move ≥ its §5 minimum; motive named.
4. Shot count within §6; no shot under its minimum.
5. Speech share ≤ the §7 limit.
6. Syntax matches §8 (no `△`, no pipes, track in the style line).

---

## §11 — CALIBRATION LOG

Record every real generation that disagrees with a number above:

| Date | Generator + version | Clip | Observation | Number changed (old → new) |
|---|---|---|---|---|
| — | — | — | — | — |

---

## §12 — THE 10-SECOND SCENE BLUEPRINT (ONE PAGE)

The whole scene on one page. Decide in this order; each step feeds the next.

### 12.1 Order of decisions
1. **Intent** (Doctrine §1): what flips between 00:00 and 00:10? No shift, no scene.
2. **Voice mode** (Doctrine §4): dialogue, solo, silence, V.O., … — per scene, with a reason.
3. **Track** (§6.1): A, B, or AB.
4. **Beats → phases**: one phase per beat (trigger, turn, landing). Split points come from the beats, never from a fixed pattern.
5. **Lines → seconds** (§2, §12.4): time every line; size each phase to its line + 1.0 s.
6. **Action per phase** (§4, §12.5): one primary move + one reaction.
7. **Camera per phase**: scale, angle, move — each with a reason (Pillar 3 §1.0, §3.0, §3.2.0).
8. **Ending**: a living settle (held emotion) or momentum handed to the next scene (Code Block 2).

### 12.2 Common 10 s shapes (illustrative, not templates)
| Shape | Phases | Typical use |
|---|---|---|
| Exchange | 2 (line → counter-line) | Two wants collide; each line gets its own window |
| Trigger → Collision → Landing | 3 | A cause, the blow, where the blow lands in someone |
| Long build → Release | 2 (≈ 6–7 s + 3–4 s) | Slow pressure, then one short decisive beat |
| Staccato | 4 (each ≥ 2 s) | Rapid volleys, panic, a chain of consequences |
| Silent arc | 2–3 | Peak or aftermath carried by action alone |

### 12.3 Description blocks in Code Block 1
| Block | Must contain | Must not contain |
|---|---|---|
| **Style line** | Mandatory prefix, visual style, track declaration | Lens millimeters, f-stops, fps, brands |
| **[context]** | Location id + `[100% Refer to image …]`, time of day, key light source and direction, natural color tone, atmospheric medium | Kelvin numbers, coordinates, a second location (unless a declared threshold space) |
| **[subject]** | **Streamlined entity declaration**: character names + Mode B reference image anchors on separate lines (e.g. `my_duyen [100% Appearance, attire, and facial features Refer to image 1]`). Entity identity only. | Postures, actions, emotions, locations, costume/age descriptors (Mode B), pronouns. |
| **[PROP]** | **Streamlined key props & fixtures**: interactive hand props and key focal fixtures separated by semicolons (e.g. `white linen bedding on queen bed; noi_go [100% Refer to image prop_crib_4view.jpg]`). | Background clutter, fixtures that belong to location sheet. |
| **Diegetic line** | Room tone + 2–4 specific Foley sounds tied to the actions | Music cues, sound effects with no on-screen cause |
| **Phases** | `[start–end]` + camera clause + 4-Vector Directing prose (Physical state, action, emotion, 3D blocking ONLY for characters framed in that shot); lines in `name says : “ … ”` or `name replies : “ … ”` syntax | Naked `name:`, dummy tags (`[TRẠNG THÁI]`), characters outside the camera frame, pipes, `△` |
| **Closing lines** | Stability line + no-text / no-duplicate directive | — |

### 12.4 Seconds ↔ syllables (Vietnamese), per phase
Maximum syllables a phase can carry = (phase length − 1.4 s) × speech rate. The 1.4 s covers the 0.3 s lip-sync start, the 0.3 s breath, and the 0.8 s mouth-close before the cut.

| Phase length | Grief / whisper (3.0 syl/s) | Calm (4.0) | Audit estimate (4.5) | Firm / anger (5.0–5.5) |
|---|---|---|---|---|
| 2.5 s | 3 | 4 | 4 | 5–6 |
| 3.0 s | 4 | 6 | 7 | 8 |
| 3.5 s | 6 | 8 | 9 | 10–11 |
| 4.0 s | 7 | 10 | 11 | 13–14 |
| 4.5 s | 9 | 12 | 13 | 15–17 |
| 5.0 s | 10 | 14 | 16 | 18 |
| 5.5 s | 12 | 16 | 18 | 18 |
| 6.0 s+ | 13+ | 18 | 18 | 18 (Gate 4B cap) |

Whole clip: ≤ ~24 syllables of speech in 10 s (§7). English: divide by roughly 2 (calm ≈ 2.3 w/s): a 4.0 s phase carries about 6 words.

### 12.5 Action capacity per window
| Window | Body | Face | Words |
|---|---|---|---|
| 1.0–2.0 s | One micro-action (head turn, jolt, grip) | Pupil, swallow, lip | 0–5 |
| 2.5–4.5 s | One primary move (3 steps and stop, hand an object across, turn around) | Jaw, throat, breath change | One line |
| 5.0–7.0 s | One cause → effect chain (walk, obstacle, stop, face) | Two-stage shift (shock → resolve) | One line + reaction, or two short lines |
| 1.0–2.5 s terminal | No gross movement; contact points hold | Breathing, eye moisture, drifting air | 0 |

Pairing rule: inside a phase that carries a line, the action declares its relationship to the line — reinforce, contradict, replace, or reveal (Doctrine §3.3). An action that merely illustrates the line is filler.

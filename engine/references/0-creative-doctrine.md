# CREATIVE DOCTRINE — Intent Before Tools
# (The thinking layer that sits above the 4 Master Pillars)

> **READ THIS BEFORE ANY PILLAR, AT STAGES 0, 2, 3 AND 4.** Story level first (§8 Story Spine Card + §9 plot engine, once per episode), scene level second (§1 Intent Card, once per scene).
> The Pillars are catalogs: scales, angles, combos, dialogue models, timings, word budgets, examples. This doctrine decides **which tool a scene needs and why**. When a Pillar number (seconds, words, shot counts, "always", "strictly") collides with the dramatic need of a specific scene, the dramatic need wins — unless the number is a **Hard Constraint** listed in `workflow.md` §2.
> Rule of thumb: **understand the scene first, then choose the tools, then state the reason in one clause.** A choice without a reason is decoration; decoration is cut.

---

## §0 — THREE KINDS OF RULES (KNOW WHICH ONE YOU ARE HOLDING)

| Kind | What it is | Examples | How to treat it |
|---|---|---|---|
| **Hard Constraint** | A technical limit of AI video generation, a safety rule, or a delivery format rule | Zero Dead Air (no "holds still", continuous micro-actions); Zero Cumulative Timestamps (prompts MUST start at 00:00 for third-party AI generators); clip duration 10s / 15s / 30s; no freeze frames; no camera hardware/Kelvin; no clothing in prose; image references; Dialogue Word Cap: Single-Speaker Shot target 25–30w (hard cap ≤ 32w), Two-Shot exchange ≤ 15w/speaker; no pronouns in visual prose; minor safety; no lip-sync during a downward POV; ≥ 2 contiguous time phases; positive ending | **Never break.** The linter blocks delivery. |
| **Craft Default** | A habit that usually produces good results | Thermal shock cold→warm in Release; Wound Prop → Echo Prop; cast rotation per beat; conflict-dense Beat 3; ~14–18 spoken words per clip; the timing blueprints of the 8 dialogue models; the 3-phase "breath" (lead-in → peak → settle) | **Use by default. Break when the scene needs it**, and write a one-line reason (`BREAK: <default> — <why>`). |
| **Project Rule** | A rule that belongs to one film, not to the system | A family's kinship-address ladder; a recurring meal; a dialect lexicon | Lives in `output/<slug>/project_rules.json` and in that project's `setting.html`. Never hard-code it into the engine or the Pillars. |

If you cannot tell which kind a rule is, treat it as a Craft Default and give a reason when you deviate.

---

## §0.1 — THE 4 SOVEREIGN LAWS OF VIVID CINEMATIC ENGINE (BỐN QUY TẮC SỐNG ĐỘNG HÓA PHIM AI — CHỐNG BỆNH ĐƠ & BỆNH ĐẸP ĐỀU)

> 🎬 **MASTER CREATIVE MANDATE**: The downfall of amateur AI filmmaking is the **"Breathing Mannequin Syndrome" (Bệnh Ma-nơ-canh Thở Nhẹ)** and **"Aesthetic Monotony" (Bệnh Cảnh Nào Cũng Đẹp Đều Vô Hồn)**. When prompts are loaded with generic aesthetic buzzwords while characters lack physical friction and purposeful action, AI video models generate stagnant, lifeless shots where actors merely blink, drift, or tilt their heads 5 degrees.
> To build vibrant, dynamic, and gripping cinema, EVERY screenplay scene and AI prompt MUST strictly enforce the **4 Sovereign Anti-Stagnation Laws**:

### 1. Purge Hollow Beauty Buzzwords (Triệt Tiêu Từ Khóa Làm Đẹp Vô Nghĩa)
- **The Stagnation Trap**: Stacking decorative buzzwords (`photorealistic`, `cinematic 8k`, `masterpiece`, `dramatic lighting`, `moody atmospheric`, `hyperrealistic`, `unreal engine 5`, `shallow depth of field`). When every frame is forced to be "dramatic", visual impact is nullified. The generative model defaults to a blurry, slow-motion cosmetic filter with zero narrative pulse.
- **The Core Law**: **ZERO HOLLOW AESTHETIC BUZZWORDS.**
- **The Directorial Fix**: Replace empty descriptors with **Physical Optical Reality & Genre-True Lighting Contracts**:
  - Specify the precise physical light source (`low-angle morning sun piercing through dust-caked louvers`, `single flickering 40W ceiling bulb casting harsh shadows`).
  - Specify the physical atmospheric medium (`suspended microscopic kitchen flour particles`, `damp morning river mist`).
  - Specify tactile surface imperfections (`scratched enamel paint`, `sweat beading along collarbones`, `frayed cotton seams`).

### 2. Targeted Action Verbs Over Passive Adjectives (Thay Tính Từ Bằng ĐỘNG TỪ HÀNH ĐỘNG CÓ MỤC TIÊU)
- **The Stagnation Trap**: Describing internal feelings with static adjectives (`she looks heartbroken`, `he is furious and terrified`, `tense atmosphere`). AI video diffusion models cannot parse abstract psychological labels; they freeze the subject into an immobile mannequin with an unconvincing grimace.
- **The Core Law**: **ZERO ABSTRACT EMOTIONAL ADJECTIVES IN PROMPT PROSE.**
- **The Directorial Fix**: Every micro-phase must be driven by **Verbs of Kinetic Purpose and Somatic Disruption**:
  - *Instead of:* "He looks angry and betrayed."
  - *Write:* `slams both flat palms downward onto the damp wooden table, sending the chipped ceramic cup skidding across the surface, jaw muscles bulging tight as his gaze bores into his opponent.`
  - *Instead of:* "She is anxious and waiting."
  - *Write:* `relentlessly picks at the torn cuticle of her thumb until red wells up, breath hitching as she whips her head toward the unlatched doorway.`
  - Every action must possess an observable kinetic vector, measurable physical force, and an explicit target.

### 3. Compulsory Prop & Environmental Tactile Interaction (Bắt Nhân Vật Tương Tác Với Đồ Vật & Môi Trường Xung Quanh)
- **The Stagnation Trap**: Floating "talking statues" standing in the middle of a room with idle hands, detached from their surroundings.
- **The Core Law**: **ZERO FLOATING HANDS / ZERO UNANCHORED BODIES.** In every single shot, characters MUST have active physical contact and tactile friction with a physical prop or architectural fixture.
- **The Directorial Fix**:
  - Characters' hands must be actively occupied: twisting a worn wedding band, smoothing a creased eviction notice against their thigh, wiping an oily stain off a laminated tabletop, clutching the pine crib balusters until knuckles whiten, unscrewing a stiff thermos cap.
  - Physical interaction forces AI diffusion networks to compute collision geometry, material density, and spatial depth, instantly destroying the synthetic "statue" effect.

### 4. Dynamic Editing Rhythm & Sequence Assembly Over Monolithic Takes (Dựng Phim Bằng Nhịp Cắt — Editing Rhythm, Không Phó Mặc Cho Một Shot Dài Đơn Điệu)
- **The Stagnation Trap**: Attempting to resolve a complex 20s–30s emotional scene or dialogue confrontation inside a single, continuous, static wide prompt. AI models degrade, hallucinate, and lose momentum after 5–8 seconds without a cut.
- **The Core Law**: **STRICT BAN ON MONOLITHIC RUN-ON SHOTS.** Any scene spanning beyond 10s MUST be architected as a **Multi-Shot Sequence (Track B Cut Sequence)** with deliberate tempo variation and distinct scale shifts (>30° axis progression):
  * **Shot 1 (In Medias Res Action / Establishing Kinetic Vector - 4s–6s)**: Opens with action already underway; establishes spatial power geometry.
  * **Cut to Shot 2 (Reverse Reaction / Somatic Impact - 6s–8s)**: Cuts on action across the 180° line (>30° shift). Captures the listener's physical shockwave, counter-tactic, or micro-acting response.
  * **Cut to Shot 3 (Tactile Prop Detail / Extreme Close-Up / Cutaway - 3s–5s)**: Isolates an expressive physical object that carries the subtext (hands shredding a document, steaming kettle, trembling fingers dropping a key).
  * **Cut to Shot 4 (Resolving Climax / Power Shift - 6s–10s)**: Reversal of power or psychological aftermath settling into the next narrative beat.
- Narrative vitality lives in the cut, not in the waiting.

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
- **One primary action per phase** keeps AI motion clean; the reaction of the other body is the second layer.
- Prefer actions that **change the state of the world** (a door closed, an object moved, a distance crossed). Actions that only illustrate a line ("nods while agreeing") are filler.
- Small, tactile, readable actions beat big choreography (Hard Constraint: no fights, chases or brawls).

### 2.5 Track A or Track B — Decide by Question, Not by Habit
- **Track A (one continuous take):** the viewer must stay inside one breath, one body, one unbroken pressure — confessions, realization, intimacy, dread.
- **Track B (cuts on the 180° axis):** the viewer must see both sides of a collision — whose move lands, who absorbs it.
- The number of phases and where they split come from the scene's beats. A scene may be 2 phases or 4; one line may take 6 seconds while the silence after it takes 4.

### 2.6 The "Why" Test (one clause per choice)
Before compiling, every shot carries a rationale the Director could defend aloud:
```
Shot 2 — OTS past Má Ba, eye level, cut on the axis — power passes to Khang; the viewer must see her face receive it.
```
If the only reason is "looks cinematic", "adds variety" or "the model blueprint says so", change the choice.

### 2.7 Spatial Geometry of Power & Proxemics (Blocking as Subtext)
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

### 2.8 Continuous Somatic Co-Presence (No Bystander Mannequins)
Cinema is the art of **reaction**, not just action:
- **Zero Passive Figures**: In a room with multiple characters, nobody is an inert spectator waiting for their turn to speak. Every spoken line or physical movement must trigger an immediate somatic ripple across all bodies present.
- **Involuntary Somatic Leaks**: When Character A attacks with a harsh line:
  - The listener (Character B) does not just wait: pupils dilate, breathing hitches, throat swallows, or hands grip fabric.
  - The third party (Character C) in the background reacts in real time: eyes drop in shame, fingers clench, or body shifts between the combatants.

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

#### Tier 2: The Five 10-Second Kinetic Action Dynamics Archetypes
Depending on dramatic tension and narrative velocity, the action inside any 10.0-second scene atom MUST be cast into one of these 5 calibrated physical dynamics:

| Archetype | Rhythmic Cadence & Physical Mechanism | Dialogue Cadence & Dead-Air Standard |
|---|---|---|
| **1. High-Velocity Stichomythia (Đấu kiếm leo thang 3 nhịp)** | 3-beat physical escalation: Prop assault ➔ Counter-assault (ripping/parrying prop) ➔ Near-miss somatic contact. | Rapid, continuous staccato lines volleying up to 00:09.0. **STRICTLY ZERO IDLE DEAD AIR**. Absolutely bans 3s passive reaction settles. |
| **2. Single-Speaker Dominance (Bất đối xứng & Áp đảo đơn phương)** | Asymmetrical power clash: 1 character presses forward with aggressive unbroken monologue; 1 listener resists purely through physical micro-reactions (recoiling, biting lip, clutching doorframe). | Single continuous speech (20–30 words) across 1–2 shots while listener absorbs silently. Eliminates the artificial "ping-pong tennis match" trap. |
| **3. The Somatic Snap Shock (Cú sốc sự thật & Phản ứng giật 1 giây — 4.5s / 4.5s / 1.0s)** | Shot 1 (00:00–00:04.5) khiêu khích/công kích ➔ Shot 2 (00:04.5–00:09.0) nổ bom sự thật phản đòn ➔ Shot 3 (00:09.0–00:10.0) Snap-cut cận cảnh giật sốc ĐÚNG 1.0S DUY NHẤT. | Spoken line terminates by 00:08.5–00:08.8. Shot 3 is strictly a 1.0s visceral snap freeze (pupil contracting, smirk vanishing, gasped breath). Banning sluggish 3s dead air. |
| **4. Pure Covert Action (Hành động tác nghiệp / Lén lút thuần túy)** | High tactile friction with environment/props: unlatching a rusty deadbolt, crawling through a low window frame, slipping a cash envelope into a mattress seam. | **DIALOGUE = EXACTLY 0 WORDS**. 100% physical suspense and tactile diegetic Foley across the entire 10 seconds. |
| **5. False Dawn to Cold Water (Đảo chiều Bình minh giả ➔ Gáo nước lạnh)** | 00:00–00:07.5: Deceptive relief, relaxed breathing, gentle smiles, domestic harmony ➔ 00:07.5–00:10.0: Brutal visual or somatic shock freezes the body mid-motion. | The scene snaps to black (`Cut to black`) exactly at the peak of physical horror/paralysis, propelling the cliffhanger into the next scene/episode. |

### 3.4 Fewer Words Near the Peak
Lines shorten as stakes rise. The climax line is often the shortest in the episode; the true peak is frequently silent.

### 3.5 Address Forms Are Power Signals
Pronouns and kinship terms (`má`, `con`, `chị`, `tui`, `mày`) are tools for showing a relationship move — closeness, rebellion, formality, contempt. **Use them when the relationship moves; drop them when they add nothing.** A reply does not need to open with an address word. Never open consecutive replies with the same word (e.g., "Dạ má..." scene after scene).

### 3.6 Lines Chain by Cause ("Therefore / But")
Each line is born from the previous line **or** the previous action. Two characters taking turns to state positions is a debate, not a scene. Look for the moment a line *lands*: the listener's tactic must change because of it.

### 3.7 Specificity Over Explanation
Specific objects, names and memories ("this hammock is the one Khang's father grew up in") carry more emotion than arguments ("tradition matters"). Characters rarely explain their reasons; they act on them.

### 3.8 The Subtext-First Mandate & Ban on Declarative Melodrama
1. **Strict Ban on Psychological Self-Diagnosis**: Characters under authentic human pressure NEVER state their own hidden wounds, explain their childhood trauma, or confess their moral epiphany aloud like a textbook therapist.
   - ❌ *Banned on-the-nose exposition*: "Hồi đó má cũng giấu... giấu hoài tới ngất" (character verbally diagnosing their own backstory wound), "Con nhớ võng của ba... mà thằng Tin phải nằm nôi" (character lecturing parental philosophy), "Con lén tập ầu ơ hoài mà hổng giống má" (character verbally exposing their vulnerability in melodrama).
   - ✅ *Authentic domestic subtext*: Characters deflect, blame concrete objects, speak through everyday domestic chores, or choke on what cannot be said. The wound is revealed through what they *refuse* to say and the involuntary betrayal of their hands, eyes, and posture.
2. **Ban on Symmetrical Ping-Pong Debating**: Two people trading balanced alternating arguments (1 line A, 1 line B, both explaining their rationale) is an academic exercise, not human drama. Real human conflict is jagged, asymmetrical, and broken: one attacks an object, the other looks away; one storms out, the other freezes; silence carries more emotional weight than speech.
3. **Ban on Cliché Fainting & Instant Reversals**: A physical collapse, medical fainting spell, or sudden dramatic fall is strictly prohibited as a cheap shortcut that causes an antagonist to instantly flip 180° from tyrant to saint in 10 seconds. Real humans do not abandon decades of entrenched pride in a flash; reversals must be forged through sustained psychological pressure, undeniable evidence, and earned vulnerability across acts.

### 3.9 The Natural Cadence Mandate: Emotional Interjections & Modal Particles (Anti-Stiffness Law)
1. **Strict Ban on Curt, Robotic & Literary Declarative Phrasing**:
   - Spoken dialogue in dramatic domestic conflict MUST NEVER be written like dry written prose, legal cross-examination, or translated subtitles devoid of emotional cadence.
   - ❌ *Banned curt/stiff lines*: "Con tự lo được... má đừng bận lòng thêm" (sounds like a cold business email), "Mầy nói vậy... là mầy coi tao là người dưng nước lã?!" (sounds like an academic ping-pong debate), "Tay mầy... mầy đi truyền nước biển hồi nào sao hổng nói tao hay?!" (sounds like a police interrogation), "Tao lặn lội lên đây... hổng phải để tụi bây xua đuổi!" (sounds like a stiff theatrical declaration).
2. **Mandatory Modal Particles & Authentic Colloquial Exclamations**:
   - Authentic Vietnamese dialogue—especially Southwestern Nam Bộ and domestic family vernacular—lives and breathes through **modal particles and visceral exclamations** (*thán từ & trợ từ tình thái*).
   - In emotional confrontation, characters involuntarily cry out with exclamative anchors: *Trời ơi, Trời đất quỷ thần ơi, Mèn đéc ơi, Má ơi con lạy má, Anh ơi, Chị ơi là chị...*
   - Lines must land on organic colloquial sentence-ending particles: *...hả trời, ...hả mầy, ...nè má, ...nè con, ...chớ bộ, ...đâu hà, ...nghen con, ...hết trơn, ...đặng*.
   - ✅ *Authentic, emotionally charged lines (≤ 18 words)*:
     - Má Ba: “Trời đất quỷ thần ơi... tay mầy vầy nè, mầy đi truyền nước biển hồi nào sao giấu tao hả mầy?!” (18 words)
     - Mỹ Duyên: “Má ơi, con tự ráng gượng được mà má... má bận lòng làm chi cho khổ thân má nè...” (17 words)
     - Má Ba: “Mèn đéc ơi mầy nói cái giọng đó... mầy coi bà già này như người dưng thiệt rồi hả?!” (17 words)
     - Má Ba: “Trời ơi tao lặn lội từ dưới quê lên... đâu phải để tụi bây xua đuổi tao hả trời?!” (17 words)
     - Minh Khang: “Má ơi con lạy má! Duyên nó đuối sức dữ lắm rồi, má đừng nói vậy tội nghiệp nó má ơi!” (18 words)
     - Dì Tám: “Bà Ba ơi là bà Ba! Con dâu nó leo tuốt lên đầu ngồi kìa, mà bà nín nhịn cho đặng hả?!” (18 words)
3. **Word Budget Discipline**: Emotional particles do NOT require exceeding the word budget. Rich, tearful, authentic colloquial cadence fits comfortably within the 12–18 word limit when redundant filler words are trimmed and replaced with genuine human breath.
4. **Strict Ban on Death-Wishing Slang & Taboo Exclamations in Medical Panic**:
   - Expressions like *"Chết chưa"* (implies "Served you right" or wishing death), *"Đáng đời"*, or any gloating/curse idioms must NEVER be used when a family member collapses, faints, or suffers an accident. Such phrasing implies malicious schadenfreude, cruelty, and deep cultural taboo.
   - Real domestic panic uses immediate protective alerts: *"Duyên ơi coi chừng té! Khang ơi, vô đỡ vợ mầy lẹ lên con!"* or *"Trời đất ơi coi chừng té con!"*

### 3.10 The Acoustic & Physical Cadence of 10s Dialogue
Inside a 10.0-second scene atom, spoken dialogue is bounded by human biological breath cycles and the optical mechanics of AI video generation:
1. **Words-Per-Second (WPS) Biological Cadence**:
   - Emotional Vietnamese speech operates at ~3.5–4.5 syllables per second.
   - An 8–10 word line consumes ~2.0–2.5 seconds of physical time.
   - An 18-word line consumes ~4.0–4.5 seconds of physical time.
2. **The Invariant 18-Word Ceiling Rationale**:
   - *Physical Acting Space*: In a 10s clip, if dialogue takes 4.5s, the remaining 5.5s is essential for breath intake (lead-in), physical action, eye reaction, and the listener's somatic settle. Exceeding 18 words freezes the body into a static talking-head puppet.
   - *Mobile Subtitle Readability*: 18 Vietnamese syllables translate to ~110–120 characters, the exact ceiling for a clean 2-line subtitle (≤ 60 chars/line) on mobile screens without obscuring faces.
   - *AI Lip-Sync Stability*: Diffusion engines maintain accurate phoneme alignment only when speech has natural biological pause buffers.
3. **The 3 Dynamic Placement Zones in a 10s Clip**:
   - *Zone 1: Opening Attack / Interruption `[00:00–00:04]`*: Spoken line lands on the opening impact (e.g. door slamming open), followed by 6 seconds of suffocating shock and silence.
   - *Zone 2: Mid-Scene Collision `[00:02.5–00:07]`*: Physical tension builds for 2.5s, dialogue detonates at the center, followed by a 3s power-shift settle.
   - *Zone 3: Closing Cliffhanger Line `[00:06.5–00:10]`*: The scene builds in tense silence; the line lands as a parting scalpel or revelation that slings directly into the next scene.

### 3.11 The Three Analytical Tiers of Dialogue
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

**Timings and word budgets in the Pillar 1 models are illustrative.** The Hard Constraints remain: Dialogue Word Cap (Single-Speaker 25–30w, cap ≤ 32w; Two-Shot ≤ 15w/speaker), natural speech rate for the clip, no lip-sync during a downward POV, V.O. with lips sealed.

### 4.1 Episode Rhythm
- Avoid **3 or more consecutive scenes in the same mode** unless the repetition itself is the point (state the reason).
- Avoid giving every scene the same turn count (e.g., exactly two lines, A then B).
- Silence earns its power by contrast: place a silent or near-silent scene next to a dense one.
- A whole-project silent film is chosen only by explicit user request (`workflow.md` §2.3). Inside a dialogue project, individual silent scenes are a normal tool.

### 4.2 Writing V.O. and Monologue Inside Code Block 1
- **Spoken monologue**: same syntax as dialogue: `Name says : “ line ” (...)`; only one speaker. The listener (if any) reacts in prose.
- **V.O.**: same `Name says : “ line ” (...)` (or `inner voice`) syntax; the parenthetical states `inner voice-over, lips remain sealed` and still begins with `Voice of a [N]-year-old ...`. The prose shows the face doing something the voice does not say.
- **Silent scene**: no quoted lines in that prompt; the dialogue card for that scene states the silence.

### 4.3 The Five Elastic Directorial Rhythms (Aligned with Tier 2 Dynamics)
Strictly eradicate any dogmatic formula forcing every scene into the exact same 3-slice division (e.g. 0–3s / 3–7s / 7–10s). A true director selects from **Five Kinetic Directorial Rhythms** matching the Tier 2 Action Dynamics:
1. **The Rapid Sparring (Track B, 2-to-3 Sharp Cuts — High-Velocity Stichomythia)**:
   - High-velocity verbal and physical fencing; quick cuts across the 180° line where lines and reactions strike like sharp staccato notes up to 00:09.0. **Zero dead-air buffer**.
2. **The Asymmetric Press (Track A or B — Single-Speaker Dominance)**:
   - One character dominates space and voice (20–30 words); the camera holds tight on the physical duress and micro-defenses of the silent absorber.
3. **The Shockwave Snap (Track B, 3-Phase — Somatic Snap Shock / 4.5s / 4.5s / 1.0s)**:
   - Dialogue detonates by 00:08.5; Shot 3 is strictly 1.0s (00:09.0–00:10.0) of sudden stunned shock before the scene cut, preserving high emotional velocity and banning sluggish 3s reaction settles.
4. **The Silent Suspense Glide (Track A, Single-Take — Pure Covert Action)**:
   - 0 words spoken. Camera tracks continuous tactile interaction with props and architecture (unlatching, searching, hiding).
5. **The Sudden Fracture (Track AB Snap-Cut — False Dawn to Cold Water)**:
   - 00:00–00:07.5 peaceful breathing/dialogue shattered at 00:07.5 by an unexpected visual strike, cutting black on the physical shock.
*(Note: For contemplative moments or grief, the Director may deploy **The Lyrical Emotional Drift** [unbroken Track A tracking glide]; and for profound emotional peaks where camera movement would dilute raw human performance, the Director deploys **The Locked-Off Performance Take (Track A-Locked)**: 100% stationary tripod, zero camera movement, transferring all kinetic energy to somatic micro-acting, tear physics, and living atmospheric dust motes).*

---

## §5 — CREATIVE REVIEW (SELF-CHECK BEFORE COMPILE)

Run this after drafting all scenes of the episode and before `compile_and_validate_episode()`. The engine prints monotony warnings for some items; the rest are judgment.

**Story (§8)**
- [ ] The episode has a Story Spine Card; every principal has a Wound → Lie → Want → Need → Fear row.
- [ ] At least 5 specific-truth details are on screen; at least 2 expected choices are subverted or refused.
- [ ] Every late reversal was planted earlier; the ending costs someone something.
- [ ] No line names the title, states the moral, or labels a feeling without a `BREAK:` reason (W9).

**Plot (§9)**
- [ ] Every scene has a gap between what a character expects and what happens.
- [ ] The Prediction Ledger has ≥ 2 BROKEN predictions, each with plants in earlier scenes (W10); some predictions are deliberately KEPT.
- [ ] The knowledge mode (suspense / mystery / empathy) switches at least once.
- [ ] Every misunderstanding passes the idiot-plot test and ends on screen.
- [ ] The major twist passes the rewatch, character and moral tests; cold water is caused by a plant or a choice.

**Intent**
- [ ] Every scene has a value shift. Scenes without one are merged or cut.
- [ ] Every scene's want, tactic and subtext are visible in the action, not only in the lines.

**Dialogue**
- [ ] No line restates what the frame shows.
- [ ] Each line has a hidden verb (what it does to the listener).
- [ ] Each line declares its Action↔Line relationship; "contradict" and "replace" appear in the episode.
- [ ] No two scenes open their reply with the same word or phrase.
- [ ] Address forms appear only where the relationship moves or the culture demands it.

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

[00:04.5–00:09.0] Cut to an over-the-shoulder shot framing minh_khang past ma_ba along the 180-degree axis, sharp optical focus locked on minh_khang at eye level, static camera — minh_khang steps in firmly, crouches to grip the hammock frame with both hands, lifting it decisively off the tiles as his voice tightens with calm defiance.
minh_khang replies : “ Bác sĩ dặn nôi phẳng mới tốt, con mang ra sau hè má nằm nghen! ”（Voice of a 27-year-old Southern Vietnamese man; warm low firm baritone, polite but unyielding filial pushback）

[00:09.0–00:10.0] Snap-cut to an intimate close-up framing ma_ba along the 180-degree axis, shallow depth of field holding razor-sharp optical focus on ma_ba's contracting pupils with background falling into soft blur, eye level, static camera — ma_ba's jaw drops slightly, pupils contracting as her assertive smirk instantly freezes, taking in a sharp ragged breath at 00:10.0.
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

| Need | Open | Use it as |
|---|---|---|
| Beat structure, hooks, twists, dialogue model catalog, parentheticals, dialect | Pillar 1 | A menu of patterns. Timings and word budgets are starting points. |
| Cast, naming, model/prop/location sheets, `setting.html` | Pillar 2 | Specification (format rules here are mostly Hard Constraints for delivery). |
| Scales, angles, combos, 3D staging, 180° axis, continuity | Pillar 3 | A vocabulary. The "situation → combo" tables are examples, not prescriptions. |
| Code Block 1/2 syntax, Track A/B format, minor safety, HTML spec | Pillar 4 | Syntax and safety (mostly Hard Constraints). Example prompts show syntax, not the only valid rhythm. |

**Order of thought at Stages 2, 3 and 4**: Story Spine Card (§8, once per episode) → plot engine: Prediction Ledger, Knowledge Matrix, twist plants (§9) → Intent Card (§1, per scene) → voice mode (§4) → Action↔Line pairing (§3) → scale / angle / movement with reasons (§2) → Pillar syntax → Creative Review (§5) → compile and audit.

---

## §8 — STORY-LEVEL DEPTH & ORIGINALITY (BEFORE ANY SCENE)

§1–§7 make a **scene** good. §8 decides whether the **story** deserves telling and whether it is told the way only this film could tell it. Pillar 1 catalogs (6-beat, 8-beat curve, 20 twists, 12 hooks, addiction engines) are menus of patterns; a script assembled only from catalog entries is correct and forgettable. Depth comes from truth, originality from specificity, pull from open questions.

### 8.1 Three Questions Before Opening Any Catalog
1. **What is this story about underneath the plot?** (the thematic question, §8.3)
2. **Why this family, this place, this object — and not any other?** (the specific truth, §8.5)
3. **What will viewers argue about after the last frame?** (the debate seed, §8.7)

If any answer is generic ("family love", "tradition vs. modernity", "it is touching"), keep digging before writing scenes.

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
- The positive ending (Hard Constraint) must **cost someone something**: who gives up what — a role, a certainty, a mask.
- The ending answers the thematic question with an **action or image**.
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
```
It is written at Stage 2 (series or short-film Spine) and refreshed per episode at Stage 3, before the scene roadmap, and published in the episode HTML as a card with `id="story-spine"` (the audit warns when it is missing). Scene Intent Cards (§1) inherit from it: each scene's want, subtext and value shift serve one row of the Spine. §9.9 adds four plot rows (PREDICT / KNOW / MISREAD / TWIST).

### 8.11 Worked Example (Authentic Serialization vs. Flawed Melodrama)
- ❌ **Flawed Rushed Melodrama (Banned Pattern)**:
  - Episode 1 opens with conflict ➔ Duyên faints ➔ Má Ba confesses her 30-year-old trauma in tears ➔ cuddle & forgive ➔ Má Ba sings a lullaby ➔ total reconciliation in 100 seconds.
  - *Why it fails*: Characters feel emotionally bipolar. A 30-year entrenched belief is erased by a convenient faint. Conflict is resolved without cost or time to breathe, leaving Episode 2 with nowhere to go except inventing random meddling neighbors.
- ✅ **Authentic Serialized Architecture (Mandatory Standard)**:
  - **Episode 1 (The Inciting Trap & Silent Fracture)**: Duyên’s postpartum exhaustion and dry pump trigger Má Ba’s deep-seated fear of obsolescence. When Má Ba brings the steel hammock, Khang’s gentle refusal lands as rejection. As Duyên’s trembling hands spill the congee and expose the hidden, bruised IV needle marks, Má Ba does NOT deliver a therapeutic confession or offer a warm hug. She freezes in stunned, choking disbelief: *"Tay mầy... mầy vô nước biển hồi nào sao hổng nói tao hay?..."*. The episode cuts to black on the unresolved shockwave—no easy answers, no lullabies, forcing the viewer to binge Episode 2.
  - **Episodes 2–4 (Escalation & Hardening)**: The wound is exposed, but defense mechanisms harden before they soften. Khang is torn between duty and love. Healing is earned across the full 4-act architecture, culminating in Act 3/4.

### 8.12 Multi-Episode Serial Arc vs. Standalone Short Film Law
1. **Format A (Standalone Short Film, 60s–120s)**:
   - A closed narrative lifecycle where the complete 6-beat transformation (Hook ➔ Setup ➔ Drama ➔ Climax ➔ Release ➔ Echo) completes inside the single runtime.
2. **Format B (Multi-Episode Series, N Episodes)**:
   - **Act-Bound Episodic Function**: An individual episode in a series is an ACT-BOUND CHAPTER. It NEVER executes all 6 beats of a closed film.
   - **Act 1 Episodes (Setup & Trap)**: Strictly forbidden from executing Beat 4 (Ego Death) or Beat 5 (Cathartic Release/Reconciliation). Act 1 episodes must end with mounting psychological pressure, sealed exits, and an unresolved Cold Water cliffhanger.
   - **Anti-Vignette / Anti-Sitcom Standard**: Never construct a series as 20 disconnected "Problem-of-the-Week" vignettes (e.g. hammock vs crib, then eyelashes, then weight scale, then pork trotter). Characters must possess psychological continuity; their relationship permanently changes at each checkpoint.

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

### 9.3 Surprise Under the Positive-Ending Mandate
The viewer of a short drama knows the ending will be good (Hard Constraint). Surprise therefore lives in:
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
| **Sitcom & Light Social Comedy** | High (25–30 words/shot; 5–10w volleys, punchline in last 2–3s). Modes: Model 1B (Rapid Volleys), Model 2 (Ensemble Overlap), Model 8 (Direct 4th Wall). | **Eccentric Ping-Pong & Mutual Misunderstanding**: Rapid rhythmic volleys, unexpected punchlines, characters talking over each other. | 30% Physical Comedy / 70% Dialogue |
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

In cinematic generative AI production, **props must be strategically bifurcated based on their visual entropy, cultural ubiquity, and semantic complexity**. Forcing 4-view turnaround reference images for mundane objects is a catastrophic waste of compute, memory, and cognitive focus. Conversely, relying on text alone for idiosyncratic, high-concept artifacts triggers uncontrollable visual hallucinations across scenes.

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE TWO-TIER PROP IMPLEMENTATION STANDARD                                 │
├────────────────────────────────────────┬───────────────────────────────────────────────────────────────┤
│ TIER 1: EVERYDAY / MUNDANE PROPS       │ TIER 2: SOVEREIGN / SOUL / WEAPON / COMPLEX PROPS             │
│ (Đạo cụ Đời thường & Vật dụng Sinh hoạt)│ (Đạo cụ Linh hồn, Vũ khí Đặc chế & Cổ vật Biểu tượng)         │
├────────────────────────────────────────┼───────────────────────────────────────────────────────────────┤
│ • Scope: Household, culinary, office,  │ • Scope: Custom weapons, ancestral talismans, intricate       │
│   and everyday items (rice bowl, tea   │   puzzle mechanisms, runic blades, glowing sci-fi cores,      │
│   cup, pen, envelope, key, wrench,     │   dynastic signets, idiosyncratic heirlooms with rare runes.  │
│   folding hammock, stool, phone).      │                                                               │
│ • Implementation: 100% PURE TEXT       │ • Implementation: MANDATORY 16:9 4-VIEW MODEL SHEET           │
│   PROMPTING (Mode A).                  │   (Mode B — Step 1C).                                         │
│ • Rationale: AI diffusion models       │ • Rationale: Text alone cannot maintain geometric consistency │
│   already possess deep semantic weights│   or ornamental precision; without an image reference,        │
│   for standard items; zero drift risk. │   diffusion models drift uncontrollably between scenes.       │
│ • Production Rule: BAN on generating   │ • Production Rule: Reference asset generated in Step 1C       │
│   16:9 Model Sheets or visual assets.  │   and strictly bound in prompts: `[100% Refer to image <ref>]`.│
└────────────────────────────────────────┴───────────────────────────────────────────────────────────────┘
```

#### 1. Tier 1 (Everyday / Ambient Props) — Mode A (Pure Text Specification)
- **Zero Pre-Production Visual Burden**: Never generate a 16:9 turnaround sheet or Midjourney/Flux image prompt for everyday domestic items (`bat_com`, `ly_nuoc`, `doi_dua`, `co_le`, `vong_xep`, `phong_bi`, `to_giay_vien_phi`). AI generative models possess vast pre-trained weights for these objects.
- **In-Prompt Anchor Formula**:
  `[PROP: {material/surface texture} {canonical noun}, {current physical state/wear}, {spatial resting location OR which hand holds it} — the only {canonical noun} in frame]`  
  *Example*: `[PROP: chipped white ceramic rice bowl, steaming with hot jasmine rice, resting on the worn mahogany table beside Duyen's left wrist — the only rice bowl in frame]`
- **Mechanical Continuity Invariance**: The Single Instance Lock, Resting Surface Clearance, and Prop Mutability Lifecycle (Intact ➔ Kinetic Fracture ➔ Inert Fragments) apply identically to Tier 1 props via pure text cues.

#### 2. Tier 2 (Sovereign / Soul / Weapon / Complex Props) — Mode B (Image-Anchored Specification)
- **Mandatory Pre-Production Visual Asset (Step 1C)**: Exactly 1–2 master sovereign artifacts per narrative arc. Rendered as a standardized 16:9 Four-View Turnaround Model Sheet (Hero 3D perspective + 3 orthographic views: front, side profile, back) on a pure white `#FFFFFF` studio backdrop.
- **In-Prompt Anchor Formula**:
  `[PROP: {Prop Name} [100% Refer to image <prop_ref>], {current physical state}, {spatial resting location OR which hand holds it} — the only {canonical noun} in frame]`  
  *Example*: `[PROP: The Obsidian Phoenix Hairpin [100% Refer to image prop_hairpin_4view.jpg], intricate carved black obsidian with blood-red jade eye, clutched in A1's trembling right fist — the only hairpin in frame]`

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





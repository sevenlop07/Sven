# Sven Cinematic Universe — Sitcom Genre Specification & Production Engine
File: `engine/genres/sitcom.md`
SSOT Status: Authoritative Standard for Situation Comedy Writing & Directing
Governed by: Screenwriter (Level 2) & Director (Level 2) under Showrunner (Level 1)

---

## Genre Card (README §2b)

| Field | Value |
|---|---|
| **Regime** | 1 — Grounded (comic register) |
| **Genre Engine** | 5 — Snowball Farce & Reset |
| **Audience payoff** | Laughter from character-flaw collisions |
| **Heart & value payoff** | Warmth: the group stays a family after the reset; the tag shows a small kindness; jokes punch at flaws, never at the weak (`0d` §6) |
| **Cast topology** (`2b-character-lines.md` §2) | Ensemble E1–E5 (one fixed flaw + want each, clash grid); no A2 or a recurring rival; 1–2 recurring guests |
| **Default episode shape** | `6–8` scenes `60–80s`, `90:10` |
| **Preferred hooks** | #7 Disrupted Order, #2 In Medias Res, #11 Diegetic Acoustic Stimulus |
| **Preferred cliffhangers** | Comic scene button or a reset with one new itch (C-codes optional) |
| **Favoured twists & budget** | TW-08 Misunderstanding, TW-14 Irony; snowball lie collapse |
| **Dialogue : visual** | `30 : 70` (physical slapstick : rapid ping-pong) |
| **Default `ending_mode` / `fatality_policy`** | positive with status-quo reset |
| **Signature bans** | heavy tragedy, lectures, jokes that need explanation, cruelty to the weak |
| **Scorecard criteria that must score 2** | Rhythm, Natural dialogue, Value shift |

Numbers defer to `engine/references/0c-canonical-numbers.md`; pacing tables below are default sketches.

---

## 0. Core Principles & Comedic Philosophy

The objective of the Sitcom Genre Engine is to guide creators seamlessly from a raw conceptual premise to a fully formatted, production-ready sitcom episode script featuring authentic character-driven laughter, rapid comedic pacing, and consistent emotional dynamics.

### 0.1 The Sitcom Formula
$$\text{Sitcom Engine} = \text{Trapped Circumstance} + \text{Amplified Petty Conflict} + \text{Character-Flaw Collisions}$$

1. **The Inescapable Trap (Hoàn cảnh cố định)**:
   - Characters are locked together in a confined physical or social ecosystem (a dysfunctional family household, a toxic shared office, a tight-knit rental row house / *xóm trọ*, a struggling café, or an urban apartment complex).
   - They cannot simply walk away from one another due to financial necessity, familial blood, career dependency, or mutual co-reliance.
2. **Exponential Amplification of Minor Stakes (Xung đột nhỏ bị thổi phồng)**:
   - Sitcom conflicts never begin with global catastrophes or life-and-death crises. They begin with trivial everyday friction: an unpaid electricity bill, a missing box of leftovers in the fridge, an accidental white lie to avoid an awkward dinner, or a petty neighborhood rivalry.
   - The comedy arises from the characters treating trivial problems with catastrophic seriousness.
3. **Humor Born from Character Flaws, Never Stand-Alone Puns (Hài từ tính cách)**:
   - Humor is not an arbitrary joke told by a talking head; it is the inevitable byproduct of a character’s specific blind spots, stubborn pride, hypocrisies, neurotic anxieties, and misaligned goals.
   - **No "Stupid for the Sake of Comedy"**: Characters must not behave like mindless caricatures. The funniest situations come from intelligent, capable people making disastrous decisions driven by their unique character flaws.
4. **The Sacred Status Quo Reset Law (Trạng thái Reset cuối tập)**:
   - Unlike continuous serial melodramas where trauma and consequences accumulate permanently, sitcoms maintain dynamic equilibrium.
   - Characters may experience temporary emotional clarity or a warm reconciliation in Act 3, but by the end of the Tag, the fundamental dynamics and status quo reset almost completely back to baseline.
5. **The Law of Scene Utility & Button**:
   - Every scene must possess a crystal-clear dramatic objective and an active obstacle.
   - Any beat or scene that neither advances the A/B narrative engine nor generates laughs must be ruthlessly excised.
   - Every scene must conclude on an emphatic **"Button"** (an undeniable visual or verbal punchline).
6. **Tangible Cultural Grounding**:
   - Comedy thrives on tactile, hyper-specific domestic details, idiosyncratic colloquial slang, and recognizable everyday situations rather than generic or translated abstractions.
7. **Decisive Lean Intake Protocol**:
   - When key premise data is missing, bundle inquiries into **maximum 3–4 concise questions** in a single pass.
   - If the user desires rapid execution, autonomously adopt robust, culturally authentic defaults and explicitly state what was chosen.

---

## 1. Input Collection & Ingestion Matrix

Before launching script production, the Screenwriter ingests the following parameters (bundled into a single concise intake turn):

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                SITCOM INTAKE BUNDLE                                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Setting & Central Milieu: Family home, shared office, rental house, café, alley...   │
│ 2. Core Cast (Recommended 4–6): Names, ages, archetypes, and primary flaws.            │
│ 3. Runtime & Delivery Format:                                                          │
│    • 22-Minute Broadcast Standard (3-Act Structure, ~22–26 pages)                      │
│    • 11-Minute Short / Cable Format (2-Act Structure, ~11–13 pages)                    │
│    • 5–10 Minute Web-Series / Micro-Sitcom (~5–10 pages)                               │
│ 4. Comedic Voice & Tone: Witty banter, warm family, satirical, slapstick, mockumentary │
│ 5. Target Audience & Rating: General Family, Young Adult / Workplace, Mature / Edgy.    │
│ 6. Linguistic Dialect & Cultural Region: Northern, Central, Southern Vietnamese...      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.1 The 1-Sentence Seed Engine (Phát triển từ ý tưởng thô)
If the user provides only a single raw sentence (e.g., *"Viết phim hài về một nhóm bạn mở tiệm giặt ủi"*), the Screenwriter immediately pitches **2–3 divergent tonal directions** before writing:
- **Direction A (The Neurotic Workplace)**: Focus on hyper-competitive operations, absurd customer complaints, and disastrous cost-cutting schemes.
- **Direction B (The Dysfunctional Found Family)**: Focus on shared financial desperation, contrasting living habits, and emotional codependency.
- **Direction C (The Mockumentary / Social Satire)**: Focus on modern urban pretensions, influencer culture, and street-level gossip dynamics.

---

## 2. Staged Production Lifecycle

Sitcom development proceeds through four distinct, verifiable phases:

```
  Phase A: Logline & Series Bible  ──►  Phase B: Episode Premise (A/B/C Plots)
                 │                                        │
                 ▼                                        ▼
  Phase D: Full Screenplay (Format & Gags) ◄──  Phase C: Beat Sheet / Outline
```

---

### Phase A: Logline & Series Bible (Hồ sơ gốc của Series)

1. **Logline**:
   - Exactly 1–2 sentences combining: `[Flawed Protagonist]` + `[Inescapable Milieu]` + `[Primary Comic Engine / Daily Friction]`.
2. **The World & Primary Sets**:
   - Establish maximum 2–3 recurring primary physical sets (e.g., The Cramped Living Room, The Corner Office, The Alley Tea Stall / Quán Nước Đầu Hẻm).
   - Define the unbreakable rules of this micro-universe (e.g., *“No one is allowed to touch the antique fan without Grandma's key”*).
3. **Character Dossiers (For each of the 4–6 core members)**:
   - **Full Name, Age, Occupation / Role**: Grounded identity.
   - **Super-Objective (Mục tiêu cốt lõi)**: What they want out of life (e.g., *“To become a luxury real estate mogul despite having zero sales”*).
   - **Core Fear / Deep Insecurity (Nỗi sợ thầm kín)**: What makes them vulnerable.
   - **The Comic Flaw / Hubris (Khuyết điểm gây cười)**: The fatal trait that triggers their own downfall (e.g., pathological stinginess, unearned arrogance, chronic inability to say "no", hypochondria).
   - **Verbal Tic / Idiosyncrasy / Catchphrase (Thói quen & Câu cửa miệng)**: A signature linguistic or somatic trait used with restraint.
   - **Interpersonal Matrix (Mạng lưới quan hệ)**:
     - The **Straight Man (Người bình thường)**: The voice of reason who reacts with sanity to madness.
     - The **Chaos Agent / Troublemaker (Người gây rối)**: The instigator whose absurd schemes ignite the plot.
     - The **Egomaniac / Blowhard (Kẻ tự cao)**: Constantly humiliated by reality.
     - The **Innocent / Eccentric (Người ngây ngô / lập dị)**: Operates on bizarre internal logic.
4. **The Central Inescapable Question (Câu hỏi trung tâm lặp lại)**:
   - Explicitly define: *Why can’t these people simply separate or leave this environment?*
5. **Season Pipeline (5–8 Evergreen Episode Concepts)**:
   - Provide 5–8 high-concept episode hooks showing the longevity of the premise.

---

### Phase B: Episode Premise & Multi-Plot Weave (Cốt truyện tập)

Every sitcom episode is structured around a multi-strand narrative weave:

1. **The Multi-Plot Triangle**:
   - **A-Plot (Primary Narrative Engine — 60% of screen time)**: Drives the episode's main dramatic question and highest comedic stakes.
   - **B-Plot (Secondary Comedic Engine — 30% of screen time)**: Involves secondary characters pursuing a completely separate, low-stakes objective.
   - **C-Plot / Runner (Recurring Gag — 10% of screen time)**: A running physical gag or escalating micro-conflict that appears 3–4 times throughout the episode.
2. **The Thematic Reflection Principle (Nguyên tắc phản chiếu chủ đề)**:
   - The A-Plot and B-Plot must **mirror each other thematically**: they explore the exact same moral lesson or human dilemma at two completely different scales (e.g., *In A-Plot, the father lies to his boss to protect his ego; in B-Plot, the son lies about eating a cup of yogurt to protect his allowance*).
   - In Act 3, the A-Plot and B-Plot must physically or narratively **collide** at the climax.
3. **The Escalation Ladder (Tình huống leo thang)**:
   - Conflict must compound exponentially. A minor mistake (e.g., spilling soy sauce on an expensive borrowed jacket) leads to a cover-up (cutting the label off), which requires a bigger lie (claiming the jacket was stolen by a ninja), which attracts police or neighbors, culminating in total chaos.

---

### Phase C: Beat Sheet & Narrative Outline (Cấu trúc phân cảnh)

#### 1. The 22-Minute Broadcast Architecture (~22–26 script pages)

| Structural Beat | Script Pages | Dramatic & Comedic Function |
|---|---|---|
| **Cold Open** | 1–2 pages | Independent high-energy gag or thematic launchpad. Hooks the audience in 10 seconds; concludes on a massive punchline into title credits. |
| **Title Sequence** | — | Theme song / Show opening. |
| **Act 1** | 6–7 pages | Introduces the status quo; A-Plot inciting incident detonates; B-Plot seedling is planted; ends on the **Point of No Return** where characters commit to a disastrous lie or plan. |
| **Act 2** | 8–9 pages | The Escalation Engine. Complications multiply; B-Plot interweaves; dramatic irony peaks; ends on the **Crisis / All Exposed Point** where all deceptions shatter simultaneously. |
| **Act 3** | 6–7 pages | Climax collision where A-Plot and B-Plot converge in one shared space; chaotic fallout; frantic scrambling; brief 30-second sincere emotional warmth (without preachy lecturing). |
| **Tag** | 1 page | Post-credits comedic coda. Delivers the ultimate callback to the Cold Open or resolves the C-Plot runner with a hilarious button. |

#### 2. The 11-Minute Format (~11–13 pages)
- Omits the extended Act 2 middle.
- Structure: **Cold Open (1p) ➔ Act 1 Setup & Point of No Return (4p) ➔ Act 2 Escalation & Climax (5p) ➔ Tag (1p)**.

#### 3. The 5–10 Minute Web-Series Format (~5–10 pages)
- Single-Plot Focus: 1 Core Premise ➔ Rapid 3-Stage Compounding Escalation ➔ 1 Sharp Final Twist / Button.

#### 4. Outline Specification Standards
Before drafting dialogue, outlines must state for every single scene:
- **Heading**: Slugline (INT/EXT. LOCATION - DAY/NIGHT).
- **Characters Present**: Specific active cast members.
- **Scene Objective**: What does Character A want right now?
- **Comic Obstacle**: What is Character B doing to obstruct them?
- **Primary Gag / Escalation Beat**: The central comedic set-piece.
- **Scene Button**: The exact final punchline or comic reaction shot closing the scene.

---

### Phase D: Screenplay Crafting & Industry Script Format

#### 1. Standard Sitcom Screenplay Formatting
The script is written in clean, standard industry format easily convertible to Final Draft, WriterDuet, or text editors:

```text
CẢNH 1. NỘI. PHÒNG KHÁCH NHÀ BÀ BA - NGÀY

Phòng khách chung cư cũ ngổn ngang ba cái quạt máy tháo tung ruột. Tiếng ve kêu râm ran ngoài cửa sổ. 

HÙNG (30 tuổi, đầu tóc bù xù, mặc áo may-ô thủng một lỗ ngay rốn) đang ngồi xổm trên sàn gạch, mồ hôi nhễ nhại cầm mỏ lết gõ cọc cọc vào cái lồng quạt gỉ sét.

BÀ BA (60 tuổi) từ trong bếp bước ra, tay bưng đĩa mít tố nữ thơm lừng nhưng mặt đanh lại như đá cẩm thạch.

HÙNG
(vừa quệt mồ hôi vừa cười cầu tài)
Mẹ, hôm nay con có hai tin. Một tin vui với một tin buồn.

BÀ BA
(ngồi phịch xuống ghế salon)
Tin buồn trước. Tin vui để dành ăn cơm xong hẵng nói cho đỡ nghẹn.

HÙNG
Tin buồn là... cái quạt máy của mẹ chính thức lên thiên đàng rồi.

BÀ BA
Còn tin vui?

HÙNG
Con tháo được ba con ốc còn xài tốt lắm!

BÀ BA
(ném trái mít xuống bàn)
Vậy tin buồn của mầy là tối nay ngủ ngoài hành lang với ba con ốc đó!
```

#### 2. Technical Script Elements
- **Scene Headings (Sluglines)**: Strictly `CẢNH [X]. NỘI/NGOẠI. ĐỊA ĐIỂM - NGÀY/ĐÊM`.
- **Character Cues**: Character names in full capital letters centered above dialogue.
- **Parentheticals (Wrylies)**: Placed in parentheses under the character name; reserved strictly for critical emotional delivery, comic timing beats, or simultaneous micro-actions (`(nói lí nhí)`, `(vừa nhai vừa nói)`). Never over-direct actors.
- **Visual Action Lines**: Present tense, active verbs, strictly observable physical reality. Zero inner monologue or literary editorializing.
- **Audience Laugh Track Notation**: For classic multi-camera format filmed before a live studio audience, insert `(tiếng cười khán giả)` at major laugh breaks; omit completely for single-camera / mockumentary styles.
- **The Scene Button**: Every scene MUST end on an unmistakable laugh button or physical punchline before cutting.

---

## 3. Comedic Engineering & Laugh Construction Arsenal

Every sitcom script generated by the Sven engine must actively employ the **10 Classical Comedy Weapons**:

| # | Comedic Weapon | Mechanism & Execution Rule |
|---|---|---|
| 1 | **The Rule of Three (Quy tắc số ba)** | Two predictable, ordinary items establish a pattern; the third item violently shatters expectation. *(e.g., "Anh Khang vừa thông minh, vừa có hiếu, vừa trốn viện phí.")* |
| 2 | **The Callback (Nhắc lại chi tiết / Phục bút)** | Re-triggering a specific phrase, prop, or embarrassing incident introduced in Act 1 in an entirely unexpected context in Act 3. |
| 3 | **Dramatic Irony (Mỉa mai kịch tính)** | The audience and one character know a devastating truth that another character is completely blind to. The comedy stems from watching the ignorant character dig their own grave. |
| 4 | **The Snowball Lie (Lời nói dối leo thang)** | A character tells a small, innocent lie to cover an embarrassment. To maintain it, they are forced to fabricate increasingly absurd lies until they are pretending to be an astronaut or a monk. |
| 5 | **The Reaction Delta (Chênh lệch phản ứng)** | Radical disproportion: A character reacts with hysterical panic to an insignificance (a bent spoon), or displays chilling indifference to a catastrophe (the living room couch on fire). |
| 6 | **Polar Odd-Couple Friction (Tương phản đối lập)** | Trapping two diametrically opposed archetypes (the extreme neat-freak vs. the chaotic slob) in a shared task with high pressure. |
| 7 | **Catchphrase Economy (Kinh tế câu cửa miệng)** | A character's signature line or tic must be used sparingly (maximum 2–3 times per episode) and must always land with increased comedic velocity. |
| 8 | **The Tactile Comic Prop (Đạo cụ gây họa)** | A single physical prop (a screeching pressure cooker, an oversized novelty painting, a cursed robot vacuum) that actively creates physical havoc across the scene. |
| 9 | **Vietnamese Cultural Wit (Hài hước bản địa)** | Leveraging linguistic idiosyncrasies: homophones, *nói lái* (spoonerisms), subverted folk proverbs (*bẻ tục ngữ*), and hyper-local tropes (tiền trọ, họp lớp khoe của, shipper giao hàng nhầm, cúng kiếng, hàng xóm soi mói). |
| 10 | **The Late-Hit Punchline Law (Điểm rơi chữ cuối)** | The funniest, most shocking, or absurd word in a punchline line must be placed at the **VERY LAST WORD** of the sentence. Never place filler after the punchline. |

### 3.1 Pacing Benchmark
In fast-paced dialogue-driven sitcoms, aim for **2 to 4 genuine laugh beats per page** (approximately one laugh every 15–30 seconds of screen time).

---

## 4. Dialogue & Character Dynamics

### 4.1 Voice Distinction Matrix
No two characters should sound identical. If character names are removed, a reader must immediately identify the speaker based on:
1. **Sentence Cadence & Rhythm**: Rapid staccato firing vs. slow, ponderous lecturing.
2. **Vocabulary Tier**: Formal intellectual jargon vs. hyper-colloquial street slang.
3. **Politeness Register & Pronouns**: In Vietnamese, kinship address forms (`mày/tao`, `anh/em`, `chú/cháu`, `con/mẹ`) immediately delineate status, tension, and power reversals.

### 4.2 Dialogue Rules
- **Short, Punchy Volleys**: Avoid long explanatory monologues. Dialogue must ricochet back and forth like a ping-pong match.
- **Subtextual Combat**: Characters rarely speak direct truths; they use dialogue as tactical weaponry to deflect blame, fish for compliments, guilt-trip family members, or justify bad decisions.
- **Strict Anti-Bookish Grammar**: Spoken Vietnamese in sitcoms strictly bans stiff literary conjunctions (`bởi vì`, `cho nên`, `tuy nhiên`, `do đó`). Use natural conversational connectors (`tại`, `nên là`, `vậy mà`, `ai dè`, `tự nhiên`).

### 4.3 Character Integrity
- **Flaws Tied to Objectives**: A character’s comedic flaw must directly obstruct what they desperately want.
- **Ensemble Equity**: Every main cast member must receive at least one shining comedic moment or distinctive joke in every episode.
- **The 30-Second Warmth Window**: In Act 3, allow a brief, genuine emotional beat where characters demonstrate underlying loyalty or affection, immediately punctured by a final comedic button.

### 4.4 The 3-Layer Organic Comedic Dialogue & Anti-Curtness Protocol
Vietnamese sitcom dialogue must never sound curt, dry, or like mechanical robot commands (*thoại cộc lốc, trơ khấc*). Even in rapid-fire comedic exchanges, lines must possess living acoustic elasticity, authentic conversational breathing, and deliberate punchline placement. Every comedic spoken line is constructed via the **3-Layer Organic Anatomy**:

$$\mathbf{Line} = \mathbf{[Layer\ 1:\ Acoustic\ Inception]} + \mathbf{[Layer\ 2:\ Comedic\ Payload]} + \mathbf{[Layer\ 3:\ Late-Hit\ Modal\ Particle]}$$

1. **Layer 1: Acoustic Inception (Hô ngữ & Cảm thán dẫn nhập)**:
   - Sets the interpersonal rhythm and establishes status/tension before the information lands.
   - Natural conversational starters: `Ủa`, `Ê`, `Trời đất ơi`, `Mẹ ơi`, `Cái gì`, `Khoan đã`, `Nói nghe nè`, `Bậy nè`.
2. **Layer 2: Comedic Payload (Nhân kịch tính & Lô-gíc trớ trêu)**:
   - The absurd justification, escalating lie, or neurotic observation.
   - Sweet spot: **8 to 14 words** with internal respiration pauses (`...`) allowing comedic timing to register.
3. **Layer 3: Late-Hit Modal Particle (Trợ từ tình thái & Điểm rơi chữ cuối)**:
   - Sentence-final modal landing particles that lock the emotional attitude and deliver the punch: `đó hả`, `luôn á`, `hả trời`, `coi được hông`, `đâu nè`, `chứ bộ`.
   - **The Late-Hit Punchline Law**: The funniest or most humiliating word must always be positioned at the **absolute end** of the sentence.

> **Negative Example (Banned — Curt & Robotic)**:
> `HÙNG: Con sửa xong quạt rồi.` *(5 words — dry, lifeless, zero comedic energy).*
>
> **Positive Example (3-Layer Organic Sitcom Line)**:
> `HÙNG (cười cầu tài): Mẹ ơi... con tháo banh cái quạt ra rồi, nhưng cứu được ba con ốc xịn lắm luôn á!` *(Layer 1: "Mẹ ơi..." + Layer 2: escalating disaster with breathing pause + Layer 3: punchline landing "xịn lắm luôn á!").*

### 4.5 The Dramatic Spine & 4-Way Cross-Scene Comedic Baton Relay
A sitcom episode is never a disconnected collection of stand-up skits. It is driven by a single, continuous **Dramatic Spine** ($\mathbf{Spine} = \mathbf{Want} + \mathbf{Obstacle} + \mathbf{Stakes}$). Between Scene $N$ and Scene $N+1$, comedic dialogue must pass an unbroken baton via the **4 Relay Vectors**:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        4-WAY SITCOM COMEDIC BATON RELAY                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Cause & Effect Baton: The petty lie or botched task in Scene N detonates the       │
│    immediate confrontation or awkward cover-up in Scene N+1.                           │
│ 2. Keyword Echo / Inversion: A signature phrase or absurd excuse coined in Scene N    │
│    is weaponized with devastating irony by another character in Scene N+1.             │
│ 3. Emotional Inertia / Escalating Panic: The frantic adrenaline or smug hubris of      │
│    Scene N directly spills into the opening 3 seconds of Scene N+1 without a reset.    │
│ 4. Prop Anchor Relay: The physical comedic hazard (a scorched pan, a leaking pipe,     │
│    a torn receipt) physically crosses the cut from Scene N into Scene N+1.             │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.6 AI Video Prompt Directing for Sitcom (Code Block 1 Standard)
When directing sitcom episodes for generative video diffusion models (Sora, Kling, Runway Gen-3, Wan 2.1), the Director must enforce:
1. **The 4-Part Sovereign Subject Formula in `[subject]:`**:
   `{ho_ten} [100% Appearance, attire, and facial features Refer to image X], {initial spatial anchor to architectural fixture}, {initial physical posture & tactile contact} — the only {ho_ten} in frame.`
   - Grounds the actors to physical fixtures at 00:00.0, preventing floating bodies and clone hallucinations.
2. **Subject-to-Scale Invariance & Frame Capacity Law**:
   - Single-subject scales (`CU`, `MCU`, `Choker`) strictly frame ONE actor. Secondary characters are `O.S.` and must NEVER be declared in `[subject]:` or described in prompt lines.
   - For rapid comedic back-and-forth, alternate angles with crisp `Cut to` transitions on the 180° line.
3. **Somatic Comic Acting & Expressive Speech Verbs**:
   - Direct physical comedy through observable micro-reactions: eye-popping double-takes, stifled giggles, jaw drops, throat swallows, and flustered hand fluttering.
   - Bind spoken lines with somatic speech verbs: `trợn tròn mắt phân trần :`, `bấm bụng cười nén :`, `giật thót hét to :`, `lí nhí chối quanh :`.
4. **Zero Dead Air & Dynamic WPS Calibration**:
   - Spoken cadence is calibrated at 1.8–2.2 WPS.
   - Terminal phases (`[00:07.0–00:10.0]`) feature living respiratory reactions, lingering awkward stares, or physical comedic settles—never a frozen frame.
5. **The 4 Sovereign Anti-Stagnation Laws (Chống Đơ & Bệnh Đẹp Đều)**:
   - *Purge Hollow Beauty Buzzwords*: Ban `photorealistic, cinematic 8k, masterpiece, moody lighting`. Use crisp high-key daylight, practical kitchen lamps, and tactile domestic textures.
   - *Targeted Action Verbs*: Replace passive adjectives (`looks funny`, `is shocked`) with dynamic kinetic verbs (`hất văng thìa`, `vỗ đét vào đùi`, `nhổm người ngó trộm qua vách`, `chộp lấy ấm trà`, `nuốt ực trân trối nhìn`).
   - *Compulsory Tactile Prop Interaction*: Comic timing lives in props. Every character must hold, drop, clatter, polish, or fiddle with utensils, scorched pans, tea cups, or doorknobs. Zero limp, empty hands.
   - *Dynamic Editing Rhythm*: Comedic pacing thrives on cuts! Split comic confrontations into multi-shot sequences (Setup ➔ Punchline cut ➔ Double-take reaction cut ➔ Escalation). Never abandon a scene to a single static 20s–30s take.

---

## 5. Quality Assurance Gate & Pre-Delivery Audit

Before any sitcom screenplay is delivered to the user or compiled for production, the Screenwriter and Director must run this **14-Point Pre-Flight Audit**:

```
[ ] 1. Core Dilemma & Logline: Is the central comic predicament crystal clear within the first 60 seconds (Page 1–2)?
[ ] 2. Dual Plot Resolution: Do both A-Plot and B-Plot possess clear inciting incidents, escalations, and satisfying resolutions?
[ ] 3. Scene Utility: Does every single scene have a defined objective, active obstacle, and an emphatic ending button?
[ ] 4. Genuine Escalation: Does the conflict compound exponentially rather than circling the same baseline annoyance?
[ ] 5. Cold Open & Tag Symmetry: Do the Cold Open and Tag feature high-impact punchlines with thematic or callback mirroring?
[ ] 6. Character-Driven Comedy: Are at least 80% of laughs derived from character flaws rather than generic stand-up one-liners?
[ ] 7. Distinct Acoustic Voices: Are character voices clearly differentiated with zero expository data-dumping?
[ ] 8. Timing & Page Budget: Does the page count strictly conform to the runtime standard (~1 page per minute)?
[ ] 9. Taste & Ethical Boundary: Does the comedy strictly avoid punching down, malicious bigotry, or trivializing genuine tragedy?
[ ] 10. Status Quo Reset: Does the episode conclude with the world returning to dynamic equilibrium ready for the next episode?
[ ] 11. Buzzword Purge Gate: Zero instances of 'photorealistic', 'cinematic 8k', or hollow beauty modifiers; lighting grounded in concrete physical fixtures.
[ ] 12. Active Verb Saturation: Every micro-phase driven by purposeful kinetic verbs of disruption, zero abstract emotional adjectives.
[ ] 13. Tactile Prop Contact: Every character's hands actively engage a prop or architectural surface in every single shot.
[ ] 14. Dynamic Editing Rhythm: Scenes > 10s partitioned into Track B multi-shot cuts with tempo variation and >30° angle shifts.
```

---

## 6. Output Formats & Operational Modes

### 6.1 Delivery Presentation
- **Short Requests (Cold Open or Single Scene)**: Rendered directly in chat markdown with standard screenplay format.
- **Full Episode Scripts**: Created and saved as a complete standalone document file (`.html` or formatted script markdown) for easy reading, export, or production.
- **Header Presentation**: Every delivered episode must open with:
  - Episode Title & Number
  - Episode Logline
  - Active Cast List
  - Estimated Runtime
  - Primary Set Locations
- **Ending Polish Menu**: Conclude delivery with **2–3 actionable enhancement pathways**:
  - *Option 1*: Punch up joke density and accelerate dialogue banter.
  - *Option 2*: Deepen character vulnerability and the Act 3 emotional warmth.
  - *Option 3*: Expand the premise into a multi-episode Season Arc Map.

### 6.2 Handling Common Request Variations
1. *"Cho tôi ý tưởng sitcom (Give me sitcom ideas)"*:
   - Provide 3–5 high-concept loglines, each featuring the central trapped circumstance, character dynamic, and engine of conflict.
2. *"Viết cold open / một cảnh (Write a cold open / single scene)"*:
   - Bypass the extended series bible; dive straight into rapid action with an explosive opening hook and a killer button.
3. *"Viết lại cho hài hơn (Punch up / make it funnier)"*:
   - Identify dead-air lulls; add escalation layers; compress dialogue lines; move punchwords to the end of sentences; inject dramatic irony or visual prop comedy.
4. *"Lên kế hoạch cả mùa (Plan a full season)"*:
   - Construct the Master Series Bible + a 10–13 Episode Season Map (Pilot, Midseason Escalation, and Season Finale with a dynamic pseudo-reset).
5. *"Chuyển thể / đổi bối cảnh (Adapt or transpose style)"*:
   - Preserve the underlying character chemistry and structural dynamics while completely rebuilding the cultural milieu, slang, and domestic props to fit the new setting.

### 6.3 Copyright & Originality Mandate
Under no circumstances may scripts copy dialogue, characters, or specific story beats from existing copyrighted television shows (e.g., *Friends, The Office, Brooklyn Nine-Nine, Gia Đình Là Số 1*). All characters, situations, cultural references, and punchlines must be 100% original creations engineered specifically for the project.

---

## Mastery Playbook — Sitcom (README §2c)

### P1. The promise and the three killers
- **Promise**: characters we love trapped together, making a small problem enormous because of who they are — and everything back to normal by the end, so we can do it again next week.
- **Killer 1 — jokes instead of situations**: laughs must come from character flaws colliding, not from one-liners anyone could say.
- **Killer 2 — real tragedy**: stakes feel huge to the characters and small to us; nobody is truly hurt.
- **Killer 3 — no escalation**: the lie or plan must get worse three times before it collapses.

### P2. Series architecture (Engine 5 — Snowball & Reset)
- **The ensemble map**: 3–5 regulars, each with one fixed flaw and one fixed want that clash (the perfectionist vs. the slob, the miser vs. the show-off). Write the **clash grid** once; every episode is a cell of that grid.
- **Episodes are self-contained**; only small threads carry over (a running gag, a slow romance, a recurring rival). A light season arc may peak at the midpoint and finale without breaking the reset.
- **Running gags**: plan 2–3 that recur with a variation each time and pay off in the finale (rule of three across the season).

### P3. Episode architecture (6–8 scenes, 60–80s)
| Phase | Scenes | Job |
|---|---|---|
| Petty spark | 1–2 | A tiny want or mishap, hook in 3s |
| Cover-up | 2–3 | A character lies or schemes to avoid a small consequence |
| Snowball | 3–5 | Each attempt to fix the lie needs a bigger lie; a second character gets dragged in |
| Farce collision | 5–6 | All threads meet in one place at the worst moment |
| Reset + button | 7–8 | The truth spills, the status quo returns, and a final visual button (a callback, a reaction) gets the last laugh |

### P4. Signature scene: the farce collision
- Same room, everyone with a different secret, every entrance at the worst time.
- **Reaction delta**: the laugh is on the face of the person who just understood; give that face the hold.
- Physical comedy uses one tactile prop that changes hands (cake, phone, wig) — track its custody.

### P5. Dialogue
- Rapid ping-pong, 3–6 words a turn; the joke word lands **last** in the line.
- Each character's flaw shows in how they speak (the know-it-all corrects, the coward agrees with everyone).
- Example (10s):
  > **Hưng** (giấu chiếc bánh cháy sau lưng): "Bánh hả? Bánh… đang nghỉ."
  > **Vợ:** "Bánh mà cũng nghỉ?"
  > **Hưng:** "Nó làm việc vất vả lắm em."
  > *Khói bốc lên từ sau lưng anh.*

### P6. Hooks, twists, buttons
- Hooks: #7 Disrupted Order, #2 In Medias Res, #11 Diegetic Sound.
- Twists: TW-08 Misunderstanding, TW-14 Irony.
- Episode end: a **button** (callback, a deadpan reaction, the running gag) instead of a cliffhanger.

### P7. Mastery checklist
1. Is the problem small to us and enormous to them?
2. Does the lie escalate exactly three times?
3. Does every laugh come from a character's fixed flaw?
4. Are all threads in one place at the collision?
5. Is the world back to normal — with one new tiny itch — at the end?

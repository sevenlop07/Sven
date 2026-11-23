# Sven Cinematic Universe — Social & Healing Drama Genre Specification & Production Engine
File: `engine/genres/drama.md`
SSOT Status: Authoritative Standard for Social, Emotional & Healing Drama Writing & Directing
Governed by: Screenwriter (Level 2) & Director (Level 2) under Showrunner (Level 1)

---

## Genre Card (README §2b)

| Field | Value |
|---|---|
| **Regime** | 1 — Grounded Real-World Drama |
| **Genre Engine** | 1 — Pressure-Cooker (villain-free healing / slice-of-life stories use `healing.md`, Engine 6) |
| **Audience payoff** | Catharsis and earned empathy |
| **Heart & value payoff** | Reconciliation that costs pride; love, forgiveness and responsibility between generations (`0d` §6) |
| **Cast topology** (`2b-character-lines.md` §2) | A1 + A2 opposing relative (love pointed the wrong way) + family satellites tied to both sides; chorus = relatives, neighbours |
| **Default episode shape** | 0c §4 Archetypes; `75:25` |
| **Preferred hooks** | #6 Body/Expression Detail, #9 Consequence First, #7 Disrupted Order |
| **Preferred cliffhangers** | False Dawn ➔ Cold Water; C4 Document Detonation, C7 Ghost's Arrival |
| **Favoured twists & budget** | TW-04 Perspective, TW-08 Misunderstanding, TW-10 Hidden Kindness, TW-13 Sacrifice; 1 major + 1 minor |
| **Dialogue : visual** | `50 : 50` (subtext dialogue : tactile labor) |
| **Default `ending_mode` / `fatality_policy`** | positive and costly / none (bittersweet on request) |
| **Signature bans** | sci-fi gadgets, magic, spy action, inflated money (0c §8), 5-second sermon conversions |
| **Scorecard criteria that must score 2** | Active character, Natural dialogue, Prediction breaks |

Numbers defer to `engine/references/0c-canonical-numbers.md`; pacing tables below are default sketches.

---

## 0. Core Principles & Dramatic Philosophy

The objective of the Social & Healing Drama Genre Engine is to create emotionally resonant, grounded stories that confront the genuine psychological and societal struggles of human life, leaving audiences with profound emotional catharsis, renewed hope, and an ending that feels undeniably **earned**—strictly rejecting unearned, artificial "fairy-tale happy endings."

### 0.1 The Drama Equation
$$\text{Earned Healing Drama} = \text{Unflinching Reality of Pain} + \text{Internal Arc of Metamorphosis} + \text{Costly Moral Choice}$$

1. **Unflinching Realism of Suffering (Không né tránh nỗi đau)**:
   - Positive, healing drama does not mean sanitizing tragedy or wearing rose-colored glasses. Pain must be palpable, biological, and socially grounded.
   - Societal and familial fractures must be confronted directly. The positivity in drama lies not in the absence of hardship, but in the courage of the human journey through it.
2. **The Earned Resolution Mandate (Cái kết xứng đáng, không phép màu)**:
   - The resolution must be the direct result of the protagonist's painful choices, sacrifices, and active effort.
   - Strictly ban *deus ex machina*, arbitrary coincidences, sudden lotto wins, or convenient miraculous recoveries that rescue characters from structural crises.
3. **The 5 Invariant Pillars of a Truly Satisfying Ending**:
   - (1) **Commensurate Resolution**: The core conflict is resolved at a scale matching its original setup.
   - (2) **Complete Internal Arc**: The protagonist completes their internal journey from a foundational Lie to an earned Truth.
   - (3) **Confronting Injustice / Antagonism**: The opposing force or injustice is directly faced and held accountable (through moral exposure or legal reckoning, without gratuitous cruelty or sadistic revenge).
   - (4) **Emotional Climax Peak**: A deeply cathartic, singular emotional release (an embrace, a long-withheld apology, a courageous public testimony, an unsent letter read aloud).
   - (5) **Resonant Horizon of Hope**: An open, lingering afterglow of hope signaling that while life remains difficult, the characters now possess the spiritual resilience to move forward.
4. **Anti-Preachiness & Show, Don't Lecture (Tuyệt đối không dạy đời)**:
   - Meaning and moral lessons emerge strictly through characters' physical actions, somatic suffering, and observable consequences—NEVER through didactic speeches, pious voice-overs, or moralizing lectures.
5. **Dimensional Antagonists & Sympathetic Counterforces**:
   - Every character, including adversaries, operates with their own coherent internal justification, generational conditioning, and wounded vulnerabilities.
   - Opponents must be deeply understood, even if their harmful actions are held strictly accountable.
6. **Decisive Lean Intake Protocol**:
   - When core project parameters are underspecified, bundle inquiries into **maximum 3–4 concise questions** in a single pass.
   - If the user desires rapid execution, autonomously adopt robust, culturally authentic defaults and explicitly state what was chosen.

### 0.2 Grounded Realism for Family, Inheritance & Corporate Drama (Regime 1)
- **Believable enterprises and money**: anchor family businesses to tangible industries (hotel & resort chains, commercial real estate, private hospitals, logistics/shipping, retail/food groups, investment firms) and keep figures relatable per `0c-canonical-numbers.md` §8 — never `$50B+` fantasy numbers, never sci-fi gadgets (neuro-watches, AI brain protocols) in a family drama.
- **Real legal and financial friction of the story's country**: contested wills and undue influence, prenuptial and morality clauses, guardianship of an ailing parent, embezzlement of company or pension funds, tax audits, board votes. Use the law of the country where the story is set (e.g., US probate for an American family, Vietnamese inheritance and land-use rules for a Vietnamese family) — never import one country's legal furniture into another's story.
- **Real human betrayals over spectacle**: the drama lives in parents, siblings and in-laws choosing between love, duty and money — not in break-ins, chases or fights (Regime 1 firewall, `workflow.md` §2.4).

---

## 1. Input Collection & Ingestion Matrix

Before launching screenplay production, the Screenwriter gathers the following parameters (bundled into a single concise intake turn):

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              DRAMA INTAKE BUNDLE                                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Core Psychological / Societal Issue: Academic pressure, generational divide,        │
│    school bullying, depression, urban loneliness, vocational prejudice, broken family, │
│    migrant labor, postpartum trauma, eldercare/dementia, grief/bereavement...          │
│ 2. Central Protagonist: Age, socio-economic circumstance, internal wound & burden.     │
│ 3. Milieu & Setting: Geographic region, era, physical environment (school, hospital,   │
│    suburban alley, factory floor, corporate office, rural home, rental room...).       │
│ 4. Delivery Format & Runtime:                                                          │
│    • Standalone Short Film (60s–120s or 5–15 minutes)                                  │
│    • Feature Film (90–120 minutes / ~90–110 script pages)                              │
│    • Multi-Episode Serial Drama / Web-Drama (N Episodes)                               │
│ 5. Tonal Register: Warm & healing, inspirational, quiet & contemplative, raw/grounded. │
│ 6. Target Audience & Sensitivity Boundaries.                                           │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.1 The 1-Topic Seed Engine (Đề xuất hướng đi từ chủ đề thô)
If the user provides only a broad subject (e.g., *"Viết phim về áp lực học đường và khoảng cách cha con"*), the Screenwriter immediately pitches **2–3 divergent narrative trajectories** (each complete with logline, core dilemma, and earned ending):
- **Direction A (The Quiet Rebellion & Shared Silence)**: Focus on institutional/family pressure, non-verbal parent-child tension, and a high-stakes personal secret that forces an honest reckoning at midnight.
- **Direction B (The Dynasty Fracture & Ethical Showdown)**: Focus on dynastic ambition vs. professional/moral integrity (corporate succession, clinical medicine, federal law, or scientific whistleblowing), culminating in a public boardroom or courtroom truth-bomb.
- **Direction C (The Generational Echo & Medical Alert)**: Focus on the father repeating his own father's mistakes until a minor health scare forces an honest conversation on a hospital bench.

---

## 2. Staged Production Lifecycle

Social & Healing Drama development proceeds through four rigorous phases:

```
  Phase A: Story Foundation & Moral Architecture
                 │
                 ▼
  Phase B: Structural Pacing & Beat Sheet (3 Acts / Multi-Episode)
                 │
                 ▼
  Phase C: Designing the Earned Ending (Setup/Payoff & Climax Peak)
                 │
                 ▼
  Phase D: Screenplay Crafting, Subtext & Sensitive Topic Protocols
```

---

### Phase A: Story Foundation & Moral Architecture (Nền móng câu chuyện)

1. **The Dramatic Logline (1–2 sentences)**:
   $$\text{Logline} = \text{[Protagonist with a Wound]} + \text{[Urgent External Goal]} + \text{[Formidable Societal/Relational Obstacle]} + \text{[The Irreversible Cost of Failure]}$$
2. **Central Thematic Question (Câu hỏi trung tâm)**:
   - A profound human dilemma with two honest, difficult answers (e.g., *“Can one forgive without forgetting?”* or *“Is silence a form of protection or a form of abandonment?”*).
   - The film systematically explores and answers this question through action, not dialogue.
3. **The Internal Metamorphosis Arc (Vòng thay đổi nội tâm)**:
   - **The Lie Believed (Niềm tin sai lầm)**: The defensive psychological delusion the protagonist clings to at the start to protect their wounded ego (e.g., *“If I show vulnerability, they will abandon me,”* or *“Love is measured strictly by financial success”*).
   - **The Crucible (Lò luyện thử thách)**: The painful experiences that render this lie unsustainable.
   - **The Truth Learned (Chân lý thức tỉnh)**: The hard-won realization that liberates the character at the climax.
4. **Comprehensive Character Dossiers**:
   - **External Want (Mong muốn bề ngoài)**: Concrete, tangible, and often misguided (e.g., win the scholarship, pay off the debt, force the child into medical school).
   - **Internal Need (Nhu cầu thực sự bên trong)**: The spiritual truth they desperately require (e.g., self-forgiveness, unconditional acceptance, freedom from parental approval).
   - **Root Trauma / The Ghost (Vết thương quá khứ)**: The defining historical loss or betrayal that created their emotional scar.
   - **The Secret / Hidden Burden (Điều họ giấu kín)**: A debt, illness, failure, or shameful truth they expend immense energy hiding from loved ones.
   - **Voice, Dialect & Behavioral Tics**: Speech tempo, regional idiom, physical habits under anxiety.
5. **The Supporting Character Constellation (Mạng lưới nhân vật)**:
   - **The Mentor / Benefactor (Ân nhân / Người dẫn đường)**: Offers tough, unvarnished wisdom without coddling.
   - **The Mirror Character (Gương phản chiếu)**: A peer or secondary figure who shows what happens if the protagonist continues down their flawed path.
   - **The Antagonistic Force (Lực cản)**: Societal prejudice, rigid institution, or a family elder whose love is tangled with toxic expectations.
   - **The Reciprocal Ally (Người đồng hành qua lại)**: Someone the protagonist initially helps, who later returns to pull the protagonist out of the abyss.
6. **The Recurring Motif (Biểu tượng chuyển hóa)**:
   - A concrete physical object, recurring sound, or recurring visual image (e.g., a cracked porcelain teacup, the rhythmic ticking of an antique wall clock, a mother's stained apron, an old bicycle bell).
   - **The Motif Transformation Law**: The motif must appear in Act 1 representing shame, confinement, or trauma, and reappear in Act 3/4 with its emotional meaning transformed 180° into grace, freedom, or enduring love.

---

### Phase B: Structural Pacing & Beat Sheet (Cấu trúc phân cảnh)

#### 1. The 3-Act Feature Architecture (~90–120 minutes / ~90–110 pages)

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE 3-ACT HEALING DRAMA STRUCTURAL MAP                                    │
├─────────────────────┬───────────────────────────┬───────────────────────────┬──────────────────────────┤
│    ACT 1 (~25%)     │       ACT 2A (~25%)       │       ACT 2B (~25%)       │       ACT 3 (~25%)       │
│  Setup & Crack in   │   Testing Old Habits &    │   The Dark Night of the   │  The Moral Choice, Climax│
│   the Ordinary Life │      Midpoint Shift       │    Soul & The Abyss       │    & Lingering Hope      │
├─────────────────────┼───────────────────────────┼───────────────────────────┼──────────────────────────┤
│ • Everyday reality  │ • Protagonist attempts to │ • Price of deception or   │ • Active moral choice to │
│ • The inner crack   │   solve the problem using │   stubbornness explodes   │   abandon the Lie        │
│ • Inciting Incident │   flawed old habits       │ • Trusted ties rupture    │ • Peak emotional climax  │
│ • Initial refusal   │ • Small temporary win     │ • The Abyss / Rock Bottom:│ • Ripple effect across   │
│ • Point of No Return│ • Midpoint Shift: A truth │   The Lie collapses under │   the community / family │
│   into the journey  │   renders old way useless │   unbearable reality      │ • Motif transformed      │
└─────────────────────┴───────────────────────────┴───────────────────────────┴──────────────────────────┘
```

#### 2. Multi-Episode Dramatic Series Architecture
- **Season Arc**: A central thematic spine runs through all episodes (e.g., a fractured family reconciling after the matriarch's stroke).
- **Episodic Narrative Puzzle Pieces**: Each episode explores a specific secondary relationship, generational perspective, or institutional barrier while advancing the overarching spine.
- **The Emotional Hook / Cliffhanger**: Every episode closes on an emotional cliffhanger—a discovered secret, a heartbreaking departure, or a long-withheld confrontation—propelling the viewer into the next episode.

#### 3. Scene Breakdown Specification
Every scene in the drama outline must specify:
- **Heading**: `CẢNH [X]. NỘI/NGOẠI. ĐỊA ĐIỂM - THỜI GIAN`.
- **Characters Present**: Specific active cast members.
- **Scene Objective (Mục tiêu)**: What does the character want in this room right now?
- **Conflict & Resistance (Xung đột)**: What emotional or social obstacle is blocking them?
- **The Value / Power Shift (Sự thay đổi cảm xúc / quyền lực)**: Beginning state $\longrightarrow$ Ending state (e.g., *Defensive arrogance $\longrightarrow$ Crushed vulnerability*).

---

### Phase C: Designing the Earned Ending (Thiết kế cái kết thỏa mãn)

A powerful ending is never improvised in the final act; it is mathematically engineered from the first 10 minutes:

```
                  ┌──────────────────────────────────────────────────┐
                  │          THE EARNED ENDING ANATOMY               │
                  └─────────────────────────┬────────────────────────┘
                                            │
           ┌────────────────────────────────┼────────────────────────────────┐
           ▼                                ▼                                ▼
┌──────────────────────┐        ┌──────────────────────┐        ┌──────────────────────┐
│  Setup & Payoff Law  │        │  Agency & Sacrifice  │        │  Realistic Scale &   │
│  All emotional bombs │        │  Protagonist acts    │        │  Motif Transformation│
│  in Act 3 were sown  │        │  alone; accepts loss │        │  A small community   │
│  in Act 1.           │        │  for deeper truth.   │        │  heals, not world.   │
└──────────────────────┘        └──────────────────────┘        └──────────────────────┘
```

1. **The Setup & Payoff Law (Luật Gieo & Gặt Cảm Xúc)**:
   - Every gesture, prop, or revelation at the climax must be seeded early. An apology in Act 3 lands with devastating weight only if the wound was planted in Act 1.
2. **The Emotional Climax Peak (Khoảnh khắc đỉnh điểm cảm xúc)**:
   - Identify the singular, unrepeatable moment of breakthrough: an estranged daughter washing her mother's swollen feet; a father quietly setting an extra pair of chopsticks on the table; a student finally speaking up against an unjust expulsion.
3. **Protagonist Agency (Chiến thắng bằng hành động tự thân)**:
   - The protagonist must actively step into the fire. They cannot be rescued by a sudden stroke of luck, an unexpected benefactor's money, or the villain's random change of heart.
4. **The Sweet-and-Bitter Equilibrium (Sự cân bằng được và mất)**:
   - Completely sugar-coated endings feel fraudulent to modern audiences.
   - For an ending to feel honest, **the protagonist must accept a meaningful loss** (relinquishing an ambition, walking away from toxic money, admitting public shame) in order to gain a profound, lasting spiritual truth (self-respect, genuine familial reconciliation, peace of conscience).
5. **Societal Resolution at a Human Scale**:
   - Healing drama does not claim to fix systemic world corruption.
   - The triumph is grounded: one neighborhood clinic changes its admission protocol; one father listens to his child for the first time; one broken family shares a quiet, warm meal together.
6. **The Final Scene & Transformed Motif**:
   - The closing scene returns to the central visual motif established in Act 1, but its context is completely transformed.
   - Few words, rich cinematic imagery, allowing the audience space to breathe and integrate the emotional experience.

---

## 3. Screenplay Crafting, Subtext & Technical Format

### 3.1 Industry Screenplay Formatting
The script is formatted cleanly for universal compatibility with screenwriting software (Final Draft, WriterDuet, Fountain) and live production:

```text
CẢNH 12. NỘI. BẾP NHÀ BÀ LÀI - ĐÊM

Một bóng đèn tròn 40W vàng ệch tỏa sáng trên chạn bát gỗ bạc phếch. Khói từ nồi nước sôi bốc lên lững lờ.

BÀ LÀI (62 tuổi, lưng còng nhẹ, mặc áo bà ba vải ú cũ sờn vai) đứng tựa lưng vào bồn rửa bằng xi măng. Đôi bàn tay nứt nẻ vì ngâm nước phèn đang chậm rãi rửa từng chiếc bát sứ mẻ miệng. Động tác chậm, đều đặn đến buốt ruột.

MINH (28 tuổi, vai đeo ba lô bạc màu, mắt trũng sâu vì ba đêm thức trắng) đứng lặng ở khung cửa bếp. 

MINH
Con đi đây.

Bà Lài không quay lại. Tiếng nước nhỏ giọt từ vòi chảy tong tỏng xuống thau nhôm.

BÀ LÀI
(không ngừng tay)
Cơm dưới lồng bàn còn nóng. Khi nào về... thì ăn.

Minh siết chặt quai ba lô. Cổ họng giật nhẹ một nhịp nhưng không nói được thành lời. Cậu quay lưng bước đi.

Bà Lài buông chiếc bát đang rửa dở. Bàn tay già nua run rẩy chạm vào mép bồn rửa, đầu gối khụy xuống một chút nhưng lưng vẫn gượng thẳng.
```

### 3.2 Master Narrative Techniques
1. **The Tactical Subtext Weapon (Lớp nghĩa ngầm)**:
   - Characters in deep pain almost never speak their true trauma directly.
   - A mother nagging about eating more vegetables is actually saying: *“I see that you are suffering and I don’t know how to fix your life.”*
   - A son arguing aggressively over the price of a train ticket is actually saying: *“I am terrified that I cannot provide for you.”*
2. **Show, Don't Tell**:
   - Internal guilt is shown through a man continuously scrubbing a clean tabletop; anxiety is shown through peeling a fingernail cuticle raw; generational love is shown through secretly slipping a warm boiled egg into a worn coat pocket.
3. **The Pregnant Pause (Khoảng lặng điện ảnh)**:
   - Drama breathes in the silence between lines. Screenplay cues such as `(im lặng)`, `(ngập ngừng)`, `(nhìn đi chỗ khác)` must be used intentionally to give actors space for internal transformation.
   - Avoid melodramatic music directions that bully the audience into crying; let the soundscape (rain on tin roof, ticking clocks, distant trains) carry the sensory weight.
4. **Sensory & Emotional Contrast (Nhịp điệu co giãn)**:
   - Continuous bleakness numbs the audience. Intersperse heavy scenes with subtle, authentic slices of everyday humor—a comical bickering over grocery prices, a clumsy slip on a wet floor, a dog barking at an odd delivery man.
   - Humor allows the film to breathe, making the subsequent emotional impact hit ten times harder.
5. **Vietnamese Kinship Pronouns & Cultural Realism**:
   - In Vietnamese domestic drama, address forms (`con/mẹ`, `anh/em`, `chú/cháu`, `mày/tao`, `bác/cháu`) are structural barometers of emotional distance and power dynamics.
   - A shift in address form (e.g., from an estranged, cold *“Chị - Tui”* to a tearful *“Má - Con”*) represents a seismic character breakthrough without needing explanatory dialogue.
   - Root scenes in authentic Vietnamese domestic textures: the communal dinner tray (*mâm cơm*), the neighborly tea table, high school parent-teacher meetings, hospital corridor waiting mats, seasonal migration journeys (*chuyến xe Tết*).

### 3.3 The Dramatic Spine & 4-Way Cross-Scene Dialogue Relay
In social and healing drama, scenes must never stand as isolated emotional vignettes. Every episode is propelled by an unbroken **Dramatic Spine** ($\mathbf{Spine} = \mathbf{Want} + \mathbf{Obstacle} + \mathbf{Stakes}$). Between Scene $N$ and Scene $N+1$, dramatic dialogue must pass a continuous narrative baton via the **4 Relay Vectors**:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        4-WAY DRAMATIC DIALOGUE RELAY MATRIX                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Cause & Effect Baton: A painful confession, ultimatum, or moral compromise in       │
│    Scene N directly causes the irreversible confrontation in Scene N+1.                │
│ 2. Keyword Echo / Inversion: A loaded phrase or wounded promise from Scene N is        │
│    echoed or shattered by another character in Scene N+1.                              │
│ 3. Emotional Inertia / Somatic Respiration: The suffocating grief, defensive anger,    │
│    or fragile breakthrough of Scene N carries into the opening 3s of Scene N+1.        │
│ 4. Prop Anchor Relay: A physical object carrying immense emotional weight (a pawn      │
│    ticket, a hospital bill, a congealed bowl of congee, an unsent letter) crosses      │
│    the cut from Scene N into Scene N+1.                                                │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.4 The 3-Layer Organic Dramatic Dialogue Anatomy & Anti-Curtness Law
Vietnamese dramatic dialogue must never sound curt, dry, or like robotic commands (*thoại cộc lốc, trơ khấc*). Pain and healing in Vietnamese culture are expressed through acoustic delicacy, respiratory vulnerability, and kinship honorifics. Every dramatic line is constructed via the **3-Layer Organic Anatomy**:

$$\mathbf{Line} = \mathbf{[Layer\ 1:\ Acoustic\ Inception]} + \mathbf{[Layer\ 2:\ Dramatic\ Payload]} + \mathbf{[Layer\ 3:\ Modal\ Particle\ Landing]}$$

1. **Layer 1: Acoustic Inception (Hô ngữ & Hơi thở dẫn nhập)**:
   - Sets the acoustic frequency and interpersonal vulnerability before words land.
   - Natural emotional starters: `Má ơi...`, `Thầy ơi...`, `Dạ chú...`, `Em nè...`, `Con xin má...`.
2. **Layer 2: Dramatic Payload (Nhân kịch tính & Tổn thương nội tâm)**:
   - The core emotional truth, hidden plea, or costly moral decision.
   - Sweet spot: **8 to 14 words** with internal respiration pauses (`...`) allowing biological breath and tears to register.
3. **Layer 3: Modal Particle Landing (Trợ từ tình thái hạ cánh)**:
   - Sentence-final modal landing particles that soften or sharpen emotional intimacy: `mà má`, `đâu anh`, `sao đặng`, `được hông`, `vậy nè`, `hở con`.

> **Negative Example (Banned — Curt & Robotic)**:
> `DUYÊN: Con không có sữa cho con bú.` *(8 words — dry, factual statement, zero emotional resonance).*
>
> **Positive Example (3-Layer Organic Dramatic Line)**:
> `DUYÊN (nghẹn ngào nấc nghẹn): Má ơi... con cố vắt kiệt cả hai bên rồi, mà sao giọt sữa nào cũng không ra hết má!` *(Layer 1: "Má ơi..." + Layer 2: physical exhaustion & heartbreak with respiration + Layer 3: emotional landing "hết má!").*

### 3.5 AI Video Prompt Directing for Drama (Code Block 1 Standard)
When compiling dramatic scenes for generative video diffusion models (Sora, Kling, Runway Gen-3, Wan 2.1), the Director must enforce:
1. **The 4-Part Sovereign Subject Formula in `[subject]:`**:
   `{ho_ten} [100% Appearance, attire, and facial features Refer to image X], {initial spatial anchor to architectural fixture}, {initial physical posture & tactile contact} — the only {ho_ten} in frame.`
   - Anchors character bodies to physical set pieces at 00:00.0, eliminating floating bodies and clone hallucinations.
2. **Subject-to-Scale Invariance & Frame Capacity Law**:
   - Single-subject scales (`CU`, `MCU`, `Choker`) strictly frame ONE actor. Secondary characters are `O.S.` and must NEVER be declared in `[subject]:` or described in prompt lines.
3. **Somatic Micro-Directing & Expressive Speech Verbs**:
   - Direct biological suffering and tenderness: tears welling on the lower eyelid without falling, nostrils flaring with choked breath, lips trembling against ceramic spoons, knuckles blanching white against bedrails.
   - Bind spoken dialogue with somatic speech verbs: `nghẹn ngào nấc nghẹn :`, `run rẩy van nài :`, `cay đắng thì thầm :`, `nén đau thầm thì :`.
4. **Zero Dead Air & Living Settle**:
   - Terminal phases (`[00:07.0–00:10.0]`) maintain continuous respiratory rhythm, lingering gaze, and subtle hand adjustments—never a frozen frame.

---

## 4. Sensitive Topic Safety Protocols (Xử lý chủ đề nhạy cảm)

When addressing acute social wounds—such as depression, self-harm, academic despair, sexual assault, domestic violence, or bereavement—the Screenwriter must enforce these strict ethical standards:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ETHICAL PROTOCOL FOR SENSITIVE THEMES                           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Zero Graphic Portrayal: Absolute ban on depicting specific methods, mechanics, or   │
│    tools of self-harm, suicide, or sexual abuse. Focus entirely on psychological       │
│    aftermath and recovery.                                                             │
│ 2. Anti-Romanticization: Suicide, self-destruction, or tragic death must NEVER be      │
│    framed as romantic, noble, poetic, or as an effective way to "punish" others.       │
│ 3. Natural Support Pathways: The story must depict seeking help (family, trusted       │
│    mentors, healthcare professionals, community elders) as an act of courageous agency.│
│ 4. Believable Psychology: Mental health struggles must be portrayed with scientific   │
│    and psychological nuance, never treated as cheap plot melodrama or demonic behavior.│
│ 5. Dignity for Vulnerable Groups: Characters with disabilities, impoverished workers,   │
│    or marginalized victims must never be treated as pitiful charity props. They must   │
│    possess pride, agency, complex virtues, and flaws.                                  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Quality Assurance Gate & Pre-Flight Audit

Before delivering any dramatic script, treatment, or outline, the Screenwriter runs this **10-Point Drama Integrity Audit**:

```
[ ] 1. Clear Logline & Thematic Core: Does the logline clearly state the protagonist's wound, desire, obstacle, and cost of failure?
[ ] 2. Complete Inner Arc: Does the protagonist genuinely journey from a destructive Lie to a hard-earned Truth?
[ ] 3. Grounded Societal Reality: Is the social problem dramatized through specific, concrete human friction rather than preachy dialogue?
[ ] 4. Dimensional Antagonism: Does the opposing force or antagonist possess an understandable internal motivation and human vulnerability?
[ ] 5. Earned Lowest Point (The Abyss): Is the Dark Night of the Soul painful enough that the subsequent turnaround carries genuine weight?
[ ] 6. Protagonist Agency: Does the protagonist achieve their emotional/moral victory through their own proactive choice, without magical intervention?
[ ] 7. Setup & Payoff Integrity: Are all pivotal third-act emotional keys, props, and revelations strictly planted in Acts 1 and 2?
[ ] 8. Sweet-and-Bitter Equilibrium: Does the ending balance an earned triumph with an honest, meaningful loss rather than a sugary fairy tale?
[ ] 9. Ethical & Sensitive Dignity: Does the script strictly comply with sensitive topic safeguards, treating vulnerable characters with deep respect?
[ ] 10. Industry Script Pacing: Does the page and beat count correspond accurately to the target runtime (~1 page per minute)?
```

---

## 6. Output Formats & Operational Modes

### 6.1 Delivery Presentation
- **Short Requests (Single Scene, Logline, or Beat)**: Rendered directly in chat markdown with complete screenplay formatting.
- **Full Scripts, Feature Outlines, or Series Bibles**: Created as complete standalone project files (`.html` or `.md`) for seamless review and production.
- **Executive Header**: Every delivered script begins with:
  - Project Title & Format
  - Central Thematic Dilemma
  - Active Cast List (with Want/Need indicators)
  - Estimated Runtime
  - Primary Milestone Sets
- **Ending Polish Menu**: Conclude delivery with **2–3 actionable refinement pathways**:
  - *Option 1*: Deepen the subtext and strip unnecessary spoken dialogue in favor of physical micro-actions.
  - *Option 2*: Sharpen the bittersweet balance of the ending to increase emotional resonance.
  - *Option 3*: Expand the storyline into a multi-episode serial roadmap.

### 6.2 Handling Common Request Variations
1. *"Cho tôi ý tưởng phim về [chủ đề] (Give me drama ideas about...)"*:
   - Provide 3–5 distinct loglines, each highlighting the protagonist's wound, the societal obstacle, and the earned ending direction.
2. *"Viết một cảnh kịch tính (Write a dramatic scene)"*:
   - Jump directly into character objective, deep subtext, observable physical behavior, and a decisive shift in emotional power.
3. *"Phim buồn quá, làm ấm hơn (The story is too bleak, make it warmer)"*:
   - Introduce an authentic companion/mentor; insert moments of mundane everyday humor to create breathing room; transform the lowest point into a turning point of agency rather than hopeless paralysis.
4. *"Cái kết chưa đã (The ending feels unearned or weak)"*:
   - Audit the Setup & Payoff trail; strip any lucky coincidences; ensure the protagonist makes an active, costly sacrifice that directly earns their spiritual redemption.
5. *"Lên kế hoạch cả mùa (Plan a multi-episode season)"*:
   - Build the Master Series Bible + Season Arc Map (establishing how each episode tackles a piece of the societal/familial puzzle leading to the final catharsis).

### 6.3 Originality & Copyright Mandate
All characters, backstories, family dynamics, and dramatic resolutions must be 100% original creations. While classical narrative archetypes may inform the structure, copying characters, scenes, or dialogue from existing works (*e.g., Parasite, Reply 1988, The Father, Manchester by the Sea*) is strictly prohibited.

---

## Mastery Playbook — Family Drama (README §2c)

### P1. The promise and the three killers
- **Promise**: the viewer watches people who love each other hurt each other for reasons the viewer understands on both sides — and waits for the moment someone finally pays the price of the truth.
- **Killer 1 — early reconciliation**: a hug or apology in Acts I–II drains every remaining episode. Defences harden before they soften.
- **Killer 2 — the cartoon villain**: the opposing relative must be "love pointed the wrong way"; write their Wound first.
- **Killer 3 — the sermon**: nobody explains the moral; the ending answers with an action or an image.

### P2. Series architecture (Engine 1 — Pressure-Cooker)
| Act | Share | What happens in a family drama |
|---|---|---|
| I Ignition | 20% | A concrete trigger (illness, will, debt, return of an absent member) forces the family into one room; `A1` makes the first protective lie |
| IIA False Dawn | ~22% | `A1`'s tactic seems to work; a cosy scene the audience distrusts; the C-plot relative quietly moves |
| IIB Midpoint | ~23% | The lie is half-exposed by an object, not a speech; one address shift (`"bố"` ➔ `"ông"`) marks the rupture |
| IIIA Dark Night | 25% | The family splits into camps; `A1` loses the person they were protecting; the old wound is named for the first time — through a memory, not a label |
| IIIB+IV Finale | 10% + coda | Public or ritual setting (death anniversary, wedding, hospital, court); `A1` gives up the mask; the opposing relative's Wound is touched; closing image answers the opening image |
- **Master secret**: a family fact (who paid for what, who is whose child, who signed) peeled one layer per episode, fully revealed at ~2/3.
- **B-plot**: the relationship that suffers from `A1`'s lie (spouse, child). **C-plot**: the quiet relative who profits or protects.

### P3. Episode architecture (8–11 scenes, default)
| Scenes | Function | Scene type |
|---|---|---|
| 01 | Ritual of daily life with one wrong detail | Hook |
| 02–03 | Who wants what at the table; first velvet-dagger line | Dialogue |
| 04 | An object reveals more than anyone says | Clue discovery |
| 05 | One character alone: the cost shows on the body | Storytelling / V.O. or silent |
| 06–08 | Confrontation that escalates in three walls | Dialogue / confrontation (one `15s`) |
| 09 | The crisis choice — `A1` protects the lie or the person | Dialogue, `15s` |
| 10–11 | Quiet aftermath, then the cold-water cliffhanger caused by a plant | Silent ➔ hook |

### P4. Signature scene: the family-meal confrontation
- Everyone has a **job with their hands** (pouring tea, peeling fruit, serving rice). The fight happens *through* the task: who serves whom first, who refuses the bowl.
- Power is spatial: who sits at the head, who stands, who leaves the table.
- Never more than 2 people actively fighting in a shot window; the others react without speaking.

### P5. Dialogue & confrontation
- Kinship pronouns are weapons: the moment someone changes how they address a parent or sibling is a plot event — plan it in the voice profile.
- Attack with care, defend with detail: the antagonist "worries" (`"Mẹ chỉ lo cho sức khoẻ của em thôi"`); the protagonist answers with one specific lived memory, not a slogan.
- Example (10s, two turns):
  > *Chị dâu xới cơm vào bát em chồng, gạt bớt thịt sang bát mình.*
  > **Chị dâu:** "Em ăn chay mấy năm rồi mà, quên à?"
  > **Em chồng** (đặt đũa xuống): "Em ăn chay từ ngày chị dọn vào."
  > *Cả bàn im. Bố gắp miếng thịt bỏ lại vào bát cô.*

### P6. Hooks, twists, cliffhangers
- Hooks: #6 Body/Expression Detail, #7 Disrupted Order, #9 Consequence First.
- Twists: TW-04 Perspective (the cruel one was protecting), TW-10 Hidden Kindness, TW-08 Misunderstanding (≤ 1 act), TW-13 Sacrifice.
- Cliffhangers: an object returns, an overheard sentence, an address that changes, a signature discovered.

### P7. Mastery checklist (add to the Scorecard)
1. Could the opposing relative's view win a family vote? If not, deepen it.
2. Is every confrontation conducted through a domestic task?
3. Has no one apologised or reconciled before the Dark Night?
4. Does each episode move one kinship address or one family secret?
5. Is the ending a gesture or image the opening promised?

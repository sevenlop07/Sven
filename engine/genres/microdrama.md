# Sven Cinematic Universe — Viral Microdrama Genre Specification & Production Engine
File: `engine/genres/microdrama.md`
SSOT Status: Authoritative Standard for High-Octane Microdrama, Vertical Serial Writing & Direction
Governed by: Screenwriter (Level 2) & Director (Level 2) under Showrunner (Level 1)

---

## Genre Card (README §2b)

| Field | Value |
|---|---|
| **Regime** | 1 (realistic) or 3 (rebirth / system) |
| **Genre Engine** | 2 — Every-Episode Dignity Reversal |
| **Audience payoff** | A status & dignity reversal on every episode: the overlooked hero's worth recognized |
| **Heart & value payoff** | Integrity outlasts arrogance: the overlooked person's worth is recognized, the wrongdoer meets a fair self-caused consequence, and the crown ends on one act of grace (`0d` §5–§6) |
| **Cast topology** (`2b-character-lines.md` §2) | A1 with hidden status + a ladder of oppressors (rising power) + main oppressor; ally, betrayer, witness who holds proof; mocking crowd that turns |
| **Default episode shape** | `~10` scenes `~100s`, `90:10` |
| **Preferred hooks** | #1 Visual Paradox, #9 Consequence First, #6 Body Detail |
| **Preferred cliffhangers** | C1–C7 rotated, never the same twice in a row |
| **Favoured twists & budget** | TW-12 Reversal, TW-05 Identity, TW-10 Hidden Kindness, TW-02 Karma (fair, self-caused); 1 mini-reversal per episode |
| **Dialogue : visual** | `40 : 60` (status proxies : staccato fencing ≤ 12 words/strike) |
| **Default `ending_mode` / `fatality_policy`** | positive / none |
| **Signature bans** | episodes with no payoff; oppression with no counter-move; gore or slaps (use status proxies); kneeling, begging or humiliation as the reward shot; a hero who gloats or turns cruel; contempt for the poor or the old as a joke |
| **Scorecard criteria that must score 2** | Hook, Cliffhanger, Value shift · Heart & Value: Phẩm giá & công bằng |

Numbers defer to `engine/references/0c-canonical-numbers.md`; pacing tables below are default sketches.

---

## 0. Core Principles & Dramatic Philosophy

The objective of the **Viral Microdrama Genre Engine** (Vi Đoản Kịch Cao Tần) is to engineer hyper-addictive, emotionally electrifying, short-format episodic series (typically 60s–120s per episode across 40–100+ episodes). It targets the dopamine pathways of modern mobile-first audiences (TikTok, YouTube Shorts, Reels, ReelShort, DramaBox) by maximizing dramatic density, eliminating narrative throat-clearing, and delivering visceral emotional payoffs—while upholding Sven's strict **Zero-Fatality & Humanitarian Standards**.

### 0.1 The Microdrama Equation
$$\text{Viral Microdrama} = \text{Hyper-Concentrated Injustice/Stakes} + \text{High-Velocity Escalation (3s/30s/Cliff)} + \text{Dignity Reversal (truth + grace)}$$

1. **The 3-Second Retention Imperative (In Medias Res at Second Zero)**:
   - No scene establishes characters through mundane biographies or passive greetings. Every episode opens at the peak of an active physical dilemma, public humiliation, or irreversible threshold (*In Medias Res*).
2. **The Dignity Reversal Law (Sảng Văn Có Tâm — replaces the "face-slap"; `0d` §5)**:
   - Market microdramas rely on crude screaming, physical slaps, kneeling, begging and violent revenge. They trigger platform bans, degrade aesthetic value, and teach the viewer that cruelty is the prize.
   - Sven's Microdrama keeps the thrill of the reversal but changes its meaning: **the payoff is the wronged person's dignity restored and the truth seen by everyone**, not the opponent's shame. The wrongdoer is undone by their own earlier choices, exposed through planted, unassailable proof (a document, a skill, a witness) and a fair, proportionate consequence (lost position, legal or financial forfeiture, public truth).
   - **The hero wins by integrity and competence and never gloats.** The camera's longest hold goes to the moment the room finally *sees* the hero (recognition) or to the wrongdoer's *realization* — never to kneeling, begging or tears of humiliation.
   - **One act of grace** closes each major arc: the hero offers a fair path, returns what matters, or helps someone who once mocked them. That grace is the final status the viewer remembers, and the heart moment that turns a binge into a story worth sharing.
3. **The Zeigarnik Addiction Loop (The Invariant Closing Cliffhanger)**:
   - An episode of a microdrama NEVER ends on a settled emotional plateau (except the series finale). Every episode concludes on a suspended consequence, a shocking revelation, or an unanswered physical threat, compelling instant transition to the next episode (*Binge-Watching Retention*).
4. **The Staccato Dialogue Fencing Law (≤ 12 Words Per Strike)**:
   - Dialogue functions as kinetic combat. Characters deliver concise, razor-sharp lines that cut through pretense, accompanied by intense micro-biomechanical gaze locks and posture shifts.

---

## 1. Official Nomenclature & System Taxonomy

| Level | Designation | Description |
|---|---|---|
| **System Module ID** | `microdrama` | Activated in `AGENT.md`, `workflow.md`, and project configurations. |
| **English Formal Label** | **Viral Microdrama & High-Retention Short Series** | Master commercial designation for episodic digital distribution. |
| **Vietnamese Industry Term** | **Vi Đoản Kịch Cao Tần (Cinematic Microdrama)** | Dòng phim ngắn nhiều tập kịch tính cao tần, chuẩn điện ảnh di động. |
| **Platform Optimization** | 9:16 Vertical Mobile or 16:9 Rapid-Kinetic Cinema | Optimized for ReelShort, DramaBox, TikTok Series, YouTube Shorts. |

---

## 2. The 5 Sovereign Optimization Pillars for Microdrama

### Pillar 1: The Asymmetrical Retention Curve (6-Phase Episode View of the Pillar 1 Part X 13-Beat Map)
> The 6 phases below are the per-episode condensation of the 13-Beat Map in `1-narrative-screenplay-architecture.md` Part X (which spans a whole series or long episode). Scene count and runtime: `0c-canonical-numbers.md` §4.
Uniform pacing destroys mobile retention. Microdramas must distribute narrative weight asymmetrically across the episode run:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ [0% ──► 5%]    BEAT 1: COLD HOOK ──► Extreme visual paradox; 0 explanation. │
│ [5% ──► 20%]   BEAT 2: THE OPPRESSIVE SQUEEZE ──► Adversary tightens trap.  │
│ [20% ──► 40%]  BEAT 3: RESISTANCE & DEFLECTION ──► Flawed defense / secrets.│
│ [40% ──► 65%]  BEAT 4: THE MIDPOINT TREMOR ──► Shocking evidence surfaces. │
│ [65% ──► 85%]  BEAT 5: THE VOLTAGE APEX ──► Showdown / Truth bomb lands.   │
│ [85% ──► 100%] BEAT 6: ZEIGARNIK CLIFFHANGER ──► Suspended cliff / Cut!    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Pillar 2: The Contextual Safety Evasion Engine (Filter-Proof Drama)
Microdramas thrive on high conflict. To prevent automated AI video platform rejections and social media bans:
- **Banned Violence Triggers**: No physical beatings, blood, open wounds, strangulation, or death curses.
- **Cinematic Status Proxies**:
  - Instead of a slap: An arrogant adversary flings a document onto the floor tiles; the protagonist calmly picks it up, smooths it flat and places it back on the table, signature side up.
  - Instead of violence: Security locks clicking shut, a bank account balance dropping to zero on a glass terminal, a corporate seal broken.
  - Instead of medical gore: A clinical patient wristband, a stamped discharge notice, trembling pale hands concealing an empty pill vial.

### Pillar 3: High-Gloss Visual Staging & Dynamic Parallax
Low-budget microdramas look flat and cheap. Sven Microdramas mandate:
- **High-Dynamic Contrast Lighting**: Deep atmospheric shadows paired with sharp 45° rim separation lights on character hair and shoulders.
- **Multi-Plane Spatial Staging**: Foreground obstruction (glass partitions, champagne glasses, door frames) framing the middleground confrontation.
- **Elastic Track Modulation**:
  - *Track A (Unbroken Take)*: Steadicam tracking an arrogant stride down an executive corridor.
  - *Track B (Multi-Shot Fencing)*: 3-shot kinetic montage (Attacker OTS ➔ Insert Prop Proof ➔ Defender Reverse OTS).
  - *Track AB (Hybrid)*: 7s continuous push-in on silent defiance ➔ 3s hard cut to the shattering truth.

### Pillar 4: The 7 Master Cliffhanger Archetypes (C1–C7)
Every microdrama episode concludes with one of these codified cliffhangers:
1. **C1 — The Identity Unmasking**: An alibi collapses; a mask slips off; a concealed face is reflected in glass.
2. **C2 — The Physical Threshold Ambush**: A hand grips a locked doorknob; an intruder's shadow blocks the only exit.
3. **C3 — The Treasonous Betrayal**: The protagonist's trusted ally is revealed holding the adversary's seal.
4. **C4 — The Irreversible Document Detonation**: An envelope tears open; the final clause exposes an undercover sting.
5. **C5 — The Catastrophic Ultimatum**: A 10-second countdown begins; one character is forced to sign or surrender.
6. **C6 — The Suspended Strike**: A hand raised, a weapon unholstered, or a decree uttered—cutting to black on the intake of breath.
7. **C7 — The Ghost's Arrival**: The person believed dead or banished walks through the grand double doors.

### Pillar 5: Staccato Dialogue & The 3-Step Strike Cadence
Confrontational dialogue is strictly capped at $\le 12$ words per line, executing the 3-step psychological strike:
1. *The Provocation (Antagonist)*: Arrogant taunt questioning legitimacy (4–8 words).
2. *The 1.5s Somatic Gaze Arrest*: Protagonist locks eyes down the axis; jaw muscle tightens; dead silence.
3. *The Fatal Reversal (Protagonist)*: Calm, razor-sharp sentence invoking unassailable authority (6–10 words).

---

## 3. The 8 Master Microdrama Trope Archetypes (MD-01 to MD-08)

| Code | Trope Name | Core Dynamic & Conflict Engine | The Dignity Reversal (Catharsis + Heart) |
|---|---|---|---|
| **MD-01** | **The Hidden Titan** *(Chủ Tịch Ẩn Thân)* | Tycoon or master disguised as humble worker/janitor to test loyalty or expose corruption. | Corporate executives enter and greet the mocked protagonist by title; the corrupt manager's own records end his post — and the hero keeps the honest staff who were kind when no one was watching. |
| **MD-02** | **The Silent Martyr** *(Nỗi Oan & Hy Sinh Thầm Lặng)* | Daughter-in-law or spouse silently endures humiliation to secretly fund elder's surgery/save family. | The medical receipt / pawned heirloom is revealed; the in-law finally sees the love behind the silence (recognition), and the family's first real conversation begins. |
| **MD-03** | **The Contract Trap** *(Hôn Nhân Hợp Đồng Lật Kèo)* | Fake marriage between cold CEO and spirited underdog designed for mutual benefit. | The emotional mask slips; what began as a transaction turns into an all-consuming protective obsession. |
| **MD-04** | **The Stolen Royal Lineage** *(Thừa Kế Thất Lạc)* | Impoverished protagonist cast out; fraudulent imposter claims their rightful dynasty. | The biometric test / heirloom token activates; rightful patriarch expels the pretender and embraces the true heir. |
| **MD-05** | **The Underdog Phoenix** *(Trở Lại Đỉnh Cao / Báo Thù)* | Protagonist betrayed, bankrupted, and exiled returns with sovereign power to reclaim what was stolen. | Systematic legal and financial truth-telling; each betrayer is undone by their own records, and the hero chooses justice over revenge — returning what was stolen to the people it hurt. |
| **MD-06** | **The Unspoken Counter-Sting** *(Bẫy Trong Bẫy)* | Antagonist gloats over successful theft or blackmail, believing victory is total. | Protagonist smiles calmly, revealing hidden microphones or an already nullified counterfeit contract. |
| **MD-07** | **The Second Chance Rebirth** *(Làm Lại Cuộc Đời)* | Protagonist granted awareness of past tragic errors, systematically avoiding the fatal traps. | Anticipating every ambush; outmaneuvering former tormentors with uncanny foresight. |
| **MD-08** | **The Discarded Genius** *(Thiên Tài Bị Ruồng Bỏ)* | Master physician, engineer, or strategist mocked by elitist peers and expelled from the institution. | The institution's grand project fails exactly where the genius warned; the genius helps anyway — on fair terms that protect the people the project serves. |

---

## 4. Episodic Pacing & 10-Second Scene Breakdown Protocol

Inside a standard **100-Second Microdrama Episode (10 Scenes $\times$ 10.0s)**:
- **Scene 01 [00:00–00:10] (Hook)**: In Medias Res shockwave; visual paradox; audience cognitive gap opened.
- **Scene 02 [00:10–00:20] (Oppression)**: Antagonist asserts dominant status; physical/financial exit sealed.
- **Scene 03 [00:20–00:30] (Resistance)**: Protagonist uses subtext-dense deflection; tension escalates.
- **Scene 04 [00:30–00:40] (Plant)**: Physical proof / sensory clue subtly captured by camera.
- **Scene 05 [00:40–00:50] (Midpoint Tremor)**: Shift in power balance; first sign of adversary's vulnerability.
- **Scene 06 [00:50–01:00] (Collision)**: Direct confrontation; Track B rapid dialogue fencing.
- **Scene 07 [01:00–01:10] (Escalation)**: Stakes double; outside forces (police, executives, family) arrive.
- **Scene 08 [01:10–01:20] (Counter-Strike)**: Protagonist presents decisive artifact; adversary falters.
- **Scene 09 [01:20–01:30] (The Abyss or Peak Shock)**: The truth lands; crowd reacts in stunned disbelief.
- **Scene 10 [01:30–01:40] (Zeigarnik Cliffhanger)**: Suspended outcome C1–C7; abrupt cut on emotional apex.

---

## 5. Integration with the Sven Engine Pipeline

1. **Activation Command**:
   - `» Microdrama Narrative Mode — ON (engine/genres/microdrama.md)`
2. **Precedence**:
   - When active, `microdrama.md` enforces high-frequency pacing, Staccato dialogue, and persistent cliffhangers over the slow-burn contemplative pacing of `drama.md`.
   - Core constraints (`workflow.md §2`: Zero Dead Air, Zero Cumulative Timestamps, 10s atoms, Safe Metaphors) remain universally binding.

---

## Mastery Playbook — Microdrama (README §2c)

### P1. The promise and the three killers
- **Promise**: injustice the viewer feels in the first 3 seconds, and a payoff — a dignity reversal, the hero's worth seen — **in every single episode**, with a bigger one always looming; the series leaves the viewer believing that integrity and kindness win (`0d`).
- **Killer 1 — oppression without a counter**: an episode where the hero only suffers loses the swipe.
- **Killer 2 — the payoff that costs nothing**: the reversal must use something planted earlier (a document, a skill, a witness), never a random rescuer.
- **Killer 3 — slow talk**: any line over ~12 words in a strike, any greeting, any explanation.

### P2. Series architecture (Engine 2 — Every-Episode Dignity Reversal)
| Block | Episodes (of 30–80) | Job |
|---|---|---|
| Hook block | 1–3 | A sharp injustice against the hero + the hidden identity/skill/kindness the viewer knows and the oppressors don't (dramatic irony) + the first mini-reversal at the end of Ep 1 |
| Ladder block | 4 – ~60% | Each episode: a bigger oppressor arrives (the "higher boss"), overreaches, and is undone by the truth; each reversal reveals one more layer of the hero's real worth — status *and* character |
| Betrayal block | ~60–80% | The ally or the person the hero protected switches side; the hero loses publicly once — the viewer must doubt |
| Crown block | last ~20% | The public truth about the main wrongdoer in front of the community that mocked the hero; a fair consequence; then **one act of grace** from the hero and a short, quiet walk-away |
- Plan a **reversal ladder**: list every oppressor in rising power, the planted proof that exposes each one, and the fair consequence each meets.

### P3. Episode architecture (~10 scenes, ~100s)
| Scenes | Function |
|---|---|
| 01 | Cold hook: humiliation or shock in progress, no explanation |
| 02–03 | Squeeze: oppressor seals the exits (status proxies: contract, seat, badge, title) |
| 04 | The hero's quiet counter-move or a plant the camera catches |
| 05–06 | Bait: the oppressor overreaches in public |
| 07–08 | The reversal: proof revealed, the crowd sees the truth |
| 09 | Fallout on faces; the hero says almost nothing and does not gloat (a heart beat lives here: someone finally sees the hero) |
| 10 | Zeigarnik cliffhanger: the higher boss arrives or a new threat lands (C1–C7, rotate) |

### P4. Signature scene: the public reversal
- Always in front of witnesses (board, wedding, family, livestream comments). The crowd is the scoreboard.
- Reversal = an **object** (seal, contract, bank screen, ID) placed on the table, not a speech.
- The longest hold goes to the wrongdoer's realization or to the face that finally recognizes the hero — never to kneeling, begging or humiliation; the hero gets the shortest line.

### P5. Dialogue & confrontation
- Strike cadence: provocation ➔ `1.5s` gaze ➔ fatal reversal, `≤ 12` words per strike.
- The oppressor talks a lot; the hero answers in `2–6` words.
- Example (10s):
  > **Trưởng phòng** (ném tập hồ sơ): "Loại thực tập như cô, mai khỏi đến."
  > **Ngân** (đặt thẻ nhân viên lên bàn, mặt sau hướng về anh ta): "Mai anh đọc kỹ chữ ký sếp mới."
  > *Hắn lật thẻ: chức danh Tổng giám đốc. Tay hắn khựng giữa không trung.*

### P6. Hooks, twists, cliffhangers
- Hooks: #1 Visual Paradox, #9 Consequence First, #6 Body Detail.
- Twists: TW-12 Reversal, TW-05 Identity, TW-10 Hidden Kindness, TW-02 Karma (fair and self-caused).
- Cliffhangers: rotate C1–C7; never the same code twice in a row.

### P7. Mastery checklist
1. Does this episode contain one complete dignity reversal, and does it set up a bigger one?
2. Was the proof used in the slap planted at least one episode earlier?
3. Is every injustice shown through status proxies, not violence — and is the payoff dignity restored, not the opponent humiliated (`0d` §5)?
4. Does the hero's real status rise by exactly one visible step?
5. Is the last frame a new, more powerful threat — with a seed of hope the viewer holds onto?

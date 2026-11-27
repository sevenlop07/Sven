# story-structure.md — Cinematic Single-Narrator Architecture (`Track S` Short & `Track L` Series)

> **Purpose:** Distills the Sven Master Screenplay Architecture (`workflow.md` §6 & `engine/references/1-narrative-screenplay-architecture.md` Part I + Part II §5) into a production-ready narrative blueprint for the **Semi-Real Roblox CGI Cinema Studio (`@RobloxDirector`)** running **Mode N1: Cinematic Narration / Tự sự kể chuyện (`1 single consistent narrator voice track` — 1st-person `"I / Tôi..."` or literary 3rd-person — paired with silent/non-verbal Roblox CGI cinema acting)**.
>
> **Why Narration-First is the Sovereign Default:** Multi-character lip-synced dialogue movies read stiff on blocky Roblox heads without dedicated multi-actor voice acting & phoneme rigs. Pairing **one expressive narrator voice track** (`voice.mp3` → `audio_to_srt.py`) with **GibbsonTV Semi-Real Cycles visuals, restrained physical acting (`RobloxAnimator` Cinema States), `cinema_expressive` micro-expressions, and Image–Narration Subtext Divergence (*Show, Don't Tell*)** delivers cinema-grade emotion cleanly and reliably. Multi-voice dialogue (`Mode N2`) is opt-in only.
>
> **Scope:** Governs **Stage R1** (concept & series blueprint) and **Stage R2** (episode script before TTS / `.mp3` generation) for ALL genres across both **Preset A (Semi-Real CGI Cinema)** and **Preset B (Roblox Toon Shorts)**. For viral `"In this world/town..."` voice cadence & rule-scoring checks, pair with `script.md` and `town-script.md`.
>
> **Which file wins (one rule for every Roblox narration):**
> 1. **Structure** (tracks, beats, archetypes, series tables, scorecards, twist engine) — **this file**, for every genre.
> 2. **Voice and numbers** (sentence stats, wpm / syllables per minute, the pause rule, banned phrases, no-copy, rotation log) — **`script.md` §0, §6, §9, §11**, for **every** narration, storytime or not.
> 3. **World-rule storytime only** ("In this world/town…": rule formula and rubric, rule lanes, town beat windows) — `town-script.md` + `script.md` §1–§3. These never apply to a drama, mystery or series that has no world rule.
> 4. **Engine-wide numbers** (`engine/references/0c-canonical-numbers.md`) and **character lines** (`engine/references/2b-character-lines.md`) apply unless a Roblox-specific number below says otherwise.
>
> **Automated check:** `python tools/script_check.py <script-sheet.md> --mode story` (any genre) or `--mode town` (storytime); add `--lang vi` for Vietnamese narration (`script.md` §11). Fix every `FAIL` before `GATE R2`.

---

## 0. The 3 Universal Pacing Laws (`20% Invariant Core`)

Every short film (`Track S`) and multi-episode series (`Track L`) obeys these 3 structural invariants:
1. **Anti-Flat-Sawtooth Law**: Episodes in different Acts NEVER share the same beat curve, runtime, or emotional tempo.
2. **Anti-Dead-Finale Fusion Law**: For any series with `N <= 12` episodes, **Act IV (Resolution / Coda) NEVER stands alone as a separate episode** (post-climax standalone episodes suffer ~80% drop-off). The Finale ALWAYS fuses **70–75% Act IIIB (3-Wave Grand Showdown) + 25–30% Act IV (Earned Cost, 180° Echo Prop & Bookend Closing Image)**.
3. **Elastic Scaling**: Episode runtime and cutting density expand and contract with dramatic weight — Ignition episodes stay brisk and hooked (`65–90s`); Midpoint and Finale episodes run denser and longer (`100–160s+`).

---

## 1. Track S — Standalone Short Film (`Format A`: `65s–150s` Closed Arc)

Use Track S when producing a single self-contained story (YouTube Shorts, TikTok, Reels, or 16:9 mini-film).

### 1.1 The 6-Beat / Closed-Arc Spine

| Beat | Runtime % | Narrative Function | 3D Roblox Execution (`Blender 5.3`) |
| :--- | :---: | :--- | :--- |
| **B1. Hook** | `0–10%` | Visual paradox or world anomaly in `0–3s`; personal stake for narrator `A1` by `6s`. | Frame 1 starts *In Medias Res* with real camera motion; zero preamble or backstory lecture. |
| **B2. Setup & Wound Prop** | `10–25%` | Normal equilibrium, `A1`'s Wound / False Belief (`Lie`), plant **Tier-1 Prop (`State 0`)** + 2–3 concrete visual clues (`P1–P3`). | Macro/MCU insert on the physical prop inside the `5-Vector` set; character face plants silent subtext. |
| **B3. 3-Wall Escalation** | `25–55%` | `A1` takes active initiative → backfires (`Wall 1`) → moral/value collision (`Wall 2`) → exits sealed (`Wall 3`). | Progressive camera compression (`WS → MS → MCU`) + lighting tightens toward cold/dark contrast. |
| **B4. 3-Wave Climax & Twist** | `55–85%` | **Wave 1:** Misread shatters (`TWIST` line at `49–78%`) → **Wave 2:** Real loss / near-defeat → **Wave 3:** `A1` drops `Lie` (*Ego Death*) and executes a clever physical **Option C** using the world rule/prop. | Short punchy narration sentences, `0.6–1.3s` ASMR pause after twist, `±3f` face snap (`shocked → determined`) + `hit_stop(2–3f)` on physical turn. |
| **B5. Release & Thermal Flip** | `85–92%` | Physical consequence of Option C + **Earned Cost** (something real paid; never cheap). | Hard-Cut Mood Shift (`≥ 0.15` luminance/temp delta via `apply_cinematic_mood`). |
| **B6. 180° Echo Coda** | `92–100%` | **Hard Coda Cap: B5 + B6 ≤ 15–20% total.** Tier-1 Prop returns in inverted state (`180° Echo`) + Bookend closing frame (or next-danger hook). **Zero preachy morals.** | Final short spoken line ends `0.5–1.5s` before cut; hold on readable visual payoff. |

### 1.2 Track S Production Caps
- **Named Cast:** `3–4` named characters max (`A1` narrator/protagonist, `A2` antagonist/counter-force, `1–2` supporting Tier B).
- **Spatial Zones:** `2–3` distinct staging zones inside `1` primary `5-Vector` set (or `2` connected sets).
- **Word Budget (`~180–220 wpm` EN / `~160–190 wpm` VN):** `65s ≈ 210w` · `90s ≈ 315w` · `120s ≈ 425w` · `150s ≈ 535w`.

---

## 2. Track L — Multi-Episode Series (`Format B`: `3–12+` Episodes)

Use Track L when building an episodic Roblox 3D series that reuses a **Shared Cast & Shared `5-Vector` Sets** across episodes (reducing R4 build effort 3–4× from Episode 2 onward) and writes/renders strictly **1 episode at a time**.

### 2.1 Top-Down 2-Table Lock (Mandatory at `GATE R1` — BEFORE Writing Episode 1)

Never improvise a series episode-by-episode without locking both tables first:

1. **Tier 1 — 8 Series Foundations**:
   - `1. Logline` (1 sentence: Protagonist + Anomaly/Inciting Force + Core Conflict + Stakes)
   - `2. Central Question` (the engine viewers binge to see answered)
   - `3. A1 Want vs. Need` (external goal vs. internal blindspot/`Lie`)
   - `4. A2 Independent Logic` (antagonist / opposing system has coherent self-justifying logic — never cartoonish evil)
   - `5. Master Secret` (**revealed in layers, full truth at ~2/3 of the series — NEVER spoiled in Episode 1**)
   - `6. Transformation Arc` (`A1 State Start → State End`, proven via physical choices)
   - `7. Act & Episode Allocation` (mapping each episode to one of the 5 Archetypes below)
   - `8. Known Ending` (final Option C choice, Earned Cost, and Bookend Closing Image locked upfront)

2. **Tier 3 — Inter-Episode Linking Table**:
   Every transition `Episode N → Episode N+1` MUST carry **at least 2 of 4 concrete bridges**:
   - **(B1) Peak Cliffhanger**: Episode `N` cuts on an active danger, unanswered question, or visual reveal.
   - **(B2) Delayed Setup → Payoff (`n → n+2`)**: A prop, remark, or visual detail planted in Episode `n` detonates 2+ episodes later.
   - **(B3) Visible Physical Consequence**: Scars, broken objects, missing cast members, or changed set dressing remain visibly altered in Episode `N+1`.
   - **(B4) Tier-1 Prop State Evolution**: The signature hero prop physically evolves across the season (`State 0 Intact → State 1 Marked → State 2 Fractured → State 3 180° Echo`).

### 2.2 Triple-Helix Plot Weave & 5 Convergence Nodes

Every Track L series weaves **3 interlocking threads** so no episode feels thin:
- **A-Plot (`55–65%`)**: External spine (`A1`'s `Want` vs. `A2` / World Rule under a ticking clock).
- **B-Plot (`25–30%`)**: Relational heart (`A1 ⇄ Family/Ally` bond — the crucible that shatters `Lie` and unlocks `Need`).
- **C-Plot (`10–15%`)**: Subterranean time-bomb (hidden traitor `B-Judas`, silent guardian, or town anomaly planted in background details) that detonates at Midpoint or Act III.

All 3 threads collide at **5 Mandatory Convergence Nodes**:
`~15%` Inciting Disruption → `~50%` Midpoint Reversal → `~75%` All Hope Lost / C-Plot Bomb → `~85–90%` Climax Crucible → `100%` 180° Echo Coda.

### 2.3 The 5 Act-Specific Episode Archetypes

| # | Archetype | Act | Typical Runtime | Episode Shape & Dramatic Job |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Ignition & Trap** | `Act I` | `65–90s` | Fast 0–3s hook, establish world rule & status quo, slam the exit shut, deliver a mini-taste of the series promise + Ep 1 cliffhanger. |
| **2** | **Counter & False Dawn** | `Act IIA` | `85–110s` | `A1` counter-attacks using their flawed `Lie`, scores a temporary *False Victory* mid-episode, then `A2` / the rule crushes it at the end. |
| **3** | **Midpoint Shatter** | `Act IIB` | `100–130s` | Peel a major layer of the **Master Secret** or detonate a betrayal **mid-episode**, permanently shifting the series from *Mystery* to *Suspense*. |
| **4** | **Siege & Dark Night** | `Act IIIA` | `95–120s` | Safe harbors collapse, C-Plot bomb hits, Tier-1 Prop fractures (`State 2`), `A1` abandons `Lie` and recognizes the true **Option C**. |
| **5** | **Unified Grand Finale** | `Act IIIB + IV` | `120–160s+` | **70–75% 3-Wave Grand Showdown** (Option C + A/B/C convergence) + **25–30% Earned Cost, Prop `State 3`, Bookend Closing Image** (closed ending unless Season 2 is greenlit). |

### 2.4 Multi-Scale Episode Allocation & Cast Caps

| Series Scale | Archetype Allocation | Total Named Cast | Max Named Cast On-Screen / Scene |
| :--- | :--- | :---: | :---: |
| **Mini-Series (`3 eps`)** | `Ep 1: Ignition` → `Ep 2: Midpoint + Dark Night` → `Ep 3: Unified Finale` | `5–6` | `≤ 4` |
| **Standard (`5 eps`)** | `Ep 1: Ignition` → `Ep 2: Counter` → `Ep 3: Midpoint` → `Ep 4: Dark Night` → `Ep 5: Finale` | `5–6` | `≤ 4` |
| **Full Arc (`8 eps`)** | `Ep 1: Ignition` → `Ep 2–3: Counter` → `Ep 4–5: Midpoint (2 layers)` → `Ep 6–7: Dark Night` → `Ep 8: Finale` | `7–9` | `≤ 4` |
| **Extended (`10 eps`)** | `Ep 1–2: Ignition` → `Ep 3–4: Counter` → `Ep 5–6: Midpoint` → `Ep 7–8: Dark Night` → `Ep 9–10: Finale` | `7–9` | `≤ 4` |
| **Season (`12 eps`)** | `Ep 1–2: Ignition` → `Ep 3–5: Counter` → `Ep 6–7: Midpoint` → `Ep 8–10: Dark Night` → `Ep 11–12: Finale` | `8–10` (Roblox build-budget cap, below the engine's `10–14` — `0c` §6) | `≤ 4` |

### 2.4b Series Continuity for a Single Narrator (Track L)
- **Character lines** (`engine/references/2b-character-lines.md`): label roles once (`A1` = the narrator, `A2` = always the opposing force), lock arc points at `GATE R1`, and keep the **Character Arc Map** (episodes × characters: want, knows, relationship, Lie status, present/absent) in Block 2B — updated after every episode. Episode 1 introduces at most `3–4` named characters, later episodes at most `1–2`; nobody vanishes more than `2` episodes without a planted reason.
- **New-viewer opener (Ep 2+)**: Shorts viewers often land mid-series. The first spoken line of every episode after Ep 1 restates the situation in one concrete sentence **and** is itself the hook (*"Three nights ago, the bell started ringing for my grandma."*) — never a "previously on" recap, never more than one sentence.
- **Title format**: `[Series hook] (Part N)` — the hook words stay identical across parts so the series is searchable; the thumbnail shows the episode's new danger.
- **Rotation log for every genre**: append one row per episode to `templates/rotation-log.md` (hook type, twist family, ending type, reveal %, subject, outcome) and run `script_check.py --log` — rotation is not storytime-only.

### 2.5 Choose 1 Primary Genre Engine (from Sven `1-narrative` §5.3)
1. **Engine 1 — Family / Social Pressure-Cooker**: Escalating domestic/community secrets, loyalty vs. truth, a fair karma payoff that leaves room to change.
2. **Engine 2 — Underdog Dignity Reversal**: Public disadvantage or unfair treatment turned via clever physical leverage and planted proof; the payoff is the hero's worth seen, never the bully humiliated (`0d` §5).
3. **Engine 3 — Survival / World-Rule Gauntlet**: Strict environmental/town rules, escalating hazards, resource/trust tradeoffs.
4. **Engine 4 — Detective / Mystery Onion-Peel**: Fair-play physical clues (`P1–P3`), misread suspects, checkmate reveal.
5. **Engine 5 — Episodic Sitcom (Snowball + Reset)**: Comedic premise spirals out of control each episode while keeping a loose B-Plot arc.
6. **Engine 6 — Healing / Slice-of-Life (*Kishōtenketsu*)**: Warm quiet contrast, unspoken care revealed through small daily objects.

---

## 3. The 100% First-Person Narration Adapter (`Law R-VOICE`)

Because `@RobloxDirector` runs **100% First-Person Narration (`1 consistent voice track`)** by default — avoiding multi-actor TTS overhead and dialogue lip-sync fragility — apply these 4 studio rules when turning any Track S or Track L blueprint into Stage R2 script prose:

1. **Image–Narration Subtext Divergence (*Show, Don't Tell*)**: Let the narrator speak what `A1` *believes* (`Lie`) while the 3D camera quietly reveals contradicting physical evidence in the background (`C-Plot` prop, another character's `±3f` eye/face shift, or a doorway shadow).
2. **Inline Quoted Lines Only**: When another character must speak a sharp line, embed it cleanly inside the single narrator's voice (*`Grandpa didn't look up. He just said, "Don't open that door after midnight."`*) — zero multi-voice speaker switching required.
3. **100% Clean Copy-Paste TTS Text (Zero Bracketed Tags)**: Never insert bracketed pause, ASMR, or direction tags (`[PAUSE]`, `[ASMR 1.0s]`, `[NGẮT THỞ ...]`) inside Block 2A narration text — they do nothing in TTS and break clean copy-paste flow. Control pacing naturally through sentence length, short punchy lines, and paragraph breaks; any silence or ambience beat is handled at R3/R5 audio editing if needed.
4. **Zero-Waste Pre-Production Scorecards (Gate Before Recording `.mp3`)**:
   - **`GATE R1` (Track L Series Lock)**: Score the Series Blueprint on **6 criteria (`0–2` each, max `12`, Pass `≥ 9/12`)**: *(1) 3-Second Visual Hook*, *(2) A1 Wound/Want/Need Depth*, *(3) A2 Coherent Opposition*, *(4) Layered Master Secret (held past Ep 1)*, *(5) Triple-Helix A/B/C Convergence*, *(6) Shared Cast & 5-Vector Set Reusability*. Rewrite any series below `9/12` before approving. At `GATE R1` (series and each concept) **and** `GATE R2` (each episode) also score the **Heart & Value Scorecard** (`engine/references/0d-heart-and-value.md` §8: value through a costly choice · planted heart moment · dignity & fairness · takeaway & hope; `0–2` each, pass `≥ 6/8`, no `0`): stories for young viewers must move them and model kindness, honesty and repair — wrongdoers meet fair consequences and can change, nobody is humiliated as the reward.
   - **`GATE R2` (Per-Episode Lock — Track S & Track L)**: Score Episode `N`'s script on the **engine's 8 engagement criteria adapted to narration** (`0–2` each, max `16`, Pass `≥ 12/16` with no criterion at `0` — same scale as `workflow.md` §8.4):
     1. **Hook** — a concrete visual anomaly in `0–3 s` and the narrator's personal stake by `6 s`.
     2. **Open loops** — at every beat cut the viewer is waiting for an answer (loop ledger `L1…` opened/paid by beat).
     3. **Value shift** — every beat flips something for `A1` (safe ➔ threatened, trust ➔ doubt…); no flat beat.
     4. **Prediction breaks** — `≥ 2` broken predictions with fair planted clues (`P1–P3`), major twist is an Option C (§4).
     5. **Rhythm** — a pattern shift every `2–3` beats (tempo, place, tone), a breathing valley before the peak, 2–3 designed pauses (`script.md` §6).
     6. **Active narrator** — `A1`'s own choice turns the episode (Option C), and it costs something.
     7. **Natural narration** — clean single-narrator ear test (`script.md` §0 / §11), feelings shown through action, zero AI clichés or labelled emotions.
     8. **Ending** — next danger / cliffhanger / bookend, a type different from the last episode, zero preachy moral.
     **Hard requirement (not scored):** 100% filmable in Blender 5.3 or Studio (`≤ 4` named cast per scene, Law R-COLLIDE friendly). Rewrite below `12/16` BEFORE generating `.mp3`, and pass `tools/script_check.py`.
   - **Block 2B Retention & Value Map** (added to the asset manifest, one block per episode — Value Card per `engine/references/0d-heart-and-value.md` §3):
     ```text
     VALUE       | Positive value affirmed: [...] — embodied by [Name]'s choice in [Beat]: [...] — at the cost of [...]
     HEART       | Heart moment (💗): Beat [NN] — [specific act / object / recognition] — planted in Beat [AA]
     TAKEAWAY    | What the viewer carries home (never spoken on screen): "[...]"
     SHADOW      | What this episode depicts without glorifying and how it is handled: [...] — or "None"
     HOOK 0–3s   | [the first image the viewer sees] ➔ question it opens
     EP QUESTION | [one yes/no question this episode answers or deepens]
     INTENSITY   | B1:[ ] B2:[ ] B3:[ ] B4:[ ] B5:[ ] B6:[ ]  (1–10; one valley 3–4 before the peak 9–10)
     LOOPS       | L1 opened at …, paid at … ; L2 …
     TWIST       | family (§4.5) · beat % · plants P1–P3
     ENDING      | type (next danger / cliffhanger / bookend) — last episode used: …
     ROTATION    | checked against templates/rotation-log.md (hook, twist family, ending type)
     ```

---

## 4. Anti-Predictability & Unpredictable Ending Engine (`Law R-TWIST`)

> **Distilled from Sven Core** (`0-creative-doctrine.md` §9 + `1-narrative-screenplay-architecture.md` Part IV + `script.md` §3.3 & §4). A good ending is **impossible to guess on the first watch, yet 100% inevitable on rewatch**.

### 4.1 The Audience Prediction Ledger & Option C Law
At every major turning point in Stage R1/R2, track what a smart viewer predicts next and decide whether to keep or break it:
```text
P1 (Beat/Scene) | Viewer predicts … | → KEPT (builds trust)
P2 (Beat/Scene) | Viewer predicts … | → BROKEN at [Twist] | Plants: P1, P2
```
- **≥ 2 `BROKEN` Predictions per Episode** (each backed by concrete plants earlier in the script — zero cheats).
- **Keep Some Predictions**: Breaking everything feels random and kills trust. Kept predictions buy credibility; broken ones spend it at the climax.
- **The Option C Law**: When the audience is locked into a binary choice (`Will A1 obey Option A or rebel with Option B?`), the strongest unpredictable turn is **Option C** — a physical detail or loophole that was visible on screen from the start, ignored by both A and B.

### 4.2 The 5 Fair-Play Misdirection Weapons
1. **Camera May Withhold, Never Lie**: Frame away, cut early, or show a reaction without its cause — never show a fake event. Every clue must hold up on frame-by-frame rewatch.
2. **Emotional Camouflage**: Bury the decisive clue inside a moment of peak laughter, panic, or grief — when the viewer's analytical guard is down.
3. **Double-Meaning Lines & Motifs**: Write lines and recurring objects that read one way before the twist and invert completely afterward (e.g., an innocent joke or insult that turns out to be literally true, without naming the twist mechanism).
4. **Pay-Off Red Herrings**: A suspicious character or object cannot vanish as dead weight — it must pay off with an unexpected real meaning (e.g., the "scary" neighbor was actually protecting the kid).
5. **Knowledge Matrix Mode Switch**: Switch at least once per episode between **Suspense / Irony** (*viewer knows more than `A1`*) and **Mystery** (*another character knows more than the viewer*). Strongest reversal: Irony flips into Mystery when the viewer discovers the "unaware" character **knew all along**.

### 4.3 Keeping Endings Unpredictable Even Under Positive or Closed Endings
When the genre leans hopeful/positive, unpredictability lives in 4 dimensions:
1. **Unexpected Route (*How*)**: Never resolve via a speech, lucky coincidence, or stranger rescue — resolve via `A1`'s clever physical use of the planted prop/rule.
2. **Unexpected Price (*Earned Cost*)**: Someone pays a real, concrete cost the viewer did not expect them to risk.
3. **Who Actually Changes**: The person expected to repent stays rigid, while the overlooked bystander or `A1` themselves undergoes the true shift.
4. **Fear of Ending B**: Make the dark outcome genuinely believable for at least one full beat before the turn so relief feels earned.

### 4.4 The 4-Stage Cold Water Cycle, Double-Bind (`Noble Lie`) & Tantalus Near-Miss (`1-narrative` §5–§8)

Do **not** reduce "Cold Water" to a cheap last-second jump-scare. In Sven Core, it is a **4-Stage Dopamine-to-Adrenaline Reactor** paired with **Delayed Gratification (`Near-Miss`)** that locks viewers into *"The Hunger for Vindication"* across episodes:

1. **The 4-Stage Cold Water Cycle (*Chu Kỳ Gáo Nước Lạnh — Double Twist / Russian Doll*)**:
   - **Stage 1 — False Dawn (`Bình Minh Giả Tạo`)**: Hand the viewer a credible glimpse of reconciliation, relief, or victory → brain releases Dopamine (*Need for Closure*).
   - **Stage 2 — Cold Water Slap (`Cú Tát Chối Bỏ`)**: Right at peak hope, shatter it with a brutal, **caused** rejection or reversal (must stem from a planted person, prop, or choice — zero random accidents; scale to genre: a neighbor's line, returned keepsake, locked door, or thrown heirloom). Dopamine crashes straight into Adrenaline & visceral frustration.
   - **Stage 3 — Double-Bind & The Noble Lie (`Con Tin Lương Tâm`)**: Peel layer 2 (*Subtext Knife*) — reveal the impossible vise forcing the harsh act (`Speak truth = lose loved one` vs. `Play the villain / Noble Lie = save them while bearing scorn`), shown via somatic betrayal (eyes stinging, trembling grip behind their back, never a speech).
   - **Stage 4 — Dramatic Irony Agony (`Khát Khao Minh Oan`)**: **The audience now knows the painful truth, while the other character walks away devastated NOT knowing** — locking an irresistible binge pull into Episode `N+1` (`Ending [Beat 5–6] of Ep N ≡ Cold Water Detonation [Beat 1] of Ep N+1`).
   - *Audio/Visual Execution (Roblox 3D)*: Warm mood + gentle BGM during False Dawn → instant BGM cut to dead silence + 1 sharp real ASMR sound + `≤ 8w` line + `±3f` face snap (`happy → shocked/sad`) → `0.5–1.0s` hold before hard cut.
   - *6 Rotating Cold-Water Triggers (never repeat back-to-back)*: `(1) Planted person arrives` · `(2) Planted object returns altered` · `(3) Sign / note / message lands` · `(4) Truth overheard` · `(5) Promise / rule broken on screen` · `(6) Body or structure gives out`.

2. **The Near-Miss / Tantalus Torment (`45–55% Midpoint` — "Water Retreats 1mm From the Lips")**:
   - Never allow effortless discovery or reunion. Pull `A1` to **1mm from the truth/goal**, then yank it back via **1 of 3 causal antagonist levers** (strictly banning random coincidences):
     - *Tier 1 (Tactical Foresight)*: `A2` moved the witness, erased the clue, or locked the door 5 minutes earlier.
     - *Tier 2 (Poisoned Half-Truth)*: `A2` feeds a half-truth that makes an ally voluntarily slam the door on `A1`.
     - *Tier 3 (Asymmetrical Hostage)*: `A2` leverages a loved one/stake, forcing `A1` or an ally into a *Noble Lie*.

3. **The 5 Jaw-Dropping Reversal Archetypes (*Aristotle: Surprising Yet Inevitable*)**:
   - *(1) Sacrificial Villain / Noble Lie* (hated all story, secretly absorbing the blow)
   - *(2) Moral Paradigm Shift* (the "good" system/belief `A1` served turns out to be the true oppressor)
   - *(3) Pyrrhic Victory & Paradoxical Surrender* (winning the trophy costs the soul; only letting go saves them)
   - *(4) The Arrogant Red Herring* (baiting the viewer's & `A2`'s own cleverness into a staged trap)
   - *(5) Impossible Moral Crucible* (zero-win dilemma broken only by a costly moral choice above self-interest)

4. **Master Coordinate Rhythm Map (*Anti-Overdose Law — Always Place a `3–4/10` Breathing Valley Before Every `9–10/10` Peak*)**:
   `0–5%` Cognitive Gap Hook → `10–25%` Setup & Chekhov Plant (*Emotional Camouflage*) → `25–45%` Knowledge Switch & Red Herring → `45–55%` **Near-Miss (`Tantalus`)** → `65–75%` **False Dawn ➔ Cold Water & Double-Bind** → `80–90%` **3-Wave Climax + Planted Option C (`10/10`)** → `90–100%` **180° Echo Prop** (Finale/Short) or **Cold-Water Cliffhanger** (Ep `1..N-1`).

### 4.5 The 11 Twist Families & Anti-Repetition Rotation (`Zero Formulaic Endings`)
Rotate twist families strictly across episodes (**never repeat the same family within 5 episodes**; **Hidden Sacrifice** is hard-capped at max `1 in 5` and never defaults to a sick/dying relative):

| # | Twist Family | Core Reversal Mechanism |
| :---: | :--- | :--- |
| **1** | **Hidden Sacrifice** *(capped ≤1/5)* | The misjudged person was secretly absorbing the cost for someone else. |
| **2** | **Narrator Was the Cause** | The threat, curse, or mistake traces directly back to `A1`'s own earlier action. |
| **3** | **Role Flip** | `A1`'s "weakness" or special status actually served a totally different purpose. |
| **4** | **Rule Misread** | The world rule works differently in direction, target, or timing than everyone assumed. |
| **5** | **The Rule Was a Lie** | An authority or system fabricated the rule/stakes to control the town. |
| **6** | **Outsider Was Right** | The mocked weirdo's bizarre claim was literally true all along. |
| **7** | **Cost Turns Into Reward** | The feared penalty of the rule flips into the exact gift `A1` needed. |
| **8** | **Cost Lands on Narrator** | After learning the real price, `A1` voluntarily steps in to pay it themselves. |
| **9** | **Time Reveal** | *When* the event happened — or *when* the narrator is telling it — overturns the premise. |
| **10** | **Wrong Target** | The sign, warning, or gift was never aimed at `A1`, but at someone right beside them. |
| **11** | **Mirror** | `A1` discovers they have become the exact person/monster they mocked in Act I. |

### 4.6 Mandatory 4-Point Twist Quality Gate (Before `GATE R2` Approval)
1. **Plant Threshold**: `≥ 2` distinct visual/verbal clues before an episode twist (`≥ 3` across episodes for a Track L Master Secret), with `≤ 2` pointing directly at the mechanism.
2. **Zero Mechanism Leakage**: No line before the twist may state the twist's core mechanism words; the final shot shows the consequence without explaining it aloud.
3. **Character Consistency Test**: The twist reveals *who someone truly was all along* — it never contradicts established behavior without a planted reason.
4. **Blind Guess Test**: Read ONLY the lines before the twist row — if a fresh reader immediately nails BOTH *who* and *why* on guess #1, weaken the most obvious clue or strengthen emotional camouflage before recording `.mp3`.

---

## 5. Master 24-Device Unpredictability Toolkit & Application Playbooks

Use this compact craft reference in **Stage R1 & Stage R2** to select 3–5 complementary devices per film/series (never cram all 24 into one episode).

### 5.1 The 24 Core Devices (5 Functional Groups)

| Group | Devices & Operational Function |
| :--- | :--- |
| **1. Perception & Misdirection** | **1. Unreliable Narrator** *(narrator's naive/biased POV contradicts 3D visuals until revealed — #1 tool for 100% First-Person Narration)* · **2. MacGuffin** *(object everyone chases that exposes character truth)* · **3. Bait-and-Switch / False Protagonist** *(focus shifts from decoy lead to true center)* · **4. Brick Joke / Delayed Payoff** *(tiny early gag/detail returns as a decisive endgame lever)* · **5. Subversion** *(flips genre stereotypes)* |
| **2. Pressure & Retention** | **6. Hitchcock's Bomb Under the Table** *(calm scene + visible hidden danger = pure suspense)* · **7. Ticking Clock** *(visible 3D deadline: 11:59 clock, dying candle, last train)* · **8. Zeigarnik Open Loop** *(open a new question before closing the old one)* · **9. Raising the Stakes** *(each fix escalates the next cost)* · **10. Point of No Return** *(burns the retreat bridge)* |
| **3. Depth & Emotion** | **11. Hamartia** *(`A1`'s own flaw pulls the disaster down — never bad luck)* · **12. Subtext** *(narration says X while 3D eyes/hands prove Y)* · **13. Foil Character** *(parallel character who chose the opposite path)* · **14. Anagnorisis** *(1-second silent realization + `±3f` face snap)* · **15. Ego Death** *(`A1`'s `Lie` shatters completely)* · **16. Catharsis** *(earned emotional release after sustained compression)* |
| **4. Structure & Time** | **17. In Medias Res** *(frame 1 opens mid-crisis)* · **18. The Prestige** *(3–5 rapid montage flashes locking all earlier clues together)* · **19. Bookend** *(opening & closing frame/line mirror each other with 180° inverted meaning)* · **20. Rashomon Effect** *(same event replayed in a later episode from another character's POV)* · **21. Kishōtenketsu** *(4-beat conflict-free perspective flip — `Ki-Shō-Ten-Ketsu`)* |
| **5. 3 Forbidden Traps** | **22. ❌ Deus Ex Machina** *(unplanted miracle/stranger rescue)* · **23. ❌ Idiot Plot** *(conflict survives only because nobody says one cost-free sentence)* · **24. ❌ Info Dump** *(long static narration explaining rules/backstory with zero visual action)* |

### 5.2 6 Practical Roblox 3D Application Playbooks (`When to Use Which Combo`)

| Scenario / Goal | Best Track | Winning Device Combo | Concrete 3D Roblox Execution (`100% Narration`) |
| :--- | :---: | :--- | :--- |
| **Case 1: Creepy World-Rule / Survival Town** | `Track S` or `Track L` | `In Medias Res` + `Ticking Clock` + `Hitchcock's Bomb` + `Unreliable Narrator` + `Bookend` | Open at `11:58 PM` as the town clock ticks; narrator insists the red light means safety while background shadows gather outside the cabin window; final frame returns to the clock at `11:58` with the rule inverted. |
| **Case 2: Family / Generational Secret Drama** | `Track S` or `Track L` | `Hamartia` + `Subtext` + `4-Stage Cold Water (Double-Bind & Noble Lie)` + `Anagnorisis` + `Catharsis` | `A1`'s pride misreads Grandpa's cold rejection (*False Dawn → Cold Water Slap*); camera lingers on Grandpa's shaking hand hiding the broken watch behind his back (*Subtext / Noble Lie*); `1.0s` snow-wind silence + `±3f` face snap when truth clicks. |
| **Case 3: Mystery / Whodunit Onion-Peel** | `Track L` (`5–10 eps`) | `MacGuffin` + `Red Herring` + `Near-Miss (Tantalus)` + `Rashomon Effect` + `The Prestige` | Everyone hunts a locked brass box (*MacGuffin*); Ep 3 nearly opens it before `A2` intercepts (*Tantalus Near-Miss*); Ep 4 replays Ep 1's alley scene from the silent witness's angle (*Rashomon*); Finale flashes 4 planted visual clues (*The Prestige*). |
| **Case 4: School / Underdog / Ironic Quirk** | `Track S` or `Track L` | `Foil Character` + `Brick Joke / Delayed Payoff` + `Subversion` + `Option C` + `Ego Death` | A "useless" quirk mocked in a comic Beat-1 gag (*Brick Joke*) is contrasted against a popular rival (*Foil*), then wins the climax via an overlooked physical loophole (*Option C*) after `A1` stops trying to imitate the rival (*Ego Death*). |
| **Case 5: Multi-Episode Binge Transition (`Ep N → N+1`)** | `Track L` (`Ep 1..N-1`) | `Point of No Return` + `Raising the Stakes` + `Zeigarnik Open Loop` + `Cold Water Cliffhanger` | Mid-episode `A1` breaks a town taboo (*Point of No Return*), escapes safely (*False Dawn*), then in the final `3s` spots the exact warning mark now glowing on their little sister's coat (*Zeigarnik Open Loop + Cold Water*) → instant black cut. |
| **Case 6: Cozy / Healing / Quiet Twist** | `Track S` (`65–120s`) | `Kishōtenketsu` + `Subtext` + `Bookend` + `Quiet Catharsis` | Zero villain, zero combat: warm daily winter routine (`Ki-Shō`), an unexpected quiet observation (`Ten`) reframes why Grandma walks to the frozen pond every morning (`Ketsu`), closing on the exact opening wide shot now bathed in warm sunrise light (*Bookend*). |

---

## 6. Genre Playbooks → First-Person Narration

Mount the genre module (`engine/genres/<genre>.md`, Genre Card + Mastery Playbook P1–P7) at `GATE R1`, then translate its signature scene into narration:

| Genre | How the narrator carries it | Watch out |
|---|---|---|
| Family drama | the narrator misreads a relative; the camera shows the hidden care (subtext divergence) | no confession speech; the truth arrives through an object |
| Microdrama | the narrator is underestimated; every episode ends on one visible status reversal | the narrator never boasts; others' faces carry the payoff |
| Sitcom | the narrator's own lie snowballs; deadpan narration over visual chaos | one lie, three escalations, reset at the end |
| Thriller / mystery | **unreliable narrator**: clues shown, narrator draws the wrong conclusion | every clue visible before the reveal (fair play) |
| Action | narration stops during the action beat; short lines before and after | no play-by-play of moves; sound effects carry the fight |
| Healing | slow, warm narration with long visual holds and ambient sound | one small inner change, no lesson spoken |
| Horror | sound-first lines ("I heard the stairs before I saw them"), short sentences, silence before the shock | never describe the entity fully; no gore |
| Romance | the narrator hides the feeling; actions betray it (the umbrella tilted, the message deleted) | the word "love" only when it costs |
| Fantasy | the narrator states the world rule as normal life; the price shows on screen | the rule shown before it matters |
| Sci-fi | the narrator uses the technology casually; the cost appears in an insert | no jargon; one premise per story |

---

## 7. Young-Audience Safety (Roblox Default)

Roblox viewers are often children, so the project's `fatality_policy` for Roblox is always **none or off-screen** and the following are Hard Constraints for every genre:
- zero gore, blood or injury detail; deaths and serious harm only happen off screen and are shown through consequence (an empty chair, a returned object);
- adult threats are uncanny, never predatory; no kidnapping-by-adult framing, no threats aimed at a child's body;
- no swearing, no self-harm, no substance use, no romance involving under-18 characters beyond innocent glances;
- horror stays "spooky", not traumatic: suggestion, sound and shadow;
- the Minor Protection Protocol (`workflow.md` §2.7) applies to every under-18 character.

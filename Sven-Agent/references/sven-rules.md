# SVEN RULES — Summary of prompt-sven.txt v3 (Omni Flash Prompt System + Dialogue Architecture)

> Original full file: `d:\Project\Short-karma\prompt-sven.txt`
> This is a **SUMMARY** for fast agent lookup. When detailed rules are needed, READ THE ORIGINAL FILE.
> **v3**: Integrates full Dialogue Architecture (§D) — cinematic dialogue following Show Don't Tell principles.

---

## § FOUNDATIONAL PRINCIPLES

**3 parties:** User ↔ Agent (Vietnamese, free internal labels) | Agent ↔ Omni Flash (specific images only)

**Omni Flash**: stateless — each Scene is an independent call, it **does NOT remember** previous Scenes, does not understand `[Final State]`, `Scene 2`, `as established`, or "continuing from".

**THE SINGLE TEST** (apply to every sentence before including in output):
> *"A person who knows nothing about the script, hasn't read the previous Scene, only reads this one sentence — can they accurately visualize the exact frame?"*

If **NO** (contains Scene/Shot numbers, "as established", "as seen before", negative sentences like "does not appear") → **rewrite** as observable physical detail.

**Content zones:**
| Zone | Audience | Labels |
|---|---|---|
| Internal: `[Final State]`, Beat Breakdown, Checklist | Agent only | Free |
| Actual output: `[Subject]`, `[Prop Profile]`, `[Context]`, Shots | Omni Flash | **ABSOLUTELY NO reference labels** |

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

**Full style library (39 styles):** see `workflow.md § 1A — VISUAL STYLE LIBRARY`



## § [0] DIRECTOR'S INTENTION LOCK — Run BEFORE Beat Breakdown, internal only

For **each Scene**, before writing the Shot breakdown, determine:

1. **ONE dramatic function**: What is this scene DOING for the story? (who just lost control / just gained it, where power shifts, what lies beneath)
2. **ONE directorial tone**: `cold-observational-from-distance` | `suffocating-close` | `chaotic-disoriented` | `still-waiting`
3. This tone governs camera / lighting / body-state / sound — **held throughout the entire Scene** (unless the Scene is TWIST — allowed to shift tone exactly once at the climax shot)
4. **If the Scene has dialogue**: Also determine — does this dialogue REVEAL or HIDE emotion? What is the character saying while their body betrays the opposite? (Subtext > Explicit)
5. **DO NOT output to Omni Flash** — internal filter only

**Quick test:** *"If I strip the technical labels, what does this Scene make the audience feel? Do all camera/lighting/dialogue choices pull in the same direction?"*

---

## § ONE-MOVE RULE

Each Shot carries **exactly ONE camera intention**: one movement, one speed, one relationship to the subject. Do not stack multiple movements in one short 2-3s Shot.

---

## § [3] CHARACTERS & PROPS

### Naming Convention (§3.0)
- Character names in Code Block 1: **1-syllable English proper noun, no vocabulary meaning, no Vietnamese diacritics** (`Lok`, `Vin`, `Ren`, `Keth`, `Tor`, `Mael`, `Ryn`)
- Vietnamese name → create internal **Name Mapping Table** at Stages 1 & 2, use throughout, NEVER output to Omni Flash
- Spiritual characters: keep original title (Quan Am, Dia Tang Vuong) + full appearance description
- Strictly forbidden: names ≥ 2 syllables (`Helen`, `Elena`), names with English meaning (`Grace`, `Hope`), latinized Vietnamese (`Tran`, `Lien`)


### [Subject] — §3.2

**MODE A — No reference image (full description):**
- Continuous paragraph ~120 words per character A/B
- Order: Name → Age → Gender → Height → Head-body ratio → Skin → Build → Hair → Facial features → Clothing & original props
- **Facial features**: observable behaviors (micro-expression), NOT abstract
- Line C: ~30-40 words

**MODE B — Reference image exists from Step 1 Pre-Production (image-anchored):**
- Only needed: **1-syllable code name** + **physical anchor traits** (height, build) + **current state** + `[Character Reference attached]`
- Remove all face, hair, costume descriptions — reference image already locks those
- Line C: name + role + `[Reference attached]`

```
[MODE B — Character format with reference image]
 
Initial pose: {camera-anchored pose}.
```

### [Prop Profile] — §3.4

**MASTER 4:3 FOUR-VIEW PROP DESIGN SHEET PROMPT STRUCTURE (Step 1C):**
```
Style: [Visual Style Name — e.g. mature western animation / Theatrical film reference, live-action style, DaVinci grading...].

Name: [Prop Name]. Category: [Weapon / Relic / Tool / Artifact / Document / Symbolic Object]. Description: [A cross-shaped blade forged in aged silver with a cool metallic patina. The ornate handguard is intricately carved with ancient runes and vampire-hunting inscriptions. The handle is wrapped in dark leather and engraved with a vampire hunter emblem. Stored in a waist leather sheath. The blade emits a sharp, cold glint under porch night light. Upon piercing a vampire, it reduces the target to fine ash — a symbol of faith-driven ultimate judgment].

Format: Prop design sheet, 4:3 landscape. Show only four views of the same prop: one main view that best presents its visual features, plus front, side, and back views. The main view must be the largest and clearest; the three orthographic views must fully show the prop shape and structure. Pure white background.

Rules: Do not include any text, letters, numbers, annotations, captions, material swatches, dimension lines, arrows, close-up detail panels, or exploded views. The prop must remain completely consistent across all views. No environmental elements, no characters, no watermark.
```

**MODE A — No reference image (full description in clip):**
- Layer 1: short identifying name (Bamboo Basket, Ledger, Bowl...)
- Layer 2: material → shape/size → color/texture → weight/how held → **CURRENT state at opening frame of this Scene**
- Add `"the only [name] in frame"` to prevent duplication

**MODE B — Reference image exists from Step 1C (image-anchored — DEFAULT):**
- Only needed: **Prop name** + `[Prop Reference attached]` + **CURRENT state** (drawn / sheathed / broken / held / resting) + camera-anchored position + `"the only [prop] in frame"`.
- Remove material, color, shape description — reference image already locks those.

```
[MODE B — Prop format with reference image]
The Silver Cross Dagger [Prop Reference attached], currently sheathed in waist leather scabbard — the only dagger in frame.
```

### [Environment / Context] — §3.6

**MASTER LOCATION / ENVIRONMENT REFERENCE PROMPT STRUCTURE (Step 1D):**
```
Style: [Visual Style Name — e.g. Pixar\Disney 3D animation style / Theatrical film reference, live-action style, DaVinci grading...].

Name: [Location Name]. Description: [A broad, detailed multi-sensory environmental description: architectural structure, exterior/interior materials, structural frame, wall coverings, smoldering light sources casting deep shadows and colored illumination, crude totems or functional artifacts hanging from overhead, floor textures, weather elements, light bleed through entrances, and overall emotional atmosphere and ritualistic/cinematic tone].

Format: Location concept design sheet, 16:9 landscape, multi-angle layout. At least 4 panels showing the same location from different camera angles or directions: wide establishing shot, reverse angle, overhead/bird-eye view, and low-angle or detail close-up. Panels may vary lighting or time of day if needed by the story. Focus entirely on full location views, with no written descriptions, detail labels, or floor plans.

Rules: No characters or people - environment only. The location must look consistent and recognizable across all panels, with the same buildings, props, and layout. Do not include any text, letters, numbers, annotations, captions, dimension lines, arrows, labels, legends, zoning notes, or watermarks.
```

**MODE A — No reference image (full description in clip):**
- Full description of architecture, floor surface, colors, light source, atmosphere (~50-70 words).

**MODE B — Reference image exists from Step 1D (image-anchored — DEFAULT):**
- Only needed: **Location name** + `[Environment Reference attached]` + **time of day phrase** + **key light source & color temperature (5600K / 2700K)** (1 line only).
- Remove all architectural and material descriptions — reference image already locks the environment.

```
[MODE B — Setting format with reference image]
The Obsidian Blacksmith Forge [Environment Reference attached], twilight before storm — key light from roaring forge hearth casting 2700K amber glow across wet stone floor.
```

### Anti-Duplication — §3.5
- **§3.5b** (Wide/Full shot): add `"the only [two] figures in the [empty] space"` when few people
- **§3.5e** (Prop): add `"the only [prop] in frame"`

> **Mode selection rule:** If Step 1 Pre-Production is complete and reference images have been created → **MANDATORY use Mode B** to avoid conflict between text description and image. If no image → use Mode A.

---

## § [4] CONTINUITY — FINAL STATE

**Final State Gate (§4):** Before writing `[Subject]`/`[Prop Profile]` of a new Scene, read `[Final State]` of the previous Scene — redraw inherited state using **specific physical detail**, no references.

**Handoff Frame (§4):** Next Shot opens EXACTLY at the moment the previous Shot ended — physical continuity.

**Single Action Rule (§4):** 1 Shot = 1 primary action, do not chain 2 independent beats with "then/after that" in the same Shot.

**Intra-Scene State Table (§4b):** Track prop state changes across Shots within the same Scene.

---

## 🛡️ 4-STEP ENTITY LOCK METHOD

1. **Step 1: Single Anchor Dictionary**: Lock 1 unique identifier phrase for Setting (`mossy stone floor`), Camera angle (`Shot Medium-Close-up`), Prop (`Wooden Bowl`), and Sound. Use word-for-word 100% from start to end of prompt, FORBIDDEN to swap synonyms.
2. **Step 2: Behavioral Handoff Bridge**: Every coordinate/prop state transition must be described through 3 anchors: *Initial position ➔ Reach/bend/pick-up behavior ➔ New position*. FORBIDDEN: position teleportation artifact.
3. **Step 3: Single Camera Continuum**: 1 Clip of 10s MUST hold EXACTLY 1 fixed camera angle and unbroken continuous setting from 00:00 to 00:10 (Beats 1, 2, 3 share the same camera parameters). FORBIDDEN: changing camera angle or cutting background within a 10s clip, to eliminate the Background Morphing Artifact.
4. **Step 4: Entity State Audit**: Run entity test checking 3 points (unified setting keyword, direct prop pickup bridge, dialogue & acoustic sync) before outputting code block.

---

📌 **DYNAMIC DURATION & KINETIC ACTION PROTOCOL**
- **Total duration PER SCENE**: MUST be **EXACTLY 10 SECONDS (10s)** for 100% of Scenes (including Scene 1 Hook).
- **Elastic Beat Division**: AI Agent has FULL CREATIVE FREEDOM to divide the 10s Scene into **2 to 4 Beats** (Shots) flexibly following the dramatic rhythm of the story (e.g., `4s-3s-3s`, `3s-4s-3s`, `2s-3s-3s-2s`, or `5s-5s`), as long as **TOTAL = EXACTLY 10s**.

| Beat Length | Biomechanical Action Budget | Flexible Application Example |
|---|---|---|
| **Beat 2s** | 1 short explosive movement / startle causal reaction | Jerk away, slap the table, step back 1 step. |
| **Beat 3s – 4s** | 2–3 causally linked sequential movement phases | Walk 3 steps + lower foot + raise scroll up. |
| **Beat 5s (Kinetic Glide)** | Extended smooth sustained movement + continuous camera tracking | Camera pulls back 2m parallel to a 5-step stride. |

**Per-Second Action and Scene Closing Rules:**
- **1-Second Budget**: AI renders maximum 1 micro-movement or 1 acceleration increment. FORBIDDEN to cram 2 independent large actions into 1 second.
- **Terminal Deceleration Hold**: The final Beat of any Scene (whether ending at 07-10s or 08-10s) **MANDATORY LAST 0.5s [09.5s - 10s]** decelerates velocity to 0 (`zero-velocity freeze hold`), locking into completely static pose (only static or smooth push-in — **FORBIDDEN** crane/orbit/arc jerks).
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
| **Dawn** (6–8h) | `dawn golden hour, low sun just above horizon` | Warm golden-orange 2200–3000K, long shadows | Low-angle raking sunlight from east |
| **Morning** (8–11h) | `mid-morning, clear daylight` | Neutral warm white 4500–5500K | Overhead sunlight at 30–45° angle |
| **Noon** (11h–13h) | `midday harsh sunlight, overhead sun` | Hard white 6000–6500K, minimal shadows | Vertical overhead sun, strong shadows beneath |
| **Afternoon** (13–16h) | `afternoon light, soft directional sun` | Warm white 4500K, long fill shadows | Angled sunlight from south-west |
| **Golden hour** (16–18h) | `golden hour, low warm sun before sunset` | Deep amber-gold 2000–2500K, long raking shadows | Low-angle side/back light from west |
| **Dusk** (18–19h) | `sunset, sun at horizon, warm dusk glow` | Orange-red 1800–2200K, silhouette potential | Sun at or below horizon, skyline glow |
| **Blue hour** (19–20h) | `blue hour dusk, post-sunset twilight` | Deep blue-purple sky, warm artificial light contrast | No direct sun, ambient sky + practical lights |
| **Night** (20–23h) | `nighttime, artificial light only` | Warm tungsten 2700–3000K interior / cool moonblue exterior | Practical lamps, candles, streetlights |
| **Late night** (23h–3h) | `late night, deep darkness` | Near-black with isolated warm pools of light | Candle / single lamp / moonlight only |

**How to embed in Code Block 1:**

```
Child's bedroom interior, nighttime — bedside table lamp (practical, frame-right) casts...
              ↑ time declared immediately after setting name, before the em dash —
```

**Full example for each time of day:**

```
Bamboo forest path exterior, dawn golden hour, low sun just above the eastern ridge —
open sky casting warm 2400K amber raking light from east-right at 10° angle...

Stone courtyard interior, midday harsh sunlight, overhead sun —
vertical sunlight entering through open roof, hard white 6200K, deep shadow pools directly beneath pillars...

Village road exterior, golden hour, low warm sun before sunset —
warm 2100K amber sidelight from frame-right at 15° angle, long stretched shadows pointing left...

Bedroom interior, nighttime, artificial light only —
bedside table lamp (practical, frame-right, bed-height) casts warm 2800K amber pool across the bed...
```

---



## § [1.F] BODY-STATE COMPATIBILITY CHECK

Before finalizing `[Subject]`, check:
- **Hands**: if character holds/handles a prop in any Shot → DO NOT lock both hands in a base pose (arms crossed, hands in pockets...) → use neutral upper-body description
- **Mouth**: do not stack 2 activities (chewing + talking, drinking + talking)
- **Legs**: base pose must not conflict with leg action in any Shot
- **Head/eyes**: do not describe 2 gaze directions simultaneously without a transition
- Always explicitly state **LEFT HAND or RIGHT HAND** when holding/handling a prop (e.g.: `held in Dax's right hand with Dax's right thumb pressed along the upper edge`). If prop is not being held, MANDATORY state `resting on the floor beside Vin's right foot — ZERO hand contact — the only [prop] in frame`.

### 📌 SHOT HEADER STRUCTURE & PURE CINEMATIC ACTION PROSE (△ BEAT OPTICAL LOCKDOWN)
1. **Master Optical Lockdown per Beat `△`:**
   $$\mathbf{\bigtriangleup\ [Timestamp]\ Shot\ [Shot\ Scale]\ |\ [Focal\ Length\ +\ Camera\ Angle]\ |\ [Trajectory\ \&\ Focus\ Target]}$$
   Every beat MUST declare the 3 optical components clearly.
2. **Eliminate All Filler Connector Words THAT STIFFEN THE PROMPT**: ABSOLUTELY FORBIDDEN awkward connectors like `Driven by the stillness...`, `As Dax halts...`, `Continuing the reach...`. A 10s Scene is a continuous visual flow — describe **DIRECTLY THE OBSERVABLE PHYSICAL ACTION**.
3. **Standard Description Across Timeline (Continuous Co-Presence & Dual-Action):**
   - `△ [00:00-00:03] Shot [Scale] | [Lens + Angle] | [Camera Trajectory]:`
     Across the space, Subject A at frame-right executes micro-action <--> Subject B at frame-left maintains defensive posture, unblinking glare.
   - `△ [00:03-00:07] Shot [Scale] | [Lens] | [Continuing Trajectory / Kinetic Tracking]:`
     Subject A heavy kinetic action / sliding prop <--> Subject B reactive block / clamping hand on prop as surface scratches.
   - `△ [00:07-00:10] Shot [Scale] | [Lens] | [Static Lock]:`
     Both subjects lean in suffocating face-to-face standoff + 0.5s zero-velocity freeze hold.

* **✅ CORRECT (Natural, decisive, proper camera & lens, continuous co-presence):**
  `△ [00:00–00:03] Shot Medium Two-Shot | 50mm f/1.4 | Slow forward push-in along table plane:`
  `Dax at frame-right steps forward on the wet granite floor, extending his right hand holding the Debt Scroll toward Vin; directly opposite at frame-left, Vin stands rigid in unblinking defiance.`

  `△ [00:03–00:07] Shot Medium Close-Up | 50mm f/1.4 | Lateral tracking reframe:`
  `Dax forcefully thrusts the Debt Scroll downward, gouging a white scratch across the stone; Vin clamps his palm down over the parchment as it strikes his cuffs.`

  `△ [00:07–00:10] Shot Choker Standoff | 85mm f/1.4 | Static lock with 0.5s freeze hold:`
  `Both men lean inches apart in suffocating face-to-face deadlock — holding the physical standoff frozen for the final 0.5 seconds.`

* **❌ WRONG (Uses awkward connectors, missing camera specs):**
  `Driven by the stillness...` / `As Dax halts...` (redundant, stiff, hazes the prompt).

---

## § [D] DIALOGUE ARCHITECTURE — Cinematic Dialogue Architecture (v3 Integrated)

> Apply when a Scene has dialogue. Dialogue is not an explanation tool — dialogue is a **psychological weapon** and the **physical surface of emotion**.

> [!CAUTION]
> **PRE-FLIGHT BEFORE WRITING ANY DIALOGUE — CHECK THESE 3 FIELDS FROM CHARACTER PROFILE (workflow.md § 1B):**
> 1. **RELATIONSHIP TYPE** — what is the real-world bond between A and B?
> 2. **POWER DYNAMIC** — who holds power at THIS specific Beat? Has the shift happened yet?
> 3. **ADDRESS FORMS** — how does A call B and B call A RIGHT NOW at this Beat?
>
> **Write the address form into the dialogue bracket FIRST, then build the line around it.**
> The wrong address form (or a missing one) breaks the entire subtext layer.
> A character suddenly calling their master by first name — without ADDRESS FORMS shift declared at this Beat — is a continuity error, not a power moment.
> Reference: `story-rules.md § Relationship Dynamic` | `workflow.md § 1B — ADDRESS FORMS template`

### 🔑 §D.0 FOUNDATIONAL PHILOSOPHY — SHOW DON'T TELL THROUGH DIALOGUE

Great cinematic dialogue **NEVER** states emotion directly. Dialogue is just the **surface layer** — what lies beneath is what the audience actually feels:

| AVOID (Stating directly) | USE (Subtext through physics + indirect dialogue) |
|---|---|
| "I hate you!" | A dialogue about a neutral topic but the voice tightens, hand squeezes the held object |
| "I'm afraid to die." | "The candle is still burning..." — voice slightly trembling, eyes on the flame not on the other person |
| "You betrayed me." | "I remember you liked sweet tea." — flat voice, not looking at their face, hand pushing the teacup across |
| "I love you." | Silence + hand lightly touching a keepsake + looking away |

**Golden rule**: If you delete the dialogue and the scene is still understandable → the dialogue is redundant. If you keep the dialogue but delete the physical action the scene loses depth → dialogue + mechanics MUST resonate, not duplicate.

---

### 🎭 §D.0b 4 DYNAMIC NARRATIVE CASTING MODELS

Who speaks in a scene is governed by **dramatic tension and narrative context**, not an artificial rule forcing the protagonist to speak in every clip:

1. **The Silent Titan (Nhân vật chính im lặng như pho tượng)**:
   - The protagonist performs monumental physical actions (unblinking stare, unsheathing blade, leaning into light); two terrified witnesses in the background whisper legends about their ruthless past.
2. **The Oppressive Monologue (Kẻ phản diện độc thoại áp bức)**:
   - The dominant antagonist delivers a cold, measured ultimatum; the bound or cornered victim remains unyielding and silent, speaking only through jaw tension and defiant glare.
3. **Sub-stakeholder Plotting (Nhân vật phụ toan tính mưu đồ)**:
   - Two conspirators, sentries, or lieutenants whisper a scheme in the shadows, revealing exposition and looming peril through dialogue while main characters move in the background.
4. **The Rivalry Clash (Đối đầu 1-1 sinh tử)**:
   - Two direct rivals collide head-on, trading lethal truths and ultimatums across a table or battlefield.

---

### 🎙️ §D.0c 4 MASTER DIALOGUE DELIVERY METHODS & 7 GENERAL APPLICATION USE CASES

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             4 MASTER DIALOGUE DELIVERY METHODS (10s TAKE)                          │
├────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. SINGLE-SPEAKER MASTER LINE (~140–160 chars) : 1 character delivers a complete 3-layer statement.│
│ 2. OFF-SCREEN THREAT / VOICEOVER (~140–160 chars): Voice echoes into a sealed room from darkness.  │
│ 3. GREEK CHORUS / MOB WITNESS (~140–160 chars)  : 1 foreground representative delivers mob bias.   │
│ 4. ACTION-INTERROGATIVE SYNERGY (~140–160 chars): Spoken truth delivered at the static pause point. │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### The 7 General Application Use Cases:
1. **Oppressive Interrogation / Debt Extraction**: Use Method 1 (Single-Speaker Master Line $\sim 140–160$ chars: Contextual Bite $\to$ Moral Trap $\to$ Death Warrant).
2. **Ideological Confrontation / Tabletop Sparring**: Use Method 1 (Single-Speaker Master Line $\sim 140–160$ chars: False Worldview Exposed $\to$ Unspoken Truth $\to$ Lethal Retort).
3. **Stealth / Enclosed Space Dread**: Use Method 2 (Off-Screen Threat $\sim 140–160$ chars: Approaching Footsteps $\to$ Cold Countdown $\to$ Unescapable Trap).
4. **Public Accusation / Mob Isolation**: Use Method 3 (Greek Chorus $\sim 140–160$ chars: Superficial Observation $\to$ Mob Prejudice $\to$ Public Condemnation).
5. **Mortal Combat Standoff**: Use Method 4 (Action-Interrogative Synergy $\sim 140–160$ chars: Blade Lock $\to$ Unmasking Cowardice $\to$ Decisive Blow).
6. **All Hope Is Lost / Ego Death (Beat 4.3)**: Use Method 1 (Single-Speaker Master Line $\sim 135–155$ chars: Shattered Defenses $\to$ Root Guilt Unveiled $\to$ Weeping Surrender).
7. **Karmic Release & Closing Maxim (Beats 5 & 6)**: Use Method 1 (Single-Speaker Master Line $\sim 135–155$ chars: Generational Curse Broken $\to$ Grace Granted $\to$ Universal Eternal Law).

---

### 🚨 §D.1 MAXIMUM DIALOGUE DENSITY & HARD-CAP 160 CHARACTERS / 10s CLIP

In every 10-second AI Video Clip, dialogue MUST strive to maximize narrative richness and vividness, targeting the **Optimal Sweet Spot of ~140–160 English characters (~20–25 words / 3.5–4.0s of continuous speech)**.

> [!IMPORTANT]
> **MAXIMUM DRAMATIC DENSITY & ANTI-FRAGMENTATION MANDATE**:
> - **BAN ON SHORT / MEANINGLESS LINES**: Strictly FORBIDDEN to write overly brief, shallow, or fragmented dialogue (e.g., "Ten years", "Yes", "No", "Stop it", < 50 chars). Choppy monosyllabic lines kill dramatic tension and waste the 10-second storytelling capacity.
> - **The 140–160 Character Master Line Architecture**: Every dialogue line must be a complete, multi-layered dramatic statement composed of 3 structural beats:
>   $$\mathbf{Line\ Architecture} = \mathbf{[Contextual\ Bite\ /\ Premise]} + \mathbf{[Ideological\ Contrast]} + \mathbf{[Devastating\ Ultimatum\ /\ Consequence]}$$
> - **Maximum Vividness**: Investing the full ~140–160 character budget delivers profound world-building, philosophical resonance, and unforgettable psychological weight in every single clip.
> - **Hard-Cap Ceiling**: Total dialogue MUST NOT exceed 160 English characters (including spaces and punctuation) to protect lip-sync from facial warping and preserve the 0.5s terminal freeze hold.

---

### 🎯 §D.2 LOGICAL CAUSALITY CHAIN — KEYWORD HANDOFF

ABSOLUTELY FORBIDDEN to write disconnected dialogue lines. Every dialogue turn MUST follow the **Logical Causality Chain — Keyword Handoff**:

* **Principle**: Each subsequent dialogue line MUST pick up **1 main Keyword** or **1 Action** from the previous line to psychologically choke or redirect the other person.

**Example of 3-turn causal chain:**
- A: `"Ten years."` (low voice, no explanation)
- B: `"Ten years... and you come back for THIS?"` (picks up "ten years", redirects to intent)
- A: `"I came back for YOU."` (picks up "come back", completely flips the subtext)

**5 types of psychological redirection:**
| Type | Mechanism | Effect |
|---|---|---|
| **Choke** | Repeat the keyword but drop the voice | Suffocates the atmosphere |
| **Flip** | Use the same keyword but completely opposite meaning | Mild psychological shock |
| **Expand** | Pull the keyword into a larger consequence | Escalates tension |
| **Cut** | Don't respond directly, switch to another topic | Unease, disorientation |
| **Counter-question** | Turn the other person's line into a reverse question | Power shifts |

---

### 🔥 §D.3 MANDATORY SEASONING — SUBTEXT + PHYSICAL MECHANICS

Cinematic dialogue **NEVER stands still**. Every line of dialogue MUST be seasoned with 2 ingredients:

1. **❤️ Internal Subtext**: Declare the true emotion hidden beneath the spoken line — what the character is FEELING but NOT SAYING.
2. **💥 Physical Micro-Biomechanics**: Translate that entire subtext into observable mechanics — MUST differ from the surface meaning of the dialogue to create depth:
   - Neck vein rising though the voice is gentle
   - Fist clenching white-knuckled though the mouth is smiling
   - Pupils dilating though the eyes are looking down
   - Eyes narrowing mockingly though the line is a compliment

**Subtext-to-Physics Table (cinematic dialogue):**

| True Subtext | Surface Dialogue | Accompanying Mechanics |
|---|---|---|
| Arrogant contempt | "You don't need to do that." | Voice gentle as if explaining to a child, eyes looking past the other person's shoulder |
| Ruthless without mercy | "I understand." | Voice completely flat, hands folding papers slowly and deliberately |
| Quietly desperate | "It's fine." | Breath inhaled through nose too deeply, jaw muscles tightening subtly |
| Fear disguised as aggression | "What are you going to do to me?" | Voice louder than usual, a small unnoticed step backward |
| Rage about to erupt | "You owe me a life!" | Fist driving straight down onto stone floor, dust erupting, neck vein visibly raised |
| Cold contempt | "Come take it then!" | Axe swung from shoulder into guard stance, lips curling into a cold mocking smile |

---

### 📌 §D.4 4-IN-1 PARENTHETICAL DIALOGUE DIRECTING SYNTAX

Every dialogue line in Screenplays and Code Block 1 MUST apply the **4-in-1 Hollywood Directing Parenthetical** — **100% English, Zero Redundant Meta-Tags** (no `Spoken dialogue:`, no `[Subject 1]`):

$$\mathbf{Character\ Name：" Spoken\ Line\ "\ （\ 1.\ Vocal\ Timbre\ \&\ Breath\ Power\ ,\ 2.\ Somatic\ Action\ ,\ 3.\ Lighting\ on\ Anatomy\ ,\ 4.\ Psychological\ Subtext\ ）}$$

**Standard canonical examples:**
- `Commander Ethan Ross："The legion burned. I survived."（voice dropping to a cold razor-sharp rasp, rising at frame-left ground level, unblinking dark eyes catching the dying amber brazier light — no hesitation, only hunger）`
- `Dax："Ten years... how much do you owe me?"（voice low and arrogant, eyes narrowing into a cold sneer, lips parting dynamically in precise lip-sync, right hand thrusting the Debt Scroll downward catching 2700K sidelight）`
- `Vin："Of course."（voice flat and unhurried, lips parting in minimal precise lip-sync, left hand folding the document closed with deliberate slowness — not looking at Dax）`

**⚠️ Camera FORBIDDEN when dialogue is present:** `Crane`, `Orbit`, `Arc`, `Whip pan`, `Strong Handheld` — only use `Static`, `Slow Push-in`, `Slow Pull-out` to protect lip-sync.

---

### 🎥 §D.5 CAMERA-SPEAKER BINDING PRINCIPLE (Lens Must Follow the Speaker)

Camera lens direction when dialogue is present MUST follow 4 rules:

#### 🔴 Rule 1 (Mandatory Default): SOMEONE SPEAKS — CAMERA CUTS TO THAT PERSON
- Any character who speaks (fighter, victim, or **crowd spectator**) → Camera MUST `focus locked on [Speaker Name]`, clearly describing face and lip-syncing expression (`lips parting dynamically in precise lip-sync`).
- **Spectator speaks**: Shot MUST face the spectator directly as they stand/lean forward over the stone balcony to speak.

#### 🔵 Rule 2 (Only for Internal Scenes): OFF-SCREEN VOICEOVER
- **ONLY FOR INTERIOR SCENES** (character is hiding, threatening voice echoing from outside).
- **ABSOLUTELY FORBIDDEN** in arena or open-environment scenes.
- Mechanism: Character A in room keeps mouth firmly closed (`lips remain closed`), eyes wide with fear.

#### 👥 Rule 3: SPECTATORS — PSYCHOLOGICAL REPRESENTATIVE OF THE CROWD
- Spectators in cinema are NEVER neutral — they represent **Mob Bias** (siding with power, mocking the vulnerable).
- **A crowd of thousands but only 1 spectator speaks**: Identify 1 representative in the foreground, shot facing that person directly.
- Example: `Vane : "Look at the fool! Kneel and beg for mercy!"` (voice loud and mocking, Vane leaning forward over the stone balcony rail, lips parting dynamically in precise lip-sync, background crowd figures cheering behind Vane)

#### 📱 Rule 4: SELFIE VLOG — CONTINUOUS FACE ANCHOR
- **ABSOLUTELY FORBIDDEN**: Character's face must NOT leave the frame, must NOT turn back and walk away from camera.
- Camera moves synchronously with character (`selfie camera arm locked continuously in right hand, walking forward with background moving behind`).
- Final beat: Character steps forward while looking into camera smiling — face anchored 100% at center of frame.

---

### 🚨 §D.6 100% ENGLISH DIALOGUE IN CODE BLOCK 1

To eliminate 100% of AI Video Model errors (Omni Flash, Kling, Veo, Sora) causing language token confusion, audio distortion, or auto-rendering Vietnamese subtitles on screen:

- **Code Block 1 (Omni Flash Prompt)**: **100% DIALOGUE IN ENGLISH**.
- **Code Block 2 (Internal) & Stage 1 Script**: Keep the **VIETNAMESE** translation for User & Voice actors to read.

---

### 🗣️ §D.7 DUAL DIALOGUE OUTPUT — Dual Output Format

All dialogue MUST be output in **2 formats**:

#### Format A — Code Block 1 (Send to Omni Flash):
```text
[Subject English Name] : "[English Dialogue Line ≤ 160 chars]" (voice tone, lips parting in precise lip-sync, physical micro-biomechanics)
```
- Start of prompt: `Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Hyper-realistic, ultra-high-definition masterwork. Cinematic 9:16 vertical...`
- End of prompt: `Do not generate subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video.`

#### Format B — Code Block 2 Internal (Dialogue Script Table):
```text
🗣️ CINEMATIC DIALOGUE SCRIPT TABLE (EMOTIONAL & PHYSICAL DIALOGUE MANIFEST):
- Scene [N] [{timestamp}] | Character: [Vietnamese Name] ([English Name]) | Type: [Direct / V.O / Monologue / Subtext / Burst]
  💬 Vietnamese translation: "[Vietnamese dialogue line]"
  🔤 English AI Prompt: "[English Dialogue Line in Code Block 1]"
  ❤️ Internal subtext: [What the character is NOT SAYING but feeling]
  💥 Physical mechanics: [Body micro-mechanics — must CONTRAST or ROOT FROM subtext, not duplicate the dialogue]
```

---

## § [2b] SVEN SCENE MATRIX (DEFAULT 7 SCENES / SCALE 2 — DYNAMIC % ALLOCATION WHEN N > 7)

- **System default**: **7 Scenes (Scale 2: 70s)**: Scene 1 (Hook), Scenes 2-3 (Setup A/B), Scenes 4-5 (Escalation A/B), Scene 6 (Twist), Scene 7 (Karma & Aftermath).
- **% allocation rule when N > 7 Scenes**: When script expands beyond 7 scenes, scene count MUST be redistributed by Duration Percentage:

| Dramatic Stage | Duration % | Allocation Rule when N > 7 Scenes | Example N = 10 Scenes | Example N = 14 Scenes |
|---|---|---|---|---|
| **1. HOOK** | **~10%** | Always keep exactly **1 Scene 10s** — Hook technique selected dynamically from 12-Hook Library per story features | Scene 1 (10s) | Scene 1 (10s) |
| **2. SETUP / PLOT** | **25 – 30%** | Open Visual Anchor from Hook, plant symbolic prop, establish setting & conflict seed | Scenes 2, 3, 4 | Scenes 2, 3, 4, 5 |
| **3. ESCALATION** | **25 – 30%** | Multi-level emotional compression (Level 1 ➔ Level 2 ➔ Level 3 Peak Tension), push bad karma/challenge to peak | Scenes 5, 6, 7 | Scenes 6, 7, 8, 9 |
| **4. TWIST / REVEAL** | **15 – 20%** | Symbolic prop insert-shot + reveal of true identity / Bodhisattva / Witness | Scene 8 | Scenes 10, 11 |
| **5. KARMA & AFTERMATH** | **15 – 20%** | Symbolic indirect retribution (first part) + still echo of lesson & transcendence (second part) | Scenes 9, 10 | Scenes 12, 13, 14 |

| Stage | Detailed SVEN execution rules |
|---|---|
| **HOOK** | Shot 1 (3s): reveal only 1 curiosity-triggering detail, NO character introduction. **MUST contain ≥ 1 Visual Anchor** that reappears in Scene 2 |
| **SETUP/PLOT** | **First Shot of Scene 2 MUST open with Visual Anchor from Hook** — same object/detail, fully re-described physically. Each subsequent scene reveals 1 more layer of information |
| **ESCALATION** | Compress emotion level by level, push cruel behavior/grievances targeting the vulnerable |
| **TWIST/REVEAL** | ≥ 1 recognition expression shot (shock/realization) + 1 **mandatory insert-shot** (Close-up/ECU static, 1-2s) |
| **KARMA + AFTERMATH** | Karma: EXACTLY the object the character was most proud of ➔ Aftermath: still, forbidden exaggeration (shouting...) |


### 8 Hook Techniques — SVEN Execution

> Select 1 technique per Scoring Framework (story-rules.md § HOOK). Add to metadata: `HOOK TECHNIQUE: #N — [name]`.

| # | Technique | Shot 1 (3s) — open | Shots 2-3 — hold | Final Shot (2s) — close |
|---|---|---|---|---|
| **#1** | **Visual Paradox** | Wide/Full: 2 contradictory images in same frame — hard cut between 2 worlds | Medium: slowly pull to reveal contrast | ECU small detail connecting 2 worlds — freeze |
| **#2** | **In medias res** | Close-up: hand/body part mid-action, cause unclear | Medium: gentle pull back revealing partial context | ECU: expression or object — freeze |
| **#3** | **Strange object/sign** | ECU: unusual static object — no explanation | Slow push-in or tilt reveal adds 1 context layer | Close-up: object + hand touching/not touching — freeze |
| **#4** | **"Frozen Frame"** | Medium/Close-up: suspended action — object falling/flying/breaking | Static or ultra-slow push-in holds the moment | ECU the one part still in motion — freeze |
| **#5** | **Atmospheric Contrast** | Wide: clearly festive/normal setting | Rack focus or pull back reveals discordant detail | Close-up: that discordant detail — freeze |
| **#6** | **Body/Expression Detail** | ECU: eyes/hands/lips with unusual micro-expression | Slow push-in or static holds expression | Cut to ECU another body part confirming emotion — freeze |
| **#7** | **Out of Place** | Medium/Wide: object/person in wrong position — no explanation | Tilt down/up or slow pan reveals more wrongness | ECU: the misplaced contact point — freeze |
| **#8** | **Overlapping Time Traces** | Close-up: surface with old + new marks simultaneously | Slow pull back reveals ruined/historical context | ECU: old-new intersection point — freeze |

### HOOK-SETUP BRIDGE — SVEN Execution for Scene 2 After Hook

> **Render problem:** Omni Flash is stateless — it doesn't know what Scene 1 (Hook) contained. If Scene 2 doesn't fully re-describe the visual anchor with physical detail, the AI video will render 2 unrelated scenes.

**Mandatory when writing Scene 2 (SETUP) immediately after Scene 1 (HOOK):**
1. **`[Prop Profile]` or `[Subject]`**: Visual anchor from Hook MUST be present — fully re-described (size, material, color, condition) — NO reference to Scene 1
2. **`[Global Shot]`**: Opening sentence describes visual anchor FIRST → expands to setting + character
3. **Beat 1 (first 3s)**: Camera opens at/near visual anchor → pull back/pan/tilt to reveal character + setting — creates "aha moment" for viewer

---

## § [10] OUTPUT STRUCTURE — 2 PHYSICAL CODE BLOCKS

### Code Block 1 (The COPY sent to Omni Flash):

> 🚨 **PRE-FLIGHT — MANDATORY BEFORE COPYING PROMPT:**
> Agent MUST list clearly which images to attach, for example:
> ```
> 📎 ATTACH BEFORE SENDING TO OMNI FLASH:
> ① [Character A name] — Character Reference (from 1B)
> ② [Character B name] — Character Reference (from 1B) ← if present
> ③ [Prop name] — Prop Reference (from 1C) ← each STABLE prop with reference
> ④ [Location name] — Environment Reference (from 1D)
> ```
> **If Phase 1 has references → MANDATORY use Mode B** (no full redescription — image already locks it).
> **If Phase 1 has no references → use Mode A** (full description ~120 words/character).

```
Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Hyper-realistic, ultra-high-definition masterwork. Cinematic 9:16 vertical, {style reference}. Shot on {lens}mm prime lens, f/{aperture}, film grain. {time of day — standard phrase from §[1.E]: e.g. "golden hour, low warm sun before sunset" / "nighttime, artificial light only" / "midday harsh sunlight, overhead sun"}.
```

> [!CAUTION]
> **TIME OF DAY is MANDATORY in the Quality line above — do NOT omit or move it to the Context block.**
> Always use a standard phrase from `§[1.E] TIME OF DAY` table (e.g. `"nighttime, artificial light only"` / `"golden hour, low warm sun before sunset"` / `"overcast, flat diffused daylight"`).
> Missing time of day = AI guesses arbitrarily → inconsistent lighting across clips.

▼ CONTEXT (choose Mode):
[MODE A — no ref] {Full setting description, camera-VISIBLE} — {key practical light source} {direction & height} casts {color temperature} light {across/over area} while {atmosphere}; {shadow behavior}; {light transition}.
[MODE B — has ref]      {Location name} [Environment Reference attached], {time of day phrase} — {key light source + color temp, 1 line only}.

▼ LINE A — PROTAGONIST (max 2 Line A+B characters at once in 1 clip):
[MODE A — no ref] {Name A}, {age}-year-old {gender}, {height}cm, {skin tone}, {build}, wearing {costume — NO detached props}. Initial pose: {camera-anchored pose, weight bearing}.
[MODE B — has ref]      {Name A}, {height}cm, {build}. [Character Reference attached]
                       Initial pose: {camera-anchored pose, weight bearing — Name A's hands empty / or right/left hand in contact with prop}.

▼ LINE B — SUPPORTING CHARACTER WITH ARC (if present in this clip, choose Mode):
[MODE A] {Name B}, {age}-year-old {gender}, {height}cm, wearing {costume}. {Camera-relative position.}
[MODE B] {Name B}, {height}cm, {build}. [Character Reference attached]. {Camera-relative position.}

▼ LINE C — CROWD / MASS / SPECTATORS (NO reference image needed — group description):

[ONLY IF PRESENT] {Short group description: estimated number, common costume, collective action, camera-anchored position}.
Line C rules: NO individual names. NO reference images. NO face close-ups. Collective action only.

── GREEK CHORUS FUNCTION (advanced Line C technique) ──────────────────────
Line C is THE VOICE OF SOCIETY — they see through incomplete information.
What they see: the surface. What the real audience knows: the depth.
That gap = DRAMATIC IRONY → the most powerful emotion in drama.

LINE C JUDGMENT PRINCIPLES:
  ① They ALWAYS see from a surface perspective — no context of the protagonist's inner world
  ② They usually JUDGE WRONGLY — criticize the protagonist, praise the antagonist
  ③ Their judgment reflects real social bias (money = skilled, silence = weak, tears = excessive)
  ④ The real audience hurts for the protagonist because they SEE THE TRUTH that Line C cannot
  ⑤ Line C NEVER knows they are wrong — they speak confidently, naturally, without malice

── LINE C WITH DIALOGUE (Greek Chorus Dialogue) ────────────────────────────────
When Line C has dialogue → flexibly describe the speaker by context. No name needed.

  VOICE    : Social whisper, natural gossip — NOT dramatic, NOT loud
  CONTENT  : Surface judgment — accurate to the information they have, WRONG in actual truth
  CAMERA   : DOES NOT cut to Line C's face — captures the echo through shots of the protagonist
              (hearing the voice without seeing the face → protagonist judged with no right of reply)
  LENGTH   : ≤ 80 characters/line

Line C dialogue syntax — FLEXIBLE by context:
  [1 male villager, ~27] : "{dialogue}" (emotional state, manner of speaking)
  [3 frightened villagers] : "{dialogue}" (spoken in unison quietly or as murmuring)
  [elderly woman nearby] : "{dialogue}" (muttering, not looking up)
  [a group of onlookers] : "{dialogue}" (buzzing within the crowd)

Examples — criticizing protagonist, society sees it wrong:
  [1 male vendor, ~40] : "Empty hands. Typical." (flat, matter-of-fact, eyes on his own stall)
  [2 women whispering] : "She should just kick him out." (disapproving click of tongue, not looking)
  [elderly woman nearby] : "That man left. Fifteen years. And now this." (murmured to herself, shaking head)

Examples — praising antagonist for good surface appearance:
  [a group of onlookers] : "He's so generous. Always smiling. Nothing like his brother." (admiring, sincere)

Examples — fear, chaos:
  [3 frightened villagers] : "Run — just run!" (scattered panic, no one looking at each other)


── LINE C APPEARANCE RHYTHM BY BEAT (6-Beat Master Arc) ────────────────────────
  B1 Hook (3%)    : ABSENT or 1 distant blurred silhouette — atmospheric texture only
  B2 Setup (12%)  : Present unintentionally — unknowing witnesses to flawed old world
  B3 Drama (35%)  : Sparse background whispers — full stage for Tier A vs B1 ideological clash (60% dialogue)
  B4 Climax (30%) : Stunned frozen observers or COMPLETELY ABSENT — tragic vacuum for Ego Death
  B5 Release (12%): 1-2 passing figures or safe haven — Tier B2 companion gives unconditional grace
  B6 Echo (8%)    : VIBRANT LIVING COMMUNITY — Tier A harmoniously integrates with Tier C society

▼ HARD LIMITS PER CLIP:
  Line A+B characters              : max 2 (if 3 characters with arc needed → split into 2 separate clips)
  Line C characters                : max 1 group description + max 2 dialogue lines/clip
  STABLE props with ref            : max 2 props/clip (3+ → use wide shot, don't close-up each)
  DESTRUCTIBLE / DUAL PROPS        : describe current state in text (Wound state at B2 ➔ Echo state at B6)

▼ DUAL-PROP SYSTEM (Wound Prop at Beat 2 ➔ 180° Echo Prop at Beat 6):
[MODE A — no ref / TRANSFORMED state] {Prop name}, {size}, {material}, {color}, {current condition at opening frame: Wound State at B2 / Transformed Echo State at B6}, resting {camera-anchored position — ZERO hand assignment — "the only [prop] in frame"}.
[MODE B — STABLE, has ref]             {Prop name} [Prop Reference attached], currently {drawn/worn/resting — current state + position} — the only {prop} in frame.

▼ THERMAL POLARITY LIGHTING & ACOUSTIC SPEC (Beat 4.3 ➔ Beat 5.1):
- Beat 4.3 (All Hope Is Lost): 5600K harsh monochrome cold (blizzard, pitch darkness, rain, ash) + ragged gasping breath.
- Beat 5.1 (Safe Harbor): 2700K soft golden warmth (crackling fireplace, rising dawn, steaming bowl) + `[pause: 1.5s]` silence + `[whispers, warm]`.

▼ ACOUSTIC (ALWAYS INCLUDE when scene has spoken dialogue — system default):
Diegetic room acoustics: {continuous background ambient sound}.

△ [{beat 1 timestamp}] Shot {Scale} | {lens}mm f/{aperture} | {Camera Trajectory}:
{Continuous spatial interaction between Subject A at frame-right and Subject B at frame-left — proper names, observable physical action.}
{Speaker 1 Full Name}：" {dialogue ≤ 160 chars in English} "（{vocal timbre & breath}, {somatic micro-action}, {lighting cast on facial anatomy}, {psychological subtext}）

△ [{middle beat timestamp}] Shot {Scale} | {lens}mm | {Continuing Trajectory / Kinetic Tracking}:
{Heavy kinetic prop friction, physical resistance, tangible surface marks — proper names, continuous co-presence.}
{Speaker 2 Full Name}：" {dialogue ≤ 160 chars in English} "（{vocal timbre & breath}, {somatic micro-action}, {lighting cast on facial anatomy}, {psychological subtext}）

△ [{final beat timestamp}] Shot {Scale} | {lens}mm | {Static lock / slow push-in}:
{Intimate suffocating confrontation — terminal 0.5s zero-velocity freeze hold — proper names.}

Continuous fluid motion, realistic physics, zero morphing. All characters remain anchored in their spatial positions throughout the shot. Sharp optical focus locked on active subjects.

Continuous fluid motion, realistic physics, zero morphing. Sharp optical focus locked on active speaker throughout shot.

Do not generate subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video. Do not render duplicate characters, extra background characters, or duplicate props.
```

---

## 🔇 § SILENT MODE (SHOW DON'T TELL) PROMPT SYNTAX ENGINE

> **Trigger:** User chooses Mode A / Silent Mode / "Show Don't Tell" / "Không thoại" / "Visual only".
> **Core Principle:** In Silent Mode, speech is 100% PURGED. Storytelling is powered entirely by **Kinetic Micro-Biomechanics**, **Prop Causality**, and **Atmospheric Diegetic Foley**.

### 🚫 Strict Prohibitions in Silent Mode Prompts:
1. ❌ **ZERO Dialogue Brackets**: Absolutely NO `[Subject] : "..."` anywhere in Code Block 1.
2. ❌ **ZERO Speech Quotes or Lip-sync Commands**: Never instruct the character to mouth words or speak.
3. ❌ **ZERO Narration / Voiceover Prompts**: No voiceover lines or abstract internal monologues.

### ✅ Mandatory Visual & Acoustic Replacements in Silent Mode:
1. **Micro-Biomechanics Amplified (400% Physicality)**:
   - *Fear/Panic*: `Lok's pupils dilate violently; cold perspiration beads along his hairline as his throat muscles seize in a dry, audible swallow`.
   - *Rage/Restraint*: `Lok's jaw clenches until the masseter muscle bulges; his fingernails dig into his calloused palm, blood vessels swelling along his forearm`.
   - *Grief/Shock*: `Lok's trembling fingers recoil from the broken relic, his chest seizing in a silent ragged gasp as his knees strike the stone floor`.
2. **Pure Diegetic Foley & Environmental Acoustic Architecture**:
   - `Diegetic acoustics: heavy torrential rain pounding rusted tin roofs, rhythmic ticking of a brass pocket watch, echoing iron footsteps on wet flagstones, low resonant sub-bass drone`.
3. **Mandatory Silent Negative Clause (End of Code Block 1)**:
   `Do not generate spoken dialogue, lip movement matching speech, voiceover, subtitles, speech captions, or on-screen text overlaid on video. Do not render duplicate characters or extra props.`

### Master Silent Mode Code Block 1 Template:

```
Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design. Hyper-realistic, ultra-high-definition masterwork. Cinematic 9:16 vertical, {style reference}. Shot on {lens}mm prime lens, f/{aperture}, film grain. {time of day phrase}.

▼ CONTEXT:
{Location name}, {time of day phrase} — {key light source + color temp, 5600K cold / 2700K warm}.

▼ LINE A — PROTAGONIST:
{Name A}, {height}cm, {build}. [Character Reference attached]. Initial pose: {camera-anchored pose, empty hands}.

▼ LINE B — ANTAGONIST / COMPANION (if present):
{Name B}, {height}cm, {build}. [Character Reference attached]. {Camera-relative position}.

▼ PROP:
{Prop name}, {current physical state: Wound state / Transformed Echo state} — the only {prop} in frame.

▼ DIEGETIC ACOUSTICS (Foley & Environment only):
Diegetic acoustics: {heavy wind howling through cracked glass, crunch of gravel under boots, ragged gasping breath, metallic scrape}.

[{beat 1 timestamp}] Shot {scale} | {lens}mm f/{aperture} | {camera movement & angle} on {Subject}
{Subject A} {kinetic action verb} {object/position} on the same floor plane. {Micro-biomechanic: pupils dilating, chest heaving in rapid panic, veins throbbing along neck}.

[{middle beat timestamp}] Shot {scale} | {lens}mm f/{aperture} | {camera movement & angle} on {Subject}
{Subject A} {physical interaction with Prop} while {Subject B} {opposing body reaction: step forward, hand gripping hilt}. {Zero spoken dialogue — pure visual tension}.

[{final beat timestamp}] Shot {scale} | {lens}mm f/{aperture} | {gentle push-in} on {Subject}
{Subject A} reaches {terminal zero-velocity freeze hold pose}, {prop rests in final state}. 0.5s static freeze.

Continuous fluid motion, realistic physics, zero morphing. Sharp optical focus locked on subject action and physical micro-expressions throughout shot.

Do not generate spoken dialogue, lip movement matching speech, voiceover, subtitles, speech captions, or on-screen text overlaid on video. Do not render duplicate characters or extra props.
```

---

## § [10c] SCENE-SPECIFIC NEGATIVE PROMPT RISK TABLE (12.8)


| Scene characteristic | Additional keywords |
|---|---|
| Strong glowing light source (halo, fire) | `overexposed highlights, blown-out light source, washed-out detail` |
| ≥ 3 characters in frame, large Line C crowd | `extra people, incorrect head count, merged figures, repeated identical background figures` |
| Water/rain/mirror/reflective surface | `warped reflection, distorted water surface, duplicated reflection` |
| Fast movement (running, impact, breaking) | `motion smear artifacts, ghosting, unnatural motion blur` |
| Close-up hand handling prop | `malformed hands, extra fingers, wrong hand grip` |
| Line C crowd | `cloned crowd, uniform identical faces in background` |
| Scene with dialogue | `subtitles, on-screen captions, dialogue text overlaid on video` |

---

## § [11] 3-LAYER CHECKLIST — Run before outputting each Scene

### 🔴 CORE (always run fully — fail = broken video):
1. ☑ Content safety pass — no direct violence/injury
2. ☑ Every sentence in actual output passes The Single Test
3. ☑ No pronouns (`he/she/it/his/her`) in entire Code Block 1 — 100% proper names
4. ☑ Every Shot line has `on {Specific Name}`
5. ☑ `[Subject]` paragraph preserves ORIGINAL appearance unchanged (do not update current state here)
6. ☑ `[Prop Profile]` reflects CURRENT state at opening frame of Scene (read Final State first)
7. ☑ Total seconds of all Shots = exactly 10s (§12.9)
8. ☑ Scene ≥ 2: `[Global Shot]` opens with Scene Bridge describing all 5 Final State groups — no references
9. ☑ **[Dialogue]** Total English dialogue characters in Scene ≤ 160 characters
10. ☑ **[Dialogue]** All Code Block 1 dialogue is 100% English, Scripting Bracket Format
11. ☑ **[Dialogue]** Camera cuts to the speaker (Camera-Speaker Binding — §D.5)
12. ☑ **[Dialogue]** Physical mechanics accompanying dialogue reflect subtext, NOT just repeating the line

### 🟠 IMPORTANT (run if time allows):
13. ☑ `[Global Shot]` does not verbatim repeat text from the Shots below it
14. ☑ Prop state changes within Scene are fully re-described in the corresponding Shot
15. ☑ Body-State Compatibility pass (hands/mouth/legs don't conflict)
16. ☑ Final Shot and Shot 3: NO crane/orbit/arc
17. ☑ Scene-specific Negative Prompt added per 12.8 risk table if Scene has risky characteristics
18. ☑ Director's Intention Lock consistent throughout Scene (directorial tone unchanged)
19. ☑ **[Dialogue]** Logical causality chain keyword handoff between turns (§D.2)
20. ☑ **[Dialogue]** Internal subtext declared & physical mechanics CONTRAST surface dialogue (§D.3)

### 🟡 NICE-TO-HAVE (may skip if time-pressed):
21. ☑ No repeated camera angle/focal length 3 consecutive Shots
22. ☑ Sound line follows chronological order matching each Shot (12.5)
23. ☑ Character identifying detail re-mentioned in relevant Close-up Shot (12.6)
24. ☑ Blocking & Eyeline Match clear for ≥ 2 characters: frame-left/right positions, eyeline direction explicitly stated when ≥ 3 people (12.3)
25. ☑ Causal Reaction Rule: character B's action is a direct causal reaction to character A's action
26. ☑ Delta-Only Discipline: inherited state preserves Single Source of Truth from original `[Subject]`, only records Delta changes
27. ☑ Single Ground Plane Rule: 100% of interacting characters standing/kneeling on THE SAME FLOOR PLANE
28. ☑ Absolute Camera-Anchored Positional Lock: declare X-Y-Z coordinates before rendering movement
29. ☑ 4 Camera-Subject Coupling Modes: select 1 of 4 modes
30. ☑ Biomechanical Velocity Budget: movement max 1-1.5m/s (3-5 steps/beat 3-4s)
31. ☑ Terminal Deceleration Protocol: seconds 09-10 (last 0.5s) decelerate velocity to 0

---

## § PROGRESS CONFIRMATION

After each Scene, print:
```
✅ Scene [X]/[N] complete. Do you want to continue to Scene [X+1]?
```
When all N Scenes are done:
```
🎬 All [N] Scenes complete.
```

---

## § [1] OPTICS, FRAMING & DIRECTORIAL CAMERA MATRIX

### 📸 A. 8 Psychological Shot Scales & Lenses (Cỡ Cảnh & Chức Năng Tâm Lý Học)

| Shot Scale | Lens & Framing | Psychological & Directorial Function | Application in 6-Beat Arc |
|---|---|---|---|
| **1. Extreme Close-Up (ECU)** | `100mm Macro` · Pupil dilation, scar ridge, trembling finger | **Peak Visceral Truth / Lie Exposure:** Magnifies involuntary micro-reactions that cannot be faked. | **Beat 4 (Ego Death)** or **Beat 1 (Cliffhanger Freeze)**. |
| **2. Close-Up (CU)** | `85mm Portrait` · Full face from chin to hair top | **Direct Emotional Vulnerability:** Raw exposure of grief, fury, tears, or predatory intent. | **Beat 4 (Climax Peak)**, sudden revelation of mortal stakes. |
| **3. Choker Shot** | `85mm` · Tight cut from chin to upper forehead | **Claustrophobic Deadlock:** Traps characters in psychological corner with zero escape. | Severe psychological ultimatums, breathless confessions. |
| **4. Medium Close-Up (MCU)** | `50mm–85mm` · Chest up | **Workhorse of Cinematic Dialogue (60% coverage):** Nuanced facial micro-expressions and chest heaving. | **Beat 1 (Disruptive Hook)** & **Beat 3 (Escalating Drama)**. |
| **5. Medium Shot (MS)** | `50mm Standard` · Waist up | **Physical Interaction & Prop Manipulation:** Table slamming, weapon unsheathing, deed signing. | Conversational bargaining, inspecting ledgers or seals. |
| **6. Cowboy Shot (MLS)** | `35mm–50mm` · Mid-thigh up | **Combat Readiness (Western Standoff):** Hands hovering near weapons/holsters/pockets. | Pre-combat standoff, tense boardroom/courtroom confrontation. |
| **7. Two-Shot / Wide (WS)** | `35mm–50mm` · Both subjects & spatial void | **Power Balance & Spatial Geography:** Establishes spatial gap (3–5m) and 1-on-1 tension. | **Beat 1 & Beat 3**: Direct dialogue setup, spatial rivalry. |
| **8. Extreme Wide (EWS/ELS)** | `16mm–24mm Wide` · Vast terrain, tiny human figure | **Cosmic / Karmic Judgment:** Human solitude, fate, helplessness before overarching destiny. | **Beat 2 (World Setup)** or **Beat 6 (Cosmic Echo)**. |

---

### ⚖️ B. 6 Power Hierarchy Camera Angles (Góc Máy & Trọng Lượng Quyền Lực)

| Camera Angle | Technical Definition | Power Dynamics & Psychological Impact | Dramatic Application |
|---|---|---|---|
| **1. Low-Angle** | Camera positioned below eye-line looking upward (15°–45°). | **Dominance, Intimidation & Grandeur:** Imparts colossal authority, tyranny, ruthless strength. | Antagonist oppressive pressure, Sovereign on throne, Protagonist rising. |
| **2. High-Angle** | Camera positioned above eye-line looking downward (15°–45°). | **Vulnerability, Defeat & Guilt:** Shrinks the subject into a powerless, judged, or cornered victim. | Interrogation victim, defeated commander on knees, cornered target. |
| **3. Eye-Level** | Camera placed at subject's exact eye height. | **Neutral Balance & Parity:** Impartial observation, equal 1-on-1 clash of matching wills. | Direct negotiation, honest confession, moral stalemate. |
| **4. Dutch Angle (Canted)** | Camera tilted 15°–25° along roll axis. | **Psychological Instability & Chaos:** World slipping off its axis, madness, sudden betrayal. | Mental collapse, sudden betrayal revelation, panic breakdown. |
| **5. Over-the-Shoulder (OTS)**| Framed behind Subject A's shoulder looking at B. | **Conversational Depth & Witness Stance:** Turns viewer into immediate witness behind character. | Core dialogue ping-pong, interrogation pressure. |
| **6. Overhead / Bird's-Eye** | Camera mounted 90° straight down from ceiling/sky. | **Cosmic Omniscience & Fate:** God-like detachment, viewing mortal struggles like chess pieces. | Tactical planning maps, aftermath crime scenes, macro destiny. |

---

### 🎥 C. Camera Movements & Directorial Prohibitions

| Movement Type | Technical Definition | Narrative Purpose | Key Prompt Syntax |
|---|---|---|---|
| **Static Shot** | Locked-off camera, zero movement on all axes. | Solemn gravity, unblinking witness to aftermath. | `Locked-off static camera, zero movement, holding unwavering gaze on...` |
| **Push In (Dolly In)** | Deliberate physical movement forward toward subject. | Tightening intimacy, escalating psychological tension. | `Slow deliberate push-in tightening focus on [Subject]'s clenched jaw...` |
| **Pull Out (Dolly Out)** | Physical movement backward away from subject. | Abandonment, loneliness, expanding dread. | `Slow pull-out retreating away from [Subject] leaving them isolated in darkness...` |
| **Pan Shot** | Horizontal rotation on fixed axis (left $\leftrightarrow$ right). | Scanning environment, revealing hidden threat in room. | `Smooth horizontal pan sweeping left-to-right across the room to reveal...` |
| **Tilt Shot** | Vertical rotation on fixed axis (up $\leftrightarrow$ down). | Scanning subject from boots to eyes, revealing height. | `Vertical tilt shot rising slowly from mud-caked boots up to the cold glare...` |
| **Tracking Shot** | Camera travels alongside, in front of, or behind subject. | Kinetic momentum, active pursuit, matching urgency. | `Lateral tracking shot moving parallel to [Subject] sprinting through...` |

**⚠️ Camera FORBIDDEN when dialogue is present:** `Crane`, `Orbit`, `Arc`, `Whip pan`, `Strong Handheld` — only use `Static`, `Slow Push-in`, `Slow Pull-out` to protect lip-sync. (Exception: 360° Orbit allowed ONLY if dialogue is placed during the final 3s static lock phase).

---

### 🔄 C.1. The 360-Degree Orbit Directorial & Prompt Protocol
When executing a 360-degree continuous orbital take in a 10s AI video prompt:
1. **Rotational Velocity Formula**: $\text{Angular Velocity} = 360^\circ / 10\text{s} = \mathbf{36^\circ / \text{second}}$.
   - `[00:00–00:03]`: Arc $0^\circ \to 90^\circ$ (Front face $\to$ Right shoulder).
   - `[00:03–00:07]`: Arc $90^\circ \to 270^\circ$ (Right shoulder $\to$ Full back $\to$ Left shoulder, revealing background threat).
   - `[00:07–00:10]`: Arc $270^\circ \to 360^\circ$ (Left shoulder $\to$ Front face complete lock + 0.5s freeze hold).
2. **Subject Central Axis Lock**: The subject MUST remain anchored at center frame $(X:50\%, Y:50\%)$ as the rotational axis (`[Subject Name] remains anchored at center frame throughout the entire 360-degree rotation`).
3. **Lip-Sync Delivery Rule**: Spoken dialogue lines MUST NEVER be placed during the fast-rotating phase ($00:00–00:07$). Spoken lines are strictly synchronized to the **final static lock phase `[00:07–00:10]`**.

---

### ⚡ D. In-Camera Transitions vs. Timeline Editing Cuts

```
+----------------------------------------------------------------------------------------------------+
| GROUP 1: IN-CAMERA TRANSITIONS (Unbroken 1-Take 10s — Zero Cut)                                    |
| • 1. The Kinetic Prop Bridge: Camera tracks moving prop (thrown scepter/sliding coin) from A to B. |
| • 2. Steadicam Arc Pivot: Sweeps semi-circular arc (90°–180°) from behind A to frame B directly.   |
| • 3. Optical Rack Focus: Static camera shifts focus from foreground A to background B.             |
| • 4. Vertical Elevation Tilt: Sweeps vertically from elevated dais (A) down to floor level (B).     |
| • 5. Continuous Lateral Reframe: Glides horizontally across table, dropping A and centering B.     |
+----------------------------------------------------------------------------------------------------+
| GROUP 2: TIMELINE EDITING CUTS (Post-Production Multi-Cue Assembly)                                |
| • 1. Shot-Reverse-Shot: Alternates between opposing angles/OTS for ping-pong dialogue battles.     |
| • 2. Reaction Shot: Cuts away from speaker to capture the silent, visceral reaction of listener.   |
| • 3. Graphic & Kinetic Match Cut: Connects two cues via identical geometry or velocity vectors.    |
| • 4. Cutaway (Insert Cut): Brief 1s insert of critical physical detail (clock, poison, dripping blood)
| • 5. Smash Cut: Violent jarring cut from high-decibel chaos to dead silence (or vice versa).       |
| • 6. J-Cut & L-Cut: Sound leads image (J-Cut) or sound lingers across cut into next scene (L-Cut). |
+----------------------------------------------------------------------------------------------------+
```

#### 📐 Graphic & Kinetic Match Cut 4-Point Contract
1. **Coordinate Parity**: Terminal frame of Cue A and Opening frame of Cue B lock the focal object at the exact same screen coordinates $(X:50\%, Y:50\%)$.
2. **Geometry Alignment**: Matching geometric silhouettes (Circle $\to$ Circle / Triangle $\to$ Triangle).
3. **Kinetic Velocity**: Velocity vectors maintain directional continuity (Down $\to$ Down / Left $\to$ Left).
4. **Chromatic Harmony**: Shared color temperature bridge (2200K Red Iron $\to$ Crimson Wax Seal).

---

### ⏱️ E. The 10-Second Clip Capacity & Scene Slicing Law

> [!IMPORTANT]
> **THE 10-SECOND SLICING MANDATE**:
> - **1 Single 10-Second Clip Capacity**: A single 10s take must accomplish **ONE dedicated cinematic objective** (e.g. a tight 1-person monologue, an intimate 2-person tabletop standoff, or a simple A-to-B kinetic tracking pan).
> - **Mandatory Scene Slicing Threshold**: Whenever a scene features **$\ge 3$ characters at different spatial elevations/locations** OR **$\ge 3$ distinct dialogue lines**, attempting to force them into a single 10s prompt causes severe temporal compression, frantic camera movement, and AI morphing.
> - **The 3-Cue Slicing Standard (30s Total)**:
>   - `CUE-01` (10s): Focus on Initiator (e.g. Sovereign on dais delivering judgment & initiating physical kinetic action).
>   - `CUE-02` (10s): Focus on Witness / Middle Ground (e.g. Terrified prelate reacting on middle steps as prop clatters past).
>   - `CUE-03` (10s): Focus on Receiver / Resister (e.g. Defiant commander pinning prop on floor and delivering lethal retort).

---

## § [3.4b] PHYSICAL PRECONDITION RULE — Destructible / Transforming Props

**Problem:** Omni Flash does not automatically infer the "physical process" leading to breaking/bending/collapse. If `[Prop Profile]` describes an intact object → next Shot requires it to break → model draws it intact or vaguely damaged.

**Mandatory rules:**
1. Any prop that will break/crack/tear/collapse in ANY Shot → `[Prop Profile]` opening the Scene MUST have ≥ 1 pre-existing weakness sign (crack, fraying rope, loose joint, rotting wood...)
2. Initial weakness level proportional to seconds allowed — a 2s Shot needs a sign closer to breaking point than a 3s Shot
3. If no precondition yet → must describe clear external force in the Shot immediately preceding the break
4. **Quick test:** read `[Prop Profile]` opening the Scene — if object is "perfect" but the next Shot requires breaking → WRONG, add precondition

**Examples:**
- ❌ WRONG: Prop Profile: "a massive wooden plaque, bright red" → Shot 2: "the plaque snaps in half"
- ✅ CORRECT: Prop Profile: "a massive wooden plaque...a hairline crack running diagonally, supporting ropes visibly frayed" → Shot 2: "the crack widens and splits fully, both halves tearing free from the frayed ropes"

---

## § [3.4c] MOTION-STATE VOCABULARY — Vocabulary for Destruction/Transformation Actions

**Problem:** Using a single completion verb (`snaps`, `shatters`, `collapses`) without an intermediate state → model "skips" from intact to result, bypassing the process.

**Rules:**
1. DO NOT use 1 single completion verb as the entire description of destruction — must include ≥ 1 INTERMEDIATE state phrase (participle/adjective: `-ing`, `already`, `tilted`, `suspended`, `frozen mid-`)
2. 2s Shot: absolute priority for state/suspended vocabulary — describe "frozen" at 1 single moment
3. 3s Shot: may use progressive verb chain AS LONG AS each phase is connected by participle/relative clause

**Recommended vocabulary:**
`already split/torn/collapsed`, `frozen mid-air`, `caught in the instant of`, `suspended`, `mid-collapse`, `mid-fall`, `hanging at an angle`, `tilted`, `scattered`, `still falling`, `half-buried`, `at the exact halfway point of vanishing`

**Vocabulary to AVOID** (when used alone): `snaps`, `crashes`, `breaks apart`, `collapses`, `tears open`, `explodes`, `dissolves`

---

## § [3.5] ANTI-DUPLICATION — Preventing Duplication

**a) Singularity Lock** — mandatory for high-risk scenes (Wide/Establishing/Crane/Orbit):
- Character: `"the only {Name} in frame"`, `"a single figure"`, `"no other person resembling {Name} visible"`
- Prop: `"the single {prop name} on the table, no duplicate nearby"`

**b) Wide/Crane/Orbit shots:** MUST describe all remaining frame content — no descriptive gaps (model will fill gaps by duplicating the main subject):
- ❌ WRONG: `Wide Shot on Minh | Minh stands in the empty field.`
- ✅ CORRECT: `Wide Shot on Minh | Minh stands alone in the empty field, the only figure in frame; rows of dry rice stalks stretch behind Minh to an empty horizon.`

**c) ≥ 2 characters in same Scene:** Each person's `[Subject]` must differ in ≥ 3 axes: height, skin/hair tone, build, perceived age, costume color.

**d) Line C / crowd:** Do not use generic plurals (`"villagers"`, `"a crowd"`). 2-3 people: short description but differing in ≥ 1 detail each. > 3 people: group description with clear variation.

**e) Common props** (bowl, cup, knife...): Must specify position + quantity: `"the only bowl on the table"` or `"two bowls: one chipped near Lien, one full near Minh"`.

---

## § [4b] INTRA-SCENE HANDOFF GATE — Intra-Scene Continuity

**Problem:** Agent uses "mental check" before each Shot → misses non-focal entities.

**Mandatory solution: Intra-Scene State Table** (internal, DO NOT output to Omni Flash):

Before Shot 1, build a table listing ALL entities present: `{Entity name} | State at start of Shot 1`

After writing each Shot → update the corresponding row immediately → only then proceed to next Shot.

**4 mandatory cross-reference groups between Shot [N] → Shot [N+1]:**
1. State of all characters present (including those not the main focus of this Shot)
2. State of all props present (including props just used on another object/character)
3. Supporting characters (Line B/C) and pets being interacted with — re-state with 1 short clause
4. Space & time — relative positions between entities, traces just left behind

**Quick test:** read the Shots in sequence as continuous prose — if any entity "loses its state" or "resets to original" without an explaining action → WRONG.

---

## § [4.5] 2-CHARACTER / CROWD / WITNESS RULES

### a) Active/Passive Rule
In each Beat (2-4s), **ONLY 1 character** performs the Primary Action (Active). The other character ONLY Reacts passively.

**Mandatory anchor positions when 2 characters in same Shot:**
`Subject A at frame-left facing frame-right; Subject B at frame-right facing frame-left`

**Prop Intermediary — blocking hand-merging:**
- NEVER allow 2 characters' hands to interlock/touch directly → use prop as intermediary object
- ✅ CORRECT: `Lok snatches the cloth pouch from Ren's trembling palms — the pouch the only contact point`
- ❌ WRONG: `Lok grabs Ren's hands and pulls.`

### b) Continuous Co-Presence & Dual-Action Somatics (Eliminating Subject Amnesia)
Generative video models suffer from **Subject Amnesia** if characters are described in isolation. Both characters MUST remain anchored in space (Frame-Left vs Frame-Right) with bidirectional actions in every second:

$$\mathbf{Subject\ A\ Initiates\ Physical\ Action}\ \longleftrightarrow\ \mathbf{Subject\ B\ Somatic\ Reaction\ Simultaneously}$$

* Example: `△ [00:03–00:07]: Dax at frame-right forcefully slides the Debt Scroll across the wood, gouging a white scratch; directly opposite at frame-left, Vin clamps his gauntleted palm over the parchment as it strikes his cuffs, chest heaving in defiance.`

### c) Domain-Specific Tactile Physics Catalog

| Genre Domain | Tactile Physics & Material Friction Details | Atmospheric & Prop Somatics |
|---|---|---|
| **⚔️ Wuxia / War / Martial Epic** | Iron armor creaking against wet ship gunwales; steel blade scraping frost off frozen stone; shattered bronze fragments crushed flat beneath iron boots; snow melting on scarred brow ridge. | Heavy wool cloaks sodden with sleet, breath freezing into thick white clouds, weapon hilts wrapped in fraying leather cords. |
| **🏛️ Aristocracy / Family / Boardroom** | Brittle red sealing wax cracking under thumb pressure; lukewarm porcelain teacup rattling on saucer; heavy brass seal chipping mahogany varnish; heavy chair legs scraping dry hardwood. | Crisp starched collars choking neck veins, signet rings catching crystal chandelier reflections, trembling inkwell quills. |
| **🕵️ Noir / Detective / Crime** | Zippo lighter metallic flint click and sharp flare of amber flame; rusted iron handcuffs clinking taut against pipe; scorch marks on magnetic tape reels; cigarette smoke swirling in streetlamp beam. | Wet asphalt reflecting sodium vapor glow, sodden trench coat shoulders, water droplets condensing on revolver cylinder. |
| **👑 Gothic / Imperial Court / Religious** | Gold royal scepter rebounding with a sharp spark off polished white marble steps; scarlet velvet cape embroidered with heavy gold bullion thread; ivory crucifix trembling against collar. | Choking incense clouds catching stained-glass sunlight, heavy bronze cathedral doors groaning shut, candelabra wax dripping onto flagstones. |

### d) Emotion Physics — ZERO abstract emotion words

| Emotion (DO NOT USE) | Replacement Mechanics (USE THIS) |
|---|---|
| `fearful` / `scared` | Pupils contracting, both shoulders hunching tensed, rapid breaths through parted lips |
| `angry` / `furious` | Temple vein visibly pulsing, jaw locked tight, eyes blazing with fixed intensity |
| `sad` / `sorrowful` | Trembling hands reaching into empty air, a tear rolling through mud-streaked cheek |
| `desperate` / `pleading` | Head bowing down, knees touching floor, open palm not yet reaching the other person |
| `shocked` / `stunned` | Step frozen mid-stride, held object released, mouth falling open without sound |
| `relieved` | Shoulders dropping slowly, a long breath out through the nose, jaw muscles releasing |

### e) Crowd "1 + Blurred Background"
- **1 sharply-focused lead character** in foreground (`sharp optical focus`)
- Crowd behind: `out-of-focus background blurred silhouettes moving as a unified mass`
- DO NOT describe multiple faces in sharp detail — AI cannot render evenly, produces artifacts

### f) Witness Reaction Shot
- **Separate Shot** — don't cram perpetrator + witness into the same 3s Shot
- **Choose 1 representative** and use a freeze reaction: `steps frozen mid-stride, hands releasing the carried object, eyes wide in shock`

---

## § [4.6] SPATIOTEMPORAL SYNCHRONIZATION MASTER SPEC

All 10s intra-scene and cross-scene synchronization follows **4 Invariant Physical Metrics**:

### 1. Spatial Topology Lock
- **Single Floor Plane Lock**: 100% of interacting characters MUST kneel/stand on the same floor plane (`on the same timber floor/dirt ground`), 1.5m – 3m apart.
- **Camera-Anchored Coordinate Declaration**: Declare X-Y-Z coordinates in the very first sentence: `Subject A at frame-left facing frame-right; Subject B at frame-right facing frame-left on the same timber floor, 2 meters apart`.
- **Separate Scene When Changing Elevation**: FORBIDDEN to cram a climb/tower ascent into 10s. Split: Scene A (at base 10s) ➔ Scene B (already at tower top 10s).

### 2. Temporal Kinetic Bridging
- **Kinetic Bridge Connector**: Beat 2/Beat 3 MUST open with a kinetic connector linking the inertia from the previous Beat (`As Lok halts an arm's length from Keth...` / `Driven by the same stillness...` / `Continuing the forward momentum...`).
- **1 Cause ➔ 2-3 Effects**: 1 Shot is a causally linked chain of physical reactions: `Lok steps forward (cause) ➔ dust motes swirl (effect 1) ➔ Keth's eyes flick downward (effect 2)`. FORBIDDEN to cram 2 independent large actions with "then/after that".

### 3. Character State Persistence
- **Single Source of Truth**: Original `[Subject]` defines appearance, age, scars, costume color. Every Beat MUST use **PROPER NAME** (`Lok`, `Keth`), ABSOLUTELY FORBIDDEN to use pronouns `he/she/it/his/her`.
- **Costume Damage Persistence**: Tears/dirt from previous Scene MUST be maintained intact in the next Scene (`left shoulder tear intact`).
- **Micro-Biomechanics**: Translate all emotion into physical mechanics (`jaw tightening`, `pupils dilating`, `knuckles whitening`).

### 5. Motion-Spatial Discontinuity Elimination Rules
- **Target Distance Lock (Forbidden Overshooting)**: If initial distance between A and B is 1.5m – 2m, A may only take **EXACTLY 1 SHORT STEP** (0.5m) in Beat 1 (00:00-00:03). FORBIDDEN to write "A strides broadly" making A overshoot past B (Overshooting artifact).
- **Temporal Handoff Continuity (NO Time Rewinding between Beats)**: Beat 2 MUST continue EXACTLY at the position and time Beat 1 stopped. FORBIDDEN if Beat 1 describes A already close to B, then Beat 2 writes "When A stops 2 steps from B" (time-rewind / position-rewind error).
- **Single Primary Prop Discipline (Prevent Prop Overflow / Prop Drift)**: In 1 Scene of 10s, ONLY declare **EXACTLY 1 PRIMARY PROP** in `[Prop Profile]`. Other architectural/setting details belong in `[Context]`. FORBIDDEN to declare 3-4 secondary props causing AI confusion and prop self-duplication.

---

## § [10c] 12 COMMON ERRORS (Cross-cutting Error Check Framework)

| # | Error Name | Identifying Signs | How to Fix |
|---|---|---|---|
| 12.1 | Profile-Action Conflict | `[Subject]` locks hands but Shot needs to hold prop | Remove hand-lock from `[Subject]`, use neutral upper-body description |
| 12.2 | Causal Motivation Gap | Character changes mind/action without observable stimulus before it | Add 1 physical trigger detail before the change-of-mind action |
| 12.3 | Spatial Overcrowding | ≥ 2 characters but no frame-left/right/foreground-background declared | Add `Subject A at frame-left... Subject B at frame-right...` |
| 12.4 | Unmotivated Camera Jump | Jump from ECU to Wide with no dramatic reason | Add 1 intermediate Shot or explain reason for scale change |
| 12.5 | Sound-Shot Mismatch | Sound line doesn't match action/timing of Shot | Rearrange Sound line chronologically to match each Shot |
| 12.6 | Identity Loss at Close-up | Close-up omits identifying detail (costume color, scar, accessory) | Restate ≥ 1 clear identifying detail in opening sentence of Shot |
| 12.7 | Number/Pronoun Agreement | Plural used but subject is singular, or `he/she/it` instead of name | Replace all personal pronouns with proper names in actual output |
| 12.8 | Missing Scene-Specific Safety | Scene has risky characteristics (crowd, water, close-up hand) but lacks appropriate `Do not...` | Add Group C phrases from Negative Prompt table (§ Negative Prompt Master List) |
| 12.9 | Total Duration Mismatch | Total seconds of Shots ≠ duration stated at Scene head | Re-add and fix the most flexible Shot (usually the final one) |
| 12.10 | Active/Passive Violation | 2 characters in same Beat both have active actions, or hands touch directly | Designate Active/Passive, add Prop Intermediary |
| 12.11 | Crowd/Witness Artifact | Multiple clear crowd faces, or perpetrator + witness in same Shot | Apply "1 + Blurred Background"; split Witness into separate Shot |
| 12.1b | Motion-in-Static Conflict | Single completion verb (`snaps`, `explodes`) with no intermediate state | Replace with participle/suspended state (see § [3.4c]) |
| **D.1** | **Dialogue Over-Explicit** | Dialogue states emotion directly (`"I am afraid"`, `"I hate you"`) | Replace with indirect dialogue + body betraying subtext (§D.0, §D.3) |
| **D.2** | **Dialogue Causality Break** | Next dialogue line does not pick up keyword from previous line | Apply Logical Causality Chain — Keyword Handoff (§D.2) |
| **D.3** | **Camera-Speaker Mismatch** | Camera does not cut to the speaker | Apply Camera-Speaker Binding §D.5 Rule 1 |
| **D.4** | **Lip-sync Camera Violation** | Beat has dialogue but uses Crane/Orbit/Arc | Switch to Static or Slow Push-in |

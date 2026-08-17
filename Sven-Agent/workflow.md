# WORKFLOW — Short Video Agent (Mandatory Working Process)

> ⚠️ **THIS IS THE FIRST FILE TO READ — ABSOLUTELY MANDATORY**
> Agent MUST read this entire file BEFORE processing any user request.

---

## 📋 FILE READING ORDER — MANDATORY AT SESSION START

```
[1] workflow.md              ← This file — read first
[2] history-registry.json   ← d:\Project\Sven\history-registry.json
[3] story-rules.md          ← references/story-rules.md
[4] sven-rules.md           ← references/sven-rules.md
```

---

## 🔍 STARTUP STEPS

### K1 — Read History Registry

```
ANTI-REPETITION CHECK:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Character names used   : [used_character_names]
Props used             : [used_props]
Locations used         : [used_locations]
Hooks used             : [used_hook_techniques]
Visual styles used     : [used_visual_styles]
Archetypes used        : [used_archetypes]
```

### K2 — Identify Request Type

| Request type | Signal | Action |
|---|---|---|
| Vague / general | No specific idea | → **Step 0** |
| Has idea | Character/setting/conflict described | → Skip Step 0, go to **Step 1** |
| Revision | Feedback on script/prompt | → Edit directly |
| Prompt only | "create prompt for scene N" | → **Stage 4** for that scene |
| Has dialogue | "dialogue", "voiceover", "lip-sync" | → Activate §D in sven-rules.md |

---

## 🗺️ PROCESS OVERVIEW

```
[INPUT] User request
          ↓
[K1] Read history-registry.json
[K2] Identify request type
          ↓
╔══════════════════════════════════════════════╗
║  STEP 0 — IDEA GENERATION                   ║
║  5 Ideas (character + setting + story        ║
║  + positive / hopeful ending)                ║
║  ✋ CHECKPOINT 0: User selects 1 Idea        ║
╚══════════════════════════════════════════════╝
          ↓
╔══════════════════════════════════════════════╗
║  STEP 1 — PRE-PRODUCTION                    ║
║  Visual Style + Character/Prop/Env Setup     ║
║  + Reference image prompts (4 angles)        ║
║  + Initial Setting Declaration               ║
║  ✋ CHECKPOINT 1: User confirms              ║
╚══════════════════════════════════════════════╝
          ↓
╔══════════════════════════════════════════════╗
║  STAGE 2 — SERIES BLUEPRINT                 ║
║  (Multi-Episode Series only)                 ║
║  4-Act episode distribution + each ep role  ║
║  ✋ CHECKPOINT 2: User confirms              ║
╚══════════════════════════════════════════════╝
          ↓
╔══════════════════════════════════════════════╗
║  STAGE 3 — DETAILED SCRIPT                  ║
║  Per episode: 8 Beat × 15s + Emotion Score  ║
║  + Cliffhanger (if series)                   ║
║  ✋ CHECKPOINT 3: User confirms each episode ║
╚══════════════════════════════════════════════╝
          ↓
╔══════════════════════════════════════════════╗
║  STAGE 4 — SVEN PROMPT                      ║
║  sven-rules.md → 2 AI Clips × 8 Beats/ep   ║
║  ✋ CHECKPOINT 4: Per Beat                   ║
╚══════════════════════════════════════════════╝
          ↓
[POST] Update history-registry.json
```

---

## 💡 STEP 0 — IDEA GENERATION

> Output **5 distinct Ideas** → wait for user to select one.

**Hard rules:**
- **Ending ALWAYS positive / hopeful** — character grows / reconciles / is saved / inspires. NEVER a dead-end tragedy with no redemption.
- 5 Ideas must differ: genre / conflict type / character arc / target emotion

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IDEA #[N] — [Suggested title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GENRE        : [Drama / Action / Thriller / ...]
FORMAT       : [Short Film 2 min / Multi-Episode Series X eps]
SETTING      : [Location + era + atmosphere — 1 sentence]
CHARACTER A  : [Protagonist — defining trait + core weakness]
CHARACTER B  : [Catalyst/antagonist — role]
PLOT         : [Core conflict — 2-3 sentences]
TWIST HINT   : [Direction hint — do not fully reveal]
OUTCOME      : [Positive / hopeful ending — what character/audience gains]
EMOTION      : [What audience feels after watching]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 🪷 SPECIAL MODE: BUDDHA AS PROTAGONIST

**Trigger:** User mentions "Duc Phat lam nhan vat chinh", "Phat lam nhan vat chinh", "Buddha protagonist", "kich ban Duc Phat"

**Activate:** Switch to Awakening & Transcendent Narrative — 3 canonical story types:

| Type | Pattern | Core Dynamic |
|---|---|---|
| **1 — Transformation of Evil** (Angulimala style) | Violent killer / warlord vs. Buddha's absolute stillness | Villain throws down weapon and repents |
| **2 — Consolation of Grief** (Kisa Gotami style) | Boundless grief of loss vs. Wisdom illuminating Impermanence | Understanding and releasing suffering |
| **3 — Humbling of Ego** (Ajatasattu style) | Power / military might vs. the grandeur of the Dharma | Ego collapses, kneels to take refuge |

**Rules for 5 Ideas in Buddha Mode:**
- 100% of 5 ideas have Buddha as central character throughout (Observer / Guide / Awakener)
- Each idea MUST use a DIFFERENT Hook technique from the 12-Hook library
- Each idea output: 👤 Buddha's role & who he awakens / 🌍 Setting / 📖 Journey / 🎣 Hook technique / ⚖️ Philosophical lesson

---

### 🗿 SPECIAL MODE: BUDDHA STATUE VENERATION

**Trigger:** User mentions "Tuong Phat", "sua tuong", "lau tuong", "thap huong", "dang do cung Phat"

**Activate:** Apply the 4-Pillar Veneration Framework:

| Pillar | Action | Karmic Reward |
|---|---|---|
| **1** | Repair cracked/broken statue | Healing broken relationships / family harmony |
| **2** | Clean dust and grime from statue | Clear karma → beauty restored, illness healed |
| **3** | Offer incense, water, flowers | Pure heart → water source saves drought, lasting good name |
| **4** | Offer food when hungry | Surrender greed → abundance forever, meeting a benefactor |

**Rules:** All 5 ideas built around one or more of the 4 pillars. Buddha statue is the symbolic prop with its own State Chain.

---

**✋ CHECKPOINT 0:** User selects Idea → Agent confirms → proceed to Step 1

---

## 🎨 STEP 1 — PRE-PRODUCTION

### 1A — VISUAL STYLE & BASIC SETTINGS

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HOW VISUAL STYLE WORKS — READ FIRST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[visual style] is set ONCE here in 1A.
It then propagates automatically into EVERY prompt downstream:

  ① Character reference grid    → "[visual style]" appended to grid prompt
  ② Prop reference grid         → "[visual style]" appended to grid prompt
  ③ Environment reference grid  → "[visual style]" appended to grid prompt
  ④ Every CLIP prompt (A + B)   → "[visual style]" in Quality block

DEFAULT (system-wide): Pixar 3D
↳ Pixar · DreamWorks · Disney · Family
↳ Use unless user explicitly picks another style.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VISUAL STYLE LIBRARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

── LIVE ACTION ────────────────────────────
  Theatrical Cinematic      Live-Action · Realistic · Premium
  Modern Microdrama         Rise-Up · Revenge · Urban
  French Arthouse           Arthouse · Parisian · Intimate
  Monumental Epic           Dune · Monumental · Sacred
  Bollywood                 Bollywood · Festive · Ornate
  Nordic Noir               Scandinavian · Bleak · Cold
  Golden Western            Western · Ranch · Golden Hour
  Pop Dystopia              Survival Game · Primary Colors · Vibrant
  Prestige HBO              Corporate · Power · Cold Luxury
  Gritty Desert             Desert · Crime · Sun-Baked
  Wes Anderson Style        Symmetry · Pastel · Refined
  David Lynch Style         Surreal · Eerie · Dreamlike · Dark
  Quentin Tarantino Style   Violent · Retro · Cult
  Christopher Nolan Style   Mind-Bending · Cool · Grand · Scale
  Blade Runner Style        Future · Ruins · Solitude
  Modern K-Drama            Romance · Urban · Idol
  Crime Drama               Cartel · Prison · Drama
  Game of Thrones Style     Medieval · War · Epic · Dark
  European Epic             Ancient · Armor · Battle · Grand

── ANIMATION ──────────────────────────────
  Cinematic 3D              Game CG · Realistic · Unreal Engine
  Soft Contemporary         Urban · Romance · Gentle
  Monochrome Manga          B&W · Manga · Raw Ink
  Mature Western Animation  Adult · Dark · Cinematic
  Spider-Verse Style        Comic Book · Halftone · Pop
  3D Cyberpunk              Neon · Cybernetic · Futuristic
  Cthulhu Style             Alien · Dark Souls · Bloodborne
  Color Ink Wash            Traditional · Colorful · Brushwork
  Junji Ito Style           Horror · Dense · Madness
  Thriller Folklore         Gloomy · Suspenseful · Folk Horror
  Clay Stop-Motion          Shaun the Sheep · Tactile · Stop-motion
  Felt Stop-Motion          Felt · Soft · Handmade
  Ghibli Style              Ghibli · Watercolor · Nostalgic
  Korean Webtoon            Webtoon · Fashion · Flat Color
  Retro 90s Cel-Shaded      90s · EVA · Slam Dunk · Classic
  High-Energy Action        Demon Slayer · Combat · VFX
  Chinese Xianxia           Xianxia · Aesthetic · Ink
  Next-Gen Cel-Shaded       Genshin · ZZZ · Star Rail
  Painterly Cel-Shaded      Arcane · Brushwork · Dramatic
★ Pixar 3D (DEFAULT)       Pixar · DreamWorks · Disney · Family

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GENRE LIBRARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Billionaire Romance       CEO Workplace Romance     Mafia Romance
  Werewolf Fantasy          Vampire Supernatural      Royal Romance
  Historical Romance        K-Drama Romance           J-Drama Healing
  Telenovela Melodrama      SEA Family Drama          BL Romance
  Revenge Drama             Family Secrets            Youth Campus
  Entertainment Industry    Medical Drama             Legal / Crime
  Thriller Mystery          Urban Fantasy             Survival Adventure
  Light Comedy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BACKGROUND LIBRARY (Primary Setting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Modern City               Luxury Mansion            Corporate Office
  University Campus         Hospital                  Courtroom
  Entertainment Set         Small Town                Island Resort
  Royal Court               Historical Palace         Mafia Underworld
  Supernatural Realm

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TROPE LIBRARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Contract Marriage         Secret Baby               Hidden Identity
  Enemies to Lovers         Second Chance             Revenge Comeback
  Forbidden Love            Love Triangle             Forced Proximity
  Heir Reveal               Cinderella Rise           Fake Relationship
  Fated Mates               Amnesia                   Time Travel
  Rebirth                   Found Family              Redemption Arc

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VISUAL STYLE  : Pixar 3D  ← DEFAULT — override only if user requests
EPISODE MODE  : [Single (Short Film) / Multi-Episode Series]
RATIO         : [9:16 vertical / 16:9 horizontal]
DURATION      : [2 min/ep — standard 8 beats × 15s]
EPISODE COUNT : [N episodes (if series)]
GENRE         : [Pick from Genre Library above]
BACKGROUND    : [Pick from Background Library above]
TROPE         : [Pick from Trope Library above — can stack 2 max]
```

> **HOW EACH SETTING FLOWS DOWNSTREAM:**
>
> | Setting | Affects what? | Applied where? |
> |---|---|---|
> | **Visual Style** | Render look of ALL images & clips | ① Appended to every reference grid prompt<br>② Quality block of every Clip A + B |
> | **Genre** | Story tone, conflict type, character dynamics | ① Step 0 — filters which Idea types to generate<br>② Stage 2S — influences Hook, Conflict, Emotion Arc |
> | **Background** | Primary environment for the film | ① 1D — Environment Profile is built around this<br>② Initial Setting Declaration uses this as anchor |
> | **Trope** | Narrative structure, twist type, character relationships | ① Step 0 — steers Idea generation<br>② Stage 2S — sets Twist Type and Beat rhythm<br>③ Anti-Repetition check in history-registry.json |
>
> **Example — Pixar 3D + SEA Family Drama + Small Town + Redemption Arc:**
> - Every grid image → rendered in Pixar 3D style
> - Idea generation → focused on family conflict, warm emotional arc, village setting
> - Environment → small Vietnamese town, warm afternoon light, weathered shop fronts
> - Beat structure → builds toward redemption moment, cathartic ending




### 1B — CHARACTER PROFILE + REFERENCE IMAGE PROMPTS

> Each Line A and B character needs: **1 reference grid image** first — then 4 individual shots if higher detail needed.

> **CHARACTER COSTUME RULES — MANDATORY:**
> - 🔴 Hands are **always empty** — no detached props (no bags, weapons, tools, objects held)
> - 🔴 Only clothing **fixed to body** — shirts, trousers, shoes, belts, hats worn on head
> - 🔴 No flowing cloaks, no draped robes, no held accessories in reference sheets
> - ✅ Fixed accessories are allowed: wristwatch, glasses ON face, earrings, necklace worn flat
> - Props the character interacts with — described in **Clip prompts only**, never in reference grid

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHARACTER: [Code name, 1 syllable]
CHARACTER LINE / ARC: [A/B/C] | [Arc type: Opening state → Closing state]
BACKSTORY TRAUMA: [Core wound that shapes behavior]

RELATIONSHIP (with the other Line A/B character):
  TYPE        : [Mentor/Apprentice | Family/Blood | Former Lovers | Rivals | Employer/Worker | Creditor/Debtor | Strangers | Enemies in Alliance]
  DESCRIPTION : [1 sentence — who are they to each other and what is the unresolved wound between them]

POWER DYNAMIC:
  Opening     : [A dominant / B dominant / Equal]
  Shift at    : [Beat N] — Triggered by: [specific action or reveal]
  Closing     : [A dominant / B dominant / Equal / Mutual loss]

ADDRESS FORMS (for dialogue scenes — lock for entire script):
  A → B       : [how A calls B: first name / nickname / "Sir" / "Boy" / no address / etc.]
  B → A       : [how B calls A]
  Shift       : [Beat N — who changes, from what to what, and what it signals]
  VN voice actor ref: [Vietnamese honorific equivalents: anh/em / ông/tôi / thầy/con / etc.]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APPEARANCE PROFILE (English, ~80 words — LOCK for entire series):
[Name], [age]-year-old [gender], [height], [skin/ethnicity], [build],
[hair color/style/length], [defining facial features as observable behavior],
wearing [clothing only: material, color, key details — NO props].

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REFERENCE IMAGE PROMPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[STEP 1 — REFERENCE GRID — CREATE FIRST — MANDATORY]
Character reference sheet — single image, 4-panel row layout (1 row × 4 columns).
Header text printed at top center of image:
"CHARACTER: [Code name] | FILM: [Film title] | AGE: [age] | [gender]"
Panel layout (left to right):
  Panel 1 : medium close-up face portrait, neutral expression, chin slightly down
  Panel 2 : full body front view (0°), arms relaxed at sides, feet shoulder-width
  Panel 3 : full body strict 90-degree left profile, arms relaxed
  Panel 4 : full body viewed from directly behind (180°), arms relaxed
All four panels: same costume, same pure white background, even studio lighting.
[Full appearance profile], [visual style], hyperrealistic, sharp detail.
Negative: dynamic poses, heavy shadows, background elements, cropped limbs,
  any object held in hands, bags, weapons, detached accessories, flowing cloaks.

[STEP 2 — 4 INDIVIDUAL SHOTS — create after if higher detail needed]

[SHOT 1 — FACE REFERENCE — Medium Close-up]
Character concept art. [Full appearance profile].
Medium close-up portrait, face looking directly at camera, neutral expression,
chin slightly down, soft front-left studio lighting, pure white background,
hyperrealistic, sharp focus on facial features, [visual style].
Negative: smile, strong expression, body below chest, heavy shadows on face.

[SHOT 2 — FULL BODY FRONT — 0°]
Character concept art. [Full appearance profile].
Full body standing straight, facing camera directly (0° angle),
arms relaxed at sides, feet shoulder-width apart,
pure white background, even studio lighting, no shadows, [visual style].
Negative: cropped limbs, dynamic/action pose, background elements.

[SHOT 3 — FULL BODY SIDE — 90°]
Character concept art. [Full appearance profile].
Full body standing, strict 90-degree left profile view,
arms relaxed, pure white background, even studio lighting, [visual style].
Negative: front-facing, three-quarter angle, cropped.

[SHOT 4 — FULL BODY BACK — 180°]
Character concept art. [Full appearance profile].
Full body standing, viewed from directly behind (180°),
arms relaxed, pure white background, even studio lighting, [visual style].
Negative: front-facing, face visible, cropped.
```

### 1C — PROP PROFILE + REFERENCE IMAGE PROMPTS

> **PROP DURABILITY RULES — MANDATORY:**
> - **STABLE prop**: physical form stays the same throughout film (apron, watch, key) — needs Reference Grid + optional 4 shots
> - **DESTRUCTIBLE prop**: changes physical state during film (bowl → shards, glass → broken pieces, rope → frayed strands)
>   - Original state → needs Reference Grid (to establish baseline appearance)
>   - Transformed/destroyed state → **description only in Clip prompt** — no new reference image needed
>   - Transformed state description must be precise: material, size of fragments, scatter pattern, surface texture

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROP: [Code name EN]
ROLE: [Symbolic prop / Supporting prop]
DURABILITY: [STABLE / DESTRUCTIBLE]
STATE CHAIN: [Initial] → [Setup] → [Twist] → [Resolution]
TRANSFORMED STATE: [If DESTRUCTIBLE — describe exact physical form after change]
  e.g. — ceramic bowl → "3 large curved shards, white glazed interior face-up,
           edge fractures showing gray clay cross-section, scattered 30cm radius"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROP PROFILE (English, LOCK for entire series):
[Prop name]: [material], [shape/dimensions], [color/texture/pattern],
[weight/feel], [distinctive marks/wear/damage], [current condition].
(Do NOT describe how it is held — hands always in Clip prompts only)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REFERENCE IMAGE PROMPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[STEP 1 — REFERENCE GRID — CREATE FIRST — MANDATORY]
Prop reference sheet — single image, 2x2 grid layout.
Header text printed at top center of image:
"PROP: [Code name] | FILM: [Film title] | ROLE: [role]"
Grid layout:
  Top-left     : three-quarter hero perspective, dramatic soft lighting
  Top-right    : strict front-view orthographic, flat even lighting
  Bottom-left  : strict 90-degree side-view orthographic
  Bottom-right : strict back-view orthographic
All views: pure white background, [full prop profile], the only [prop name] in frame.
[visual style], photorealistic, sharp surface detail.
Negative: hands holding prop, background elements, duplicate props.

[STEP 2 — 4 INDIVIDUAL SHOTS — create after if higher detail needed]

[SHOT 1 — HERO PERSPECTIVE — 3/4 angle]
Product concept art. [Full prop profile]. Three-quarter perspective,
dramatic soft lighting highlighting texture and material,
pure white background, photorealistic, sharp surface detail,
the only [prop name] in frame, [visual style].

[SHOT 2 — FRONT ORTHOGRAPHIC]
Product concept art. [Full prop profile]. Strict front-view orthographic,
no perspective distortion, centered, even flat studio lighting,
white background, all front details visible, the only [prop name] in frame.

[SHOT 3 — SIDE ORTHOGRAPHIC — 90°]
Product concept art. [Full prop profile]. Strict 90-degree side-view orthographic,
no perspective distortion, centered, even flat lighting,
white background, all side details visible, the only [prop name] in frame.

[SHOT 4 — BACK ORTHOGRAPHIC]
Product concept art. [Full prop profile]. Strict back-view orthographic,
no perspective distortion, centered, even flat lighting,
white background, all back details visible, the only [prop name] in frame.
```

### 1D — ENVIRONMENT PROFILE + REFERENCE IMAGE PROMPTS

> Each location needs: **1 reference grid image** first — then 4 individual shots if higher detail needed.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENVIRONMENT: [Location name]
TIME OF DAY: [Time + weather]
ATMOSPHERE: [Emotional tone]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENVIRONMENT PROFILE (English, LOCK for entire series):
[Location]: [architectural style], [size/scale], [key structural elements],
[floor material], [lighting source], [color palette], [atmospheric condition],
[time of day], [distinctive environmental details].

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REFERENCE IMAGE PROMPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[STEP 1 — REFERENCE GRID — CREATE FIRST — MANDATORY]
Environment reference sheet — single image, 2x2 grid layout.
Header text printed at top center of image:
"ENVIRONMENT: [Location name] | FILM: [Film title] | TIME: [time of day] | ATMOS: [tone]"
Grid layout:
  Top-left     : wide establishing shot, low angle, full scope of location
  Top-right    : alternate wide from opposite or elevated angle
  Bottom-left  : aerial top-down view, floor plan layout fully visible
  Bottom-right : medium close on key focal point (altar/door/workbench/etc.)
All views: no characters, [full environment profile], [visual style], cinematic composition.
Negative: people, animals, written text overlays other than header.

[STEP 2 — 4 INDIVIDUAL SHOTS — create after if higher detail needed]

[SHOT 1 — ESTABLISHING WIDE — Low angle]
Environment concept art. [Full environment profile]. Wide establishing shot, low angle,
full scope of [location], [lighting], dramatic atmosphere,
no characters, [visual style], cinematic composition.

[SHOT 2 — ALTERNATE WIDE — Second angle]
Environment concept art. [Full environment profile]. Wide from [opposite/elevated] angle,
[different spatial relationship], [lighting], no characters, [visual style].

[SHOT 3 — TOP-DOWN / BIRD'S EYE]
Environment concept art. [Full environment profile]. Aerial top-down view,
complete floor plan layout visible, spatial relationships clear,
lighting from above, no characters, [visual style].

[SHOT 4 — KEY DETAIL FOCUS]
Environment concept art. [Full environment profile]. Medium shot focused on
[key focal point: altar/door/throne/workbench/etc.], dramatic lighting,
atmosphere and texture emphasis, no characters, [visual style].
```

### 1E — INITIAL SETTING DECLARATION

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INITIAL SETTING — STARTING STATE (Single Source of Truth)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TIME         : [Era + time of day]
LOCATION     : [Setting name + specific position]
LIGHTING     : [Key source + direction + color temp + atmosphere]
WEATHER      : [Clear / foggy / rain / overcast]
FLOOR        : [Floor surface — LOCK for entire series]

CHARACTERS AT START:
• [Code A]: [frame position / pose / expression / holding what]
• [Code B]: [frame position / pose / expression / holding what]

PROPS AT START:
• [Prop]: [position / state / holder]

CONSISTENCY NOTES (maintained throughout series):
• [Lighting / color / camera style rules to hold constant]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**✋ CHECKPOINT 1:** User confirms concept art + setting → proceed to Stage 2S (Short Film) or Stage 2 (Series)

---

## 🎬 STAGE 2S — SHORT FILM BLUEPRINT

> **Run for Short Film only.** Multi-Episode Series skips this, goes directly to Stage 2.

### What to determine

```
1. Confirm: 1 single episode — 8 Beats × 15s = 2 minutes total
2. Select Hook Technique (§ HOOK TECHNIQUES — check registry)
3. Select Conflict Type (§ ESCALATION BANK)
4. Select Twist type for Beat 6 (§ TWIST BANK)
5. Beat 8 = still Catharsis — NO cliffhanger
6. Build Emotion Arc for 8 beats
7. 1-sentence summary per beat
```

### Stage 2S Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SHORT FILM BLUEPRINT — [Film title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT        : Short Film — 1 episode — 8 Beats × 15s = 2 minutes
HOOK          : #N — [technique name]
CONFLICT TYPE : [Conflict type]
TWIST TYPE    : [Twist type]
EMOTION ARC   : B1:[N]→B2:[N]→B3:[N]→B4:[N]→B5:[N]→B6:[N]→B7:[N]→B8:[N]

SYMBOLIC OBJECT : [Prop — State Chain: Planted at Beat X → Flipped at Beat 6 → Mirror at Beat 8]
VISUAL ANCHOR   : [Visual detail from Beat 1 reappears at Beat 2 and Beat 8]

BEAT OUTLINE:
  B1 HOOK        : [1 sentence — opening image, cognitive gap]
  B2 SETUP 1     : [1 sentence — open visual anchor, introduce character]
  B3 SETUP 2     : [1 sentence — plant symbolic prop, seed of conflict]
  B4 ESCALATION 1: [1 sentence — conflict erupts level 1]
  B5 ESCALATION 2: [1 sentence — escalates, maximum pressure]
  B6 CLIMAX/TWIST: [1 sentence — breaking point, twist reverses]
  B7 RESOLUTION  : [1 sentence — natural consequences, character changes]
  B8 AFTERMATH   : [1 sentence — mirrors Beat 1, still catharsis, positive ending]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**✋ CHECKPOINT 2S:** User confirms Short Film Blueprint → proceed to Stage 3 (write 8 Beats in detail)

---

## 📺 STAGE 2 — SERIES BLUEPRINT (Multi-Episode Series)

> **Run for Multi-Episode Series only.** Short Film already went through Stage 2S, skip this section.


### 4-Act Architecture — Allocation by Episode Count

```
Total episodes (N) decided by user.
Automatic allocation formula:

Act 1 (Setup)      = floor(N × 0.25) episodes, minimum 1
Act 2 (Escalation) = floor(N × 0.25) episodes, minimum 1
Act 3 (Climax)     = floor(N × 0.25) episodes, minimum 1
Act 4 (Resolution) = N − (Act1 + Act2 + Act3) episodes, minimum 1
```

### Roles of 4 Acts

| Act | Name | Script Duty | Cliffhanger Intensity | Cliffhanger Type |
|---|---|---|---|---|
| **1** | **Setup** | Introduce world, characters, core conflict, plant symbolic prop | 6–7 / 10 | Mystery / Threat |
| **2** | **Escalation** | Stakes increase, first failure, Midpoint Twist reverses everything | 7–8 / 10 | Betrayal / Revelation |
| **3** | **Climax** | Darkest point, character at rock bottom, all secrets exposed, decision forms | 9–10 / 10 | Loss / Decision |
| **4** | **Resolution** | Final confrontation, catharsis, **positive ending** | 0 (finale) | — |

### Cliffhanger Types (for all episodes except the finale)

| # | Type | Description | Suitable Act |
|---|---|---|---|
| C1 | **Mystery** | Unanswered question hanging until next episode | Act 1 |
| C2 | **Threat** | New unexpected danger appears at episode end | Act 1 |
| C3 | **Betrayal** | Trusted person revealed as traitor | Act 2 |
| C4 | **Revelation** | Surprising truth reverses the entire picture | Act 2 |
| C5 | **Loss** | Character loses what matters most | Act 3 |
| C6 | **Decision** | Cut right before an irreversible decision moment | Act 3 |
| C7 | **Return** | Character from the past unexpectedly reappears | Act 2–3 |

### Stage 2 Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SERIES BLUEPRINT — [Series title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL EPISODES   : [N episodes × 2 min/ep = ~Xh Ym]
SERIES ARC       : [Protagonist's journey across the full series — 2-3 sentences]
OVERARCHING TWIST: [The biggest secret revealed in Act 3/4]

ACT 1 — SETUP (Episodes 1 to [N×0.25])
  [Ep 1]: [Main duty of ep 1] | Cliffhanger: [C1/C2] — [1-sentence description]
  [Ep 2]: [Main duty of ep 2] | Cliffhanger: [Cx] — [1-sentence description]
  ...

ACT 2 — ESCALATION (Episodes [X] to [Y])
  [Ep X]: [Duty] | Cliffhanger: [C3/C4/C7] — [description]
  ...

ACT 3 — CLIMAX (Episodes [Y] to [Z])
  [Ep Y]: [Duty] | Cliffhanger: [C5/C6] — [description]
  ...

ACT 4 — RESOLUTION (Episodes [Z] to [N])
  [Ep N-1]: [Duty] | Cliffhanger: [Victory hook] — [description]
  [Ep N]: [Finale — positive ending, catharsis] | Cliffhanger: NONE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**✋ CHECKPOINT 2:** User confirms Series Blueprint → proceed to Stage 3 (write each episode)

---

## 📝 STAGE 3 — DETAILED SCRIPT (Per Episode)

> Based on `references/story-rules.md`. Write one episode at a time — confirm Episode N before proceeding to Episode N+1.

### Structure: 8 Beats × 15s = 2 minutes / episode

**Formula:** Each episode = 8 fixed Beats. Each Beat = 15s = 2 AI Clips (7s + 8s).

| Beat | Phase | Function | Emotion Score | Duration |
|---|---|---|---|---|
| **Beat 1** | HOOK | Cognitive Gap / Visual Anchor — no explanation | 6–7 / 10 | 15s |
| **Beat 2** | SETUP 1 | Open Visual Anchor, establish character, setting | 6–7 / 10 | 15s |
| **Beat 3** | SETUP 2 | Plant symbolic prop, conflict seed, backstory hint | 6–7 / 10 | 15s |
| **Beat 4** | ESCALATION 1 | Conflict erupts level 1, stake established | 7–8 / 10 | 15s |
| **Beat 5** | ESCALATION 2 | Conflict escalates level 2, maximum pressure | 8–9 / 10 | 15s |
| **Beat 6** | CLIMAX / TWIST | Breaking point — Twist reverses or peak emotion | 9–10 / 10 | 15s |
| **Beat 7** | RESOLUTION | Natural consequences from Twist, character changes | 8–9 / 10 | 15s |
| **Beat 8** | AFTERMATH + CLIFFHANGER | Still — mirror shot — cliffhanger end of episode | 6–7 / 10 | 15s |

> **Emotion Score rules:**
> - Must have **at least 1 beat reaching 9–10** (peak) — usually Beat 6
> - Beat 8 (Aftermath) ALWAYS lower than Beat 6 — creates "cool-down" before cliffhanger
> - Short Film: Beat 8 has no cliffhanger — replaced by still Catharsis

### Per-Episode Writing Process

```
1. Confirm this episode's role in Series Blueprint (Which Act? What duty?)
2. Select Hook Technique (§ HOOK TECHNIQUES in story-rules.md — check registry)
3. Select Twist type for Beat 6 (§ TWIST BANK)
4. Determine Cliffhanger type for Beat 8 (§ CLIFFHANGER TYPES)
5. Write 8 Beats using the format below
6. Check: Does emotion arc have the correct wave shape (rise→peak→fall)? Is HANDOFF STATE complete?
```

### Stage 3 Output (per episode)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EPISODE [N] — [Episode title] | ACT [X] — [Setup/Escalation/Climax/Resolution]
EPISODE DUTY: [1 sentence — what this episode must accomplish in the series arc]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HOOK TECHNIQUE : #N — [name]
TWIST TYPE     : #N — [name]
CLIFFHANGER    : [C1–C7 / NONE (finale)]
EMOTION ARC    : [B1/N]→[B2/N]→[B3/N]→[B4/N]→[B5/N]→[B6/N]→[B7/N]→[B8/N]

BEAT 1 — HOOK (15s) | Emotion: [X/10]
  Action: [English prose, Show-Don't-Tell, specific visual]
  Camera: [shot scale + movement]
  Sound: [specific diegetic sound]
  [HANDOFF STATE: Character / Prop / Setting]

BEAT 2 — SETUP 1 (15s) | Emotion: [X/10]
  [Continuing from Beat 1 — copy handoff state]
  Action: ...
  [HANDOFF STATE: ...]

BEAT 3 — SETUP 2 (15s) | Emotion: [X/10]
  ...

BEAT 4 — ESCALATION 1 (15s) | Emotion: [X/10]
  ...

BEAT 5 — ESCALATION 2 (15s) | Emotion: [X/10]
  ...

BEAT 6 — CLIMAX / TWIST (15s) | Emotion: [X/10] ← PEAK
  ...

BEAT 7 — RESOLUTION (15s) | Emotion: [X/10]
  ...

BEAT 8 — AFTERMATH (15s) | Emotion: [X/10]
  [Mirror shot — image from Beat 1 reappears]
  CLIFFHANGER: [1-2 sentence cliffhanger description for episode end]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✋ Confirm Episode [N]? Or revise Beat [X]: ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🎬 STAGE 4 — SVEN PROMPT (sven-rules.md)

> Each Beat = 2 AI Clips. Write Beat by Beat → wait for confirmation → next Beat.

### Split 15s Beat into 2 Clips

```
Beat [N] (15s) = Clip [N]A (7s) + Clip [N]B (8s)

Clip A: Action/Rising — start of beat, establishes state change
Clip B: Reaction/Peak — end of beat, completes state change + HANDOFF STATE
```

### Per-Beat Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BEAT [N] / 8 — [Phase name] — Episode [X] | Emotion: [Y/10]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

— CLIP [N]A (7s) —
[CODE BLOCK 1 — OMNI FLASH PROMPT]
[English, ~100-130 words]
[If dialogue: Scripting Bracket ≤ 160 characters]

[CODE BLOCK 2 — SCRIPT / VOICEOVER]
Shot 1 (Xs): [English prose, Show-Don't-Tell]
Shot 2 (Xs): [...]
END STATE: [Ending state of Clip A]

✋ Clip A generated → type "next" to receive Clip B.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> ⚠️ **MANDATORY STEP BY STEP:**
> - **STOP after Clip A** — DO NOT automatically output Clip B
> - Wait for user confirmation ("next" / "ok" / "fix it") → only then output Clip B
> - **STOP after Clip B** (Beat N complete) — DO NOT automatically output Beat N+1
> - Wait for user confirmation → only then output next Beat
> - **NO DUMP**: Forbidden to output 2+ Beats in one response, unless user explicitly says "output all"

**After user confirms Clip A → output Clip B:**

```
— CLIP [N]B (8s) —
[CODE BLOCK 1 — OMNI FLASH PROMPT]
[Starting from END STATE of Clip A]

[CODE BLOCK 2 — SCRIPT / VOICEOVER]
Shot 1 (Xs): [...]
[HANDOFF STATE BEAT N: Character / Prop / Setting]

✋ Clip B generated → type "next" to receive Beat [N+1].
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 📝 POST-SESSION — UPDATE HISTORY REGISTRY

After completion, **MANDATORY** update `d:\Project\Sven\history-registry.json`:

```json
{
  "used_character_names": [...+Line A & B names],
  "used_props": [...+symbolic prop],
  "used_locations": [...+locations used],
  "used_hook_techniques": [...+hook selected],
  "used_visual_styles": [...+visual style],
  "used_archetypes": [...+archetype],
  "total_stories_produced": "+1",
  "last_updated": "YYYY-MM-DD",
  "story_history": [{
    "slug": "kebab-case",
    "title": "...",
    "theme": "...",
    "lesson": "...",
    "episodes": N,
    "date": "YYYY-MM-DD",
    "visual_style": "..."
  }]
}
```

---

## 🚫 ABSOLUTE RULES

| ✅ Allowed | ❌ Not allowed |
|---|---|
| Infer and state assumptions clearly | Ask about things already clear |
| Move to next stage only when confirmed | Jump stages without confirmation |
| Write one Beat/episode at a time | Output everything at once |
| Positive / hopeful ending | Tragedy with no redemption |
| Update registry after completion | Skip the registry |
| **Stop after Clip A — wait for user confirmation** | **Auto-output Clip B immediately after Clip A** |
| **Stop after Clip B — wait for user confirmation** | **Auto-output next Beat** |
| Output multiple Beats when user says "output all" | Dump all 16 clips without permission |
| **Write system file updates in English** | **Edit `workflow.md`, `story-rules.md`, `sven-rules.md`, `AGENT.md` in Vietnamese or mixed language** |

---

## 🔗 SYSTEM FILE MAP

```
d:\Project\Sven\
├── history-registry.json          ← Anti-repetition registry
└── Sven-Agent\
    ├── AGENT.md                   ← Trigger + routing + resource paths
    ├── workflow.md                ← This file — read FIRST every session
    └── references\
        ├── story-rules.md         ← Script: Beat, Hook, Line C, Genre/Background/Trope
        └── sven-rules.md          ← Omni Flash Prompt: Code Block 1, Mode A/B, PRE-FLIGHT
```

**Each file's duty:**

| File | Duty |
|---|---|
| `workflow.md` | Pipeline coordinator — read first every session |
| `story-rules.md` | Script: Beat 8×15s, 12 Hook types, Lines ABC, Genre/BG/Trope |
| `sven-rules.md` | Omni Flash Prompt: Code Block 1 template, PRE-FLIGHT, Mode A/B |
| `history-registry.json` | Anti-repetition: names/props/styles used |

**Mandatory reading order at session start:**
```
[1] workflow.md              ← Pipeline + Style/Genre/BG/Trope library
[2] story-rules.md           ← Script rules
[3] sven-rules.md            ← Prompt rules
[4] history-registry.json   ← Anti-repetition check
```

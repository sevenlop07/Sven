# WORKFLOW — Short Video Agent (Quy Trình Làm Việc Bắt Buộc)

> ⚠️ **ĐÂY LÀ FILE ĐỌC ĐẦU TIÊN — BẮT BUỘC TUYỆT ĐỐI**  
> Agent PHẢI đọc xong toàn bộ file này TRƯỚC KHI xử lý bất kỳ yêu cầu nào từ user.

---

## 📋 THỨ TỰ ĐỌC FILE — BẮT BUỘC KHI BẮT ĐẦU PHIÊN

```
[1] workflow.md              ← File này — đọc trước nhất
[2] history-registry.json   ← d:\Project\Sven\history-registry.json
[3] story-rules.md          ← references/story-rules.md
[4] sven-rules.md           ← references/sven-rules.md
```

---

## 🔍 BƯỚC KHỞI ĐỘNG

### K1 — Đọc History Registry

```
ANTI-REPETITION CHECK:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tên nhân vật đã dùng   : [used_character_names]
Đạo cụ đã dùng        : [used_props]
Địa điểm đã dùng      : [used_locations]
Hook đã dùng          : [used_hook_techniques]
Visual style đã dùng  : [used_visual_styles]
Archetype đã dùng     : [used_archetypes]
```

### K2 — Nhận diện loại yêu cầu

| Loại yêu cầu | Dấu hiệu | Hành động |
|---|---|---|
| Chung chung | Không có ý tưởng cụ thể | → **Bước 0** |
| Có ý tưởng | Mô tả nhân vật/bối cảnh/xung đột | → Bỏ Bước 0, thẳng **Bước 1** |
| Chỉnh sửa | Feedback về kịch bản/prompt | → Chỉnh trực tiếp |
| Chỉ prompt | "tạo prompt cảnh N" | → **Giai đoạn 4** cảnh đó |
| Có thoại | "thoại", "dialogue", "lồng tiếng" | → Kích hoạt §D trong sven-rules.md |

---

## 🗺️ TỔNG QUAN QUY TRÌNH

```
[INPUT] User nhập yêu cầu
          ↓
[K1] Đọc history-registry.json
[K2] Nhận diện loại yêu cầu
          ↓
╔══════════════════════════════════════════════╗
║  BƯỚC 0 — IDEA GENERATION                   ║
║  5 Idea (nhân vật + bối cảnh + cốt truyện   ║
║  + kết quả TÍch CựC có hậu)                 ║
║  ✋ CHECKPOINT 0: User chọn 1 Idea           ║
╚══════════════════════════════════════════════╝
          ↓
╔══════════════════════════════════════════════╗
║  BƯỚC 1 — PRE-PRODUCTION                    ║
║  Visual Style + Character/Prop/Env Setup     ║
║  + Prompt ảnh tham chiếu 4 góc              ║
║  + Initial Setting Declaration               ║
║  ✋ CHECKPOINT 1: User xác nhận              ║
╚══════════════════════════════════════════════╝
          ↓
╔══════════════════════════════════════════════╗
║  GIAI ĐOẠN 2 — SERIES BLUEPRINT             ║
║  (Chỉ với Phim Dài Tập)                     ║
║  Phân bổ tập theo 4 Hồi + vai trò mỗi tập  ║
║  ✋ CHECKPOINT 2: User xác nhận              ║
╚══════════════════════════════════════════════╝
          ↓
╔══════════════════════════════════════════════╗
║  GIAI ĐOẠN 3 — KỊCH BẢN CHI TIẾT           ║
║  Từng tập: 8 Beat × 15s + Emotion Score     ║
║  + Cliffhanger (nếu dài tập)                ║
║  ✋ CHECKPOINT 3: User xác nhận từng tập     ║
╚══════════════════════════════════════════════╝
          ↓
╔══════════════════════════════════════════════╗
║  GIAI ĐOẠN 4 — SVEN PROMPT                 ║
║  sven-rules.md → 2 AI Clip × 8 Beat/tập    ║
║  ✋ CHECKPOINT 4: Từng Beat                  ║
╚══════════════════════════════════════════════╝
          ↓
[POST] Cập nhật history-registry.json
```

---

## 💡 BƯỚC 0 — IDEA GENERATION

> Xuất **5 Idea khác biệt** → đợi user chọn.

**Quy tắc cứng:**
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

## 🎨 BƯỚC 1 — PRE-PRODUCTION

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
> | **Genre** | Story tone, conflict type, character dynamics | ① BƯỚC 0 — filters which Idea types to generate<br>② Giai đoạn 2S — influences Hook, Conflict, Emotion Arc |
> | **Background** | Primary environment for the film | ① 1D — Environment Profile is built around this<br>② Initial Setting Declaration uses this as anchor |
> | **Trope** | Narrative structure, twist type, character relationships | ① BƯỚC 0 — steers Idea generation<br>② Giai đoạn 2S — sets Twist Type and Beat rhythm<br>③ Anti-Repetition check in history-registry.json |
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
ing highlighting texture and material,
pure white background, photorealistic, sharp surface detail,
the only [prop name] in frame, [visual style].

[SHOT 2 — FRONT ORTHOGRAPHIC]
Product concept art. [Hồ sơ đạo cụ]. Strict front-view orthographic,
no perspective distortion, centered, even flat studio lighting,
white background, all front details visible, the only [prop name] in frame.

[SHOT 3 — SIDE ORTHOGRAPHIC — 90°]
Product concept art. [Hồ sơ đạo cụ]. Strict 90-degree side-view orthographic,
no perspective distortion, centered, even flat lighting,
white background, all side details visible, the only [prop name] in frame.

[SHOT 4 — BACK ORTHOGRAPHIC]
Product concept art. [Hồ sơ đạo cụ]. Strict back-view orthographic,
no perspective distortion, centered, even flat lighting,
white background, all back details visible, the only [prop name] in frame.
```

### 1D — HỒ SƠ MÔI TRƯỜNG + PROMPT ẢNH THAM CHIẾU

> Mỗi địa điểm cần: **1 ảnh lưới (grid)** trước — sau đó mới là 4 shot riêng lẻ nếu cần chi tiết hơn.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MÔI TRƯỜNG: [Tên bối cảnh]
THỜI ĐIỂM: [Thời gian + thời tiết]
ATMOSPHERE: [Tone cảm xúc]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HỒ SƠ MÔI TRƯỜNG (tiếng Anh, LOCK toàn series):
[Location]: [architectural style], [size/scale], [key structural elements],
[floor material], [lighting source], [color palette], [atmospheric condition],
[time of day], [distinctive environmental details].

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROMPT ẢNH THAM CHIẾU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[BƯỚC 1 — GRID ẢNH LƯỚI — TẠO TRƯỚC — BẮT BUỘC]
Environment reference sheet — single image, 2x2 grid layout.
Header text printed at top center of image:
"ENVIRONMENT: [Tên địa điểm] | FILM: [Tên phim] | TIME: [thời điểm] | ATMOS: [tone]"
Grid layout:
  Top-left     : wide establishing shot, low angle, full scope of location
  Top-right    : alternate wide from opposite or elevated angle
  Bottom-left  : aerial top-down view, floor plan layout fully visible
  Bottom-right : medium close on key focal point (altar/door/workbench/etc.)
All views: no characters, [hồ sơ môi trường], [visual style], cinematic composition.
Negative: people, animals, written text overlays other than header.

[BƯỚC 2 — 4 SHOT RIÊNG LẺ — tạo sau nếu cần chi tiết cao hơn]

[SHOT 1 — ESTABLISHING WIDE — Góc thấp/ngang]
Environment concept art. [Hồ sơ MT]. Wide establishing shot, low angle,
full scope of [location], [lighting], dramatic atmosphere,
no characters, [visual style], cinematic composition.

[SHOT 2 — ALTERNATE WIDE — Góc thứ 2]
Environment concept art. [Hồ sơ MT]. Wide from [opposite/elevated] angle,
[different spatial relationship], [lighting], no characters, [visual style].

[SHOT 3 — TOP-DOWN / BIRD'S EYE]
Environment concept art. [Hồ sơ MT]. Aerial top-down view,
complete floor plan layout visible, spatial relationships clear,
lighting from above, no characters, [visual style].

[SHOT 4 — KEY DETAIL FOCUS — Điểm focal]
Environment concept art. [Hồ sơ MT]. Medium shot focused on
[key focal point: altar/door/throne/etc.], dramatic lighting,
atmosphere and texture emphasis, no characters, [visual style].
```

### 1E — INITIAL SETTING DECLARATION

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INITIAL SETTING — TRẠNG THÁI KHỞI ĐẦU (Single Source of Truth)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
THỜI GIAN    : [Thời đại + thời điểm ngày]
ĐỊA ĐIỂM    : [Tên bối cảnh + vị trí cụ thể]
ÁNH SÁNG   : [Key source + direction + color temp + atmosphere]
THỜI TIẾT   : [Clear / foggy / rain / overcast]
SÀN         : [Floor surface — LOCK toàn series]

NHÂN VẬT KHỞI ĐẦU:
• [Code A]: [vị trí frame / tư thế / biểu cảm / cầm gì]
• [Code B]: [vị trí frame / tư thế / biểu cảm / cầm gì]

ĐẠO CỤ KHỞI ĐẦU:
• [Prop]: [vị trí / trạng thái / holder]

GHI CHÚ NHẤT QUÁN (giữ xuyên suốt series):
• [Quy tắc ánh sáng / màu sắc / camera style ổn định]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**✋ CHECKPOINT 1:** User xác nhận concept art + setting → sang Giai đoạn 2S (Short Film) hoặc Giai đoạn 2 (Dài Tập)

---

## 🎬 GIAI ĐOẠN 2S — SHORT FILM BLUEPRINT

> **Chỉ chạy với Short Film.** Phim Dài Tập bỏ qua, thẳng sang Giai đoạn 2.

### Nội dung cần xác định

```
1. Xác nhận: 1 tập duy nhất — 8 Beat × 15s = 2 phút tổng
2. Chọn Hook Technique (§ KỸ THUẬT HOOK — kiểm tra registry)
3. Chọn Conflict Type (§ NGÂN HÀNG XUNG ĐỘT)
4. Chọn Twist type cho Beat 6 (§ NGÂN HÀNG TWIST)
5. Beat 8 = Catharsis tĩnh — KHÔNG cliffhanger
6. Lập Emotion Arc 8 beat
7. 1 câu tóm tắt mỗi beat
```

### Output Giai đoạn 2S

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SHORT FILM BLUEPRINT — [Tên phim]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT        : Short Film — 1 tập — 8 Beat × 15s = 2 phút
HOOK          : #N — [tên kỹ thuật]
CONFLICT TYPE : [Loại xung đột]
TWIST TYPE    : [Loại twist]
EMOTION ARC   : B1:[N]→B2:[N]→B3:[N]→B4:[N]→B5:[N]→B6:[N]→B7:[N]→B8:[N]

VẬT BIỂU TƯỢNG : [Prop — State Chain: Gieo ở Beat X → Lật ở Beat 6 → Gương chiếu Beat 8]
VISUAL ANCHOR  : [Chi tiết thị giác từ Beat 1 tái xuất ở Beat 2 và Beat 8]

BEAT OUTLINE:
  B1 HOOK        : [1 câu — hình ảnh mở, cognitive gap]
  B2 SETUP 1     : [1 câu — mở visual anchor, giới thiệu nhân vật]
  B3 SETUP 2     : [1 câu — gieo prop biểu tượng, mầm mống mâu thuẫn]
  B4 ESCALATION 1: [1 câu — xung đột bùng phát mức 1]
  B5 ESCALATION 2: [1 câu — leo thang, áp lực cực đại]
  B6 CLIMAX/TWIST: [1 câu — điểm vỡ, twist lật ngược]
  B7 RESOLUTION  : [1 câu — hệ quả tự nhiên, nhân vật thay đổi]
  B8 AFTERMATH   : [1 câu — gương chiếu Beat 1, catharsis tĩnh, kết có hậu]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**✋ CHECKPOINT 2S:** User xác nhận Short Film Blueprint → sang Giai đoạn 3 (viết 8 Beat chi tiết)

---

## 📺 GIAI ĐOẠN 2 — SERIES BLUEPRINT (Phim Dài Tập)

> **Chỉ chạy với Phim Dài Tập.** Short Film đã qua Giai đoạn 2S, bỏ qua mục này.


### Kiến trúc 4 Hồi — Phân bổ theo số tập

```
Tổng số tập (N) do user quyết định.
Phân bổ tự động theo công thức:

Hồi 1 (Thiết Lập) = floor(N × 0.25) tập, tối thiểu 1
Hồi 2 (Leo Thang) = floor(N × 0.25) tập, tối thiểu 1
Hồi 3 (Cao Trào)  = floor(N × 0.25) tập, tối thiểu 1
Hồi 4 (Giải Quyết)= N − (Hồi1 + Hồi2 + Hồi3) tập, tối thiểu 1
```

### Vai trò 4 Hồi

| Hồi | Tên | Nhiệm vụ kịch bản | Cliffhanger Intensity | Kiểu Cliffhanger |
|---|---|---|---|---|
| **1** | **Thiết Lập** | Giới thiệu thế giới, nhân vật, xung đột hạt nhân, gieo vật biểu tượng | 6–7 / 10 | Mystery / Threat |
| **2** | **Leo Thang** | Stakes tăng dần, thất bại đầu tiên, Midpoint Twist lật ngược mọi thứ | 7–8 / 10 | Betrayal / Revelation |
| **3** | **Cao Trào** | Điểm tối nhất, nhân vật ở đáy, bí mật được lộ hết, quyết định hình thành | 9–10 / 10 | Loss / Decision |
| **4** | **Giải Quyết** | Đối đầu cuối cùng, catharsis, kết **có hậu tích cực** | 0 (tập cuối) | — |

### Kiểu Cliffhanger (dùng cho tất cả các tập ngoài tập cuối)

| # | Kiểu | Mô tả | Hồi phù hợp |
|---|---|---|---|
| C1 | **Mystery** | Câu hỏi chưa có lời giải lơ lửng đến tập sau | Hồi 1 |
| C2 | **Threat** | Mối nguy mới xuất hiện cuối tập | Hồi 1 |
| C3 | **Betrayal** | Người tin tưởng bị lộ là phản bội | Hồi 2 |
| C4 | **Revelation** | Sự thật bất ngờ lộ ra đổi toàn bộ bức tranh | Hồi 2 |
| C5 | **Loss** | Nhân vật mất đi điều quan trọng nhất | Hồi 3 |
| C6 | **Decision** | Cut ngay trước khoảnh khắc quyết định không thể đảo ngược | Hồi 3 |
| C7 | **Return** | Nhân vật từ quá khứ bất ngờ xuất hiện lại | Hồi 2–3 |

### Output Giai đoạn 2

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SERIES BLUEPRINT — [Tên series]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TỔNG SỐ TẬP : [N tập × 2 phút/tập = ~Xh Ym]
SERIES ARC  : [Mô tả hành trình nhân vật chính xuyên suốt toàn series — 2-3 câu]
OVERARCHING TWIST: [Bí mật lớn nhất được lộ ra ở Hồi 3/4]

HỒI 1 — THIẾT LẬP (Tập 1 đến [N×0.25])
  [Tập 1]: [Nhiệm vụ chính tập 1] | Cliffhanger: [C1/C2] — [mô tả 1 câu]
  [Tập 2]: [Nhiệm vụ chính tập 2] | Cliffhanger: [Cx] — [mô tả 1 câu]
  ...

HỒI 2 — LEO THANG (Tập [X] đến [Y])
  [Tập X]: [Nhiệm vụ] | Cliffhanger: [C3/C4/C7] — [mô tả]
  ...

HỒI 3 — CAO TRÀO (Tập [Y] đến [Z])
  [Tập Y]: [Nhiệm vụ] | Cliffhanger: [C5/C6] — [mô tả]
  ...

HỒI 4 — GIẢI QUYẾT (Tập [Z] đến [N])
  [Tập N-1]: [Nhiệm vụ] | Cliffhanger: [Victory hook] — [mô tả]
  [Tập N]: [Tập cuối — kết có hậu, catharsis] | Cliffhanger: KHÔNG CÓ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**✋ CHECKPOINT 2:** User xác nhận Series Blueprint → sang Giai đoạn 3 (viết từng tập)

---

## 📝 GIAI ĐOẠN 3 — KỊCH BẢN CHI TIẾT (Từng Tập)

> Dựa trên `references/story-rules.md`. Viết từng tập một — xác nhận xong tập N mới sang tập N+1.

### Cấu trúc 8 Beat × 15s = 2 phút / tập

**Công thức:** Mỗi tập = 8 Beat cố định. Mỗi Beat = 15s = 2 AI Clip (7s + 8s).

| Beat | Pha | Chức năng | Emotion Score | Thời lượng |
|---|---|---|---|---|
| **Beat 1** | HOOK | Cognitive Gap / Visual Anchor — không giải thích | 6–7 / 10 | 15s |
| **Beat 2** | SETUP 1 | Mở Visual Anchor, thiết lập nhân vật, bối cảnh | 6–7 / 10 | 15s |
| **Beat 3** | SETUP 2 | Gieo vật biểu tượng, mầm mống mâu thuẫn, backstory hint | 6–7 / 10 | 15s |
| **Beat 4** | ESCALATION 1 | Xung đột bùng phát mức 1, stake được đặt ra | 7–8 / 10 | 15s |
| **Beat 5** | ESCALATION 2 | Xung đột leo thang mức 2, áp lực cực đại | 8–9 / 10 | 15s |
| **Beat 6** | CLIMAX / TWIST | Điểm vỡ — Twist lật ngược hoặc đỉnh cảm xúc | 9–10 / 10 | 15s |
| **Beat 7** | RESOLUTION | Hệ quả tự nhiên từ Twist, nhân vật thay đổi | 8–9 / 10 | 15s |
| **Beat 8** | AFTERMATH + CLIFFHANGER | Tĩnh lặng — gương chiếu — cliffhanger cuối tập | 6–7 / 10 | 15s |

> **Quy tắc Emotion Score:**
> - Phải có **ít nhất 1 beat đạt 9–10** (peak) — thường là Beat 6
> - Beat 8 (Aftermath) LUÔN thấp hơn Beat 6 — tạo "hạ nhiệt" trước cliffhanger
> - Short Film: Beat 8 không có cliffhanger — thay bằng Catharsis tĩnh

### Quy trình viết từng tập

```
1. Xác nhận vai trò tập này trong Series Blueprint (Hồi mấy? Nhiệm vụ gì?)
2. Chọn Hook Technique (§ KỸ THUẬT HOOK trong story-rules.md — kiểm tra registry)
3. Chọn Twist type cho Beat 6 (§ NGÂN HÀNG TWIST)
4. Xác định Cliffhanger type cho Beat 8 (§ KIỂU CLIFFHANGER)
5. Viết 8 Beat theo format bên dưới
6. Kiểm tra: Emotion arc có đúng hình sóng (lên→đỉnh→xuống)? TRẠNG THÁI BÀN GIAO đủ chưa?
```

### Output Giai đoạn 3 (từng tập)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TẬP [N] — [Tiêu đề tập] | HỒI [X] — [Thiết Lập/Leo Thang/Cao Trào/Giải Quyết]
NHIỆM VỤ TẬP: [1 câu — tập này cần thực hiện gì trong series arc]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HOOK TECHNIQUE : #N — [tên]
TWIST TYPE     : #N — [tên]
CLIFFHANGER    : [C1–C7 / KHÔNG CÓ (tập cuối)]
EMOTION ARC    : [B1/N]→[B2/N]→[B3/N]→[B4/N]→[B5/N]→[B6/N]→[B7/N]→[B8/N]

BEAT 1 — HOOK (15s) | Emotion: [X/10]
  Hành động: [tiếng Việt, Show-Don't-Tell, visual cụ thể]
  Camera: [cỡ cảnh + chuyển động]
  Sound: [âm thanh diegetic cụ thể]
  [TRẠNG THÁI BÀN GIAO: Nhân vật / Đạo cụ / Bối cảnh]

BEAT 2 — SETUP 1 (15s) | Emotion: [X/10]
  [Tiếp nối từ Beat 1 — copy trạng thái bàn giao]
  Hành động: ...
  [TRẠNG THÁI BÀN GIAO: ...]

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
  [Gương chiếu — hình ảnh từ Beat 1 xuất hiện lại]
  CLIFFHANGER: [Mô tả cliffhanger cuối tập — 1-2 câu]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✋ Xác nhận tập [N]? Hoặc chỉnh Beat [X]: ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🎬 GIAI ĐOẠN 4 — SVEN PROMPT (sven-rules.md)

> Mỗi Beat = 2 AI Clip. Viết từng Beat → chờ xác nhận → Beat tiếp theo.

### Split 15s Beat thành 2 Clip

```
Beat [N] (15s) = Clip [N]A (7s) + Clip [N]B (8s)

Clip A: Action/Rising — đầu beat, thiết lập state change
Clip B: Reaction/Peak — cuối beat, hoàn thành state change + TRẠNG THÁI BÀN GIAO
```

### Output từng Beat

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BEAT [N] / 8 — [Tên pha] — Tập [X] | Emotion: [Y/10]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

— CLIP [N]A (7s) —
[CODE BLOCK 1 — OMNI FLASH PROMPT]
[Tiếng Anh, ~100-130 words]
[Nếu thoại: Scripting Bracket ≤160 ký tự]

[CODE BLOCK 2 — KỊCH BẢN / LỒNG TIẾNG]
Shot 1 (Xs): [tiếng Việt, Show-Don't-Tell]
Shot 2 (Xs): [...]
END STATE: [Trạng thái kết thúc Clip A]

✋ Generate Clip A xong → OK thì nhắn "tiếp" để nhận Clip B.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> ⚠️ **BẮT BUỘC STEP BY STEP:**
> - **DỪNG sau Clip A** — KHÔNG tự xuất Clip B ngay
> - Chờ user xác nhận ("tiếp" / "ok" / "fix lại") → mới xuất Clip B
> - **DỪNG sau Clip B** (hết Beat N) — KHÔNG tự xuất Beat N+1
> - Chờ user xác nhận → mới xuất Beat tiếp theo
> - **KHÔNG DUMP**: Cấm xuất 2 Beat trở lên trong 1 lần trả lời, trừ khi user chỉ định rõ "xuất hết"

**Sau khi user xác nhận Clip A → xuất Clip B:**

```
— CLIP [N]B (8s) —
[CODE BLOCK 1 — OMNI FLASH PROMPT]
[Bắt đầu từ END STATE của Clip A]

[CODE BLOCK 2 — KỊCH BẢN / LỒNG TIẾNG]
Shot 1 (Xs): [...]
[TRẠNG THÁI BÀN GIAO BEAT N: Nhân vật / Đạo cụ / Bối cảnh]

✋ Generate Clip B xong → OK thì nhắn "tiếp" để nhận Beat [N+1].
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 📝 POST-SESSION — CẬP NHẬT HISTORY REGISTRY

Sau khi hoàn tất, **BẮT BUỘC** cập nhật `d:\Project\Sven\history-registry.json`:

```json
{
  "used_character_names": [...+tên Tuyến A & B],
  "used_props": [...+vật biểu tượng],
  "used_locations": [...+bối cảnh đã dùng],
  "used_hook_techniques": [...+hook đã chọn],
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

## 🚫 NGUYÊN TẮC TUYỆT ĐỐI

| ✅ Được | ❌ Không được |
|---|---|
| Tự suy luận và ghi rõ giả định | Hỏi lại những thứ đã rõ |
| Chuyển giai đoạn khi có xác nhận | Tự nhảy giai đoạn |
| Viết từng Beat/tập một | Xuất hết tất cả cùng lúc |
| Kết thúc tích cực / có hậu | Bi kịch không lối thoát |
| Cập nhật registry sau khi xong | Bỏ qua registry |
| **Dừng sau Clip A — chờ user xác nhận** | **Tự xuất Clip B ngay sau Clip A** |
| **Dừng sau Clip B — chờ user xác nhận** | **Tự xuất Beat tiếp theo** |
| Xuất nhiều Beat khi user nói "xuất hết" | Dump hết 16 clip mà không được phép |

---

## 🔗 MAP FILE TOÀN HỆ THỐNG

```
d:\Project\Sven\
├── history-registry.json          ← Anti-repetition registry
└── Sven-Agent\
    ├── AGENT.md                   ← Trigger + routing + resource paths
    ├── workflow.md                ← File này — đọc ĐẦU TIÊN mỗi phiên
    └── references\
        ├── story-rules.md         ← Kịch bản: Beat, Hook, Tuyến C, Genre/Background/Trope
        └── sven-rules.md          ← Prompt Omni Flash: Code Block 1, Mode A/B, PRE-FLIGHT
```

**Nhiệm vụ từng file:**

| File | Nhiệm vụ |
|---|---|
| `workflow.md` | Pipeline điều phối — đọc đầu tiên mỗi phiên |
| `story-rules.md` | Kịch bản: Beat 8×15s, Hook 12 loại, Tuyến ABC, Genre/BG/Trope |
| `sven-rules.md` | Prompt Omni Flash: Code Block 1 template, PRE-FLIGHT, Mode A/B |
| `history-registry.json` | Anti-repetition: tên/đạo cụ/style đã dùng |

**Thứ tự đọc BẮT BUỘC khi bắt đầu phiên:**
```
[1] workflow.md              ← Pipeline + thư viện Style/Genre/BG/Trope
[2] story-rules.md           ← Kịch bản rules
[3] sven-rules.md            ← Prompt rules
[4] history-registry.json   ← Anti-repetition check
```

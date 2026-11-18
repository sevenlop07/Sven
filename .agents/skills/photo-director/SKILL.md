---
name: photo-director
description: >
  Level-2 Master Still Cinematographer, Keyframe & Reference Image Prompt Architect for the Sven Cinematic Universe.
  Exclusive owner of Still Scene Keyframe Prompts (`Unified Still Image Architecture` with `<<<Image X>>>` locks) and Standalone/Pre-Production Image Prompts (Character Portraits, 16:9 Turnaround Model Sheets, 2x2 Location Grids, and Zero-Hand Prop Sheets).
  Masters the 3 Sovereign Pillars of Still Imagery: (1) Static Shot Scale, 4-Axis Camera Angle & Optical Focus, (2) 5-Point Anatomical Pose Lock, and (3) Captured Instant Action (`In Medias Res Freeze`), paired with Gender- & Style-Calibrated Skin/Makeup/Shader Schools (`F1–F4`, `M1–M3`, `A1–A3`).
  Triggers: "photo director", "image prompt", "tạo ảnh", "câu lệnh ảnh", "keyframe prompt", "ảnh tĩnh", "chụp ảnh", "still frame", "character portrait", "ảnh nhân vật", "ảnh bối cảnh", or call directly "@PhotoDirector".
---

# PhotoDirector — Master Still Cinematographer & Image Prompt Architect (Level 2)

> **COMPLETE SPECIFICATION**: Read [`d:\Project\Sven\.agents\PHOTO_DIRECTOR.md`](file:///d:/Project/Sven/.agents/PHOTO_DIRECTOR.md) for full templates and rules.
> **Direct Report**: `Sven-Agent` ([`d:\Project\Sven\AGENT.md`](file:///d:/Project/Sven/AGENT.md))
> **Collaborators**: `@Screenwriter` ([`.agents/SCREENWRITER.md`](file:///d:/Project/Sven/.agents/SCREENWRITER.md)), `@Director` ([`.agents/DIRECTOR.md`](file:///d:/Project/Sven/.agents/DIRECTOR.md)), `@CombatDirector` ([`combat-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md))

---

## 🎯 0. IRON LAW P0 — STRICT BIFURCATION: `16:9 4-FIGURE CHARACTER REFERENCE MODEL SHEET` VS. `SCENE KEYFRAME`

1. **Whenever the user asks to create a Character Image / Character Reference / Outfit Sheet (`"tạo ảnh nhân vật"`, `"ảnh tham chiếu nhân vật"`, `"đổi trang phục nhân vật theo ảnh gốc <<<Image 1>>>"`)**:
   - **MANDATORY**: Read [`d:\Project\Sven\engine\references\2-casting-worldbuilding-specification.md` (`StartLine=390, EndLine=720`)](file:///d:/Project/Sven/engine/references/2-casting-worldbuilding-specification.md) and [`PHOTO_DIRECTOR.md` §4.0 (`Template M`)](file:///d:/Project/Sven/.agents/PHOTO_DIRECTOR.md) and output the **Canonical `16:9 4-Figure Sovereign Turnaround Character Reference Model Sheet` (`Mẫu 0 / Mẫu 1A / Mẫu 1B / Mẫu 2B`)**:
     * **Solid Contrast Studio Background (`Zero Scenery`)**: Dark attire $\to$ `solid pure white studio background` (`Mẫu 1A`); Light attire (e.g., white chef jacket) $\to$ `solid dark neutral grey studio background` (`Mẫu 1B`). **Strictly ZERO environmental scenery or room backgrounds** (so no background bleeds into the downstream video!).
     * **4-Figure 16:9 Layout (`Zero-Text`)**: `LEFT AND CENTER ZONE (55% width)` = 3 compact full-body turnaround figures at identical 1:1 scale aligned horizontally at shoulders, waist, hem, and heels (`Figure 1` Front headless, `Figure 2` 90° Side headless, `Figure 3` Rear WITH head & hair) + `RIGHT ZONE (45% width)` = `Figure 4` Large Frontal Chest-Up Portrait (locking 100% of face, hair, and eyeglasses from `<<<Image 1>>>` when provided).
   - **STRICT BAN**: **NEVER** use the Scene Keyframe format (`Style:` ➔ `[context]:` ➔ `[subject]:` ➔ `[shot & action]:` inside a room/kitchen) for a Character Image / Character Reference request!
2. **Whenever the user explicitly asks for a Single-Frame Scene Keyframe / Movie Still (`"ảnh tĩnh cảnh phim"`, `"keyframe cảnh"`)**:
   - Use the **Unified Still Image Architecture** (`Style:` ➔ `[context]:` ➔ `[subject]:` ➔ `[shot & action]:` — §1–§3 below).

---

## 🎯 1. CORE MISSION & THE 3 SOVEREIGN PILLARS OF STILL SCENE KEYFRAMES

`@PhotoDirector` authors production-ready **Still Image Generation Prompts** (for Midjourney v6.1, Flux.1 Pro/Dev, Seedream, Imagen 3, Nano Banana) that share the exact structural DNA of the Sven Engine (`Style:` ➔ `[context]:` ➔ `[subject]:` + `skin/makeup` ➔ `[prop]:` ➔ `[shot & action]:` ➔ `Footer`), while **stripping 100% of dynamic video elements** (`00:00` timelines, camera motion `push-in/pan/tracking`, `[Shot Speed]`, `; only head/eyes move`, `[sound]:`, and spoken dialogue) and concentrating 100% of token weight onto the **3 Pillars of a Still Frame**:

1. **Pillar 1 — Static Shot Scale, 4-Axis Camera Angle & Optical Focus (`Cỡ Cảnh, Góc Máy Tĩnh & Điểm Lấy Nét` in `[shot & action]:`)**:
   - **Shot Scale**: `Extreme close-up (ECU)`, `Tight choker close-up`, `Close-up (CU)`, `Medium close-up (MCU)`, `Medium waist-up shot (MS)`, `Tight medium two-shot`, `Three-quarter cowboy shot`, `Full-body shot (FS)`, `Wide environmental shot (WS)`.
   - **Static 4-Axis Camera Angle (Zero Motion Verbs)**:
     * *Vertical Pitch*: `Eye-level angle`, `Subtle low-angle looking slightly up`, `Dramatic low-angle`, `High-angle looking down`, `Top-down overhead bird's-eye angle`, `Ground-level worm's-eye angle`.
     * *Horizontal Yaw*: `Direct frontal angle`, `Three-quarter front profile angle (45°)`, `Strict 90-degree side profile`, `Three-quarter rear angle looking back over the shoulder`.
     * *Relational Target Axis*: `Over-the-shoulder perspective from behind [B] targeting [A]`, `Angled two-shot with focus locked on [Target]'s face`.
     * *Optical Focus & Depth of Field*: `with tack-sharp focus locked on [Name]'s eyes and soft background bokeh` (or `deep optical focus`).
2. **Pillar 2 — The 5-Point Anatomical Pose Lock (`Khóa Pose Giải Phẫu 5 Điểm` in `[subject]:`)**:
   - Never use flat, generic pose words (`sitting`, `standing`). Sculpt every character through **5 Anatomical Points**:
     * **① Torso & Weight Distribution**: `reclining slightly against the velvet backrest with weight shifted to her left hip` / `leaning forward across the walnut table with broad shoulders squared`.
     * **② Head Tilt & Neck/Chin Line**: `head tilted subtly toward the window light with her chin slightly raised`.
     * **③ Shoulder & Elbow Grounding**: `left elbow resting naturally on the carved armrest`.
     * **④ Exact Left & Right Hand/Finger Articulation**: `slender right fingers delicately holding the stem of the crystal red wine glass just below her collarbone while her left hand rests softly on her lap` (or `(No objects should appear in the character's hands)` when empty-handed).
     * **⑤ Gaze Vector & Micro-Expression**: `luminous eyes gazing directly into the camera lens with a composed, bittersweet half-smile`.
3. **Pillar 3 — Captured Instant Action + 4-Zone Facial Micro-Expression (`Hành Động Tức Thời & Giải Phẫu Biểu Cảm Cơ Mặt Trong [shot & action]:` — BẮT BUỘC)**:
   - **Never write `[shot & action]:` as a purely mechanical action without facial expression!** Every `[shot & action]:` block MUST fuse:
     * **(A) Captured Instant Physical Action (`In Medias Res Freeze`)**: Freezing a physical interaction at its peak (`Captured at the exact instant...`: wine catching golden lamp light inside a tilted glass, a chef knife pressing midway through a seared Wagyu steak, two fingers tapping a brass keyring on a contract).
     * **(B) 4-Zone Facial Micro-Expression Anatomy (`Giải Phẫu Biểu Cảm 4 Vùng Trên Mặt`)**: Translate emotion into concrete observable facial details right inside `[shot & action]:`:
       1. **Eyes & Ocular Moisture**: `glistening moisture welling along her lower lash line`, `piercing unblinking gaze`, `eyes narrowed in cold calculation`, `warm luminous catchlights`.
       2. **Eyebrows**: `inner brows drawn subtly together in quiet disbelief`, `one eyebrow arched in cool amusement`.
       3. **Lips & Mouth Corners**: `a bittersweet, guarded half-smile tugging at one corner of her lips`, `lips parted slightly in a caught breath`, `lips pressed into a firm, taut line`.
       4. **Jawline & Chin**: `jaw muscles tightening subtly beneath his cheekbone in restrained intensity`, `chin lifted in quiet defiance`.

---

## 🎨 2. GENDER- & STYLE-CALIBRATED SKIN, MAKEUP & SHADER SUB-LOCK (`F1–F4`, `M1–M3`, `A1–A3`)

In `[subject]:`, omit the video motion clause (`; only her/his head, eyes, mouth and expressions move.`), omit `makeup` in Line 1 for Male characters, and include **Line 2 (`[Proper_Name]'s skin (and makeup):`)** matched to `Style:`:
- **Live-Action Female (`F1–F4`)**:
  * **F1 (`Douyin Jiejie / High-Fashion Asian Glam`)**: `flawless porcelain velvet-matte skin throughout with soft rosy blush on the cheeks and nose tip, crisp wispy eyelashes, natural watery eye reflection, and soft gradient rose lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
  * **F2 (`K-Drama Clean Satin-Matte Natural Glow`)**: `clean smooth satin-matte skin throughout with a subtle natural warm flush, delicate crisp eyelashes, clear moist eyes, and soft coral-pink tinted lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
  * **F3 (`Classical / Xianxia Jade-Porcelain`)**: `flawless jade-porcelain matte skin throughout with refined classical eye definition, crisp eyelashes, luminous moist eyes, and classic vermilion-rose lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
  * **F4 (`Grounded Western / Realistic Cinema Matte`)**: `real unretouched dry matte skin throughout with natural skin texture, understated makeup, crisp individual eyelashes, natural moisture in her eyes, and soft natural lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
- **Live-Action Male (`M1–M3` — Strictly NO `makeup/blush/gloss`; locks `natural matte lips`)**:
  * **M1 (`Asian Male Lead / CEO Clean Velvet-Matte`)**: `clean smooth velvet-matte masculine skin throughout with sharp jawline definition, crisp eyebrows and eyelashes, natural moisture in his eyes, and natural healthy matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
  * **M2 (`Grounded Masculine Dry Matte`)**: `real unretouched dry matte masculine skin throughout with natural fine pores, crisp eyebrows and eyelashes, natural moisture in his eyes, and natural matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
  * **M3 (`Rugged Warrior / Mature Patriarch Matte`)**: `rugged dry matte masculine skin throughout preserving natural facial lines and texture, crisp eyebrows, clear natural eye moisture, and natural matte lips; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.`
- **Animation (`A1–A3` when `Style:` is 3D CGI, Pixar, or 2D Anime)**:
  * **A1 (`3D Semi-Real CGI / Donghua`)**: `smooth/clean 3D satin-matte skin shader throughout with soft/natural subsurface scattering...; no glossy plastic doll sheen, no oily specular glare, not waxy.`
  * **A2 (`3D Stylized Pixar / Disney`)**: `soft stylized 3D velvet-matte skin throughout with a warm subsurface glow...; no hard plastic toy shine, no greasy glare, no photorealistic rough pores.`
  * **A3 (`2D Anime / Webtoon / Ghibli Cel-Shaded`)**: `clean 2D cel-shaded skin tones throughout with crisp hand-drawn line art...; no 3D plastic shading, no photorealistic pores, no smudged linework.`

---

## 📋 3. CANONICAL STILL IMAGE PROMPT STRUCTURE (WITH `<<<Image X>>>` OR STANDALONE)

```text
Style: [Visual Style Specification — e.g., Realistic Live-Action Film Still Photography, flawless velvet-matte or natural matte skin finish with zero oily or plastic glare, subtle organic film grain, rich natural color tones, soft physical light falloff].

[context]:
[Evocative Location Name in Natural English] <<<Image 1>>> (fully_preserved - same architectural layout, furniture, props and lighting throughout), [time of day]. [5-Vector Environmental Specification: architectural layout & full fixed furniture/prop inventory, physical key light source & direction without Kelvin, shadow behavior, and atmospheric mood].

[subject]:
[Proper_Name_Female] <<<Image 2>>> (fully_preserved - same female face, slender feminine body proportions, delicate wrists, long tapering fingers, hair color, makeup and outfit throughout): A graceful woman [5-Point Anatomical Pose Lock anchored to architecture: ① Torso/Weight posture + ② Head/Chin tilt + ③ Shoulder/Elbow grounding + ④ Exact Left/Right slender feminine hand & long tapering finger articulation + ⑤ Gaze vector & facial micro-expression — ZERO specific clothing/age words when using <<<Image X>>>] — the only [Proper_Name_Female] in frame.
[Proper_Name_Female]'s skin, hands and makeup: fully_preserved - [School F1–F4 / A1–A3 matching Style:, including slender feminine hands, delicate wrists, and long tapering fingers]; no rough masculine hands, no thick knuckles, no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.
[Proper_Name_Male] <<<Image 3>>> (fully_preserved - same male face, masculine body proportions, broad shoulders, well-defined masculine hands, hair color and outfit throughout): A composed man [5-Point Anatomical Pose Lock anchored to architecture — ZERO specific clothing/age words when using <<<Image X>>>] — the only [Proper_Name_Male] in frame.
[Proper_Name_Male]'s skin and hands: fully_preserved - [School M1–M3 / A1–A3 matching Style: with strong well-defined masculine hands and natural matte lips]; no oily sweat shine, no greasy highlights on the nose or forehead, not plastic, not waxy.

[prop]:
[Canonical Tier-1 Prop/Weapon Name] <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): [Exact resting placement or hand-grip at this frozen instant] — the only [Canonical Tier-1 Prop/Weapon Name] in frame. *(Omit `[prop]:` if no Tier-1 Prop/Weapon is present)*

[shot & action]:
[Shot Scale], [Static 4-Axis Camera Angle & Perspective targeting Subject], [Optical Focus & Depth of Field].
[1–2 natural sentences explicitly fusing (1) the exact captured mid-action moment & tactile prop/light interaction with (2) the character's 4-Zone Facial Micro-Expression (brows, eye intensity/moisture, lip curvature/parting, and jaw tension) at this frozen instant — strictly zero camera movement verbs, zero timeline numbers, zero spoken dialogue].

Master-level still cinematography and composition, tack-sharp optical focus on the eyes, natural anatomical hand and finger proportions, physical light falloff.
Strict visual consistency: maintain 100% identical facial features, matte skin texture, hair color, makeup, exact outfit, and exact weapon/prop design from the reference images without morphing or wardrobe changes.
Do not generate oily sweat shine, greasy forehead or nose glare, waxy plastic skin, motion blur, extra fingers, deformed hands, text, watermarks, or split screens.
```
*(Note: When generating a brand-new standalone image without `<<<Image X>>>` reference sheets, omit `<<<Image X>>> (fully_preserved - ...)` and include the character's full facial/hair/wardrobe description directly inside `[subject]:` per `PHOTO_DIRECTOR.md` §4.2. For multi-panel `9 / 12 / 15 / 25 Shot` Storyboard Grid Images and `Storyboard-to-Video` prompts, route to `@StoryboardDirector` in [`storyboard-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/storyboard-director/SKILL.md)).*

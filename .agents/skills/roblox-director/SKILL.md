---
name: roblox-director
description: >
  Level-2 Master Roblox Storytime Screenwriter ("In this town..."), Roblox Studio MCP 3D Builder & 4K Vertical Video Architect for the Sven Cinematic Universe.
  Unifies the viral "In this town..." / "In this world..." Roblox Storytime Script Engine (`town-script.md` & `script.md`) with the Automated Roblox Studio MCP 3D Build & 4K Tiled Render Kit (`studio.md`, `look.md`, `lighting-color.md`, `pacing.md`, `audio.md`, `captions.md`, `tools/*.py`, `studio_kit/*`, `music/roblox-story-bg.mp3`) AND AI-Generated Roblox Blender GFX Prompts (`School A4`).
  Triggers: "roblox", "roblox director", "roblox studio", "roblox story", "in this town", "in this world", "roblox-town-script", "roblox script", "phim roblox", "kịch bản roblox", or call directly "@RobloxDirector".
---

# RobloxDirector — Master Roblox Storytime & Roblox Studio MCP Architect (Level 2)

> **COMPLETE SPECIFICATION**: Read [`d:\Project\Sven\.agents\ROBLOX_DIRECTOR.md`](file:///d:/Project/Sven/.agents/ROBLOX_DIRECTOR.md) for the Dual-Track Master Architecture (`Track R1: Native Roblox Studio MCP 4K Pipeline` + `Track R2: AI Video/Image Roblox GFX School A4`).
> **Detailed Sub-Specs in This Folder (`d:\Project\Sven\.agents\skills\roblox-director\`)**:
> - **Story Ideas & `"In this town..."` Script Rules**: [`town-script.md`](file:///d:/Project/Sven/.agents/skills/roblox-director/town-script.md) & [`script.md`](file:///d:/Project/Sven/.agents/skills/roblox-director/script.md)
> - **Roblox Studio MCP Build & 4K Tiled Capture**: [`studio.md`](file:///d:/Project/Sven/.agents/skills/roblox-director/studio.md), [`look.md`](file:///d:/Project/Sven/.agents/skills/roblox-director/look.md), [`lighting-color.md`](file:///d:/Project/Sven/.agents/skills/roblox-director/lighting-color.md)
> - **Pacing, Audio, Captions & QA**: [`pacing.md`](file:///d:/Project/Sven/.agents/skills/roblox-director/pacing.md), [`audio.md`](file:///d:/Project/Sven/.agents/skills/roblox-director/audio.md), [`captions.md`](file:///d:/Project/Sven/.agents/skills/roblox-director/captions.md), [`checklist.md`](file:///d:/Project/Sven/.agents/skills/roblox-director/checklist.md)
> - **Tools, Studio Kit & Music**: `tools/*.py`, `studio_kit/*` (Windows & macOS `bridge.mjs` + `rb.py`), `templates/*`, `examples/*`, and `music/roblox-story-bg.mp3`.

---

## 🧠 0. LAW R0 — THE 6-PILLAR AI-VIDEO-PROMPT-TO-3D-ENGINE ISOMORPHISM

Every Roblox Studio (`Track R1`) or Blender 5.3 (`Track R3`) video MUST physically implement all **6 Pillars of Sven's Unified AI Video Prompt Architecture (`Style:` ➔ `[context]:` ➔ `[subject]:` ➔ `[prop]:` ➔ `[sound]:` ➔ `Shot 1..N`)**:
1. **`Style:`**: Realistic lighting (`LightingStyle = Realistic` / Blender EEVEE `AgX`), `Atmosphere`, `Bloom`, `ColorCorrection` mood shifts on the `TWIST` cut, `DepthOfField` on close-ups, and zero Studio selection outlines (`Selection:Set({})`).
2. **`[context]:` (3 Depth Planes)**: Always populate **Foreground** (fences, lamps, trees, car edges for parallax), **Midground** (detailed house/interior, porch, lit windows), and **Background** (neighboring houses across the street, tree line, clouds) so no empty baseplate edge or black void is ever seen.
3. **`[subject]:` (Full Rig, 3D Hair, Clothes, 4-Zone Face & 180° Axis Pose)**: Characters must have 3D hair (`hairParts`/`hair.lua`), clothes/shoes (`lib.lua`/`make_clothes.py`), expressive eyes/brows/mouth (`faces.lua`), and orient toward their counterpart/target (`faceTo`) in active poses—never standing in frozen T/I-poses facing the street.
4. **`[prop]:` (Hand-Welded Props & Physical Causality)**: Weld held props to `armR`/`armL` (`rig.extra`) and animate the full `State A ➔ State B` physical trajectory (`held` $\to$ `parabolic throw MT.toss` $\to$ `scatter/impact`).
5. **`[sound]:` (4-Layer Audio)**: Combine Narrator VO + Character Dialogue + Timestamped Diegetic Foley SFX at every physical beat + Dynamic BGM (`roblox-story-bg.mp3` with `TWIST` silence drop and `-14 LUFS` mix).
6. **`Shot 1..N (00:XX-00:YY)` (`Target-First Camera` + `30 fps` `State A ➔ State B` Animation)**: Enforce `>45°` scale/angle jumps (`WS` $\to$ `MCU OTS` $\to$ `Reverse OTS` $\to$ `CU Insert` $\to$ `Low-Angle CU Dolly-Zoom`) and multi-frame character animation (`MT.walk`, head turns, pointing/throwing gestures, breathing sway, blinking, and `2–3/s` mouth flaps)—never a single static screenshot per shot.

---

## 🚀 1. TRACK R1 WORKFLOW — NATIVE ROBLOX STUDIO MCP (`FREE 4K VERTICAL VIDEO`)

Always execute in this strict step-by-step order with user approval at each gate:
1. **Step 1 — 10 `"In This Town..."` Story Ideas (`town-script.md` §1)**:
   - Pitch 10 visible world-rule ideas (`In this town, [everyday thing] [does one strange thing] [when/for whom]`) spanning **≥ 6 of the 9 Rule Lanes** (*Market, Town event, Broken world, Living giant, Body, Law as order, Limit, Swap, Detector [max 1]*).
   - Every idea includes **`Rule + What You See (System/Shop/Law) + Twist (from 11 Twist Families) + Last Line (Next Danger) + Comment Debate Question`**, scored on the 12-Point Rubric (`≥ 9/12`).
2. **Step 2 — Full Script Sheet (`script.md` + `tools/script_check.py` & `tools/plan_timing.py`)**:
   - Write in first-person kid narrator voice (`A1–A2 English`, `mean 6–8w/sentence`, `~220 wpm`, `20s / 60s / 150s`), following the **11-Beat % Map**, planting `P1 / P2 / P3`, placing `Pause A (0.8–1.3s)` after the twist and `Pause B (0.6–1.0s)` before the last line, and ending on a **Next-Danger Cliffhanger** (never a moral).
   - Run `python .agents/skills/roblox-director/tools/script_check.py` and `plan_timing.py`. **Stop for user approval before voice/Studio work.**
3. **Step 3 — Voice & Word Timestamps (`audio.md`)**:
   - Generate or load `voice.mp3` (ask before spending paid ElevenLabs credits) and extract word-level timestamps (`words.json`).
4. **Step 4 — Shot List (`look.md`, `pacing.md` + `tools/shotlist_check.py`)**:
   - Build `shot-list.md` (`~1 shot/s`, cuts on sentence starts leading by `0–2 frames`, `CU/MCU ≥ 25%`, `Rule Object in Shot 1 & ≥ 50% of shots`, `in-engine camera moves ≥ 70%`, `1 Dolly-Zoom or Rack Focus on Twist`).
5. **Step 5 — Roblox Studio MCP Build (`studio.md` + `studio_kit/`)**:
   - Connect to Roblox Studio MCP (`Enable Studio as MCP server` in Studio; use direct MCP tools or run `node .agents/skills/roblox-director/studio_kit/bridge.mjs` + `python .agents/skills/roblox-director/studio_kit/rb.py`).
   - Build **Grey Blockout** first (show screenshots) $\to$ **World & Realistic Lighting (`templates/lighting-presets.lua`)** $\to$ **R6/R15 Cast with Custom Clothes (`make_clothes.py`) & 24 Bold Face Decals (`make_faces_v2.py`)** $\to$ **Zero-Clipping Check (`MT.resolve`, `MT.clips()`)** $\to$ **Check Sheet of All Shots**.
6. **Step 6 — 4K Tiled Vertical Render, Captions & Final Mix (`captions.md`, `checklist.md`)**:
   - Render via 2-tile (`1080×1920` HD) or 4-tile (`2160×3840` 4K) stitched capture (`render2.py` / `render4k.py` + `stitch.py` / `stitch4k.py`).
   - Generate popped word captions (`tools/make_caps.py` or `make_caps_toon.py`), mix with `music/roblox-story-bg.mp3` to `-14 LUFS`, and pass the 6-Area QA Checklist (`checklist.md` `≥ 8/10`).

---

## 🎨 2. TRACK R2 WORKFLOW — AI IMAGE & AI VIDEO ROBLOX GFX PROMPTS (`SCHOOL A4`)

When generating Roblox visuals via AI image/video generators (`Seedance`, `Kling`, `Midjourney`, or `@RefVideoDirector`) without Roblox Studio, enforce **School A4 (`Roblox Blocky R6/R15 & ABS Plastic Shader Lock`)**:
- Lock `cylindrical rounded-top head with bold 2D printed decal face (thick black outlines, large expressive eyes, heavy brows, zero 3D human nose), blocky R15/R6 torso and limbs with curved C-shaped blocky claw hands (strictly NO five human fingers), smooth satin-matte ABS toy plastic shader with realistic global illumination`.

---

## 🛠️ 3. TRACK R3 WORKFLOW — HEADLESS BLENDER 5.x ANIMATION & ROBLOX EXPORT SUITE (`28 blender-* SKILLS`)

Always start any Blender or custom 3D animation/rigging task with [`blender-core/SKILL.md`](file:///d:/Project/Sven/.agents/skills/blender-core/SKILL.md):
- **Headless Execution**: `python .agents/skills/blender-core/scripts/run_in_blender.py [--blend in.blend] <script.py> -- <args>`
- **Key Skills for Roblox & 3D Machinima**:
  * `blender-character-rigging` + `blender-animation` (`retarget.py`, `bake_action.py`, `loop_check.py`): Build R15/custom rigs, retarget mocap/Mixamo/BVH, and author 30fps Bezier/Quaternion character animations.
  * `blender-export-pipelines` (`export_asset.py --preset roblox` / `roblox_gltf` + `references/roblox.md`): Export R15 avatars (`15 _Geo parts`, `≤10,742 tris`), layered clothing (`_InnerCage` / `_OuterCage`), accessories (`≤4k tris`), MeshParts (`≤20k tris`), and animation clips into Roblox Studio.
  * `blender-lighting-lookdev` + `blender-time-of-day` + `blender-weather-fx` + `blender-rendering` (`render_batch.py`): Render 30–60fps EEVEE/Cycles animations in the background.
  * `blender-asset-qa` (`qa_check.py --profile roblox` + `review_shots.py`): Verify zero z-fighting, zero floating parts, and clean normals/weights before delivery.

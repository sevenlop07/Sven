---
name: roblox-director
description: >
  Level-2 Master Roblox 3D Film, Series & Animation Director for the Sven Cinematic Universe (16:9 Widescreen & 9:16 Vertical across All Genres).
  Orchestrates the Generalized 5-Stage Audio-First & SRT-Driven Roblox Filmmaking Pipeline: (R1) Concept & Aspect Ratio Lock (16:9 or 9:16), (R2) Story & Clean Voice Script for User MP3 Generation, (R3) Automated MP3-to-SRT & Contiguous Shot Timeline Extraction (`tools/audio_to_srt.py`), (R4) SRT-to-Sven-Core 6-Pillar 3D Scene Breakdown & Preview Check Sheet (Creator Store 3D Assets + R6/R15 Cast + 30fps `State A -> State B` Animation via Roblox Studio MCP & Headless Blender 5.3 RTX 3060), and (R5) Final 30fps 16:9/9:16 Master Render + 4-Layer Audio/SFX/SRT Mix.
  Triggers: "roblox", "roblox director", "roblox studio", "phim roblox", "kịch bản roblox", "video roblox", "blender roblox", or call directly "@RobloxDirector".
---

# RobloxDirector — Generalized Master Roblox 3D Film, Series & Animation Architect (Level 2)

> **COMPLETE SPECIFICATION**: Read [`d:\Project\Sven\.agents\ROBLOX_DIRECTOR.md`](file:///d:/Project/Sven/.agents/ROBLOX_DIRECTOR.md) for the Generalized 5-Stage Audio-First / SRT-Driven Architecture (`Stage R1–R5`), the 6-Pillar Sven Core Isomorphism (`Law R0`), Universal `16:9` & `9:16` Aspect Ratio Support across all genres, and the 3 Execution Engines (`Engine E1: Roblox Studio MCP`, `Engine E2: Headless Blender 5.3 RTX 3060`, `Engine E3: AI Roblox GFX School A4`).

---

## 🚀 THE 5-STAGE GENERALIZED AUDIO-FIRST & SRT-DRIVEN WORKFLOW (`STAGE R1 ➔ R5`)

Always execute in this strict step-by-step order with user approval at each gate:

1. **STAGE R1 — Concept Pitch, Genre & Aspect Ratio Lock (`16:9` Widescreen or `9:16` Vertical ➔ `✋ GATE R1`)**:
   - Support **ALL Genres** (*Drama, Family/Karma, Mystery/Thriller, Sci-Fi/Alien, Horror/Supernatural, Action/Adventure, Sitcom/Comedy*, and optional *Storytime*).
   - Lock **Aspect Ratio** (`16:9` for YouTube long-form/series or `9:16` for Shorts/Reels/TikTok) and **Target Duration**.
   - Pitch 5 high-retention story concepts using Sven Core narrative architecture (`0–3s Hook`, `3-Layer Stakes`, `Planted Clues P1/P2/P3`, `Option C Twist`, `Cliffhanger/Payoff`). Stop for user selection.

2. **STAGE R2 — Full Story & Clean Voice Script for User `.mp3` Generation (`Viết Câu Chuyện Để User Tạo File .mp3` ➔ `✋ GATE R2`)**:
   - Write the full story/dialogue script and present:
     * **Block 2A (`Clean Copy-Paste Voice Script`)**: Pure spoken text formatted for the user to copy-paste directly into ElevenLabs / TTS to generate their `.mp3` audio file.
     * **Block 2B (`3D Asset Manifest`)**: Characters (`[subject]`), 3D Locations (`[context]`), and Interactive Props (`[prop]`).
   - Stop and wait for the user to provide the `.mp3` audio file (or request local TTS generation).

3. **STAGE R3 — Automated MP3-to-SRT & Sven Core Director Blueprint (`tools/audio_to_srt.py` + `tools/srt_to_director_plan.py`)**:
   - Run `python .agents/skills/roblox-director/tools/audio_to_srt.py <audio.mp3> --script <story.txt> --out-dir <out_dir>` to extract `<stem>.srt`, word-level `words.json`, and contiguous `srt_shots.json`.
   - Immediately run `python .agents/skills/roblox-director/tools/srt_to_director_plan.py <out_dir>/srt_shots.json --aspect 16:9|9:16` to generate **`director_plan.json`** (auto sub-cuts `>3.6s` SRT blocks on `words.json` clauses, splits Speech vs. Pause reaction windows, extracts stressed `accent_frames`, assigns `scale/angle/move/axis_side` with zero adjacent repeats, and audits thresholds).

4. **STAGE R4 — SRT-to-Core 6-Pillar 3D Scene Breakdown & Preview Check Sheet (`Law R0` ➔ `✋ GATE R4`)**:
   - Translate every beat in `director_plan.json` / `srt_shots.json` into a **6-Pillar 3D Scene Specification (`Style:` ➔ `[context]:` ➔ `[subject]:` ➔ `[prop]:` ➔ `[sound]:` ➔ `Shot K [State A ➔ State B @ 30fps]`)**:
     * **`[context]:` & Lighting**: Never use flat untextured boxes or washed-out front floodlights! Use [`studio_kit/blender_env_lighting.py`](file:///d:/Project/Sven/.agents/skills/roblox-director/studio_kit/blender_env_lighting.py) (`apply_cinematic_mood` with `MULTIPLE_SCATTERING` sky, directional Key/SkyFill/HeroRim, Blender 5.3 Compositor Aerial Mist + `Fog Glow` bloom; `build_suburban_street_set` / `build_hero_house` textured clapboard houses, pitched roofs, shuttered glowing windows, picket fences, paving slabs, streetlamps, and horizon trees covering all OTS/wide sightlines) or Creator Store 3D models (`search.py` + `ins.py` + `MT.put`).
     * **`[subject]:`**: Unique **R15** silhouettes (`blender_roblox_kit.py`: 6 `body_profile` presets + 10 faceted UGC ribbon `hair_style`s with `make_stylized_hair_mat` + 4 sculpted color-matched facial hair options [`mustache`, `goatee`, `full_beard`, `stubble_scruff`] + accessories + `add_scarf_3d`), `585×559` clothes, shader-baked **11 UGC Anime & Comedy Face Archetypes** (`make_faces_ugc_anime.py` at `35°` UV arc + vowel/punctuation-aware `build_lipsync_schedule(words.json)`), oriented along the **180° interpersonal axis**.
     * **`[prop]:`**: Held props strictly bone-tracked to hands (`kit.bake_prop_follow` with `CONSTANT` hold keyframes before pickup) + parabolic gravity & multi-bounce floor settle (`kit.animate_toss_physics` / `kit.animate_drop_physics` at `g=18–20 m/s²`) triggering `kit.add_camera_shake` on collision `impact_frame`.
     * **`Shot K (SRT Beat)`**: Target-First Camera Rig (`kit.place_shot_camera` + `audit_camera_plan`: `>= 25%` Close `48–58mm`, `<= 40%` `MS`, `>= 35%` non-eye-level, `>45°` cuts, `OTS` $\to$ `Reverse OTS` on 180° axis, `y < 55%` Caption Safe, `orbit_arc`/`crane_up`/`crane_down`/`dolly_zoom`) + **Hybrid R15 Animation (`blender_r15_hybrid.py`)**: Foot/Hand IK (`setup_r15_hybrid_rig`), Mixamo `.fbx`/`.bvh` auto-retargeting via `retarget_mocap_to_r15` or grounded `animate_walk_ik` / `animate_crouch_pickup` for macro physical action, `animate_idle_weight_shift` + `kit.speak_emphasis_r15` (`words.json` accents) + `snap_r15_pose(..., anticipate=True)` for dialogue, Blender 5.3 NLA crossfades (`push_action_to_nla`), and `bake_secondary_overlap` (`Sec_Pony`/`Sec_Scarf` whip delay).
   - **Mandatory Collision Audit, Camera Audit, Playblast QA & Preview Check Sheet**: Maintain `>= 0.76m–0.85m` character separation, run `kit.audit_scene_collisions(...)` (`0` penetrations) + `kit.audit_camera_plan(...)` (`0` repeats), inspect Preview PNGs (`checks.py`) + fast `10fps` motion playblast (`kit.render_playblast_qa`) via `read_file` (checking exposure, practical glow, zero box-wall horizon, hair/beard fit, zero clipping) BEFORE full 30fps GPU rendering.

5. **STAGE R5 — Full 30fps Master Render (`16:9` or `9:16`) + 4-Layer Audio/SFX/SRT Mix (`✋ GATE R5`)**:
   - Render all shots at `30 fps` via Roblox Studio MCP (`render.py --shots srt_shots.json` for `16:9`; `render2.py`+`stitch.py` or `render4k.py`+`stitch4k.py` for `9:16`) or Headless Blender 5.3 GPU (`RTX 3060` via `temp_render_to()`).
   - Generate subtitles via `make_caps.py` / `make_caps_toon.py` (`--aspect 9:16|16:9`) and run `python tools/compile_video.py --project-dir output/<slug> --voice voice.mp3 --shots srt_shots.json --frames-dir shots --subs caps.ass --aspect 9:16|16:9 --out final.mp4` (`-14 LUFS` mix + `.mp4` master).

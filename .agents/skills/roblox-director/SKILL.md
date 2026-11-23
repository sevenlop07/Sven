---
name: roblox-director
description: >
  Roblox 3D films, series and animations (16:9 or 9:16, any genre) for the Sven repo, built in Blender 5.3 (default) or
  Roblox Studio MCP: R1 concept → R2 TTS voice script → R3 mp3→SRT shot timeline → R4 3D scene with code-rigged Roblox
  acting (Law R-ANIM, no mocap) + pose QA → R5 render + audio/caption mix. Use for "roblox", "phim roblox",
  "video roblox", "kịch bản roblox", "roblox studio", "blender roblox", or "@RobloxDirector".
---

# Roblox Director — stage router

**Spec & laws:** `.agents/ROBLOX_DIRECTOR.md` (read lines 1–271: pipeline R1–R5 + §4 Law R-ANIM, Law R-LOOK, Law R-COLLIDE, Law R-WORLD & Law R-STORY/VOICE quality core).
This file only tells you *what to open and run at each stage*. Stop at every gate for the user's approval.
Runtime-neutral: "view an image" = use your runtime's image-reading tool; never claim a check you did not do.

## Stage map
| Stage | Read (JIT) | Run | Gate deliverable |
|---|---|---|---|
| **R1** concept | `ROBLOX_DIRECTOR.md` §2 R1; **`story-structure.md`** (Track S 6-Beat / Track L 5-Archetype + Triple-Helix + `Law R-VOICE`); genre rules from `.agents/SCREENWRITER.md` / `engine/genres/*.md`; `town-script.md` for "In this town/world…" reels | — | Track S/L lock, Genre Engine, 16:9 or 9:16, 5 concepts + Track L Tier 1/3 Blueprint (`Series Scorecard ≥ 9/12`) → user picks (GATE R1) |
| **R2** script | **`story-structure.md`** (precedence note, §3 `Law R-VOICE` + scorecard, §2.4b series continuity, §6 genre → narration, §7 young-audience safety); `script.md` §0/§6/§9 voice & numbers for every genre (+ §11 for Vietnamese); `script.md` §1–§3 + `town-script.md` only for world-rule storytime; `pacing.md`; `audio.md` §1 | `tools/script_check.py script-sheet.md --mode story\|town [--lang vi]`, `tools/plan_timing.py script-sheet.md` | `Episode Scorecard ≥ 12/16` + Block 2A clean single-narrator TTS text + Block 2B manifest with Retention Map (+ Character Arc Map for series); wait for `.mp3` (GATE R2) |
| **R3** timeline | `ROBLOX_DIRECTOR.md` §2 R3 | `tools/audio_to_srt.py <audio.mp3> --script <story.txt> --out-dir output/<slug>` → if the sheet has pause rows: `tools/insert_pauses.py <audio> output/<slug>/words.json <script-sheet.md>` and re-run `audio_to_srt.py` on the `_paused.wav` → `tools/srt_to_director_plan.py output/<slug>/srt_shots.json --aspect 16:9\|9:16` | `<stem>.srt`, `words.json`, `srt_shots.json`, `director_plan.json` |
| **R4** build | `pipeline.md` (engine facts, build budget, run order); `ROBLOX_DIRECTOR.md` §4; `look.md`, `lighting-color.md`; Blender: `studio_kit/blender_roblox_anim.py` docstring; Studio: `studio.md`, `templates/mcp-setup.md` | Blender via `tools/run_roblox_blender.py --slug <slug> <script.py> -- …`; Studio via `studio_kit/bridge.mjs` + `rb.py` | pose-QA sheet + preview contact sheet (viewed), `scene_built.blend`, frame count → user picks render mode (GATE R4) |
| **R5** render & mix | `audio.md` §4 (mix), `captions.md`, `checklist.md` | `tools/render_dispatcher.py --slug <slug> --target local\|pack\|external\|studio`; `tools/make_caps.py` / `make_caps_toon.py`; `tools/compile_video.py` | `final.mp4` (−14 LUFS, ≤ −1 dBTP, captions burned) + QA score (GATE R5) |

Reference implementation of R4–R5 for both engines: `output/test_action20/` (`blender/build_scene.py`,
`studio/scene.lua`, `studio/studio_capture.py`, `make_videos.py`).

## Rules you must not skip (details: `ROBLOX_DIRECTOR.md` §4)
1. **Acting:** Blender = `RobloxAnimator` (27 states, distance-locked gait, material-baked faces). Studio = official R15
   animation ids. **No Mixamo/BVH/FBX mocap** (the quality-gate hook flags it).
2. **QA & Zero-Clipping before render (`Law R-COLLIDE`):** Call `an.check_path_clearance(strict=True)` before `bake()`, pass `target_height_m` to every `env.spawn_core_glb_asset(...)`, run `kit.audit_scene_collisions(cast, frames=None, frame_step=5, use_bvh=True, strict=True)` (auto-collects all env meshes + checks `CHAR_OBSTACLE`, `CHAR_CHAR`, `GROUND_SINK`, `SELF_CLIP` across the full timeline), `kit.audit_camera_plan`, and inspect `rba.render_pose_qa(...)` + keyframe previews. Never launch a full render without the user's render-mode choice.
3. **Assets:** core `assets/` first, official catalog ids second, Creator Store only after stripping scripts/remotes/GUIs.
4. **Studio capture:** bridge in its own console, window visible (minimised = white frames), white-frame guard + resume.
5. **Budget:** stay inside `pipeline.md` §1 caps; distinct silhouette per character.
6. **LookDev, Lighting & 5-Vector Worlds (`Law R-LOOK` + `Law R-WORLD`):** Seamless Blocky R15 (`kit.build_roblox_character` with archetype `body_profile`, Micro-PBR `shirt_fabric`/`pants_fabric` in `puffer|wool|coat|denim|default`, Cavity AO, Skin SSS, Anti-Glare 2D Face Mask) + bold high-contrast `storybook_toon` (default) / `cartoon` / `rubberhose` faces (`make_faces_expressive.py`, legacy anime faces retired) + zero-clipping 3D accessories + 5-Vector AI-Core Sets (PolyHaven 2K HDRI + 1K PBR ground, 3-plane architecture with warm window spill & 180° reverse backdrop, `env.build_atmospheric_particles` 3D snow/dust, `env.render_location_2x2_grid` audit) + Blender 5.3 Light-Linked Hero Key (40°) & Contrasting Rim (`env.setup_hero_light_linking`).
7. **Captions, Audio & Two-Track Narration Story (`Law R-CAP`, `Law R-AUDIO`, `Law R-STORY`, `Law R-VOICE`):** Captions come **100% exclusively from spoken voiceover audio** (`voice.mp3` → `words.json` → `make_caps_toon.py`, zero SFX caption text). Audio layers spoken narration with **natural environmental ASMR ambience** (rain, wind, wet mud/water squelch, footsteps — zero synthetic Python beep/bang fight SFX). Default to **100% First-Person Narration** following `story-structure.md` (`Track S` 6-Beat Short or `Track L` 5-Archetype Triple-Helix Series, passing `Series ≥ 9/12` and `Episode ≥ 12/16` scorecards; zero generic punch/kick brawl filler).

## Doc map
| File | Use it for |
|---|---|
| `story-structure.md` | **Track S (Short 6-Beat) & Track L (Series Triple-Helix + 5 Archetypes) + 100% First-Person Narration (`Law R-VOICE`) + R1/R2 Scorecards** |
| `pipeline.md` | engine capabilities & measured speeds, build budget, R4→R5 run order, scene-data conventions |
| `look.md` | shot sizes, lenses, camera moves, faces, bodies, sets, self-checks |
| `lighting-color.md` | moods (`mood@clock`), colour script, practicals, measurement (`tools/measure.py`) |
| `pacing.md` | cut rules, hook, holds, pacing check |
| `audio.md` | voice/TTS settings, music per beat, SFX, mix targets |
| `captions.md` | caption spec (toon style via `tools/make_caps_toon.py`) |
| `checklist.md` | final QA score before the user posts |
| `studio.md` | Studio MCP driving, capture quality, R6/R15 characters, collision rules |
| `script.md`, `town-script.md` | optional "In this world/town…" storytime preset |
| `templates/` | shot list, script sheet, cue sheet, hero cast, rotation log, MCP setup, lighting presets |
| `tools/doc_link_check.py` | run after editing any of these docs (0 problems required) |

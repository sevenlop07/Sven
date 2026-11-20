---
name: roblox-director
description: >
  Roblox 3D films, series and animations (16:9 or 9:16, any genre) for the Sven repo, built in Blender 5.3 (default) or
  Roblox Studio MCP: R1 concept → R2 TTS voice script → R3 mp3→SRT shot timeline → R4 3D scene with code-rigged Roblox
  acting (Law R-ANIM, no mocap) + pose QA → R5 render + audio/caption mix. Use for "roblox", "phim roblox",
  "video roblox", "kịch bản roblox", "roblox studio", "blender roblox", or "@RobloxDirector".
---

# Roblox Director — stage router

**Spec & laws:** `.agents/ROBLOX_DIRECTOR.md` (read lines 1–260: pipeline R1–R5 + §4 Law R-ANIM quality core).
This file only tells you *what to open and run at each stage*. Stop at every gate for the user's approval.
Runtime-neutral: "view an image" = use your runtime's image-reading tool; never claim a check you did not do.

## Stage map
| Stage | Read (JIT) | Run | Gate deliverable |
|---|---|---|---|
| **R1** concept | `ROBLOX_DIRECTOR.md` §2 R1; genre rules from `.agents/SCREENWRITER.md` / `engine/genres/*.md`; `town-script.md` only for "In this town/world…" reels | — | genre, 16:9 or 9:16, duration, 5 concepts → user picks (GATE R1) |
| **R2** script | `pacing.md`; `audio.md` §1 (voice); `script.md` only for world-rule storytime | `tools/script_check.py` (storytime), `tools/plan_timing.py script-sheet.md` | Block 2A clean TTS text + Block 2B cast/location/prop manifest; wait for the user's `.mp3` (GATE R2) |
| **R3** timeline | `ROBLOX_DIRECTOR.md` §2 R3 | `tools/audio_to_srt.py <audio.mp3> --script <story.txt> --out-dir output/<slug>` → `tools/srt_to_director_plan.py output/<slug>/srt_shots.json --aspect 16:9\|9:16` | `<stem>.srt`, `words.json`, `srt_shots.json`, `director_plan.json` |
| **R4** build | `pipeline.md` (engine facts, build budget, run order); `ROBLOX_DIRECTOR.md` §4; `look.md`, `lighting-color.md`; Blender: `studio_kit/blender_roblox_anim.py` docstring; Studio: `studio.md`, `templates/mcp-setup.md` | Blender via `tools/run_roblox_blender.py --slug <slug> <script.py> -- …`; Studio via `studio_kit/bridge.mjs` + `rb.py` | pose-QA sheet + preview contact sheet (viewed), `scene_built.blend`, frame count → user picks render mode (GATE R4) |
| **R5** render & mix | `audio.md` §4 (mix), `captions.md`, `checklist.md` | `tools/render_dispatcher.py --slug <slug> --target local\|pack\|external\|studio`; `tools/make_caps.py` / `make_caps_toon.py`; `tools/compile_video.py` | `final.mp4` (−14 LUFS, ≤ −1 dBTP, captions burned) + QA score (GATE R5) |

Reference implementation of R4–R5 for both engines: `output/test_action20/` (`blender/build_scene.py`,
`studio/scene.lua`, `studio/studio_capture.py`, `make_videos.py`).

## Rules you must not skip (details: `ROBLOX_DIRECTOR.md` §4)
1. **Acting:** Blender = `RobloxAnimator` (27 states, distance-locked gait, material-baked faces). Studio = official R15
   animation ids. **No Mixamo/BVH/FBX mocap** (the quality-gate hook flags it).
2. **QA before render:** `rba.render_pose_qa(...)` sheet + keyframe previews at final framing, both viewed; `kit.audit_scene_collisions`,
   `kit.audit_camera_plan`. Never launch a full render without the user's render-mode choice.
3. **Assets:** core `assets/` first, official catalog ids second, Creator Store only after stripping scripts/remotes/GUIs.
4. **Studio capture:** bridge in its own console, window visible (minimised = white frames), white-frame guard + resume.
5. **Budget:** stay inside `pipeline.md` §1 caps; distinct silhouette per character.

## Doc map
| File | Use it for |
|---|---|
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

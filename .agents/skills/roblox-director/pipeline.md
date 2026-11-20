# pipeline.md: run book — engine facts, build budget, run order, scene-data conventions

Runtime-neutral (Claude Code, Gemini/Antigravity, any agent). Rules and gates live in `../../ROBLOX_DIRECTOR.md`;
this file is the practical "how much / in which order / what the engines can do". Numbers marked MEASURED come from
`output/test_action20/` (RTX 3060, Windows 11, Blender 5.3, Roblox Studio 2026-11).

## 0. What each engine can and can't do

### 0.1 Blender 5.3 (Engine E2 — default)
- Headless, resumable, deterministic. Run every script through
  `python .agents/skills/roblox-director/tools/run_roblox_blender.py --slug <slug> <script.py> -- …` (renders stage in
  `%TEMP%\sven_blender_<slug>` and sync back to `output/<slug>/`).
- EEVEE 1080×1920: **1.7–1.9 s/frame** (MEASURED, 600 frames in 17–19 min). Cycles: plan 5–10× that; offload with R5-B.
- Acting: `studio_kit/blender_roblox_anim.py` only (Law R-ANIM). Faces switch inside the material (portable `.blend`).
- QA: `rba.render_pose_qa` (pose sheet), `kit.render_playblast_qa` (motion), `kit.audit_scene_collisions`, `kit.audit_camera_plan`.

### 0.2 Roblox Studio MCP (Engine E1 — only when real Roblox-engine look is the brief)
- Built into Studio (`StudioMCP.exe`); driven through `studio_kit/bridge.mjs` (run it in its own console window) + `rb.py`.
- Tools used: `execute_luau` (Edit), `screen_capture` (viewport only, JPEG, width ≤ 1920), `search_asset`, `insert_asset`,
  `upload_image`. `video_capture` works only in a Client playtest (not frame-exact) — don't use it for masters.
- Capture: viewport size = whatever the Studio window gives (MEASURED 1452×753 maximised on 1080p). 9:16 needs 2 pitched tiles
  per frame + `stitch.py`; 4K needs `tiles4k.py` + `stitch4k.py`. **≈ 3.5 s/frame** at 1080×1920 (MEASURED).
- The window must stay visible (minimised ⇒ white frames). The machine is unusable while capturing.
- `generate_animation` makes R15 clips only (≤ 30 s); prefer the official R15 animation ids (`ROBLOX_DIRECTOR.md` §4.6).
- Creator Store inserts must be sanitized (`ROBLOX_DIRECTOR.md` §4.5).

### 0.3 Capture size vs edit zoom
The edit-zoom limit in look.md §3 is `output size ÷ render size`: Blender renders at the output size (no headroom — do real
camera moves instead); Studio tiles are ≈ 84 % of native at 4K, so keep edit zoom ≤ +5 %.

## 1. Build budget (POLICY — per episode, before anything is built)
Fill the build-cost block of the shot list (`templates/shot-list.md`) and stay inside these caps. Exceeding one needs the user's OK.

| Item | Cap | Note |
|---|---|---|
| Sets (distinct locations) | ≤ 3 (60 s), ≤ 5 (2–5 min) | reuse with relight / `mood@clock` before building a new one |
| Principal cast rigs | ≤ 4 | crowd = palette-swapped clones, never new builds |
| Face states per character | ≤ 8 | from the face pack; lip-sync uses 3 mouth states |
| Custom acting poses (`pose` state) | ≤ 10 | everything else from the 27 `RobloxAnimator` states |
| Contact poses (two rigs touching) | ≤ 3 | hardest pose work; QA each from 2 angles |
| Rule-object images (signs, screens, decals) | ≤ 12 | |
| Special builds (a new system: rain, destruction, vehicle…) | ≤ 1 | reused for free afterwards |
| Impact VFX moments | ≤ 4 | each paired with `hit_stop` + camera shake |

## 2. Run order (R4 → R5)
**Blender (default):**
1. Blockout + set (`blender_env_lighting.py` / `blender_auto_director.build_blockout_scene`) → set preview PNG, view it.
2. Cast (`kit.build_roblox_character`, hair, faces) → CU preview, view it.
3. Acting (`RobloxAnimator` per character, root paths from the shot plan) → `render_pose_qa` sheet, view it.
4. Cameras (`kit.place_shot_camera` or per-frame keys) → `audit_camera_plan`; keyframe previews at final framing, view them.
5. `kit.pack_all_textures()` → save `scene_built.blend` → **GATE R4** (contact sheet + frame count + render-mode choice).
6. R5: `tools/render_dispatcher.py` (local or external) → `tools/compile_video.py` (voice, music, SFX, captions) → GATE R5.

**Studio:**
1. Open a Baseplate place, start the bridge, write `studio_kit/studio_id.txt`.
2. Load the scene lib (pattern: `output/test_action20/studio/scene.lua` — `build()`, `cast()`, `frame(f)`, `tile(id, F)`).
3. Preview 6–8 frames with tiled capture (`studio_capture.py preview …`), view them, fix framing.
4. Full capture (`studio_capture.py render`) with the white-frame guard → `make_videos.py`-style assembly / `compile_video.py`.

## 3. Scene-data conventions (Appendix A)
- **Mood**: write `mood@clock` (e.g. `normalDay@18.5`, `twistReveal@21`). Blender: `env.apply_cinematic_mood(col, mood=…)`
  plus the sun elevation for the clock; Studio: `Lighting.ClockTime = clock` + the mood's look values (`T.look()` pattern).
  A night clock on a day mood = an interior lit by practicals; fix darkness with practicals, not global brightness.
- **Shot**: `{id, fs, fe, V (vertical FOV), target, move}`; one camera function per shot evaluated per frame
  (pattern: `camFor(f)` in `output/test_action20/studio/scene.lua` and `cam_for(f)` in `blender/build_scene.py`).
- **Dolly-zoom**: keep `d × tan(FOV/2)` constant; author it as `{at, dur, to_distance}` inside the shot's camera function.
- **Timeline**: shots come from `srt_shots.json` / `director_plan.json`; acting segments are authored in seconds and baked at 30 fps.

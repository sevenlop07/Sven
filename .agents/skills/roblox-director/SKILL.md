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

3. **STAGE R3 — Automated MP3-to-SRT & Contiguous Shot Timeline Extraction (`tools/audio_to_srt.py`)**:
   - Run `python .agents/skills/roblox-director/tools/audio_to_srt.py <audio.mp3> --script <story.txt> --out-dir <out_dir>` to extract:
     * `<stem>.srt`: Exact sentence-by-sentence SRT timestamps (`00:00:XX,XXX --> 00:00:YY,YYY`) snapped to the verbatim script.
     * `words.json`: Word-level timestamps for `2–3 swaps/s` lip-sync mouth flaps (`talk`) and captions.
     * `srt_shots.json`: Contiguous `Shot 1..N` timeline windows (`0.00s` $\to$ `runtime_sec`, zero dead gaps).

4. **STAGE R4 — SRT-to-Core 6-Pillar 3D Scene Breakdown & Preview Check Sheet (`Law R0` ➔ `✋ GATE R4`)**:
   - Translate every SRT block in `srt_shots.json` (`Shot 1..N`) into a **6-Pillar 3D Scene Specification (`Style:` ➔ `[context]:` ➔ `[subject]:` ➔ `[prop]:` ➔ `[sound]:` ➔ `Shot K [State A ➔ State B @ 30fps]`)**:
     * **`[context]:`**: 3 Depth Planes (`Foreground + Midground + Background`) populated with free Creator Store 3D models (`search.py` + `ins.py` + `lib3.lua` `MT.put` & `MT.clean`) or Blender 3D sets, lit with `Realistic` / `EEVEE AgX` moods (`normalDay`, `sadWarm`, `scaryNight`, `twistNight`) and `DepthOfField`.
     * **`[subject]:`**: Articulated R6/R15 rigs (`MT.make` / `MT.who` or Blender R15 armature) with 3D hair (`hair.lua`), custom clothes (`make_clothes.py`), 24 expressive faces (`faces.lua`), oriented along the **180° interpersonal axis (`faceTo`)** in active poses.
     * **`[prop]:`**: Held props welded to hands (`rig.extra` on `armR`/`armL`) executing physical trajectories (`MT.toss`, `MT.drop`).
     * **`Shot K (SRT Window)`**: Target-First Camera with `>45°` scale/angle jumps (`WS` $\to$ `MCU OTS` $\to$ `Reverse OTS` $\to$ `CU Insert` $\to$ `Low-Angle CU Dolly-Zoom`) + continuous `30 fps` character animation (`MT.frame(id, f)`, `MT.walk`, head turns, arm gestures, breathing, blinking, and `words.json`-synced mouth flaps).
   - Run zero-clipping QA (`MT.resolve`, `MT.clips()`, `qa_check.py --profile roblox`) and capture a **Preview Check Sheet** of all shots (`s01..sN`) for user approval before full rendering.

5. **STAGE R5 — Full 30fps Master Render (`16:9` or `9:16`) + 4-Layer Audio/SFX/SRT Mix (`✋ GATE R5`)**:
   - Render all shots at `30 fps` via Roblox Studio MCP (`render.py` for `16:9`; `render2.py`+`stitch.py` or `render4k.py`+`stitch4k.py` for `9:16`) or Headless Blender 5.3 GPU (`RTX 3060` `render_batch.py`).
   - Mix User `.mp3` + Timestamped Diegetic Foley SFX + Dynamic BGM (`-14 LUFS`) and burn in `.srt` (for `16:9`) or `.ass` popped captions (`make_caps.py` / `make_caps_toon.py` for `9:16`) into the final `.mp4`.

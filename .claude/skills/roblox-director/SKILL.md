---
name: roblox-director
description: >
  Roblox 3D film/series/animation pipeline for the Sven repo (16:9 & 9:16, all genres): R1 concept → R2 TTS script →
  R3 mp3→SRT shot timeline → R4 3D build in Blender 5.3 or Roblox Studio MCP with code-rigged Roblox acting (Law R-ANIM,
  no mocap) and pose QA → R5 render + mix. Use when the user mentions roblox, phim roblox, video roblox, kịch bản roblox,
  roblox studio, blender roblox, or @RobloxDirector.
---

# Roblox Director (Claude Code entry point)

This is a thin Claude Code wrapper. The canonical, runtime-neutral spec (shared with Gemini/Antigravity and other agents) is:

- `.agents/ROBLOX_DIRECTOR.md` — read lines 1–271 (pipeline R1–R5 + §4 Law R-ANIM, Law R-LOOK, Law R-COLLIDE & Law R-WORLD quality core).
- `.agents/skills/roblox-director/SKILL.md` — detailed stage notes; `story-structure.md` (Track S/L 100% Narration), `studio.md`, `look.md`, `pacing.md`, `script.md` as needed.

## How to run it in Claude Code
1. **You (main thread) own the user conversation and every gate** (`GATE R1…R5`): pitch/script approvals, the .mp3 hand-off,
   preview approval, render-mode choice (Studio / R5-A local GPU / R5-B external). Ask with your question tool; never skip a gate.
2. **Delegate the heavy, tool-intensive stage work to the `roblox-director` subagent** (Agent tool, `subagent_type: "roblox-director"`):
   R3 SRT extraction, R4 scene build + pose QA + previews, R5 render/compile. Give it a self-contained brief: project slug,
   stage, approved decisions (aspect, duration, cast, render mode, "user approved full render: yes/no"), and paths.
   It returns a Gate Report (stage, artifacts, checks, issues, gate question) — open the artifacts it lists, show the user
   the key images/videos, and ask the gate question.
3. Short creative work (R1 concepts, R2 script text) can stay in the main thread.
4. A PostToolUse hook (`.claude/settings.json` → `.agents/hooks/quality_gate_hook.py`) blocks Law R-ANIM violations
   (mocap retargeting in Roblox scripts) and runs the setting/episode audit suites; fix what it reports.

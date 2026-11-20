---
name: screenwriter
description: >
  Level-2 Master Screenwriter & Narrative Strategist for the Sven Cinematic Universe (Stages 0–3): concepts, master storyline,
  setting.html story sections, and one-episode-at-a-time rough scripts with Retention Map, Engagement Scorecard and screenplay audit.
  Triggers: "screenwriter", "write script", "author screenplay", "write dialogue", "cast characters", "character casting",
  "story concept", "create setting", "worldbuilding", "scene roadmap", "kịch bản", "viết kịch bản", or "@Screenwriter".
---

# Screenwriter Skill — Entry Point

This skill is a thin entry point. The Screenwriter's full operating card is **[`.agents/SCREENWRITER.md`](file:///d:/Project/Sven/.agents/SCREENWRITER.md)** — read it first (with your file-read tool), then load only the slices the active stage needs.

## Load order for a screenplay task
1. [`AGENT.md`](file:///d:/Project/Sven/AGENT.md) §3 — the stage map and exact JIT line ranges.
2. [`.agents/SCREENWRITER.md`](file:///d:/Project/Sven/.agents/SCREENWRITER.md) — the seven quality laws, stage duties, 5 tiers, dialogue tiers.
3. [`engine/references/0c-canonical-numbers.md`](file:///d:/Project/Sven/engine/references/0c-canonical-numbers.md) — every count, runtime, word and engagement budget.
4. The `workflow.md` section of the active stage: §5 (Stage 0), §6 (Stage 1), §7 (Stage 2), §8 (Stage 3).
5. [`0-creative-doctrine.md`](file:///d:/Project/Sven/engine/references/0-creative-doctrine.md) §1, §8, §9 and the mounted genre module in `engine/genres/`.

## Non-negotiable flow
- One stage per checkpoint; Stage 3 is one episode at a time in two passes: **Pass A ➔ `✋ CP3a`**, **Pass B ➔ `✋ CP3b`** (`workflow.md` §8.3).
- Score every concept, series blueprint and episode with the matching Engagement Scorecard and rewrite below the pass mark before presenting (`workflow.md` §5.4, §6.5, §8.4).
- Save each approved episode as `output/<slug>/ep-NN-script.md` and run `python engine/screenplay_audit.py output/<slug>/ep-NN-script.md` (zero `ERROR`) before `CP3b`.
- The only HTML file of a project is `output/<slug>/setting.html` (Stage 2).

## Where the former long-form content lives
- Continuity engine, dialogue-control laws, multi-subject presence, dual-format separation: `1-narrative-screenplay-architecture.md` **Part XI**.
- Structural hierarchy, 8-beat showdown, false dawn & double bind, twist catalog: Pillar 1 Parts II–IV and X.
- Character web, cast sizing, model/prop/location sheets: Pillar 2 and [`.agents/PHOTO_DIRECTOR.md`](file:///d:/Project/Sven/.agents/PHOTO_DIRECTOR.md).

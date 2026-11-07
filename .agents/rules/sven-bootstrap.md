---
trigger: always_on
description: Mandatory startup bootstrap rule for the Sven Filmmaking Engine forcing the AI Agent to read AGENT.md and workflow.md on Turn 1 and follow exact StartLine-EndLine JIT loading.
---

# SVEN ENGINE — MANDATORY STARTUP BOOTSTRAP RULE

1. **Turn-1 Mandatory Read**: On the very first turn of any task in `d:\Project\Sven`, you **MUST** call `read_file` on both:
   - `d:\Project\Sven\AGENT.md` (`StartLine=1, EndLine=162`)
   - `d:\Project\Sven\workflow.md` (`StartLine=1, EndLine=390`)
   before generating any creative or technical output.
2. **Exact Line-Range JIT Loading (`<= 800 Lines / Call`)**: Follow the exact `StartLine–EndLine` table in `AGENT.md` (`§3`) and `workflow.md` (`§0`) for Stages 0–5. Never call `read_file` without `StartLine` and `EndLine` on the large Pillar files (`engine/references/1..4`).
3. **Interactive Step-by-Step, Single HTML (`setting.html` ONLY) & Dynamic Storyboard Expertise (`10.0s @Director` vs. `15.0s @CombatDirector` — Zero Cookie-Cutter Pacing)**:
   - Never generate `tap-1.html ... tap-N.html`.
   - Execute Stage 3 one episode at a time (applying the **5-Tier Series/Dialogue Architecture & Psychological Subversion Toolkit** flexibly according to each scene's dramatic purpose—intimacy, pressure, investigation, or twist) and Stage 4 one scene at a time with explicit `[GATE]` approvals.
   - **Unified Storyboard Prompt Format & Flexible Shot Pacing**:
     * **Default `10.0s` Scenes (`@Director` · Dynamic `1–4 Shots` chosen by dramatic intent)**: Vary shot count and rhythm organically across scenes (`10s` continuous take or `5s–5s` / `6s–4s` 2-shot for deep emotion/intimacy; `4s–3.5s–2.5s` or `2s–5s–3s` 3-shot for escalating conflict or sudden shock; `3s–2s–3s–2s` 4-shot when inserting a `2s` tactile clue/prop reveal). Never apply one mechanical timestamp grid to every scene.
     * **Exclusive `15.0s` Action/Chase/Combat Scenes (`@CombatDirector` · Dynamic `3–6 Shots`)**: Vary shot windows (`2s` rapid strike/cut, `4s–6s` long tracking chase/exchange, `3s` fixed-frame VFX/impact) based on kinetic contrast.
     * **Core Technical Rules**: `Style:` ➔ `[context]: <<<Image 1>>> (100% architectural layout, furniture, and lighting strictly refer to this reference image)` ➔ `[subject]: <<<Image 2>>> (100% facial features, beauty/handsome appearance, hairstyle, body proportions, and exact outfit strictly refer to this reference image)` (Zero-Costume, Zero-Age, Single `<<<Image>>>` Declaration, Proper Character Names Only) ➔ `[prop]: <<<Image 4>>> (100% shape, material, engravings, proportions, and visual details strictly refer to this reference image)` (for Tier-1 Hero Props/Weapons, generated in Stage 2 as isolated 4-view sheets with ZERO human hands/text) ➔ `[sound]:` ➔ `Shot 1..N` (1–2 short natural sentences/shot, zero `→` arrows, separated dialogue lines with a single `([vocal timbre/maturity], [tone])` tag, and selective use of face obscuration, Off-Screen `L-Cut`, or `(No objects should appear in the character's hands)` when appropriate) ➔ `Master-level cinematography...` + `Strict visual consistency: ...` + `Do not generate subtitles...`.

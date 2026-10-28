# scripts/ — build and revision scripts for `com-khong-chan-nuoc-mat`

Per `workflow.md` §9.7, project build scripts live here, never in the workspace root.

| Script | Purpose |
|---|---|
| `revisions/01_apply_dialogue.py` … `05_apply_plot.py` | Episode 1 revision patches, applied in order on 2026-10-07 (dialogue depth → shot scale/angle → camera moves → Story Spine → plot engine). Each one edits `tap-1.html` scene by scene with replacements asserted by count, and backs up the file first. These are a **history log**: they have already been applied, so running one again fails its assertions on purpose. |
| `apply_phase_b_ep1.py` | Phase B for Episode 1 (`workflow.md` §8.5): it changes the `setting.html` header to 10 × 10s = 100s per episode and inserts the scene-level roadmap with compact Intent Cards. Dialogue is pulled verbatim from `tap-1.html`. |
| `recompile_tap1.py` | Passes `tap-1.html` through `engine/prompt_compiler.compile_and_validate_episode()`, which rewrites the file and runs the full audit. Run it after every revision patch. |

Backups made before each patch are stored in the conversation scratch folder whose path is written inside each script.

# Project Staging Rules — Cơm Không Chan Nước Mắt

> Project-specific staging rules moved out of the engine (`.agents/DIRECTOR.md`, former Discipline §13) so that engine files stay universal. The Director MUST read this file before compiling any prompt for this series. Universal rules still come from `.agents/DIRECTOR.md`; this file only adds constraints specific to this film's setting.

## 1. Modern Domestic Architectural Staging & Freestanding Fixture Law

- **Zero Rural Fallacies in Modern Architecture**: The series is set in a modern urban townhouse: smooth tiled floors, reinforced concrete walls, sliding glass doors. There are **no wooden pillars, house columns, or structural posts** in the middle of rooms or on verandas to tie ropes to.
- **Freestanding Collapsible Folding Hammock**: Any hammock in this series is a **freestanding collapsible folding hammock with a stainless-steel tubular frame** (võng xếp khung inox di chuyển được).
  - As furniture, it is declared in `[context]:`, never in `[PROP]:`.
  - Name it in natural English without underscores: `freestanding stainless-steel folding hammock`.
- **Open Space Staging**:
  - Inside rooms: kept folded compactly against a corner wall so walking paths stay clear.
  - Deployed: set up on a spacious, uncluttered floor area (e.g., the breezy open veranda tiles). The character pulls open the tubular steel legs, clicks the notched locking struts into place, hooks the mesh bed onto the two posts, and tests the tension with both palms (one move per beat, per DIRECTOR.md D8).
  - Zero ropes tied to walls or pillars; 100% freestanding on the floor tiles.
- **Child Safety Cross-Check**: The child entity `cu_tin` is never placed in the hammock (DIRECTOR.md §6 Zero Harm Standard); `cu_tin` rests only in the pine wood crib declared in `[context]:`.

## 2. Related Project Data

- Machine-checked project rules (kinship ladder, meal terms, bookish terms, banned minor names) live in [`project_rules.json`](./project_rules.json) and are enforced by `engine/episode_audit_suite.py` Gates 3F, 4D, 4E, 4F.

# Sven Cinematic Universe — Master Genre Library & Narrative Formats
File: `engine/genres/README.md`
SSOT Status: Master Genre Registry for Screenwriting & Direction

---

## 1. Architectural Purpose

The **Genre Library** (`engine/genres/`) serves as the modular repository of structural, comedic, and dramatic conventions for the Sven Cinematic Universe. While the core Sven pipeline (`workflow.md`, `engine/references/0-creative-doctrine.md`, `1-narrative-screenplay-architecture.md`) governs cinematic physics, camera grammar, and character staging, each genre introduces specialized narrative engines, pacing mathematics, dialogue rules, and audience contract expectations.

```
                           ┌────────────────────────────────────────┐
                           │      Sven Showrunner (AGENT.md)        │
                           └───────────────────┬────────────────────┘
                                               │
                                               ▼
                           ┌────────────────────────────────────────┐
                           │     Stage 0 & Stage 1: Genre Select    │
                           └───────────────────┬────────────────────┘
                                               │
               ┌───────────────────────────────┴───────────────────────────────┐
               ▼                                                               ▼
┌──────────────────────────────┐                              ┌──────────────────────────────┐
│  Standard Serial Continuum   │                              │   Modular Genre Library      │
│  (Multi-Episode Serial Arc)  │                              │   (engine/genres/)           │
│  - Bleeding wound endings    │                              │                              │
│  - Cumulative moral stakes   │                              │  ► sitcom.md (Situation      │
│  - No episodic reset         │                              │    Comedy Engine)            │
│  (e.g., Cơm Không Chan Nước  │                              │  ► drama.md (Social & Healing│
│   Mắt)                       │                              │    Drama Engine)             │
└──────────────────────────────┘                              │  ► thriller.md (Planned)     │
                                                              │  ► rom-com.md (Planned)      │
                                                              │  ► mockumentary.md (Planned) │
                                                              └──────────────────────────────┘
```

---

## 2. Active & Registered Genre Modules

| Genre Module | File | Narrative Engine | Structural Model | Reset Mechanics |
|---|---|---|---|---|
| **Sitcom (Situation Comedy)** | [`sitcom.md`](file:///d:/Project/Sven/engine/genres/sitcom.md) | Trapped Characters + Escalating Petty Conflict + Character-Flaw Comedy | Cold Open + 3 Acts (or 2 Acts) + Tag; Multi-Plot A/B/C Weave | **100% Status Quo Reset** (End of episode returns to baseline) |
| **Social & Healing Drama** | [`drama.md`](file:///d:/Project/Sven/engine/genres/drama.md) | Real Societal Pain + Internal Metamorphosis Arc + Costly Moral Choice | 3-Act Feature (25/25/25/25%) or Puzzle-Piece Episodic Arc | **Permanent Moral Metamorphosis** (Earned resolution, sweet-and-bitter balance) |
| **Viral Microdrama (Vi Đoản Kịch)** | [`microdrama.md`](file:///d:/Project/Sven/engine/genres/microdrama.md) | Hyper-Concentrated Stakes + Rapid Escalation + Dopamine Face-Slap Reversal | Asymmetrical 13-Beat Retention Curve; 10s Scene Atoms; Invariant Closing Cliffhanger (C1–C7) | **Zero Reset** (Addictive binge loop across 40–100+ episodes) |
| **Serial Melodrama / Family Epic** | [`1-narrative-screenplay-architecture.md`](file:///d:/Project/Sven/engine/references/1-narrative-screenplay-architecture.md) | Cumulative Psychological Trauma + Generational Conflict + Moral Transformation | 4-Act Macro Arc (20% / 45% / 25% / 10%); 10s Scene Breakdown | **Zero Reset** (Serial progression with persistent cliffhangers) |
| **Romantic Comedy (Rom-Com)** | *(Planned)* | Mutual Obstacle / Dislike + Shared Mission + Inevitable Vulnerability | 3-Act Meet Cute, False Compatibility, All Hope Lost, Grand Gesture | Relational Advancement |
| **Psychological Thriller** | *(Planned)* | Asymmetric Information + Looming Catastrophe + Paranoia Spiral | 8-Beat Showdown, Multiple False Dawns, Russian-Doll Twists | Irreversible Revelations |
| **Workplace Mockumentary** | *(Planned)* | Institutional Absurdity + Talking Head Asides + Cringe Comedy | Single-Camera, Documentary Realism, Rapid Glances to Lens | Dynamic Equilibrium |

---

## 3. Operational Protocol for Sven Agents

1. **Triggering Genre Modes**:
   - Explicit user directive: *"Write a sitcom episode"*, *"Viết kịch bản drama"*, *"phim chữa lành"*, *"social drama"*, *"thể loại drama"*.
   - During **Stage 0 (Concept & Hook)**: When pitching concepts, the Screenwriter may propose formats matching these genre modules.
2. **Precedence & Rule Hierarchy**:
   - When a specific genre module is activated (e.g. `sitcom.md` or `drama.md`), its structural rules (e.g. episodic reset vs. earned moral transformation, specific beat formulas, standard scriptwriting format) take precedence over generic serial rules.
   - Fundamental production constraints (such as Child Safety, Zero Dead Air in AI prompts, and Colloquial Dialogue Standards) remain universally binding.
3. **Delivery Standards**:
   - Short beats, scenes, and cold opens: Delivered directly in chat markdown.
   - Full episode screenplays and feature scripts: Rendered with complete standard industry formatting (sluglines, character cues, parentheticals, scene buttons/shifts) ready for production or export.

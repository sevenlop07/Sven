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
└──────────────────────────────┘                              │  ► microdrama.md (Viral      │
                                                              │    Microdrama Engine)        │
                                                              │  ► action.md (Action, Chase  │
                                                              │    & Combat Engine)          │
                                                              │  ► fantasy.md (Time-Travel,  │
                                                              │    Isekai & Xianxia Engine)  │
                                                              │  ► thriller.md (Thriller,    │
                                                              │    Mystery & Folk Suspense)  │
                                                              └──────────────────────────────┘
```

---

## 2. Active & Registered Genre Modules

| Genre Module | File | Narrative Engine | Structural Model | Reset Mechanics |
|---|---|---|---|---|
| **Sitcom (Situation Comedy)** | [`sitcom.md`](file:///d:/Project/Sven/engine/genres/sitcom.md) | Trapped Characters + Escalating Petty Conflict + Character-Flaw Comedy | Cold Open + 3 Acts (or 2 Acts) + Tag; Multi-Plot A/B/C Weave | **100% Status Quo Reset** (End of episode returns to baseline) |
| **Social & Healing Drama** | [`drama.md`](file:///d:/Project/Sven/engine/genres/drama.md) | Real Societal Pain + Internal Metamorphosis Arc + Costly Moral Choice | 3-Act Feature (25/25/25/25%) or Puzzle-Piece Episodic Arc | **Permanent Moral Metamorphosis** (Earned resolution, sweet-and-bitter balance) |
| **Viral Microdrama (Vi Đoản Kịch)** | [`microdrama.md`](file:///d:/Project/Sven/engine/genres/microdrama.md) | Hyper-Concentrated Stakes + Rapid Escalation + Dopamine Face-Slap Reversal | Asymmetrical 13-Beat Retention Curve; 10s Scene Atoms; Invariant Closing Cliffhanger (C1–C7) | **Zero Reset** (Addictive binge loop across 40–100+ episodes) |
| **Action, Martial Arts, Chase & Combat** | [`action.md`](file:///d:/Project/Sven/engine/genres/action.md) | Suppressed Emotional Compression (`1.0x`) + High-Velocity Chase/Combat Climax (`2.3x–10x`) + Moral Resolution | 3-Zone Hybrid Episode (40% Drama Setup / 40% Micro-Timeline Combat & Chase / 20% Aftermath); Kinetic Arrow (`→`) Syntax via `@CombatDirector` | **Zero Reset** (Irreversible stakes, physical & moral transformation) |
| **Time-Travel, Portal Isekai & Supernatural Fantasy** | [`fantasy.md`](file:///d:/Project/Sven/engine/genres/fantasy.md) | Asymmetric Knowledge/Awakened Power + `TH3` Spatial-Temporal Shifts + Ticking Cost + `Seedance` Climax | 10-Scene Speculative Arc; 3 Hard World Rules; Tier-1 Relic 3-State Evolution; Native `3D Semi-Real (Mẫu 2B)` & `TH3` Integration | **Zero Reset** (Timeline/Realm progression with butterfly-effect cliffhangers) |
| **Psychological Thriller, Mystery & Folk Suspense** | [`thriller.md`](file:///d:/Project/Sven/engine/genres/thriller.md) | Knowledge Matrix Switch (`Suspense ➔ Mystery ➔ Prestige Reveal`) + Fair-Play Visual Clues + Chiaroscuro Staging | 10-Scene Investigative/Survival Arc; $\ge 2$ Non-Verbal Clue Plants; 70% Visual/Acoustic Tension + `Seedance` Pursuit Peaks | **Zero Reset** (Irreversible unmaskings & escalating mastermind conspiracy) |
| **Healing & Slice-of-Life** | [`healing.md`](file:///d:/Project/Sven/engine/genres/healing.md) | Ordinary life seen precisely + one small inner knot that loosens; no villains | Engine 6 Kishōtenketsu (Ki – Shō – Ten – Ketsu) | **Small permanent inner change**
| **Speculative Sci-Fi** | [`scifi.md`](file:///d:/Project/Sven/engine/genres/scifi.md) | One "What If?" + 3 Hard World Rules (Mechanism – Failure Limit – Human Cost) + a dilemma only this world could pose | Engine 4 (mystery-led) or 3 (survival-led); 0c §4 | **Permanent world-state change**
| **Horror & Folk Dread** | [`horror.md`](file:///d:/Project/Sven/engine/genres/horror.md) | Rules of the haunting + withheld information + a human secret the haunting exposes; zero gore | Engine 4 dread variant; build ➔ false release ➔ shock | **Haunting not finished (serial)**
| **Romance & Romantic Drama** | [`romance.md`](file:///d:/Project/Sven/engine/genres/romance.md) | Attraction × an obstacle inside each lover + rising cost of admitting it | Engine 1 or 6; emotional distance must change every episode | **Earned declaration / union**
| **Serial Melodrama / Family Epic** | [`1-narrative-screenplay-architecture.md`](file:///d:/Project/Sven/engine/references/1-narrative-screenplay-architecture.md) | Cumulative Psychological Trauma + Generational Conflict + Moral Transformation | 4-Act Macro Arc (20% / 45% / 25% / 10%); 10s Scene Breakdown | **Zero Reset** (Serial progression with persistent cliffhangers) |

---

## 2b. Genre Card Schema (every module, new or old)
Each module opens with a compact **Genre Card** so the Screenwriter can calibrate scorecards without reading the whole file:
`Regime (1–4)` · `Genre Engine (1–6)` · `Audience payoff` · `Default episode shape (cite 0c §4)` · `Preferred hook types (#1–#12)` · `Preferred cliffhangers (C1–C7)` · `Favoured twist codes (TW-xx) & budget` · `Dialogue : visual ratio` · `Default ending_mode / fatality_policy` · `Signature bans` · `Scorecard criteria that must score 2`.
Pacing tables inside modules are **default sketches** that flex with the Act Archetype and the locked runtime (`0c-canonical-numbers.md` §4); they never override it.

## 2c. Mastery Playbook Schema (every module)
After its Genre Card, each module ends with a **Mastery Playbook** — the part the Screenwriter reads first when writing in that genre:
`P1` the promise and the three killers · `P2` series architecture · `P3` episode architecture (scene-by-scene function table) · `P4` the genre's signature scene · `P5` dialogue & confrontation style with a short worked example · `P6` best-fit hooks, twists, cliffhangers · `P7` a 5-question mastery checklist added to the Engagement Scorecard (`workflow.md` §8.4).
Examples in playbooks are illustrations; never reuse their names or premises in a project.

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

# SVEN — Autonomous Cinematic Video Generation Engine

> **Hollywood-Grade Storytelling, 3D Spatial Geometry & Physics-Driven AI Video Architecture**  
> Operating standard for high-retention generative cinema (Sora, Runway Gen-3, Kling, Wan 2.1, Hailuo, Veo).

---

## 🏛️ Repository Architecture

The Sven engine is organized into modular layers: autonomous specialized skills, deep cinematic knowledge references, execution orchestrators, and final production deliverables.

```text
d:\Project\Sven\
├── .agents\
│   └── skills\
│
├── engine\
│   └── references\
│       ├── 1-narrative-screenplay-architecture.md   ← Pillar 1: 6 Beats, 20 Twists, Dialogue Geometries, WPS
│       ├── 2-casting-worldbuilding-specification.md ← Pillar 2: Cast Topology, Model Sheets, setting.html, 39 Styles
│       ├── 3-cinematography-3d-staging.md          ← Pillar 3: 14 Scales, 6 Angles, 7 Combos, 3D Cartesian, Continuity
│       └── 4-ai-video-prompt-compiler.md            ← Pillar 4: 10s Units, Living Settle, Mode B Laws, tap-X.html, Linter
│
├── AGENT.md                                  ← Master Routing, Orchestration & Execution Directives
├── workflow.md                               ← Complete Production Workflow Bible & Phase Protocols
├── history-registry.json                     ← Anti-Repetition Registry (Names, Props, Plots, Arenas)
├── README.md                                 ← Workspace Architecture & Operational Guide
├── .gitignore                                ← System & Temporary Scratch Exclusion Rules
│
└── output\                                   ← 🎬 FINAL PRODUCTION DELIVERABLES DIRECTORY
    └── {project-slug}\                       ← Standalone Project Package
        ├── setting.html                      ← Master Production Bible (10 Mandatory Sections)
        ├── tap-1.html ... tap-N.html         ← Production-Ready 10s Video Prompts (Two-Block System)
        └── seo-youtube.html                  ← Two-Tier Multi-Language YouTube SEO & Viral Growth Package
```

---

## ⚙️ Core Operational Engine

### 1. The Autonomous Talent Ecosystem
- **Executive Producer & Showrunner (`AGENT.md`)**: Macro-pipeline governor, human checkpoints, concept greenlighting.
- **Master Screenwriter (`.agents/skills/screenwriter/` & `.agents/SCREENWRITER.md`)**: Master of Pillar 1 (Narrative & Screenplay) and Pillar 2 (Pre-Production & Worldbuilding).
- **Film Director (`.agents/skills/director/` & `.agents/DIRECTOR.md`)**: Master of Pillar 3 (Cinematography & 3D Staging) and Pillar 4 (AI Video Prompt Compiler).
- **YouTube Growth Architect (`.agents/skills/youtube-growth-architect/`)**: Master of Stage 5 Distribution, high-CTR titles, visual tension thumbnails, and master SEO.

### 2. The Two-Block Prompt Standard
Every 10-second generative video clip is rendered using strict physical boundaries:
- **Code Block 1 (Visual Latent Engine Only)**: Pure visual prose formatted for model comprehension. Strictly excludes camera jargon (`24fps`, `16:9`, `50mm f/1.4`, metric units `cm/kg`), sound directives, or meta labels. Every character anchored via standardized Mode B prompts.
- **Code Block 2 (Production Soundscape & Continuity)**: Houses `[Diegetic Foley Soundscape]`, character dialogue with cinematic delivery subtext, and `[HANDOVER STATE]` vectors for next-clip match cuts.

### 3. Specialized Camera Protocols
- **First-Person POV Protocol**: Enforces physical foreground anchoring (hands on reins/cockpit controls, mount crest), synchronized roll/tilt dynamic physics, and eliminates third-person avatar artifacts.
- **Handheld Front-Facing Vlog Protocol**:
  - *The Ghost Camera Rule*: The recording smartphone is never depicted on screen.
  - *The Continuous One-Hand Anchor*: Exactly one hand holds the camera off-screen throughout all 10 seconds.
  - *Anti-Filter Safety Standard*: Eliminates sensual trigger tokens, utilizing intellectual elegance, dignified poise, and natural atmospheric framing.
  - *Clean UI Negative Guard*: Completely purges on-screen UI overlays, battery icons, or recording frames.

---

## 🚀 Production Deliverables Pipeline (`output/`)

All generated deliverables are stored at the end of the pipeline under `output/{project-slug}/`:

| Deliverable | Purpose | Key Contents |
|---|---|---|
| **`setting.html`** | Master Production Bible | 10 Mandatory Sections: High-concept premise, 4-pillar character matrix, 16:9 reference sheets, world arena, prop chains, and master scene roadmap. |
| **`tap-[N].html`** | Production Episode File | Complete 8×10s scene sequence with Side-by-Side Dual-Block prompts, physical actions, dialogue delivery, and continuity handovers. |
| **`seo-youtube.html`** | Growth & Distribution | High-CTR title variants, multi-paragraph SEO descriptions, timestamped chapter markers, prioritized hashtag banks, and thumbnail visual directives. |

---

## 🛡️ Best Practices & Quality Control

1. **Self-Sufficiency**: Reference files under `engine/references/` are exhaustive. When edge cases arise, update the references directly to maintain system evolution.
2. **Anti-Repetition**: Check `history-registry.json` prior to initiating any new production to ensure character names, props, and thematic twists remain 100% unique.
3. **Clean Workspace Standard**:
   - Temporary scripts and scratch files belong strictly in `scratch/` (auto-ignored by Git).
   - Core skills reside exclusively in `.agents/skills/`.
   - All completed production deliverables are deposited into `output/`.

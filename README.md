# SVEN — Autonomous Cinematic Video Generation Engine

> **Hollywood-Grade Storytelling, 3D Spatial Geometry & Physics-Driven AI Video Architecture**  
> Operating standard for high-retention generative cinema (Sora, Runway Gen-3, Kling, Wan 2.1, Hailuo, Veo).

---

## 🏛️ Repository Architecture

The Sven engine is organized into modular layers: autonomous talent personas, deep cinematic knowledge references (The Thinking Layer, The 4 Master Pillars, Directorial Assistants), deterministic compilation and audit engines, and final production deliverables.

```text
d:\Project\Sven\
├── .agents\                                     ← LEVEL 2 TALENT PERSONAS & SKILLS
│   ├── DIRECTOR.md                              ← Level 2: Creative & Technical Film Director (Pillars 3 & 4)
│   ├── SCREENWRITER.md                          ← Level 2: Master Screenwriter & Worldbuilder (Pillars 1 & 2)
│   ├── hooks.json                               ← Autonomous Workflow Hooks & Session Lifecycles
│   └── skills\
│       ├── director\                            ← Director Operational Skill
│       ├── screenwriter\                        ← Screenwriter Operational Skill
│       └── youtube-growth-architect\            ← Growth Architect Skill (Packaging, SEO, Retention)
│
├── engine\                                      ← PRODUCTION AUTOMATION & SSOT KNOWLEDGE CORE
│   ├── runbooks.json                            ← Production Presets Catalog (Microdrama, Drama, Sitcom, etc.)
│   ├── runbook_manager.py                       ← CLI Manager for Production Presets & Aspect Ratio Config
│   ├── prompt_compiler.py                       ← Deterministic Episode HTML Compiler
│   ├── episode_audit_suite.py                   ← Master Episode Linter & Quality Gates (Gates 1–5, Gate 3Q)
│   ├── setting_audit_suite.py                   ← Pre-Production Linter & Gate 1.5 Validator
│   │
│   ├── genres\                                  ← Specialized Genre Blueprints & Dialectical Matrices
│   │   ├── drama.md                             ← Social & Healing Drama (Subtext, Micro-Sacrifices)
│   │   ├── sitcom.md                            ← Situational Comedy (Fast Banter, Comic Mechanics)
│   │   └── microdrama.md                        ← High-Tension Viral Microdrama (Cliffhangers, Reversals)
│   │
│   └── references\                              ← THE CINEMATIC KNOWLEDGE ENGINE (SSOT)
│       ├── 0-creative-doctrine.md               ← The Thinking Layer: Intent → Choice → Reason (Spine & Plot)
│       ├── 0b-temporal-camera-grammar.md        ← Temporal & Camera Grammar: Timing Numbers & Prompt Syntax
│       │
│       ├── 1-narrative-screenplay-architecture.md   ← Pillar 1: 6 Beats, 20 Twists, Dialogue Geometries, WPS
│       ├── 2-casting-worldbuilding-specification.md ← Pillar 2: Cast Topology, 16:9 Sheets, 39 Visual Styles
│       ├── 3-cinematography-3d-staging.md          ← Pillar 3: 14 Scales, 6 Angles, 7 Combos, 3D Cartesian
│       ├── 3b-lighting-atmospheric-physics.md      ← Directorial Assistant 3B: 6-Point Lighting & Atmosphere
│       ├── 4-ai-video-prompt-compiler.md            ← Pillar 4: Prompt Compilers, Handover States, Mode B Laws
│       └── 4b-diegetic-foley-sound-design.md        ← Directorial Assistant 4B: Code Block 2 Soundscape & Foley
│
├── AGENT.md                                     ← Level 1: Executive Producer & Showrunner Bible
├── workflow.md                                  ← Master Production Pipeline Bible & Constitutional SSOT
├── history-registry.json                        ← 14-Axis Anti-Repetition Registry (Names, Props, Plots, Arenas)
├── README.md                                    ← Workspace Architecture & Operational Guide
├── .gitignore                                   ← System & Temporary Scratch Exclusion Rules
│
└── output\                                      ← 🎬 FINAL PRODUCTION DELIVERABLES DIRECTORY
    └── {project-slug}\                          ← Standalone Project Package
        ├── project_rules.json                   ← Project-Specific Rule Overrides & Constraints
        ├── setting.html                         ← Master Pre-Production Bible (Characters, Props, Locations)
        ├── tap-1.html ... tap-N.html            ← Production Episode Files (Scene Cards, Prompts, Handovers)
        └── seo-youtube.html                     ← Two-Tier Multi-Language YouTube SEO & Packaging Suite
```

---

## ⚙️ Core Operational Engine

### 1. The Pre-Production First Standard (`setting.html`)
To eliminate optical hallucinations, character drift, and rushed prompts, Sven strictly enforces **The Pre-Production First Standard**:
- **Mandatory Pre-Production Gate (`setting.html`)**: Before scene prompt generation, the Screenwriter and Director deliver `setting.html` containing: (1) Characters & Casting Topology, (2) Reference Image Prompts & Anchors (16:9 Model Sheets), (3) Key Props & Chekhov State Chains, (4) Locations & 5-Vector Staging, (5) Episode Main Storylines & Scene Roadmap.
- **Gate 1.5 Validation**: Verified via `python engine/setting_audit_suite.py output/<slug>/setting.html` before any video prompt compilation begins.
- **Abolition of Blind Full-Episode Dumps**: Rushing to dump an entire 10-scene episode in one blind pass is abolished. Directing proceeds **scene-by-scene directly on chat** (Interactive Chat Co-Pilot), verifying framing scale, camera angle, kinematics, somatic action, and dialogue lip-sync before assembling into `tap-X.html`.

### 2. Dual Delivery Protocols: Option 1 vs. Option 2
- **Option 1: One-Shot Full-Package Mode (`mode-batch`)**: The Showrunner and Director compile the entire approved episode into `tap-X.html` in one single audited pass.
- **Option 2: Interactive Chat Co-Pilot Mode (`mode-copilot`)**: The Director presents each scene interactively in chat using the **Scene Directorial Card** (Intent, Dialogue Relay, Camera Choreography, Biomechanical Acting, Foley, and Prompt Preview). The user reviews and refines scene-by-scene before automated compilation.

### 3. Production Presets & Aspect Ratio Sovereignty Law
- **Production Presets Catalog ([`engine/runbooks.json`](file:///d:/Project/Sven/engine/runbooks.json))**: 1-click initialization of project parameters (pacing, word caps, scene counts, camera quotas) via `python engine/runbook_manager.py init <preset> <slug>`.
- **Aspect Ratio Sovereignty Law (`workflow.md` §2.2b)**: Aspect ratio (16:9 widescreen, 9:16 vertical, 4:3 classic, or 2.39:1 anamorphic) is **100% user-governed**. Genres suggest defaults, but the user's explicit preference is sovereign.

### 4. The Autonomous Talent Ecosystem
- **👑 Sven-Agent ([`AGENT.md`](file:///d:/Project/Sven/AGENT.md))**: Level-1 Executive Producer & Showrunner. Owns macro pipeline, checkpoints, and quality gates.
- **🖋️ Master Screenwriter ([`.agents/SCREENWRITER.md`](file:///d:/Project/Sven/.agents/SCREENWRITER.md))**: Master of Pillar 1 (Narrative & Dialogue) and Pillar 2 (Cast & Worldbuilding).
- **🎬 Creative & Technical Film Director ([`.agents/DIRECTOR.md`](file:///d:/Project/Sven/.agents/DIRECTOR.md))**: Master of Pillar 3 (Cinematography & 3D Staging) and Pillar 4 (AI Video Prompt Compiler). Supported by Specialized Directorial Assistants (3B Lighting & 4B Sound Design).
- **📈 YouTube Growth Architect ([`SKILL.md`](file:///d:/Project/Sven/.agents/skills/youtube-growth-architect/SKILL.md))**: Master of Stage 5 Distribution, high-CTR packaging, thumbnail visual tension, and entity SEO.

---

## 🎥 Cinematographic & AI Prompt Compiler Standards

### 1. The Optical Camera Clause Law & Gate 3Q
- **Upfront Optical Declaration**: In every timeline beat (`[start–end]`), camera framing, focal plane, and depth of field (DoF/bokeh) MUST be declared inside the **Camera Clause before the em-dash `—`** (e.g., `Medium close-up framing ho_ten_A at eye level, shallow depth of field holding sharp optical focus on ho_ten_A's facial features with background softly falling into bokeh, slow push-in — [action]`).
- **Strict Prohibition of Trailing Tags**: Tacking isolated, dangling sentences like `. Focus on [name].` at the tail of action prose is strictly banned.
- **Automated Enforcement**: Enforced by **Gate 3Q** in `engine/episode_audit_suite.py` as a blocking error.

### 2. The 3 Camera Shot Architectures
- **Track A (Single-Shot Continuous Take)**: 1 single camera, unbroken take, **0 cuts**. Scale and angle change strictly through physical camera trajectory (`slow push-in`, `tracking`, `pedestal up`).
- **Track B (Multi-Shot Cut Sequence)**: Multi-camera coverage cut on the **180° Action Axis** (2–4 shots per 10s clip). Every subsequent shot begins with `Cut to`. Enforces the 4 Continuity Locks (Gaze Vector, Kinetic Baton Relay, Audio Suture, Handover Ledger).
- **Track AB (Hybrid Take + Cut)**: One continuous take (≥ 5s holding 2+ phases) punctuated by 1–2 decisive cuts on the power shift (Take ➔ Button, Trigger ➔ Take, Take ➔ Cut ➔ Take).
- **Track A-Locked Performance Take (Golden Quota §9.8)**: Stationary camera locked on a tripod (0 cuts, 0 camera moves). Camera setup declared once in prose header; timeline brackets dedicated 100% to somatic micro-acting and environmental physics. Strictly capped at 1–2 scenes per 9–10 scene episode (~15–20% ratio).

### 3. Subject & Prop Governance
- **4-Part Sovereign Subject Formula**:
  `{ho_ten} [100% Appearance, attire, and facial features Refer to image X], {architectural anchor}, {body posture}, hands free of props, {eyeline toward a character or landmark} — the only {ho_ten} in frame.`
- **Biomechanical Launchpad & Kinetic Handshake Protocol**: Action prose emerges directly from the physical posture declared in `[subject]:`.
- **The Two-Tier `[PROP]:` Scope Law**: `[PROP]:` holds every handheld item, one per line in natural English without underscores, each with a resting place independent of character hands. Tier 1 hero props (max 1–2 per series) carry `[100% Refer to image …]`; Tier 2 everyday items are text only. Furniture and fixtures (blankets, pillows, chairs, beds, cribs) belong 100% to `[context]:` as rich set dressing inventory.
- **Zero Ghost Object Law**: Any object touched in action must be pre-declared in `[context]:` or `[PROP]:`.

### 4. Zero Dead Air & Independent Render Atoms
- **Zero Dead Air Law (Gate 3O)**: Continuous micro-action density spanning 100% of the clip duration. Phrases that freeze characters (`the frame holds still`, `stands rigid through 00:10`) are strictly banned.
- **Zero Cumulative Timestamps (Gate 3M)**: Third-party AI video tools render each scene as an independent atom. Prompts must always start at `00:00` (e.g., `[00:00–00:03.5]`), never cumulative episode stamps like `[00:10–00:20]`.

---

## 🚀 Production Deliverables & Quality Gates

All final outputs are stored under `output/{project-slug}/`:

| Deliverable | Stage | Key Contents | Automated Quality Gate |
|---|---|---|---|
| **`setting.html`** | Stage 1 | Master Pre-Production Bible: 16:9 Model Sheets, Hero Props, 5-Vector Locations, and Scene Roadmap. | `python engine/setting_audit_suite.py output/<slug>/setting.html` (Gate 1.5) |
| **`tap-[N].html`** | Stage 4 | Master Episode File: Story Spine Card, Tier 1 Scene Cards, Two-Block Prompts, Copy Buttons & Toasts. | `python engine/episode_audit_suite.py output/<slug>/tap-N.html` (Gates 1–5, Gate 3Q) |
| **`seo-youtube.html`** | Stage 5 | Distribution Package: 4 Universal Title Formulas, 4-Tier NLP Descriptions, 7 Tag Clusters, Thumbnail Specs. | CP5 Final Review & History Registry Sync |

---

## 🛡️ Best Practices & Quality Control

1. **Constitutional SSOT Hierarchy**: Explicit user instructions > `workflow.md` §2 (Hard Constraints) > Creative Doctrine (`0`) & Grammar (`0b`) > Master Pillars 1–4 > Role files (`AGENT.md`, `DIRECTOR.md`, `SCREENWRITER.md`).
2. **Anti-Repetition Engine**: Check `history-registry.json` prior to initiating any new production to ensure character names, hero props, and plot twists remain 100% unique across the universe.
3. **Clean Workspace Standard**:
   - Temporary scripts and test files belong strictly in `scratch/` (auto-ignored by Git).
   - Core talent agents and skills reside exclusively in `.agents/`.
   - All completed production packages reside in `output/{project-slug}/`.

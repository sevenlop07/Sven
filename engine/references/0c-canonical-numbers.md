# 0c — CANONICAL NUMBERS (Single Source of Truth for Counts, Durations & Budgets)

> **Authority**: Every count, duration, ratio and word budget used by the Screenwriter (Stages 0–3) and the Directors (Stage 4) lives **here**. When any other file (workflow, role files, skills, Pillars, genre modules) shows a different number, that copy is stale and **this table wins** — below only an explicit user instruction and the project's own `output/<slug>/project_rules.json`.
> **Rule for authors**: other files **cite** this file (`0c §N`) instead of copying numbers. `0b-temporal-camera-grammar.md` keeps the speech-physics derivations; the resulting limits are restated here once.
> Kind of rule (doctrine §0): rows marked **HC** are Hard Constraints; everything else is a Craft Default that may be broken with a `BREAK: <default> — <reason>` line.

---

## §1 — Clip Atoms & Shot Topology

| Item | Value | Kind |
|---|---|---|
| Clip durations | `10.0s` (default) · `15.0s` (extended) · `30.0s` only on explicit user request. No other durations. | HC |
| Prompt timeline | Every prompt starts at `00:00` and runs contiguously to `00:10` / `00:15` / `00:30` (zero cumulative episode timestamps). | HC |
| Shots per `10.0s` dialogue/drama clip (`@Director`) | `1–4`, chosen by intent (doctrine §0.1.6). `Mode D1-A` = 1 shared fixed-camera header with timed turns. | Default |
| Shots per `15.0s` dialogue/drama clip (`@Director`) | `1` (`Mode D1-A`) or `3–4` cuts (`Mode D1-B / D1-C / D1-D`). | Default |
| Shots per action clip (`@CombatDirector`) | Topology by intent: `1–2` inertial long-take · `3–5` asymmetric exchange · `6–9` rapid-cut blitz (`1.5–2.0s` per cut). | Default |
| Shots per product commercial (`@CommercialDirector`) | `10.0s = 6` · `15.0s = 9`. | HC |
| Visual prose per shot / per timed turn | `1–2` natural sentences, `12–30` words, one state change `A ➔ B`, zero `→` arrows. | HC (Gate 3R) |

## §2 — Speech & Dialogue Budgets

| Item | Value | Kind |
|---|---|---|
| Safe speech rate | `~2.5 EN words/s` · `~3.0 VN syllables/s` (0b §2). | HC |
| Spoken shot / turn window | `3.2s–4.5s`; no spoken window under `3.0s`. $T = 0.4s + words/2.5 + 0.5–0.8s$ (VN: syllables/3.0). **Mode 2 exception**: ping-pong turns of `≤ 8` EN words / `≤ 10` VN syllables fit `3.2s–3.5s`; the final `6–8`-word turn fits `≥ 3.4s` incl. the `~0.8s` tail (also CTA-A/CTA-B commercial windows). | HC (Law D4/D5) |
| Max spoken shots | `3` in `10.0s` · `4` in `15.0s`. | HC (Law D4) |
| Words per `10.0s` clip | `0–22` words total, `0–3` turns. | HC |
| Words per `15.0s` dialogue clip | `18–32` words total, `2–4` turns. | HC |
| Words per `15.0s` action clip | `0–16` words total; `0` during sprint / impact / VFX shots; optional checkmate line. | HC |
| Line length in Mode 2 ping-pong | Shots `1..N-1`: `7–8 EN words` / `8–10 VN syllables`; final shot: `6–8` words + `~0.8s` silent closed-lip tail. | HC (Law D5) |
| Clip ending | Law D5: **Mode 1** (default) final `2.0–3.0s` shot has `0` spoken words · **Mode 2** all shots speak, final turn keeps the `0.5–1.0s` (`~0.8s`) closed-lip tail. Both are valid. | HC |
| Calm checkmate line | `2–6` words — a tool for decisive reversals, not a quota for every confrontation. | Default |
| Native interjection at line start (Law D2) | On at most **1 in 3** spoken lines of a clip, never the same interjection twice in a row, never on a calm/authority line. | Default |

## §3 — Stage 3 Rough Prose per Scene

| Scene kind | Prose | Dialogue |
|---|---|---|
| `10.0s` scene (`@Director`) | `3–5` present-tense sentences | per §2 |
| `15.0s` dialogue / showdown (`@Director`) | `4–6` sentences | per §2 |
| `15.0s` action (`@CombatDirector`) | `5–7` kinetic sentences | per §2 |

## §4 — Episode Runtime & Scene Count

- **Episode runtime is a project parameter** locked at K3 (`project_rules.json → "episode_runtime_s"`). Scene count ≈ runtime ÷ `~11s` (mix of `10.0s` and `15.0s` clips).
- **Default runtime and scene count per Act Archetype** (serial engines, `workflow.md` §6.4):

| Archetype | Scenes | Runtime |
|---|---|---|
| 1 — Act I Ignition & Trap | `6–8` | `65–85s` |
| 2 — Act IIA Counter & False Dawn | `8–9` | `85–100s` |
| 3 — Act IIB Midpoint Shatter | `9–11` | `100–125s` |
| 4 — Act IIIA Siege & Dark Night | `8–10` | `95–115s` |
| 5 — Act IIIB + IV Unified Finale | `10–14` | `115–155s` |

- **Format / genre defaults** (used when the project does not lock a runtime):

| Format / genre | Scenes | Runtime |
|---|---|---|
| Standalone short film (6-beat) | `6–12` (`1–3` × `15.0s` peaks) | `65–135s` |
| Microdrama episode | `~10` | `~100s` |
| Thriller / fantasy episode | `~10` (flex with archetype) | `100–110s` |
| Sitcom episode (Engine 5) | `6–8` | `60–80s` |
| Opt-in extended episode | `12–18` | `~3 min` |

- **4-stage episode allocation**: Open/Hook `15–20%` (Scenes 1–2) · Develop `40–50%` · Climax `20–25%` · Close/Cliffhanger `10%`.
- **Location sequences per episode**: `2–4` (typically `2–3`), each `2–4` consecutive scenes in one space (W11).
- **Characters**: `≤ 4` named characters per scene (Tier C flexible); `1–2` characters actively interacting per shot window.
- **Clip ratio `10.0s : 15.0s` by Genre Engine**: Engine 1 `75:25` · Engine 2 `90:10` · Engine 3 `60:40` · Engine 4 `75:25` · Engine 5 `90:10` · Engine 6 `65:35`.

## §5 — Engagement & Plot Budgets (per episode unless stated)

| Item | Value |
|---|---|
| Hook | lands inside the first `3s` of Scene 01 (one of the 12 hook types, Pillar 1 Part III) |
| Open question at every cut | `≥ 1` open loop is live at every scene cut |
| Pattern shift | change of scene structure, voice mode, tempo or space at least every `2–3` scenes (`~20–30s`) |
| Value shift | every scene flips at least one value (`+ ➔ −` or `− ➔ +`); no shift = merge or cut |
| Twist budget | `1` major + `1–2` minor reversals per episode; more cancel each other |
| Audience predictions | `≥ 2` BROKEN per episode, each with plants in earlier scenes; keep some predictions |
| Plants per twist | `≥ 2` (episode twist) · `≥ 3` (series master twist), in different scenes and forms |
| Knowledge-mode switch | `≥ 1` switch (suspense ↔ mystery ↔ empathy) per episode |
| Silent / sparse scene | `≥ 1` per episode |
| Same scene structure in a row | never `3` consecutive scenes with the same structure, emotion or tempo |
| Inter-episode connectors | `≥ 2` of: cliffhanger · setup/payoff · visible consequence · recurring motif |
| Master secret | one new layer per episode; full reveal at `~2/3` of the series |
| Misunderstanding lifespan | `≤ 1` act |
| Rotation | hook type, twist code (`TW-xx`) and cliffhanger type (`C1–C7`) never repeat in consecutive episodes |
| Engagement Scorecard pass mark | `≥ 12 / 16` with no criterion at `0` (`workflow.md` §8.4) |

## §6 — Cast Sizing

| Format | Named characters |
|---|---|
| Short film (1 episode) | `3–4` |
| Mini-series (3–5 episodes) | `5–6` |
| Full series (6–10+ episodes) | `7–9` |
| Mega series (12–20+ episodes) | `10–14` |

- **New named characters on screen**: Episode 1 `≤ 3–4`; every later episode `≤ 1–2` (`2b-character-lines.md` §6).
- **Absence**: no named character absent more than `2` consecutive episodes without a planted reason; A1 in `≥ 60%` of an episode's scenes unless a declared POV episode (`2b` §5).

## §7 — Macro Structure

- Plot weave: `A-Plot 55–65%` · `B-Plot 25–30%` · `C-Plot 10–15%`.
- Series acts: `20% Setup ➔ 45% Escalation & Midpoint ➔ 25% Abyss & Climax ➔ 10% Resolution`.
- Convergence nodes: Inciting `~15%` · Midpoint `~50%` · All-Hope-Lost `~75%` · Climax `~85–90%` · Echo Resolution `100%`.
- Unified finale (series `N ≤ 12`): `70–75%` showdown + `25–30%` coda in one episode.

## §8 — Regime 1 Realism Figures (Grounded Drama)

- Enterprise valuation `$50M–$1.2B`; liquid trusts, debts and deadlines `$5M–$80M`. No `$50B+` fantasy numbers.

## §9 — Short-Form Retention Targets (Stage 5 feedback loop)

| Metric | Target for `60–180s` episodes |
|---|---|
| Viewers still watching at `3s` | `≥ 80%` |
| Viewers still watching at `30s` | `≥ 60%` |
| Average percentage viewed | `≥ 55%` |
| Next-episode click-through (series) | `≥ 25%` |

Record actuals per episode in `history-registry.json → performance` (`workflow.md` §11).

## §10 — Known Superseded Numbers & Legacy Sections in the Pillars

The Pillars are large catalogs written before this table. Where they disagree with `0c`, **`0c` wins** (`workflow.md` §2.1). Known spots:

| Where | Legacy text | Use instead |
|---|---|---|
| Pillar 4 § 2 (Dual Scene Paradigm) and § 6 item 9; § Part VI Gate 4B notes | Single-speaker `10s` budgets `14–24w`, "cap ≤ 32w" | `0c` §2: `≤ 22` words per `10s` clip, `18–32` per `15s` dialogue clip |
| Pillar 4 Part VI (`tap-X.html` specification) and `episode_audit_suite.py` | Per-episode HTML files and their audit | Retired by the Single-HTML Law; Stage 3 scripts are `ep-NN-script.md` audited by `engine/screenplay_audit.py` |
| Doctrine §3.3 Tier 2, Pillar 4 § 1.2 | "One continuous camera shot per clip" | `0c` §1: one dramatic beat per clip; shot topology by intent (`1–4` dialogue, `1–9` action) |
| Any file | "`3.5s–4.5s` spoken window", "Zero Tail-Cut = 0 words in the final shot" | `0c` §2: `3.2s–4.5s`; Law D5 Mode 1 or Mode 2 |
| Any file | "`12–18` scenes per ~3-min episode" as the default | `0c` §4: scene count from the Act Archetype or the locked runtime |
| Any file | Zero fatality / positive ending as Hard Constraints | `workflow.md` §2.11: Craft Defaults set per project (`ending_mode`, `fatality_policy`); zero gore stays hard |


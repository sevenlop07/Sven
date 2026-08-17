---
name: multi-scene-video-continuity
description: Screenwriting and continuity-theory knowledge for breaking a long-form video concept into a chain of short AI-generated clips (typically 5-10s each, text-to-video or image-to-video) that must read as one continuous sequence. Use this skill whenever the task involves scripting, storyboarding, or scene-breakdown for multi-scene AI video generation, "start-to-end" / last-frame-to-first-frame chaining, character or object consistency across generated clips, continuity bibles/state tracking, beat sheets for short-form video, or any workflow where a longer story must be produced as a stitched sequence of independently-generated video segments. Trigger this even if the user only asks to "write a script" or "break this into scenes" for an AI video project, or asks about maintaining a consistent character/product/setting across clips — do not wait for them to say "continuity" or "skill" explicitly.
---

# Multi-Scene AI Video Continuity & Scripting

> **Internal note:** This document is a **foundational knowledge base** for training/informing an internal AI agent's reasoning — not an end-user tutorial and not a prompt-writing guide. It exists so the agent has the correct screenwriting and continuity-theory concepts to reason with when planning, structuring, or auditing multi-clip video scripts. It should be loaded into the agent's context/knowledge, not surfaced to end users as instructions to follow themselves.

## Purpose

This skill provides the screenwriting and continuity-theory foundation needed to script a long-form video as a **chain of short, independently-generated AI video clips** (typically 5-10 seconds each) that must be stitched together and read as one seamless sequence — whether generation is image-to-video (using last-frame/first-frame chaining), text-to-video, or a hybrid.

This is a **knowledge skill**, not a prompt-writing skill. It does not tell the agent how to phrase prompts for a specific video model. It tells the agent how to *think about and structure a script* so that whatever prompting system sits downstream has clean, well-formed input to work with. Use it to plan, break down, and audit scripts — the actual prompt engineering is handled elsewhere in the system.

---

## Core Concept: The Clip Is Not a Scene

In traditional screenwriting, a "scene" is defined by continuous space + continuous time and can run for minutes. In AI-generated multi-clip video, the atomic unit is different:

**A clip = one action beat = one state change.**

A clip should begin at a defined state (State A) and end at a different, recognizably distinct state (State B) — a change in position, pose, expression, camera framing, or lighting. Never plan a clip around a time duration ("give me 10 seconds of walking"); plan it around what *changes* during that duration.

**Rule of thumb:** if you cannot name what is different between the first and last frame of a planned clip, it is not a well-formed clip — either merge it with a neighbor or split it further.

**Anti-pattern to flag:** cramming 2-3 distinct actions into a single clip (e.g., "opens the door, walks in, and looks around") almost always produces a rushed, visually confused clip, because the generation model has to compress multiple state changes into a few seconds. Split into separate clips instead.

**Worked example:**

❌ Bad — one clip, four state changes stacked:
> "Character opens the door, walks into the room, looks around, then sits down in the chair."
> (door closed→open) + (outside→inside) + (looking forward→looking around) + (standing→sitting) — four separate changes forced into one clip. The model has to compress all four into a few seconds, usually producing rushed or dropped actions.

✅ Good — split into four clips, one state change each:

| Clip | Start State | End State | State Change |
|---|---|---|---|
| 1 | Standing at closed door | Door open, hand still on handle | Closed → Open |
| 2 | Standing at threshold | Fully inside, standing mid-room | Outside → Inside |
| 3 | Standing, looking straight ahead | Head turned, scanning the room | Forward gaze → Scanning |
| 4 | Standing beside chair | Seated | Standing → Sitting |

Each clip's End State becomes the next clip's Start State — the handoff is unambiguous because each clip only changed one thing.

---

## Continuity Theory (from film script supervision)

These are long-established live-action filmmaking principles that transfer directly and are the single highest-leverage knowledge to give the agent.

- **Continuity of action / match on action:** the pose, motion, and momentum of a subject at the end of clip N should logically match its state at the start of clip N+1. A character mid-stride at the end of one clip should be mid-stride (same leg forward) at the start of the next, not reset to a static stance.
- **180-degree rule:** once an imaginary line is established through the main axis of action (e.g., the direction two characters are facing each other, or the direction of travel), the camera should stay on one side of that line across the clip sequence. Crossing it without a deliberate transition disorients the viewer and reads as a spatial "jump" even if each clip is individually well-made.
- **Eyeline match:** if a subject is looking in a direction at the end of a clip, the next clip should pay off or continue that direction of attention (what they're looking at, or continuing to move that way).
- **Continuity of wardrobe/props/setting details:** clothing, held objects, hairstyles, lighting direction, and background elements must not change between clips unless the script explicitly calls for it (a costume change, a time skip, weather changing). Any change must be *motivated* by the story, never accidental.
- **Screen direction consistency:** if a subject or vehicle exits frame-right in one clip, it should generally enter frame-left in the next (standard convention for "continuing the same direction of travel"), unless the script uses a reversal deliberately.

**Agent checklist per handoff between clips** — before finalizing a clip transition, verify:
1. Position/pose continuity
2. Direction of movement / screen direction
3. Eyeline / gaze direction
4. Wardrobe, props, hairstyle
5. Lighting direction and color temperature
6. Time of day / weather
7. Camera side of the 180-degree line

---

## Multi-Subject Scenes (2-3+ Characters)

The "one state change per clip" rule does **not** become "one state change per character" when multiple characters share a clip. It generalizes to:

**1 clip = 1 event/interaction, regardless of how many characters participate in that event.**

Two characters shaking hands is *one* state change (not-touching → touching) even though two people are involved, because it is one causally-linked event.

**Anti-pattern:** two independent, unrelated actions happening in parallel within the same clip — e.g., "Character A walks in and sits down, while Character B stands up and walks to the door." These are two unrelated state changes that just happen to overlap in time, not one event. Split into separate clips, even if it means the two characters are temporarily not shown "simultaneously" — the sequence can still imply simultaneity through pacing without forcing both into one clip.

**Valid multi-character clip:** an action-and-reaction pair, where one character's change is *caused by* or *directly responds to* the other's — e.g., "Character B stands up and turns toward Character A, who has just entered." This is still one beat, because B's motion is a direct causal reaction to A's presence, not an unrelated parallel action.

**Rules for scripting 3+ characters:**
1. **Identify a primary subject (driver) per clip.** Even with three people in frame, one person's action should be the beat's driver; the others are in a relatively static or reactive state.
2. **Track each character's continuity independently.** Wardrobe, position, and gaze direction must be verified per-character at every checkpoint — do not let one character's continuity data bleed into another's.
3. **Block by interaction thread.** If three characters have two separate interaction threads (A talks to B, C observes from a distance), script them as separate clips per thread rather than forcing all three into one compound event.
4. **Eyelines get harder to track with 3+ subjects.** With two characters, only one eyeline pair needs to match. With three or more, explicitly state who is looking at whom at the end of every clip — this is one of the most common generation failure points as character count grows.

---

## Beat Sheet Structure for Short-Form Chained Video

Because each clip is short, the overall script should be organized as a **beat sheet**, not full-scene prose description.

- **Beat:** the smallest unit of story movement — a mini-arc of setup → micro-tension or intention → micro-resolution/transition, playable in a single clip.
- **Mini-arc grouping:** group beats into clusters of roughly 3-5 clips that form a complete mini-arc (setup → rising action → small peak/turn → transition out). This mirrors how three-act structure or Save-the-Cat-style beat sheets scale down: instead of one large arc across the whole runtime, the sequence becomes a chain of small arcs, each internally satisfying, that also connect to the next.
- Reference frameworks the agent can draw on for pacing logic: three-act structure, Save the Cat beat sheet, and general short-form/commercial editing pacing (where cognitive load per shot is much higher per second than in long-form film, so each beat must be legible fast).

**Information density rule:** a viewer can absorb roughly one to two new pieces of visual information per short clip (new setting, new character, complex action). A clip introducing a new location, a new character, AND a complex action simultaneously will almost always fail to read clearly — both to a human viewer and to the generation model attempting to render it. Apply a "one dominant idea per clip" discipline, the same principle used in slide design ("one idea per slide").

---

## The Continuity Ledger (State Tracking)

This is the digitized version of a film production's **continuity bible** (traditionally kept by the script supervisor). It is the single most important structural artifact for multi-clip generation, because clips are usually generated somewhat independently and nothing "remembers" state automatically the way a live film shoot does.

### Do not nest everything under Character

A common mistake is treating location, lighting, time of day, and props as sub-fields *inside* each character's entry. This breaks down as soon as a scene has more than one character or any object that outlives a single character's involvement:

- **Location/lighting/weather belong to the scene, not to a person.** If they're duplicated per-character, two characters in the same room can drift out of sync with each other (one entry says "living room," the other accidentally says "kitchen").
- **Props can change hands.** A cup handed from Character A to Character B is a transfer — if the prop only exists as a sub-field of one character, there's no clean way to represent the handoff.
- **Time of day and weather apply to everyone and everything in frame at once** — they should be updated in exactly one place, not copied into every character's block.

### Correct structure: three independent, parallel entity types

**1. Character Entities** — only what is physically attached to that person.
```
Entity: Character A
  - Fixed Description: (permanent appearance — never drifts)
  - Current Pose/Position/Expression: (updates every clip)
  - Wearing: (clothing/accessories currently on the body)
  - Holding: (reference to a Prop Entity — do not re-describe the prop here)
  - Last Updated At: clip #
```

**2. Prop/Object Entities** — tracked independently so they can be picked up, put down, or transferred without touching character data.
```
Entity: Prop 1
  - Fixed Description: (permanent appearance — never drifts)
  - Current Holder: (a Character Entity, "no one"/set down, or a location)
  - Current Condition: (full/empty, open/closed, intact/damaged, etc.)
  - Last Updated At: clip #
```

**3. Scene Environment Entities** — one shared entry per distinct setting, referenced by every character/prop present in it. Do not duplicate per character.
```
Entity: Environment 1
  - Location:
  - Time of Day:
  - Lighting Direction & Color Temperature:
  - Weather:
  - Fixed Background Elements:
  - Last Updated At: clip #
```

When a clip involves multiple characters, the agent reads **one shared Environment entity** plus each relevant **Character Entity** separately — never a copy of the environment nested inside each character.

### Categories of change

Two categories of change must be explicitly distinguished, and this distinction applies across all three entity types, not just characters:

- **Plot arc change** — a change the story *wants*: a character getting soaked in a rainstorm, a door going from closed to open, day turning to night, a prop changing hands. This is intentional and should be written into the ledger deliberately, with the clip that causes it identified.
- **Visual identity drift** — a change that should NOT happen: hair color shifting, a logo changing, a face looking subtly different, clothing changing color without narrative reason, an environment's lighting shifting with no scripted cause. This is a generation error to catch, not a story beat.

When scripting each new clip, the agent should read the ledger's current state for every entity appearing in that clip (character, prop, and environment), use it as the mandatory starting condition, then update the ledger with the new ending condition once the clip is defined.

**Checkpointing:** for long sequences, insert a checkpoint every 3-5 clips where the ledger state for every entity type is explicitly re-verified against its *original* fixed description (not just the previous clip), because small per-clip errors compound across a chain (drift accumulates). If a real generation shows an entity has drifted too far from its fixed description, the correct recovery is to regenerate from the last clean checkpoint, not to keep chaining forward from the drifted state.

---

## Transition Grammar

Different scripted transitions between clips carry different risk profiles for AI generation, and the agent should choose deliberately rather than defaulting to a straight cut every time:

- **Match cut:** the ending state of clip N is nearly identical in framing/pose to the starting state of clip N+1. Lowest risk, most seamless, should be the default choice whenever the action allows it.
- **Cutaway:** insert a short secondary clip (a close-up of an object, a detail, a hand) between two riskier clips. Useful as a *deliberate* tool to bridge a difficult continuity jump (e.g., a location change, a costume change, a big lighting shift) — the cutaway gives the sequence a place to "reset" without the viewer noticing a discontinuity in the main subject.
- **Jump cut:** an intentional, noticeable skip (time compression, "later that day"). This should only ever be a *scripted narrative choice*, never used to paper over a failed continuity match — if a transition is jarring because generation drifted, that is a production error, not a valid jump cut.

**Rule for the agent:** at every clip boundary, explicitly decide which of these three transition types is intended, and if match cut is not achievable given the story content, insert a cutaway on purpose rather than leaving an unplanned hard discontinuity.

---

## Ending a Clip Well (End-State Design)

Because the last frame/state of a clip becomes the anchor for the next (whether via literal frame-chaining or via description in a text prompt), clips should be scripted to **end at a legible, relatively stable moment**:

- Avoid scripting a clip to end mid-fast-motion or mid-motion-blur (e.g., mid-turn, mid-run, mid-gesture) — these produce ambiguous or corrupted end states that are hard to continue from cleanly.
- Prefer ending on a brief settle: a completed gesture, a held pose, a stopped movement, a clear gaze — even half a second of near-stillness at the end of a beat makes the next clip's starting condition unambiguous.
- If the story genuinely requires ending on fast motion (e.g., a chase), script an explicit cutaway or a deliberate jump cut immediately after, rather than trying to chain directly off a blurred end state.

---

## Script Deliverable Format

A well-formed script has **two layers**: a one-time Entity Registry, and a Clip Table that records only what *changes* (deltas), never full re-descriptions. This mirrors the ledger structure above and is the format the agent should default to when actually writing a script.

### Layer 1 — Entity Registry (declared once, at the top of the script)

Declare every recurring Character, Prop, and Environment exactly once, using the three-entity-type structure from the Continuity Ledger section. Nothing in this registry should ever be re-typed inside the Clip Table — the table only references entity names and records deltas against this baseline.

```
CHARACTERS
CHARACTER A — [name]
Fixed Description: ...

CHARACTER B — [name]
Fixed Description: ...

PROPS
PROP 1 — [name]
Fixed Description: ...

ENVIRONMENTS
ENV 1 — [name]
Lighting/Time of Day/Weather: ...
Space: ...

ENV 2 — [name]
Lighting/Time of Day/Weather: ...
Space: ...
```

Also declare **global constants** once — visual style, aspect ratio/format intentions, overall lighting mood — which hold across the entire sequence unless a specific clip calls for a deliberate shift.

### Layer 2 — Clip Table (delta-only)

| Clip | Entities Present | Main Event (1 state change) | Env | Prop Change | End State (handoff) | Transition |
|---|---|---|---|---|---|---|

- **Entities Present** — reference entity names/labels from the Registry only. Never re-describe an entity's fixed appearance here.
- **Main Event** — one sentence, one dominant event, imperative voice. Per the Multi-Subject Scenes section, this may involve multiple characters as long as it is one causally-linked event.
- **Env** — the Environment entity active for this clip. Leave as-is (or mark with a dash) if unchanged from the previous clip; only write a transition (`ENV 1 → ENV 2`) when the environment actually changes, and treat any such change as a high-risk boundary requiring a deliberate Transition choice (see below).
- **Prop Change** — leave blank if no prop changed hands or condition this clip. Only fill in when a Prop Entity's `Current Holder` or `Current Condition` changes (e.g., `Prop 1: B → A`).
- **End State (handoff)** — the specific, non-blurred ending condition this clip hands to the next; this becomes the next clip's implicit Start State and should never need to be re-typed there.
- **Transition** — match cut / cutaway / jump cut, chosen deliberately per the Transition Grammar section. Mandatory to specify explicitly whenever Env changes.

**Why delta-only, not full-redescription:** if every clip row re-describes each character's full appearance, wardrobe, and the room's lighting, the script both bloats and becomes a second, competing source of truth against the Entity Registry — any edit has to be made in two places and they will eventually disagree. Delta-only tables keep the Registry as the single source of truth and make every row auditable at a glance: scanning the Prop Change and Env columns alone tells the agent exactly where the continuity risk points are in the whole sequence.

**Common structural error to flag:** if a drafted Clip Table row contains a full character description ("a man, 30s, black hair...") instead of just a name/label, that's a sign the delta discipline has broken down — correct it back to a reference plus only what changed.

---

## Common Failure Patterns to Flag During Script Review

The agent should proactively flag these when reviewing or writing a script, since they are the most common root causes of a broken final sequence:

1. **Compound beats** — more than one state change packed into a single clip.
2. **Silent drift** — a fixed-description entity changing between clips with no narrative reason and no ledger flag.
3. **Blurred handoffs** — a clip scripted to end mid-fast-motion, making the next clip's starting condition ambiguous.
4. **Missing transition intent** — no explicit decision about match cut / cutaway / jump cut at a risky boundary, leaving continuity to chance.
5. **Overloaded first clip of a new setting** — introducing a new location, new character, and new action all in the clip immediately after a location change (should be split, or eased in with a cutaway/establishing beat).
6. **No checkpoint entities** — a long chain (6+ clips) with no point where state is re-verified against the original fixed description, allowing drift to compound silently.
7. **180-degree violations across clip boundaries** — camera side flipping between clips of the same continuous action without a motivated reason.
8. **Environment nested inside character** — location/lighting/weather duplicated per-character instead of tracked once as a shared Environment entity, risking two characters in the same scene silently disagreeing on where or when they are.
9. **Untracked prop handoffs** — a prop changing hands between characters with no explicit `Current Holder` update, leaving it ambiguous who is holding what in the next clip.
10. **Parallel unrelated actions forced into one clip** — two characters doing unconnected things at the same time crammed into a single clip instead of split into separate, sequential beats.
11. **Full re-description inside the Clip Table** — a clip row re-typing a character's or environment's full fixed description instead of referencing the Entity Registry and recording only the delta; creates a second, driftable source of truth.
12. **Missing eyeline resolution with 3+ characters** — a multi-character clip that doesn't specify who is looking at whom by the end state, left to chance as character count grows.

---

## Quick Reference Summary

| Concept | One-line definition |
|---|---|
| Clip / Beat | Smallest scriptable unit; one event, one state change (may involve multiple characters if causally linked) |
| Entity Registry | One-time declaration of every Character/Prop/Environment; the single source of truth |
| Clip Table | Delta-only record of what changes per clip; never re-describes entities, only references + changes |
| Character Entity | Tracks only what's physically attached to a person (pose, wardrobe, what they're holding) |
| Prop Entity | Tracked independently so it can be picked up, set down, or transferred between characters |
| Environment Entity | One shared entry per setting (location/lighting/time/weather); referenced, never duplicated per character |
| Fixed Description | The permanent identity of an entity; should never drift |
| Current State | The entity's changing condition; updates every clip |
| Primary subject (driver) | The character whose action drives a multi-character beat; others are reactive/static |
| Match cut | Default, lowest-risk transition between visually similar end/start states |
| Cutaway | Deliberate bridge clip used to mask a risky continuity jump (mandatory to consider on any Environment change) |
| Jump cut | Intentional narrative time-skip; never a fix for failed continuity |
| Mini-arc | A cluster of 3-5 beats forming a small complete story movement |
| Checkpoint | Periodic re-verification of every entity's state against its original fixed description |
| Plot arc change | Intentional story-driven change (should happen) — applies to characters, props, and environments alike |
| Visual identity drift | Unintentional generation error (should be caught, not scripted) |

# 3c — CAMERA MASTER GRAMMAR (The Director's Complete Working Reference)

> **What this is**: the single working reference the Director uses to choose every camera decision — who the camera is, how far, from what height, how it moves, what is sharp, how the frame is built, and how the shot cuts to the next. It completes Pillar 3 (`3-cinematography-3d-staging.md`, the long catalog with deep dives) and is written to be **read in full in one call** at Stage 4.
> **Authority**: intent comes from `0-creative-doctrine.md` §1–§2; timings, speech windows and shot counts from `0c-canonical-numbers.md`; prompt syntax from `0b-temporal-camera-grammar.md`. This file owns the *choice* of camera tools.
> **Prompt law**: describe optics with words, never hardware numbers (no focal lengths in mm, no f-stops, no Kelvin — Pillar 3 §2.1). Every shot targets a named subject (`targeting [Name]`, Law 3 Target-First).

---

## §0 — THE DIRECTOR'S 8 QUESTIONS (DECISION ORDER)

Answer in this order for every shot. Each answer is one clause; a choice without a reason is decoration (doctrine §2.6).

| # | Question | Decides | Section |
|---|---|---|---|
| 1 | What must the viewer **feel or learn** in this shot? | the shot's job | doctrine §1 Intent Card |
| 2 | **Whose eyes** is the camera? | perspective | §4 |
| 3 | How **close** must we be to feel it? | shot size | §1 |
| 4 | Who holds **power** right now? | vertical angle, yaw, roll | §3 |
| 5 | Does the camera need to **move** — and why? | movement + landing | §5 |
| 6 | What must be **sharp**, what may blur? | lens feel, focus | §6, §7 |
| 7 | Where does the **eye land** in the frame? | composition | §8 |
| 8 | How does this shot **hand over** to the next? | cut, continuity | §9 |

**Three governing principles**
1. **Distance = psychological closeness.** Closer is more intimate or more oppressive; wider is more context, isolation or fate.
2. **Angle = power at this instant.** It may change inside a scene when power changes — never at random.
3. **Movement needs a motive**: (a) follow a moving subject, (b) reveal information, (c) express an inner change. No motive ➔ static camera.

---

## §1 — SHOT SIZE LADDER (15 SIZES)

| # | Size | Frame boundary | Feeling / function | Lip-sync | Prompt phrase |
|---|---|---|---|---|---|
| 1 | Extreme Wide (EWS) | subject < 10% of frame height | fate, scale, isolation, world | ❌ V.O. only | `extreme wide shot, [Name] a tiny figure in [place]` |
| 2 | Wide / Establishing (WS) | the whole room or street | where we are, who is where | ⚠️ short calls | `wide establishing shot of [place], [Name] at [landmark]` |
| 3 | Solitary Environmental | lone figure in a large empty space | abandonment, quiet | ✅ V.O./breath | `wide shot, [Name] alone in the vast empty [place]` |
| 4 | Full Shot (FS) | head to feet | bearing, body language, physical comedy | ✅ | `full shot of [Name], head to toe` |
| 5 | Medium Wide (MWS) | knees up | walking dialogue, group of 2–3, comedy blocking | ✅ | `medium wide shot from the knees up` |
| 6 | Cowboy (MLS) | mid-thigh up | standoff, readiness, hands near the waist | ✅ | `cowboy shot from mid-thigh up` |
| 7 | Medium Shot (MS) | waist up | neutral conversation, gesture with props | ✅ | `medium shot from the waist up` |
| 8 | Medium Close-Up (MCU) | mid-chest up | the dialogue workhorse; face + hands | ✅ best | `medium close-up from mid-chest up` |
| 9 | Close-Up (CU) | chin to crown | emotion, decision, subtext | ✅ | `close-up on [Name]'s face` |
| 10 | Big Close-Up / Choker | lower lip to eyebrows | suffocation, peak tension | ⚠️ 1–4 words | `very tight close-up from brow to lower lip` |
| 11 | Extreme Close-Up (ECU) | one eye, a scar, a tear | visceral truth | ❌ no lips | `extreme close-up on [Name]'s eye` |
| 12 | Italian Shot | eyes only, edge to edge | duel stare, recognition | ❌ | `extreme close-up framing only [Name]'s eyes` |
| 13 | Head-On | face dead centre, straight down the lens | direct challenge, confession | ✅ | `head-on symmetrical close-up of [Name]` |
| 14 | Insert / Macro Insert | object + hand contact | proof, clue, Chekhov detail | ❌ no face | `macro insert of [Name]'s hand on the [prop]` |
| 15 | Cutaway | a detail outside the action | breath, irony, time passing | ❌ | `cutaway to [detail]` |

**Ladder rules**
- **Escalate with emotion**: WS ➔ MS ➔ MCU ➔ CU across a confrontation; release by jumping back wide after the peak.
- **Change size by at least two steps** when cutting the same subject (MS ➔ CU, not MS ➔ MCU), or change angle ≥ 30° (§9).
- **Lip-sync safe zone** is FS to CU; dialogue in EWS, ECU, Italian or Insert is banned.
- **Hands need MS or closer**; a prop handoff needs an Insert or MCU.

---

## §2 — FUNCTIONAL SHOT TYPES (WHO IS IN THE FRAME, AND WHY)

| Type | Definition | Use it for | Watch out |
|---|---|---|---|
| **Clean single** | one person, nobody else in frame | isolation, verdict, monologue | loses the relationship |
| **Dirty single** | one person, a sliver of the other's shoulder/head in the foreground | dialogue that keeps the bond visible | keep the foreground soft |
| **Two-shot** | both people readable | balance of power, intimacy, comedy | equal size = equal power |
| **Over-the-shoulder (OTS)** | past A's shoulder onto B's face | the dialogue standard; the listener's presence | A's face must not be readable too |
| **Shot / reverse shot** | alternate OTS or singles on each speaker | ping-pong exchanges | keep both on the same side of the 180° line |
| **Three-shot / group shot** | 3+ people composed in depth | meetings, meals, verdicts in front of witnesses | no more than 1–2 people acting at once (`0c` §4) |
| **Reaction shot** | the listener, silent | the true payoff of a line; comedy lands here | hold it; do not cut away too fast |
| **Insert** | the object the scene turns on | proof, plant, twist | announce its owner in the shot |
| **Cutaway** | a related detail outside the action | rhythm, irony, compression | must still carry meaning |
| **Reveal shot** | information withheld, then exposed by a move, a focus pull or a character stepping aside | twists, entrances, scale | plant what is revealed earlier |
| **Hero shot** | low angle, slow push or rise, strong backlight | a character's rise, a victory, a transformation | use once per arc or it cheapens |
| **Profile** | strict 90° side view | confrontation nose-to-nose, distance between two people | faces less readable for lip-sync |
| **POV** | through a character's eyes | discovery, threat, desire | the POV owner is shown before or after |
| **Master + coverage (AI adaptation)** | in film: one wide take of the whole scene + closer angles. In AI video: **the first clip of a location sequence establishes the geography (WS/MWS); later clips (TH1) cover singles and inserts inside that geography** | keeping space readable across 10s/15s clips | never open a new location on a CU without an anchor |

---

## §3 — ANGLES & POWER

### 3.1 Vertical (height of the lens)
Overhead 90° (fate, chessboard) · High (vulnerable, judged) · Eye-level (equal, honest) · Chest-level (natural, flattering) · Hip (readiness, weapons) · Knee (march, swagger) · Low (dominance, threat, heroism) · Worm's eye (crushing scale) · Nadir 90° up (trapped below). Full matrix: Pillar 3 §3.1.

### 3.2 Horizontal (around the subject)
Frontal (confession, challenge) · Three-quarter front (the default human angle) · Profile (distance, standoff) · Three-quarter back (following, hiding intent) · Back (mystery, walking away, the unseen face).

### 3.3 Roll
Dutch tilt 15°–25° = a world off balance (madness, guilt, intoxication, villain's ground). Use for one scene, not a whole episode.

### 3.4 Power choreography in a confrontation
1. **Start**: the dominant character is shot from slightly below; the weaker from slightly above.
2. **The crack**: when the weaker one plays their card, bring both to eye-level (power equal).
3. **Reversal**: invert the heights — the former victim now from below, the former oppressor from above.
4. **Payoff**: the defeated face in a high-angle CU, held in silence.
- Seated vs standing beats any lens angle: the person who stands up takes the power; the one who sits down cedes it.
- In 9:16, height difference reads stronger than horizontal distance — use it.

---

## §4 — PERSPECTIVE (WHO IS THE CAMERA)

| Perspective | Feeling | Rule |
|---|---|---|
| Third-person objective | neutral storytelling | the default |
| POV (first person) | discovery, threat, desire | show the owner before/after; hands may enter frame |
| Over-the-shoulder subjective | sharing a character's side of the argument | favour the character the audience should side with |
| Direct address / vlog / selfie | intimacy, confession, comedy aside | only when the story's form allows breaking the wall |
| SnorriCam (body-mounted) | panic, drunkenness, disorientation | short bursts only |
| **Voyeur** (through a gap, a window, foliage) | being watched, secrecy, dread | foreground frame partially blocks the view |
| **CCTV / found footage** | evidence, cold detachment, horror | high fixed corner angle, wide, static; timestamp-free (no text) |
| **Mirror / reflection** | duality, self-judgement, hidden presence | the reflection carries the truth |
| **God's eye / drone** | fate, scale, the world closing in | slow, high, deliberate |
| **Screen view** (phone, laptop) | messages, video calls, evidence | show the screen only in an Insert, never with readable text; the reaction carries the meaning |

---

## §5 — CAMERA MOVEMENT

### 5.1 The movement contract
Every move has: **motive** (follow / reveal / express) · **direction** · **speed** (a `[Shot Speed]` tier from `0b` §4.2) · **landing** (the framing it ends on). One move per shot (One-Move Rule). Write start and end framing: `slow push-in from a medium shot to a close-up on [Name]`.

### 5.2 Catalog
| Move | What the camera does | Expresses | AI-safe phrasing |
|---|---|---|---|
| Static / locked-off | nothing | weight, observation, dialogue focus | `static camera` |
| Pan | turns left/right on the spot | following, scanning, connecting two people | `slow pan from [A] to [B]` |
| Tilt | turns up/down on the spot | scale, revealing height, a look up or down | `slow tilt up from [boots] to [face]` |
| Push-in (dolly in) | travels toward the subject | realisation, rising tension | `slow push-in toward [Name]'s face` |
| Pull-out (dolly out) | travels away | isolation, consequence, revealing context | `slow pull-out revealing [context]` |
| Truck / crab | travels sideways | parallel walk, gliding past a line of people | `lateral tracking shot moving right alongside [Name]` |
| Pedestal | the whole camera rises/lowers | rising to a reveal, sinking with defeat | `camera rises vertically from [table] to [Name]'s eyes` |
| Follow (from behind) | travels behind a moving subject | entering the unknown, pursuit | `camera follows behind [Name] down the corridor` |
| Lead (in front) | travels backward in front | determination, confrontation in motion | `camera leads [Name], moving backward as she advances` |
| Arc | moves on a partial circle | shifting perspective, revealing the other side | `slow half-arc around [Name]` |
| Orbit 360° | full circle | spinning world, union, overwhelm | rare; never during dialogue |
| Crane / jib | sweeping vertical + horizontal | grandeur, opening/closing a sequence | `crane shot rising above [place]` |
| Steadicam / gimbal glide | smooth floating travel | immersion, long take | `smooth gliding steadicam` |
| Handheld | organic shake | urgency, documentary truth, panic | `subtle handheld` (avoid heavy shake with lip-sync) |
| Whip pan | very fast pan with blur | sudden attention, comedy, transition | a cut point, not a dialogue shot |
| Zoom (optical) | magnifies without moving | voyeurism, TV-documentary feel | do not confuse with push-in |
| Crash zoom | violent fast zoom | comic shock, sudden threat | 1 per scene max |
| Dolly zoom (vertigo) | push + opposite zoom | horror of realisation | once per film |
| **Rack zoom / snap zoom** | fast stepped zoom in two beats | comedy, horror sting | sparing |
| **Drone reveal** | flies up or back to reveal geography | scale, arrival, ending | slow; establishing or closing clips only |
| **FPV dive** | fast agile flight through spaces | thrill, chase, impossible journey | action only (`@CombatDirector`) |
| **Barrel roll** | camera rotates around the lens axis | disorientation, fall, supernatural shift | action/fantasy; ≤ 1 per episode |
| **Bullet time / time-slice** | frozen moment, camera arcs around it | the decisive instant | Tier 5 `ultra-slow-motion suspension` |
| **Speed ramp** | real-time ➔ slow-motion ➔ real-time | impact, beauty, hit-stop | action and commercials; state the ramp in prose |
| **Timelapse / hyperlapse** | compressed time | days passing, transformation | establishing or transition clips only |

### 5.3 Movement rules
- **Dialogue = static or very slow push** (Law D1). Moves land before the line starts.
- **Moving subject + moving camera** is fine if the camera simply follows; never add a second camera move.
- **Stillness after motion** is the strongest punctuation: end a fast sequence on a locked frame.
- **Speed matches emotion**: slow push = dawning truth; fast push = shock; slow pull = loneliness; fast pull = being thrown out.

---

## §6 — LENS FEEL (DESCRIBED IN WORDS)

| Feel | Effect on space | Use | Prompt words |
|---|---|---|---|
| Wide-angle | stretches space, exaggerates depth and nearby features | comedy, unease, cramped rooms made strange, action energy | `wide-angle perspective, exaggerated depth` |
| Normal | natural human vision | honest drama, default | `natural perspective` |
| Telephoto | compresses space, separates subject from background | surveillance, longing across distance, crowds pressing in | `telephoto compression, background compressed close behind [Name]` |
| Macro | tiny detail huge | clues, textures, food, tears | `macro detail` |
| Fisheye | extreme curvature | hallucination, comedy, peephole | `fisheye distortion` (rare) |
| Anamorphic look | wide cinematic frame, horizontal flares, oval bokeh | epic, romance, prestige | `anamorphic cinematic look, horizontal lens flare` |
| Tilt-shift look | thin slice of focus, miniature effect | god's-eye fate, satire | `tilt-shift miniature effect` |

---

## §7 — FOCUS & DEPTH OF FIELD

| Tool | Meaning | Prompt |
|---|---|---|
| Shallow focus | isolate one person's inner world | `shallow depth of field, background softly blurred` |
| Deep focus | everything matters; relationships in space | `deep focus, foreground and background both sharp` |
| **Rack focus** | attention moves from A to B (cause ➔ effect, speaker ➔ listener, object ➔ owner) | `focus shifts from [the letter] to [Name]'s face` |
| **Split diopter look** | two planes sharp at once, a tense split | `split-focus composition, [A] sharp in the foreground and [B] sharp in the background` |
| Intentional defocus | dizziness, tears, memory | `image drifts softly out of focus` |
| Foreground occlusion | secrecy, voyeurism, depth | `soft out-of-focus foreground [object] partially framing [Name]` |
Focus is a pointer: whatever is sharp is what the viewer must think about.

---

## §8 — COMPOSITION

### 8.1 Core tools
- **Rule of thirds**: eyes on the upper third line; the subject on a vertical third, facing the open side.
- **Centre symmetry**: power, ritual, confrontation, madness (head-on).
- **Leading lines**: corridors, tables, roads pointing to the subject.
- **Frame within a frame**: doors, windows, mirrors, arches = trapped, watched, separated.
- **Negative space**: empty frame around a person = loneliness, threat to come (horror: leave room for something to appear).
- **Headroom & lead room**: small headroom in CU; give looking room in the direction of the gaze. **Short-siding** (subject looks toward the near edge) = unease, being cornered.
- **Depth layers**: foreground / midground / background each carry something (Pillar 3 §1.0c).
- **Balance**: a heavy subject on one side balanced by light or an object on the other; deliberate imbalance = instability.
- **Size within frame**: the bigger figure dominates; scale two people to show power.

### 8.2 Vertical 9:16 composition (microdrama, Shorts, Reels, TikTok)
1. **Stack vertically, not side by side**: put people at different heights or depths (one seated, one standing; one near, one far) instead of left-right.
2. **Faces in the upper third**; keep the lower 20% and the right edge free for platform UI (captions, buttons).
3. **Prefer MCU and CU** — wide horizontal staging collapses on a phone.
4. **Vertical OTS**: the foreground shoulder at the bottom corner, the face high on the opposite side.
5. **Two-shot**: diagonal depth (near shoulder low-left, far face high-right).
6. **Movement**: tilts and pedestals read better than pans; vertical reveals (feet ➔ face) are native to the format.
7. **Inserts fill the frame**: hand + object centred, no wasted margins.

---

## §9 — CUTTING & CONTINUITY

| Rule | Statement |
|---|---|
| 180° rule | keep the camera on one side of the line between two characters; cross only with a visible move or a neutral shot |
| 30° rule | a cut on the same subject changes angle ≥ 30° or size by two steps, or it feels like a jump cut |
| Eyeline match | if A looks screen-left at B, B looks screen-right back at A |
| Screen direction | a character moving left-to-right keeps that direction across cuts unless we see the turn |
| Match on action | cut in the middle of a movement (a hand reaching, a door opening) to hide the cut |
| Scale progression | establish ➔ approach ➔ intimacy; reset wide when the space changes |

| Cut type | Use |
|---|---|
| Straight cut | default |
| Match cut (shape, motion, sound) | link two times/places by a shared form |
| Smash cut | abrupt change of mood (calm ➔ chaos, boast ➔ humiliation) |
| J-cut / L-cut | sound leads or trails the picture: smooth dialogue, dread |
| Jump cut | impatience, comedy, time compression — deliberate only |
| Cross-cut | two simultaneous lines of action |
| Cutaway / insert | evidence and rhythm |
**Across AI clips**: the last frame of clip K must be a clean landing pose so clip K+1 (TH1) can start from it; flip the axis to the other speaker at the cut (Law D6).

---

## §10 — CAMERA GRAMMAR BY GENRE

| Genre | Default sizes | Angles | Movement | Signature shot | Avoid |
|---|---|---|---|---|---|
| Family drama | MS, MCU, CU; group shots at meals | eye-level; subtle height shifts for power | static, slow push on realisation | reaction CU of the silent family member | flashy moves, Dutch angles |
| Microdrama | MCU, CU, inserts of status proxies | strong low/high power angles | snap pushes on reveals, whip to reaction | low-angle reveal of the hidden identity + high-angle CU of the humbled | long wides, slow builds |
| Sitcom | MWS and FS for physical comedy, MCU for lines | eye-level | static; crash zoom as a joke | wide two-shot holding the awkward pause, then reaction CU | cutting away from the reaction too early |
| Thriller | CU, inserts, wide isolation | high angles on the hunted, low on the hunter | slow creeping push, rack focus on clues | insert of the clue the detective has not noticed yet | showing everything; fast cutting in interrogations |
| Action | FS and MWS for readable choreography, inserts for impact | low for the hero, high for the fallen | tracking, follow, speed ramp, whip | one-take tracking fight with a hit-stop | shaky close fights you cannot read |
| Healing | WS and MS, hands at work in CU | eye-level, gentle chest-level | static, slow glide, long holds | locked-off wide of a ritual with ambient sound | dramatic angles, fast moves |
| Horror | wides with negative space, CU of reactions | slightly off-level, low in corridors | very slow push or none; sudden stillness | empty doorway held in a long static shot | revealing the entity early |
| Romance | two-shots measuring the distance, CU of glances and hands | eye-level; soft three-quarter front | slow push as they lean in, slow arc on the real moment | close two-shot of the near-miss | cold clinical framing |
| Fantasy | EWS of worlds, hero low angles, macro of relics | heroic low angles, god's-eye fate | crane, drone reveal, barrel roll in clashes | the relic in macro as its state changes | camera chaos without spatial anchor |
| Sci-fi | symmetric wides, inserts of interfaces (no readable text) | centred, clinical | slow precise dollies, locked frames | the cost made visible in a macro insert | jargon-heavy screens, cluttered frames |

---

## §11 — SCENE RECIPES (HOW TO SHOOT EACH SCENE TYPE)

| Scene type | 10s / 15s recipe |
|---|---|
| **Opening hook** | an anomaly in the first 3s: start on an Insert or CU of the wrong detail, then widen to context (or the reverse for scale) |
| **Two-person dialogue** | `Mode D1-A`: one static MCU two-shot or OTS for the whole clip · `Mode D1-B`: static OTS ➔ reverse OTS ➔ CU (escalating) · `Mode D1-C`: OTS ➔ macro insert of evidence ➔ CU reaction |
| **Confrontation / power reversal** | apply §3.4: start with height difference, equalise at the crack, invert at the reversal, end on a silent high-angle CU of the loser |
| **Group / table scene (3–6 people)** | first clip: a wide or overhead geography shot; then OTS/dirty singles only on the 1–2 people in conflict; others react in soft focus; the head of the table may be shot head-on for authority |
| **Phone / message / video call** | CU of the reader ➔ Insert of the screen (no readable text) ➔ CU reaction; for calls, cross-cut two singles keeping opposite eyelines |
| **Clue discovery / twist** | normal MS ➔ slow push or rack focus to the Insert ➔ CU attitude change; the camera may withhold, never lie |
| **V.O. / inner monologue** | CU or profile, static or very slow push; the eye-line shift carries the thought; hands in a tactile insert to close |
| **Reveal of a character** | feet or back first (tilt up / follow), face last; or a rack focus from foreground to the figure in the doorway |
| **Chase / action** | `@CombatDirector`: tracking or follow + inserts at impacts + a stillness landing |
| **Cliffhanger frame** | end on a held CU or a static wide with something entering; never end mid-motion blur |
| **Silent / healing scene** | locked-off MS or WS, long hold, one small movement inside the frame |

---

## §12 — MASTER COMBOS (SIZE + ANGLE + MOVE = ONE IDEA)

| # | Combo | Recipe | Use |
|---|---|---|---|
| 1 | Intimidation Tilt | low angle, tilt up from shoes to face | antagonist entrance |
| 2 | Isolation Pull-Out | CU ➔ slow pull-out to a solitary wide | abandonment after a loss |
| 3 | Chessboard Overhead + Dutch | overhead of the room, then a tilted CU | trapped by fate / madness |
| 4 | Vertigo Reveal | dolly zoom on the realising face | the horror of understanding |
| 5 | Surrounding Orbit | slow 360° around a person surrounded | overwhelm or union |
| 6 | Subjective Scanning POV | POV pans across a room, stops on the detail | discovery |
| 7 | Whistleblower Handheld | direct-address handheld | confession, exposé |
| 8 | **The Dawning Push** | static MS, then slow push to CU as the truth lands | realisation without words |
| 9 | **The Silent Verdict** | after the checkmate line, cut to a held high-angle CU of the loser, no sound but breath | power reversal payoff |
| 10 | **The Doorway Witness** | foreground door frame (soft), the scene seen from outside, someone overhearing | secrets, misunderstandings |
| 11 | **The Rack-Focus Accusation** | sharp on the evidence in the foreground, focus moves to the accused's face | interrogation, family showdown |
| 12 | **The Hero Rise** | low angle + slow pedestal up + backlight as the character stands | turning point, victory |
| 13 | **The Distance Two-Shot** | static two-shot; the space between two people is the subject; one steps closer at the end | romance, reconciliation |
| 14 | **The Smash-Cut Humiliation** | boastful CU, smash cut to the consequence in a wide | comedy, microdrama face-slap |

---

## §13 — WRITING CAMERA FOR AI VIDEO MODELS

1. **One camera instruction per shot**, written early in the shot line: `[size], [angle] targeting [Name], [move] , [speed tag]`.
2. **State the landing**: `…ending on a close-up of [Name]` — models drift when the end frame is unspecified.
3. **Prefer plain film vocabulary** (push-in, pull-out, pan, tilt, tracking, static) over invented poetry; add the motive in a clause.
4. **Avoid compound moves** ("orbit while zooming and tilting"); split them across shots.
5. **Keep subject motion and camera motion simple**: if two people move, lock the camera; if the camera travels, one subject moves.
5b. **Motion density** (`workflow.md` §2.5, `0c` §1): fill each shot's duration with one primary action stretched across preparation ➔ execution ➔ after-beat, one biological reaction and continuous micro-motion (breath, fingers, fabric, rain, steam, light flicker). A long shot with a one-second action invites the model to improvise; a short shot with three actions makes it morph. A static camera on a still subject is fine only when the subject breathes, blinks and reacts.
6. **Lip-sync shots**: FS to CU, static or very slow push, face unobstructed, frontal or three-quarter.
7. **Fast moves** (whip, crash zoom, FPV) belong in non-dialogue shots and need a stillness landing after.
8. **Commonly failing requests** — rewrite them:
   - Dialogue during an orbit ➔ static OTS, then a separate arc shot without lines.
   - Full-body dialogue in a crowd ➔ MCU on the speaker, the crowd as soft background.
   - ECU of lips speaking ➔ CU of the face.
   - Readable text on screens or paper ➔ show the reaction, keep the text unreadable.
   - Two characters crossing paths while the camera arcs ➔ lock the camera.
9. **Model differences**: behaviour varies by model and version (Seedance, Kling, Veo, others). Record what works for this project in `output/<slug>/project_rules.json → "camera_notes"` and reuse it; never assume one model's quirks apply to another.

---

## §14 — CAMERA PRE-FLIGHT (BEFORE EVERY SCENE PROMPT)

1. Can I state in one clause why each shot has its size, angle and move?
2. Does every shot target a named subject?
3. Does the angle reflect who holds power right now — and does it change when power changes?
4. Is there at most one camera move per shot, with a motive and a landing?
5. Are all speaking shots within the lip-sync safe sizes and static (or a very slow push)?
6. Is the 180° line kept, and does each cut change angle ≥ 30° or size by two steps?
7. Is the composition right for the aspect ratio (9:16 stacking vs 16:9 lateral)?
8. Does the clip end on a clean landing frame that the next scene can start from?

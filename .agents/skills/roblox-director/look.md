# look.md: shots, camera, faces, bodies, sets

> **v2 note (2026-11-14):** the rules and numbers here still apply. Roblox Studio tools named here (Luau CFrame/Motor6D poses, Animation Editor, Moon Animator, FieldOfView, BillboardGui) are replaced by the Blender kit — acting now comes from `studio_kit/blender_roblox_anim.py` (Law R-ANIM, `ROBLOX_DIRECTOR.md` §4; mocap/RoMixamo retired).


Tags: **REF-RANGE** = measured in the 6 reference reels (bell, memories, town, dog, monster, train; 458 shots). **HYPOTHESIS** = a beat-the-refs bet, not proven; A/B it on the user's own analytics.
Limits: no view or retention data exists for any ref, so "the refs do X" never means "X works". Never use `shots.json` `move` labels as evidence (wrong about half the time). Camera numbers below come from a background affine fit on frames, not from labels. Lighting and colour live in `lighting-color.md`; cut timing lives in `pacing.md`.

Key finding to remember: **the refs' "push-ins" are mostly centre-anchored 2D zooms with no parallax** (46 of 76 reliable fits, median leftover drift ≤0.9 % of frame width per second). They were most likely added in the edit, not shot as real camera moves. A real in-engine move is the easiest visible upgrade.

How this file relates to the user's studio rules: `scene-rules` still applies (no camera spin, no clipping, nobody facing the wrong way, roll 0). One exception: scene-rules' "nothing on screen at second 0" is about titles and labels in code-built videos. In these reels the **world** is on screen and moving at frame 1. No title or label is; captions arrive with the first word.

---

## 0. The numbers on one page

| # | rule | target | refs | tag |
|---|---|---|---|---|
| L1 | Close shots (CU + MCU + ECU) | **≥25 %** of shots | 4–31 %, pooled 14 % (62/458) | HYPOTHESIS |
| L2 | Medium shots | **≤40 %** | 29–55 %, pooled 42 % | HYPOTHESIS |
| L3 | Wides (WS + EWS) | 15–30 % | 5–39 %, pooled 23 % | REF-RANGE |
| L4 | Inserts (object or text, no face) | 8–12 % | 3–12 %, pooled 8 % | REF-RANGE |
| L5 | Readable face (eyes and mouth visible, ≥4 % of frame height) | **≥60 % of shots, 100 % of key lines** | 27–64 %, pooled 45 % | HYPOTHESIS |
| L6 | Non-eye-level angles | **≥35 %** | 13–33 %, pooled 25 % | HYPOTHESIS |
| L7 | Shots with a real in-engine camera move | **≥70 %** | 67 % of sampled ref shots move at all, almost all as 2D zooms | HYPOTHESIS (70 %) on a REF-RANGE base |
| L8 | Edit-zoom-only shots / fully static shots | ≤20 % / ≤10 % | refs: about 61 % edit-style zooms, about 30 % static | HYPOTHESIS |
| L9 | Shot length | median 1.3–2.0 s; **no shot >3.5 s** except 1–2 designed holds of 4–6 s | medians 1.13–2.93 s | REF-RANGE (cap from pacing.md) |
| L10 | First shot | moves at frame 1; rule object readable in frame 1; first cut by 2.5 s | 5/6 show the rule in shot 1 (dog waits 18 s) | REF-RANGE + HYPOTHESIS (2.5 s) |
| L11 | Rule object on screen, readable | in shot 1 and in **≥50 %** of shots. A mark on the body counts only at MS or tighter (or where it is ≥2 % of frame height): tag RULE only there | 13–71 % | HYPOTHESIS (50 %) |
| L12 | Every rule-state change | an object or decal change **within 1 shot** | bell #30 grey bell right after "it stopped" | REF-RANGE (best ref) |
| L13 | Emotion swap | face decal changes **within ±3 frames (±0.1 s)** of the key word | bell #24 at 49.7 s, memories #41 at 111.8 s | REF-RANGE |
| L14 | Mouth flaps on on-screen dialogue | **2–3 swaps/s** | only monster #130 (every 0.3–0.5 s) and train #51 | REF-RANGE (n=2) |
| L15 | Stiff idle bodies | **≤40 %** of shots; posed or animated on **≥35 %** | stiff 39–76 %, pooled 56 %; custom pose 16 % | HYPOTHESIS |
| L16 | Locations | **5–8** per 60–120 s; a new location on average every ≤10 s | 3–9; every 5.2–14.3 s | HYPOTHESIS |
| L17 | Same setup (set + size + angle family, whoever is in it: "low 10°" vs "low 12°" is the same angle) | **≤2 times** per video | memories ×8, town ×6, dog ×4, monster ×4 | HYPOTHESIS |
| L18 | Final shot | **≥3 s**, on the rule object's final state | bell 6.07 s, memories 5.3 s; town, dog, monster 0.9–1.07 s | REF-RANGE (best 2) |
| L20 | Move variety | no move type (push, truck, crane, orbit, pan…) on >40 % of shots; ≥3 types | round-1 plan: push-ins on 57 % (the in-engine version of the refs' edit zooms) | HYPOTHESIS |
| L19 | Hero avatar | custom, never the default "noob" or any Classic Avatar | bell + memories use the noob; town = dog avatar | HARD (Roblox Creator Terms bar Classic Avatars in off-platform film) |

---

## 1. Shot sizes

Sizes used in the shot list: EWS, WS, MS, MCU, CU, ECU, OTS, INS (insert).

- **Close shots ≥25 %** (L1, HYPOTHESIS). In a 70-shot reel that is ≥18 CU/MCU/ECU. Put them on: every key line, every decal swap that carries the story, the twist line, and the reaction right after the twist.
- **MS ≤40 %** (L2). MS is the refs' default "nothing shot". When a shot list has two MS in a row, make one of them a CU or an OTS.
- **WS/EWS 15–30 %** (L3). One establishing wide per new location, then go in. The world-rule wide (the whole street, the whole valley) counts here.
- **Inserts 8–12 %** (L4). Use them for rule-state changes, signs, notes and props, not as filler.
- **Readable face** (L5): eyes and mouth visible and at least 4 % of frame height (about 77 px at 1920). Faces are hidden on key lines in the refs (town #77 "I cried" shows the back of the head; dog #29 "I yelled" hides the face). **A key line never plays on the back of a head.**
- Step-ins on the same angle (bell #20 → #21, MCU → CU) are fine once per scene, as a deliberate emphasis.
- **Keep the caption band clear** (captions.md HARD rule: no caption over a face or the rule object). Captions sit at 70 % of frame height, so faces, the rule object and readable signs stay **above 55 % of frame height (y < 1056)**. In a CU/ECU put the eye line at about one third of the frame height and the chin above 55 % (HYPOTHESIS: framing habit). A rule object on the body (a mark on the cheek) is framed like a face. A rule object on the ground or low on a wall (footprints, shadows) needs a high angle (the ground plane rises into the top half) or a low camera aimed up the wall; write the framing in the shot notes.

## 2. Angles and lenses

- **Non-eye-level ≥35 %** (L6, HYPOTHESIS). Low angle (camera 1–2 studs below eye line, tilted up 10–20°) for threat, power and the rule object looming. High angle (2–4 studs above, tilted down 20–35°) for isolation and smallness. Top-down for "everyone at once" shots. Keep eye level for honest dialogue.
- **Dutch tilt**: ≤5° roll, only on chaos beats, never two shots in a row (scene-rules: roll is 0 otherwise).
- **Lens** (Roblox `Camera.FieldOfView` is the vertical FOV; HYPOTHESIS from the Moon Animator guide's 20–50 range): CU/MCU 30–40°, MS/OTS 40–55°, WS 55–70°, EWS 60–70°. The default 70° on a close-up bends blocky heads and shows too much set.
- OTS: the near shoulder fills 15–30 % of the frame width and is out of focus if DOF is on; the far face is readable. The camera stays on one side of the line between two talkers for the whole scene (scene-rules 180° rule).

## 3. Camera moves: in-engine vs edit zoom

### 3.1 How much
- **≥70 % of shots have a real in-engine move** (L7). Default move: **slow push-in**, but no move type on more than 40 % of shots (L20): mix trucks, orbits, cranes and static frames with motion inside them. Speeds:

| situation | speed | tag |
|---|---|---|
| dialogue, narration, realisation | push-in **3–8 % per second** (image scale) | HYPOTHESIS inside the ref range (+0.7 to +12.6 %/s medians) |
| punch on a key word | up to **20 %/s** for ≤1 s | REF-RANGE (bell twist +13.7 to +20.5 %/s) |
| walker | truck beside them at their walk speed, ≥2 % of frame width per second | HYPOTHESIS (train #40 is the one ref that does it) |
| ending | pull-out 2–4 %/s | HYPOTHESIS (bell #35) |
| reveal | orbit ≤30° total, ≤20°/s (scene-rules), from back-of-head to face | HYPOTHESIS (no ref does it with the camera) |

- Turning image speed into studs: a push-in toward a subject at distance *d* studs grows the image by about *v / d* per second. So **5 %/s at 8 studs = move the camera 0.4 studs/s**; at 4 studs (a CU) it is 0.2 studs/s. A 2 s shot at 5 %/s from 8 studs ends at 7.2 studs.
- Ease every move (Sine InOut, or a long ease-out on the push). Aim at a fixed invisible target part, never at a character who walks near the lens (scene-rules: that flips the camera).

### 3.2 When to use which

| use an **in-engine move** (camera CFrame / FOV tween in Studio) | an **edit zoom** (scale keyframe in the editor) is OK |
|---|---|
| any shot with depth: WS, MS in a set, OTS, low and high angles; parallax is the point | flat subjects: full-screen notes, phone and UI screens, signs shot straight on (they have no depth, so parallax can't show) |
| walker follows, orbits, crane-downs, the twist dolly-zoom or rack focus | a one-frame punch step on a key word (100 → 105 %) on top of an in-engine move |
| every emotional push-in on a face (the background should slide behind the head) | rescuing a take that came out static: ≤ +5 % over the whole shot |
| | stills made with `screen_capture` (they can only move in the edit) |

- **Edit-zoom limit: ≤ +5 % total** on a 1080×1920 capture (HYPOTHESIS: more than that softens the image). If the viewport can be captured bigger than the output (see pipeline.md step 0), the limit rises to output-size ÷ capture-size, for example +33 % for 1440×2560.
- **FOV zoom in-engine** (changing `FieldOfView` without moving the camera) is optically the same flat zoom as an edit zoom, but without softness. Use it for punches; use a physical move (dolly) for everything else.
- Edit-zoom-only shots ≤20 %, fully static shots ≤10 % (L8). A static shot must be a choice ("everything freezes before the scare"), written in the shot list notes.

### 3.3 The twist move (pick one per episode, rotate)
One move on the twist line that no ref uses (U8, HYPOTHESIS):
- **Dolly-zoom**: move the camera back while narrowing the FOV so the face stays the same size. Keep *d* × tan(FOV/2) constant: FOV₂ = 2·atan((d₁/d₂)·tan(FOV₁/2)). Example: from 6 studs at 40° to 10 studs → 24.6°, over 1.0–1.5 s. In scene data: `dolly = { at = 0.3, dur = 1.2, to = 10 }` on the shot (pipeline.md Appendix A); the runner does the math inside the shot. `camFn` is the general per-shot override for any other move.
- **Rack focus**: DOF `FocusDistance` tweens from the near object's distance to the face's distance (or the reverse) over 0.4–0.8 s, starting on the twist word: `P.rack(from, to, secs)` in the lighting module, or `rack = {at, from, to, secs}` on the shot in scene data. This shot is the one DOF exception: DOF is on even if the mood has it off, `NearIntensity` ≤0.5, `FarIntensity` ≤0.5; the next cut restores the mood's DOF.
Alternate the two between consecutive episodes.

## 4. Shot length
- Median 1.3–2.0 s, mean 1.3–2.5 s, 20–48 cuts per minute (REF-RANGE; details in pacing.md).
- **Cap 3.5 s** per shot. Exceptions: 1–2 designed holds of 4–6 s at the reveal and/or the ending, each with a slow move and no cut inside (REF-RANGE: bell 6.07 s, memories 6.03 s).
- Cuts land on sentence starts, 0–2 frames before the first word (pacing.md). The shot list is built from the word timestamps, so this falls out of the plan.

## 5. The first shot
- **Frame 1 already moves** (L10): an in-engine push, track or crane-down. A whip/zoom "settle" (5/6 refs, 0.13–0.2 s, flow 6.5–10.8 px against a median ≤0.6 px) is an **option only**: use it when the story motivates it (impact, speed) and **never in two consecutive episodes**.
- **The rule is visible and readable in frame 1**: the rule object, sign or creature, not just the caption. Best composition: hero + rule object (+ threat) in one frame (monster #1).
- First cut by 2.5 s, shot 1 ≤3.0 s, ≥2 shots in the first 3.5 s (HYPOTHESIS; refs hold shot 1 for 0.7–4.2 s).
- One decal swap on the hook's key word (bell #1 swaps to shocked on "you" at about 3.7 s).

## 6. Showing the world rule on screen
- **Every rule-state change = an object or decal change within 1 shot** (L12): the bell turns grey, the lantern goes out, the coin drops. Write the change in the shot list's props column. It gets the rule-object sound only while audio.md §3's cap allows (≤2 before 65 %); act-1 examples beyond the cap stay silent.
- **Rule object in ≥50 % of shots** (L11). Dress every set with it (signs, the object over doors, a UI screen).
- What reads fastest in the refs (look-analyst ranking, opinion from frame review): (1) an object attached to every character that changes state (bell); (2) a creature or prop in frame (monsters, coins); (3) signs, labels and UI text; (4) face-decal states (tears); (5) full-screen text inserts. Prefer 1–2; use 3–5 as support.
- **Full-screen text inserts** (notes, letters, screens): held **≥1.8 s** (REF-RANGE: dog #9 2.5 s, town #57 2.1 s), text cap height ≥3.5 % of frame height (about 67 px; HYPOTHESIS), ≤12 words.
- Signs in the set: SurfaceGui + TextLabel (bold font, high contrast), facing the camera (scene-rules), never inside the caption band (55–80 % of frame height) when they need to be read.

### 6.1 Abstract rule objects: shadows, light, sounds, invisible marks

Roblox can't make a shadow show anything but its caster, can't show a sound, and can't show what's invisible. Fake them cheaply, and **count every distinct image or state against the build caps** (pipeline.md: ≤12 rule-object images; the first system you build is 1 special build, reused for free after).

| rule object | cheapest method | notes |
|---|---|---|
| **story shadows / silhouettes** | black PNG silhouettes (soft 4-8 px edge baked in, ImageTransparency ~0.3) on a SurfaceGui (or Decal) on a thin non-colliding, CanQuery-off part 0.02-0.05 studs off the wall, ground or curtain. Move them with TweenService (an ImageLabel sliding inside a `ClipsDescendants` frame), change them with the ShotRunner's `shadows` events (`setShadow`, images in a `ShadowLibrary` module) | test `LightInfluence` 0 vs 1 on the first set (UNVERIFIED which reads better). A lamp "erasing" a shadow = ImageTransparency 0.3 → 1 over about 6 frames. A shadow across road and wall is two parts split at the kerb seam, lined up per shot with `screen_capture` |
| real shadow puppet (one test) | an opaque cut-out part outside the frame, between a shadow-casting SpotLight and the wall; Realistic lighting casts it for free | UNVERIFIED; a Transparency-1 part casts no shadow, so the puppet must be opaque and off-frame |
| real cast shadows | keep `CastShadow` on for rigs, and turn it off only on shots where a story shadow shares the surface, or add a dark contact-blob decal under the feet | rigs with no shadow float in sunlit wides |
| long shadows | the light sits low and behind the caster (headlights, a porch light); a streetlight overhead makes a short shadow at the feet | the real set shadows must agree with the fake ones |
| curtains and windows | a Fabric part at Transparency ~0.2 with a warm PointLight behind it, the silhouette on the outside face | |
| **sounds** (a rule that is heard) | show the source reacting: a ParticleEmitter ring from the object, the object shaking (a 2-frame CFrame jitter), a light that pulses with it, heads turning; the SFX carries the rest | one visible proxy per sound, used every time (it becomes the rule object) |
| **invisible marks / auras** | a reveal device makes them visible on screen: a UV torch, a phone camera (a SurfaceGui "screen" showing the mark), dust or rain settling on it, the mark visible only in a mirror shot | the device is the rule object: in shot 1 and in ≥50 % of shots (L11) |

For any rule object tied to windows, walls or a street, draw a top-down diagram (rooms, windows, light sources, camera side) before the shot list: left and right flip between inside and outside (script.md §3.4).

## 7. Emotion: own-PNG face decals

### 7.1 The face kit (the user's own PNGs, his own IP)
Three Decals on the Head, Face = Front, all named and layered: `Eyes` (ZIndex 1), `Brows` (ZIndex 2), `Mouth` (ZIndex 3). Each PNG is a 512×512 transparent canvas (1024×1024, Roblox's upload maximum, for any layer seen in ECU) with the part drawn in its final position, so the layers line up without offsets. Lines ≥12 px at 512 (they must read at MS size).

Minimum kit per character (HYPOTHESIS: enough for the refs' range of emotions):
- Eyes: open, half, closed, closed-happy, wide, look-left, look-right, cry (tear streak)
- Brows: neutral, sad, angry, raised
- Mouth: closed-neutral, smile, frown, open-small, open-big, O, gritted

**Rules that live on the body** (a crack, a mark, a glowing date, tears that stay) get a 4th Decal on the Head named for the rule (`Mark`, ZIndex 4, same canvas, 1024 px if it is seen in ECU) and drawn **inside the front face area** (a Front decal can't reach the ear) with staged states: forming 25 / 50 / 75 / 100 %, then any shrink or gone states the story needs. The ShotRunner's `setFace(rig, "Mark", state)` swaps any named decal on the Head, so a forming mark is a run of `faces` events 1 frame apart; a mark on another body part is set from an `events` fn.

8 × 4 × 7 = 224 combinations from 19 PNGs. Store the asset IDs in a `FaceLibrary` ModuleScript (`FaceLibrary.Hero.Mouth.O = "rbxassetid://…"`). **Run the 2-minute decal test in templates/mcp-setup.md before drawing the full kit.**

### 7.2 Timing
- **Emotion swap on the key word ±3 frames** (L13). Two ways, both REF-RANGE: cut to a new shot whose face already shows the emotion (bell #33, memories #52), or swap in-shot on the stressed word (bell #24). Brows may lead the mouth by 2–4 frames (HYPOTHESIS: reads as a thought before the reaction).
- Hold an emotion face ≥0.5 s before the next change (HYPOTHESIS), unless it is a flap.
- **Mouth flaps** (L14): only when the character speaks a quoted line on camera. Alternate open-small / closed (open-big on stressed words) at **2–3 swaps per second**, closed during pauses ≥0.15 s. Narration over a shot is not dialogue: the hero's mouth stays shut. If a quoted line has no flap, use a speech bubble (BillboardGui) instead (bell does this 4 times).
- **Blinks**: eyes closed for 3 frames (0.1 s) every 3–4 s, never during a key word (HYPOTHESIS; none of the 6 refs blink).
- Eyes look toward whoever is talking or toward the rule object; only look into the lens when the hero talks to the viewer.

## 8. Body animation
- **Stiff idle ≤40 % of shots; posed or animated ≥35 %** (L15). Nobody stands frozen in an MS while they talk (bell #10 "Everyone laughed": nobody moves).
- Everyone not acting gets a breathing idle: torso bob 0.05 studs on a 2–3 s cycle, head turn 5–10° toward the speaker (HYPOTHESIS, craft note).
- **R6 tools** (rigs are R6, like the refs):
  - Built-in Animation Editor: free, enough for simple acting.
  - **Luau CFrame poses**: Claude writes poses as `Motor6D.C0` offsets on the R6 joints (Neck, Right/Left Shoulder, Right/Left Hip, RootJoint) and tweens between them. Cheapest route through the MCP. The joint axes differ per joint; test each new pose once with `screen_capture` and save it in a `PoseLibrary` module.
  - **Moon Animator 2**: about $30 one-time. Multi-rig timeline, camera track, marker-driven face swaps in Edit mode. **Ask the user before buying.** Buy it only if the free routes fail the first test.
  - ~~RoMixamo~~ — retired. Human mocap does not read as Roblox (see `ROBLOX_DIRECTOR.md` §4 Law R-ANIM). Studio: official R15 animation ids; Blender: `studio_kit/blender_roblox_anim.py`.
  - **Not** the MCP's `generate_animation`: it makes R15 animations only, up to 10 s. Useless for R6 acting.
- Starter pose library (8 poses, HYPOTHESIS): point, hand-to-face, head-drop slump, flinch, hug/hold, hands-on-head, kneel, reach-out. Each has a 6–12-frame ease in and holds ≥0.4 s on emotional beats.
- Turn before walking (≥0.3 s, scene-rules). Feet on the floor; held props welded to the hand.

## 9. Sets and cast
- **5–8 locations per 60–120 s** (L16), 6–9 for 3 min. One location per scene, a new one on average every ≤10 s.
- **Dress every free map with 2–3 story props** (signs, labels, the rule object, a UI screen, a handwritten note).
- **Avoid the shared free school map** (blue-locker hallway, the classroom with the bulletin board and grey lockers): bell and memories both use it. If the story needs a school, use another map and change wall colours, materials and 3 props.
- **No setup more than twice** (L17): a setup is set + size + angle family. The checker counts repeats.
- **Hero = a custom avatar** (L19, HARD). Built on a Rig Builder R6 rig with the user's own face PNGs, own shirt and pants textures, and **one saturated signature colour that reads at EWS size** (benchmark: monster's bee stripes + orange backpack). Lock him in a cast file (`reels-shorts/cast/<name>.md`: name, signature colour, outfit, face-kit decal IDs, signature prop) and reuse him across episodes. A recurring original cast also counts against YouTube's "inauthentic content" templating rule. **If no cast file exists yet** (or you can't see that folder), describe the hero in the shot list with those 5 fields, mark it "new: needs the user's OK", and write the cast file after he approves; never invent a second hero when one exists.
- Each supporting character owns one costume colour that reads at WS size. Captions keep the episode's one accent colour (captions.md §1.1); a character's colour shows on their costume and speech bubble, not in the captions.
- Hair and accessories from the Creator Store are the same grey zone as free maps (fine to record in Studio). The hero's look should not depend on one of them (keep it portable).

## 10. VFX, props and signs
- Particle VFX instead of flat shapes (HYPOTHESIS): a ring shockwave ParticleEmitter + gold glint when a rule object fires (not bell's flat white ellipse); a trail and glow on floating objects (not memories' plain sphere); a beam or aura for magic speech (not dog's yellow square).
- The rule object glows: Neon material + a PointLight (lighting-color.md `practical()`), so it is the brightest thing in frame (p99 ≥240).
- Every VFX burst gets a matching SFX hit (audio.md).
- **Prop deaths** (a loss shown by the object left behind: monster's hat, shoe, slack rope) are an **option, used in at most every other episode**. Never "always".
- Numbers as props or captions are good specifics ("31" weddings, "200" dates in monster).
- Roblox can't render some common story shots: see §16 before writing a mirror, a foot insert or a speech bubble.

## 11. The ending shot
- **≥3 s on the rule object's final state** (L18). Default: slow pull-out at 2–4 %/s. Music resolves under it (audio.md).
- No 0.9–1.07 s back-of-head ending (town, dog, monster). If the face is hidden, it is a choice and the rule object carries the shot.
- **Mirrored bookend** (the last shot echoes shot 1, like train #66 vs #1): an **option, at most every other episode**.

## 12. Continuity checks (run on the shot list, then on stills)
- [ ] The set matches the line (bell #6 says "lunch" in the classroom).
- [ ] Every sound gag has its object on screen (town "Clink" #78 shows only a shoulder).
- [ ] One flashback grade for the whole episode (`dreamMemory`); every flashback shot uses it (monster and town mix graded and ungraded flashbacks).
- [ ] Outfit, hair, face kit and signature prop are the same in every shot of a character.
- [ ] Time of day and mood stay fixed inside a scene (brightness within ±0.08, warmth within ±0.10; lighting-color.md).
- [ ] 180° line held in every two-person scene; eyelines meet.
- [ ] Feet on the floor, nothing clipping, held props welded (scene-rules).
- [ ] The rule object's state is right in every shot (a lantern that went out stays out).
- [ ] No Roblox logo, no Studio UI, no selection outlines, no cursor in any frame.

## 13. What all 6 refs do weakly, and the upgrade

| weakness (evidence) | upgrade | rule |
|---|---|---|
| Fake camera: about 61 % of reliable fits are flat 2D zooms; only train trucks for real | in-engine push-ins, trucks, orbits; edit zoom only on flat inserts | L7, L8, §3 |
| Few close shots (14 %) and faces hidden on key lines (town #77, dog #29) | CU/MCU ≥25 %, readable face on every key line | L1, L5 |
| Stiff bodies (56 % stiff idle), no lip movement in 4/6 | pose library + breathing idle; flaps at 2–3/s on dialogue | L14, L15 |
| No blinks, no eye direction | blink every 3–4 s; eyes to the speaker | §7.2 |
| Same setup repeated (memories ×8, town ×6) | ≤2 per setup | L17 |
| Free maps and default avatars (shared school map, noob MC, town = dog MC) | custom hero, dressed sets, no shared school map | L19, §9 |
| Rule shown in only 13–17 % of shots in memories, dog, train | rule object in ≥50 % of shots; state change within 1 shot | L11, L12 |
| Flat VFX (2D halo ellipse, plain sphere, yellow square) | particles + glow + matching SFX | §10 |
| Abrupt endings (3/6 end on ≤1.07 s, no face) | ≥3 s final shot on the rule object | L18 |
| Continuity slips (lunch in the classroom, mixed flashback grades) | §12 checklist | §12 |
| No twist camera language (no dolly-zoom or rack focus in any ref) | one per episode, alternating | §3.3 |

## 14. Rotate between episodes (anti-template)
Whip intro, mirrored bookend and prop deaths (each at most every other episode), the twist move (dolly-zoom ↔ rack focus), lead location type and where the rule object lives rotate between episodes. Rules: `templates/rotation-log.md` (optional rows 13-18). Hold placement is in pacing.md.

## 15. Self-checks (zero tokens, on the user's Mac)

- **Shot list:** `python3 tools/shotlist_check.py shotlist.md` (format in `templates/shot-list.md`) before anything is built. It checks L1-L11, L15-L18 and the mood names, and prints L12 / L14 counts. On a partial list (a 15 s test scene) L16 and L18 are informational only.
- **Move check on a recorded take** (did each shot really move?): `python3 tools/move_check.py take.mp4 cuts.txt`, where `cuts.txt` holds one shot start per line, starting at 0. It cannot tell an in-engine move from an edit zoom (both fit the same 2D model); the shot list says which is which. Tested on the bell reference: it reads bell #19–#23 as +13 to +21 %/s zoom-ins, matching the look analysis.

## 16. Roblox limits (check before writing a shot)

| limit | so | tag |
|---|---|---|
| No real reflections (no mirror rendering; glass and water show only the sky and lights) | write mirrors, shop windows and puddles so the reflection is never needed, or fake a mirror: the camera sits where the mirror is, behind a thin glass part, and the actor looks into the lens (the one other allowed look into the lens, §7.2) | craft note, HYPOTHESIS until a capture |
| R6 limbs are blocks: no feet, no fingers | no foot inserts ("his shoes on my sneakers"), no finger or hand-detail inserts; show the whole body instead | fact (R6 rig) |
| Contact between two rigs (hand-holding, a hand on a cheek, stepping on feet) is the hardest pose work in the pipeline | ≤3 contact poses per episode (pipeline.md Build budget) | HYPOTHESIS |
| DOF works off depth; whether a mostly transparent part (Transparency ~0.85) counts as a focus target is UNVERIFIED | rack-focus targets are opaque parts (a toothbrush, a photo frame); test the rack with `screen_capture` before building the twist around it, and keep a dolly-zoom as the fallback | UNVERIFIED |
| A BillboardGui bubble sits above the head | speech bubbles only on MS or wider; in a CU it is off frame or over the face, so let the narration carry the line | fact |
| Images upload at most 1024 px | decals seen in ECU on a 1024 canvas; even then an ECU of a small decal area is soft, so keep marks large and simple | fact (upload cap) |
| A Front-face decal covers only the front of the head | body marks stay inside the front face, or add a matching side decal | fact |
| A shadow only copies its caster; sounds and invisible things can't be seen | fake them (§6.1) and count the images against the build caps | fact |

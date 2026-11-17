# lighting-color.md: renderer, moods, colour script, measurement

> **v2 note (2026-11-14):** colour targets, moods, twist shift and measurement (§2–6) still apply. Roblox renderer settings (§1, `LightingStyle`, Studio quality, `lighting-presets.lua`) are replaced by `k.apply_look()` in Blender — see `blender.md` §1.


Tags: **REF-RANGE** = measured in the 6 reference reels. **HYPOTHESIS** = a beat-the-refs bet; A/B it on the user's own analytics.
Metrics (all 0–1 unless noted, measured on a frame with the top and bottom 8 % cut off): **bright** = mean HSV value, **sat** = mean HSV saturation, **contrast** = std of grey, **warm** = mean (R − B)/255, **p1 / p99** = 1st / 99th percentile of grey (0–255), **clip** = % pixels ≥250, **crush** = % pixels ≤12. For the refs, p99 means "mean of per-shot keyframe p99".
Limits: the refs are 720p re-encodes with captions burned in, so their numbers carry some caption leak. **Always measure the user's renders caption-free**: white captions clip at 255 and would pass the highlight and practical tests falsely. All Studio values are starting points until a test capture passes §6.

---

## 1. Renderer settings (HARD)
- `Lighting.LightingStyle = Enum.LightingStyle.Realistic` and `Lighting.PrioritizeLightingQuality = true`. **Never write `Lighting.Technology`** (deprecated; superseded by those two). `ShadowSoftness` only works with Realistic.
- Studio → File → Studio Settings → Rendering: **Editor Quality Level 21** (max) and **Mesh Detail Level00**. Post effects may not show at lower quality.
- After inserting a free map, run `P.cleanFreeModelFx()` (templates/lighting-presets.lua). Free maps bring their own ColorCorrection, Bloom, Blur and extra Atmospheres, which stack on top of ours.
- Indoors, don't raise `Lighting.Brightness` to fix a dark room: Roblox's indoor guide says it makes shadows murky. Add a practical instead (§5). Walls ≥1 stud thick so light doesn't leak.

## 2. Targets for a finished episode (measured with `measure.py`, §6)

| # | target | refs | tag |
|---|---|---|---|
| C1 | **Median sat 0.35–0.50** | per-video medians 0.32–0.55; town 0.55 and dog 0.49 read loud | REF-RANGE band |
| C2 | **≤10 % of shots with sat >0.60** | town 40 %, dog 22 % fail; train 0 % | REF-RANGE (fixes the worst refs) |
| C3 | **p99 ≥240 in ≥25 % of shots**, and p99 <225 in ≤50 % | town 71 % and monster 92 % of shots under 225 fail; dog passes (33 % ≥240, 45 % <225) | REF-RANGE |
| C4 | **p1 10–25** in ≥80 % of shots; crushed pixels ≤5 % in every shot | town/monster/dog p1 7–9, crushed >10 % in 20–23 % of their shots | REF-RANGE target; 80 % tolerance is HYPOTHESIS. Fog, snow or whiteout shots may sit above 25 on purpose |
| C5 | No hue family >40 % of all pixels | dog orange 41 % fails; town 35 % passes (palette method). measure.py counts brown as orange, so it reads town 44 %, dog 43 %, monster 33 %, train 24 %: treat 40 % as approximate | REF-RANGE |
| C6 | Inside one scene: brightness within ±0.08, warmth within ±0.10 shot to shot | refs jump 0.08–0.17 between adjacent shots (memories 0.166) | HYPOTHESIS |
| C7 | **Deliberate shift on the twist cut**: at least one of bright, sat, warm moves **≥0.15** (4 s after vs 4 s before); 0.10 is the minimum pass | refs have no twist signature: dBright +0.003, +0.009, +0.037, −0.095, −0.001, +0.162 at the canonical twist times | HYPOTHESIS (the beat-the-refs lever) |
| C8 | Ending warmer than the rule section by **≥ +0.10** warm | memories +0.18, train +0.17, monster +0.26, dog +0.10; bell +0.07, town +0.03 | REF-RANGE (4/6) |
| C9 | Night: bright 0.25–0.35 **and** sat ≥0.40, with one coloured glow (≥1 % of pixels >240) | refs keep sat 0.39–0.55 at night | REF-RANGE |
| C10 | ≥1 visible practical in ≥80 % of interior shots (clip ≥1 % of pixels, caption-free) | refs mostly light interiors with no visible source (town 0 % of shots >5 % clip) | HYPOTHESIS |
| C11 | Sad → payoff: the reveal is ≥0.25 brighter than the sad scene | memories (0.27 shop → 0.81 Ollie room); bell hospital is the sad match | HYPOTHESIS from 2 refs: **flip it in ≥1 of every 4 episodes** (payoff goes dark) |
| — | Vignette, heavy "cinematic" grade | refs have none (corner ÷ centre 0.99–1.19) | OPTIONAL style only; no evidence it helps |

## 3. Mood presets (full values in `templates/lighting-presets.lua`)

Key values below; every preset also sets Atmosphere Color/Decay, Bloom Size, CC TintColor, SunRays and DOF so switching never leaves stale values.

| mood | matched ref shots | Brightness / ClockTime / Exposure | Ambient | Atmosphere Density / Haze | Bloom Int / Thr | CC Contrast / Saturation | DOF Far / InFocus | calibration target (b / s / c / w) |
|---|---|---|---|---|---|---|---|---|
| **normalDay** | memories 14–61 s classroom (b .68 s .45 c .25 w +.02); dog 0–23 s street and living room (b .71 s .52 w +.15) | 2.5 / 14.5 / +0.3 | 95,90,85 | 0.25 / 0.3 | 0.35 / 1.0 | +0.08 / +0.05 | off | 0.62–0.72 / 0.42–0.52 / 0.22–0.26 / +0.02…+0.15 |
| **sad** (cool, soft) | bell hospital #19–#23, 38.7–45.4 s (b .52 s .32 c .18 w −.09) | 1.2 / 11 / −0.4 | 70,85,110 | 0.35 / 1.0 | 0.25 / 1.0 | −0.05 / −0.22 | 0.3 / 8 | 0.48–0.55 / 0.28–0.34 / 0.16–0.20 / −0.12…−0.05 |
| **sadWarm** (bright, blown window) | memories Ollie room #49–#57, 133–160 s (b .81 s .40 c .21 w +.26) | 3 / 15 / +0.5 | 140,125,105 | 0.2 / 0.6 | 0.8 / 0.8 | −0.04 / −0.08 | off | 0.76–0.84 / 0.36–0.44 / 0.19–0.23 / +0.20…+0.30 |
| **scaryNight** (dark, not grey) | memories shop #39 98.1 s (b .14 s .55, cyan jars) and 98–108 s (b .27); train tunnel 46.6–72 s; town clink night 49–74 s | 0.6 / 0 / −0.5 | 28,32,48 | 0.45 / 1.8 | 0.6 / 0.85 | +0.05 / **−0.05** | 0.5 / 6 | 0.25–0.35 / 0.40–0.55 / 0.17–0.21 / −0.03…+0.05 + one coloured practical |
| **twistReveal** (golden pop, contrast drops) | memories #45–#49, 121.3–133.3 s (b .82–.94 w +.17…+.40; contrast −0.095 at the cut) | 3.5 / 16.5 / +0.7 | 150,130,110 | 0.3 / 0.8 | 0.9 / 0.75 | −0.05 / 0 | off | 0.80–0.92 / 0.28–0.45 / 0.15–0.20 / +0.18…+0.35; hold 3–6 s |
| **twistNight** (night palette swap, no ref) | none: HYPOTHESIS, for a twist that happens at night (blue → amber at about the same darkness) | 0.8 / 0 / −0.1 | 70,52,40 | 0.35 / 1.2 | 0.8 / 0.8 | −0.03 / 0 | off | 0.38–0.48 / 0.40–0.50 / 0.17–0.21 / +0.12…+0.25 (≥0.15 warm shift from scaryNight) |
| **dreamMemory** (the one flashback grade) | dog flashback crib #37–#41, 64.5–81 s (b .61 s .41 w +.01, blue room + yellow glowing eyes); memories #12 30.2 s pink sunset | 1.5 / 19.5 / 0 | 80,85,140 | 0.4 / 1.2 | 0.7 / 0.8 | −0.10 / 0 | 0.5 / 4 | 0.55–0.65 / 0.38–0.46 / 0.19–0.23 / −0.02…+0.05 |

All preset values are HYPOTHESIS; the targets are REF-RANGE (measured on the matched shots).

**Time of day is separate from mood.** Write a mood as `mood@clock` in the shot list and scene data (`normalDay@21` = the normalDay look at 9 pm, `twistReveal@21` = the twist grade with no sun in the window); `P.apply` and the ShotRunner read the same string, and `P.setTime(clock)` changes only the clock. A night clock on a day mood is an interior lit by practicals: re-measure it, and fix a dark room with practicals or Ambient (§1), not Brightness. Anything else (a warmer Ambient, a tint) is a variant: `P.variant("sad", "sad_bathroom", {lighting = {...}})`, defined in a ModuleScript `ReplicatedStorage.EpisodeMoods` that RunScenes requires before playing (pipeline.md Appendix A), so the variant exists in Play mode too.

**Night versions of sad moods.** At night C9 (sat ≥0.40, one coloured glow) beats a preset's day saturation: use `sad_night` / `sadWarm_night` (in the module, HYPOTHESIS values), not `sad` at sat 0.28–0.34.

**Rack focus and per-shot DOF.** `P.rack(from, to, secs)` turns DOF on for one shot (Near/Far ≤0.5) and tweens the focus; in scene data write `rack = { at = 0.4, from = 1.2, to = 4.0, secs = 0.6 }` on the shot and the ShotRunner restores the mood's DOF on the next cut. Focus targets are opaque parts (look.md §16).
Changes from the team draft, per the critic: night saturation stays at −0.05 (never −0.3); DOF `FarIntensity` is capped at 0.5 everywhere (dreamMemory was 0.8); no vignette in the module.

## 4. The colour script of an episode
1. **One mood per scene**, chosen in the shot list's mood column. Keep C6 inside a scene. The mood changes in exactly three ways: (a) on a scene cut, hard, no tween; (b) on the twist cut, hard, no tween (point 2); (c) inside a scene only when the story changes the light (a lamp goes out, the twist grade steps down while the scene goes on): point 5.
2. **A deliberate shift on the twist cut** (C7, HYPOTHESIS). Apply the new mood with **no tween**, exactly on the twist cut, so the change lands with the line. Pick one shift type and rotate it between episodes:
   - **dark → bright warm** (sad or scaryNight → twistReveal or sadWarm): memories' reveal shape (+0.25 bright, +0.18 warm).
   - **warm → cold** (normalDay or sadWarm → sad or scaryNight): the truth is worse than we thought (train's tunnel shift is −0.21 sat and −0.21 warm).
   - **palette swap** at the same brightness (blue haze → orange dust): monster's act change at #105.
3. **One flashback grade** (`dreamMemory`) for every flashback in the episode. No ungraded flashbacks.
4. **Ending warmer than the rule section** by ≥ +0.10 (C8), unless this is the 1-in-4 episode where the payoff goes dark (C11 flip).
5. In-scene changes (case c): tween over 8–12 frames (0.3–0.4 s), with a sound hit when brightness moves >0.2 (a practical's click counts as one of the 2–5 SFX per minute; if it would break the cap, keep the step ≤0.2 and play no sound) (HYPOTHESIS; refs jump hard, for example memories −0.367 at 98.9 s, and it reads as a set change). Write it in the shot-list notes: `→ sadWarm, tween 0.35 s`.

## 5. Practical, key and rim light

| light | rule | values | tag |
|---|---|---|---|
| **Practical** (lamp, window, screen, candle, the rule object) | ≥1 visible in ≥80 % of interior shots (C10); it is the brightest thing in frame | `P.practical(part)`: PointLight Range 14, Brightness 2, Shadows on, part set to Neon. Roblox indoor recipe for comparison: SpotLight Angle 140, Brightness 4, Range 12; candle PointLight 0.7, colour 255,202,156. Windows: `keepLook = true` and let bloom do the glow | HYPOTHESIS (refs: only train shows its sources) |
| **Night colour glow** | one saturated practical per night shot (cyan jar, yellow eyes, neon) | Brightness 2–3, a colour the palette doesn't have yet | REF-RANGE (C9) |
| **Key** ("cheat" light per shot) | only on CU/MCU where the face decal sits in shadow; weak, from the camera side | `P.key(face, cam)`: SpotLight 35° off the lens axis, 2 studs above, Brightness 1–1.5, Range 14 | HYPOTHESIS (film habit; refs have none) |
| **Rim** | on every CU/MCU and on hero wides against a busy background; warm rim on cool scenes, cool rim on warm scenes | `P.rim(face, cam)`: SpotLight 6 studs behind, 3 up, Brightness 3, Range 18, Angle 70 | HYPOTHESIS (no ref shows a rim) |
| **Free-model lights** | clamp Range to ≤20 (`cleanFreeModelFx`); don't switch shadows on for dozens of lights (frame drops while recording) | | opinion |

Delete per-shot lights after the take: `P.clearShotLights()`.

## 6. Measuring a test capture (zero tokens, on the Mac)

1. Record the shots caption-free (captions are added in the edit anyway).
2. Grab one still per shot, at mid-shot, from the OBS take: `python3 measure.py --video take.mov --times 1.05,2.60,3.90 …` (the times come from the shot list). Or save stills by hand and name interior shots `int_….png`.
   Avoid paying tokens for this: `screen_capture` returns images to Claude, so use it for framing checks, not for measuring.
3. Read the PASS/FAIL lines. Fix in this order, one lever at a time, then re-measure:
   - brightness → `ExposureCompensation` (start with ±0.3 per 0.05 of bright; HYPOTHESIS, re-measure);
   - saturation → `ColorCorrection.Saturation` (±0.1 per 0.05 of sat);
   - warmth → `ColorCorrection.TintColor` or `Atmosphere.Color`;
   - dull highlights (p99) → a practical or the rule object in Neon, or Bloom Threshold down 0.05; **not** global exposure;
   - crushed blacks (p1, crush) → raise `Ambient` 10–15 per channel, or a key light; not exposure.
4. Twist shift: grab stills from the 4 s before and after the twist cut into two folders and run `python3 measure.py --compare "before/*.png" "after/*.png"`.
5. Write the calibrated values back into `M.MOODS` in the Luau module, so the next episode starts from them.

Tested on the references: memories' reveal (shots #40–44 vs #46–49) reads +0.365 bright, +0.250 warm, PASS; town fails C1–C5, train passes C1–C3 and C5. That matches the colour analysis.

The code is `tools/measure.py`.

## 7. Post grade (in the editor, after recording)
Grade only to land the targets; the look comes from the Studio moods. Values are for CapCut / Resolve-style controls, HYPOTHESIS unless noted.

| step | normal | sad | scary/night | twist | dream |
|---|---|---|---|---|---|
| Exposure | 0 to +0.15 EV if p99 <225 | −0.1 EV | −0.2 EV | +0.3 EV | 0 |
| Contrast | +5 % | −5 % | 0 (refs keep contrast 0.19 at night) | −5 % (ref dropped 0.095) | −8 % |
| Saturation | 100 % | 70–75 % | **90–95 %** (don't go grey) | 100 % | 100 % |
| Temperature | 0 | −8 (cool) | −5 | +12 (warm) | −4…+5, magenta tint +3 |
| Highlights | p99 to about 245 | — | — | glow +20 % | glow +25 % |
| Blacks | p1 12–20 | lift to 18 | 10–14 | 15 | 20 |

Order: (1) exposure and blacks/whites to hit p1 and p99; (2) per-scene temperature and saturation on that scene's range only; (3) a shared 10–15 % output sharpen if the capture was upscaled. Captions sit on a layer above the grade, so their colours stay exact. Vignette: optional style, off by default.

## 8. What the refs do weakly, and the fix

| weakness (evidence) | fix |
|---|---|
| Colour follows location, not story: only 7 of 28 beat transitions clear 1.5× the normal cut-to-cut jump; twists have no colour signature | mood per scene + deliberate twist shift (C7) |
| Dull highlights: p99 town 213, monster 205 | a practical in every interior, the rule object in Neon (C3, C10) |
| Crushed faces in dark sets (town cabin #46–#48) | raise Ambient, key light on CU (C4, §5) |
| Oversaturated monotone sets: town 40 % of shots >0.6 sat, cabin orange on 46 of 100 shots | C1, C2, C5, a contrasting practical colour |
| Flashbacks graded inconsistently (monster, town) | one `dreamMemory` grade (§4.3) |
| Jarring brightness jumps between cuts inside a scene (memories 0.166) | C6 |

## 9. Rotate between episodes
Twist shift type, payoff direction (darker in ≥1 of every 4 episodes, C11) and the night practical colour rotate; rules in `templates/rotation-log.md` (optional rows 22-24).

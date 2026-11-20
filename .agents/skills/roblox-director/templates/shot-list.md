# Shot list template (one per episode)

Save as `reels-shorts/projects/<episode>/shotlist.md`. Build it **after** the voice is timed: every row's time comes from `words.json`, and every cut sits on a sentence start, 1 frame before the first word (pacing.md), unless the notes say why not.
For a plan with no voice yet, use `tools/plan_timing.py`'s `words_planned.json` and rebuild every time from the real `words.json` later. Check it with `tools/shotlist_check.py` before building anything. The checker reads the columns by position, so keep all 12 columns and the codes below.

## Codes (the checker depends on them)

| column | write it like this |
|---|---|
| **#** | 1, 2, 3 … (plain number) |
| **time** | `start–end` in seconds from the voice file, e.g. `4.70–6.60` |
| **line** | the words spoken over the shot. Start with **★** on every key line: the stake line, the misread line, the twist line, the climax line, the last line, every quoted line of a main character and every line with a decal swap on its key word (each ★ needs a readable face, L5) |
| **size** | first word one of: EWS, WS, MS, MCU, CU, ECU, OTS, INS |
| **angle** | eye, low, high, top, dutch (≤5°). Add the tilt if it matters: `low 15°` (the checker groups by the first word, so a setup is subject + size + angle word + set) |
| **camera move** | first letter = who makes the move: **E** = in-engine (Studio camera), **Z** = edit zoom only, **S** = static. Then the move and speed: `E push-in 5%/s FOV 35`, `E truck R 3%/s`, `E orbit 20° + push 4%/s`, `Z 100→105%`, `E push 4%/s + Z punch 105% on "Friday"` |
| **subject + face decal** | `Name (F): eyes / brows / mouth` and swaps with the word: `→ mouth-O on "Friday"`. **(F)** = face readable in this shot. No (F) = face not readable |
| **pose/anim** | pose or clip name (`kneel + pinky promise`, `walk` (RobloxAnimator state)). Write **`idle`** first if the body is stiff idle (counts against L15). Add `flap 2.5/s` for on-camera dialogue |
| **set** | location name, the same spelling every time (the checker counts them) |
| **lighting mood** | one of `normalDay`, `sad`, `sadWarm`, `scaryNight`, `twistReveal`, `dreamMemory`, optionally `@clock` (`normalDay@21`), or a variant from `EpisodeMoods`; then practicals in brackets. Changes on a scene cut or the twist cut (hard), or inside a scene as a tween written in the notes (lighting-color.md §4) |
| **props/signs** | what is dressed in. Write **RULE** when the rule object is in frame and readable (L11: a mark on the body only at MS or tighter) and **RULE-CHANGE** when its state changes in this shot (L12) |
| **notes** | holds, whip or bookend choice, SFX hit, anything that breaks a default and why |

## Template (copy)

| # | time | line | size | angle | camera move | subject + face decal | pose/anim | set | lighting mood | props/signs | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |  |  |  |

## Filled example: first 15 s of a fictional episode (shape only, do not reuse the story)
Rule: "In this world, every promise you make lights a lantern over your door." 53 words in 15.0 s = 212 wpm. Capture 1080×1920 at 60 fps, delivered at 30 fps. This is also the scene for the first end-to-end test in pipeline.md.

| # | time | line | size | angle | camera move | subject + face decal | pose/anim | set | lighting mood | props/signs | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.00–2.10 | In this world, every promise you make lights a | WS | high 25° | E crane-down + push-in 6%/s FOV 60 | Hero: back three-quarter, small in frame | walk | lantern street | normalDay@18.5 (+ lantern practicals) | RULE: lanterns over every door | frame 1 moves; no whip this episode (used last episode) |
| 2 | 2.10–3.10 | lantern over your door. | INS | low 15° | E push-in 8%/s FOV 35 | lantern over a door | — | lantern street | normalDay@18.5 | RULE-CHANGE: lantern ignites (ParticleEmitter burst + PointLight 0→2 over 6 frames) | the one mid-sentence cut, on "lantern"; SFX: soft whoomp |
| 3 | 3.10–4.70 | Break it, and the lantern dies. | MS | eye | E truck L 3%/s FOV 45 | Neighbour (F): eyes-half / brows-sad / mouth-frown → eyes-closed on "dies" | hand drops from door handle | lantern street | normalDay@18.5 | RULE-CHANGE: his lantern snuffs out on "dies" (smoke puff, light 2→0 in 3 frames) | swap ±3 frames of "dies" |
| 4 | 4.70–6.60 | Our street glowed like a birthday cake. | EWS | top 70° | E truck R 2%/s + slow descend | street from above | walkers (`walk` state, distance-locked) | lantern street | normalDay@18.5 | RULE: 40+ lanterns | atmosphere Haze 0.3; the "world" wide |
| 5 | 6.60–9.40 | Mine had one lantern. One. From when I was six. | MS | low 12° | E pan R 4%/s + slow rise FOV 45 | Hero (F): eyes-half / brows-neutral / mouth-closed → brows-sad on "six" | hands in hoodie pocket, weight shift | Hero's door | normalDay | RULE: one small lantern; tag "AGE 6" hanging from it | longest shot 2.8 s (cap 3.5) |
| 6 | 9.40–12.10 | ★ I promised my little sister I'd never leave her alone. | CU | eye | E orbit 15° + push-in 4%/s FOV 35 | Hero (F): eyes-soft / brows-raised / mouth-smile; Sister in soft focus | kneel + pinky promise | Hero's porch | sadWarm | RULE: the lantern flares brighter on "never" | DOF focusOn(Hero.Head), FarIntensity 0.3 |
| 7 | 12.10–13.30 | Then the letter came. | MS | high 30° | E crane-down 4%/s FOV 45 | Hero (F): eyes-open / brows-neutral / mouth-closed | bend down, pick up letter | Hero's hallway | sadWarm | RULE: lantern visible through the door glass; letter on the mat | SFX: mail slot clack on cut |
| 8 | 13.30–15.00 | ★ Moving date: Friday. | MCU | low 10° | E push-in 4%/s FOV 35 + Z punch 105% on "Friday" | Hero (F): eyes-wide / brows-raised / mouth-O on "Friday" | hands shake (2-frame jitter on the letter) | Hero's hallway | sadWarm | letter readable in the foreground: "MOVING DATE: FRIDAY" | text cap height ≥3.5 % of frame; edit zoom ≤ +5 % |

What the checker says about this example: close shots 25 %, MS 38 %, readable face 62 % (both ★ lines have one), non-eye angles 75 %, in-engine moves 100 %, static 0 %, stiff idle 0 %, no setup repeated more than twice, rule object in shot 1 and in 88 % of shots. On this 8-shot opening, L4 (1 insert = 12.5 %), L16 (4 locations) and L18 (final shot 1.7 s) read FAIL, which is expected for a partial list: it is an opening, not an episode.

## Build cost (fill before the build; caps in pipeline.md "Build budget")

| item | new | reused | cap | over? why |
|---|---|---|---|---|
| sets | | | ≤6 total, ≤2 new | |
| full-kit rigs | | | ≤5 | |
| face PNGs | | | ≤40 new | |
| rule-object images (uploads) | | | ≤12 | |
| poses | | | ≤15 new | |
| contact poses | | | ≤3 | |
| special builds | | | ≤2 | |
| VFX setups | | | ≤3 new | |
| outfits / crowd method | | | 1 per character / cloned static | |

## Before you build
- [ ] Every row's time is from `words.json`; cuts on sentence starts ≥55 % (pacing.md)
- [ ] `shotlist_check.py` passes, or each FAIL has a reason in the notes
- [ ] Build cost block filled; every number inside its cap, or the reason and the user's OK written
- [ ] Nothing on look.md §16's Roblox-limits list (foot inserts, bubbles on CUs, rack off a transparent part)
- [ ] Mood column has a deliberate change on the twist cut (lighting-color.md §4)
- [ ] Rotation choices (whip, bookend, prop death, twist move, hold) written in the notes of the rows they affect and logged in the rotation-log row

# pacing.md: cuts, hook, pauses, holds

Tags: **REF-RANGE** = measured in the 6 reference reels; **HYPOTHESIS** = beat-the-refs bet, A/B it on the user's analytics.
Limits: no view data, so refs are not proven good. Never use `shots.json` `move` labels (wrong about 49 % of the time) or `audio.json` `music_changes` / `sfx_hits` as evidence. Camera-move rules live in the look file of this skill, not here. n = 6, and town and dog are one template.

## 1. The core idea
The one sync that beats chance in the refs: **cuts land on sentence starts**, leading the first word by 0-65 ms. Cuts on music beats are at chance (38-75 % vs 38-66 % chance) and cuts on "word starts" are meaningless at 220+ wpm (random times score 63-89 %). So: cut to the text, never to the music.

## 2. Cut rules

| # | rule | refs | tag |
|---|---|---|---|
| 1 | Put a cut on **>=60 % of sentence starts**, **0 to 2 frames (0-66 ms) before the first word**. Cut times are frames at 30 fps, so lead by 1 frame (33 ms) by default | sentence starts with a cut: monster 87, train 86, bell 73, memories 52, dog 38, town 26 %. Mean lead -65 (monster), -18, -8, +24 ms | REF-RANGE (4/6 strong); the 60 % floor is HYPOTHESIS |
| 2 | **>=55 % of all cuts sit on sentence starts**; <=40 % of cuts fall inside a sentence | cuts on sentence starts: memories 78, bell 71, monster 65, train 57 vs chance 9-18 %; town 23 and dog 37 are the failures (77 % and 63 % mid-sentence) | REF-RANGE |
| 3 | **Mean shot 1.3-2.5 s; cut rate 20-48 per min** | mean 1.23-2.94 s (only memories above 2.0), 20.1-48.4 cuts/min, median 30 | REF-RANGE |
| 4 | **About 5-6 words per shot** (never over 10 words except in a designed hold). Check: words per shot = wpm / 60 x mean shot length. At 220 wpm and 1.6 s shots that is 5.9 | bell 5.83, town 6.43, monster 5.52, train 5.82 (dog 7.9, memories 10.8 are the loose ones) | REF-RANGE |
| 5 | A sentence of 10+ words gets 2+ shots; a sentence of 4 words or fewer gets one shot or shares a shot | 1.4-2.1 shots per sentence of 6-8.7 words | REF-RANGE |
| 6 | **No shot over 3.5 s** except 1-2 designed 4-6 s holds (section 4) | only memories has many shots over 3 s (27); the others have 1-8 | REF-RANGE |
| 7 | Extra cuts between sentence starts go on clause breaks (comma, "but", "then"), at uneven spacing. No metronome cutting | town/dog cut at near-periodic spacing and ignore the text | HYPOTHESIS |
| 8 | No beat-sync. If a track has a strong beat, do not snap cuts to it | beats at chance in 6/6 | REF-RANGE |

## 3. First 3 s and first 10 s

| rule | value | tag |
|---|---|---|
| First word | starts at **0.00-0.20 s**; sentence 1 states the whole rule ("In this world, ..." / "In this town, ...") and ends at 2.0-4.5 s | REF-RANGE (6/6; first word 0.00-0.16 s) |
| First cut | **by 2.5 s**. Shot 1 never longer than 3.0 s | refs: 0.70, 2.17, 2.50, 2.50, 4.07, 4.17 s; 5/6 hold shot 1 for 2.2-4.2 s, so the hook is slower than the body, a shared weakness. The 2.5 / 3.0 caps are HYPOTHESIS |
| First 10 s | **>=4 cuts** | refs 3-10, median 3.5. HYPOTHESIS (a bet above the median) |
| Words in 0-3 s | 9-13 (a quick sanity check on wpm) | REF-RANGE |
| Frame 1 | the picture already shows the rule's object or the world, and moves | see look file; 5/6 refs show the rule object in shot 1 (dog waits until 18 s) |
| Music/captions | music on frame 1 (audio.md section 2); first caption appears on the first word (captions.md) | REF-RANGE |

## 4. Holds, slowdowns and the ending

| rule | value | tag |
|---|---|---|
| Designed holds | **1-2 holds of 4-6 s** at the reveal and/or the ending, with a slow camera move and no cut inside. A hold starts on a cut, and that cut sits on a sentence start or inside the designed pause just before it (§5): a final hold that starts in pause B covers pause + last line + tail | REF-RANGE (bell 6.07 s final; memories 6.03, 6.0, 5.43 s). Placement of memories' holds is not at its reveal (129.1 s), so "reveal and/or ending" is a choice, not a law |
| Rolling-10 s swing | a check, not a goal: refs swing 1.9-4.2x, but random cutting with CV 0.4 already gives about 1.9x | REF-RANGE |
| Last 15 s | make it **different from the body**: >=1.2x slower (bell 1.88x, train 1.22x, memories 1.21x) **or** >=12 % faster (monster 0.88x). Do not stay flat | town/dog sit at 0.96-0.98x: nothing changes at the ending. No universal speed change at the twist (3/6 slower, 3/6 faster), so do not force one there |
| Final shot | >=3 s | HYPOTHESIS (bell 6.07 s) |

## 5. Pauses (picture side)

The pause rule itself (how many, how long, where) is **script.md §6**: 2-3 designed pauses of 0.6-1.3 s, A after the twist line, B before the last line. Picture rules around them:

| rule | value | tag |
|---|---|---|
| Cut inside a pause | put the cut **inside the pause or within 0.05 s of it** | REF-RANGE (a cut falls in or within 0.05 s of 8 of the 11 largest pauses) |
| Silence beat | voice gap 0.8-1.3 s (pause A), music <=-50 dBFS for 1.0-1.5 s, the cut lands **0.0-0.1 s before the voice resumes**. Only with music-event type A (audio.md §2) | REF-RANGE n=1 (bell: 1.28 s gap, cut 0.07 s before) |
| Captions in a pause | the last caption stays on screen; no blank | REF-RANGE (bell) |

## 6. Rotation (anti-template)
Hold placement, ending pace and mean shot length rotate between episodes; the rules are in `templates/rotation-log.md` (optional rows 19-21). Log them in the cue-sheet header.

## 7. Pacing self-check (zero tokens)

`python3 tools/pacing_check.py cuts.txt words.json duration_seconds`. `cuts.txt` = one cut time in seconds per line, excluding 0 (export from the NLE or `ffmpeg scdet`); `words.json` = the word-timestamp transcript (captions.md §3). Sentence starts come from the punctuation in the tokens; wpm is speech only (designed pauses taken out). **On a plan** (no voice yet), make both files with `python3 tools/plan_timing.py script-sheet.md --shots shotlist.md` and use the runtime it prints.

Fail handling: fix the picture timing first (move cuts to sentence starts), then add or remove words per shot. Do not re-generate voice for a pacing failure unless wpm is out of range.

| check | pass |
|---|---|
| cuts/min | 20-48 |
| mean shot | 1.3-2.5 s |
| shots over 3.5 s | <=2, each 4-6 s and a designed hold |
| sentence starts with a cut | >=60 % |
| cuts on sentence starts | >=55 % |
| mean lead | -66..0 ms |
| first cut / first word | <=2.5 s / <=0.2 s |
| cuts in first 10 s | >=4 |
| pauses >=0.5 s | 2-3, each 0.6-1.3 s, the last one 0.6-1.0 s before the last line (script.md §6; or `ffmpeg silencedetect=n=-38dB:d=0.5`) |
| last 15 s vs body | >=1.2x slower or >=12 % faster |

# Script sheet: [episode title]

Copy this file into the episode folder and fill it in. One row = one spoken sentence (two very short sentences may share a row). A row is a timing unit, not a shot: the shot list splits 10+-word rows and may merge ≤4-word rows (`pacing.md` rule 5). Rules behind each column: `script.md` (words, beats, pauses), `pacing.md` (cuts, shot length), `audio.md` (music, SFX), `captions.md` (highlights), `look.md` and the lighting presets (`normalDay`, `sad`, `sadWarm`, `scaryNight`, `twistReveal`, `dreamMemory` in `lighting-presets.lua`).
The tools read this table by its header names: `tools/plan_timing.py` fills the time column, `tools/script_check.py` runs the script.md §9.3 numbers.

## Header (fill before the table)

| field | value |
|---|---|
| Rule (line 1, 8-15 words) | |
| Rubric score (/12, tests 1-6) | 1: _ 2: _ 3: _ 4: _ 5: _ 6: _ = _ |
| Comment-bait question | |
| Twist family / ending payoff type | |
| Rotation checked (`script_check.py --log`): core fields vs the last 3-5 rows; missing core fields back-filled | |
| Target runtime (60-180 s) and reveal % (Variant A ~52 % / B ~68 %, ≥10 points from last episode) | |
| Motif (3+ uses, last in final 10 %) | |
| Planted clues and the joke clue (reads as an insult first, never the mechanism) | |
| Cast and voices | NARR = the user clone; NAME = voice / pitch note; KID = designed voice or ≤+10 st |
| Music plan (1-2 events, 45-90 %, on a cut, on the twist or climax line; event-1 type A / B / C differs from the last episode) | |
| Words / speech end / runtime / reveal % | |
| Tone (brief → ending; script.md §0.2) | |
| Skeleton (before opening examples/: family=…; sign=…; belief=…; reaction=…; discovery=…; subject=…; outcome=…; climax=…; ending=…; lastline=…, values in `tools/skeletons.txt`) | |
| Music event 1 type (A / B / C) | |
| Twist mechanism words (`script_check.py` searches every line before the reveal) | |
| Twist clues (2-4; mark the ≤2 direct ones) | |
| Guess test (script.md §3.3: blind reader, pre-twist lines only): reader + 3 guesses + not guessed / guessed, or UNCHECKED | |
| Logic questions (script.md §3.4): 3 "why doesn't X just…?" + answers | |
| Staged contrast, if any: the line that planted X + its time | |

## Timing rules

- **220 wpm = 3.67 words per second.** Row seconds = spoken words / 3.67 / rate. Count numbers as spoken: "2C" = 2 words, "2045" = 3 ("twenty forty-five"), "4:10" = 2. First word at 0.1 s. `tools/plan_timing.py sheet.md --rewrite-times` does all of this and writes the time column.
- **Slow reads:** end the line cell with `(0.6x)` (1-3 word punch lines, read inside the main take) or `(0.85x)` (the last line, its own take); the row stretches by 1/rate (`audio.md` §1.3).
- **Designed pauses** follow `script.md` §6 (the one pause rule): 2-3 pause rows of 0.6-1.3 s, A right after the twist line, B right before the last line, C optional at the climax. Each is its own row: `*(pause 0.8 s, hold the shot)*`; its length is the whole silence. Normal sentence gaps (0.15-0.30 s) are already inside the 220 wpm average; don't add them.
- Add a 0.5-1.5 s tail after the last word (the tools assume 1.2 s; `--tail` changes it). Runtime = last word end + tail.
- Write `start-end (pct %)` in the time column. pct = start / runtime × 100. Check every beat against `script.md` §3.
- Shot length: mean 1.3-2.5 s; no shot over 3.5 s except 1-2 designed 4-6 s holds at the reveal or the ending. A row of 10+ words or over 3.5 s gets a second cut on a phrase break; note it in the shot column.
- Cut on the sentence start, 0-65 ms before the first word. Never cut on music beats.
- After drafting, read the whole sheet aloud with a stopwatch. If it is >5 % off the computed runtime, fix the words, not the voice speed.

## Column guide

| column | what to write |
|---|---|
| # | row number (pauses get `-`) |
| time | `start-end (pct %)` in seconds |
| line | exactly what is said; narrator's own quoted speech in "quotes" |
| speaker | `NARR`, or the character tag from the cast line (DAD, THEO, KID, OFFICER, SIGN) |
| beat | hook / rule, **rule clear** (on the row whose end completes the rule), stake, example, status quo, flaw, inciting, misread, clue, doubt, reveal, **TWIST** (capitals, the twist line), turn, climax, extra payoff, **LAST LINE**, motif n/3. `script_check.py` finds the beats by these words |
| shot | size + subject: WS, MS, MCU, CU, ECU, OTS, INSERT, then who or what. Close shots (CU+MCU+ECU) ≥25 % (HYPOTHESIS; refs 4-31 %) |
| camera | the move: push-in (default), pull-back, track, pan, tilt, crane, orbit, rack focus, static hold. ≥70 % of shots move |
| lighting mood | `mood@clock` (`normalDay@21` = the day look at 9 pm; no `@` = the preset's own time), then practicals or notes in brackets |
| music cue | cue letter (A, B), layer changes, and `EVENT 1/2` on the cut where an event lands |
| SFX | real diegetic sounds only, 2-5 per minute, ≥50 % in the last 35 % |
| caption highlight | the accent word for this line, or `-`: names, rule words, the 1-2 peak words only (never props or function words). At most one per sentence; ≤13 % of the words after the hook is a ceiling, and most lines get `-`. The hook line: `whole line in accent` (if this episode accents the hook). `make_caps.py --sheet` reads this column |

## Filled example (first 6 rows of `examples/gold-1.md`)

| # | time (s) | line | speaker | beat | shot (size + subject) | camera | lighting mood | music cue | SFX | caption highlight |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.1-3.4 (0 %) | In this world, your footprints glow for one day, everywhere you walk. | NARR | hook / rule | WS: narrator walking down a dusk sidewalk, cyan prints lighting up behind each step | low track behind, moving on frame 1 | normalDay@18.5 | Cue A in at 0.0 (soft pluck bed) | - | whole line in accent |
| 2 | 3.4-6.6 (3 %) | Last spring, a new line showed up under my window every morning. | NARR | stake | MS: narrator's bedroom window from the yard, glowing line in the wet grass | slow push-in | normalDay@8 | A | - | - |
| 3 | 6.6-8.3 (6 %) | Nobody here can keep a secret. | NARR | rule cost, rule clear | WS: high street, dozens of crossing glow trails on the sidewalk | crane down | normalDay | A | - | - |
| 4 | 8.3-11.6 (7 %) | My mom literally always knows when I go to the candy store. | NARR | example 1 | MS: Mom on the porch, arms crossed, trail behind her runs to a CANDY shop sign | pan along trail | normalDay | A | - | - |
| 5 | 11.6-14.3 (10 %) | Mr. Hale told his wife he went to the gym. | NARR | example 2 (funny) | MCU: Mr. Hale in a tracksuit, sprinkles on his shirt | slow push-in | normalDay | A | - | - |
| 6 | 14.3-16.2 (12 %) | His prints went to the donut shop. | NARR | example 2 | INSERT: glowing big prints end at a DONUTS door decal | tilt up to sign | normalDay | A | - | - |

## Sheet (copy rows as needed)

| # | time (s) | line | speaker | beat | shot (size + subject) | camera | lighting mood | music cue | SFX | caption highlight |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.1- | In this world, | NARR | hook / rule | | moving on frame 1 | | Cue A in at 0.0 | | whole line in accent |
| 2 | | | | stake | | | | | | |
| 3 | | | | | | | | | | |

## Before handing to the user

- [ ] `script.md` §9.3 self-check: all 16 pass (`tools/script_check.py` + the guess test)
- [ ] Rotation-log row drafted (the 7 core fields of `templates/rotation-log.md`, then any optional ones)
- [ ] 3 titles (formats A, B, C) and 3 cover texts written; no cover text burned into frame 0

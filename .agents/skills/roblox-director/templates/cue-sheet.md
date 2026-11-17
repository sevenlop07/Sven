# Cue sheet template (one per episode)

Fill the header first (it enforces rotation), then one row per beat. Times are seconds from the final voice track, and also % of runtime. Rules and tags (REF-RANGE / HYPOTHESIS) are in audio.md, pacing.md, captions.md. Nothing here is generated until the user approves credit use.

## Header (copy, fill)
```
Episode: ____            Runtime: ___ s     Words: ___     wpm (words / speech seconds): ___ (target 200-240)
Voice: model ____ / stability __ / similarity __ / style __ / speed __ ; extra voices: ____ (method: designed | shift +/-__ st)
Reveal %: __  Twist/climax line + time: "____" @ ___ s (___ %)     Last line starts at: ___ % (>=92 %)
Rotation (rules per field in templates/rotation-log.md; copy these into the episode's log row):
  opener sound: ____     music event 1 type: A silence | B cue change | C layer     event position %: ____
  body track: ____       rule-object motif sound: ____    micro-drops: yes/no
  ending: held note | rule-object sound | silence
  hold: reveal | ending | both     ending pace: slower>=1.2x | faster>=12%     accent colour: ____    hook accented: yes/no
Previous episode used: (copy its log line here)
Credits needed (tracks/SFX with licence + URL): ____
Accent words (names, rule object, emotional words, 10-13 % of words after the hook): ____
```

## Beat table
Columns: **time | beat | music (file + action: in / out / drop / silence / swap / layer-in / layer-out / rise) | SFX (file + target line + cut-lock Y/N) | voice note (pause s, pace, pitch/emotion) | level (LUFS or dB)**.

| time (s / %) | beat | music | SFX | voice note | level |
|---|---|---|---|---|---|
| | 1 Hook | | | | |
| | 2 Rule examples | | | | |
| | 3 Hero + problem | | | | |
| | 4 Escalation | | | | |
| | 5 Climax / twist (music event 1-2, in 45-90 %) | | | | |
| | 6 Reveal / payoff | | | | |
| | 7 Last line + tail | | | | |

Per-row reminders: music on frame 1; <=2 rule-object sounds before 65 % (an opener using it counts); SFX 2-5 per min, >=35 % on cuts, >=50 % after 65 %; designed pauses per script.md §6 (A after the twist line, B before the last line); no cut on a music beat just because it is a beat.

## Self-check (tick before export)
- [ ] first word <= 0.2 s; music on frame 1; first cut <= 2.5 s
- [ ] 1-2 music events, each on a cut within +-0.5 s of the climax/twist line, 45-90 %
- [ ] SFX count / min = ___ (2-5), on-cut % = ___ (>=35), in last 35 % = ___ % (>=50)
- [ ] voice minus bed 7-10 dB; never under 5 dB in any 10 s window; bed rises +2..4 dB toward the end
- [ ] ducking 3-4 dB (HYPOTHESIS), integrated -14 LUFS +-0.5, true peak <= -1.0 dBTP
- [ ] tail 0.5-1.5 s after the last word; pause B 0.6-1.0 s before the last line, read at about 0.85x
- [ ] pacing_check.py all PASS; captions QA passes
- [ ] IG "AI info" toggled for cloned or TTS voice; credits.txt written

---

## Filled example (fictional episode, to show format; do not copy its choices)

Premise (made up): "In this world, an elevator only stops on a floor where someone is waiting for you."

```
Episode: E07 "Floor 9"   Runtime: 96 s   Words: 340   wpm: 340 words / 87 s speech = 234
Voice: eleven_multilingual_v2 / stability 45 / similarity 80 / style 5 / speed 1.15 ; extra voices: security guard (clone, -5 st), little sister (designed voice)
Reveal %: 66   Twist/climax line: "Nobody pressed nine. I did, a year ago." @ 68.4 s (71 %)   Last line starts at: 94 %
Rotation: opener sound: none | music event 1 type: B cue change | event position: 71 % | body track: Investigations (audition first)
  rule-object motif sound: ding | micro-drops: no | ending: rule-object sound on last word
  hold: ending | ending pace: slower >= 1.2x | accent colour: red #FD3433 | hook accented: no
Previous episode used (example only): opener sparkle | type A silence | position 58 % | Dark Fog | clink | micro-drops yes | silence ending | reveal hold | faster | yellow | hook accented
Credits: Investigations, Hitman (Kevin MacLeod, incompetech, CC BY 4.0, credit line in description); ding from the library pack (licence to confirm)
Accent words: elevator, nine, Mia, waiting, alone
```

| time (s / %) | beat | music | SFX | voice note | level |
|---|---|---|---|---|---|
| 0.0-3.1 / 0-3 | Hook: "In this world, an elevator only stops where someone is waiting." | Investigations IN on frame 1, no fade | none (opener rotated away from sparkle) | first word 0.05 s; 232 wpm | music bed -23 LUFS |
| 3.1-14 / 3-15 | Rule examples: the mailman, the landlord | Investigations continues | `ding` low, on the cut at 8.2 s (1 of 2 allowed before 65 %), cut-lock Y | gap 0.2 s; punch line "Floor 3. Again." at 0.6x rate | ding 7 dB under voice |
| 14-31 / 15-32 | Hero (Mia, narrator) + problem: nobody ever waits for me | bass layer-in at 24 s (+3 dB) | none | 235 wpm, flat | bed -23 |
| 31-62 / 32-65 | Escalation: the one floor that never opens | Investigations, bed +2 dB at 55 s | `whoosh-short` on the cut at 47.0 s, Y; second `ding` at 61.4 s (2 of 2 before 65 %), cut-lock N | 238 wpm; guard line at -5 st | voice -16, bed -23 |
| 62-70 / 65-73 | **Climax/twist** "Nobody pressed nine. I did, a year ago." | **swap**: Investigations out, Hitman in, on the cut at 68.4 s, overlap 0.3 s; riser-short 66.4-68.4 under it | `riser-short` ends on the cut; `impact-bass-1` on the cut (cut-lock Y) | pause A 1.0 s after the twist line; "Nobody pressed nine." at 0.6x rate | riser -9 dB under voice, impact 0 dB vs voice |
| 70-86 / 73-90 | Reveal: the sister waited on nine | Hitman, bed +3 dB from 78 s | `ding` x2 at 74.0 (Y) and 79.5 s (N) | little sister designed voice; yell at 76 s +4 LU (about -10 LUFS short-term) | dings 0..+3 dB vs voice |
| 86-96 / 90-100 | Last line + tail: "Floor nine. She pressed it too." | Hitman holds, tail 1.2 s after the last word, fade over the tail | `ding` ON the last word (the rule-object sound, final) at 94.8 s | pause B 0.7 s before the last line; last line at 0.85x rate | ending voice-bed >= 6 dB |

Counts for this sheet: real SFX = 7 (ding 8.2, whoosh-short 47.0, ding 61.4, impact 68.4, ding 74.0, ding 79.5, ding 94.8; the riser is part of the music transition) in 1.6 min = 4.4 per min; on-cut 4 of 7 = 57 %; after 65 % = 4 of 7 = 57 %; rule-object sounds: 2 before 65 %, 3 in the climax and ending; designed pauses: 2 (A 1.0 s after the twist line, B 0.7 s before the last line); music events: 1 (B cue change at 71 %).

# audio.md: voice, music, SFX, mix for "In this world..." Roblox reels

Tags: **REF-RANGE** = measured in the 6 reference reels (bell, memories, town, dog, monster, train). **HYPOTHESIS** = a beat-the-refs bet, not seen in refs; A/B it on the user's own analytics.
Honest limits: no view or retention data exists for any ref, so "ref did X" never means "X works". n = 6 reels, and town and dog share one track and one voice. Never use `audio.json` `music_changes` / `sfx_hits` as evidence (52-88 % of "hits" are music notes). Real SFX and cue changes below come from the re-measurement.

Hard rules (non-negotiable, not evidence-based):
- Roblox in-game audio is **muted** at capture (licensing). All sound is added in the edit.
- **Never generate ElevenLabs audio without asking the user** (credits). Ask once per episode with the text's character count (ElevenLabs bills text characters; check the current plan page) and the expected takes: `script_check.py` prints characters per speaker. Default ask: 2 takes of the narration + 1-2 per character line + 2 takes of the last line. Stop if credits run out.
- Budget $40/month total, already spent on ElevenLabs. Fill every gap from free, monetization-safe sources (section 5). Do not buy packs.
- Own-voice clone is exempt from YouTube's AI disclosure. Instagram/Meta asks for the "AI info" label on realistic-sounding AI audio, so toggle it on when the narration is the clone or TTS.

---

## 1. Voice

### 1.1 Model and settings (ElevenLabs, the user's "the user professional voice" = a professional clone)
All HYPOTHESIS (derived from ElevenLabs docs, not from the refs; nobody has generated test takes yet).

| use | model | settings | why |
|---|---|---|---|
| Main narration | `eleven_multilingual_v2` | stability 40-50, similarity 75-85, style 0-10, speaker boost on, speed 1.10-1.20 | Only model with a speed slider (0.7-1.2) and the docs call it the most stable on long-form. Stability 40-50 keeps pitch variation near the refs' pitch SD of 4.3-5.7 st (REF-RANGE) |
| Emotional or character lines (yell, whisper) | `eleven_v4` (supports PVC) | stability low-mid, similarity 0.75, tags like `[whispering]`, `[shouting]` | No speed or style slider and no SSML, so generate these as separate short takes and fit them in the editor |
| Avoid | `eleven_v3` with the PVC | n/a | Docs say PVCs are not fully optimized for v3 |
| Burmese-language versions | `eleven_v4` | same as above | v4 lists Burmese; v2 probably does not (check before use) |

Source: https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech , https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4

### 1.2 Delivery speed
- **Target 200-240 wpm for 100-180 s stories** (REF-RANGE: memories 222, town 245, dog 247 sound workable; monster 270 has 0 pauses >=0.2 s and a 3.3-4.4 dB voice-over-bed margin, so it is too dense). Never above 250 wpm, never a median line rate above 5.5 syl/s.
- ≤80 s stories or action stories may sit at 160-200 wpm (bell 161, train 176).
- If the clone reads at about 150-170 wpm at speed 1.0, set speed 1.10-1.20 first. If still short, time-stretch in the editor by at most 1.10 with pitch preserved (HYPOTHESIS: speed near 1.2 may degrade quality, the docs warn "extreme values").
- **wpm = word count / speech duration**, measured from first word start to last word end, minus the designed pauses (`pacing_check.py` does this). Measure it on the first take before generating more takes (saves credits).

### 1.3 Pauses (set in the editor, not in the model)
**The pause rule is script.md §6** (one rule for the whole skill): default sentence gap 0.15-0.30 s; 2-3 designed pauses of 0.6-1.3 s, **A** 0.8-1.3 s right after the twist line (REF-RANGE n=2: bell 1.29 s, memories 0.88 s), **B** 0.6-1.0 s right before the last line (HYPOTHESIS: no ref gives the last line more than 0.38 s), **C** optional at the climax line; nothing else ≥0.5 s. A pause's length is the whole silence between the two words: set the gap in the editor to that length.

Slow punch lines: 1-3 word lines at about 0.6x the video's median syllable rate, and the last line at about 0.85x (HYPOTHESIS; the refs' slowest lines are all 1-3 word punches at 1.25-3.4 syl/s, but their last lines run at 0.98-1.31x). How: **read 1-3 word punch lines inside the main take**, with 0.2-0.4 s of silence on each side (a full stop or a line break in the text, then trim in the editor); that usually lands them near 0.6x the syllable rate. Do not generate separate slow takes for punch lines: spliced takes at 120-133 wpm sound pasted in (round-1 critic). Only the last line gets its own take, at speed 1.0 while the body runs at 1.10-1.20 (≈ 0.85x). All HYPOTHESIS until the first take. Mark them `(0.6x)` / `(0.85x)` in the sheet's line cell so the timing tools stretch those rows.

### 1.4 Casting other characters
| character | method | tag |
|---|---|---|
| kid, animal | a separately designed voice (ElevenLabs voice design costs credits, so ask the user first), OR clone shifted **+6 to +10 st, hard cap +10** | HYPOTHESIS cap. Refs shift +8 to +16 st (Cora +8.1, Kyle +10.1, poodle +10.1, guard +13.5, Max +15.9); the analyst flagged +13 and above as chipmunk |
| menacing adult | clone shifted **-4 to -6 st** | REF-RANGE (memories dealer -5.9, Eli -4.9, taunt -6.4) |
| parent, friendly adult | narrator pitch, +-3 st | REF-RANGE (mom -0.4 to +2.0, cosine >0.92) |
| yell | short-term loudness **+3 to +5 LU** over integrated (about -10 to -11 LUFS short-term) | REF-RANGE (town -9.4, dog -10.5 vs -14.2) |

Free pitch shift on the user's Mac: `ffmpeg -i in.wav -af "rubberband=pitch=F" out.wav` with F = 2^(st/12): +4 st 1.260, +6 1.414, +8 1.587, +10 1.782, -4 0.794, -5 0.749, -6 0.707. Listen to every shifted line once; if it sounds like a cartoon, drop 2 st. Cast at most 3 voices besides the narrator's clone (HYPOTHESIS: casting and listening work); any other speaker is a narrated quote with a speech bubble (script.md §7).

---

## 2. Music (rules per beat)

Layout, in % of runtime (REF-RANGE unless tagged):
| beat | % | music |
|---|---|---|
| Hook | 0-3 | Music is on **frame 1**, at full bed level, no fade-in (first words at 0.00-0.16 s in all 6) |
| Rule examples to escalation | 3-65 | One track, one arrangement. Optional bass layer in at 25-35 % (+2-4 dB; monster +4.2 at 26 %, dog at 26 %, train at 20 %) |
| **Music events** | 45-90 | **1-2 events** (cue change, layer drop/in, or silence), each **on a cut** and within +-0.5 s of the **climax or twist line** (4/6: bell 56.5 silence, town 115.0 swap, train 104.0 swap, monster 130 / 152.5 layer out; memories 83.0 lands on neither and dog has none, which is the weakest pattern) |
| Build | last 30 % | Bed rises **+2 to +4 dB** from the first to the last 10-30 s (4/6: +1.9 to +4.1). Keep voice minus bed >=6 dB at the end (bell dipped to +1.5) |
| Ending | last word | **0.5-1.5 s tail** after the last word: held note, rule-object sound, or silence. HYPOTHESIS (5/6 refs cut under a running bed) |

**Music-event types.** Log the type of event 1 (the twist/climax event); event 2 may be any type. Event 1's type differs from the last episode's, and between two A's at least 2 episodes go without A (A in ep1 → next A in ep4 at the earliest; n=1 evidence, so test it):
- **A. Silence drop** (n=1, bell): music to <=-50 dBFS for 1.0-1.5 s on the last word of the line where the rule breaks, with a 0.8-1.3 s voice pause. Then 5-12 s of room tone or world bed only, then music back >=+20 dB on a cut (bell: +31 dB). Music must have been running before it, or there is nothing to drop.
- **B. Cue change** (memories, town, train): a new track, or a new section of the same track (including the track's own arrangement bringing in new instruments), on a cut at the turn/climax line. Overlap 0.0-0.5 s, not a long crossfade.
- **C. Layer move** (monster): a layer of the same track goes in or out on the cut (bass in at the stakes line, out at the turn). The library is stereo mixes with no stems, so by default C is an EQ or level move on the one track: a low-pass in (or out), or the top end −12 dB, over 0.1-0.3 s on the cut. Layer two different tracks only after checking they share a key and tempo (HYPOTHESIS; clash risk).
- **Optional micro-drops** (HYPOTHESIS, 2-6 per video): 0.3-1.0 s dips of >=10 dB before punch lines, re-entry within 0.1 s of a cut. The memories dips may be the track's own phrase rests, so test before relying on them.
- **Never beat-sync cuts.** Cuts on music beats are at chance in all 6 refs (38-75 % vs 38-66 % chance). Cuts follow sentence starts (see pacing.md); music follows the story.

Keep the same track for a whole story unless an event swaps it (dog: 1 track, 0 events; do not copy that).

---

## 3. SFX

| rule | value | tag |
|---|---|---|
| density | **2-5 real SFX per minute** | REF-RANGE (verified 0-5.3/min: bell 5.3, town 4.2, train 3.2-4.1, monster 1.4-2.5, dog 0.5-1, memories 0) |
| cut lock | **>=35 % within 0.1 s of a cut** (transient peak at the cut frame, or 1-3 frames before it) | REF-RANGE (bell 43 %, town 36 %, train 33 % vs chance 9-16 %) |
| late loading | **>=50 % in the last 35 %** of runtime | REF-RANGE (town 10/11, monster 5/7, train 5/9) |
| motif | one **diegetic rule-object sound** (bell ding, clink, door, rumble). <=2 audible uses before 65 % (an opener that uses it counts), then >=3 in the climax and ending, and sound it on the last word if the script ends on it. Extra rule-state changes before 65 % (act-1 examples) stay silent: the picture and the spoken word carry them | REF-RANGE n=2 (bell, town); town narrated "Clink" 8 times with no sound, then sounded 4; its last spoken "Clink." had no SFX, a missed payoff |
| world bed | where the world has a machine/crowd/room, a low bed with a **>=10 dB change** when the rule changes | REF-RANGE n=2 (train rumble -10 to -14 dB after "it stops"; bell room tone while music is out) |
| drop then impact | after a micro-drop, a low impact on a cut, <=4 per video, all in the last 30 % | HYPOTHESIS (town's booms may be its track's own swells) |
| level | cut ticks/whooshes 6-10 dB under the voice; climax rule-object hits 0 to +3 dB over the voice short-term | HYPOTHESIS (town clinks +43-46 dB HF over the bed) |
| opening stinger | **optional**, 0.15-0.25 s, rotate (see section 7) | REF-RANGE 3/6 (town and dog share one sparkle-whoosh template, monster a sub-boom) |

Sounds the refs do not use (none of the 6 had a comedic or meme event): record-scratch, boom-meme, error, glitch-1, pop, slide-down. Treat them as untested, not forbidden; use at most one in a deliberately comic episode and log it.

---

## 4. Mix targets (final file)

| item | target | tag |
|---|---|---|
| Integrated loudness | **-14 LUFS +-0.5** | REF-RANGE (all 6 at -14.1/-14.2; may reflect platform normalisation, still the right target; YouTube normalises near -14) |
| True peak | **<= -1.0 dBTP** (set the limiter ceiling at -1.5 for margin) | REF-RANGE: refs run -1.0 to +0.2, so beat them |
| Voice bus | -15.5 to -16.5 LUFS integrated | REF-RANGE |
| Music + SFX bus | -22 to -25 LUFS integrated | REF-RANGE (-21.0 to -27.6) |
| Voice minus bed | **7-10 dB** integrated; never under 5 dB in any 10 s window | REF-RANGE (4.4-12.1, median 7.9; masking in monster 43-130 s and bell's last 10 s) |
| Ducking | **3-4 dB**, attack 20-50 ms, release 250-400 ms | HYPOTHESIS (refs: none, bed moves -1 to +2.6 dB in pauses). Lets the bed sit at about -21 to -22 between lines at a >=8 dB margin under speech |
| Loudness range | 3-6 LU | REF-RANGE 2.2-4.8, a little wider to make room for the silence beat |
| Ending | bed +2 to +4 dB vs the opening, tail 0.5-1.5 s | see section 2 |

Free check on the user's Mac (zero tokens): `ffmpeg -i final.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12` gives integrated LUFS, LRA and true peak. Measure voice and music buses by exporting them separately. Final normalise: `ffmpeg -i in.wav -af loudnorm=I=-14:TP=-1.5:LRA=7 out.wav` (run twice, or use measured values, to hit the target).

Optional ducking in ffmpeg: `[music][voice]sidechaincompress=threshold=0.05:ratio=3:attack=30:release=300[ducked]`. Tune the threshold until the gain reduction measured under speech is 3-4 dB; the numbers above set the target, not the filter parameters.

---

## 5. Library map and free sources

the user's mood labels are **HYPOTHESIS**: guessed from titles and Kevin MacLeod's catalogue; **audition each file before first use** and write the real mood into the cue sheet. All 8 music titles in `library/music/my-vdox-pack/` match incompetech (Kevin MacLeod) titles; confirm each file's source before relying on the licence line below. SFX pack provenance is unknown: confirm its licence once.

### 5.1 Music
| mood needed (ref cue measured) | `library/music/my-vdox-pack/` | gap source and search terms |
|---|---|---|
| Horror ostinato (monster: A minor, ~130 bpm pluck) | Darkest Child, Dark Fog | Pixabay Music: "music box horror", "creepy lullaby" |
| Sustained sad pad (town/dog: F minor, no pulse) | Long Note Four | Pixabay: "sad ambient pad", "emotional strings slow"; YouTube Audio Library mood Sad, genre Ambient |
| Mystery / pivot | Investigations | n/a |
| Tension / chase | Hitman | Pixabay: "tense cinematic pulse" |
| Sad piano ballad (memories Cue B: 76 bpm) | **gap** | Pixabay: "sad piano emotional"; incompetech filter feel somber + piano |
| Wonder / warm bell-pop (bell: D major, 112 bpm) | **gap** | Pixabay: "glockenspiel whimsical", "magical wonder light"; YT Audio Library mood Happy/Inspirational |
| Hopeful end (train: E major, no bass) | **gap** | Pixabay: "hopeful cinematic strings"; YT Audio Library mood Inspirational |
| Comic world | Fluffing a Duck, Run Amok, Sneaky Snitch | 0 comic cues in the refs. HYPOTHESIS: only for a deliberately comic or heist-style world; test once and log |

### 5.2 SFX
| need (ref sound) | `library/sfx/my-vdox-pack/` | gap source and search terms |
|---|---|---|
| bell/ding/ring (bell 11.97, 15.88; partials 1.9-5.4 kHz) | ding, chime, ping (small) | Freesound CC0: "school bell ding", "handbell", "bell ring sustain" |
| low impact / sub-boom (20-64 Hz) | impact-bass-1, impact-bass-2 (not boom-meme) | n/a |
| whoosh / swish (0.9 s, 3.7-3.9 kHz) | whoosh, whoosh-short, whoosh-up, whoosh-cinematic | n/a |
| cut tick (0.13 s) | click, key-press (at about -8 dB) | n/a |
| riser into the turn (not in refs) | riser, riser-short | n/a |
| phone buzz | notification | Freesound CC0: "phone vibrate" |
| opening sparkle (3/6 template) | sparkle (+ whoosh-cinematic) | n/a |
| heartbeat under silence beat (not in refs) | heartbeat (HYPOTHESIS) | n/a |
| typing / keyboard | typing, key-press | n/a |
| coin clink | **gap** (ping is too synthetic, GUESS) | Freesound CC0: "coin drop glass jar", "coin clink"; Pixabay SFX "coin drop" |
| train brake / alarm | **gap** | Pixabay SFX "train brake screech", "emergency alarm"; Freesound CC0 "train brakes squeal" |
| world beds (rumble, room tone) | **gap** | Freesound CC0: "train interior rumble loop", "room tone classroom" |
| glass crack / crack forming | **gap** | Freesound CC0: "glass crack", "ice crack"; a "closing" variant = the same file reversed: `ffmpeg -i crack.wav -af areverse crack_rev.wav` |
| door bang / slam | **gap** | Freesound CC0: "door slam", "gym door push bar" |
| crowd / walla bed (gym, cafeteria) | **gap** | Freesound CC0: "school cafeteria ambience", "crowd walla indoor" |

The library folders and `studio/timing.py` are on the user's Mac, outside the skill. When you can't see them, list each needed file as "confirm in library" with a free-source search term as the fallback.

### 5.3 Licensing (verified from the audio report's sources, 2026-11-14)
- **incompetech (Kevin MacLeod)**: CC BY 4.0, monetization allowed, credit required in the description: `Title Kevin MacLeod (incompetech.com) / Licensed under Creative Commons: By Attribution 4.0 / https://creativecommons.org/licenses/by/4.0/` . If a Content ID claim appears, reply with the track's ISRC. https://incompetech.com/music/royalty-free/faq.html
- **Pixabay (music + SFX)**: free, no attribution, modification allowed, no standalone resale. Neither page addresses Content ID and claims on Pixabay tracks are reported by third parties, so save the download page for every track. https://pixabay.com/service/license-summary/
- **Freesound**: use **CC0** only (or CC BY with credit). **CC BY-NC is not usable in monetized videos.** https://freesound.org/help/faq/
- **YouTube Audio Library**: monetizable for YouTube Partner Program members; CC tracks need credit; filter "Attribution not required". The page does not cover Instagram. GUESS: not explicitly covered for Reels. https://support.google.com/youtube/answer/3376882
- Keep `credits.txt` per episode: track, source URL, licence, date downloaded.

---

## 6. What the refs did (not a recipe)

| ref | music | silence | SFX | mix |
|---|---|---|---|---|
| bell (79 s) | warm D-major bed; music out at 56.5 s on "it stopped" (-88 dBFS for 1.5 s), 11.5 s of room tone, +31 dB slam back at 68.0 s on "My bell." | the only designed silence | dings on cuts (0.01-0.03 s), ~5.3/min | voice-bed +5.2; last 10 s masked |
| memories (179 s) | pad, one change at 83.0 s (46 %), on neither turn nor climax | 12 dips, maybe track rests | 0 confirmed | +8.5 |
| town (158 s) | F-minor pad, swap at 115.0 s (73 %) on "He was one short" | 4 dip-then-boom pairs late | 8 spoken "Clink" without sound, 4 real clinks late, 10 of 11 SFX after 121 s | +12.1, most voice-forward |
| dog (111 s) | same track as town, no event | none | one opener, climax line has no SFX | +10.5 |
| monster (170 s) | bass in 43.5 s, out 130 s, out 152.5 s | none | ~1.4-2.5/min, 0 % cut-locked | +4.4, masking |
| train (131 s) | swap on cut at 104.0 s (79 %) "But I'm faster" | none | brake screeches at climax, rumble drops after "it stops" | +7.2 |

Shared gaps to beat: no ducking, last line never slowed, 5/6 no ending tail, true peak over -1 in 5/6, world-rule sound as SFX in only 3/6.

---

## 7. Rotation (anti-template)

Opener sound, music event type and position, body track, rule-object sound, micro-drops and ending sound rotate between episodes. The fields and their rules are in `templates/rotation-log.md` (core C6, optional rows 6-12); fill them in the cue-sheet header. Choose the character-voice method per character, not by habit.

# QA checklist — score every package before the user records or posts

Score each area out of 10. A package that fails any HARD item scores 0 in that area.
Each item is tagged **[plan]** (checkable on the script sheet + shot list + cue sheet + caption plan), **[read]** (needs the user's read-aloud, or a blind reader for the guess test) or **[cut]** (needs the recording or the export).

**Two numbers per area:**
- **(a) Plan score** = points earned ÷ points checkable now × 10. [cut] items, and [read] items not yet done (an UNCHECKED guess test, the user's read), are left out of both. **Plan gate: every area (a) ≥ 8 and no HARD fail.** Every [plan] item must be checked: it is never "plan-only".
- **(b) Strict score** = points earned out of 10; anything unchecked scores 0. **Final gate, after recording and before posting: every area (b) ≥ 8.** So every [read] and [cut] item has to be checked by then.
- Report both: `Script (a) 9.0 / (b) 7`. A self-judged pass on a [read] item (an author or critic who knows the twist "guessing" it) counts as unchecked.
Numbers come from the tools where possible: `script_check.py` (area 1, pauses, highlights), `plan_timing.py` → `shotlist_check.py` + `pacing_check.py` (areas 2, 5), `measure.py`, `move_check.py`, ffmpeg loudness (cut).

## 1. Script /10 (script.md)
HARD [plan]: rule stated in the first sentence, starting ≤0.2 s · no banned phrase (§9.1) · no moral as the last line and no twist told by a side character (§9.2) · the core rotation fields pass (no family, primary or secondary, in the last 5; emotional outcome and subject pair not in the last 3; reveal move not the last episode's) · no copied line shape (refs' included: bell's "never… not once… birthday" ladder), no 5-word overlap, no skeleton sharing ≥5 of 12 slots and no signature move shared with a gold or ref (§9.4)
- (1) [plan] The rule passes the rubric (script.md §1.2), and the brief's tone holds past the reveal and in the last line (§0.2), or a planned shift is in the header
- (1) [plan] Beats: stake line by 6 s, misread 10–36 %, reveal 49–78 % and ≥10 points from the last episode, climax 69–96 %, last line ≥92 %
- (1) [plan] Twist is fair: 2–4 twist clues, the setup visible ≥30 s earlier (quote it), the false belief attributed, never stated as the narrator's fact
- (1) [plan] Twist isn't given away: ≤2 direct clues (all twist clues listed), no line before the reveal states the mechanism, the joke clue reads as an insult first
- **Bonus (+1, the area stays ≤10) [read]:** blind guess test (script.md §3.3: fresh haiku reader, pre-twist lines only, never self-judged). Not guessed = +1; partial = OK; guessed on #1 = WARN (fix if cheap). The refs and golds were guessed on #1, so this is never a gate
- (1) [plan] Logic pass done (script.md §3.4, all 10 questions): 3 "why doesn't X just…?" answered, every main character placed, the rule holds for background characters and in daylight, one rule grammar, nobody knows what he can't, and the world's belief about the rule is named
- (1) [plan] One motif used ≥3 times, last use in the final 10 %; ≥3 concrete specifics per 100 s; any §9.2 staged contrast has its planted X quoted with a time
- (1) [plan] Sentence mean 6–8 words; 45–65 % of sentences ≤6 words; every fragment adds a new fact
- (1) [plan] Voice (script.md §0.1): casual markers about 1 per 15 s of narration, contractions, ≤1 simile per 30 s (`script_check.py`), and every line passes "would a 12-year-old say this to a friend?"
- (1) [read] The user reads it aloud and changes nothing, or his changes are made. **Any named §0.1 pattern left in (movie line, aphorism, literary gesture) scores both voice points 0**
- (1) [plan] The narrator's final choice costs him something he now knows the price of (script.md §3.3); the last line lands with no moral, doesn't name the mechanism or restate the final shot, and the extra payoff sits inside the final 15 %

## 2. Look /10 (look.md, lighting-color.md)
HARD: custom hero avatar (no noob or classic) [plan] · no Roblox logo [cut] · LightingStyle Realistic, no `Technology` property [plan]
- (1) [plan] The rule object is readable in shot 1 and in ≥50 % of shots (a mark on the body counts only at MS or tighter, look.md L11)
- (1) [plan] Close shots ≥25 %; readable face on every key line
- (1) [plan] Posed or animated body on ≥35 % of shots; nobody frozen in a medium shot while they talk
- (1) [cut] Face-decal swaps hit the key word (±0.1 s); lip flaps on dialogue
- (1) [plan] Real in-engine camera move on ≥70 % of shots, no move type on >40 % of shots, ≥3 types; one rack focus or dolly-zoom on the twist line ([cut]: `move_check.py` confirms)
- (1) [plan] 5–8 locations; 2–3 story props per set; no setup (set + size + angle family) used more than twice
- (1) [plan] A mood per scene with practicals in interiors, a visible lighting or palette shift on the twist cut ([cut]: `measure.py --compare` Δ ≥0.10)
- (1) [cut] Colour targets: median saturation 0.35–0.50, ≤10 % of shots over 0.6, p99 ≥240 in ≥25 % of shots, p1 10–25
- (1) [plan] Build scope inside the caps of pipeline.md "Build budget" (sets, rigs, face PNGs, poses, contact poses, special builds, VFX), with the build-cost block filled in the shot list, and nothing on look.md §16's Roblox-limits list
- (1) [plan] Final shot ≥3 s on the rule object's final state

## 3. Audio /10 (audio.md)
HARD: no Roblox in-game music [cut] · no paid generation without the user's OK [plan] · true peak ≤ −1.0 dBTP [cut]
- (2) [plan] Narration at 200–240 wpm (≤80 s: 160–240) with the designed pauses of script.md §6: 2–3 pauses of 0.6–1.3 s, A after the twist line and B before the last line ([cut]: `pacing_check.py` on the real words.json)
- (2) [plan] 1–2 music events at 45–90 %, on a cut, landing on the climax or twist line; event-1 type differs from the last episode (audio.md §2)
- (2) [plan] 2–5 real SFX per minute, ≥35 % on cuts, ≥50 % in the last 35 %; the rule object has its own sound, ≤2 before 65 %
- (1) [plan] Character voices: ≤3 besides the narrator; designed voice or a shift ≤+10 st; menacing adults −4 to −6 st
- (2) [cut] −14 LUFS integrated, voice 7–10 dB over the bed, no clipping
- (1) [cut] Music resolves under the final shot (no hard cut to black mid-phrase)

## 4. Captions /10 (captions.md)
HARD [plan]: captions never cover a face or the rule object (both stay above 55 % of frame height) · they sit inside the IG/Shorts safe zone
- (3) [plan] One word per caption (or the episode's chosen style), centred at about 70 % of frame height, at spec size, font and outline
- (3) [cut] Caption onset −2…0 frames from the word start
- (2) [plan] Highlights: only names, rule words and 1–2 peak words (the category rule comes first), at most one per sentence, ≤13 % of the words after the hook (a lower % is fine)
- (2) [plan] Pop 125 % → 100 % over 4 frames; no other caption animation

## 5. Pacing /10 (pacing.md)
- (2) [plan] Mean shot 1.3–2.5 s; cut rate 20–48 per minute
- (2) [plan] ≥55 % of cuts land on sentence starts, leading the first word by 0–2 frames; no beat-synced cutting
- (2) [plan] No shot over 3.5 s except 1–2 designed holds of 4–6 s at the reveal or ending
- (2) [plan] First 3 s: rule spoken, first cut by 2.5 s, frame 1 already moving
- (2) [plan] Runtime within ±5 % of the target runtime in the script sheet header (60–180 s), with the beats placed by % (script.md §3.2)

## 6. Beats the refs (upgrades.md)
- Count upgrades U1–U14 met. **Needs ≥10.** (a) counts the ones a plan can show, out of those it can check; (b) counts all 14.

## Scoring log (add to `reels-shorts/projects/<episode>/QA.md`)
| area | score | failed items | fix |
|---|---|---|---|

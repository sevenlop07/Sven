# captions.md: word-by-word captions at 1080x1920

> **Toon style (the default now): use style-toon.md §6 instead of this spec.** Phrases of 2–4 words, ALL CAPS, about 56 px, one coloured key word, fade-in, made with `tools/make_caps_toon.py`. The one-word spec below is the older moody-ref style.

Tags: **REF-RANGE** = measured in the 6 refs (4/6 use one word per caption: bell, memories, monster, train; town and dog use 1-3 word phrases); **HYPOTHESIS** = beat-the-refs bet or an unmeasured platform convention. Machine-readable twin: `templates/caption-preset.json`.
Limits: no view data. Font names are GUESSES from glyph shapes. The caption-onset lead (-54 to -81 ms) was not independently reproduced (the check was inconclusive), so the timing rule below is a window to aim for, verified by hand on 1-2 words per video.

## 1. Spec (1080x1920, 30 fps)

| item | value | tag |
|---|---|---|
| Chunking | **one word per caption** (refs 1.00-1.05 tokens per caption, 2.5-3.8 captions/s). Phrase mode (1-3 words, mean 1.65, town/dog) only for reads of 245+ wpm; choose one mode per video | REF-RANGE |
| Font | **Montserrat ExtraBold** (free, Google Fonts). Fallback order: Poppins ExtraBold, Arial Black. Condensed phrase mode: Anton (closest free to Impact) | GUESS from glyphs (bell/memories look like Montserrat/Poppins heavy) |
| Size | **104 px** font (ascender-to-descender extent about 101 px = 5.25 % of height). Lighter look (monster/train): 72 px | REF-RANGE (101 px bell/memories; 66-72 px monster, train, town, dog) |
| Position | horizontal centre 50 %; **vertical centre at 70.0 % of height = y 1344 px** (text spans about 1294-1394). Never move it per caption | REF-RANGE (bell/memories 70.0 %, monster/train 70.6 %, IQR +-0.15 %; town/dog 61.7 %) |
| Max width | 65 % of frame (675 px); long words shrink to fit, up to 80 % | REF-RANGE (max 62-82 %) |
| Fill | white `#FFFFFF` | REF-RANGE |
| Punctuation | captions drop commas, full stops and quote marks; keep `?`, `!` and apostrophes (`make_caps.py` does this) | HYPOTHESIS (one word per caption reads cleaner without them) |
| Outline | black, **12 px** (about 9 px at 720p x1.5), round joins, outside stroke. Lighter variant 7-9 px | REF-RANGE |
| Shadow | black 100 %, offset x0 / y+6, blur 0-4 px (outline merges with the shadow: 98 % dark out to 9 px) | REF-RANGE |
| Pop | scale **125 % to 100 % over 4 frames (133 ms)**: 1.25, 1.18, 1.10, 1.04, 1.0. No fade-out; the next caption replaces it | REF-RANGE (bell 1.22..1.0, memories 1.25..1.0; monster/train none) |
| Onset | **-2 to 0 frames vs the word start** (default -1 frame = -33 ms). Target: >=75 % of captions within +-100 ms of the word | REF-RANGE (4 refs measured -54 to -81 ms mean, bell +21 ms, train +103 ms and the worst); the exact lead is unverified, see limits |
| Gap between captions | <=1 frame in >=85 % of cases (no blank between words) | REF-RANGE (85-94 % in 5/6; train 27 % blinks off for 100 ms, avoid) |
| Duration | typical 0.2-0.3 s; minimum 0.1 s; a word held until the next one starts. In a pause the last caption stays on screen | REF-RANGE (median 0.20-0.37 s, p10 0.10) |
| Watermark | **none by default** (4/6 refs had none; do not use the Roblox logo or a classic avatar as an icon). Optional channel handle: top-left, bold white, dark outline, about 33 px tall, 40 px from the left, 130 px from the top, static | REF-RANGE n=1 (bell, @StudGang) for the position |

### 1.1 Highlight rule (accent color)
- **One accent color per video.** Default yellow `#FEDD30` (bell) or red `#FD3433` (memories). Pick by world mood: warm/wonder yellow, horror/violence red (HYPOTHESIS; the refs do not show a mood mapping). Rotating between episodes is allowed and logged (see section 4).
- **Hook:** the whole first sentence in the accent color, however long it runs (bell 0.2-3.7 s, memories 0.0-4.07 s; 2/6 refs; others none). Optional; alternate it on/off across episodes.
- **After the hook, the category rule comes first:** accent only character names, the rule's words (its object, its state words), and the 1-2 emotional peak words of the episode. **At most one accent per sentence** (one word, or one 2-word name like "Mr. Hale"). Most lines get none. **≤13 % of the words is a ceiling, not a target**: a lower share is fine; never pad the list with props or ordinary nouns (radio, duck, Friday) to reach a number. Never function words ("the", "a", "and"). HYPOTHESIS inside the ref range (bell about 19 % of later words, memories about 5 % in 35 short bursts; the others none). `script_check.py` prints the share and the accent list to check by category.
- Train used one fixed lime `#E2FD00` for every word, so a single colour is a valid alternative; it is not the default because it loses the emphasis channel.

### 1.2 Safe zones (HYPOTHESIS: general platform conventions, not measured here)
Reels, Shorts and TikTok overlay a caption/handle block and an action-button column. Keep all text inside **x 60-900 and y 250-1550 px**. The caption centre at y 1344 with a 675 px max width spans x 202-877 and y 1294-1394, so it clears the bottom block (about the last 20 %, y > 1536) and the right button column (x > 960). Check once per platform on a real upload. Watermarks never go in the bottom 20 % or the right 12 %.

## 2. Quality checks
| check | pass |
|---|---|
| caption centre y | 69.5-70.5 % of height |
| text height | 5.0-5.5 % (104 px font) |
| gap <=1 frame | >=85 % of captions |
| onset within +-100 ms of the word | >=75 % |
| first caption | on the first word (0.00-0.20 s) |
| accent words after the hook | names, rule words, 1-2 peaks only; ≤13 %; at most one per sentence; none on function words |
| caption contrast | renders must be caption-free for the colour tests used elsewhere (white captions clip at 255) |

## 3. Generating captions automatically (zero tokens, on the user's Mac)

Pipeline: narration audio (final voice track) -> word-timestamp transcript JSON -> caption events (ASS file) -> ffmpeg/libass burn-in, or import the ASS into the NLE.

1. **Word timestamps.** Preferred (HYPOTHESIS): force-align the known script to the voice take, which avoids mis-heard words: WhisperX `whisperx voice.wav --model small --align_model WAV2VEC2_ASR_BASE_960H --output_format json` or `stable-ts` alignment. Alternatives: `faster-whisper` with `word_timestamps=True`, or Parakeet. Known issue: Parakeet word timestamps sit on an 80 ms grid with zero-length gaps, so use captions' `--lead` to calibrate and verify by eye. ElevenLabs `creative_transcribe_audio` also works but costs credits, so do not use it unless the user says yes.
2. **Accents.** Preferred: `--sheet script-sheet.md` lights exactly the word in each row's `caption highlight` cell, inside that row only, so a rule word or a name that repeats is not lit everywhere ("whole line" lights the hook row). Old way: `--accent "Chloe,bell"` lights every occurrence of those words. Matching is case-insensitive with punctuation stripped.
3. **Run** `python3 tools/make_caps.py words.json caps.ass --sheet script-sheet.md` to produce `caps.ass`, then:
   `ffmpeg -i video.mp4 -vf "ass=caps.ass:fontsdir=fonts" -c:a copy out.mp4` with `Montserrat-ExtraBold.ttf` in `./fonts/`. Use a caption-free export for colour and clipping tests. It prints the accent share after the hook separately (ceiling 13 %). To light one occurrence by time instead, use `--accent-at "31.0,97.4"`. On a plan, run it on `plan_timing.py`'s `words_planned.json` to check the highlight plan.
4. Spot-check 1-2 words per video against the waveform (onset -2 to 0 frames); adjust `--lead` once.

Notes: ASS colours are BGR (`FEDD30` yellow becomes `&H0030DDFE&`; the script converts). `\an5\pos(540,1344)` centres the word on x 540 and y 1344, so the pop scales around the centre. Phrase mode (Anton, 1-3 words) is a manual variant: group tokens and drop the pop.

## 4. Rotation (anti-template)
Allowed to vary between episodes, logged in the rotation log (optional row 25, `templates/rotation-log.md`) and the cue-sheet header: accent colour (yellow `#FEDD30` / red `#FD3433` / none), hook fully accented or not, one-word vs phrase mode (phrase mode only at 245+ wpm). Fixed across episodes (channel identity, not content): font, position, outline, pop.

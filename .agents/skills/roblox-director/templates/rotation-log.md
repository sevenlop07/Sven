# Rotation log (one row per episode; the only place rotation is defined)

The live log is `reels-shorts/projects/ROTATION-LOG.md`; a log supplied in a brief replaces it. Copy the header below into it once, then add one row per episode **when the plan is written**, and update it after the cut. Every file that says "rotate" points here. `tools/script_check.py sheet.md --log ROTATION-LOG.md --ep 4` checks the core fields and skips the plan's own row.

**Controlled words.** The `subject`, `outcome` and `reveal move` cells use only the words in `tools/skeletons.txt`, and `family` is numbers (`3 + 10`). `--log` fails any other word and suggests a mapping. Free-text notes go in `notes`. Mapping hints: dad/mom/son → `parent-child`; grandpa or grandma + their partner → `grandparent-partner`; grandparent + the narrator → `grandparent-child`; neighbour → `stranger-family`; "lifelong love" → `romance`; "reconnects" → `reunion`; "kept her safe" → `protection`.

Why: YouTube's YPP does not monetize "templated storylines" or "characters … put in the same situation over and over again with the same outcome" (POLICY). The refs are templated themselves (town and dog share a track, an avatar and an opener). Round 2 repeated ep2's outcome (an old man's love for Grandma) because the log had no field for it.

## Core fields (mandatory, every episode)

A missing core field in an old row is **back-filled from that episode's plan files** (script sheet header, cue sheet) or asked from the user. It is never assumed free.

| # | field | values | rule | from |
|---|---|---|---|---|
| C1 | twist family, primary + secondary | 1-11 (script.md §4), e.g. `3 + 10`; use the tie-break table in script.md §4 | **neither** in the last 5 episodes (two families that share a mechanism are the same family); hidden sacrifice max 1 in any 5, never for a sick or dying relative | script.md §4 |
| C2 | twist subject (who → whom) | the `subject` values in `tools/skeletons.txt` (parent-child, grandparent-partner, friend-narrator, sibling, self …) | **not in the last 3 episodes** | script.md §4 |
| C3 | emotional outcome | reunion / romance / friendship / sacrifice-revealed / protection / loss / dread / freedom / exposure | **not in the last 3 episodes** | script.md §4 |
| C4 | tone (brief → ending) | creepy / sad / warm / funny, plus any planned shift ("creepy → warm at 57 %") | logged, not rotated: the user's brief sets it; the ending must match it unless the shift is planned | script.md §0.2 |
| C5 | reveal % | the **twist line** (the TWIST row), as a % of runtime | ≥10 points from the last episode | script.md §3 |
| C6 | music event 1 type | A silence drop / B cue change / C layer move | differs from the last episode; between two A's, at least 2 episodes without A (A in ep1 → next A in ep4 at the earliest) | audio.md §2 |
| C7 | reveal move | the `reveal` words in `tools/skeletons.txt` (whose-sign, what-i-was, i-caused-it, rule-works-otherwise …) | differs from the last episode (round 3 repeated ep3's "the sign was for the person next to me") | script.md §4 |

## Optional fields (log them when you can; a missing one is free: choose, and log it now)

| # | field | values | rule | from |
|---|---|---|---|---|
| 1 | misread source | crowd / official / sign-record / narrator alone | differs from the last episode | script.md §3.3 |
| 2 | rule type | trace, everyone-has-X, body mark, trade, place … | not the same 3 episodes in a row | script.md §1 |
| 3 | ending payoff type | reversal / rule → reward / time jump | differs from the last episode (HYPOTHESIS) | script.md §8 |
| 4 | last-line type | callback image / sound callback / rule-object state / dark open line / small action with the motif | differs from the last episode | script.md §8 |
| 5 | act-1 example shape | price ladder, funny exposure … | the price ladder never in back-to-back episodes | script.md §1.1 |
| 6 | music event position % | number | ≥10 points from the last episode | audio.md §7 |
| 7 | music event 2 type | A / B / C / none | free (logged to learn) | audio.md §2 |
| 8 | body track | file name | not the last episode's | audio.md §7 |
| 9 | opener sound | none / low impact / rule-object sound (counts toward the rule-sound cap) / whoosh-short / sparkle | differs from the last episode | audio.md §7 |
| 10 | rule-object sound | ding / clink / crack … | not the last episode's | audio.md §7 |
| 11 | ending sound | log the sound **on the last word** if there is one (rule-object sound), else the tail: held note / silence 1.0-1.5 s | differs from the last episode | audio.md §7 |
| 12 | micro-drops | yes / no | alternate (we are testing them) | audio.md §2 |
| 13 | twist camera move | dolly-zoom / rack focus | alternate | look.md §3.3 |
| 14 | whip intro | yes / no | yes at most every other episode | look.md §5 |
| 15 | mirrored bookend | yes / no | yes at most every other episode | look.md §11 |
| 16 | prop-death shots | yes / no | yes at most every other episode | look.md §10 |
| 17 | lead location type | interior / exterior / vehicle | differs from the last episode | look.md §9 |
| 18 | where the rule object lives | on people / on buildings / sky or screen / objects / shadows and light | differs from the last episode | look.md §6 |
| 19 | hold placement | reveal / ending / both | differs from the last episode | pacing.md §4 |
| 20 | ending pace | slower ≥1.2x / faster ≥12 % | alternate | pacing.md §4 |
| 21 | mean shot (s) | number | ≥0.3 s from the last episode | pacing.md §2 |
| 22 | twist light shift | dark → bright warm / warm → cold / palette swap | differs from the last episode | lighting-color.md §4 |
| 23 | payoff light direction | brighter / darker | darker in ≥1 of every 4 episodes | lighting-color.md §2 C11 |
| 24 | night practical colour | cyan / amber / red / green … | differs from the last episode | lighting-color.md §5 |
| 25 | caption accent colour + hook accented | yellow / red / none; yes / no | hook accented: alternate | captions.md §1.1 |

## Log (copy this header into ROTATION-LOG.md; keep these column names)

Core fields have their own columns; optional fields go in one `optional` cell as `field=value; field=value` (e.g. `opener=none; twist move=rack; hold=ending`), so the table stays readable.

| ep | date | family | subject | outcome | tone | reveal % | event type | reveal move | skeleton | optional | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

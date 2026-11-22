# script.md: writing an "In this world..." story script

Read this before writing any episode script. (The `team/` evidence files cited below live outside the skill; every number you need is in this file.) It covers the rule, title and hook, beat map, twist, motif, sentences, dialogue, ending, banned list and the workflow. The production sheet format is in `templates/script-sheet.md`. **Don't open `examples/` until your rule, skeleton and first draft exist** (§10): the golds are for a quality comparison after drafting, never a starting point. In round 2 an agent that read them first rebuilt gold-1 beat for beat.

**Evidence.** Every number comes from the 6 reference reels (bell 79 s, memories 179 s, town 158 s, dog 111 s, monster 170 s, train 131 s) as measured in the original reference analysis (script, audio and pacing/caption analysts plus a critic pass; not kept in this repo — the numbers below are its distilled result). No view or retention data exists for any ref. So a ref range shows what the refs did, not what works.

Tags used on every rule:
- **REF-RANGE**: measured from the 6 refs. Stay inside it.
- **HYPOTHESIS**: our bet to beat the refs. Keep it, and A/B it on the user's own analytics (retention at 3 s, 30 s and the reveal; comments per 1k views).
- **POLICY**: platform rule (YouTube Partner Program), not taste.

---

## 0. Voice (the user's rules, non-negotiable)

| rule | number | tag |
|---|---|---|
| Very simple English, A1-A2 | Flesch-Kincaid grade ≤2.5; ≤5 % of words have 3+ syllables (refs 1.1-2.9 and 2.8-6.1 %) | REF-RANGE |
| First person, one narrator, told to a friend | 6/6 refs first person; narrator unnamed by default (5/6) | REF-RANGE |
| Raw and casual | casual words where they fit (§0.1); no strong swearing (0/6 refs swear; young Roblox audience) | HYPOTHESIS |
| Show feelings with actions | "I stopped laughing." "He put salt in his coffee." never "I felt so guilty" | REF-RANGE (bell, town) |
| 3+ syllable words only when they are concrete nouns | hospital, medicine, apartment, detention; never enormous, incredible, devastating | REF-RANGE |

### 0.1 Testing the voice (a [plan] item: never "plan-only")

A script can pass every number and still read like an edited picture book. These tests run on the sheet (`tools/script_check.py`, patterns in `tools/patterns.txt`); all are HYPOTHESIS (the round-1 critic's bet on the user's stated "raw, casual" voice) until his ear and analytics agree.
- **Casual markers about 1 per 15 s of narration** ("honestly" counts anywhere except the gold-shaped flaw admission "Honestly, I [verb]."), (kinda, bro, dude, I mean, literally, honestly, basically, so yeah, like as a filler, way past, super…), where they fit. Never 2 in one sentence, never the same one 4 times.
- **Contractions**: "didn't", "it's", "I'd". An uncontracted pair ("could not") only when the line stresses it.
- **0 narrator-tone patterns**: aphorisms ("[Abstract] [verb] when you…"), movie lines ("a partner who won't laugh"), literary gestures ("held out his hand"), written English ("In it,"), "That's when…", named feelings, staged contrasts beyond §9.2.
- **Similes ≤1 per 30 s.** A polished comic simile ("Like a robot falling down stairs.") is the kind a model reaches for.
- **The ear test, line by line:** would a 12-year-old say this out loud to a friend? Then The user reads it aloud; that read is the final test.

17 lines from the round-1 draft (E02) and what fixed them. Copy the fix pattern, never these lines:

| line | problem | try |
|---|---|---|
| And cracks never go away. | narrator states the false belief as fact; trailer tone | And grown-ups say they never go away. |
| One lie, 41 years ago. | trailer fragment | And it was from one lie. Like, 41 years ago. |
| He said yes. He couldn't. | staged reveal beat, written rhythm | He said yes. He could not dance at all. |
| Right cheek. | filler fragment; the picture already says it | cut |
| In it, his crack went past his chin. | "In it," is written English | In the photo, his crack went way past his chin. |
| Bad old camera. | a writer's clipped dismissal, no fact | I figured the camera was just old. |
| Like a robot falling down stairs. | polished comic simile | He looked like he was falling over the whole time. |
| Maybe if he learns, it'll fall off. | the joke states the twist's mechanism | an insult that hits the hero and isn't the mechanism |
| That night, Grandpa held out his hand. | literary gesture | That night, Grandpa asked me to dance with him. |
| I need a partner who won't laugh. | movie line | Come on, kid. Just one song. |
| I stepped on his 5. | written elision, a joke built for reading | I stepped on his like 5 times. |
| My crack was half as long. | stiff comparative | My crack was half gone. |
| Lies close up when you make them true. | aphorism: the moral, spoken | a concrete fact: "Every time I get a step right, it gets a little smaller." |
| He wasn't the biggest liar in town. He was just the slowest dancer. | staged contrast the viewer never believed (§9.2) | cut both |
| We danced three songs, and I never let go. | "never let go" cliché | We danced three songs. I didn't let go of his hand once. |
| On the second song, my cheek got warm. | fine (keep): the only sensory line in act 3, so add more like it | keep |
| He said yes again. This time, it was true. | neat bow that explains the final shot; gold-1's "this time" frame | He said yes. (the sealing shot does the rest) |

### 0.2 Tone modes (the brief's tone holds past the reveal)

**The tone the user asks for (creepy / sad / warm / funny) is still the tone after the reveal and in the last line**, unless the sheet header plans a shift ("Tone: creepy → warm at 57 %, because …") and the rotation log records it. A creepy brief that turns into a rom-com at the twist fails the brief (round-2 critic ruling).

| tone | script | picture | sound | evidence |
|---|---|---|---|---|
| **creepy** | dread covers most of the runtime (≥60 %, HYPOTHESIS); a threat or rumor set up in act 1 pays off (never drop it); the twist keeps or deepens the dread (families 3, 8, 9, 11 suit it); end on a dark open line (monster: "one of them touched me") or a second sign nobody can explain. Losses shown by props left behind, never on screen | `scaryNight` (dark but not grey, one coloured practical, C9); low angles on the threat; frame 1 = hero + rule object + threat; act palette shifts; faster cutting at the end (≤0.88x) | horror ostinato (music-box or pizzicato pluck) + a sub-bass layer for the stakes, stripped at the reveal; world bed drops when the rule acts; real threat sounds (the gap monster leaves) | monster: A-minor pluck ~130 bpm, bass in at 43.5 s and out at 130 / 152.5 s, hat / shoe / rope prop deaths, blue → orange → red dusk, mean shot 1.23 s, last 15 s 0.88x (REF n=1) |
| **sad** | grief shown as actions (town: "He put salt in his coffee."); one silence beat; the ending slows (≥1.2x) | `sad` (cool, soft) for the low, `sadWarm` for the payoff; the ending warmer than the rule section (C8) | a sustained pad with no pulse, or a sad piano cue change at the turn | bell hospital (sad preset), bell's 1.29 s silence + 1.88x slower ending, town/dog F-minor pad (REF) |
| **warm** | a small funny or tender act-1 example, a payoff that turns the rule into a gift (family 7) | `normalDay` → `sadWarm` / `twistReveal` golden pop; ending warmer | wonder bed (glockenspiel / light pluck), a cue change into a hopeful track | bell's D-major 112 bpm bed, memories' golden reveal (+0.25 bright), train's hopeful E-major end (REF) |
| **funny** | act-1 examples with a price (they are the refs' only comedy); the twist still costs someone something | `normalDay`; quick inserts on the joke object | comic tracks and meme SFX are untested: at most one comic SFX (audio.md §3) | refs: funny examples in memories, dog, town; 0 comic music cues (so the rest is HYPOTHESIS) |

**Safety, every tone** (young Roblox audience; POLICY-minded ruling): no adult-wants-a-child framing, and an adult threat is uncanny, never predatory; no gore; deaths happen off screen and show through props; no strong swearing (§0).

---

## 1. The world rule

### 1.1 Formula

`In this world, [an everyday thing] [does one strange thing] [when / for whom].`

| part | rule | tag |
|---|---|---|
| Opening words | "In this world," (4/6) or "In this town," (2/6). First word at 0.0-0.2 s. | REF-RANGE (6/6, 0.00-0.16 s) |
| Length | One sentence, 8-15 words, spoken in 2.0-4.5 s. | REF-RANGE (mean 3.4 s) |
| Tense | The rule is in present tense. The story is in past tense. | REF-RANGE (5/6) |
| Limit or cost | Sentence 2 or 3 adds a limit: never, gone, only, can't, one day. By 12.5 s. | REF-RANGE (5/6) |
| Fully clear | Every part of the rule the twist needs is said by ≤9 % of runtime and ≤15 s. | REF-RANGE (mean 8.7 %, 4.2-18.9 s; train is late at 14.5 %) |
| Rule object on screen | The rule is visible during sentence 1 (bells over heads, a shop sign, tears, monsters on lawns). | REF-RANGE (5/6; dog waits 18 s) |
| Act 1 examples | 1-3 concrete examples of the rule. At least 1 is funny or has a price. Do not reuse the price-ladder shape (A buys X, B buys Y, C is worth most) in back-to-back episodes. | REF-RANGE (memories, dog, town, monster) |
| Plant for the ending | One act-1 example quietly sets up the ending (dog's frame, gold-2's grandpa). | REF-RANGE (dog, town) |

Good: "In this world, your footprints glow for one day, everywhere you walk." (12 words)
Bad: "See, a hundred years ago, the entire planet froze, and..." (train: a 23-word backstory before the rule is clear; rule clear at 18.9 s).

### 1.2 Rule scoring rubric (score before writing anything else)

Score each test 0, 1 or 2. Max 12.

| # | test | 2 | 1 | 0 |
|---|---|---|---|---|
| 1 | Understood in 3 s, sound off (picture + first caption words) | a stranger gets it from frame + 6 words | needs the full sentence | needs act 1 |
| 2 | Showable in Roblox as an object, decal, particle or BillboardGui | one prop, decal or particle shows it, and its state can change on screen | needs a cutaway or text | needs narration only |
| 3 | Personal cost to the narrator | narrator pays daily (never rung, 2045, someone at my window) | cost hits others | no cost |
| 4 | Built-in reversal | the same rule can flip from cost to gift or from gift to trap | a flip needs a new rule | no flip possible |
| 5 | Comment bait ("would you...?", "what would yours say?") | every viewer can answer about themselves | only some can | nobody can |
| 6 | Freshness vs the crowded lane | rule type not in the market's top 3 (below), no ref copy, no market title with the same trigger | top-3 type with a new object, or a known story's theme with a new object or mechanism | "X is deadly" / forbidden act / a ref, film or well-known story premise (same object doing the same thing) |

**Pass bar: ≥9 of 12, with test 1 = 2, test 2 = 2 and test 6 ≥ 1.** (HYPOTHESIS.)
**The market's top 3** (32 premise shorts tallied by title, frequency only, no views): 1. forbidden act / "X is deadly" (8), 2. everyone-gets-X (5), 3. creature/monster (4) and trade/sell (4, tied). Smaller lanes: body/appearance shows hidden info (3, incl. "lie → turn blue"), place you can't leave (3), counter/number (2), time limit, sound trigger, age ritual (1 each). The 31 premise lines are in `tools/market_titles.txt`: search it for your trigger. So a lie-shows-on-your-body rule scores test 6 = 1 at most (a market title has the trigger), and a Pinocchio nose or a Snowpiercer train scores 0. A "known story" is one most 10-year-olds know: a fairy tale, a Disney/Pixar film, a famous book or film.

**When the user gives the rule,** the 5 candidates are variants of his line (wording, object, limit), scored the same way. Keep his line unless a variant scores ≥2 higher, and say why. **Test 4 scores whether a flip is possible, not whether line 1 says it; for a rule-misread twist (family 4), score it on the hidden rule.** Never put the flip in the rule line when the twist depends on it (a rule-misread twist dies if line 1 states the real rule), and check every candidate against the planned twist family before choosing.

Calibration (opinion, scored by the method above): bell 12, monster 9 (creature lane), train 7 (Snowpiercer copy, fails). Gold-1 footprints 11, gold-2 hand date 11.

---

## 2. Title, hook and cover

| rule | detail | tag |
|---|---|---|
| Title = the rule | The title is the spoken first line minus emoji and hashtags. | REF-RANGE (every visible market title) |
| Format A (majority) | `In This World, Your [CAPS NOUN] [verb]... [emoji]`. Caps on the rule noun in ~14 of 28 titles, emoji in 20 of 28. | REF-RANGE |
| Format B (minority) | Sentence case with a full stop: `In this world, your hand shows the day you'll meet your best friend.` | HYPOTHESIS (stands out from the template publisher; A/B against A) |
| Format C | Rule + stake: `In This World, Your Hand Shows A Date. Mine Says 2045 😭` | HYPOTHESIS |
| Line 1 = rule | Same words as the title. | REF-RANGE (6/6) |
| Personal stake by 6 s | First me / my / mine line starts by 6 s (about 22 words at 220 wpm). | HYPOTHESIS (only bell 4.2 s and monster 2.2 s do it; others 14-33 s) |
| First frame moves | Frame 1 is already a push, track or whip. A whip only if motivated, never in back-to-back episodes. | REF-RANGE + critic ruling |
| Cover text | 2-5 words, asks the question, never spoils the twist. It lives on the cover frame and thumbnail only. Frame 0 of the video shows the world plus the spoken caption, never a title card. | the user's standing rule |
| Hashtags | In the description: `#roblox #robloxstory #shorts`. Don't copy the "#rblx #stories" template publisher's exact title pattern. | REF-RANGE (market) |

---

## 3. Beat map

### 3.1 Windows (REF-RANGE, from `script-beats.json`)

| beat | refs (% of runtime) | median | rule |
|---|---|---|---|
| rule fully clear | 5.3-14.5 | 8.3 | ≤9 % and ≤15 s |
| narrator stake | 0-24.8 | 9.7 | by 6 s (HYPOTHESIS) |
| inciting moment | 12.3-52.2 | 25.5 | not fixed; vary it |
| misread plant (false belief the viewer shares) | 9.5-36.0 | 21.1 | 10-36 % |
| doubt (first crack) | 20.7-43.1 | 39.4 | before the reveal |
| reveal / twist line | 49.0-77.7 | 59.8 | 49-78 % (the logged "reveal %" is always the **twist line**, the row tagged TWIST) |
| narrator's turn | 60.6-91.5 | 67.2 | after the reveal |
| climax | 68.8-95.8 | 83.7 | 69-96 % |
| extra payoff | 85.9-96.0 | 88.8 | inside the last 15 % |
| last line starts | 92.4-98.8 | 97.7 | ≥92 %, speech ends ≤1.5 s before video end |

Act word share in the refs: act 1 13-54 % (mean 27), act 2 24-65 % (mean 37), act 3 22-51 % (mean 36). Keep every act ≤55 % (HYPOTHESIS: memories' 65 % act 2 holds the subplot that never pays off).

### 3.2 Beat targets for any runtime (60-180 s)

The §3.1 windows are % of runtime, so they hold at every length. **Seconds = % × runtime / 100** (117 s, reveal at 68 %: 79.6 s). Pick Variant A (early reveal) or B (late reveal), or any reveal inside 49-78 %, so the reveal moves **≥10 points from the last episode** (POLICY + HYPOTHESIS: YouTube does not monetize "templated storylines"; a fixed beat % every episode is a template).

| beat | window % (REF-RANGE) | A: aim % | B: aim % |
|---|---|---|---|
| rule line ends | ≤7 | 3-6 | 3-6 |
| stake line starts | by 6 s (HYPOTHESIS) | | |
| rule fully clear | ≤9 and ≤15 s | 7-9 | 7-9 |
| inciting | 12-52 | 15 | 22 |
| misread plant | 10-36 | 22 | 32 |
| doubt | before the reveal | 42 | 55 |
| reveal / twist line | 49-78 | 52 | 68 |
| turn | after the reveal | 60 | 74 |
| climax | 69-96 | 78 | 86 |
| extra payoff | ≥85 | 87 | 90 |
| last line starts | ≥92 | 94 | 95 |

The aim % are HYPOTHESIS (points inside each window, split early / late); anywhere inside the window passes.

**Word budget** at 220 wpm (3.67 words/s): `spoken words ≈ (runtime − 0.1 − pauses − tail − slow-read extra) × 3.67`. Pauses are 1.4-3.6 s (§6), the tail 0.5-1.5 s, and a slow-read line adds words / 3.67 × (1/rate − 1) (a 2-word line at 0.6x adds 0.4 s). With 2.2 s of pauses, a 1.2 s tail and no slow reads:

| runtime (s) | 60 | 90 | 120 | 150 | 180 |
|---|---|---|---|---|---|
| spoken words | ≈207 | ≈317 | ≈427 | ≈537 | ≈647 |

For a runtime in between, use the formula (or interpolate). A ≤80 s story may read at 160-200 wpm (`audio.md` §1.2): then budget words × wpm / 220 and run the tools with `--wpm`.

Content by length: **≤80 s**: 1 act-1 example, ≤2 named characters, pauses A and B only. **≥130 s**: add one proof scene in act 2 (a scene that shows the misjudged person's real nature without giving away the twist, like gold-2's backpack on the roof). Never add a subplot that does not pay off (memories' 21 s theft subplot, flagged).

### 3.3 Story rules inside the map

| rule | tag |
|---|---|
| The narrator shares the false belief and has one flaw he fixes by acting. | REF-RANGE (5/6; train's narrator has none) |
| Rule-misread twist (family 4): the false belief is the rule as everyone states it. It counts as the misread plant only when a source (official, crowd, sign, the narrator) repeats it inside 10-36 %; the limit line in sentence 2-3 alone does not count. | ruling (keeps the plant inside the window) |
| The misread's source changes every episode: crowd, official, sign/record, the narrator alone. Never write "Everyone thought". | REF-RANGE (6/6 have a misread) + critic ruling |
| Hide ≥1 clue inside a joke or insult that reads as an insult first and is literally true about something. It never paraphrases the twist's mechanism (town's "How does he do that?" points at a mystery, not the answer; "Maybe if he learns, it'll fall off" gives the twist away). | REF-RANGE (town, monster, dog) + critic ruling |
| The narrator finds the truth through an object or an action, not a speech. | REF-RANGE (bell, town, monster do; dog, memories, train are told) |
| The twist is fair: **≥2 twist clues** before the reveal, each one a concrete thing the viewer saw or heard, and **≤2 of them point straight at the mechanism**. A twist clue is any pre-reveal line whose meaning changes after the twist: list them all in the header (no total cap; the blind test measures the load). No line before the reveal states the mechanism: write the mechanism words in the sheet header ("Twist mechanism words") and `script_check.py` searches for them. | HYPOTHESIS |
| **Blind guess test: a beat-the-refs bonus, not a gate (never self-judge).** `script_check.py sheet.md --pretwist pretwist.txt` writes every line before the first reveal row. Give ONLY that file to a fresh, cheap reader: with an Agent/Task tool, spawn a new agent on the cheapest model (haiku) and ask "Here is the first part of a short story. Give your top 3 guesses for the twist, one line each." No Agent tool: leave `pretwist.txt` for the orchestrating session or for the user to read and guess, and write `Guess test: UNCHECKED`. Results: **not guessed** (no guess has the who or the why) = a bonus point; **partial** (who or why, not the mechanism) = OK; **guessed on #1** (same who and why) = WARN: weaken the strongest clue if it's cheap, otherwise ship (a match on #2 or #3 is OK). Write the reader and the 3 guesses verbatim in the header. **Calibration:** the same blind haiku test guessed bell (a ref) and both golds on guess #1; round 2 passed fully and round 3 partly. Most good twists in this genre are guessable, so the test can only earn a bonus. The author, a critic or any agent that has read the twist never judges it (round 2's critic said "guessed"; the blind reader missed it). | REF (rounds 2-3 + ref/gold calibration) |
| Tag `misread` on the **first line that states the false belief**, attributed (said, called, thought, believe, "grown-ups say"), not on an observation that later supports it. That line sits in 10-36 %. | critic ruling (round 3) |
| The narrator tells the story after it happened, so he never states the false belief as a present-tense fact. Attribute it: a person, a sign, "grown-ups say". | critic ruling (matters most for family 4) |
| The climax is one action that uses the rule (sit with her, cry the last tear, talk for Max, write the date). | REF-RANGE |
| **The narrator's final choice costs him something he now knows the price of** (the twist taught him what it costs, and he chooses it anyway). A choice that costs a bruise makes the hope cheap (round 3: her first text was "fall on the ice"; "break your arm", his own old cost, would have earned it). | critic ruling (town: "Now, I'm the one who pays") |

### 3.4 Logic pass (before the draft is final)

Commenters find plot holes in the first hour. Answer these in the sheet header ("Logic questions": 3 questions + answers) and fix the script where an answer is missing:
1. The 3 "why doesn't X just…?" questions a commenter will post. Each is answered in a line or a clue.
2. Where is every main character in every scene? Someone alive and close who should obviously be there is a hole (E02: Grandma was alive, so why did Grandpa practise alone for 41 years?).
3. Does the rule's cost hold for every background character? (If cracks close, did nobody else ever see one close?)
4. If the rule object's size or strength varies, the script states the rule for it ("Big lies, big cracks.").
5. Does the time scale work? (41 years of practice vs one week with the kid.)
6. Is the false belief framed as a belief, never as the narrator's fact (§3.3)?
7. Is the rule visible all day? Then how is the secret kept in daylight? (Round 2: the want-shadows showed at lunch, so Grandma's and Voss's would too.) State a limit ("It only shows at night.") or a reason they hide.
8. Does the twist use the same rule grammar as act 1's examples? If act-1 shadows *show* the wanted thing, the twist shadow can't suddenly *reach* toward a person.
9. Does every character know every name and fact he says? (A man who "never talked to anybody" can't greet Grandma by name unless the script shows how he knows it.)
10. Does the world already know how the rule works? If the twist shows a hidden way it works, why doesn't everyone know? Name the belief the world uses instead (usually your misread) and say it once in act 1, attributed ("Grown-ups say some kids are just bad luck to stand next to.").
For a story with windows, walls or a street, draw a top-down diagram (who is where, where the light is) before the shot list: left and right flip between inside and outside.

---

## 4. Twist families and the rotation log

| # | family | what it is | ref / example | status |
|---|---|---|---|---|
| 1 | Hidden sacrifice | the misjudged person was secretly paying for someone | bell, memories, town, dog (4/6) | **capped**: max 1 in any 5 episodes; never for a sick or dying relative; never the default |
| 2 | Narrator was the cause | the mystery or the harm traces back to the narrator | gold-1 (the footprints were his own) | open |
| 3 | Role flip | the narrator's special status had a different purpose | monster ("I was the door") | open, never the default |
| 4 | Rule misread | the rule works differently than everyone believed (direction, target, meaning, timing) | (none in refs) | open |
| 5 | The rule was a lie | an authority faked the rule or its stakes | train | open; never a film premise copy |
| 6 | Outsider was right | the mocked person's claim was true all along | gold-2 (Theo "already met his") | open |
| 7 | Rule turned into reward | the cost of the rule becomes the gift | bell's ring, dog's frame (as endings) | open as a main twist |
| 8 | Cost lands on narrator | the narrator chooses or is forced to pay the price | town ending (he pays now) | open |
| 9 | Time reveal | when it happened, or when it is being told, is not what we assumed | gold-2 ending (2045) | open |
| 10 | Wrong target | the sign, gift or threat was meant for someone else | (none in refs) | open |
| 11 | Mirror | the narrator turns out to be what he mocked | (none in refs) | open |

**Overlapping families: one tie-break.** Classify by the new fact the twist line states. A twist that fits two families logs both (`3 + 10`), and **neither may match a family in the rotation window** (`script_check.py --log` checks primary and secondary). Fixed calls:

| if the twist line says… | it is | also log |
|---|---|---|
| the sign, gift or threat was for someone else ("it was meant for her") | **10** always | the other fit, e.g. 3 |
| someone secretly paid for someone | **1** | 8 if the narrator takes the cost over |
| the narrator's own special status had another purpose | **3** | 10 if that purpose was another person's sign |
| the narrator caused it | **2** | 11 if he turns out to be what he mocked |
| the rule works differently than everyone believed | **4** | the family of what the new working reveals |
| an authority faked it | **5** | |

Two families that share a mechanism count as the same family for rotation (round 3: "my bad things were really my sister's", labelled 3, is 3 + 10, and ep3 was 10). The reveal move (`reveal` in `tools/skeletons.txt`: whose-sign, what-i-was, i-caused-it …) is a core log field too: never the same as the last episode.

**Rotation log (POLICY).** YouTube's YPP policy does not monetize "templated storylines" or "**videos where characters are put in the same situation over and over again with the same outcome**" (verified on the live YPP policy page by the original critic pass). The refs' 4/6 hidden-sacrifice twist matches that line almost word for word.

Log every episode in the rotation log (`templates/rotation-log.md`). **7 core fields are mandatory**: twist family (primary + secondary), twist subject (who → whom, e.g. grandparent → partner), emotional outcome (reunion, romance, friendship, sacrifice revealed, protection, loss, dread, freedom, exposure), tone, reveal % (twist line), music-event-1 type and reveal move, all in the controlled words of `tools/skeletons.txt`. Before picking a twist, read the last rows (`script_check.py --log` does it):
1. The twist family is not in the last 5 episodes. Hidden sacrifice at most once in any 5; never for a sick or dying relative; no dead or dying mom (3/6 refs).
2. **The emotional outcome and the subject pair are not in the last 3 episodes** (round 2 repeated ep2's "old man's love for Grandma": the "same situation… same outcome" YPP warns about).
3. The reveal % differs from the last episode by ≥10 points; the misread source and the ending payoff type differ from the last episode; the rule type is not the same 3 episodes in a row.
A missing core field is back-filled from that episode's plan files or asked from the user, never assumed free. Optional fields that are missing are free: choose, and log them now.

---

## 5. Motif and callbacks

| rule | tag |
|---|---|
| One motif (a sound word, an object or a 1-3 word phrase) used ≥3 times, with the last use in the final 10 % or in the final line. | REF-RANGE (only town: "Clink" ×14, last at 157.2 of 157.7 s; others peak at 78-82 %) |
| The motif changes meaning at least once (town: greed → love → his own tear). | REF-RANGE (town) |
| ≥3 setup → payoff callbacks; the final line pays off a line from the first 20 %. | REF-RANGE (5/6) |
| If the motif is a sound, play a real SFX on its last use. | HYPOTHESIS (town's last "Clink." had none, `audio.md`) |
| ≥3 concrete specifics per 100 s: numbers, room numbers, prices, times, named objects. Prefer digits that can be shown. | REF-RANGE (town 18 numbers, monster 26, bell 1 number but many objects) |

---

## 6. Sentence rules

| measure | target | refs | tag |
|---|---|---|---|
| Mean words per sentence (spoken words) | 6-8 (aim ~7) | pooled 7.5 (5.9-8.7) | REF-RANGE |
| Sentences ≤6 words | 45-65 % (aim ~50) | pooled 48 % (31.8-64.7; 5/6 ≥45) | REF-RANGE |
| Sentences ≤3 words | 15-25 % | pooled 18 % | REF-RANGE |
| Longest sentence | ≤20 words | 14-23 | REF-RANGE |
| Verbless fragments | 12-25 %, and every fragment adds a new fact (number, name, object, sound, place) | bell 23.5 %, town 25.8 %, dog 17.5 %, monster 13 % | REF-RANGE + critic ruling |
| Emphasis-only fragments ("Forever." "Not once." "Never again.") | 0, unless it is a rule fact | slop vector (critic §5.4) | REF + POLICY |
| Starts with And / But / So / Then | ≤20 % of sentences, never 3 in a row | train 31.8 % (flagged) | REF-RANGE |
| Same subject opening ("He... He... He...") | never 3 in a row | humanizer rule | HYPOTHESIS |
| Tense | past by default. The rule and "now" status lines may be present. A fully present story is allowed. Never switch mid-story. | 5/6 past; memories' one slip flagged | REF-RANGE |
| Delivery speed | **200-240 wpm** (time scripts at 220); never >250. ≤80 s stories may read at 160-200 | 161-270; 270 masks under the bed | REF-RANGE (critic ruling) |
| Sentence gap | 0.15-0.30 s by default (already inside the 220 wpm average) | town/dog p50 0.17 s | REF-RANGE |
| **Designed pauses (the one pause rule; audio, pacing, checklist and upgrades point here)** | **2-3 per video, each 0.6-1.3 s; no other gap ≥0.5 s.** **A** (required): 0.8-1.3 s right after the twist line, or the line where the rule breaks. **B** (required): 0.6-1.0 s right before the last line. **C** (optional): 0.6-1.3 s next to the climax line. Each is its own sheet row | bell 1.29 s and memories 0.88 s after the rule breaks; no ref gives the last line more than 0.38 s | A: REF-RANGE (n=2); B, C: HYPOTHESIS |
| Slow reads | 1-3 word punch lines at about 0.6x, read inside the main take with 0.2-0.4 s of silence around them; only the last line (about 0.85x) is its own take (`audio.md` §1.3). Mark them at the end of the line cell: `Pizza day. (0.6x)`; the tools stretch the row | refs' slowest lines are 1-3 word punches | HYPOTHESIS |
| Numbers | write digits (captions show "6"), but count them as spoken words for timing ("2045" = twenty forty-five = 3 words) | memories, monster captions | REF-RANGE |

---

## 7. Dialogue

| rule | number | tag |
|---|---|---|
| Share of words | 3-20 % including narrated quotes (pooled 11.3 %; narration carries 77-97 %); don't pad lines to reach a number | REF-RANGE |
| Line length | ≤10 words per line | REF-RANGE (town ≤7) |
| Run length | no character speaks >3 sentences in a row | REF-RANGE (Ollie's 9-sentence dump, flagged) |
| Who speaks | the narrator carries ≥80 % of words; 2-4 other speakers per episode | REF-RANGE (narration 77-97 %) |
| Voices | at most 3 voices besides the narrator's clone. A speaker without a voice is a narrated quote: the narrator says the line (in "quotes", tag NARR) and a speech bubble shows it on screen (bell does this 4 times) | HYPOTHESIS (casting and listening work per voice) |
| Job of a line | a line either plants a clue, shows a flaw, or lands a callback. Never exposition ("He tells me the truth", "Hey, stop right there!") | REF-RANGE (flagged in train, memories) |
| The reveal | a side character may give the reason in ≤10 words after the narrator finds the truth, never the truth itself | REF-RANGE (dog, memories, train are told) |

**Marking lines for voice casting** (the sheet's `speaker` column):

| tag | meaning | voice |
|---|---|---|
| `NARR` | narration | your ElevenLabs voice (or a free text-to-speech voice) |
| `NARR` with "quotes" | the narrator speaking inside the story | same clone, shorter and drier take |
| `NAME` (DAD, THEO, OFFICER) | a character | listed in the cast line at the top of the sheet with its voice |
| `KID` / `NAME (kid)` | child or animal | designed voice, or the clone pitched up ≤+10 semitones (refs used +8 to +16; above +10 reads as chipmunk) |
| menacing adult | | −4 to −6 semitones or a designed voice |
| parent | | ±3 semitones or a designed voice (refs: parents at narrator pitch, timbre match >0.92) |
| `SIGN` / `TEXT` | read-out text on screen | narrator voice, or on screen only |

Yells sit +3 to +5 LU above the narration short-term (`audio.md`).

---

## 8. Endings

| rule | tag |
|---|---|
| The last line starts at ≥92 % and the speech ends ≤1.5 s before the video ends; hold a 0.5-1.5 s tail on the last word. | REF-RANGE (5/6 no outro) |
| One extra payoff inside the last 15 % after the reveal: a reversal, the rule turned into a reward, or a time jump. | REF-RANGE (5/6 at ≥85 %) |
| Final 3 lines: **[a concrete consequence] → [an image or a short quote] → [the callback or motif line, ≤12 words]**. | REF-RANGE (bell, town, dog) |
| The last line types, rotate them: callback image (dog's frame), sound callback (town's clink), rule-object state change (bell's "My bell."), dark open line (monster), small action with the motif (gold-2). | REF-RANGE + rotation |
| The final shot is ≥3 s and shows the rule object's final state. Mirror the hook shot at most every other episode. | critic ruling |
| Never end on a stated moral, an explanation of the twist, or "finally free". | REF-RANGE (0/6 end on a moral; memories' explaining end, flagged) |
| When the final shot shows the rule object's final state, the last line never names the mechanism (true, lie, heal, close, gone) or restates what the shot shows. End on an image, a sound, an action or a ≤4-word callback. `script_check.py` flags mechanism words in the last line. | critic ruling |

---

## 9. Banned list and self-check

### 9.1 Banned phrases (ban outright)

- "for the first time" in any form (7 uses in 5/6 refs), including "first … ever" ("her first text ever"; `tools/patterns.txt` [banned-regex] catches the forms), "I finally understood", "I finally knew", "That's when I finally understood", "for the first time, I understood"
- "little did I know", "in a world where", "Everyone thought"
- "Suddenly", "what I saw next...", "what I see next makes me furious", "that's when I noticed something strange", "He told me the truth"
- "my heart sank / shattered", "tears streamed down my face", "a wave of...", "time stood still", "the silence was deafening", "I couldn't believe my eyes", "in that moment", "It was then that", "every fiber of my being", "I will never forget", "forever changed"
- "an unbreakable bond", "a bittersweet reminder", "a testament to", "tapestry", "the weight of [abstract]", "journey", "symphony", "resonate"
- "Have you ever wondered", "Let me tell you", "Here's the thing", "See," as an opener
- "we're finally free", "and they lived happily"
- abstract long adjectives: enormous, entire, actual, incredible, unimaginable, overwhelming, devastating, palpable, unwavering

### 9.2 Banned or capped structures

- "It wasn't X. It was Y." max 1 per script, and only where the viewer actually believed X (monster's "I wasn't special. I was the door." works because it is the only one). To use it, quote the line that planted X with its time in the sheet header ("Staged contrast") and check that nothing between them contradicts X; otherwise cut it.
- A reason line that is an aphorism ("Lies close up when you make them true."). A side character gives a concrete fact instead.
- Rhetorical questions to the viewer: max 1 (bell, town, dog, monster use 0).
- Rhetorical triplets and list-of-three rhythm ("cold, dark and lonely"; "In math, at lunch, in the bathroom" is a real list of places, fine once).
- Emphasis-only fragments, rows of fragments that add no fact.
- A moral as the last line (HARD in checklist.md). Explaining the twist after the viewer got it.
- Named feelings instead of actions. Adverb + said ("said quietly", "whispered softly").
- Em dashes, semicolons, ellipses inside the narration (captions read them badly).
- A mid-story tense switch.
- A twist told by a side character's speech (HARD in checklist.md). The rest of §9.2 costs a point, not the area.
- The secret-sacrifice-for-a-dying-relative twist as a default; a dead or dying mom as the hook of the pain.

### 9.3 Self-check (all 16 must pass before the user sees the script)

Run `python tools/script_check.py script-sheet.md --last-reveal <last episode's reveal %>`. It computes items 2, 3, 5, 8-13, the voice tests (§0.1), the mechanism and last-line tests and the caption-highlight share from the sheet (banned phrases are read from §9.1 above); lines marked CHECK and items 1, 4, 6, 7, 14, 15 are yours.

1. Rule rubric ≥9/12 with tests 1 and 2 at 2 and test 6 ≥1. Score written at the top of the sheet.
2. Line 1 = title rule, 8-15 words, starts "In this world," or "In this town,".
3. Stake line (me / my / mine) starts by 6 s; rule fully clear by ≤9 %.
4. Twist family is not in the last 5 log rows, and is not secret sacrifice for a sick or dying relative.
5. Reveal % is 49-78 and ≥10 points from the last episode; misread 10-36 %; climax 69-96 %; last line ≥92 %.
6. ≥2 planted clues before the reveal, ≥1 hidden in a joke, and the narrator finds the truth through an object or action.
7. Motif used ≥3 times, last use in the final 10 %; final line pays off a line from the first 20 %.
8. ≥3 concrete specifics per 100 s (count them).
9. Sentence stats: mean 6-8 words, 45-65 % ≤6 words, 15-25 % ≤3 words, no sentence >20 words, every fragment adds a fact, ≤20 % And/But/So/Then starts.
10. Dialogue 5-20 % of words, every line ≤10 words, no run >3 sentences, every speaker tagged for casting.
11. Zero hits from §9.1 and §9.2 (search the text for each phrase), no em dashes, past tense held.
12. Read aloud at 220 wpm: runtime is the target ±5 %, the designed pauses follow §6 (A and B present), and the voice tests of §0.1 pass (if a line sounds like a narrator or a movie trailer, rewrite it).
13. No copying (§9.4): 0 copy-shape hits, 0 five-word overlaps with the refs or golds, and the skeleton shares ≤4 of 10 slots with every gold and ref.
14. Logic pass (§3.4) answered in the header.
15. Twist: 2-4 clues, ≤2 direct, no line before the reveal states the mechanism, and the blind guess test says "not guessed" (or UNCHECKED until The user reads it; §3.3).
16. Tone: the brief's tone holds past the reveal (§0.2), or the shift is planned in the header.

### 9.4 No-copy list (copy the method, never a line shape)

Never reuse a line shape, act-1 example frame, callback or ending frame from the golds or the refs. The canonical list is `tools/patterns.txt` [copy-shapes]: "[Neighbour] told his wife [lie]", "this time" endings, "I lied." climaxes, "the [poorest/biggest] X in town", "stopped laughing" / "nobody laughed", the walk-ahead → walk-beside callback, "walked me home", the numbers 41 and 2045, a cookie broken in half, dates turning gold. `script_check.py` also flags any 5-word run (3+ content words) shared with the refs' scripts (`tools/ref_lines.txt`) or the gold sheets. **After each published episode, add its own key shapes to patterns.txt**, so the channel doesn't repeat itself either.

**Skeleton and signature check.** Line shapes are not enough: round 2 copied gold-1's whole skeleton with new nouns (a sign at the window every night → fear of an intruder who "wants in" → a defensive prop → a "wants you" joke → outside at night, the whole trail → love for someone else → a night knock, the man already waiting → a family meal). Write your skeleton in the sheet header **before you open `examples/`**: `Skeleton | family=…; sign=…; belief=…; reaction=…; discovery=…; subject=…; outcome=…; climax=…; ending=…; lastline=…` with the values listed in `tools/skeletons.txt`. The 12 slots now include `reveal` (the question the twist answers) and `signature`: a ref's trademark story move (bell's sign that never worked and finally fires, town's hidden cost paid in secret, monster's "I was the cause", the secret sacrifice for a sick relative). `script_check.py` fails a skeleton that shares 5 or more slots with any gold or ref (HYPOTHESIS threshold; the round-2 copy shared 6 with gold-1), **or whose signature is any ref's or gold's**: round 3 avoided every listed string and still rebuilt bell's payoff ("her phone never buzzed, not once since her birthday" → "that night, her phone buzzed"). A new episode's signature is `none`. Log each episode's skeleton in the rotation log's `skeleton` column: `--log` then checks the channel against itself.

---

## 10. Workflow for a new episode

1. **Rule.** Write 5 candidate rules with the formula (§1.1). Score each with the rubric (§1.2). Keep the best that passes. Write the comment-bait question for it.
2. **Log check.** Read the last 5 rows of the rotation log (`templates/rotation-log.md`). Note every value you can't use this episode.
3. **Twist.** Pick an allowed family (§4). Write the twist line first (≤8 words, an object or an action the narrator sees). Write the 2-4 clues that make it fair (≤2 direct) and the joke that hides one of them without naming the mechanism. Then the logic pass (§3.4).
4. **Beat map + skeleton.** Pick the target runtime (60-180 s) and the reveal % (§3.2) so the reveal shifts ≥10 points from the last episode. Work out the beat seconds and the word budget, and write the 10-slot skeleton (§9.4) and the tone (§0.2) into the header.
5. **Motif.** Pick one motif that can change meaning, place its 3+ uses, and put the last use in the final line.
6. **Draft.** Write line by line into `templates/script-sheet.md`, one sentence per row (two very short sentences may share a row). A row is a timing unit, not a shot: most rows start a cut (57-78 % of ref cuts land on a sentence start), but the shot list splits 10+-word rows and may merge ≤4-word rows (`pacing.md` rule 5). Write the ending's final 3 lines (§8) before act 2.
6b. **Now, and only now, open `examples/`.** Compare quality (clue tables, beat tables, register). Never take a line, a beat order or an ending from a gold; if one comes back to you, change it.
7. **Humanize.** Run the `humanizer` skill on the narration. **No humanizer skill:** do the pass by hand, line by line: (1) staged contrasts out ("It wasn't X. It was Y." beyond §9.2's one); (2) triplets and list-of-three rhythm out; (3) trailer fragments ("6 weeks in a cast.") into kid sentences ("I was in a cast for like 6 weeks."); (4) evidence-arranging lines ("Both times, Lulu was right there.") into talk; (5) no 3 sentences opening the same way; (6) written words out ("own", "in it", "theirs", dashes, semicolons). Then put it in the user's register (§0.1: casual markers, contractions, no narrator tone) and run `script_check.py`.
8. **Timing check.** `python tools/plan_timing.py script-sheet.md --rewrite-times` fills the time column (spoken words / 3.67 / rate, pause rows, first word at 0.1 s, 1.2 s tail) and writes a planned `words_planned.json` + `cuts.txt` for the shot-list and pacing checks. Check every beat against §3. Then read it aloud once with a stopwatch; if the stopwatch is >5 % off, fix the script, not the speed.
9. **Fill the sheet.** Shot, camera, lighting preset, music cue, SFX and caption highlight for every row (`templates/script-sheet.md`).
10. **Self-check.** Run §9.3 (`tools/script_check.py --log … --pretwist …`) and the blind guess test. Draft the rotation-log row. Write 3 titles (formats A, B, C) and 3 cover texts. Hand to the user.

---

## 11. Vietnamese narration (`--lang vi`)

Every rule above holds for a Vietnamese narrator except the English-only numbers below. `tools/script_check.py` switches to these targets automatically when the sheet is written in Vietnamese (or with `--lang vi`). Tag: **HYPOTHESIS** until Vietnamese episodes have their own retention data in `history-registry.json → performance_log`.

### 11.1 Timing
- Vietnamese is timed in **syllables**, not words: **~3.2 syllables/s** while reading (170–210 syllables/min for the speech, pauses excluded). `script_check.py` uses 3.2 syllables/s unless `--wpm` is given; pass `--wpm 192` to `plan_timing.py` for Vietnamese sheets.
- Runtime budget: `60 s ≈ 180` syllables · `90 s ≈ 270` · `120 s ≈ 360` · `150 s ≈ 450`.
- The same pause rule (§6): 2–3 designed pauses of 0.6–1.3 s, one right after the twist line, one right before the last line.

### 11.2 Sentences
- Mean **8–12 syllables** per sentence; **35–60 %** of sentences `≤ 8` syllables; **10–25 %** `≤ 4` syllables; never more than **25** syllables.
- Every short fragment adds a fact (a number, a name, an object, a sound, a place).
- Fewer than 20 % of sentences start with `Và / Nhưng / Rồi / Thế là / Vậy là`, never 3 in a row.

### 11.3 Voice
- **One narrator, first person**, telling a friend. Pick the pronoun from the narrator's age and keep it: a child says `mình` / `tớ` (or `tao` for a cheeky kid), an adult says `tôi`; family terms for the others (`bà ngoại`, `ba`, `mẹ`, `anh Hai`).
- Spoken, not written: short clauses, natural particles where they fit (`á`, `nè`, `nha`, `luôn`, `thôi`), one casual marker every ~15 s (`kiểu`, `thật ra`, `nói chung`, `ờ`). Never two in one sentence, never the same one 4 times.
- Everyday words: abstract Sino-Vietnamese or literary words (`tuyệt vọng`, `định mệnh`, `vĩnh viễn`, `linh hồn`, `bi thương`, `thấu hiểu`, `vô tận`) only when the character would really say them.
- Feelings shown through actions (`Mẹ cầm cái muỗng mà không ăn.`), never named (`Mẹ buồn lắm.`).
- Kinship address changes are plot events: the narrator switching `ba` ➔ `ông ấy` marks a rupture (`engine/references/2b-character-lines.md` §5).

### 11.4 Banned Vietnamese phrases (`script_check.py --lang vi` reads this list)
- "lần đầu tiên trong đời", "chưa bao giờ trong đời", "bỗng nhiên", "đột nhiên", "không ngờ rằng"
- "tim tôi như thắt lại", "nước mắt lăn dài", "thời gian như ngừng trôi", "im lặng đến đáng sợ", "tôi không tin vào mắt mình"
- "một sợi dây vô hình", "hành trình", "bản giao hưởng", "minh chứng cho", "kỷ niệm khó quên"
- "và đó là lúc tôi hiểu ra", "tôi đã học được rằng", "cuối cùng tôi cũng hiểu", "bài học"
- "các bạn có bao giờ tự hỏi", "để tôi kể cho bạn nghe", "các bạn biết không"
- "mãi mãi hạnh phúc", "và họ sống hạnh phúc"

### 11.5 Self-check
Run `python tools/script_check.py script-sheet.md --lang vi` (`--mode story` unless it is a world-rule storytime). The English-only tests (Flesch-Kincaid, contractions, similes regex, adverb + said) are replaced by the syllable, Sino-Vietnamese and simile checks above; everything else (beats, twist, pauses, no-copy, rotation) is unchanged.

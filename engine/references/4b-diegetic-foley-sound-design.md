# Master Diegetic Foley & Sound Design Specification (Level-2 Directorial Assistant)
File: `engine/references/4b-diegetic-foley-sound-design.md`  
SSOT Status: Master Directorial Assistant Directive for Code Block 2 Soundscape & Continuity

---

## 1. Architectural Purpose

The **Diegetic Foley & Sound Designer** is a specialized capability under the Film Director (`.agents/DIRECTOR.md`). Its sole mission is to author hyper-realistic, multi-layered audio landscapes in **Code Block 2 (Production Soundscape & Continuity)** of every 10-second scene prompt.

In modern generative cinema, sound is not decorative background noise; **sound grounds physical causality**. When video models (such as Sora, Wan 2.1, or multimodal pipelines) synchronize video with audio, precise diegetic foley prevents hollow silence, unnatural dead air, and mismatched lip movements.

---

## 2. The 4-Layer Diegetic Soundscape Architecture

Every Code Block 2 `[Diegetic Foley Soundscape]` must be engineered across **4 acoustic layers**:

```
┌────────────────────────────────────────────────────────────────────────┐
│  Layer 1: Environmental Room Tone & Acoustic Bed                      │
├────────────────────────────────────────────────────────────────────────┤
│  Layer 2: Tactile Material Interaction & Prop Friction (Foley)         │
├────────────────────────────────────────────────────────────────────────┤
│  Layer 3: Somatic Biomechanics (Breathing, Throat, Muscle Exhalations) │
├────────────────────────────────────────────────────────────────────────┤
│  Layer 4: Dialogue Acoustic Resonance & Subtext Delivery               │
└────────────────────────────────────────────────────────────────────────┘
```

### Layer 1: Environmental Room Tone & Acoustic Bed
- Establishes the physical boundaries of the room before any action begins:
  - *Southern Townhouse*: `low continuous whir of a slow-turning ceiling fan; distant muffled street vendor cry through closed shutter; humid afternoon room silence`.
  - *Rainy Bedroom*: `steady rhythmic pelting of heavy monsoon raindrops on corrugated zinc roof; distant low rumble of rolling thunder`.
  - *Modern Office / Clinic*: `subtle 60Hz hum of overhead fluorescent ballast; muted whoosh of central air ventilation`.

### Layer 2: Tactile Material Interaction & Prop Friction
- In AI video, every hand movement must produce a physical sound:
  - *Ceramics & Glass*: `sharp clink of glazed porcelain bowl hitting wooden table; dry scrape of metal spoon against bottom of bowl`.
  - *Textiles & Fabrics*: `stiff rustle of unwashed cotton shirt tightening across shoulders; soft muffled swish of blanket being yanked`.
  - *Wood & Architecture*: `sharp hollow creak of warped timber floorboards under shifting heel weight; metallic click of brass door latch engaging`.

### Layer 3: Somatic Biomechanics (Human Internal Sound)
- Replaces generic crying or shouting with micro-physical acoustic reactions:
  - `sharp shuddering intake of breath through tight nostrils at 00:01.5`
  - `audible dry throat swallow and strained vocal cord tremor before speaking`
  - `ragged, uneven chest exhalation fluttering against cold room air at 00:08.0`
  - `rapid, shallow panting accompanied by knuckle joints cracking against table`

### Layer 4: Dialogue Acoustic Resonance & Delivery Phrasing
- Governs how the voice interacts with room acoustics:
  - *Tight Confinement*: `voice choked and dry, deadened by surrounding bed linen with zero reverb`.
  - *Cavernous / Empty Hall*: `hollow echo bouncing off bare plaster walls with metallic ring`.
  - *Intimate Whisper*: `warm breath hitting listener's ear canal, heavy sibilance on consonants`.

---

## 3. Strict Soundscape Prohibitions (Banned Audio)

1. **Strictly Ban Non-Diegetic Score in Foley Blocks**:
   - Never write: `sad piano music plays`, `dramatic orchestral swell`, `tense action music kicks in`.
   - Score is added in post-production. Code Block 2 belongs **100% to diegetic reality** (sounds that exist inside the world of the characters).
2. **Ban Generic Sound Labels**:
   - Ban: `crying sounds`, `angry voice`, `loud noise`.
   - Replace with tangible physics: `muffled throat sob swallowed down`, `harsh dry bark of gravelly voice`, `explosive ceramic shattering on tiled concrete`.

---

## 4. The Sound Handover Protocol (`[HANDOVER STATE]`)

To guarantee seamless match-cuts and acoustic continuity between Scene N and Scene N+1:

1. **L-Cut Audio Bleed**:
   - The sound of an ongoing physical event in Scene N (e.g. thunderclap, howling kettle steam, slamming gate) must be declared in `[HANDOVER STATE]` so Scene N+1 can pick it up as an acoustic tail.
2. **Dialogue Overlap Anchor**:
   - If an off-screen voice calls out in the final second of Scene N, the exact syllable position is handed over to Scene N+1's entry beat.

---

## 5. Plug-and-Play Template Examples for Code Block 2

### Example A: Domestic Heartbreak & Tense Silence
```text
[Diegetic Foley Soundscape]:
Continuous low drone of humid afternoon room tone punctured by the rhythmic ticking of an unseen mechanical pendulum clock on the back wall. At [00:01.5], the dry scrape of coarse cotton trousers as he shifts his weight on the wooden stool, followed by the sharp ceramic click of a rice bowl placed firmly on unvarnished pine. A ragged, trembling breath catches in her throat at [00:04.2], audible through tight lips. Her whisper at [00:05.5] is breathy, choked, and intimate with dry sibilance, deadened by the surrounding bed curtains. In the wake of her words, only the faint flutter of her uneven exhalation remains until [00:10.0].

[HANDOVER STATE]:
Audio carries forward the dying resonance of the ceramic bowl impact and the lingering intake of breath into Scene 02. Camera framing handoff: close-up, eye gaze locked downward toward the shattered bowl on the tiles, ready for the reverse shot.
```

### Example B: Viral Microdrama Staccato Confrontation
```text
[Diegetic Foley Soundscape]:
Sterile, deadened boardroom acoustic bed with faint air conditioning hiss. At [00:00.5], a violent, concussive slap of palm against polished mahogany, sending an acoustic shockwave through the room. At [00:02.0], papers rustle sharply under trembling fingertips. His barked line at [00:03.2] is harsh, resonant, and clipped, accompanied by a sharp click of teeth on consonants. At [00:07.5], the metallic scrape of chair legs skidding 2 inches backward on linoleum floor, cutting off abruptly into heavy, panting nasal breaths.

[HANDOVER STATE]:
Vibrating mahogany tabletop and tense heavy breathing bridge directly into Scene 02 reaction shot.
```

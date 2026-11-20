# Sven Cinematic Universe — Action, Martial Arts, Chase & Supernatural Combat Genre Engine
File: `engine/genres/action.md`
SSOT Status: Authoritative Standard for High-Stakes Action-Drama, Martial Arts, Tactical Chases & Supernatural Combat
Governed by: Screenwriter (Level 2), Director (Level 2) & Combat Director (`@CombatDirector` — `.agents/skills/combat-director/SKILL.md`) under Showrunner (Level 1)

---

## Genre Card (README §2b)

| Field | Value |
|---|---|
| **Regime** | 1 (grounded action only when the story is real-world) · 3 (supernatural) · 4 (martial / crime) |
| **Genre Engine** | 3 — Gauntlet & Breakthrough |
| **Audience payoff** | Kinetic adrenaline + tactical victory earned by character |
| **Default episode shape** | 0c §4 Archetypes; `60:40` `10s:15s`; 3-Zone `40% drama : 40% action : 20% fallout` |
| **Preferred hooks** | #2 In Medias Res, #4 Suspended Kinetic Moment, #9 Consequence First |
| **Preferred cliffhangers** | C2 Threshold Ambush, C6 Suspended Strike, C3 Betrayal |
| **Favoured twists & budget** | TW-05 Identity, TW-12 Reversal, TW-09 Reverse Rescue; 1 major + 1–2 minor |
| **Dialogue : visual** | `40 : 60` dialogue : visual |
| **Default `ending_mode` / `fatality_policy`** | positive / none (knockout or disarmament, never on-screen death) |
| **Signature bans** | fights without psychological compression; fights that change nothing; Regime-1 professionals forced into combat |
| **Scorecard criteria that must score 2** | Hook, Rhythm, Active character |

Numbers defer to `engine/references/0c-canonical-numbers.md`; pacing tables below are default sketches.

---

## 0. Core Principles & Dramatic Philosophy

The objective of the **Action, Martial Arts, Chase & Supernatural Combat Genre Engine** is to architect high-adrenaline, emotionally grounded action cinema (short films, 10-scene episodic series, Wuxia/Xianxia vertical dramas, urban martial arts thrillers, and supernatural awakened-bloodline series).

In the Sven Cinematic Universe, **action is never hollow physical gymnastics**. A fight or chase only erupts when emotional compression, moral injustice, or ticking-clock stakes reach an unbearable boiling point where words can no longer resolve the conflict (*When dialogue is exhausted, physics takes over*).

### 0.1 The Action-Drama Equation
$$\text{Cinematic Action-Drama} = \text{Suppressed Emotional Compression (1.0x Setup)} + \text{High-Velocity Kinetic Chase/Combat (2.3x–10x Climax)} + \text{Earned Moral Resolution (1.0x Aftermath)}$$

1. **The Restraint-to-Detonation Law (Nén Tâm Lý Trước Khi Nổ Vật Lý)**:
   - The audience must ache for the protagonist to fight back before the first punch is thrown. Early scenes establish a powerful restraint (an oath of non-violence, a hostage/loved one at risk, a sealed bloodline, or a desire for peace) that the antagonist ruthlessly tramples until the moral red line is crossed.
2. **Dual-Speed Temporal Orchestration (`@Director` Static-Camera Dialogue vs. `@CombatDirector` First-Principles Kinetic Physics & Flexible Shot Topology)**:
   - Dramatic setup and aftermath scenes operate at natural human conversational tempo (`1–4 Shots` per `10.0s / 15.0s` clip with `static camera` per `Law D1`) governed by `@Screenwriter` and `@Director`.
   - Chase, combat, vehicle drift, split-second rescue, sports climax, and high-velocity craft scenes switch immediately to `@CombatDirector` (`combat-director/SKILL.md`), which **never forces a fixed shot count onto every scene**, instead choosing the **Shot Topology** organically from scene intent (**`Topology 1`: `1–2 Shot` Unbroken 3A Inertial Long-Take**; **`Topology 2`: `3–5 Shot` Asymmetric Dynamic Exchange**; or **`Topology 3`: `6–9 Shot` Staccato Rapid-Cut Blitz**) and driving velocity through the **4 Core Kinetic Physics Levers**:
     1. **Surface-Bound Material & VFX Physics (`死死贴附`)**: Anchoring elemental auras/slash streaks, real-world fire/smoke/sparks/water, or pure tactile deformation directly to host surfaces rather than floating overlays.
     2. **Camera Inertia & Relative Velocity**: Pairing `AAA action-game inertial whip-follow camera work` with sharp impact recoil so speed is felt even inside a single unbroken take.
     3. **Directional Motion Blur & Trajectory Release**: Allowing `strong directional motion blur` on fast extremities/weapons to eradicate sluggish AI slow-motion.
     4. **Time-Ramp Modulation & Hit-Stop Weight (`变速卡点`)**: Contrasting rapid acceleration (`blistering whip-fast speed`) with crisp impact compression (`explosive real-time speed` hit-stop snaps) and selective suspension only when dramatically earned.
3. **100% Filter-Safe Physical Brutality & Adult-Only Combat Ethics**:
   - Upholds Sven's **Zero-Fatality, Zero-Gore & Minor Protection Mandate**: Combat and chases involve adult characters only (minors are strictly protected and never placed in violence or danger per Pillar 4 §[10d]).
   - Brutality is communicated 100% through **velocity, biomechanical momentum transfer, somatic pain reactions, and visible environmental destruction** (cracking timber tables, shattering tempered glass, bending iron railings, splintering tree bark, exploding water splashes)—strictly zero blood splatters, zero gore, and zero executions.
4. **The Adaptive Triad Law (`[context]` Terrain $\leftrightarrow$ `[subject]` Innate Skills $\leftrightarrow$ `Action` Synthesis — Zero Mechanical Copy-Pasting)**:
   - Never copy external combat templates blindly (strictly purge raw metric numbers like `20m/70m/20cm`, hardware jargon like `35mm/8K`, and Mode B costume re-descriptions).
   - Every action scene is governed by the **Adaptive Triad**:
     1. **`[context]:` (Tactical Terrain & Spatial Layout)**: Maps the exact 3D spatial relationships between landmarks, obstacles, vertical tiers, and chokepoints so character positions are physically grounded.
     2. **`[subject]:` (Spatial Placement + Innate Character Skills)**: Anchors each character to a landmark from `[context]:` and declares their **Innate Skills / Signature Combat DNA** (from `setting.html` Section 1—e.g., evasive momentum redirection, pinpoint joint-locks, parkour agility, brute-force cleaving, or specific supernatural power).
     3. **`Action Timeline` (Skill $\times$ Terrain $\times$ Story Stake)**: Every timeline beat must show the character actively applying their **declared innate skill** onto the **specific terrain** in `[context]:` to solve the dramatic conflict—never generic, interchangeable fighting.

---

## 1. Official Nomenclature & System Taxonomy

| Level | Designation | Description |
|---|---|---|
| **System Module ID** | `action` | Activated in `AGENT.md`, `workflow.md`, `engine/runbooks.json`, and project configs. |
| **English Formal Label** | **High-Stakes Action, Martial Arts, Chase & Supernatural Combat** | Master designation for martial arts, urban action, Wuxia/Xianxia, and chase thrillers. |
| **Vietnamese Industry Term** | **Phim Hành Động, Võ Thuật, Truy Đuổi & Dị Năng Kịch Tính** | Dòng phim hành động võ thuật, truy đuổi tốc độ cao và đối kháng siêu nhiên gắn kết cốt truyện. |
| **Specialist Skill Engine** | [`combat-director/SKILL.md`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md) | Invoked automatically for all chase, parkour, 1v1 duel, 1vMany brawl, and supernatural combat scenes. |

---

## 2. The 5 Sovereign Pillars of the Action & Chase Engine

### Pillar 1: The 3-Zone Hybrid Episode Architecture (40% Drama – 40% Action/Chase – 20% Aftermath)
An action-drama episode (`100s–120s` across 10–12 scenes) weaves dramatic acting and kinetic action into three distinct zones:

```text
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ ZONE 1: THE EMOTIONAL PRESSURE COOKER (Scenes 01–04 · 40% · Speed: 1.0x · @Director)     │
│ • Scene 01 (Hook): Threat arrival / In Medias Res cornering.                             │
│ • Scene 02 (Setup): The Restraint Vow / Hostage / Sealed Power.                          │
│ • Scene 03 (Drama 1): Verbal sparring & humiliation; protagonist seeks peaceful exit.    │
│ • Scene 04 (Ignition Snap): Antagonist crosses red line → Protagonist catches wrist at   │
│   00:08.5 and delivers the razor-sharp Pre-Combat One-Liner.                             │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ ZONE 2: THE PURSUIT & COMBAT CLIMAX (Scenes 05–08 · 40% · Speed: 2.3x–10x · @Combat)     │
│ • Scene 05 (Wave 1): High-Speed Tactical Chase OR 1vN Guard Crowd Sweep.                 │
│ • Scene 06 (Wave 2): 1v1 Boss Seesaw Clash & Crisis Reversal (protagonist pushed back).  │
│ • Scene 07 (Awakening): 3s Somatic/Story Glance + Aura/Resolve Ignition → 7s Blitz.      │
│ • Scene 08 (Wave 3): All-Out Final Exchange, Structural Destruction & Decisive Finish.   │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ ZONE 3: AFTERMATH, CATHARSIS & CLIFFHANGER (Scenes 09–10 · 20% · Speed: 1.0x · @Director)│
│ • Scene 09 (Release): Heaving breath in wrecked arena; rescuing loved one / moral mercy. │
│ • Scene 10 (Echo / Cliffhanger): Restorative peace OR Cold-Water Mastermind Reveal.      │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

### Pillar 2: High-Velocity Chase, Vehicle Drift & Parkour Mechanics (Truy Đuổi, Đua Xe Drift & Vượt Địa Hình)
When a scene involves a chase (foot chase, urban parkour, vehicle drift, forest pursuit, or supernatural hunt), enforce three kinetic laws:
1. **Obstacle Pre-Planting & Tactile Interaction (Zero `→` Arrows)**: `[context]:` must inventory physical obstacles along the pursuit vector (market stalls, narrow alley crates, rooftop air ducts, wet asphalt corners, ancient tree trunks). Across sequential `1.5s–2.0s` rapid cuts (`Shot 1..N`), each shot depicts 1 clean obstacle interaction in a single punchy sentence (e.g., vaulting one-handed over a wooden crate in `Shot 2`, sliding beneath a low steel pipe in `Shot 3`, or drifting past an apex in `Shot 4` with white tire smoke and golden friction sparks tightly clinging to the spinning rear tire tread).
2. **Predator-Prey Distance Compression**: Express chase tension through closing spatial proximity along the Target Axis (`Wide inertial tracking follow shot targeting Elena as Dante closes from three paces behind to point-blank reach`).
3. **Inertial Whip-Camera & Surface-Adhered Slipstream Cues**: Combine surface-adhered wake physics (`cyan-white electric arcs and cold-white calligraphic slash streaks tightly clinging to garment hems and blade edge`) with **`AAA action-game inertial whip-follow camera work`** and **`strong directional motion blur`**.

### Pillar 3: The Momentum Seesaw, Flexible Shot Topology (1-Shot Inertial Take ↔ 3–5 Shot Dynamic Exchange ↔ Multi-Shot Rapid-Cut Blitz) & Time-Ramp Decision Matrix
Governed by `@CombatDirector` ([`SKILL.md`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md)):
- **Flexible Shot Topology Over Fixed Shot Counts (`Strictly Zero → Arrows`)**: Never chain 4–6 disconnected actions with `→` arrows, and never force every fight into a single fixed shot count! Choose the shot topology that serves the scene:
  * **Topology 1 (`1–2 Shots` — Unbroken 3A Inertial Long-Take)**: A continuous `8s–12s` dynamic camera trajectory (`AAA inertial chase camera whipping behind the launch, snapping into a split-second time-ramp impact pause on the blade lock, and orbiting the counter-flurry`) followed by a `2s–3s` composed settle.
  * **Topology 2 (`3–5 Shots` — Asymmetric Dynamic Exchange)**: Combining a sustained `4s–5s` tracking sprint/exchange with sharp impact cuts and a reversal/checkmate.
  * **Topology 3 (`6–9 Shots` — Staccato Multi-Shot Rapid-Cut Blitz)**: Used when fracturing a high-frequency multi-angle clash or multi-step craft montage into `1.5s–2.0s` cuts on peak action (`1 focused action per short cut` + `> 45°` angle jumps).
- **Zero Ground-Time & Terrain Rebounds**: Knocked-back fighters use pre-declared fixtures (stone parapets, iron pillars, wooden crates) to rebound or absorb impact on a dedicated `explosive real-time speed` shot.
- **Simultaneous Cross-Counters & Cross-Dashes**: Highlight equal power by directing both fighters to streak past each other or clash blades in an `explosive real-time speed` impact snap that detonates surface-adhered embers and lightning arcs.
- **The Time-Ramp Speed-Ramping Decision Matrix (Eradicating Unintentional Slow-Motion)**:
  - *Strictly Banned (`0% Unintentional Slow-Motion`)* during rapid punches, sword flurries, knife mincing, or sprinting shots (`blistering whip-fast speed` with `strong directional motion blur`).
  - *Selective Time-Ramp Apex (`1 Shot of 2.0s–2.5s` at `ultra-slow-motion suspension`, max 1 per `15.0s` clip)*: Placed strictly between a `blistering whip-fast speed` launch shot and a `blistering whip-fast speed` / `crisp real-time speed` follow-through shot at **1 Peak Visual Apex** (e.g., mid-air vault amidst suspended raindrops and crackling cyan electric arcs, mid-air flambé fire ribbons clinging to a rotating steak, a car mirror grazing concrete 2cm away with suspended sparks, or an aerial kick apex).
- **Advanced Aerial & Supernatural Surface-Adhered VFX Mechanics**:
  - *Surface-Adhered VFX Contrast (`死死贴附`)*: Always anchor contrasting elemental signatures directly onto each fighter's clothing/armor and blade (`silver-white moonlight luminescence, cyan-white electric arcs, and cold-white calligraphic dry-brush slash streaks tightly clinging and physically adhered to Lin's garment hems and sword blade` vs. `thick black-crimson miasma aura and dark-gold embers tightly coiled and physically adhered across Mei's armor plates and heavy saber blade`).

### Pillar 4: Combat-Sovereign `[subject]:` & `[prop]:` Protocol + Hand-Grip Biomechanics Lock
- **Double-Lock `fully_preserved` Reference, 4-Layer Gender/Hand Anatomy Lock & Zero-Costume/Zero-Age Law**: Every fighter is declared by a fixed **Proper Character Name** (`Kael`, `Vance`, `Lin`, `Mei`, `Elena`) with `<<<Image X>>> (fully_preserved - same female/male face, slender feminine / masculine body proportions...)` in Line 1 and `<Name>'s skin, hands (and makeup): fully_preserved - ...` in Line 2. Strictly zero clothing/garment words and zero age/hair/beard words in `[subject]:` or `Shot 1..N`.
- **Mandatory Combat & Surface-Adhered Physics Identity in `[subject]:`**: Every fighter's `[subject]:` line declares:
  1. Initial 3D architectural anchor & coiled stance at `00:00`
  2. Exact weapon/tool hand-grip state (or `(No objects should appear in the character's hands)` if unarmed)
  3. **Surface-Adhered VFX / Physical Matter Lock** (`tightly clinging and physically adhered to...`)
  4. Eyeline locked on the opponent + singularity seal (`— the only [Proper_Name] in frame`).
- **The 5 Biomechanical Hand-Grip Laws (Eradicating Weapon & Prop Glitches)**:
  1. **Single-Handed vs. Two-Handed Hilt Classification**:
     - *1-Handed Weapons/Tools (`Straight Sword, Saber, Dagger, Chef Knife, Baton`)*: Lock to ONE specific hand (`gripped in her slender right hand` / `his strong right hand`) and explicitly declare the other hand empty (`while her/his left hand remains empty`). Never put two hands on a short hilt.
     - *2-Handed Weapons (`Heavy Greatsword, Two-Handed Katana, Spear, Staff`)*: Explicitly space both hands along the handle (`right hand below crossguard, left hand anchored at pommel` or `hands spaced shoulder-width apart on the shaft`).
  2. **Weapon-Hand vs. Empty Off-Hand Action Partition**: The hand holding a weapon ONLY executes blade slashes, thrusts, and parries; all wrist grabs, pushes, and off-hand actions MUST be explicitly assigned to the **`free left hand`**.
  3. **Tool/Weapon Switch Strictly on a Shot Cut**: When switching tools (e.g., setting a knife aside to twist a pepper mill), transition cleanly at the start of a new `Shot N` (`With the knife set aside, both of Marcus's strong masculine hands twist...`).
  4. **Zero Unannounced Hand-Swapping**: Keep the weapon in the same declared hand from `00:00` to `00:15.0`.
  5. **Disarm State Tracking**: If disarmed, explicitly state where the weapon lands AND that the hand is now empty (`leaving Vance's right hand empty`).

### Pillar 5: Multi-Clip Continuity Chaining (`Law D6` & Clean Terminal Landing) & 100% Diegetic Combat Acoustics
- **100% Diegetic Foley (`Strictly zero background music`)**: Synchronize rapid footwork friction, razor-sharp blade wind-whistles, crackling electric arcs, metallic blade clashes, and structural impacts across `Shot 1..N`.
- **Clean Terminal Keyframe Landing (`Final Shot @00:13.0–00:15.0`)**: The final shot of every `@CombatDirector` clip (`natural real-time speed`, `0 spoken words`) settles both characters into a **Clean Composed Landing Pose free of wild mid-swing motion blur** so the extracted `Last Frame @00:15.0` is razor-sharp for `TH1 / TH3` handover into Scene $N+1$.

---

## 3. The 8 Master Action-Drama & Chase Trope Archetypes (AC-01 to AC-08)

| Code | Trope Name | Core Narrative & Dramatic Engine | The Climax Chase / Combat Payoff |
|---|---|---|---|
| **AC-01** | **The Sealed Master Unchained** *(Cao Thủ Ẩn Danh Phá Phong Ấn)* | Former grandmaster or elite operative lives as a humble worker/father under a vow of peace until villains threaten his family. | Catches the villain's weapon bare-handed in Scene 04; sweeps 7 henchmen in Scene 05 and dismantles the boss in Scenes 06–08. |
| **AC-02** | **The Corridor of One Against Many** *(Đơn Thương Độc Mã Mở Đường Máu)* | Protagonist must fight through a narrow hallway, park walkway, or courtyard guarded by uniformed enforcers to reach a hostage. | High-velocity `1vN` domino destruction where each guard is launched into a pre-planted environmental fixture. |
| **AC-03** | **The Relentless Hunter-Prey Chase** *(Truy Đuổi Sinh Tử & Parkour)* | Protagonist holds vital evidence/antidote and is pursued through dense urban alleys, rooftops, or forests by an elite tracker. | High-speed parkour chase (vaulting crates, sliding under pipes, wall-rebounds) transitioning into a cornered close-quarters counter-fight. |
| **AC-04** | **The Awakened Bloodline / Blink-Speed Reversal** *(Thức Tỉnh Huyết Mạch Siêu Tốc)* | Underdog pushed to rock bottom unlocks dormant supernatural velocity or elemental qi when a loved one is endangered. | `10x` Blink-speed combat with decaying motion afterimages, leaf/dust slipstreams, whip-pan camera lag, and a devastating aerial finish. |
| **AC-05** | **The Equal Rivals Seesaw Duel** *(Song Hùng Kịch Chiến Cân Sức)* | Two peak martial artists with contrasting styles (e.g., Agile Counter-Boxer vs. Veteran Muay Thai Clinch Fighter) collide over an unyielding code. | Relentless `2.3x` back-and-forth seesaw brawl: combos, clinches, cracked tables, simultaneous cross-counters, and mutual respect/exhaustion. |
| **AC-06** | **The Sacred Guardian's Last Stand** *(Tử Thủ Bảo Vệ Mục Tiêu)* | Protagonist plants their feet in front of a doorway, crib, or altar, refusing to yield a single inch against waves of attackers. | Every parry, counter-throw, and weapon block is spatially anchored to keeping the enemy away from the protected landmark. |
| **AC-07** | **The Betrayed Disciple's Counter-Strike** *(Phản Đồ Đối Đầu Sư Môn)* | Arrogant traitor uses stolen sect techniques to humiliate the school; the overlooked true disciple steps into the ring. | Armed or unarmed martial arts duel exposing the flaw in the traitor's stolen technique through precision counter-strikes. |
| **AC-08** | **The Ticking-Clock Rescue Raid** *(Đột Kích Giải Cứu Đếm Ngược)* | Protagonist infiltrates an underground stronghold with minutes left to rescue a kidnapped family member before a deadline. | Covert tactical entry (`PURE_VISUAL_STEALTH`) erupting into an all-out high-velocity close-quarters takedown sequence. |

---

## 4. Episodic Pacing & 10-Second Scene Breakdown Protocol

Inside a standard **100-Second Action-Drama Episode (10 Scenes $\times$ 10.0s, with optional 15s/30s Climax override on user request)**:
- **Scene 01 `[00:00–00:10]` (Hook — `@Director` `1.0x`)**: In Medias Res physical threat or tense cornering; cognitive gap opened.
- **Scene 02 `[00:10–00:20]` (Restraint Setup — `@Director` `1.0x`)**: Root wound, protected person/prop, and the reason the protagonist holds back.
- **Scene 03 `[00:20–00:30]` (Escalation & Humiliation — `@Director` `1.0x`)**: Antagonist tightens the trap; rapid verbal fencing (`CADENCE: RAPID_SPARRING`).
- **Scene 04 `[00:30–00:40]` (The Ignition Snap — `@Director` $\to$ `@CombatDirector`)**: Antagonist crosses the moral line (`00:00–00:08.5`) $\to$ Protagonist intercepts the strike mid-air at `00:08.5–00:10.0` with a cold pre-combat vow.
- **Scene 05 `[00:40–00:50]` (Combat/Chase Wave 1 — `@CombatDirector` `2.3x–10x`)**: Explosive opening blitz, `1vN` guard sweep, or high-speed tactical chase across obstacles (`6–8 micro-phases`).
- **Scene 06 `[00:50–01:00]` (Combat Wave 2: Boss Clash — `@CombatDirector` `2.3x–10x`)**: `1v1` balanced seesaw duel against the primary adversary; adversary's heavy counter drives protagonist into a fixture.
- **Scene 07 `[01:00–01:10]` (Mid-Fight Awakening & Reversal — `@CombatDirector` `2.3x–10x`)**: Split-second glance at the narrative stake (`00:00–00:02.5`) $\to$ Full-power martial/aura comeback (`00:02.5–00:10.0`).
- **Scene 08 `[01:10–01:20]` (Combat Wave 3: Decisive Climax — `@CombatDirector` `2.3x–10x`)**: Simultaneous cross-counters, terrain springboard rebound, and the final devastating strike that disarms/defeats the adversary.
- **Scene 09 `[01:20–01:30]` (Release & Somatic Aftermath — `@Director` `1.0x`)**: Wrecked arena preserved in `[context]:`; heavy breathing, moral mercy, and embracing the rescued loved one (`Track A-Locked` or slow push-in).
- **Scene 10 `[01:30–01:40]` (Echo Resolution OR Zeigarnik Cliffhanger — `@Director` `1.0x`)**: Earned restorative peace (Standalone) OR a `00:07.5–00:10.0` Cold-Water reveal of a deadlier threat (Series).

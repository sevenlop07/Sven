# Sven Cinematic Universe — Action, Martial Arts, Chase & Supernatural Combat Genre Engine
File: `engine/genres/action.md`
SSOT Status: Authoritative Standard for High-Stakes Action-Drama, Martial Arts, Tactical Chases & Supernatural Combat
Governed by: Screenwriter (Level 2), Director (Level 2) & Combat Director (`@CombatDirector` — `.agents/skills/combat-director/SKILL.md`) under Showrunner (Level 1)

---

## 0. Core Principles & Dramatic Philosophy

The objective of the **Action, Martial Arts, Chase & Supernatural Combat Genre Engine** is to architect high-adrenaline, emotionally grounded action cinema (short films, 10-scene episodic series, Wuxia/Xianxia vertical dramas, urban martial arts thrillers, and supernatural awakened-bloodline series).

In the Sven Cinematic Universe, **action is never hollow physical gymnastics**. A fight or chase only erupts when emotional compression, moral injustice, or ticking-clock stakes reach an unbearable boiling point where words can no longer resolve the conflict (*When dialogue is exhausted, physics takes over*).

### 0.1 The Action-Drama Equation
$$\text{Cinematic Action-Drama} = \text{Suppressed Emotional Compression (1.0x Setup)} + \text{High-Velocity Kinetic Chase/Combat (2.3x–10x Climax)} + \text{Earned Moral Resolution (1.0x Aftermath)}$$

1. **The Restraint-to-Detonation Law (Nén Tâm Lý Trước Khi Nổ Vật Lý)**:
   - The audience must ache for the protagonist to fight back before the first punch is thrown. Early scenes establish a powerful restraint (an oath of non-violence, a hostage/loved one at risk, a sealed bloodline, or a desire for peace) that the antagonist ruthlessly tramples until the moral red line is crossed.
2. **Dual-Speed Temporal Orchestration (`1.0x` Drama vs. `2.3x–10x` Combat/Chase)**:
   - Dramatic setup and aftermath scenes operate at natural human tempo (`1.0x`, `2–3 phases` per 10s clip) governed by `@Screenwriter` and `@Director`.
   - Chase and combat scenes switch immediately to `@CombatDirector` high-velocity micro-timelines (`2.3x` martial arts or `10x` superhuman blink-speed, `5–8 phases` per 10s clip or `12–15 phases` per 30s clip) driven by **Kinetic Arrow Chains (`→`)**.
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

### Pillar 2: High-Velocity Chase & Parkour Mechanics (Truy Đuổi & Vượt Địa Hình)
When a scene involves a chase (foot chase, urban parkour, forest pursuit, or blink-speed hunt), enforce three kinetic laws:
1. **Obstacle Pre-Planting & Tactile Vaulting**: `[context]:` must inventory physical obstacles along the pursuit vector (market stalls, narrow alley crates, rooftop air ducts, ancient tree trunks, wet concrete corridors). In the timeline, runners must physically interact with them (`vaults one-handed over a wooden crate → slides beneath a low steel pipe → kicks off a brick wall to round the corner`).
2. **Predator-Prey Distance Compression**: Express chase tension through closing spatial proximity within the same frame (`Medium-wide tracking shot framing prey sprinting in foreground as hunter closes from three paces behind to point-blank lunging reach`).
3. **Blink-Speed Pursuit & Camera Reaction Lag**: For supernatural chases, combine spatial wake cues (`purple-black motion streaks`, `decaying afterimages`, `leaves sucked into the slipstream`, `vertical tree-trunk running`) with **Camera Reaction Lag** (`camera momentarily loses weka_2 for a split-second before whip-panning to catch weka_2 landing across the clearing`).

### Pillar 3: The Momentum Seesaw, Micro-Timeline Arrow Syntax (`→`) & Slow-Motion Decision Matrix
Governed by `@CombatDirector` ([`SKILL.md`](file:///d:/Project/Sven/.agents/skills/combat-director/SKILL.md)):
- **Zero Turn-Based Waiting**: Every `1.5s–2.5s` phase chains `4–6 anatomical action nodes` with arrows (`→`): `[Attack Combo] → [Parry / Head-Slip / Duck] → [Instant Counter-Strike] → [Fixture Impact]`.
- **Zero Ground-Time & Terrain Rebounds**: Knocked-down fighters never lie flat (`→ hits the floor and rolls straight back onto both feet with zero ground delay` or `uses the wooden bar counter as a springboard to launch an explosive counter-kick`).
- **Simultaneous Cross-Counters**: Highlight equal power by directing both fighters to land hooks/strikes at the exact same instant, jolting half a step back before re-colliding.
- **The Slow-Motion Decision Matrix (3 Banned Zones vs. 5 Golden Speed-Ramp Moments)**:
  - *Strictly Banned (`0% Slow-Motion`)* in: (1) Grounded close-quarters hand-to-hand combos (Muay Thai, MMA, street brawls), (2) Pure blink-speed perception blitzes, and (3) Knockback trajectories / falling bodies (slow-motion makes falling bodies look floaty and weightless).
  - *Allowed ONLY as a **`Fast Velocity → 0.5s Brief Slow-Motion ECU → Instant Snap Back to Extreme Speed` Sandwich** (max 1–2 times per clip)* at **5 Golden Moments**:
    1. **Mid-Air Lethal Catch** (hand snatching an incoming ankle, fist, or blade inches from the face with sparks and shocked eyes).
    2. **Razor-Thin Near-Miss** (blade or heel slicing centimeters past the nose/throat, whipping loose hair strands).
    3. **Aerial Split / 360-Rotation Apex** (exact instant an acrobatic kick or split double-kick connects with the targets' jaws).
    4. **Eye-of-the-Storm Grapple Lock** (faces inches apart mid-air or in a weapon bind with opposing auras crackling).
    5. **Final Blow Contact Frame** (exact millisecond the finishing strike compresses into the boss's chest before snapping back to extreme speed for the ground crash).
- **Advanced Aerial & Supernatural Timeline Mechanics**:
  - *Vertical Altitude Axis Choreography*: Vary height continuously across phases (low dust layer $\leftrightarrow$ mid-air clash $\leftrightarrow$ high moonlight apex $\leftrightarrow$ downward crater slam) to prevent static hovering.
  - *Dual-Energy Collision Geometry*: Direct opposing auras as reactive physical matter (sparks on block, double-helix tornado vortex during spinning throws, meteor vs. lightning bolt during dives).
  - *Mid-Trajectory Pursuit Combos*: Launch opponent skyward $\to$ godspeed dash to overtake them mid-air $\to$ slam them into the crater.

### Pillar 4: Combat-Sovereign `[subject]:` & `[PROP]:` Protocol + Hand-Grip Biomechanics Lock
- **Strict Mode B Compliance**: Zero clothing, footwear, hair, height, or age descriptions in `[subject]:` or action prose (`[100% Appearance, attire, and facial features Refer to image X]` locks all visual appearance).
- **Mandatory Combat & Story Identity in `[subject]:`**: Every fighter's `[subject]:` line declares:
  1. Initial spatial anchor & coiled guard posture at `00:00.0`
  2. Specific **Martial Arts Style & Biomechanical Specialty** (e.g., *explosive street counter-boxing*, *underground Muay Thai clinch-and-elbow*, *swift Wudang circular swordplay*)
  3. **Unarmed Guard / Tier-1 Weapon Grip / Supernatural Aura Signature** (e.g., *crackling purple-pink-black blink-speed aura*, *frost-infused silver longsword*)
  4. **Narrative Combat Stake** tied to the main plot (e.g., *desperate resolve to shield the younger sister behind the door*).
- **The 5 Biomechanical Hand-Grip Laws (Eradicating Weapon & Prop Glitches)**:
  1. **Single-Handed vs. Two-Handed Hilt Classification**:
     - *1-Handed Weapons (`Kunai, Tanto, Straight Sword, Baton`)*: Lock to ONE specific hand (`gripped in forward/reverse hold in right hand`) and explicitly declare the other hand empty (`left hand completely empty`). Never put two hands on a short hilt (causes Fused-Fist glitches).
     - *2-Handed Weapons (`Heavy Broadsword, Greatsword, Katana 2-Hand, Spear, Staff`)*: Explicitly space both hands along the handle (`right hand below crossguard, left hand anchored at pommel` or `hands spaced shoulder-width apart on the shaft`).
  2. **Weapon-Hand vs. Empty Off-Hand Action Partition**: The hand holding a weapon ONLY executes blade slashes, thrusts, and parries; all punches, wrist grabs, floor-posts, and one-handed seals MUST be explicitly assigned to the **`empty left hand`** (or legs/knees).
  3. **Explicit Two-to-One Hand Release**: A fighter holding a 2-handed weapon cannot grab, punch, or post on the floor unless the prompt first states: `releases left hand from the pommel, shifting the blade to a single right-handed hold` (prevents 3rd-arm hallucinations).
  4. **Zero Unannounced Hand-Swapping**: Keep the weapon in the same declared hand from `00:00` to `00:10.0`, re-anchoring `right-hand blade` in each phase.
  5. **Disarm State Tracking**: If disarmed, explicitly state where the weapon lands AND that the hand is now empty (`leaving ryuji's right hand empty`) to prevent ghost weapon respawning.

### Pillar 5: Multi-Clip 3-Slot Continuity Chaining & 100% Diegetic Combat Acoustics
- **100% Diegetic Foley (`Strictly zero background music`)**: Synchronize rapid footwork friction, ragged breathing, cloth air-whip, visceral flesh-and-bone impacts (`WHAM-THUD-CRACK`), blade clashes, and structural destruction.
- **Chaining Consecutive Fight/Chase Clips (`10s + 10s + 10s`)**: End Scene N at `00:10.0` on a **Mid-Lunge Cut Point** (`both fighters plant both feet and lunge furiously back at each other at 00:10.0`) so Scene N+1 ignites at full velocity at `00:00.0`.

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

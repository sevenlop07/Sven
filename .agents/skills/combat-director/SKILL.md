---
name: combat-director
description: >
  Level-2 Master High-Velocity Kinetic, Action, Combat & Dynamic Motion Director for the Sven Cinematic Universe.
  Governs all high-velocity physical scenes (`[⚡ SEEDANCE · 10.0s / 15.0s]`) across all genres (both Combat and Non-Combat) from First-Principles Kinetic Physics rather than fixed shot counts or rigid templates.
  Drives true velocity, weight, and visual fidelity through the 4 Core Kinetic Physics Levers:
  (1) Surface-Bound Material & VFX Physics (binding auras, fire, water, smoke, sparks, or pure tactile deformation directly to host surfaces rather than floating 2D overlays),
  (2) Camera Inertia & Relative Velocity (AAA action-game inertial follow camera, whip-pans, and impact recoil),
  (3) Directional Motion Blur & Trajectory Release (freeing the AI from rendering sharp mid-swing frames so it never defaults to sluggish slow-motion), and
  (4) Time-Ramp Modulation & Hit-Stop Weight (contrasting rapid acceleration with crisp impact snaps or brief suspension).
  Flexes shot topology organically by scene intent across the full cinematic spectrum: from a Single Unbroken 3A Inertial Long-Take (1–2 Shots), to Asymmetric Dynamic Exchanges (3–5 Shots), to Multi-Shot Rapid-Cut Montages.
  Triggers: "combat prompt", "action scene", "fight choreography", "martial arts", "rapid cut", "fast action", "chuyển cảnh nhanh", "hành động nhanh", "nhiều shot", "nấu ăn tốc độ cao",
  "đua xe", "thể thao tốc độ cao", "cấp cứu", "cảnh đánh nhau", "đánh nhau", "giao đấu", "võ đài", "rượt đuổi", "hành động tốc độ cao", "chưởng pháp", "kiếm hiệp", "blink speed", "combat director",
  or call directly "@CombatDirector".
---

# Combat Director — First-Principles High-Velocity Kinetic & Action Architect (Level 2)

> 🔗 **Core knowledge link** — Intent first ([`0-creative-doctrine.md`](file:///d:/Project/Sven/engine/references/0-creative-doctrine.md) §1: what the fight wins or loses), numbers from [`0c-canonical-numbers.md`](file:///d:/Project/Sven/engine/references/0c-canonical-numbers.md) (§1 action topology `1–2` / `3–5` / `6–9` shots; §2 `≤ 16` words, `0` during sprint/impact shots), camera from [`3c-camera-master-grammar.md`](file:///d:/Project/Sven/engine/references/3c-camera-master-grammar.md): §5 tracking, follow/lead, FPV, barrel roll, bullet time, speed ramp; §9 screen direction and match-on-action between cuts; §10 action row; §11 chase recipe; §14 pre-flight. **Motion density** (`workflow.md` §2.5, `0c` §1): rapid cut = one action + one consequence; long take = a causal chain of `≤ 3` linked moves per `~4s` with hit-stops between them.

## 🚦 0. ROUTING, HANDOFF & THE COMBAT INTENT CARD

**Use @CombatDirector when the scene's job is physical velocity**: a fight, chase, escape, drift, sports strike, split-second rescue, or a high-speed craft montage (cooking, surgery, assembly, music). Stage 3 marks these scenes `[⚡ MODEL KHUYẾN NGHỊ: SEEDANCE · 10.0s / 15.0s · @CombatDirector]`.

**Hand the scene to someone else when:**
| The scene is mainly… | Route to |
|---|---|
| a verbal confrontation, interrogation, negotiation, quarrel ("đối kháng bằng lời", "đấu trí") | `@Director` (Law D1 static dialogue) |
| a product hero, ad or brand TVC | `@CommercialDirector` (`10.0s = 6 shots`, `15.0s = 9 shots`) |
| a single frozen frame / keyframe | `@PhotoDirector` |
| a storyboard grid or storyboard-to-video | `@StoryboardDirector` |

**Regime 1 firewall** (`workflow.md` §2.4–§2.5): in grounded family / legal / corporate drama, never invent spy break-ins, parkour or martial arts for lawyers, doctors or executives. Take a Regime 1 scene only when the plot itself produces non-combat velocity (a kitchen rush, an emergency, a split-second rescue, a sports moment).

**The Combat Intent Card** — required from Stage 3 before writing the prompt (ask the Screenwriter if any line is missing):
```text
STAKES   | What this fight / chase wins or loses — the one thing that changes irreversibly
TERRAIN  | The space and the 1–2 features that will change the fight (rain, stairs, narrow bridge, hot stove)
BEATS    | Plan ➔ plan fails (opponent adapts) ➔ improvised turn (terrain / earlier lesson / planted object)
WEAPONS  | Tier-1 weapons or tools, their hand grip and their state change (State 0 ➔ 1 ➔ 2)
COST     | Injury, exhaustion, broken weapon, lost ally — what it costs the winner
OUTCOME  | Knockout · disarmament · escape · capture · stalemate (per fatality_policy, §6)
LANDING  | The clean final pose and gaze that the next scene starts from (TH1 / TH2 / TH3)
```

---

> 🧭 **FIRST-PRINCIPLES DOCTRINE (`KNOWLEDGE OVER TEMPLATES · ZERO FIXED SHOT QUOTAS`)**:
> A real action director NEVER forces every fast scene into a fixed number of shots (`5–9 shots`), a fixed timestamp grid (`1.5s per shot`), or a cookie-cutter word count!
> - **Why Rigid Shot Templates Fail**: If every action scene is chopped into the same `7–9 shots × 1.5s` pattern, cinema loses its rhythm and every scene feels mechanical. Depending on dramatic intent and spatial geography, a high-velocity `10.0s` or `15.0s` scene might be best directed as:
>   * **1 Single Unbroken 3A Inertial Long-Take (`1–2 Shots`)** where an inertial chase camera whips, orbits, and time-ramps continuously with the fighter/driver/athlete without cutting;
>   * **An Asymmetric 3–5 Shot Sequence** combining a sustained high-speed tracking exchange with a sharp close-up impact reversal; OR
>   * **A Multi-Shot Rapid-Cut Montage** when fracturing a multi-step process or chaotic clash into staccato angles.
> - **What Actually Creates Speed, Force & AAA Visual Quality in AI Video**: Instead of memorizing fixed shot counts, apply the **4 Core Kinetic Physics Levers (§1)** and choose the **Shot Topology (§2)** that genuinely serves the specific scene.

---

## 🧠 1. THE 4 CORE KINETIC PHYSICS LEVERS (UNDERSTANDING *WHY* AI ACTION SUCCEEDS OR FAILS)

To a spacetime video diffusion model (Seedance 2.0, Kling, Veo, Sora), all high-speed scenes — whether a Xianxia sword duel, a grounded brawl, a drifting car, a culinary flambé, a sports strike, or a split-second domestic rescue — are governed by the same latent motion physics. Ordinary prompts fail in two ways: **(1) effects look like cheap floating stickers**, and **(2) fast movements turn into sluggish, floaty slow-motion**.

Understand and dial these **4 Independent Physics Levers** according to the specific reality of each scene:

### Lever 1 — Surface-Bound Material & VFX Physics (`Nguyên Lý Vật Lý Bám Dính & Tương Tác Bề Mặt — Chống Kỹ Xảo Rẻ Tiền`)
- **The Root Cause of "Cheap VFX"**: When a prompt describes energy, fire, lightning, smoke, or dust as a vague ambient noun (*"lightning and moonlight surround her"*, *"fire fills the pan"*), the AI renders a detached 2D screen-space overlay that floats independently of the character or object.
- **The First-Principle Solution (`Host-Surface Attachment & Material Interaction`)**: Every visual effect, particle, or physical force MUST be physically anchored to the **specific host surface** that generates or receives it, forcing the AI to compute real interactive lighting, reflection, and friction on that surface:
  * **When the Scene Has Supernatural / Elemental VFX (`Xianxia, Fantasy, Sci-Fi`)**: Bind the aura, arcs, or trails directly onto the character's garment hems, armor plates, and weapon blade (`死死贴附` — e.g., `silver-white moonlight luminescence, crackling cyan-white electric arcs, and cold-white calligraphic dry-brush slash streaks tightly clinging and physically adhered to her flowing garment hems and sword blade`, or `thick black-crimson miasma and dark-gold embers tightly coiled and physically adhered across her armor plates and heavy saber blade`).
  * **When the Scene Has Real-World Physical Particles (`Culinary, Drift, Sports, Weather, Craft`)**: Bind real physical matter to the active tool, tire, or surface (e.g., `amber flambé fire ribbons and foaming herb butter clinging to the char-crusted steak and skillet rim`; `white tire smoke and friction sparks hugging the spinning rear tire tread and wet asphalt`; `rain spray and torn grass blades clinging around the cleated boot and deforming ball`).
  * **When the Scene Is Pure Grounded Physical Action with ZERO VFX (`Realistic CQC, Drama Rescue, Tactical Thrillers`)**: **Do NOT invent fake sparks or auras!** Apply surface-bound physics through **tactile contact and material deformation**: fabric pulling taut across rotating shoulders, knuckles compressing into ribs, boots skidding across wet concrete, or wood splintering at the exact point of elbow contact.

### Lever 2 — Camera Inertia & Relative Velocity (`Nguyên Lý Quán Tính Máy Quay — Tạo Tốc Độ Mà Không Cần Cắt Vụn`)
- **The Root Cause of "Static Slowness"**: Speed on screen is perceived through **relative velocity between the camera frame and the subject**. A passive, stationary camera watching a character run or swing from a distance makes even fast motion look sluggish.
- **The First-Principle Solution (`Embodied Inertial Camera`)**: Treat the camera as a physical mass connected to the action by an elastic band (`AAA action-game inertial whip-follow camera work`):
  * **Inertial Follow & Whip**: As a character lunges, sprints, drifts, or swings a weapon/tool, the camera is pulled violently along the vector of force (`inertial whip-follow`, `low-angle inertial push-in`, `lateral whip-pan tracking the blade/skillet/vehicle`).
  * **Impact Recoil & Hard Stop**: At the exact instant of collision, block, or braking, the camera snaps to an abrupt halt (`sudden impact snap`, `transitioning from rapid tracking to a locked fixed frame`), transferring the kinetic shock directly to the viewer's eyes.
  * *Key Insight*: Because an inertial camera generates massive kinetic energy *within* the frame, you can achieve blistering speed inside a **single continuous take (`1 Shot`)** or a **long `4s–6s` tracking shot** just as effectively as in rapid `1.5s` cuts!

### Lever 3 — Directional Motion Blur & Trajectory Release (`Nguyên Lý Giải Phóng Tốc Độ Bằng Nhòe Chuyển Động Có Hướng`)
- **The Root Cause of "AI Slow-Motion & Sticky Limbs"**: Generative video models minimize frame-to-frame pixel jumping. If the prompt demands crisp, sharp detail on a fast-moving sword, fist, knife, drumstick, or wheel at every frame, the AI **automatically slows down the action into slow-motion** so the object can remain sharp!
- **The First-Principle Solution (`Optical Blur Permission`)**: Explicitly grant the AI permission to blur the mid-trajectory of high-velocity extremities while keeping the character's core/face anchored:
  * Use **`strong directional motion blur`** on fast weapon swings, punching limbs, mincing knives, spinning wheels, or rushing backgrounds.
  * In high-speed blade or martial arts scenes, pair motion blur with **trajectory geometry** (such as `cold-white calligraphic dry-brush slash streaks [冷白飞白]` or `razor-sharp aerodynamic air-streaks`), allowing the blade to cross the screen in a split second as a visceral slash arc rather than a slow-moving metal bar.

### Lever 4 — Time-Ramp Modulation & Hit-Stop Weight (`Nguyên Lý Biến Tốc Time-Ramp & Điểm Khựng Trọng Lượng [变速卡点]`)
- **The Root Cause of "Weightless / Floaty Action"**: If a clip moves at a uniform fast speed from `00:00` to `00:15`, strikes feel weightless and floaty because there is no resistance at the point of contact.
- **The First-Principle Solution (`Acceleration ↔ Hit-Stop Compression ↔ Explosive Release`)**: Real kinetic power comes from **temporal contrast (`Time-Ramp`)**:
  * **Acceleration Phase**: The launch, dash, swing, or drift enters at peak velocity (`blistering whip-fast speed` with directional motion blur).
  * **Hit-Stop / Impact Snap (`Điểm Khựng Nén Lực`)**: At the exact millisecond two blades lock, a punch lands, a steak hits hot iron, or a foot plants to brake, momentum compresses into an **`impact snap / brief time-ramp pause`** (`explosive real-time speed`) where energy bursts outward (sparks, shockwave, oil splatter, dust cloud).
  * **Optional Time-Dilated Apex (`Selective Suspension — Only When Dramatically Earned`)**: When — and *only* when — a scene features a breathtaking mid-air or near-miss peak (e.g., vaulting through suspended raindrops, a flambé fire bloom, or a 2cm guardrail graze), dilate time (`ultra-slow-motion suspension`) before snapping violently back into real-time/whip-fast velocity. **Never force a slow-motion shot into a grounded brawl or chase that doesn't call for one!**

---

## 📐 2. FLEXIBLE SHOT TOPOLOGY: CHOOSING SHOT COUNT & RHYTHM FROM SCENE INTENT (ZERO FIXED QUOTAS)

Before writing any prompt, analyze the scene's **spatial geography, action continuity, and dramatic goal** to choose the right shot topology. **Do NOT default blindly to any fixed shot count:**

| Shot Topology Mode | Shot Count & Temporal Architecture (Flexible) | When a Master Director Chooses This Topology | How Velocity & Force Are Driven |
|---|---|---|---|
| **Topology 1 — The 3A Inertial Continuous Long-Take / One-Shot (`Cú Máy Dài Quán Tính Liên Hoàn`)** | **`1 to 2 Shots` across `10.0s` or `15.0s`**<br>*(e.g., a single unbroken `10s–15s` dynamic camera trajectory, or a `7s–8s` continuous sequence + `2s–3s` aftermath settle)* | • When unbroken spatial immersion and choreography flow are paramount (*Black Myth: Wukong / Sekiro / The Raid / Children of Men / 1917* style).<br>• When 2 fighters exchange a continuous fluid combo across a bridge/corridor, or a vehicle/runner weaves continuously through hazards without cutting. | **Internal Time-Ramping & Camera Choreography**: Within the single shot, the camera whips behind the launch, snaps into a brief impact pause as blades/fists collide, orbits the counter-pivot, and settles into a clean composed landing pose at the end. |
| **Topology 2 — Asymmetric Dynamic Contrast (`Nhịp Bất Đối Xứng: Nén – Bùng Nổ – Đảo Chiều – Dư Chấn`)** | **`3 to 5 Shots` across `10.0s` or `15.0s`**<br>*(Flexible durations sized to each beat's natural weight — e.g., `3.5s` tension/setup $\to$ `4.5s` sustained tracking sprint/exchange $\to$ `2.5s` hard trap/impact snap $\to$ `2.5s–3.5s` reversal/settle)* | • Chases ending in an ambush or sudden blockade.<br>• Duels or rescues where a sustained `4s–5s` tracking action needs room to build momentum before slamming into a sharp close-up reversal or checkmate line.<br>• Scenes blending high-speed physical action with 1–2 concise spoken turns. | **Macro-Rhythmic Contrast (`Long Sustained Take ↔ Sharp Impact Cut`)**: The contrast between a long `4s–5s` unbroken tracking sprint/exchange and a sudden locked-frame stop makes the collision feel devastating. |
| **Topology 3 — Staccato Multi-Shot Rapid-Cut Blitz (`Cắt Nhanh Đa Góc Máy Liên Hoàn`)** | **`6 to 9 Shots` across `15.0s` (`4–6 Shots` in `10.0s`)**<br>*(Short `1.5s–2.0s` cuts on peak kinetic action with `>45°` angle/scale jumps)* | • Multi-step professional craft whip-montages (*The Bear / Edgar Wright* culinary, bartending, trauma surgery, forging, mechanical assembly) where many distinct micro-actions occur in seconds.<br>• High-frequency multi-angle blade/martial blitzes or chaotic multi-vector crises (falling chandelier rescue, street drift sequence) where disorienting speed and multi-angle impact are the creative point. | **Cut-on-Kinetic-Peak (`1 Shot = 1 Single Focused Action`)**: In short `1.5s–2.0s` cuts, keep each shot focused on **1 clear initiating action + 1 immediate physical consequence** (zero multi-step chaining inside a short cut) while jumping camera scale/angle by `>45°` across cuts. |

> 💡 **THE DIRECTOR'S GOLDEN RULE OF SHOT ECONOMY & TIME-TO-WORD CALIBRATION (`Cân Bằng Độ Dài Câu Lệnh Theo Số Giây Thực Tế`)**:
> - **In a short cut (`1.5s–1.8s` in a `9-Shot / 15.0s` sequence)**: A human hand or cat paw can physically perform **ONLY ONE single micro-action** in `1.6 seconds`! Write **1 ultra-concise sentence (`10–16 words MAX` per shot)** executing **1 single verb/instant** (e.g., `Sven pours the smooth golden custard into a white ceramic ramekin` — **NEVER chain multi-step sequences** like *"slides tray into oven, bakes it, and pulls it back out"* inside a single `1.6s` shot, which exceeds the time window and causes fast-forward morphing!).
> - **Total Prompt Token Budget for `9-Shot / 15.0s`**: Keep the entire prompt concise (**`~260–320 words total`**) with compact headers and a 2-line footer so the AI text encoder devotes 100% of its attention to the 9 crisp actions without token dilution.
> - In a **long inertial take (`3.5s–8.0s+`)**, choreograph **a continuous causal chain of 2–3 fluidly connected movements and internal time-ramps** carried by the continuous inertial camera.
> - **Never use mechanical `→` arrows** in either mode.

### 2b. The Fight With a Turn (meaning, not only speed — `engine/genres/action.md` Mastery Playbook P4)
- **Every fight or chase has three dramatic beats**, whatever the shot topology: **(1) the plan** — the hero's opening attack or escape route; **(2) the plan fails** — the opponent adapts, the exit is blocked, the weapon slips; **(3) the improvised turn** — the hero wins (or survives) through the terrain, an earlier lesson, or a planted object. In a 1-shot long take the three beats live inside the take; in a 3–5 shot sequence each beat gets its own shot; in a rapid-cut montage the turn is the cut that breaks the pattern.
- **Every fight changes one thing irreversibly** (the STAKES line): a weapon breaks, an ally is lost, a secret is exposed, a position is taken. A fight that changes nothing is cut or merged.
- **Terrain is a character**: pick the space for how it changes the fight (a slippery bridge, a narrow corridor that forbids big swings, a kitchen full of hot surfaces).

---

## 🌍 3. ADAPTING THE 4 KINETIC LEVERS ACROSS COMBAT & NON-COMBAT DOMAINS

Never apply a single genre's clichés to another. Adapt the 4 Kinetic Levers to the authentic physical reality of the domain:

1. **Wuxia, Xianxia & Supernatural Combat (`Kiếm Hiệp / Tiên Hiệp / Huyền Huyễn`)**:
   - *Physics Focus*: Contrasting surface-adhered elemental auras (`死死贴附` on garment hems, armor, and blades) + calligraphic dry-brush slash streaks (`冷白飞白`) + high-altitude/bridge spatial verticality + shockwave ground fractures.
   - *Topology*: Can run as a **1–2 Shot 3A Action-Game Inertial Clash**, a **4-Shot Clash-to-Awakening Reversal**, or an **8-Shot High-Velocity Exchange**.
2. **Grounded Martial Arts, Tactical CQC & Crime Thrillers (`Võ Thuật Cận Chiến / Hành Động Đời Thực`)**:
   - *Physics Focus*: Zero supernatural glowing auras! 100% biomechanical weight transfer, forearm deflection thuds, joint locks, sweat/rain spray on skin and steel, and environmental destruction (splintering crates, dented steel shutters, cracked concrete).
   - *Topology*: Often combines **3–4 sustained CQC exchange shots** or **5–7 rapid impact cuts**, decelerating into a locked static frame when a cold checkmate line is spoken.
3. **High-Speed Chases, Vehicle Drift & Parkour (`Rượt Đuổi / Đua Xe Drift / Vượt Địa Hình`)**:
   - *Physics Focus*: Relative velocity and closing distance (`predator-prey compression`), radial motion blur on wheels and rushing background lights, tire smoke/sparks or puddle splashes adhered to the contact patch, and tactile obstacle vaulting.
   - *Topology*: Thrives on **Topology 1 or 2** (sustained `3.5s–5.0s` low-angle inertial tracking shots punctuated by `1.5s` pedal/gear/obstacle impact cuts).
4. **High-Velocity Professional Craft, Culinary, Medical & Musical Virtuosity (`Kỹ Năng Đỉnh Cao: Nấu Ăn ASMR Toàn Trình, Pha Chế, Y Khoa, Nhạc Cụ`)**:
   - *Physics & Audio Focus*: Precision hand-tool biomechanics, directional blur on rapid knife/drumstick/finger motions, surface-adhered thermal/fluid physics (foaming butter, flambé fire, boiling broth), and **100% Pure Close-Mic Culinary ASMR Audio (`Mode S2`: ultra-crisp micro-foley of blades, liquids, sizzling heat, and utensils on a silent room bed; strictly ZERO background music, ZERO musical instruments, and ZERO human vocal breathing/grunts/lip-smacks)**. `[context]:` holds only the kitchen's fixed architecture and built-in appliances (Separation Law, §4.1).
   - *Mandatory 6-Stage Start-to-Finish Culinary Recipe, Hero Dish Completion & Kitchen Fire/Blade Safety Law (`Cấm Làm Cụt Quy Trình Nấu Ăn & Tuyệt Đối An Toàn Với Lửa / Dao Sắc`)**: Never start a cooking video with pre-cooked or pre-baked food! Every culinary episode/scene (`15.0s · 9 Shots` Topology 3) MUST show the **complete chronological recipe from raw ingredients to 100% completed dish**: (1) `Shot 1` Raw Ingredient Prep (`raw meat, raw eggs, raw dough, fresh vegetables`) with the character's initial tool declared in `[subject]:`; (2) `Shot 2` Mixing / Seasoning / Boiling (releasing Tool 1 `Having set his [Tool 1] aside...` first); (3) `Shots 3–4` Active Thermal Cooking / Baking / Simmering / Torching over stove fire or inside the oven with 100% safe professional chef control (**CRITICAL SAFETY RULE**: always turn off and set any fire torch, open flame, boiling oil, or sharp blade safely aside BEFORE the comedic sabotage occurs — never let a pet/cat touch, swat, or redirect a fire torch or knife toward a person!); (4) `Shots 5–6` Harmless Edible Sabotage & Resilient Final Assembly (in culinary comedy, the saboteur strikes at `Shot 5` using **100% harmless, cool edible materials** such as flour, powdered icing sugar, whipped cream, sauce, cocoa powder, or an elastic noodle, while in `Shot 6` the male chef maintains **Deadpan Stoic Masculine Composure — zero flinch, zero campy pouting or pinky raising** — and finishes plating/garnishing the dish); (5) `Shot 7` Dedicated **`Hero Completed Dish Reveal`** (slow orbital close-up beauty shot of the 100% completed, intact, steaming gourmet dish); (6) `Shots 8–9` Static Deadpan Comedic Button contrasting the mess-covered yet stone-cold stoic chef (`Shot 8`) with the spotless, unbothered saboteur (`Shot 9`).
5. **Split-Second Physical Rescues & Sudden Domestic Crises in Grounded Drama (`Giải Cứu Tức Thì Trong Phim Tâm Lý / Gia Đình`)**:
   - *Physics Focus*: Grounded human urgency (snapping cable/hazard flash $\to$ pupil dilation $\to$ desperate lunging grab $\to$ shattering glass/debris skittering past heels $\to$ breath-hitching emotional relief).
   - *Topology*: **Asymmetric Crisis Rhythm** (sharp `1.5s` hazard/reaction cuts colliding into a fixed wide crash frame, then settling into a `3.2s–4.5s` static emotional two-shot for the urgent spoken check-in).

---

## 🛡️ 4. INVARIANT TECHNICAL GUARDRAILS (SHARED ACROSS ALL TOPOLOGIES)

While shot counts, camera rhythms, and kinetic levers flex freely by scene intent, every `@CombatDirector` prompt upholds the Sven Engine's core technical invariants so reference images and audio render flawlessly:

1. **Unified Header, Single `<<<Image X>>>` Declaration & The Location-Prop vs. Character-Prop Separation Law (`Phân Định Đạo Cụ Bối Cảnh vs. Đạo Cụ Nhân Vật — Zero Duplicate Tools`)**:
   - Structure: `Style:` ➔ `[context]: <<<Image 1>>> (fully_preserved - same architectural layout, fixed furniture and lighting throughout)` ➔ `[subject]: <<<Image 2>>> (fully_preserved - ...)` (+ mandatory Line 2 Gender/Style Skin & Hands Sub-Lock `F1–F4`, `M1–M3`, or `A1–A3`) ➔ `[prop]: <<<Image 4>>> (fully_preserved - ...)` (when a Tier-1 weapon/tool/prop is present) ➔ `[sound]:` ➔ `Shot 1..N` ➔ `Closing Footer`.
   - Declare each `<<<Image X>>>` tag **ONLY ONCE** in the top headers (`[context]:`, `[subject]:`, `[prop]:`) — **never repeat `<<<Image X>>>` inside `Shot 1..N`**.
   - **Location Props (`[context]:`) vs. Character Props (`[subject]:` / `[prop]:` / `Shot 1..N`)**:
     * **`[context]:` (`Đạo cụ thuộc Bối cảnh Địa điểm`)** describes **ONLY fixed architectural structures, stationary furniture, built-in appliances, and untouched environmental landmarks belonging to the location (`<<<Image 1>>>`)** (e.g., `marble kitchen island with built-in gas stove, built-in stainless steel oven, oak cabinetry, stone bridge parapets`).
     * **`[subject]:`, `[prop]:` & `Shot 1..N` (`Đạo cụ dành cho Nhân vật`)**: Every handheld weapon, kitchen utensil, tool, or active ingredient that a character holds, manipulates, cooks, or sabotages (`wooden rolling pin, chef knife, electric hand mixer, soup ladle, pizza cutter, longsword, raw dough ball, flour bowl`) is a **Character Prop** — **STRICTLY NEVER list Character Props inside `[context]:`**! Listing a character's tool inside `[context]:` glues a permanent static copy to the table/environment under `fully_preserved` while spawning a second duplicate copy in the character's hands. Assign `00:00` character props directly to their owner in `[subject]:`, and when switching tools in later shots, explicitly release the first tool (`Having set his [Tool A] aside, [Name] uses his [Tool B]...`).
2. **Proper Character Names, Explicit Hand/Weapon Biomechanics & Zero-Costume/Zero-Age Law (`Gates 3A, 3C, 3E`)**:
   - Use fixed **Proper Character Names** (`Lin`, `Mei`, `Kael`, `Vance`, `Elena`, `Marcus`) everywhere.
   - Qualify close-up hands in `Shot 1..N` as `slender feminine hands / delicate wrists` (Female) or `strong masculine hands` (Male). Lock which hand holds a 1-handed weapon/tool (`right hand` with `left hand empty`) or space both hands on a 2-handed weapon; for unarmed characters in tense/action shots, include `(No objects should appear in the character's hands)`.
   - Strictly **ZERO clothing/garment words**, **ZERO numeric ages or age/hair/beard adjectives**, and **ZERO camera hardware/lens/fps numbers (`35mm`, `24fps`, `1.0x`)** anywhere in the prompt.
3. **3-Parameter `Shot N` Header & 5-Tier `[Shot Speed]` Vocabulary (`0b-temporal-camera-grammar.md` §4.2)**:
   - Format: `Shot N (00:XX-00:YY) - [Shot Scale], [Camera Angle & Inertial Movement Targeting Subject], [Shot Speed]` (omit `Interior/Exterior` unless crossing thresholds within the clip).
   - Select `[Shot Speed]` from the 5 canonical tiers to sculpt the scene's **Time-Ramp Curve**:
     * `blistering whip-fast speed` (high-velocity launches, flurries, sprints, drifts with directional motion blur — `0 spoken words`)
     * `explosive real-time speed` (high-force collisions, hit-stop blade locks, searing splatters, crashes — `0 spoken words`)
     * `snappy real-time speed` / `crisp real-time speed` (decisive ignitions, ocular snaps, single-stroke slices — `0 spoken words`)
     * `ultra-slow-motion suspension` (selective time-dilated apex when earned — `0 spoken words`)
     * `natural real-time speed` (mandatory for any shot with spoken dialogue and for the final composed settle beat).
4. **Dialogue Protection & Clean Terminal Keyframe Landing (`Laws D1–D6` & Zero Tail-Cut Law)**:
   - Never place spoken dialogue inside a `1.5s–2.5s` high-speed blur/impact cut (which ruins both lip-sync and combat motion).
   - Whenever a character speaks a setup, rescue, or checkmate line, allocate a **`3.2s–4.5s` decelerated window at `natural real-time speed`** (using `static camera` per `Law D1`, a **rationed Native Exclamation Trigger** per `Law D2` — never on a calm checkmate line — and an **Expressive Vocal-Behavior Tag** per `Law D3`), and ensure the clip ends with either a **wordless final settle beat (`0 spoken words`)** or a **`0.8s` silent closed-lip tail buffer (`Law D5`)** in a **Clean Composed Landing Pose** free of wild mid-swing blur for `TH1/TH3` `Last Frame` extraction.

---

## 📋 5. ILLUSTRATIVE MULTI-TOPOLOGY EXAMPLES (SHOWING HOW DIFFERENT SCENES DEMAND DIFFERENT STRUCTURES)

> ⚠️ **NOTE**: These examples illustrate **how different dramatic intents produce completely different shot topologies** (`2-Shot Continuous Inertial Clash` vs. `5-Shot Asymmetric Chase & Ambush` vs. `8-Shot Rapid-Cut Duel / Montage`). **Never copy them as rigid templates** — always derive shot count, durations, and kinetic levers from the active scene!

### Example 1 — Topology 1 (`2-Shot Continuous 3A Action-Game Inertial Clash + Settle` · `15.0s: 12.0s Unbroken Inertial Take + 3.0s Composed Settle`)
*Use when the user wants an unbroken, immersive 3A action-game camera (`Black Myth / Sekiro` feel) that dynamically time-ramps across a continuous combo without cutting every 1.5 seconds:*
```text
Style: High-end 3D Semi-Real Xianxia CG animation, unbroken AAA action-game inertial follow camera work, strong directional motion blur on high-speed blade trajectories paired with crisp internal time-ramp hit-stop pauses, high-contrast nocturnal storm lighting, satin-matte skin and armor finish with zero plastic doll sheen.

[context]:
Ancient stone Wind Bridge suspended between misty mountain peaks <<<Image 1>>> (fully_preserved - same architectural layout, weathered stone parapets, cracked flagstones and lighting throughout), stormy twilight. Whipping mountain wind driving cold mist across the wet stone bridge deck, carved stone railings, and cool moonlight piercing through dark storm clouds.

[subject]:
Lin <<<Image 2>>> (fully_preserved - same female face, slender feminine body proportions, delicate wrists, long tapering fingers, hair color, makeup and outfit throughout; natural head, eye, expression, hand and body movement.): A graceful woman crouched in a coiled sword-draw stance at the end of the stone Wind Bridge, her slender right hand gripping the silver longsword while her left hand remains empty, with silver-white moonlight luminescence, crackling cyan-white electric arcs, and cold-white calligraphic dry-brush slash streaks tightly clinging and physically adhered to her flowing garment hems and sword blade, fierce gaze locked on Mei — the only Lin in frame.
Lin's skin, hands and makeup: fully_preserved - flawless jade-porcelain matte skin across her face, neck, and slender feminine hands, with delicate wrists, long tapering fingers, refined classical eye definition, crisp eyelashes, luminous moist eyes, and classic vermilion-rose lips; no rough masculine hands, no thick knuckles, no oily sweat shine, not plastic, not waxy.
Mei <<<Image 3>>> (fully_preserved - same female face, slender feminine body proportions, delicate wrists, long tapering fingers, hair color, makeup and outfit throughout; natural head, eye, expression, hand and body movement.): A poised woman standing at the center of the stone Wind Bridge opposite Lin, her slender right hand gripping the dark heavy saber while her left hand remains empty, with thick black-crimson miasma aura and glowing dark-gold embers tightly coiled and physically adhered across her armor plates and heavy saber blade, cold piercing eyes fixed on Lin — the only Mei in frame.
Mei's skin, hands and makeup: fully_preserved - flawless jade-porcelain matte skin across her face, neck, and slender feminine hands, with delicate wrists, long tapering fingers, sharp classical eye definition, crisp eyelashes, and deep crimson matte lips; no rough masculine hands, no thick knuckles, no oily sweat shine, not plastic, not waxy.

[prop]:
Silver longsword <<<Image 4>>> (fully_preserved - same shape, material, surface finish and proportions throughout): Gripped in Lin's slender right hand at 00:00 — the only silver longsword in frame.
Dark heavy saber <<<Image 5>>> (fully_preserved - same shape, material, surface finish and proportions throughout): Gripped in Mei's slender right hand at 00:00 — the only dark heavy saber in frame.

[sound]:
Continuous unbroken 3A combat acoustics: explosive stone-cracking launch, rushing wind, three rapid metallic blade clashes with crackling cyan lightning and dark-gold ember bursts, a brief time-ramp bass hum on the mid-air parry, and a heavy stone shockwave landing. Strictly zero background music and zero spoken dialogue.

Shot 1 (00:00-00:12.0) - Dynamic medium-wide tracking shot, unbroken AAA inertial chase camera targeting Lin, whipping behind her and orbiting the clash with Mei, blistering whip-fast speed
The inertial camera rockets forward directly behind Lin's back as she shatters the wet stone tile and lunges into Mei, snapping into a split-second time-ramp impact pause as Lin's silver longsword and Mei's heavy saber lock in a violent burst of surface-adhered cyan electric arcs and dark-gold embers. Driven by the rebound momentum, the camera whips laterally around both fighters as Lin unleashes a blurred flurry of cold-white calligraphic dry-brush slashes against Mei's black-crimson saber parries before both warriors streak past each other across the cracking stone bridge.

Shot 2 (00:12.0-00:15.0) - Low-angle medium close-up, slow settling frame targeting Lin with Mei in the background, natural real-time speed
Lin slides to a balanced halt in the foreground with her silver longsword lowered in her slender right hand, while the clinging cyan-white electric arcs along her blade and garment hems gently subside into the drifting bridge mist.

Master-level cinematography and composition, unbroken AAA action-game camera inertia, crisp internal time-ramped combat pacing, atmospheric sound design.
Strict visual consistency: maintain 100% identical facial features, slender feminine hand proportions, jade-porcelain matte skin shader, hair color, makeup, exact outfit, and exact weapon design from the reference images across all shots without morphing or wardrobe changes.
Do not generate duplicate props or utensils, rough masculine hands on female characters, floating detached VFX, sluggish unintentional slow-motion, glossy plastic doll sheen, subtitles, dialogue text, titles, timestamps, or any written text anywhere in the video. Do not generate spoken dialogue, lip movement matching speech, or voiceover.
```

### Example 2 — Topology 2 (`5-Shot Asymmetric Chase, Hard Trap Stop & Ambush` · `15.0s: 3.5s–4.0s–2.3s–3.2s–2.0s`)
*Use when a scene needs a psychological snap-freeze, a sustained `4.0s` unbroken tracking sprint, an abrupt trap halt, and a spoken hunter checkmate:*
- `Shot 1 (00:00-00:03.5)` [`Close-up, side angle targeting Elena, natural real-time speed`]: False calm shatters into panic + short whispered line (`"Oh god... I'm sorry."`).
- `Shot 2 (00:03.5-00:07.5)` [`Wide inertial tracking follow shot targeting Elena, blistering whip-fast speed`]: Full-speed flight down the wet brick alley with directional motion blur and puddle splashes clinging to her boots (`0 dialogue`).
- `Shot 3 (00:07.5-00:09.8)` [`Wide shot transitioning to fixed frame targeting Elena, explosive real-time speed`]: Hard braking skid as crimson runes ignite and adhere tightly across the wet asphalt beneath her soles (`0 dialogue`).
- `Shot 4 (00:09.8-00:13.0)` [`Medium shot, static rear angle targeting Dante, natural real-time speed`]: Elena spins into Dante blocking the road `(No objects should appear in the character's hands)` + calm checkmate line with no interjection (`"Miss, you seem lost."`).
- `Shot 5 (00:13.0-00:15.0)` [`Medium close-up, static OTS from behind Dante targeting Elena, natural real-time speed`]: Wordless dread recoil as the rune ring seals (`0 dialogue`).

### Example 3 — Topology 3 (`7-to-9 Shot Staccato Rapid-Cut Montage / Blitz` · `15.0s`)
*Use when the scene's dramatic essence is a high-frequency multi-angle blitz (e.g., an 8-cut multi-angle blade exchange, a 7-cut split-second chandelier rescue, or a 9-cut culinary whip-montage):*
- Each `1.5s–2.0s` rapid cut frames **1 single focused action and surface-adhered impact** with **`>45°` camera angle/scale jumps** (`ECU Side ➔ Top-Down Overhead ➔ Low-Angle Whip-Push ➔ Diagonal Macro Impact ➔ Selective 2.0s Time-Ramp Apex ➔ Crisp Settle`).
- *(For culinary scenes, enforce the 4-Phase Culinary State-Transformation Rule: `[context]:` holds ONLY the kitchen's fixed architecture and built-in appliances; the raw ingredient, the empty serving plate and every utensil are assigned to the cook in `[subject]:` (or `[prop]:` for a Tier-1 item) at `00:00` $\to$ raw prep $\to$ thermal searing contact bridge $\to$ fully cooked/steaming active cooking $\to$ plated steaming finish, with the food's state written shot by shot + `Strict culinary state progression: ...` footer).*

---

## 🛡️ 6. SAFETY & OUTCOMES (PLATFORM-SAFE ACTION)

- **Hard Constraints** (`workflow.md` §2.11): zero gore, zero blood spray, zero dismemberment, zero graphic violence and **zero on-screen death**. Under-18 characters never fight, are never threatened with a weapon and are never in physical danger on screen (Minor Protection Protocol, `workflow.md` §2.7).
- **Outcomes** (choose per the project's `fatality_policy`, positive and zero fatalities by default): **knockout · disarmament · escape · capture · surrender · stalemate**. An off-screen death is possible only when the user enabled it, and is shown by consequence, never by the act. Every fight carries a **moral turn** (`0d` §6, §10): force protects someone, the victor shows restraint or mercy to a beaten opponent, and the camera never lingers on suffering or gloating.
- **Safe visual proxies for force**: a weapon knocked spinning from a hand, an armor plate cracking, a shockwave fracturing the ground, a fighter driven to one knee, breath fogging, sweat and rain spray, dust bursting from a wall — never wounds.
- Weapons stay in a **ready or lowered** position at the landing pose; no weapon is ever pointed at a bystander, child or the camera.

---

## 🔁 7. HANDOVER, SAVE & AUDIT

**Code Block 2 — Kinetic Handover State** (delivered after every Code Block 1):
```text
[Diegetic Foley Soundscape]:
Room/terrain tone + timestamped impacts, footsteps, engine or tool sounds tied to Shot 1..N.

[HANDOVER STATE AT 00:10.0 (or 00:15.0)]:
- Proper_Name_A: [landing pose relative to a landmark, which hand holds what, gaze, breath / exhaustion, visible strain or minor injury (never wounds)]
- Proper_Name_B: [same fields]
- Weapons & Props: [state (State 0 / 1 / 2), position or hand custody, any broken fragments renamed (`the sword` ➔ `the broken sword hilt`)]
- Terrain: [what changed — cracked flagstones, overturned cart, puddles, smoke drifting]
- Motion Vector: [screen direction of the last movement and where the next scene's motion continues]
- Outbound Continuity Reference Case for Scene N+1: [TH1 / TH2 / TH3]
```

**Save & audit**: save Code Block 1 as `output/<slug>/prompts/ep-NN-scene-KK.md` and run `python engine/prompt_audit.py <file>`; fix every `ERROR` before presenting the scene (`workflow.md` §9.3).

---

## ✅ 8. COMBAT PRE-FLIGHT (BEFORE EVERY PROMPT)

1. **Stakes**: what does this fight or chase win or lose, and what changes irreversibly?
2. **Turn**: are the plan ➔ failure ➔ improvised turn beats present?
3. **Topology**: was the shot count chosen from the scene's intent (long take / asymmetric / rapid-cut), not by habit?
4. **Levers**: are effects bound to host surfaces, the camera inertial, motion blur permitted on fast extremities, and a time-ramp or hit-stop placed at the impact?
5. **Dialogue**: is every spoken line in a decelerated `3.2s–4.5s` static shot at `natural real-time speed`, with interjections rationed?
6. **Landing**: does the clip end on a clean composed pose (no mid-swing blur) ready for the next scene?
7. **Safety**: zero gore, zero on-screen death, no minor in danger, outcome per `fatality_policy`?
8. **Separation**: are all weapons, tools and ingredients owned by characters in `[subject]:` / `[prop]:` and absent from `[context]:`?
9. **Handover**: is Code Block 2 filled (poses, weapon states, terrain, motion vector, TH case)?
10. **Audit**: did the saved prompt pass `engine/prompt_audit.py` with zero `ERROR`?

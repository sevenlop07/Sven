# studio.md: building in Roblox Studio (v4, 2026-11-14)

the creator's call on 2026-11-14: build the episode **in Roblox Studio, driven by Claude**, with free Creator Store assets, and make it look as good as the reels he sends. This file is the Studio route. `blender.md` stays the fallback.
Working example: `your project folder ` (96 animated shots, 4,462 frames). The kit is copied in `studio_kit/`.

## 1. How Claude drives Studio (free, local)
- Studio has a built-in MCP server: `/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP`. Tools used: `execute_luau` (Edit), `screen_capture`, `upload_image`, `search_asset`, `insert_asset`, `list_roblox_studios`.
- `studio_kit/bridge.mjs` runs on the Mac, launched from a `.command` file. It reads `queue/*.json` jobs and writes `done/*.json`. Its `render` job loops frames: execute a template with `{{F}}`, then `screen_capture` to `<out>/<frame>.png` (the data is JPEG).
- `rb.py lua file.lua` runs Luau. `rb.py cap out.png` captures.
- **Studio can close by itself**, for example when an update installs. On "No Roblox Studio instances are connected": reopen Studio (Baseplate template), write the new id to `studio_id.txt`, re-insert the library with `ins.py`, run `MT.cleanLib`, and reload the libs in order: faces, lib, lib2, lib3, hair, lib4, lib5, lib6, cloth, lib7, lib8, times, shots. Keep the asset list (name:id) in the project notes.
- After `screen_capture`, the camera is `Fixed`. **Set `CameraType = Scriptable` before every camera move**, or the move is ignored.

## 2. Picture quality (the #1 reason the first cut looked bad)
- `screen_capture` returns the viewport. The width is capped at 1920 px, and the height is whatever the viewport has. A centre 9:16 crop of a landscape capture is only about 450–590 px wide, so it looks blurry when stretched to 1080. **Never ship a centre-crop render.**
- **Tiled capture (use this):** `MT.frameTile(id, F)` renders each frame twice from the same camera centre: pitched up by V/4, then down by V/4, each with FOV V/2 + 6°. `stitch.py` joins the two exactly (a pure rotation is a homography, so there is no parallax and no seam) into a true 1080x1920 frame. It costs 2 captures per frame, about 1.2 s per capture.
- **4K (2160x3840):** `tiles4k.py` plans 4 pitched rows per frame from `fov.json` (each tile ≈84 % of native 4K, so it's sharper than any upscale), `render4k.py` queues them (`MT.frameTileN`), `stitch4k.py` feathers them together, and `join_4k.py` makes the 4K master, an HD copy for Studio Preview, and a phone preview. That's 4 captures per frame, about 3.6 h for a 4,462-frame episode. Start it before bed.
- Face decals render at about 256 texels in Studio, so in 4K close-ups the ink edges show small steps even from 1024 px uploads. A SurfaceGui face doesn't fix it: the flat plane sits behind the head mesh and the face disappears. Keep decals; upload faces at 1024 (`faces_hd/`) anyway.
- Before rendering, size the viewport: Studio full screen, Properties panel open, **Command Bar closed** (Window > Script > Command Bar). Aim for a viewport about 950x520 pt, so the capture isn't downscaled (≤1920 px wide) and is as tall as possible.
- `MT.quality()`: `EditQualityLevel` and `QualityLevel` = Level21, `MeshPartDetailLevel` = Level04, `EagerBulkExecution` = true.
- Lighting: `LightingStyle = Realistic`, `PrioritizeLightingQuality = true`. Light Atmosphere and Bloom only. Preload face and clothing images before the first frame (`ContentProvider:PreloadAsync`), or the first frames come out blank.

## 3. Characters that look like real Roblox (not blocks)
- Use a real **R6 character**: parts named `Torso`, `Head`, `Left Arm`, `Right Arm`, `Left Leg`, `Right Leg` (1x2x1), plus a `Humanoid` (DisplayDistanceType None, health off), a classic `Shirt` and `Pants`, and our face decals. Parts stay anchored; we place every part each frame ourselves. No sleeve or shoe blocks: the clothes draw them.
- **Clothes:** make our own 585x559 templates (`make_clothes.py`). Colours are baked in, with shading, collars, hoodie pocket and strings, stripes, v-neck, suit and tie, jeans seams, shoes. Upload them with `upload_image` (free, your own account) and keep the ids in `cloth_ids.json`. Every cast member gets a different style; the crowd mixes tee, hoodie, collar and stripe.
- **Head = standard R6 proportions, scaled the same on every axis** (`MT.HEAD = 1.25`: part (2,1,1)×H, SpecialMesh Head 1.25, centre 0.5×H above the neck). Never stretch the head unevenly (the old 2.0×1.75×1.8): hair can't fit a stretched head and sinks into it.
- **Hair = Creator Store accessories at the same scale k = H**, placed by their own `HairAttachment` against the head point (0, 0.6×k, 0). Then hair sits exactly as it does in the game, with no sinking and no floating. To dye hair, set the mesh colour and clear TextureId.
- **Accessory offset maths:** handle = head × HeadPoint × (HandleAttachment)⁻¹, and (T(p)·R)⁻¹ = R⁻¹·T(−p): rotate first, then translate. The reverse order looks fine for hairs whose attachment has no rotation, but shifts hairs with a 180° attachment (`hair_kardi`, `hair_fluffy`) about 0.6 studs, so the back of the scalp shows. Check every new hair from the front and the back on a test row before you use it.

## 4. Nothing goes through anything (hard rule)
Real objects can't share space. `lib8.lua` enforces it automatically, and every episode must pass it:
1. **Per shot, at build (`MT.resolve`, runs after every `def.build`):**
   - Arms out of their own torso, nearby props and other people: search small pose changes on the forearm half of the arm (the shoulder joint is allowed to overlap).
   - Then push characters apart (the crowd moves for the cast; cast against cast moves half each) and away from props. A lying character is lifted out of the bed or floor.
   - Caps: crowd 3 studs, cast 1.5 studs. Bigger moves mean the shot itself is wrong; fix the shot.
2. **Per frame (`MT.frame` guard):** if idle sway pushes an arm into something, that arm keeps its clean base pose.
3. **QA scan before render (`_c.lua` pattern):** every shot at its first, middle and last frame, with `MT.clips()` (each body part shrunk by 0.15 studs, so touching is OK and passing through is not). Hair-handle boxes are ignored, because mesh boxes are bigger than the hair. Fix whatever is left by hand.
- **Spacing:** R6 shoulders are 4 studs wide. Side-by-side people need ≥4.4 studs between centres, and rows ≥3.3 studs apart. The old 2.6-stud crowd grid put everyone inside each other.
- **R6 arms can't cross the chest** (no elbows). Hug-self is arms forward (75°, 5° across); cover-face is (110°, 5°, 20° out). Hugs between two people are arms around the shoulders, never through the torso.
- Feet on the floor: `MT.floating()` reports anyone standing more than 0.15 studs above or below the surface under them.

## 5. Physics that looks real
- Thrown things fly a parabola with spin (`MT.toss`). Dropped things fall with gravity, then do 2 bounces losing 60 % each (`MT.drop`). Landings get a short settle (`MT.settle`). Game gravity is 196.2 studs/s², but use about 60 so the arc reads at 30 fps.
- Held props follow the hand (`rig.extra` on `armR`/`armL`). Nothing floats or sticks unless it's held.
- Walks: feet plant on the ground, legs swing about ±18°, and the body moves at walking speed (about 6–8 studs/s). Nobody slides.
- Water: a character "in" water stands on the riverbed, and the water surface hides the legs. Mark beds, rugs, water, riverbeds and sand as soft surfaces in the clip check.

## 6. Sets
- Use free Creator Store models (`search.py`, priceFilter free; `ins.py` to insert; `MT.clean` strips scripts, sounds, prompts, Humanoids, particles, fire and smoke). Big tree clusters (`trees_oak` is 40+ studs wide, `trees_pine` about 60) go far behind the action, never near a camera path.
- Check every camera for walls, tree clusters and foreground hair on a check sheet (`checks.sh id:frame …`) before any full render.

## 7. Order of work
build libs → `MT.quality()` → clip scan (§4.3) → check sheet of every shot → `fov.json` (`MT.shotFovs()`) → `render2.py <all ids> force` → `stitch.py <ids>` → join (crop off, frames are already 1080x1920) → Studio Preview with voice, music and captions. A full 96-shot episode is about 9,000 captures, roughly 3 hours on the Mac. Tell the user the time before you start.

## 8. The ref look, v2 (the user, 2026-11-15: "the expressions are still off… I want the video quality like this")
What the top refs do, measured on 3 frames (Simon Says, In this town I'd cry everyday):
- **Faces are bold and big:** thick black ink outlines, large white eyes with pupils and glints, heavy angled brows, mouths with a dark inside, teeth and tongue, plus tears, sweat drops, blush and anger marks. Features fill about 70 % of the face. Our first atlas (thin lines, small dots) read as "off". `studio_kit/make_faces_v2.py` draws 24 faces this way at 4x, then shrinks them to 1024 px. Sad and worried brows: the inner ends go **up**. Angry: the inner ends go **down**. Eyes sit at about 47 % of the image height, so bangs don't hide them.
- **Hair must not cover the eyes.** Bangs over the eyes kill the new faces. Swap the hair (dad got `hair_black_messy`, mom got `hair_long_bangs`) and check every cast close-up.
- **Cameras: close, low, wide.** Close-ups at 0.82× the distance, the camera 0.55 studs below eye level looking slightly up, 28 mm (`lib9.lua` wraps `MT.cu`). The character fills the frame.
- **Colour and depth:** saturation +0.12, contrast +0.06, and a soft background blur (DepthOfField: focus on the subject, in-focus radius 0.7×distance, FarIntensity 0.22).
- **Clothes:** fabric folds and grain on every template (`make_clothes.py` `fabric()`).
- New uploads can show blank for a few minutes until Roblox approves them. Wait and re-check before rendering.

## 9. v2.1: trained on "That Guy Animation" (Claude + Roblox Studio stories, free), 2026-11-15
Source: youtu.be/YhjjHh6Y2xc ("How I make viral Roblox stories with Claude for free", 273 s, watched frame by frame: `Youtube video ref/links/ref_v21/`). Their free prompt runs in 8 steps with stops for the user. Here is what we take, merged with our own pipeline.

### 9.1 Story (overrides where it disagrees with script.md)
- **The rule must be visible.** "In this town, …" plus something that shouldn't be true, and you can see it on a person or in the street (a kid shrinks when he lies, a door changes colour, a bridge appears). If it needs explaining, it's the wrong rule. Pitch 10 visible rules, keep the one that makes you ask "wait, what happens then?"
- **Shape:** rule → life under the rule (the town cheers it) → one grandparent's story → the one kid who notices → something arrives that makes the rule cruel → the narrator does one clever physical thing → the twist turns the first line around → **end on the next danger.** No moral, never "and that's when I learned". People share cliffhangers, not lessons.
- **Plant 3 small details early, all of which pay off:** something the kid has to repeat, something odd the kid noticed, something a grandparent once said.
- **Length:** 20 s, 60 s or the full ~2.5 min. Longer gets more watch time per view (room to build the town, plant details and land the twist).
- **The rule is written big on screen in the first second**, so it works without sound.
- **Stop for the user's OK on the script** before building anything.

### 9.2 Build order
1. **Grey blockout** of every location (ground, buildings, people as grey blocks). Take a high view and an eye-level view, and check the layout before any detail.
2. **World:** build at the origin with streaming off. Terrain for a strong landform. Free textured buildings in **one consistent style**, a main street with landmarks, and dense dressing (props, lamps, trees, grass, fences). **Interiors are real rooms:** a bed with a fabric blanket and pillows, a lamp, a plant, string lights, patterned wallpaper, a rug, a desk with books.
3. **Light:** low warm sun, hard visible shadows, faint sun rays, distant layered mountains, turquoise water. At night: blue moonlight plus warm lamps that are visible in the room.
4. **Cast:** live **R15 avatars from HumanoidDescription**. `Players:CreateHumanoidModelFromDescription` works in Edit mode (verified 2026-11-15). Dress everyone differently with free classic shirts, pants and accessories. Give each one a readable accessory (hat, hair, glasses) and a runtime face. If the rule is visible (a number over each head), show it on everyone.
5. **Animation = real Roblox animations.** Load them on the Animator, `Play()` them, then call `animator:StepAnimations(1/30)` once per captured frame in Edit mode. That's frame-exact and works with the tiled 4K capture (verified with the R15 wave animation 507770239). Wait until `track.Length > 0` before stepping (it loads asynchronously). Use the default R15 ids (idle, walk, run, wave, point, cheer, laugh, sit). Check each one loads before use. Keep our own pose code only for poses no animation has.
6. **Shot plan:** about one shot per second (at least one per line), mostly short. Mix pushes and pulls with an occasional tilt. Change the place or the subject often. **Something moves in every shot.** Text and signs go in the **top third** of the frame. Readable props carry the story (a glowing "8:59" clock, a teacher's nameplate, "Homework:" on the chalkboard).
7. **Their capture vs ours:** they roll the client camera 90° in Play and screen-record the landscape monitor (a quick trick: the 16:9 screen holds a 9:16 frame). We keep Edit-mode tiled capture (native 1080x1920 or 4K, frame-exact, no recorder permissions). Same idea: never crop a landscape frame.
8. **Proof:** check screenshots of every shot, fix problems in one round, then render. Use free assets only, delete every inserted script, never publish.

### 9.3 Edit
Warm storyteller voice. Captions **one word at a time** (white, bold, black outline; key words yellow), a few SFX, vertical export. No captions or music inside the Studio footage.

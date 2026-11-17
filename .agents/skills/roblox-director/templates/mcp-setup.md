# Roblox Studio MCP + Claude Code: setup and first tests

> **v2 note (2026-11-14):** old Roblox Studio route, reference only. Blender setup is in `../SETUP.md`.


Source: Roblox's MCP docs (create.roblox.com/docs/studio/mcp, checked 2026-11-14) and the production research. The MCP server is **built into Roblox Studio**. Transport is **stdio**, so Claude Code must run **locally on the same Mac**: the Terminal CLI or the desktop app's Code tab, never a cloud session. Don't install the archived `studio-rust-mcp-server` (archived Apr 2026) or community servers; they aren't needed.

## Setup (about 10 minutes, once)
1. Update Roblox Studio (Creator Dashboard). Check Activity Monitor: Studio's **Kind** must be **Apple**.
2. Open any place (a new Baseplate is fine). The MCP only works while Studio is open with a place loaded.
3. Studio: **Assistant → … → Manage MCP Servers → turn on "Enable Studio as MCP server"**.
4. Studio: **Assistant Settings → MCP Servers → Quick connect → Claude Code** (turn it on).
5. If Quick connect doesn't work, in Terminal:
   ```bash
   claude mcp add --transport stdio --scope user Roblox_Studio -- /Applications/RobloxStudio.app/Contents/MacOS/StudioMCP
   ```
6. Quit and restart **both** Studio and Claude Code (setup changes need a restart).
7. Check: `claude mcp list` shows `Roblox_Studio` connected, and Studio shows a green indicator for the connected client.
8. In Claude Code, first message: *"Call list_roblox_studios and tell me the studio_id."* Every MCP call needs that id.
9. Studio → File → Studio Settings → Rendering: **Editor Quality Level 21**, **Mesh Detail Level00** (effects may not show otherwise).

What it can and can't do: pipeline.md step 0.2. The two limits that matter most: **no video recording** (OBS records) and **`generate_animation` is R15-only, max 10 s** (no use for R6 acting).

---

## Test A: classroom from free models + the sad preset (paste into Claude Code)

```text
Use the Roblox Studio MCP. Call list_roblox_studios first and use that studio_id. Keep replies short.
1. search_asset in the Creator Store for "classroom" (models). Skip the common free school map with blue lockers and the bulletin-board classroom (lots of Roblox story channels use it). List the top 3 results (name, asset ID, creator) and insert_asset the first one that is not that map. Put it under a Model named "Set_Classroom" at the origin.
2. execute_luau (Edit): inside Set_Classroom, print any script line containing "require(", then destroy every Script, LocalScript, ModuleScript and Sound. Print how many of each you removed.
3. Create a ModuleScript ReplicatedStorage.LightingPresets whose Source is the exact contents of this skill's templates/lighting-presets.lua (read the file; set .Source with execute_luau, or use multi_edit if that is blocked).
4. execute_luau: local P = require(game.ReplicatedStorage.LightingPresets); P.cleanFreeModelFx(); P.apply("sad"). Then find one ceiling lamp or window part in the set and call P.practical on it (keepLook = true if it is a window).
5. screen_capture once, camera in a back corner of the room about 5 studs high, looking at the teacher's desk. Tell me the capture's pixel size and how many seconds it took.
6. save_place.
```
Pass: the set is in, 0 scripts left, the room reads cool and soft with one visible light source, no errors in `get_console_output`.

## Test B: R6 rig + own face decals + a face swap (this is the 2-minute decal test)

Have 4 PNGs ready (512×512, transparent): `eyes_open.png`, `brows_neutral.png`, `mouth_closed.png`, `mouth_O.png`.

```text
Use the Roblox Studio MCP (same studio_id). Keep replies short.
1. execute_luau (Edit): make an R6 rig named "Hero" with
   game.Players:CreateHumanoidModelFromDescription(Instance.new("HumanoidDescription"), Enum.HumanoidRigType.R6),
   parent it to workspace at (0, 3, -6), anchor its HumanoidRootPart, and give it non-default body colours
   (head 255,204,153; torso 230,90,60; legs 40,40,60). If that call fails, stop and tell me to click
   Avatar > Rig Builder > R6 > Block Rig, then rename that rig "Hero" and continue.
2. Remove the Head's default "face" decal.
3. Upload my 4 PNGs with upload_image: <paste the 4 file paths>. If upload_image can't take local files, tell me;
   I'll use Asset Manager > Bulk Import and paste the IDs.
4. On Hero.Head add 3 Decals, Face = Front: "Eyes" (ZIndex 1, eyes_open), "Brows" (ZIndex 2, brows_neutral),
   "Mouth" (ZIndex 3, mouth_closed).
5. screen_capture a close-up: camera 4 studs in front of the head at head height, looking at the head.
6. execute_luau: set Hero.Head.Mouth.Texture to the mouth_O id. screen_capture again with the same camera.
7. Answer in 3 lines: do all 3 layers render? Do they line up? Does the mouth swap show in the second capture?
```

## Test C: camera + screen_capture (framing, FOV, cost)

```text
Use the Roblox Studio MCP (same studio_id). Keep replies short.
1. execute_luau (Edit): set workspace.CurrentCamera.CFrame = CFrame.lookAt(head + Vector3.new(0, 0.5, 6), head)
   where head = workspace.Hero.Head.Position, and FieldOfView = 35.
2. screen_capture with that same camera position and look-at target.
3. Same again from 3 studs away with FieldOfView = 70.
4. Report: the pixel size of each capture, seconds per capture, and whether screen_capture used the FieldOfView
   I set (the FOV 35 shot should show much less background than the FOV 70 shot).
```
Pass: both captures show the hero centred; you now know the capture size, the speed and whether FOV carries over. Write all three numbers into pipeline.md (they replace UNVERIFIED notes).

---

## The 2-minute decal test (critic §4c): pass / fail and what to do

Why: Roblox migrated Classic Heads and Faces to Dynamic Heads in early 2026 (with a partial walk-back: a toggle to turn off face animation, and a promise to make classic-look heads easier for creators). A plain Decal with the user's own image on a Studio-built R6 rig is ordinary part texturing and should still render, but nobody has checked it on his Mac yet. The whole face system (look.md §7) depends on it.

| result | meaning | do this |
|---|---|---|
| **All 3 layers render, aligned, swap visible** | PASS | draw the full kit (19 PNGs per character), fill FaceLibrary |
| Decals blank | the images are still in moderation, or the IDs are decal IDs rather than image IDs | wait 5 minutes and re-capture; use the image ID (Asset Manager → right-click → Copy ID) |
| Layers flicker or the wrong one is on top | same ZIndex | set ZIndex 1 / 2 / 3 |
| Layers render but stretch or sit off-centre on the round head | the PNG canvas isn't the same for all layers | redraw all layers on one shared 512×512 canvas, part drawn in place |
| Nothing renders on the mesh head | decals blocked on the Head mesh | swap the head for a plain Block part (a blocky head) and decal that, or use a SurfaceGui (Face = Front) with 3 ImageLabels |
| All of the above fail | | one combined PNG per expression (about 20 per character, fewer combinations), on a Block head |

After it passes, also check once in **Play mode** (the shot runner swaps faces on the client): `start_stop_play`, then `execute_luau` (Client) to swap the mouth, then `screen_capture`.

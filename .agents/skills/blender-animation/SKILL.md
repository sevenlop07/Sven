---
name: blender-animation
description: Animation in Blender 5.3 - slotted/layered actions and the channelbag API, Python keyframing, F-curves, game loops with pop/hitch checks, NLA clips, pose library, mocap/BVH/Mixamo retargeting with auto bone maps, baking control rigs to export skeletons, root motion, per-clip export. Use for any keyframe, action, NLA, mocap, or animation-export task.
license: MIT
metadata:
  author: blender-agent-skills
  version: "1.2.0"
---

# Animation

The execution model is in `blender-core` (its `references/bpy-patterns.md` has verified keyframe/driver snippets). Rigs are in `blender-character-rigging`.

## 5.x data model (what changed)
- An **Action** holds **slots** (one per animated ID) and **layers → strips → channelbags → F-curves**. A single action can animate several objects (e.g. a rig and its camera) through different slots.
- Assign: `ob.animation_data.action = act`, then make sure `ob.animation_data.action_slot` is set (picked automatically when a suitable slot exists; otherwise `act.slots.new(id_type="OBJECT", name=ob.name)`).
- F-curves: `cb = anim_utils.action_ensure_channelbag_for_slot(act, slot)`, then `cb.fcurves.ensure(path, index=i, group_name=...)`. `action.fcurves` **no longer exists**.
- The simplest route is still `pb.keyframe_insert("rotation_quaternion", frame=f)`, which creates the action, slot and channelbag.

## Workflow (keyframe animation, studio style)
1. **Blocking**: key poses on every channel (`CONSTANT` interpolation, `bpy.context.preferences.edit.keyframe_new_interpolation_type`) on golden frames (contact, down, passing, up for walks).
2. **Breakdowns**: add in-betweens that define arcs and spacing.
3. **Spline**: switch to `BEZIER`, fix spacing in the Graph Editor, and clean overshoot. Auto-clamped handles avoid overshoot.
4. **Polish**: offsets/overlap (follow-through on hair, tails, cloth bones), arcs, moving holds (never a perfectly frozen character), and contact stability (feet locked with IK).
5. **Review**: MCP `look(mode="frames", frame_count=8)` or a Workbench playblast (`blender-rendering`).

## The 12 Principles of Animation (Disney) in Blender 5.3 & Pose-Calling Rules
Never snap a rig linearly from Pose A to Pose B or leave all bones starting and stopping on the exact same frame (`Dead Stop`). Enforce all 12 principles mathematically (implemented in `roblox-director/studio_kit/blender_roblox_kit.py` `snap_r15_pose` / `apply_pose_lib` / `POSE_LIB` and `blender_r15_hybrid.py`):
1. **Squash and Stretch (Center-of-Mass Compression)**: When bone scaling is disallowed (Roblox/game rigs), express squash and stretch via vertical hip displacement (`LowerTorso.location.z` `_hip_offset` `-0.02m..-0.28m`) paired with Foot IK knee flexion and spine pitch compression on jump wind-ups, impacts, and recoils.
2. **Anticipation (`2–4f` Reverse Wind-Up)**: Precede every dynamic gesture, turn, strike, or throw with a `2–4 frame` counter-move (`14%–18%` in the opposite direction + slight hip dip) before launching toward the target pose (`anticipate=True`).
3. **Staging & Camera-Sightline Corridors**:
   - **Sightline Clearance**: Never scatter foreground trees, lampposts, or props on a blind grid across the camera-to-subject ray. Reserve clear camera sightline corridors and frame silhouettes cleanly.
   - **Readable Silhouette**: Open elbows away from the ribs (`Z/roll ±10°..28°`) so arms never merge into the torso silhouette from the active camera angle.
4. **Pose-to-Pose + Straight Ahead Hybrid**: Use **Pose-to-Pose** (`Key Pose -> Extreme -> Breakdown Arc`) for intentional character acting (`POSE_LIB`), layered with **Straight Ahead** physics/procedural secondary motion (`bake_secondary_overlap` on hair/scarf bones, rigid-body/parabolic prop trajectories).
5. **Follow Through & Overlapping Action (Mandatory Kinematic Chain Stagger)**:
   - Never stop all bones on the same frame. Drive motion from the center of mass outward:
     `LowerTorso / Hips (Frame F)` → `UpperTorso / Chest (F + 1)` → `UpperArm / LowerArm (F + 2, after a +7% Overshoot at F)` → `Head / Gaze (F + 3)` → `Hair / Scarf / Cloth Secondary Bones (F + 3..4 lag)`.
6. **Slow In and Slow Out (`BEZIER` `AUTO_CLAMPED` Handles)**: Author pose transitions with `BEZIER` interpolation and `AUTO_CLAMPED` F-curve handles so limbs accelerate smoothly out of rest and decelerate into holds. Use `VECTOR` handles only at physical impact/contact frames.
7. **Arcs (Midpoint Breakdown Injection)**: Linear Euler/Quaternion interpolation between two distant poses cuts along a straight chord and clips through the chest. Always inject a **Midpoint Breakdown Keyframe (`t = 0.5`, `arc_breakdown=True`)**: add a `+4.5°` downward chin dip on head yaw turns and a `±11°` outward elbow abduction on large arm swings.
8. **Secondary Action (NLA Layered Acting)**: Combine a lower-body locomotion or weight-shift track (`Track 1: Walk IK / Idle Weight Shift`) with an upper-body emotional/conversational overlay (`Track 2: POSE_LIB / speak_emphasis_r15`) and periodic eye blinks (`every 90–105 frames`).
9. **Timing, Spacing & Moving Holds (`30 fps` Calibration)**:
   - Fast reflex / flinch / strike: `4–6 frames` (`0.13s–0.20s`).
   - Natural conversational gesture / turn: `8–12 frames` (`0.27s–0.40s`).
   - Heavy lift / exhaustion / bow: `18–32 frames` (`0.60s–1.05s`).
   - **Moving Hold (`hold_frames >= 12`)**: After landing a key pose, never freeze the character at 0 velocity; sustain a subtle `±1.5°` chest/head breathing micro-settle across the hold window.
10. **Exaggeration**: Push torso tilt, head pitch/yaw, and arm extension `15%–25%` beyond pedestrian angles so emotional intent reads immediately in Medium and Wide shots.
11. **Solid Posing (Contrapposto & Zero Twinning)**: Strictly ban symmetric mirror posing ("twinning") where left and right arms/legs share identical angles. Enforce **Contrapposto** (`LowerTorso` hip tilt/twist counter-balanced by opposite `UpperTorso` shoulder tilt/twist along an S- or C-curve Line of Action) while locking `IK_Foot.L/R = 1.0` flat to the floor (`0.000m` foot sliding).
12. **Appeal**: Assign distinct base postures (`confident_stand`, `neutral_relaxed`, `cross_arms`, `look_up_awe`, `lean_balustrade`, `combat_guard` across the 24-pose `POSE_LIB`) and distinct energy/timing scales to each character.

## Game animation rules
- **One action per clip**, named `<Rig>_<Clip>` or just `<Clip>`, with a fake user so it survives saving.
- **Loops**: first and last frames identical. Export frames 1..N and let the engine drop the duplicate, or exclude the last frame (UE/Unity "loop pose" options). An F-curve `CYCLES` modifier helps preview but **doesn't export**, so bake it. Verify with `scripts/loop_check.py -- --object RIG --action Walk [--root-motion root] [--fix]`: it reports pose **pops** (last ≠ first, per bone, in deg/m) and speed **hitches** across the seam, and `--fix` keys the first-frame values on the last frame (root travel is kept).
- **FPS**: author at 30 (or 24) and let engines resample. Set `scene.render.fps` before importing mocap.
- **Root motion**: the root bone carries the translation (and yaw). The hips keep the bob/sway. `scripts/bake_action.py --root-motion xy` moves the hips' ground motion to the root. In-place clips: the root stays at the origin.
- **Additive/overlay** clips (aim offsets, breathing) are exported as normal clips and marked additive in the engine.
- Keep the bone transform channels the engine expects. **Don't animate bone scale** unless the engine supports it (Roblox and many mobile pipelines don't).

## Bake control rig → export skeleton
```
scripts/bake_action.py -- --list
scripts/bake_action.py -- --source RIG_Body --target GAME_RIG_Body [--actions Walk Run] [--root-motion xy --hips spine]
```
This gives one baked action per clip (`GAME_RIG_Body|Walk`), cleaned, with fake users, plus one muted NLA track per clip (`CLIP_Walk`) so FBX (`bake_anim_use_nla_strips`/all actions) and glTF (`ACTIONS` mode) export every clip. The target's constraints are muted afterward so it plays the baked data; run `--follow` to drive it live again. Self-bake (IK/constraints → keys on the same rig): `--source X --target X`.

## Mocap and retargeting
- Import: `bpy.ops.import_anim.bvh(filepath=..., global_scale=0.01 if cm else 1, rotate_mode="NATIVE", update_scene_fps=True)`, `import_scene.fbx` (Mixamo, `automatic_bone_orientation=True`).
- Retarget: `scripts/retarget.py -- --source Mocap --target GAME_RIG [--map auto|map.json] [--in-place] [--name Walk]`. Each target bone gets the source bone's **world rotation change from rest** on its own rest orientation, so rolls, bone axes, Y-up/cm FBX object transforms and proportions don't matter. The hips travel is scaled by the hips-height ratio. Keys go straight into a new `TARGET|Name` action (quaternion, linear, fake user). Measured on a Mixamo-style rig (Y-up, 0.01 scale, rolled) → Rigify-named rig with 15% longer legs: 17 bones, < 0.1° error.
- The auto map understands Mixamo (`mixamorig:LeftUpLeg`), Rigify `DEF-`/`ORG-`, UE/Unity/BVH-style names, and spine chains of different lengths. Check it first with `--show-map` (`unmapped_key_parts` must be empty), and pass a JSON `{target: source}` for anything custom (fingers, props).
- **Rest poses must match** (T vs A matters most): pose the target's rest like the source's first. Then clean, add root motion, and export with `bake_action.py`.
- Clean mocap: decimate keys (`graph.decimate`, ratio 0.3–0.5), use an F-curve `SMOOTH` modifier or the Butterworth filter (`graph.butterworth_smooth`), and fix foot sliding with IK pins and then bake.
- Production retarget tools: Auto-Rig Pro (paid), Rokoko (free), and the engine-side retargeters (UE IK Retargeter, Unity Humanoid).

## NLA and pose library
- NLA: push actions down as strips (`track.strips.new(name, start, action)`) to layer/blend clips (blend type `REPLACE`/`ADD`/`COMBINE`), and use Tweak mode to edit. Strips need an action slot set when the action has several slots (`strip.action_slot`).
- The pose library (bundled `pose_library`) stores poses as **assets**: `poselib.create_pose_asset(pose_name=...)`, `poselib.apply_pose_asset` / `blend_pose_asset`. Use it for hand shapes, face poses, and a T/A rest pose.

## Shape keys and other properties
Any property can be keyed: `kb.keyframe_insert("value", frame=f)` (shape key), `mat.node_tree.nodes[...].inputs[...].keyframe_insert("default_value")` (materials, which engines usually ignore), custom props `ob.keyframe_insert('["prop"]')`.

## Gotchas
- `pb.matrix = ...` followed by `keyframe_insert` needs the right `scene.frame_set(f)` **first**, or an evaluation overwrites the pose.
- Connected bones (`use_connect`) can't translate. Hips/pelvis must be unconnected from the root.
- `bake_action` with visual keying reads **evaluated** poses, so constraints, IK and drivers are all captured. Mute the target's own constraints afterward (the script does), or they keep overriding the keys.
- Quaternion vs Euler: game bones should use `QUATERNION` (no gimbal lock, smooth slerp). Euler is fine for single-axis controls. Don't mix modes between keys. 5.3 converts existing animation: `pose_bone.convert_rotation_mode("QUATERNION", bake=False)` (also on objects) or `anim.rotation_mode_convert(mode=...)` for the selection.
- glTF sampling: `export_force_sampling` bakes every frame (the safe default). Non-linear F-curve modifiers and drivers only export when sampled.

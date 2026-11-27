#!/usr/bin/env python3
"""
Self-test / demo for blender_roblox_anim.py (Law R-ANIM). Builds one R15 kit character, plays EVERY state in
sequence (locomotion on a real root path, the rest in place) and writes a pose-QA sheet with one frame per state.

  blender -b --factory-startup --python demo_roblox_anim.py -- <out_dir>
Then VIEW <out_dir>/pose_qa_sheet.png (row 1 front, row 2 side). Any agent changing blender_roblox_anim.py must
re-run this and look at the sheet before committing.
"""
import os
import sys

import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import blender_roblox_kit as kit  # noqa: E402
import blender_roblox_anim as rba  # noqa: E402

ASSETS = os.path.join(HERE, "..", "assets")
_args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
out = _args[0] if _args else os.path.join(kit.get_stage_dir("roblox_anim_demo"), "qa")

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.fps = 30
ch = kit.build_roblox_character("Demo", os.path.join(ASSETS, "clothes", "shirt_me.png"),
                                os.path.join(ASSETS, "clothes", "pants_me.png"),
                                os.path.join(ASSETS, "faces_storybook_toon", "neutral.png"),
                                rig_type="R15", hair_style="boy",
                                body_profile="boy_athletic", yaw_deg=90)
an = rba.RobloxAnimator(ch, fps=30)
D = 1.2
order = ["idle", "walk", "run", "sprint", "jump", "fall", "land", "crouch", "sit", "pickup", "cheer", "wave", "point",
         "clap", "talk", "shock", "scared", "sad", "angry", "think", "punch", "kick", "hit", "dance", "look_around",
         "lie", "pose"]
speeds = {"walk": 2.24, "run": 4.48, "sprint": 6.3}
keys, x, t = [(0.0, (0.0, 0.0), 90)], 0.0, 0.0
sample = []
for i, s in enumerate(order):
    params = {"height": 1.6} if s == "jump" else {}
    if s == "pose":
        params = {"pose": {"RightUpperArm": [-120, 40, 0], "LeftUpperArm": [-20, 60, 0], "Head": [-10, 0, 20]}}
    an.add(s, t, t + D, fade=0.15, **params)
    x += speeds.get(s, 0.0) * D
    keys.append((t + D, (x, 0.0), 90))
    sample.append(int((t + (0.55 if s == "jump" else 0.7) * D) * 30) + 1)
    t += D
an.root_keys(keys)
an.face(0, t, "happy")
an.bake(1, int(t * 30) + 1)
sc.frame_end = int(t * 30) + 1
sheet = rba.render_pose_qa(ch["armature"], sample, out, size=(150, 200))
print("[DEMO] states:", ", ".join(f"{s}@{f}" for s, f in zip(order, sample)))
print("[DEMO] sheet:", sheet)

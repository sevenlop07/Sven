#!/usr/bin/env python3
"""
blender_roblox_anim.py — Code-Rigged Roblox-Style Acting Engine for the R15 kit rig (Blender 5.2+/5.3).

WHY THIS EXISTS (Law R-ANIM)
  Human mocap (Mixamo/BVH/FBX) does NOT read as Roblox on blocky R15 parts: human twist flings offset
  box-limbs outward, human lean/elbow bends look broken, and human cadence slides feet at Roblox speeds
  (Roblox WalkSpeed = 16 studs/s = 4.5 m/s). Real Roblox animation is simple, readable pendulum motion.
  This module generates that motion procedurally, deterministically, with no external files.

WHAT YOU GET
  * 24 acting states: idle, walk, run, sprint, jump, fall, land, crouch, sit, lie, pickup, cheer, wave,
    point, clap, talk, shock, scared, sad, angry, think, punch, kick, hit, dance, look_around, pose.
  * Locomotion phase-locked to the real ground distance of the root path (zero foot sliding at any speed).
  * Timeline with crossfades, additive head-look layer, hit-stop, joint limits (no limb-through-torso).
  * Face expressions baked into the head material (keyframed node switch) — the .blend stays self-contained
    for external/cloud render workers (no Python frame handlers needed).
  * Pose QA renderer: character-locked front + side views composed into one sheet (inspect before rendering!).

AXES (all joint params are degrees, Roblox-"Transform"-style, relative to the parent part, in the character's
rest axes; the kit character faces -Y at yaw 0):
  rx  limbs hanging down: rx < 0 swings FORWARD; knees rx > 0 bend back; elbows rx < 0 bend forward.
      torso/head (pointing up): rx > 0 leans/nods FORWARD, rx < 0 leans back / looks up.
  ry  upper arms / upper legs: ry > 0 spreads OUTWARD on both sides (side sign handled automatically).
  rz  yaw about vertical: rz > 0 turns to the character's LEFT.
  "_bob" = vertical LowerTorso offset in metres (crouch / bounce).

QUICK START
    import blender_roblox_kit as kit, blender_roblox_anim as rba
    ch = kit.build_roblox_character("Alex", shirt, pants, face_png, rig_type="R15", body_profile="boy_athletic")
    an = rba.RobloxAnimator(ch, fps=30)
    an.root_keys([(0.0, (0, 0), 90), (4.0, (9, 0), 90), (7.0, (9, 0), 90), (13.0, (45, 0), 90)])  # t, (x, y) m, yaw
    an.add("walk", 0.0, 4.0)
    an.add("look_around", 4.0, 6.0)
    an.add("shock", 6.0, 7.0, fade=0.12)
    an.add("run", 7.0, 12.85, fade=0.25)
    an.add("jump", 12.85, 14.25, height=1.8)          # anticipation -> air -> land, root lift automatic
    an.add("cheer", 14.25, 20.0)
    an.look(4.3, 5.9, yaw=[0, 55, -55, 0])             # additive head sweep
    an.face(0, 4.2, "neutral"); an.face(4.2, 7, "scared"); an.face(14.3, 20, "happy")
    an.hit_stop(14.39, frames=2)
    an.bake(frame_start=1, frame_end=600)
    rba.render_pose_qa(ch["armature"], [30, 200, 300, 400, 520], "/tmp/qa")   # LOOK at the sheet before final render
"""
import math
import os

import bpy
from mathutils import Euler, Quaternion, Vector

BONES = ["LowerTorso", "UpperTorso", "Head", "LeftUpperArm", "LeftLowerArm", "RightUpperArm", "RightLowerArm",
         "LeftUpperLeg", "LeftLowerLeg", "RightUpperLeg", "RightLowerLeg"]

# joint limits (deg) — keep blocky parts out of each other
LIMITS = {
    "LowerTorso": ((-95, 95), (-90, 90), (-45, 45)),   # whole-body root: wide so lie/fall poses work
    "UpperTorso": ((-35, 50), (-20, 20), (-50, 50)),
    "Head": ((-45, 45), (-25, 25), (-85, 85)),
    "UpperArm": ((-185, 75), (3, 130), (-60, 60)),
    "LowerArm": ((-145, 0), (-20, 20), (-30, 30)),
    "UpperLeg": ((-120, 55), (-8, 60), (-35, 35)),
    "LowerLeg": ((0, 150), (-5, 5), (-10, 10)),
}

WALK_STUDS = 8.0 * 0.28     # nominal walk speed (m/s) — Roblox-ish casual walk
RUN_STUDS = 16.0 * 0.28     # Roblox default WalkSpeed 16 studs/s


def clamp(x, a, b): return max(a, min(b, x))
def smooth(x): x = clamp(x, 0.0, 1.0); return x * x * (3 - 2 * x)
def lerp(a, b, s): return a + (b - a) * s


def zero():
    p = {b: [0.0, 0.0, 0.0] for b in BONES}
    p["_bob"] = 0.0
    return p


def blend(a, b, w):
    if w <= 0.0: return a
    if w >= 1.0: return b
    out = {}
    for k in a:
        if k == "_bob":
            out[k] = a[k] + (b[k] - a[k]) * w
        else:
            out[k] = [a[k][i] + (b[k][i] - a[k][i]) * w for i in range(3)]
    return out


def both(p, part, val):
    for s in ("Left", "Right"):
        p[s + part] = list(val)


def _keys(keys, t):
    """Piecewise smoothstep interpolation of [(t, tuple), ...]."""
    if t <= keys[0][0]: return keys[0][1]
    if t >= keys[-1][0]: return keys[-1][1]
    for i in range(len(keys) - 1):
        if keys[i][0] <= t <= keys[i + 1][0]:
            w = smooth((t - keys[i][0]) / max(1e-6, keys[i + 1][0] - keys[i][0]))
            return tuple(lerp(a, b, w) for a, b in zip(keys[i][1], keys[i + 1][1]))
    return keys[-1][1]


# ============================================================ STATES
# signature: state(u, d, ctx) -> pose ; u = seconds since segment start, d = segment duration,
# ctx = {"phase": radians (locomotion), "amp": 0..1.2 stride scale, "params": dict, "t": absolute time}

def st_idle(u, d, ctx):
    p = zero()
    br = math.sin(2 * math.pi * u / 3.2)
    sway = math.sin(2 * math.pi * u / 7.0)
    p["UpperTorso"][0] = 1.2 * br
    p["Head"][0] = -1.0 * br
    p["LowerTorso"][2] = 2.0 * sway
    both(p, "UpperArm", [-3 + 2 * br, 6, 0])
    both(p, "LowerArm", [-10, 0, 0])
    both(p, "UpperLeg", [-2, 2, 0])
    both(p, "LowerLeg", [3, 0, 0])
    p["_bob"] = -0.004 * (1 + br)
    return p


def _cycle(phase, amp, kind):
    """Roblox pendulum gait. kind: walk | run | sprint."""
    p = zero()
    s, c = math.sin(phase), math.cos(phase)
    A, Aa, kb, ks, eb, es, lean, bob = {
        "walk": (32, 30, 6, 34, 10, 18, 2, 0.022),
        "run": (55, 62, 14, 78, 48, 30, 9, 0.045),
        "sprint": (65, 75, 18, 95, 70, 25, 16, 0.055),
    }[kind]
    A, Aa = A * amp, Aa * amp
    k = max(amp, 0.2)
    p["LeftUpperLeg"] = [-A * s, 2, 0]
    p["RightUpperLeg"] = [A * s, 2, 0]
    p["LeftLowerLeg"][0] = (kb + ks * max(0.0, c)) * k
    p["RightLowerLeg"][0] = (kb + ks * max(0.0, -c)) * k
    p["LeftUpperArm"] = [Aa * s, 5, 0]
    p["RightUpperArm"] = [-Aa * s, 5, 0]
    p["LeftLowerArm"][0] = -(eb + es * max(0.0, -s)) * max(amp, 0.3)
    p["RightLowerArm"][0] = -(eb + es * max(0.0, s)) * max(amp, 0.3)
    p["UpperTorso"] = [lean * amp, 0, (6 if kind != "walk" else 4) * s * amp]
    p["LowerTorso"][2] = -(4 if kind != "walk" else 3) * s * amp
    p["Head"][0] = -(lean * 0.6) * amp
    p["_bob"] = -bob * abs(c) * amp
    return p


def st_walk(u, d, ctx): return _cycle(ctx["phase"], ctx["amp"], "walk")
def st_run(u, d, ctx): return _cycle(ctx["phase"], ctx["amp"], "run")
def st_sprint(u, d, ctx): return _cycle(ctx["phase"], ctx["amp"], "sprint")


def _jump_keys(d):
    """anticipation 0.15 s -> air (d - 0.4 s) -> land 0.25 s; values: thigh, knee, arm rx, spread, elbow, lean, bob."""
    air = max(0.25, d - 0.40)
    t0, t1 = 0.15, 0.15 + air
    return [
        (0.00, (-10, 18, 8, 6, -18, 6, -0.02)),
        (0.15, (-38, 62, 32, 6, -20, 16, -0.10)),
        (t0 + 0.12 * air, (-8, 8, -150, 14, -12, -2, 0.0)),
        (t0 + 0.50 * air, (-62, 96, -168, 24, -18, 10, 0.02)),
        (t0 + 0.85 * air, (-24, 28, -115, 20, -14, 4, 0.0)),
        (t1, (-42, 66, -55, 18, -30, 18, -0.11)),
        (t1 + 0.25, (-10, 16, -18, 8, -16, 5, -0.01)),
    ], t0, t1


def st_jump(u, d, ctx):
    keys, _, _ = _jump_keys(d)
    thigh, knee, arx, ary, elb, lean, bob = _keys(keys, u)
    p = zero()
    p["LeftUpperLeg"][0], p["RightUpperLeg"][0] = thigh, thigh * 0.8 + 4
    p["LeftLowerLeg"][0], p["RightLowerLeg"][0] = knee, knee * 0.85
    p["LeftUpperArm"] = [arx, ary, 0]
    p["RightUpperArm"] = [arx * 0.95, ary, 0]
    both(p, "LowerArm", [elb, 0, 0])
    p["UpperTorso"][0] = lean
    p["Head"][0] = -lean * 0.6
    p["_bob"] = bob
    return p


def jump_lift(u, d, height):
    """Root height (m) inside a jump segment: parabola between takeoff and touchdown."""
    _, t0, t1 = _jump_keys(d)
    if t0 <= u <= t1:
        s = (u - t0) / (t1 - t0)
        return 4.0 * height * s * (1 - s)
    return 0.0


def st_fall(u, d, ctx):
    p = zero()
    w = math.sin(2 * math.pi * 3.0 * u)
    p["LeftUpperArm"] = [-120 + 15 * w, 40, 0]
    p["RightUpperArm"] = [-120 - 15 * w, 40, 0]
    both(p, "LowerArm", [-25, 0, 0])
    p["LeftUpperLeg"] = [-30 + 10 * w, 8, 0]
    p["RightUpperLeg"] = [-10 - 10 * w, 8, 0]
    both(p, "LowerLeg", [40, 0, 0])
    p["UpperTorso"][0] = -6
    p["Head"][0] = -10
    return p


def st_land(u, d, ctx):
    k = 1 - smooth(u / max(0.2, d))
    p = zero()
    both(p, "UpperLeg", [-45 * k, 4, 0])
    both(p, "LowerLeg", [75 * k, 0, 0])
    both(p, "UpperArm", [-40 * k, 18 * k + 5, 0])
    both(p, "LowerArm", [-30 * k - 8, 0, 0])
    p["UpperTorso"][0] = 18 * k
    p["_bob"] = -0.13 * k
    return p


def st_crouch(u, d, ctx):
    p = st_idle(u, d, ctx)
    both(p, "UpperLeg", [-60, 6, 0])
    both(p, "LowerLeg", [105, 0, 0])
    p["UpperTorso"][0] = 22
    both(p, "UpperArm", [-25, 10, 0])
    both(p, "LowerArm", [-40, 0, 0])
    p["_bob"] = -ctx["params"].get("drop", 0.22)
    return p


def st_sit(u, d, ctx):
    p = st_idle(u, d, ctx)
    both(p, "UpperLeg", [-90, 4, 0])
    both(p, "LowerLeg", [90, 0, 0])
    both(p, "UpperArm", [-30, 8, 0])
    both(p, "LowerArm", [-45, 0, 0])
    p["UpperTorso"][0] = 4
    p["_bob"] = -ctx["params"].get("drop", 0.27)
    return p


def st_lie(u, d, ctx):
    p = zero()
    p["LowerTorso"][0] = -88          # lie on the back (root stays; use root keys to place)
    both(p, "UpperArm", [-8, 12, 0])
    both(p, "LowerLeg", [4, 0, 0])
    p["Head"][0] = 8
    p["_bob"] = ctx["params"].get("drop", -0.45)
    return p


def st_pickup(u, d, ctx):
    """crouch-reach-lift over the segment (reach at 45%, back up by 100%)."""
    k = math.sin(math.pi * clamp(u / max(0.3, d), 0, 1))
    p = st_idle(u, d, ctx)
    both(p, "UpperLeg", [-70 * k, 6, 0])
    both(p, "LowerLeg", [110 * k, 0, 0])
    p["UpperTorso"][0] = 38 * k
    p["RightUpperArm"] = [-70 * k, 8, 0]
    p["LeftUpperArm"] = [-45 * k, 10, 0]
    both(p, "LowerArm", [-12, 0, 0])
    p["Head"][0] = 10 * k
    p["_bob"] = -0.26 * k
    return p


def st_cheer(u, d, ctx):
    p = zero()
    f = ctx["params"].get("rate", 2.0)
    a = math.sin(2 * math.pi * f * u)
    b = math.sin(2 * math.pi * f * u + 0.6)
    p["LeftUpperArm"] = [-(148 + 16 * a), 26, 0]
    p["RightUpperArm"] = [-(148 + 16 * b), 26, 0]
    p["LeftLowerArm"][0] = -(14 + 22 * (1 - a) / 2)
    p["RightLowerArm"][0] = -(14 + 22 * (1 - b) / 2)
    hop = abs(math.sin(2 * math.pi * (f / 2) * u))
    both(p, "UpperLeg", [-10 * hop, 3, 0])
    both(p, "LowerLeg", [18 * hop, 0, 0])
    p["UpperTorso"] = [-8, 0, 6 * math.sin(math.pi * u)]
    p["Head"][0] = -12
    p["_bob"] = -0.05 * hop
    return p


def st_wave(u, d, ctx):
    p = st_idle(u, d, ctx)
    side = ctx["params"].get("side", "Right")
    w = math.sin(2 * math.pi * 2.2 * u)
    p[side + "UpperArm"] = [-150, 28, 0]
    p[side + "LowerArm"] = [-35 - 25 * w, 0, 0]
    p["Head"][2] = 8 if side == "Right" else -8
    return p


def st_point(u, d, ctx):
    p = st_idle(u, d, ctx)
    side = ctx["params"].get("side", "Right")
    k = smooth(u / 0.2)
    p[side + "UpperArm"] = [-92 * k, 6, ctx["params"].get("aim_yaw", 0.0)]
    p[side + "LowerArm"] = [-4, 0, 0]
    p["UpperTorso"][0] = 6 * k
    return p


def st_clap(u, d, ctx):
    p = st_idle(u, d, ctx)
    c = (1 + math.sin(2 * math.pi * 2.5 * u)) / 2
    both(p, "UpperArm", [-72, 6 + 26 * c, 0])
    both(p, "LowerArm", [-48, 0, 0])
    return p


def st_talk(u, d, ctx):
    """conversational gestures; params: energy (0.5..1.5), side ('Right'/'Left'/'Both')."""
    p = st_idle(u, d, ctx)
    e = ctx["params"].get("energy", 1.0)
    g1 = math.sin(2 * math.pi * 0.9 * u) * math.sin(2 * math.pi * 0.23 * u + 1.0)
    g2 = math.sin(2 * math.pi * 0.7 * u + 2.0)
    side = ctx["params"].get("side", "Both")
    for s, g in (("Right", g1), ("Left", g2)):
        if side in (s, "Both"):
            p[s + "UpperArm"] = [-(28 + 14 * g) * e, 10 + 6 * g * e, 0]
            p[s + "LowerArm"] = [-(55 + 20 * g) * e, 0, 0]
    p["Head"][0] = 3 * math.sin(2 * math.pi * 1.6 * u) * e
    p["Head"][2] = 6 * math.sin(2 * math.pi * 0.35 * u) * e
    p["UpperTorso"][2] = 3 * g1 * e
    return p


def st_shock(u, d, ctx):
    p = st_idle(u, d, ctx)
    both(p, "UpperArm", [-38, 28, 0])
    both(p, "LowerArm", [-62, 0, 0])
    both(p, "UpperLeg", [-6, 4, 0])
    both(p, "LowerLeg", [14, 0, 0])
    p["UpperTorso"][0] = -9
    p["Head"][0] = -6
    p["_bob"] = -0.03
    return p


def st_scared(u, d, ctx):
    p = zero()
    tr = 2.0 * math.sin(2 * math.pi * 9 * u)
    both(p, "UpperArm", [-105 + tr, 12, 0])
    both(p, "LowerArm", [-125, 0, 0])
    both(p, "UpperLeg", [-22, 5, 0])
    both(p, "LowerLeg", [38, 0, 0])
    p["UpperTorso"][0] = 18
    p["Head"][0] = 14
    p["_bob"] = -0.07
    return p


def st_sad(u, d, ctx):
    p = st_idle(u, d, ctx)
    p["UpperTorso"][0] = 20
    p["Head"][0] = 26
    both(p, "UpperArm", [2, 4, 0])
    both(p, "LowerArm", [-4, 0, 0])
    p["_bob"] = -0.02
    return p


def st_angry(u, d, ctx):
    p = st_idle(u, d, ctx)
    sh = 2.5 * math.sin(2 * math.pi * 6 * u)
    both(p, "UpperArm", [-22 + sh, 24, 0])
    both(p, "LowerArm", [-95, 0, 0])
    p["UpperTorso"][0] = 10
    p["Head"][0] = 6
    both(p, "UpperLeg", [-4, 10, 0])
    return p


def st_think(u, d, ctx):
    p = st_idle(u, d, ctx)
    p["RightUpperArm"] = [-58, 14, -20]
    p["RightLowerArm"] = [-132, 0, 0]
    p["LeftUpperArm"] = [-30, 6, 25]
    p["LeftLowerArm"] = [-95, 0, 0]
    p["Head"] = [8, 0, 10 * math.sin(2 * math.pi * 0.3 * u)]
    return p


def st_punch(u, d, ctx):
    """alternating jabs; params: rate (hits/s)."""
    p = zero()
    r = ctx["params"].get("rate", 2.5)
    ph = (u * r) % 1.0
    hit = smooth(ph / 0.35) * (1 - smooth((ph - 0.5) / 0.4))
    lead = "Right" if int(u * r) % 2 == 0 else "Left"
    rear = "Left" if lead == "Right" else "Right"
    p[lead + "UpperArm"] = [-30 - 62 * hit, 10, 0]
    p[lead + "LowerArm"] = [-100 + 96 * hit, 0, 0]
    p[rear + "UpperArm"] = [-35, 14, 0]
    p[rear + "LowerArm"] = [-110, 0, 0]
    p["UpperTorso"] = [8, 0, (18 if lead == "Right" else -18) * hit]
    p["LowerTorso"][2] = (-6 if lead == "Right" else 6) * hit
    p["LeftUpperLeg"], p["RightUpperLeg"] = [-18, 6, 0], [10, 6, 0]
    both(p, "LowerLeg", [22, 0, 0])
    p["_bob"] = -0.04
    return p


def st_kick(u, d, ctx):
    p = zero()
    k = math.sin(math.pi * clamp(u / max(0.3, d), 0, 1))
    side = ctx["params"].get("side", "Right")
    other = "Left" if side == "Right" else "Right"
    p[side + "UpperLeg"] = [-95 * k, 6, 0]
    p[side + "LowerLeg"] = [70 * (1 - k) + 5, 0, 0]
    p[other + "LowerLeg"] = [15, 0, 0]
    both(p, "UpperArm", [-20, 35 * k + 6, 0])
    both(p, "LowerArm", [-40, 0, 0])
    p["UpperTorso"][0] = -14 * k
    return p


def st_hit(u, d, ctx):
    """knock-back reaction: snap back in 0.08 s, then recover over the segment."""
    k = smooth(u / 0.08) * (1 - smooth((u - 0.15) / max(0.2, d - 0.15)))
    p = st_idle(u, d, ctx)
    p["UpperTorso"][0] = -26 * k
    p["Head"][0] = -22 * k
    both(p, "UpperArm", [-55 * k, 35 * k + 5, 0])
    both(p, "LowerArm", [-30 * k - 10, 0, 0])
    both(p, "LowerLeg", [20 * k, 0, 0])
    p["_bob"] = -0.05 * k
    return p


def st_dance(u, d, ctx):
    p = zero()
    b = 2 * math.pi * ctx["params"].get("bpm", 120) / 60.0 * u
    s = math.sin(b)
    p["LeftUpperArm"] = [-90 - 60 * s, 30, 0]
    p["RightUpperArm"] = [-90 + 60 * s, 30, 0]
    both(p, "LowerArm", [-40, 0, 0])
    p["LowerTorso"][2] = 14 * s
    p["UpperTorso"][2] = -10 * s
    both(p, "LowerLeg", [20 * abs(s), 0, 0])
    both(p, "UpperLeg", [-10 * abs(s), 8, 0])
    p["Head"][2] = 10 * s
    p["_bob"] = -0.04 * abs(s)
    return p


def st_look_around(u, d, ctx):
    p = st_idle(u, d, ctx)
    p["Head"][2] = _keys([(0, (0,)), (0.2 * d, (55,)), (0.35 * d, (55,)), (0.6 * d, (-55,)), (0.75 * d, (-55,)), (d, (0,))], u)[0]
    p["UpperTorso"][2] = p["Head"][2] * 0.25
    return p


def st_pose(u, d, ctx):
    """static custom pose: params['pose'] = {bone: [rx, ry, rz], '_bob': m}; merges over idle."""
    p = st_idle(u, d, ctx)
    for k, v in ctx["params"].get("pose", {}).items():
        p[k] = v if k == "_bob" else list(v)
    return p


STATES = {
    "idle": st_idle, "walk": st_walk, "run": st_run, "sprint": st_sprint, "jump": st_jump, "fall": st_fall,
    "land": st_land, "crouch": st_crouch, "sit": st_sit, "lie": st_lie, "pickup": st_pickup, "cheer": st_cheer,
    "wave": st_wave, "point": st_point, "clap": st_clap, "talk": st_talk, "shock": st_shock, "scared": st_scared,
    "sad": st_sad, "angry": st_angry, "think": st_think, "punch": st_punch, "kick": st_kick, "hit": st_hit,
    "dance": st_dance, "look_around": st_look_around, "pose": st_pose,
}
LOCOMOTION = {"walk": ("walk", 32.0, WALK_STUDS), "run": ("run", 55.0, RUN_STUDS), "sprint": ("sprint", 65.0, RUN_STUDS * 1.4)}


# ============================================================ ANIMATOR
class RobloxAnimator:
    def __init__(self, char_info, fps=30):
        self.ch = char_info
        self.arm = char_info["armature"]
        self.fps = fps
        self.segs = []          # (state, t0, t1, fade, params)
        self.looks = []         # (t0, t1, yaw_keys, pitch_keys)
        self.faces = []         # (t0, t1, expr)
        self.face_frames = None
        self.stops = []         # (t, n_frames)
        self.root = None        # [(t, (x, y), yaw_deg)] or callable t -> (x, y, yaw)
        self.side = {b.name: (1.0 if b.head_local.x > 0 else -1.0) for b in self.arm.data.bones}
        legs = [self.arm.data.bones.get(n) for n in ("LeftUpperLeg", "LeftLowerLeg")]
        self.leg_len = sum((b.tail_local - b.head_local).length for b in legs if b) or 0.58
        self.base_z = self.arm.location.z

    # ---------------- authoring
    def add(self, state, t0, t1, fade=0.2, **params):
        if state not in STATES:
            raise ValueError(f"unknown state '{state}'. choose from: {sorted(STATES)}")
        self.segs.append((state, float(t0), float(t1), float(fade), params))
        self.segs.sort(key=lambda s: s[1])
        return self

    def root_keys(self, keys):
        """keys: [(t, (x, y), yaw_deg)] in metres/deg (yaw: kit convention, 90 = faces +X), or a callable."""
        self.root = keys
        return self

    def look(self, t0, t1, yaw=(0, 0), pitch=(0, 0)):
        self.looks.append((float(t0), float(t1), list(yaw), list(pitch)))
        return self

    def face(self, t0, t1, expr):
        self.faces.append((float(t0), float(t1), expr))
        return self

    def face_schedule(self, frames):
        """1-indexed list of expression names per frame (e.g. kit.build_lipsync_schedule output)."""
        self.face_frames = frames
        return self

    def hit_stop(self, t, frames=2):
        self.stops.append((float(t), int(frames)))
        return self

    # ---------------- evaluation
    def _world_t(self, f):
        t = (f - 1) / self.fps
        for ts, n in self.stops:
            fi = int(math.floor(ts * self.fps)) + 1
            if fi < f <= fi + n:
                return (fi - 1) / self.fps
        return t

    def _root_at(self, t):
        if self.root is None:
            return (self.arm.location.x, self.arm.location.y, math.degrees(self.arm.rotation_euler.z))
        if callable(self.root):
            return self.root(t)
        ks = [(k[0], (k[1][0], k[1][1], k[2])) for k in self.root]
        return _keys(ks, t)

    def _seg_at(self, t):
        cur = None
        for i, s in enumerate(self.segs):
            if s[1] <= t:
                cur = i
        return cur

    def _eval_seg(self, i, t, loco):
        state, t0, t1, fade, params = self.segs[i]
        ctx = {"phase": loco.get(i, (0.0, 1.0))[0], "amp": loco.get(i, (0.0, 1.0))[1], "params": params, "t": t}
        return STATES[state](clamp(t - t0, 0, max(t1 - t0, 1e-3) + 2.0), t1 - t0, ctx)

    def pose_at(self, t, loco):
        i = self._seg_at(t)
        if i is None:
            return st_idle(t, 1, {"params": {}})
        p = self._eval_seg(i, t, loco)
        state, t0, t1, fade, params = self.segs[i]
        if i > 0 and fade > 0 and t - t0 < fade:
            p = blend(self._eval_seg(i - 1, t, loco), p, smooth((t - t0) / fade))
        for lt0, lt1, yk, pk in self.looks:
            if lt0 <= t <= lt1:
                n = max(1, len(yk) - 1)
                u = (t - lt0) / max(1e-6, lt1 - lt0)
                p["Head"][2] += _keys([(j / n, (v,)) for j, v in enumerate(yk)], u)[0]
                m = max(1, len(pk) - 1)
                p["Head"][0] += _keys([(j / m, (v,)) for j, v in enumerate(pk)], u)[0]
        return p

    def lift_at(self, t):
        i = self._seg_at(t)
        if i is None:
            return 0.0
        state, t0, t1, fade, params = self.segs[i]
        if state == "jump":
            return jump_lift(t - t0, t1 - t0, params.get("height", 1.6))
        return 0.0

    # ---------------- bake
    def bake(self, frame_start=1, frame_end=None):
        sc = bpy.context.scene
        frame_end = frame_end or sc.frame_end
        arm = self.arm
        loco = {}           # seg index -> (phase, amp) updated per frame
        phase_acc = {}
        prev = None
        for f in range(frame_start, frame_end + 1):
            t = self._world_t(f)
            x, y, yaw = self._root_at(t)
            dist = 0.0 if prev is None else math.hypot(x - prev[0], y - prev[1])
            prev = (x, y)
            speed = dist * self.fps
            # advance locomotion phases for every locomotion segment (keeps crossfades continuous)
            for i, s in enumerate(self.segs):
                if s[0] in LOCOMOTION:
                    kind, A, vnom = LOCOMOTION[s[0]]
                    amp = clamp(s[4].get("amp", speed / vnom if vnom else 1.0), 0.25, 1.15)
                    cyc = 4.0 * self.leg_len * math.sin(math.radians(A * amp))
                    phase_acc[i] = phase_acc.get(i, 0.0) + 2 * math.pi * dist / max(1e-3, cyc)
                    if speed < 0.05 and s[1] <= t <= s[2]:
                        amp = 0.25
                    loco[i] = (phase_acc[i], amp)
            pose = self.pose_at(t, loco)
            arm.location = (x, y, self.base_z + self.lift_at(t))
            arm.rotation_euler = Euler((0, 0, math.radians(yaw)), "XYZ")
            arm.keyframe_insert("location", frame=f)
            arm.keyframe_insert("rotation_euler", frame=f)
            apply_pose(arm, pose, f, self.side)
        if self.faces or self.face_frames:
            self._bake_faces(frame_start, frame_end)
        return self

    def _bake_faces(self, fs, fe):
        tex = self.ch.get("face_tex_node")
        if tex is None:
            return
        faces_dir = os.path.dirname(bpy.path.abspath(tex.image.filepath)) if tex.image else ""
        sched = {}
        for f in range(fs, fe + 1):
            if self.face_frames:
                sched[f] = self.face_frames[min(f, len(self.face_frames) - 1)]
            else:
                t = (f - 1) / self.fps
                sched[f] = next((e for a, b, e in reversed(self.faces) if a <= t < b), None)
        bake_face_switch(tex, sched, faces_dir)


def apply_pose(arm, pose, frame, side_sign):
    """Write one frame. basis = rest^-1 @ T @ rest  (T = Rz @ Ry @ Rx in rest-aligned armature axes)."""
    for b in BONES:
        pb = arm.pose.bones.get(b)
        if pb is None:
            continue
        key = next((k for k in LIMITS if b.endswith(k) or b == k), None)
        rx, ry, rz = pose[b]
        if key:
            (a0, a1), (b0, b1), (c0, c1) = LIMITS[key]
            rx, ry, rz = clamp(rx, a0, a1), clamp(ry, b0, b1), clamp(rz, c0, c1)
        if b.startswith(("Left", "Right")):
            ry = ry * -side_sign.get(b, 1.0)   # +ry = outward on either side
        T = (Quaternion((0, 0, 1), math.radians(rz)) @ Quaternion((0, 1, 0), math.radians(ry))
             @ Quaternion((1, 0, 0), math.radians(rx)))
        rest = pb.bone.matrix_local.to_quaternion()
        pb.rotation_mode = "QUATERNION"
        pb.rotation_quaternion = rest.inverted() @ T @ rest
        pb.keyframe_insert("rotation_quaternion", frame=frame, group=b)
        if b == "LowerTorso":
            pb.location = rest.inverted() @ Vector((0.0, 0.0, pose["_bob"]))
            pb.keyframe_insert("location", frame=frame, group=b)


def bake_face_switch(tex_node, schedule, faces_dir):
    """Replace a single face Image Texture with a keyframed node switch (self-contained in the .blend).
    schedule: {frame: expr_name or None}. Images are loaded from faces_dir/<expr>.png and packed."""
    nt = tex_node.id_data
    exprs = []
    for e in schedule.values():
        if e and e not in exprs:
            exprs.append(e)
    if not exprs:
        return
    out_col = [l.to_socket for l in nt.links if l.from_node == tex_node and l.from_socket.name == "Color"]
    out_alp = [l.to_socket for l in nt.links if l.from_node == tex_node and l.from_socket.name == "Alpha"]
    texs = []
    for i, e in enumerate(exprs):
        path = os.path.join(faces_dir, e + ".png")
        if not os.path.exists(path):
            print(f"[FACE] missing {path}; skipped")
            continue
        img = bpy.data.images.load(path, check_existing=True)
        img.colorspace_settings.name = "sRGB"
        try:
            img.pack()
        except Exception:
            pass
        n = tex_node if i == 0 else nt.nodes.new("ShaderNodeTexImage")
        n.image = img
        n.extension = "CLIP"
        if i > 0:
            n.inputs["Vector"].default_value = tex_node.inputs["Vector"].default_value
            for l in nt.links:
                if l.to_node == tex_node and l.to_socket.name == "Vector":
                    nt.links.new(l.from_socket, n.inputs["Vector"])
        texs.append((e, n))
    col, alp = texs[0][1].outputs["Color"], texs[0][1].outputs["Alpha"]
    mixes = []
    for e, n in texs[1:]:
        mc = nt.nodes.new("ShaderNodeMix"); mc.data_type = "RGBA"
        ma = nt.nodes.new("ShaderNodeMix"); ma.data_type = "FLOAT"
        nt.links.new(col, mc.inputs[6]); nt.links.new(n.outputs["Color"], mc.inputs[7])
        nt.links.new(alp, ma.inputs[2]); nt.links.new(n.outputs["Alpha"], ma.inputs[3])
        col, alp = mc.outputs[2], ma.outputs[0]
        mixes.append((e, mc, ma))
    for s in out_col:
        nt.links.new(col, s)
    for s in out_alp:
        nt.links.new(alp, s)
    last = {}
    for f in sorted(schedule):
        e = schedule[f]
        for name, mc, ma in mixes:
            v = 1.0 if e == name else 0.0
            if last.get(name) != v:
                for m in (mc, ma):
                    m.inputs[0].default_value = v
                    m.inputs[0].keyframe_insert("default_value", frame=f)
                last[name] = v
    if nt.animation_data and nt.animation_data.action:
        from blender_roblox_kit import iter_action_fcurves
        for fc in iter_action_fcurves(nt.animation_data.action):
            for kp in fc.keyframe_points:
                kp.interpolation = "CONSTANT"


# ============================================================ QA
def render_pose_qa(arm, frames, out_dir, size=(260, 340), dist=8.0, sheet_name="pose_qa_sheet.png", isolate=True):
    """Character-locked orthographic FRONT + SIDE workbench renders of the given frames, composed into
    <out_dir>/<sheet_name> (row 1 = front, row 2 = side). Inspect it: limbs must stay attached, never pass
    through the torso, feet must not slide or sink, silhouettes must read at thumbnail size.
    isolate=True hides everything except the character (its collection + objects bound to the armature)."""
    import numpy as np
    sc = bpy.context.scene
    hidden = []
    if isolate:
        char_cols = set(arm.users_collection)
        def _mine(o):
            if o == arm or any(c in char_cols for c in o.users_collection):
                return True
            p = o.parent
            while p:
                if p == arm:
                    return True
                p = p.parent
            return any(m.type == "ARMATURE" and m.object == arm for m in getattr(o, "modifiers", []))
        for o in sc.objects:
            if o.type not in ("CAMERA", "LIGHT") and not _mine(o) and not o.hide_render:
                o.hide_render = True
                hidden.append(o)
    keep = (sc.camera, sc.render.engine, sc.render.resolution_x, sc.render.resolution_y, sc.render.filepath,
            sc.render.use_motion_blur, sc.frame_current)
    os.makedirs(out_dir, exist_ok=True)
    sc.render.engine = "BLENDER_WORKBENCH"
    sc.render.use_motion_blur = False
    sc.render.resolution_x, sc.render.resolution_y = size
    cd = bpy.data.cameras.new("PoseQA"); cd.type = "ORTHO"; cd.ortho_scale = 2.4
    cam = bpy.data.objects.new("PoseQA", cd); sc.collection.objects.link(cam); sc.camera = cam
    tiles = {"front": [], "side": []}
    for f in frames:
        sc.frame_set(f)
        m = arm.matrix_world.to_3x3()
        c = arm.matrix_world.translation + Vector((0, 0, 0.8))
        for tag, d in (("front", m @ Vector((0, -1, 0))), ("side", m @ Vector((1, 0, 0)))):
            cam.location = c + d.normalized() * dist
            cam.rotation_euler = (c - cam.location).to_track_quat("-Z", "Y").to_euler()
            p = os.path.join(out_dir, f"qa_f{f:04d}_{tag}.png")
            sc.render.filepath = p
            bpy.ops.render.render(write_still=True)
            tiles[tag].append(p)
    rows = []
    for tag in ("front", "side"):
        imgs = []
        for p in tiles[tag]:
            im = bpy.data.images.load(p)
            a = np.array(im.pixels[:], dtype=np.float32).reshape(im.size[1], im.size[0], 4)
            imgs.append(a)
            bpy.data.images.remove(im)
        rows.append(np.concatenate(imgs, axis=1))
    sheet = np.concatenate(rows[::-1], axis=0)   # Blender pixel rows start at the bottom
    h, w = sheet.shape[:2]
    out = bpy.data.images.new("pose_qa_sheet", w, h, alpha=True)
    out.pixels.foreach_set(sheet.ravel())
    out.filepath_raw = os.path.join(out_dir, sheet_name)
    out.file_format = "PNG"
    out.save()
    bpy.data.images.remove(out)
    bpy.data.objects.remove(cam); bpy.data.cameras.remove(cd)
    for o in hidden:
        o.hide_render = False
    (sc.camera, sc.render.engine, sc.render.resolution_x, sc.render.resolution_y, sc.render.filepath,
     sc.render.use_motion_blur, _) = keep
    sc.frame_set(keep[-1])
    return os.path.join(out_dir, sheet_name)

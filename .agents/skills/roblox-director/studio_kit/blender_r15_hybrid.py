#!/usr/bin/env python3
"""
blender_r15_hybrid.py — Hybrid 3D Animation Engine (HƯỚNG 3) for @RobloxDirector.
Combines:
1. Non-destructive R15 Control Upgrade: Foot IK (zero ground slip), Hand IK, and Secondary Hair/Scarf overlap bones.
2. True Grounded IK Acting Clips: Weight-shifted Idle, Parabolic Foot-Pinned Walk IK, and Crouch/Pickup IK.
3. Blender 5.3 NLA Hybrid Mixer + Word-Accented Upper-Body Overlay (`words.json`).
4. Mixamo (.fbx) & Mocap (.bvh) Auto-Retarget Bridge (`blender-animation/scripts/retarget.py` compatible).
"""
import json
import math
import os
import sys
import bpy
from bpy_extras import anim_utils
from mathutils import Euler, Matrix, Quaternion, Vector

STUD = 0.28
CORE_SKILL_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CORE_ANIMS_DIR = os.path.join(CORE_SKILL_DIR, "assets", "anims")
ANIM_SCRIPTS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "blender-animation", "scripts"))


def resolve_anim_path(name_or_path: str) -> str:
    """Resolve either an explicit path or a bare Mixamo clip name ('Waving' / 'Waving.fbx') from Core assets/anims/."""
    if os.path.exists(name_or_path):
        return name_or_path
    for cand in (name_or_path, f"{name_or_path}.fbx", f"{name_or_path}.bvh"):
        p = os.path.join(CORE_ANIMS_DIR, cand)
        if os.path.exists(p):
            return p
    return name_or_path


def _char_vec_to_bone_local(arm_obj, bone_name: str, delta_char_m: Vector) -> Vector:
    """Convert an offset vector in character-space meters into pose_bone.location space."""
    b = arm_obj.data.bones.get(bone_name)
    if b is None:
        return delta_char_m
    return b.matrix_local.to_3x3().inverted() @ delta_char_m


def _set_ik_influence(arm_obj, frame: int, foot_l=None, foot_r=None, hand_l=None, hand_r=None, ramp: int = 0):
    mapping = [
        ("LeftLowerLeg", "IK", foot_l),
        ("RightLowerLeg", "IK", foot_r),
        ("LeftLowerArm", "IK", hand_l),
        ("RightLowerArm", "IK", hand_r),
    ]
    for bname, cname, val in mapping:
        if val is None:
            continue
        pb = arm_obj.pose.bones.get(bname)
        if not pb:
            continue
        con = pb.constraints.get(cname)
        if not con:
            continue
        if ramp > 0 and frame > ramp:
            con.keyframe_insert("influence", frame=frame - ramp)
        con.influence = float(val)
        con.keyframe_insert("influence", frame=frame)


def setup_r15_hybrid_rig(char_info: dict):
    """
    Upgrade an existing R15 character with:
    - IK_Foot.L/R + Pole_Knee.L/R (forward knee pre-bend, zero foot slip)
    - IK_Hand.L/R + Pole_Elbow.L/R (backward elbow pre-bend)
    - Secondary Spring Bones: Sec_Pony (under Head) & Sec_Scarf (under UpperTorso)
    """
    if char_info.get("rig_type") != "R15":
        return char_info
    if char_info.get("hybrid_ready"):
        return char_info

    arm = char_info["armature"]
    m = char_info["metrics"]
    hs = m["hs"]
    lh = m["lh"]
    neck_z = m["neck_z"]
    kn_z = 0.5 * lh

    old_mode = bpy.context.mode
    bpy.context.view_layer.objects.active = arm
    arm.select_set(True)

    with bpy.context.temp_override(object=arm, active_object=arm):
        bpy.ops.object.mode_set(mode="EDIT")
        eb = arm.data.edit_bones
        root_b = eb.get("Root")

        # 1. Foot IK & Knee Poles (slight -Y pre-bend at knee guarantees anatomical forward flexion)
        for side, prefix in (("L", "Left"), ("R", "Right")):
            ul = eb.get(prefix + "UpperLeg")
            ll = eb.get(prefix + "LowerLeg")
            if ul and ll:
                ul.tail.y -= 0.028 * STUD
                ll.head.y = ul.tail.y
                ik = eb.new(f"IK_Foot.{side}")
                ik.head = ll.tail.copy()
                ik.tail = ik.head + Vector((0.0, -0.26 * STUD, 0.0))
                ik.parent = root_b
                ik.use_deform = False

                pl = eb.new(f"Pole_Knee.{side}")
                pl.head = Vector((ul.tail.x, -0.95 * STUD, kn_z * STUD))
                pl.tail = pl.head + Vector((0.0, -0.15 * STUD, 0.0))
                pl.parent = root_b
                pl.use_deform = False

        # 2. Hand IK & Elbow Poles (slight +Y back pre-bend at elbow)
        for side, prefix in (("L", "Left"), ("R", "Right")):
            ua = eb.get(prefix + "UpperArm")
            la = eb.get(prefix + "LowerArm")
            if ua and la:
                ua.tail.y += 0.025 * STUD
                la.head.y = ua.tail.y
                ik = eb.new(f"IK_Hand.{side}")
                ik.head = la.tail.copy()
                ik.tail = ik.head + Vector((0.0, -0.22 * STUD, 0.0))
                ik.parent = root_b
                ik.use_deform = False

                pl = eb.new(f"Pole_Elbow.{side}")
                pl.head = Vector((ua.tail.x, +0.95 * STUD, ua.tail.z))
                pl.tail = pl.head + Vector((0.0, +0.15 * STUD, 0.0))
                pl.parent = root_b
                pl.use_deform = False

        # 3. Secondary Overlap Bones for Hair Tail & Scarf Ends
        head_b = eb.get("Head")
        ut_b = eb.get("UpperTorso")
        if head_b and "Sec_Pony" not in eb:
            sp = eb.new("Sec_Pony")
            sp.head = Vector((0.0, 0.62 * hs * STUD, (neck_z + 0.82 * hs) * STUD))
            sp.tail = Vector((0.0, 1.02 * hs * STUD, (neck_z - 0.55 * hs) * STUD))
            sp.parent = head_b
            sp.use_deform = True
        if ut_b and "Sec_Scarf" not in eb:
            ss = eb.new("Sec_Scarf")
            ss.head = Vector((0.0, -0.45 * STUD, (neck_z - 0.15) * STUD))
            ss.tail = Vector((0.0, -0.58 * STUD, (neck_z - 0.85) * STUD))
            ss.parent = ut_b
            ss.use_deform = True

        bpy.ops.object.mode_set(mode="OBJECT")

    # Configure Pose IK Constraints (influence defaults to 0.0 so legacy FK calls behave identically)
    for side, prefix, p_ang in (("L", "Left", -90.0), ("R", "Right", -90.0)):
        pb = arm.pose.bones.get(prefix + "LowerLeg")
        if pb:
            c = pb.constraints.new("IK")
            c.name = "IK"
            c.target = arm
            c.subtarget = f"IK_Foot.{side}"
            c.pole_target = arm
            c.pole_subtarget = f"Pole_Knee.{side}"
            c.pole_angle = math.radians(p_ang)
            c.chain_count = 2
            c.influence = 0.0

    for side, prefix, p_ang in (("L", "Left", 90.0), ("R", "Right", 90.0)):
        pb = arm.pose.bones.get(prefix + "LowerArm")
        if pb:
            c = pb.constraints.new("IK")
            c.name = "IK"
            c.target = arm
            c.subtarget = f"IK_Hand.{side}"
            c.pole_target = arm
            c.pole_subtarget = f"Pole_Elbow.{side}"
            c.pole_angle = math.radians(p_ang)
            c.chain_count = 2
            c.influence = 0.0

    # Smoothly re-weight hanging hair locks (Ponytail / Wisps) & Scarf tails onto Secondary bones
    col = char_info["collection"]
    pony_anchor = Vector((0.0, 0.62 * hs * STUD, (neck_z + 0.82 * hs) * STUD))
    for obj in col.objects:
        if obj.type != "MESH":
            continue
        nm = obj.name
        if any(k in nm for k in ("_Hair_PonyCore", "_Hair_PonyWing", "_Hair_BunLock", "_Hair_BobCheek")):
            vg_h = obj.vertex_groups.get("Head")
            vg_s = obj.vertex_groups.get("Sec_Pony") or obj.vertex_groups.new(name="Sec_Pony")
            for v in obj.data.vertices:
                dist = (v.co - pony_anchor).length
                w_tail = max(0.0, min(1.0, (dist - 0.14 * hs * STUD) / max(0.05, 0.42 * hs * STUD)))
                if vg_h:
                    vg_h.add([v.index], 1.0 - w_tail, "REPLACE")
                vg_s.add([v.index], w_tail, "REPLACE")
        elif "ScarfTail" in nm or "ScarfEnd" in nm:
            vg_u = obj.vertex_groups.get("UpperTorso")
            vg_s = obj.vertex_groups.get("Sec_Scarf") or obj.vertex_groups.new(name="Sec_Scarf")
            z_top = (neck_z - 0.12) * STUD
            for v in obj.data.vertices:
                drop = max(0.0, z_top - v.co.z)
                w_s = max(0.0, min(1.0, drop / (0.55 * STUD)))
                if vg_u:
                    vg_u.add([v.index], 1.0 - w_s, "REPLACE")
                vg_s.add([v.index], w_s, "REPLACE")

    if old_mode == "POSE":
        bpy.ops.object.mode_set(mode="POSE")
    char_info["hybrid_ready"] = True
    return char_info


def _key_bone(arm_obj, bname: str, frame: int, loc_char_m: Vector = None, rot_deg=None):
    pb = arm_obj.pose.bones.get(bname)
    if pb is None:
        return
    if loc_char_m is not None:
        pb.location = _char_vec_to_bone_local(arm_obj, bname, loc_char_m)
        pb.keyframe_insert("location", frame=frame)
    if rot_deg is not None:
        pb.rotation_mode = "XYZ"
        pb.rotation_euler = Euler([math.radians(a) for a in rot_deg])
        pb.keyframe_insert("rotation_euler", frame=frame)


def animate_idle_weight_shift(
    char_info: dict,
    fs: int,
    fe: int,
    loc=None,
    yaw_deg: float = None,
    sway_m: float = 0.055,
    crouch_m: float = 0.032,
    cycle_frames: int = 44,
):
    """
    Standing human weight shift with Foot IK locked 100% flat to the floor (0.000m slip).
    Hips sway left-right, stance knee straightens while opposite knee softens naturally.
    """
    setup_r15_hybrid_rig(char_info)
    arm = char_info["armature"]
    if loc is not None:
        arm.location = Vector(loc)
        arm.keyframe_insert("location", frame=fs)
    if yaw_deg is not None:
        arm.rotation_euler = Euler((0.0, 0.0, math.radians(yaw_deg)))
        arm.keyframe_insert("rotation_euler", frame=fs)

    _set_ik_influence(arm, fs, foot_l=1.0, foot_r=1.0, hand_l=0.0, hand_r=0.0)
    _key_bone(arm, "IK_Foot.L", fs, Vector((0.0, 0.0, 0.0)), (0, 0, 0))
    _key_bone(arm, "IK_Foot.R", fs, Vector((0.0, 0.0, 0.0)), (0, 0, 0))

    span = max(1, fe - fs)
    step = max(8, cycle_frames // 4)
    for fr in list(range(fs, fe, step)) + [fe]:
        ph = ((fr - fs) / float(max(1, cycle_frames))) * 2.0 * math.pi
        s = math.sin(ph)
        c = math.cos(ph)
        hip_dx = s * sway_m
        hip_dz = -crouch_m * (0.65 + 0.35 * abs(c))
        _key_bone(arm, "LowerTorso", fr, Vector((hip_dx, 0.0, hip_dz)), (2.0, s * 3.5, s * 4.5))
        _key_bone(arm, "UpperTorso", fr, rot_deg=(3.0 + c * 1.5, -s * 2.5, -s * 5.0))
        _key_bone(arm, "Head", fr, rot_deg=(-2.0 - c * 1.2, s * 1.5, s * 3.5))
        _key_bone(arm, "RightUpperArm", fr, rot_deg=(-6.0 + s * 3.0, 0.0, -7.0))
        _key_bone(arm, "RightLowerArm", fr, rot_deg=(-18.0 - s * 4.0, 0.0, 0.0))
        _key_bone(arm, "LeftUpperArm", fr, rot_deg=(-5.0 - s * 3.0, 0.0, 7.0))
        _key_bone(arm, "LeftLowerArm", fr, rot_deg=(-15.0 + s * 4.0, 0.0, 0.0))
        _key_bone(arm, "IK_Foot.L", fr, Vector((0.0, 0.0, 0.0)))
        _key_bone(arm, "IK_Foot.R", fr, Vector((0.0, 0.0, 0.0)))


def animate_walk_ik(
    char_info: dict,
    fs: int,
    fe: int,
    ps,
    pe,
    yaw_deg: float,
    stride_m: float = None,
    step_height_m: float = 0.13,
    arm_amp_deg: float = 30.0,
):
    """
    True Grounded Walk Cycle using Foot IK:
    - During stance (55% of cycle), foot stays 100% locked flat on world Z (zero ground skate!).
    - During swing (45% of cycle), foot lifts in a crisp parabolic arc forward to next stride mark.
    - Root moves smoothly with ease-in start / ease-out stop and lands cleanly on both feet at fe.
    """
    setup_r15_hybrid_rig(char_info)
    arm = char_info["armature"]
    m = char_info["metrics"]
    if stride_m is None:
        stride_m = m["stride_m"]

    p0 = Vector(ps)
    p1 = Vector(pe)
    travel = p1 - p0
    dist_xy = math.hypot(travel.x, travel.y)
    cycles = max(1, int(round(dist_xy / max(0.25, stride_m))))
    span = max(1, fe - fs)

    _set_ik_influence(arm, fs, foot_l=1.0, foot_r=1.0, hand_l=0.0, hand_r=0.0)
    steps = cycles * 12
    rot_m = Euler((0.0, 0.0, math.radians(yaw_deg))).to_matrix()
    inv_rot = rot_m.inverted()
    leg_x = 0.255 * m["tw"] * STUD

    def world_foot_at(u_global: float, side_sgn: float):
        """
        Compute exact world (x, y, z) of Left/Right foot for walk progress u_global in [0..1].
        During stance, world X/Y stays mathematically constant (0.000m foot skate!).
        """
        rest_side = rot_m @ Vector((side_sgn * leg_x, 0.0, 0.0))
        half_steps = cycles * 2
        g = u_global * half_steps
        step_idx = min(half_steps - 1, int(math.floor(g)))
        frac = g - step_idx
        is_left = (side_sgn > 0)
        # Alternate swing steps: even steps move Left foot, odd steps move Right foot
        moving_this_step = ((step_idx % 2 == 0) == is_left)

        def foot_anchor_u(k_step: int) -> float:
            # Determine normalized path position of this foot after k_step half-steps
            own_moves = (k_step + (1 if is_left else 0)) // 2
            return min(1.0, own_moves / float(cycles))

        u_start = foot_anchor_u(step_idx)
        u_end = foot_anchor_u(step_idx + 1)
        if not moving_this_step or abs(u_end - u_start) < 1e-6:
            w_xy = p0.lerp(p1, u_start) + rest_side
            return Vector((w_xy.x, w_xy.y, p0.z))
        # Swing phase: smooth cubic horizontal advance + clean 0.13m parabolic toe clearance!
        s_u = 0.5 - 0.5 * math.cos(math.pi * frac)
        w_xy = p0.lerp(p1, u_start + (u_end - u_start) * s_u) + rest_side
        z_lift = 4.0 * step_height_m * frac * (1.0 - frac)
        return Vector((w_xy.x, w_xy.y, p0.z + z_lift))

    rest_l = arm.data.bones["IK_Foot.L"].head_local.copy()
    rest_r = arm.data.bones["IK_Foot.R"].head_local.copy()

    for i in range(steps + 1):
        t = i / float(steps)
        fr = int(round(fs + t * span))
        t_pos = 0.84 * t + 0.16 * (0.5 - 0.5 * math.cos(math.pi * t))
        env = min(1.0, t / 0.12) * min(1.0, (1.0 - t) / 0.12) if 0.0 < t < 1.0 else 0.0

        cur_root = p0.lerp(p1, t_pos)
        arm.location = cur_root
        arm.rotation_euler = Euler((0.0, 0.0, math.radians(yaw_deg)))
        arm.keyframe_insert("location", frame=fr)
        arm.keyframe_insert("rotation_euler", frame=fr)

        wl = world_foot_at(t_pos, +1.0)
        wr = world_foot_at(t_pos, -1.0)
        dl_char = inv_rot @ (wl - cur_root) - rest_l
        dr_char = inv_rot @ (wr - cur_root) - rest_r
        if i == 0 or i == steps:
            dl_char.z = 0.0; dr_char.z = 0.0
        _key_bone(arm, "IK_Foot.L", fr, dl_char)
        _key_bone(arm, "IK_Foot.R", fr, dr_char)

        ph = t * cycles * 2.0 * math.pi
        sw = math.sin(ph) * env
        bob_z = -0.042 * (1.0 - abs(math.cos(ph))) * env
        _key_bone(arm, "LowerTorso", fr, Vector((sw * 0.032, 0.0, bob_z)), (4.0 * env, sw * 2.5, sw * 6.0))
        _key_bone(arm, "UpperTorso", fr, rot_deg=(6.0 * env, -sw * 2.2, -sw * 7.5))
        _key_bone(arm, "Head", fr, rot_deg=(-4.0 * env, 0.0, sw * 3.0))
        _key_bone(arm, "LeftUpperArm", fr, rot_deg=(-sw * arm_amp_deg - 4.0 * env, 0.0, 6.0))
        _key_bone(arm, "LeftLowerArm", fr, rot_deg=(-16.0 - max(0.0, sw * 18.0), 0.0, 0.0))
        _key_bone(arm, "RightUpperArm", fr, rot_deg=(sw * arm_amp_deg - 4.0 * env, 0.0, -6.0))
        _key_bone(arm, "RightLowerArm", fr, rot_deg=(-16.0 - max(0.0, -sw * 18.0), 0.0, 0.0))


def animate_crouch_pickup(
    char_info: dict,
    fs: int,
    pick_fr: int,
    fe: int,
    target_world_m,
    hand: str = "R",
    crouch_m: float = 0.28,
):
    """
    Full-body squat & pickup with Foot IK locked flat on ground + Hand IK reaching exact world target!
    """
    setup_r15_hybrid_rig(char_info)
    arm = char_info["armature"]
    sn = "Right" if hand.upper() == "R" else "Left"
    ik_h = f"IK_Hand.{hand.upper()}"
    sgn = -1.0 if hand.upper() == "R" else 1.0

    # Convert world pickup point to character-space offset relative to resting wrist
    inv_arm = arm.matrix_world.inverted()
    tgt_char = inv_arm @ Vector(target_world_m)
    rest_wrist = arm.data.bones[ik_h].head_local.copy()
    reach_delta = tgt_char - rest_wrist

    _set_ik_influence(arm, fs, foot_l=1.0, foot_r=1.0)
    _set_ik_influence(arm, fs + 2, hand_l=(0.0 if hand.upper() == "R" else 1.0), hand_r=(1.0 if hand.upper() == "R" else 0.0), ramp=2)

    # Frame fs: start standing upright
    _key_bone(arm, "IK_Foot.L", fs, Vector((0, 0, 0)))
    _key_bone(arm, "IK_Foot.R", fs, Vector((0, 0, 0)))
    _key_bone(arm, "LowerTorso", fs, Vector((0, 0, 0)), (0, 0, 0))
    _key_bone(arm, "UpperTorso", fs, rot_deg=(2, 0, 0))
    _key_bone(arm, "Head", fs, rot_deg=(-2, 0, 0))
    _key_bone(arm, ik_h, fs, Vector((0, 0, 0)))

    # Anticipation lift (+3f) before bending down
    fa = fs + 4
    _key_bone(arm, "LowerTorso", fa, Vector((0, 0, 0.02)), (-4, 0, 0))
    _key_bone(arm, "UpperTorso", fa, rot_deg=(-6, 0, 0))

    # Peak crouch & hand contact at pick_fr (feet stay 0.000m glued!)
    _key_bone(arm, "IK_Foot.L", pick_fr, Vector((0, 0, 0)))
    _key_bone(arm, "IK_Foot.R", pick_fr, Vector((0, 0, 0)))
    _key_bone(arm, "LowerTorso", pick_fr, Vector((-sgn * 0.04, 0.08, -crouch_m)), (18, 0, sgn * 8))
    _key_bone(arm, "UpperTorso", pick_fr, rot_deg=(28, 0, sgn * 12))
    _key_bone(arm, "Head", pick_fr, rot_deg=(18, 0, -sgn * 6))
    _key_bone(arm, ik_h, pick_fr, reach_delta)
    # Hold contact briefly (+4f)
    _key_bone(arm, ik_h, min(fe - 4, pick_fr + 4), reach_delta)
    _key_bone(arm, "LowerTorso", min(fe - 4, pick_fr + 4), Vector((-sgn * 0.04, 0.08, -crouch_m)), (18, 0, sgn * 8))

    # Stand back up cleanly with overshoot settle
    _key_bone(arm, "IK_Foot.L", fe, Vector((0, 0, 0)))
    _key_bone(arm, "IK_Foot.R", fe, Vector((0, 0, 0)))
    _key_bone(arm, "LowerTorso", fe, Vector((0, 0, 0)), (0, 0, 0))
    _key_bone(arm, "UpperTorso", fe, rot_deg=(3, 0, 0))
    _key_bone(arm, "Head", fe, rot_deg=(-2, 0, 0))
    _set_ik_influence(arm, fe, hand_l=0.0, hand_r=0.0, ramp=5)


def bake_secondary_overlap(char_info: dict, fs: int, fe: int, lag_frames: int = 3, amp: float = 0.42):
    """
    Drive realistic inertia follow-through on Sec_Pony (long hair) & Sec_Scarf (cloth tails)
    from evaluated Head/UpperTorso motion across [fs..fe].
    """
    setup_r15_hybrid_rig(char_info)
    arm = char_info["armature"]
    sc = bpy.context.scene
    has_pony = "Sec_Pony" in arm.pose.bones
    has_scarf = "Sec_Scarf" in arm.pose.bones
    if not (has_pony or has_scarf):
        return

    head_rots = {}
    root_locs = {}
    for fr in range(fs, fe + 1):
        sc.frame_set(fr)
        pb_h = arm.pose.bones.get("Head")
        head_rots[fr] = (arm.matrix_world @ pb_h.matrix).to_euler("XYZ") if pb_h else Euler()
        root_locs[fr] = arm.matrix_world.translation.copy()

    for fr in range(fs, fe + 1):
        f_prev = max(fs, fr - lag_frames)
        # Angular & linear velocity lag creates whip opposite to sudden turns/stops!
        d_yaw = (head_rots[fr].z - head_rots[f_prev].z) * amp * 1.4
        d_pitch = (head_rots[fr].x - head_rots[f_prev].x) * amp
        vel = (root_locs[fr] - root_locs[f_prev])
        speed = math.hypot(vel.x, vel.y)
        trail_x = min(0.55, speed * 2.2)

        if has_pony:
            pb_p = arm.pose.bones["Sec_Pony"]
            pb_p.rotation_mode = "XYZ"
            pb_p.rotation_euler = Euler((trail_x - d_pitch, 0.0, -d_yaw))
            pb_p.keyframe_insert("rotation_euler", frame=fr)
        if has_scarf:
            pb_s = arm.pose.bones["Sec_Scarf"]
            pb_s.rotation_mode = "XYZ"
            pb_s.rotation_euler = Euler((trail_x * 0.85 - d_pitch * 0.7, 0.0, -d_yaw * 0.8))
            pb_s.keyframe_insert("rotation_euler", frame=fr)


def push_action_to_nla(
    arm_obj,
    action,
    track_name: str,
    start_frame: int,
    end_frame: int = None,
    blend_type: str = "REPLACE",
    blend_in: int = 6,
    blend_out: int = 6,
    time_scale: float = 1.0,
    repeat: float = 1.0,
):
    """Push a Blender 5.3 Slotted Action onto an NLA track with crossfade, repeat & slot binding."""
    arm_obj.animation_data_create()
    trk = arm_obj.animation_data.nla_tracks.get(track_name) or arm_obj.animation_data.nla_tracks.new()
    trk.name = track_name
    strip = trk.strips.new(action.name, int(start_frame), action)
    strip.blend_type = blend_type
    strip.blend_in = float(blend_in)
    strip.blend_out = float(blend_out)
    strip.scale = float(time_scale)
    strip.repeat = float(repeat)
    if end_frame is not None and end_frame > start_frame:
        strip.frame_end = float(end_frame)
    if hasattr(strip, "action_slot") and action.slots:
        strip.action_slot = action.slots[0]
    return strip


def push_current_action_to_nla(arm_obj, track_name: str, clip_name: str, start_frame: int, blend_type: str = "REPLACE", blend_in: int = 6, blend_out: int = 6):
    """Stash the currently active action on arm_obj down into an NLA track so multiple clips blend cleanly."""
    if not arm_obj.animation_data or not arm_obj.animation_data.action:
        return None
    act = arm_obj.animation_data.action
    act.name = clip_name
    act.use_fake_user = True
    arm_obj.animation_data.action = None
    return push_action_to_nla(arm_obj, act, track_name, start_frame, blend_type=blend_type, blend_in=blend_in, blend_out=blend_out)


def build_r15_mocap_map(src_arm, tgt_arm) -> dict:
    """
    Build an R15-aware Mixamo/BVH/UE -> Roblox R15 bone map covering LowerTorso & UpperTorso
    (fixing retarget.py auto-map gaps on Roblox R15 torso names).
    """
    if ANIM_SCRIPTS not in sys.path:
        sys.path.insert(0, ANIM_SCRIPTS)
    import retarget  # noqa: E402
    bmap, _ = retarget.auto_map(src_arm, tgt_arm)
    s_names = {b.name.lower(): b.name for b in src_arm.data.bones}

    def find_src(candidates):
        for cand in candidates:
            for low, real in s_names.items():
                if cand in low:
                    return real
        return None

    if "LowerTorso" in tgt_arm.data.bones and "LowerTorso" not in bmap:
        hit = find_src(["hips", "pelvis", "root"])
        if hit:
            bmap["LowerTorso"] = hit
    if "UpperTorso" in tgt_arm.data.bones and "UpperTorso" not in bmap:
        hit = find_src(["spine2", "upperchest", "chest", "spine1", "spine"])
        if hit:
            bmap["UpperTorso"] = hit
    return bmap


def retarget_mocap_to_r15(
    char_info: dict,
    anim_filepath: str,
    clip_name: str = None,
    frames=None,
    in_place: bool = False,
    target_fs: int = None,
    target_fe: int = None,
    push_nla: bool = True,
    repeat: float = 1.0,
):
    """
    Import a Mixamo .fbx or .bvh mocap clip, map cleanly onto Roblox R15 (LowerTorso/UpperTorso/limbs),
    automatically align T-pose / A-pose rest differences (so Mixamo arms don't cross inward through torso),
    scale hips motion by hip-height ratio, write a Blender 5.3 Slotted Action, and optionally push onto NLA.
    """
    setup_r15_hybrid_rig(char_info)
    anim_filepath = resolve_anim_path(anim_filepath)
    tgt = char_info["armature"]
    ext = os.path.splitext(anim_filepath)[1].lower()
    before = set(bpy.data.objects)
    if ext == ".bvh":
        bpy.ops.import_anim.bvh(filepath=anim_filepath, global_scale=0.01, rotate_mode="NATIVE", update_scene_fps=False)
    elif ext == ".fbx":
        bpy.ops.import_scene.fbx(filepath=anim_filepath, automatic_bone_orientation=True)
    else:
        raise ValueError(f"Unsupported mocap extension: {ext}")

    added = [o for o in bpy.data.objects if o not in before]
    src = next((o for o in added if o.type == "ARMATURE"), None)
    if src is None:
        raise RuntimeError(f"No armature found in {anim_filepath}")

    bmap = build_r15_mocap_map(src, tgt)
    bmap = {t: s for t, s in bmap.items() if t in tgt.data.bones and s in src.data.bones}
    if not bmap:
        raise ValueError(f"No R15 bones mapped from {anim_filepath}")
    hips = "LowerTorso" if "LowerTorso" in bmap else None

    act_src = src.animation_data.action if src.animation_data else None
    if frames:
        f0, f1 = int(frames[0]), int(frames[1])
    elif act_src:
        f0, f1 = (int(round(v)) for v in act_src.frame_range)
    else:
        f0, f1 = 1, 30

    def _rot(mat):
        return mat.to_3x3().normalized().to_quaternion()

    sc = bpy.context.scene
    tw_rot = _rot(tgt.matrix_world)
    order = sorted(tgt.data.bones, key=lambda b: len(b.parent_recursive))
    rest_rel = {
        b.name: (b.parent.matrix_local.inverted() @ b.matrix_local if b.parent else b.matrix_local.copy())
        for b in order
    }
    t_rest_w = {b: _rot(tgt.matrix_world @ tgt.data.bones[b].matrix_local) for b in bmap}

    # Align T-pose / A-pose limb rest orientation differences (crucial for Mixamo T-pose -> Roblox I-pose arms!)
    s_rest_w = {}
    for tb, sb in bmap.items():
        sr = _rot(src.matrix_world @ src.data.bones[sb].matrix_local)
        if any(k in tb for k in ("UpperArm", "LowerArm", "UpperLeg", "LowerLeg")):
            s_dir = ((src.matrix_world @ src.data.bones[sb].tail_local) - (src.matrix_world @ src.data.bones[sb].head_local)).normalized()
            t_dir = ((tgt.matrix_world @ tgt.data.bones[tb].tail_local) - (tgt.matrix_world @ tgt.data.bones[tb].head_local)).normalized()
            if s_dir.length > 1e-4 and t_dir.length > 1e-4:
                q_fix = s_dir.rotation_difference(t_dir)
                sr = q_fix @ sr
        s_rest_w[sb] = sr

    ratio = 1.0
    if hips:
        s_hips_rest = src.matrix_world @ src.data.bones[bmap[hips]].head_local
        t_hips_rest = tgt.matrix_world @ tgt.data.bones[hips].head_local
        ratio = t_hips_rest.z / s_hips_rest.z if abs(s_hips_rest.z) > 1e-6 else 1.0

    keys = {b: [] for b in bmap}
    locs = []
    err = 0.0
    for f in range(f0, f1 + 1):
        sc.frame_set(f)
        pose = {}
        for b in order:
            M_parent = pose.get(b.parent.name, Matrix.Identity(4)) if b.parent else Matrix.Identity(4)
            base = M_parent @ rest_rel[b.name]
            if b.name not in bmap:
                pose[b.name] = base
                continue
            s = bmap[b.name]
            sw = _rot(src.matrix_world @ src.pose.bones[s].matrix)
            dw = sw @ s_rest_w[s].inverted() @ t_rest_w[b.name]
            da = tw_rot.inverted() @ dw
            lq = _rot(base).inverted() @ da
            prev = keys[b.name][-1][1] if keys[b.name] else None
            if prev is not None and lq.dot(prev) < 0:
                lq.negate()
            loc = Vector()
            if b.name == hips and not in_place:
                hs = src.matrix_world @ src.pose.bones[s].head
                want_w = t_hips_rest + (hs - s_hips_rest) * ratio
                want_a = tgt.matrix_world.inverted() @ want_w
                loc = base.to_3x3().inverted() @ (want_a - base.translation)
                locs.append((f, loc.copy()))
            pose[b.name] = base @ Matrix.Translation(loc) @ lq.to_matrix().to_4x4()
            keys[b.name].append((f, lq))
            got = tw_rot @ _rot(pose[b.name])
            ang = (got @ t_rest_w[b.name].inverted()).rotation_difference(sw @ s_rest_w[s].inverted()).angle
            err = max(err, math.degrees(min(ang, 2.0 * math.pi - ang)))

    cname = clip_name or os.path.splitext(os.path.basename(anim_filepath))[0]
    act = bpy.data.actions.new(f"{tgt.name}|{cname}")
    act.use_fake_user = True
    tgt.animation_data_create()
    tgt.animation_data.action = act
    slot = tgt.animation_data.action_slot or act.slots.new(id_type="OBJECT", name=tgt.name)
    tgt.animation_data.action_slot = slot
    cb = anim_utils.action_ensure_channelbag_for_slot(act, slot)

    lin_val = bpy.types.Keyframe.bl_rna.properties["interpolation"].enum_items["LINEAR"].value
    def _write_fc(path, idx, group, pts):
        fc = cb.fcurves.ensure(path, index=idx, group_name=group)
        fc.keyframe_points.add(len(pts))
        fc.keyframe_points.foreach_set("co", [v for p in pts for v in p])
        fc.keyframe_points.foreach_set("interpolation", [lin_val] * len(pts))
        fc.update()

    for b, ks in keys.items():
        tgt.pose.bones[b].rotation_mode = "QUATERNION"
        for i in range(4):
            _write_fc(f'pose.bones["{b}"].rotation_quaternion', i, b, [(f, q[i]) for f, q in ks])
    if locs:
        for i in range(3):
            _write_fc(f'pose.bones["{hips}"].location', i, hips, [(f, v[i]) for f, v in locs])

    for o in added:
        bpy.data.objects.remove(o, do_unlink=True)

    res = {
        "ok": True, "action": act.name, "frames": [f0, f1], "mapped": len(bmap),
        "hips": hips, "hips_scale": round(ratio, 4), "max_error_deg": round(err, 3),
    }

    if push_nla and act and target_fs is not None:
        src_len = max(1.0, float(f1 - f0))
        t_scale = ((target_fe - target_fs) / (src_len * max(1.0, repeat))) if target_fe else 1.0
        _set_ik_influence(tgt, target_fs, foot_l=0.0, foot_r=0.0, hand_l=0.0, hand_r=0.0)
        tgt.animation_data.action = None
        push_action_to_nla(tgt, act, "Mocap_Base", target_fs, end_frame=target_fe, blend_type="REPLACE", time_scale=t_scale, repeat=repeat)
    return act, res

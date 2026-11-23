#!/usr/bin/env python3
"""
render_dispatcher.py — Stage R5 Dual-Mode Render Dispatcher for @RobloxDirector (Sven Core).

Unifies Stage R5 30fps rendering across two execution targets so heavy renders never block
the user's local workstation unless explicitly requested:

1. Mode R5-A (`--target local`):
   - Renders directly on the local GPU (e.g., RTX 3060) from `output/<slug>/scene_built.blend`
     (or the project build script), staging frames via `%TEMP%/sven_blender_<slug>/shots` with
     live 15-second sync to `output/<slug>/shots/`, automatic resume of existing frames, and
     final video assembly via `tools/compile_video.py`.

2. Mode R5-B (`--target external` / `--target pack`):
   - Offloads rendering to any third-party GPU provider specified by the user (Google Cloud /
     Colab, RunPod, Vast.ai, Kaggle, AWS/GCP VM, SSH server, or custom HTTP tunnel).
   - `--action pack`: Produces a self-contained, cross-platform portable render bundle
     (`output/<slug>/<slug>_render_bundle.zip`) containing:
       * `scene_built.blend` (with all textures packed),
       * `director_plan.json`, `srt_shots.json`, `words.json`, `caps.ass`, `voice.mp3`,
       * `universal_render_worker.py` (standalone Linux/Windows Blender 5.3 OPTIX/CUDA worker
         with auto path-remapping, frame-range sharding `--frame-start/--frame-end`, resume
         support, and automatic `compile_video.py` final assembly),
       * Core toolkit scripts (`.agents/skills/roblox-director/tools/compile_video.py`, etc.).
   - `--action dispatch --provider http_tunnel --url <tunnel_url>`: Streams batch render jobs
     to a remote HTTP/Cloudflare tunnel GPU worker with built-in Cost Guardrails (`--allow-paid`,
     `--max-cost-vnd`), saves every frame batch locally to `output/<slug>/shots/`, and runs
     `compile_video.py`.
   - `--action dispatch --provider ssh --host <user@host>`: Pushes the portable render bundle
     over SCP/SSH, runs `universal_render_worker.py` on the remote third-party GPU, and pulls
     back the rendered output.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROBLOX_SKILL_ROOT = os.path.normpath(os.path.join(HERE, ".."))
BLENDER_CORE_SCRIPTS = os.path.normpath(os.path.join(ROBLOX_SKILL_ROOT, "..", "blender-core", "scripts"))
REPO_ROOT = os.path.normpath(os.path.join(ROBLOX_SKILL_ROOT, "..", "..", ".."))
OUTPUT_ROOT = os.path.join(REPO_ROOT, "output")
URL_CACHE_FILE = os.path.join(OUTPUT_ROOT, ".remote_gpu_url.txt")

if BLENDER_CORE_SCRIPTS not in sys.path:
    sys.path.insert(0, BLENDER_CORE_SCRIPTS)

try:
    from run_in_blender import find_blender
except ImportError:
    def find_blender():
        default = r"C:\Program Files\Blender Foundation\Blender 5.3\blender.exe"
        return default if os.path.isfile(default) else shutil.which("blender")

GPU_HOURLY_USD = {
    "T4": 0.00,
    "L4": 0.24,
    "A100": 1.10,
    "V100": 0.55,
    "RTX 4090": 0.44,
    "RTX 3090": 0.22,
}
USD_TO_VND = 25500


UNIVERSAL_WORKER_TEMPLATE = '''#!/usr/bin/env python3
"""
universal_render_worker.py — Standalone Cross-Platform Blender 5.3 GPU Render Worker.
Generated automatically by Sven Core `tools/render_dispatcher.py`.

Can run inside Blender (`blender -b scene_built.blend -P universal_render_worker.py -- ...`)
or as a standalone host script on any third-party Linux/Windows GPU server (Google Cloud,
Colab, RunPod, Vast.ai, AWS/GCP, or local machine).
"""
import argparse
import json
import os
import subprocess
import sys
import time

try:
    import bpy
    INSIDE_BLENDER = True
except ImportError:
    INSIDE_BLENDER = False

HERE = os.path.dirname(os.path.abspath(__file__))


def _shot_folder_for_frame(fr_idx: int, fps: float, srt_shots: list) -> str:
    t_sec = (fr_idx - 1) / float(fps)
    for s in srt_shots:
        if float(s["window_start"]) - 1e-4 <= t_sec < float(s["window_end"]) - 1e-4:
            return f"s{int(s['index']):02d}"
    return f"s{int(srt_shots[-1]['index']):02d}"


def run_inside_blender(args):
    # 1. Auto-remap any unpacked texture paths from Windows to current host layout
    for img in bpy.data.images:
        if img.filepath and not img.packed_file:
            rel = img.filepath.replace("\\\\", "/")
            for marker in (".agents/", "assets/"):
                if marker in rel:
                    sub = rel[rel.index(marker):]
                    cand = os.path.join(HERE, sub)
                    if os.path.isfile(cand):
                        img.filepath = cand
                        try:
                            img.reload()
                        except Exception:
                            pass

    plan_path = os.path.join(HERE, "director_plan.json")
    srt_path = os.path.join(HERE, "srt_shots.json")
    sc = bpy.context.scene
    has_srt = os.path.isfile(plan_path) and os.path.isfile(srt_path)
    if has_srt:
        plan = json.load(open(plan_path, encoding="utf-8"))
        srt_shots = json.load(open(srt_path, encoding="utf-8"))["shots"]
        fps = float(plan.get("fps", sc.render.fps or 30))
        total_frames = int(round(plan["runtime"] * fps))
    else:
        srt_shots = []
        fps = float(sc.render.fps or 30)
        total_frames = int(sc.frame_end or 300)

    if args.engine:
        sc.render.engine = args.engine

    active_backend = "EEVEE"
    if sc.render.engine == "CYCLES":
        prefs = bpy.context.preferences.addons["cycles"].preferences
        active_backend = "CPU"
        for backend in ("OPTIX", "CUDA", "HIP", "METAL", "ONEAPI"):
            try:
                prefs.compute_device_type = backend
                prefs.get_devices()
                gpu_devs = [d for d in prefs.devices if d.type != "CPU"]
                if gpu_devs:
                    for d in prefs.devices:
                        d.use = (d.type != "CPU")
                    active_backend = backend
                    break
            except Exception:
                continue
        sc.cycles.device = "GPU" if active_backend != "CPU" else "CPU"
        sc.cycles.samples = int(args.samples)
        sc.cycles.adaptive_threshold = 0.04
        sc.cycles.max_bounces = 3
        sc.cycles.diffuse_bounces = 2
        sc.cycles.glossy_bounces = 2
        sc.render.use_persistent_data = True
        try:
            sc.cycles.denoiser = "OPENIMAGEDENOISE"
        except Exception:
            pass
    else:
        sc.render.use_persistent_data = True
        if hasattr(sc, "eevee"):
            if hasattr(sc.eevee, "taa_render_samples"):
                sc.eevee.taa_render_samples = int(args.samples)
            if hasattr(sc.eevee, "use_raytracing"):
                sc.eevee.use_raytracing = True
            if hasattr(sc.eevee, "use_gtao"):
                sc.eevee.use_gtao = True

    if args.width > 0 and args.height > 0:
        sc.render.resolution_x = args.width
        sc.render.resolution_y = args.height
    sc.render.image_settings.file_format = "PNG"

    shots_dir = os.path.join(HERE, "shots")
    frames_dir = os.path.join(HERE, "frames")
    if has_srt:
        os.makedirs(shots_dir, exist_ok=True)
    else:
        os.makedirs(frames_dir, exist_ok=True)

    f_start = max(1, int(args.frame_start or sc.frame_start or 1))
    f_end = min(total_frames, int(args.frame_end or total_frames))
    if args.frames:
        frame_list = [int(x) for x in args.frames.split(",") if x.strip()]
    else:
        frame_list = list(range(f_start, f_end + 1))

    print(f"@@START@@ total={len(frame_list)} range={f_start}..{f_end} backend={active_backend}", flush=True)
    t0 = time.time()
    rendered = 0
    for fr in frame_list:
        if has_srt:
            sf = _shot_folder_for_frame(fr, fps, srt_shots)
            s_dir = os.path.join(shots_dir, sf)
            os.makedirs(s_dir, exist_ok=True)
            out_fp = os.path.join(s_dir, f"frame_{fr:05d}.png")
        else:
            out_fp = os.path.join(frames_dir, f"{fr:05d}.png")
        if not args.force and os.path.isfile(out_fp) and os.path.getsize(out_fp) > 1000:
            print(f"@@SKIP@@ {fr}", flush=True)
            continue
        t_fr = time.time()
        sc.frame_set(fr)
        sc.render.filepath = out_fp
        bpy.ops.render.render(write_still=True)
        dt_fr = time.time() - t_fr
        rendered += 1
        avg_fr = (time.time() - t0) / max(1, rendered)
        print(f"@@DONE@@ {fr} {dt_fr:.2f} avg={avg_fr:.2f}", flush=True)


def run_host_cli(args):
    blender_bin = args.blender or os.environ.get("BLENDER_EXE") or "blender"
    blend_file = os.path.join(HERE, "scene_built.blend")
    if not os.path.isfile(blend_file):
        raise FileNotFoundError(f"scene_built.blend not found in {HERE}")
    cmd = [
        blender_bin,
        "-b",
        blend_file,
        "--python-exit-code",
        "1",
        "-P",
        os.path.abspath(__file__),
        "--",
        "--samples",
        str(args.samples),
        "--frame-start",
        str(args.frame_start),
        "--frame-end",
        str(args.frame_end),
    ]
    if args.engine:
        cmd += ["--engine", args.engine]
    if args.frames:
        cmd += ["--frames", args.frames]
    if args.force:
        cmd.append("--force")
    subprocess.run(cmd, check=True)

    if not args.skip_compile:
        plan_path = os.path.join(HERE, "director_plan.json")
        srt_path = os.path.join(HERE, "srt_shots.json")
        if os.path.isfile(plan_path) and os.path.isfile(srt_path) and os.path.isfile(os.path.join(HERE, "compile_video.py")):
            plan = json.load(open(plan_path, encoding="utf-8"))
            aspect = plan.get("aspect", "9:16")
            compile_cmd = [
                sys.executable,
                os.path.join(HERE, "compile_video.py"),
                "--project-dir",
                HERE,
                "--voice",
                "voice.mp3",
                "--shots",
                "srt_shots.json",
                "--frames-dir",
                "shots",
                "--subs",
                "caps.ass",
                "--aspect",
                aspect,
                "--out",
                "final.mp4",
            ]
            subprocess.run(compile_cmd, check=True)
        elif os.path.isfile(os.path.join(HERE, "make_video.py")):
            subprocess.run([sys.executable, os.path.join(HERE, "make_video.py")], check=True)


def main():
    argv = sys.argv[sys.argv.index("--") + 1 :] if INSIDE_BLENDER and "--" in sys.argv else sys.argv[1:]
    ap = argparse.ArgumentParser(description="Universal Blender 5.3 GPU Render Worker")
    ap.add_argument("--blender", default="", help="Path to blender binary when running from host shell")
    ap.add_argument("--engine", default="", choices=["", "CYCLES", "BLENDER_EEVEE"])
    ap.add_argument("--samples", type=int, default=16)
    ap.add_argument("--width", type=int, default=0)
    ap.add_argument("--height", type=int, default=0)
    ap.add_argument("--frame-start", type=int, default=0)
    ap.add_argument("--frame-end", type=int, default=0)
    ap.add_argument("--frames", default="", help="Optional comma-separated list of frame numbers")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--skip-compile", action="store_true")
    args = ap.parse_args(argv)

    if INSIDE_BLENDER:
        run_inside_blender(args)
    else:
        run_host_cli(args)


if __name__ == "__main__":
    main()
'''


def get_missing_frames(proj_dir: str, total_frames: int, fps: int, srt_shots: list) -> list[int]:
    def _shot_folder(fr_idx: int) -> str:
        t_sec = (fr_idx - 1) / float(fps)
        for s in srt_shots:
            if float(s["window_start"]) - 1e-4 <= t_sec < float(s["window_end"]) - 1e-4:
                return f"s{int(s['index']):02d}"
        return f"s{int(srt_shots[-1]['index']):02d}"

    missing = []
    shots_dir = os.path.join(proj_dir, "shots")
    for fr in range(1, total_frames + 1):
        sf = _shot_folder(fr)
        fp = os.path.join(shots_dir, sf, f"frame_{fr:05d}.png")
        if not (os.path.isfile(fp) and os.path.getsize(fp) > 1000):
            missing.append(fr)
    return missing


def inspect_project_status(slug: str) -> dict:
    """Inspect a project's Stage R4/R5 readiness, missing frame count, and bundle status."""
    proj_dir = os.path.join(OUTPUT_ROOT, slug)
    if not os.path.isdir(proj_dir):
        raise FileNotFoundError(f"Project directory not found: {proj_dir}")

    blend_path = os.path.join(proj_dir, "scene_built.blend")
    plan_path = os.path.join(proj_dir, "director_plan.json")
    srt_path = os.path.join(proj_dir, "srt_shots.json")

    total_frames = 0
    fps = 30
    aspect = "9:16"
    missing_count = 0
    if os.path.isfile(plan_path) and os.path.isfile(srt_path):
        plan = json.load(open(plan_path, encoding="utf-8"))
        srt_shots = json.load(open(srt_path, encoding="utf-8"))["shots"]
        fps = int(plan.get("fps", 30))
        aspect = plan.get("aspect", "9:16")
        total_frames = int(round(plan["runtime"] * fps))
        missing = get_missing_frames(proj_dir, total_frames, fps, srt_shots)
        missing_count = len(missing)
    else:
        frames_dir = os.path.join(proj_dir, "frames")
        done_pngs = [f for f in os.listdir(frames_dir) if f.endswith(".png")] if os.path.isdir(frames_dir) else []
        build_py = os.path.join(proj_dir, "build_scene.py")
        if os.path.isfile(build_py):
            txt = open(build_py, encoding="utf-8", errors="ignore").read()
            import re
            m_nf = re.search(r"NF\s*=\s*(\d+),\s*(\d+)", txt) or re.search(r"NF\s*=\s*(\d+)", txt)
            if m_nf:
                total_frames = int(m_nf.group(2) if m_nf.lastindex == 2 else m_nf.group(1))
        if total_frames == 0:
            total_frames = len(done_pngs)
        missing_count = max(0, total_frames - len(done_pngs))

    return {
        "slug": slug,
        "project_dir": proj_dir,
        "has_scene_built_blend": os.path.isfile(blend_path),
        "blend_size_mb": round(os.path.getsize(blend_path) / (1024 * 1024), 2) if os.path.isfile(blend_path) else 0.0,
        "fps": fps,
        "aspect": aspect,
        "total_frames": total_frames,
        "completed_frames": total_frames - missing_count,
        "missing_frames": missing_count,
    }


def package_portable_bundle(slug: str, include_existing_shots: bool = False) -> dict:
    """Create a self-contained portable render ZIP for any third-party GPU provider."""
    proj_dir = os.path.join(OUTPUT_ROOT, slug)
    if not os.path.isdir(proj_dir):
        raise FileNotFoundError(f"Project directory not found: {proj_dir}")

    worker_path = os.path.join(proj_dir, "universal_render_worker.py")
    with open(worker_path, "w", encoding="utf-8") as f:
        f.write(UNIVERSAL_WORKER_TEMPLATE)

    compile_src = os.path.join(HERE, "compile_video.py")
    compile_dst = os.path.join(proj_dir, "compile_video.py")
    if os.path.isfile(compile_src):
        shutil.copy2(compile_src, compile_dst)

    bundle_path = os.path.join(proj_dir, f"{slug}_render_bundle.zip")
    skip_dirs = {"preview", "final_picks", "qa", "playblast_frames", "__pycache__"}
    if not include_existing_shots:
        skip_dirs.update({"shots", "frames"})

    allowed_exts = {
        ".blend", ".py", ".json", ".srt", ".ass", ".mp3", ".wav",
        ".txt", ".md", ".glb", ".fbx", ".obj", ".hdr", ".exr", ".png", ".jpg",
    }
    file_count = 0
    with zipfile.ZipFile(bundle_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(proj_dir):
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            for fname in files:
                if fname.endswith(("_render_bundle.zip", ".mp4", ".blend1")) or fname.startswith(("chk_sheet", "preview_sheet", "final_sheet")):
                    continue
                ext = os.path.splitext(fname)[1].lower()
                if ext not in allowed_exts:
                    continue
                fp = os.path.join(root, fname)
                rel = os.path.relpath(fp, proj_dir).replace("\\", "/")
                ctype = (
                    zipfile.ZIP_STORED
                    if ext in {".png", ".jpg", ".mp3", ".glb", ".fbx"}
                    else zipfile.ZIP_DEFLATED
                )
                zf.write(fp, rel, compress_type=ctype)
                file_count += 1

    status = inspect_project_status(slug)
    status.update(
        {
            "bundle_zip": bundle_path,
            "bundle_size_mb": round(os.path.getsize(bundle_path) / (1024 * 1024), 2),
            "bundled_files": file_count,
            "worker_script": worker_path,
            "third_party_cli_command": "python3 universal_render_worker.py --samples 16",
        }
    )
    return status


def run_local_render(slug: str, samples: int = 16, engine: str = "", max_frames: int = 0, skip_compile: bool = False) -> dict:
    """Execute Mode R5-A: Render directly on the local GPU with %TEMP% staging and auto-resume."""
    proj_dir = os.path.join(OUTPUT_ROOT, slug)
    blend_path = os.path.join(proj_dir, "scene_built.blend")
    if not os.path.isfile(blend_path):
        raise FileNotFoundError(
            f"scene_built.blend not found in {proj_dir}. Run the Stage R4 build script first."
        )

    blender_exe = find_blender()
    if not blender_exe:
        raise RuntimeError("Blender 5.3 executable not found on local machine.")

    # Stage inside %TEMP% for Windows OpenImageIO safety
    stage_dir = os.path.join(tempfile.gettempdir(), f"sven_blender_{slug}")
    os.makedirs(stage_dir, exist_ok=True)
    for fname in ("scene_built.blend", "director_plan.json", "srt_shots.json", "make_video.py"):
        src = os.path.join(proj_dir, fname)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(stage_dir, fname))

    worker_path = os.path.join(stage_dir, "universal_render_worker.py")
    with open(worker_path, "w", encoding="utf-8") as f:
        f.write(UNIVERSAL_WORKER_TEMPLATE)

    for dname in ("shots", "frames"):
        if os.path.isdir(os.path.join(proj_dir, dname)):
            shutil.copytree(os.path.join(proj_dir, dname), os.path.join(stage_dir, dname), dirs_exist_ok=True)

    cmd = [
        blender_exe,
        "-b",
        os.path.join(stage_dir, "scene_built.blend"),
        "--python-exit-code",
        "1",
        "-P",
        worker_path,
        "--",
        "--samples",
        str(samples),
    ]
    if engine:
        cmd += ["--engine", engine]
    if max_frames > 0:
        cmd += ["--frame-start", "1", "--frame-end", str(max_frames)]

    stop_evt = threading.Event()

    def _bg_sync():
        while not stop_evt.wait(15.0):
            for dname in ("shots", "frames"):
                if os.path.isdir(os.path.join(stage_dir, dname)):
                    shutil.copytree(os.path.join(stage_dir, dname), os.path.join(proj_dir, dname), dirs_exist_ok=True)

    t_sync = threading.Thread(target=_bg_sync, daemon=True)
    t_sync.start()

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", bufsize=1)
    for line in proc.stdout:
        s = line.strip()
        if s.startswith("@@"):
            print(s, flush=True)
    ret = proc.wait()
    stop_evt.set()
    t_sync.join(timeout=2.0)

    for dname in ("shots", "frames"):
        if os.path.isdir(os.path.join(stage_dir, dname)):
            shutil.copytree(os.path.join(stage_dir, dname), os.path.join(proj_dir, dname), dirs_exist_ok=True)

    if ret != 0:
        raise RuntimeError(f"Local Blender render exited with code {ret}")

    if not skip_compile and max_frames == 0:
        plan_path = os.path.join(proj_dir, "director_plan.json")
        if os.path.isfile(plan_path):
            plan = json.load(open(plan_path, encoding="utf-8"))
            aspect = plan.get("aspect", "9:16")
            compile_py = os.path.join(HERE, "compile_video.py")
            subprocess.run(
                [
                    sys.executable,
                    compile_py,
                    "--project-dir",
                    proj_dir,
                    "--voice",
                    "voice.mp3",
                    "--shots",
                    "srt_shots.json",
                    "--frames-dir",
                    "shots",
                    "--subs",
                    "caps.ass",
                    "--aspect",
                    aspect,
                    "--out",
                    "final.mp4",
                ],
                check=True,
            )
        elif os.path.isfile(os.path.join(proj_dir, "make_video.py")):
            subprocess.run([sys.executable, os.path.join(proj_dir, "make_video.py")], check=True)
    return inspect_project_status(slug)


def run_external_dispatch(
    slug: str,
    provider: str = "bundle_only",
    url: str = "",
    ssh_host: str = "",
    remote_dir: str = "/tmp/sven_render",
    samples: int = 16,
    batch_size: int = 25,
    max_frames: int = 0,
    allow_paid: bool = False,
    max_cost_vnd: int = 20000,
    skip_compile: bool = False,
) -> dict:
    """Execute Mode R5-B: Package and dispatch render to a third-party external GPU provider."""
    bundle_info = package_portable_bundle(slug)
    proj_dir = bundle_info["project_dir"]

    if provider == "bundle_only":
        return bundle_info

    if provider == "http_tunnel":
        legacy_client = os.path.join(OUTPUT_ROOT, "remote_gpu_client.py")
        if not os.path.isfile(legacy_client):
            raise FileNotFoundError(f"HTTP tunnel client not found at {legacy_client}")
        cmd = [
            sys.executable,
            legacy_client,
            "--slug",
            slug,
            "--mode",
            "final",
            "--samples",
            str(samples),
            "--batch-size",
            str(batch_size),
            "--max-cost-vnd",
            str(max_cost_vnd),
        ]
        if url:
            cmd += ["--url", url]
        if max_frames > 0:
            cmd += ["--max-frames", str(max_frames)]
        if allow_paid:
            cmd.append("--allow-paid")
        if skip_compile:
            cmd.append("--skip-compile")
        subprocess.run(cmd, check=True)
        return inspect_project_status(slug)

    if provider == "ssh":
        if not ssh_host:
            raise ValueError("--ssh-host (e.g. root@gpu-host -p 22) is required for provider=ssh")
        bundle_zip = bundle_info["bundle_zip"]
        subprocess.run(["ssh", ssh_host, f"mkdir -p {remote_dir}"], check=True)
        subprocess.run(["scp", bundle_zip, f"{ssh_host}:{remote_dir}/bundle.zip"], check=True)
        remote_cmd = (
            f"cd {remote_dir} && unzip -o -q bundle.zip && "
            f"python3 universal_render_worker.py --samples {samples} --skip-compile && "
            f"zip -r -q shots_out.zip shots/"
        )
        subprocess.run(["ssh", ssh_host, remote_cmd], check=True)
        local_shots_zip = os.path.join(proj_dir, "shots_out.zip")
        subprocess.run(["scp", f"{ssh_host}:{remote_dir}/shots_out.zip", local_shots_zip], check=True)
        with zipfile.ZipFile(local_shots_zip, "r") as zf:
            zf.extractall(proj_dir)
        os.remove(local_shots_zip)
        if not skip_compile:
            plan = json.load(open(os.path.join(proj_dir, "director_plan.json"), encoding="utf-8"))
            aspect = plan.get("aspect", "9:16")
            subprocess.run(
                [
                    sys.executable,
                    os.path.join(HERE, "compile_video.py"),
                    "--project-dir",
                    proj_dir,
                    "--voice",
                    "voice.mp3",
                    "--shots",
                    "srt_shots.json",
                    "--frames-dir",
                    "shots",
                    "--subs",
                    "caps.ass",
                    "--aspect",
                    aspect,
                    "--out",
                    "final.mp4",
                ],
                check=True,
            )
        return inspect_project_status(slug)

    raise ValueError(f"Unsupported external provider: {provider}")


def run_studio_render(
    slug: str,
    quality: str = "hd",
    aspect: str = "9:16",
    shots: list[str] = None,
    force: bool = False,
    skip_compile: bool = False,
) -> dict:
    """Execute Mode R5-Studio: Queue & capture 30fps shots directly inside Roblox Studio MCP (`bridge.mjs`)."""
    proj_dir = os.path.join(OUTPUT_ROOT, slug)
    srt_path = os.path.join(proj_dir, "srt_shots.json")
    if not os.path.isfile(srt_path):
        raise FileNotFoundError(f"srt_shots.json not found in {proj_dir}")

    studio_kit_dir = os.path.join(ROBLOX_SKILL_ROOT, "studio_kit")
    srt_data = json.load(open(srt_path, encoding="utf-8"))
    shot_ids = shots or [s.get("shot_id") or f"s{int(s['index']):02d}" for s in srt_data.get("shots", [])]

    if aspect == "16:9" or quality == "1x":
        render_script = os.path.join(studio_kit_dir, "render.py")
        out_prefix = os.path.join(proj_dir, "shots")
    elif quality == "4k":
        render_script = os.path.join(studio_kit_dir, "render4k.py")
        out_prefix = os.path.join(proj_dir, "frames4k")
    else:
        render_script = os.path.join(studio_kit_dir, "render2.py")
        out_prefix = os.path.join(proj_dir, "frames2")

    cmd = [sys.executable, render_script, "--shots", srt_path, "--out-prefix", out_prefix, *shot_ids]
    if force:
        cmd.append("force")
    subprocess.run(cmd, check=True)
    return {
        "slug": slug,
        "engine": "Roblox_Studio_MCP",
        "quality": quality,
        "aspect": aspect,
        "queued_shots": shot_ids,
        "queue_dir": os.path.join(studio_kit_dir, "queue"),
        "note": "Jobs queued for studio_kit/bridge.mjs. For tiled 9:16 (hd/4k), run stitch.py / stitch4k.py after capture finishes, then compile_video.py.",
    }


def main():
    ap = argparse.ArgumentParser(description="Sven Core Stage R5 Tri-Mode Render Dispatcher (Roblox Studio / Local Blender / 3rd-Party External GPU)")
    ap.add_argument("--slug", required=True, help="Project folder under output/<slug>")
    ap.add_argument(
        "--target",
        choices=["status", "studio", "local", "external", "pack"],
        default="status",
        help="Execution target: 'status' (inspect), 'studio' (Mode R5-Studio Roblox Studio MCP capture), 'local' (Mode R5-A Local Blender GPU), 'pack' (build 3rd-party bundle), or 'external' (Mode R5-B 3rd-Party GPU)",
    )
    ap.add_argument(
        "--studio-quality",
        choices=["1x", "hd", "4k"],
        default="hd",
        help="Capture mode when --target studio is used: '1x' (single capture), 'hd' (2-tile 9:16 via render2.py), or '4k' (multi-tile via render4k.py)",
    )
    ap.add_argument(
        "--provider",
        choices=["bundle_only", "http_tunnel", "ssh"],
        default="bundle_only",
        help="Third-party provider connector when --target external is selected",
    )
    ap.add_argument("--url", default="", help="Remote HTTP/Cloudflare tunnel URL for provider=http_tunnel")
    ap.add_argument("--ssh-host", default="", help="SSH host for provider=ssh (e.g. root@1.2.3.4)")
    ap.add_argument("--remote-dir", default="/tmp/sven_render", help="Remote working directory for provider=ssh")
    ap.add_argument("--engine", default="", choices=["", "CYCLES", "BLENDER_EEVEE"])
    ap.add_argument("--samples", type=int, default=16)
    ap.add_argument("--batch-size", type=int, default=25)
    ap.add_argument("--max-frames", type=int, default=0)
    ap.add_argument("--allow-paid", action="store_true")
    ap.add_argument("--max-cost-vnd", type=int, default=20000)
    ap.add_argument("--skip-compile", action="store_true")
    args = ap.parse_args()

    if args.target == "status":
        res = inspect_project_status(args.slug)
    elif args.target == "studio":
        st = inspect_project_status(args.slug)
        res = run_studio_render(
            args.slug,
            quality=args.studio_quality,
            aspect=st.get("aspect", "9:16"),
            skip_compile=args.skip_compile,
        )
    elif args.target == "pack":
        res = package_portable_bundle(args.slug)
    elif args.target == "local":
        res = run_local_render(
            args.slug,
            samples=args.samples,
            engine=args.engine,
            max_frames=args.max_frames,
            skip_compile=args.skip_compile,
        )
    elif args.target == "external":
        res = run_external_dispatch(
            args.slug,
            provider=args.provider,
            url=args.url,
            ssh_host=args.ssh_host,
            remote_dir=args.remote_dir,
            samples=args.samples,
            batch_size=args.batch_size,
            max_frames=args.max_frames,
            allow_paid=args.allow_paid,
            max_cost_vnd=args.max_cost_vnd,
            skip_compile=args.skip_compile,
        )
    else:
        raise ValueError(f"Unknown target: {args.target}")

    print(json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

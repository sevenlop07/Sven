#!/usr/bin/env python3
"""
SVEN DEPTH VIDEO STUDIO v2.5 — Local GPU Video-to-Depth, Caption Eraser & Character Isolator
============================================================================================
Converts standard RGB videos into temporally-stabilized Depth Map videos
with built-in:
  1. Burned-in Caption / Subtitle & Watermark Eraser (Morphological Stroke Detection +
     Telea Spatial Inpainting + Depth-Domain Surface Healing).
  2. AI Character & Action Isolation (MODNet CUDA Human/Character Matting + Foreground
     Depth Fallback) that strips away background clutter and captions, keeping ONLY
     the character, the character's 3D physical action, and the original audio track.
"""

import os
import sys
import re
import glob
import site
import time
import json
import math
import uuid
import shutil
import threading
import subprocess
import traceback
import argparse
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

# Ensure stdout/stderr are valid file streams when launched via pythonw.exe
_LOG_DIR = Path(__file__).resolve().parent.parent / "scratch"
_LOG_DIR.mkdir(parents=True, exist_ok=True)
_LOG_FILE = _LOG_DIR / "depth_studio_server.log"
if sys.stdout is None or sys.stderr is None:
    _log_stream = open(_LOG_FILE, "a", encoding="utf-8", buffering=1)
    if sys.stdout is None:
        sys.stdout = _log_stream
    if sys.stderr is None:
        sys.stderr = _log_stream


# ---------------------------------------------------------------------------
# 1. BOOTSTRAP NVIDIA CUDA 12 DLL DIRECTORIES BEFORE IMPORTING ONNXRUNTIME
# ---------------------------------------------------------------------------
def _bootstrap_cuda_dlls() -> list:
    added_paths = []
    search_roots = list(site.getsitepackages())
    user_site = site.getusersitepackages()
    if isinstance(user_site, str):
        search_roots.append(user_site)

    for root in search_roots:
        pattern = os.path.join(root, "nvidia", "*", "bin")
        for bin_dir in glob.glob(pattern):
            if os.path.isdir(bin_dir) and bin_dir not in added_paths:
                added_paths.append(bin_dir)
                if hasattr(os, "add_dll_directory"):
                    try:
                        os.add_dll_directory(bin_dir)
                    except Exception:
                        pass
    if added_paths:
        os.environ["PATH"] = os.pathsep.join(added_paths) + os.pathsep + os.environ.get("PATH", "")
    return added_paths


CUDA_DLL_PATHS = _bootstrap_cuda_dlls()

import cv2
import numpy as np
import onnxruntime as ort
from huggingface_hub import hf_hub_download, try_to_load_from_cache
from aiohttp import web

# ---------------------------------------------------------------------------
# 2. CONSTANTS & MODEL CATALOG
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output" / "depth_videos"
UPLOAD_DIR = PROJECT_ROOT / "scratch" / "depth_uploads"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

NO_WINDOW_FLAG = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000) if os.name == "nt" else 0

MODEL_CATALOG: Dict[str, Dict[str, str]] = {
    "small": {
        "repo_id": "onnx-community/Depth-Anything-V2-Small",
        "filename": "onnx/model_fp16.onnx",
        "fallback": "onnx/model.onnx",
        "label": "Depth Anything V2 — Small (FP16 · ~50 FPS · ~1.2 GB VRAM)",
    },
    "base": {
        "repo_id": "onnx-community/Depth-Anything-V2-Base",
        "filename": "onnx/model_fp16.onnx",
        "fallback": "onnx/model.onnx",
        "label": "Depth Anything V2 — Base (FP16 · ~30 FPS · ~2.2 GB VRAM)",
    },
    "large": {
        "repo_id": "onnx-community/Depth-Anything-V2-Large",
        "filename": "onnx/model_fp16.onnx",
        "fallback": "onnx/model.onnx",
        "label": "Depth Anything V2 — Large (FP16 · ~16 FPS · ~4.2 GB VRAM)",
    },
}

MODNET_SPEC = {
    "repo_id": "Xenova/modnet",
    "filename": "onnx/model.onnx",
}

IMAGENET_MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32).reshape(1, 1, 3)
IMAGENET_STD = np.array([0.229, 0.224, 0.225], dtype=np.float32).reshape(1, 1, 3)


def sanitize_stem(name: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9_-]+", "_", name).strip("_")
    return clean[:48] if clean else "video"


def is_model_cached(model_key: str) -> bool:
    if model_key == "modnet":
        try:
            res = try_to_load_from_cache(MODNET_SPEC["repo_id"], MODNET_SPEC["filename"])
            return isinstance(res, str) and os.path.exists(res)
        except Exception:
            return False
    spec = MODEL_CATALOG.get(model_key)
    if not spec:
        return False
    try:
        res = try_to_load_from_cache(spec["repo_id"], spec["filename"])
        return isinstance(res, str) and os.path.exists(res)
    except Exception:
        return False


def probe_video_metadata(video_path: Path) -> Dict[str, Any]:
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise ValueError(f"Không thể đọc file video: {video_path.name}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    if not fps or fps <= 0 or math.isnan(fps):
        fps = 30.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 0)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    duration = round(frames / fps, 2) if frames > 0 else 0.0

    ret, first_frame = cap.read()
    cap.release()

    thumb_url = ""
    if ret and first_frame is not None:
        thumb_name = f"_thumb_{sanitize_stem(video_path.stem)}_{int(video_path.stat().st_mtime)}.jpg"
        thumb_path = OUTPUT_DIR / thumb_name
        th_w = 480
        th_h = max(120, int(round(height * (th_w / float(max(1, width))))))
        small = cv2.resize(first_frame, (th_w, th_h), interpolation=cv2.INTER_AREA)
        cv2.imwrite(str(thumb_path), small, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
        thumb_url = f"/output/{thumb_name}"

    size_mb = round(video_path.stat().st_size / (1024 * 1024), 2)
    return {
        "name": video_path.name,
        "path": str(video_path),
        "width": width,
        "height": height,
        "fps": round(fps, 2),
        "frames": frames,
        "duration_sec": duration,
        "size_mb": size_mb,
        "thumb_url": thumb_url,
    }


# ---------------------------------------------------------------------------
# 3. HARDWARE TELEMETRY (GPU / VRAM)
# ---------------------------------------------------------------------------
def get_hardware_status() -> Dict[str, Any]:
    gpu_name = "CPU Mode"
    vram_total_mb = 0
    vram_used_mb = 0
    vram_free_mb = 0
    gpu_util = 0

    try:
        cmd = [
            "nvidia-smi",
            "--query-gpu=name,memory.total,memory.used,memory.free,utilization.gpu",
            "--format=csv,noheader,nounits",
        ]
        out = subprocess.check_output(
            cmd,
            stdin=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=2,
            creationflags=NO_WINDOW_FLAG,
        ).strip()
        if out:
            parts = [p.strip() for p in out.split("\n")[0].split(",")]
            if len(parts) >= 5:
                gpu_name = parts[0]
                vram_total_mb = int(float(parts[1]))
                vram_used_mb = int(float(parts[2]))
                vram_free_mb = int(float(parts[3]))
                gpu_util = int(float(parts[4]))
    except Exception:
        pass

    providers = ort.get_available_providers()
    cuda_ready = "CUDAExecutionProvider" in providers or "TensorrtExecutionProvider" in providers
    models_cached = {k: is_model_cached(k) for k in list(MODEL_CATALOG.keys()) + ["modnet"]}

    return {
        "gpu_name": gpu_name,
        "vram_total_mb": vram_total_mb,
        "vram_used_mb": vram_used_mb,
        "vram_free_mb": vram_free_mb,
        "gpu_util": gpu_util,
        "cuda_ready": cuda_ready,
        "providers": providers,
        "models_cached": models_cached,
    }


# ---------------------------------------------------------------------------
# 4. CAPTION / SUBTITLE ERASER (RGB INPAINTING + DEPTH SURFACE HEALING)
# ---------------------------------------------------------------------------
def detect_caption_mask(frame_bgr: np.ndarray, zone_mode: str = "bottom") -> np.ndarray:
    """
    Detect burned-in captions/subtitles (high-contrast bright/colored glyphs with dark outline
    or sharp text strokes) inside the configured vertical zone(s).
    Returns a uint8 binary mask (255 = caption pixel to erase, 0 = normal scene).
    """
    h, w = frame_bgr.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)

    zones = []
    if zone_mode == "bottom":
        zones.append((int(h * 0.64), int(h * 0.98), int(w * 0.04), int(w * 0.96)))
    elif zone_mode == "center_bottom":
        zones.append((int(h * 0.42), int(h * 0.98), int(w * 0.04), int(w * 0.96)))
    elif zone_mode == "top_bottom":
        zones.append((int(h * 0.02), int(h * 0.18), int(w * 0.02), int(w * 0.98)))
        zones.append((int(h * 0.64), int(h * 0.98), int(w * 0.04), int(w * 0.96)))
    else:  # "full"
        zones.append((int(h * 0.03), int(h * 0.97), int(w * 0.03), int(w * 0.97)))

    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)

    # Morphological kernels scaled to resolution
    k_scale = max(1.0, min(w, h) / 540.0)
    kw = max(9, int(round(15 * k_scale)) | 1)
    kh = max(5, int(round(7 * k_scale)) | 1)
    kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (kw, kh))
    kernel_small = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    kernel_dilate = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (max(7, int(round(9 * k_scale)) | 1), max(7, int(round(9 * k_scale)) | 1))
    )

    for (y1, y2, x1, x2) in zones:
        if y2 <= y1 or x2 <= x1:
            continue
        roi_gray = gray[y1:y2, x1:x2]

        # 1. Top-Hat (bright text strokes on darker bg) & Black-Hat (dark outlines around bright text)
        tophat = cv2.morphologyEx(roi_gray, cv2.MORPH_TOPHAT, kernel_small)
        blackhat = cv2.morphologyEx(roi_gray, cv2.MORPH_BLACKHAT, kernel_small)

        # 2. High-contrast stroke energy (text has both bright fill and dark stroke within a few pixels)
        bright_core = (roi_gray > 195).astype(np.uint8) * 255
        dark_stroke = (blackhat > 38).astype(np.uint8) * 255
        top_stroke = (tophat > 42).astype(np.uint8) * 255

        # Dilate dark stroke slightly and intersect with bright core / top-hat
        dark_dilated = cv2.dilate(dark_stroke, kernel_small, iterations=1)
        outlined_text = cv2.bitwise_and(cv2.bitwise_or(bright_core, top_stroke), dark_dilated)

        # Also catch high-gradient horizontal text clusters
        grad_x = cv2.Sobel(roi_gray, cv2.CV_16S, 1, 0, ksize=3)
        grad_y = cv2.Sobel(roi_gray, cv2.CV_16S, 0, 1, ksize=3)
        grad_mag = cv2.addWeighted(cv2.convertScaleAbs(grad_x), 0.6, cv2.convertScaleAbs(grad_y), 0.4, 0)
        high_grad = (grad_mag > 85).astype(np.uint8) * 255
        stroke_candidates = cv2.bitwise_or(outlined_text, cv2.bitwise_and(high_grad, top_stroke))

        # Group horizontally into word/caption bars
        closed = cv2.morphologyEx(stroke_candidates, cv2.MORPH_CLOSE, kernel_rect)

        # Filter connected components by text-line geometry (exclude large natural body parts)
        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(closed, connectivity=8)
        roi_mask = np.zeros_like(roi_gray)
        roi_h, roi_w = roi_gray.shape[:2]
        max_glyph_h = int(roi_h * 0.48)
        min_area = max(18, int(18 * k_scale * k_scale))

        for lbl in range(1, num_labels):
            bx, by, bw, bh, area = stats[lbl]
            if area < min_area:
                continue
            if bh > max_glyph_h and bw > int(roi_w * 0.65):
                # Too tall and massive to be a subtitle line
                continue
            aspect = bw / float(max(1, bh))
            if aspect >= 0.35 and bh <= max_glyph_h:
                roi_mask[labels == lbl] = 255

        if np.any(roi_mask):
            roi_mask = cv2.dilate(roi_mask, kernel_dilate, iterations=1)
            mask[y1:y2, x1:x2] = cv2.bitwise_or(mask[y1:y2, x1:x2], roi_mask)

    return mask


def erase_captions_rgb(frame_bgr: np.ndarray, caption_mask: np.ndarray) -> np.ndarray:
    """Inpaint detected caption pixels in RGB space before running depth & segmentation."""
    if not np.any(caption_mask):
        return frame_bgr
    # Downscale inpainting if frame is > 720p for ultra-fast real-time execution
    h, w = frame_bgr.shape[:2]
    if h > 720:
        scale = 540.0 / float(h)
        sw, sh = max(16, int(round(w * scale))), max(16, int(round(h * scale)))
        small_bgr = cv2.resize(frame_bgr, (sw, sh), interpolation=cv2.INTER_AREA)
        small_mask = cv2.resize(caption_mask, (sw, sh), interpolation=cv2.INTER_NEAREST)
        inpainted_small = cv2.inpaint(small_bgr, small_mask, inpaintRadius=4, flags=cv2.INPAINT_TELEA)
        inpainted_full = cv2.resize(inpainted_small, (w, h), interpolation=cv2.INTER_CUBIC)
        out = frame_bgr.copy()
        m_bool = caption_mask > 0
        out[m_bool] = inpainted_full[m_bool]
        return out
    return cv2.inpaint(frame_bgr, caption_mask, inpaintRadius=4, flags=cv2.INPAINT_TELEA)


def heal_caption_depth(depth_2d: np.ndarray, caption_mask: np.ndarray) -> np.ndarray:
    """Smooth out any residual high-frequency text embossing in the depth map."""
    if not np.any(caption_mask):
        return depth_2d
    h, w = depth_2d.shape[:2]
    # Use a heavily smoothed version of the depth map to replace caption stroke pixels
    sw, sh = max(16, w // 6), max(16, h // 6)
    low_freq = cv2.resize(depth_2d, (sw, sh), interpolation=cv2.INTER_AREA)
    low_freq = cv2.GaussianBlur(low_freq, (7, 7), 0)
    smooth_full = cv2.resize(low_freq, (w, h), interpolation=cv2.INTER_CUBIC)

    # Feather the caption mask for seamless depth blending
    alpha = cv2.GaussianBlur(caption_mask.astype(np.float32) / 255.0, (11, 11), 0)
    return depth_2d * (1.0 - alpha) + smooth_full * alpha


# ---------------------------------------------------------------------------
# 5. DEPTH & CHARACTER SEGMENTATION ENGINE (ONNX RUNTIME CUDA)
# ---------------------------------------------------------------------------
class DepthVideoEngine:
    def __init__(self):
        self.sessions: Dict[str, Tuple[ort.InferenceSession, str, str, str]] = {}
        self.modnet_session: Optional[Tuple[ort.InferenceSession, str, str]] = None
        self.lock = threading.Lock()

    def _build_ort_providers(self) -> list:
        avail = ort.get_available_providers()
        preferred = []
        if "CUDAExecutionProvider" in avail:
            preferred.append("CUDAExecutionProvider")
        preferred.append("CPUExecutionProvider")
        return preferred

    def get_session(self, model_key: str = "small") -> Tuple[ort.InferenceSession, str, str, str]:
        model_key = model_key if model_key in MODEL_CATALOG else "small"
        with self.lock:
            if model_key in self.sessions:
                return self.sessions[model_key]

            spec = MODEL_CATALOG[model_key]
            try:
                model_path = hf_hub_download(repo_id=spec["repo_id"], filename=spec["filename"])
            except Exception:
                model_path = hf_hub_download(repo_id=spec["repo_id"], filename=spec["fallback"])

            sess_opts = ort.SessionOptions()
            sess_opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
            sess = ort.InferenceSession(model_path, sess_options=sess_opts, providers=self._build_ort_providers())

            inp = sess.get_inputs()[0]
            active_provider = sess.get_providers()[0]
            info = (sess, inp.name, inp.type, active_provider)
            self.sessions[model_key] = info
            return info

    def get_modnet_session(self) -> Tuple[ort.InferenceSession, str, str]:
        """Load MODNet human/character segmentation model on CUDA (47+ FPS)."""
        with self.lock:
            if self.modnet_session is not None:
                return self.modnet_session

            model_path = hf_hub_download(repo_id=MODNET_SPEC["repo_id"], filename=MODNET_SPEC["filename"])
            sess_opts = ort.SessionOptions()
            sess_opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
            sess = ort.InferenceSession(model_path, sess_options=sess_opts, providers=self._build_ort_providers())
            inp = sess.get_inputs()[0]
            self.modnet_session = (sess, inp.name, sess.get_providers()[0])
            return self.modnet_session

    @staticmethod
    def compute_inference_dims(width: int, height: int, target_short_side: int = 518) -> Tuple[int, int]:
        side = max(14, int(round(target_short_side / 14.0)) * 14)
        return side, side

    def infer_frame(
        self,
        sess: ort.InferenceSession,
        input_name: str,
        input_type: str,
        frame_bgr: np.ndarray,
        infer_w: int,
        infer_h: int,
    ) -> np.ndarray:
        orig_h, orig_w = frame_bgr.shape[:2]
        resized = cv2.resize(frame_bgr, (infer_w, infer_h), interpolation=cv2.INTER_CUBIC)
        rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
        norm = (rgb - IMAGENET_MEAN) / IMAGENET_STD
        chw = np.transpose(norm, (2, 0, 1))[None, ...]

        if "float16" in input_type:
            chw = chw.astype(np.float16)
        else:
            chw = chw.astype(np.float32)

        raw_depth = sess.run(None, {input_name: chw})[0]
        depth_2d = np.squeeze(raw_depth).astype(np.float32)
        if depth_2d.shape[0] != orig_h or depth_2d.shape[1] != orig_w:
            depth_2d = cv2.resize(depth_2d, (orig_w, orig_h), interpolation=cv2.INTER_CUBIC)
        return depth_2d

    def infer_character_matte(
        self,
        frame_bgr: np.ndarray,
        raw_depth: Optional[np.ndarray] = None,
    ) -> np.ndarray:
        """
        Extract character alpha matte [0.0 .. 1.0] isolating ONLY the character & their action.
        Uses MODNet CUDA human matting as primary detector, with automatic Depth-Otsu foreground
        fallback if the subject is a non-human creature/object.
        """
        orig_h, orig_w = frame_bgr.shape[:2]
        sess, input_name, _ = self.get_modnet_session()

        # MODNet runs at native 512x512 in 22ms on CUDA without cuDNN fallback
        mw, mh = 512, 512
        resized = cv2.resize(frame_bgr, (mw, mh), interpolation=cv2.INTER_AREA)
        rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB).astype(np.float32)
        norm = (rgb - 127.5) / 127.5
        chw = np.transpose(norm, (2, 0, 1))[None, ...].astype(np.float32)

        matte = sess.run(None, {input_name: chw})[0]
        matte_2d = np.squeeze(matte).astype(np.float32)
        matte_2d = np.clip(matte_2d, 0.0, 1.0)

        # Fallback: if MODNet detects no human character (e.g., animal/car/prop video),
        # isolate the nearest foreground subject from the depth map via Otsu thresholding
        if float(np.percentile(matte_2d, 98.0)) < 0.22 and raw_depth is not None:
            d_min, d_max = float(np.min(raw_depth)), float(np.max(raw_depth))
            d_u8 = ((raw_depth - d_min) / max(1e-5, d_max - d_min) * 255.0).astype(np.uint8)
            _, fg_mask = cv2.threshold(d_u8, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            fg_float = cv2.GaussianBlur(fg_mask.astype(np.float32) / 255.0, (9, 9), 0)
            return fg_float

        if matte_2d.shape[0] != orig_h or matte_2d.shape[1] != orig_w:
            matte_2d = cv2.resize(matte_2d, (orig_w, orig_h), interpolation=cv2.INTER_CUBIC)

        # Clean low-alpha background noise while preserving smooth anti-aliased edges
        matte_2d = np.where(matte_2d < 0.12, 0.0, matte_2d)
        matte_2d = np.clip((matte_2d - 0.12) / 0.88, 0.0, 1.0)
        return matte_2d


ENGINE = DepthVideoEngine()
JOBS: Dict[str, Dict[str, Any]] = {}


# ---------------------------------------------------------------------------
# 6. COLORIZATION & CONTACT SHEET GENERATION
# ---------------------------------------------------------------------------
def colorize_depth(
    norm_depth_01: np.ndarray,
    colormap: str = "grayscale",
    gamma: float = 1.0,
    orig_bgr: Optional[np.ndarray] = None,
    char_matte: Optional[np.ndarray] = None,
) -> np.ndarray:
    if colormap == "character_rgb" and orig_bgr is not None:
        if char_matte is not None:
            m3 = char_matte[..., None]
            return (orig_bgr.astype(np.float32) * m3).astype(np.uint8)
        return orig_bgr

    if colormap == "clean_rgb" and orig_bgr is not None:
        return orig_bgr

    d = np.clip(norm_depth_01, 0.0, 1.0)
    if abs(gamma - 1.0) > 1e-3:
        d = np.power(d, gamma)

    if colormap == "inverted":
        d = 1.0 - d
        if char_matte is not None:
            d = d * char_matte
        u8 = (d * 255.0).astype(np.uint8)
        return cv2.cvtColor(u8, cv2.COLOR_GRAY2BGR)
    elif colormap == "inferno":
        u8 = (d * 255.0).astype(np.uint8)
        colored = cv2.applyColorMap(u8, cv2.COLORMAP_INFERNO)
        if char_matte is not None:
            colored = (colored.astype(np.float32) * char_matte[..., None]).astype(np.uint8)
        return colored
    elif colormap == "turbo":
        u8 = (d * 255.0).astype(np.uint8)
        colored = cv2.applyColorMap(u8, cv2.COLORMAP_TURBO)
        if char_matte is not None:
            colored = (colored.astype(np.float32) * char_matte[..., None]).astype(np.uint8)
        return colored
    elif colormap == "side_by_side":
        if char_matte is not None:
            d = d * char_matte
        u8 = (d * 255.0).astype(np.uint8)
        depth_bgr = cv2.cvtColor(u8, cv2.COLOR_GRAY2BGR)
        if orig_bgr is not None:
            return np.hstack([orig_bgr, depth_bgr])
        return depth_bgr
    else:
        if char_matte is not None:
            d = d * char_matte
        u8 = (d * 255.0).astype(np.uint8)
        return cv2.cvtColor(u8, cv2.COLOR_GRAY2BGR)


def generate_contact_sheet(video_path: Path, out_jpg: Path, step_sec: float = 0.5, max_cols: int = 5) -> Optional[Path]:
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        return None
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    if fps <= 0 or math.isnan(fps):
        fps = 30.0
    step_frames = max(1, int(round(fps * step_sec)))

    thumbs = []
    idx = 0
    while len(thumbs) < 60:
        ret, frame = cap.read()
        if not ret:
            break
        if idx % step_frames == 0:
            t_sec = idx / fps
            h, w = frame.shape[:2]
            tw = 320
            th = max(120, int(round(h * (tw / float(w)))))
            thumb = cv2.resize(frame, (tw, th), interpolation=cv2.INTER_AREA)
            label = f"{t_sec:05.2f}s (F{idx})"
            cv2.rectangle(thumb, (0, 0), (165, 28), (0, 0, 0), -1)
            cv2.putText(thumb, label, (8, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 180), 1, cv2.LINE_AA)
            thumbs.append(thumb)
        idx += 1
    cap.release()

    if not thumbs:
        return None

    th, tw = thumbs[0].shape[:2]
    cols = min(max_cols, len(thumbs))
    rows = int(math.ceil(len(thumbs) / float(cols)))
    grid = np.zeros((rows * th, cols * tw, 3), dtype=np.uint8)
    for i, im in enumerate(thumbs):
        r = i // cols
        c = i % cols
        grid[r * th : (r + 1) * th, c * tw : (c + 1) * tw] = im
    cv2.imwrite(str(out_jpg), grid, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    return out_jpg


# ---------------------------------------------------------------------------
# 7. STREAMING VIDEO CONVERSION PIPELINE
# ---------------------------------------------------------------------------
def process_video_job(job_id: str, params: Dict[str, Any]) -> None:
    job = JOBS[job_id]
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        input_path = Path(params["input_path"])
        if not input_path.exists():
            raise FileNotFoundError(f"Không tìm thấy file video: {input_path}")

        model_key = params.get("model", "small")
        colormap = params.get("colormap", "grayscale")
        infer_res = int(params.get("infer_res", 518))
        ema_alpha = float(params.get("ema_alpha", 0.85))
        frame_blend = float(params.get("frame_blend", 0.15))
        gamma = float(params.get("gamma", 1.0))
        low_pct = float(params.get("low_pct", 1.0))
        high_pct = float(params.get("high_pct", 99.0))
        keep_audio = bool(params.get("keep_audio", True))
        make_sheet = bool(params.get("make_contact_sheet", True))
        max_out_height = int(params.get("max_out_height", 0))

        # New Caption Eraser & Character-Only Isolation Controls
        remove_captions = bool(params.get("remove_captions", True))
        caption_zone = params.get("caption_zone", "bottom")
        isolate_character = bool(params.get("isolate_character", True))

        job["status"] = "loading_model"
        job["message"] = f"Đang nạp mô hình Depth ({model_key.upper()}) lên VRAM RTX 3060..."
        sess, input_name, input_type, active_provider = ENGINE.get_session(model_key)

        if isolate_character:
            job["message"] = "Đang nạp mô hình AI Tách Nhân Vật (MODNet CUDA)..."
            ENGINE.get_modnet_session()

        job["provider"] = active_provider

        cap = cv2.VideoCapture(str(input_path))
        if not cap.isOpened():
            raise RuntimeError(f"Không thể mở video: {input_path}")

        fps = cap.get(cv2.CAP_PROP_FPS)
        if not fps or fps <= 0 or math.isnan(fps):
            fps = 30.0
        orig_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        orig_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)

        out_w, out_h = orig_w, orig_h
        if max_out_height > 0 and orig_h > max_out_height:
            scale = max_out_height / float(orig_h)
            out_w = max(2, int(round(orig_w * scale / 2.0)) * 2)
            out_h = max(2, int(round(orig_h * scale / 2.0)) * 2)
        else:
            out_w = max(2, (orig_w // 2) * 2)
            out_h = max(2, (orig_h // 2) * 2)

        infer_w, infer_h = ENGINE.compute_inference_dims(out_w, out_h, target_short_side=infer_res)
        final_w = out_w * 2 if colormap == "side_by_side" else out_w
        final_h = out_h

        clean_stem = sanitize_stem(params.get("original_name") or input_path.stem)
        mode_tag = "char_only" if isolate_character else "full"
        timestamp_tag = time.strftime("%H%M%S")
        out_filename = f"{clean_stem}_{mode_tag}_{model_key}_{colormap}_{timestamp_tag}.mp4"
        temp_raw_mp4 = OUTPUT_DIR / f"_tmp_{job_id}.mp4"
        final_mp4 = OUTPUT_DIR / out_filename
        preview_jpg = OUTPUT_DIR / f"_preview_{job_id}.jpg"

        ffmpeg_exe = shutil.which("ffmpeg") or "ffmpeg"
        ffmpeg_cmd = [
            ffmpeg_exe,
            "-nostdin",
            "-y",
            "-f",
            "rawvideo",
            "-vcodec",
            "rawvideo",
            "-s",
            f"{final_w}x{final_h}",
            "-pix_fmt",
            "bgr24",
            "-r",
            f"{fps:.4f}",
            "-i",
            "-",
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-movflags",
            "+faststart",
            str(temp_raw_mp4),
        ]

        proc = subprocess.Popen(
            ffmpeg_cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=NO_WINDOW_FLAG,
        )

        job["status"] = "processing"
        job["total_frames"] = total_frames
        job["fps_video"] = round(fps, 2)
        job["resolution"] = f"{final_w}×{final_h}"
        job["infer_resolution"] = f"{infer_w}×{infer_h}"

        ema_dmin: Optional[float] = None
        ema_dmax: Optional[float] = None
        prev_norm: Optional[np.ndarray] = None
        prev_matte: Optional[np.ndarray] = None

        frame_idx = 0
        t_start = time.time()

        while True:
            if job.get("cancel_requested"):
                try:
                    proc.stdin.close()
                    proc.terminate()
                except Exception:
                    pass
                cap.release()
                temp_raw_mp4.unlink(missing_ok=True)
                preview_jpg.unlink(missing_ok=True)
                job["status"] = "cancelled"
                job["message"] = "Đã dừng xử lý theo yêu cầu."
                return

            ret, frame = cap.read()
            if not ret:
                break

            if frame.shape[1] != out_w or frame.shape[0] != out_h:
                frame = cv2.resize(frame, (out_w, out_h), interpolation=cv2.INTER_AREA)

            # STEP A: Remove burned-in captions / subtitles from the RGB frame first
            caption_mask = None
            clean_frame = frame
            if remove_captions:
                caption_mask = detect_caption_mask(frame, zone_mode=caption_zone)
                if np.any(caption_mask):
                    clean_frame = erase_captions_rgb(frame, caption_mask)

            # STEP B: Run Depth Anything V2 on the caption-cleaned frame
            if colormap == "clean_rgb":
                raw_depth = np.zeros((out_h, out_w), dtype=np.float32)
            else:
                raw_depth = ENGINE.infer_frame(sess, input_name, input_type, clean_frame, infer_w, infer_h)
                if remove_captions and caption_mask is not None and np.any(caption_mask):
                    raw_depth = heal_caption_depth(raw_depth, caption_mask)

            # STEP C: Isolate ONLY the character & character action (removing background & text residue)
            char_matte = None
            if isolate_character:
                char_matte = ENGINE.infer_character_matte(clean_frame, raw_depth=raw_depth)
                # Also force zero inside non-body floating caption islands if any
                if prev_matte is not None:
                    char_matte = 0.85 * char_matte + 0.15 * prev_matte
                prev_matte = char_matte

            # STEP D: Normalize depth dynamically (focused on character pixels when isolated!)
            if isolate_character and char_matte is not None:
                fg_pixels = raw_depth[char_matte > 0.25]
                if fg_pixels.size > 64:
                    d_min = float(np.percentile(fg_pixels, low_pct))
                    d_max = float(np.percentile(fg_pixels, high_pct))
                else:
                    d_min = float(np.percentile(raw_depth, low_pct))
                    d_max = float(np.percentile(raw_depth, high_pct))
            else:
                d_min = float(np.percentile(raw_depth, low_pct))
                d_max = float(np.percentile(raw_depth, high_pct))

            if d_max - d_min < 1e-5:
                d_max = d_min + 1.0

            if ema_dmin is None or ema_alpha <= 0.0:
                ema_dmin, ema_dmax = d_min, d_max
            else:
                ema_dmin = ema_alpha * ema_dmin + (1.0 - ema_alpha) * d_min
                ema_dmax = ema_alpha * ema_dmax + (1.0 - ema_alpha) * d_max

            norm_depth = (raw_depth - ema_dmin) / max(1e-5, (ema_dmax - ema_dmin))
            if isolate_character and char_matte is not None:
                # Boost minimum character visibility so the character stands out clearly from pure black (0)
                norm_depth = 0.18 + 0.82 * np.clip(norm_depth, 0.0, 1.0)
            else:
                norm_depth = np.clip(norm_depth, 0.0, 1.0)

            if prev_norm is not None and frame_blend > 0.0:
                norm_depth = (1.0 - frame_blend) * norm_depth + frame_blend * prev_norm
            prev_norm = norm_depth

            out_bgr = colorize_depth(
                norm_depth_01=norm_depth,
                colormap=colormap,
                gamma=gamma,
                orig_bgr=clean_frame,
                char_matte=char_matte,
            )
            proc.stdin.write(out_bgr.tobytes())

            frame_idx += 1
            elapsed = max(1e-3, time.time() - t_start)
            proc_fps = frame_idx / elapsed
            pct = int(min(99, round((frame_idx / float(max(1, total_frames))) * 100))) if total_frames > 0 else 50
            eta_sec = max(0.0, (total_frames - frame_idx) / max(0.1, proc_fps)) if total_frames > 0 else 0.0

            job["processed_frames"] = frame_idx
            job["progress"] = pct
            job["proc_fps"] = round(proc_fps, 1)
            job["eta_sec"] = round(eta_sec, 1)
            flags_str = []
            if remove_captions:
                flags_str.append("Đã xóa Caption")
            if isolate_character:
                flags_str.append("Tách riêng Nhân Vật")
            flag_badge = f" [{' + '.join(flags_str)}]" if flags_str else ""
            job["message"] = (
                f"Frame {frame_idx}/{total_frames or '?'}{flag_badge} · "
                f"Tốc độ: {proc_fps:.1f} FPS · Còn ~{eta_sec:.1f}s"
            )

            if frame_idx == 1 or frame_idx % 8 == 0:
                try:
                    ph, pw = out_bgr.shape[:2]
                    target_pw = min(640, pw)
                    target_ph = max(160, int(round(ph * (target_pw / float(pw)))))
                    small_prev = cv2.resize(out_bgr, (target_pw, target_ph), interpolation=cv2.INTER_AREA)
                    cv2.imwrite(str(preview_jpg), small_prev, [int(cv2.IMWRITE_JPEG_QUALITY), 82])
                    job["preview_url"] = f"/output/{preview_jpg.name}?t={int(time.time()*1000)}"
                except Exception:
                    pass

        cap.release()
        proc.stdin.close()
        proc.wait()
        preview_jpg.unlink(missing_ok=True)

        if keep_audio:
            job["message"] = "Đang ghép âm thanh gốc (Audio Muxing) vào file MP4..."
            mux_cmd = [
                ffmpeg_exe,
                "-nostdin",
                "-y",
                "-i",
                str(temp_raw_mp4),
                "-i",
                str(input_path),
                "-c:v",
                "copy",
                "-c:a",
                "aac",
                "-map",
                "0:v:0",
                "-map",
                "1:a:0?",
                "-shortest",
                "-movflags",
                "+faststart",
                str(final_mp4),
            ]
            res = subprocess.run(
                mux_cmd,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=NO_WINDOW_FLAG,
            )
            if res.returncode == 0 and final_mp4.exists():
                temp_raw_mp4.unlink(missing_ok=True)
            else:
                shutil.move(str(temp_raw_mp4), str(final_mp4))
        else:
            shutil.move(str(temp_raw_mp4), str(final_mp4))

        if make_sheet:
            job["message"] = "Đang tạo ảnh lưới Contact Sheet (0.5s/frame)..."
            sheet_path = OUTPUT_DIR / f"{final_mp4.stem}_contact_sheet.jpg"
            if generate_contact_sheet(final_mp4, sheet_path, step_sec=0.5):
                job["contact_sheet_path"] = str(sheet_path)
                job["contact_sheet_url"] = f"/output/{sheet_path.name}"

        total_time = round(time.time() - t_start, 2)
        avg_fps = round(frame_idx / max(0.1, total_time), 1)
        size_mb = round(final_mp4.stat().st_size / (1024 * 1024), 2) if final_mp4.exists() else 0.0

        job["status"] = "completed"
        job["progress"] = 100
        job["elapsed_sec"] = total_time
        job["avg_fps"] = avg_fps
        job["size_mb"] = size_mb
        job["output_name"] = final_mp4.name
        job["output_path"] = str(final_mp4)
        job["output_url"] = f"/output/{final_mp4.name}"
        job["message"] = (
            f"Hoàn tất! Đã xử lý {frame_idx} frame trong {total_time}s "
            f"(Trung bình {avg_fps} FPS · Đã giữ Audio gốc)."
        )

    except Exception as exc:
        job["status"] = "error"
        job["message"] = f"Lỗi: {str(exc)}"


# ---------------------------------------------------------------------------
# 8. STUDIO WEB UI FRONTEND (v2.5 WITH CAPTION ERASER & CHARACTER ISOLATOR)
# ---------------------------------------------------------------------------
INDEX_HTML = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SVEN Depth Video Studio v2.5 — Caption Eraser & Character Action Isolator</title>
<style>
  :root {
    --bg: #090d16;
    --panel: #111827;
    --panel-2: #1e293b;
    --panel-3: #0f172a;
    --border: #334155;
    --accent: #10b981;
    --accent-hover: #059669;
    --blue: #3b82f6;
    --text: #f8fafc;
    --muted: #94a3b8;
    --danger: #ef4444;
    --warn: #f59e0b;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Segoe UI', Inter, system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  .navbar {
    background: rgba(17, 24, 39, 0.95);
    border-bottom: 1px solid var(--border);
    padding: 12px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    position: sticky;
    top: 0;
    z-index: 50;
  }
  .brand { display: flex; align-items: center; gap: 12px; }
  .badge-pro {
    background: linear-gradient(135deg, #10b981, #059669);
    color: #022c22;
    font-weight: 800;
    font-size: 12px;
    padding: 4px 10px;
    border-radius: 6px;
    letter-spacing: 0.5px;
  }
  .brand h1 { font-size: 18px; font-weight: 700; color: #fff; }
  .hw-pill {
    display: flex;
    align-items: center;
    gap: 10px;
    background: var(--panel-3);
    border: 1px solid var(--border);
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12.5px;
    color: #cbd5e1;
  }
  .dot-live {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 8px var(--accent);
  }

  .workspace {
    max-width: 1540px;
    width: 100%;
    margin: 18px auto;
    padding: 0 20px 32px;
    display: grid;
    grid-template-columns: 450px 1fr;
    gap: 20px;
    align-items: start;
  }
  @media (max-width: 1120px) {
    .workspace { grid-template-columns: 1fr; }
  }

  .panel {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
  }
  .panel-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 14px;
  }
  .step-title {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--accent);
  }
  .step-num {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: rgba(16, 185, 129, 0.18);
    border: 1px solid var(--accent);
    color: var(--accent);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    font-weight: 800;
  }

  .upload-label {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 2px dashed #475569;
    background: rgba(30, 41, 59, 0.55);
    border-radius: 12px;
    padding: 20px 16px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s ease;
    user-select: none;
  }
  .upload-label:hover, .upload-label.dragover {
    border-color: var(--accent);
    background: rgba(16, 185, 129, 0.08);
  }
  .upload-icon { font-size: 30px; margin-bottom: 6px; }
  .upload-title { font-size: 14px; font-weight: 700; color: #fff; }
  .upload-sub { font-size: 12px; color: var(--muted); margin-top: 4px; }
  .upload-btn-fake {
    margin-top: 10px;
    background: var(--panel-2);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 6px 15px;
    border-radius: 8px;
    font-size: 12.5px;
    font-weight: 600;
  }
  .upload-label:hover .upload-btn-fake {
    border-color: var(--accent);
    color: var(--accent);
  }

  .upload-progress-wrap {
    display: none;
    margin-top: 12px;
    background: var(--panel-3);
    padding: 10px 12px;
    border-radius: 8px;
    border: 1px solid var(--border);
  }
  .file-info-card {
    display: none;
    margin-top: 12px;
    background: var(--panel-3);
    border: 1px solid var(--accent);
    border-radius: 10px;
    padding: 12px;
    gap: 12px;
    align-items: center;
  }
  .file-thumb {
    width: 84px;
    height: 54px;
    object-fit: cover;
    border-radius: 6px;
    background: #000;
    border: 1px solid var(--border);
    flex-shrink: 0;
  }
  .file-meta { flex: 1; min-width: 0; }
  .file-name {
    font-size: 13.5px;
    font-weight: 700;
    color: #fff;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .file-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 5px;
  }
  .mini-badge {
    background: var(--panel-2);
    border: 1px solid var(--border);
    padding: 2px 7px;
    border-radius: 5px;
    font-size: 11px;
    color: #cbd5e1;
    font-family: monospace;
  }

  /* HIGHLIGHTED FEATURE CARDS: CAPTION ERASER & CHARACTER ISOLATOR */
  .feature-box {
    background: rgba(16, 185, 129, 0.07);
    border: 1px solid rgba(16, 185, 129, 0.45);
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 14px;
  }
  .feature-box-title {
    font-size: 12px;
    font-weight: 800;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
  }
  .switch-row {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 7px 0;
    cursor: pointer;
  }
  .switch-row input[type="checkbox"] {
    accent-color: var(--accent);
    width: 17px;
    height: 17px;
    margin-top: 2px;
    flex-shrink: 0;
  }
  .switch-row strong {
    display: block;
    font-size: 13px;
    color: #fff;
  }
  .switch-row span {
    display: block;
    font-size: 11.5px;
    color: var(--muted);
    margin-top: 1px;
  }

  .preset-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 14px;
  }
  .preset-btn {
    background: var(--panel-3);
    border: 1px solid var(--border);
    border-radius: 9px;
    padding: 10px;
    text-align: left;
    cursor: pointer;
    color: var(--text);
    transition: all 0.15s;
  }
  .preset-btn:hover { border-color: var(--accent); }
  .preset-btn.active {
    border-color: var(--accent);
    background: rgba(16, 185, 129, 0.12);
    box-shadow: inset 0 0 0 1px var(--accent);
  }
  .preset-btn strong { display: block; font-size: 12.5px; color: #fff; }
  .preset-btn span { font-size: 11px; color: var(--muted); }

  .field { margin-bottom: 12px; }
  .field label {
    display: flex;
    justify-content: space-between;
    font-size: 12.5px;
    font-weight: 600;
    color: #cbd5e1;
    margin-bottom: 5px;
  }
  .field label .val { color: var(--accent); font-family: monospace; }
  select, input[type="text"] {
    width: 100%;
    background: var(--panel-3);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 9px 11px;
    border-radius: 8px;
    font-size: 12.8px;
  }
  select:focus, input[type="text"]:focus {
    outline: none;
    border-color: var(--accent);
  }
  input[type="range"] { width: 100%; accent-color: var(--accent); cursor: pointer; }
  .hint { font-size: 11px; color: var(--muted); margin-top: 2px; }

  details.adv-box {
    background: var(--panel-3);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px 12px;
    margin-bottom: 14px;
  }
  details.adv-box summary {
    cursor: pointer;
    font-size: 12.5px;
    font-weight: 700;
    color: #cbd5e1;
    user-select: none;
  }
  .adv-body { margin-top: 12px; padding-top: 10px; border-top: 1px solid var(--border); }

  .check-line {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12.5px;
    margin-bottom: 8px;
    cursor: pointer;
  }
  .check-line input { accent-color: var(--accent); width: 15px; height: 15px; }

  .btn {
    background: var(--panel-2);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 8px 13px;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
    font-size: 12.5px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    text-decoration: none;
    transition: all 0.15s;
  }
  .btn:hover { border-color: var(--accent); color: var(--accent); }
  .btn-run {
    width: 100%;
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: #022c22;
    border: none;
    padding: 13px;
    font-size: 14.5px;
    font-weight: 800;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.15s;
  }
  .btn-run:hover { filter: brightness(1.08); transform: translateY(-1px); }
  .btn-run:disabled { opacity: 0.45; cursor: not-allowed; transform: none; }
  .btn-stop {
    background: rgba(239, 68, 68, 0.15);
    border: 1px solid var(--danger);
    color: #fca5a5;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 700;
    cursor: pointer;
    display: none;
  }
  .btn-stop:hover { background: var(--danger); color: #fff; }

  .status-strip {
    background: var(--panel-3);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 16px;
  }
  .status-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    font-size: 13.5px;
  }
  .bar-bg {
    width: 100%;
    height: 10px;
    background: #090d16;
    border-radius: 999px;
    overflow: hidden;
    margin: 10px 0 8px;
  }
  .bar-fill {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, var(--blue), var(--accent));
    transition: width 0.2s ease;
  }
  .status-sub {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: var(--muted);
  }

  .view-tabs {
    display: flex;
    gap: 8px;
    margin-bottom: 14px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 10px;
    flex-wrap: wrap;
  }
  .tab-btn {
    background: var(--panel-3);
    border: 1px solid var(--border);
    color: var(--muted);
    padding: 7px 14px;
    border-radius: 8px;
    font-size: 12.5px;
    font-weight: 700;
    cursor: pointer;
  }
  .tab-btn.active {
    background: rgba(16, 185, 129, 0.15);
    border-color: var(--accent);
    color: var(--accent);
  }

  .dual-stage {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }
  @media (max-width: 820px) {
    .dual-stage { grid-template-columns: 1fr; }
  }
  .viewport-card {
    background: #05070b;
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  .viewport-head {
    background: var(--panel-2);
    padding: 8px 12px;
    font-size: 12px;
    font-weight: 700;
    color: #cbd5e1;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border);
  }
  .viewport-body {
    position: relative;
    height: 360px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: radial-gradient(circle at center, #111827 0%, #05070b 100%);
  }
  .viewport-body video, .viewport-body img.live-frame {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: none;
  }
  .empty-placeholder {
    text-align: center;
    color: var(--muted);
    padding: 20px;
    font-size: 13px;
  }
  .empty-placeholder .big-ic { font-size: 36px; margin-bottom: 8px; opacity: 0.6; }

  .wipe-stage {
    display: none;
    position: relative;
    width: 100%;
    height: 440px;
    background: #05070b;
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    user-select: none;
  }
  .wipe-stage video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
  #wipeDepthVideo {
    clip-path: inset(0 0 0 50%);
  }
  .wipe-handle {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 3px;
    background: var(--accent);
    cursor: ew-resize;
    z-index: 10;
  }
  .wipe-knob {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--accent);
    color: #022c22;
    font-weight: 900;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 12px rgba(0,0,0,0.6);
    font-size: 14px;
  }

  .sheet-stage {
    display: none;
    background: #05070b;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px;
    text-align: center;
    max-height: 520px;
    overflow-y: auto;
  }
  .sheet-stage img {
    max-width: 100%;
    border-radius: 6px;
  }

  .toolbar {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 14px;
    padding-top: 14px;
    border-top: 1px solid var(--border);
    align-items: center;
  }

  .history-grid {
    display: flex;
    flex-direction: column;
    gap: 8px;
    max-height: 250px;
    overflow-y: auto;
  }
  .hist-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--panel-3);
    border: 1px solid var(--border);
    padding: 9px 14px;
    border-radius: 8px;
    font-size: 12.5px;
    gap: 10px;
  }
  .hist-row:hover { border-color: #475569; }
</style>
</head>
<body>

<input type="file" id="masterFileInput" accept="video/*,.mp4,.mov,.mkv,.webm,.avi" style="display:none">

<nav class="navbar">
  <div class="brand">
    <span class="badge-pro">SVEN STUDIO v2.5</span>
    <h1>Tách Độ Sâu Nhân Vật · Xóa Caption · Giữ Hành Động & Audio (RTX CUDA)</h1>
  </div>
  <div class="hw-pill">
    <span class="dot-live"></span>
    <span id="hwStatusText">Đang kết nối GPU RTX 3060...</span>
  </div>
</nav>

<div class="workspace">
  <!-- LEFT PANEL -->
  <div>
    <!-- STEP 1 -->
    <div class="panel">
      <div class="panel-header">
        <div class="step-title"><span class="step-num">1</span> Chọn Video Đầu Vào</div>
        <button class="btn" type="button" onclick="triggerFileDialog()" style="padding:5px 10px;font-size:12px;">📂 Duyệt File...</button>
      </div>

      <label for="masterFileInput" class="upload-label" id="dropArea">
        <div class="upload-icon">🎬</div>
        <div class="upload-title">Bấm vào đây để Chọn Video hoặc Kéo Thả File</div>
        <div class="upload-sub">Hỗ trợ MP4, MOV, MKV, WEBM, AVI</div>
        <span class="upload-btn-fake">📂 Chọn Video từ Máy Tính</span>
      </label>

      <div class="upload-progress-wrap" id="uploadProgressBox">
        <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px;">
          <span id="uploadFileName">Đang nạp file...</span>
          <strong id="uploadPctText" style="color:var(--accent);">0%</strong>
        </div>
        <div class="bar-bg" style="margin:4px 0;"><div class="bar-fill" id="uploadBarFill"></div></div>
      </div>

      <div class="file-info-card" id="loadedFileCard">
        <img id="loadedThumb" class="file-thumb" src="" alt="Thumb">
        <div class="file-meta">
          <div class="file-name" id="loadedName">video.mp4</div>
          <div class="file-badges">
            <span class="mini-badge" id="badgeRes">1920×1080</span>
            <span class="mini-badge" id="badgeDur">10.0s</span>
            <span class="mini-badge" id="badgeFps">30 FPS</span>
            <span class="mini-badge" id="badgeSize">12 MB</span>
          </div>
        </div>
      </div>

      <details class="adv-box" style="margin-top:12px;margin-bottom:0;">
        <summary>🔗 Hoặc dán trực tiếp đường dẫn file video trên ổ cứng</summary>
        <div class="adv-body" style="display:flex;gap:8px;">
          <input type="text" id="directPathInput" placeholder="VD: D:\Videos\scene_01.mp4">
          <button class="btn" type="button" onclick="probeDirectPath()">Nạp</button>
        </div>
      </details>
    </div>

    <!-- STEP 2 -->
    <div class="panel">
      <div class="panel-header">
        <div class="step-title"><span class="step-num">2</span> Lọc Nhân Vật, Xóa Caption & Độ Sâu</div>
        <button class="btn" type="button" onclick="applyPreset('char_action_clean')" style="padding:4px 9px;font-size:11.5px;">🔄 Mặc định</button>
      </div>

      <!-- CORE FEATURE BOX: CAPTION ERASER + CHARACTER ACTION ISOLATOR -->
      <div class="feature-box">
        <div class="feature-box-title">🛡️ Bộ Lọc Tách Nhân Vật & Khử Phụ Đề (AI CUDA)</div>

        <label class="switch-row">
          <input type="checkbox" id="isolateCharCheck" checked>
          <div>
            <strong>🕺 Chỉ Lấy Nhân Vật & Hành Động (Tách Bỏ Hậu Cảnh)</strong>
            <span>Dùng AI MODNet khóa riêng hình thể & chuyển động nhân vật trên nền đen sạch (loại bỏ hoàn toàn nhiễu nền & chữ).</span>
          </div>
        </label>

        <label class="switch-row">
          <input type="checkbox" id="removeCaptionCheck" checked onchange="toggleCaptionZoneUI()">
          <div>
            <strong>🧹 Tự Động Xóa Caption / Phụ Đề Ở Video Gốc</strong>
            <span>Quét nét chữ phụ đề, xóa bằng Inpainting và làm phẳng bề mặt độ sâu để không bị in chữ nổi lên nhân vật.</span>
          </div>
        </label>

        <div class="field" id="captionZoneField" style="margin-top:6px;margin-bottom:4px;">
          <label>Vùng quét xóa Caption / Phụ đề:</label>
          <select id="captionZoneSelect">
            <option value="bottom" selected>Phụ đề đáy video (65%–100% dưới · Chuẩn phim/clip)</option>
            <option value="center_bottom">Giữa & Đáy (42%–100% · Phụ đề TikTok / Reels / Shorts)</option>
            <option value="top_bottom">Đỉnh & Đáy (Xóa cả Logo góc trên + Phụ đề dưới)</option>
            <option value="full">Quét chữ toàn khung hình (Full Frame)</option>
          </select>
        </div>

        <label class="switch-row" style="padding-bottom:2px;">
          <input type="checkbox" id="keepAudioCheck" checked>
          <div>
            <strong>🔊 Giữ Nguyên Audio / Giọng Nói Từ Video Gốc</strong>
          </div>
        </label>
      </div>

      <!-- 4 QUICK PRESETS -->
      <div class="preset-grid">
        <button type="button" class="preset-btn active" id="preset_char_action_clean" onclick="applyPreset('char_action_clean')">
          <strong>🕺 Độ Sâu Nhân Vật (Sạch Chữ)</strong>
          <span>Chỉ lấy Nhân Vật + Độ sâu + Audio</span>
        </button>
        <button type="button" class="preset-btn" id="preset_char_rgb_clean" onclick="applyPreset('char_rgb_clean')">
          <strong>🎭 Nhân Vật Màu Gốc (Nền Đen)</strong>
          <span>Tách nhân vật màu RGB + Xóa chữ</span>
        </button>
        <button type="button" class="preset-btn" id="preset_full_scene_clean" onclick="applyPreset('full_scene_clean')">
          <strong>🏞️ Độ Sâu Toàn Cảnh (Xóa Chữ)</strong>
          <span>Giữ cả bối cảnh + Xóa phụ đề</span>
        </button>
        <button type="button" class="preset-btn" id="preset_sbs_compare" onclick="applyPreset('sbs_compare')">
          <strong>🌓 Video Ghép Đôi Đối Chiếu</strong>
          <span>Trái: Đã xóa chữ | Phải: Độ sâu NV</span>
        </button>
      </div>

      <div class="field">
        <label>Kiểu video xuất ra (Output Mode):</label>
        <select id="colormapSelect">
          <option value="grayscale" selected>⚪ Độ Sâu Trắng – Đen Chuẩn (Gần = Trắng, Xa = Đen · ControlNet / V2V)</option>
          <option value="character_rgb">🎭 Nhân Vật Màu Gốc Trên Nền Đen (Isolated Character RGB + Audio)</option>
          <option value="clean_rgb">✨ Video Gốc Đã Xóa Caption (Clean RGB Video + Audio)</option>
          <option value="inverted">⚫ Độ Sâu Trắng – Đen Đảo Ngược (Z-Depth)</option>
          <option value="inferno">🔥 Độ Sâu Bản Đồ Nhiệt Inferno (Thermal 3D)</option>
          <option value="turbo">🌈 Độ Sâu Bản Đồ Nhiệt Turbo 3D</option>
          <option value="side_by_side">🌓 Ghép Song Song (Video Đã Xóa Chữ | Độ Sâu Nhân Vật)</option>
        </select>
      </div>

      <div class="field">
        <label>Mô hình AI Độ Sâu (Chạy trên VRAM RTX 3060):</label>
        <select id="modelSelect">
          <option value="small" selected>⚡ Depth Anything V2 — Small (FP16 · Nhanh & Nét · Đã sẵn sàng)</option>
          <option value="base">⚖️ Depth Anything V2 — Base (FP16 · Chuẩn Studio · Đã sẵn sàng)</option>
          <option value="large">💎 Depth Anything V2 — Large (FP16 · Chi tiết cực đại)</option>
        </select>
      </div>

      <details class="adv-box">
        <summary>⚙️ Tinh chỉnh Độ Nét, Khử Nháy & Tương Phản Nâng Cao</summary>
        <div class="adv-body">
          <div class="field">
            <label>Độ phân giải suy luận AI (Tensor Resolution):</label>
            <select id="inferResSelect">
              <option value="392">392 px — Siêu tốc</option>
              <option value="518" selected>518 px — Chuẩn gốc (Khuyên dùng)</option>
              <option value="700">700 px — Chi tiết cao (Rõ ngón tay & viền tóc)</option>
              <option value="924">924 px — Ultra Macro</option>
            </select>
          </div>

          <div class="field">
            <label>Giới hạn độ phân giải video xuất ra:</label>
            <select id="maxHeightSelect">
              <option value="0" selected>Giữ nguyên độ phân giải gốc (Original)</option>
              <option value="1080">Tối đa 1080p (Full HD)</option>
              <option value="720">Tối đa 720p (HD)</option>
            </select>
          </div>

          <div class="field">
            <label>Khóa chống nhấp nháy độ sáng (EMA Lock): <span class="val" id="emaVal">0.85</span></label>
            <input type="range" id="emaSlider" min="0" max="0.96" step="0.02" value="0.85"
                   oninput="document.getElementById('emaVal').innerText = this.value">
          </div>

          <div class="field">
            <label>Độ mượt liên kết Frame (Temporal Blend): <span class="val" id="blendVal">0.15</span></label>
            <input type="range" id="blendSlider" min="0" max="0.45" step="0.05" value="0.15"
                   oninput="document.getElementById('blendVal').innerText = this.value">
          </div>

          <div class="field">
            <label>Độ cong chiều sâu (Gamma Curve): <span class="val" id="gammaVal">1.00</span></label>
            <input type="range" id="gammaSlider" min="0.50" max="1.80" step="0.05" value="1.00"
                   oninput="document.getElementById('gammaVal').innerText = parseFloat(this.value).toFixed(2)">
          </div>

          <label class="check-line">
            <input type="checkbox" id="makeSheetCheck" checked>
            <span>Tạo thêm ảnh lưới Contact Sheet (0.5s/frame)</span>
          </label>
        </div>
      </details>

      <div style="display:flex;gap:10px;">
        <button type="button" class="btn-run" id="startBtn" onclick="startConversion()">
          🚀 TÁCH NHÂN VẬT · XÓA CAPTION · XUẤT ĐỘ SÂU
        </button>
        <button type="button" class="btn-stop" id="stopBtn" onclick="cancelConversion()">
          ⏹️ Dừng
        </button>
      </div>
    </div>
  </div>

  <!-- RIGHT PANEL -->
  <div>
    <div class="panel">
      <div class="status-strip">
        <div class="status-top">
          <strong id="statusTitle">Sẵn sàng — Hãy chọn một video ở khung bên trái để bắt đầu.</strong>
          <span id="pctBadge" style="color:var(--accent);font-weight:800;font-size:15px;">0%</span>
        </div>
        <div class="bar-bg"><div class="bar-fill" id="mainProgressBar"></div></div>
        <div class="status-sub">
          <span id="pipelineMeta">Engine: Depth Anything V2 + MODNet Character Matting + Caption Inpainter (CUDA)</span>
          <span id="fpsBadge" style="color:#fff;font-family:monospace;font-weight:700;">-- FPS</span>
        </div>
      </div>

      <div class="view-tabs">
        <button type="button" class="tab-btn active" id="tabBtnDual" onclick="switchViewTab('dual')">
          🌓 Xem Song Song (Gốc vs. Đã Tách Nhân Vật & Độ Sâu)
        </button>
        <button type="button" class="tab-btn" id="tabBtnWipe" onclick="switchViewTab('wipe')">
          🌗 Kéo Rèm So Sánh (Before / After Slider)
        </button>
        <button type="button" class="tab-btn" id="tabBtnSheet" onclick="switchViewTab('sheet')">
          🖼️ Ảnh Lưới Contact Sheet (0.5s/frame)
        </button>
        <div style="margin-left:auto;display:flex;gap:8px;">
          <label class="check-line" style="margin:0;font-size:12px;color:#cbd5e1;">
            <input type="checkbox" id="autoSyncCheck" checked>
            <span>Khóa phát đồng bộ 2 video</span>
          </label>
        </div>
      </div>

      <div class="dual-stage" id="stageDual">
        <div class="viewport-card">
          <div class="viewport-head">
            <span>🎥 VIDEO GỐC (ORIGINAL RGB)</span>
            <span id="leftDimTag" style="color:var(--muted);font-family:monospace;"></span>
          </div>
          <div class="viewport-body">
            <div class="empty-placeholder" id="origPlaceholder">
              <div class="big-ic">🎞️</div>
              <div>Chưa nạp video gốc</div>
            </div>
            <video id="origVideo" controls playsinline></video>
          </div>
        </div>

        <div class="viewport-card">
          <div class="viewport-head">
            <span>🕺 KẾT QUẢ: NHÂN VẬT & ĐỘ SÂU (ĐÃ XÓA CAPTION + GIỮ AUDIO)</span>
            <span id="rightDimTag" style="color:var(--accent);font-family:monospace;"></span>
          </div>
          <div class="viewport-body">
            <div class="empty-placeholder" id="depthPlaceholder">
              <div class="big-ic">🕺</div>
              <div>Bấm nút màu xanh bên trái để tách nhân vật, xóa caption & tạo video độ sâu</div>
            </div>
            <img id="liveRenderImg" class="live-frame" alt="Live GPU Frame">
            <video id="depthVideo" controls playsinline></video>
          </div>
        </div>
      </div>

      <div class="wipe-stage" id="stageWipe">
        <video id="wipeOrigVideo" loop muted playsinline></video>
        <video id="wipeDepthVideo" loop muted playsinline></video>
        <div class="wipe-handle" id="wipeHandle">
          <div class="wipe-knob">↔</div>
        </div>
      </div>

      <div class="sheet-stage" id="stageSheet">
        <div id="sheetEmptyMsg" style="color:var(--muted);padding:40px;">
          Ảnh lưới Contact Sheet (0.5s/frame) sẽ hiển thị tại đây sau khi chuyển đổi xong.
        </div>
        <img id="sheetImg" src="" alt="Contact Sheet" style="display:none;">
      </div>

      <div class="toolbar">
        <button type="button" class="btn" onclick="toggleSyncPlay()">⏯️ Phát / Dừng Đồng Bộ</button>
        <a class="btn" id="downloadBtn" href="#" download style="display:none;border-color:var(--accent);color:var(--accent);">
          💾 Tải Video Kết Quả (.MP4)
        </a>
        <button type="button" class="btn" id="revealBtn" onclick="revealInExplorer()" style="display:none;">
          📂 Hiện File Trong Thư Mục
        </button>
        <button type="button" class="btn" onclick="openOutputFolder()">
          📁 Mở Thư Mục Output
        </button>
        <input type="text" id="outputPathBox" readonly placeholder="Đường dẫn file kết quả sẽ hiện ở đây..."
               style="flex:1;min-width:220px;font-family:monospace;font-size:12px;">
      </div>
    </div>

    <div class="panel">
      <div class="panel-header">
        <div class="step-title">🗂️ Lịch Sử Video Đã Xử Lý</div>
        <button type="button" class="btn" onclick="refreshHistory()" style="padding:4px 10px;font-size:12px;">🔄 Làm mới</button>
      </div>
      <div class="history-grid" id="historyList">
        <div style="color:var(--muted);font-size:12.5px;">Chưa có video nào được tạo.</div>
      </div>
    </div>
  </div>
</div>

<script>
let currentServerPath = "";
let currentOriginalName = "";
let currentOutputPath = "";
let activeJobId = null;
let pollTimer = null;
let syncingGuard = false;

const masterFileInput = document.getElementById('masterFileInput');
const dropArea = document.getElementById('dropArea');
const origVideo = document.getElementById('origVideo');
const depthVideo = document.getElementById('depthVideo');
const wipeOrigVideo = document.getElementById('wipeOrigVideo');
const wipeDepthVideo = document.getElementById('wipeDepthVideo');

function triggerFileDialog() {
  masterFileInput.value = "";
  masterFileInput.click();
}

function toggleCaptionZoneUI() {
  const on = document.getElementById('removeCaptionCheck').checked;
  document.getElementById('captionZoneField').style.display = on ? 'block' : 'none';
}

dropArea.addEventListener('dragover', e => {
  e.preventDefault();
  e.stopPropagation();
  dropArea.classList.add('dragover');
});
dropArea.addEventListener('dragleave', e => {
  e.preventDefault();
  e.stopPropagation();
  dropArea.classList.remove('dragover');
});
dropArea.addEventListener('drop', e => {
  e.preventDefault();
  e.stopPropagation();
  dropArea.classList.remove('dragover');
  if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
    handleSelectedFile(e.dataTransfer.files[0]);
  }
});

masterFileInput.addEventListener('change', () => {
  if (masterFileInput.files && masterFileInput.files.length > 0) {
    handleSelectedFile(masterFileInput.files[0]);
  }
});

function handleSelectedFile(file) {
  currentOriginalName = file.name;
  const localBlobUrl = URL.createObjectURL(file);
  showOriginalVideo(localBlobUrl);

  const progBox = document.getElementById('uploadProgressBox');
  const progFill = document.getElementById('uploadBarFill');
  const progPct = document.getElementById('uploadPctText');
  document.getElementById('uploadFileName').innerText = `Đang nạp: ${file.name}`;
  progBox.style.display = 'block';
  progFill.style.width = '0%';
  progPct.innerText = '0%';
  document.getElementById('statusTitle').innerText = `Đang nạp video "${file.name}" vào bộ đệm...`;

  const fd = new FormData();
  fd.append('file', file);

  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/api/upload', true);

  xhr.upload.onprogress = e => {
    if (e.lengthComputable) {
      const pct = Math.round((e.loaded / e.total) * 100);
      progFill.style.width = pct + '%';
      progPct.innerText = pct + '%';
    }
  };

  xhr.onload = () => {
    progBox.style.display = 'none';
    if (xhr.status === 200) {
      const d = JSON.parse(xhr.responseText);
      applyProbedVideoInfo(d);
    } else {
      alert('Không thể nạp file video. Vui lòng kiểm tra định dạng file.');
    }
  };

  xhr.onerror = () => {
    progBox.style.display = 'none';
    alert('Lỗi kết nối tới server local khi nạp file.');
  };

  xhr.send(fd);
}

async function probeDirectPath() {
  const pathVal = document.getElementById('directPathInput').value.trim();
  if (!pathVal) {
    alert('Vui lòng dán đường dẫn file video trên máy!');
    return;
  }
  const r = await fetch('/api/probe_path', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ path: pathVal })
  });
  const d = await r.json();
  if (d.error) {
    alert(d.error);
    return;
  }
  if (d.preview_url) {
    showOriginalVideo(d.preview_url);
  }
  applyProbedVideoInfo(d);
}

function showOriginalVideo(url) {
  document.getElementById('origPlaceholder').style.display = 'none';
  origVideo.style.display = 'block';
  origVideo.src = url;
  origVideo.load();
  wipeOrigVideo.src = url;
}

function applyProbedVideoInfo(d) {
  currentServerPath = d.path;
  currentOriginalName = d.name || "video.mp4";
  document.getElementById('loadedFileCard').style.display = 'flex';
  document.getElementById('loadedName').innerText = d.name;
  document.getElementById('badgeRes').innerText = `${d.width}×${d.height}`;
  document.getElementById('badgeDur').innerText = `${d.duration_sec}s (${d.frames} frames)`;
  document.getElementById('badgeFps').innerText = `${d.fps} FPS`;
  document.getElementById('badgeSize').innerText = `${d.size_mb} MB`;
  document.getElementById('leftDimTag').innerText = `${d.width}×${d.height} · ${d.fps} FPS`;
  if (d.thumb_url) {
    document.getElementById('loadedThumb').src = d.thumb_url;
  }
  document.getElementById('statusTitle').innerText =
    `Đã nạp: ${d.name} (${d.width}×${d.height}, ${d.frames} frames). Bấm nút xanh ở cột trái để bắt đầu!`;
}

function applyPreset(name) {
  document.querySelectorAll('.preset-btn').forEach(b => b.classList.remove('active'));
  const btn = document.getElementById('preset_' + name);
  if (btn) btn.classList.add('active');

  if (name === 'char_action_clean') {
    document.getElementById('isolateCharCheck').checked = true;
    document.getElementById('removeCaptionCheck').checked = true;
    document.getElementById('keepAudioCheck').checked = true;
    document.getElementById('colormapSelect').value = 'grayscale';
    document.getElementById('modelSelect').value = 'small';
  } else if (name === 'char_rgb_clean') {
    document.getElementById('isolateCharCheck').checked = true;
    document.getElementById('removeCaptionCheck').checked = true;
    document.getElementById('keepAudioCheck').checked = true;
    document.getElementById('colormapSelect').value = 'character_rgb';
    document.getElementById('modelSelect').value = 'small';
  } else if (name === 'full_scene_clean') {
    document.getElementById('isolateCharCheck').checked = false;
    document.getElementById('removeCaptionCheck').checked = true;
    document.getElementById('keepAudioCheck').checked = true;
    document.getElementById('colormapSelect').value = 'grayscale';
    document.getElementById('modelSelect').value = 'base';
  } else if (name === 'sbs_compare') {
    document.getElementById('isolateCharCheck').checked = true;
    document.getElementById('removeCaptionCheck').checked = true;
    document.getElementById('keepAudioCheck').checked = true;
    document.getElementById('colormapSelect').value = 'side_by_side';
    document.getElementById('modelSelect').value = 'small';
  }
  toggleCaptionZoneUI();
}

async function startConversion() {
  if (!currentServerPath) {
    alert('Vui lòng chọn hoặc kéo thả một file video ở Bước 1 trước!');
    triggerFileDialog();
    return;
  }

  const payload = {
    input_path: currentServerPath,
    original_name: currentOriginalName,
    model: document.getElementById('modelSelect').value,
    colormap: document.getElementById('colormapSelect').value,
    infer_res: parseInt(document.getElementById('inferResSelect').value),
    max_out_height: parseInt(document.getElementById('maxHeightSelect').value),
    ema_alpha: parseFloat(document.getElementById('emaSlider').value),
    frame_blend: parseFloat(document.getElementById('blendSlider').value),
    gamma: parseFloat(document.getElementById('gammaSlider').value),
    keep_audio: document.getElementById('keepAudioCheck').checked,
    make_contact_sheet: document.getElementById('makeSheetCheck').checked,
    remove_captions: document.getElementById('removeCaptionCheck').checked,
    caption_zone: document.getElementById('captionZoneSelect').value,
    isolate_character: document.getElementById('isolateCharCheck').checked,
  };

  document.getElementById('startBtn').disabled = true;
  document.getElementById('stopBtn').style.display = 'inline-flex';
  document.getElementById('downloadBtn').style.display = 'none';
  document.getElementById('revealBtn').style.display = 'none';

  document.getElementById('depthPlaceholder').style.display = 'none';
  depthVideo.pause();
  depthVideo.style.display = 'none';
  const liveImg = document.getElementById('liveRenderImg');
  liveImg.style.display = 'none';

  const r = await fetch('/api/convert', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  });
  const d = await r.json();
  if (d.error) {
    alert(d.error);
    document.getElementById('startBtn').disabled = false;
    document.getElementById('stopBtn').style.display = 'none';
    return;
  }

  activeJobId = d.job_id;
  if (pollTimer) clearInterval(pollTimer);
  pollTimer = setInterval(pollJobStatus, 450);
}

async function cancelConversion() {
  if (!activeJobId) return;
  await fetch(`/api/cancel/${activeJobId}`, { method: 'POST' });
}

async function pollJobStatus() {
  if (!activeJobId) return;
  try {
    const r = await fetch(`/api/job/${activeJobId}`);
    const d = await r.json();

    document.getElementById('statusTitle').innerText = d.message || d.status;
    document.getElementById('pctBadge').innerText = (d.progress || 0) + '%';
    document.getElementById('mainProgressBar').style.width = (d.progress || 0) + '%';

    if (d.proc_fps) {
      document.getElementById('fpsBadge').innerText = `${d.proc_fps} FPS`;
    }
    if (d.resolution) {
      document.getElementById('pipelineMeta').innerText =
        `Output: ${d.resolution} · AI Tensor: ${d.infer_resolution} · ${d.provider || 'CUDA'}`;
      document.getElementById('rightDimTag').innerText = `LIVE · ${d.resolution}`;
    }

    const liveImg = document.getElementById('liveRenderImg');
    if (d.preview_url && d.status === 'processing') {
      liveImg.src = d.preview_url;
      liveImg.style.display = 'block';
    }

    if (d.status === 'completed') {
      clearInterval(pollTimer);
      document.getElementById('startBtn').disabled = false;
      document.getElementById('stopBtn').style.display = 'none';
      liveImg.style.display = 'none';

      depthVideo.style.display = 'block';
      depthVideo.src = d.output_url;
      depthVideo.load();
      wipeDepthVideo.src = d.output_url;

      document.getElementById('rightDimTag').innerText = `${d.resolution} · ${d.size_mb} MB`;
      document.getElementById('fpsBadge').innerText = `TB: ${d.avg_fps} FPS`;

      const dl = document.getElementById('downloadBtn');
      dl.href = d.output_url;
      dl.download = d.output_name;
      dl.style.display = 'inline-flex';

      currentOutputPath = d.output_path;
      document.getElementById('outputPathBox').value = d.output_path;
      document.getElementById('revealBtn').style.display = 'inline-flex';

      if (d.contact_sheet_url) {
        const sImg = document.getElementById('sheetImg');
        sImg.src = d.contact_sheet_url;
        sImg.style.display = 'inline-block';
        document.getElementById('sheetEmptyMsg').style.display = 'none';
      }

      setTimeout(() => {
        origVideo.currentTime = 0;
        depthVideo.currentTime = 0;
        origVideo.play().catch(() => {});
        depthVideo.play().catch(() => {});
      }, 300);

      refreshHistory();
      refreshHardware();
    } else if (d.status === 'error' || d.status === 'cancelled') {
      clearInterval(pollTimer);
      document.getElementById('startBtn').disabled = false;
      document.getElementById('stopBtn').style.display = 'none';
      liveImg.style.display = 'none';
      document.getElementById('depthPlaceholder').style.display = 'block';
    }
  } catch (e) {}
}

origVideo.addEventListener('play', () => {
  if (!document.getElementById('autoSyncCheck').checked || syncingGuard) return;
  if (depthVideo.src) {
    syncingGuard = true;
    depthVideo.currentTime = origVideo.currentTime;
    depthVideo.play().catch(() => {});
    setTimeout(() => { syncingGuard = false; }, 80);
  }
});
origVideo.addEventListener('pause', () => {
  if (!document.getElementById('autoSyncCheck').checked || syncingGuard) return;
  if (depthVideo.src) {
    syncingGuard = true;
    depthVideo.pause();
    setTimeout(() => { syncingGuard = false; }, 80);
  }
});
origVideo.addEventListener('seeking', () => {
  if (!document.getElementById('autoSyncCheck').checked || syncingGuard) return;
  if (depthVideo.src && Math.abs(depthVideo.currentTime - origVideo.currentTime) > 0.15) {
    syncingGuard = true;
    depthVideo.currentTime = origVideo.currentTime;
    setTimeout(() => { syncingGuard = false; }, 80);
  }
});

function toggleSyncPlay() {
  if (origVideo.paused) {
    if (depthVideo.src) depthVideo.currentTime = origVideo.currentTime;
    origVideo.play().catch(() => {});
    if (depthVideo.src) depthVideo.play().catch(() => {});
  } else {
    origVideo.pause();
    depthVideo.pause();
  }
}

function switchViewTab(mode) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('stageDual').style.display = (mode === 'dual') ? 'grid' : 'none';
  document.getElementById('stageWipe').style.display = (mode === 'wipe') ? 'block' : 'none';
  document.getElementById('stageSheet').style.display = (mode === 'sheet') ? 'block' : 'none';

  if (mode === 'dual') {
    document.getElementById('tabBtnDual').classList.add('active');
    wipeOrigVideo.pause();
    wipeDepthVideo.pause();
  } else if (mode === 'wipe') {
    document.getElementById('tabBtnWipe').classList.add('active');
    origVideo.pause();
    depthVideo.pause();
    if (wipeOrigVideo.src && wipeDepthVideo.src) {
      wipeOrigVideo.currentTime = 0;
      wipeDepthVideo.currentTime = 0;
      wipeOrigVideo.play().catch(() => {});
      wipeDepthVideo.play().catch(() => {});
    }
  } else if (mode === 'sheet') {
    document.getElementById('tabBtnSheet').classList.add('active');
  }
}

const stageWipe = document.getElementById('stageWipe');
const wipeHandle = document.getElementById('wipeHandle');
let isDraggingWipe = false;

stageWipe.addEventListener('mousedown', () => { isDraggingWipe = true; });
window.addEventListener('mouseup', () => { isDraggingWipe = false; });
stageWipe.addEventListener('mousemove', e => {
  if (!isDraggingWipe && e.buttons !== 1) return;
  const rect = stageWipe.getBoundingClientRect();
  let pct = ((e.clientX - rect.left) / rect.width) * 100;
  pct = Math.max(2, Math.min(98, pct));
  wipeHandle.style.left = pct + '%';
  wipeDepthVideo.style.clipPath = `inset(0 0 0 ${pct}%)`;
});

async function refreshHardware() {
  try {
    const r = await fetch('/api/hardware');
    const d = await r.json();
    const el = document.getElementById('hwStatusText');
    if (d.vram_total_mb > 0) {
      el.innerText = `${d.gpu_name} · VRAM trống: ${d.vram_free_mb}/${d.vram_total_mb} MB · Depth V2 + MODNet CUDA`;
    } else {
      el.innerText = `${d.gpu_name} · Providers: ${d.providers.join(', ')}`;
    }
  } catch (e) {}
}

async function refreshHistory() {
  try {
    const r = await fetch('/api/history');
    const d = await r.json();
    const box = document.getElementById('historyList');
    if (!d.files || d.files.length === 0) {
      box.innerHTML = '<div style="color:var(--muted);font-size:12.5px;">Chưa có video nào trong output/depth_videos.</div>';
      return;
    }
    box.innerHTML = d.files.map(f => `
      <div class="hist-row">
        <div style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex:1;">
          <strong style="color:#fff;">${f.name}</strong>
          <span style="color:var(--muted);margin-left:8px;">${f.size_mb} MB · ${f.time_str}</span>
        </div>
        <div style="display:flex;gap:6px;">
          <button type="button" class="btn" style="padding:4px 10px;font-size:12px;"
                  onclick='previewHistoryItem(${JSON.stringify(f)})'>👁️ Xem trên khung</button>
          <a class="btn" style="padding:4px 10px;font-size:12px;" href="${f.url}" download="${f.name}">💾 Tải</a>
        </div>
      </div>
    `).join('');
  } catch (e) {}
}

function previewHistoryItem(f) {
  switchViewTab('dual');
  document.getElementById('depthPlaceholder').style.display = 'none';
  document.getElementById('liveRenderImg').style.display = 'none';
  depthVideo.style.display = 'block';
  depthVideo.src = f.url;
  depthVideo.load();
  depthVideo.play().catch(() => {});
  wipeDepthVideo.src = f.url;

  currentOutputPath = f.path;
  document.getElementById('outputPathBox').value = f.path;
  const dl = document.getElementById('downloadBtn');
  dl.href = f.url;
  dl.download = f.name;
  dl.style.display = 'inline-flex';
  document.getElementById('revealBtn').style.display = 'inline-flex';
}

async function revealInExplorer() {
  if (!currentOutputPath) return;
  await fetch('/api/reveal_file', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ path: currentOutputPath })
  });
}

async function openOutputFolder() {
  await fetch('/api/open_folder', { method: 'POST' });
}

refreshHardware();
refreshHistory();
</script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# 9. AIOHTTP ROUTES & SERVER HANDLERS
# ---------------------------------------------------------------------------
async def handle_index(request: web.Request) -> web.Response:
    return web.Response(
        text=INDEX_HTML,
        content_type="text/html",
        headers={"Cache-Control": "no-store, no-cache, must-revalidate, max-age=0"},
    )


async def handle_hardware(request: web.Request) -> web.Response:
    return web.json_response(get_hardware_status())


async def handle_history(request: web.Request) -> web.Response:
    files = []
    for p in sorted(OUTPUT_DIR.glob("*.mp4"), key=lambda x: x.stat().st_mtime, reverse=True):
        if p.name.startswith("_"):
            continue
        st = p.stat()
        files.append(
            {
                "name": p.name,
                "path": str(p),
                "url": f"/output/{p.name}",
                "size_mb": round(st.st_size / (1024 * 1024), 2),
                "time_str": time.strftime("%H:%M:%S %d/%m", time.localtime(st.st_mtime)),
            }
        )
    return web.json_response({"files": files[:30]})


async def handle_upload(request: web.Request) -> web.Response:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    reader = await request.multipart()
    field = await reader.next()
    while field is not None and field.name != "file":
        field = await reader.next()
    if field is None:
        return web.json_response({"error": "Không nhận được file tải lên"}, status=400)

    orig_name = Path(field.filename or "upload.mp4").name
    ext = Path(orig_name).suffix.lower() or ".mp4"
    safe_stem = sanitize_stem(Path(orig_name).stem)
    safe_filename = f"upload_{int(time.time())}_{safe_stem}{ext}"
    dest = UPLOAD_DIR / safe_filename

    with open(dest, "wb") as f:
        while True:
            chunk = await field.read_chunk()
            if not chunk:
                break
            f.write(chunk)

    try:
        info = probe_video_metadata(dest)
        info["name"] = orig_name
        return web.json_response(info)
    except Exception as exc:
        return web.json_response({"error": str(exc)}, status=400)


async def handle_probe_path(request: web.Request) -> web.Response:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = await request.json()
    raw_path = data.get("path", "").strip().strip('"').strip("'")
    p = Path(raw_path)
    if not raw_path or not p.exists() or not p.is_file():
        return web.json_response({"error": f"Không tìm thấy file: {raw_path}"}, status=400)

    try:
        info = probe_video_metadata(p)
        prev_name = f"_direct_{sanitize_stem(p.stem)}{p.suffix.lower()}"
        prev_dest = OUTPUT_DIR / prev_name
        if not prev_dest.exists():
            shutil.copy2(str(p), str(prev_dest))
        info["preview_url"] = f"/output/{prev_name}"
        return web.json_response(info)
    except Exception as exc:
        return web.json_response({"error": str(exc)}, status=400)


async def handle_convert(request: web.Request) -> web.Response:
    data = await request.json()
    input_path = data.get("input_path", "").strip().strip('"')
    if not input_path or not Path(input_path).exists():
        return web.json_response({"error": f"Không tìm thấy file video đầu vào: {input_path}"}, status=400)

    job_id = uuid.uuid4().hex[:10]
    JOBS[job_id] = {
        "job_id": job_id,
        "status": "queued",
        "progress": 0,
        "message": "Đang khởi tạo tiến trình GPU CUDA...",
    }
    t = threading.Thread(target=process_video_job, args=(job_id, data), daemon=True)
    t.start()
    return web.json_response({"job_id": job_id})


async def handle_cancel(request: web.Request) -> web.Response:
    job_id = request.match_info.get("job_id", "")
    job = JOBS.get(job_id)
    if job:
        job["cancel_requested"] = True
    return web.json_response({"ok": True})


async def handle_job_status(request: web.Request) -> web.Response:
    job_id = request.match_info.get("job_id", "")
    job = JOBS.get(job_id)
    if not job:
        return web.json_response({"error": "Job not found"}, status=404)
    return web.json_response(job)


async def handle_open_folder(request: web.Request) -> web.Response:
    try:
        subprocess.Popen(["explorer.exe", str(OUTPUT_DIR)])
    except Exception:
        pass
    return web.json_response({"ok": True, "folder": str(OUTPUT_DIR)})


async def handle_reveal_file(request: web.Request) -> web.Response:
    data = await request.json()
    p = Path(data.get("path", ""))
    try:
        if p.exists():
            subprocess.Popen(["explorer.exe", f"/select,{str(p)}"])
        else:
            subprocess.Popen(["explorer.exe", str(OUTPUT_DIR)])
    except Exception:
        pass
    return web.json_response({"ok": True})


def create_app() -> web.Application:
    app = web.Application(client_max_size=2 * 1024 * 1024 * 1024)
    app.router.add_get("/", handle_index)
    app.router.add_get("/api/hardware", handle_hardware)
    app.router.add_get("/api/history", handle_history)
    app.router.add_post("/api/upload", handle_upload)
    app.router.add_post("/api/probe_path", handle_probe_path)
    app.router.add_post("/api/convert", handle_convert)
    app.router.add_post("/api/cancel/{job_id}", handle_cancel)
    app.router.add_get("/api/job/{job_id}", handle_job_status)
    app.router.add_post("/api/open_folder", handle_open_folder)
    app.router.add_post("/api/reveal_file", handle_reveal_file)
    app.router.add_static("/output", str(OUTPUT_DIR))
    return app


def main() -> None:
    parser = argparse.ArgumentParser(description="SVEN Depth Video Studio v2.5 (Local Web UI + CLI)")
    parser.add_argument("--cli", action="store_true", help="Run in headless CLI mode")
    parser.add_argument("--input", "-i", type=str, help="Input video file path")
    parser.add_argument("--model", "-m", type=str, default="small", choices=["small", "base", "large"])
    parser.add_argument(
        "--colormap",
        "-c",
        type=str,
        default="grayscale",
        choices=["grayscale", "character_rgb", "clean_rgb", "inverted", "inferno", "turbo", "side_by_side"],
    )
    parser.add_argument("--infer-res", type=int, default=518)
    parser.add_argument("--ema", type=float, default=0.85)
    parser.add_argument("--blend", type=float, default=0.15)
    parser.add_argument("--gamma", type=float, default=1.0)
    parser.add_argument("--no-remove-captions", action="store_true", help="Disable caption removal")
    parser.add_argument("--caption-zone", type=str, default="bottom", choices=["bottom", "center_bottom", "top_bottom", "full"])
    parser.add_argument("--no-isolate-character", action="store_true", help="Keep full background instead of isolating character")
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=7865)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    if args.cli:
        if not args.input:
            print("Error: --input is required when using --cli", file=sys.stderr)
            sys.exit(1)
        job_id = "cli_job"
        JOBS[job_id] = {"job_id": job_id, "status": "queued", "progress": 0, "message": "Starting CLI conversion..."}
        params = {
            "input_path": args.input,
            "model": args.model,
            "colormap": args.colormap,
            "infer_res": args.infer_res,
            "ema_alpha": args.ema,
            "frame_blend": args.blend,
            "gamma": args.gamma,
            "keep_audio": True,
            "make_contact_sheet": True,
            "remove_captions": not args.no_remove_captions,
            "caption_zone": args.caption_zone,
            "isolate_character": not args.no_isolate_character,
        }
        process_video_job(job_id, params)
        final_state = JOBS[job_id]
        print(json.dumps(final_state, indent=2, ensure_ascii=False))
        sys.exit(0 if final_state.get("status") == "completed" else 1)

    url = f"http://{args.host}:{args.port}"
    if not args.no_browser:
        import webbrowser
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()

    app = create_app()
    web.run_app(app, host=args.host, port=args.port, print=None)


if __name__ == "__main__":
    main()

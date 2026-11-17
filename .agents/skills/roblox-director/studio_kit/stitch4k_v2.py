#!/usr/bin/env python3
"""Join R pitched captures per frame into 2160x3840 frames: frames4k_v2/<id>/ -> frames_4k/<id>/NNNNN.jpg.
Pure rotations about one camera centre, so each tile maps by an exact homography; seams are feathered."""
import json, os, sys, cv2, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "tiles4k.json")))
W, H = 2160, 3840
_cache = {}
def plan(sid, w, h):
    key = (sid, w, h)
    if key in _cache: return _cache[key]
    t = T[sid]; V = np.radians(t["V"]); Ft = np.radians(t["Ft"])
    fo = (H / 2) / np.tan(V / 2); ft = (h / 2) / np.tan(Ft / 2)
    u, v = np.meshgrid(np.arange(W, dtype=np.float32) + 0.5, np.arange(H, dtype=np.float32) + 0.5)
    x = (u - W / 2) / fo; y = -(v - H / 2) / fo; z = -np.ones_like(x)
    maps, wts = [], []
    feather = 40.0
    for p in t["p"]:
        d = np.radians(p)
        yt = np.cos(d) * y + np.sin(d) * z
        zt = -np.sin(d) * y + np.cos(d) * z
        mx = (w / 2 + ft * x / (-zt)).astype(np.float32)
        my = (h / 2 - ft * yt / (-zt)).astype(np.float32)
        wy = np.clip(np.minimum(my, h - my) / feather, 0, 1)
        wx = np.clip(np.minimum(mx, w - mx) / feather, 0, 1)
        maps.append((mx - 0.5, my - 0.5)); wts.append((wy * wx).astype(np.float32))
    tot = np.maximum(sum(wts), 1e-6)
    bands = []
    for (mx, my), wi in zip(maps, wts):
        wn = wi / tot
        rows = np.where(wn.max(axis=1) > 1e-4)[0]
        r0, r1 = int(rows.min()), int(rows.max()) + 1
        bands.append((r0, r1, np.ascontiguousarray(mx[r0:r1]), np.ascontiguousarray(my[r0:r1]), np.ascontiguousarray(wn[r0:r1, :, None])))
    _cache.clear(); _cache[key] = bands
    return bands
def compose(ims, bands):
    acc = np.zeros((H, W, 3), np.float32)
    for im, (r0, r1, mx, my, wt) in zip(ims, bands):
        acc[r0:r1] += cv2.remap(im, mx, my, cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE).astype(np.float32) * wt
    return np.clip(acc, 0, 255).astype(np.uint8)
def shot(sid, redo=False):
    R = T[sid]["rows"]
    src = os.path.join(HERE, "frames4k_v2", sid); dst = os.path.join(HERE, "frames_4k_v2", sid)
    if not os.path.isdir(src): return 0
    os.makedirs(dst, exist_ok=True)
    fs = sorted(f for f in os.listdir(src) if f[:5].isdigit())
    n = 0
    for i in range(len(fs) // R):
        out = os.path.join(dst, f"{i + 1:05d}.jpg")
        if os.path.exists(out) and not redo and os.path.getmtime(out) > os.path.getmtime(os.path.join(src, fs[i * R + R - 1])): n += 1; continue
        ims = [cv2.imread(os.path.join(src, fs[i * R + k])) for k in range(R)]
        if any(im is None for im in ims): continue
        h, w = ims[0].shape[:2]
        cv2.imwrite(out, compose(ims, plan(sid, w, h)), [cv2.IMWRITE_JPEG_QUALITY, 94]); n += 1
    return n
if __name__ == "__main__":
    for sid in sys.argv[1:]: print(sid, shot(sid, redo=True))

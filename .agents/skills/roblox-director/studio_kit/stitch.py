#!/usr/bin/env python3
"""Join tile pairs from render2.py into sharp 1080x1920 frames.
frames2/<id>/00001.png (upper tile, JPEG data), 00002.png (lower tile) ... -> frames_hd/<id>/00001.jpg ...
Camera maths: Roblox FieldOfView is vertical. Tile k is the base camera pitched by +-V/4 with FOV V/2+margin."""
import json, os, sys, cv2, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
FOV = json.load(open(os.path.join(HERE, "fov.json")))
MARGIN = 6.0
W, H = 1080, 1920
_maps = {}
def maps(V, w, h):
    key = (round(V, 3), w, h)
    if key in _maps: return _maps[key]
    Vr = np.radians(V); d = Vr / 4; Ft = np.radians(V / 2 + MARGIN)
    fo = (H / 2) / np.tan(Vr / 2); ft = (h / 2) / np.tan(Ft / 2)
    u, v = np.meshgrid(np.arange(W, dtype=np.float32) + 0.5, np.arange(H, dtype=np.float32) + 0.5)
    x = (u - W / 2) / fo; y = -(v - H / 2) / fo; z = -np.ones_like(x)
    out = []
    for sgn in (1, -1):
        dd = sgn * d
        yt = np.cos(dd) * y + np.sin(dd) * z
        zt = -np.sin(dd) * y + np.cos(dd) * z
        mx = (w / 2 + ft * x / (-zt)).astype(np.float32) - 0.5
        my = (h / 2 - ft * yt / (-zt)).astype(np.float32) - 0.5
        out.append((mx, my))
    feather = 24
    wgt = np.clip((H / 2 + feather - (np.arange(H) + 0.5)) / (2 * feather), 0, 1).astype(np.float32)  # 1 = upper tile
    wgt = np.repeat(wgt[:, None], W, axis=1)[..., None]
    _maps[key] = (out, wgt)
    return _maps[key]
def stitch(a, b, V):
    h, w = a.shape[:2]
    (m1, m2), wgt = maps(V, w, h)
    t1 = cv2.remap(a, m1[0], m1[1], cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    t2 = cv2.remap(b, m2[0], m2[1], cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    return (t1 * wgt + t2 * (1 - wgt)).astype(np.uint8)
def shot(sid):
    src = os.path.join(HERE, "frames2", sid); dst = os.path.join(HERE, "frames_hd", sid)
    os.makedirs(dst, exist_ok=True)
    fs = sorted(f for f in os.listdir(src) if f[:5].isdigit())
    n = 0
    for i in range(0, len(fs) - 1, 2):
        a = cv2.imread(os.path.join(src, fs[i])); b = cv2.imread(os.path.join(src, fs[i + 1]))
        if a is None or b is None: continue
        out = stitch(a, b, FOV[sid])
        cv2.imwrite(os.path.join(dst, f"{i // 2 + 1:05d}.jpg"), out, [cv2.IMWRITE_JPEG_QUALITY, 95]); n += 1
    return n
if __name__ == "__main__":
    for sid in sys.argv[1:]: print(sid, shot(sid))

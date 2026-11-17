"""Stitch finished 4K shots frame by frame until a deadline (seconds, argv[1]); safe to re-run, skips frames already done."""
import json, os, sys, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cv2, numpy as np, stitch4k_v2 as stitch4k
T = stitch4k.T
def finished():
    dn = os.listdir(os.path.join(HERE, "done"))
    ids = []
    for sc in json.load(open(os.path.join(HERE, "..", "shots", "shots.json"))):
        for s in sc["shots"]:
            if any(f.endswith("_" + s["id"] + ".json") and int(f.split("_")[0]) >= 1794748000000 for f in dn): ids.append(s["id"])
    return ids
def task(a):
    sid, i = a
    R = T[sid]["rows"]; src = os.path.join(HERE, "frames4k_v2", sid); dst = os.path.join(HERE, "frames_4k_v2", sid)
    out = os.path.join(dst, f"{i + 1:05d}.jpg")
    if os.path.exists(out): return 0
    ims = [cv2.imread(os.path.join(src, f"{i * R + k + 1:05d}.png")) for k in range(R)]
    if any(im is None for im in ims): return 0
    h, w = ims[0].shape[:2]
    img = stitch4k.compose(ims, stitch4k.plan(sid, w, h))
    os.makedirs(dst, exist_ok=True)
    cv2.imwrite(out + ".tmp.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 94]); os.replace(out + ".tmp.jpg", out)
    return 1
if __name__ == "__main__":
    end = time.time() + float(sys.argv[1] if len(sys.argv) > 1 else 160)
    jobs = []
    for sid in finished():
        n = len([f for f in os.listdir(os.path.join(HERE, "frames4k_v2", sid)) if f[:5].isdigit()]) // T[sid]["rows"]
        d = os.path.join(HERE, "frames_4k_v2", sid)
        have = set(os.listdir(d)) if os.path.isdir(d) else set()
        jobs += [(sid, i) for i in range(n) if f"{i + 1:05d}.jpg" not in have]
    done = 0
    p = Pool(2)
    if True:
        for r in p.imap(task, jobs[:int(sys.argv[2]) if len(sys.argv) > 2 else 400], chunksize=4):
            done += r
            if time.time() > end: break
    p.terminate()
    print("stitched", done, "left", len(jobs) - done)

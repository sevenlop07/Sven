import os, sys, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cv2, stitch4k
T = stitch4k.T
def task(a):
    sid, i = a
    R = T[sid]["rows"]; src = os.path.join(HERE, "frames4k", sid); dst = os.path.join(HERE, "frames_4k", sid)
    out = os.path.join(dst, f"{i + 1:05d}.jpg")
    if os.path.exists(out) and os.path.getmtime(out) > os.path.getmtime(os.path.join(src, f"{i * R + R:05d}.png")): return 0
    ims = [cv2.imread(os.path.join(src, f"{i * R + k + 1:05d}.png")) for k in range(R)]
    if any(im is None for im in ims): return 0
    img = stitch4k.compose(ims, stitch4k.plan(sid, ims[0].shape[1], ims[0].shape[0]))
    cv2.imwrite(out + ".tmp.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 94]); os.replace(out + ".tmp.jpg", out); return 1
if __name__ == "__main__":
    end = time.time() + 150
    jobs = []
    for sid in open(os.path.join(HERE, "_redo.txt")).read().split():
        n = len([f for f in os.listdir(os.path.join(HERE, "frames4k", sid)) if f[:5].isdigit()]) // T[sid]["rows"]
        jobs += [(sid, i) for i in range(n)]
    p = Pool(2); d = 0
    for r in p.imap(task, jobs, chunksize=4):
        d += r
        if time.time() > end: break
    p.terminate(); print("restitched", d, "of", len(jobs))

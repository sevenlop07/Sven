#!/usr/bin/env python3
# measure.py - colour/light check for caption-free stills, one PNG/JPG per shot. Zero tokens.
# usage: python3 measure.py stills/*.png            (name interior shots with "int_" in the file name)
#        python3 measure.py --video take.mov --times 0.4,2.1,3.9   (grabs one frame per time with ffmpeg)
#        python3 measure.py --compare "before/*.png" "after/*.png"  (twist shift: stills from 4 s before vs 4 s after the cut)
USAGE = "usage: measure.py stills/*.png | --video take.mov --times t1,t2,... | --compare 'before/*.png' 'after/*.png'"
import sys, os, subprocess, tempfile, glob
import cv2, numpy as np

def stats(path):
    im = cv2.imread(path)
    h = im.shape[0]
    im = im[int(h * .08):int(h * .92)]                      # skip top/bottom UI bands
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    v = hsv[..., 2] / 255.0; s = hsv[..., 1] / 255.0
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(float)
    warm = ((im[..., 2].astype(float) - im[..., 0]) / 255).mean()
    hue = hsv[..., 0].astype(int) * 2                       # 0-360
    chroma = (s > .20) & (v > .15)
    fam = {}
    if chroma.any():
        hh = hue[chroma]
        bins = {"red": (hh < 15) | (hh >= 345), "orange": (hh >= 15) & (hh < 45), "yellow": (hh >= 45) & (hh < 70),
                "green": (hh >= 70) & (hh < 165), "cyan": (hh >= 165) & (hh < 200), "blue": (hh >= 200) & (hh < 255),
                "purple": (hh >= 255) & (hh < 345)}
        fam = {k: m.mean() * chroma.mean() for k, m in bins.items()}  # share of ALL pixels
    return dict(name=os.path.basename(path), bright=v.mean(), sat=s.mean(), contrast=g.std() / 255, warm=warm,
                p1=np.percentile(g, 1), p99=np.percentile(g, 99), clip=(g >= 250).mean() * 100,
                crush=(g <= 12).mean() * 100, fam=fam, interior="int_" in os.path.basename(path))

def grab(video, times):
    d = tempfile.mkdtemp(); out = []
    for i, t in enumerate(times):
        p = os.path.join(d, f"shot{i+1:03d}.png")
        subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", video, "-frames:v", "1", p], check=True)
        out.append(p)
    return out

args = sys.argv[1:]
if args and args[0] == "--compare":
    A = [stats(f) for f in sorted(glob.glob(args[1]))]; B = [stats(f) for f in sorted(glob.glob(args[2]))]
    if not A or not B: sys.exit(USAGE)
    best = 0
    for k in ("bright", "sat", "warm", "contrast"):
        a = np.mean([r[k] for r in A]); b = np.mean([r[k] for r in B]); best = max(best, abs(b - a) if k != "contrast" else 0)
        print(f"{k:9s} before {a:+.3f}  after {b:+.3f}  delta {b - a:+.3f}")
    print(f"largest bright/sat/warm shift {best:.3f}: target >=0.15, minimum 0.10  {'PASS' if best >= .15 else ('MIN-PASS' if best >= .10 else 'FAIL')}")
    sys.exit(0)
if args and args[0] == "--video":
    files = grab(args[1], [float(x) for x in args[3].split(",")])
else:
    files = sorted(f for a in args for f in glob.glob(a))
if not files:
    sys.exit(USAGE)
R = [stats(f) for f in files]
print(f"{'shot':24s} bright  sat   contr  warm   p1  p99  clip% crush%")
for r in R:
    flag = []
    if r["sat"] > .60: flag.append("SAT>0.6")
    if not 10 <= r["p1"] <= 25: flag.append("p1")
    if r["crush"] > 5: flag.append("CRUSH")
    if r["interior"] and r["clip"] < 1: flag.append("NO-PRACTICAL?")
    print(f"{r['name'][:24]:24s} {r['bright']:.3f}  {r['sat']:.3f} {r['contrast']:.3f} {r['warm']:+.3f} {r['p1']:4.0f} {r['p99']:4.0f} {r['clip']:5.1f} {r['crush']:5.1f}  {' '.join(flag)}")
n = len(R)
sat = np.array([r["sat"] for r in R]); p99 = np.array([r["p99"] for r in R])
fams = {}
for r in R:
    for k, x in r["fam"].items(): fams[k] = fams.get(k, 0) + x
tot = len(R)  # share of ALL pixels (neutrals count in the denominator, like a palette)
top = max(fams, key=fams.get) if fams else "-"
ints = [r for r in R if r["interior"]]
def ok(b): return "PASS" if b else "FAIL"
print(f"\nshots {n}")
print(f"median sat {np.median(sat):.3f}  (target 0.35-0.50)  {ok(.35 <= np.median(sat) <= .50)}")
print(f"shots sat>0.6 {np.mean(sat > .6)*100:.0f}%  (target <=10%)  {ok(np.mean(sat > .6) <= .10)}")
print(f"shots p99>=240 {np.mean(p99 >= 240)*100:.0f}%  (target >=25%)  {ok(np.mean(p99 >= 240) >= .25)}")
print(f"shots p99<225 {np.mean(p99 < 225)*100:.0f}%  (target <=50%)  {ok(np.mean(p99 < 225) <= .50)}")
p1ok = np.mean([10 <= r['p1'] <= 25 for r in R]); cr = np.mean([r['crush'] <= 5 for r in R])
print(f"shots with p1 in 10-25 {p1ok*100:.0f}%  (target >=80%)  {ok(p1ok >= .8)}")
print(f"shots with crushed (<=12) pixels <=5% {cr*100:.0f}%  (target 100%)  {ok(cr == 1)}")
print(f"top hue family {top} {fams.get(top,0)/tot*100:.0f}% of all pixels  (target <=40%)  {ok(fams.get(top,0)/tot <= .40)}")
if ints:
    sh = np.mean([r["clip"] >= 1 for r in ints])
    print(f"interior shots with a visible practical (clip>=1%) {sh*100:.0f}%  (target >=80%)  {ok(sh >= .8)}")

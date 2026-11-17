#!/usr/bin/env python3
"""sheetlib.py - shared parser + timing model for script sheets (used by script_check.py, plan_timing.py, make_caps.py).

A script sheet is any markdown table whose header has a `line` and a `speaker` column (templates/script-sheet.md,
the "Full script sheet" table in examples/gold-*.md). Rows:
  spoken row : speaker is a tag (NARR, DAD, ...). A slow read is marked at the end of the line: `(0.6x)` or `(read at 0.6x)`.
  pause row  : the line cell says `*(pause 0.8 s, hold the shot)*`.
Timing model (script.md section 3, HYPOTHESIS until a real take replaces it): first word at 0.1 s; each spoken row lasts
spoken_words / 3.67 / rate seconds (220 wpm; normal sentence gaps are inside that average); pause rows add their seconds;
runtime = last row end + tail. Numbers count as spoken words ("2045" = twenty forty five = 3).
"""
import re

WPS = 220 / 60
FIRST_WORD = 0.1
ONES = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
        "seventeen eighteen nineteen").split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
ABBR = re.compile(r"\b(Mr|Mrs|Ms|Dr|St)\.")
RATE = re.compile(r"\(\s*(?:read at\s*)?(\d*\.?\d+)\s*x\s*\)", re.I)
PAUSE = re.compile(r"pause\s+(\d*\.?\d+)\s*s", re.I)


def w_int(n):
    if n < 20: return [ONES[n]]
    if n < 100: return [TENS[n // 10]] + ([ONES[n % 10]] if n % 10 else [])
    if n < 1000: return [ONES[n // 100], "hundred"] + (w_int(n % 100) if n % 100 else [])
    if 1100 <= n <= 2099 and not 2000 <= n <= 2009:                      # years: nineteen eighty five, twenty forty five
        return w_int(n // 100) + (w_int(n % 100) if n % 100 else ["hundred"])
    return w_int(n // 1000) + ["thousand"] + (w_int(n % 1000) if n % 1000 else [])


def spoken(tok):
    """written token -> list of spoken words (numbers, times, 2C, $5, 50%)."""
    t = tok.strip("\"'“”‘’()*,.!?;:")
    if not t: return []
    m = re.fullmatch(r"(\d{1,2}):(\d\d)", t)
    if m:
        h, mm = int(m[1]), int(m[2])
        return w_int(h) + ([] if mm == 0 else (["oh"] + w_int(mm) if mm < 10 else w_int(mm)))
    m = re.fullmatch(r"(\$)?(\d[\d,]*)(st|nd|rd|th|s|%|¢|[A-Za-z])?", t)
    if m:
        out = w_int(int(m[2].replace(",", "")))
        if m[1]: out.append("dollars")
        if m[3] in ("%",): out.append("percent")
        elif m[3] == "¢": out.append("cents")
        elif m[3] and len(m[3]) == 1 and m[3] not in "s": out.append(m[3])   # 2C
        return out
    if re.search(r"\d", t):
        return sum((w_int(int(x)) for x in re.findall(r"\d+", t)), []) + re.findall(r"[A-Za-z]+", t)
    return [t]


def syl(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w: return 0
    if len(w) <= 3: return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))


def sentences(text):
    t = ABBR.sub(r"\1", text)
    return [s.strip() for s in re.split(r"(?<=[.?!])[\"”]?\s+", t) if s.strip()]


def split_row(cells):
    return [c.strip() for c in cells.strip().strip("|").split("|")]


def find_table(path):
    """the largest table with `line` + `speaker` headers -> (column index dict, list of cell lists + [line number])."""
    best, cur = ({}, []), None
    for no, ln in enumerate(open(path, encoding="utf-8")):
        s = ln.strip()
        if not s.startswith("|"):
            if cur and len(cur[1]) > len(best[1]): best = cur
            cur = None; continue
        c = split_row(s)
        low = [x.lower() for x in c]
        if any(x.startswith("line") for x in low) and any(x.startswith("speaker") for x in low):
            if cur and len(cur[1]) > len(best[1]): best = cur
            idx = {}
            for i, x in enumerate(low):
                for key in ("#", "time", "line", "speaker", "beat", "shot", "camera", "lighting", "music", "sfx", "caption"):
                    if x.startswith(key) and key not in idx: idx[key] = i
            cur = (idx, []); continue
        if cur is None or set(s) <= set("|-: "): continue
        cur[1].append(c + [no])          # last item = line number in the file
    if cur and len(cur[1]) > len(best[1]): best = cur
    return best


def load(path, tail=1.2):
    """-> dict(rows=[...], runtime, speech_end). Each row: kind, text, speaker, beat, hl, rate, words (spoken count),
    tokens (written), start, end, sheet_time (the time cell as written)."""
    idx, raw = find_table(path)
    if not raw: raise SystemExit(f"{path}: no table with 'line' and 'speaker' columns")
    g = lambda c, k: c[idx[k]] if k in idx and idx[k] < len(c) else ""
    rows, t = [], FIRST_WORD
    for c in raw:
        line = g(c, "line"); sp = g(c, "speaker").strip("` ")
        m = PAUSE.search(line)
        if m and sp in ("", "-"):
            d = float(m[1]); rows.append(dict(kind="pause", start=t, end=t + d, secs=d, text="", beat="pause", lineno=c[-1])); t += d; continue
        if sp in ("", "-") or not line: continue
        rate = 1.0
        mr = RATE.search(line)
        if mr: rate = float(mr[1]); line = RATE.sub("", line)
        line = line.replace("*", "").strip()
        toks = line.split()
        n = sum(len(spoken(x)) for x in toks)
        d = n / WPS / rate
        rows.append(dict(kind="line", text=line, speaker=sp.upper(), beat=g(c, "beat"), hl=g(c, "caption"), rate=rate,
                         words=n, tokens=toks, start=t, end=t + d, sheet_time=g(c, "time"), lineno=c[-1]))
        t += d
    return dict(rows=rows, speech_end=t, runtime=t + tail, tail=tail, time_col=idx.get("time"))

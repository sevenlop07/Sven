#!/usr/bin/env python3
"""Send one job to the Roblox bridge and wait for the result.
  rb.py call <tool> '<json args>' [save.png]
  rb.py lua <file.lua> [Edit|Client|Server]      run a Luau file in Studio
  rb.py cap <save.png>                            screen capture"""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
SID_F = os.path.join(HERE, "studio_id.txt")
sid = open(SID_F).read().strip() if os.path.exists(SID_F) else ""
def send(job, timeout=170):
    name = f"{int(time.time()*1000)}.json"
    tmp = os.path.join(HERE, "queue", name + ".tmp")
    json.dump(job, open(tmp, "w")); os.rename(tmp, os.path.join(HERE, "queue", name))
    d = os.path.join(HERE, "done", name); t0 = time.time()
    while not os.path.exists(d):
        if time.time() - t0 > timeout: return {"error": "no answer from bridge (is the bridge window open?)"}
        time.sleep(0.25)
    for _ in range(40):
        time.sleep(0.15)
        try: return json.load(open(d))
        except ValueError: pass
    return json.load(open(d))
def text(r):
    res = r.get("res", r)
    if isinstance(res, dict) and "result" in res:
        return "\n".join(c.get("text", str(c)) for c in res["result"].get("content", []))
    return json.dumps(res)[:3000]
if __name__ == "__main__":
    m = sys.argv[1]
    if m == "call":
        args = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
        if sys.argv[2] != "list_roblox_studios": args.setdefault("studio_id", sid)
        job = {"name": sys.argv[2], "arguments": args}
        if len(sys.argv) > 4: job["save"] = sys.argv[4]
        r = send(job)
    elif m == "lua":
        code = open(sys.argv[2]).read()
        r = send({"name": "execute_luau", "arguments": {"code": code, "datamodel_type": sys.argv[3] if len(sys.argv) > 3 else "Edit", "studio_id": sid}})
    elif m == "cap":
        r = send({"name": "screen_capture", "arguments": {"capture_id": "ScreenCapture_1", "studio_id": sid}, "save": sys.argv[2]})
    print(f"[{r.get('ms', '?')} ms]", text(r)[:6000])

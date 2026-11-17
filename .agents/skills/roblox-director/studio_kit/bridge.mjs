// Bridge between job files in this folder and Roblox Studio's own MCP server (StudioMCP, stdio).
// Cross-platform (Windows & macOS): Automatically locates StudioMCP.exe on Windows or StudioMCP on macOS.
// Jobs: queue/<name>.json -> result in done/<name>.json
//   { "name": "<tool>", "arguments": {...}, "save": "caps/x.png" }          one tool call
//   { "batch": [ {name, arguments, save?}, ... ] }                           several calls, in order
//   { "render": { "tool": "...", "code_arg": "code", "template": "...{{F}}...", "frames": [a, b], "capture": {name, arguments}, "out": "frames/s001" } }
// Stop it: close this Terminal window (or Ctrl+C).
import { spawn } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
fs.mkdirSync(path.join(HERE, "queue"), { recursive: true });
fs.mkdirSync(path.join(HERE, "done"), { recursive: true });

function findStudioMCP() {
  if (process.env.STUDIO_MCP_BIN && fs.existsSync(process.env.STUDIO_MCP_BIN)) {
    return process.env.STUDIO_MCP_BIN;
  }
  if (process.platform === "win32") {
    const localAppData = process.env.LOCALAPPDATA || path.join(process.env.USERPROFILE || "C:\\Users\\Default", "AppData", "Local");
    const versionsDir = path.join(localAppData, "Roblox", "Versions");
    if (fs.existsSync(versionsDir)) {
      const candidates = fs.readdirSync(versionsDir)
        .map((d) => path.join(versionsDir, d, "StudioMCP.exe"))
        .filter((p) => fs.existsSync(p))
        .sort((a, b) => fs.statSync(b).mtimeMs - fs.statSync(a).mtimeMs);
      if (candidates.length > 0) return candidates[0];
    }
    return path.join(versionsDir, "StudioMCP.exe");
  }
  return "/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP";
}

const BIN = findStudioMCP();
const log = (...a) => { const s = new Date().toTimeString().slice(0, 8) + " " + a.join(" "); console.log(s); fs.appendFileSync(path.join(HERE, "bridge.log"), s + "\n"); };
fs.writeFileSync(path.join(HERE, "bridge.log"), "");
log("bridge starting, folder:", HERE, "binary:", BIN);
if (!fs.existsSync(BIN)) { log("FAILED: StudioMCP not found at", BIN); process.exit(1); }
const p = spawn(BIN, [], { stdio: ["pipe", "pipe", "pipe"] });
let buf = "", id = 0; const wait = new Map();
p.stdout.on("data", (d) => { buf += d; let i; while ((i = buf.indexOf("\n")) >= 0) { const line = buf.slice(0, i).trim(); buf = buf.slice(i + 1); if (!line) continue;
  try { const m = JSON.parse(line); if (m.id != null && wait.has(m.id)) { wait.get(m.id)(m); wait.delete(m.id); } } catch { log("non-json from StudioMCP:", line.slice(0, 200)); } } });
p.stderr.on("data", (d) => fs.appendFileSync(path.join(HERE, "bridge_stderr.log"), d));
p.on("exit", (c) => { log("StudioMCP exited with code", c); process.exit(1); });
const call = (method, params, ms = 180000) => new Promise((ok) => { const i = ++id; const t = setTimeout(() => { wait.delete(i); ok({ error: { message: "timeout after " + ms + " ms" } }); }, ms);
  wait.set(i, (m) => { clearTimeout(t); ok(m); }); p.stdin.write(JSON.stringify({ jsonrpc: "2.0", id: i, method, params }) + "\n"); });
const out = (f, o) => { fs.mkdirSync(path.dirname(path.join(HERE, f)), { recursive: true }); fs.writeFileSync(path.join(HERE, f), JSON.stringify(o, null, 1)); };
const saveImages = (r, save, tag) => { const c = r?.result?.content; if (!Array.isArray(c)) return r; let n = 0;
  for (const item of c) if (item.type === "image" && item.data) { const ext = (item.mimeType || "image/png").split("/")[1].replace("jpeg", "jpg");
    const f = save ? (n ? save.replace(/(\.\w+)?$/, `_${n}$1`) : save) : `caps/${tag}_${n}.${ext}`; const full = path.join(HERE, f);
    fs.mkdirSync(path.dirname(full), { recursive: true }); fs.writeFileSync(full, Buffer.from(item.data, "base64")); item.data = "(saved to " + f + ")"; item.bytes = fs.statSync(full).size; n++; }
  return r; };
const one = async (j, tag) => saveImages(await call("tools/call", { name: j.name, arguments: j.arguments || {} }, j.timeout || 180000), j.save, tag);

const init = await call("initialize", { protocolVersion: "2024-11-05", capabilities: {}, clientInfo: { name: "roblox-bridge", version: "1.0" } }, 30000);
p.stdin.write(JSON.stringify({ jsonrpc: "2.0", method: "notifications/initialized" }) + "\n");
out("tools.json", { init, tools: await call("tools/list", {}, 30000) });
log("connected to StudioMCP:", JSON.stringify(init?.result?.serverInfo || init?.error || {}));
const Q = path.join(HERE, "queue");
for (;;) {
  const jobs = fs.readdirSync(Q).filter((f) => f.endsWith(".json")).sort();
  if (!jobs.length) { fs.writeFileSync(path.join(HERE, "bridge_alive.txt"), String(Date.now())); await new Promise((r) => setTimeout(r, 400)); continue; }
  const f = jobs[0], tag = f.replace(/\.json$/, "");
  let j; try { j = JSON.parse(fs.readFileSync(path.join(Q, f), "utf8")); } catch (e) { fs.renameSync(path.join(Q, f), path.join(Q, f + ".bad")); log("bad job", f, String(e)); continue; }
  fs.rmSync(path.join(Q, f)); const t0 = Date.now(); let res;
  try {
    if (j.batch) { res = []; for (const [k, b] of j.batch.entries()) res.push(await one(b, tag + "_" + k)); }
    else if (j.render) { const R = j.render; res = { frames: 0, errors: [] }; const [a, b] = R.frames;
      for (let fr = a; fr <= b; fr++) {
        const fn = path.join(HERE, R.out, String(fr).padStart(5, "0") + ".png"); if (fs.existsSync(fn) && !R.force) { res.frames++; continue; }
        const e = await call("tools/call", { name: R.tool, arguments: { ...(R.args || {}), [R.code_arg]: R.template.replaceAll("{{F}}", String(fr)) } }, 60000);
        if (e.error || e?.result?.isError) { res.errors.push({ fr, e: JSON.stringify(e).slice(0, 300) }); if (res.errors.length > 5) break; continue; }
        const c = saveImages(await call("tools/call", R.capture, 60000), path.join(R.out, String(fr).padStart(5, "0") + ".png"), tag);
        if (c.error || c?.result?.isError) { res.errors.push({ fr, c: JSON.stringify(c).slice(0, 300) }); if (res.errors.length > 5) break; continue; }
        res.frames++; if (fr % 20 === 0) fs.writeFileSync(path.join(HERE, "render_progress.txt"), `${tag} ${fr}/${b}`); } }
    else res = await one(j, tag);
  } catch (e) { res = { error: String(e) }; }
  out("done/" + f, { ms: Date.now() - t0, res }); log("job", f, "done in", Date.now() - t0, "ms");
}

#!/usr/bin/env python3
"""Auto-Launching Stdio <-> HTTP MCP Bridge for Blender 5.3 (scenario-blender).

Connects stdio MCP clients (Antigravity, Claude Desktop, Cursor) to Blender 5.3's
local `scenario-blender` MCP server at `http://127.0.0.1:9876/mcp`.
- If Blender 5.3 GUI (or an existing headless daemon) is already listening on port 9876,
  forwards requests directly to that live session.
- If port 9876 is not reachable, automatically spawns a headless Blender 5.3 MCP daemon
  (`blender.exe --background --online-mode --command scenario_blender --port 9876`),
  waits for it to come online, and forwards the request seamlessly.
"""

from __future__ import annotations

import argparse
import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

DEFAULT_URL = "http://127.0.0.1:9876/mcp"
DEFAULT_BLENDER_EXE = r"C:\Program Files\Blender Foundation\Blender 5.3\blender.exe"
_DAEMON_PROC = None


def _is_port_open(host: str = "127.0.0.1", port: int = 9876, timeout: float = 0.35) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _ensure_blender_mcp_running(url: str, blender_exe: str, port: int = 9876) -> bool:
    global _DAEMON_PROC
    if _is_port_open("127.0.0.1", port):
        return True
    if not os.path.isfile(blender_exe):
        return False
    creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    _DAEMON_PROC = subprocess.Popen(
        [
            blender_exe,
            "--background",
            "--online-mode",
            "--command",
            "scenario_blender",
            "--port",
            str(port),
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creationflags,
    )
    deadline = time.time() + 12.0
    while time.time() < deadline:
        if _is_port_open("127.0.0.1", port):
            return True
        time.sleep(0.25)
    return _is_port_open("127.0.0.1", port)


def forward(url: str, message: dict, blender_exe: str, port: int = 9876, timeout: int = 300):
    if not _is_port_open("127.0.0.1", port):
        _ensure_blender_mcp_running(url, blender_exe, port)
    data = json.dumps(message).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            return json.loads(body) if body else None
    except urllib.error.HTTPError as err:
        body = err.read()
        try:
            return json.loads(body)
        except ValueError:
            return {
                "jsonrpc": "2.0",
                "id": message.get("id"),
                "error": {"code": -32000, "message": f"HTTP {err.code}: {body[:200]!r}"},
            }
    except (urllib.error.URLError, OSError) as err:
        return {
            "jsonrpc": "2.0",
            "id": message.get("id"),
            "error": {"code": -32001, "message": f"Blender MCP is not reachable at {url}: {err}"},
        }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="blender-mcp-bridge")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--port", type=int, default=9876)
    parser.add_argument("--blender", default=DEFAULT_BLENDER_EXE)
    args = parser.parse_args(argv)
    out = sys.stdout
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            message = json.loads(line)
        except ValueError as err:
            out.write(
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": None,
                        "error": {"code": -32700, "message": f"Parse error: {err}"},
                    }
                )
                + "\n"
            )
            out.flush()
            continue
        response = forward(args.url, message, args.blender, args.port)
        if response is not None and message.get("id") is not None:
            out.write(json.dumps(response) + "\n")
            out.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())

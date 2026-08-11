"""Serve the built static site locally for preview (Python only)."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "site"


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview the built site")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    if not ROOT.exists():
        raise SystemExit("Run `python3 build.py` first.")

    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    print(f"Preview: http://127.0.0.1:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()

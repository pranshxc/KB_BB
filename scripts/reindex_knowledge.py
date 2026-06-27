#!/usr/bin/env python3
"""Trigger knowledge-rag reindex.

knowledge-rag automatically indexes all documents in its configured
documents_dir on MCP server startup. This script starts the server
briefly to trigger that indexing.

Note: If indexing takes longer than the timeout (default 120s),
the remaining files will be indexed on the next MCP connection.

Usage:
  python reindex_knowledge.py
  python reindex_knowledge.py --path security-brain
"""

import argparse
import os
import signal
import subprocess
import sys
import time
from pathlib import Path


def find_knowledge_rag_dir() -> Path | None:
    cwd = Path.cwd().resolve()
    for parent in [cwd] + list(cwd.parents):
        candidate = parent / "knowledge-rag"
        if (candidate / "pyproject.toml").is_file():
            return candidate
    return None


def find_venv_python(kr_dir: Path) -> Path | None:
    for cand in [
        kr_dir / ".venv" / "bin" / "python",
        kr_dir / "venv" / "bin" / "python",
    ]:
        if cand.is_file():
            return cand.resolve()
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Trigger knowledge-rag reindex (by starting the MCP server)"
    )
    parser.add_argument("--path", default="security-brain", help="Documents path (used in config)")
    parser.add_argument("--kr-dir", default=None, help="Path to knowledge-rag directory")
    parser.add_argument("--timeout", type=int, default=120, help="Seconds to run server (default: 120)")
    args = parser.parse_args()

    print()
    print("=" * 60)
    print("  knowledge-rag Reindex Trigger")
    print("  Note: knowledge-rag auto-indexes on MCP server startup.")
    print("  This script starts the server to trigger that behavior.")
    print("=" * 60)

    kr_dir = Path(args.kr_dir) if args.kr_dir else find_knowledge_rag_dir()
    if not kr_dir:
        print("\nERROR: Cannot find knowledge-rag directory.")
        print("  Run from inside the KB_BB repo or pass --kr-dir.")
        sys.exit(1)

    py = find_venv_python(kr_dir)
    if not py:
        print("\nknowledge-rag venv not found.")
        print(f"  Expecting .venv/ or venv/ in {kr_dir}")
        print("  Run the install script first.")
        sys.exit(1)

    print(f"\n  knowledge-rag: {kr_dir}")
    print(f"  Python:        {py}")
    print(f"  Timeout:       {args.timeout}s")

    env = os.environ.copy()
    env.setdefault("KNOWLEDGE_RAG_DIR", str(kr_dir.resolve()))
    if "DYLD_LIBRARY_PATH" not in env and Path("/opt/homebrew/opt/expat/lib").is_dir():
        env["DYLD_LIBRARY_PATH"] = "/opt/homebrew/opt/expat/lib"

    print(f"\n  Starting knowledge-rag for {args.timeout}s...")
    print(f"  (Indexing progress will show below)")
    print(f"  (Press Ctrl+C to stop early)\n")

    proc = subprocess.Popen(
        [str(py), "-m", "mcp_server.server", "--transport", "sse"],
        cwd=str(kr_dir),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    try:
        proc.wait(timeout=args.timeout)
    except subprocess.TimeoutExpired:
        proc.send_signal(signal.SIGTERM)
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()

    out = proc.stdout.read() if proc.stdout else ""
    for line in out.split("\n")[-10:]:
        if line.strip():
            print(f"  {line.strip()}")

    print(f"\n  Server stopped (exit code: {proc.returncode})")
    print(f"\n  Index files will be in: {kr_dir}/data/")
    print(f"  The server will resume indexing on next MCP connection startup.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Trigger knowledge-rag reindex.

This script wraps the knowledge-rag indexing. It finds the knowledge-rag
directory and runs the proper reindex command.

Usage:
  python reindex_knowledge.py
  python reindex_knowledge.py --path security-brain
"""

import argparse
import os
import subprocess
import sys
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
    parser = argparse.ArgumentParser(description="Trigger knowledge-rag reindex")
    parser.add_argument("--path", default="security-brain", help="Documents path for reindex")
    parser.add_argument("--kr-dir", default=None, help="Path to knowledge-rag directory")
    args = parser.parse_args()

    kr_dir = Path(args.kr_dir) if args.kr_dir else find_knowledge_rag_dir()
    if not kr_dir:
        print("ERROR: Cannot find knowledge-rag directory.")
        print("  Run from inside the KB_BB repo or pass --kr-dir.")
        sys.exit(1)

    py = find_venv_python(kr_dir)
    if not py:
        print("knowledge-rag venv not found.")
        print(f"  Expecting .venv/ or venv/ in {kr_dir}")
        print("  Run the install script first.")
        sys.exit(1)

    print(f"Found knowledge-rag: {kr_dir}")
    print(f"Python: {py}")

    # The knowledge-rag MCP server auto-indexes on startup.
    # For reindex, we run the server briefly or use the Python API.
    print()
    print("Starting knowledge-rag for reindex...")
    print("(Press Ctrl+C after indexing completes)")

    env = os.environ.copy()
    kr_parent = kr_dir.parent
    env.setdefault("KNOWLEDGE_RAG_DIR", str(kr_dir.resolve()))
    if "DYLD_LIBRARY_PATH" not in env and Path("/opt/homebrew/opt/expat/lib").is_dir():
        env["DYLD_LIBRARY_PATH"] = "/opt/homebrew/opt/expat/lib"

    # Run the server with SSE transport to trigger indexing
    result = subprocess.run(
        [str(py), "-m", "mcp_server.server", "--transport", "sse"],
        cwd=str(kr_dir),
        env=env,
        timeout=60,
        capture_output=True,
        text=True,
    )
    print(result.stdout[-500:] if result.stdout else "")
    print(result.stderr[-500:] if result.stderr else "")
    print(f"\nExit code: {result.returncode}")

    if result.returncode == 0:
        print("Reindex complete.")
    else:
        print("Reindex may have been interrupted (non-zero exit).")
        print("The server will auto-index on next MCP connection startup.")


if __name__ == "__main__":
    main()

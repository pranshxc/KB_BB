#!/usr/bin/env python3
"""Write user-specific MCP config files with absolute local paths.

Usage:
  python generate_mcp_config.py
  python generate_mcp_config.py --kr-dir /path/to/knowledge-rag
  python generate_mcp_config.py --output-dir .
  python generate_mcp_config.py --client claude  # print to stdout
"""

import argparse
import json
import os
import sys
from pathlib import Path


def find_venv_python(kr_dir: Path) -> Path | None:
    """Find the venv Python in a knowledge-rag directory."""
    candidates = [
        kr_dir / ".venv" / "bin" / "python",
        kr_dir / "venv" / "bin" / "python",
        kr_dir / ".venv" / "Scripts" / "python.exe",
        kr_dir / "venv" / "Scripts" / "python.exe",
    ]
    for c in candidates:
        if c.is_file():
            return c.resolve()
    return None


def detect_expat_path() -> str | None:
    """Detect Homebrew expat path on macOS."""
    for p in ["/opt/homebrew/opt/expat/lib", "/usr/local/opt/expat/lib"]:
        if Path(p).is_dir():
            return p
    return None


def make_claude_config(python_path: str, expat_path: str | None) -> dict:
    """Generate the Claude Code MCP server block."""
    entry = {
        "type": "stdio",
        "command": python_path,
        "args": ["-m", "mcp_server.server"],
    }
    if expat_path:
        entry["env"] = {"DYLD_LIBRARY_PATH": expat_path}
    return {"mcpServers": {"security-brain": entry}}


def make_opencode_config(python_path: str, expat_path: str | None) -> dict:
    """Generate the opencode MCP server block."""
    entry = {
        "type": "local",
        "command": [python_path, "-m", "mcp_server.server"],
        "enabled": True,
    }
    if expat_path:
        entry["environment"] = {"DYLD_LIBRARY_PATH": expat_path}
    return {"$schema": "https://opencode.ai/config.json", "mcp": {"security-brain": entry}}


def make_generic_config(python_path: str) -> dict:
    """Generate a generic MCP server block."""
    return {"mcpServers": {"security-brain": {"command": python_path, "args": ["-m", "mcp_server.server"]}}}


def main():
    parser = argparse.ArgumentParser(description="Generate user-specific MCP config files.")
    parser.add_argument("--kr-dir", default=None, help="Path to knowledge-rag directory")
    parser.add_argument("--output-dir", default=None, help="Output directory for config files")
    parser.add_argument(
        "--client",
        choices=["claude", "opencode", "generic"],
        default=None,
        help="Print config for a specific client to stdout instead of writing files",
    )
    args = parser.parse_args()

    # Auto-detect knowledge-rag directory
    kr_dir = None
    if args.kr_dir:
        kr_dir = Path(args.kr_dir)
    else:
        # Walk up from CWD looking for knowledge-rag/pyproject.toml
        cwd = Path.cwd().resolve()
        for parent in [cwd] + list(cwd.parents):
            candidate = parent / "knowledge-rag"
            if (candidate / "pyproject.toml").is_file():
                kr_dir = candidate
                break
        if not kr_dir and (cwd / ".." / "knowledge-rag" / "pyproject.toml").resolve().is_file():
            kr_dir = (cwd / ".." / "knowledge-rag").resolve()
        if not kr_dir:
            print("Error: Cannot find knowledge-rag directory. Use --kr-dir", file=sys.stderr)
            sys.exit(1)

    python_path = find_venv_python(kr_dir)
    if not python_path:
        print(f"Error: No venv Python found in {kr_dir}", file=sys.stderr)
        print("Run the install script first to set up the virtual environment.", file=sys.stderr)
        sys.exit(1)

    expat_path = detect_expat_path()
    python_str = str(python_path)

    # Single-client output mode
    if args.client:
        configs = {
            "claude": make_claude_config,
            "opencode": make_opencode_config,
            "generic": make_generic_config,
        }
        config = configs[args.client](python_str, expat_path)
        print(json.dumps(config, indent=2))
        return

    # File output mode
    output_dir = Path(args.output_dir) if args.output_dir else kr_dir.parent / "configs"
    output_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "claude-code.mcp.json": make_claude_config(python_str, expat_path),
        "opencode.json": make_opencode_config(python_str, expat_path),
        "generic-mcp.json": make_generic_config(python_str),
    }

    for fname, content in files.items():
        path = output_dir / fname
        path.write_text(json.dumps(content, indent=2) + "\n", encoding="utf-8")
        print(f"  Written: {path}")

    # Print the claude mcp add command
    print(f"\n  Or register directly:")
    print(f"    claude mcp add security-brain -s user -- {python_str} -m mcp_server.server")
    if expat_path:
        print(f"\n  (DYLD_LIBRARY_PATH={expat_path} is set in config)")


if __name__ == "__main__":
    main()

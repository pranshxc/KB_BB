#!/usr/bin/env python3
"""
Print user-friendly MCP setup instructions for the Security Brain.

Usage:
  python print_mcp_setup.py
  python print_mcp_setup.py --venv-python /path/to/venv/bin/python
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def find_venv_python() -> str | None:
    """Auto-detect the venv Python path."""
    candidates = [
        Path("knowledge-rag/.venv/bin/python"),
        Path("knowledge-rag/venv/bin/python"),
        Path(".venv/bin/python"),
        Path("venv/bin/python"),
    ]
    for c in candidates:
        if c.is_file():
            return str(c.resolve())
    # Try which
    kr = shutil.which("knowledge-rag")
    if kr:
        return kr
    return None


def resolve_base_dir() -> Path:
    """Find the base directory (where security-brain/ lives)."""
    # Check if we're in the project root
    for p in [Path.cwd(), Path.cwd().parent]:
        if (p / "security-brain").is_dir():
            return p
    return Path.cwd()


def main():
    parser = argparse.ArgumentParser(description="Print MCP setup instructions.")
    parser.add_argument("--venv-python", default=None, help="Path to venv Python")
    args = parser.parse_args()

    base = resolve_base_dir()
    py = args.venv_python or find_venv_python()

    print("=" * 60)
    print("  Security Brain — MCP Setup Instructions")
    print("=" * 60)

    # ── 1. Activate venv ─────────────────────────────────────────────
    print(f"""
{chr(27)}[96m1. Activate Virtual Environment{chr(27)}[0m

   cd {base / 'knowledge-rag'}
   source .venv/bin/activate
""")

    # ── 2. Start MCP Server ──────────────────────────────────────────
    print(f"{chr(27)}[96m2. Start MCP Server{chr(27)}[0m")

    if py:
        print(f"   {py} -m mcp_server.server")
    else:
        print(f"   cd {base / 'knowledge-rag'}")
        print(f"   source .venv/bin/activate")
        print(f"   knowledge-rag")
    print()

    # ── 3. Test MCP Connection ───────────────────────────────────────
    print(f"{chr(27)}[96m3. Test MCP Connection{chr(27)}[0m")
    print(f"   If using Claude Code:")
    print(f"     claude mcp list")
    print(f"     claude mcp restart security-brain")
    print()

    # ── 4. Claude Code Setup ─────────────────────────────────────────
    print(f"{chr(27)}[96m4. Claude Code Setup{chr(27)}[0m")
    print(f"   Config file: {base / 'configs/claude-code.mcp.json'}")
    print()
    if py:
        display_py = py.replace("/Users/", "~/")
        print(f"   Or add via CLI:")
        print(f"     claude mcp add security-brain -s user -- {display_py} -m mcp_server.server")
        print()
    print(f"   Content of {base / 'configs/claude-code.mcp.json'}:")
    print(f"""   {{
     "mcpServers": {{
       "security-brain": {{
         "type": "stdio",
         "command": "{py or '/path/to/venv/bin/python'}",
         "args": ["-m", "mcp_server.server"]
       }}
     }}
   }}""")
    print()

    # ── 5. opencode Setup ────────────────────────────────────────────
    print(f"{chr(27)}[96m5. opencode Setup{chr(27)}[0m")
    print(f"   Config file: {base / 'configs/opencode.json'}")
    print(f"   Copy to ~/.config/opencode/opencode.json or project-level opencode.json")
    print()

    # ── 6. Generic MCP Clients ───────────────────────────────────────
    print(f"{chr(27)}[96m6. Any MCP Client{chr(27)}[0m")
    print(f"   Config file: {base / 'configs/generic-mcp.json'}")
    print(f"   Point your client at:")
    if py:
        print(f"     Command: {py}")
        print(f"     Args:    -m mcp_server.server")
    else:
        print(f"     See configs/generic-mcp.json")
    print()

    # ── 7. Troubleshooting ──────────────────────────────────────────
    print(f"{chr(27)}[96m7. Troubleshooting{chr(27)}[0m")
    print(f"   Issue: Python expat library conflict on macOS")
    print(f"   Fix:   export DYLD_LIBRARY_PATH=\"/opt/homebrew/opt/expat/lib:$DYLD_LIBRARY_PATH\"")
    print()
    print(f"   Issue: 'knowledge-rag: command not found'")
    print(f"   Fix:   source .venv/bin/activate first, or use full path to Python")
    print()
    print(f"   Issue: No documents indexed")
    print(f"   Fix:   Ensure security-brain/ has files, run: knowledge-rag")
    print(f"          (it auto-indexes on startup)")
    print()
    print(f"   Issue: MCP server not connecting")
    print(f"   Fix:   Check Python version (3.11+ required)")
    print(f"          Check ~/.claude.json for correct paths")
    print(f"          Restart Claude Code completely")

    # ── 8. Example Prompts ──────────────────────────────────────────
    print(f"""
{chr(27)}[96m8. Example Prompts{chr(27)}[0m

   Use my Security Brain to find HackerOne examples of password reset token invalidation bugs.
   Search for IDOR bugs in organization membership systems and produce a secure review checklist.
   Use the knowledge base to review OAuth redirect_uri handling.
   Find SSRF-related HackerOne reports and summarize defensive mitigations.
   Search my Security Brain for GraphQL authorization bypass patterns.
   Use the security taxonomy to explain common XSS prevention techniques.
   Find file upload vulnerability patterns in my Security Brain.
   Search for information disclosure examples and build a detection checklist.
   What does the knowledge base say about JWT algorithm confusion?
   Use the Security Brain to create a secure code review checklist for API authentication.
""")

    # ── 9. macOS expat note ─────────────────────────────────────────
    print(f"{chr(27)}[93mNote:{chr(27)}[0m On macOS with Homebrew Python, you may need to set")
    print(f"      DYLD_LIBRARY_PATH=\"/opt/homebrew/opt/expat/lib\"")
    print(f"      as an environment variable in your MCP config.")
    print("=" * 60)


if __name__ == "__main__":
    main()

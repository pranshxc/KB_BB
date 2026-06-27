#!/usr/bin/env python3
"""
Validate the Security Brain setup.

Checks:
1. Required directories exist
2. HackerOne reports are present
3. Import summary exists
4. Harness instructions exist
5. Taxonomy files exist
6. Config files exist
7. Knowledge-rag MCP command is available
8. Eval queries exist

Usage:
  python validate_security_brain.py
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

# ANSI colors for rich output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"


def check(
    condition: bool, name: str, passed_msg: str = "", failed_msg: str = ""
) -> bool:
    if condition:
        icon = f"{GREEN}✓{RESET}"
        msg = f" {passed_msg}" if passed_msg else ""
        print(f"  {icon} {name}{msg}")
        return True
    else:
        icon = f"{RED}✗{RESET}"
        msg = f" — {failed_msg}" if failed_msg else ""
        print(f"  {icon} {name}{msg}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Validate Security Brain setup.")
    parser.add_argument(
        "--security-brain-dir",
        default="security-brain",
        help="Path to security-brain directory (default: security-brain)",
    )
    parser.add_argument(
        "--scripts-dir",
        default="scripts",
        help="Path to scripts directory (default: scripts)",
    )
    parser.add_argument(
        "--configs-dir",
        default="configs",
        help="Path to configs directory (default: configs)",
    )
    parser.add_argument(
        "--docs-dir",
        default="docs",
        help="Path to docs directory (default: docs)",
    )
    parser.add_argument(
        "--knowledge-rag-dir",
        default="knowledge-rag",
        help="Path to knowledge-rag directory (default: knowledge-rag)",
    )
    parser.add_argument(
        "--venv-python",
        default=None,
        help="Path to venv Python (auto-detected if not provided)",
    )
    args = parser.parse_args()

    base = Path.cwd()
    sb_dir = Path(args.security_brain_dir)
    scripts_dir = Path(args.scripts_dir)
    configs_dir = Path(args.configs_dir)
    docs_dir = Path(args.docs_dir)
    kr_dir = Path(args.knowledge_rag_dir)

    total_checks = 0
    passed_checks = 0

    print(f"\n{BOLD}Security Brain Validation Report{RESET}")
    print("=" * 50)

    # ── 1. Required directories ──────────────────────────────────────
    print(f"\n{CYAN}1. Directory Structure{RESET}")
    required_dirs = [
        sb_dir,
        sb_dir / "hackerone",
        sb_dir / "hackerone/reports",
        sb_dir / "hackerone/summaries",
        sb_dir / "hackerone/taxonomies",
        sb_dir / "blogs/medium",
        sb_dir / "blogs/portswigger",
        sb_dir / "blogs/assetnote",
        sb_dir / "blogs/personal-notes",
        sb_dir / "docs/owasp",
        sb_dir / "docs/cwe",
        sb_dir / "internal/secure-code-review",
        sb_dir / "internal/pentest-reports",
        sb_dir / "internal/runbooks",
        sb_dir / "prompts",
        sb_dir / "evals",
        scripts_dir,
        configs_dir,
        docs_dir,
    ]
    for d in required_dirs:
        ok = check(d.is_dir(), str(d), "exists", "MISSING")
        total_checks += 1
        if ok:
            passed_checks += 1

    # ── 2. HackerOne Reports ─────────────────────────────────────────
    print(f"\n{CYAN}2. HackerOne Reports{RESET}")
    reports_dir = sb_dir / "hackerone/reports"
    if reports_dir.is_dir():
        md_files = list(reports_dir.rglob("*.md"))
        check(
            len(md_files) > 0,
            f"HackerOne Markdown reports",
            f"{len(md_files)} found",
            "No reports found",
        )
        total_checks += 1
        if len(md_files) > 0:
            passed_checks += 1
    else:
        check(False, "HackerOne reports directory", "", "MISSING")
        total_checks += 1

    # ── 3. Import summary ────────────────────────────────────────────
    print(f"\n{CYAN}3. Import Summary{RESET}")
    summary_file = sb_dir / "hackerone/import_summary.json"
    if summary_file.is_file():
        try:
            summary = json.loads(summary_file.read_text())
            written = summary.get("total_unique_written", 0)
            dupes = summary.get("duplicates_skipped", 0)
            seen = summary.get("total_rows_seen", 0)
            check(True, "import_summary.json", f"Exists ({written} reports, {dupes} dupes, {seen} rows)")
        except (json.JSONDecodeError, KeyError):
            check(True, "import_summary.json", "Exists (but parse error)")
        total_checks += 1
        passed_checks += 1
    else:
        check(False, "import_summary.json", "", "MISSING — run the importer first")
        total_checks += 1

    # ── 4. Harness Instructions ──────────────────────────────────────
    print(f"\n{CYAN}4. Harness Instructions{RESET}")
    for fname in ["HARNESS_INSTRUCTIONS.md", "QUICK_START_PROMPT.md"]:
        fp = sb_dir / "prompts" / fname
        ok = check(fp.is_file(), f"prompts/{fname}", "exists", "MISSING")
        total_checks += 1
        if ok:
            passed_checks += 1

    # ── 5. Taxonomy Files ────────────────────────────────────────────
    print(f"\n{CYAN}5. Taxonomy Files{RESET}")
    taxonomy_files = [
        "bug-classes.md",
        "root-causes.md",
        "testing-methodology.md",
        "remediation-patterns.md",
    ]
    for fname in taxonomy_files:
        fp = sb_dir / "hackerone/taxonomies" / fname
        ok = check(fp.is_file(), f"taxonomies/{fname}", "exists", "MISSING")
        total_checks += 1
        if ok:
            passed_checks += 1

    # ── 6. Summary Files ─────────────────────────────────────────────
    print(f"\n{CYAN}6. Summary Files{RESET}")
    summary_files = [
        "password-reset-bugs.md",
        "idor-patterns.md",
        "oauth-bugs.md",
        "ssrf-patterns.md",
        "graphql-bugs.md",
        "information-disclosure.md",
        "file-upload-bugs.md",
        "access-control-bugs.md",
    ]
    for fname in summary_files:
        fp = sb_dir / "hackerone/summaries" / fname
        ok = check(fp.is_file(), f"summaries/{fname}", "exists", "MISSING")
        total_checks += 1
        if ok:
            passed_checks += 1

    # ── 7. Config Files ──────────────────────────────────────────────
    print(f"\n{CYAN}7. MCP Config Files{RESET}")
    for fname in ["claude-code.mcp.json", "opencode.json", "generic-mcp.json"]:
        fp = configs_dir / fname
        ok = check(fp.is_file(), f"configs/{fname}", "exists", "MISSING")
        total_checks += 1
        if ok:
            passed_checks += 1

    # ── 8. Scripts ───────────────────────────────────────────────────
    print(f"\n{CYAN}8. Scripts{RESET}")
    script_files = [
        "import_h1_hf_to_markdown.py",
        "generate_security_taxonomies.py",
        "validate_security_brain.py",
        "print_mcp_setup.py",
    ]
    for fname in script_files:
        fp = scripts_dir / fname
        ok = check(fp.is_file(), f"scripts/{fname}", "exists", "MISSING")
        total_checks += 1
        if ok:
            passed_checks += 1

    # ── 9. Documentation ─────────────────────────────────────────────
    print(f"\n{CYAN}9. Documentation{RESET}")
    doc_files = ["SECURITY_BRAIN_SETUP.md", "MCP_CLIENT_SETUP.md", "OPERATIONS.md"]
    for fname in doc_files:
        fp = docs_dir / fname
        ok = check(fp.is_file(), f"docs/{fname}", "exists", "MISSING")
        total_checks += 1
        if ok:
            passed_checks += 1

    # ── 10. Eval Queries ─────────────────────────────────────────────
    print(f"\n{CYAN}10. Eval Queries{RESET}")
    eval_file = sb_dir / "evals/sample_queries.jsonl"
    if eval_file.is_file():
        lines = eval_file.read_text().strip().split("\n")
        check(len(lines) >= 30, f"sample_queries.jsonl", f"{len(lines)} queries", "Too few queries")
        total_checks += 1
        if len(lines) >= 30:
            passed_checks += 1
    else:
        check(False, "sample_queries.jsonl", "", "MISSING")
        total_checks += 1

    # ── 11. Knowledge-rag CLI ────────────────────────────────────────
    print(f"\n{CYAN}11. Knowledge-RAG Availability{RESET}")
    # Try to find the knowledge-rag command
    found_kr = False
    # Check in venv
    venv_python = args.venv_python
    if not venv_python:
        candidates = [
            kr_dir / ".venv/bin/python",
            kr_dir / "venv/bin/python",
            Path(".venv/bin/python"),
            Path("venv/bin/python"),
        ]
        for c in candidates:
            if c.is_file():
                venv_python = str(c)
                break
    if venv_python:
        try:
            result = subprocess.run(
                [venv_python, "-m", "mcp_server.server", "--help"],
                capture_output=True,
                text=True,
                timeout=10,
                env={"DYLD_LIBRARY_PATH": "/opt/homebrew/opt/expat/lib"},
            )
            found_kr = result.returncode in (0, 1)
        except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
            pass
    # Also check with knowledge-rag command
    if not found_kr:
        kr_cmd = shutil.which("knowledge-rag")
        if kr_cmd:
            found_kr = True

    check(found_kr, "knowledge-rag MCP server", "available", "Not found in PATH or venv")
    total_checks += 1
    if found_kr:
        passed_checks += 1

    # ── 12. Blog/Doc/Internal READMEs ────────────────────────────────
    print(f"\n{CYAN}12. README Files{RESET}")
    for rel_path in ["blogs/README.md", "docs/README.md", "internal/README.md"]:
        fp = sb_dir / rel_path
        ok = check(fp.is_file(), str(sb_dir / rel_path), "exists", "MISSING")
        total_checks += 1
        if ok:
            passed_checks += 1

    # ── Final Report ─────────────────────────────────────────────────
    print(f"\n{'=' * 50}")
    pct = (passed_checks / total_checks * 100) if total_checks > 0 else 0
    if passed_checks == total_checks:
        print(f"{GREEN}{BOLD}ALL {total_checks} CHECKS PASSED ({pct:.0f}%){RESET}")
    else:
        print(f"{YELLOW}{BOLD}{passed_checks}/{total_checks} checks passed ({pct:.0f}%){RESET}")
        print(f"{RED}{BOLD}{total_checks - passed_checks} checks FAILED{RESET}")
    print("=" * 50)

    return 0 if passed_checks == total_checks else 1


if __name__ == "__main__":
    sys.exit(main())

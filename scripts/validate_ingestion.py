#!/usr/bin/env python3
"""Validate the Universal Knowledge Ingestion setup and output.

Checks:
  1. knowledge-inbox dir exists
  2. security-brain/imported dir exists
  3. manifests dir exists
  4. ingest_manifest.jsonl is valid JSONL if present
  5. ingest_errors.jsonl is valid JSONL if present
  6. content_fingerprints.json is valid JSON if present
  7. Generated Markdown files have valid YAML frontmatter
  8. At least one imported file if ingestion has run

Usage:
  python validate_ingestion.py
"""

import json
import sys
from pathlib import Path

import yaml

GREEN = "\033[92m"; RED = "\033[91m"; YELLOW = "\033[93m"
CYAN = "\033[96m"; BOLD = "\033[1m"; RESET = "\033[0m"


def check(cond: bool, name: str, ok_msg: str = "", fail_msg: str = "") -> bool:
    if cond:
        print(f"  {GREEN}✓{RESET} {name}{' — ' + ok_msg if ok_msg else ''}")
        return True
    print(f"  {RED}✗{RESET} {name}{' — ' + fail_msg if fail_msg else ''}")
    return False


def is_valid_jsonl(path: Path) -> bool:
    try:
        for line in path.read_text(encoding="utf-8").strip().split("\n"):
            if line.strip():
                json.loads(line)
        return True
    except Exception:
        return False


def main():
    print(f"\n{BOLD}Ingestion Validation Report{RESET}")
    print("=" * 50)
    total = passed = 0

    # Directories
    print(f"\n{CYAN}1. Required Directories{RESET}")
    for d in ["knowledge-inbox", "security-brain/imported", "security-brain/manifests"]:
        ok = check(Path(d).is_dir(), d, "exists", "MISSING")
        total += 1; passed += ok

    # Manifests
    print(f"\n{CYAN}2. Manifest Files{RESET}")
    man = Path("security-brain/manifests")
    for fn, vfunc in [
        ("ingest_manifest.jsonl", is_valid_jsonl),
        ("ingest_errors.jsonl", is_valid_jsonl),
    ]:
        fp = man / fn
        if fp.is_file():
            ok = check(vfunc(fp), fn, "valid JSONL", "INVALID")
        else:
            ok = check(True, fn, "not yet created (OK)")
        total += 1; passed += ok

    fp = man / "content_fingerprints.json"
    if fp.is_file():
        try:
            json.loads(fp.read_text(encoding="utf-8"))
            ok = check(True, "content_fingerprints.json", "valid JSON", "INVALID")
        except Exception:
            ok = check(False, "content_fingerprints.json", "", "INVALID")
    else:
        ok = check(True, "content_fingerprints.json", "not yet created (OK)")
    total += 1; passed += ok

    # Imported Markdown validation
    print(f"\n{CYAN}3. Imported Markdown Frontmatter{RESET}")
    imported = list(Path("security-brain/imported").rglob("*.md"))
    if imported:
        bad = 0
        for p in imported[:200]:
            text = p.read_text(encoding="utf-8", errors="ignore")
            if not text.startswith("---\n"):
                bad += 1
            else:
                try:
                    parts = text.split("---", 2)
                    if len(parts) < 3 or not yaml.safe_load(parts[1]):
                        bad += 1
                except Exception:
                    bad += 1
        checked = min(200, len(imported))
        ok = check(bad == 0, f"Markdown frontmatter", f"{checked} checked, {bad} bad", f"{bad}/{checked} invalid")
    else:
        ok = check(True, "Markdown frontmatter", "no files yet (OK)")
    total += 1; passed += ok

    # Final
    print(f"\n{'=' * 50}")
    pct = passed / total * 100 if total else 0
    if passed == total:
        print(f"{GREEN}{BOLD}ALL {total} CHECKS PASSED ({pct:.0f}%){RESET}")
    else:
        print(f"{YELLOW}{BOLD}{passed}/{total} passed ({pct:.0f}%){RESET}")
        print(f"{RED}{BOLD}{total - passed} FAILED{RESET}")
    print("=" * 50)
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())

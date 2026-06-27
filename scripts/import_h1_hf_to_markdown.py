#!/usr/bin/env python3
"""
Import HackerOne disclosed reports from Hugging Face datasets,
normalize into Markdown with YAML frontmatter, and save to a structured directory.

Datasets:
  - elamaran619/hackerone_disclosed_reports
  - Hacker0x01/hackerone_disclosed_reports

Usage:
  python import_h1_hf_to_markdown.py
  python import_h1_hf_to_markdown.py --limit 100
  python import_h1_hf_to_markdown.py --dataset elamaran619/hackerone_disclosed_reports
  python import_h1_hf_to_markdown.py --organize-by-weakness --overwrite
"""

import argparse
import hashlib
import json
import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml
from slugify import slugify
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("h1-importer")

# The Hugging Face datasets we support
DEFAULT_DATASETS = [
    "elamaran619/hackerone_disclosed_reports",
    "Hacker0x01/hackerone_disclosed_reports",
]

# Fields preserved in YAML frontmatter from each report
FRONTMATTER_FIELDS = [
    "source",
    "dataset",
    "h1_id",
    "row_id",
    "original_report_id",
    "title",
    "weakness",
    "team_handle",
    "team_name",
    "created_at",
    "disclosed_at",
    "has_bounty",
    "visibility",
    "substate",
    "vote_count",
    "asset_identifier",
    "asset_type",
    "max_severity",
]

# Fields that may provide the vulnerability text body
VULN_FIELDS = [
    "vulnerability_information",
    "vulnerability",
    "description",
    "details",
    "report",
    "summary",
]

# Fields that may provide the report title
TITLE_FIELDS = ["title", "subject", "name", "report_title"]


def safe_str(val, default: str = "") -> str:
    """Safely extract a string from a value that may be dict, None, or other types."""
    if val is None:
        return default
    if isinstance(val, dict):
        # Try common text-containing keys
        for key in ("name", "value", "text", "label", "title", "handle"):
            if key in val and isinstance(val[key], (str, int, float)):
                return str(val[key])
        # Try stringifying the most useful single value
        if len(val) == 1:
            return str(list(val.values())[0])
        return default
    if isinstance(val, (int, float, bool)):
        return str(val)
    return str(val)


def slugify_filename(text: str, maxlen: int = 120) -> str:
    """Create a safe, short filename from text."""
    s = slugify(text, lowercase=True, max_length=maxlen, word_boundary=True)
    if not s:
        s = hashlib.md5(text.encode()).hexdigest()[:12]
    return s


def extract_id(report: dict) -> str | None:
    """Extract the best available stable ID from a report."""
    for key in ("original_report_id", "id", "_id", "report_id", "h1_id"):
        val = report.get(key)
        if val is not None:
            return str(val)
    # Fallback: hash title + vulnerability_information
    title = report.get("title", "") or ""
    vuln = report.get("vulnerability_information", "") or ""
    if title or vuln:
        return hashlib.sha256(f"{title}:{vuln}".encode()).hexdigest()[:16]
    return None


def extract_vulnerability_text(report: dict) -> str:
    """Extract vulnerability body text from a report."""
    for field in VULN_FIELDS:
        val = report.get(field)
        if val and isinstance(val, str) and len(val.strip()) > 10:
            return val.strip()
    return ""


def make_tags(report: dict) -> list[str]:
    """Generate tags from report metadata."""
    tags = ["hackerone"]
    weakness = safe_str(report.get("weakness") or report.get("bug_type") or "")
    if weakness:
        tag = slugify(weakness, lowercase=True)
        if tag:
            tags.append(tag)
    severity = safe_str(report.get("max_severity") or report.get("severity") or "")
    if severity and severity.lower() not in ("none", "", "info"):
        tags.append(f"severity-{slugify(severity, lowercase=True)}")
    asset_type = safe_str(report.get("asset_type") or "")
    if asset_type:
        tags.append(f"asset-{slugify(asset_type, lowercase=True)}")
    return tags


def normalize_report(report: dict, dataset_name: str) -> dict | None:
    """Normalize a single report dict into our standard format."""
    title = None
    for field in TITLE_FIELDS:
        val = report.get(field)
        if val and isinstance(val, str) and len(val.strip()) > 3:
            title = val.strip()
            break
    if not title:
        # Use a placeholder based on ID
        rid = extract_id(report) or "unknown"
        title = f"HackerOne Report {rid}"

    vuln_text = extract_vulnerability_text(report)
    report_id = extract_id(report) or "unknown"

    weakness = safe_str(report.get("weakness") or report.get("bug_type") or "")
    team = report.get("team") or {}
    team_handle = safe_str(report.get("team_handle")) or safe_str(team.get("handle"))
    team_name = safe_str(report.get("team_name")) or safe_str(team.get("name"))
    created_at = safe_str(report.get("created_at") or report.get("created") or "")
    disclosed_at = safe_str(report.get("disclosed_at") or report.get("disclosed") or "")

    has_bounty = report.get("has_bounty", False) or report.get("has_bounty?", False)
    if isinstance(has_bounty, str):
        has_bounty = has_bounty.lower() in ("true", "yes", "1")
    visibility = safe_str(report.get("visibility") or report.get("state") or "")
    substate = safe_str(report.get("substate") or report.get("status") or "")
    vote_count = report.get("vote_count", 0)
    if isinstance(vote_count, str):
        try:
            vote_count = int(vote_count)
        except (ValueError, TypeError):
            vote_count = 0

    # structured_scope contains asset_identifier, asset_type, max_severity
    structured_scope = report.get("structured_scope") or {}
    if isinstance(structured_scope, dict):
        asset_identifier = safe_str(report.get("asset_identifier")) or safe_str(structured_scope.get("asset_identifier"))
        asset_type = safe_str(report.get("asset_type")) or safe_str(structured_scope.get("asset_type"))
        max_severity = safe_str(report.get("max_severity")) or safe_str(structured_scope.get("max_severity"))
    else:
        asset_identifier = safe_str(report.get("asset_identifier") or "")
        asset_type = safe_str(report.get("asset_type") or "")
        max_severity = safe_str(report.get("max_severity") or report.get("severity") or "")

    row_id = str(report.get("__index_level_0__", "")) or ""

    # Build a clean dict
    normalized = {
        "source": "hackerone",
        "dataset": dataset_name,
        "h1_id": report_id,
        "row_id": row_id,
        "original_report_id": report_id,
        "title": title,
        "weakness": weakness,
        "team_handle": team_handle,
        "team_name": team_name,
        "created_at": str(created_at),
        "disclosed_at": str(disclosed_at),
        "has_bounty": has_bounty,
        "visibility": str(visibility),
        "substate": str(substate),
        "vote_count": vote_count,
        "asset_identifier": str(asset_identifier),
        "asset_type": str(asset_type),
        "max_severity": str(max_severity),
        "tags": make_tags(report),
        "_vulnerability_text": vuln_text,
    }
    return normalized


def report_to_markdown(normalized: dict) -> str:
    """Convert a normalized report dict to YAML frontmatter + Markdown body."""
    frontmatter = {}
    for field in FRONTMATTER_FIELDS:
        val = normalized.get(field)
        if val is not None and val != "":
            if isinstance(val, list):
                frontmatter[field] = val
            else:
                frontmatter[field] = val
    frontmatter["tags"] = normalized.get("tags", ["hackerone"])

    title = normalized.get("title", "Untitled Report")
    vuln_text = normalized.get("_vulnerability_text", "")
    source = f"HackerOne Report ID: {normalized.get('h1_id', 'unknown')}"
    weakness = normalized.get("weakness", "N/A")
    program = normalized.get("team_name") or normalized.get("team_handle") or "N/A"
    disclosed = normalized.get("disclosed_at", "N/A")
    bounty = "Yes" if normalized.get("has_bounty") else "No"
    vis = normalized.get("visibility", "N/A")
    state = normalized.get("substate", "N/A")

    yaml_str = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)

    md = f"""---
{yaml_str}---

# {title}

## Metadata

- {source}
- Weakness: {weakness}
- Program: {program}
- Disclosed At: {disclosed}
- Has Bounty: {bounty}
- Visibility: {vis}
- Substate: {state}

## Original Report

{vuln_text}

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
"""
    return md


def safe_filename(report_id: str, title: str, weakness: str = "") -> str:
    """Generate a safe, unique filename."""
    title_slug = slugify_filename(title)
    wid = ""
    if weakness:
        w = slugify_filename(weakness)
        if w:
            wid = f"_{w}"
    rid = slugify_filename(report_id, maxlen=16)
    return f"h1_{rid}{wid}_{title_slug}.md"


def process_dataset(
    dataset_name: str,
    output_dir: Path,
    seen_ids: set,
    limit: int | None = None,
    organize_by_weakness: bool = False,
    overwrite: bool = False,
) -> dict:
    """Load a Hugging Face dataset and write reports as Markdown files."""
    from datasets import load_dataset

    stats = {
        "dataset": dataset_name,
        "loaded": False,
        "splits": [],
        "rows_seen": 0,
        "rows_written": 0,
        "duplicates_skipped": 0,
        "errors": 0,
        "error_details": [],
    }

    try:
        log.info(f"Loading dataset: {dataset_name}")
        dataset = load_dataset(dataset_name, trust_remote_code=True)
        stats["loaded"] = True
    except Exception as e:
        log.error(f"Failed to load dataset {dataset_name}: {e}")
        stats["errors"] = 1
        stats["error_details"].append(str(e))
        return stats

    for split_name in list(dataset.keys()):
        log.info(f"Processing split: {split_name}")
        split = dataset[split_name]
        stats["splits"].append(split_name)
        total = limit if limit else len(split)
        stats["rows_seen"] += total

        for i in tqdm(range(min(total, len(split))), desc=f"  [{split_name}]", unit="reports"):
            try:
                raw = split[i]
                normalized = normalize_report(raw, dataset_name)
                if not normalized:
                    continue

                report_id = normalized["h1_id"]
                title = normalized["title"]

                # Deduplicate
                dedup_key = report_id
                if dedup_key in seen_ids:
                    stats["duplicates_skipped"] += 1
                    continue
                seen_ids.add(dedup_key)

                # Determine output subdirectory
                if organize_by_weakness and normalized.get("weakness"):
                    weakness_slug = slugify_filename(normalized["weakness"])
                    report_dir = output_dir / weakness_slug
                else:
                    report_dir = output_dir

                report_dir.mkdir(parents=True, exist_ok=True)

                filename = safe_filename(report_id, title, normalized.get("weakness", ""))
                filepath = report_dir / filename

                if filepath.exists() and not overwrite:
                    stats["duplicates_skipped"] += 1
                    continue

                md_content = report_to_markdown(normalized)
                filepath.write_text(md_content, encoding="utf-8")
                stats["rows_written"] += 1

            except Exception as e:
                log.warning(f"  Error processing row {i}: {e}")
                stats["errors"] += 1
                stats["error_details"].append(f"Row {i}: {e}")
                continue

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Import HackerOne disclosed reports from Hugging Face datasets to Markdown."
    )
    parser.add_argument(
        "--output-dir",
        default="security-brain/hackerone/reports",
        help="Output directory for Markdown files (default: security-brain/hackerone/reports)",
    )
    parser.add_argument(
        "--dataset",
        action="append",
        dest="datasets",
        help="Hugging Face dataset to load (can be specified multiple times)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit rows per dataset split (default: no limit)",
    )
    parser.add_argument(
        "--no-limit",
        action="store_true",
        help="Explicitly disable row limit (overrides --limit)",
    )
    parser.add_argument(
        "--organize-by-weakness",
        action="store_true",
        help="Organize reports into subdirectories by weakness category",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing Markdown files",
    )
    args = parser.parse_args()

    # Determine output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Determine datasets
    datasets_to_process = args.datasets if args.datasets else DEFAULT_DATASETS

    # Determine limit
    limit = None
    if args.no_limit:
        limit = None
    elif args.limit is not None:
        limit = args.limit
    # Default: no limit

    log.info("=" * 60)
    log.info("HackerOne → Markdown Importer")
    log.info("=" * 60)
    log.info(f"Output directory: {output_dir.resolve()}")
    log.info(f"Datasets: {datasets_to_process}")
    log.info(f"Limit per split: {'unlimited' if limit is None else limit}")
    log.info(f"Organize by weakness: {args.organize_by_weakness}")
    log.info(f"Overwrite existing: {args.overwrite}")
    log.info("")

    # Track unique report IDs across all datasets
    seen_ids: set = set()
    all_stats = []

    for ds_name in datasets_to_process:
        log.info(f"\n{'─' * 40}")
        log.info(f"Processing: {ds_name}")
        log.info(f"{'─' * 40}")
        stats = process_dataset(
            dataset_name=ds_name,
            output_dir=output_dir,
            seen_ids=seen_ids,
            limit=limit,
            organize_by_weakness=args.organize_by_weakness,
            overwrite=args.overwrite,
        )
        all_stats.append(stats)

    # Build summary
    total_seen = sum(s["rows_seen"] for s in all_stats)
    total_written = sum(s["rows_written"] for s in all_stats)
    total_dupes = sum(s["duplicates_skipped"] for s in all_stats)
    total_errors = sum(s["errors"] for s in all_stats)
    datasets_loaded = [s["dataset"] for s in all_stats if s["loaded"]]
    datasets_failed = [s["dataset"] for s in all_stats if not s["loaded"]]

    summary = {
        "datasets_attempted": datasets_to_process,
        "datasets_loaded": datasets_loaded,
        "datasets_failed": datasets_failed,
        "splits_processed": list(set(s for st in all_stats for s in st["splits"])),
        "total_rows_seen": total_seen,
        "total_unique_written": total_written,
        "duplicates_skipped": total_dupes,
        "total_errors": total_errors,
        "output_directory": str(output_dir.resolve()),
        "timestamp": datetime.utcnow().isoformat(),
    }

    # Write summary
    summary_path = output_dir.parent / "import_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    # Print final report
    log.info("\n" + "=" * 60)
    log.info("IMPORT SUMMARY")
    log.info("=" * 60)
    log.info(f"  Datasets attempted:  {len(datasets_to_process)}")
    log.info(f"  Datasets loaded:     {len(datasets_loaded)}")
    if datasets_failed:
        log.warning(f"  Datasets failed:     {len(datasets_failed)} → {datasets_failed}")
    log.info(f"  Rows seen:           {total_seen}")
    log.info(f"  Unique reports:      {total_written}")
    log.info(f"  Duplicates skipped:  {total_dupes}")
    log.info(f"  Errors:              {total_errors}")
    log.info(f"  Output:              {output_dir.resolve()}")
    log.info(f"  Summary:             {summary_path.resolve()}")
    log.info("=" * 60)

    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

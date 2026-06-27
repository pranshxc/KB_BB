#!/usr/bin/env python3
"""URL ingestion for the Security Brain.

Read URLs from a file, fetch each page, extract title and readable
text, and convert to Markdown documents.

Usage:
  python ingest_urls.py --input knowledge-inbox/urls.txt --output security-brain/imported/blogs
"""

import argparse
import hashlib
import json
import logging
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import yaml

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("ingest-urls")

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False

DEFAULT_TIMEOUT = 15
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (compatible; SecurityBrain/1.0; +https://github.com/pranshxc/KB_BB)"
)
DEFAULT_MANIFEST_DIR = "security-brain/manifests"


def fetch_page(url: str, timeout: int = DEFAULT_TIMEOUT) -> tuple:
    if not HAS_REQUESTS:
        return None, "requests library not installed. Run: pip install requests"
    try:
        resp = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": DEFAULT_USER_AGENT},
            allow_redirects=True,
        )
        resp.raise_for_status()
        if len(resp.content) > 10 * 1024 * 1024:
            return None, "Response too large (>10MB)"
        return resp, None
    except Exception as e:
        return None, str(e)


def extract_content(html: str) -> tuple:
    if not HAS_BS4:
        title = "No title"
        m = re.search(r"<title[^>]*>([^<]+)</title>", html, re.IGNORECASE)
        if m:
            title = m.group(1).strip()
        stripped = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
        stripped = re.sub(r"<style[^>]*>.*?</style>", "", stripped, flags=re.DOTALL | re.IGNORECASE)
        stripped = re.sub(r"<[^>]+>", " ", stripped)
        stripped = re.sub(r"&[a-z]+;", " ", stripped)
        stripped = re.sub(r"\s+", " ", stripped).strip()
        return title, stripped

    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title else "No title"
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return title, text


def safe_filename(title: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    slug = re.sub(r"[-\s]+", "-", slug)[:100]
    return slug or "page"


def ingest_urls(input_path: str, output_dir: str, manifest_dir: str) -> dict:
    in_file = Path(input_path)
    out_dir = Path(output_dir)
    man_dir = Path(manifest_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    man_dir.mkdir(parents=True, exist_ok=True)

    if not in_file.is_file():
        log.error(f"Input file not found: {in_file}")
        sys.exit(1)

    urls = [
        line.strip()
        for line in in_file.read_text(encoding="utf-8", errors="replace").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    log.info(f"Found {len(urls)} URLs to process")

    stats = {"total": len(urls), "ingested": 0, "errors": 0, "skipped": 0}

    for i, url in enumerate(urls, 1):
        log.info(f"[{i}/{len(urls)}] {url[:80]}...")
        resp, err = fetch_page(url)
        if err:
            log.warning(f"  Error: {err}")
            stats["errors"] += 1
            _append_error(man_dir, url, err)
            continue

        title, text = extract_content(resp.text)
        if not text or len(text) < 50:
            log.warning("  Not enough content extracted")
            stats["skipped"] += 1
            _append_error(man_dir, url, "Insufficient content")
            continue

        raw_hash = hashlib.sha256(resp.content).hexdigest()
        text_hash = hashlib.sha256(text.encode("utf-8", errors="replace") or b"").hexdigest()

        parsed = urlparse(url)
        domain = parsed.netloc.replace(".", "_")

        fm = {
            "source": "url",
            "source_type": "url",
            "source_url": url,
            "domain": parsed.netloc,
            "title": title,
            "category": "blogs",
            "tags": ["imported", "url", "blogs"],
            "raw_sha256": raw_hash,
            "text_sha256": text_hash,
            "ingested_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "sensitivity": "public",
            "redactions_applied": False,
        }
        fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)

        md = f"""---
{fm_yaml}---

# {title}

## Source Information

- URL: {url}
- Domain: {parsed.netloc}
- Ingested At: {fm["ingested_at"]}

## Content

{text}
"""
        fname = f"{domain}_{safe_filename(title)}_{raw_hash[:8]}.md"
        filepath = out_dir / fname
        filepath.write_text(md, encoding="utf-8")
        log.info(f"  -> {filepath.name}")
        stats["ingested"] += 1

        time.sleep(0.5)

    return stats


def _append_error(man_dir: Path, url: str, error: str) -> None:
    with open(man_dir / "ingest_errors.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"source": url, "error": str(error), "timestamp": datetime.now(timezone.utc).isoformat()}) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Ingest URLs into the Security Brain")
    parser.add_argument("--input", default="knowledge-inbox/urls.txt", help="URL list file")
    parser.add_argument("--output", default="security-brain/imported/blogs", help="Output directory")
    parser.add_argument("--manifest-dir", default=DEFAULT_MANIFEST_DIR, help="Manifest directory")
    args = parser.parse_args()

    print()
    print("=" * 50)
    print("  URL Ingestion")
    print("=" * 50)

    if not HAS_REQUESTS:
        print("ERROR: requests library not installed.")
        print("  pip install requests beautifulsoup4")
        sys.exit(1)

    stats = ingest_urls(args.input, args.output, args.manifest_dir)

    print()
    print("-" * 40)
    print(f"  URLs total:    {stats['total']}")
    print(f"  Ingested:      {stats['ingested']}")
    print(f"  Skipped:       {stats['skipped']}")
    print(f"  Errors:        {stats['errors']}")
    print("-" * 40)
    print(f"\nOutput: {args.output}")


if __name__ == "__main__":
    main()

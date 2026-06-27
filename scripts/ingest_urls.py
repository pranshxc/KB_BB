#!/usr/bin/env python3
"""URL ingestion for the Security Brain.

Read URLs from a file, fetch each page, extract title and readable
text, and convert to Markdown documents. Uses the same deduplication,
topic detection, and secret redaction as ingest_anything.py.

Usage:
  python ingest_urls.py --input knowledge-inbox/urls.txt --output security-brain/imported/blogs
"""

import argparse
import hashlib
import json
import logging
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
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


# ── Copy topic detection from ingest_anything ───────────────────────
def load_taxonomy() -> Dict[str, List[str]]:
    p = Path("configs/content_taxonomy.yaml")
    if not p.is_file():
        p = Path(__file__).resolve().parent.parent / "configs/content_taxonomy.yaml"
    if not p.is_file():
        return {}
    try:
        data = yaml.safe_load(p.read_text()) or {}
        raw = data.get("topics", {})
        if not isinstance(raw, dict):
            return {}
        out: Dict[str, List[str]] = {}
        for topic_name, topic_data in raw.items():
            if isinstance(topic_data, dict) and "keywords" in topic_data:
                out[topic_name] = [str(k).lower() for k in topic_data["keywords"]]
        return out
    except Exception:
        return {}


TOPICS_CACHE: Optional[Dict[str, List[str]]] = None


def detect_topics(text: str) -> List[str]:
    global TOPICS_CACHE
    if TOPICS_CACHE is None:
        TOPICS_CACHE = load_taxonomy()
    if not text or len(text) < 20 or not TOPICS_CACHE:
        return []
    text_lower = text.lower()
    matches = []
    for topic, keywords in TOPICS_CACHE.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score >= 1:
            matches.append((topic, score))
    matches.sort(key=lambda x: -x[1])
    return [m[0] for m in matches[:6]]


# ── Copy secret redaction from ingest_anything ──────────────────────
SECRET_PATTERNS: List[Tuple[str, str]] = [
    (r'(?i)(api[_-]?key|apikey|api[_-]?secret|secret[_-]?key)\s*[:=]\s*["\']?([^\s"\']{8,})["\']?', r'\1=***REDACTED***'),
    (r'(?i)(password|passwd|pwd)\s*[:=]\s*["\']?([^\s"\']+)["\']?', r'\1=***REDACTED***'),
    (r'(?i)(token|jwt|bearer)\s+["\']?([A-Za-z0-9\-_\.]{20,})["\']?', r'\1 ***REDACTED***'),
    (r'(?i)(aws[_-]?(access[_-]?key|secret)|AKIA[A-Z0-9]{16})', '***REDACTED-AWS-KEY***'),
    (r'(?i)(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{20,}', '***REDACTED-GH-TOKEN***'),
    (r'(?i)(-----BEGIN\s(?:RSA\s)?PRIVATE\sKEY-----.*?-----END\s(?:RSA\s)?PRIVATE\sKEY-----)', '***REDACTED-PRIVATE-KEY***', re.DOTALL),
    (r'(?i)(sk-[A-Za-z0-9_/]{20,})', '***REDACTED-API-KEY***'),
]


def redact_secrets(text: str) -> Tuple[str, bool]:
    changed = False
    result = text
    for item in SECRET_PATTERNS:
        pattern = item[0]
        replacement = item[1]
        flags = item[2] if len(item) > 2 else re.MULTILINE
        new_result, count = re.subn(pattern, replacement, result, flags=flags)
        if count > 0:
            changed = True
            result = new_result
    return result, changed


# ── Deduplication helpers ───────────────────────────────────────────
def load_fingerprints() -> Dict[str, str]:
    fp_file = Path(DEFAULT_MANIFEST_DIR) / "content_fingerprints.json"
    if fp_file.is_file():
        try:
            return json.loads(fp_file.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def append_manifest(entry: dict) -> None:
    man_dir = Path(DEFAULT_MANIFEST_DIR)
    man_dir.mkdir(parents=True, exist_ok=True)
    with open(man_dir / "ingest_manifest.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, default=str) + "\n")


def append_error(source: str, error: str, stage: str = "fetch") -> None:
    man_dir = Path(DEFAULT_MANIFEST_DIR)
    man_dir.mkdir(parents=True, exist_ok=True)
    with open(man_dir / "ingest_errors.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "source": source, "error": str(error), "stage": stage,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }) + "\n")


def fetch_page(url: str, timeout: int = DEFAULT_TIMEOUT) -> tuple:
    if not HAS_REQUESTS:
        return None, "requests library not installed. Run: pip install requests"
    try:
        resp = requests.get(
            url, timeout=timeout,
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


def ingest_urls(input_path: str, output_dir: str, manifest_dir: str = DEFAULT_MANIFEST_DIR) -> dict:
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

    # Load dedupe fingerprints
    fingerprints = load_fingerprints()
    fp_file = man_dir / "content_fingerprints.json"

    stats = {"total": len(urls), "ingested": 0, "errors": 0, "skipped": 0}

    for i, url in enumerate(urls, 1):
        log.info(f"[{i}/{len(urls)}] {url[:80]}...")

        # Check URL already ingested (fingerprint by URL)
        url_hash = hashlib.sha256(url.encode()).hexdigest()
        if url_hash in fingerprints:
            log.info("  Skipped (duplicate URL)")
            stats["skipped"] += 1
            continue

        resp, err = fetch_page(url)
        if err:
            log.warning(f"  Error: {err}")
            stats["errors"] += 1
            append_error(url, err, "fetch")
            continue

        title, text = extract_content(resp.text)
        if not text or len(text) < 50:
            log.warning("  Not enough content extracted")
            stats["skipped"] += 1
            append_error(url, "Insufficient content")
            continue

        # Redact secrets
        text, redacted = redact_secrets(text)

        # Hash content for dedupe
        raw_hash = hashlib.sha256(resp.content).hexdigest()
        text_hash = hashlib.sha256(text.encode("utf-8", errors="replace") or b"").hexdigest()

        if raw_hash in fingerprints or text_hash in fingerprints:
            log.info("  Skipped (duplicate content)")
            stats["skipped"] += 1
            continue

        # Detect topics
        topics = detect_topics(text)

        # Build frontmatter
        parsed = urlparse(url)
        domain = parsed.netloc.replace(".", "_")

        fm = {
            "source": "url",
            "source_type": "url",
            "source_url": url,
            "domain": parsed.netloc,
            "title": title,
            "category": "blogs",
            "detected_topics": topics,
            "tags": ["imported", "url", "blogs"] + topics[:4],
            "raw_sha256": raw_hash,
            "text_sha256": text_hash,
            "ingested_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "sensitivity": "public",
            "redactions_applied": redacted,
        }
        fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)

        md = f"""---
{fm_yaml}---

# {title}

## Source Information

- URL: {url}
- Domain: {parsed.netloc}
- Ingested At: {fm["ingested_at"]}
- Redacted: {redacted}

## Content

{text}
"""
        fname = f"{domain}_{safe_filename(title)}_{raw_hash[:8]}.md"
        filepath = out_dir / fname
        filepath.write_text(md, encoding="utf-8")
        log.info(f"  -> {filepath.name}")
        stats["ingested"] += 1

        # Update fingerprints
        fingerprints[url_hash] = url
        fingerprints[raw_hash] = url
        fingerprints[text_hash] = url
        fp_file.write_text(json.dumps(fingerprints, indent=2, sort_keys=True), encoding="utf-8")

        # Append manifest
        append_manifest({
            "source": url,
            "output": str(filepath),
            "source_type": "url",
            "category": "blogs",
            "title": title,
            "topics": topics,
            "redacted": redacted,
            "raw_size": len(resp.content),
            "raw_sha256": raw_hash,
            "text_sha256": text_hash,
            "ingested_at": datetime.now(timezone.utc).isoformat(),
        })

        time.sleep(0.5)

    return stats


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

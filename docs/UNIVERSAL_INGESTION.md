# Universal Smart Knowledge Ingestion

Drop any textual/knowledge data into `knowledge-inbox/`, then tell an AI harness to ingest everything into the Security Brain RAG knowledge base.

## Overview

The Universal Ingestion pipeline:

1. **Scans** `knowledge-inbox/` recursively
2. **Extracts** text from 15+ file formats
3. **Normalizes** everything to Markdown with YAML frontmatter
4. **Deduplicates** by SHA256 content fingerprinting
5. **Classifies** into categories (blogs, documents, notes, code, datasets)
6. **Detects** security topics using configurable taxonomy
7. **Redacts** secrets (API keys, tokens, passwords) automatically
8. **Writes** manifests tracking every ingestion

## Supported File Types

| Category | Extensions |
|----------|-----------|
| Markdown | `.md`, `.markdown` |
| Text | `.txt`, `.log` |
| HTML | `.html`, `.htm` |
| PDF | `.pdf` (requires pymupdf or pypdf) |
| DOCX | `.docx` (requires python-docx) |
| PPTX | `.pptx` (requires python-pptx) |
| Spreadsheet | `.csv`, `.tsv`, `.xlsx` |
| JSON | `.json`, `.jsonl` |
| Code | `.py`, `.js`, `.ts`, `.go`, `.rs`, `.java`, `.rb`, `.php`, `.c`, `.cpp`, `.h`, `.cs`, `.sh`, `.yaml`, `.yml`, `.toml`, `.ini` |
| Archive | `.zip`, `.tar`, `.tar.gz`, `.tgz` |

Graceful degradation: if a parser dependency is missing, the file is skipped and an error is logged — other files continue to ingest.

## How to Use

### 1. Drop files into the inbox

```bash
cp my-article.html knowledge-inbox/
cp ~/Downloads/report.pdf knowledge-inbox/
cp -r ~/notes/security/ knowledge-inbox/
```

### 2. Dry-run to preview

```bash
python scripts/ingest_anything.py --dry-run --verbose
```

### 3. Ingest

```bash
python scripts/ingest_anything.py
```

With indexing:
```bash
python scripts/ingest_anything.py --index
```

### 4. Ingest URLs

Create `knowledge-inbox/urls.txt` with one URL per line, then:
```bash
python scripts/ingest_urls.py --input knowledge-inbox/urls.txt --output security-brain/imported/blogs
```

### 5. Validate

```bash
python scripts/validate_ingestion.py
```

### 6. Generate report

```bash
python scripts/generate_ingestion_report.py
```

## How Deduplication Works

Every file is hashed twice:
- **raw SHA256** — hash of the original file bytes
- **text SHA256** — hash of the extracted text content

If either hash matches a previously ingested file, the duplicate is skipped. Fingerprints persist in `security-brain/manifests/content_fingerprints.json`.

## How Secret Redaction Works

The redaction engine scans for common patterns:
- API keys (sk-..., ghp_..., AIza...)
- AWS keys (AKIA...)
- GitHub tokens (ghp_..., gho_...)
- Private keys (PEM format)
- Passwords/secrets after key=value assignments

Redacted text is replaced with `***REDACTED-...***` markers. Set `--no-redact` to skip.

## How Topic Detection Works

The content is scanned against 28 security topics defined in `configs/content_taxonomy.yaml`. Each topic has keyword patterns. Topics are ranked by keyword match count and the top 6 are written as frontmatter.

## Optional Dependencies

```bash
pip install pyyaml rich python-slugify requests beautifulsoup4 pandas pypdf pymupdf python-docx python-pptx openpyxl
```

If a package is missing, the parser for that format is skipped with a log error — other formats continue to work.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "PDF extraction failed" | `pip install pymupdf` or `pip install pypdf` |
| "DOCX extraction failed" | `pip install python-docx` |
| "Spreadsheet extraction failed" | `pip install pandas openpyxl` |
| "HTML extraction failed" | `pip install beautifulsoup4` |
| "No files ingested" | Check `--input` directory, try `--verbose` |
| "File too large" | Adjust `--max-file-size-mb` (default 50) |

## Examples

### Ingest a single blog post
```bash
cp blog-post.html knowledge-inbox/
python scripts/ingest_anything.py --verbose
```

### Ingest a directory of Markdown notes
```bash
cp -r ~/security-notes/* knowledge-inbox/
python scripts/ingest_anything.py --dedupe --redact-secrets
```

### Ingest with reindex
```bash
python scripts/ingest_anything.py --index
```

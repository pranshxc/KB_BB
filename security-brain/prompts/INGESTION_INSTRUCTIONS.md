# Knowledge Ingestion Instructions

When the user asks to add data/documents/blogs/files to the knowledge base:

## Workflow

1. **Inspect** `knowledge-inbox/` — check what files are present.
2. **Dry-run first** if the user has not explicitly approved ingestion:
   ```
   python scripts/ingest_anything.py --input knowledge-inbox --output security-brain/imported --dry-run
   ```
3. **Ingest** everything from the inbox:
   ```
   python scripts/ingest_anything.py --input knowledge-inbox --output security-brain/imported --dedupe --redact-secrets
   ```
4. **Index** if the user requests. With `--index` flag or separately:
   ```
   python scripts/reindex_knowledge.py --path security-brain
   ```
5. **Validate** the output:
   ```
   python scripts/validate_ingestion.py
   ```
6. **Summarize** results:
   - Files scanned
   - Files ingested
   - Duplicates skipped
   - Errors
   - Output directory
   - Index status

## Rules

- Keep copyrighted content local and private.
- Redact secrets by default (enabled by default).
- Do not ingest arbitrary system directories outside the repo without explicit user permission.
- Supported formats: MD, TXT, HTML, PDF, DOCX, PPTX, XLSX, CSV, JSON, JSONL, code files, ZIP/TAR archives.
- Deduplication is on by default — identical content is skipped via SHA256 fingerprinting.

## Step-by-Step Examples

### Drop and ingest a blog post
```
cp article.html knowledge-inbox/
python scripts/ingest_anything.py
```

### Ingest a directory of security notes
```
cp -r ~/Documents/security-notes/* knowledge-inbox/
python scripts/ingest_anything.py --verbose
```

### Ingest and reindex in one step
```
python scripts/ingest_anything.py --index
```

### Ingest URLs from a list
```
python scripts/ingest_urls.py --input knowledge-inbox/urls.txt
```

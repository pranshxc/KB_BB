# Security Brain — Operations Guide

## How to Update Datasets

### Update HackerOne Reports

Re-run the importer with `--overwrite` to refresh reports:

```bash
cd /path/to/project
source knowledge-rag/.venv/bin/activate
python scripts/import_h1_hf_to_markdown.py --overwrite
```

This will:
- Re-download datasets from Hugging Face
- Re-deduplicate by report ID
- Overwrite existing Markdown files
- Update the import summary

### Add New Hugging Face Datasets

Pass additional datasets:

```bash
python scripts/import_h1_hf_to_markdown.py \
  --dataset elamaran619/hackerone_disclosed_reports \
  --dataset Hacker0x01/hackerone_disclosed_reports \
  --dataset your-org/your-dataset
```

## How to Add New Documents

### Manual File Addition

1. Create a Markdown file with YAML frontmatter
2. Place it in the appropriate `security-brain/` subdirectory
3. Reindex the knowledge base

### Adding Multiple Files

```bash
# Add all .md files from a directory
cp -r my-notes/*.md security-brain/internal/secure-code-review/

# Reindex
# Restart knowledge-rag server, or call reindex_documents()
```

### Supported File Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| Markdown | .md | Section-aware chunking (best results) |
| Plain text | .txt | Fixed-size chunking |
| PDF | .pdf | Text-based PDFs only |
| Word | .docx | Headings preserved |
| Excel | .xlsx | Sheet-by-sheet |
| PowerPoint | .pptx | Slide-by-slide |
| JSON | .json | Structure-aware |
| CSV | .csv | Row-based |
| Jupyter | .ipynb | Markdown + code cells |
| Source code | .py, .js, .ts, .c, .cpp | Function/class-aware |

## How to Rebuild Index

### Smart Reindex (Changes Only)

```
reindex_documents(force=True)
```

### Nuclear Rebuild (Full Re-embedding)

Use when changing embedding models or after index corruption:

```
reindex_documents(full_rebuild=True)
```

### Via CLI

Restart the knowledge-rag server — it auto-indexes on startup.

### Check Reindex Status

```
get_reindex_status()
```

## How to Backup the Knowledge Base

### Documents Backup

```bash
# Backup the Markdown documents
tar -czf security-brain-backup-$(date +%Y%m%d).tar.gz security-brain/
```

### Index Backup

The index is stored in `knowledge-rag/data/`. Backup with the server stopped:

```bash
tar -czf kr-index-backup-$(date +%Y%m%d).tar.gz knowledge-rag/data/
```

### Full State Backup

```bash
tar -czf full-security-brain-$(date +%Y%m%d).tar.gz \
  security-brain/ \
  knowledge-rag/data/ \
  knowledge-rag/config.yaml
```

## How to Troubleshoot Failed Ingestion

### Hugging Face Dataset Fails

```bash
# Check network connectivity
python -c "from datasets import load_dataset; ds = load_dataset('elamaran619/hackerone_disclosed_reports', trust_remote_code=True); print('OK')"

# Try with a small limit first
python scripts/import_h1_hf_to_markdown.py --limit 10
```

### Markdown Files Not Indexing

Check:
1. Files are in the correct directory
2. knowledge-rag `config.yaml` includes the correct `documents_dir`
3. File format is in `supported_formats`
4. File is not in an `exclude_patterns` path

### Index Shows Zero Documents

```bash
# Restart the server and watch for indexing log:
knowledge-rag
# Look for: "Indexed X documents with Y chunks"
```

### Memory Issues

For large knowledge bases:
- Reduce `chunk_size` in config.yaml
- Use `exclude_patterns` to skip unnecessary files
- Consider enabling GPU acceleration

## How to Tune Retrieval Quality

### Adjust hybrid_alpha

- `hybrid_alpha=0.0`: Pure BM25 (exact term matching)
- `hybrid_alpha=0.3`: Keyword-heavy (default, good for technical terms)
- `hybrid_alpha=0.5`: Balanced
- `hybrid_alpha=0.7`: Semantic-heavy (conceptual queries)
- `hybrid_alpha=1.0`: Pure semantic

### Set min_score

```python
search_knowledge("query", min_score=0.2)  # Filter low-quality results
```

### Enable/Disable Reranker

In `config.yaml`:
```yaml
models:
  reranker:
    enabled: true  # Better ranking, slight latency
```

### Query Expansion

Add synonyms in `config.yaml`:
```yaml
query_expansions:
  idor:
    - insecure direct object reference
    - idor
    - bola
    - broken object level authorization
```

## How to Create Curated Summaries

1. Review related HackerOne reports for a vulnerability class
2. Identify common patterns (root cause, impact, fix)
3. Create a Markdown file with YAML frontmatter and structured sections
4. Place in `security-brain/hackerone/summaries/`
5. Add cross-references to specific reports
6. Reindex to make it searchable

Example format:

```yaml
---
title: "Password Reset Bug Patterns"
category: "summary"
tags:
  - password-reset
  - authentication
  - curated
---
```

## How to Run Evaluations

### Evaluate Retrieval Quality

```python
evaluate_retrieval(test_cases='[
    {"query": "password reset token not expiring", "expected_filepath": "security-brain/hackerone/reports/h1_..._password-reset.md"},
    {"query": "IDOR organization membership", "expected_filepath": "security-brain/hackerone/reports/h1_..._idor.md"}
]')
```

Returns MRR@5 and Recall@5 metrics.

### Sample Evaluation Queries

Use `security-brain/evals/sample_queries.jsonl`:

```bash
python -c "
import json
with open('security-brain/evals/sample_queries.jsonl') as f:
    for line in f:
        q = json.loads(line)
        print(q['query'])
"
```

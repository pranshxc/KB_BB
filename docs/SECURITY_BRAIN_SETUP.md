# Security Brain Setup Guide

## Overview

The Security Brain is a local RAG (Retrieval-Augmented Generation) knowledge base for LLM harnesses. It uses `knowledge-rag` as the MCP/RAG engine, ingesting HackerOne disclosed reports, security taxonomies, and curated summaries into a Markdown-based knowledge base that can be queried via any MCP client (Claude Code, opencode, Cursor, etc.).

**Key capabilities:**
- Ingest HackerOne disclosed reports from Hugging Face datasets
- Convert reports to clean Markdown with YAML frontmatter
- Index and search via hybrid search (BM25 + semantic vectors + cross-encoder reranking)
- 100% local — no API keys, no data leaves your machine
- 20 supported file formats (MD, PDF, DOCX, JSON, CSV, and more)

## Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                      MCP Client                                │
│        (Claude Code / opencode / Cursor / etc.)                │
└──────────────────────────┬─────────────────────────────────────┘
                           │ MCP stdio protocol
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                  knowledge-rag MCP Server                      │
│  ┌──────────┐  ┌──────────┐  ┌─────────────────────────────┐  │
│  │ Chunking │  │Parsing   │  │  Hybrid Search              │  │
│  │ (20 fmt) │  │Metadata  │  │  BM25 + Semantic + Reranker │  │
│  └────┬─────┘  └────┬─────┘  └──────────────┬──────────────┘  │
│       └──────────────┴──────────────────────┘                   │
└──────────────────────────┬─────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                    Security Brain (Documents)                   │
│  ┌──────────┐  ┌──────────┐  ┌─────────────────────────────┐  │
│  │HackerOne │  │Blogs/    │  │  Internal / Taxonomy / Docs │  │
│  │ Reports  │  │Articles  │  │                             │  │
│  └──────────┘  └──────────┘  └─────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

## Folder Structure

```
security-brain/
├── hackerone/
│   ├── reports/            # HackerOne disclosed reports (Markdown)
│   ├── summaries/          # Curated vulnerability summaries
│   └── taxonomies/         # Bug classes, root causes, testing methodology
├── blogs/                  # Blog/article summaries (medium, portswigger, etc.)
├── docs/                   # Reference docs (owasp, cwe, cheatsheets)
├── internal/               # Internal security docs (code review, pentests)
├── prompts/                # LLM harness instructions
└── evals/                  # Sample evaluation queries
configs/                    # MCP configuration examples
scripts/                    # Utility scripts
docs/                       # Documentation
```

## Ingestion Process

### HackerOne Reports

1. **Data source**: Hugging Face datasets (`elamaran619/hackerone_disclosed_reports`, `Hacker0x01/hackerone_disclosed_reports`)
2. **Processing**: Normalize fields, deduplicate by report ID, extract vulnerability text
3. **Conversion**: Convert to Markdown with YAML frontmatter preserving metadata (title, weakness, program, severity, bounty, visibility)
4. **Output**: Organized in `security-brain/hackerone/reports/` optionally organized by weakness category

### Taxonomy & Summary Files

Generated manually via `scripts/generate_security_taxonomies.py`. These provide high-quality AppSec knowledge covering bug classes, root causes, testing methodology, remediation patterns, and curated vulnerability summaries.

## Indexing Process

Knowledge-rag indexes documents from the `security-brain/` directory. It:

1. **Parses** files based on format (Markdown section-aware, PDF, text, etc.)
2. **Chunks** content (section-aware for .md, fixed-size for others)
3. **Embeds** chunks using FastEmbed ONNX (BAAI/bge-small-en-v1.5, 384D)
4. **Stores** in ChromaDB vector database + BM25 inverted index
5. **Searches** via hybrid search with cross-encoder reranking

### Indexing Command

The MCP server auto-indexes on startup:

```bash
cd knowledge-rag
source .venv/bin/activate
knowledge-rag     # Starts server + indexes documents/
```

Or trigger reindexing via MCP tools:
```
reindex_documents(force=True)         # Smart reindex (changes only)
reindex_documents(full_rebuild=True)   # Nuclear rebuild
```

## HackerOne Report Normalization

Each report is processed into this format:

```yaml
---
source: hackerone
dataset: "elamaran619/hackerone_disclosed_reports"
h1_id: 411337
title: "Forget password link not expiring after email change"
weakness: "Authentication Bypass"
team_handle: "example"
team_name: "Example"
created_at: "2018-09-19T05:13:33.396Z"
disclosed_at: "2018-09-20T06:42:43.088Z"
has_bounty: true
visibility: "full"
substate: "resolved"
vote_count: 10
max_severity: "medium"
tags:
  - hackerone
  - authentication-bypass
---
```

Each report includes enrichment sections:
- **Likely Vulnerability Class** (to be filled by analysis)
- **Likely Root Cause** (to be filled by analysis)
- **Potential Impact** (to be filled by analysis)
- **Defensive Test Cases** (to be filled by analysis)
- **Remediation Ideas** (to be filled by analysis)

## Adding New Documents

### Markdown Files

Place files directly in the appropriate `security-brain/` subdirectory:

```bash
cp my-notes.md security-brain/internal/secure-code-review/
```

Any .md, .txt, .pdf, .docx, .json, .csv, .ipynb file is supported.

### Via MCP Tools

```python
# Add from content
add_document(content="# Title\n\nBody...", filepath="blogs/medium/my-article.md", category="blogs")

# Add from URL
add_from_url(url="https://example.com/article", category="blogs", title="Custom Title")
```

### Reindexing

After adding files, restart the MCP server or call:

```
reindex_documents()
```

For full rebuild:

```
reindex_documents(full_rebuild=True)
```

## Known Limitations

- Python 3.11+ required (tested with 3.12 on macOS)
- On macOS with Homebrew Python, DYLD_LIBRARY_PATH must be set for expat library compatibility
- FastEmbed models download on first run (~50MB embedding, ~25MB reranker)
- Full HackerOne dataset may be ~40K+ reports — indexing time scales with count
- Markdown files with section headers produce better chunking than plain text
- PDF parsing supports text-based PDFs only (no OCR)

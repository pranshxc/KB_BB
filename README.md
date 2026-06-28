# Security Brain

A local RAG knowledge base for LLM harnesses, built on `knowledge-rag`. Ingests HackerOne disclosed reports, security taxonomies, blog writeups, and curated vulnerability summaries — searchable via any MCP client (Claude Code, opencode, Cursor, etc.).

`knowledge-rag` is included as a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

## One-Click Install

**Claude Code:**
```bash
bash <(curl -fsSL https://raw.githubusercontent.com/pranshxc/KB_BB/main/scripts/install.sh) claude
```

**opencode:**
```bash
bash <(curl -fsSL https://raw.githubusercontent.com/pranshxc/KB_BB/main/scripts/install.sh) opencode
```

Or clone and run manually:
```bash
git clone --recurse-submodules https://github.com/pranshxc/KB_BB.git ~/KB_BB
cd ~/KB_BB
bash scripts/install.sh claude   # or: opencode, generic
```

**What it does automatically:**
1. Clones the repo + knowledge-rag submodule
2. Sets up Python 3.11+ venv and installs dependencies
3. Generates security taxonomies
4. Downloads 12,492 HackerOne reports
5. Downloads pre-built ChromaDB index (108,561 chunks, ~390MB compressed)
6. Registers the MCP server with your client
7. Ready to query immediately — no 30-minute wait

## What's Inside

| Data | Count | Source |
|------|-------|--------|
| HackerOne reports | 12,492 | Hugging Face datasets |
| Security blog writeups | 5,253 | Medium, Portswigger, etc. |
| Security taxonomies | 12 | Bug classes, root causes, remediation |
| Curated summaries | 8 | Password reset, IDOR, OAuth, SSRF, GraphQL |
| Total indexed chunks | 157,321 | ChromaDB vector index |

## Project Structure

```
├── security-brain/              # Knowledge base content
│   ├── hackerone/
│   │   ├── reports/             # 12,492 HackerOne reports (Markdown + YAML)
│   │   ├── summaries/           # Curated vulnerability summaries
│   │   └── taxonomies/          # Bug classes, root causes, testing methodology
│   ├── imported/
│   │   └── blogs/               # 5,253 ingested security blog posts
│   ├── blogs/                   # Blog/article placeholders
│   ├── docs/                    # Reference docs (OWASP, CWE)
│   ├── internal/                # Internal security docs
│   ├── prompts/                 # Harness instructions
│   ├── evals/                   # Sample evaluation queries
│   └── manifests/               # Ingestion manifests and fingerprints
├── knowledge-rag/               # MCP RAG engine (git submodule)
├── knowledge-inbox/             # Drop files here for ingestion
├── scripts/                     # Utility scripts
├── configs/                     # MCP and ingestion configs
└── docs/                        # Full documentation
```

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/install.sh` | One-click install (clone, setup, download index, register MCP) |
| `scripts/import_h1_hf_to_markdown.py` | Import HackerOne reports from Hugging Face |
| `scripts/ingest_anything.py` | Universal ingestion — drop any file into `knowledge-inbox/` |
| `scripts/ingest_urls.py` | Fetch and ingest URLs into the knowledge base |
| `scripts/generate_security_taxonomies.py` | Generate taxonomy/summary files |
| `scripts/generate_mcp_config.py` | Write local MCP configs with absolute paths |
| `scripts/download_index.sh` | Download pre-built ChromaDB index |
| `scripts/reindex_knowledge.py` | Trigger knowledge-rag reindex |
| `scripts/validate_security_brain.py` | Validate entire setup |
| `scripts/validate_ingestion.py` | Validate ingestion output |
| `scripts/generate_ingestion_report.py` | Generate ingestion summary report |

## Add New Knowledge

Drop any file into `knowledge-inbox/` and ingest:

```bash
# Preview what would be processed
python scripts/ingest_anything.py --dry-run

# Ingest everything
python scripts/ingest_anything.py --dedupe --redact-secrets

# Ingest and reindex
python scripts/ingest_anything.py --index
```

Supported: Markdown, Text, HTML, PDF, DOCX, PPTX, XLSX, CSV, JSON, JSONL, code files, ZIP/TAR archives.

## Docs

- [docs/SECURITY_BRAIN_SETUP.md](docs/SECURITY_BRAIN_SETUP.md) — architecture, ingestion, indexing
- [docs/MCP_CLIENT_SETUP.md](docs/MCP_CLIENT_SETUP.md) — Claude Code, opencode, generic client setup
- [docs/UNIVERSAL_INGESTION.md](docs/UNIVERSAL_INGESTION.md) — universal knowledge ingestion
- [docs/OPERATIONS.md](docs/OPERATIONS.md) — updates, tuning, troubleshooting

## Requirements

- Python 3.11+
- ~200MB disk for embedding models (auto-downloaded on first query)
- ~900MB disk for ChromaDB index (downloaded by install script)
- MCP-compatible LLM harness

## License

MIT

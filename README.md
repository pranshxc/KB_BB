# Security Brain

A local RAG knowledge base for LLM harnesses, built on `knowledge-rag`. Ingests HackerOne disclosed reports, security taxonomies, and curated vulnerability summaries — searchable via any MCP client (Claude Code, opencode, Cursor, etc.).

`knowledge-rag` is included as a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules). Clone with `--recurse-submodules` or run `git submodule update --init` after cloning.

## One-Click Install

```bash
# Claude Code
bash <(curl -fsSL https://raw.githubusercontent.com/pranshxc/KB_BB/main/scripts/install.sh) claude

# opencode
bash <(curl -fsSL https://raw.githubusercontent.com/pranshxc/KB_BB/main/scripts/install.sh) opencode
```

Or if already cloned:

```bash
git submodule update --init     # get knowledge-rag
./scripts/install.sh             # auto-detect
./scripts/install.sh claude      # force Claude Code
```

The install script: clones the repo, initializes the `knowledge-rag` submodule, sets up a Python venv, installs dependencies, generates taxonomies, downloads 12,492 HackerOne reports, starts background indexing, and registers the MCP server.

## Manual Setup

```bash
git clone --recurse-submodules https://github.com/pranshxc/KB_BB.git
cd KB_BB/knowledge-rag
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && pip install -e .
pip install datasets pyyaml python-slugify tqdm rich
cd ..

# Generate taxonomies & import reports
python scripts/generate_security_taxonomies.py
python scripts/import_h1_hf_to_markdown.py

# Generate local MCP config
python scripts/generate_mcp_config.py

# Or register directly:
claude mcp add security-brain -s user -- \
  "$PWD/knowledge-rag/.venv/bin/python" -m mcp_server.server

# Start the MCP server
cd knowledge-rag && .venv/bin/python -m mcp_server.server
```

## Structure

```
├── security-brain/          # Knowledge base
│   ├── hackerone/
│   │   ├── reports/         # 12,492 HackerOne reports (Markdown + YAML)
│   │   ├── summaries/       # Curated vulnerability summaries
│   │   └── taxonomies/      # Bug classes, root causes, testing methodology
│   ├── blogs/               # Blog/article placeholders
│   ├── docs/                # Reference docs (OWASP, CWE)
│   ├── internal/            # Internal security docs
│   ├── prompts/             # Harness instructions
│   └── evals/               # Sample evaluation queries
├── knowledge-rag/           # MCP RAG engine (git submodule)
├── scripts/                 # Utility scripts
├── configs/                 # MCP configuration templates
└── docs/                    # Full documentation
```

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/install.sh` | One-click install (clone, setup, index, register) |
| `scripts/import_h1_hf_to_markdown.py` | Import HackerOne reports from Hugging Face |
| `scripts/generate_security_taxonomies.py` | Generate taxonomy/summary files |
| `scripts/generate_mcp_config.py` | Write local MCP configs with absolute paths |
| `scripts/validate_security_brain.py` | Validate entire setup (50 checks) |
| `scripts/print_mcp_setup.py` | Print MCP setup instructions |
| `scripts/ingest_anything.py` | Universal ingestion: drop any file into `knowledge-inbox/` |
| `scripts/ingest_urls.py` | Fetch and ingest URLs into the knowledge base |
| `scripts/reindex_knowledge.py` | Trigger knowledge-rag reindex |
| `scripts/validate_ingestion.py` | Validate ingestion output |
| `scripts/generate_ingestion_report.py` | Generate ingestion summary report |

## Universal Knowledge Ingestion

Drop any supported file into `knowledge-inbox/` and run:

```bash
# Preview
python scripts/ingest_anything.py --dry-run

# Ingest everything
python scripts/ingest_anything.py --dedupe --redact-secrets

# With reindex
python scripts/ingest_anything.py --index
```

Supports: Markdown, Text, HTML, PDF, DOCX, PPTX, XLSX, CSV, JSON, JSONL, code files, ZIP/TAR archives. Gracefully falls back if parser dependencies are missing. See [`docs/UNIVERSAL_INGESTION.md`](docs/UNIVERSAL_INGESTION.md) for full docs.

## Docs

- [docs/SECURITY_BRAIN_SETUP.md](docs/SECURITY_BRAIN_SETUP.md) — architecture, ingestion, indexing
- [docs/MCP_CLIENT_SETUP.md](docs/MCP_CLIENT_SETUP.md) — Claude Code, opencode, generic client setup
- [docs/OPERATIONS.md](docs/OPERATIONS.md) — updates, tuning, troubleshooting

## Stats

- **12,492** unique HackerOne reports from 2 Hugging Face datasets
- **26,732** indexed chunks (172MB ChromaDB index)
- **12** taxonomy + summary files
- **34** sample evaluation queries
- **0** import errors
- **100%** validation pass rate

## Requirements

- Python 3.11+
- ~200MB disk for embedding models (auto-downloaded)
- MCP-compatible LLM harness

## License

MIT

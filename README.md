# Security Brain

A local RAG knowledge base for LLM harnesses, built on `knowledge-rag`. Ingests HackerOne disclosed reports, security taxonomies, and curated vulnerability summaries — searchable via any MCP client (Claude Code, opencode, Cursor, etc.).

## One-Click Install

```bash
# Claude Code
bash <(curl -fsSL https://raw.githubusercontent.com/REPO_OWNER/security-brain/main/scripts/install.sh) claude

# opencode
bash <(curl -fsSL https://raw.githubusercontent.com/REPO_OWNER/security-brain/main/scripts/install.sh) opencode
```

Or if you've already cloned the repo:

```bash
./scripts/install.sh          # auto-detect client
./scripts/install.sh claude   # force Claude Code
./scripts/install.sh opencode # force opencode
```

**What it does**: clones the repo, sets up Python venv, installs deps, downloads 12,492 HackerOne reports, indexes them, and registers the MCP server with your client. Takes ~2 min for setup, then indexes in background.

## Manual Setup

```bash
git clone https://github.com/REPO_OWNER/security-brain.git
cd security-brain/knowledge-rag
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && pip install -e .
cd .. && python scripts/generate_security_taxonomies.py
python scripts/import_h1_hf_to_markdown.py

# Start the MCP server
cd knowledge-rag && .venv/bin/python -m mcp_server.server

# In another terminal, register with client:
claude mcp add security-brain -s user -- /path/to/knowledge-rag/.venv/bin/python -m mcp_server.server
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
├── knowledge-rag/           # MCP RAG engine (submodule-ready)
├── scripts/                 # Utility scripts
├── configs/                 # MCP configuration examples
└── docs/                    # Full documentation
```

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/import_h1_hf_to_markdown.py` | Import HackerOne reports from Hugging Face |
| `scripts/generate_security_taxonomies.py` | Generate taxonomy/summary files |
| `scripts/validate_security_brain.py` | Validate entire setup (50 checks) |
| `scripts/print_mcp_setup.py` | Print MCP setup instructions |

## Docs

- [SECURITY_BRAIN_SETUP.md](docs/SECURITY_BRAIN_SETUP.md) — architecture, ingestion, indexing
- [MCP_CLIENT_SETUP.md](docs/MCP_CLIENT_SETUP.md) — Claude Code, opencode, generic client setup
- [OPERATIONS.md](docs/OPERATIONS.md) — updates, tuning, troubleshooting

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

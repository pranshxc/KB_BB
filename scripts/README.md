# Security Brain Scripts

## Scripts Overview

| Script | Purpose | Usage |
|--------|---------|-------|
| `import_h1_hf_to_markdown.py` | Import HackerOne disclosed reports from Hugging Face and convert to Markdown | `python import_h1_hf_to_markdown.py [options]` |
| `generate_security_taxonomies.py` | Generate security taxonomy and summary Markdown files | `python generate_security_taxonomies.py [options]` |
| `validate_security_brain.py` | Validate the entire Security Brain setup | `python validate_security_brain.py [options]` |
| `print_mcp_setup.py` | Print MCP setup instructions for all clients | `python print_mcp_setup.py [options]` |

## Detailed Usage

### import_h1_hf_to_markdown.py

Import HackerOne disclosed reports from Hugging Face datasets.

```bash
# Default: import all datasets, no limit
python import_h1_hf_to_markdown.py

# Limit to 100 reports per split
python import_h1_hf_to_markdown.py --limit 100

# Overwrite existing files
python import_h1_hf_to_markdown.py --overwrite

# Organize by weakness category
python import_h1_hf_to_markdown.py --organize-by-weakness

# Custom output directory
python import_h1_hf_to_markdown.py --output-dir /path/to/reports

# Custom datasets
python import_h1_hf_to_markdown.py --dataset elamaran619/hackerone_disclosed_reports
```

**Options:**
- `--output-dir`: Output directory (default: `security-brain/hackerone/reports`)
- `--dataset`: Hugging Face dataset (can specify multiple times)
- `--limit N`: Limit rows per dataset split
- `--no-limit`: Explicitly disable row limit
- `--organize-by-weakness`: Organize into subdirectories by weakness
- `--overwrite`: Overwrite existing files

### generate_security_taxonomies.py

Generate taxonomy and summary Markdown files.

```bash
# Default: generate all taxonomies and summaries
python generate_security_taxonomies.py

# Custom directories
python generate_security_taxonomies.py \
  --taxonomies-dir security-brain/hackerone/taxonomies \
  --summaries-dir security-brain/hackerone/summaries
```

**Options:**
- `--taxonomies-dir`: Taxonomy output directory
- `--summaries-dir`: Summary output directory

### validate_security_brain.py

Validate the Security Brain setup — checks directories, files, indexes, and MCP server.

```bash
# Default: validate everything
python validate_security_brain.py

# With custom paths
python validate_security_brain.py \
  --security-brain-dir security-brain \
  --knowledge-rag-dir knowledge-rag \
  --venv-python knowledge-rag/.venv/bin/python
```

**Options:**
- `--security-brain-dir`: Security brain directory
- `--scripts-dir`: Scripts directory
- `--configs-dir`: Configs directory
- `--docs-dir`: Docs directory
- `--knowledge-rag-dir`: knowledge-rag directory
- `--venv-python`: Path to venv Python (auto-detected)

### print_mcp_setup.py

Print setup instructions for all MCP clients.

```bash
python print_mcp_setup.py
python print_mcp_setup.py --venv-python /path/to/venv/bin/python
```

## Workflow

### Initial Setup

```bash
# 1. Generate taxonomies
python generate_security_taxonomies.py

# 2. Import HackerOne reports
python import_h1_hf_to_markdown.py

# 3. Validate
python validate_security_brain.py

# 4. Print setup instructions
python print_mcp_setup.py
```

### Updating

```bash
# Re-import HackerOne reports (overwrite)
python import_h1_hf_to_markdown.py --overwrite

# Validate after update
python validate_security_brain.py

# Restart MCP server to reindex
```

## Dependencies

All scripts require Python 3.11+ and these packages:
- `datasets` (for Hugging Face dataset loading)
- `pyyaml` (for YAML frontmatter)
- `python-slugify` (for filename generation)
- `tqdm` (for progress bars)
- `rich` (for formatted output, optional)

Install via:
```bash
pip install datasets pyyaml python-slugify tqdm rich
```

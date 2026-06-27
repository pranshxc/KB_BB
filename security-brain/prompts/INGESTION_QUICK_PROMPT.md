# Ingestion Quick Prompt

Paste this prompt into Claude Code or opencode to ingest everything from `knowledge-inbox/`:

---

Use the KB_BB Smart Knowledge Ingestion pipeline.
Ingest all supported files from `knowledge-inbox/` into `security-brain/imported/`, deduplicate, redact secrets, validate, and reindex the knowledge base.

Steps:
1. Dry-run: `python scripts/ingest_anything.py --dry-run`
2. If clean: `python scripts/ingest_anything.py --dedupe --redact-secrets --index`
3. Validate: `python scripts/validate_ingestion.py`
4. Report summary

---

## One-liner

> Ingest everything from knowledge-inbox/ into the Security Brain. Dedupe, redact secrets, validate, and reindex.

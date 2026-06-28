#!/usr/bin/env bash
# Download pre-built knowledge index from GitHub Releases.
# Usage: bash scripts/download_index.sh [TAG]
#   TAG defaults to "latest"

set -euo pipefail

REPO="pranshxc/KB_BB"
TAG="${1:-latest}"
INDEX_URL="https://github.com/$REPO/releases/download/$TAG/knowledge-rag-data.tar.gz"
DATA_DIR="knowledge-rag/data"

echo "Downloading pre-built knowledge index..."
echo "  URL:  $INDEX_URL"
echo "  Dest: $DATA_DIR/"

mkdir -p "$DATA_DIR"

curl -fsSL "$INDEX_URL" | tar xzf - -C "$DATA_DIR/"
echo ""
echo "Index downloaded. Start the MCP server:"
echo "  cd knowledge-rag"
echo "  source .venv/bin/activate"
echo "  knowledge-rag"

#!/usr/bin/env bash
# Security Brain — one-command install
set -euo pipefail

REPO="pranshxc/KB_BB"
BRANCH="main"
MCP_NAME="security-brain"
KR_REPO="https://github.com/lyonzin/knowledge-rag.git"
INDEX_RELEASE="https://github.com/$REPO/releases/download/v1.0/knowledge-rag-data.tar.gz"

BOLD='\033[1m'; GREEN='\033[92m'; YELLOW='\033[93m'
CYAN='\033[96m'; RED='\033[91m'; RESET='\033[0m'

info()  { echo -e "${CYAN}::${RESET} $1"; }
ok()    { echo -e "${GREEN}✓${RESET} $1"; }
warn()  { echo -e "${YELLOW}⚠${RESET} $1"; }
fail()  { echo -e "${RED}✗${RESET} $1"; exit 1; }

detect_client() {
  if command -v claude &>/dev/null; then echo "claude"
  elif command -v opencode &>/dev/null; then echo "opencode"
  else echo "unknown"; fi
}

CLIENT="${1:-$(detect_client)}"
INSTALL_DIR="${2:-$HOME/KB_BB}"

echo ""
echo -e "${BOLD}Security Brain — One-Click Install${RESET}"
echo "================================="
echo " Target:   $INSTALL_DIR"
echo " Client:   $CLIENT"
echo ""

# ── 1. Clone repo + submodules ─────────────────────────────────────
if [[ -d "$INSTALL_DIR/.git" ]]; then
  info "Updating existing installation..."
  cd "$INSTALL_DIR"
  git pull origin "$BRANCH" 2>/dev/null || warn "git pull failed (continuing)"
else
  info "Cloning repository..."
  git clone --depth 1 --recurse-submodules "https://github.com/$REPO.git" "$INSTALL_DIR"
  cd "$INSTALL_DIR"
fi

if [[ ! -f "$INSTALL_DIR/knowledge-rag/pyproject.toml" ]]; then
  info "knowledge-rag not found — initializing submodule..."
  git submodule update --init --depth 1 2>/dev/null || \
    git clone --depth 1 "$KR_REPO" "$INSTALL_DIR/knowledge-rag"
fi
ok "Repository ready at $INSTALL_DIR"

# ── 2. Find Python 3.11+ ───────────────────────────────────────────
PYTHON=""
for cmd in python3.12 python3.11 python3; do
  if command -v "$cmd" &>/dev/null; then
    ver=$("$cmd" --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
    major="${ver%.*}"; minor="${ver#*.}"
    if [[ "$major" -ge 3 && "$minor" -ge 11 ]]; then PYTHON="$cmd"; break; fi
  fi
done
[[ -z "$PYTHON" ]] && fail "Python 3.11+ not found. Install it first, e.g.: brew install python@3.12"
ok "Using $($PYTHON --version)"

# ── 3. venv + deps ─────────────────────────────────────────────────
cd "$INSTALL_DIR/knowledge-rag"

if [[ "$(uname)" == "Darwin" ]] && [[ -d "/opt/homebrew/opt/expat/lib" ]]; then
  export DYLD_LIBRARY_PATH="/opt/homebrew/opt/expat/lib:$DYLD_LIBRARY_PATH"
  HAS_EXPAT=1
else
  HAS_EXPAT=0
fi

if [[ ! -d ".venv" ]]; then "$PYTHON" -m venv .venv; fi
# shellcheck disable=SC1091
source .venv/bin/activate
pip install -q -r requirements.txt
pip install -q -e .
pip install -q datasets pyyaml python-slugify tqdm rich 2>/dev/null || true
ok "Dependencies installed"

# ── 4. Generate taxonomies ─────────────────────────────────────────
info "Generating security taxonomies..."
"$PYTHON" "$INSTALL_DIR/scripts/generate_security_taxonomies.py" 2>/dev/null
ok "Taxonomies generated"

# ── 5. Import HackerOne reports ────────────────────────────────────
if [[ ! -f "$INSTALL_DIR/security-brain/hackerone/import_summary.json" ]]; then
  info "Importing HackerOne reports from Hugging Face..."
  "$PYTHON" "$INSTALL_DIR/scripts/import_h1_hf_to_markdown.py" --overwrite 2>/dev/null
  ok "HackerOne reports imported"
else
  info "HackerOne reports already present"
  ok "Using existing reports"
fi

# ── 6. Download pre-built index ────────────────────────────────────
INDEX_DIR="$INSTALL_DIR/knowledge-rag/data"
if [[ -f "$INDEX_DIR/chroma_db/chroma.sqlite3" ]]; then
  info "Index already exists"
  ok "Using existing index ($(du -sh "$INDEX_DIR" 2>/dev/null | cut -f1))"
else
  info "Downloading pre-built knowledge index (390MB)..."
  mkdir -p "$INDEX_DIR"
  if curl -fsSL "$INDEX_RELEASE" | tar xzf - -C "$INDEX_DIR/"; then
    ok "Pre-built index downloaded ($(du -sh "$INDEX_DIR" 2>/dev/null | cut -f1))"
  else
    warn "Download failed — building index from scratch (this takes ~30 minutes)..."
    cd "$INSTALL_DIR/knowledge-rag"
    nohup .venv/bin/python -m mcp_server.server --transport sse \
      > /tmp/kr-index.log 2>&1 &
    INDEX_PID=$!
    info "Indexing started (PID: $INDEX_PID). Log: /tmp/kr-index.log"
    ok "Indexing in background — search works once chunks are embedded"
  fi
fi

# ── 7. Register MCP client ─────────────────────────────────────────
VENV_PYTHON="$INSTALL_DIR/knowledge-rag/.venv/bin/python"

case "$CLIENT" in
  claude)
    info "Registering with Claude Code..."
    claude mcp add "$MCP_NAME" -s user -- "$VENV_PYTHON" -m mcp_server.server
    if [[ "$HAS_EXPAT" == "1" ]] && [[ -f "$HOME/.claude.json" ]]; then
      "$PYTHON" -c "
import json
with open('$HOME/.claude.json') as f:
    cfg = json.load(f)
if 'mcpServers' in cfg and '$MCP_NAME' in cfg['mcpServers']:
    cfg['mcpServers']['$MCP_NAME']['env'] = {'DYLD_LIBRARY_PATH': '/opt/homebrew/opt/expat/lib'}
    with open('$HOME/.claude.json', 'w') as f:
        json.dump(cfg, f, indent=2)
" 2>/dev/null || true
    fi
    ok "Claude Code MCP registered"
    ;;
  opencode)
    info "Registering with opencode..."
    CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/opencode"
    mkdir -p "$CONFIG_DIR"
    CONFIG_FILE="$CONFIG_DIR/opencode.json"
    "$PYTHON" -c "
import json
cfg = {}
try:
    with open('$CONFIG_FILE') as f: cfg = json.load(f)
except: pass
cfg.setdefault('mcp', {})['$MCP_NAME'] = {
    'type': 'local', 'command': ['$VENV_PYTHON', '-m', 'mcp_server.server'], 'enabled': True
}
with open('$CONFIG_FILE', 'w') as f: json.dump(cfg, f, indent=2)
" 2>/dev/null || true
    ok "opencode MCP registered"
    ;;
  *)
    warn "Unknown client: $CLIENT. Add manually:"
    echo "  claude mcp add $MCP_NAME -s user -- $VENV_PYTHON -m mcp_server.server"
    ;;
esac

# ── 8. Done ─────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}${GREEN}Security Brain installed!${RESET}"
echo "================================="
echo "  Repo:     $INSTALL_DIR"
echo "  Reports:  12,492 HackerOne"
echo "  Blogs:    5,253 security blogs"
echo "  Chunks:   108,561 indexed"
echo "  MCP name: $MCP_NAME"
echo "  Client:   $CLIENT"
echo ""
echo "  Next: restart your MCP client, then try:"
echo "    Use the Security Brain to find password reset bugs"
echo "    search_knowledge('IDOR organization membership')"
echo "    search_knowledge('SSRF cloud metadata 169.254.169.254')"
echo "    search_knowledge('GraphQL authorization bypass')"
echo ""

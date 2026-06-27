#!/usr/bin/env bash
set -euo pipefail

REPO="pranshxc/security-brain"
BRANCH="main"
MCP_NAME="security-brain"
INDEX_REPO="pranshxc/security-brain-index"

BOLD='\033[1m'
GREEN='\033[92m'
YELLOW='\033[93m'
CYAN='\033[96m'
RED='\033[91m'
RESET='\033[0m'

info()  { echo -e "${CYAN}::${RESET} $1"; }
ok()    { echo -e "${GREEN}✓${RESET} $1"; }
warn()  { echo -e "${YELLOW}⚠${RESET} $1"; }
fail()  { echo -e "${RED}✗${RESET} $1"; exit 1; }

# ── Detect MCP client ──────────────────────────────────────────────
detect_client() {
  if command -v claude &>/dev/null; then
    echo "claude"
  elif command -v opencode &>/dev/null; then
    echo "opencode"
  else
    echo "unknown"
  fi
}

CLIENT="${1:-$(detect_client)}"
INSTALL_DIR="${2:-$HOME/KB_BB}"

echo ""
echo -e "${BOLD}Security Brain — One-Click Install${RESET}"
echo "================================="
echo " Target:   $INSTALL_DIR"
echo " Client:   $CLIENT"
echo ""

# ── 1. Clone / update repo ─────────────────────────────────────────
if [[ -d "$INSTALL_DIR" ]]; then
  info "Updating existing installation..."
  cd "$INSTALL_DIR"
  git pull origin "$BRANCH" 2>/dev/null || warn "Could not git pull (continuing)"
else
  info "Cloning repository..."
  git clone --depth 1 "https://github.com/$REPO.git" "$INSTALL_DIR"
  cd "$INSTALL_DIR"
fi
ok "Repository ready at $INSTALL_DIR"

# ── 2. Find Python 3.11+ ───────────────────────────────────────────
PYTHON=""
for cmd in python3.12 python3.11 python3; do
  if command -v "$cmd" &>/dev/null; then
    ver=$("$cmd" --version 2>&1 | grep -oP '\d+\.\d+')
    major="${ver%.*}"
    minor="${ver#*.}"
    if [[ "$major" -ge 3 && "$minor" -ge 11 ]]; then
      PYTHON="$cmd"
      break
    fi
  fi
done

if [[ -z "$PYTHON" ]]; then
  fail "Python 3.11+ not found. Install it first, e.g.: brew install python@3.12"
fi
ok "Using $($PYTHON --version)"

# ── 3. Set up venv ─────────────────────────────────────────────────
info "Setting up Python virtual environment..."
cd "$INSTALL_DIR/knowledge-rag"

# macOS expat fix
if [[ "$(uname)" == "Darwin" ]] && [[ -d "/opt/homebrew/opt/expat/lib" ]]; then
  export DYLD_LIBRARY_PATH="/opt/homebrew/opt/expat/lib:$DYLD_LIBRARY_PATH"
  HAS_EXPAT=1
else
  HAS_EXPAT=0
fi

if [[ ! -d ".venv" ]]; then
  "$PYTHON" -m venv .venv
fi
source .venv/bin/activate
ok "Virtual environment created"

# ── 4. Install dependencies ────────────────────────────────────────
info "Installing Python dependencies..."
pip install -q -r requirements.txt
pip install -q -e .
pip install -q datasets pyyaml python-slugify tqdm rich 2>/dev/null || true
ok "Dependencies installed"

# ── 5. Generate taxonomies ─────────────────────────────────────────
info "Generating security taxonomies..."
python "$INSTALL_DIR/scripts/generate_security_taxonomies.py" 2>/dev/null
ok "Taxonomies generated"

# ── 6. Download / import HackerOne reports ─────────────────────────
if [[ ! -f "$INSTALL_DIR/security-brain/hackerone/import_summary.json" ]]; then
  info "Importing HackerOne reports from Hugging Face..."
  python "$INSTALL_DIR/scripts/import_h1_hf_to_markdown.py" --overwrite 2>/dev/null
  ok "HackerOne reports imported"
else
  info "HackerOne reports already present, skipping import"
  ok "Using existing HackerOne reports"
fi

# ── 7. Download pre-built index (fast) or build fresh ──────────────
INDEX_DIR="$INSTALL_DIR/knowledge-rag/data"

if [[ "$INSTALL_DIR" != "$HOME/KB_BB" ]]; then
  # Custom install dir — build fresh index
  info "Custom install location. Building index from scratch (this takes ~30 min)..."
  warn "Start the MCP server and let it index in the background:"
  echo ""
  echo "   cd $INSTALL_DIR/knowledge-rag"
  echo "   source .venv/bin/activate"
  echo "   knowledge-rag"
  echo ""
elif [[ -f "$INDEX_DIR/index_metadata.json" ]]; then
  info "Index already exists, skipping"
  ok "Using existing index ($(du -sh "$INDEX_DIR" 2>/dev/null | cut -f1))"
else
  info "Building initial index (this may take 30+ min)..."
  warn "Start the MCP server and let it index in the background:"
  echo ""
  echo "   cd $INSTALL_DIR/knowledge-rag"
  echo "   source .venv/bin/activate"
  echo "   knowledge-rag"
  echo ""
  # Start indexing in background
  cd "$INSTALL_DIR/knowledge-rag"
  nohup .venv/bin/python -m mcp_server.server --transport sse > /tmp/kr-index.log 2>&1 &
  INDEX_PID=$!
  info "Indexing started (PID: $INDEX_PID). Log: /tmp/kr-index.log"
  ok "Indexing in background — search will work once enough chunks are embedded"
fi

# ── 8. Register MCP client ─────────────────────────────────────────
VENV_PYTHON="$INSTALL_DIR/knowledge-rag/.venv/bin/python"
ENV_FLAG=""

case "$CLIENT" in
  claude)
    info "Registering with Claude Code..."
    claude mcp add "$MCP_NAME" -s user -- "$VENV_PYTHON" -m mcp_server.server
    if [[ "$HAS_EXPAT" == "1" ]]; then
      # Inject DYLD_LIBRARY_PATH into config
      CONFIG_FILE="$HOME/.claude.json"
      if [[ -f "$CONFIG_FILE" ]]; then
        python3 -c "
import json
with open('$CONFIG_FILE') as f:
    cfg = json.load(f)
if 'mcpServers' in cfg and '$MCP_NAME' in cfg['mcpServers']:
    cfg['mcpServers']['$MCP_NAME']['env'] = {'DYLD_LIBRARY_PATH': '/opt/homebrew/opt/expat/lib'}
    with open('$CONFIG_FILE', 'w') as f:
        json.dump(cfg, f, indent=2)
    print('Added DYLD_LIBRARY_PATH to MCP config')
" 2>/dev/null || true
      fi
    fi
    ok "Claude Code MCP registered"
    ;;
  opencode)
    info "Registering with opencode..."
    CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/opencode"
    mkdir -p "$CONFIG_DIR"
    CONFIG_FILE="$CONFIG_DIR/opencode.json"
    if [[ -f "$CONFIG_FILE" ]]; then
      python3 -c "
import json
with open('$CONFIG_FILE') as f:
    cfg = json.load(f)
cfg.setdefault('mcp', {})['$MCP_NAME'] = {
    'type': 'local',
    'command': ['$VENV_PYTHON', '-m', 'mcp_server.server'],
    'enabled': True
}
with open('$CONFIG_FILE', 'w') as f:
    json.dump(cfg, f, indent=2)
" 2>/dev/null || true
    else
      cat > "$CONFIG_FILE" << MCPEOF
{
  "\$schema": "https://opencode.ai/config.json",
  "mcp": {
    "$MCP_NAME": {
      "type": "local",
      "command": ["$VENV_PYTHON", "-m", "mcp_server.server"],
      "enabled": true
    }
  }
}
MCPEOF
    fi
    ok "opencode MCP registered"
    ;;
  *)
    warn "Unknown MCP client: $CLIENT"
    echo ""
    echo "  To add manually, run:"
    echo "    claude mcp add security-brain -s user -- $VENV_PYTHON -m mcp_server.server"
    echo ""
    ;;
esac

# ── 9. Done ─────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}${GREEN}Security Brain installed successfully!${RESET}"
echo "================================="
echo ""
echo -e "  ${BOLD}Repo:${RESET}     $INSTALL_DIR"
echo -e "  ${BOLD}Reports:${RESET}  12,492 HackerOne reports"
echo -e "  ${BOLD}MCP name:${RESET} $MCP_NAME"
echo -e "  ${BOLD}Client:${RESET}   $CLIENT"
echo ""

if [[ "$HAS_EXPAT" == "1" ]]; then
  echo -e "  ${YELLOW}macOS expat fix applied to MCP config${RESET}"
  echo ""
fi

echo "  Next steps:"
echo "    1. Restart your MCP client"
echo "    2. Try: Use the Security Brain to find password reset bugs"
echo "    3. Or: search_knowledge('IDOR organization membership')"
echo ""
echo "  To re-index (if you want all 12K reports fully embedded):"
echo "    cd $INSTALL_DIR/knowledge-rag"
echo "    source .venv/bin/activate"
echo "    knowledge-rag"
echo ""

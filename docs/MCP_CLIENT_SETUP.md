# MCP Client Setup Guide

This guide explains how to connect your MCP client to the Security Brain knowledge-rag server.

## Prerequisites

- Python 3.11+
- knowledge-rag installed and configured (see SECURITY_BRAIN_SETUP.md)
- Virtual environment activated

## 1. Start the MCP Server

### Manual Start

```bash
cd /path/to/knowledge-rag
source .venv/bin/activate

# macOS expat fix (if needed):
export DYLD_LIBRARY_PATH="/opt/homebrew/opt/expat/lib:$DYLD_LIBRARY_PATH"

# Start server:
knowledge-rag
```

The server auto-indexes documents and starts listening on stdio for MCP commands.

### Verify Server

```bash
# In Claude Code:
claude mcp list

# Expected output includes "security-brain" or the MCP server name
```

## 2. Claude Code Setup

### Option A: Using Claude Code CLI (Recommended)

```bash
claude mcp add security-brain -s user -- \
  /path/to/knowledge-rag/.venv/bin/python \
  -m mcp_server.server
```

### Option B: Manual Config

Config file location: `~/.claude.json`

```json
{
  "mcpServers": {
    "security-brain": {
      "type": "stdio",
      "command": "/path/to/knowledge-rag/.venv/bin/python",
      "args": ["-m", "mcp_server.server"],
      "env": {
        "DYLD_LIBRARY_PATH": "/opt/homebrew/opt/expat/lib"
      }
    }
  }
}
```

A pre-configured example is available at `configs/claude-code.mcp.json`.

**Note**: Update the `command` path to match your system.

## 3. opencode Setup

Config file location: `~/.config/opencode/opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "security-brain": {
      "type": "local",
      "command": [
        "/path/to/knowledge-rag/.venv/bin/python",
        "-m",
        "mcp_server.server"
      ],
      "enabled": true,
      "environment": {
        "DYLD_LIBRARY_PATH": "/opt/homebrew/opt/expat/lib"
      }
    }
  }
}
```

A pre-configured example is available at `configs/opencode.json`.

## 4. Generic MCP Client Setup

For Claude Desktop, Cursor, Antigravity, Windsurf, or any stdio MCP client:

```json
{
  "mcpServers": {
    "security-brain": {
      "command": "/path/to/knowledge-rag/.venv/bin/python",
      "args": ["-m", "mcp_server.server"]
    }
  }
}
```

For VS Code (uses `servers` key instead of `mcpServers`):

```json
{
  "servers": {
    "security-brain": {
      "type": "stdio",
      "command": "/path/to/knowledge-rag/.venv/bin/python",
      "args": ["-m", "mcp_server.server"]
    }
  }
}
```

## 5. Verify Connection

### Test Search

In your MCP client, run:

```
search_knowledge("password reset token", max_results=3)
```

Expected: Returns HackerOne reports and taxonomy documents matching the query.

### List Documents

```
list_documents()
```

### Get Stats

```
get_index_stats()
```

## 6. Example Prompts for Claude Code

Once connected, try these prompts:

1. "Use my Security Brain to find HackerOne examples of password reset token invalidation bugs."
2. "Search for IDOR bugs in organization membership systems and produce a secure review checklist."
3. "Use the knowledge base to review OAuth redirect_uri handling."
4. "Find SSRF-related HackerOne reports and summarize defensive mitigations."
5. "Search my Security Brain for GraphQL authorization bypass patterns."
6. "Use the security taxonomy to explain common XSS prevention techniques."
7. "Find file upload vulnerability patterns in my Security Brain."
8. "Search for information disclosure examples and build a detection checklist."
9. "What does the knowledge base say about JWT algorithm confusion?"
10. "Use the Security Brain to create a secure code review checklist for API authentication."

## 7. Troubleshooting

| Symptom | Solution |
|---------|----------|
| MCP server not found | Activate venv: `source .venv/bin/activate` |
| ImportError: pyexpat | Set `DYLD_LIBRARY_PATH` for Homebrew expat |
| Slow first query | Normal — models download on first query |
| No documents found | Run `reindex_documents()` or restart server |
| Python version error | Ensure Python 3.11+ (`python --version`) |
| "Failed to connect" | Check paths in config file, restart MCP client |

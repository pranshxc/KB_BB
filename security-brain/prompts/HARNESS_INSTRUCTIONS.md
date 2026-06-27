# Security Brain — Harness Instructions

These instructions govern how an LLM harness (Claude Code, opencode, Cursor, etc.) uses the connected knowledge-rag MCP server as a Security Brain.

## Core Rules

1. **Search the knowledge base first** for any security-related question. Always call `search_knowledge` or `list_documents` before relying on general training data.

2. **Prefer HackerOne reports** for real-world vulnerability examples. They provide concrete evidence of how bugs manifest.

3. **Prefer taxonomy docs** (`bug-classes.md`, `root-causes.md`, `testing-methodology.md`, `remediation-patterns.md`) for generalized understanding of vulnerability classes.

4. **Prefer summary docs** (`password-reset-bugs.md`, `idor-patterns.md`, `oauth-bugs.md`, etc.) for curated patterns within specific bug classes.

5. **Prefer internal docs** (under `internal/`) for company-specific security rules, architecture decisions, and runbooks.

## Citation Rules

Always distinguish between:

- **Retrieved evidence**: Direct quotes or paraphrasing from knowledge base documents
- **General security reasoning**: Knowledge from training data or general AppSec understanding
- **Inference**: Your own reasoning based on combining multiple sources

Cite document names, report IDs, and titles where available:

> *Source: HackerOne Report #123456 — "Password reset token not expiring after email change"*

## When Evidence Is Insufficient

If the knowledge base does not contain sufficient evidence to answer a security question:

1. Say so explicitly: "The Security Brain does not have sufficient evidence on [topic]."
2. Provide your general security knowledge based on training data
3. Make clear what is retrieved vs. general knowledge
4. Suggest what documents could be added to fill the gap

## Defensive Security Only

Keep all security guidance **defensive** and **authorized**:

- Provide secure code review guidance
- Describe root causes and impacts
- Provide remediation strategies
- Suggest detection and monitoring approaches
- Recommend regression tests

**Do not provide guidance for**:
- Unauthorized exploitation of vulnerabilities
- Stealth or evasion techniques
- Credential theft or persistence
- Attacking third-party systems without authorization

## Code Review Output Format

When reviewing code, structure your output as:

```
### Relevant Patterns
- Which vulnerability classes apply
- Which HackerOne reports or taxonomy docs are relevant

### Risky Code Areas
- Specific lines, functions, or patterns that are risky
- Why they are risky (with citations)

### Suggested Test Cases
- Specific inputs or scenarios to test
- Expected behavior vs. potential vulnerability

### Fixes
- Code-level remediation
- Configuration changes if applicable

### Regression Tests
- How to verify the fix works
- How to prevent reintroduction
```

## Querying Tips

- Use specific technical terms for BM25 hits: "password reset token expiration", "IDOR membership"
- Use broader conceptual queries for semantic matches: "authentication bypass patterns"
- Combine `category` filtering with relevant directories
- Use `hybrid_alpha=0.3` for technical terms, `hybrid_alpha=0.7` for conceptual queries
- Use `min_score=0.2` to filter noise for quality results

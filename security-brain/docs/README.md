# Security Documentation

This directory stores reference security documentation.

## Structure

```
docs/
├── owasp/           # OWASP guides and references
├── cwe/             # CWE definitions and mappings
└── cheatsheets/     # Security cheatsheets
```

## How to Add Content

### OWASP Content

Add Markdown summaries of OWASP guides. Recommended topics:
- OWASP Top 10 (2021)
- OWASP ASVS (Application Security Verification Standard)
- OWASP Cheat Sheet Series
- OWASP Testing Guide

### CWE References

Add CWE definitions relevant to your technology stack. Include:
- CWE ID and name
- Description
- Typical severity
- Mitigation references

### Cheatsheets

Create security cheatsheets using Markdown format with YAML frontmatter:

```yaml
---
title: "Security Cheatsheet Title"
category: "cheatsheet"
tags:
  - secure-coding
  - web
  - api
---
```

### Adding via knowledge-rag MCP

```
add_document(content="# My Doc...", filepath="docs/owasp/top-ten.md", category="docs")
```

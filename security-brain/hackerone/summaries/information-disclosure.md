---
title: Information Disclosure Patterns
description: Common information disclosure vulnerability patterns.
created: 2026-06-26
tags:
  - hackerone
  - information-disclosure
  - summary
---

# Information Disclosure Vulnerability Patterns

## Common Vulnerability Patterns

### 1. Debug Endpoints Exposed
- `/debug`, `/api/docs`, `/swagger`, `/actuator/health`
- Verbose error messages with stack traces
- Database error exposure in responses

### 2. Directory Listing
- Directory listing enabled on web servers
- Backup files exposed (.bak, ~, .swp)
- Git folder exposed (.git/config, .git/HEAD)

### 3. Source Code Disclosure
- Minified source maps (.map files)
- Backup files with source code
- IDE configuration files (.idea, .vscode)

### 4. Sensitive Data in Responses
- API responses include internal IDs, email addresses
- PII in logs or error messages
- Token/secret in URL parameters

## Defensive Checklist
- [ ] Disable debug endpoints in production
- [ ] Implement generic error messages
- [ ] Disable directory listing
- [ ] Set proper security headers
- [ ] Audit API responses for sensitive data
- [ ] Scan for exposed files periodically

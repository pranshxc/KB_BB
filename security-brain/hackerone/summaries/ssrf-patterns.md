---
title: SSRF Vulnerability Patterns
description: Common Server-Side Request Forgery vulnerability patterns and defenses.
created: 2026-06-26
tags:
  - hackerone
  - ssrf
  - server-side
  - cloud
  - summary
---

# SSRF Vulnerability Patterns

## Common Vulnerability Patterns

### 1. Cloud Metadata Access
- Accessing AWS `http://169.254.169.254/latest/meta-data/`
- Accessing GCP `http://metadata.google.internal/computeMetadata/v1/`
- Accessing Azure `http://169.254.169.254/metadata/instance`

### 2. Internal Network Scanning
- SSRF to internal services (Redis, MySQL, Elasticsearch)
- Port scanning via SSRF
- Protocol smuggling (gopher://, dict://, file://)

### 3. Blind SSRF
- Outbound request to attacker-controlled server
- Timing-based data exfiltration

### 4. DNS Rebinding
- Domain initially resolves to legitimate IP
- After validation, attacker changes DNS to internal IP

### 5. SSRF via File Upload / Image Processing
- Image URL processing leads to SSRF
- PDF generation with external resource inclusion

## Defensive Checklist
- [ ] Block access to private/meta IP ranges
- [ ] Use URL allowlist, not denylist
- [ ] Validate URL scheme (reject file://, gopher://, dict://)
- [ ] Use dedicated HTTP client with restricted capabilities
- [ ] Apply network-level controls (firewall, proxy)
- [ ] Disable DNS rebinding protection on resolver

---
title: File Upload Vulnerability Patterns
description: Common file upload security vulnerabilities.
created: 2026-06-26
tags:
  - hackerone
  - file-upload
  - summary
---

# File Upload Vulnerability Patterns

## Common Vulnerability Patterns

### 1. Content-Type Bypass
- Attacker modifies Content-Type header to bypass validation
- MIME type sniffing by browser leads to XSS

### 2. Path Traversal in Filename
- Filename contains ../ to write outside upload directory
- Archive extraction creates files outside target dir (Zip Slip)

### 3. Unrestricted File Upload
- Executable files uploaded (.php, .jsp, .war)
- SVG upload with embedded scripts (XSS)

### 4. File Size / Resource Abuse
- No file size limit → disk exhaustion
- Multiple large parallel uploads → DoS

### 5. Storage-Based Attacks
- Uploaded files served from same domain → cookie theft
- Direct access to uploaded files without authorization

## Defensive Checklist
- [ ] Validate file content, not just content-type
- [ ] Generate random filenames, preserve extension safely
- [ ] Restrict executable file extensions
- [ ] Set file size limits
- [ ] Serve uploads from separate domain/CDN
- [ ] Scan uploads for malware
- [ ] Use anti-virus / sandbox for suspicious files

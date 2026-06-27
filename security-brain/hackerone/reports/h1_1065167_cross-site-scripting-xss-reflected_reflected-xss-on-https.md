---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1065167'
original_report_id: '1065167'
title: Reflected XSS on https://█████████/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-12-23T14:47:28.932Z'
disclosed_at: '2021-02-01T17:47:32.810Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://█████████/

## Metadata

- HackerOne Report ID: 1065167
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-02-01T17:47:32.810Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Vulnerable Website URL or Application:
```javascript
https://███████/███████=%22%3E%3Csvg/onload=alert(%22nagli%22)%3E
```

##Description of Security Issue: (please limit to one site/app per submission)

Reflected XSS due to no input validation

██████████

##Steps needed to reproduce bug:
Navigate to
```javascript
https://███████/█████████=%22%3E%3Csvg/onload=alert(%22nagli%22)%3E
```
Choose whatever javascript you'd like to execute on the sub_div_ofc_sym_cd query parameter

##Remediation
Sanitize the input on the that parameter

##Best Regards
nagli

## Impact

Executing Javascript on behalf of the victim

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

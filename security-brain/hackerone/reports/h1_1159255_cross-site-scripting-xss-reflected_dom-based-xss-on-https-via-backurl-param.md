---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1159255'
original_report_id: '1159255'
title: DOM Based XSS on https://████ via backURL param
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-04-09T14:34:17.917Z'
disclosed_at: '2021-05-11T20:15:57.434Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# DOM Based XSS on https://████ via backURL param

## Metadata

- HackerOne Report ID: 1159255
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-05-11T20:15:57.434Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**

The following endpoint suffers from DOM Based XSS

```
https://████████/██████=javascript:alert(document.domain)
```

The ████████ param determines the content which will be displayed on the "Back to Search Result" button, eventually leading to RXSS.

## References

██████

## Regards
nagli

## Impact

Executing javascript on the victims behalf

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Navigate to
```
https://█████/████=javascript:alert(document.domain)
```

2. Click on "Back to Search Result"

## Suggested Mitigation/Remediation Actions
Sanitize the user input and do not allow malicious schemes to be inserted per the user input.

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

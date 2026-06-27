---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '374057'
original_report_id: '374057'
title: Corda Server XSS ████████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2018-06-29T22:11:41.943Z'
disclosed_at: '2019-12-02T19:06:16.354Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Corda Server XSS ████████

## Metadata

- HackerOne Report ID: 374057
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:06:16.354Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Cord server will display the error message if something isn't allowed to be used thus allowing xss
**Description:**
/scripts/ctredirector.dll allows users to call images or files. We can use the parameter @_FILE to dictate a file or url, if it fails it'll display the url into the page. We then leverage an additional parameter named @_TEXTDESCRIPTIONEN to make the page display as a text which then allows the opportunity to trigger XSS.
## Impact
Medium
## Step-by-step Reproduction Instructions
Check the following URL in firefox
http://█████████/scripts/ctredirector.dll//?@_FILEhttp://google.com/%3Csvg/onload=confirm(document.cookie)%3E%3E@_TEXTDESCRIPTIONEN

## Product, Version, and Configuration (If applicable)
Corda Server
## Suggested Mitigation/Remediation Actions
Update corda

## Impact

An attacker can steal session cookies and conduct sophisticated phishing campaigns using this exploit

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

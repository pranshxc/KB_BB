---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1071524'
original_report_id: '1071524'
title: Reflected XSS on https://█████████html?url
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-01-04T20:44:42.793Z'
disclosed_at: '2021-01-25T19:52:15.659Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://█████████html?url

## Metadata

- HackerOne Report ID: 1071524
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-01-25T19:52:15.659Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Vulnerable Website URL or Application:
https://███████html?url=javascript:alert("nagli")

##Description of Security Issue: (please limit to one site/app per submission)
Reflected XSS due to no input validation

█████████

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

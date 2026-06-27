---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '484905'
original_report_id: '484905'
title: XSS Reflected
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2019-01-24T01:37:55.408Z'
disclosed_at: '2020-05-27T14:08:16.473Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS Reflected

## Metadata

- HackerOne Report ID: 484905
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2020-05-27T14:08:16.473Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team ,

I found that https://████████/████/household/updateProfileInfo.action has vulnerability by XSS Reflected in household.householdID parameter .

I can verify it with following URL: https://█████████/██████/household/updateProfileInfo.action?household.householdID=%27;alert(document.domain)//

## Impact

XSS Reflected Attack

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

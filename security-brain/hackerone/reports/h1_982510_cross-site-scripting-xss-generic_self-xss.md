---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '982510'
original_report_id: '982510'
title: Self XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2020-09-15T09:58:16.767Z'
disclosed_at: '2020-09-17T16:07:54.581Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 53
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self XSS

## Metadata

- HackerOne Report ID: 982510
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2020-09-17T16:07:54.581Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have found self xss in `myshopify.com/admin/apps/import-store/`
POC

1 - Go to yourstore.myshopify.com
2 - Go to settings > App -> Import [ maybe ask you for your platform select any one ]
3 -  Upload  file csv with file name payload xss "><img src=xx onerror=alert(document.domain)>

## Impact

XSS Attack

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

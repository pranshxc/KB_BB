---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '887879'
original_report_id: '887879'
title: xss stored in https://your store.myshopify.com/admin/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2020-05-31T12:27:24.446Z'
disclosed_at: '2020-08-24T16:08:20.442Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 45
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# xss stored in https://your store.myshopify.com/admin/

## Metadata

- HackerOne Report ID: 887879
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2020-08-24T16:08:20.442Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hello , 
i fond xss stored in  https://your store.myshopify.com/admin/
steps ;
1. go to ```https://swqdewd.myshopify.com/admin/menus/new```
2. click in Add menu item
3. add name ```"><img src="x" onerror="alert(document.cookie)">``` AND any link 
4. now click add 
5. click in remove item 
6. alert 
7. watch the vedio poc for more information

## Impact

xss attack .....

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

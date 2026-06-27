---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '756729'
original_report_id: '756729'
title: Stored XSS in Shopify Chat
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2019-12-12T07:01:36.511Z'
disclosed_at: '2019-12-23T14:45:28.796Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 102
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in Shopify Chat

## Metadata

- HackerOne Report ID: 756729
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2019-12-23T14:45:28.796Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1.install app `Shopify Chat`
2.Click chat on the shop homepage or Shopify Ping to send poc `javascript:alert(1)//https://dqdqdqdqdq.myshopify.com`
3.Click url, alert
{F657395}

## Impact

1.Front end user Self-XSS
2.Administrator XSS foreground user

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

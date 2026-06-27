---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '422707'
original_report_id: '422707'
title: Reflected XSS on $Any$.myshopify.com/admin
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2018-10-11T19:25:34.947Z'
disclosed_at: '2018-11-13T10:16:42.532Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 58
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on $Any$.myshopify.com/admin

## Metadata

- HackerOne Report ID: 422707
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2018-11-13T10:16:42.532Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Description :
Hi,
I have found a reflected cross site scripting vulnerability in <any>.myshopify.com/admin through return_url parameter .

# Step to reproduce :
1-Go to https://<Any>.myshopify.com/admin/authenticate?return_url=javascript:alert(100)//
2-Click on reload this page
3-Xss alert message

## Impact

Xss attack in <Any>.myshopify.com/admin

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

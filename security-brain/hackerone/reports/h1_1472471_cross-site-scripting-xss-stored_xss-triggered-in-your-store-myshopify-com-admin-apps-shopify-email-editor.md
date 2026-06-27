---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1472471'
original_report_id: '1472471'
title: Xss triggered in Your-store.myshopify.com/admin/apps/shopify-email/editor/****
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2022-02-06T09:48:54.622Z'
disclosed_at: '2022-04-25T11:01:01.398Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 62
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Xss triggered in Your-store.myshopify.com/admin/apps/shopify-email/editor/****

## Metadata

- HackerOne Report ID: 1472471
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2022-04-25T11:01:01.398Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
I have found `Store` Xss in shopify-email

#Reproduction Instructions /
1.Configure `shopify-email` for Shopify stores at https://apps.shopify.com/shopify-email
2.Goto `Your-store.myshopify.com/admin/apps/shopify-email/template-branding` 
3.Change F1607675 with "><img src=xx onerror=alert(document.domain)> click `Save`.
4.Now Select any F1607682.
#██████████

#Proof of Concept
███
████

## Impact

Stored XSS triggered.

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

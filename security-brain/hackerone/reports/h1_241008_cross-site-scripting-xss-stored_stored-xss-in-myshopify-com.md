---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '241008'
original_report_id: '241008'
title: Stored XSS in *.myshopify.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2017-06-17T13:20:45.777Z'
disclosed_at: '2017-06-27T13:33:49.917Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in *.myshopify.com

## Metadata

- HackerOne Report ID: 241008
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2017-06-27T13:33:49.917Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

First of all in noticed that this is out of scope "Any issue related to the storefront area being displayed in a <iframe> element in the admin area, for example in the Theme Editor." 

This is not in the store front and this will be set in an XSS payload.

1. Go to https://(YOUR SHOP).myshopify.com/admin/themes/THEME id)/editor
2. Select header and scroll down to "annoucement text".
3. Fill there as payload: "&gt;<img src="x" onerror="alert(document.cookie)">
4. Click save and the XSS will be popped up.

I have checked it twice and it is not gonna reflect on the store front. This XSS is in the myshopify/admin section.

POC screen:
https://snag.gy/FImTKd.jpg

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

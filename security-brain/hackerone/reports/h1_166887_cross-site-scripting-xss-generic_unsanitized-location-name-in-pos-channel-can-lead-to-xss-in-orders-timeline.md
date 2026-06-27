---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '166887'
original_report_id: '166887'
title: Unsanitized Location Name in POS Channel can lead to XSS in Orders Timeline
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-09-08T16:41:23.254Z'
disclosed_at: '2016-09-19T16:02:04.941Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Unsanitized Location Name in POS Channel can lead to XSS in Orders Timeline

## Metadata

- HackerOne Report ID: 166887
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-09-19T16:02:04.941Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi!

I would like to report XSS at Shopify Admin Interface in Orders TImeline, in line Usename processes this order at NAME

NAME is not sanitized and if this is set to <img src=x onerror=prompt(1)> XSS will happen

***POC***
Visit
https://whitehat-3.myshopify.com/admin/orders/2253786753
or
https://whitehat-3.myshopify.com/admin/orders/2253753665

XSS will trigger!

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

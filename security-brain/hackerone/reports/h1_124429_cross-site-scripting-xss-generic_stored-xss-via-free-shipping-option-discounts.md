---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '124429'
original_report_id: '124429'
title: Stored XSS via "Free Shipping" option (Discounts)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-03-19T09:34:31.733Z'
disclosed_at: '2016-04-05T12:11:17.812Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS via "Free Shipping" option (Discounts)

## Metadata

- HackerOne Report ID: 124429
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-04-05T12:11:17.812Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

POC  steps:
1) Go to the customers page and add a new search group named as "><img src=x onerror=prompt(7) (see img1.png)
2) Go to the discounts page, create a new discount code and mark the "Free Shipping" option. 
3) Open a web proxy (i.e. tamper data) and press the "save discount" button.
4) Through the web proxy (i.e. tamper data) modify the POST request and change the value of "discount%5Bapplies_to_resource%5D" to "customer_saved_search" and the "discount%5Bapplies_to_id%5D" to "1131411463" (the id of the new search group in step 1)(see img2.png).
5) Xssed (img3.png)

    Click Save

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

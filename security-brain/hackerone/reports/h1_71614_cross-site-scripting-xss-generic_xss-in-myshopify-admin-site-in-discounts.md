---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '71614'
original_report_id: '71614'
title: XSS in Myshopify Admin Site in DISCOUNTS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-06-19T08:30:40.360Z'
disclosed_at: '2015-07-20T14:37:18.182Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Myshopify Admin Site in DISCOUNTS

## Metadata

- HackerOne Report ID: 71614
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-07-20T14:37:18.182Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

POC

1. Go to Customers and add a new search group named "><img src=x onerror=prompt(7) See creategroup.png
2. Go to Discounts and add a Discount Code based on Customer group and choose the one created above
3. Click Save

XSS in discounts occur (discountxss.png)

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

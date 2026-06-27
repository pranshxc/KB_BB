---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '117449'
original_report_id: '117449'
title: XSS in Draft Orders in Timeline i SHOPIFY Admin Site!
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-02-19T16:48:32.007Z'
disclosed_at: '2016-07-28T16:25:00.228Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Draft Orders in Timeline i SHOPIFY Admin Site!

## Metadata

- HackerOne Report ID: 117449
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-07-28T16:25:00.228Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Create an Draft with a product named "><img src=x onerror=prompt('XSSP')
2. Send the Draft to someone and complete the order.
Order is shown as Completed Drafts as order.png
3. Create a timeline and reference this Draft. As soon as you click POST you will be XSSEd (xss.png)

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

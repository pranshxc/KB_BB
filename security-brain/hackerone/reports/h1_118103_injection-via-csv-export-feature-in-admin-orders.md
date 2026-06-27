---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118103'
original_report_id: '118103'
title: Injection via CSV Export feature in Admin Orders
team_handle: shopify
created_at: '2016-02-23T08:05:15.169Z'
disclosed_at: '2016-03-12T12:39:59.386Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
---

# Injection via CSV Export feature in Admin Orders

## Metadata

- HackerOne Report ID: 118103
- Weakness: 
- Program: shopify
- Disclosed At: 2016-03-12T12:39:59.386Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

i found out that the filtering of "=,-,+" is not working in all data.
there's a way to bypass it.

1. Create a product with title =cmd|' /C calc'!'D2'
2. Add variants (more than 2 variants) then save it.
3. Go to Orders > Create Order
4. search the product we made =cmd|' /C calc'!'D2'
5. Add 2 variants from same item
6. Mark as paid
7. Create Order
8. Go Back to order page > Export > Open in excel

you will see that the first variant is successfully filtered the "="
but the next variant is not filtered anymore.

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

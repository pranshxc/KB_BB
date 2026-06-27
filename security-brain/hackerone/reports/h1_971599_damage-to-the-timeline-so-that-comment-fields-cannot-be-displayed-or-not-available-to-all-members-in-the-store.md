---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '971599'
original_report_id: '971599'
title: damage to the timeline so that comment fields cannot be displayed or not available
  to all members in the store
team_handle: shopify
created_at: '2020-08-31T20:31:36.763Z'
disclosed_at: '2020-09-09T16:45:15.103Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
---

# damage to the timeline so that comment fields cannot be displayed or not available to all members in the store

## Metadata

- HackerOne Report ID: 971599
- Weakness: 
- Program: shopify
- Disclosed At: 2020-09-09T16:45:15.103Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

see https://a-alert-b-y000-b-finda.myshopify.com/admin/discounts/416981811222


I tried to make a discount code with a product name and a discount code like: ± <img src = x onerror = alert (1)> ±

when I havehtag (#) the product name on the timeline (comment) and I get a "server error" reply and it causes crashes to the timeline, so comments are automatically inactive or non-existent.

This can be done by members who want to destroy the shop, so that all members of the shop feel the impact.

## step for reproduction
1. create a product name and discount code using a payload like: ± <img src = x onerror = alert (1)> ±
2. Product name hashtags in the timeline
3. The comment field cannot be displayed

## Impact

The comment field cannot be displayed

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

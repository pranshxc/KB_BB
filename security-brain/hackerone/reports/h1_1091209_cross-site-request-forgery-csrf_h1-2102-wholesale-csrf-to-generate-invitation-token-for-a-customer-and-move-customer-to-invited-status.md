---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1091209'
original_report_id: '1091209'
title: '[h1-2102] Wholesale - CSRF to Generate Invitation Token for a Customer and
  Move Customer to Invited Status'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2021-01-31T13:14:18.813Z'
disclosed_at: '2021-12-06T01:26:09.626Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# [h1-2102] Wholesale - CSRF to Generate Invitation Token for a Customer and Move Customer to Invited Status

## Metadata

- HackerOne Report ID: 1091209
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2021-12-06T01:26:09.626Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
There is a CSRF vulnerability in the Wholesale application to generate an invitation token for a user and move that user to `invited` status.

## Steps To Reproduce:
1. Log in to Shopify and configure Wholesale
2. Add a price list
3. Add a customer with the tag `wholesale`
4. Adjust the pricelist to include the user with the `wholesale` tag
5. At this point you should see the user in the customer section (see figure 1)
6. Now, navigate to `https://poc.rhynorater.com/wholesaleShopify/CSRF.html`
7. Wait 30 seconds (for good measure)
8. Refresh the customer page and note that the user is in the status of `invited`

Figure 1
{F1178635}

## Supporting Material/References:

## Impact

Move customer to `invited` status and generated invite link.

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

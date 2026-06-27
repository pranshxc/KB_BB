---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '837729'
original_report_id: '837729'
title: Session works after logout from Shopify account and password of online store
  is displayed
team_handle: shopify
created_at: '2020-04-03T04:56:50.206Z'
disclosed_at: '2020-04-27T16:09:54.014Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 154
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Session works after logout from Shopify account and password of online store is displayed

## Metadata

- HackerOne Report ID: 837729
- Weakness: 
- Program: shopify
- Disclosed At: 2020-04-27T16:09:54.014Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When a user creates a Shopify Lite Plan account, in the product creation stage when the account has not been upgraded, the store's password is enabled such that any visitor who wants to access the store is required to enter password before being granted access to view the products listed in the online store. 

When a logout request has been made and response has been received/displayed that logout is successful, session still works when
https://unctify.myshopify.com/accounts/passwords is entered in the browser url address bar; the resulting Shopify page displays the password required to enter the store which is supposed to be visible to only the admin and those who have been sent this password.

Please see the PoC attached.

## Impact

Third party can view the listed products and also exploit the user session vulnerability.

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

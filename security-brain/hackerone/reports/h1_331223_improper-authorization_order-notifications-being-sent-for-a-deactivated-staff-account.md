---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '331223'
original_report_id: '331223'
title: Order notifications being sent for a deactivated staff account
weakness: Improper Authorization
team_handle: shopify
created_at: '2018-03-29T21:38:50.768Z'
disclosed_at: '2018-04-12T08:20:21.139Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# Order notifications being sent for a deactivated staff account

## Metadata

- HackerOne Report ID: 331223
- Weakness: Improper Authorization
- Program: shopify
- Disclosed At: 2018-04-12T08:20:21.139Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Steps to reproduce :
-

- Have a staff account with settings permission
- The staff account can go to notifications & add himself so as to get new order notifications
- Now,deactivate the staff account via the admin.
- Create a new order,you shall see that the staff still receives the order notification via email.
- This happens because the account still exists,but if staff deleted , then there is no account,hence no email) so no notification.

## Impact

- Info disclosure about a customer of a store the staff account cant have access to.

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

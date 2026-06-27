---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '240083'
original_report_id: '240083'
title: Updating payout preference to CurrencyCloud doesn't notify user via email
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2017-06-15T04:56:28.889Z'
disclosed_at: '2018-01-31T02:05:10.071Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Updating payout preference to CurrencyCloud doesn't notify user via email

## Metadata

- HackerOne Report ID: 240083
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2018-01-31T02:05:10.071Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When change payment method in user's payments, then a notification about 
Change payment method is sent to the user (email).

However, user not always gets a notification about change payment method - when change payment method via add payout method on Payout Methods, then such a notification is not send to the user (email).

Also,
when user try to change payment method , they were asked to verify the request by entering hackerone password. for the same reason a verification should be there on add payout method.

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

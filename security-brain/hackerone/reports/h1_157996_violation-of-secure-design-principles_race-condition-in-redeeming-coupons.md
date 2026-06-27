---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '157996'
original_report_id: '157996'
title: Race Condition in Redeeming Coupons
weakness: Violation of Secure Design Principles
team_handle: instacart
created_at: '2016-08-09T22:12:20.760Z'
disclosed_at: '2016-09-12T08:40:37.759Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
tags:
- hackerone
- violation-of-secure-design-principles
---

# Race Condition in Redeeming Coupons

## Metadata

- HackerOne Report ID: 157996
- Weakness: Violation of Secure Design Principles
- Program: instacart
- Disclosed At: 2016-09-12T08:40:37.759Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

There exists a race condition in redeeming coupons, allowing a user to redeem the same coupon multiple times, and stacking savings added. This allows for a user to get virtually any discount.

POC:

1. Visit your account and select 'Promo Codes'.
2. Select redeem promo code, and add any promo code. For example, I found the code 'dallas20'.
3. Intercept the request using a proxy, and make the request multiple times, asynchronously.
4. The code will be redeemed multiple times.

For an example, see the screenshot attached.

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

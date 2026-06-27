---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1849626'
original_report_id: '1849626'
title: Fee discounts can be redeemed many times, resulting in unlimited fee-free transactions
weakness: Business Logic Errors
team_handle: stripe
created_at: '2023-01-28T03:16:41.084Z'
disclosed_at: '2023-02-25T01:27:24.869Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 230
asset_identifier: api.stripe.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Fee discounts can be redeemed many times, resulting in unlimited fee-free transactions

## Metadata

- HackerOne Report ID: 1849626
- Weakness: Business Logic Errors
- Program: stripe
- Disclosed At: 2023-02-25T01:27:24.869Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi there, first off, I am an actual Stripe customer using Stripe for my real business, so I used my actual Stripe account to test this (as there is no other way). I realize this is not ideal but hope you understand given the unique scenario!

I was recently offered a fee discount of $20,000 on Stripe transactions. Stripe Support applied the offer to my account, and I was shown a prompt to accept the fee discount in my dashboard. 

I decided I should try and look for a race condition in this acceptance. So, I used Burp Turbo Intruder to race the request that accepts the fee discount, `/ajax/accept_fee_discount_offer` (forgot to take screenshot as I did not think it would work!). 

It seems a race was not even needed though, as I called it 30 times and 30 fee discounts were immediately applied to my account! As a result, I now have $600,000 of fee-free processing applied to my account. Obviously, this is not ideal for Stripe as you only intended to offer me $20,000! I believe you could keep calling this endpoint if you wanted to, you just need a valid `fdo_` ID.

████

## Impact

Unlimited fee-free discounts. This will cost Stripe about 3% of each discount, so $600 each time a $20k discount is abused.

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

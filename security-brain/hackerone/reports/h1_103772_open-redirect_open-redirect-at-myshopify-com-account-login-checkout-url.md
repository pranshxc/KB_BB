---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '103772'
original_report_id: '103772'
title: Open Redirect at *.myshopify.com/account/login?checkout_url=
weakness: Open Redirect
team_handle: shopify
created_at: '2015-12-06T09:51:14.788Z'
disclosed_at: '2015-12-16T04:33:41.881Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- open-redirect
---

# Open Redirect at *.myshopify.com/account/login?checkout_url=

## Metadata

- HackerOne Report ID: 103772
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2015-12-16T04:33:41.881Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Any user after logging into an any myshopify shop can be redirected to other domain.

To reproduce:
Send this to victim: 
http://sehyoginfoshop.myshopify.com/account/login?checkout_url=.np

Now when our victim logs in,
He will be redirected to
https://sehyoginfoshop.myshopify.com.np/

Which is not a shopify domain.

Fix: While redirecting Use <shop-name>"/"$checkout_url instead of <shop-name>$checkout_url

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

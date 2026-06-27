---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '155222'
original_report_id: '155222'
title: (BYPASS) Open Redirect after login at http://ecommerce.shopify.com
weakness: Open Redirect
team_handle: shopify
created_at: '2016-07-30T00:49:24.264Z'
disclosed_at: '2016-09-01T16:00:50.952Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- open-redirect
---

# (BYPASS) Open Redirect after login at http://ecommerce.shopify.com

## Metadata

- HackerOne Report ID: 155222
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2016-09-01T16:00:50.952Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The users can be redirected to some other site which is in control of the attacker from http://ecommerce.shopify.com/accounts

Let's say user is attacker asked victim to login from the here :
https://ecommerce.shopify.com/accounts?return_to=%40evil.com/

When victim enters the password he is redirected to https://evil.com

These can be controlled by the attacker and used in other attacks

Works in all browsers!!

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

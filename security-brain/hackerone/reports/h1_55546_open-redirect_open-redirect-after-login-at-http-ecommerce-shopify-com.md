---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55546'
original_report_id: '55546'
title: Open Redirect after login at http://ecommerce.shopify.com
weakness: Open Redirect
team_handle: shopify
created_at: '2015-04-09T20:00:50.208Z'
disclosed_at: '2015-10-05T18:38:33.749Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- open-redirect
---

# Open Redirect after login at http://ecommerce.shopify.com

## Metadata

- HackerOne Report ID: 55546
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2015-10-05T18:38:33.749Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The users can be redirected to some other site which is in control of the attacker from http://ecommerce.shopify.com/accounts

Let's say user is attacker asked victim to login from the here :
http://ecommerce.shopify.com/accounts?found_email=true&return_to=.mx%2F&user[email]=email@email.com

When victim enters the password he is redirected to http://ecommerce.shopify.com.mx/
This com.mx can be changed to multiple like .es .tw etc

These can be controlled by the attacker and used in other attacks

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

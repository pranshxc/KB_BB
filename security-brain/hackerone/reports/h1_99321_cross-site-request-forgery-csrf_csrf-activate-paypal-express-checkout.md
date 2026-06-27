---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99321'
original_report_id: '99321'
title: '[CSRF] Activate PayPal Express Checkout'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2015-11-12T16:57:37.924Z'
disclosed_at: '2015-12-03T17:26:19.144Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# [CSRF] Activate PayPal Express Checkout

## Metadata

- HackerOne Report ID: 99321
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2015-12-03T17:26:19.144Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , i have found a CSRF issue when activating PayPal Express checkout.
#Steps to reproduce: 
1. Create a new store then login with the admin account.
2. Go to `https://<your_store>.myshopify.com/admin/settings/payments` and you'll see that PayPal Express checkout is already active , so click the edit button and deactivate it.
3. Go to the following link: `https://<your_store>.myshopify.com/admin/payments/complete_paypal_oauth/41` and you'll see that PayPal Express checkout was activated and you'll get a message saying: *Successfully activated your account*.

I have been trying to link a malicious paypal email through this CSRF by using the following link: 
`https://<your_store>.myshopify.com/admin/payments/complete_paypal_oauth/41?verification_token=<PAYPAL_TOKEN>` but it doesn't work.

This issue is a little bit confusing when being reproduced since it will only work on a store in which the admin never tried to activate PayPal before because if he did so , a `request token` will be generated and will be validated for whenever the link is visited.

Please tell me if you are having an issue reproducing it and I will send you a PoC video. 

Thanks.

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

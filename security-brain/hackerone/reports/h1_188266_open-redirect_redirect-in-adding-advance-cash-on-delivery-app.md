---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '188266'
original_report_id: '188266'
title: Redirect in adding advance cash on delivery app
weakness: Open Redirect
team_handle: shopify
created_at: '2016-12-04T19:45:00.205Z'
disclosed_at: '2017-06-27T16:46:55.082Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- open-redirect
---

# Redirect in adding advance cash on delivery app

## Metadata

- HackerOne Report ID: 188266
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2017-06-27T16:46:55.082Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

When you install `Advance Cash on delivery` App in your shop, it takes you to the url 

{F140362}

`https://<YourShop>.myshopify.com/admin/authorize_gateway/1041328?api_key=ceb1a596e2b039d02dfb5772303f6273&return_url=https://cod.shopifyapps.com/gateway_enabled`


{F140363}

Here, `return_url` can be used for redirection.

So if any shop which has this app installed but not yet activated, attacker can just send the above url to the victim by just changing the shop name in the url to the victim's shop name and `return_url` with some malicious url . api_key will remain the same.

`https://<YourShop>.myshopify.com/admin/authorize_gateway/1041328?api_key=ceb1a596e2b039d02dfb5772303f6273&return_url=https://google.com`

#Steps

1. Lets assume a victim Shop with `Advance cash on delivery` app installed but not activated yet

2. Send the url `https://<YourShop>.myshopify.com/admin/authorize_gateway/1041328?api_key=ceb1a596e2b039d02dfb5772303f6273&return_url=https://google.com` to the victim.

3. On click of Activate button, victim will be redirected to `https://google.com`

Thanks & Regards
Ashish

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

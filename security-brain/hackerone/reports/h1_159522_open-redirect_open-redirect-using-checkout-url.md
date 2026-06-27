---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159522'
original_report_id: '159522'
title: Open redirect using checkout_url
weakness: Open Redirect
team_handle: shopify
created_at: '2016-08-15T18:09:01.794Z'
disclosed_at: '2016-09-01T16:55:02.115Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- open-redirect
---

# Open redirect using checkout_url

## Metadata

- HackerOne Report ID: 159522
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2016-09-01T16:55:02.115Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , I would like to report an open redirect issue in `<account>.myshopify.com/account/logout` and `<account>.myshopify.com/account/login`
#Details:
Your application allow redirecting to `https://checkout.shopify.com/` through `https://<shop>.myshopify.com/account/logout?return_url=<url>` 
The page `https://checkout.shopify.com/<Store_id>` will display the 404 page of the store. 

Here is how this can be used for open redirection: 
1. Attacker creates a store then adds a new URL redirect with `/[Store_id]` in the **Old path** field and the malicious website(e.g:evil.com) in the **Redirect to** field.
{F112369}
2. Attacker sends the victim a link like this: 
`https://<victim>.myshopify.com/account/logout?return_url=https://checkout.shopify.com/[Attacker's_store_id] `
3. The victim will be redirected to the malicious website. 

#PoC:
`https://<account>.myshopify.com/account/logout?return_url=https://checkout.shopify.com/14372648`
This will redirect you to evil.com

`https://<account>.myshopify.com/account/login?checkout_url=https://checkout.shopify.com/14372648`
This will redirect you to evil.com after you login. 

Thanks!

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

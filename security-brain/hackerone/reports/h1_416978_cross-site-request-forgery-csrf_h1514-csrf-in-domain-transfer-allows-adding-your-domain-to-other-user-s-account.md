---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '416978'
original_report_id: '416978'
title: H1514 CSRF in Domain transfer allows adding your domain to other user's account
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2018-10-01T17:47:43.255Z'
disclosed_at: '2020-03-30T16:25:16.748Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# H1514 CSRF in Domain transfer allows adding your domain to other user's account

## Metadata

- HackerOne Report ID: 416978
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2020-03-30T16:25:16.748Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Shopify allows users to buy their own domain from the Shopify system. One of the facility on this is that if you buy the domain through Shopify, you can do an inter-store transfers. This means:


> You can only transfer your domain to a Shopify store owned by you. It can take up to 24 hours to complete the transfer.

I ended up finding a CSRF that allows adding my domain to user X's store granted I know their *.myshopify.com.

**Description:**

When you request for a transfer of your domain to another store, an email is sent to you with the transfer link. This link looks like this: 

`https://www.shopify.com/login?redirect=settings/domains/initiate_inter_shop_domain_transfer?transfer_code=6fa6d18a-d2d1-4114-b11e-236b20f81398`

What I realized was that it was asking me to login to my store inorder to transfer the domain. But because this would then redirect to settings/domains and initiate transfer, I decided to check what happens if I change the link to: 

https://victimstore.myshopify.com/admin/settings/domains/initiate_inter_shop_domain_transfer?transfer_code=6fa6d18a-d2d1-4114-b11e-236b20f81398.

After I changed the link, I saved it as a HTML tag: `<img src=https://victimstore.myshopify.com/admin/settings/domains/initiate_inter_shop_domain_transfer?transfer_code=6fa6d18a-d2d1-4114-b11e-236b20f81398>` and saved it as a .html file. Then, I logged into my "victim" store in incognito (no previous login to any shopify store) and opened the HTML. Soon after that the domain was transferred to the victim store. 

The interesting part here is that it copies not just the domain but the DNS data as well. This not only included the MX, A, NS records but email forwarders and custom subdomains that I as an attacker would set prior to transferring. 

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

**Not sure when the transfer link expires so if this does not work, please ping me on Slack**

  1. Edit the attached html and replace YOURSTORE with your myshopify.com domain. You will then realize that going to h1-5142.com will redirect to your store.

## Impact

Domain changes to victim's store. I will look into this more in the coming week to escalate the attack further (possibly to steal store info and payment details).

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

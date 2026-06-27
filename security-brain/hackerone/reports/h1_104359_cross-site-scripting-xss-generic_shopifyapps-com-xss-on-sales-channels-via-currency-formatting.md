---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '104359'
original_report_id: '104359'
title: shopifyapps.com XSS on sales channels via currency formatting
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-12-09T14:29:32.305Z'
disclosed_at: '2015-12-14T19:10:36.696Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# shopifyapps.com XSS on sales channels via currency formatting

## Metadata

- HackerOne Report ID: 104359
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-12-14T19:10:36.696Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

pinterest, twitter, buy button and facebook sales channels vulnerable to xss via currency formatting.

steps to reproduce:
- remove pinterest, twitter, buy button and facebook sales channels at *.myshopify.com/admin/channels
- go to *.myshopify.com/admin/settings/general
- change currency formating as shown at the `currency_formatting.jpg`(check attachment)
- add pinterest, twitter, buy button and facebook sales channels at *.myshopify.com/admin/channels
- check pinterest, twitter and buy button tabs
- create collection and add a product to it (skip this step if you already have collection with product)
- go to facebook tab --> shop  ( `*.myshopify.com/admin/apps/shopify-facebook/collections` )

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

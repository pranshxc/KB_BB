---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1421804'
original_report_id: '1421804'
title: Direct Access To admin Dashboard
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2021-12-09T18:01:10.603Z'
disclosed_at: '2022-01-20T19:15:58.586Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- improper-authentication-generic
---

# Direct Access To admin Dashboard

## Metadata

- HackerOne Report ID: 1421804
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2022-01-20T19:15:58.586Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

* This issue affect two Subdomains, https://data-stories-website.shopifycloud.com/admin.php  `and`  https://datastories.shopify.com/admin.php

## Summary:
Hi Team,
When Link to https://datastories.shopify.com/admin   or  https://data-stories-website.shopifycloud.com/admin the subdomain redirect you to https://shopify.okta.com/login/login.htm?fromURI=/oauth2/v1/authorize/redirect?okta_key=PJl7eQUE9mYSKrtADqQAMe6v3y_SA3iqFtstkVPavAA for OKTA authentication to perform non admins from the Admin dashboard at https://datastories.shopify.com/admin.
But non authentications users still can access the admin dashboard  just by add any extintion to the admin word => https://datastories.shopify.com/admin.php .
When link to https://datastories.shopify.com/admin.php You can see the admin dashboard for the subdomain and the information replaced in.
* You can't discard, edit  or create Globals while you are not authenticated, But you can still see administrative information.
* When You press Ctrl+U you can see parameter called `authenticity_token` which admin csrf_token, This token can used to perform CSRF attack on the site admin **I can't perform for u the CSRF attack now for manu reasons, but accessing this token is critical issue**.

## Steps To Reproduce:

  1. Link to https://datastories.shopify.com/admin.php , and  https://data-stories-website.shopifycloud.com/admin.php

## Impact

Direct access to admin dashboard

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

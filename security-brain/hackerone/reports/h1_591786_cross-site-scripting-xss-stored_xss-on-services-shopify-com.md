---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '591786'
original_report_id: '591786'
title: XSS on services.shopify.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2019-05-28T20:08:24.042Z'
disclosed_at: '2019-06-14T18:39:04.294Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS on services.shopify.com

## Metadata

- HackerOne Report ID: 591786
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2019-06-14T18:39:04.294Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hy security,
 i Got a stored xss in one of your sub-domain "services.shopify.com"

steps:
1- Go to https://(your_store).myshopify.com/admin/apps/experts_marketplace/services_marketplace
2- Then Go to  All services>Marketing and sales>email marketing> Design custom email templates >click select
3- fill al the data, there will be an option for "attach file"
4: selcet a html file where the xss payloads are got stored.
5. write click on the attached file and go to that location, you will see the pop-up

## Impact

can steal cookies

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

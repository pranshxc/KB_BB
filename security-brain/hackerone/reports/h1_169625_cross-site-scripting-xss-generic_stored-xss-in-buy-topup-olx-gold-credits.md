---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '169625'
original_report_id: '169625'
title: Stored XSS in buy topup OLX Gold Credits
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-09-15T18:37:14.375Z'
disclosed_at: '2017-07-30T12:36:31.451Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in buy topup OLX Gold Credits

## Metadata

- HackerOne Report ID: 169625
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2017-07-30T12:36:31.451Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

in this link: https://www.olx.ph/payment/wallet/topupaccount/

1.input in 2) name: " onfocus=prompt(1) autofocus bad="
2.Select a payment
3.tick I accept OLX's Terms and Conditions
4.Click Continue

Then go back to this page (https://www.olx.ph/payment/wallet/topupaccount/), XSS :)

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

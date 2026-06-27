---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '20221'
original_report_id: '20221'
title: Cross Site Scripting (Stored)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: expressionengine
created_at: '2014-07-16T12:24:28.962Z'
disclosed_at: '2014-09-30T04:45:26.470Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross Site Scripting (Stored)

## Metadata

- HackerOne Report ID: 20221
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: expressionengine
- Disclosed At: 2014-09-30T04:45:26.470Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Occurred in the URL : https://store.ellislab.com/billing
After adding a product to the cart proceed to add the billing and card information and in the card fields give your card details respectively and in the fields 
1. First name
2. Last name
3. Street Address
4. Apt/Suite/#
5. City. 

Give the following payload : "><img src=x onerror=prompt(0);> and click on Place Order and there it goes 5 stored XSS will appear

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

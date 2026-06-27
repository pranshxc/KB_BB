---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1420697'
original_report_id: '1420697'
title: '[app.lemlist.com] Improper handling of payment lead to bypass payment'
weakness: Business Logic Errors
team_handle: lemlist
created_at: '2021-12-09T00:18:16.799Z'
disclosed_at: '2022-05-17T08:54:42.188Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: app.lemlist.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# [app.lemlist.com] Improper handling of payment lead to bypass payment

## Metadata

- HackerOne Report ID: 1420697
- Weakness: Business Logic Errors
- Program: lemlist
- Disclosed At: 2022-05-17T08:54:42.188Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello Team,
I truly hope it treats you awesomely on your side of the screen :)

due to improper handling of payment methods, an attacker can easily bypass the payment and benefit from a paid plan.

## Steps To Reproduce:

1. Log to your account
1. Go to the billing page
1. Fill in the address tab
1. Go to the next tab `Payment Card` 
1. ==Now the interesting step Make sure you don't have any money on your credit card==
1.  Chose `Email outreach` and wait until you get a notification that the payment is failed
1.  Next  increase the number of seats for example 50 
1. Again you will get a notification that the payment is failed
1. Now Cancel the subscription
1. Now I can use the paid features without paying anything.

# POC
{{F1538593}}

## Impact

I think the impact is pretty obvious, an attacker can use paid plans without paying anything.

if you need more info feel free to ping me 

best Regards
@omarelfarsaoui

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

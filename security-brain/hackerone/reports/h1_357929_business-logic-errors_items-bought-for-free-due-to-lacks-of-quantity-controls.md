---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '357929'
original_report_id: '357929'
title: Items bought for free due to lacks of quantity controls
weakness: Business Logic Errors
team_handle: reverb
created_at: '2018-05-26T17:13:59.486Z'
disclosed_at: '2018-08-31T12:43:21.141Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
asset_identifier: sandbox.reverb.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Items bought for free due to lacks of quantity controls

## Metadata

- HackerOne Report ID: 357929
- Weakness: Business Logic Errors
- Program: reverb
- Disclosed At: 2018-08-31T12:43:21.141Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The server fails to check the quantity of the items that are going to be sell. Values <= 0 are accepted as 1.

PoC:

Go here
https://sandbox.reverb.com/fr/item/139897-fender-2-strap-leather-test-2018-leather

Intercept the response after clicking "Add to cart" and put "quantity: 0"

{F302179}

Proceed to checkout

{F302180}

Place order

{F302181}

{F302182}

I used one of the fake credit cards you provide us.

## Impact

Items are sold gratis

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

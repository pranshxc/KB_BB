---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '927661'
original_report_id: '927661'
title: Ability to manipulate price with a max threshold of `<1 Rupee` in support rider
  parameter
weakness: Violation of Secure Design Principles
team_handle: zomato
created_at: '2020-07-20T08:28:26.210Z'
disclosed_at: '2020-08-08T07:36:50.195Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Ability to manipulate price with a max threshold of `<1 Rupee` in support rider parameter

## Metadata

- HackerOne Report ID: 927661
- Weakness: Violation of Secure Design Principles
- Program: zomato
- Disclosed At: 2020-08-08T07:36:50.195Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team

I have found an issue in support rider amount calculation at the time of checkout where the amount is tamperable by negative fraction of rupees which makes the total amount decreased by maximum of 1rs.

POC - 

1-Goto - zomato.com
2 - Add anything to your cart
3- At the checkout page , Add some money to Support Riders , click on any 25,50,100
4- Intercept the request of adding support rider money.
5- Change the price of Support Rider to " -0.99" in both fields of donation money.
6- Forward the request , the Cart value will change.
7- Pay by any platform, order will get placed.


Thanks

## Impact

Price Manipulation in Support Rider

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

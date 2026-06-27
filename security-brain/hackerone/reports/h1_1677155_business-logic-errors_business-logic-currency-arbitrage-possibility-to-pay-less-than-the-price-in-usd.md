---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1677155'
original_report_id: '1677155'
title: Business Logic, currency arbitrage - Possibility to pay less than the price
  in USD
weakness: Business Logic Errors
team_handle: portswigger
created_at: '2022-08-22T22:05:27.379Z'
disclosed_at: '2022-10-26T06:57:05.992Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 9
asset_identifier: portswigger.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Business Logic, currency arbitrage - Possibility to pay less than the price in USD

## Metadata

- HackerOne Report ID: 1677155
- Weakness: Business Logic Errors
- Program: portswigger
- Disclosed At: 2022-10-26T06:57:05.992Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Currency fluctuate all the time. Theses days EUR / USD key pair is around 1for1. It was even 1:0.99 when I was writing this report.
Portswigger doesn't change dynamically the price and exchange rate dynamically. 

Vulnerability at the following link: https://portswigger.net/buy/pro 

When you want to buy a product choose the currency, you can noticed they are fixed and with today difference it's quite a big difference.

## Impact

USD price is 399$USD, while EUR price is 349$. 
Therefore someone could just change the price to Euro and pay 347 $USD (349 Euro) instead of 399$(with current rate).

PS: It scale with the price, it could lead to thousands of dollars lost for your company.

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

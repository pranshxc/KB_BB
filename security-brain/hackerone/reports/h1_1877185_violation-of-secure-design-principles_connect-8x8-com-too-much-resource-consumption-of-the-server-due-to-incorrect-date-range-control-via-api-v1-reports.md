---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1877185'
original_report_id: '1877185'
title: 'connect.8x8.com: Too much resource consumption of the server due to incorrect
  date range control via /api/v1/reports?dateFrom='
weakness: Violation of Secure Design Principles
team_handle: 8x8-bounty
created_at: '2023-02-16T23:11:54.437Z'
disclosed_at: '2023-06-26T20:27:28.838Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: connect.8x8.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# connect.8x8.com: Too much resource consumption of the server due to incorrect date range control via /api/v1/reports?dateFrom=

## Metadata

- HackerOne Report ID: 1877185
- Weakness: Violation of Secure Design Principles
- Program: 8x8-bounty
- Disclosed At: 2023-06-26T20:27:28.838Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi Team, When we enter the date range in the reporting endpoint, we see this in the response. When we increase the date range, the byte returned by the server increases. By repeating this over and over, we can cause the server to consume too many resources. As a result, the server may crash.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. First we must be logged in and go to https://connect.8x8.com/messaging/reports
  2. We can see this request when we look at burp requests 
https://connect.8x8.com/api/v1/reports?dateFrom=2023-02-10&dateTo=2023-02-17&tzName=Europe%2FIstanbul&tz=(UTC%2B03%3A00)&tzOffset=180&timeInterval=1440
  3.  the server will respond late as you increase the date range and the response size will increase a lot {F2178902} {F2178901}

## Remediation
Date range control can be added.

## Impact

Potential Dos...

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

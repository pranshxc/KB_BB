---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1566017'
original_report_id: '1566017'
title: Race condition on https://judge.me/people
weakness: Concurrent Execution using Shared Resource with Improper Synchronization
  ('Race Condition')
team_handle: judgeme
created_at: '2022-05-11T14:32:05.746Z'
disclosed_at: '2022-08-01T05:28:05.901Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- concurrent-execution-using-shared-resource-with-improper-synchronization-race-condition
---

# Race condition on https://judge.me/people

## Metadata

- HackerOne Report ID: 1566017
- Weakness: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
- Program: judgeme
- Disclosed At: 2022-08-01T05:28:05.901Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##summary:An attacker can increase the followers of  the users of judge.me

Tools required : 
1.burpsuit
2.turbo intruder

##steps to reproduce:
1.visit https://judge.me/people
2.like a user and intercept the request
3.now  send it to turbo intruder and configure the script to 
     race.py

## Impact

The attacker can increase their followers in a bad way by creating fake followers

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

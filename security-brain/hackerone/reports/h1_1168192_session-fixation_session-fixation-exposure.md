---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1168192'
original_report_id: '1168192'
title: Session Fixation Exposure
weakness: Session Fixation
team_handle: versa-networks
created_at: '2018-07-12T00:00:00.000Z'
disclosed_at: '2021-05-05T20:20:38.170Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- session-fixation
---

# Session Fixation Exposure

## Metadata

- HackerOne Report ID: 1168192
- Weakness: Session Fixation
- Program: versa-networks
- Disclosed At: 2021-05-05T20:20:38.170Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In VOS user session identifier (authentication token) is issued to the browser prior to authentication but is not changed after the user successfully logs into the application. Failing to issue a new session ID following a successful login introduces the possibility for an attacker to set up a trap session on the device the victim is likely to login with.

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

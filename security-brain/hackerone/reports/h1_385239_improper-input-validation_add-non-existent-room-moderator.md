---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '385239'
original_report_id: '385239'
title: Add non-existent room moderator
weakness: Improper Input Validation
team_handle: chaturbate
created_at: '2018-07-22T20:48:19.768Z'
disclosed_at: '2018-10-19T22:09:10.778Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# Add non-existent room moderator

## Metadata

- HackerOne Report ID: 385239
- Weakness: Improper Input Validation
- Program: chaturbate
- Disclosed At: 2018-10-19T22:09:10.778Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
A broadcaster can add or remove a non-existent user as a moderator.  This is submitted using the testbed as it wasn't possible to initiate a broadcast on the production site.  

Steps
1. As a broadcaster add a moderator to the broadcast (attachment 1).
2. Observe the request sent to the server (attachment 2).
3. Replay the request from step 2.  Change the second to last part of the URL to a non-existent user (attachment 3).
4. Observe the server broadcasts the operation to the room  (attachment 4).

## Impact

It is unclear what side effects, if any, this could have.  This is really being reported because the application had very strict access controls and this seems to one of the only places it was obvious the access controls and input validation weren't as strict as they could be.

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

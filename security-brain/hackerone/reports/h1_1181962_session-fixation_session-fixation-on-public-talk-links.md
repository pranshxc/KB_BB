---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1181962'
original_report_id: '1181962'
title: Session fixation on public talk links
weakness: Session Fixation
team_handle: nextcloud
created_at: '2021-05-01T14:18:01.780Z'
disclosed_at: '2021-06-16T08:40:00.261Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: nextcloud/spreed
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- session-fixation
---

# Session fixation on public talk links

## Metadata

- HackerOne Report ID: 1181962
- Weakness: Session Fixation
- Program: nextcloud
- Disclosed At: 2021-06-16T08:40:00.261Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. userA shares a talk room and protects it with a password
2. userB opens links but doesn't enter the password yet
3. Attacker steals the cookies from userB
4. userB logs in
5. attacker is now also able to read the conversation etc

## Impact

In short the attacker is able to take over the session of the guest userB on this talk room.

The session id should be renewed once the password is entered.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '277213'
original_report_id: '277213'
title: Two accounts can be made with same password
team_handle: legalrobot
created_at: '2017-10-14T15:01:52.479Z'
disclosed_at: '2017-10-20T08:18:00.109Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: www.legalrobot.com
asset_type: URL
max_severity: medium
tags:
- hackerone
---

# Two accounts can be made with same password

## Metadata

- HackerOne Report ID: 277213
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-10-20T08:18:00.109Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

A really nice bug to look into i found this while i was making my own account as i was testing for some serious bug i decided to just look into that how Legal Robot behaves when two account are made with the same password.

Hacker Scenario: Person1 makes a account with a password called password now person2 too makes his password called password [we ca see that the both user made their password the same] the person2 acts as attacker and tries different emails using his password using some tools luckily he/she finds out that there is another email whose password is same, He/she logs into it and do whatever he/she wants to do and Person1(Victim) won't know. Sorry but i doon't know how to name this weakness 

See the PoC video:

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

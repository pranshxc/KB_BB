---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '412526'
original_report_id: '412526'
title: No rate limit in stats api token endpoint
weakness: Improper Restriction of Authentication Attempts
team_handle: chaturbate
created_at: '2018-09-21T17:44:18.120Z'
disclosed_at: '2018-10-19T17:41:22.424Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# No rate limit in stats api token endpoint

## Metadata

- HackerOne Report ID: 412526
- Weakness: Improper Restriction of Authentication Attempts
- Program: chaturbate
- Disclosed At: 2018-10-19T17:41:22.424Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Brute force on statsapi endpoint to view stats of an user##


## Steps To Reproduce:

  1.  Stats api token can be generated at https://chaturbate.com/statsapi/authtoken/
https://chaturbate.com/statsapi/?username=hackeronetestchat&token=**vulnerable**

 I've used my profile and and my token to check brute force

The  correct token returned with 200 ok status

## Impact

An attacker could view the stats of an user

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

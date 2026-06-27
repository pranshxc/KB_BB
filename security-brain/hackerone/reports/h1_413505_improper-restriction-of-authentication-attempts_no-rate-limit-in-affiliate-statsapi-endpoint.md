---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '413505'
original_report_id: '413505'
title: No rate limit in affiliate statsapi endpoint
weakness: Improper Restriction of Authentication Attempts
team_handle: chaturbate
created_at: '2018-09-24T19:11:43.656Z'
disclosed_at: '2018-10-19T17:41:26.170Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# No rate limit in affiliate statsapi endpoint

## Metadata

- HackerOne Report ID: 413505
- Weakness: Improper Restriction of Authentication Attempts
- Program: chaturbate
- Disclosed At: 2018-10-19T17:41:26.170Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Brute force at affiliate statsapi##


## Steps To Reproduce:

  1. The affiliate stats api link is vulnerable to brute force

 https:// chaturbate.com/affiliates/apistats/?username=hackeronetestchat&token=**vulnerable**
I've used my profile and and my token to check brute force

The correct token returned with 200 ok status

## Impact

An attacker could view the  affiliates stats of an user

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

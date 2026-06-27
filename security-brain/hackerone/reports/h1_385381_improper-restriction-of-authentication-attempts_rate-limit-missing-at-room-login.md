---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '385381'
original_report_id: '385381'
title: Rate limit missing at room login
weakness: Improper Restriction of Authentication Attempts
team_handle: chaturbate
created_at: '2018-07-23T12:48:31.761Z'
disclosed_at: '2018-09-30T07:42:38.524Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Rate limit missing at room login

## Metadata

- HackerOne Report ID: 385381
- Weakness: Improper Restriction of Authentication Attempts
- Program: chaturbate
- Disclosed At: 2018-09-30T07:42:38.524Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello there,

User are able to protect there broadcasting with password, so only password granted visitor can login to broadcast room. I notice that rate limit are missing at the endpoint `/roomlogin/user/` which enable me to brute force on password field.

I made 1k+ request but still server not block my request.

##Steps to reproduce:-

1. Create two account A and B. protect A's room with password.
2. Login to B's account and access A's room with random password.
3. Send the request to intruder and run till you get right password

  *  {F323575}

## Impact

Attacker are able to access some one private room.

***Thanks!***

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

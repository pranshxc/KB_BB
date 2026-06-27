---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1879549'
original_report_id: '1879549'
title: Basic auth header on WebDAV requests is not bruteforce protected
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2023-02-20T11:47:15.231Z'
disclosed_at: '2023-06-02T04:18:38.749Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 49
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Basic auth header on WebDAV requests is not bruteforce protected

## Metadata

- HackerOne Report ID: 1879549
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2023-06-02T04:18:38.749Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I hope you are doing well.

Vulnerability Name :- Basic Authentication Bypass due to Lack of Rate Limit

Vulnerable URL :- https://efss.qloud.my/remote.php/dav/calendars/ha.ckitbharat3@gmail.com/app-generated--deck--board-5269/

Steps to Reproduce :- 1. Login --> Go to Tasks.
2. Copy private Link.
3. It looks like :- https://efss.qloud.my/remote.php/dav/calendars/ha.ckitbharat3@gmail.com/app-generated--deck--board-5269/
4. Open it in other browser .
5. It asks for username and password .
6. Username/email is in URL , enter same and for password enter random password.
7. Capture this request in burp suite.
8. There is an Auth header --> copy there value and see it's b64 encoded --> decode it --> create payloads of password and encode it as b64.
9. Send to intruder and select that position and paste the payload list.
10. Click on start attack and Boom! after few mins it got bypassed with Response code 200.

## Impact

1. Basic Authentication Bypass.
2. Full Account takeover because attacker can easily know the password through here because of brute forcing as no rate limit is there.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1179232'
original_report_id: '1179232'
title: Able to blocking users with 2fa from login into their accounts by just knowing
  the SteamID
weakness: Reliance on Cookies without Validation and Integrity Checking in a Security
  Decision
team_handle: cs_money
created_at: '2021-04-29T02:30:16.882Z'
disclosed_at: '2023-12-14T18:55:58.977Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 53
asset_identifier: cs.money
asset_type: URL
max_severity: critical
tags:
- hackerone
- reliance-on-cookies-without-validation-and-integrity-checking-in-a-security-decision
---

# Able to blocking users with 2fa from login into their accounts by just knowing the SteamID

## Metadata

- HackerOne Report ID: 1179232
- Weakness: Reliance on Cookies without Validation and Integrity Checking in a Security Decision
- Program: cs_money
- Disclosed At: 2023-12-14T18:55:58.977Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, team!

## Summary:
By changing the steamID cookie on confirm 2fa code request, I am able to block the login of an account with 2fa for 5 minutes (300 seconds).
So I am able to block users with 2fa from login into their accounts by just knowing the SteamID.

## Steps To Reproduce:

  1. Login into your account with 2fa. 
1. Get the request to confirm the 2fa code.

{F1282394}


```http
POST /login/confirm HTTP/1.1
Host: cs.money
Content-Length: 28
Connection: close
Cookie: steamid=<victim_steam_id>;

{"token":"foo","code":"foo"}
```

2. Change the cookie steamid to the victim one.
3. Repeat the request 4 times (4 wrong codes).

-------

█████

## Impact

I hacker could block everyone with 2fa from login into cs.money.

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

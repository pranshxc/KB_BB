---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1392287'
original_report_id: '1392287'
title: No-Rate limit of current password on delete account endpoint(https://www.xvideos.com/account/close)
team_handle: xvideos
created_at: '2021-11-05T11:02:31.899Z'
disclosed_at: '2021-11-23T11:02:21.168Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 63
asset_identifier: www.xvideos.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# No-Rate limit of current password on delete account endpoint(https://www.xvideos.com/account/close)

## Metadata

- HackerOne Report ID: 1392287
- Weakness: 
- Program: xvideos
- Disclosed At: 2021-11-23T11:02:21.168Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team!!!
This Attack happen when victim login in other device and forget to logout ,Then attacker can delete  it's account by brute force the current password because current password has no-rate limit.
After guessing current password attacker can easily delete the victim account.
Steps To Reproduce:
1.Login in https://www.xvideos.com/ with right credentials
2.Navigate to Dashboard --> Account->  Delete my account and Personal Data
3.add random password in current password field 
4.Capture the request and send it for fuzz
you get a different response when you enter a right password.

****  Response in right password :-
            Too fast. Please try again in few seconds

           Response of wrong password :-
          Too fast. Please try again in few seconds is missing.

POC - I have attached a video poc in which I demonstrate the attack.

## Impact

As Attacker I can delete victim account by brute force the victim current password, Due to no-rate limit on this endpoint.

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

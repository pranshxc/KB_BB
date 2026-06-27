---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1842114'
original_report_id: '1842114'
title: Missing brute force protection on password confirmation modal
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2023-01-20T16:45:21.320Z'
disclosed_at: '2023-03-21T13:46:57.708Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Missing brute force protection on password confirmation modal

## Metadata

- HackerOne Report ID: 1842114
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2023-03-21T13:46:57.708Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I hope you are doing well.

I found a vulnerability in Next cloud , let's exploit

I am not reporting this for every feature in different different report , please increase the severity in single Report. 

Vulnerability Name :- Lack of Rate limit While Generating Backup code , Deleting Account , Profile Updating

Vulnerability Description :- Hi Team , there is no rate limit while sending request to  Generating Backup code , Deleting Account , Profile Updating endpoint that leads to bypass the password protection and even attacker can view current password of user.

Steps to Reproduce :- 1. Signup with an provider and verify your account.
2. Once verified --> Go to Settings --> Security.
3. Click on Generate Backup code , enable password less authentication , Update Profile  it asks for password for authentication.
4. Enter Random Password --> Capture this request n burp suite.
5. Sent this to intruder and select password position and select Payload type as Brute Force.
6. Click on Attack.
7. Boom! On correct password you got response 200 ok and for incorrect you got 403 Forbidden.

Reference Report Next cloud team resolved previously :- #1596673

## Impact

Password protected Authentication Bypass.
2. Attacker able to know the user current password in cleartext and able to takeover the account if they are at same place or someone forgot to logout from public PC also.

POC Attached

If you need further info I am here to help you.
Thanks and Regards,
BhaRat

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

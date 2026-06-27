---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1894653'
original_report_id: '1894653'
title: Missing brute force protection for passwords of password protected share links
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2023-03-07T04:33:46.798Z'
disclosed_at: '2023-04-25T09:32:28.295Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Missing brute force protection for passwords of password protected share links

## Metadata

- HackerOne Report ID: 1894653
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2023-04-25T09:32:28.295Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I hope you are doing well.

Vulnerability Name :- Bypass Password of Shared Files due to Lack of Rate Limit

Vulnerability Description :- Hi Team, I found a vulnerability in which I am able to bypass password protection of shared files due to lack of Rate limit.

Vulnerable URL :- https://efss.qloud.my/index.php/s/7ARMkjXJXAEz2kr

Steps to Reproduce :- 1. Login --> Go to Files --> Set Password.
2. Copy Shared Link.
3. It looks like :- https://efss.qloud.my/index.php/s/7ARMkjXJXAEz2kr
4. Open it in other browser .
5. It asks for password .
6. Enter random password.
7. Capture this request in burp suite.
8. Send to intruder and select that position and paste the payload list.
10. Click on start attack and Boom! after few mins it got bypassed with Response code 303.

## Impact

It leads to bypass the password of protected share files.

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

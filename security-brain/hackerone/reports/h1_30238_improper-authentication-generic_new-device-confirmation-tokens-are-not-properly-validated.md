---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '30238'
original_report_id: '30238'
title: New Device confirmation tokens are not properly validated.
weakness: Improper Authentication - Generic
team_handle: coinbase
created_at: '2014-10-06T19:06:07.299Z'
disclosed_at: '2015-05-25T18:36:59.890Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# New Device confirmation tokens are not properly validated.

## Metadata

- HackerOne Report ID: 30238
- Weakness: Improper Authentication - Generic
- Program: coinbase
- Disclosed At: 2015-05-25T18:36:59.890Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, team
I noticed that the new device confirmation code sent by your server is not validated .
POC:
1) Login to a new computer and ask for confirmation code two times.
Say around at 12.00 PM and at 12.01 PM
2) Now verify the device with the confirmation token which arrived at 12.01 PM
and after doing your work
go to https://www.coinbase.com/settings/security_settings
and remove that device .
say around 12.30 PM
3) Now you need to confirm the device once again and your server will send the new device confirmation code to user's email address at 12.30 PM
4) Here this time  use the confirmation code which arrived at 12.00 PM and u can see that , your device is confirmed.

Fix:
Invalidate all the previous confirmation tokens as soon as new token is generated.

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

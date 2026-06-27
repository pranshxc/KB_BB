---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159202'
original_report_id: '159202'
title: Full Account Takeover
weakness: Improper Authentication - Generic
team_handle: olx
created_at: '2016-08-14T08:43:10.866Z'
disclosed_at: '2016-09-17T15:29:29.856Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- improper-authentication-generic
---

# Full Account Takeover

## Metadata

- HackerOne Report ID: 159202
- Weakness: Improper Authentication - Generic
- Program: olx
- Disclosed At: 2016-09-17T15:29:29.856Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

[Issue resolved by the OLX support , at the time of discovery of bug , olx.in was not in scope]

Whenever a user wants to login through the mobile app , the user enters his mobile number and then he is presented with a screen to enter the OTP . The problem is that there is no rate limiting on the number of attempts , since the OTP is only 4 digits long , all the combinations can be tried in a very short span of time hence anyone can login in anyone's account by typing victim's mobile number and trying all OTPs.

Here is the original video and PDF i sent to the OLX Support.
https://youtu.be/ds8dOFt_8s4

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1060541'
original_report_id: '1060541'
title: No rate limit lead to otp brute forcing
weakness: Improper Restriction of Authentication Attempts
team_handle: mtn_group
created_at: '2020-12-17T00:00:13.361Z'
disclosed_at: '2021-08-16T19:57:01.452Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# No rate limit lead to otp brute forcing

## Metadata

- HackerOne Report ID: 1060541
- Weakness: Improper Restriction of Authentication Attempts
- Program: mtn_group
- Disclosed At: 2021-08-16T19:57:01.452Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello.
There is no rate limit protection in the endpoint https://mtnonline.com/nim/submit , Which could lead to brute force otp code.

## How To Reproduce:
Visit https://mtnonline.com/nim and complete all the required field and submit.
when next page load, user will be ask otp code.
Enter any five digit number and intercept the request using burp suit.
Send the request to intruder and clear all the payload except for otp.
Select brute forcer in payload type and clear the alphabetic character in character set and leave only digit.
In the min. length and max. length enter 5.
Click on attact button.

In the attached image, all the response code where  303 which means see other, that is means try again.
If rate limit is working, from 3 to 4 request, their response should be 429 means too many request.

## Supporting Material/References:

  * [attachment / reference]


##Thanks

## Impact

Attacker can send unlimited request before code the code to expire and guess the correct otp since it can be 5 minutes to expire.

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

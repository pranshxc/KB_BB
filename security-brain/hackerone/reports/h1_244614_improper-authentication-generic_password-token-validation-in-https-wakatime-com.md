---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244614'
original_report_id: '244614'
title: Password token validation in https://wakatime.com/
weakness: Improper Authentication - Generic
team_handle: wakatime
created_at: '2017-06-30T03:11:56.800Z'
disclosed_at: '2017-07-24T02:38:16.440Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# Password token validation in https://wakatime.com/

## Metadata

- HackerOne Report ID: 244614
- Weakness: Improper Authentication - Generic
- Program: wakatime
- Disclosed At: 2017-07-24T02:38:16.440Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

I noticed that when requesting multiple reset links at https://wakatime.com/reset_password/ all tokens are valid and can be used.

In numerous applications the following policy is adopted as an additional security measure:

keep valid only that token with shorter lifetime (last requested)
or

invalidate all reset links generated after successful use of one of these tokens
Please check it.

Steps to reproduce:
1.Go to password reset page and request two times for pass reset token
2.Then go to your email and visit first pass reset link
3.Then you will realize that it is not getting expired .

Browser/OS: 
Chroem latest linux

Attack scenario:
There is not a immediate thereat to this but it is implemented for best practice and for secure design principle.

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

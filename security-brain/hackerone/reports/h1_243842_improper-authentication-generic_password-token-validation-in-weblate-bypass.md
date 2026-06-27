---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '243842'
original_report_id: '243842'
title: Password token validation in Weblate Bypass
weakness: Improper Authentication - Generic
team_handle: weblate
created_at: '2017-06-27T21:10:31.715Z'
disclosed_at: '2017-08-21T17:39:12.452Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# Password token validation in Weblate Bypass

## Metadata

- HackerOne Report ID: 243842
- Weakness: Improper Authentication - Generic
- Program: weblate
- Disclosed At: 2017-08-21T17:39:12.452Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

This is a bypass of the fix on #229987. I could confirm that old link still works. Though you would need to use 2 browsers to pull this off

##Reproduction Steps
1. In Browser1, request a password reset
- Load link sent to your email in the same browser 
- Request another password reset in Browser2
- Load link sent to your email in the same browser 
- Change the password on Browser2
- Successful :D
- Change the password on Browser1
- Success :D
- Now login in any of the password with the last password.

Shuaib.

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

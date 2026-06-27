---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17383'
original_report_id: '17383'
title: Category- Broken Authentication and Session Management (leads to account compromise
  if some conditions are met)
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2014-06-23T19:33:37.309Z'
disclosed_at: '2014-07-26T07:34:59.979Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- improper-authentication-generic
---

# Category- Broken Authentication and Session Management (leads to account compromise if some conditions are met)

## Metadata

- HackerOne Report ID: 17383
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2014-07-26T07:34:59.979Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Hope you are good!

Steps to repro:
1) Create a HackerOne account having email address "a@x.com".
2) Now Logout and ask for password reset link. Don't use the password reset link.
3) Login using the same password back and update your email address to "b@x.com" and verify the same.
4) Now logout and use the password reset link which was mailed to "a@x.com" in step 2.
5) Password will be changed.

All previous password reset links should automatically expire once a user changes his email address.
Please let me know if this can be fixed.

Best Regards
Anand Prakash

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

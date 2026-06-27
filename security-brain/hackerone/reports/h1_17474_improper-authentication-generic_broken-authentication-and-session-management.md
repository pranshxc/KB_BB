---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17474'
original_report_id: '17474'
title: Broken Authentication and Session Management
weakness: Improper Authentication - Generic
team_handle: phabricator
created_at: '2014-06-24T16:46:28.892Z'
disclosed_at: '2014-08-05T05:37:48.223Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- improper-authentication-generic
---

# Broken Authentication and Session Management

## Metadata

- HackerOne Report ID: 17474
- Weakness: Improper Authentication - Generic
- Program: phabricator
- Disclosed At: 2014-08-05T05:37:48.223Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Hope you are good!

Steps to repro:
1) Create a Phabricator account having email address "a@x.com".
2) Now Logout and ask for password reset link. Don't use the password reset link sent to your mail address.
3) Login using the same password back and update your email address to "b@x.com" and verify the same. Remove "a@x.com".
4) Now logout and use the password reset link which was mailed to "a@x.com" in step 2.
5) Password will be changed.

All previous password reset links should automatically expire once a user changes his email address.
Please fix this.

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

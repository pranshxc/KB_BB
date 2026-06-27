---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '23579'
original_report_id: '23579'
title: Broken Authentication and Session Management
weakness: Improper Authentication - Generic
team_handle: secret
created_at: '2014-08-11T11:05:48.890Z'
disclosed_at: '2014-11-17T14:30:48.057Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# Broken Authentication and Session Management

## Metadata

- HackerOne Report ID: 23579
- Weakness: Improper Authentication - Generic
- Program: secret
- Disclosed At: 2014-11-17T14:30:48.057Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Hope you are good!

Steps to Reproduce:
1) Create a Secret account having email address "a@email.com".
2) Now Logout and ask for password reset link. Don't use the password reset link.
3) Login using the same password back and update your email address to "b@email.com" and verify the same.
4) Now logout and use the password reset link which was mailed to "a@email.com" in step 2.
5) Password will be changed.

All previous password reset links should automatically expire once a user changes his email address.
Please let me know if this can be fixed.

Best Regards,
Vinoth Kumar J

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

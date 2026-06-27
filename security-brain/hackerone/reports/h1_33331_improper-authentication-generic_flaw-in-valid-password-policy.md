---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '33331'
original_report_id: '33331'
title: Flaw in valid password policy.
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2014-10-30T18:02:58.969Z'
disclosed_at: '2014-11-30T23:06:50.928Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Flaw in valid password policy.

## Metadata

- HackerOne Report ID: 33331
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2014-11-30T23:06:50.928Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Steps to reproduce**
1. Go to twitter.com
2. Login with your existing password
3. Change your password from settings.Make 6 space character as your password.
4. After successful update of your password,logout from twitter.com
5. Now login from mobile.twitter.com with existing password (which is 6 or more or less space characters)
6. Now go to settings.
7. Try to update your password.
8. Every time you you request for update,it will say password can't be blank.So you will never be able to update your password from mobile.twitter.com again.

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

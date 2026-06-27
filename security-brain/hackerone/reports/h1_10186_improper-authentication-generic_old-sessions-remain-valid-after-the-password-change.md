---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '10186'
original_report_id: '10186'
title: Old Sessions remain valid after the password change.
weakness: Improper Authentication - Generic
team_handle: relateiq
created_at: '2014-04-28T20:40:51.532Z'
disclosed_at: '2014-06-11T08:54:02.327Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Old Sessions remain valid after the password change.

## Metadata

- HackerOne Report ID: 10186
- Weakness: Improper Authentication - Generic
- Program: relateiq
- Disclosed At: 2014-06-11T08:54:02.327Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Industry Standard Procedure**
When the password is changed or email address has been updated for any particular account,all the sessions which were active with the old password/email should be destroyed.
**Reason**
If somehow anybody hacked into your account and you understand that someone has trespassed into your account,then what will you do?You will change your password to secure your account.But in relateIQ changing the password doesnot destroys the other sessions which are logged in with old passwords.So,your account remains insecure even after the changing of password.

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

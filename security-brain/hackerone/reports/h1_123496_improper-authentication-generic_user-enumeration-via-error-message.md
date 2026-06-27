---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123496'
original_report_id: '123496'
title: User enumeration via error message
weakness: Improper Authentication - Generic
team_handle: veris
created_at: '2016-03-16T00:07:44.409Z'
disclosed_at: '2016-03-18T05:59:17.177Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# User enumeration via error message

## Metadata

- HackerOne Report ID: 123496
- Weakness: Improper Authentication - Generic
- Program: veris
- Disclosed At: 2016-03-18T05:59:17.177Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi guys,

Well, the issue is in authentication process, an attacker able to enumerate registered users on the site via brute forcing the login page, in case when ***user is not exist***, system returns the following error message: "User not exist", in case when ***user exist***, but incorrect password: "Password does not match".

Mitigation: handle the above situation correctly, e.g.: "Login failed. Invalid user ID or password". This doesn't inform the attacker on which credential is wrong and make enumeration more difficult

Thanks

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

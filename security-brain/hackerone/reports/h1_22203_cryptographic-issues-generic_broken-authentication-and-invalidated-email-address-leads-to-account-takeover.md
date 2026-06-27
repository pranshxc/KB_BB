---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '22203'
original_report_id: '22203'
title: Broken authentication and invalidated email address leads to account takeover
weakness: Cryptographic Issues - Generic
team_handle: x
created_at: '2014-08-03T14:46:13.932Z'
disclosed_at: '2014-11-28T23:15:20.750Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
tags:
- hackerone
- cryptographic-issues-generic
---

# Broken authentication and invalidated email address leads to account takeover

## Metadata

- HackerOne Report ID: 22203
- Weakness: Cryptographic Issues - Generic
- Program: x
- Disclosed At: 2014-11-28T23:15:20.750Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi, team.
I found a bug in twitter.com
Description and POC:
1) Create a twitter account having email address "abcd@x.com".
2) Now Logout and ask for password reset link. Don't use the password reset link.
3) Login using the same password back and update your email address to "efgh@x.com" and verify the same.
4) Now logout and use the password reset link which was mailed to "abcd@x.com" in step 2.
5) You can see that it is possible to change the password.
Here  the password reset link of "abcd@x.com" which was old email address associated with twitter can be use to change the password of twitter account having  updated email address "efgh@x.com".

Attack scenario:
If victim's previous "abcd@x.com" account was compromised, he decided to updated his twitter email address to "efgh@x.com" but before updating by mistake he asked for password reset link. As a result his twitter account will be compromised by the attacker.

Fix: As soon as new email address is updated all the previous links should also get expired.

If you want further information please let me know.

Thanks and regards.
Mohd Haji

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148914'
original_report_id: '148914'
title: Session Management Issue CMS Airship
weakness: Memory Corruption - Generic
team_handle: paragonie
created_at: '2016-07-02T20:57:46.397Z'
disclosed_at: '2016-07-02T21:02:26.633Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- memory-corruption-generic
---

# Session Management Issue CMS Airship

## Metadata

- HackerOne Report ID: 148914
- Weakness: Memory Corruption - Generic
- Program: paragonie
- Disclosed At: 2016-07-02T21:02:26.633Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hey, I've found a session management issue in CMS Airship [bridge.cspr.ng]

Issue
----------
[*] When the password of an account is changed from a session, other sessions doesn't expire!

### Steps to Reproduce
[+] We Need to use two broswers

1. Login to one browser
2. Login to second browser
3. Then change the password from one browser.
4. After changing the password, go to other browser, the session will still be alive

- That means, server-side session not expire after password change.

How to Fix?
---------------
Server-side session should expire after password is changed from one session, or it should ask (either logout from other devices/browsers OR don't destroy the session [Like facebook does when changing password])

I hope you'll fix this soon! :-)

Thanks,
-Ahsan Tahir

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

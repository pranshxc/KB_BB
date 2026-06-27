---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '147388'
original_report_id: '147388'
title: Session doesn't expired after login
team_handle: fantasytote
created_at: '2016-06-26T05:38:32.964Z'
disclosed_at: '2016-07-23T16:51:31.725Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# Session doesn't expired after login

## Metadata

- HackerOne Report ID: 147388
- Weakness: 
- Program: fantasytote
- Disclosed At: 2016-07-23T16:51:31.725Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I don't know is it a valid vulnerability under your program but I found it.
Attacker can use victims cookie to logged in user account again.

Steps
=====
1) Login as user
2) Copy cookie you may use http://www.editthiscookie.com addon to edit cookies.
3) Logged out and delete cookie.
4) Now as a attacker Paste the copied cookie and see you are logged in into victims account.

If you need more information then I'll make a video as PoC on it.


Thanks 
Happy to help :)

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

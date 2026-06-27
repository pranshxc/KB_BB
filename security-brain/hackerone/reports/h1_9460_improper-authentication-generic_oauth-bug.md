---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9460'
original_report_id: '9460'
title: OAuth Bug
weakness: Improper Authentication - Generic
team_handle: respondly
created_at: '2014-04-24T00:01:08.472Z'
disclosed_at: '2014-04-30T18:17:24.431Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# OAuth Bug

## Metadata

- HackerOne Report ID: 9460
- Weakness: Improper Authentication - Generic
- Program: respondly
- Disclosed At: 2014-04-30T18:17:24.431Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I read the bug of @melvin and I also try to bypass this
https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=https://hackerone.com

so I made a bypassing tehcnique but didnt work 
https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com

But I think I found a bug 
This is the Screen shot: http://prntscr.com/3cu58e

When a user authorizes their twitter to connect with the URL above they will encounter that error.

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

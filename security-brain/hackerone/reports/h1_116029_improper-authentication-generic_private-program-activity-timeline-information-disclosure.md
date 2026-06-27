---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116029'
original_report_id: '116029'
title: Private program activity timeline information disclosure
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2016-02-12T02:16:41.103Z'
disclosed_at: '2016-03-16T12:26:36.421Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- improper-authentication-generic
---

# Private program activity timeline information disclosure

## Metadata

- HackerOne Report ID: 116029
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2016-03-16T12:26:36.421Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI,

There are some company which are hosting as external
https://hackerone.com/directory?query=type%3Aexternal&sort=name%3Aascending&page=1

but some one was hosting private BB on HackerOne which are not visible unless they invite you. However, you can check if any company is hosting private BB on HackerOne or not if you can guess the username they use.

Poc
https://hackerone.com/<redacted> : its external bb but the have a private bb

now let's discloure there activites :
https://hackerone.com/<redacted>/activities.json

and you can use it to check if they are private bb or not 
Generally most company chooses the same name as their company name like yahoo.

Cheers,
@tws_charfeddine

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244721'
original_report_id: '244721'
title: Open Redirect on [My.com]
weakness: Open Redirect
team_handle: mailru
created_at: '2017-06-30T11:41:42.910Z'
disclosed_at: '2017-08-14T10:27:59.188Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- open-redirect
---

# Open Redirect on [My.com]

## Metadata

- HackerOne Report ID: 244721
- Weakness: Open Redirect
- Program: mailru
- Disclosed At: 2017-08-14T10:27:59.188Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,
I have discovered an Open Redirect vulnerability affects logged-in users within the following parameter:
https://account.my.com/login_continue/?continue=

It seems like you allow only the URLs end with ```my.com``` which can be obviously bypassed using the listed methods :- 
- https://account.my.com/login_continue/?continue=http://3xr.me%5Cmy.com/
- https://account.my.com/login_continue/?continue=//notmy.com *any Domain ends with my.com*

Regards,
@exr

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

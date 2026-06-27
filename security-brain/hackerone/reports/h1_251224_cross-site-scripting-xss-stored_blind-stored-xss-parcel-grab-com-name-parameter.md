---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '251224'
original_report_id: '251224'
title: Blind stored xss [parcel.grab.com] > name parameter
weakness: Cross-site Scripting (XSS) - Stored
team_handle: grab
created_at: '2017-07-19T14:37:48.344Z'
disclosed_at: '2017-09-14T11:41:24.572Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 46
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind stored xss [parcel.grab.com] > name parameter

## Metadata

- HackerOne Report ID: 251224
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: grab
- Disclosed At: 2017-09-14T11:41:24.572Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,


___my previously reported blind xss is fixed but i found same type of xss in diffrent area with more impact.___


# Steps to repro:
1. create new account with name `"><script src=https://x.com></script>` here https://parcel.grab.com/
2.  afftected page is https://app.detrack.com/a/
where admin can see all the user's of application
and this is one more impact full because it contains all the user's email address. attacker can hijack all the information from there using xss
affeffcted page poc:
{F204498██████████
3. go here https://app.detrack.com/a/ and find ████████ , that is my account with xss payload.


thanks

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

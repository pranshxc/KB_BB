---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '96847'
original_report_id: '96847'
title: Un-handled exception leads to Information Disclosure
weakness: Information Disclosure
team_handle: keybase
created_at: '2015-10-30T19:35:01.692Z'
disclosed_at: '2016-07-15T14:07:44.857Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Un-handled exception leads to Information Disclosure

## Metadata

- HackerOne Report ID: 96847
- Weakness: Information Disclosure
- Program: keybase
- Disclosed At: 2016-07-15T14:07:44.857Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Steps:
1. Login to https://keybase.io/
2. Click on Me icon from top-right button (https://keybase.io/[username])
3. Click on Edit picture button (https://keybase.io/[username]#edit-me)
4. Intercept the traffic using proxy tool (e,g, Burp Suite)
5. Click on "Prove my Twitter identity" link
6. In the request, change the value of "sig_gen" parameter value from TwitterProof to some other random string (Attached image: Request.png)
7. Forward the request

Result: Unhandled exception occurs, which shows error dialog box as shown in attached image Error.png
Notice that the error dialog message contains sensitive information like-
application Module Names, Method Names, Error Location, Path etc.

This behavior is not acceptable. Keybase should not display any server side application details to end-users when an exception occurs.

Reference:
https://cwe.mitre.org/data/definitions/209.html

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

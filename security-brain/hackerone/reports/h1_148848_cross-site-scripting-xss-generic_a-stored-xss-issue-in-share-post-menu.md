---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148848'
original_report_id: '148848'
title: '"a stored xss issue in share post menu"'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2016-07-02T10:48:07.828Z'
disclosed_at: '2017-06-25T00:03:46.211Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# "a stored xss issue in share post menu"

## Metadata

- HackerOne Report ID: 148848
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2017-06-25T00:03:46.211Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

good day:

when a team mate named an xss  payload:
ex: "><img src=x onerror=alert(1)>
     "><img src=x onerror=alert(1)>
that xss payload will execute when making a post then share it, to a team that has an xss payload named.  that shared as a direct message please see screenshot 

when making post here:
https://hunter22.slack.com/files/create/space

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

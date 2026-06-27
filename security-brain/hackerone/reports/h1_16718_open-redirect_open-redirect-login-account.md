---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '16718'
original_report_id: '16718'
title: Open Redirect login account
weakness: Open Redirect
team_handle: slack
created_at: '2014-06-17T08:19:28.976Z'
disclosed_at: '2014-08-25T21:58:02.476Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- open-redirect
---

# Open Redirect login account

## Metadata

- HackerOne Report ID: 16718
- Weakness: Open Redirect
- Program: slack
- Disclosed At: 2014-08-25T21:58:02.476Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An open redirect is an application that takes a parameter and redirects a user to the parameter value without any validation. This vulnerability is used in phishing attacks to get users to visit malicious sites without realizing it.

###Reproduction Instructions 

go to `www.[TEAM].slack.com/?redir=llink?url=https://twitter.com/` log in your account on this link then redirect to twitter,google and any webiste you want.


###Proof of concept:
```
https://asdasda.slack.com/?redir=llink?url=https://twitter.com/
```


Regards,
Jayson Zabate

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

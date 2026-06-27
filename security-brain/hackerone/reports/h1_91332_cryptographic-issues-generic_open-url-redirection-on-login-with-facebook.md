---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '91332'
original_report_id: '91332'
title: Open Url redirection on login with facebook
weakness: Cryptographic Issues - Generic
team_handle: imgur
created_at: '2015-09-30T23:52:18.030Z'
disclosed_at: '2015-12-09T17:55:15.849Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# Open Url redirection on login with facebook

## Metadata

- HackerOne Report ID: 91332
- Weakness: Cryptographic Issues - Generic
- Program: imgur
- Disclosed At: 2015-12-09T17:55:15.849Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

steps to produce:
1, go to the site imgur.com and login with facebook and if you are new user then u must be asked for username on the link 
https://imgur.com/register/thirdparty/facebook?redirect=http://imgur.com/

nw just change the parameter redirect= value to https://google.com and hit enter and give username and  click next and you will redirected to google

Regards
Dipak

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

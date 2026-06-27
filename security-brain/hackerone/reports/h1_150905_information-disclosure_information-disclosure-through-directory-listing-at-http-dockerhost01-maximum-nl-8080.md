---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150905'
original_report_id: '150905'
title: Information disclosure through directory listing at http://dockerhost01.maximum.nl:8080
weakness: Information Disclosure
team_handle: radancy
created_at: '2016-07-12T13:13:35.951Z'
disclosed_at: '2019-07-10T15:25:43.703Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
tags:
- hackerone
- information-disclosure
---

# Information disclosure through directory listing at http://dockerhost01.maximum.nl:8080

## Metadata

- HackerOne Report ID: 150905
- Weakness: Information Disclosure
- Program: radancy
- Disclosed At: 2019-07-10T15:25:43.703Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello!

Description:
Information disclosure through enabled directory listing.
Links as poc:
http://dockerhost01.maximum.nl:8080
http://dockerhost01.maximum.nl:8080/logs/  (See pic 1 2 3 )
The unauthenticated user can get some juicy info about internal infrastructure, docker containers, logs, tokens and etc
There is also some design issues with api.  User can request infrastructure information without any authentication.
Links as poc:
http://dockerhost01.maximum.nl:8080/api/v1/nodes

For obvious reasons, I can not check whether this service is in scope, thats why i haven't searched for any critical informations and haven't check tokens and other stuff

Please let me know if you need some extra information.
Sorry for out of scope report, i thought it could be informative for you!
Thanks in advance!

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

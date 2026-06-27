---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280912'
original_report_id: '280912'
title: apache access.log leakage via long request on https://rapida.ru/
weakness: Buffer Over-read
team_handle: qiwi
created_at: '2017-10-20T10:16:15.573Z'
disclosed_at: '2018-02-05T08:08:41.696Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 42
tags:
- hackerone
- buffer-over-read
---

# apache access.log leakage via long request on https://rapida.ru/

## Metadata

- HackerOne Report ID: 280912
- Weakness: Buffer Over-read
- Program: qiwi
- Disclosed At: 2018-02-05T08:08:41.696Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Issue
access.log is leaked by attacker who trying send many requests.

#Explain:
Honestly i don't know how the bug is happened, but i guess if the access.log is too large, it will dump some part into the response, and attacker happily get it.

#Reproduce:
1. Access to https://rapida.ru/search/?q=<many character>
2. Send it to burp intruder
3. Make many request into the server
4. See the response

#Impact
The access log contains ip address of user, time request, the path of request url, if the page contain many secret paths, like admin private path or make some request with information on GET method, the impact is higher.

#Video PoC
{F231092}

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

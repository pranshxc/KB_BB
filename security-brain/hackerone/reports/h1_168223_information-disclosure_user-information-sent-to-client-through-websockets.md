---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '168223'
original_report_id: '168223'
title: User Information sent to client through websockets
weakness: Information Disclosure
team_handle: instacart
created_at: '2016-09-14T06:34:04.814Z'
disclosed_at: '2016-12-07T19:33:01.275Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# User Information sent to client through websockets

## Metadata

- HackerOne Report ID: 168223
- Weakness: Information Disclosure
- Program: instacart
- Disclosed At: 2016-12-07T19:33:01.275Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I noticed when monitoring the websocket requests that the account information of user, including user_id is sent to the client. 

__{"t":"d","d":{"r":8,"a":"p","b":{"p":"/carts/3671079_xjdJHqx88J435eDW5zxN/users/-KRbGN8R6uIjy6_OPx_j","d":{"id":25390626,"name":"Username}}}}__

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

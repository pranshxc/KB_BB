---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '211283'
original_report_id: '211283'
title: Cross Site WebSocket Hijacking
weakness: Improper Authentication - Generic
team_handle: legalrobot
created_at: '2017-03-07T07:55:45.004Z'
disclosed_at: '2017-10-16T07:07:08.356Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Cross Site WebSocket Hijacking

## Metadata

- HackerOne Report ID: 211283
- Weakness: Improper Authentication - Generic
- Program: legalrobot
- Disclosed At: 2017-10-16T07:07:08.356Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

### Description:
The given URL fails to validate Origin header- leading to Cross-Site WebSocket Hijacking. 

### Impact:
The impact, however, depends on how the server is configured. For example, it might require an authentication token which are user specific. In such cases, it might not be as sever as it would be in cases where server doesn't require anything at all.  
Since almost all the request in the site are performed in web socket, it might be possible to hijack the websocket. The impact would be similar to side-wise CSRF plus every response from server could be possible to be read by attacker.

### Affected Domain: 
app.legalrobot.com/socketjs/444/jfalksf/websocket

### Reference: 
https://www.christian-schneider.net/CrossSiteWebSocketHijacking.html
https://www.notsosecure.com/how-cross-site-websocket-hijacking-could-lead-to-full-session-compromise/

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

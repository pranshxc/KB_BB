---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178990'
original_report_id: '178990'
title: The websocket traffic is not secure enough
weakness: Cross-Site Request Forgery (CSRF)
team_handle: legalrobot
created_at: '2016-10-30T19:17:43.941Z'
disclosed_at: '2017-08-27T11:11:43.633Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# The websocket traffic is not secure enough

## Metadata

- HackerOne Report ID: 178990
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: legalrobot
- Disclosed At: 2017-08-27T11:11:43.633Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

'Cross-Site WebSocket Hijacking' is possible, because the websocket connection is not secure (enough). 
The traffic from and to the websocket can be sniffed with Chrome (see attachment), and replayed elsewhere (cross-domain). Explanation: https://www.christian-schneider.net/CrossSiteWebSocketHijacking.html

**Steps**:
After opening the homepage (https://app.legalrobot-uat.com) a websocket is created after a HTTP request like: https://app.legalrobot-uat.com/sockjs/689/k287_2tz/websocket, with a HTTP101 (switching protocols) response, resulting in a connection wss://app.legalrobot-uat.com/sockjs/689/k287_2tz/websocket.

This (upgrade) request can be called from an external origin.
{F131186}

After knowing the websocket URL, messages (captured in chrome) can be successfully sent. 

For example:
Open a session:  ["{\"msg\":\"connect\",\"version\":\"1\",\"support\":[\"1\",\"pre2\",\"pre1\"]}"]
Ping:  ["{\"msg\":\"ping\"}"]
Login:  ["{\"msg\":\"method\",\"method\":\"login\",\"params\":[{\"user\":{\"email\":\"arnotstacc@gmail.com\"},\"password\":{\"digest\":\"082a7a2a81c2733fd03567e47e0b6d9f09d32ec80065bda9c5cd34dd1c4f9edf\",\"algorithm\":\"sha-256\"}}],\"id\":\"7\"}"]
It is also unnecessary, to include the password algorithm in the login message (which can be encrypted with: http://md5decrypt.net/en/Sha256/)

A successful test with above messages using: http://ironwasp.org/cswsh.html (an online test tool).
{F131189}

**Suggestions to fix**:
- Check the origin from the requester server-side and adjust the Origin header for the 'upgrade' request.
- Add additional 'CSRF tokens'.
- Encrypt messages, so they cannot be intercepted in Chrome

**Additional references**:
https://www.notsosecure.com/how-cross-site-websocket-hijacking-could-lead-to-full-session-compromise/
https://www.owasp.org/index.php/Testing_WebSockets_(OTG-CLIENT-010)
https://humblesoftwaredev.wordpress.com/2016/08/01/securing-websocket-sockjs-connection/

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

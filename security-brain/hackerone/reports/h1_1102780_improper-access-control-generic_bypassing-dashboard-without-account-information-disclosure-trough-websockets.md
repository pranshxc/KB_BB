---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1102780'
original_report_id: '1102780'
title: bypassing dashboard without account + Information disclosure trough websockets
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2021-02-13T15:55:38.338Z'
disclosed_at: '2021-04-20T13:57:04.868Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
asset_identifier: support.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# bypassing dashboard without account + Information disclosure trough websockets

## Metadata

- HackerOne Report ID: 1102780
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2021-04-20T13:57:04.868Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Sumarry :** 
I found a information disclosure for bypassing parameter url attacker can redirect to dashboard without login user/pass page
and websocket can be exposed in response/dashboard.

**URL Effected**
https://support.nextcloud.com/#password_reset

### Steps To Reproduce:
  * Opened directory at https://support.nextcloud.com/#password_reset
  * Forget-password  and repeat url to burp-suite
  * In directory added a parameter bypass is ``//%0d%0aSet-Cookie:%20crlf-injection=mickeybrew//``
  * and look a responsive , you can be redirect to dashboard panel without user/pass
  * Show the ``network-browser`` and you can found api directory and websocket
  * Directory websocket is https://support.nextcloud.com/api/v1/signshow
  * Opened it and **Boom** You can see Information disclosure through websocket

**Request**
```
GET #password_reset/%0d%0aSet-Cookie:%20crlf-injection=mickey HTTP/1.1
Host: support.nextcloud.com
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 91
```
 ### Screenshots POC
█████
██████
███████
███

## Impact

It may cause the attacker to log into the dashboard page without logging in via user/pass, and the attacker finds sensitive files on open fires.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280389'
original_report_id: '280389'
title: No Rate limit on Password Reset Function
weakness: Improper Authentication - Generic
team_handle: infogram
created_at: '2017-10-19T10:58:34.318Z'
disclosed_at: '2017-12-12T15:15:38.464Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# No Rate limit on Password Reset Function

## Metadata

- HackerOne Report ID: 280389
- Weakness: Improper Authentication - Generic
- Program: infogram
- Disclosed At: 2017-12-12T15:15:38.464Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Infogram Security Team
***************************

###Description:-
I have identified that when resetting the password, the request has no rate limit which then can be used to brute force through one request. Which can be annoying to the infogram users.

###Steps to reproduce:-
* Request for password reset link.
* Catch the above request in burp suit send it to the repeater
* Now send continuous request to the server.

**NOTE:**  *Every time you will receive the same response which is {"status":"ok"}*

>HTTP/1.1 200 OK
Date: Thu, 19 Oct 2017 10:39:31 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 15
Connection: close
Server: nginx
X-DNS-Prefetch-Control: off
Strict-Transport-Security: max-age=10886400
X-Download-Options: noopen
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: no-referrer
X-Frame-Options: SAMEORIGIN
ETag: W/"f-VaSQ4oDUiZblZNAEkkN+sX+q3Sg"
X-Infogram-Server: b302

{"status":"ok"}

* I tried sending 25 request which was success. (It can be more..) 
{F230753}

###Solution:- 
You should limit the rate for password reset links to avoid such kind of issues.

*************************
Best Regards
*Akaash Sharma :)*

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

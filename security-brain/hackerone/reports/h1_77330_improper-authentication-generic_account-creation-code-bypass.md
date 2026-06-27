---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '77330'
original_report_id: '77330'
title: Account creation code bypass
weakness: Improper Authentication - Generic
team_handle: maplogin
created_at: '2015-07-21T14:10:49.060Z'
disclosed_at: '2015-07-25T01:11:49.064Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# Account creation code bypass

## Metadata

- HackerOne Report ID: 77330
- Weakness: Improper Authentication - Generic
- Program: maplogin
- Disclosed At: 2015-07-25T01:11:49.064Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi Team i was able to make an authentication bypass in your application .

Steps to replicate:

there are two phase evolved 
1) creating account using valid otp sent to registered email id .
2) capture the response it will be like 

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
Vary: Accept-Encoding
Date: Tue, 21 Jul 2015 13:52:27 GMT
Server: Google Frontend
Set-Cookie: session="eyJTVEFSVCI6Ik9LIiwiQ09ERSI6dHJ1ZSwiRU1BSUwiOiJhYWFydW5hZ2Fyd2FsQGdtYWlsLmNvbSIsIk1PREUiOiJTRVQifQ\075\075|1437486747|1a8ca2ba59d77ea84586c163405f547b686d6a2f"; Path=/; secure; HttpOnly
Alternate-Protocol: 443:quic,p=1
Expires: Tue, 21 Jul 2015 13:52:27 GMT
Content-Length: 39

{"status": "OK", "url": "/secretpage/"}


Now attacker chance phase two:

1) Create an account with valid information 
2) Now some OTP will be sent to your registered email address 
3) now provide any random 4 digit number 
4)now edit the response for the specific request to 
{"status": "OK", "url": "/secretpage/"}
and add set cookie header value to any random number  of same length
5) OTP will be bypassed PFA Screen shot.

Let me know if you need more details.

Thanks
Arun

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

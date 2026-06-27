---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '77067'
original_report_id: '77067'
title: No rate limiting for sensitive actions (like "forgot password") enables user
  enumeration
weakness: Violation of Secure Design Principles
team_handle: keybase
created_at: '2015-07-20T20:27:29.820Z'
disclosed_at: '2015-08-04T05:11:44.793Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- violation-of-secure-design-principles
---

# No rate limiting for sensitive actions (like "forgot password") enables user enumeration

## Metadata

- HackerOne Report ID: 77067
- Weakness: Violation of Secure Design Principles
- Program: keybase
- Disclosed At: 2015-08-04T05:11:44.793Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

I noticed a small information leak which allows an attacker to check whether an email address is associated with an account.


Steps to reproduce:

Send a POST-Request to the url POST /_/api/1.0/send-reset-pw.json HTTP/1.1 as the following example shows:


POST /_/api/1.0/send-reset-pw.json HTTP/1.1
Host: keybase.io
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0
Accept: */*

Cookie: guest=lgHZIDQ5ZjA0ZmY4YzE5YzBmZDdkOGZkMDQ3ZGZmZjczZjA4zlWtVuDOAAFRgMDEIEx%2BMZOb3r1Tv4NfNl%2Fsn5Mklyrd%2FgDZTXDwDLAusRJi

email_or_username=ed_aguillon@fandergroup%2ecom
_____________________

After checking THOUSANDS of request i notice that there's no error,

Here's the responce after  1000 request:

HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Mon, 20 Jul 2015 20:21:52 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 205
Connection: close
X-Powered-By: Express
Vary: X-HTTP-Method-Override
X-Frame-Options: SAMEORIGIN
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload

{"status":{"code":203,"desc":"user not found","name":"___BAD_LOGIN_USER_NOT_FOUND___"},"csrf_token":"lgHZIDQ5ZjA0ZmY4YzE5YzBmZDdkOGZkMDQ3ZGZmZjczZjA4zlWtWCbOAAFRgMDEIKUlcZOdMAo7T2X2Ee209zIYzRnWeuRICMnbn6U4GbEa"}

____________________________


Suggested fix:

You should always return a status message like: "If your email exists in our database, you'll receive a reset link". That way an attacker cannot distinguish between the two cases.

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

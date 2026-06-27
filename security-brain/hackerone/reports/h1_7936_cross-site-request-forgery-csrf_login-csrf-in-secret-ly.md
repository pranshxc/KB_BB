---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7936'
original_report_id: '7936'
title: Login CSRF in Secret.ly
weakness: Cross-Site Request Forgery (CSRF)
team_handle: secret
created_at: '2014-04-17T22:39:04.632Z'
disclosed_at: '2014-06-09T01:35:00.433Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Login CSRF in Secret.ly

## Metadata

- HackerOne Report ID: 7936
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: secret
- Disclosed At: 2014-06-09T01:35:00.433Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://www.secret.ly/_/login

POST /_/login HTTP/1.1
Host: www.secret.ly
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 55
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
{"Login":"user@vendor.tld","Password":"user_password_here"}

As you can see that this form does not contain any CSRF token,So it is vulnerable to Login CSRF attack.And also note that the login request is prone to bruteforce attack.You might want to impose some extra layer of security to prevent bruteforce attacks on **SECRET.LY**

Read [this](http://stackoverflow.com/questions/6412813/do-login-forms-need-tokens-against-csrf-attacks) for more information about the requirement of CSRF tokens on login forms.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5204'
original_report_id: '5204'
title: Cookie missing the HttpOnly flag
team_handle: coinbase
created_at: '2014-03-30T03:24:28.073Z'
disclosed_at: '2014-04-30T00:52:50.016Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
---

# Cookie missing the HttpOnly flag

## Metadata

- HackerOne Report ID: 5204
- Weakness: 
- Program: coinbase
- Disclosed At: 2014-04-30T00:52:50.016Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello coinbase,

Iam saikiran.Iam a security researcher.while i was going through your site i found that your website does not have HTTPOnly flag for the cookies.it is not a vulnerability but it is a new improvement and improves the security of your site.

If your not aware of HTTPOnly flag here is a small description..

HTTPOnly flag means - no cookie for you..if the HttpOnly flag is included in the HTTP response header, the cookie cannot be accessed through client side script . As a result, even if a cross-site scripting (XSS) flaw exists, and a user accidentally accesses a link that exploits this flaw, the browser  will not reveal the cookie to a third party.If HTTPOnly flaf is missing, As a result, the cookie (typically your session cookie) becomes vulnerable to theft of modification by malicious script.This may allow an attacker to get the cookie information using XSS attacks. The majority of XSS attacks target theft of session cookies. A server could help mitigate this issue by setting the HTTPOnly flag on a cookie it creates, indicating the cookie should not be accessible on the client.


Iam listing down the cookies which are missing the HTTPOnly flag...
• __cfduid 
• request_method 
• return_to
• _cb_cookie_test 

want to know more about httponly flag...
https://www.owasp.org/index.php/HttpOnly...

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

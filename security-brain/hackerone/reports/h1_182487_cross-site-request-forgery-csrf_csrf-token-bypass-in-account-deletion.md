---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '182487'
original_report_id: '182487'
title: CSRF Token Bypass in Account Deletion
weakness: Cross-Site Request Forgery (CSRF)
team_handle: gitlab
created_at: '2016-11-16T11:14:50.871Z'
disclosed_at: '2017-04-20T16:50:53.899Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF Token Bypass in Account Deletion

## Metadata

- HackerOne Report ID: 182487
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: gitlab
- Disclosed At: 2017-04-20T16:50:53.899Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The authentication token `authenticity_token` used in the POST request for deleting an account can be bypassed, by replacing the same with a token generated for deleting another account. This way, a self submitting form can be used to delete another user's account as long as he/she's logged in.

**Steps to Reproduce:**
1. Create an account and copy the POST request for deleting it.

```
POST /users HTTP/1.1
Host: gitlab.com
Referer: https://gitlab.com/profile/account
Cookie: _gitlab_session=1staccount_cookie;
Content-Type: application/x-www-form-urlencoded

_method=delete&authenticity_token=auth_1staccount
```
2. Create another account and send the above request after replacing the `_gitlab_session` cookie with that of the new one.  The `authenticity_token` remains the same as that of the first account.
3. Send the request and the new account gets deleted.

I have not explored all possible scenarios like different IP addresses or something. But the above situation, where I used accounts created using emails from a temporary email address generator, was reproduced multiple times.

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

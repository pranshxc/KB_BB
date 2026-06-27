---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '738'
original_report_id: '738'
title: Information disclosure (reset password token) and changing the user's password
weakness: Cross-Site Request Forgery (CSRF)
team_handle: security
created_at: '2014-01-17T00:49:34.781Z'
disclosed_at: '2014-02-19T23:44:04.883Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Information disclosure (reset password token) and changing the user's password

## Metadata

- HackerOne Report ID: 738
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: security
- Disclosed At: 2014-02-19T23:44:04.883Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The user gets an e-mail with password recovery link, which includes reset password token. The user clicks this link and is expected to enter a new password twice. Before entering the password the user clicks a link to a picture (https://xkcd.com/936/). When this happens, cross-domain referer leakage takes place. 


GET /936/ HTTP/1.1
Host: xkcd.com
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: pl,en-us;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://hackerone.com/users/password/edit?reset_password_token=HERE_IS_THE_VALUE_OF_RESET_PASSWORD_TOKEN
Connection: keep-alive


It allows the person who has control of xkcd.com to change the user's password (CSRF attack), because this person knows reset password token of the user, uses a new user's password of his choice and authenticity_token is not needed to make it happen.

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

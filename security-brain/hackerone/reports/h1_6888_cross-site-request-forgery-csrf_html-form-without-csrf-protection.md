---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6888'
original_report_id: '6888'
title: HTML Form without CSRF protection
weakness: Cross-Site Request Forgery (CSRF)
team_handle: irccloud
created_at: '2014-04-10T21:58:47.674Z'
disclosed_at: '2014-05-14T13:06:59.608Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# HTML Form without CSRF protection

## Metadata

- HackerOne Report ID: 6888
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: irccloud
- Disclosed At: 2014-05-14T13:06:59.608Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Cross-site request forgery, also known as a one-click attack or session riding and abbreviated as CSRF or XSRF, is a type of malicious exploit of a website whereby unauthorized commands are transmitted from a user that the website trusts.


Attack details
Form name: <empty>
Form action: https://www.irccloud.com/
Form method: POST

Form inputs:

email [Text]
password [Password]
org_invite [Hidden]

Request
GET / HTTP/1.1
Pragma: no-cache
Cache-Control: no-cache
Referer: http://www.irccloud.com/
Host: www.irccloud.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36
Accept: */*

The impact of this vulnerability:-

An attacker may force the users of a web application to execute actions of the attacker's choosing. A successful CSRF exploit can compromise end user data and operation in case of normal user. If the targeted end user is the administrator account, this can compromise the entire web application.

How to fix this vulnerability:-

Check if this form requires CSRF protection and implement CSRF countermeasures if necessary.

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

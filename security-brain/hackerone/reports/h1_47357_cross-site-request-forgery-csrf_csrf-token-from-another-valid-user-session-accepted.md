---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47357'
original_report_id: '47357'
title: CSRF token from another valid user session accepted
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mobilevikings
created_at: '2015-02-10T21:15:00.309Z'
disclosed_at: '2015-04-03T14:03:59.511Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF token from another valid user session accepted

## Metadata

- HackerOne Report ID: 47357
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mobilevikings
- Disclosed At: 2015-04-03T14:03:59.511Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

While testing website i have found interesting issue. For example request to remove sim auth:
POST /en/sims/authorization/remove/admin/1036359/ HTTP/1.1
Host: mobilevikings.be
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:35.0) Gecko/20100101 Firefox/35.0
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-CSRFToken: LI6qbdczbgPPQ7fxXR3duFENgY1qr3wB
X-Requested-With: XMLHttpRequest
Referer: https://mobilevikings.be/en/account/authorization/overview/
Cookie: mobilevikingsbe=fda79999f5d3ea86aee1cac688306948; csrftoken=LI6qbdczbgPPQ7fxXR3duFENgY1qr3wB; cookies.js=1; _ga=GA1.2.843387348.1423586164; __utmx=177304377.1C02iW_2TT2rFZKjDPjE7Q$0:0; __utmxx=177304377.1C02iW_2TT2rFZKjDPjE7Q$0:1423600511:8035200; __atuvc=5%7C6
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Content-Length: 0

Response:
HTTP/1.1 302 FOUND
Server: nginx/1.4.2
Date: Tue, 10 Feb 2015 21:02:50 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Vary: Cookie
Location: https://mobilevikings.be/en/account/authorization/overview/
Content-Language: en-be
Set-Cookie: messages="cc71d85271dc293bce25170e9cfb3d36beef0b5f$[[\"__json_message\"\0540\05425\054\"Authorization on this SIM card for  has been removed.\"]]"; Path=/
Content-Length: 0

Problem is that this request works with 
 X-CSRFToken: LI6qbdczbgPPQ7fxXR3duFENgY1qr3wB
this token i got from another account
the real token was 
AlEqSERKOXKjZfSdw2WtPY4l7n5b68BM

This issue make possible to attacker bypass CSRF using his own valid token (for example thru xss). Best practice is:
- token from different user do not work on other session
- and much better if token change on each request

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

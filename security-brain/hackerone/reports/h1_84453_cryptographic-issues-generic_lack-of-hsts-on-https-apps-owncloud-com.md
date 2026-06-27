---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '84453'
original_report_id: '84453'
title: Lack of HSTS on https://apps.owncloud.com
weakness: Cryptographic Issues - Generic
team_handle: owncloud
created_at: '2015-08-24T19:12:30.073Z'
disclosed_at: '2016-03-10T09:21:42.481Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cryptographic-issues-generic
---

# Lack of HSTS on https://apps.owncloud.com

## Metadata

- HackerOne Report ID: 84453
- Weakness: Cryptographic Issues - Generic
- Program: owncloud
- Disclosed At: 2016-03-10T09:21:42.481Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

There is lack of HSTS on you domain https://apps.owncloud.com

https://apps.owncloud.com/content/add.php

GET /content/add.php HTTP/1.1
Host: apps.owncloud.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://apps.owncloud.com/
Cookie: _ga=GA1.2.253154774.1440349970; __hstc=123946325.064f8833b677bb3f8fa92d275de0cf1c.1440349971890.1440349971890.1440443053275.2; hsfirstvisit=https%3A%2F%2Fowncloud.com%2F|https%3A%2F%2Fhackerone.com%2Fowncloud|1440349971889; hubspotutk=064f8833b677bb3f8fa92d275de0cf1c; _gat=1; __hssrc=1; __hssc=123946325.5.1440443053275; PHPSESSID=ja6a63hdb3ff617kqnm4luebk1
Connection: keep-alive
Cache-Control: max-age=0

HTTP/1.1 200 OK
Date: Mon, 24 Aug 2015 19:10:36 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.11
X-Frame-Options: SAMEORIGIN
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Content-Encoding: gzip
Vary: Accept-Encoding
Content-Length: 3258
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html


More:

https://www.owasp.org/index.php/HTTP_Strict_Transport_Security

Regards,
Prayas

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

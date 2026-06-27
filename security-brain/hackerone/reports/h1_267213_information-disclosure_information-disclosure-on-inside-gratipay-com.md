---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '267213'
original_report_id: '267213'
title: Information Disclosure on inside.gratipay.com
weakness: Information Disclosure
team_handle: gratipay
created_at: '2017-09-09T16:40:06.281Z'
disclosed_at: '2017-09-09T17:23:17.044Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: https://inside.gratipay.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# Information Disclosure on inside.gratipay.com

## Metadata

- HackerOne Report ID: 267213
- Weakness: Information Disclosure
- Program: gratipay
- Disclosed At: 2017-09-09T17:23:17.044Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello @gratipay, By checking request headers I've been able to identify that inside.gratipay.com is running on Server: WSGIServer/0.1 Python/2.7.11.

Request:
https://inside.gratipay.com/assets/inside-gratipay.svg
GET /assets/inside-gratipay.svg HTTP/1.1
Host: inside.gratipay.com
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: image/png,image/*;q=0.8,*/*;q=0.5
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://inside.gratipay.com/
Connection: keep-alive
Cache-Control: max-age=0

Response:
HTTP/1.1 200 OK
Connection: close
Date: Sat, 09 Sep 2017 16:21:50 GMT
Server: WSGIServer/0.1 Python/2.7.11
Content-Type: image/svg+xml
via: 1.1 vegur

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

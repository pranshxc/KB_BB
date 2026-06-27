---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '106384'
original_report_id: '106384'
title: Application error message
weakness: Information Disclosure
team_handle: radancy
created_at: '2015-12-22T00:08:02.707Z'
disclosed_at: '2017-03-31T02:20:44.138Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# Application error message

## Metadata

- HackerOne Report ID: 106384
- Weakness: Information Disclosure
- Program: radancy
- Disclosed At: 2017-03-31T02:20:44.138Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Request
GET / HTTP/1.1
Host: 12345'"\'\");|]*%00{%0d%0a<%00>%bf%27'####
Referer: https://serverhk.maximum.com:443/
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10
Accept: */*

Response
HTTP/1.1 500 Internal Server Error
Server: nginx/1.8.0
Date: Tue, 22 Dec 2015 00:02:00 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 122538
Connection: keep-alive
Strict-Transport-Security: max-age=31536000
X-Request-Id: f8204df5-0ff8-436e-9967-de2f33d6e5a7
X-Runtime: 0.629495

The impact of this vulnerability
The error messages may disclose sensitive information. This information can be used to launch further attacks.

How to fix this vulnerability
Review the source code for this script.

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

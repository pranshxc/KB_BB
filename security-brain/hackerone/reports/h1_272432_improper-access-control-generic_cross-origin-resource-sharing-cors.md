---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '272432'
original_report_id: '272432'
title: Cross-origin resource sharing (CORS)
weakness: Improper Access Control - Generic
team_handle: aspen
created_at: '2017-09-27T16:50:23.882Z'
disclosed_at: '2017-09-27T16:58:37.312Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 9
asset_identifier: new.aspen.io
asset_type: URL
max_severity: none
tags:
- hackerone
- improper-access-control-generic
---

# Cross-origin resource sharing (CORS)

## Metadata

- HackerOne Report ID: 272432
- Weakness: Improper Access Control - Generic
- Program: aspen
- Disclosed At: 2017-09-27T16:58:37.312Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Cross-origin resource sharing (CORS) is a mechanism that allows restricted resources (e.g. fonts) on a web page to be requested from another domain outside the domain from which the resource originated. The Access-Control-Allow-Origin header indicates whether a resource can be shared based by returning the value of the Origin request header, "*", or "null" in the response. 

The impact of this vulnerability
Any website can make XHR requests to your site and access the responses

Request
GET / HTTP/1.1
Host: new.aspen.io
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*


Response
HTTP/1.1 200 OK
Server: GitHub.com
Content-Type: text/html; charset=utf-8
Last-Modified: Fri, 09 Sep 2016 02:44:52 GMT
Access-Control-Allow-Origin: *
Expires: Wed, 27 Sep 2017 15:41:41 GMT
Cache-Control: max-age=600
X-GitHub-Request-Id: 6B08:6D67:84A53D1:B5695B7:59CBC45B
Content-Length: 11931
Accept-Ranges: bytes
Date: Wed, 27 Sep 2017 16:43:33 GMT
Via: 1.1 varnish
Age: 548
Connection: keep-alive
X-Served-By: cache-hhn1523-HHN
X-Cache: HIT
X-Cache-Hits: 9
X-Timer: S1506530614.564453,VS0,VE0
Vary: Accept-Encoding
X-Fastly-Request-ID: 3f8903f4431ae9750cb02a8648b31c391fe5cc26
Original-Content-Encoding: gzip

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

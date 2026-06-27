---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '214570'
original_report_id: '214570'
title: Nginx Version Disclosure
weakness: Information Disclosure
team_handle: airbnb
created_at: '2017-03-18T22:56:59.090Z'
disclosed_at: '2017-03-23T22:31:50.227Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Nginx Version Disclosure

## Metadata

- HackerOne Report ID: 214570
- Weakness: Information Disclosure
- Program: airbnb
- Disclosed At: 2017-03-23T22:31:50.227Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,
While i was testing airbnb i found nginx version disclosure in HTTP Response. Which can help attacker to gain information or an attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.
**URL:**
https://www.airbnb.com/ 

**Version:**
 1.7.12 

**HTTP Response:**
HTTP/1.1 200 OK
Cache-Control: public, max-age=1176
ETag: W/"9c73019eae963a92b713b293a694505c"
Set-Cookie: erf_eligible=54; expires=Wed, 17-May-2017 22:25:40 GMT; domain=.airbnb.com
Set-Cookie: p1_hcopy6=adventure; expires=Wed, 17-May-2017 22:25:40 GMT; domain=.airbnb.com
Strict-Transport-Security: max-age=10886400; includeSubdomains
Server: nginx/1.7.12
Link: <https://a0.muscache.com/airbnb/static/packages/common-781445fb2cd2b545764ac59a2005b6fc.css>;rel=preload;as=style,<https://a0.muscache.com/airbnb/static/packages/common_o2.1-729252007d757207298cba7196a6b137.css>;rel=preload;as=style,<https://a0.muscache.com/airbnb/static/packages/map_search-672ac441e9af02915c7275d3ba35d9b8.css>;rel=preload;as=style,<https://a0.muscache.com/airbnb/static/p1/main-993bb6971017210f496e34db17fa32ec.css>;rel=preload;as=style,<https://a0.muscache.com/airbnb/static/packages/header_cookie.bundle-96e417780c11600460e5.js>;rel=preload;as=script
X-Server-Name: www.airbnb.com
X-XSS-Protection: 1; mode=block
Connection: keep-alive
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Vary: Accept-Encoding
Content-Length: 70282
Content-Type: text/html; charset=utf-8
X-UA-Compatible: IE=Edge,chrome=1
Status: 200 OK
Content-Security-Policy: default-src 'self' https:; connect-src 'self' https: ws://localhost.airbnb.com:8888 *.inspectlet.com wss://ws.inspectlet.com http:; font-src 'self' data: *.muscache.com fonts.gstatic.com use.typekit.net; frame-src *; img-src 'self' https: *.inspectlet.com http: data:; media-src 'self' https:; object-src 'self' https:; script-src 'sha256-2S1zmL0hHGfsnw+rP+m+rBKOma7sejqhykg8DdWFKfU=' 'sha256-rfTud2kTm0UjtJ6PqxcrkglfrUD4H8WCcS9mCs6PJ5s=' 'self' https: 'unsafe-eval' 'unsafe-inline' *.inspectlet.com http:; style-src 'self' https: 'unsafe-inline' http:; report-uri /tracking/csp?action=show&controller=homepages&req_uuid=c0608401-9001-4060-941d-afd1caeca2ac&version=b6612629f48f5a51b6937512a73e9d33e1bffbbd;
Date: Sat, 18 Mar 2017 22:25:40 GMT
Content-Encoding: 

**Solution:**
Add the following line to your nginx.conf file to prevent information leakage from the SERVER header of its HTTP response: 	
server_tokens off

Kind Regards,
Mahad Ahmed

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

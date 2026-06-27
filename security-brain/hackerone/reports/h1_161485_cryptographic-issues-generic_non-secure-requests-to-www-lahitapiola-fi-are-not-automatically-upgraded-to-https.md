---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161485'
original_report_id: '161485'
title: Non-secure requests to www.lahitapiola.fi are not automatically upgraded to
  HTTPS
weakness: Cryptographic Issues - Generic
team_handle: localtapiola
created_at: '2016-08-19T22:16:58.943Z'
disclosed_at: '2019-10-09T19:24:52.048Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cryptographic-issues-generic
---

# Non-secure requests to www.lahitapiola.fi are not automatically upgraded to HTTPS

## Metadata

- HackerOne Report ID: 161485
- Weakness: Cryptographic Issues - Generic
- Program: localtapiola
- Disclosed At: 2019-10-09T19:24:52.048Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

To reproduce, send a `HEAD` request to `http://www.lahitapiola.fi` like so:

```
curl -I http://www.lahitapiola.fi
HTTP/1.1 301 Moved Permanently
Date: Fri, 19 Aug 2016 22:11:59 GMT
Location: http://www.lahitapiola.fi/henkilo
Cache-Control: max-age=60
Expires: Fri, 19 Aug 2016 22:12:59 GMT
Content-Type: text/html; charset=iso-8859-1
Set-Cookie: TS0159a426=0147052ac59d111bf38a364a9cd7c5f17c819d9baeab5600d1c4d83de4302318828d8e96ab; Path=/
Transfer-Encoding: chunked
```

You will see that the server does not instruct the client to upgrade the connection to HTTPS. The server responds with a 301 status code but redirects the visitors to the non-HTTPS site. It should respond with a 301 status code and the response header `Location` set to `https://www.lahitapiola.fi`.

Non-secure connections need to be upgraded to HTTPS as soon as possible using a permanent redirect. Since this isn't happening, any information transmitted by users (including usernames and passwords) is at risk of compromise. Considering that the site responds to HTTPS requests @ `https://www.lahitapiola.fi` this oversight should be corrected.

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

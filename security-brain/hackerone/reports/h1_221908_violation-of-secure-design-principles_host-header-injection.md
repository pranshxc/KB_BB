---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '221908'
original_report_id: '221908'
title: Host header Injection
weakness: Violation of Secure Design Principles
team_handle: homebrew
created_at: '2017-04-18T14:34:10.772Z'
disclosed_at: '2017-04-19T09:04:56.488Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Host header Injection

## Metadata

- HackerOne Report ID: 221908
- Weakness: Violation of Secure Design Principles
- Program: homebrew
- Disclosed At: 2017-04-19T09:04:56.488Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

HI SECURITY TEAM

Here is host header injection.

#Request (changing host to www.google.com)
GET / HTTP/1.1
Host: www.google.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive

#RESPONSE(www.google.com injected)
HTTP/1.1 301 Moved Permanently
Cache-Control: public, max-age=0, must-revalidate
Content-Length: 35
Content-Type: text/plain
Date: Tue, 18 Apr 2017 14:23:25 GMT
Location: https://google.com/
Age: 0
Connection: keep-alive
Server: Netlify

Redirecting to https://google.com/

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '185833'
original_report_id: '185833'
title: Incomplete or No Cache-control and Pragma HTTP Header Set
team_handle: gratipay
created_at: '2016-11-27T16:22:25.984Z'
disclosed_at: '2017-03-17T19:01:10.112Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# Incomplete or No Cache-control and Pragma HTTP Header Set

## Metadata

- HackerOne Report ID: 185833
- Weakness: 
- Program: gratipay
- Disclosed At: 2017-03-17T19:01:10.112Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.

HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn
Date: Sun, 27 Nov 2016 16:18:06 GMT
Content-Type: text/html; charset=UTF-8
X-Gratipay-Version: 2014
Set-Cookie: csrf_token=chYzzQF9UYGunrz4V68ggeuvV6MpTjTZ; expires=Sun, 04 Dec 2016 16:18:06 GMT; Path=/; secure
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Cache-Control: no-cache
Via: 1.1 vegur

Solution:
Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate, private; and that the pragma HTTP header is set with no-cache.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '83373'
original_report_id: '83373'
title: 'owncloud.com: Cross Site Tracing'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: owncloud
created_at: '2015-08-19T07:33:14.093Z'
disclosed_at: '2015-10-11T07:07:01.177Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# owncloud.com: Cross Site Tracing

## Metadata

- HackerOne Report ID: 83373
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: owncloud
- Disclosed At: 2015-10-11T07:07:01.177Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

`REQUEST:`
TRACE / HTTP/1.0
Host: owncloud.com
Cookie: 74b33b43fa`

`RESPONSE:`
HTTP/1.1 200 OK
Date: Wed, 19 Aug 2015 06:59:31 GMT
Server: Apache/2.2.17 (Linux/SUSE)
Connection: close
Content-Type: message/http

TRACE / HTTP/1.0
Host: owncloud.com
Cookie: 74b33b43fa; wordpress_test_cookie=WP+Cookie+check; _icl_current_language=en


This vulnerability can show cookie with http only flag

with xss it's a very critical attack vector

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '315838'
original_report_id: '315838'
title: Non-Cloudflare IPs allowed to access origin servers
weakness: Violation of Secure Design Principles
team_handle: coalition
created_at: '2018-02-14T01:39:07.667Z'
disclosed_at: '2018-05-28T04:11:21.614Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 23
asset_identifier: platform.thecoalition.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Non-Cloudflare IPs allowed to access origin servers

## Metadata

- HackerOne Report ID: 315838
- Weakness: Violation of Secure Design Principles
- Program: coalition
- Disclosed At: 2018-05-28T04:11:21.614Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Security Team,

**Summary:** Like report #255978 It is possible to access origin servers served by nginx and not cloudflare. 

**Description:** Even though these IP's don't serve a functional version of the app it is possible to enable DDoS attacks by bypassing cloudflare protections.

## Steps To Reproduce:

  1. 52.32.239.55
  2. 54.69.218.2
  3. 34.208.41.101
 
There are more IP's but I think these are enough as a proof of concept.

## Impact

Response header from one of origin IP's :
`Connection:keep-alive
Content-Encoding:gzip
Content-Length:4774
Content-Type:text/html; charset=utf-8
Date:Wed, 14 Feb 2018 01:28:15 GMT
Request-Id:542a2e00-1126-11e8-bfba-c90bcfe9a4b2
Server:nginx/1.12.1
Strict-Transport-Security:max-age=16070400
Vary:Accept-Encoding
X-Content-Type-Options:nosniff
X-Download-Options:noopen
X-Frame-Options:deny
X-XSS-Protection:1; mode=block`

and the regular website:

`cf-ray:3ecc3592fd2a7e21-DTW
content-encoding:br
content-type:text/html; charset=utf-8
date:Wed, 14 Feb 2018 01:21:12 GMT
expect-ct:max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
request-id:57feab10-1125-11e8-a7fe-31e9cef0afb4
server:cloudflare
status:200
strict-transport-security:max-age=2592000; includeSubDomains
vary:Accept-Encoding
x-content-type-options:nosniff
x-download-options:noopen
x-frame-options:deny
x-xss-protection:1; mode=block`

Also http://54.69.218.2/login serves an insecure login page.

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

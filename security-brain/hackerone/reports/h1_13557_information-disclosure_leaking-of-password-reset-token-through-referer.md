---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13557'
original_report_id: '13557'
title: Leaking of password reset token through referer
weakness: Information Disclosure
team_handle: factlink
created_at: '2014-05-27T08:10:06.992Z'
disclosed_at: '2014-07-08T10:00:32.004Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Leaking of password reset token through referer

## Metadata

- HackerOne Report ID: 13557
- Weakness: Information Disclosure
- Program: factlink
- Disclosed At: 2014-07-08T10:00:32.004Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

When we request a password reset link, after that before Writing a new password, Going to an External link would cause Referer leakage...

Remote Address:74.125.68.95:443
Request URL:https://fonts.googleapis.com/css?family=Open+Sans:400italic,700italic,400,700
Request Method:GET
Status Code:200 OK
Request Headers
:host:fonts.googleapis.com
:method:GET
:path:/css?family=Open+Sans:400italic,700italic,400,700
:scheme:https
:version:HTTP/1.1
accept:text/css,*/*;q=0.1
accept-encoding:gzip,deflate,sdch
accept-language:en-US,en;q=0.8
cache-control:max-age=0
referer:https://factlink-staging.herokuapp.com/users/password/edit?reset_password_token=8GbCsdRTX3yx3wZzwPuy
user-agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36
Query String Parametersview sourceview URL encoded
family:Open Sans:400italic,700italic,400,700
Response Headers
alternate-protocol:443:quic
cache-control:private, max-age=86400
content-encoding:gzip
content-length:387
content-type:text/css
date:Tue, 27 May 2014 08:08:05 GMT
expires:Tue, 27 May 2014 08:08:05 GMT
server:GSE
status:200 OK
timing-allow-origin:*
version:HTTP/1.1
x-content-type-options:nosniff
x-frame-options:SAMEORIGIN
x-xss-protection:1; mode=block

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

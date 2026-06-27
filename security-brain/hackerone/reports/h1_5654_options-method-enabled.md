---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5654'
original_report_id: '5654'
title: OPTIONS Method Enabled
team_handle: c2fo
created_at: '2014-04-02T17:28:52.902Z'
disclosed_at: '2014-04-07T14:24:52.358Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# OPTIONS Method Enabled

## Metadata

- HackerOne Report ID: 5654
- Weakness: 
- Program: c2fo
- Disclosed At: 2014-04-07T14:24:52.358Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability Details:-
I detected that OPTIONS method is allowed. This issue is reported as extra information. 

Impact:-
Information disclosed from this page can be used to gain additional information about the target system. 

Remedy:-
Disable OPTIONS method in all production systems. 


POC :-
Request :-
OPTIONS /wp-content/themes/theme/js/ HTTP/1.1
Host: c2fo.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive

Responce :-
HTTP/1.1 200 OK
Connection: keep-alive
Date: Wed, 02 Apr 2014 17:21:31 GMT
Server: WP Engine/6.0.2
Keep-Alive: timeout=20
X-Type: default
X-Frame-Options: SAMEORIGIN
Allow: GET,HEAD,POST,OPTIONS,TRACE
Content-Length: 0
Content-Type: httpd/unix-directory

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

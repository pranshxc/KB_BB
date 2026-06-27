---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '166278'
original_report_id: '166278'
title: Host Header Injection/Redirection
weakness: Violation of Secure Design Principles
team_handle: rubygems
created_at: '2016-09-19T06:45:55.200Z'
disclosed_at: '2018-02-08T23:15:27.189Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Host Header Injection/Redirection

## Metadata

- HackerOne Report ID: 166278
- Weakness: Violation of Secure Design Principles
- Program: rubygems
- Disclosed At: 2018-02-08T23:15:27.189Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

rubygems.org is vulnerable to host header injection because the host header can be changed to something outside the target domain.

Attack vectors are somewhat limited but depends on how the host header is used by the back-end application code. If code references the hostname used in the URL such as password reset pages, an attacker could spoof the host header of the request in order to trick the application to forwarding the password reset email to the attackers domain instead, etc. Other attack vectors may also be possible through manipulation of hyperlinks or other misc. code that relies on the host/domain of the request.

nc rubygems.org 80
GET / HTTP/1.1
Host: google.com

HTTP/1.1 301 Moved Permanently
Server: nginx
Date: Mon, 19 Sep 2016 06:44:25 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Connection: keep-alive
Location: https://google.com/
X-UA-Compatible: IE=Edge,chrome=1

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

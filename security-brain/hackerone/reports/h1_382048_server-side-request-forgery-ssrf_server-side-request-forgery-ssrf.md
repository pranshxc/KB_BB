---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '382048'
original_report_id: '382048'
title: Server-Side Request Forgery (SSRF)
weakness: Server-Side Request Forgery (SSRF)
team_handle: deptofdefense
created_at: '2018-07-16T13:13:13.567Z'
disclosed_at: '2019-12-02T19:09:40.073Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Server-Side Request Forgery (SSRF)

## Metadata

- HackerOne Report ID: 382048
- Weakness: Server-Side Request Forgery (SSRF)
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:09:40.073Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I've found a Server-Side Request Forgery (SSRF)

Steps to reproduce:

+ start listening on your server 
+ navigate to http://██████/help/ACPS.htm#http://$yourserver:$port
+ you will get the request

██████

## Impact

Server-Side Request Forgery (SSRF) Attack

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

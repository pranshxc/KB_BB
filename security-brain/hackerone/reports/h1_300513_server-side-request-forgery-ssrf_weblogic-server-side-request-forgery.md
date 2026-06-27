---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '300513'
original_report_id: '300513'
title: WebLogic Server Side Request Forgery
weakness: Server-Side Request Forgery (SSRF)
team_handle: deptofdefense
created_at: '2017-12-25T21:57:03.064Z'
disclosed_at: '2019-12-02T19:02:34.799Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# WebLogic Server Side Request Forgery

## Metadata

- HackerOne Report ID: 300513
- Weakness: Server-Side Request Forgery (SSRF)
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:02:34.799Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Universal Description Discovery and Integration (UDDI) application is publicly available on this WebLogic server. The SearchPublicRegistries.jsp page can be abused by unauthenticated attackers to cause the WebLogic web server to connect to an arbitrary TCP port of an arbitrary host. Responses returned are fairly verbose and can be used to infer whether a service is listening on the port specified. This vulnerability affects Oracle Fusion Middleware 10.0.2, 10.3.6.

The impact of this vulnerability
An attacker can force the WebLogic web server to connect to an arbitrary TCP port of an arbitrary host.

How to fix this vulnerability
Apply the Oracle Critical Patch Update Advisory from July 2014 or restrict access to the UDDI application.

https://blog.gdssecurity.com/labs/2015/3/30/weblogic-ssrf-and-xss-cve-2014-4241-cve-2014-4210-cve-2014-4.html

## Impact

https://███████/uddiexplorer/SearchPublicRegistries.jsp?operator=http://127.0.0.1:80&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search

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

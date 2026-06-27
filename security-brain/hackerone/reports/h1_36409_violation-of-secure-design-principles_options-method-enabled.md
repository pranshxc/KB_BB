---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '36409'
original_report_id: '36409'
title: Options Method Enabled
weakness: Violation of Secure Design Principles
team_handle: openfolio
created_at: '2014-11-17T20:09:50.250Z'
disclosed_at: '2014-12-21T19:42:15.903Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Options Method Enabled

## Metadata

- HackerOne Report ID: 36409
- Weakness: Violation of Secure Design Principles
- Program: openfolio
- Disclosed At: 2014-12-21T19:42:15.903Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Vuln Details:

Domain:  
https://openfolio.com/

I detected that OPTIONS method is allowed

Impact:

Information disclosed from this page can be used to gain additional information about the target system.

Remedy:
Disable OPTIONS method in all production systems.

POC:

Request:

OPTIONS /signup/ HTTP/1.1
Cache-Control: no-cache
Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.170 Safari/537.36 Netsparker
Accept-Language: en-us,en;q=0.5
Host: openfolio.com
Cookie: csrftoken=sZn2eGRmRYFaXIFuPEbH31Fc5C7bZVQz; sessionid=o5t6wtfpeqs4f1fflyc1urhcg4qotbtb
Accept-Encoding: gzip, deflate

Response:

OPTIONS /signup/ HTTP/1.1
Cache-Control: no-cache
Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.170 Safari/537.36
Accept-Language: en-us,en;q=0.5
Host: openfolio.com
Cookie: csrftoken=sZn2eGRmRYFaXIFuPEbH31Fc5C7bZVQz; sessionid=o5t6wtfpeqs4f1fflyc1urhcg4qotbtb
Accept-Encoding: gzip, deflate

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

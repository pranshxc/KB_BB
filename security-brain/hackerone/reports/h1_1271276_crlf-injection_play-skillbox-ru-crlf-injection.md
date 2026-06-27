---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1271276'
original_report_id: '1271276'
title: '[play.skillbox.ru] CRLF Injection'
weakness: CRLF Injection
team_handle: mailru
created_at: '2021-07-21T02:58:21.866Z'
disclosed_at: '2021-10-30T15:19:56.986Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
asset_identifier: 'Ext. O: Delegated subdomain or branded partner service'
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- crlf-injection
---

# [play.skillbox.ru] CRLF Injection

## Metadata

- HackerOne Report ID: 1271276
- Weakness: CRLF Injection
- Program: mailru
- Disclosed At: 2021-10-30T15:19:56.986Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Domain, site, application
The / folder / to / folder redirect script is vulnerable to a CRLF Injection attack.
PoC Setting cookie crlf=CRLF;domain=.skillbox.ru;path=/;/ All browsers except FireFox are affected

##Affected URL:
http://play.skillbox.ru/

##Payload
%0D%0ASet-Cookie:crlf=CRLF;domain=.skillbox.ru;path=/;/
##Testing environment
OS: Windows 10
BurpSuite v2021.7.1-8747 (Early Adopter)

##Steps to reproduce
1. Open the URL http://play.skillbox.ru/%0D%0ASet-Cookie:crlf=CRLF;domain=.skillbox.ru;path=/;/
2. Intercept the request and send it to the reporter.
3. Click on Send and look for the  Set-Cookie:crlf=CRLF;domain=.skillbox.ru;path=/;/ in the response.

{F1383683}


PoC, exploit code, screenshots, video, references, additional resources
Please refer to the attached PoC.

## Impact

##Impact
Can be used in combination with other vulnerabilities (if any) / factors, for example:
1) XSS via Cookie
2) Fixing the session
3) Bypassing Cookie-Based CSRF Protection
4) Bypassing header best practices.

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

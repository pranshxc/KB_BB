---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1350671'
original_report_id: '1350671'
title: XSS Stored on https://seedr.ru
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2021-09-24T18:47:28.635Z'
disclosed_at: '2022-03-18T08:22:36.037Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: NATIVEROLL
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS Stored on https://seedr.ru

## Metadata

- HackerOne Report ID: 1350671
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2022-03-18T08:22:36.037Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Site: https://seedr.ru/
OS version: Windows 10
browser: Google chrome

Stored cross-site scripting  arises when an application receives data from an untrusted source and includes that data within its later HTTP responses in an unsafe way. 
I changed my nickname to a code that demonstrates the malicious code of the attacker, now any user, including administrators, will be compromised. When an administrator account is stolen, both the server side and the privacy of users are at risk. Therefore, I consider this vulnerability to be of high severity level.
"Groups" are also vulnerable to XSS stored. I changed the name of the group to demo code. Now everyone who visits my group page is potentially compromised. Accordingly, you can send a link to the group, which will also lead to the compromise of users. (even if the group hasn't been published yet).
Link:
https://seedr.ru/group/4/614e14e79762b6055d8b4586

How to prevent XSS attacks
In general, effectively preventing XSS vulnerabilities is likely to involve a combination of the following measures:
Filter input on arrival. At the point where user input is received, filter as strictly as possible based on what is expected or valid input.
Encode data on output. At the point where user-controllable data is output in HTTP responses, encode the output to prevent it from being interpreted as active content. Depending on the output context, this might require applying combinations of HTML, URL, JavaScript, and CSS encoding.
Use appropriate response headers. To prevent XSS in HTTP responses that aren't intended to contain any HTML or JavaScript, you can use the Content-Type and X-Content-Type-Options headers to ensure that browsers interpret the responses in the way you intend.
Content Security Policy. As a last line of defense, you can use Content Security Policy (CSP) to reduce the severity of any XSS vulnerabilities that still occur.

## Impact

If an attacker can control the script running in the victim's browser, he can completely compromise that user. In this case, any user who comes to my page will be compromised, and this may be the site administrator, which will jeopardize the security in general. Also, an attacker can take any of the actions applicable to the impact of reflected XSS vulnerabilities.

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

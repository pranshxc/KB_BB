---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163676'
original_report_id: '163676'
title: Legal | Application is Missing CSP(Content Security Policy) Header
weakness: Violation of Secure Design Principles
team_handle: legalrobot
created_at: '2016-08-26T22:14:47.426Z'
disclosed_at: '2016-08-31T06:12:39.693Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Legal | Application is Missing CSP(Content Security Policy) Header

## Metadata

- HackerOne Report ID: 163676
- Weakness: Violation of Secure Design Principles
- Program: legalrobot
- Disclosed At: 2016-08-31T06:12:39.693Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

-Content Security Policy Header used to allow only source code to execute in the application from the domain mentioned in its list. By using this we can restrict code to execute which is written in application either by developer or by Hacker

-Since application contains no such header i am going to  inject an image from third party domain which is not of application domain

<img src="https://s-media-cache-ak0.pinimg.com/564x/ab/2d/bd/ab2dbda0c6c11455527c0dd34d5f5bf6.jpg" height="500" width="500"/>

third party domain
https://s-media-cache-ak0.pinimg.com/564x/ab/2d/bd/ab2dbda0c6c11455527c0dd34d5f5bf6.jpg

Refer-https://www.owasp.org/index.php/Content_Security_Policy_Cheat_Sheet

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

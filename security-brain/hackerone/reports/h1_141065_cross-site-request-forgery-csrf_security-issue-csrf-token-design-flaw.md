---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141065'
original_report_id: '141065'
title: 'Security Issue : CSRF Token Design Flaw'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: drchrono
created_at: '2016-05-25T23:50:54.437Z'
disclosed_at: '2016-07-30T23:44:29.036Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Security Issue : CSRF Token Design Flaw

## Metadata

- HackerOne Report ID: 141065
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: drchrono
- Disclosed At: 2016-07-30T23:44:29.036Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Introduction:

Hello I am Bruin, a security researcher and analyst. I have been able to identify a bypass in your CSRF protection mechanism, which upon a successful execution can result in a successful CSRF attack on a victim's account.

Description:

CSRF Token's are different from session ID'S in a way that they are not consistent in entire user session but drchrono.com do not practice the rotation of CSRF token's for every request in a session.

Reproduction Steps:

< Log in to drchrono.com
< go to settings
< go to profile
< click change password
< fill out the fields
< click save and intercept the request
< copy POST data
< repeat the process

--Observe that the CSRF token from both request's is same.

Impact:

It can be misused in multiple ways, some of the scenarios are listed below :

*An attacker capturing the CSRF token via cross site scripting can use it to plant a successful CSRF attack even if the session id is unusable.
*A network based attack can be used to capture and replay the token on to the victim's account.

Fix:

Rotate the token on each consecutive session.

Please let me know if any additional information is required . I shall be waiting for your reply.

Regards,
Bruin,
Security Researcher.

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

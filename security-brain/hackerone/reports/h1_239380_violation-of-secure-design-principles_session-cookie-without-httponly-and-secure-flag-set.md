---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '239380'
original_report_id: '239380'
title: Session Cookie without HttpOnly and secure flag set
weakness: Violation of Secure Design Principles
team_handle: stellar
created_at: '2017-06-12T23:57:59.756Z'
disclosed_at: '2017-06-14T12:03:10.146Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Session Cookie without HttpOnly and secure flag set

## Metadata

- HackerOne Report ID: 239380
- Weakness: Violation of Secure Design Principles
- Program: stellar
- Disclosed At: 2017-06-14T12:03:10.146Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

vulnerable URL: www.stellar.org
The PHPSESSID cookie does not have the HTTPOnly flag set. 
When a cookie is set with the HTTPOnly flag, it instructs the browser that the cookie can only accessed by the server and not by client-side scripts. 
This is an important security protection for session cookies.

reference : https://hackerone.com/reports/75357

{F193713}

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

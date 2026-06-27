---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '75357'
original_report_id: '75357'
title: Session Cookie without HttpOnly and secure flag set
weakness: Violation of Secure Design Principles
team_handle: qiwi
created_at: '2015-07-14T10:05:39.855Z'
disclosed_at: '2015-09-27T08:36:43.881Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Session Cookie without HttpOnly and secure flag set

## Metadata

- HackerOne Report ID: 75357
- Weakness: Violation of Secure Design Principles
- Program: qiwi
- Disclosed At: 2015-09-27T08:36:43.881Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

vulnerable URL:https://portal.int.qiwi.com/login.php
The PHPSESSID cookie does not have the HTTPOnly flag set. 
When a cookie is set with the HTTPOnly flag, it instructs the browser that the cookie can only accessed by the server and not by client-side scripts. 
This is an important security protection for session cookies.

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

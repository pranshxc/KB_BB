---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361184'
original_report_id: '361184'
title: CSRF ON EDITING NAME (OPTIONAL)
weakness: Cross-Site Request Forgery (CSRF)
team_handle: liberapay
created_at: '2018-06-02T20:48:29.577Z'
disclosed_at: '2018-06-04T11:49:17.355Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF ON EDITING NAME (OPTIONAL)

## Metadata

- HackerOne Report ID: 361184
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: liberapay
- Disclosed At: 2018-06-04T11:49:17.355Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Allows an attacker to change one's account information in this case ie information from "Name (Optional)". Attackers can change the information without having to login to victim account or without having to login but only by using CSRF technique. I tried changing the "Name (Optional)" information to "YOU HAVE BEEN HACKED".

For reproduce stages I attach in the url https://www.youtube.com/watch?v=aDMd5cjAHZI

potential url with csrf attack https://liberapay.com/talaohu28/edit/username


Regards,
LahatalePutih

## Impact

Change other people's information without having to login

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '59660'
original_report_id: '59660'
title: Multiple Cross Site Request Forgery Vulnerabilities in Concrete5 version 5.7.3.1
weakness: Cross-Site Request Forgery (CSRF)
team_handle: concretecms
created_at: '2015-05-05T09:18:16.152Z'
disclosed_at: '2016-06-26T18:28:02.667Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Multiple Cross Site Request Forgery Vulnerabilities in Concrete5 version 5.7.3.1

## Metadata

- HackerOne Report ID: 59660
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: concretecms
- Disclosed At: 2016-06-26T18:28:02.667Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Concrete5 implements a Synchronizer Token Pattern in order to provide anti-CSRF capabilities, which is done within the Concrete\Core\Validation\CSRF\Token class. However, the application fails to properly use this feature in every block or dashboard page which makes a system state change, such as settings modification. As a result, the application is vulnerable to some Cross Site Request Forgery (CSRF) attacks.

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

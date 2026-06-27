---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163815'
original_report_id: '163815'
title: Lack of CSRF token validation at server side
weakness: Cross-Site Request Forgery (CSRF)
team_handle: gratipay
created_at: '2016-08-27T13:55:11.557Z'
disclosed_at: '2017-07-10T10:00:17.097Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Lack of CSRF token validation at server side

## Metadata

- HackerOne Report ID: 163815
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: gratipay
- Disclosed At: 2017-07-10T10:00:17.097Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Description: Gratipay is not validating csrf token at server side for few requests. So csrf protection is not implemented application wide.

Proof of concept (Video):https://drive.google.com/file/d/0B8z7y7DxxQbwUHY4YTduYzMxbnc/view?usp=sharing

Recommended Fix:
For CSRF Protection:
1. Each critical operation request must be accompanied with a "token"
•Token is:
- Long, Random, not repeated for application lifetime.
- Unique per session or even per operation
- Part of URL in GET
- Hidden Field in POST (forms)
- Attacker cannot know / predict this token and hence cannot create requests to exploit the operation.

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

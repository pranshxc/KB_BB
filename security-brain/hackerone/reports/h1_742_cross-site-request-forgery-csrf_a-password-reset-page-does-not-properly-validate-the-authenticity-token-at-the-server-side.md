---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '742'
original_report_id: '742'
title: A password reset page does not properly validate the authenticity token at
  the server side.
weakness: Cross-Site Request Forgery (CSRF)
team_handle: security
created_at: '2014-01-17T14:53:50.225Z'
disclosed_at: '2014-04-19T20:59:39.929Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# A password reset page does not properly validate the authenticity token at the server side.

## Metadata

- HackerOne Report ID: 742
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: security
- Disclosed At: 2014-04-19T20:59:39.929Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Go to https://hackerone.com/users/password/new and request a new password.
2. go to email, and click on the link.
3. put the new password, submit and intercept the request; remove the authenticity token from the request and now forward it to the server.
4. you will see request still got completed and user logged in. The token did not verify on the server side.

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

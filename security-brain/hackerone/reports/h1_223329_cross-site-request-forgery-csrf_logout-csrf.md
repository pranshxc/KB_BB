---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223329'
original_report_id: '223329'
title: Logout CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: weblate
created_at: '2017-04-24T09:08:31.928Z'
disclosed_at: '2017-05-17T14:20:15.774Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Logout CSRF

## Metadata

- HackerOne Report ID: 223329
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: weblate
- Disclosed At: 2017-05-17T14:20:15.774Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

This is a low risk but want you to know that logout on this domain `demo.weblate.org` did not protect the logout form with csrf token, therefor i can logout any user by sending this url `https://demo.webplate.org/accounts/logout/`.

Logout should have post method with a valid csrf token.

Let me know if you need more info.

Regards
Japz

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

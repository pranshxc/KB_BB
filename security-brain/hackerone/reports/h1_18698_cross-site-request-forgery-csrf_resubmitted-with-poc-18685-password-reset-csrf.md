---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '18698'
original_report_id: '18698'
title: 'Resubmitted with POC #18685 Password reset CSRF'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: relateiq
created_at: '2014-07-01T18:06:26.190Z'
disclosed_at: '2014-09-16T17:46:11.996Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Resubmitted with POC #18685 Password reset CSRF

## Metadata

- HackerOne Report ID: 18698
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: relateiq
- Disclosed At: 2014-09-16T17:46:11.996Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey there
I found out that an attacker can use the password reset link to forge requests because there is no CSRF token in that particular request to validate that request. You should always have a CSRF token in the password reset request.

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

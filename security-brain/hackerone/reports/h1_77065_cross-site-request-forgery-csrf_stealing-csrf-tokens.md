---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '77065'
original_report_id: '77065'
title: Stealing CSRF Tokens
weakness: Cross-Site Request Forgery (CSRF)
team_handle: keybase
created_at: '2015-07-20T20:20:11.116Z'
disclosed_at: '2015-07-22T20:45:48.771Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Stealing CSRF Tokens

## Metadata

- HackerOne Report ID: 77065
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: keybase
- Disclosed At: 2015-07-22T20:45:48.771Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**hello**

I See that you allow cross origin request in API, but you leak CSRF on every invalid request

Vulnerable URL:
===========================
https://keybase.io/_/api/1.0/user/lookup.json?usernames=test%22%3E%3Cimg%20src=x%20onerror=prompt%281%29%3E

Response
====================================
```
xyz....
"csrf_token":"lgHZIDVjN2RiOGNiZjNhZjkxYzRjYTgzMjI3MmJmY2Q1ZTA4zlWtVxXOAAFRgMDEIPn2lkhARPmRDF5dcdo+u+y+DyNuLvCZsk6wbWih8i8a"}
```

POC is attached.

**Regards,
Wesecureapp**

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

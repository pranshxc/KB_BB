---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '395246'
original_report_id: '395246'
title: ███████ Site Exposes █████████ forms
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2018-08-14T19:53:38.495Z'
disclosed_at: '2019-04-05T19:45:03.914Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# ███████ Site Exposes █████████ forms

## Metadata

- HackerOne Report ID: 395246
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2019-04-05T19:45:03.914Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary

The █████ site (https://██████.mil/) allows authenticated users to submit ██████ e-forms. Due to a vulnerability in this system, any authenticated user can access the full █████████ e-form of any other user.

## Steps to reproduce

1. Intercept an authenticated request on █████████ containing an Authorization header.
2. Replace the url with `█████████`. Observe that the id in the url can be incremented/decremented to view recently generated OMPFs.
3. Upon submitting the request, the user's full ███████ form JSON response will be sent.

## Impact

Access to ████ is possible through either a Department of Defense Self-Service logon, CAC card, or █████████password. Thus, a compromise of a single account on any of these systems would allow for unrestricted access to all ████ forms.

The ████ form includes the following
- PII such as SSN, DoB, addresses, etc
- Personal remarks
- Other fields related to security clearances, education, maritial status, etc

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

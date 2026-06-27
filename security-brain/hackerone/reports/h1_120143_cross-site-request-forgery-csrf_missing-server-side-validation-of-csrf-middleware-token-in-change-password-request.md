---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '120143'
original_report_id: '120143'
title: Missing Server Side Validation of CSRF Middleware Token in Change Password
  Request
weakness: Cross-Site Request Forgery (CSRF)
team_handle: veris
created_at: '2016-03-02T15:32:36.389Z'
disclosed_at: '2016-06-12T16:04:43.892Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Missing Server Side Validation of CSRF Middleware Token in Change Password Request

## Metadata

- HackerOne Report ID: 120143
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: veris
- Disclosed At: 2016-06-12T16:04:43.892Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I have found that CSRF Middleware Token is not getting validated at server side in CHANGE PASSWORD request. This request even works without csrfmiddlewaretoken.

Steps to Reproduce:

1. Login to your Veris View Account.
2. Go to Settings.
3. Change your password.
4. Submit the form.
5. Intercept this request in burp suite.
6. Remove csrfmiddlewaretoken parameter from the request.
7. Forward the request.
8. You'll notice the success message as Password changed Successfully.

Proof of Concept: Please find it attached.

Do evaluate it and inform me accordingly.

Best Regards,

Hely H. Shah

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

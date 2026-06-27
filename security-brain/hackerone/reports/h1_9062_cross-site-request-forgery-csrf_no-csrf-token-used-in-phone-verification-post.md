---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9062'
original_report_id: '9062'
title: No CSRF token used in Phone Verification POST
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mailru
created_at: '2014-04-22T13:19:51.521Z'
disclosed_at: '2014-06-11T09:01:06.930Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# No CSRF token used in Phone Verification POST

## Metadata

- HackerOne Report ID: 9062
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mailru
- Disclosed At: 2014-06-11T09:01:06.930Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

When I tried to register in mail.ru,I submitted my phone number and Got a verification code in my phone.
During submission of that code,I saw that POST goes without any CSRF tokens.And I identified two other vulnerabilities on that procedure.

1. No Session Verification on server side while submitting the code.This phone verification system should be designed in such a way,so that no one could use that without a proper session.Now with the present design,anyone can submit codes randomly without any session verification.
2. No limitation on random submissions on that form.Any user can try unlimited number of codes on that form.Mail.ru does not have any limit on number of wrong tries at this endpoint.This should be checked.
3. No CSRF token is available on this form submission.Mail.ru should impose CSRF tokens in this form to protect it against CSRF attacks.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223525'
original_report_id: '223525'
title: Spamming any user from Reset Password Function
weakness: Violation of Secure Design Principles
team_handle: weblate
created_at: '2017-04-24T17:59:43.823Z'
disclosed_at: '2017-05-17T15:20:12.672Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Spamming any user from Reset Password Function

## Metadata

- HackerOne Report ID: 223525
- Weakness: Violation of Secure Design Principles
- Program: weblate
- Disclosed At: 2017-05-17T15:20:12.672Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It is possible to spam any user whose email-id is known.

csrfmiddlewaretoken token can be used more than one.
Users can be spammed heavily by just Brute force attack on password reset page.

Implementtion:
Implement a Captcha.

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

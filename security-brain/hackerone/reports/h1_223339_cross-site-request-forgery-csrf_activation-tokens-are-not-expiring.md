---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223339'
original_report_id: '223339'
title: Activation tokens are not expiring
weakness: Cross-Site Request Forgery (CSRF)
team_handle: weblate
created_at: '2017-04-24T09:27:49.633Z'
disclosed_at: '2017-05-17T14:18:37.808Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Activation tokens are not expiring

## Metadata

- HackerOne Report ID: 223339
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: weblate
- Disclosed At: 2017-05-17T14:18:37.808Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Domain: `demo.weblate.org`

In this bug, maybe it is low risk but i have found a way to login any person to the attackers account, therefor when any user login to attackers account, the attacker can see the users activity on attackers account. The issue relies on the password reset.

### Stes to reproduce:

  1. Create fake account and generate reset password link.
  2. Go to email, get the reset password link and send it to victim
  3. When victim click the link, victim automatically login to attackers account.

Please note that when the victim clicks the reset password link, victim will redirect to the page that ask to insert password, but even if the victim did not inout password, and click the profile name at the upper right of the reset password page. The victim will redirect to attackers profile account, meaning upon clicking the reset password link, victim already logged in to attackers account.

### Mitigation:

Do not automatically login the user after clicking the reset password link.

Let me know if you need more information.

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

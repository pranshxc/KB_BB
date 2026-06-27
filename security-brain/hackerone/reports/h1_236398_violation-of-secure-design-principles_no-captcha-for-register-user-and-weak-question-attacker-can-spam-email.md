---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '236398'
original_report_id: '236398'
title: no captcha for register user and weak question attacker can spam email
weakness: Violation of Secure Design Principles
team_handle: weblate
created_at: '2017-06-04T10:01:49.028Z'
disclosed_at: '2019-10-26T07:37:59.257Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 27
tags:
- hackerone
- violation-of-secure-design-principles
---

# no captcha for register user and weak question attacker can spam email

## Metadata

- HackerOne Report ID: 236398
- Weakness: Violation of Secure Design Principles
- Program: weblate
- Disclosed At: 2019-10-26T07:37:59.257Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi
in https://demo.weblate.org/accounts/register/ attacker can register with same email and if didnt click on confirm link attacker can make request with infinite loop

so attacker can spam another email with your service

question is so simple any bot that can read source can generate answer for it

you can make fix with if email register in database user cant make register request within 24 hour

good luck

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223531'
original_report_id: '223531'
title: User Enumeration when adding email to account
team_handle: weblate
created_at: '2017-04-24T18:23:39.916Z'
disclosed_at: '2017-05-17T15:20:24.394Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# User Enumeration when adding email to account

## Metadata

- HackerOne Report ID: 223531
- Weakness: 
- Program: weblate
- Disclosed At: 2017-05-17T15:20:24.394Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It is possible to find all the Register emails which can be use for spam or other purposes

csrfmiddlewaretoken token can be used more than one.
All Register Email can be found by just brute force attack.
Your web endpoint https://demo.weblate.org/accounts/email/ when changing email after login.
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

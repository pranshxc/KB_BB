---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '675398'
original_report_id: '675398'
title: '[invalid][false-positive] csrftoken on profile page'
weakness: Violation of Secure Design Principles
team_handle: wakatime
created_at: '2019-08-17T04:04:01.824Z'
disclosed_at: '2019-08-20T07:32:21.557Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# [invalid][false-positive] csrftoken on profile page

## Metadata

- HackerOne Report ID: 675398
- Weakness: Violation of Secure Design Principles
- Program: wakatime
- Disclosed At: 2019-08-20T07:32:21.557Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

step of reproduce-
1. Go to https://wakatime.com and create account.
2. login account after that go public profile.
3. after that change the full name and intercept brup suite and delete csrftoken.
4. After forward then you see name was changed.

## Impact

Violation of Secure Design Principles

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

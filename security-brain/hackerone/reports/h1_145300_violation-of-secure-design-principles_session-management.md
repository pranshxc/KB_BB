---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145300'
original_report_id: '145300'
title: Session Management
weakness: Violation of Secure Design Principles
team_handle: paragonie
created_at: '2016-06-17T06:46:52.777Z'
disclosed_at: '2016-06-17T17:28:24.663Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Session Management

## Metadata

- HackerOne Report ID: 145300
- Weakness: Violation of Secure Design Principles
- Program: paragonie
- Disclosed At: 2016-06-17T17:28:24.663Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

When i click on forgot password i will get a reset link to my account
when i login with the same email and password it will login to my account
now if i open the reset link in another web browser and change the password and login to my account the session in the first browser is not expired i am able to use my account in both browsers

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

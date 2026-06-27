---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '276123'
original_report_id: '276123'
title: Password Complexity Not Enforced On Password Change
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2017-10-10T14:38:29.036Z'
disclosed_at: '2018-03-03T13:55:25.389Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: owncloud/core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Password Complexity Not Enforced On Password Change

## Metadata

- HackerOne Report ID: 276123
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2018-03-03T13:55:25.389Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi!

Owncloud does not enforce password complexity on password change, so it's possible to use passwords of any size or form. 

In example I can set my password to be "a" or "qwerty".

__________________________________________________________________
How to reproduce:
Change your password to something that does not match your required complexity.
__________________________________________________________________

__________________________________________________________________
Proof Of Concept:
Login with my dummy account
account --> "testingdisp2@gmail.com"
password --> "q"
__________________________________________________________________

Thanks!
WdeM

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

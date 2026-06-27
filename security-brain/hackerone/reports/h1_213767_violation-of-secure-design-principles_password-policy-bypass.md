---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '213767'
original_report_id: '213767'
title: Password Policy Bypass
weakness: Violation of Secure Design Principles
team_handle: legalrobot
created_at: '2017-03-15T19:12:09.828Z'
disclosed_at: '2017-08-28T06:14:15.929Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Password Policy Bypass

## Metadata

- HackerOne Report ID: 213767
- Weakness: Violation of Secure Design Principles
- Program: legalrobot
- Disclosed At: 2017-08-28T06:14:15.929Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi LegalRobot team,

I noticed that there is a strong Password policy enforced on login page which only allows passwords with 8 or more characters and they need to be a combination of Capital letters, small letters, and numbers/special characters.
However i found that i am able to bypass this Password policy when trying to change password and set a very weak password on account.

I have attached steps to reproduce the issue (set the character 'a' as password) in document, please take a look at it.

Alternatively, i can give you credentials for my account which has password set to 123

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

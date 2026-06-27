---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '273560'
original_report_id: '273560'
title: Validation of Password reset tokens
weakness: Violation of Secure Design Principles
team_handle: wakatime
created_at: '2017-10-01T07:59:47.492Z'
disclosed_at: '2017-10-01T14:56:19.826Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Validation of Password reset tokens

## Metadata

- HackerOne Report ID: 273560
- Weakness: Violation of Secure Design Principles
- Program: wakatime
- Disclosed At: 2017-10-01T14:56:19.826Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Dear sir,
At first, i am very happy to report an issue.  Before three months, i reported to wakatime and again i am reporting another issue now.

Note:-This report is similar to #244614 which was previously reported at the start of this bug bounty program.

Vulnerability:-
->If two password reset tokens are generated at a time, then the first reset token doesn't expire after the generation of second reset token.
->Similarly, if 100 password reset tokens are generated then only the last generated reset token should be valid, but here all 100 tokens are being valid until any one in it is used to change password.
->As per industrial standards, and also as a best security issue, only one token should be valid at a time but not all the tokens.

I hope that you will resolve this issue as i am reporting a valid issue.  Any issues, please let me know

Thank you

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

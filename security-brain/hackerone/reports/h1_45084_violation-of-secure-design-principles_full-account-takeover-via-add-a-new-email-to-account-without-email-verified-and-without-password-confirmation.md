---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '45084'
original_report_id: '45084'
title: Full account takeover via Add a New Email to account without email verified
  and without password confirmation.
weakness: Violation of Secure Design Principles
team_handle: vimeo
created_at: '2015-01-25T01:05:36.959Z'
disclosed_at: '2015-03-06T07:26:26.764Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Full account takeover via Add a New Email to account without email verified and without password confirmation.

## Metadata

- HackerOne Report ID: 45084
- Weakness: Violation of Secure Design Principles
- Program: vimeo
- Disclosed At: 2015-03-06T07:26:26.764Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

#Description :
This is especially important if the application is commonly used in shared computers such as cyber cafes or airport terminals
##Bug :
 Add a New Email to account without email verified and without password confirmation when the leaves open email ,Leading to the theft of account In less than a minute by reset password .
##PoC:
http://goo.gl/tsqR60

#Suggestion for fix a bug :
Request Confirm password to add this email.
##Example :
http://goo.gl/y3mK0C

Regards,
Ahmed El-Mahalawy

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '98469'
original_report_id: '98469'
title: Email Verification Link can be Used as Password Reset Link!
weakness: Improper Authentication - Generic
team_handle: deriv
created_at: '2015-11-07T15:43:12.214Z'
disclosed_at: '2015-12-03T11:07:42.983Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Email Verification Link can be Used as Password Reset Link!

## Metadata

- HackerOne Report ID: 98469
- Weakness: Improper Authentication - Generic
- Program: deriv
- Disclosed At: 2015-12-03T11:07:42.983Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello again!

basically,I have found a new issue which allows attacker to use a Email Verification Link and make it into a password reset link!

Proof Of Concept:
When you Send a Email Verification Link
It looks like this "https://www.binary.com/user/validate_link?step=account&verify_token=q4b4QVyLZD9daVpAdiXAIiAExC8DaGmqFPk8wNt9nTqAm7Pa&l=EN"

Remove "step=account" from the URL, and tadaa! you will see once u enter the email you can change password!

Thank you,
-Karim

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

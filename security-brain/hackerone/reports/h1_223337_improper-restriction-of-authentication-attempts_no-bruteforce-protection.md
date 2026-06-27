---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223337'
original_report_id: '223337'
title: No BruteForce Protection
weakness: Improper Restriction of Authentication Attempts
team_handle: weblate
created_at: '2017-04-24T09:26:18.124Z'
disclosed_at: '2017-05-17T18:04:05.577Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# No BruteForce Protection

## Metadata

- HackerOne Report ID: 223337
- Weakness: Improper Restriction of Authentication Attempts
- Program: weblate
- Disclosed At: 2017-05-17T18:04:05.577Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works.

hosted.weblate.org/accounts/login/ 

This login page doesn't have any protection against password-guessing attacks (brute force attacks). It's recommended to implement some type of account lockout after a defined number of incorrect password attempts. Consult Web references for more information about fixing this problem.

**The impact of this vulnerability:**

An attacker may attempt to discover a weak password by systematically trying every possible combination of letters, numbers, and symbols until it discovers the one correct combination that works.

**How to fix this vulnerability:**

It's recommended to implement some type of account lockout after a defined number of incorrect password attempts.

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

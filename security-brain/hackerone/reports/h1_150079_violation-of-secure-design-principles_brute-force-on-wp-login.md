---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150079'
original_report_id: '150079'
title: Brute force on wp-login
weakness: Violation of Secure Design Principles
team_handle: iandunn-projects
created_at: '2016-07-08T19:40:45.966Z'
disclosed_at: '2016-08-18T01:18:08.025Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Brute force on wp-login

## Metadata

- HackerOne Report ID: 150079
- Weakness: Violation of Secure Design Principles
- Program: iandunn-projects
- Disclosed At: 2016-08-18T01:18:08.025Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works. 

This login page doesn't have any protection against password-guessing attacks (brute force attacks). It's recommended to implement some type of account lockout after a defined number of incorrect password attempts. 

Consult Web references for more information about fixing this problem.

Affected items:
/wordpress/wp-login.php 

The impact of this vulnerability?
An attacker may attempt to discover a weak password by systematically trying every possible combination of letters, numbers, and symbols until it discovers the one correct combination that works.

How to fix this vulnerability:
It's recommended to implement some type of account lockout after a defined number of incorrect password attempts.

Web references:
https://www.owasp.org/index.php/Blocking_Brute_Force_Attacks

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

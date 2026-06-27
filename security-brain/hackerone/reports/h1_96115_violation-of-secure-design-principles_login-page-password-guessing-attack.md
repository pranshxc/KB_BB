---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '96115'
original_report_id: '96115'
title: Login page password-guessing attack
weakness: Violation of Secure Design Principles
team_handle: revive_adserver
created_at: '2015-10-27T16:47:40.969Z'
disclosed_at: '2024-04-19T13:50:18.408Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
- violation-of-secure-design-principles
---

# Login page password-guessing attack

## Metadata

- HackerOne Report ID: 96115
- Weakness: Violation of Secure Design Principles
- Program: revive_adserver
- Disclosed At: 2024-04-19T13:50:18.408Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability description :-
A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works. 

This login page doesn't have any protection against password-guessing attacks (brute force attacks). It's recommended to implement some type of account lockout after a defined number of incorrect password attempts. Consult Web references for more information about fixing this problem. 

Attack details :-
The scanner tested 100 invalid credentials and no account lockout was detected.

The impact of this vulnerability :-
An attacker may attempt to discover a weak password by systematically trying every possible combination of letters, numbers, and symbols until it discovers the one correct combination that works.

How to fix this vulnerability :-
It's recommended to implement some type of account lockout after a defined number of incorrect password attempts.

Replication Steps :-

1. I go to login page.
2. intercept Request in Burp suite.
3. request send to intruder .
4. request add username and password.
5. select cluster bomb.
6. select payload username and password.
7. start intruder.

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

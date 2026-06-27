---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8017'
original_report_id: '8017'
title: Login page password-guessing attack
team_handle: localize
created_at: '2014-04-18T11:47:47.259Z'
disclosed_at: '2014-04-20T15:49:41.172Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 3
tags:
- hackerone
---

# Login page password-guessing attack

## Metadata

- HackerOne Report ID: 8017
- Weakness: 
- Program: localize
- Disclosed At: 2014-04-20T15:49:41.172Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Login page password-guessing attack


Vulnerability description

A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works. 

This login page doesn't have any protection against password-guessing attacks (brute force attacks). It's recommended to implement some type of account lockout after a defined number of incorrect password attempts. Consult Web references for more information about fixing this problem. 

This vulnerability affects http://www.localize.io/

 Attack details
I tested 10 invalid credentials and no account lockout was detected.

The impact of this vulnerability
An attacker may attempt to discover a weak password by systematically trying every possible combination of letters, numbers, and symbols until it discovers the one correct combination that works.

How to fix this vulnerability
It's recommended to implement some type of account lockout after a defined number of incorrect password attempts. 

Web references
Blocking Brute Force Attacks
http://www.owasp.org/index.php/Blocking_Brute_Force_Attacks

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

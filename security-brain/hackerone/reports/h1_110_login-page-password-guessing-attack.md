---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '110'
original_report_id: '110'
title: Login page password-guessing attack
team_handle: security
created_at: '2013-10-31T20:55:10.087Z'
disclosed_at: '2014-01-16T10:31:34.000Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 17
tags:
- hackerone
---

# Login page password-guessing attack

## Metadata

- HackerOne Report ID: 110
- Weakness: 
- Program: security
- Disclosed At: 2014-01-16T10:31:34.000Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works. 

hackerone.com page doesn't have any protection against password-guessing attacks (brute force attacks). It's recommended to implement some type of account lockout after a defined number of incorrect password attempts.

I personally tried many times with wrong password even though no account lockout was detected.

Fix : Implement captcha

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

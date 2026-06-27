---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7869'
original_report_id: '7869'
title: No BruteForce Protection
weakness: Cryptographic Issues - Generic
team_handle: localize
created_at: '2014-04-17T18:24:14.705Z'
disclosed_at: '2014-04-22T05:01:18.355Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# No BruteForce Protection

## Metadata

- HackerOne Report ID: 7869
- Weakness: Cryptographic Issues - Generic
- Program: localize
- Disclosed At: 2014-04-22T05:01:18.355Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works. 

http://www.localize.io/

This login page doesn't have any protection against password-guessing attacks (brute force attacks). It's recommended to implement some type of account lockout after a defined number of incorrect password attempts. Consult Web references for more information about fixing this problem. 

The impact of this vulnerability:-

An attacker may attempt to discover a weak password by systematically trying every possible combination of letters, numbers, and symbols until it discovers the one correct combination that works.

How to fix this vulnerability:-

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '744692'
original_report_id: '744692'
title: The login of Hotor Not is Vulnerable to bruteforce.
weakness: Improper Restriction of Authentication Attempts
team_handle: bumble
created_at: '2019-11-22T16:36:11.608Z'
disclosed_at: '2020-01-23T18:16:56.069Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 58
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# The login of Hotor Not is Vulnerable to bruteforce.

## Metadata

- HackerOne Report ID: 744692
- Weakness: Improper Restriction of Authentication Attempts
- Program: bumble
- Disclosed At: 2020-01-23T18:16:56.069Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I was able to validate that The Login of HotorNot is Vulnerable to BruteForcing .

Steps to reproduce:
1. https://hotornot.com/signin
2.Use Burp intruder attack for BruteForcing 
3.Send as many requests you want.

Fix:
Proper mitigation of BruteForcing should be done using Ratelimitng etc implementation.

## Impact

If attacker successfully Bruteforces the he/she might takeover it.Which might lead in users Privacy Violation

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

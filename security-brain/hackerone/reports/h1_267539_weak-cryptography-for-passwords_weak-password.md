---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '267539'
original_report_id: '267539'
title: Weak password
weakness: Weak Cryptography for Passwords
team_handle: radancy
created_at: '2017-09-11T16:06:02.269Z'
disclosed_at: '2018-01-10T14:20:24.805Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- weak-cryptography-for-passwords
---

# Weak password

## Metadata

- HackerOne Report ID: 267539
- Weakness: Weak Cryptography for Passwords
- Program: radancy
- Disclosed At: 2018-01-10T14:20:24.805Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

It takes ash123456789123456789 as a password,which is not secure.It can be cracked using Dictionary,brute force etc attacks.

Impact:
If password complexity is not enforced people may tend to put  easily guessable password which may be exploitable for a malicious user.

Solution-To make it more secure,you should use more secure password such as use of upper case,Special Characters,etc.

Steps to reproduce:

1.First goto https://mijn.werkenbijdefensie.nl/profiel_aanmaken/
2.type necessary details
3.Type password-ash123456789123456789
4.Click on create account

Chrome latest
Windows 10 Enterprise Edition

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

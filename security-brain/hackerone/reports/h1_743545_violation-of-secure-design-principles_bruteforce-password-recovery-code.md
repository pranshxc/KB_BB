---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '743545'
original_report_id: '743545'
title: Bruteforce password recovery code
weakness: Violation of Secure Design Principles
team_handle: bumble
created_at: '2019-11-21T17:54:12.936Z'
disclosed_at: '2020-01-18T17:45:58.360Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 252
tags:
- hackerone
- violation-of-secure-design-principles
---

# Bruteforce password recovery code

## Metadata

- HackerOne Report ID: 743545
- Weakness: Violation of Secure Design Principles
- Program: bumble
- Disclosed At: 2020-01-18T17:45:58.360Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
It's possible to bruteforce recovery code from SMS as iOS application doesn't have limits for incorrect inputs. I have tried 50+ different combinations until I reached code from SMS.

## Steps To Reproduce
1. Click "Use another option" on application startup view
1. Enter your phone number
1. Click "Forgotten number"
1. Click "OK" on pop-up window
1. Bruteforce 4 digits code 

## PoC video
https://youtu.be/QV80pD0wZsE

## Mitigation
1. Limit quantity of attempts to enter recovery code
1. Don't store recovery code on target device to compare it with user's input

## Details
Devices: Iphone SE (13.2), Iphone 6s (12.4)
App: Bumble (5.140.0)

## Impact

Account takeover.

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

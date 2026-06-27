---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1188633'
original_report_id: '1188633'
title: Linux Desktop application "sifnoded" executable does not use Pie / no ASLR
weakness: Violation of Secure Design Principles
team_handle: sifchain
created_at: '2021-05-07T20:30:08.100Z'
disclosed_at: '2021-12-09T19:48:57.448Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Linux Desktop application "sifnoded" executable does not use Pie / no ASLR

## Metadata

- HackerOne Report ID: 1188633
- Weakness: Violation of Secure Design Principles
- Program: sifchain
- Disclosed At: 2021-12-09T19:48:57.448Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Sifchain,
sifnoded binary from the Linux application is no position independent executable
PoC;
**$file sifnoded
Output will be like ;
███████

Position independent executables are required for full ASLR support on Linux. Non-pie-binaries are loaded to a fixed location, thus allowing ROP attacks.
Reference for this report; #415272
Thanks.

## Impact

A simple memory corruption bug like a buffer overflow can easily lead to a remote code execution bug. With ASLR these bugs are much harder and sometimes impossible to exploit.

LSB executable should be "LSB shared object" or "LSB pie executable"

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

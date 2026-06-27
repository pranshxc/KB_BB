---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '219323'
original_report_id: '219323'
title: CSV injection in gratipay.com via payment history export feature.
weakness: Command Injection - Generic
team_handle: gratipay
created_at: '2017-04-07T15:58:07.218Z'
disclosed_at: '2017-11-03T07:55:04.511Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- command-injection-generic
---

# CSV injection in gratipay.com via payment history export feature.

## Metadata

- HackerOne Report ID: 219323
- Weakness: Command Injection - Generic
- Program: gratipay
- Disclosed At: 2017-11-03T07:55:04.511Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I discovered this issues thanks to Matt who pointed out that the participant's name is directly placed into a CSV file: https://github.com/gratipay/gratipay.com/issues/4399#issuecomment-292250609

# Summary
---

Gratipay allows users to export payment history as a .csv file. By injecting a payload into a participant's name an attacker could exfiltrate data or execute code on the target machine. For instance, with `=cmd|' /C calc'!A0` I am able to open up `calc.exe` on Windows.

# Steps to reproduce
---

1) Create a user A called `=cmd|' /C calc'!A0`;
2) User B donates a small sum to user A;
3) Export payment history from B;
4) Open the .csv file on a Windows machine.

Result: `calc.exe` pops up.

# Fix
---

Prefix `=`, `+`, `-` and `@` symbols with a `'` in issues when exporting them to a .csv file.

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

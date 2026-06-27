---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6883'
original_report_id: '6883'
title: Bruteforcing irccloud login
weakness: Violation of Secure Design Principles
team_handle: irccloud
created_at: '2014-04-10T21:41:29.872Z'
disclosed_at: '2014-05-26T08:35:47.565Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Bruteforcing irccloud login

## Metadata

- HackerOne Report ID: 6883
- Weakness: Violation of Secure Design Principles
- Program: irccloud
- Disclosed At: 2014-05-26T08:35:47.565Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is no mitigation, defenses in anyway or a lockout mechanism in the login page. A malicious minded user can continually tries to brute force an account password.

I have tried to input 20 incorrect password and I have not been lockout, tried the corrct password in the 21st time and it login successfully.

Kindly take a look sir. kindly also let me know if you needed more information.

Clifford

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

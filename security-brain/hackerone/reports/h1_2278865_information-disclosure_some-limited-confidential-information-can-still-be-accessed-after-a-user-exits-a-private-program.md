---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2278865'
original_report_id: '2278865'
title: Some limited confidential information can still be accessed after a user exits
  a private program
weakness: Information Disclosure
team_handle: security
created_at: '2023-12-08T20:57:05.654Z'
disclosed_at: '2024-01-19T13:11:44.014Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 74
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Some limited confidential information can still be accessed after a user exits a private program

## Metadata

- HackerOne Report ID: 2278865
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2024-01-19T13:11:44.014Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Good morning team!!!
I identified a bug where it is possible to access some limited confidential information from a private program even after you have already exited that program. 
information like:
:number of domains
:Bounties paid
:Number of hackers paid
:Response efficiency
:Minimum reward and maximum reward
:Sobre

steps:
1:do you accept a private invitation
2:you add this program to your favorites
3:the expiry date for sending reports arrives
4:Now you can no longer send reports to this program or have access to its policy page
5:now go to opportunities -> My programs
6:And there is your program and you have access to the information mentioned above

## Impact

Disclosure of private program information

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '108928'
original_report_id: '108928'
title: Signals get affected once reports closed as self
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-01-07T05:10:02.293Z'
disclosed_at: '2016-04-25T08:56:37.845Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- violation-of-secure-design-principles
---

# Signals get affected once reports closed as self

## Metadata

- HackerOne Report ID: 108928
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-04-25T08:56:37.845Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

According to your documentation "https://hackerone.com/blog/introducing-signal-and-impact"

#Examples 

Activity(Reputation) 

Report Self close as (N/A) :  0  .  

its means Signals are not  affected . But our case signal affected  by  self-closed reports

Signals doesn't take the 0 baseline into consideration for  self-closed reports

Regards,
kpr

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

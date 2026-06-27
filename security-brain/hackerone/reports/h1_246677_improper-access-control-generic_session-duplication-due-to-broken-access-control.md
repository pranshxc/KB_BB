---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '246677'
original_report_id: '246677'
title: Session Duplication due to Broken Access Control
weakness: Improper Access Control - Generic
team_handle: wakatime
created_at: '2017-07-08T15:42:40.205Z'
disclosed_at: '2017-07-10T07:33:51.921Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 2
tags:
- hackerone
- improper-access-control-generic
---

# Session Duplication due to Broken Access Control

## Metadata

- HackerOne Report ID: 246677
- Weakness: Improper Access Control - Generic
- Program: wakatime
- Disclosed At: 2017-07-10T07:33:51.921Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Due to improper validation of user before generating an API-KEY and improper measures taken at the time of password reset, it is possible to generate a parallel session at the attacker's end.

Proof of concept video is attached to confirm the vulnerability and to demonstrate the Impact of this _logical_ bug.

Steps to Reproduce
=============
Attacker
---------
- Create an account with victims email.
- Download the coding platforms and get API-KEY.
- He can code from the platforms using the victims API-key.

Victim
-------
- User fails to create an account, due to email already registered and does a password reset.
- Downloads the coding platform and get API-KEY.
- He codes using API-KEY.

It is possible for the Attacker and Victim, for coding at the same time, which will be shown at the dashboard. Attacker can reduce the difficulty and can damage the reputation of the coder.

 Impact
=====

__Attacker can brute-force email and register multiple account on wakatime to get API-Key of many users.__
 
Improper rank calculation.

Session duplication by the attacker

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

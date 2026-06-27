---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1344951'
original_report_id: '1344951'
title: Expired SSL Certificate allows credentials steal
weakness: Violation of Secure Design Principles
team_handle: deptofdefense
created_at: '2021-09-20T15:04:57.013Z'
disclosed_at: '2021-11-29T22:06:47.987Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- violation-of-secure-design-principles
---

# Expired SSL Certificate allows credentials steal

## Metadata

- HackerOne Report ID: 1344951
- Weakness: Violation of Secure Design Principles
- Program: deptofdefense
- Disclosed At: 2021-11-29T22:06:47.987Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi security Team!
I've found this website with no valid SSL Certificate.

https://██████████

Certificate has expired 314 days ago.

## Impact

Error message can appear on page and **user can have his credentials stolen by an attacker capturing the network data.**

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit: https://██████████ and check the SSL Certificate. It was expired in november 2020.

## Suggested Mitigation/Remediation Actions

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

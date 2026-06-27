---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '59666'
original_report_id: '59666'
title: Unsafe usage of Host HTTP header in Concrete5 version 5.7.3.1
weakness: Violation of Secure Design Principles
team_handle: concretecms
created_at: '2015-05-05T09:26:07.592Z'
disclosed_at: '2018-01-11T21:59:17.230Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Unsafe usage of Host HTTP header in Concrete5 version 5.7.3.1

## Metadata

- HackerOne Report ID: 59666
- Weakness: Violation of Secure Design Principles
- Program: concretecms
- Disclosed At: 2018-01-11T21:59:17.230Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Concrete5 is affected by a design issue related to the Host HTTP header. Such header is being used to define the base URL for the application. Since the Host header can be arbitrarily manipulated by an attacker, this can have some security impacts.

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

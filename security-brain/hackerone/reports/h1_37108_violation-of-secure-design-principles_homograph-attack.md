---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '37108'
original_report_id: '37108'
title: Homograph attack.
weakness: Violation of Secure Design Principles
team_handle: x
created_at: '2014-11-22T10:43:43.834Z'
disclosed_at: '2015-01-01T03:40:56.115Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Homograph attack.

## Metadata

- HackerOne Report ID: 37108
- Weakness: Violation of Secure Design Principles
- Program: x
- Disclosed At: 2015-01-01T03:40:56.115Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

In the report  31193      cmiller said    "Twitter does warn if the user tries to visit a malicious URL while passing through our t.co URL shortening service. Thanks!"


URL redirection warning not given for punny code URL.


ATTACK:
 I mainly envision using this as an attack against admins of programs that use twitter. for example, if a bad guy can put up a spoof site behind one of these IDN links that one of the admins carelessly enters their credentials into, then the bad guy can go do bad stuff against the target site...

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

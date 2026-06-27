---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1591504'
original_report_id: '1591504'
title: The software does not implement sufficient measures to prevent multiple failed
  authentication attempts within in a short time frame, making it more su
weakness: Improper Restriction of Authentication Attempts
team_handle: linkedin
created_at: '2022-06-05T05:14:29.349Z'
disclosed_at: '2022-06-15T18:18:31.610Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: www.linkedin.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# The software does not implement sufficient measures to prevent multiple failed authentication attempts within in a short time frame, making it more su

## Metadata

- HackerOne Report ID: 1591504
- Weakness: Improper Restriction of Authentication Attempts
- Program: linkedin
- Disclosed At: 2022-06-15T18:18:31.610Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

example->

String username = request.getParameter("username");
String password = request.getParameter("password");

int authResult = authenticateUser(username, password);



the security tokens can be bypassed easily , they are dont make user account safe .

//script -> check attached  file

## Impact

Technical Impact: Bypass Protection Mechanism
An attacker could perform an arbitrary number of authentication attempts using different passwords, and eventually gain access to the targeted account.

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

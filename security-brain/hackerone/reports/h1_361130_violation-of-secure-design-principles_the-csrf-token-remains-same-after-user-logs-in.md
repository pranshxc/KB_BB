---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361130'
original_report_id: '361130'
title: The csrf token remains same after user logs in
weakness: Violation of Secure Design Principles
team_handle: liberapay
created_at: '2018-06-03T18:55:18.745Z'
disclosed_at: '2018-06-04T09:05:45.391Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# The csrf token remains same after user logs in

## Metadata

- HackerOne Report ID: 361130
- Weakness: Violation of Secure Design Principles
- Program: liberapay
- Disclosed At: 2018-06-04T09:05:45.391Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

###Description
As the CSRF token doesn't change after login. Any other user that uses the same workstation is vulnerable. A safer way would be to use dynamic CSRF token or just change the token after login, so attacker doesn't get hold of this.

### Details of the attacks scenario in a shared workstation environment

1. The attacker simply copies the authenticity token. This token is the only protection against the CSRF attack.
2. Any other user that uses the workstation after that is vulnerable to CSRF. The attacker simply needs to craft a link with the required GET or POST method as he already have the CSRF token and send it to the victim via email, chat etc.
3. he attacker can trick the victim in doing anything he wants without the user being aware of it.

## Impact

Any other user that uses the same workstation is vulnerable to CSRF attack

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

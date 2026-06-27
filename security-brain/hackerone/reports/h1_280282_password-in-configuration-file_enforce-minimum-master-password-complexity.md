---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280282'
original_report_id: '280282'
title: Enforce minimum master password complexity
weakness: Password in Configuration File
team_handle: torproject
created_at: '2017-10-19T06:15:18.766Z'
disclosed_at: '2017-10-19T10:50:33.686Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
tags:
- hackerone
- password-in-configuration-file
---

# Enforce minimum master password complexity

## Metadata

- HackerOne Report ID: 280282
- Weakness: Password in Configuration File
- Program: torproject
- Disclosed At: 2017-10-19T10:50:33.686Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi Team, 

Actual results:

There is no password complexity set for Master password in about:preferences#security , Because I was able to set my password like 123,123456,www, admin etc which is really common, apart from that we can use spaces as well in master password i was able to set space as my master password :/ 

Expected results:
Recommendation - Provide robust rules including upper lower letters, special characters etc.

Ref: https://bugzilla.mozilla.org/show_bug.cgi?id=1408427 

Regards
Dhiraj

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

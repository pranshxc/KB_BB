---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '994612'
original_report_id: '994612'
title: jira discloser information
weakness: Information Disclosure
team_handle: informatica
created_at: '2020-09-30T04:30:22.257Z'
disclosed_at: '2022-10-03T13:03:54.800Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# jira discloser information

## Metadata

- HackerOne Report ID: 994612
- Weakness: Information Disclosure
- Program: informatica
- Disclosed At: 2022-10-03T13:03:54.800Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The ticket raising system used by informatica suffers from an informational vulnerability where in an attacker can view certain details about open bugs or project information of informatica. Details include  names and potentially  and ticket names which an unauthorized personnel can view without login that can be very useful to an attacker.

endpoints:

https://infajira.informatica.com/secure/QueryComponent!Default.jspa

## Impact

attacker miss use this information

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

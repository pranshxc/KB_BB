---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2323303'
original_report_id: '2323303'
title: Program admins could add verified domains to an organization
weakness: Improper Access Control - Generic
team_handle: security
created_at: '2024-01-17T12:00:37.422Z'
disclosed_at: '2024-03-07T15:10:05.577Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 66
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Program admins could add verified domains to an organization

## Metadata

- HackerOne Report ID: 2323303
- Weakness: Improper Access Control - Generic
- Program: security
- Disclosed At: 2024-03-07T15:10:05.577Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

in hackerone according to the documentation https://docs.hackerone.com/en/articles/8490190-domain-verification only an organization admin could add verified domain .but there is an bypass.

steps to reproduce:
1. create an sandbox
2.remove org admin permission(you must add program admin permission before removing org admin) 
3. go to the url
      https://hackerone.com/<program you are admin of>/domain_ownerships/new
4.from there you will be able to add verified domain in the org

## Impact

access of restricted feature
privilage escalation

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

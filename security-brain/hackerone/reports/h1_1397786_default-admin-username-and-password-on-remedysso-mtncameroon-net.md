---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1397786'
original_report_id: '1397786'
title: Default Admin Username and Password on remedysso.mtncameroon.net
team_handle: mtn_group
created_at: '2021-11-10T19:00:17.340Z'
disclosed_at: '2022-09-01T20:50:32.925Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: mtncameroon.net
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Default Admin Username and Password on remedysso.mtncameroon.net

## Metadata

- HackerOne Report ID: 1397786
- Weakness: 
- Program: mtn_group
- Disclosed At: 2022-09-01T20:50:32.925Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
A Remedy Single Sign-On (Remedy SSO) Server is running at https://remedysso.mtncameroon.net/rsso/admin/#/.  
It is possible to access the application is using the default Administrator credentials.

## Steps To Reproduce:
Go to https://remedysso.mtncameroon.net/rsso/admin/#/ and login with credentials:
- Username: Admin
- Password: RSSO#Admin#

## Remediation
Change the password of the Admin user or disable the account.

## References
https://cwe.mitre.org/data/definitions/521.html

## Impact

A MNT Group Single Sign-On application was misconfigured in a manner that may have allowed a malicious user to login with the administrator user. The user is capable to perform any kind of configuration of the SSO system and retrieve sensitive information about organization users and infrastructure.

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

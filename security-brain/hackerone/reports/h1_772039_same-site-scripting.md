---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '772039'
original_report_id: '772039'
title: Same site Scripting
team_handle: drive_net_inc
created_at: '2020-01-11T03:52:50.245Z'
disclosed_at: '2020-01-13T12:56:22.183Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 46
asset_identifier: api.drive2.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Same site Scripting

## Metadata

- HackerOne Report ID: 772039
- Weakness: 
- Program: drive_net_inc
- Disclosed At: 2020-01-13T12:56:22.183Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Same site scripting 
I have found an error of some misconfigured DNS in a subdomain of yours which causes same site scripting.

PoC
1 Open a terminal and type ping localhost.drive2.ru
You would see that it resolves back to 127.0.0.1
A screenshot has been attached

## Impact

This may cause security issues in multiple user systems. An attack procedure can be found here : https://seclists.org/bugtraq/2008/Jan/270

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

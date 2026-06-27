---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '920401'
original_report_id: '920401'
title: SharePoint Web Services Exposed to Anonymous Access
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2020-07-10T03:54:27.682Z'
disclosed_at: '2020-11-24T13:51:29.920Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# SharePoint Web Services Exposed to Anonymous Access

## Metadata

- HackerOne Report ID: 920401
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2020-11-24T13:51:29.920Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The SharePoint configuration for this particular site allows any user to access the spdisco.aspx on the web server which discloses the location of of all SharePoint's web service endpoints. The URLs are: 
██████████
███

## Impact

An adversary may utilize the exposed information about the web services to mount specific attacks against this SharePoint site. It may allow the attacker to communicate with the web service to further identify potential weaknesses and further compromise the system.

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

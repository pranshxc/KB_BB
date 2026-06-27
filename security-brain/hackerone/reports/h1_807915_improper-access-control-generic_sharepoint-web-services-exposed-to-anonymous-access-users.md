---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '807915'
original_report_id: '807915'
title: SharePoint Web Services Exposed to Anonymous Access Users
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2020-03-01T02:24:56.186Z'
disclosed_at: '2020-07-14T17:17:58.499Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- improper-access-control-generic
---

# SharePoint Web Services Exposed to Anonymous Access Users

## Metadata

- HackerOne Report ID: 807915
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2020-07-14T17:17:58.499Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Any unauthenticated/anonymous users are able to access the SharePoint Web Services (.wsdl files) for the █████ Initiative website.

**Description:**
The SharePoint installation for this particular site allows any user to access the spdisco.aspx on the web server which discloses the location of of all SharePoint's web service endpoints. The URL is: https://█████/██████/_vti_bin/spdisco.aspx

## Impact
An adversary may utilize the exposed information about the web services to mount specific attacks against this SharePoint site. It may allow the attacker to communicate with the web service to further identify potential weaknesses and further compromise the system.

## Step-by-step Reproduction Instructions

1. Navigate to https://███████/██████████/_vti_bin/spdisco.aspx

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions
Disable anonymous access to spdisco.aspx

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

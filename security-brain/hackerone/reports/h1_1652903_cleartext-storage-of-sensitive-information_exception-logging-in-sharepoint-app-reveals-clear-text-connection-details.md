---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1652903'
original_report_id: '1652903'
title: Exception logging in Sharepoint app reveals clear-text connection details
weakness: Cleartext Storage of Sensitive Information
team_handle: nextcloud
created_at: '2022-07-28T14:40:07.820Z'
disclosed_at: '2022-11-26T12:46:33.424Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: nextcloud/sharepoint
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Exception logging in Sharepoint app reveals clear-text connection details

## Metadata

- HackerOne Report ID: 1652903
- Weakness: Cleartext Storage of Sensitive Information
- Program: nextcloud
- Disclosed At: 2022-11-26T12:46:33.424Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
On Exceptions thrown in the context of the SharePoint app, connection credentials may be written to the Nextcloud log in clear text.

## Steps To Reproduce:

Attempt to configure a sharepoint mount in an erroneous way.

## Supporting Material/References:

  * was files publically: https://github.com/nextcloud/sharepoint/issues/141

## Impact

When an attacker gets hold of the nextcloud log, they may gain knowledge of credentials to connect to a SharePoint service.

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

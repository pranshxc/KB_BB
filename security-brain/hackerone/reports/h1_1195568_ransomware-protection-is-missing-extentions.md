---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1195568'
original_report_id: '1195568'
title: Ransomware protection is missing extentions
team_handle: nextcloud
created_at: '2021-05-13T12:26:38.544Z'
disclosed_at: '2021-06-16T08:42:24.626Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Ransomware protection is missing extentions

## Metadata

- HackerOne Report ID: 1195568
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-06-16T08:42:24.626Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

So again I'm not sure if this is in scope. However you do advertise this on your enterprise pages. So I assume so.

In any case. It seems your `ransomeware_protection` app is missing some common extentions.
See for example https://avepointcdn.azureedge.net/assets/webhelp/compliance_guardian_installation_and_administration/index.htm#!Documents/ransomwareencryptedfileextensionlist.htm

As one example the 'pec' extention is not on your list.

## Impact

It seems your ransomware list was last updated 6 months ago.
There have been several ransom wares since.

However since you claim things like 'Best Ransomware protection in the industry' I would expect a lot more regular updates etc.

Long story short. This might deep your users safe while in reality this app is not really maintained and outdated.

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

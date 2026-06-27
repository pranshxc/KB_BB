---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1781751'
original_report_id: '1781751'
title: Ability to control the filename when uploading a logo or favicon on theming
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2022-11-22T20:46:30.773Z'
disclosed_at: '2023-04-10T15:59:02.387Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Ability to control the filename when uploading a logo or favicon on theming

## Metadata

- HackerOne Report ID: 1781751
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2023-04-10T15:59:02.387Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello,

When uploading a logo or favicon the filename can be controlled by attacker since the ```key``` can be modified which serves as the  filename.


{F2044799}

{F2044800}

{F2044798}

Due to an error the path is also disclosed

{F2044802}

## Steps To Reproduce:
[add details for how we can reproduce the issue]

1. go to ```http://localhost/settings/admin/theming```
2. upload  a logo or favicon
3. intercept the request using burp
4. modify the key

## Impact

The attacker can upload any files directly in the webapp and path disclosure. Combining both information can be useful in later attacks.

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

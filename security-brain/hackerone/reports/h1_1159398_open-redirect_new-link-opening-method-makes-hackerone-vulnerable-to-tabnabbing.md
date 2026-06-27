---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1159398'
original_report_id: '1159398'
title: New link opening method makes hackerone vulnerable to tabnabbing
weakness: Open Redirect
team_handle: security
created_at: '2021-04-09T19:12:56.244Z'
disclosed_at: '2021-07-07T08:49:31.383Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 49
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# New link opening method makes hackerone vulnerable to tabnabbing

## Metadata

- HackerOne Report ID: 1159398
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2021-07-07T08:49:31.383Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hackerone recently changed how it opens the external links and this new way is vulnerable to tabnabbing.
**Description:**
Please see the POC.
### Steps To Reproduce

1.  Click here:  https://awasthi7.github.io/
2.  Click on proceed when warning appears.
3.  The site will open in new tab and hackerone tab will be replaced by Google.

### Optional: Your Environment (Browser version, Device, etc)

 * 

### Optional: Supporting Material/References (Screenshots)

 *

## Impact

Unvalidated redirect

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

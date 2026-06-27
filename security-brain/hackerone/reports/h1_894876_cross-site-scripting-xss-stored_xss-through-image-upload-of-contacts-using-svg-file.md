---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '894876'
original_report_id: '894876'
title: XSS through image upload of contacts using svg file
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nextcloud
created_at: '2020-06-09T21:06:51.436Z'
disclosed_at: '2020-12-17T10:51:42.015Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS through image upload of contacts using svg file

## Metadata

- HackerOne Report ID: 894876
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nextcloud
- Disclosed At: 2020-12-17T10:51:42.015Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This is a bypass of report #808287

Upload the attached file for the image of a contact, right click "Open image in new tab" and you will see the xss.

## Impact

The person viewing the image of a contact can be victim of XSS.

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

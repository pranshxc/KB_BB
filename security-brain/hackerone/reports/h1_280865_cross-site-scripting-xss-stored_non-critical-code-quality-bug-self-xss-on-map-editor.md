---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280865'
original_report_id: '280865'
title: Non Critical Code Quality Bug / Self XSS on Map Editor
weakness: Cross-site Scripting (XSS) - Stored
team_handle: infogram
created_at: '2017-10-20T06:22:02.275Z'
disclosed_at: '2017-12-12T16:22:20.785Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Non Critical Code Quality Bug / Self XSS on Map Editor

## Metadata

- HackerOne Report ID: 280865
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: infogram
- Disclosed At: 2017-12-12T16:22:20.785Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I've found non-critical XSS on map editor. It is not for bounty just for code quality.

This is my url:

https://infogram.com/app/#edit/c024c717-31c2-4c31-8491-1cc9534e9adb

When i added map on form then edit Country name and replace with "<script>alert(1);</script>" it is executed. 

Attached screenshots.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '270993'
original_report_id: '270993'
title: resolved bugs in a program are public despite the program settings
weakness: Information Disclosure
team_handle: security
created_at: '2017-09-22T20:23:04.743Z'
disclosed_at: '2017-10-13T22:00:30.762Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: www.hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# resolved bugs in a program are public despite the program settings

## Metadata

- HackerOne Report ID: 270993
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2017-10-13T22:00:30.762Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

when navigating to https://hackerone.com/YOUR_PROGRAM_HANDLE/display_options
and unchecking the **Reports resolved** checkbox, the resolved bugs number won't be public at the program page, but going to https://hackerone.com/directory?query=YOUR_PROGRAM_HANDLE , the number of the resolved bug will bo shown although it was set no to be visible.

if this is intended behavior then I don't under stand why this settings option does exist!

thanks you!

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

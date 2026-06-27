---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '665144'
original_report_id: '665144'
title: Partial SSN exposed through Presentation slides on ██████████
weakness: Insecure Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2019-07-31T20:41:30.997Z'
disclosed_at: '2019-10-10T19:14:00.989Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Partial SSN exposed through Presentation slides on ██████████

## Metadata

- HackerOne Report ID: 665144
- Weakness: Insecure Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2019-10-10T19:14:00.989Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
During a search of ████████ I discovered that one of the slides ina presentation contained a screen shot of live data. 
**Description:**
The slides describe testing and using military application to organize and aggregate data on users. On one of the slides it does show a screen shot of actual data. I'm assuming it's live due to the fact that part of it was blocked out like the previous report where it showed XXXX and 4 digits.
## Impact
Critical
## Step-by-step Reproduction Instructions
████
## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
Purge the file

## Impact

Last 4  digits of an SSN can be used on various web portals along with knowing the full name of the soldier can give us access to sensitive portals

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

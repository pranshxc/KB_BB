---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '144129'
original_report_id: '144129'
title: Old titles are not hidden in reports with limited disclosure
weakness: Information Disclosure
team_handle: security
created_at: '2016-06-10T23:02:02.969Z'
disclosed_at: '2016-06-21T22:28:32.371Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- information-disclosure
---

# Old titles are not hidden in reports with limited disclosure

## Metadata

- HackerOne Report ID: 144129
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-06-21T22:28:32.371Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When a report is made public it shows all activity that took place in that report. This includes showing if the title of the report was changed and what it was changed from. 

This could cause information to be public that the business may not wish to make public if the person that created the report put a very descriptive title.
For Example
https://hackerone.com/reports/140392
This report was changed to only say a subdomain contained a cj vuln but the previous title which is still visible in the activity specifies the exact subdomain that was originally included in the title.

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

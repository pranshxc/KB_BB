---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '133322'
original_report_id: '133322'
title: Manipulate report timeline activity by using null byte.
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-04-20T20:06:30.896Z'
disclosed_at: '2016-07-01T18:15:02.180Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 12
tags:
- hackerone
- violation-of-secure-design-principles
---

# Manipulate report timeline activity by using null byte.

## Metadata

- HackerOne Report ID: 133322
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-07-01T18:15:02.180Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Null bytes are not permitted in report body, or even in report title. But that can be used in the comment section of `self-closing` (for reporter) and `change-status` (for team). When a null byte is used as a comment, that report timeline activity disappears!

For example: 
https://hackerone.com/reports/133317 report was closed using a null byte in comment.

{F88258}

There is no activity log in the report details for the closing, but the report is closed.

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

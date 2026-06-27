---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '263'
original_report_id: '263'
title: Report title autocompletion
weakness: Information Disclosure
team_handle: security
created_at: '2013-11-07T07:11:08.392Z'
disclosed_at: '2015-06-08T00:30:09.283Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Report title autocompletion

## Metadata

- HackerOne Report ID: 263
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2015-06-08T00:30:09.283Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Scenario:
1. Researcher uses a shared computer.
2. Researcher submits a report.
3. Researcher logs out.
4. Another person logs in, on another account.
5. Another person submits a report.
6. When entering a title, the title of the previous report submitted by the researcher is shown in autocompletion box.

This gives away the title of the bug to other users of the web browser, even though the researcher logged out properly.

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

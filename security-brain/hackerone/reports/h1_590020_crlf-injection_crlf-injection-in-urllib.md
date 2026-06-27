---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '590020'
original_report_id: '590020'
title: CRLF Injection in urllib
weakness: CRLF Injection
team_handle: ibb
created_at: '2019-05-25T10:16:29.801Z'
disclosed_at: '2020-05-06T02:15:20.166Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 337
asset_identifier: Python (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- crlf-injection
---

# CRLF Injection in urllib

## Metadata

- HackerOne Report ID: 590020
- Weakness: CRLF Injection
- Program: ibb
- Disclosed At: 2020-05-06T02:15:20.166Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi. I found CRLF Injection a few months ago.
Please refer my bug issue.
https://bugs.python.org/issue35906

Thank you

## Impact

lead to SSRF. 
e.g. can exploit a internal redis server to send arbitrary packet data including ascii and non-ascii.

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

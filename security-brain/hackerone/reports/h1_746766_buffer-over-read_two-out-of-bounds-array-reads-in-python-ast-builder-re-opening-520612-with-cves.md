---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '746766'
original_report_id: '746766'
title: Two out-of-bounds array reads in Python AST builder (Re-opening 520612 with
  CVEs)
weakness: Buffer Over-read
team_handle: ibb
created_at: '2019-11-26T17:21:45.088Z'
disclosed_at: '2021-08-25T20:51:45.994Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: Python (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- buffer-over-read
---

# Two out-of-bounds array reads in Python AST builder (Re-opening 520612 with CVEs)

## Metadata

- HackerOne Report ID: 746766
- Weakness: Buffer Over-read
- Program: ibb
- Disclosed At: 2021-08-25T20:51:45.994Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I'm re-submitting #520612 after getting CVEs issued, as instructed in an automated email from November 17th.

Getting CVEs issued took a while, but here they are:

- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19274
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19275

## Impact

A service that takes Python snippets as payload, but doesn't necessarily execute them, could possibly be caused to crash, leading to a denial of service. Examples of such services include online playgrounds for static analysis tools, syntax highlighting & formatting services, etc.

I didn't copy-and-paste all the original details here; see the original issue ( #520612 ) for that.

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

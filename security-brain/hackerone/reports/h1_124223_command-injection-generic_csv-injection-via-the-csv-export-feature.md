---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '124223'
original_report_id: '124223'
title: CSV Injection via the CSV export feature
weakness: Command Injection - Generic
team_handle: security
created_at: '2016-03-18T11:10:35.503Z'
disclosed_at: '2016-04-25T10:37:54.435Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- command-injection-generic
---

# CSV Injection via the CSV export feature

## Metadata

- HackerOne Report ID: 124223
- Weakness: Command Injection - Generic
- Program: security
- Disclosed At: 2016-04-25T10:37:54.435Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I've bypassed #111192 by using this string ";=cmd|' /C calc'!A0" without doublequotes. Steps to reproduce are as in #111192. Tested in excel 2003-2013

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

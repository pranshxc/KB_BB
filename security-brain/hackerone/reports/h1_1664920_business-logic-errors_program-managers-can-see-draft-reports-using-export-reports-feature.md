---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1664920'
original_report_id: '1664920'
title: Program managers can see draft reports using Export Reports feature
weakness: Business Logic Errors
team_handle: security
created_at: '2022-08-09T22:26:01.528Z'
disclosed_at: '2023-05-18T11:42:08.022Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Program managers can see draft reports using Export Reports feature

## Metadata

- HackerOne Report ID: 1664920
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2023-05-18T11:42:08.022Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Hello. I have discovered a bug in the new draft feature. 

Program managers can see draft reports using Export Reports feature. 

### Steps To Reproduce

1. Make a draft (do not send) report on a public/private program.
2. Go to the `https://hackerone.com/<program-handle>/export_reports` page and export reports.
3. Check your e-mail and download the file got from HackerOne.
4. Check the CSV file:

{F1860656}

As you see, it says draft and disclosed report title, severity, weakness, etc.

When you try to find it in the program inbox you can't find it, so completely sure this is a bug.

{F1860658}

## Impact

Program managers can see draft reports using Export Reports feature leads to PII disclosure without reporter permission.

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

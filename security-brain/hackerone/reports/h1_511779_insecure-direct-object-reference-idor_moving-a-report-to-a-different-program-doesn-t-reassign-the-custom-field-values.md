---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '511779'
original_report_id: '511779'
title: Moving a report to a different program doesn't reassign the Custom Field Values
weakness: Insecure Direct Object Reference (IDOR)
team_handle: security
created_at: '2019-03-18T18:18:07.087Z'
disclosed_at: '2019-04-25T16:40:53.709Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Moving a report to a different program doesn't reassign the Custom Field Values

## Metadata

- HackerOne Report ID: 511779
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: security
- Disclosed At: 2019-04-25T16:40:53.709Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When a report is moved to a different program, all associated objects are either removed or copied to the new program. During an internal security review of the Custom Fields feature it was observed that this isn't the case for Custom Field Values. This means that even after a report has moved, the report is referencing an object that may not belong to a program the user controls.

# Proof of concept

* Submit a report to a program where you have the ability to move the report to another program
* Move the report to a program you also have access to
* Confirm through the Rails console that the report references values that belong to the program the report was submitted to

## Impact

The associated values and attributes may leak confidential information, either through the value itself or updating the attributes at a later point in time.

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

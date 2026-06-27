---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2096271'
original_report_id: '2096271'
title: Staff and Triage can modify the initial post of a report, including of already
  disclosed reports
weakness: Improper Access Control - Generic
team_handle: security
created_at: '2023-08-04T09:51:22.535Z'
disclosed_at: '2023-08-28T11:33:37.531Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 39
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Staff and Triage can modify the initial post of a report, including of already disclosed reports

## Metadata

- HackerOne Report ID: 2096271
- Weakness: Improper Access Control - Generic
- Program: security
- Disclosed At: 2023-08-28T11:33:37.531Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

FULL DISCLOSURE: I am a HackerOne employee and learned about it through this submission: https://███████-/issues/67828

**Summary:**

Members of the HackerOne program (and likely other program members on their own program) and Triage can edit the information of the original report

I used https://hackerone.com/reports/2000000 to demonstrate and the changes have since been reverted.

**Description:**

### Steps To Reproduce

1. Go to any report, disclosed or undisclosed
2. Press "edit information" on the original post
3. Edit & save.
4. Your changes are saved 

### Optional: Supporting Material/References (Screenshots)

{F2560190}
{F2560189} {F2560191}
{F2560195}

## Impact

Members and Triage can rewrite the story the hacker is trying to tell and edits are not transparant

- Give hackers a bad image in disclosed reports
- Tell a different story or lower impact artificially
- The body is supposed to be immutable after 20 minutes

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

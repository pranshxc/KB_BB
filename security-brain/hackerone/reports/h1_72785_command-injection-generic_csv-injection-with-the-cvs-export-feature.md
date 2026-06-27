---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '72785'
original_report_id: '72785'
title: CSV Injection with the CVS export feature
weakness: Command Injection - Generic
team_handle: security
created_at: '2015-06-26T19:53:52.138Z'
disclosed_at: '2015-09-21T22:04:25.799Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- command-injection-generic
---

# CSV Injection with the CVS export feature

## Metadata

- HackerOne Report ID: 72785
- Weakness: Command Injection - Generic
- Program: security
- Disclosed At: 2015-09-21T22:04:25.799Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The "Download as a CSV" feature of HackerOne does not properly "escape" fields. This allows an adversary to turn a field into active content so when a response team download the csv and opens it, the active content gets executed. Here is more information about this issue: http://www.contextis.com/resources/blog/comma-separated-vulnerabilities/

Here is one method to reproduce this issue:

1. As a researcher, I can report an issue with a name starting with "=1+1"
2. As a response team, I choose to export all issues found to CSV containing the issue in (1)
3. As a response team, I now open this CSV file in excel or another spreadsheet program
4. You can see the cell containing the issue name in (1) is displayed as "2" which means the code is executed.

Mitigation:
Ensure all fields are properly "escaped" before returning the CSV file to the user.

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

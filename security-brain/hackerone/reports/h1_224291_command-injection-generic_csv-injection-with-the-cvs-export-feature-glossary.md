---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224291'
original_report_id: '224291'
title: CSV Injection with the CVS export feature - Glossary
weakness: Command Injection - Generic
team_handle: weblate
created_at: '2017-04-27T11:17:22.094Z'
disclosed_at: '2017-05-17T14:19:37.838Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- command-injection-generic
---

# CSV Injection with the CVS export feature - Glossary

## Metadata

- HackerOne Report ID: 224291
- Weakness: Command Injection - Generic
- Program: weblate
- Disclosed At: 2017-05-17T14:19:37.838Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The "Download as a CSV" feature of Weblate does not properly "escape" fields. Here is more information about this issue: http://www.contextis.com/resources/blog/comma-separated-vulnerabilities/

Here is one method to reproduce this issue:

1) I can add new information in Glossary with a name starting with "=1+1;" or "-2+3+cmd|' /C calc'!G2;"
2) I choose to export all Glossary to CSV containing the issue in (1)
3) I now open this CSV file in excel or another spreadsheet program
4) You can see the cell containing the issue name in (1) is displayed as "2" (=1+1;) which means the code is executed.

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

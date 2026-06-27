---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '160520'
original_report_id: '160520'
title: Bypass fix in https://hackerone.com/reports/151516 report.
weakness: Command Injection - Generic
team_handle: iandunn-projects
created_at: '2016-08-18T20:27:27.247Z'
disclosed_at: '2016-10-12T04:04:29.634Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- command-injection-generic
---

# Bypass fix in https://hackerone.com/reports/151516 report.

## Metadata

- HackerOne Report ID: 160520
- Weakness: Command Injection - Generic
- Program: iandunn-projects
- Disclosed At: 2016-10-12T04:04:29.634Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi.

**Steps to reproduce:**

1. The same in previous https://hackerone.com/reports/151516 report.
2. But payload to bypass your fix would be like this: `;=cmd|' /C calc'!A0`

**Solution:**

1. Add `;` in your escape function esc_csv() on line 2858 of camptix.php

**References:**

1. https://www.owasp.org/index.php/CSV_Excel_Macro_Injection

Tested on Windows 7 64 + Microsoft Office Exel 2003(think will work and on later versions)

Regards.

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

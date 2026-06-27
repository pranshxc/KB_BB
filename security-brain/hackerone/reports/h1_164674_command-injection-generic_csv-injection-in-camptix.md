---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164674'
original_report_id: '164674'
title: CSV Injection in Camptix
weakness: Command Injection - Generic
team_handle: iandunn-projects
created_at: '2016-08-31T09:24:53.228Z'
disclosed_at: '2016-10-12T07:49:59.216Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- command-injection-generic
---

# CSV Injection in Camptix

## Metadata

- HackerOne Report ID: 164674
- Weakness: Command Injection - Generic
- Program: iandunn-projects
- Disclosed At: 2016-10-12T07:49:59.216Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, Ian!

I see you tried to escape "=, -, +, @" in your code ([#151516](https://hackerone.com/reports/151516)), but let me show simple workaround.

I've made CSV injection by using this string ";=cmd|' /C calc'!A5" without doublequotes.

";" will bypass your trying to set the quote in the beginning of the string.

";" acts as a new cell separator.

Tested in the Excel 2016

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

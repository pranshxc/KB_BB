---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226783'
original_report_id: '226783'
title: HTML Injection on airlink.ubnt.com
weakness: Code Injection
team_handle: ui
created_at: '2017-05-07T20:19:20.150Z'
disclosed_at: '2017-06-22T14:13:24.451Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- code-injection
---

# HTML Injection on airlink.ubnt.com

## Metadata

- HackerOne Report ID: 226783
- Weakness: Code Injection
- Program: ui
- Disclosed At: 2017-06-22T14:13:24.451Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi
I found an html injection vulnerability on airlink.ubnt.com

Steps to reproduce:

First go to: https://airlink.ubnt.com/#/ptp
Next go on Save Simulation button and as simulation name put: "><marquee><h1>HTMLINJECTIONHERE</h1></marquee> and save it
Now go on Open Simulation button and you will see html being executed :) 

Your team should fix it
Thanks

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

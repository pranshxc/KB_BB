---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '283742'
original_report_id: '283742'
title: HTML injection
team_handle: infogram
created_at: '2017-10-28T11:49:46.965Z'
disclosed_at: '2017-10-31T10:30:42.556Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# HTML injection

## Metadata

- HackerOne Report ID: 283742
- Weakness: 
- Program: infogram
- Disclosed At: 2017-10-31T10:30:42.556Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi team ...

i found HTML i on https://infogram.com/app/#/library
step

..
1- go to https://infogram.com/app/#/library
2- choose Report Templates .
3- Use Report Classic
4- click to edit_data
5- edit cell __Employee ID__
5- payload

  >  <h1>hacked</h1>
    <marquee behavior="scroll" direction="left">hacked</marquee>
   <h1 style="background-color:#000099;">hacked</h1>

6-execute HTML .. 

POC .. video on attached

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

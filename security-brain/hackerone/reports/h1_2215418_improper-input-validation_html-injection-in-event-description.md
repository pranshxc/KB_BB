---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2215418'
original_report_id: '2215418'
title: Html injection in event Description
weakness: Improper Input Validation
team_handle: linkedin
created_at: '2023-10-19T09:20:39.756Z'
disclosed_at: '2024-01-29T04:50:05.234Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 45
asset_identifier: www.linkedin.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# Html injection in event Description

## Metadata

- HackerOne Report ID: 2215418
- Weakness: Improper Input Validation
- Program: linkedin
- Disclosed At: 2024-01-29T04:50:05.234Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Hi team

there is Html injection   when user add   Description to event  when public user search for  published event

#Step's

* login to https://www.linkedin.com/groups/ 
* create event mark it as Public add <a href="https://malicious-site.com">Click me!</a> as  Description
{F2785963}
* save change now navigate to ==Search== enter your event name 
* when ==result== show up html code get executed in the Description

{F2785962}


POC:F2785976

## Impact

attacker able to run html code

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

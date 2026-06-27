---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2310620'
original_report_id: '2310620'
title: New Hacktivity features:Bounty rewards leakage Where programs doesn’t decide
  to disclose bounty in limited disclosure report
weakness: Information Disclosure
team_handle: security
created_at: '2024-01-10T07:10:41.003Z'
disclosed_at: '2024-03-28T11:27:32.680Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 86
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# New Hacktivity features:Bounty rewards leakage Where programs doesn’t decide to disclose bounty in limited disclosure report

## Metadata

- HackerOne Report ID: 2310620
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2024-03-28T11:27:32.680Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hello,

few months ago i submit  #2030964 and sadly its closed as duplicate of this #1961639 , but i found to access same issue i.e:  users hidden bounty information  leak as new feature method that is bounty amount filter on hacktivity.

█████████

steps to reproduce
-
go to hacktivity page 
add filter - ` total_awarded_amount:10000` or `total_awarded_amount:8000`
you can see bounty awarded amount on report which is not visible as normal 

i add some report please check
-
https://hackerone.com/reports/977212
https://hackerone.com/reports/881901
https://hackerone.com/reports/513236

now the feature to hide bounty amount is not worth here. please fix this so a non- authorized users, or no-one can see if hackers want hide bounty amount

## Impact

due to new features hacktivity filter  Anyone can seen total bounty award even hackers want to be hide from public

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

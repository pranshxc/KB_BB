---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '981796'
original_report_id: '981796'
title: Information Disclosure of Garbage Collection Cycle
weakness: Information Disclosure
team_handle: basecamp
created_at: '2020-09-14T15:56:50.331Z'
disclosed_at: '2020-11-04T19:09:20.464Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: '*.hey.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Information Disclosure of Garbage Collection Cycle

## Metadata

- HackerOne Report ID: 981796
- Weakness: Information Disclosure
- Program: basecamp
- Disclosed At: 2020-11-04T19:09:20.464Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Upon enumerating a subdomain content I found a directory that discloses the duration of the garbage collection cycles.
I think that these information should be kept private because public should not know information about the target application and how it operates or do its garbage collection process.

##Steps To Reproduce
1. Navigate to the target url: https://gopher.hey.com/metrics
2. See the data.

███

## Impact

This information may help attackers understand more things about the target application which may help in further investigation and exploitation.

Kind Regards.

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

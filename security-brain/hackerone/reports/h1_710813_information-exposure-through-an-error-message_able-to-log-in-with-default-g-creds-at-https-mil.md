---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '710813'
original_report_id: '710813'
title: Able to log in with default ██████g creds at  https█████████████████████.mil
weakness: Information Exposure Through an Error Message
team_handle: deptofdefense
created_at: '2019-10-10T01:34:54.464Z'
disclosed_at: '2021-01-12T21:38:03.946Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-exposure-through-an-error-message
---

# Able to log in with default ██████g creds at  https█████████████████████.mil

## Metadata

- HackerOne Report ID: 710813
- Weakness: Information Exposure Through an Error Message
- Program: deptofdefense
- Disclosed At: 2021-01-12T21:38:03.946Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary████**
was able to use ████████████████████████ to log into this instance of Adobe Experience Manager, though it does not seem to be in used at the moment 
**Description███████**
while navigating to https█████████████████████████.mil, I performed some fuzzing and found that `/repository` was available which asked for authentication using `███████████████████` worked and I could then access another path found by fuzing `lc` [link](https█████████████.mil/lc) which then showed me the ██████ panel. 

## Impact
Medium since it is not being used
## Step-by-step Reproduction Instructions

1. Navigate to  https████████████████.mil/repository 
2. use ████████████████ (username██████████password)
3. navigate to  https██████████████████████.mil/lc 

## Product, Version, and Configuration (If applicable)

Adobe Experience Manager

## Suggested Mitigation/Remediation Actions

Remove this application if it is not being used

## Impact

Medium - I was able to use █████████████ to log in 

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

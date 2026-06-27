---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1607429'
original_report_id: '1607429'
title: Twitter Account hijack through broken link in https://runpanther.io
team_handle: panther_labs
created_at: '2022-06-20T14:04:31.154Z'
disclosed_at: '2022-07-28T16:57:49.838Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: '*.runpanther.io'
asset_type: WILDCARD
max_severity: high
tags:
- hackerone
---

# Twitter Account hijack through broken link in https://runpanther.io

## Metadata

- HackerOne Report ID: 1607429
- Weakness: 
- Program: panther_labs
- Disclosed At: 2022-07-28T16:57:49.838Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

A link(https://twitter.com/runpanther_) in https://runpanther.io  was broken and anyone could create that account which leads to account impersonate

## Steps To Reproduce:

1.Go to https://runpanther.io
2.Scroll down to bottom there you can see that twitter icon.
3.Click on that icon, you will redirected to twitter account which i have been hijacked
4.Anyone could claim this username and broken link could be hijacked.

## Supporting Material/References:
Similar report that was reported previously in panther_lab
https://hackerone.com/reports/1117079

## Impact

Since the link can be hijacked so any attacker can claim the link and make fake twitter profile of panther labs and can do scam with them.

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

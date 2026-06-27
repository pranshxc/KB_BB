---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1563142'
original_report_id: '1563142'
title: Slowvote and Countdown can cause Denial of Service due to recursive inclusion
weakness: Uncontrolled Resource Consumption
team_handle: phabricator
created_at: '2022-05-09T00:33:09.851Z'
disclosed_at: '2022-05-09T18:37:16.485Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Slowvote and Countdown can cause Denial of Service due to recursive inclusion

## Metadata

- HackerOne Report ID: 1563142
- Weakness: Uncontrolled Resource Consumption
- Program: phabricator
- Disclosed At: 2022-05-09T18:37:16.485Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Similar to #85011, if you edit a Slowvote or Countdown object and include its own object ID in the description, then it will recursively include and prevent the page from loading.

mongoose

## Impact

Denial of Service. You can include the Slowvote or Countdown object on any other object to also prevent it from loading. If it is included in the feed, you could also prevent the home page from loading.

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

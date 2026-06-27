---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '272097'
original_report_id: '272097'
title: Interger overflow in eval trigger write out of bound
weakness: Integer Underflow
team_handle: ibb
created_at: '2017-09-26T16:44:35.846Z'
disclosed_at: '2017-12-11T07:53:16.489Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: Perl (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- integer-underflow
---

# Interger overflow in eval trigger write out of bound

## Metadata

- HackerOne Report ID: 272097
- Weakness: Integer Underflow
- Program: ibb
- Disclosed At: 2017-12-11T07:53:16.489Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi security team,
i [reported](https://rt.perl.org/Public/Bug/Display.html?id=131562)  some samples triggered crash in eval funtion in perl. 
The bug come because variable `start` and `items` used type `I32` which takes half the range of line_t and folds it into negative numbers, leading to trying to store the lines at negative indexes.

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

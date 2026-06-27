---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152281'
original_report_id: '152281'
title: Use After Free/Double Free in Garbage Collection
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-07-19T12:15:08.141Z'
disclosed_at: '2019-10-13T11:08:45.357Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# Use After Free/Double Free in Garbage Collection

## Metadata

- HackerOne Report ID: 152281
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-13T11:08:45.357Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=72605

I don't know if the bug is qualified.

I reported this bug since php some guys added this commit: https://github.com/php/php-src/commit/1c84b55adea936b065a20102202bea3d1d243225
Then they had reverted this commit before PHP updates release: https://github.com/php/php-src/commit/171c759d791f809ebc31711fd0b0b5bb632cd2cc
So I think this bug have been fixed. if I don't submit this bug until php updates release, then this bug will be tagged as `Type: Security` and fix in next PHP updates release.

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

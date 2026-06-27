---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '135293'
original_report_id: '135293'
title: bcpowmod accepts negative scale and corrupts _one_ definition
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-04-29T03:30:19.373Z'
disclosed_at: '2019-10-13T18:11:23.424Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# bcpowmod accepts negative scale and corrupts _one_ definition

## Metadata

- HackerOne Report ID: 135293
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-13T18:11:23.424Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=72093

Two issues reported on the same bug, bcpowermod accepts a negative value which also is able to corrupt the one definition and leads to memory corruption problems.

Reported to developers on 2016-04-24, fixed 2016-04-25 and released at 2016-04-28, affected PHP 5.5 , 5.6 and 7.

http://php.net/ChangeLog-5.php#5.5.35
http://php.net/ChangeLog-5.php#5.6.21
http://php.net/ChangeLog-7.php#7.0.6

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

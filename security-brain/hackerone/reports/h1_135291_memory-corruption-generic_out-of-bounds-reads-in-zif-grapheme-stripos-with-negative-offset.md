---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '135291'
original_report_id: '135291'
title: Out-of-bounds reads in zif_grapheme_stripos with negative offset
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-04-29T03:23:04.103Z'
disclosed_at: '2019-10-13T18:21:26.951Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# Out-of-bounds reads in zif_grapheme_stripos with negative offset

## Metadata

- HackerOne Report ID: 135291
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-13T18:21:26.951Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=72061

grapheme_stripos from the intl extension had a security issue when handling negative offsets, this allowed to read from arbitrary memory locations.

Reported to developers on 2016-04-24, fixed 2016-04-29 and released at 2016-04-28, affected PHP 5.5 , 5.6 and 7.

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

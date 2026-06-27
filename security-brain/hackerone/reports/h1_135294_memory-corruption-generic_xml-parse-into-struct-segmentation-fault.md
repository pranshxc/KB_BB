---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '135294'
original_report_id: '135294'
title: xml_parse_into_struct segmentation fault
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-04-29T03:38:30.259Z'
disclosed_at: '2019-10-13T18:06:53.554Z'
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

# xml_parse_into_struct segmentation fault

## Metadata

- HackerOne Report ID: 135294
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-13T18:06:53.554Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=72099

Invalid memory access while parsing XML input using xml_parse_into_struct, parser->level wasn't being checked and then used as an offset parser->ltags[parser->level-1].

Reported to developers on 2016-04-25, fixed 2016-04-25 and released at 2016-04-28, affected PHP 5.5 , 5.6 and 7.

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

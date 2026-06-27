---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141197'
original_report_id: '141197'
title: get_icu_value_internal out-of-bounds read
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-05-26T14:19:23.800Z'
disclosed_at: '2019-10-13T18:12:26.202Z'
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

# get_icu_value_internal out-of-bounds read

## Metadata

- HackerOne Report ID: 141197
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-13T18:12:26.202Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=72241

Absence of null character terminator causes unexpected zend_string length and leaks heap memory when using several intl functions that commonly receive user input:

- locale_canonicalize
- locale_filter_matches
- locale_lookup
- locale_parse
- locale_get_primary_language 

This affected PHP version 5.5, 5.6 and 7.0, patch released today:

http://php.net/ChangeLog-5.php#5.5.36

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

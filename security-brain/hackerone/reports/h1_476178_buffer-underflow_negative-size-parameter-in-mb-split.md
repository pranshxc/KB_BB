---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '476178'
original_report_id: '476178'
title: Negative size parameter in mb_split
weakness: Buffer Underflow
team_handle: ibb
created_at: '2019-01-07T20:25:48.915Z'
disclosed_at: '2020-11-09T01:48:52.585Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- buffer-underflow
---

# Negative size parameter in mb_split

## Metadata

- HackerOne Report ID: 476178
- Weakness: Buffer Underflow
- Program: ibb
- Disclosed At: 2020-11-09T01:48:52.585Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=77367

mb_split doesn't correctly detect the length when the $string has an unfinished multibyte character at the end of the string. This causes a crash due to a negative parameter to add_next_index_stringl, which calls zend_string_init and memcpy.

Could reproduce on master.

## Impact

This could be used to cause memory corruption/leakage.

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

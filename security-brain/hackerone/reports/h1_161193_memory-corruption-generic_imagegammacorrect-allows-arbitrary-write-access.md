---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161193'
original_report_id: '161193'
title: imagegammacorrect allows arbitrary write access
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-08-19T02:58:07.154Z'
disclosed_at: '2019-10-13T18:15:54.600Z'
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

# imagegammacorrect allows arbitrary write access

## Metadata

- HackerOne Report ID: 161193
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-13T18:15:54.600Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Upstream Bug
---
2016-08-02 03:46 UTC
https://bugs.php.net/bug.php?id=72730

Summary
--
imagegammacorrect accepts two gamma values, if they don't have the same sign then the palette colors will be assigned values bigger than 0xFF, later this values are used to calculate the transparent color using the gdTrueColorAlpha macro, and a negative value will be assigned to the transparent color.  This negative value is used as an index and allows writing an arbitrary null, similar to bug #72512 

Patch
--
2016-08-10 07:16 UTC
http://git.php.net/?p=php-src.git;a=commit;h=4d76676101f8814520ea988e42b3bda54eb9e255

Fixed for PHP 5.6.25, PHP 7.0.10
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php#7.0.10

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161189'
original_report_id: '161189'
title: select_colors write out-of-bounds
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-08-19T02:49:28.093Z'
disclosed_at: '2019-10-31T06:16:34.902Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# select_colors write out-of-bounds

## Metadata

- HackerOne Report ID: 161189
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-31T06:16:34.902Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Upstream Bug
---
2016-07-28 06:38 UTC
https://bugs.php.net/bug.php?id=72697

Summary
--
Type mismatch parameters between ncolors and colorsWanted parameters at zif_imagetruecolortopalette and php_gd_gdImageTrueColorToPalette, ncolors is a 64 bit integer and colorsWanted is 32 bits, ncolors' value 0x1000000000000000 becomes 0 inside php_gd_gdImageTrueColorToPalette. Later, select_colors will not allocate enough memory and writes out of bounds.

Patch
--
2016-08-10 07:01 UTC
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

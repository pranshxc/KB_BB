---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152784'
original_report_id: '152784'
title: imagegif/output out-of-bounds access
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-07-21T05:19:57.431Z'
disclosed_at: '2019-10-13T18:20:54.513Z'
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

# imagegif/output out-of-bounds access

## Metadata

- HackerOne Report ID: 152784
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-13T18:20:54.513Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Bug
https://bugs.php.net/bug.php?id=72519

Summary
output function from gd_gif_out.c causes out-of-bounds access of the masks array when ctx->cur_bits becomes a negative number while generating a gif file.

Reported to PHP 
2016-06-30 04:10 UTC

Patch
2016-07-19 07:47 UTC
http://git.php.net/?p=php-src.git;a=commit;h=8dc5ffa479f886fae235d4ff6391e14546a3fda9

Fixed for PHP 5.5 (security only mode), PHP 5.6, PHP 7.0
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php

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

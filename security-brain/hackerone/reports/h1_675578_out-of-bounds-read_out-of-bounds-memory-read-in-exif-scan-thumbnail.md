---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '675578'
original_report_id: '675578'
title: Out of Bounds Memory Read in exif_scan_thumbnail
weakness: Out-of-bounds Read
team_handle: ibb
created_at: '2019-08-17T16:33:30.569Z'
disclosed_at: '2020-11-09T01:49:45.909Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- out-of-bounds-read
---

# Out of Bounds Memory Read in exif_scan_thumbnail

## Metadata

- HackerOne Report ID: 675578
- Weakness: Out-of-bounds Read
- Program: ibb
- Disclosed At: 2020-11-09T01:49:45.909Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have found and reported an out of bounds memory read in PHP [exif_scan_thumbnail]
When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.31, 7.2.x below 7.2.21 and 7.3.x below 7.3.8 it is possible to supply it with data what will cause it to read past the allocated buffer.
This has been fixed and assigned CVE-2019-11041
The bug report is here: https://bugs.php.net/bug.php?id=78222
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11041
https://nvd.nist.gov/vuln/detail/CVE-2019-11041

## Impact

This may lead to information disclosure or crash.

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

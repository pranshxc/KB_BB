---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '665330'
original_report_id: '665330'
title: Out of Bounds Memory Read in php_jpg_get16
weakness: Buffer Over-read
team_handle: ibb
created_at: '2019-08-01T05:45:21.955Z'
disclosed_at: '2020-11-09T01:47:14.529Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- buffer-over-read
---

# Out of Bounds Memory Read in php_jpg_get16

## Metadata

- HackerOne Report ID: 665330
- Weakness: Buffer Over-read
- Program: ibb
- Disclosed At: 2020-11-09T01:47:14.529Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have found and reported an out of bounds memory read in PHP [php_jpg_get16]
When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.30, 7.2.x below 7.2.19 and 7.3.x below 7.3.6 it is possible to supply it with data what will cause it to read past the allocated buffer.
This has been fixed and assigned CVE-2019-11040
The bug report is here: https://bugs.php.net/bug.php?id=77988
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11040
https://nvd.nist.gov/vuln/detail/CVE-2019-11040

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

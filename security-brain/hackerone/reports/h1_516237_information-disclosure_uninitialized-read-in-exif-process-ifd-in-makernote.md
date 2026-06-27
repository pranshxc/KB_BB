---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '516237'
original_report_id: '516237'
title: Uninitialized read in exif_process_IFD_in_MAKERNOTE
weakness: Information Disclosure
team_handle: ibb
created_at: '2019-03-27T03:18:50.881Z'
disclosed_at: '2020-10-10T02:17:45.672Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- information-disclosure
---

# Uninitialized read in exif_process_IFD_in_MAKERNOTE

## Metadata

- HackerOne Report ID: 516237
- Weakness: Information Disclosure
- Program: ibb
- Disclosed At: 2020-10-10T02:17:45.672Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This bug is present in exif_process_IFD_in_MAKERNOTE method of ext/exif/exif.c file.

Detailed description and steps to reproduce for this bug is present in bug report submitted to php.net.
Bug Report : https://bugs.php.net/bug.php?id=77563
PHP version : 7.1.26
CVE-ID : 2019-9638

## Impact

Uninitialized data may leak data from memory.

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

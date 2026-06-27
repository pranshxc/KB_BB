---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '73238'
original_report_id: '73238'
title: Buffer Over-read in unserialize when parsing Phar
team_handle: ibb
created_at: '2015-03-29T00:00:00.000Z'
disclosed_at: '2015-04-14T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# Buffer Over-read in unserialize when parsing Phar

## Metadata

- HackerOne Report ID: 73238
- Weakness: 
- Program: ibb
- Disclosed At: 2015-04-14T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=69324

ext/phar/phar.c in PHP before 5.4.40, 5.5.x before 5.5.24, and 5.6.x before 5.6.8 allows remote attackers to obtain sensitive information from process memory or cause a denial of service (buffer over-read and application crash) via a crafted length value in conjunction with crafted serialized data in a phar archive, related to the phar_parse_metadata and phar_parse_pharfile functions.

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

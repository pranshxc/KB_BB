---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '261335'
original_report_id: '261335'
title: Heap Use After Free Read in unserialize()
weakness: Use After Free
team_handle: ibb
created_at: '2017-08-18T13:20:37.058Z'
disclosed_at: '2018-11-27T15:59:52.397Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- use-after-free
---

# Heap Use After Free Read in unserialize()

## Metadata

- HackerOne Report ID: 261335
- Weakness: Use After Free
- Program: ibb
- Disclosed At: 2018-11-27T15:59:52.397Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

ext/standard/var_unserializer.re in PHP 7.0.x through 7.0.22 and 7.1.x through 7.1.8 is prone to a heap use after free while unserializing untrusted data, related to improper use of the hash API for key deletion in a situation with an invalid array size. Exploitation of this issue can have an unspecified impact on the integrity of PHP.

This is CVE-2017-12932 and the bug report confirming that I reported the issue is here: https://bugs.php.net/bug.php?id=74103

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

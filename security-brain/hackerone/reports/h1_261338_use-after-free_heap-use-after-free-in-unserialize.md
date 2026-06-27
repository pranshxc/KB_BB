---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '261338'
original_report_id: '261338'
title: Heap Use After Free in unserialize()
weakness: Use After Free
team_handle: ibb
created_at: '2017-08-18T13:24:49.512Z'
disclosed_at: '2018-11-27T15:59:52.330Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- use-after-free
---

# Heap Use After Free in unserialize()

## Metadata

- HackerOne Report ID: 261338
- Weakness: Use After Free
- Program: ibb
- Disclosed At: 2018-11-27T15:59:52.330Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

ext/standard/var_unserializer.re in PHP 7.0.x before 7.0.21 and 7.1.x before 7.1.7 is prone to a heap use after free while unserializing untrusted data, related to the zval_get_type function in Zend/zend_types.h. Exploitation of this issue can have an unspecified impact on the integrity of PHP.

This has been fixed and assigned CVE-2017-12934.  The bug report is here: https://bugs.php.net/bug.php?id=74101

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

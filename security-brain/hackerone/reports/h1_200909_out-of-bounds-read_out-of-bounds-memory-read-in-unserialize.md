---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '200909'
original_report_id: '200909'
title: Out of bounds memory read in unserialize()
weakness: Out-of-bounds Read
team_handle: ibb
created_at: '2017-01-24T20:38:29.185Z'
disclosed_at: '2017-05-28T19:23:37.252Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- out-of-bounds-read
---

# Out of bounds memory read in unserialize()

## Metadata

- HackerOne Report ID: 200909
- Weakness: Out-of-bounds Read
- Program: ibb
- Disclosed At: 2017-05-28T19:23:37.252Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have found and reported an out of bounds memory read in PHP:
https://bugs.php.net/bug.php?id=73825

It affected all three supported versions and has been fixed with the latest updates:
https://secure.php.net/ChangeLog-5.php#5.6.30
https://secure.php.net/ChangeLog-7.php#7.0.15
https://secure.php.net/ChangeLog-7.php#7.1.1

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

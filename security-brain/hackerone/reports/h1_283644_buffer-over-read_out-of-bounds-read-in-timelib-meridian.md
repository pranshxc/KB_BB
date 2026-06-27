---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '283644'
original_report_id: '283644'
title: Out-Of-Bounds Read in timelib_meridian()
weakness: Buffer Over-read
team_handle: ibb
created_at: '2017-10-28T00:16:57.759Z'
disclosed_at: '2019-10-14T04:38:08.877Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- buffer-over-read
---

# Out-Of-Bounds Read in timelib_meridian()

## Metadata

- HackerOne Report ID: 283644
- Weakness: Buffer Over-read
- Program: ibb
- Disclosed At: 2019-10-14T04:38:08.877Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
While deserializing an invalid dateTime value, wddx_deserialize() would result in a heap out-of-bounds read in timelib_meridian(). As wddx_deserialize() is exposed to network data, and sometimes echo the results back to client, this issue could potentially allow remote peeking of the process memory. It should also affect other PHP APIs that make use of timelib_meridian().
This issue is similar to but is a separate issue of CVE-2017-11145, it is related to the "back of" and "front of" directives in the timelib format.

Details can be found at: https://bugs.php.net/bug.php?id=75055

Impact
Affects both PHP 5 before 5.6.32 (ChangeLog http://www.php.net/ChangeLog-5.php#5.6.32) and PHP 7 before 7.1.11 (ChangeLog http://www.php.net/ChangeLog-7.php#7.1.11).
Resolved PHP bug report, will update the pending CVE.

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

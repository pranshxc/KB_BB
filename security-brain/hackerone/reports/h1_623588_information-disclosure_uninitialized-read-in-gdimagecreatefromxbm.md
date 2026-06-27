---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '623588'
original_report_id: '623588'
title: Uninitialized read in gdImageCreateFromXbm
weakness: Information Disclosure
team_handle: ibb
created_at: '2019-06-21T02:53:16.633Z'
disclosed_at: '2020-10-10T02:16:30.335Z'
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

# Uninitialized read in gdImageCreateFromXbm

## Metadata

- HackerOne Report ID: 623588
- Weakness: Information Disclosure
- Program: ibb
- Disclosed At: 2020-10-10T02:16:30.335Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This bug is present in gdImageCreateFromXbm method of ext/gd/libgd/gd_xbm.c file.
This method contains below mentioned lines.
```c
...
unsigned int b;
...
sscanf(h, "%x", &b);
		for (bit = 1; bit <= max_bit; bit = bit << 1) {
			gdImageSetPixel(im, x++, y, (b & bit) ? 1 : 0);
...
```

So when sscanf method is not able to read a hex value, "b" variable will contain uninitialized data.
Bug Report : https://bugs.php.net/bug.php?id=77973
PHP Version : 7.1.29
CVE-ID : [2019-11038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11038)

## Impact

Uninitialized data may leak data from stack memory.

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

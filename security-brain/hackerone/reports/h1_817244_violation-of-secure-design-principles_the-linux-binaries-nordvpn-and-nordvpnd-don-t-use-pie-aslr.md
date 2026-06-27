---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '817244'
original_report_id: '817244'
title: The Linux binaries (nordvpn and nordvpnd) don't use PIE/ASLR
weakness: Violation of Secure Design Principles
team_handle: nordsecurity
created_at: '2020-03-12T00:38:19.028Z'
disclosed_at: '2020-04-22T11:29:59.782Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: NordVPN - Linux Executable
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# The Linux binaries (nordvpn and nordvpnd) don't use PIE/ASLR

## Metadata

- HackerOne Report ID: 817244
- Weakness: Violation of Secure Design Principles
- Program: nordsecurity
- Disclosed At: 2020-04-22T11:29:59.782Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:

The Linux binaries `nordvpn` and `nordvpnd` don't have PIE/ASLR enabled. A such feature is used to harden programs against the exploitation of memory corruption bugs and should be enabled.

The use of ASLR has long been debated among the Golang community. However, it seems that it's becoming the default choice now.

## Steps To Reproduce:

```
$ rabin2 -I /usr/bin/nordvpn | grep pic
pic      false
$ rabin2 -I /usr/sbin/nordvpnd | grep pic
pic      false
```

## Supporting Material/References:

  * https://insanitybit.github.io/2016/12/28/golang-and-rustlang-memory-safety
  * https://github.com/golang/go/issues/35192
  * https://fedoraproject.org/wiki/Changes/golang-buildmode-pie

## Impact

Any memory corruption bug (e.g. buffer overflow) can easily lead to a working exploit when ASLR is not enabled.

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

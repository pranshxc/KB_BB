---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '218567'
original_report_id: '218567'
title: SIGSEGV in array_copy - array.c:71
weakness: Memory Corruption - Generic
team_handle: shopify-scripts
created_at: '2017-04-04T16:56:10.017Z'
disclosed_at: '2017-04-13T22:44:41.115Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- memory-corruption-generic
---

# SIGSEGV in array_copy - array.c:71

## Metadata

- HackerOne Report ID: 218567
- Weakness: Memory Corruption - Generic
- Program: shopify-scripts
- Disclosed At: 2017-04-13T22:44:41.115Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

File [2] as input causes a segfault in mruby.

mruby crashes in ary_copy (array.c:71):
```
Program received signal SIGSEGV, Segmentation fault.
0x000000000040e088 in array_copy (src=<optimized out>, size=<optimized out>, dst=<optimized out>) at /tmp/mruby/src/array.c:71
71          dst[i] = src[i];
```

Test platform:
Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.39-1+deb8u1 x86_64 GNU/Linux

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

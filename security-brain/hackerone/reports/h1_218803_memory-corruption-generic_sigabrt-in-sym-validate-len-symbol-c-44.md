---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '218803'
original_report_id: '218803'
title: SIGABRT in sym_validate_len - symbol.c:44
weakness: Memory Corruption - Generic
team_handle: shopify-scripts
created_at: '2017-04-05T16:41:18.484Z'
disclosed_at: '2017-05-02T22:09:02.427Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- memory-corruption-generic
---

# SIGABRT in sym_validate_len - symbol.c:44

## Metadata

- HackerOne Report ID: 218803
- Weakness: Memory Corruption - Generic
- Program: shopify-scripts
- Disclosed At: 2017-05-02T22:09:02.427Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

File [2] as input causes a sigabrt in mruby.

mruby raise an exception in sym_validate_len (symbol.c:44)
```
#0  0x00000000005d3908 in raise ()
#1  0x00000000005d3b3a in abort ()
#2  0x0000000000415b52 in mrb_exc_raise (mrb=<optimized out>, exc=...) at /tmp/mruby/src/error.c:310
#3  0x0000000000415c81 in mrb_raise (mrb=0x94fc10, c=<optimized out>, msg=<optimized out>) at /tmp/mruby/src/error.c:318
#4  0x000000000041afdd in sym_validate_len (mrb=0x94fc10, len=65535) at /tmp/mruby/src/symbol.c:44
```

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

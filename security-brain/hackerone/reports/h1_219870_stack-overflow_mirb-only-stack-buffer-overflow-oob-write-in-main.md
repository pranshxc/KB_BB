---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '219870'
original_report_id: '219870'
title: 'mirb only: stack-buffer-overflow (OOB write) in main()'
weakness: Stack Overflow
team_handle: shopify-scripts
created_at: '2017-04-10T05:06:09.058Z'
disclosed_at: '2017-05-09T12:43:12.853Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- stack-overflow
---

# mirb only: stack-buffer-overflow (OOB write) in main()

## Metadata

- HackerOne Report ID: 219870
- Weakness: Stack Overflow
- Program: shopify-scripts
- Disclosed At: 2017-05-09T12:43:12.853Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Triggered in `7e28510` (7 April 2017) with `mirb` only.

`cat test013.rb | mirb`

```
==17976==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fffeb477fb0 at pc 0x408c21 bp 0x7fffeb477a90 sp 0x7fffeb477a88
WRITE of size 1 at 0x7fffeb477fb0 thread T0
    #0 0x408c20 in main /root/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:466
    #1 0x7f96e4703b44 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b44)
    #2 0x40aefc (/root/mruby/bin/mirb+0x40aefc)

Address 0x7fffeb477fb0 is located in stack of thread T0 at offset 1184 in frame
    #0 0x40549f in main /root/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:361

  This frame has 4 object(s):
    [32, 56) 'args'
    [96, 126) 'unexpected_end'
    [160, 1184) 'last_code_line' <== Memory access at offset 1184 overflows this variable
    [1216, 5312) 'ruby_code'
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /root/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:466 main
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

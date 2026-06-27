---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '221251'
original_report_id: '221251'
title: heap-buffer-overflow (read outside of buffer) in mrb_vm_exec()
weakness: Heap Overflow
team_handle: shopify-scripts
created_at: '2017-04-15T18:08:56.021Z'
disclosed_at: '2017-05-09T12:43:39.447Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- heap-overflow
---

# heap-buffer-overflow (read outside of buffer) in mrb_vm_exec()

## Metadata

- HackerOne Report ID: 221251
- Weakness: Heap Overflow
- Program: shopify-scripts
- Disclosed At: 2017-05-09T12:43:39.447Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Triggered in `3231219` (14 April 2017). Compiled with afl-gcc + asan.

`./mirb < test000`

```
==10555==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200001c920 at pc 0x52be2c bp 0x7ffe6751ada0 sp 0x7ffe6751ad98
READ of size 16 at 0x60200001c920 thread T0
    #0 0x52be2b in mrb_vm_exec /root/mruby/src/vm.c:1556
    #1 0x530a19 in mrb_vm_run /root/mruby/src/vm.c:829
    #2 0x53260f in mrb_run /root/mruby/src/vm.c:2644
    #3 0x53260f in ecall /root/mruby/src/vm.c:320
    #4 0x4fd59f in mrb_vm_exec /root/mruby/src/vm.c:1716
    #5 0x530a19 in mrb_vm_run /root/mruby/src/vm.c:829
    #6 0x53260f in mrb_run /root/mruby/src/vm.c:2644
    #7 0x53260f in ecall /root/mruby/src/vm.c:320
    #8 0x508b65 in mrb_vm_exec /root/mruby/src/vm.c:1170
    #9 0x530a19 in mrb_vm_run /root/mruby/src/vm.c:829
    #10 0x53260f in mrb_run /root/mruby/src/vm.c:2644
    #11 0x53260f in ecall /root/mruby/src/vm.c:320
    #12 0x508b65 in mrb_vm_exec /root/mruby/src/vm.c:1170
    #13 0x530a19 in mrb_vm_run /root/mruby/src/vm.c:829
    #14 0x40781f in main /root/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549
    #15 0x7f93c4ea5b44 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b44)
    #16 0x40a71c (/root/mruby/bin/mirb+0x40a71c)

0x60200001c920 is located 0 bytes to the right of 16-byte region [0x60200001c910,0x60200001c920)
allocated by thread T0 here:
    #0 0x7f93c55849f6 in __interceptor_realloc (/usr/lib/x86_64-linux-gnu/libasan.so.1+0x549f6)
    #1 0x421a2e in mrb_realloc_simple /root/mruby/src/gc.c:202
    #2 0x421a2e in mrb_realloc /root/mruby/src/gc.c:216
    #3 0x421a2e in mrb_malloc /root/mruby/src/gc.c:237

SUMMARY: AddressSanitizer: heap-buffer-overflow /root/mruby/src/vm.c:1556 mrb_vm_exec
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

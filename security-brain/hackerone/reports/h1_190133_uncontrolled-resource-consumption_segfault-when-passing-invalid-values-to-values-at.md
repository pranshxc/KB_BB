---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '190133'
original_report_id: '190133'
title: Segfault when passing invalid values to `values_at`
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-12-10T15:08:58.789Z'
disclosed_at: '2016-12-17T23:45:41.864Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Segfault when passing invalid values to `values_at`

## Metadata

- HackerOne Report ID: 190133
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2016-12-17T23:45:41.864Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Introduction
============

Passing primitive non-`Fixnum` values to the `values_at` method of `Struct` and `Range` leads to a segfault in both mruby and mruby-engine/parent Ruby process.

Proof of concept
================

list-crash.rb
-------------

    [].values_at true

struct-crash.rb
---------------

    Struct.new.new.values_at true

1. Save either of the above as `crash.rb`.
2. Run either:
   a) `mruby crash.rb`
   b) `sandbox crash.rb`
3. Both cause a segfault due to an invalid pointer dereference.

Discussion
==========

The crash is introduced in commit `79a621dd739faf4cc0958e11d6a887331cf79e48`.

The underlying cause is that the new `mrb_range_ptr` attempts to dereference a pointer derived from a `mrb_value` to check whether the `edges` member is `NULL` without ensuring that the `mrb_value` in question is a non-primitive (and therefore has a valid pointer value). In the case of the `values_at` methods, its arguments are passed to `mrb_get_values_at` which in turn passes it to `range_beg_len`. There it is passed to `mrb_range_ptr` before checking its type.

Solution
========

To fix the crash, the type of the value passed to `range_beg_len` should be checked before calling `mrb_range_ptr`. We've also looked through the codebase for other problematic instances, but found none.

    diff --git a/src/range.c b/src/range.c
    index 4179574..73fe758 100644
    --- a/src/range.c
    +++ b/src/range.c
    @@ -252,9 +252,10 @@ static mrb_bool
    range_beg_len(mrb_state *mrb, mrb_value range, mrb_int *begp, mrb_int *lenp, mrb_int len, mrb_bool trunc)
    {
    mrb_int beg, end;
    -  struct RRange *r = mrb_range_ptr(mrb, range);
    +  struct RRange *r;
    
    if (mrb_type(range) != MRB_TT_RANGE) return FALSE;
    +  r = mrb_range_ptr(mrb, range);
    
    beg = mrb_int(mrb, r->edges->beg);
    end = mrb_int(mrb, r->edges->end);



--
Denis Kasak
Damir Jelić

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181685'
original_report_id: '181685'
title: Range#initialize_copy null pointer dereference
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-11-12T01:19:47.017Z'
disclosed_at: '2016-12-17T01:03:44.537Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Range#initialize_copy null pointer dereference

## Metadata

- HackerOne Report ID: 181685
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2016-12-17T01:03:44.537Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Heya!

It's possible to segfault mruby through mruby-engine with the following snippet of code:

    Range.remove_method(:initialize_copy)
    (1..2).dup.to_s

This can be triggered through mruby-engine like this:

    MRubyEngine.new(512*1024, 1000, 1000).sandbox_eval("/tmp", %{
      Range.remove_method(:initialize_copy)
      (1..2).dup.to_s
    })

The `dup` and `clone` methods allocate a new object and then call `initialize_copy` on the new object with the old object as an argument to copy over internal state.

Removing `Range#initialize_copy` makes it possible to construct an uninitialized `Range` object. Calling (pretty much) any instance method on the uninitialized `Range` object afterwards causes mruby to dereference a null pointer, leading to a segfault.

I've attached a patch that fixes the bug by copying internal range state before calling `initialize_copy`, similar to what mruby already does for classes and modules.

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

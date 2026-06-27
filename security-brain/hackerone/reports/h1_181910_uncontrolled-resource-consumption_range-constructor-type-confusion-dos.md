---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181910'
original_report_id: '181910'
title: Range constructor type confusion DoS
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-11-13T12:41:55.264Z'
disclosed_at: '2016-12-17T01:03:07.728Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Range constructor type confusion DoS

## Metadata

- HackerOne Report ID: 181910
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2016-12-17T01:03:07.728Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It's possible to crash mruby by redefining the `Range` class and then using the range literal syntax:

    Range = Array
    (1..2).inspect

The `mrb_range_new` function allocates and initializes a range object backed by the `RRange` struct, however it uses runtime constant lookup to find the `Range` class object. Redefining the `Range` constant to point to a different class and calling an instance method causes a segfault, as the `RRange::edges` field is confused for the `iv` field on other structs.

It may be possible to achieve RCE through this vulnerability, but there are significant complicating factors and I have not spent the time trying to develop an RCE PoC.

I have attached a patch which fixes this bug. My patch adds a `range_class` field to `mrb_state`, following the pattern other core classes use to avoid runtime constant lookups.

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

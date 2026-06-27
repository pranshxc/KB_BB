---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '182274'
original_report_id: '182274'
title: Null pointer dereference due to TOCTTOU bug in mrb_time_initialize
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-11-15T13:01:54.580Z'
disclosed_at: '2017-01-15T19:56:05.964Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Null pointer dereference due to TOCTTOU bug in mrb_time_initialize

## Metadata

- HackerOne Report ID: 182274
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-01-15T19:56:05.964Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

mrb_time_initialize sets the data pointer to NULL before parsing function arguments. Parsing function arguments can call out to ruby code to call methods to do type coercion. If the type coercion method tries to access the time object it will dereference a NULL pointer.

The following snippet results in a native crash under mruby-engine:
```
$x = Time.new
class Tmp
    def to_i
        $x.mday
    end
end
$x.initialize Tmp.new
```

Attached is a patch to mruby to fix this issue.

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

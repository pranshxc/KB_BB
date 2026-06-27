---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '185041'
original_report_id: '185041'
title: Type confusion in mrb_exc_set leading to memory corruption
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-11-25T09:46:06.737Z'
disclosed_at: '2016-12-16T20:26:40.161Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Type confusion in mrb_exc_set leading to memory corruption

## Metadata

- HackerOne Report ID: 185041
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2016-12-16T20:26:40.161Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Similar to #181871, but the bug is more general. The E_*_ERROR macros are not constants, so the exception types can be redefined to not be exceptions:

    #define E_NOTIMP_ERROR              (mrb_class_get(mrb, "NotImplementedError"))

This means that any code calling mrb_raise on an exception macro can instead get a non-exception object, leading to memory corruption and arbitrary code execution. This snippet causes a native crash in mruby-engine:

    NotImplementedError = String
    Module.constants # mrb_raise(mrb, E_NOTIMP_ERROR, "Module.constants not implemented");

This should be fixed by making mrb_exc_set check that it is an exception type. Attached is a patch to mruby to fix this problem.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '183405'
original_report_id: '183405'
title: Null target_class DoS
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-11-19T02:41:38.411Z'
disclosed_at: '2016-12-17T01:02:59.955Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Null target_class DoS

## Metadata

- HackerOne Report ID: 183405
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2016-12-17T01:02:59.955Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The `Object#instance_exec` method in `mrbgems/mruby-object-ext/src/object.c` executes a block in the context of an object. It sets the VM's `target_class` pointer to the singleton class of this object. `target_class` is used as the definition target for constants and methods.

If a singleton class cannot be created for an object, `target_class` is set to `NULL`. The `OP_CLASS` and `OP_MODULE` opcodes in the VM assume `target_class` is not null when defining new classes and modules.

This causes a null pointer dereference and segfaults the mruby VM.

Sample code:

```
1.instance_exec { class X; end }
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

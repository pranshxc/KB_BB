---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '215854'
original_report_id: '215854'
title: Garbage collector crash
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2017-03-24T14:38:27.607Z'
disclosed_at: '2017-04-15T14:45:02.271Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Garbage collector crash

## Metadata

- HackerOne Report ID: 215854
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-04-15T14:45:02.271Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This github [issue](https://github.com/mruby/mruby/issues/3063] seems to have been reintroduced.

    f = Fiber.new do
        m = Fiber.current
        Fiber.yield Proc.new {}
    end

    f = f.resume
    GC.start
    
It causes mruby to abort due to a failed assertion.    
    
    $ mruby poc
    mruby: /home/user/repos/mruby/src/gc.c:698: mrb_gc_mark: Assertion `(obj)->tt != MRB_TT_FREE' failed.
    Aborted

The issue was reintroduced in ecee8c51b0ad8cddd9e422a3e5105f902d7e2781 and is still present in 051e40c0493f2de332f5439e3230c9fe6958bf1a.

The issue is fixed by reverting ecee8c51b0ad8cddd9e422a3e5105f902d7e2781.

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

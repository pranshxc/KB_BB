---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '185387'
original_report_id: '185387'
title: Null pointer dereference regression in parse.y
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-11-26T05:04:27.125Z'
disclosed_at: '2016-12-17T20:09:00.506Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Null pointer dereference regression in parse.y

## Metadata

- HackerOne Report ID: 185387
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2016-12-17T20:09:00.506Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Just pulled the latest mruby code, and found that some of my fuzzing test cases now crash. Bisected it to commit `227daa881137d5251e03eea0883b9b574a1f064e`. Reverting this change no longer causes a crash.

The minimised file causing the crash is:

```
f ()
```

Also affects mruby-engine.

Cheers,

Hugh

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

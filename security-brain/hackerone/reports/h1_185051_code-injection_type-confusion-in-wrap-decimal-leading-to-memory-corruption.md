---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '185051'
original_report_id: '185051'
title: Type confusion in wrap_decimal leading to memory corruption
weakness: Code Injection
team_handle: shopify-scripts
created_at: '2016-11-25T10:04:55.525Z'
disclosed_at: '2017-01-15T20:03:46.620Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
tags:
- hackerone
- code-injection
---

# Type confusion in wrap_decimal leading to memory corruption

## Metadata

- HackerOne Report ID: 185051
- Weakness: Code Injection
- Program: shopify-scripts
- Disclosed At: 2017-01-15T20:03:46.620Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Decimal can be redefined, causing the Decimal class lookup in wrap_decimal to be invalid. This can lead to memory corruption or arbitrary code execution.

The following snippet results in a native crash in mruby-engine
    olddecimal = Decimal.new(1)
    Decimal = Hash
    a = -olddecimal
    puts a

I suspect you caught this along with charliesome's similar bug for Struct. If not I'll follow up with a patch and an RCE exploit.

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

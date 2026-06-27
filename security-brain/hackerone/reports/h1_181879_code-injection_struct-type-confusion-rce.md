---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181879'
original_report_id: '181879'
title: Struct type confusion RCE
weakness: Code Injection
team_handle: shopify-scripts
created_at: '2016-11-13T07:21:17.397Z'
disclosed_at: '2016-12-17T01:03:22.530Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- code-injection
---

# Struct type confusion RCE

## Metadata

- HackerOne Report ID: 181879
- Weakness: Code Injection
- Program: shopify-scripts
- Disclosed At: 2016-12-17T01:03:22.530Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Heya!

I've been poking at mruby a bit more and I've found a vulnerability that allows an attacker to take control of the instruction pointer.

I've attached a proof of concept script that when run in mruby will jump to `0x0000133713371337` and segfault.

While the proof of concept script just jumps to an attacker controlled address and crashes, it would almost certainly be possible to achieve full remote code execution, especially given an arbitrary read/write primitive (which is easily created using the same techniques as in the proof of concept)

The proof of concept script has detailed annotations throughout about how it works, but I'm also happy to clarify anything if need be :)

Cheers,

███████

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

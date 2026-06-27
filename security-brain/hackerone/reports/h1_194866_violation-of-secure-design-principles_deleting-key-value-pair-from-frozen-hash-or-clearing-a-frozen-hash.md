---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '194866'
original_report_id: '194866'
title: Deleting Key-value pair from Frozen HASH or Clearing a Frozen HASH
weakness: Violation of Secure Design Principles
team_handle: shopify-scripts
created_at: '2016-12-30T19:24:05.402Z'
disclosed_at: '2017-01-05T16:49:46.236Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- violation-of-secure-design-principles
---

# Deleting Key-value pair from Frozen HASH or Clearing a Frozen HASH

## Metadata

- HackerOne Report ID: 194866
- Weakness: Violation of Secure Design Principles
- Program: shopify-scripts
- Disclosed At: 2017-01-05T16:49:46.236Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey!

while reviewing mruby for vulnerabilities, I stumble onto a snippet that allow an attacker to delete "key-value Pair" from a "Frozen" Hash or to clear the "Frozen" HASH.

Reproduction Step
=============
1.) Create a __Hash__ like  h = { "a" => 100, "b" => 200 }
2.) __Freeze__ this hash
3.) Now call ___delete___ method with __"KEY"__ (the case if you don't know the KEY then you can call ___.keys___ method to obtaine all available KEYS in the HASH) ( or call ___.clear___ method to clear the HASH )

POC
===

h = { "a" => 100, "b" => 200 }
h.freeze
h.delete("a")
@output = h

Look at ___h___ you will get remaining values after deletion even if the HASH has been frozen. ( in case of ___h.clear___ you will get empty HASH ).

Explanation
========

Bug is happened because there is no method calling to check weather the HASH is frozen or not in both methods  *mrb_hash_delete*   [hash.c#552](https://github.com/mruby/mruby/blob/master/src/hash.c#L552)  and  *mrb_hash_clear*  [hash.c#619](https://github.com/mruby/mruby/blob/master/src/hash.c#L619)  in https://github.com/mruby/mruby/blob/master/src/hash.c


This bug may come handy to delete details to cause data corruption.

Fix
==
Just apply   mrb_hash_modify(mrb, self);  &  mrb_hash_modify(mrb, hash);   on line  [555](https://github.com/mruby/mruby/blob/master/src/hash.c#L555)  and  on line  [622](https://github.com/mruby/mruby/blob/master/src/hash.c#L622) respectively.

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

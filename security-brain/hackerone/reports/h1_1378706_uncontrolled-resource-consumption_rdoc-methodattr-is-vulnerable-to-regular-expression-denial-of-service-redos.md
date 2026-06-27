---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1378706'
original_report_id: '1378706'
title: RDoc::MethodAttr is vulnerable to Regular Expression Denial of Service (ReDoS)
weakness: Uncontrolled Resource Consumption
team_handle: ruby
created_at: '2021-10-22T16:05:30.113Z'
disclosed_at: '2023-07-18T09:19:26.247Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# RDoc::MethodAttr is vulnerable to Regular Expression Denial of Service (ReDoS)

## Metadata

- HackerOne Report ID: 1378706
- Weakness: Uncontrolled Resource Consumption
- Program: ruby
- Disclosed At: 2023-07-18T09:19:26.247Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The method `block_params` in class `RDoc::MethodAttr` uses a regular expression that is vulnerable to Denial of Service due to catastrophic backtracking.

The regular expression is:
```
([A-Z:a-z0-9_]+)\.([a-z0-9_]+)(\s*\(\s*[a-z0-9_.,\s]*\s*\)\s*)?
```
Source: https://github.com/ruby/ruby/blob/master/lib/rdoc/method_attr.rb#L265

The ReDoS requence is: `(\s*\(\s*[a-z0-9_.,\s]*\s*\)\s*)`. It contains three overlapping repeating groups (repeated characters are 0x20, 0xa0, [09-0d]), so the worst-case complexity is cubic as there are 3 infinitely repeating groups. Cubic complexity here means that if the vulnerable part of the string is doubled in length, the execution time should be about 8 times longer (2^3).

# PoC

I have not found a way to exploit this vulnerability directly from the file documentation (by running rdoc), however directly it is very easy:

```ruby
use 'rdoc'
RDoc::MethodAttr.new(nil, nil).block_params = '0.0(' + ' '*3456 + '0'
```

The client's code that relies on `AnyMethod` is also vulnerable since it inherits `MethodAttr`:

```ruby
use 'rdoc'
RDoc::AnyMethod.new(nil, nil).block_params = '0.0(' + ' '*3456 + '0'
```

If an attacker  provides a malicious string to `AnyMethod|MethodAttr`'s `block_params` documentation parser, it will get stuck processing the input for an extremely long time, consuming 100% CPU.

## Impact

An attacker could cause an effective denial of service, by crafting an input which exploits catastrophic backtracking for the regular expression.

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

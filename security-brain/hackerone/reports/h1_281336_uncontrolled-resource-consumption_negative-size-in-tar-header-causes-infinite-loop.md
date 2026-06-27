---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '281336'
original_report_id: '281336'
title: Negative size in tar header causes infinite loop
weakness: Uncontrolled Resource Consumption
team_handle: rubygems
created_at: '2017-10-21T03:56:09.259Z'
disclosed_at: '2018-03-01T05:47:32.276Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://github.com/rubygems/rubygems
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Negative size in tar header causes infinite loop

## Metadata

- HackerOne Report ID: 281336
- Weakness: Uncontrolled Resource Consumption
- Program: rubygems
- Disclosed At: 2018-03-01T05:47:32.276Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Proof of concept

The attached file loop.gem causes an infinite loop in any command that tries to iterate over the entries in the tar container.
```
gem install loop.gem
gem unpack loop.gem
gem specification loop.gem
```

# Summary

[`Gem::Package::TarHeader.from`](https://github.com/rubygems/rubygems/blob/v2.6.14/lib/rubygems/package/tar_header.rb#L97-L124) uses [`oct`](https://ruby-doc.org/core-2.4.2/String.html#method-i-oct) to parse fields in the tar header. `oct` does more than just parse octal digits, for example it permits these unexpected syntaxes:
- sign characters:
  - `"+012345".oct # 5349`
  - `"-012345".oct # -5349`
- radix prefixes:
  - `"0x12abc".oct # 76476`
  - `"0b10000".oct # 16`
- silently ignoring errors:
  - `"123,456".oct # 83`
  - `"nothing".oct # 0`

The ability to encode negative values enables a DoS (infinite loop) in the tar reader. The proof-of-concept loop.gem has a size field of `-0000001000\x00`, or −512. The negative size causes [`Gem::Package::TarReader.each`](https://github.com/rubygems/rubygems/blob/v2.6.14/lib/rubygems/package/tar_reader.rb#L52) to seek *backwards* after reading the header, so it reads the same header over and over.

I suppose one could cause a lot of CPU usage on the rubygems.org server by uploading copies of loop.gem, but I didn't try it.

# Remediation

Instead of doing the conversion using `oct`, there could be a special-purpose function that validates its input better. It might be enough to check that the string matches `/\A[0-7]+\z/` before calling `oct`.

The attached patch file adds a test that `Gem::Package::TarHeader.from` rejects various bogus syntax.

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

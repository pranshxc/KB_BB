---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '192127'
original_report_id: '192127'
title: Buffer underflow in sprintf
weakness: Memory Corruption - Generic
team_handle: ruby
created_at: '2016-12-18T05:30:43.743Z'
disclosed_at: '2017-03-05T04:12:40.333Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- memory-corruption-generic
---

# Buffer underflow in sprintf

## Metadata

- HackerOne Report ID: 192127
- Weakness: Memory Corruption - Generic
- Program: ruby
- Disclosed At: 2017-03-05T04:12:40.333Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

So I found this in mruby as part of the shopify-scripts program, and I notice that my patch also landed upstream in ruby as well. Shame on me for not checking ruby as well!

Wondered if it counted for a bounty here as well?

https://github.com/mruby/mruby/issues/3347 <- issue that shopify guys opened on my behalf.
https://github.com/ruby/ruby/commit/0854193a684acc2b3a13ab28091a4397000c8822 <- commit landed upstream.

https://hackerone.com/reports/191328 (still open so not public) is the original report of mine.

Let me know if you need anything more.

Cheers,

Hugh

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '66724'
original_report_id: '66724'
title: type confusion in Sass::ParserState::ParserState(Sass::ParserState const&)
weakness: Memory Corruption - Generic
team_handle: libsass
created_at: '2015-06-09T01:40:57.151Z'
disclosed_at: '2015-06-11T18:57:44.532Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- memory-corruption-generic
---

# type confusion in Sass::ParserState::ParserState(Sass::ParserState const&)

## Metadata

- HackerOne Report ID: 66724
- Weakness: Memory Corruption - Generic
- Program: libsass
- Disclosed At: 2015-06-11T18:57:44.532Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I haven't actually spent much time on the bug, because it doesn't look super exploitable outside of a local DoS, but the attached PoC will crash sassc in the middle of libsass from latest git, trying to deref $0x8, which appears to be the value of some tag in a tagged union.

Let me know if I can help chasing this down, but I mostly wanted to just punt it over the fence.

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

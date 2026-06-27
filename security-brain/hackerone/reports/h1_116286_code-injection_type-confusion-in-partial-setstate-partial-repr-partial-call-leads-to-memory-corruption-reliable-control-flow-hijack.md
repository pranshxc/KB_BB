---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116286'
original_report_id: '116286'
title: Type confusion in partial.setstate, partial_repr, partial_call leads to memory
  corruption, reliable control flow hijack
weakness: Code Injection
team_handle: ibb
created_at: '2016-02-13T19:23:44.612Z'
disclosed_at: '2016-09-20T04:01:06.202Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: Python (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- code-injection
---

# Type confusion in partial.setstate, partial_repr, partial_call leads to memory corruption, reliable control flow hijack

## Metadata

- HackerOne Report ID: 116286
- Weakness: Code Injection
- Program: ibb
- Disclosed At: 2016-09-20T04:01:06.202Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

See my official writeups here:

http://bugs.python.org/issue25944
http://bugs.python.org/issue25945

The maintainers merged these bug reports.
In one case, the type confusion leads to a reliable control of the instruction pointer as calling `repr` on a corrupted partial calls a function pointer that is controlled reliably by the user. I've uploaded that case here as well.

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

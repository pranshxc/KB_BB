---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '274998'
original_report_id: '274998'
title: Use of unitialized value in token_check_object (src/or/parsecommon.c:224)
weakness: Memory Corruption - Generic
team_handle: torproject
created_at: '2017-10-11T04:53:58.839Z'
disclosed_at: '2019-10-04T16:25:57.684Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 3
tags:
- hackerone
- memory-corruption-generic
---

# Use of unitialized value in token_check_object (src/or/parsecommon.c:224)

## Metadata

- HackerOne Report ID: 274998
- Weakness: Memory Corruption - Generic
- Program: torproject
- Disclosed At: 2019-10-04T16:25:57.684Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Triggered in `22139c0`, compiled with `-fsanitize=memory` and clang 6.0.0-trunk.

`./fuzz-consensus < test00d68`

```
=9591==WARNING: MemorySanitizer: use-of-uninitialized-value
    #0 0x55ca86e51348 in token_check_object /root/tor/src/or/parsecommon.c:224:13
    #1 0x55ca86e51348 in get_next_token /root/tor/src/or/parsecommon.c:397
    #2 0x55ca86e3ff83 in tokenize_string /root/tor/src/or/parsecommon.c:72:11
    #3 0x55ca8711139a in networkstatus_parse_vote_from_string /root/tor/src/or/routerparse.c:3417:7
    #4 0x55ca8676fbd1 in fuzz_main /root/tor/src/test/fuzz/fuzz_consensus.c:66:8
    #5 0x55ca8676f29d in main /root/tor/src/test/fuzz/fuzzing_common.c:179:3
    #6 0x7f32a84f2b44 in __libc_start_main /build/glibc-6V9RKT/glibc-2.19/csu/libc-start.c:287
    #7 0x55ca866fc8ce in _start (/root/tor/src/test/fuzz/fuzz-consensus+0x3bc8ce)

SUMMARY: MemorySanitizer: use-of-uninitialized-value /root/tor/src/or/parsecommon.c:224:13 in token_check_object
```

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115702'
original_report_id: '115702'
title: '[tor] libevent dns OOB read'
weakness: Memory Corruption - Generic
team_handle: torproject
created_at: '2016-02-10T14:43:24.014Z'
disclosed_at: '2017-10-19T10:15:46.793Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- memory-corruption-generic
---

# [tor] libevent dns OOB read

## Metadata

- HackerOne Report ID: 115702
- Weakness: Memory Corruption - Generic
- Program: torproject
- Disclosed At: 2017-10-19T10:15:46.793Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The DNS code of Libevent contains this rather obvious OOB read:

```c
3122 static char *
3123 search_make_new(const struct search_state *const state, int n, const char *const base_name) {
3124     const size_t base_len = strlen(base_name);
3125     const char need_to_append_dot = base_name[base_len - 1] == '.' ? 0 : 1;
```

If the length of ```base_name``` is 0, then line 3125 reads 1 byte before the buffer. This will trigger a crash on ASAN-protected builds.

To reproduce:

Build libevent with ASAN:
```
$ CFLAGS='-fomit-frame-pointer -fsanitize=address' ./configure && make -j4
```
Put the attached ```resolv.conf``` and ```poc.c``` in the source directory and then do:

```
$ gcc -fsanitize=address -fomit-frame-pointer poc.c .libs/libevent.a
$ ./a.out
=================================================================
==22201== ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60060000efdf at pc 0x4429da bp 0x7ffe1ed47300 sp 0x7ffe1ed472f8
READ of size 1 at 0x60060000efdf thread T0
```

This happens because I create a zero-length string in ```poc.c```:
```c
    char* hostname = malloc(32);
    memset(hostname, 0, 32);
    //hostname[0] = 'x';
```

If you uncomment the last line, it will not crash.

Guido

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

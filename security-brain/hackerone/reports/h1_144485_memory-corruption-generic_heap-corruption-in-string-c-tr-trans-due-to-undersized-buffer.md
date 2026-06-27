---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '144485'
original_report_id: '144485'
title: Heap corruption in string.c tr_trans() due to undersized buffer
weakness: Memory Corruption - Generic
team_handle: ruby
created_at: '2016-06-13T14:41:34.582Z'
disclosed_at: '2016-06-21T00:57:04.703Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- memory-corruption-generic
---

# Heap corruption in string.c tr_trans() due to undersized buffer

## Metadata

- HackerOne Report ID: 144485
- Weakness: Memory Corruption - Generic
- Program: ruby
- Disclosed At: 2016-06-21T00:57:04.703Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

(originally send by e-mail on 6 Jun 2016)

Configure with ASAN AddressSanitizer:

```
mkdir install; CFLAGS="-fsanitize=address" ./configure
--disable-install-doc --disable-install-rdoc --disable-install-capi
-prefix=`realpath ./install` && make -j4 && make install
```

Then execute:

```
$ ./ruby -e '"a".encode("utf-32").tr("b".encode("utf-32"),
"c".encode("utf-32"))'
=================================================================
==17122==ERROR: AddressSanitizer: heap-buffer-overflow on address
0x602000014a98 at pc 0x7ff04065cf01 bp 0x7ffdfe7629b0 sp 0x7ffdfe7629a8
WRITE of size 4 at 0x602000014a98 thread T0
...
...
```

The actual corruption occurs here:

```c
6196     TERM_FILL(t, rb_enc_mbminlen(enc));
```

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

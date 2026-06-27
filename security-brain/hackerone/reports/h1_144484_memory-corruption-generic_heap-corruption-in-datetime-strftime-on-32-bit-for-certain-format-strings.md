---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '144484'
original_report_id: '144484'
title: Heap corruption in DateTime.strftime() on 32 bit for certain format strings
weakness: Memory Corruption - Generic
team_handle: ruby
created_at: '2016-06-13T14:40:11.745Z'
disclosed_at: '2016-06-21T00:56:51.607Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- memory-corruption-generic
---

# Heap corruption in DateTime.strftime() on 32 bit for certain format strings

## Metadata

- HackerOne Report ID: 144484
- Weakness: Memory Corruption - Generic
- Program: ruby
- Disclosed At: 2016-06-21T00:56:51.607Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

(originally send by e-mail on 4 Jun 2016)

Setting a very high precision in the date_strftime_with_tmx() function,
the following check (in the STRFTIME macro in date_strftime.c) will not
work as expected if 's' >= 0x80000000 (this is the same type of issue as
the other vulnerability I submitted).

```c
124         if (start + maxsize < s + precision) {          \
125             errno = ERANGE;                 \
126             return 0;                       \
127         }
```

This code causes a crash on my 32 bit system:

```ruby
require 'date'
d =  DateTime.new(2007,11,19,8,37,48,"-06:00")
d.strftime("%2147483647c")
```

64 bit is probably not affected (strictly technically possible, but
unlikely).

Let me know if you need more information.

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
